#!/usr/bin/env python3
"""Check URLs that are excluded from Sphinx linkcheck due to CI environment limitations.

Reads linkcheck_ignore patterns from source/conf.py, then extracts URLs that
will generate actual hyperlinks in the built documentation by parsing RST
hyperlink syntax:

  1. Inline references:      `Link text <URL>`_  /  `Link text <URL>`__
  2. Hyperlink targets:      .. _label: URL  (label may be quoted)
  3. Bare URLs in paragraph text (skipped when inside code blocks)

Checks each matched URL with SSL verification disabled. URLs that are
unreachable (connection errors, timeouts) are skipped — these are typically
VPN-only or auth-required URLs that cannot be reached from CI.

Exit codes:
  0 - all checked URLs are reachable (2xx/3xx)
  1 - one or more URLs returned a 4xx response (broken links)
"""

import ast
import re
import sys
import time
from pathlib import Path

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CONF_PY = Path("source/conf.py")
SOURCE_DIR = Path("source")
REQUEST_TIMEOUT = 20
INTER_URL_DELAY = 1  # seconds between URL checks (politeness)
RETRY_DELAY = 1      # seconds between retry attempts on 5xx
MAX_RETRIES = 3

# URL check result status values
STATUS_OK = "ok"
STATUS_BROKEN = "broken"
STATUS_UNREACHABLE = "unreachable"

# Shared request kwargs for all HTTP calls (SSL verification disabled intentionally)
REQ_KWARGS: dict = {
    "verify": False,
    "timeout": REQUEST_TIMEOUT,
    "allow_redirects": True,
}

# RST patterns that produce actual <a> hyperlinks
# Pattern 1: inline reference  `text <URL>`_  or  `text <URL>`__
RE_INLINE = re.compile(r"`[^`<]*<(https?://[^>]+)>`__?")
# Pattern 2: named hyperlink target  .. _label: URL  (label may be quoted)
RE_TARGET = re.compile(r"^\s*\.\.\s+_`?[^`:]+`?:\s+(https?://\S+)", re.MULTILINE)
# Pattern 3: bare URL in paragraph text (not in a code block)
RE_BARE = re.compile(r"(?<![`<])(https?://[^\s`<>\"')\]\\]+)")

# RST directives that introduce a literal/code block
CODE_BLOCK_DIRECTIVES = re.compile(
    r"^\s*\.\.\s+(code-block|code|sourcecode|highlight|parsed-literal)::"
)


def line_of(text: str, pos: int) -> int:
    """Return the 1-based line number of character position pos in text."""
    return text[:pos].count("\n") + 1


def get_ignore_patterns() -> list[re.Pattern]:
    """Parse linkcheck_ignore from conf.py and return compiled patterns.

    Uses pat.match() semantics to match Sphinx's own linkcheck behavior,
    where patterns are anchored to the start of the URL.
    """
    tree = ast.parse(CONF_PY.read_text())
    patterns = []
    for node in tree.body:  # Only top-level assignments needed
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "linkcheck_ignore":
                    if isinstance(node.value, ast.List):
                        for elt in node.value.elts:
                            if not (isinstance(elt, ast.Constant) and isinstance(elt.value, str)):
                                continue
                            try:
                                patterns.append(re.compile(elt.value))
                            except re.error as e:
                                print(
                                    f"WARNING: skipping invalid regex in linkcheck_ignore: "
                                    f"{elt.value!r} ({e})",
                                    file=sys.stderr,
                                )
    return patterns


