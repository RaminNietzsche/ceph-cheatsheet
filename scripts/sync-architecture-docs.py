#!/usr/bin/env python3
"""Sync RGW architecture docs from dev-code/rgw into architecture/rgw/*.fa.md."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SRC = ROOT / "dev-code" / "rgw" / "docs-extended" / "pages"
OUT = ROOT / "arch" / "rgw"

SNIPPET_BLOCK = re.compile(
    r'```(?:\w+ title="[^"]*")?\s*\n--8<-- "([^"]+)"\s*\n```',
    re.MULTILINE,
)
SNIPPET_INLINE = re.compile(r'--8<-- "([^"]+)"')
GITHUB = "https://github.com/ceph/ceph/blob/main/src/rgw/"


def source_root() -> Path:
    import os

    if env := os.environ.get("DEV_CODE_RGW_PAGES"):
        return Path(env)
    if DEFAULT_SRC.is_dir():
        return DEFAULT_SRC
    alt = ROOT / "dev-code" / "rgw" / "docs-extended" / "pages"
    if alt.is_dir():
        return alt
    raise SystemExit("RGW docs source not found (dev-code/rgw symlink or DEV_CODE_RGW_PAGES).")


def github_link(ref: str) -> str:
    path, *lines = ref.split(":")
    anchor = ""
    if len(lines) >= 2:
        anchor = f"#L{lines[0]}-L{lines[1]}"
    elif len(lines) == 1:
        anchor = f"#L{lines[0]}"
    return f"{GITHUB}{path}{anchor}"


def process(text: str) -> str:
    def block(m: re.Match[str]) -> str:
        ref = m.group(1)
        path = ref.split(":")[0]
        return f"\n> **Source:** [`{path}`]({github_link(ref)})\n"

    text = SNIPPET_BLOCK.sub(block, text)
    text = SNIPPET_INLINE.sub(
        lambda m: f"[`{m.group(1).split(':')[0]}`]({github_link(m.group(1))})",
        text,
    )
    replacements = [
        ("../../cheatsheet/guides/roles/rgw-admin.md", "../../../cheatsheet/guides/roles/rgw-admin.md"),
        ("../../cheatsheet/cli/troubleshooting.md", "../../../cheatsheet/cli/troubleshooting.md"),
        ("../guides/deployment-implementation-guide.md", "../../../cheatsheet/guides/roles/rgw-admin.md"),
        ("../guides/source-code-in-docs.md", "https://github.com/ceph/ceph/tree/main/src/rgw"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def sync_file(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    body = process(src.read_text(encoding="utf-8"))
    if not dest.name.endswith(".fa.md"):
        dest = dest.with_name(dest.stem + ".fa.md")
    dest.write_text(body, encoding="utf-8")


def main() -> None:
    src = source_root()
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    mapping = [
        ("index.md", OUT / "OVERVIEW.fa.md"),
        *[(f"architecture/{p.name}", OUT / "architecture" / p.name.replace(".md", ".fa.md"))
          for p in sorted((src / "architecture").glob("*.md"))],
        *[(f"modules/{p.name}", OUT / "modules" / p.name.replace(".md", ".fa.md"))
          for p in sorted((src / "modules").glob("*.md"))],
        ("learning-program/index.md", OUT / "learning-program" / "index.fa.md"),
    ]

    for rel, dest in mapping:
        sync_file(src / rel, dest)

    print(f"Synced {len(mapping)} Persian architecture page(s) to {OUT}")


if __name__ == "__main__":
    main()
