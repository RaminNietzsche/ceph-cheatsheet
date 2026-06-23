#!/usr/bin/env python3
"""Generate RGW config deep-dive guide pages from config/rgw/*.md tables."""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_RGW = ROOT / "config" / "rgw"
GUIDES = ROOT / "guides" / "rgw-config"

HANDWRITTEN = {
    "d4n_writecache_enabled",
    "daos_pool",
    "dbstore_config_uri",
    "dbstore_db_dir",
    "dbstore_db_name_prefix",
    "rgw_account_default_quota_max_objects",
    "rgw_account_default_quota_max_size",
    "rgw_acl_grants_max_num",
    "rgw_admin_entry",
    "rgw_allow_notification_secrets_in_cleartext",
    "rgw_asio_assert_yielding",
    "rgw_backend_store",
    "rgw_barbican_url",
    "rgw_beast_enable_async",
    "rgw_bucket_counters_cache",
    "rgw_bucket_counters_cache_size",
    "rgw_bucket_default_quota_max_objects",
    "rgw_bucket_default_quota_max_size",
    "rgw_bucket_eexist_override",
    "rgw_bucket_index_max_aio",
}

GROUP_TITLES = {
    "motr-experimental": "Motr (experimental backend)",
    "lifecycle-counters": "RGW LC counters",
    "bucket-ops": "Bucket operations and index",
    "d4n-cache": "D4N / D3N cache",
    "metadata-cache": "RGW metadata cache",
    "encryption": "Encryption and KMS",
    "multisite-zones": "Multisite zones and realm",
    "multisite-sync": "Multisite sync",
    "resharding": "Dynamic resharding",
    "quotas": "Quota sync and defaults",
    "garbage-collection": "Garbage collection",
    "lifecycle": "Lifecycle (LC) workers",
    "dmclock": "dmclock scheduler",
    "keystone-sts": "Keystone and STS",
    "ldap": "LDAP authentication",
    "swift": "Swift API",
    "nfs": "NFS gateway",
    "notifications": "Bucket notifications",
    "lua": "Lua scripting",
    "http-curl": "HTTP / libcurl",
    "opa-authz": "OPA authorization",
    "rest-connections": "REST connections (multisite)",
    "posix-experimental": "POSIX backend (experimental)",
    "debug-inject": "Debug and fault injection",
    "admin-cors": "Admin CORS",
    "feature-toggles": "Feature toggles",
    "performance-tuning": "Performance and concurrency",
    "caches-and-ttl": "Caches and TTL",
    "timeouts-intervals": "Timeouts and intervals",
    "frontends-dns": "Frontends and DNS",
    "s3-api": "S3 API behavior",
    "usage-logging": "Usage logging",
    "ops-logging": "Ops logging",
    "logging": "Access and object logging",
    "torrent": "BitTorrent",
    "object-expiry": "Object expiry hints",
    "ratelimit": "Rate limiting",
    "scheduler": "Request scheduler",
    "multipart": "Multipart uploads",
    "copy-progress": "Copy progress",
    "object-io": "Object read/write I/O",
    "users-quotas": "Users and per-user settings",
    "limits-listing": "Limits and listing",
    "general": "General RGW options",
}

ROW_RE = re.compile(
    r'^\| <span id="SP_([^"]+)">([^<]+)</span> \|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|'
)
SEE_ALSO_RE = re.compile(r"\[\[([^\]]+)\]\(#SP_([^)]+)\)\]")
INDEX_LINK_RE = re.compile(r"^ - \[([^\]]+)\]\(([^)]+)\)")


@dataclass
class Option:
    name: str
    desc: str
    level: str
    typ: str
    default: str
    daemon_default: str
    min_val: str
    max_val: str
    valid_values: str
    flags: str
    long_desc: str
    see_also_raw: str
    source_file: str

    @property
    def effective_default(self) -> str:
        return self.daemon_default.strip() or self.default.strip() or "(empty)"

    @property
    def full_desc(self) -> str:
        parts = [self.desc.strip(), self.long_desc.strip()]
        return " ".join(p for p in parts if p)


def strip_badge(cell: str) -> str:
    m = re.search(r"badge-level-(\w+)", cell)
    if m:
        return m.group(1).capitalize()
    return cell.strip()