def extract_rst_links(rst_file: Path) -> list[tuple[str, int]]:
    """Return (url, lineno) pairs for every hyperlink in an RST file.

    Uses RST-aware parsing to skip URLs inside code blocks.
    """
    text = rst_file.read_text(errors="replace")
    results: list[tuple[str, int]] = []
    seen: set[str] = set()

    # --- Patterns 1 & 2: parse via regex on full text (line numbers via finditer) ---
    for m in RE_INLINE.finditer(text):
        url = m.group(1).strip()
        if url not in seen:
            seen.add(url)
            results.append((url, line_of(text, m.start())))

    for m in RE_TARGET.finditer(text):
        url = m.group(1).strip()
        if url not in seen:
            seen.add(url)
            results.append((url, line_of(text, m.start())))

    # --- Pattern 3: bare URLs, skipping code block content ---
    in_code_block = False
    code_block_indent = 0

    for lineno, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        indent = len(line) - len(stripped)

        if CODE_BLOCK_DIRECTIVES.match(line):
            in_code_block = True
            code_block_indent = indent
            continue

        # Leaving a code block when indentation returns to directive level
        if in_code_block:
            if stripped and indent <= code_block_indent:
                in_code_block = False
            else:
                continue  # skip lines inside code block

        # Lines ending with '::' introduce a literal block
        if stripped.endswith("::"):
            in_code_block = True
            code_block_indent = indent
            continue

        for m in RE_BARE.finditer(line):
            url = re.sub(r"[.,;:]+$", "", m.group(1))
            if url not in seen:
                seen.add(url)
                results.append((url, lineno))

    return results


def find_urls_in_source(patterns: list[re.Pattern]) -> dict[str, list[str]]:
    """Return a dict mapping ignored URL -> list of 'file:line' locations."""
    url_locations: dict[str, list[str]] = {}
    for rst_file in SOURCE_DIR.rglob("*.rst"):
        for url, lineno in extract_rst_links(rst_file):
            if any(p.match(url) for p in patterns):
                url_locations.setdefault(url, []).append(f"{rst_file}:{lineno}")
    return url_locations


def check_url(session: requests.Session, url: str) -> tuple[str, int | None]:
    """Return (status, http_code_or_None).

    status is one of: STATUS_OK, STATUS_BROKEN, STATUS_UNREACHABLE
    """
    for attempt in range(MAX_RETRIES):
        try:
            resp = session.head(url, **REQ_KWARGS)
            # Some servers reject HEAD; fall back to GET (stream to avoid downloading body)
            if resp.status_code == 405:
                resp = session.get(url, stream=True, **REQ_KWARGS)
                resp.close()
            code = resp.status_code
            if 200 <= code < 400:
                return STATUS_OK, code
            if 400 <= code < 500:
                return STATUS_BROKEN, code
            # 5xx: retry
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            if attempt == MAX_RETRIES - 1:
                return STATUS_UNREACHABLE, None
        if attempt < MAX_RETRIES - 1:
            time.sleep(RETRY_DELAY)
    return STATUS_UNREACHABLE, None


def main() -> int:
    compiled = get_ignore_patterns()
    if not compiled:
        print("No linkcheck_ignore patterns found in conf.py.", file=sys.stderr)
        return 1

    ignored_urls = find_urls_in_source(compiled)

    if not ignored_urls:
        print("No ignored URLs found in RST source files.")
        return 0

    print(f"Checking {len(ignored_urls)} ignored URL(s)...\n")

    broken: dict[str, tuple[int | None, list[str]]] = {}
    sorted_items = sorted(ignored_urls.items())

    with requests.Session() as session:
        session.headers["User-Agent"] = "Mozilla/5.0 (compatible; LinkChecker/1.0)"
        for i, (url, locations) in enumerate(sorted_items):
            status, code = check_url(session, url)
            label = f"HTTP {code}" if code else STATUS_UNREACHABLE
            print(f"  [{status.upper():11s}] ({label:12s}) {url}")
            if status == STATUS_BROKEN:
                broken[url] = (code, locations)
            if i < len(sorted_items) - 1:
                time.sleep(INTER_URL_DELAY)

    print()
    if broken:
        print(f"{len(broken)} broken link(s) found:\n")
        for url, (code, locations) in broken.items():
            print(f"  URL:    {url}")
            print(f"  Status: HTTP {code}")
            print("  Found in:")
            for loc in locations:
                print(f"    {loc}")
            print()
        return 1

    print("All reachable ignored URLs are OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
