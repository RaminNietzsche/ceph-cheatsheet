#!/usr/bin/env python3
"""Sync Persian RGW docs from dev-code/rgw/docs-extended into arch/rgw/*.fa.md."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rgw_docs_extended import (  # noqa: E402
    OUT,
    collect_sources,
    needs_locale_stubs,
    process,
    source_root,
    write_locale_stubs,
)


def main() -> int:
    src = source_root()
    pairs = collect_sources(src)
    if not pairs:
        raise SystemExit(f"No markdown pages under {src}")

    stubs = 0
    for src_path, dest_path in pairs:
        body = process(src_path.read_text(encoding="utf-8"))
        sync_file_content(dest_path, body)
        rel = src_path.relative_to(src)
        if needs_locale_stubs(rel):
            write_locale_stubs(rel, body)
            stubs += 2

    print(f"Synced {len(pairs)} Persian page(s) from {src} → {OUT} (+ {stubs} en/zh stubs)")
    return 0


def sync_file_content(dest: Path, body: str) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(body, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
