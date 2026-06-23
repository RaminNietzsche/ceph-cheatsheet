#!/usr/bin/env python3
"""Validate MkDocs nav paths and hub locale switcher URLs."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from repo_paths import DOCS_EN, ROOT, nav_path_to_en_file  # noqa: E402

MKDOCS = ROOT / "mkdocs.yml"

NAV_MD_RE = re.compile(r"^\s+-\s+(?:[^:]+:\s+)?([\w./-]+\.md)\s*$", re.MULTILINE)
HUB_LANG_RE = re.compile(
    r'<a\s+href="([^"]+)"\s+class="hub-lang__item"[^>]*>',
    re.IGNORECASE,
)

LOCALE_EXPECTATIONS: dict[str, dict[str, set[str]]] = {
    "docs/en/index.md": {"en": set(), "fa": {"/fa/"}, "zh": {"/zh/"}},
    "docs/fa/index.md": {"en": {"/en/"}, "fa": set(), "zh": {"/zh/"}},
    "docs/zh/index.md": {"en": {"/en/"}, "fa": {"/fa/"}, "zh": set()},
    "docs/en/cheatsheet/index.md": {"en": set(), "fa": {"/fa/cheatsheet/"}, "zh": {"/zh/cheatsheet/"}},
    "docs/fa/cheatsheet/index.md": {"en": {"/en/cheatsheet/"}, "fa": set(), "zh": {"/zh/cheatsheet/"}},
    "docs/zh/cheatsheet/index.md": {"en": {"/en/cheatsheet/"}, "fa": {"/fa/cheatsheet/"}, "zh": set()},
    "docs/en/arch/index.md": {"en": set(), "fa": {"/fa/arch/"}, "zh": {"/zh/arch/"}},
    "docs/fa/arch/index.md": {"en": {"/en/arch/"}, "fa": set(), "zh": {"/zh/arch/"}},
    "docs/zh/arch/index.md": {"en": {"/en/arch/"}, "fa": {"/fa/arch/"}, "zh": set()},
    "docs/en/dev/index.md": {"en": set(), "fa": {"/fa/dev/"}, "zh": {"/zh/dev/"}},
    "docs/fa/dev/index.md": {"en": {"/en/dev/"}, "fa": set(), "zh": {"/zh/dev/"}},
    "docs/zh/dev/index.md": {"en": {"/en/dev/"}, "fa": {"/fa/dev/"}, "zh": set()},
}


def collect_nav_paths() -> list[str]:
    text = MKDOCS.read_text(encoding="utf-8")
    return NAV_MD_RE.findall(text)


def validate_nav() -> list[str]:
    errors: list[str] = []
    for rel in collect_nav_paths():
        full = nav_path_to_en_file(rel)
        if not full.exists():
            errors.append(f"nav target missing: {rel} (expected {full.relative_to(ROOT)})")
    return errors


def validate_hub_locales() -> list[str]:
    errors: list[str] = []
    for rel, expected in LOCALE_EXPECTATIONS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"hub page missing: {rel}")
            continue
        hrefs = set(HUB_LANG_RE.findall(path.read_text(encoding="utf-8")))
        for locale, allowed in expected.items():
            if not allowed:
                continue
            if not hrefs & allowed:
                errors.append(
                    f"{rel}: locale {locale} link expected one of {sorted(allowed)}, "
                    f"got {sorted(hrefs)}"
                )
    return errors


def main() -> int:
    errors: list[str] = []
    errors.extend(validate_nav())
    errors.extend(validate_hub_locales())
    if errors:
        print("validate-docs-paths: FAILED", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    nav_n = len(collect_nav_paths())
    print(f"validate-docs-paths: OK ({nav_n} nav entries, locale hub links)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
