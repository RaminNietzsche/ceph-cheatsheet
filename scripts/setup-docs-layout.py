#!/usr/bin/env python3
"""Ensure docs/{en,fa,zh}/ layout exists for MkDocs folder i18n."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from repo_paths import DOCS, DOCS_EN, DOCS_FA, DOCS_ZH, LOCALES  # noqa: E402

REQUIRED_SECTIONS = ("cheatsheet", "arch", "dev")


def main() -> int:
    missing: list[str] = []
    for locale in LOCALES:
        root = DOCS / locale
        root.mkdir(parents=True, exist_ok=True)
        for section in REQUIRED_SECTIONS:
            sec = root / section
            if not sec.is_dir():
                missing.append(str(sec.relative_to(DOCS.parent)))

    if missing:
        print("docs layout incomplete — run:", file=sys.stderr)
        print("  python3 scripts/migrate-to-docs-locale-folders.py --remove-legacy", file=sys.stderr)
        for m in missing:
            print(f"  missing: {m}", file=sys.stderr)
        return 1

    print(f"docs layout OK ({DOCS_EN.name}/, {DOCS_FA.name}/, {DOCS_ZH.name}/ + sections)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
