#!/usr/bin/env python3
"""Split config/readme.md into per-subsystem INDEX.md files."""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from repo_paths import CONFIG  # noqa: E402

SOURCE = CONFIG / "readme.md"

SUBSYSTEMS = {
    "osd": "Object Storage Daemon (OSD)",
    "immutable-object-cache": "Immutable Object Cache",
    "rbd": "RADOS Block Device (RBD)",
    "mds-client": "CephFS MDS Client",
    "mon": "Monitor (MON)",
    "crimson": "Crimson / Seastore (experimental)",
    "cephfs-mirror": "CephFS Mirror",
    "rgw": "RADOS Gateway (RGW / S3)",
    "rbd-mirror": "RBD Mirror",
    "mds": "Metadata Server (CephFS MDS)",
    "global": "Global / cross-cutting options",
    "mgr": "Manager (MGR)",
    "ceph-exporter": "Ceph Exporter",
}

# [name](/config/sub/file.md#SP_x) or [name](sub/file.md#SP_x)
LINK_RE = re.compile(
    r"\[(?P<label>[^\]]+)\]\((?P<href>(?:/config/)?(?P<sub>[^/]+)/(?P<file>[^#\)]+)#(?P<anchor>SP_[^)]+))\)"
)


def rel_href(from_sub: str, to_sub: str, to_file: str, anchor: str) -> str:
    if from_sub == to_sub:
        return f"{to_file}#{anchor}"
    return f"../{to_sub}/{to_file}#{anchor}"


def rewrite_index_links(text: str, subsystem: str) -> str:
    def repl(match: re.Match[str]) -> str:
        href = rel_href(
            subsystem,
            match.group("sub"),
            match.group("file"),
            match.group("anchor"),
        )
        return f"[{match.group('label')}]({href})"

    return LINK_RE.sub(repl, text)


def split_index() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"Source not found: {SOURCE}")

    content = SOURCE.read_text(encoding="utf-8")
    lines = content.splitlines(keepends=True)

    sections: dict[str, list[str]] = {}
    current: str | None = None

    for line in lines:
        if line.startswith("# ") and not line.startswith("## "):
            name = line[2:].strip().lower()
            if name in SUBSYSTEMS:
                current = name
                sections[current] = [f"# {name}\n", "\n"]
                continue
        if current is not None:
            sections[current].append(line)

    for name, body in sections.items():
        target_dir = CONFIG / name
        target_dir.mkdir(parents=True, exist_ok=True)
        index_path = target_dir / "INDEX.md"
        index_text = rewrite_index_links("".join(body).rstrip() + "\n", name)
        index_path.write_text(index_text, encoding="utf-8")

        readme_path = target_dir / "README.md"
        title = SUBSYSTEMS[name]
        md_files = sorted(p.name for p in target_dir.glob("*.md") if p.name not in {"README.md", "INDEX.md"})
        files_section = "\n".join(f"- [{f}]({f})" for f in md_files)
        readme_path.write_text(
            f"# {title}\n\n"
            f"[← Back to config index](../OVERVIEW.md)\n\n"
            f"- [Full option index](INDEX.md)\n\n"
            f"## Config files\n\n{files_section}\n",
            encoding="utf-8",
        )

    print(f"Split {len(sections)} subsystems from {SOURCE}")


if __name__ == "__main__":
    split_index()
