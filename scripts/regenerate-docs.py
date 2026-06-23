#!/usr/bin/env python3
"""Regenerate all documentation including en/fa/zh variants."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = sys.executable

STEPS = [
    [PY, "scripts/generate-role-scale-guides.py"],
    [PY, "scripts/generate-rgw-guide.py"],
    [PY, "scripts/generate-config-guide.py", "all"],
    [PY, "scripts/sync-i18n-config.py"],
    [PY, "scripts/sync-docs-index.py"],
    [PY, "scripts/sync-i18n-pages.py"],
    [PY, "scripts/fix-html-hrefs.py"],
]


def main() -> int:
    for cmd in STEPS:
        print(f"\n→ {' '.join(cmd)}")
        subprocess.run(cmd, cwd=ROOT, check=True)
    print("\nDone — run `mkdocs serve` to preview (language switcher in header).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