def parse_table(path: Path) -> list[Option]:
    opts: list[Option] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        name = m.group(2).strip()
        opts.append(
            Option(
                name=name,
                desc=m.group(3).strip(),
                level=strip_badge(m.group(4)),
                typ=m.group(5).strip(),
                default=m.group(6).strip(),
                daemon_default=m.group(7).strip(),
                min_val=m.group(8).strip(),
                max_val=m.group(9).strip(),
                valid_values=m.group(10).strip(),
                flags=m.group(13).strip(),
                long_desc=m.group(15).strip(),
                see_also_raw=m.group(11).strip(),
                source_file=path.name,
            )
        )
    return opts


def parse_index_order() -> list[tuple[str, str]]:
    order: list[tuple[str, str]] = []
    for line in (CONFIG_RGW / "INDEX.md").read_text(encoding="utf-8").splitlines():
        m = INDEX_LINK_RE.match(line)
        if m:
            order.append((m.group(1), m.group(2)))
    return order


def group_for(name: str) -> str:
    if name.startswith("motr_"):
        return "motr-experimental"
    if name.startswith("rgwlc_"):
        return "lifecycle-counters"
    if name.startswith("rgw_crypt"):
        return "encryption"
    if name.startswith("rgw_keystone") or name.startswith("rgw_sts"):
        return "keystone-sts"
    if name.startswith("rgw_ldap"):
        return "ldap"
    if name.startswith("rgw_swift"):
        return "swift"
    if name.startswith("rgw_nfs"):
        return "nfs"
    if name.startswith("rgw_lc_"):
        return "lifecycle"
    if name.startswith("rgw_gc_"):
        return "garbage-collection"
    if name.startswith("rgw_dmclock"):
        return "dmclock"
    if name.startswith("rgw_bucket_"):
        return "bucket-ops"
    if name.startswith(("rgw_d4n", "rgw_d3n")) or name.startswith("d4n_"):
        return "d4n-cache"
    if name.startswith("rgw_cache"):
        return "metadata-cache"
    if name.startswith(("rgw_zone", "rgw_realm", "rgw_region", "rgw_period")):
        return "multisite-zones"
    if any(
        x in name
        for x in (
            "_sync_",
            "rgw_sync",
            "rgw_meta_sync",
            "rgw_data_sync",
            "rgw_bucket_sync",
            "rgw_run_sync",
            "rgw_data_log",
            "rgw_md_log",
            "rgw_data_notify",
            "rgw_md_notify",
        )
    ):
        return "multisite-sync"
    if name.startswith("rgw_reshard") or name.startswith("rgw_dynamic_reshard"):
        return "resharding"
    if "quota" in name:
        return "quotas"
    if name.startswith("rgw_posix"):
        return "posix-experimental"
    if any(x in name for x in ("kafka", "notif", "topic_persist")):
        return "notifications"
    if name.startswith("rgw_lua"):
        return "lua"
    if name.startswith("rgw_curl"):
        return "http-curl"
    if name.startswith("rgw_opa"):
        return "opa-authz"
    if name.startswith("rgw_rest_"):
        return "rest-connections"
    if "inject" in name or (name.startswith("rgw_debug") and "debug" in name):
        return "debug-inject"
    if name.startswith("rgw_gcors"):
        return "admin-cors"
    if name.startswith("rgw_enable_") or name.startswith("rgw_disable_"):
        return "feature-toggles"
    if any(
        x in name
        for x in (
            "max_aio",
            "concurrent",
            "thread",
            "async_rados",
            "spawn_window",
            "batch",
            "chunk",
            "connection_pool",
            "num_control",
            "max_worker",
            "max_objs",
            "processor",
            "stripe",
            "readahead",
            "inflight",
        )
    ):
        return "performance-tuning"
    if any(x in name for x in ("cache", "ttl", "lru")) and "crypt" not in name:
        return "caches-and-ttl"
    if any(
        x in name
        for x in ("timeout", "interval", "period", "delay", "wait", "sleep", "tick")
    ):
        return "timeouts-intervals"
    if name.startswith(("rgw_frontends", "rgw_frontend", "rgw_dns")):
        return "frontends-dns"
    if name.startswith("rgw_s3_"):
        return "s3-api"
    if name.startswith("rgw_usage"):
        return "usage-logging"
    if name.startswith("rgw_ops_log"):
        return "ops-logging"
    if name.startswith("rgw_log_"):
        return "logging"
    if name.startswith("rgw_torrent"):
        return "torrent"
    if name.startswith("rgw_objexp"):
        return "object-expiry"
    if name.startswith("rgw_ratelimit"):
        return "ratelimit"
    if name.startswith("rgw_scheduler"):
        return "scheduler"
    if name.startswith("rgw_multipart"):
        return "multipart"
    if name.startswith("rgw_copy_obj"):
        return "copy-progress"
    if name.startswith(("rgw_get_obj", "rgw_put_obj")):
        return "object-io"
    if name.startswith("rgw_user_"):
        return "users-quotas"
    if name.startswith(("rgw_max_", "rgw_list_", "rgw_delete_", "rgw_multi_obj")):
        return "limits-listing"
    return "general"


