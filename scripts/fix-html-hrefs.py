#!/usr/bin/env python3
"""Rewrite .md suffixes in raw HTML href attributes for MkDocs static output."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HREF_RE = re.compile(r'(<a\s[^>]*?)href="([^"]+)"', re.IGNORECASE)

FILES = [
    ROOT / "config" / "OVERVIEW.md",
    ROOT / "guides" / "OVERVIEW.md",
    ROOT / "cli" / "OVERVIEW.md",
    ROOT / "REFERENCE.md",
]


def site_href(href: str) -> str:
    if not href.endswith(".md"):
        return href
    if href.startswith(("http://", "https://", "mailto:")):
        return href
    return href[:-3] + "/"


def fix_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    changed = False

    def repl(match: re.Match[str]) -> str:
        nonlocal changed
        prefix, href = match.group(1), match.group(2)
        new_href = site_href(href)
        if new_href != href:
            changed = True
        return f'{prefix}href="{new_href}"'

    updated = HREF_RE.sub(repl, text)
    if changed:
        path.write_text(updated, encoding="utf-8")
    return changed


def main() -> None:
    targets = FILES
    if len(sys.argv) > 1:
        targets = [Path(p) for p in sys.argv[1:]]
    fixed = 0
    for path in targets:
        if not path.exists():
            print(f"skip missing {path}")
            continue
        if fix_file(path):
            print(f"fixed {path.relative_to(ROOT)}")
            fixed += 1
    print(f"Done — updated {fixed} file(s)")


if __name__ == "__main__":
    main()
