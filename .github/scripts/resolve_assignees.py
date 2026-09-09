#!/usr/bin/env python3
"""Resolve code owners for files listed in a broken-links issue body.

Parses the markdown table in an issue body to extract file paths, then uses
the CODEOWNERS file to determine who should be assigned to the issue.

Usage:
    python resolve_assignees.py issue_body.md

Output:
    Comma-separated list of GitHub usernames (without @ prefix) suitable for
    use with `gh issue edit --add-assignee`.

Exit codes:
    0 - success, assignees printed to stdout
    1 - no assignees found or error
"""

import re
import sys
from pathlib import Path

from codeowners import CodeOwners

CODEOWNERS_PATH = Path(".github/CODEOWNERS")
MAX_ASSIGNEES = 10

# Pattern to match file paths in the markdown table.
# Table format: | `source/path/file.rst` | lineno | URL | status |
RE_FILE_PATH = re.compile(r"^\|\s*`([^`]+)`\s*\|", re.MULTILINE)


def extract_file_paths(issue_body: str) -> list[str]:
    """Extract file paths from the broken links table in an issue body."""
    return RE_FILE_PATH.findall(issue_body)


def get_owners_for_file(owners: CodeOwners, filepath: str) -> list[str]:
    """Get the list of owners for a file path.

    Returns usernames without the @ prefix.
    """
    # The codeowners library expects paths without leading slash for matching,
    # but CODEOWNERS patterns may have leading slashes.
    # Normalize the path to match CODEOWNERS format.
    normalized = filepath.lstrip("/")

    matches = owners.of(normalized)
    if not matches:
        return []

    # matches is a list of (owner_type, owner_name) tuples
    # owner_type is 'USERNAME' or 'TEAM', owner_name includes the @ prefix
    return [owner_name.lstrip("@") for _, owner_name in matches]


def select_assignees(
    file_owners: dict[str, list[str]], max_assignees: int = MAX_ASSIGNEES
) -> list[str]:
    """Select assignees ensuring at least one owner per file, up to max.

    Args:
        file_owners: Dict mapping file paths to list of owners
        max_assignees: Maximum number of assignees (GitHub limit is 10)

    Returns:
        List of unique usernames to assign
    """
    if not file_owners:
        return []

    # Collect all unique owners
    all_owners: set[str] = set()
    for owners in file_owners.values():
        all_owners.update(owners)

    # If we're under the limit, return all owners
    if len(all_owners) <= max_assignees:
        return sorted(all_owners)

    # Otherwise, ensure at least one owner per file
    selected: set[str] = set()

    # First pass: pick the first owner for each file to ensure coverage
    for filepath, owners in file_owners.items():
        if owners and not selected.intersection(owners):
            # No owner for this file is selected yet, add the first one
            selected.add(owners[0])

    # If we're already at the limit, stop
    if len(selected) >= max_assignees:
        return sorted(list(selected)[:max_assignees])

    # Second pass: add remaining owners until we hit the limit
    for owner in sorted(all_owners):
        if owner not in selected:
            selected.add(owner)
            if len(selected) >= max_assignees:
                break

    return sorted(selected)


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <issue_body.md>", file=sys.stderr)
        return 1

    issue_body_path = Path(sys.argv[1])
    if not issue_body_path.exists():
        print(f"ERROR: {issue_body_path} not found.", file=sys.stderr)
        return 1

    if not CODEOWNERS_PATH.exists():
        print(f"ERROR: {CODEOWNERS_PATH} not found.", file=sys.stderr)
        return 1

    # Load CODEOWNERS
    with CODEOWNERS_PATH.open() as fh:
        owners = CodeOwners(fh.read())

    # Parse issue body for file paths
    issue_body = issue_body_path.read_text()
    file_paths = extract_file_paths(issue_body)

    if not file_paths:
        print("No file paths found in issue body.", file=sys.stderr)
        return 1

    # Get owners for each file
    file_owners: dict[str, list[str]] = {}
    for filepath in file_paths:
        owners_list = get_owners_for_file(owners, filepath)
        if owners_list:
            file_owners[filepath] = owners_list

    if not file_owners:
        print("No code owners found for any files.", file=sys.stderr)
        return 1

    # Select assignees
    assignees = select_assignees(file_owners)

    if not assignees:
        print("No assignees selected.", file=sys.stderr)
        return 1

    # Output comma-separated list for gh issue edit --add-assignee
    print(",".join(assignees))
    return 0


if __name__ == "__main__":
    sys.exit(main())