def when_to_use(opt: Option) -> str:
    name, level, typ = opt.name, opt.level, opt.typ
    if level == "Dev" or "inject" in name or "debug" in name:
        return "Development, testing, or upstream debugging only — not for production tuning."
    if name.startswith("motr_") or name.startswith("rgw_posix"):
        return "Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments."
    if typ == "Bool" and opt.effective_default.lower() in ("true", "false"):
        default = opt.effective_default.lower()
        if default == "true":
            return "Enabled by default; disable only when troubleshooting the related feature."
        return "Disabled by default; enable when you need the related feature and accept its trade-offs."
    if "_url" in name or "_uri" in name or name.endswith("_addr"):
        return "Set when integrating with an external service; leave empty if the feature is unused."
    if "quota" in name and "max" in name:
        return "Set tenant or platform default limits for new users, accounts, or buckets."
    if "max_" in name or "limit" in name:
        return "Adjust when clients hit request-size or concurrency limits, or to protect cluster resources."
    if "cache" in name or "ttl" in name:
        return "Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure."
    if "sync" in name or "multisite" in opt.full_desc.lower():
        return "Multisite replication and sync tuning — adjust when lag or sync load is problematic."
    if level == "Basic":
        return "Core RGW behavior — review before changing in production."
    return "Advanced tuning — change from upstream default only with a measured workload and rollback plan."


def related_options(opt: Option) -> list[str]:
    refs: list[str] = []
    for m in SEE_ALSO_RE.finditer(opt.see_also_raw):
        refs.append(m.group(2))
    return refs


