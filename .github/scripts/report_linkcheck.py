#!/usr/bin/env python3
"""Report broken links from Sphinx linkcheck output for the scheduled workflow.

Reads build/linkcheck/output.json and prints a Markdown-formatted issue body
listing all broken links (HTTP 4xx only).  Timeouts and connection errors are
CI noise and are excluded.

Supports deduplication against known broken URLs from open issues.  When a
--known-urls-file is provided, broken links already tracked in open issues are
marked with "Related to #NNN" in the status column instead of the HTTP error.

Exit codes:
  0 - no broken links found
  1 - at least one NEW broken link found (create issue)
  2 - output.json missing or unreadable
  3 - broken links found but ALL are already known (skip issue creation)
"""

import argparse
import json
import re
import sys
from pathlib import Path

OUTPUT_JSON = Path("build/linkcheck/output.json")
SOURCE_DIR = "source"

# Sphinx 9.x writes code=0 for all broken entries; the actual HTTP status
# is only in the info field (e.g. "404 Client Error: Not Found for url: ...").
# This pattern matches that prefix so we can detect 4xx responses either way.
RE_4XX_INFO = re.compile(r"^4\d\d\b")


def _is_broken_4xx(entry: dict) -> bool:
    """Return True if the entry represents an HTTP 4xx broken link."""
    code = entry.get("code", 0)
    if 400 <= code < 500:
        return True
    # Fallback for Sphinx versions that always write code=0
    if code == 0 and entry.get("status") == "broken":
        return bool(RE_4XX_INFO.match(entry.get("info", "")))
    return False


def _load_known_urls(path: Path | None) -> dict[str, int]:
    """Load known URLs from a JSON file mapping URL to issue number."""
    if path is None or not path.exists():
        return {}
    try:
        with path.open() as fh:
            data = json.load(fh)
            # Ensure values are integers
            return {url: int(num) for url, num in data.items()}
    except (json.JSONDecodeError, ValueError):
        return {}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Report broken links from Sphinx linkcheck output."
    )
    parser.add_argument(
        "--known-urls-file",
        type=Path,
        default=None,
        help="JSON file mapping known broken URLs to issue numbers",
    )
    args = parser.parse_args()

    if not OUTPUT_JSON.exists():
        print(f"ERROR: {OUTPUT_JSON} not found.", file=sys.stderr)
        return 2

    known_urls = _load_known_urls(args.known_urls_file)

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
            if _is_broken_4xx(entry):
                broken.append(entry)

    if not broken:
        print("All links are OK.")
        return 0

    # Categorize broken links as new or known
    new_broken = []
    known_broken = []
    for entry in broken:
        uri = entry.get("uri", "")
        if uri in known_urls:
            entry["_known_issue"] = known_urls[uri]
            known_broken.append(entry)
        else:
            new_broken.append(entry)

    # If all broken links are already known, skip issue creation
    if not new_broken:
        print(
            f"All {len(known_broken)} broken link(s) are already tracked in open issues."
        )
        return 3

    # Generate issue body
    total = len(broken)
    new_count = len(new_broken)
    print(
        f"The weekly link check found {total} broken link(s) "
        f"({new_count} new, {len(known_broken)} already tracked).\n\n"
        "These links return HTTP 4xx responses and should be updated or removed.\n"
    )
    print("## Broken Links\n")
    print("| File | Line | URL | Status |")
    print("|------|------|-----|--------|")

    # Print new broken links first, then known ones
    for e in new_broken:
        filepath = f"{SOURCE_DIR}/{e.get('filename', 'unknown')}"
        code = e.get("code", "")
        info = e.get("info", "").split("\n")[0]
        status = f"{code} — {info}".strip(" —") if code else info
        lineno = e.get("lineno", "?")
        uri = e.get("uri", "")
        print(f"| `{filepath}` | {lineno} | {uri} | {status} |")

    for e in known_broken:
        filepath = f"{SOURCE_DIR}/{e.get('filename', 'unknown')}"
        issue_num = e.get("_known_issue")
        status = f"Related to #{issue_num}"
        lineno = e.get("lineno", "?")
        uri = e.get("uri", "")
        print(f"| `{filepath}` | {lineno} | {uri} | {status} |")

    print(
        "\n## Action Required\n\n"
        "Update the broken link(s) in the referenced source file(s) to point to "
        "the correct URL, or add them to `linkcheck_ignore` in `source/conf.py` "
        "if they cannot be verified from the CI environment."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
