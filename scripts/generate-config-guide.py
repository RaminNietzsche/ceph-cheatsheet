#!/usr/bin/env python3
"""Generate config deep-dive guides for Ceph subsystems (non-RGW)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from config_guide_lib import SubsystemProfile, generate_subsystem, slug_title

try:
    from subsystem_enrichments import SUBSYSTEM_ENRICHMENTS
except ImportError:
    SUBSYSTEM_ENRICHMENTS = {}

ROOT = Path(__file__).resolve().parent.parent


def _rules(*pairs: tuple[str, object]) -> callable:
    """Build group_for from (slug, predicate|string-prefix) pairs."""

    def group_for(name: str) -> str:
        for slug, pred in pairs:
            if callable(pred):
                if pred(name):
                    return slug
            elif isinstance(pred, str):
                if name.startswith(pred) or pred in name:
                    return slug
            elif isinstance(pred, tuple):
                if any(name.startswith(p) or p in name for p in pred):
                    return slug
        return pairs[-1][0] if pairs else "general"

    return group_for


def _stem(name: str, opt_source: str = "") -> str:
    return Path(opt_source).stem if opt_source else "general"


def _second_token(prefix: str):
    def inner(name: str) -> str:
        if not name.startswith(prefix):
            return "general"
        rest = name[len(prefix) :]
        return rest.split("_")[0] if "_" in rest else rest or "general"

    return inner


# --- OSD (158 options) ---

OSD_GROUP = _rules(
    ("scrub", lambda n: "scrub" in n),
    ("recovery", lambda n: any(x in n for x in ("backfill", "recovery", "recover"))),
    ("mclock", lambda n: "mclock" in n or "dmclock" in n),
    ("agent", lambda n: "agent" in n),
    ("classes", lambda n: "class" in n),
    ("crush", lambda n: "crush" in n),
    ("debug", lambda n: "debug" in n or "inject" in n),
    ("intervals", lambda n: any(x in n for x in ("interval", "sleep", "timeout", "period"))),
    ("limits", lambda n: any(x in n for x in ("max_", "min_", "cap", "limit"))),
    ("paths", lambda n: any(x in n for x in ("_path", "_dir", "_data"))),
    ("general", lambda n: True),
)

OSD_PROFILE = SubsystemProfile(
    id="osd",
    title="OSD",
    config_subdir="osd",
    guides_subdir="osd-config",
    group_for=OSD_GROUP,
    group_titles={
        "scrub": "Scrub",
        "recovery": "Recovery & backfill",
        "mclock": "mClock scheduler",
        "agent": "Cache agent",
        "classes": "Object classes",
        "crush": "CRUSH & weight",
        "debug": "Debug & injection",
        "intervals": "Intervals & throttling",
        "limits": "Limits & caps",
        "paths": "Paths & data dirs",
        "general": "General runtime",
    },
    nav_sections=[
        ("Recovery & backfill", "recovery", ["recovery"]),
        ("Scrub", "scrub", ["scrub"]),
        ("mClock scheduler", "mclock", ["mclock"]),
        ("Limits & intervals", "limits-intervals", ["limits", "intervals"]),
        ("Runtime & paths", "runtime", ["paths", "agent", "classes", "crush", "general"]),
        ("Debug", "debug", ["debug"]),
    ],
    section_slugs={
        "Recovery & backfill": "recovery",
        "Scrub": "scrub",
        "mClock scheduler": "mclock",
        "Limits & intervals": "limits-intervals",
        "Runtime & paths": "runtime",
        "Debug": "debug",
        "Other": "other",
    },
    nav_marker="osd-nav",
    restart_service="osd",
)

# --- MON (156 options) ---

MON_GROUP = _rules(
    ("backup", lambda n: "backup" in n),
    ("logging", lambda n: "log" in n),
    ("pg-pool", lambda n: any(x in n for x in ("scrub", "pg_", "pool"))),
    ("quorum-paxos", lambda n: any(x in n for x in ("paxos", "election", "quorum", "accept_timeout"))),
    ("auth", lambda n: "auth" in n or "cap" in n),
    ("osd-related", lambda n: n.startswith("osd_") or (n.startswith("mon_") and "osd" in n)),
    ("mgr-related", lambda n: n.startswith("mgr_") or "mgr" in n),
    ("mds-related", lambda n: n.startswith("mds_")),
    ("intervals", lambda n: any(x in n for x in ("interval", "timeout", "period", "delay"))),
    ("paths", lambda n: any(x in n for x in ("_path", "_dir", "_data", "_file"))),
    ("general", lambda n: True),
)

MON_PROFILE = SubsystemProfile(
    id="mon",
    title="MON",
    config_subdir="mon",
    guides_subdir="mon-config",
    group_for=MON_GROUP,
    group_titles={
        "backup": "Monitor backup",
        "logging": "Cluster logging",
        "pg-pool": "PG & pool health",
        "quorum-paxos": "Quorum & Paxos",
        "auth": "Auth & caps",
        "osd-related": "OSD-related settings",
        "mgr-related": "MGR-related settings",
        "mds-related": "MDS-related settings",
        "intervals": "Intervals & timeouts",
        "paths": "Paths & storage",
        "general": "General monitor",
    },
    nav_sections=[
        ("Quorum & Paxos", "quorum", ["quorum-paxos"]),
        ("PG & pool health", "pg-pool", ["pg-pool"]),
        ("Logging & backup", "logging", ["logging", "backup"]),
        ("Cross-daemon", "cross-daemon", ["osd-related", "mgr-related", "mds-related"]),
        ("Auth & runtime", "runtime", ["auth", "intervals", "paths", "general"]),
    ],
    section_slugs={
        "Quorum & Paxos": "quorum",
        "PG & pool health": "pg-pool",
        "Logging & backup": "logging",
        "Cross-daemon": "cross-daemon",
        "Auth & runtime": "runtime",
        "Other": "other",
    },
    nav_marker="mon-nav",
    restart_service="mon",
)

# --- MGR (52 options) ---

MGR_GROUP = _rules(
    ("mgr-modules", lambda n: n.startswith("mgr_") or n.startswith("cephadm_")),
    ("pg-pool", lambda n: any(x in n for x in ("pg_", "pool", "scrub"))),
    ("mds-related", lambda n: n.startswith("mds_")),
    ("intervals", lambda n: "interval" in n or "timeout" in n),
    ("paths", lambda n: "_path" in n or "_dir" in n),
    ("general", lambda n: True),
)

MGR_PROFILE = SubsystemProfile(
    id="mgr",
    title="MGR",
    config_subdir="mgr",
    guides_subdir="mgr-config",
    group_for=MGR_GROUP,
    group_titles={
        "mgr-modules": "Manager & cephadm modules",
        "pg-pool": "PG & pool settings",
        "mds-related": "MDS-related settings",
        "intervals": "Intervals",
        "paths": "Paths",
        "general": "General manager",
    },
    nav_sections=[
        ("Modules & cephadm", "modules", ["mgr-modules"]),
        ("Cluster settings", "cluster", ["pg-pool", "mds-related", "intervals", "paths", "general"]),
    ],
    section_slugs={
        "Modules & cephadm": "modules",
        "Cluster settings": "cluster",
        "Other": "other",
    },
    nav_marker="mgr-nav",
    restart_service="mgr",
)

# --- MDS (194 options) ---

MDS_GROUP = _rules(
    ("auth", lambda n: "auth" in n or "cap" in n),
    ("logging", lambda n: "log" in n),
    ("debug", lambda n: "debug" in n or "inject" in n),
    ("pg-pool", lambda n: "pg_" in n or "pool" in n),
    ("intervals", lambda n: "interval" in n or "timeout" in n),
    ("mds-core", lambda n: n.startswith("mds_")),
    ("general", lambda n: True),
)

MDS_PROFILE = SubsystemProfile(
    id="mds",
    title="MDS",
    config_subdir="mds",
    guides_subdir="mds-config",
    group_for=MDS_GROUP,
    group_titles={
        "auth": "Auth & capabilities",
        "logging": "Logging",
        "debug": "Debug",
        "pg-pool": "PG & pool",
        "intervals": "Intervals",
        "mds-core": "Metadata server core",
        "general": "General",
    },
    nav_sections=[
        ("Metadata server", "mds-core", ["mds-core"]),
        ("Auth & logging", "auth-logging", ["auth", "logging"]),
        ("Operations", "ops", ["intervals", "pg-pool", "debug", "general"]),
    ],
    section_slugs={
        "Metadata server": "mds-core",
        "Auth & logging": "auth-logging",
        "Operations": "ops",
        "Other": "other",
    },
    nav_marker="mds-nav",
    restart_service="mds",
)

# --- MDS client (70 options) ---

MDS_CLIENT_GROUP = _rules(
    ("client", "client_"),
    ("fuse", "fuse_"),
    ("debug", lambda n: "debug" in n),
    ("cache", lambda n: "cache" in n),
    ("general", lambda n: True),
)

MDS_CLIENT_PROFILE = SubsystemProfile(
    id="mds-client",
    title="MDS client",
    config_subdir="mds-client",
    guides_subdir="mds-client-config",
    group_for=MDS_CLIENT_GROUP,
    group_titles={
        "client": "CephFS client",
        "fuse": "FUSE client",
        "debug": "Debug",
        "cache": "Cache",
        "general": "General",
    },
    nav_sections=[
        ("Clients", "clients", ["client", "fuse"]),
        ("Other", "other", ["debug", "cache", "general"]),
    ],
    section_slugs={"Clients": "clients", "Other": "other"},
    nav_marker="mds-client-nav",
)

# --- RBD (97 options) ---

def _rbd_group(name: str) -> str:
    if not name.startswith("rbd_"):
        return "general"
    rest = name[4:]
    return rest.split("_")[0] if "_" in rest else "general"


RBD_PROFILE = SubsystemProfile(
    id="rbd",
    title="RBD",
    config_subdir="rbd",
    guides_subdir="rbd-config",
    group_for=_rbd_group,
    group_titles={
        "qos": "QoS & throttling",
        "cache": "Cache",
        "journal": "Journal",
        "mirroring": "Mirroring",
        "readahead": "Readahead",
        "default": "Defaults",
        "general": "General",
    },
    nav_sections=[
        ("Performance", "performance", ["qos", "cache", "readahead", "io"]),
        ("Mirroring & journal", "mirror", ["mirroring", "journal"]),
        ("Defaults & misc", "misc", ["default", "discard", "move", "persistent", "general"]),
    ],
    section_slugs={
        "Performance": "performance",
        "Mirroring & journal": "mirror",
        "Defaults & misc": "misc",
        "Other": "other",
    },
    nav_marker="rbd-nav",
)

# --- Global (852 options, group by source file) ---

GLOBAL_STORAGE = {
    "bluestore",
    "bluefs",
    "filestore",
    "memstore",
    "bdev",
    "objectstore",
    "rocksdb",
    "journal",
    "journaler",
    "erasure",
    "ec",
    "compressor",
    "qat",
    "uadk",
}
GLOBAL_AUTH = {"auth", "cephx", "keyring", "gss", "rotating", "key", "keyfile"}
GLOBAL_NETWORK = {"ms", "public", "heartbeat", "objecter", "osdc"}
GLOBAL_CLUSTER = {"mon", "mgr", "osd", "crush", "cluster", "monmap", "fsid", "ceph", "rados"}
GLOBAL_DEBUG = {"debug", "inject", "event", "log", "clog", "err", "perf", "lockdep"}
GLOBAL_RUNTIME = {
    "daemonize",
    "run",
    "chdir",
    "pid",
    "threadpool",
    "mempool",
    "throttler",
    "thp",
    "container",
    "service",
    "host",
    "device",
    "tmp",
    "fatal",
    "breakpad",
    "jaeger",
    "openssl",
    "plugin",
    "fio",
    "filer",
    "enable",
    "no",
    "admin",
    "setuser",
    "setgroup",
    "target",
    "restapi",
    "crash",
    "cephsqlite",
    "librados",
    "max",
}


def _global_group(name: str) -> str:
    # Resolved via source file in generate — override below
    return "general"


def global_group_from_source(source_file: str) -> str:
    stem = Path(source_file).stem
    return stem


def _make_global_profile() -> SubsystemProfile:
    profile = SubsystemProfile(
        id="global",
        title="Global",
        config_subdir="global",
        guides_subdir="global-config",
        group_for=lambda n: "general",
        nav_marker="global-nav",
    )

    def group_for(name: str) -> str:
        # name-only fallback; real grouping uses opt.source_file in generate_global
        return name.split("_")[0] if "_" in name else "general"

    profile.group_for = group_for
    return profile


GLOBAL_PROFILE = _make_global_profile()

GLOBAL_NAV = [
    ("Storage backends", "storage", sorted(GLOBAL_STORAGE)),
    ("Auth & keys", "auth", sorted(GLOBAL_AUTH)),
    ("Network & I/O", "network", sorted(GLOBAL_NETWORK)),
    ("Cluster maps", "cluster", sorted(GLOBAL_CLUSTER)),
    ("Logging & debug", "debug", sorted(GLOBAL_DEBUG)),
    ("Runtime & host", "runtime", sorted(GLOBAL_RUNTIME)),
]

# --- Smaller subsystems ---

RBD_MIRROR_PROFILE = SubsystemProfile(
    id="rbd-mirror",
    title="RBD mirror",
    config_subdir="rbd-mirror",
    guides_subdir="rbd-mirror-config",
    group_for=lambda n: "mirror",
    group_titles={"mirror": "RBD mirror"},
    nav_sections=[("RBD mirror", "topics", ["mirror"])],
    section_slugs={"RBD mirror": "topics"},
    nav_marker="rbd-mirror-nav",
)

CEPHFS_MIRROR_PROFILE = SubsystemProfile(
    id="cephfs-mirror",
    title="CephFS mirror",
    config_subdir="cephfs-mirror",
    guides_subdir="cephfs-mirror-config",
    group_for=lambda n: "mirror",
    group_titles={"mirror": "CephFS mirror"},
    nav_sections=[("CephFS mirror", "topics", ["mirror"])],
    section_slugs={"CephFS mirror": "topics"},
    nav_marker="cephfs-mirror-nav",
)

def _crimson_group(name: str) -> str:
    if name.startswith("seastore_"):
        return "seastore"
    return "crimson"


CRIMSON_PROFILE = SubsystemProfile(
    id="crimson",
    title="Crimson",
    config_subdir="crimson",
    guides_subdir="crimson-config",
    group_for=_crimson_group,
    group_titles={"crimson": "Crimson OSD", "seastore": "Seastore"},
    nav_sections=[("Crimson", "topics", ["crimson", "seastore"])],
    section_slugs={"Crimson": "topics"},
    nav_marker="crimson-nav",
    restart_service="osd",
)

IMMUTABLE_PROFILE = SubsystemProfile(
    id="immutable-object-cache",
    title="Immutable cache",
    config_subdir="immutable-object-cache",
    guides_subdir="immutable-cache-config",
    group_for=lambda n: "immutable",
    group_titles={"immutable": "Immutable object cache"},
    nav_sections=[("Immutable cache", "topics", ["immutable"])],
    section_slugs={"Immutable cache": "topics"},
    nav_marker="immutable-cache-nav",
)

CEPH_EXPORTER_PROFILE = SubsystemProfile(
    id="ceph-exporter",
    title="Ceph exporter",
    config_subdir="ceph-exporter",
    guides_subdir="ceph-exporter-config",
    group_for=lambda n: "exporter",
    group_titles={"exporter": "ceph-exporter"},
    nav_sections=[("Exporter", "topics", ["exporter"])],
    section_slugs={"Exporter": "topics"},
    nav_marker="ceph-exporter-nav",
    restart_service="ceph-exporter",
)


PROFILES: dict[str, SubsystemProfile] = {
    "osd": OSD_PROFILE,
    "mon": MON_PROFILE,
    "mgr": MGR_PROFILE,
    "mds": MDS_PROFILE,
    "mds-client": MDS_CLIENT_PROFILE,
    "rbd": RBD_PROFILE,
    "global": GLOBAL_PROFILE,
    "rbd-mirror": RBD_MIRROR_PROFILE,
    "cephfs-mirror": CEPHFS_MIRROR_PROFILE,
    "crimson": CRIMSON_PROFILE,
    "immutable-object-cache": IMMUTABLE_PROFILE,
    "ceph-exporter": CEPH_EXPORTER_PROFILE,
}

ALL_IDS = list(PROFILES.keys())


def generate_global(patch_nav: bool = True) -> int:
    from collections import defaultdict

    from config_guide_lib import (
        Option,
        generate_subsystem,
        parse_index_order,
        parse_table,
        slug_title,
    )

    profile = GLOBAL_PROFILE
    by_name: dict[str, Option] = {}
    for md in sorted(profile.config_dir.glob("*.md")):
        if md.name in ("INDEX.md", "README.md"):
            continue
        for opt in parse_table(md):
            by_name[opt.name] = opt

    index_order = parse_index_order(profile.config_dir)
    all_options: list[Option] = []
    for name, _href in index_order:
        if name in by_name:
            all_options.append(by_name[name])

    groups: dict[str, list[Option]] = defaultdict(list)
    for opt in all_options:
        groups[Path(opt.source_file).stem].append(opt)

    profile.group_titles = {stem: slug_title(stem) for stem in groups}
    assigned: set[str] = set()
    nav_sections: list[tuple[str, str, list[str]]] = []
    section_slugs: dict[str, str] = {}

    for section_title, section_dir, stems in GLOBAL_NAV:
        present = [s for s in stems if s in groups]
        if present:
            nav_sections.append((section_title, section_dir, present))
            section_slugs[section_title] = section_dir
            assigned.update(present)

    other = sorted(set(groups) - assigned)
    if other:
        nav_sections.append(("Other", "other", other))
        section_slugs["Other"] = "other"

    profile.nav_sections = nav_sections
    profile.section_slugs = section_slugs
    profile.group_for = lambda name: Path(by_name[name].source_file).stem if name in by_name else "general"

    # Reuse generate_subsystem body with pre-built groups
    profile.guides_dir.mkdir(parents=True, exist_ok=True)
    from config_guide_lib import (
        render_group,
        render_overview,
        render_tuning_index,
        topic_path,
        patch_mkdocs_nav,
    )

    (profile.guides_dir / "OVERVIEW.md").write_text(
        render_overview(profile, groups, len(all_options)), encoding="utf-8"
    )
    (profile.guides_dir / "TUNING.md").write_text(
        render_tuning_index(profile, all_options), encoding="utf-8"
    )
    for slug, options in sorted(groups.items()):
        path = topic_path(profile, slug)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_group(profile, slug, options), encoding="utf-8")

    keep = {topic_path(profile, slug) for slug in groups} | {
        profile.guides_dir / "OVERVIEW.md",
        profile.guides_dir / "TUNING.md",
    }
    for path in profile.guides_dir.rglob("*.md"):
        if path not in keep:
            path.unlink()
    for path in sorted(profile.guides_dir.iterdir(), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()

    if patch_nav:
        patch_mkdocs_nav(profile, groups, ROOT / "mkdocs.yml")

    print(f"global: {len(groups)} topics, {len(all_options)} options → guides/global-config/")
    return len(all_options)


def generate_rbd(patch_nav: bool = True) -> int:
    profile = RBD_PROFILE
    from config_guide_lib import parse_table

    stems: set[str] = set()
    for md in profile.config_dir.glob("*.md"):
        if md.name not in ("INDEX.md", "README.md"):
            for opt in parse_table(md):
                stems.add(_rbd_group(opt.name))

    titles = {s: profile.group_titles.get(s, slug_title(s)) for s in stems}
    profile.group_titles = titles
    all_slugs = sorted(stems)
    perf = [s for s in all_slugs if s in ("qos", "cache", "readahead", "io")]
    mirror = [s for s in all_slugs if s in ("mirroring", "journal")]
    misc = [s for s in all_slugs if s not in perf and s not in mirror]
    profile.nav_sections = [
        ("Performance", "performance", perf or all_slugs),
        ("Mirroring & journal", "mirror", mirror),
        ("Defaults & misc", "misc", misc),
    ]
    return generate_subsystem(profile, patch_nav=patch_nav)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "subsystems",
        nargs="*",
        choices=[*ALL_IDS, "all"],
        default=["all"],
        help=f"Subsystem id(s) or 'all' (default). Choices: {', '.join(ALL_IDS)}",
    )
    parser.add_argument("--no-nav", action="store_true", help="Do not patch mkdocs.yml")
    args = parser.parse_args()
    targets = ALL_IDS if not args.subsystems or args.subsystems == ["all"] else args.subsystems

    total = 0
    for sid in targets:
        profile = PROFILES[sid]
        profile.enrichments = SUBSYSTEM_ENRICHMENTS.get(sid, {})
        if sid == "global":
            total += generate_global(patch_nav=not args.no_nav)
        elif sid == "rbd":
            total += generate_rbd(patch_nav=not args.no_nav)
        else:
            total += generate_subsystem(PROFILES[sid], patch_nav=not args.no_nav)

    print(f"Done — {total} options across {len(targets)} subsystem(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