def optimal_value(opt: Option) -> str:
    name, typ, level = opt.name, opt.typ, opt.level
    default = opt.effective_default
    bounds = ""
    if opt.min_val or opt.max_val:
        bounds = f" Valid range: min={opt.min_val or '—'}, max={opt.max_val or '—'}."

    if level == "Dev" or "inject" in name or ("debug" in name and "interval" in name):
        return (
            f"Keep the upstream default (`{default}`) in production. "
            "Enable or change only during targeted debugging sessions."
        )

    if any(x in name for x in ("password", "secret", "token", "key", "client_id")):
        return (
            "Not a performance knob — use credentials from your identity/KMS provider. "
            "Rotate via secrets management; never commit values to config repos."
        )

    if name.endswith("_url") or name.endswith("_uri") or name.endswith("_addr"):
        return (
            "Use the nearest stable endpoint reachable from every RGW node. "
            "Verify with curl from each host; measure p99 latency of dependent operations "
            f"and keep the default (`{default}`) if the integration is unused."
        )

    if name.endswith("_path") or name.endswith("_dir") or name.endswith("_file"):
        return (
            "Place on fast, dedicated storage with sufficient free space. "
            f"Default (`{default}`) is fine when that path is on a separate volume."
        )

    if "quota" in name and ("max_" in name or "default" in name):
        return (
            "Derive from product tiers and cluster capacity (leave 20–30% headroom). "
            f"`-1` means unlimited. Verify with test users via `radosgw-admin quota get`."
        )

    if "quota" in name and ("ttl" in name or "cache" in name or "sync" in name):
        return (
            "Balance quota enforcement freshness vs RGW/CLS load. "
            f"Start at default (`{default}`); shorten if users exceed limits before stats catch up, "
            "lengthen if quota sync dominates CPU."
        )

    if "max_aio" in name or "concurrent" in name or "spawn_window" in name:
        return (
            "Performance sweep: baseline at default, then increase in steps while watching "
            "RGW CPU, request p99, and OSD slow ops. "
            f"Optimal is the highest value before OSD or network saturation.{bounds} "
            f"Default: `{default}`."
        )

    if "cache" in name and typ in ("Int", "Uint"):
        return (
            f"Size to active working set (accounts, buckets, or keys you monitor). "
            f"Sweep around default (`{default}`) while watching RGW RSS.{bounds}"
        )

    if "cache" in name and typ == "Bool":
        return (
            f"Enable only when the related metrics or correctness path needs it. "
            f"Default (`{default}`) is usually optimal for standard deployments."
        )

    if "ttl" in name or "interval" in name or "period" in name or name.endswith("_roll_time"):
        return (
            f"Lower for fresher behavior / faster reaction; higher to reduce background load. "
            f"Adjust from default (`{default}`) only when logs show sync, cache, or timeout issues.{bounds}"
        )

    if "timeout" in name or name.endswith("_wait_time"):
        return (
            f"Increase if clients see timeouts under load; decrease to fail fast. "
            f"Default (`{default}`) matches typical LAN latency.{bounds}"
        )

    if typ == "Bool":
        if "require" in name or "verify" in name or "ssl" in name or "enforce" in name:
            return f"Security/compliance setting — prefer `true` in production unless a trusted lab requires `{default}`."
        if "enable" in name or "enabled" in name:
            return (
                f"Enable when the feature is required; otherwise keep default (`{default}`) "
                "to minimize background threads and memory."
            )
        return (
            f"Policy choice aligned with client API expectations. "
            f"Test with your S3/Swift clients; default (`{default}`) matches upstream."
        )

    if opt.valid_values:
        return (
            f"Choose from valid values {opt.valid_values}. "
            f"Default `{default}` is optimal unless your backend or integration requires another value."
        )

    if typ in ("Int", "Uint") and ("max_" in name or "num" in name or "size" in name):
        return (
            f"Raise only when clients hit documented limits; lower to protect RGW/OSD. "
            f"Default (`{default}`) matches S3 compatibility for most workloads.{bounds}"
        )

    if name.startswith("rgw_dmclock"):
        return (
            "Tune reservation/limit/weight together per queue (admin, auth, data, metadata). "
            f"Use `ceph daemon rgw.<id> perf dump` and dmclock stats; start from defaults (`{default}`)."
        )

    if name.startswith("rgw_zone") or name.startswith("rgw_realm"):
        return (
            "Set by `radosgw-admin realm/zone` workflows — not hand-tuned numerically. "
            f"Must match multisite period configuration; default OID/name: `{default}`."
        )

    return (
        f"Start from upstream default (`{default}`). "
        "Change one option at a time under representative load; "
        "use `ceph config get client.rgw` and RGW perf counters to validate."
    )


def format_see_also(opt: Option) -> str:
    refs = related_options(opt)
    if not refs:
        return ""
    lines = ["**Related options:**", ""]
    for ref in refs:
        lines.append(f"- [`{ref}`](../../config/rgw/{opt.source_file}#SP_{ref})")
    lines.append("")
    return "\n".join(lines)


def format_example(opt: Option) -> str:
    if opt.flags and "STARTUP" in opt.flags:
        restart = "\nceph orch restart rgw"
    else:
        restart = ""
    val = opt.effective_default
    if val in ("(empty)", ""):
        val = "<value>"
    elif opt.typ == "Str" and not val.startswith('"'):
        val = f'"{val}"' if " " in val or "/" in val else val
    return (
        f"```bash\n"
        f"ceph config set client.rgw {opt.name} {val}\n"
        f"ceph config get client.rgw {opt.name}{restart}\n"
        f"```"
    )


