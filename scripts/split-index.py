#!/usr/bin/env python3
"""Split config/readme.md into per-subsystem INDEX.md files."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config"
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
        index_path.write_text("".join(body).rstrip() + "\n", encoding="utf-8")

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
