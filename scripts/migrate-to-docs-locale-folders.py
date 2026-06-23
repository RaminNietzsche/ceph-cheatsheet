#!/usr/bin/env python3
"""One-time migration: merge cheatsheet/arch/dev into docs/{en,fa,zh}/."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from repo_paths import (  # noqa: E402
    DOCS,
    DOCS_EN,
    DOCS_FA,
    DOCS_ZH,
    LEGACY_ARCH,
    LEGACY_CHEATSHEET,
    LEGACY_DEV,
    LOCALES,
)

SECTIONS: tuple[tuple[Path, str], ...] = (
    (LEGACY_CHEATSHEET, "cheatsheet"),
    (LEGACY_ARCH, "arch"),
    (LEGACY_DEV, "dev"),
)

DOCS_SHELL_STEMS = ("index", "version", "compatibility", "license", "readability-guide")

SHARED_KEEP = frozenset({"stylesheets", "javascripts", "README.md"})


def locale_for_filename(name: str) -> tuple[str, str] | None:
    if name.endswith(".fa.md"):
        return "fa", name[: -len(".fa.md")] + ".md"
    if name.endswith(".zh.md"):
        return "zh", name[: -len(".zh.md")] + ".md"
    if name.endswith(".md"):
        return "en", name
    return None


def copy_md(src: Path, dest: Path, dry_run: bool) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dry_run:
        print(f"  {src.relative_to(src.anchor)} → {dest}")
        return
    shutil.copy2(src, dest)


def migrate_section_tree(src_root: Path, section: str, dry_run: bool) -> int:
    if not src_root.is_dir():
        print(f"skip missing section: {src_root}", file=sys.stderr)
        return 0
    count = 0
    for src in sorted(src_root.rglob("*.md")):
        parsed = locale_for_filename(src.name)
        if not parsed:
            continue
        locale, dest_name = parsed
        rel_parent = src.parent.relative_to(src_root)
        dest = DOCS / locale / section / rel_parent / dest_name
        copy_md(src, dest, dry_run)
        count += 1
    return count


def migrate_docs_shell(dry_run: bool) -> int:
    count = 0
    for stem in DOCS_SHELL_STEMS:
        en_src = DOCS / f"{stem}.md"
        if en_src.is_file() and not en_src.is_symlink():
            copy_md(en_src, DOCS_EN / f"{stem}.md", dry_run)
            count += 1
        for locale in ("fa", "zh"):
            loc_src = DOCS / f"{stem}.{locale}.md"
            if loc_src.is_file():
                copy_md(loc_src, DOCS / locale / f"{stem}.md", dry_run)
                count += 1
    return count


def remove_legacy(dry_run: bool) -> None:
    for path in (LEGACY_CHEATSHEET, LEGACY_ARCH, LEGACY_DEV):
        if path.exists():
            if dry_run:
                print(f"would remove {path}")
            else:
                shutil.rmtree(path)
                print(f"removed {path.relative_to(path.parent.parent)}")

    for name in ("cheatsheet", "arch", "dev"):
        link = DOCS / name
        if link.is_symlink() or link.exists():
            if dry_run:
                print(f"would remove {link}")
            else:
                link.unlink()
                print(f"removed {link.relative_to(DOCS.parent)}")

    for stem in DOCS_SHELL_STEMS:
        for suffix in ("", ".fa", ".zh"):
            old = DOCS / f"{stem}{suffix}.md"
            if old.is_file() and not old.is_symlink():
                if dry_run:
                    print(f"would remove {old}")
                else:
                    old.unlink()
                    print(f"removed {old.relative_to(DOCS.parent)}")

    readme = DOCS / "README.md"
    if readme.is_symlink() or readme.exists():
        if dry_run:
            print(f"would remove {readme}")
        else:
            readme.unlink(missing_ok=True)


def ensure_locale_dirs(dry_run: bool) -> None:
    for loc in LOCALES:
        path = DOCS / loc
        if dry_run:
            print(f"ensure {path}")
        else:
            path.mkdir(parents=True, exist_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Print actions only")
    parser.add_argument(
        "--remove-legacy",
        action="store_true",
        help="Delete root cheatsheet/arch/dev and docs symlinks after copy",
    )
    args = parser.parse_args()

    ensure_locale_dirs(args.dry_run)
    total = migrate_docs_shell(args.dry_run)
    for src, section in SECTIONS:
        n = migrate_section_tree(src, section, args.dry_run)
        print(f"migrated {n} file(s) → docs/{{en,fa,zh}}/{section}/")
        total += n

    print(f"total migrated: {total} markdown file(s)")

    if args.remove_legacy:
        remove_legacy(args.dry_run)

    if not args.dry_run and not args.remove_legacy:
        print("Tip: re-run with --remove-legacy after verifying docs/en/ content")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