def render_option(opt: Option) -> str:
    startup = " · **STARTUP** (restart required)" if opt.flags and "STARTUP" in opt.flags else ""
    table_link = f"../../config/rgw/{opt.source_file}#SP_{opt.name}"
    parts = [
        f"### {opt.name}",
        "",
        "| | |",
        "|---|---|",
        f"| Type | {opt.typ} · default `{opt.effective_default}` · **{opt.level}**{startup} |",
        f"| Table | [{opt.source_file}#SP_{opt.name}]({table_link}) |",
        "",
    ]
    if opt.full_desc:
        parts.extend([f"**What it does:** {opt.full_desc}", ""])
    parts.extend([f"**When to use:** {when_to_use(opt)}", ""])
    see = format_see_also(opt)
    if see:
        parts.append(see)
    parts.extend(["**Example:**", "", format_example(opt), ""])
    parts.extend([f"**Finding optimal value:** {optimal_value(opt)}", "", "---", ""])
    return "\n".join(parts)


def render_group(slug: str, options: list[Option]) -> str:
    title = GROUP_TITLES.get(slug, slug.replace("-", " ").title())
    lines = [
        f"# {title}",
        "",
        f"RGW config deep dive — {len(options)} options. "
        f"[← RGW config overview](OVERVIEW.md) · "
        f"[Handwritten batch](../rgw-config-options.md) · "
        f"[INDEX](../../config/rgw/INDEX.md)",
        "",
        "| Option | Default | Level |",
        "|--------|---------|-------|",
    ]
    for opt in options:
        lines.append(
            f"| [{opt.name}](#{opt.name}) | `{opt.effective_default}` | {opt.level} |"
        )
    lines.extend(["", "---", ""])
    for opt in options:
        lines.append(render_option(opt))
    lines.extend(["", "[← RGW config overview](OVERVIEW.md)", ""])
    return "\n".join(lines)


def render_overview(groups: dict[str, list[Option]], total: int) -> str:
    lines = [
        "# RGW Config Deep Dive — All Options",
        "",
        f"Extended reference for **{total}** RADOS Gateway options "
        f"(plus [19 handwritten options](../rgw-config-options.md) with extra examples). "
        "Generated from [config/rgw/INDEX.md](../../config/rgw/INDEX.md).",
        "",
        "```bash",
        "./scripts/lookup-config.sh <option-name>",
        "```",
        "",
        "## Topics",
        "",
        "| Topic | Options |",
        "|-------|---------|",
    ]
    for slug in sorted(groups, key=lambda s: GROUP_TITLES.get(s, s)):
        title = GROUP_TITLES.get(slug, slug)
        lines.append(f"| [{title}]({slug}.md) | {len(groups[slug])} |")
    lines.extend(
        [
            "",
            "## Tuning models",
            "",
            "| Model | How to choose |",
            "|-------|---------------|",
            "| **Policy** | Security, API compatibility, compliance |",
            "| **Capacity** | Disk, tenant plans, cluster headroom |",
            "| **Performance** | Baseline → incremental change → monitor OSD/RGW |",
            "",
            "[← Guides overview](../OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md)",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    by_name: dict[str, Option] = {}
    for md in sorted(CONFIG_RGW.glob("*.md")):
        if md.name in ("INDEX.md", "README.md"):
            continue
        for opt in parse_table(md):
            by_name[opt.name] = opt

    index_order = parse_index_order()
    remaining: list[Option] = []
    for name, _href in index_order:
        if name in HANDWRITTEN:
            continue
        if name not in by_name:
            print(f"warning: {name} in INDEX but not parsed", file=sys.stderr)
            continue
        remaining.append(by_name[name])

    groups: dict[str, list[Option]] = defaultdict(list)
    for opt in remaining:
        groups[group_for(opt.name)].append(opt)

    GUIDES.mkdir(parents=True, exist_ok=True)
    (GUIDES / "OVERVIEW.md").write_text(
        render_overview(groups, len(remaining)), encoding="utf-8"
    )
    for slug, options in sorted(groups.items()):
        (GUIDES / f"{slug}.md").write_text(
            render_group(slug, options), encoding="utf-8"
        )

    print(f"Wrote {len(groups)} topic files + OVERVIEW ({len(remaining)} options)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
