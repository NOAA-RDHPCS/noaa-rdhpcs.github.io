#!/usr/bin/env python3
"""Analyze Sphinx linkcheck output against PR changes to categorize broken links.

Reads build/linkcheck/output.json and cross-references it with the files and
lines modified in the current PR (via git diff against the base branch) to
produce one of three categories for each broken link:

  new
    The broken URL appears in a file modified by the PR *and* on a line that
    was added or changed in the PR.  The workflow fails and a PR comment is
    posted.

  preexisting_modified
    The broken URL appears in a file the PR touched, but the URL itself was
    not on an added or changed line.  A warning comment is posted; the
    workflow does not fail.

  preexisting_unrelated
    The broken URL appears in a file the PR did not touch.  These are silently
    ignored — the weekly scheduled link check handles them.

Only HTTP 4xx responses are treated as definitively broken.  Timeouts and
connection errors are CI noise and are skipped.

A markdown comment body is written to comment_body.md when there are any
"new" or "preexisting_modified" broken links.  No file is written (and no
comment is posted) when all links are clean or only unrelated pre-existing
links are found.

Exit codes:
  0 - no new broken links (workflow passes)
  1 - one or more new broken links introduced by this PR (workflow fails)
  2 - output.json missing or unreadable (do not block the PR)
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

OUTPUT_JSON = Path("build/linkcheck/output.json")
SOURCE_DIR = "source"
COMMENT_FILE = Path("comment_body.md")

# RST URL patterns — same set as check_ignored_links.py
RE_INLINE = re.compile(r"`[^`<]*<(https?://[^>]+)>`__?")
RE_TARGET = re.compile(r"^\s*\.\.\s+_`?[^`:]+`?:\s+(https?://\S+)", re.MULTILINE)
RE_BARE = re.compile(r"(?<![`<])(https?://[^\s`<>\"')\]\\]+)")


def get_broken_links() -> list[dict]:
    """Parse output.json and return entries with HTTP 4xx status only."""
    if not OUTPUT_JSON.exists():
        print(f"WARNING: {OUTPUT_JSON} not found — skipping analysis.", file=sys.stderr)
        sys.exit(2)

    broken = []
    with OUTPUT_JSON.open() as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            if entry.get("status") == "broken" and 400 <= entry.get("code", 0) < 500:
                filename = entry.get("filename")
                if not filename or not entry.get("uri"):
                    print(f"WARNING: skipping malformed entry: {entry}", file=sys.stderr)
                    continue
                # Normalize filename (relative to source/) to repo-root-relative path
                entry["filepath"] = f"{SOURCE_DIR}/{filename}"
                broken.append(entry)
    return broken


def get_modified_rst_files(base_ref: str) -> set[str]:
    """Return repo-root-relative paths of RST files modified in the PR."""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", f"origin/{base_ref}...HEAD", "--", "*.rst"],
            capture_output=True, text=True, check=True,
        )
    except subprocess.CalledProcessError as exc:
        print(f"WARNING: git diff failed: {exc.stderr.strip()}", file=sys.stderr)
        sys.exit(2)
    return {line.strip() for line in result.stdout.splitlines() if line.strip()}


def get_added_urls(base_ref: str, rst_files: set[str]) -> set[str]:
    """Return URLs that appear on added/changed lines in the PR diff."""
    if not rst_files:
        return set()

    try:
        result = subprocess.run(
            ["git", "diff", f"origin/{base_ref}...HEAD", "--"] + sorted(rst_files),
            capture_output=True, text=True, check=True,
        )
    except subprocess.CalledProcessError as exc:
        print(f"WARNING: git diff failed: {exc.stderr.strip()}", file=sys.stderr)
        sys.exit(2)

    urls: set[str] = set()
    for line in result.stdout.splitlines():
        if not line.startswith("+") or line.startswith("+++"):
            continue
        content = line[1:]
        for m in RE_INLINE.finditer(content):
            urls.add(re.sub(r"[.,;:]+$", "", m.group(1).strip()))
        for m in RE_TARGET.finditer(content):
            urls.add(re.sub(r"[.,;:]+$", "", m.group(1).strip()))
        for m in RE_BARE.finditer(content):
            urls.add(re.sub(r"[.,;:]+$", "", m.group(1)))
    return urls


def format_table(entries: list[dict]) -> str:
    """Format broken link entries as a Markdown table."""
    rows = [
        "| File | Line | URL | Status |",
        "|------|------|-----|--------|",
    ]
    for e in entries:
        code = e.get("code", "")
        info = e.get("info", "").split("\n")[0]  # first line only
        status = f"{code} — {info}".strip(" —") if code else info
        filepath = e.get("filepath", "unknown")
        lineno = e.get("lineno", "?")
        uri = e.get("uri", "")
        rows.append(f"| `{filepath}` | {lineno} | {uri} | {status} |")
    return "\n".join(rows)


def main() -> int:
    base_ref = os.environ.get("BASE_REF", "main")

    broken = get_broken_links()
    if not broken:
        return 0

    modified_files = get_modified_rst_files(base_ref)
    added_urls = get_added_urls(base_ref, modified_files)

    new_broken: list[dict] = []
    preexisting_modified: list[dict] = []

    for entry in broken:
        if entry["filepath"] in modified_files:
            if entry["uri"] in added_urls:
                new_broken.append(entry)
            else:
                preexisting_modified.append(entry)
        # preexisting_unrelated: silently skip

    if not new_broken and not preexisting_modified:
        return 0

    # Build PR comment
    sections = ["<!-- linkcheck-pr-comment -->\n## 🔗 Link Check Results\n"]

    if new_broken:
        sections.append("### ❌ New broken links introduced by this PR\n")
        sections.append(
            "These links were added or changed in this PR and are unreachable. "
            "Please fix them before merging.\n"
        )
        sections.append(format_table(new_broken))
        sections.append("")

    if preexisting_modified:
        if new_broken:
            sections.append("---\n")
        sections.append("### ⚠️ Pre-existing broken links in files you modified\n")
        sections.append(
            "These were already broken before your PR — no action needed from you. "
            "They will be tracked by the weekly link check.\n"
        )
        sections.append(format_table(preexisting_modified))
        sections.append("")

    COMMENT_FILE.write_text("\n".join(sections))
    return 1 if new_broken else 0


if __name__ == "__main__":
    sys.exit(main())
