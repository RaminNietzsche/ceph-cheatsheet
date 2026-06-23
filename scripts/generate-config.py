#!/usr/bin/env python3
"""Generate config markdown from upstream Ceph option YAML files."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from repo_paths import CONFIG, ROOT  # noqa: E402

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

UPSTREAM = Path(__file__).resolve().parent / "upstream"
BASE_URL = "https://raw.githubusercontent.com/ceph/ceph/{ref}/src/common/options/{name}.yaml.in"

SUBSYSTEMS = [
    "global",
    "osd",
    "mon",
    "mgr",
    "mds",
    "mds-client",
    "rgw",
    "rbd",
    "rbd-mirror",
    "cephfs-mirror",
    "crimson",
    "immutable-object-cache",
    "ceph-exporter",
]

SUBSYSTEM_TITLES = {
    "global": "Global / cross-cutting options",
    "osd": "Object Storage Daemon (OSD)",
    "mon": "Monitor (MON)",
    "mgr": "Manager (MGR)",
    "mds": "Metadata Server (CephFS MDS)",
    "mds-client": "CephFS MDS Client",
    "rgw": "RADOS Gateway (RGW / S3)",
    "rbd": "RADOS Block Device (RBD)",
    "rbd-mirror": "RBD Mirror",
    "cephfs-mirror": "CephFS Mirror",
    "crimson": "Crimson / Seastore (experimental)",
    "immutable-object-cache": "Immutable Object Cache",
    "ceph-exporter": "Ceph Exporter",
}

README_SECTION_ORDER = [
    "osd",
    "immutable-object-cache",
    "rbd",
    "mds-client",
    "mon",
    "crimson",
    "cephfs-mirror",
    "rgw",
    "rbd-mirror",
    "mds",
    "global",
    "mgr",
    "ceph-exporter",
]

TABLE_HEADER = (
    "| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | "
    "Min | Max | Valid Values | verbatim | See also | Flags | Services | "
    "Validator | Long Desc | Tags |\n"
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | "
    "--- | --- | --- | --- | --- |\n"
)

LEVEL_LEGEND = (
    '<div class="level-legend">'
    '<span class="badge badge-level-basic">Basic</span>'
    '<span class="badge badge-level-advanced">Advanced</span>'
    '<span class="badge badge-level-dev">Dev</span>'
    "</div>\n\n"
)


def group_key(subsystem: str, name: str) -> str:
    if subsystem == "global":
        parts = name.split("_")
        return parts[0] if len(parts) > 1 else name
    if subsystem == "rgw":
        if name.startswith("motr_"):
            return "motr"
        if name.startswith("rgwlc_"):
            return "rgwlc"
        return "rgw"
    if subsystem == "mon":
        if name.startswith("paxos_"):
            return "paxos"
        if name.startswith("mds_"):
            return "mds"
        if name.startswith("osd_"):
            return "osd"
        return "mon"
    if subsystem == "mgr":
        if name.startswith("cephadm_"):
            return "cephadm"
        if name.startswith("mon_"):
            return "mon"
        return "mgr"
    if subsystem == "mds-client":
        for prefix in ("client", "debug", "fake", "fuse", "osd"):
            if name.startswith(f"{prefix}_"):
                return prefix
        return name.split("_")[0]
    if subsystem == "crimson":
        if name.startswith("seastore_"):
            return "seastore"
        return "crimson"
    if subsystem == "rbd-mirror":
        return "rbd"
    if subsystem == "cephfs-mirror":
        return "cephfs"
    if subsystem == "immutable-object-cache":
        return "immutable"
    return subsystem


def group_title(key: str) -> str:
    if key == "rgwlc":
        return "Rgwlc"
    return key.replace("-", " ").title()


def fetch_yaml(name: str, ref: str, cache_dir: Path) -> str:
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_path = cache_dir / f"{name}.yaml.in"
    url = BASE_URL.format(ref=ref, name=name)
    if cache_path.exists() and cache_path.stat().st_size > 0:
        return cache_path.read_text(encoding="utf-8")
    print(f"  downloading {name} …")
    with urllib.request.urlopen(url, timeout=120) as resp:
        text = resp.read().decode("utf-8")
    cache_path.write_text(text, encoding="utf-8")
    return text


def load_options(text: str) -> list[dict]:
    cleaned = re.sub(r"@[A-Za-z0-9_]+@", "0", text)
    data = yaml.safe_load(cleaned)
    return data.get("options") or []


def fmt_type(value: str) -> str:
    aliases = {
        "uuid": "Uuid",
        "addr": "Addr",
        "addrvec": "Addrvec",
        "secs": "Secs",
        "millisecs": "Millisecs",
    }
    lower = value.lower()
    if lower in aliases:
        return aliases[lower]
    return lower[:1].upper() + lower[1:]


def fmt_level(value: str) -> str:
    label = value[:1].upper() + value[1:].lower()
    css = {
        "basic": "badge-level-basic",
        "advanced": "badge-level-advanced",
        "dev": "badge-level-dev",
    }.get(label.lower(), "badge-level-advanced")
    return f'<span class="badge {css}">{label}</span>'


def fmt_default(value, typ: str) -> str:
    if value is None:
        return ""
    if typ == "bool":
        if isinstance(value, bool):
            return "True" if value else "False"
        return "True" if str(value).lower() in ("true", "1", "yes") else "False"
    if isinstance(value, bool):
        return "True" if value else "False"
    if isinstance(value, (int, float)):
        return str(value)
    return str(value)


def fmt_services(services) -> str:
    if not services:
        return ""
    if isinstance(services, list):
        if len(services) == 1:
            return str(services[0])
        return json.dumps(services)
    return str(services)


def fmt_flags(flags) -> str:
    if not flags:
        return ""
    return " ".join(f.upper().replace("-", "_") for f in flags)


def fmt_tags(tags) -> str:
    if not tags:
        return ""
    return " ".join(str(t) for t in tags)


def fmt_enum(values) -> str:
    if not values:
        return ""
    return json.dumps([str(v) for v in values])


def option_href(
    from_subsystem: str,
    from_filename: str,
    to_name: str,
    option_locations: dict[str, tuple[str, str]],
) -> str:
    to_subsystem, to_filename = option_locations[to_name]
    if to_subsystem == from_subsystem and to_filename == from_filename:
        return f"#SP_{to_name}"
    from_dir = CONFIG / from_subsystem
    to_path = CONFIG / to_subsystem / to_filename
    rel = Path(os.path.relpath(to_path, from_dir)).as_posix()
    return f"{rel}#SP_{to_name}"


def fmt_see_also(
    names: list[str],
    from_subsystem: str,
    from_filename: str,
    option_locations: dict[str, tuple[str, str]],
) -> str:
    if not names:
        return ""
    links = []
    for name in names:
        if name not in option_locations:
            links.append(name)
            continue
        href = option_href(from_subsystem, from_filename, name, option_locations)
        links.append(f"[{name}]({href})")
    return f"[{', '.join(links)}]"


def clean_cell(value: str) -> str:
    if not value:
        return ""
    value = value.replace("\r", " ").replace("\n", " ")
    value = re.sub(r"\s+", " ", value).strip()
    value = value.replace("|", "\\|")
    # Prevent C++ validator snippets like "[](std::string …)" becoming markdown links.
    value = value.replace("[", "&#91;").replace("]", "&#93;")
    return value


def option_row(
    opt: dict,
    subsystem: str,
    filename: str,
    option_locations: dict[str, tuple[str, str]],
) -> str:
    name = opt["name"]
    typ = opt.get("type", "str")
    desc = clean_cell(opt.get("desc") or "")
    long_desc = clean_cell(opt.get("long_desc") or opt.get("long desc") or "")
    level = fmt_level(opt.get("level", "advanced"))
    default = fmt_default(opt.get("default"), typ)
    daemon_default = fmt_default(opt.get("daemon_default"), typ)
    min_val = fmt_default(opt.get("min"), typ) if opt.get("min") is not None else ""
    max_val = fmt_default(opt.get("max"), typ) if opt.get("max") is not None else ""
    enum_values = fmt_enum(opt.get("enum_values"))
    verbatim = clean_cell(str(opt.get("verbatim", "") or ""))
    see_also = fmt_see_also(
        opt.get("see_also") or [], subsystem, filename, option_locations
    )
    flags = fmt_flags(opt.get("flags"))
    services = fmt_services(opt.get("services"))
    validator = clean_cell(str(opt.get("validator") or ""))
    tags = fmt_tags(opt.get("tags"))

    if desc and not desc.startswith(" "):
        desc = f" {desc}"
    if long_desc and not long_desc.startswith(" "):
        long_desc = f" {long_desc}"

    cells = [
        f'<span id="SP_{name}">{name}</span>',
        desc,
        level,
        fmt_type(typ),
        default,
        daemon_default,
        min_val,
        max_val,
        enum_values,
        verbatim,
        see_also,
        flags,
        services,
        validator,
        long_desc,
        tags,
    ]
    return "| " + " | ".join(cells) + " |"


def write_markdown_files(
    all_options: dict[str, list[dict]],
    option_locations: dict[str, tuple[str, str]],
) -> None:
    for subsystem, options in all_options.items():
        target_dir = CONFIG / subsystem
        target_dir.mkdir(parents=True, exist_ok=True)

        groups: dict[str, list[dict]] = defaultdict(list)
        for opt in options:
            key = group_key(subsystem, opt["name"])
            groups[key].append(opt)

        keep_files = set()
        for key, opts in groups.items():
            filename = f"{key}.md"
            keep_files.add(filename)
            path = target_dir / filename
            rows = [
                option_row(opt, subsystem, filename, option_locations)
                for opt in sorted(opts, key=lambda o: o["name"])
            ]
            path.write_text(LEVEL_LEGEND + TABLE_HEADER + "\n".join(rows) + "\n", encoding="utf-8")

        for stale in target_dir.glob("*.md"):
            if stale.name in keep_files or stale.name in {"README.md", "INDEX.md"}:
                continue
            stale.unlink()
            print(f"  removed stale {stale.relative_to(ROOT)}")


def write_master_index(all_options: dict[str, list[dict]]) -> None:
    lines = ["[[_TOC_]]", ""]
    for subsystem in README_SECTION_ORDER:
        options = all_options.get(subsystem)
        if not options:
            continue
        lines.append(f"# {subsystem}")
        lines.append("")
        groups: dict[str, list[str]] = defaultdict(list)
        for opt in options:
            key = group_key(subsystem, opt["name"])
            filename = f"{key}.md"
            name = opt["name"]
            groups[key].append(
                f" - [{name}]({subsystem}/{filename}#SP_{name})"
            )
        for key in sorted(groups, key=lambda k: group_title(k).lower()):
            lines.append(f"## {group_title(key)}")
            lines.extend(sorted(groups[key]))
            lines.append("")
    (CONFIG / "readme.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_version_file(ref: str) -> None:
    content = (
        f"source: https://github.com/ceph/ceph\n"
        f"ref: {ref}\n"
        f"generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\n"
    )
    (ROOT / "VERSION").write_text(content, encoding="utf-8")


def run_split_index() -> None:
    script = ROOT / "scripts" / "split-index.py"
    subprocess.run([sys.executable, str(script)], check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", default="main", help="Ceph git ref (default: main)")
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=UPSTREAM,
        help="Directory for cached upstream YAML files",
    )
    parser.add_argument("--skip-split", action="store_true")
    args = parser.parse_args()

    all_options: dict[str, list[dict]] = {}
    option_locations: dict[str, tuple[str, str]] = {}

    print(f"Fetching Ceph option YAML (ref={args.ref}) …")
    for subsystem in SUBSYSTEMS:
        text = fetch_yaml(subsystem, args.ref, args.cache_dir)
        options = load_options(text)
        all_options[subsystem] = options
        for opt in options:
            key = group_key(subsystem, opt["name"])
            option_locations[opt["name"]] = (subsystem, f"{key}.md")
        print(f"  {subsystem}: {len(options)} options")

    print("Writing markdown tables …")
    write_markdown_files(all_options, option_locations)
    write_master_index(all_options)
    write_version_file(args.ref)

    if not args.skip_split:
        print("Splitting per-subsystem indexes …")
        run_split_index()

    total = sum(len(v) for v in all_options.values())
    print(f"Done — {total} options across {len(all_options)} subsystems.")


if __name__ == "__main__":
    main()
