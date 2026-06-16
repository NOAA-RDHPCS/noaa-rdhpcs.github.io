#!/usr/bin/env python3
"""Report broken links from Sphinx linkcheck output for the scheduled workflow.

Reads build/linkcheck/output.json and prints a Markdown-formatted issue body
listing broken links (HTTP 4xx excluding 429) and rate-limited links (HTTP 429)
in separate sections.  Timeouts and connection errors are CI noise and are
excluded.

Supports deduplication against known URLs from open issues.  When a
--known-urls-file is provided, links already tracked in open issues are
marked with "Related to #NNN" in the status column instead of the HTTP error.

Exit codes:
  0 - no broken or rate-limited links found
  1 - at least one NEW broken or rate-limited link found (create issue)
  2 - output.json missing or unreadable
  3 - links found but ALL are already known (skip issue creation)
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
RE_429_INFO = re.compile(r"^429\b")


def _is_rate_limited(entry: dict) -> bool:
    """Return True if the entry represents an HTTP 429 rate-limited response."""
    code = entry.get("code", 0)
    if code == 429:
        return True
    # Fallback for Sphinx versions that always write code=0
    if code == 0 and entry.get("status") == "broken":
        return bool(RE_429_INFO.match(entry.get("info", "")))
    return False


def _is_broken_4xx(entry: dict) -> bool:
    """Return True if the entry represents an HTTP 4xx broken link (excluding 429)."""
    # First check if it's rate-limited (429) - handle separately
    if _is_rate_limited(entry):
        return False

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


def _format_status(entry: dict) -> str:
    """Format the status column for a link entry."""
    code = entry.get("code", "")
    info = entry.get("info", "").split("\n")[0]
    return f"{code} — {info}".strip(" —") if code else info


def _print_link_table(entries: list[dict], known_entries: list[dict]) -> None:
    """Print a markdown table of links."""
    print("| File | Line | URL | Status |")
    print("|------|------|-----|--------|")

    # Print new entries first
    for e in entries:
        filepath = f"{SOURCE_DIR}/{e.get('filename', 'unknown')}"
        status = _format_status(e)
        lineno = e.get("lineno", "?")
        uri = e.get("uri", "")
        print(f"| `{filepath}` | {lineno} | {uri} | {status} |")

    # Print known entries with "Related to #NNN"
    for e in known_entries:
        filepath = f"{SOURCE_DIR}/{e.get('filename', 'unknown')}"
        issue_num = e.get("_known_issue")
        status = f"Related to #{issue_num}"
        lineno = e.get("lineno", "?")
        uri = e.get("uri", "")
        print(f"| `{filepath}` | {lineno} | {uri} | {status} |")


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

    # Categorize all entries
    broken = []
    rate_limited = []

    with OUTPUT_JSON.open() as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            if _is_rate_limited(entry):
                rate_limited.append(entry)
            elif _is_broken_4xx(entry):
                broken.append(entry)

    if not broken and not rate_limited:
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

    # Categorize rate-limited links as new or known
    new_rate_limited = []
    known_rate_limited = []
    for entry in rate_limited:
        uri = entry.get("uri", "")
        if uri in known_urls:
            entry["_known_issue"] = known_urls[uri]
            known_rate_limited.append(entry)
        else:
            new_rate_limited.append(entry)

    # If all links are already known, skip issue creation
    if not new_broken and not new_rate_limited:
        total_known = len(known_broken) + len(known_rate_limited)
        print(
            f"All {total_known} link(s) are already tracked in open issues."
        )
        return 3

    # Generate issue body - intro paragraph
    broken_total = len(broken)
    rate_limited_total = len(rate_limited)

    intro_parts = []
    if broken_total > 0:
        intro_parts.append(
            f"{broken_total} broken link(s) "
            f"({len(new_broken)} new, {len(known_broken)} already tracked)"
        )
    if rate_limited_total > 0:
        intro_parts.append(
            f"{rate_limited_total} rate-limited link(s) "
            f"({len(new_rate_limited)} new, {len(known_rate_limited)} already tracked)"
        )

    print(f"The weekly link check found {' and '.join(intro_parts)}.\n")

    # Broken Links section
    if broken:
        print(
            "These links return HTTP 4xx responses and should be updated or removed.\n"
        )
        print("## Broken Links\n")
        _print_link_table(new_broken, known_broken)
        print()

    # Rate-Limited Links section
    if rate_limited:
        print("## Rate-Limited Links\n")
        print(
            "The following links returned HTTP 429 (Too Many Requests). These may be "
            "valid links that rate-limit automated requests from CI environments.\n"
        )
        _print_link_table(new_rate_limited, known_rate_limited)
        print(
            "\nIf a rate-limited link appears repeatedly across multiple weekly "
            "checks, consider adding its domain to `linkcheck_ignore` in "
            "`source/conf.py` with a comment explaining that the site rate-limits "
            "automated requests.\n"
        )

    # Action Required section
    print("## Action Required\n")
    print(
        "Update the broken link(s) in the referenced source file(s) to point to "
        "the correct URL, or add them to `linkcheck_ignore` in `source/conf.py` "
        "if they cannot be verified from the CI environment."
    )

    return 1


if __name__ == "__main__":
    sys.exit(main())
