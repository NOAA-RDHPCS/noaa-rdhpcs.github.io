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
import sys
from pathlib import Path

OUTPUT_JSON = Path("build/linkcheck/output.json")
SOURCE_DIR = "source"


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
            if entry.get("status") == "broken" and 400 <= entry.get("code", 0) < 500:
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
        filepath = f"{SOURCE_DIR}/{e['filename']}"
        code = e.get("code", "")
        info = e.get("info", "").split("\n")[0]
        status = f"{code} — {info}".strip(" —") if code else info
        print(f"| `{filepath}` | {e['lineno']} | {e['uri']} | {status} |")

    print(
        "\n## Action Required\n\n"
        "Update the broken link(s) in the referenced source file(s) to point to "
        "the correct URL, or add them to `linkcheck_ignore` in `source/conf.py` "
        "if they cannot be verified from the CI environment."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
