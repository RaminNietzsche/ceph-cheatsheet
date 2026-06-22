#!/usr/bin/env python3
"""Sync docs/index.md from REFERENCE.md for MkDocs home page."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFERENCE = ROOT / "REFERENCE.md"
INDEX = ROOT / "docs" / "index.md"

SUBSTITUTIONS = [
    ("[`VERSION`](VERSION)", "[VERSION](../VERSION)"),
    (
        "[README](https://github.com/RaminNietzsche/ceph-cheatsheet) · [License](LICENSE)",
        "[README](https://github.com/RaminNietzsche/ceph-cheatsheet) · [License](../LICENSE)",
    ),
]


def main() -> None:
    if not REFERENCE.exists():
        raise SystemExit(f"Missing {REFERENCE}")
    text = REFERENCE.read_text(encoding="utf-8")
    for old, new in SUBSTITUTIONS:
        text = text.replace(old, new)
    INDEX.parent.mkdir(parents=True, exist_ok=True)
    INDEX.write_text(text, encoding="utf-8")
    print(f"Synced {INDEX} from {REFERENCE}")


if __name__ == "__main__":
    main()
