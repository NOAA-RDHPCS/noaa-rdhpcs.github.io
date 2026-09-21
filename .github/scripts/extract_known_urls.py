#!/usr/bin/env python3
"""Extract known broken URLs from open GitHub issues.

Parses JSON output from `gh issue list --json number,body` and extracts URLs
from the markdown table in each issue body.  Outputs a JSON mapping of URL to
the lowest (oldest) issue number that tracks it.

Usage:
    gh issue list --json number,body > open_issues.json
    python extract_known_urls.py open_issues.json > known_urls.json

Output format:
    {"http://example.com/broken": 742, "http://other.com/gone": 755}
"""

import json
import re
import sys
from pathlib import Path

# Pattern to match URLs in the markdown table's URL column.
# The table format is: | `filepath` | lineno | URL | status |
# URLs appear after the third pipe on data rows.
RE_TABLE_ROW = re.compile(
    r"^\|\s*`[^`]+`\s*\|\s*\d+\s*\|\s*(https?://[^\s|]+)\s*\|",
    re.MULTILINE,
)


def extract_urls_from_body(body: str) -> list[str]:
    """Extract all URLs from the broken links table in an issue body."""
    return RE_TABLE_ROW.findall(body)


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <open_issues.json>", file=sys.stderr)
        return 1

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"ERROR: {input_path} not found.", file=sys.stderr)
        return 1

    try:
        with input_path.open() as fh:
            issues = json.load(fh)
    except json.JSONDecodeError as e:
        print(f"ERROR: Failed to parse JSON: {e}", file=sys.stderr)
        return 1

    # Map URL -> lowest issue number (oldest issue)
    url_to_issue: dict[str, int] = {}

    for issue in issues:
        number = issue.get("number")
        body = issue.get("body", "")
        if not number or not body:
            continue

        urls = extract_urls_from_body(body)
        for url in urls:
            if url not in url_to_issue or number < url_to_issue[url]:
                url_to_issue[url] = number

    print(json.dumps(url_to_issue, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
