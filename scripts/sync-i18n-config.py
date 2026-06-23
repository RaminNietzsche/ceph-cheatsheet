#!/usr/bin/env python3
"""Write .fa.md and .zh.md for config/OVERVIEW only (tables stay English in config/)."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from i18n import set_locale, t, write_localized  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OVERVIEW = ROOT / "config" / "OVERVIEW.md"


def main() -> None:
    if not OVERVIEW.exists():
        raise SystemExit(f"Missing {OVERVIEW}")
    body = OVERVIEW.read_text(encoding="utf-8")
    contents = {"en": body}
    for locale in ("fa", "zh"):
        set_locale(locale)
        note = t("upstream_table_note")
        contents[locale] = f"{note}\n\n{body}" if note else body
    set_locale("en")
    write_localized(OVERVIEW, contents)
    print(f"Synced i18n variants for {OVERVIEW.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
