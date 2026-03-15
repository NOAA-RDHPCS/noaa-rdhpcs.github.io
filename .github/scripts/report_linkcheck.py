#!/usr/bin/env python3
"""Report broken links from Sphinx linkcheck output for the scheduled workflow.

Reads build/linkcheck/output.json and prints a Markdown-formatted issue body
listing all broken links (HTTP 4xx only).  Timeouts and connection errors are
CI noise and are excluded.

Exit codes:
  0 - no broken links found
  1 - one or more broken links found
  2 - output.json missing or unreadable
"""

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


def main() -> int:
    if not OUTPUT_JSON.exists():
        print(f"ERROR: {OUTPUT_JSON} not found.", file=sys.stderr)
        return 2

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

    print(
        f"The weekly link check found {len(broken)} broken link(s).\n\n"
        "These links return HTTP 4xx responses and should be updated or removed.\n"
    )
    print("## Broken Links\n")
    print("| File | Line | URL | Status |")
    print("|------|------|-----|--------|")
    for e in broken:
        filepath = f"{SOURCE_DIR}/{e.get('filename', 'unknown')}"
        code = e.get("code", "")
        info = e.get("info", "").split("\n")[0]
        status = f"{code} — {info}".strip(" —") if code else info
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
