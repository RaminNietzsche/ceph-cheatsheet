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
BATCH1_GUIDE = ROOT / "guides" / "rgw-config-options.md"

# Curated batch-1 guide — same options also appear in topic files with identical tuning format.
BATCH1_NAMES = {
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
    "experimental-backends": "Experimental backends",
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
    if name in (
        "daos_pool",
        "dbstore_config_uri",
        "dbstore_db_dir",
        "dbstore_db_name_prefix",
        "rgw_backend_store",
        "rgw_config_store",
    ):
        return "experimental-backends"
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


def tuning_model(opt: Option) -> str:
    name, typ, level = opt.name, opt.typ, opt.level

    if name.endswith("_tracing_enabled") or (
        level == "Dev"
        and "counters_cache" not in name
        and not any(
            x in name
            for x in ("spawn_window", "beast_enable_async", "objexp_chunk", "roll_time")
        )
        and ("inject" in name or "debug" in name or name.startswith("rgw_debug") or "instrumentation" in name or "asio_assert" in name or "op_thread" in name)
    ):
        return "Dev"
    if name in ("rgw_backend_store",) or name.startswith(("motr_", "rgw_posix")):
        return "Architecture"
    if name in ("daos_pool",) or name.endswith(("_path", "_dir", "_file", "_base_path")):
        return "Capacity"
    if name.endswith("_config_uri") or (name.endswith("_uri") and "file:" in opt.effective_default):
        return "Capacity"
    if name.endswith(("_url", "_uri", "_addr")) or name in ("rgw_barbican_url", "rgw_keystone_url"):
        return "Connectivity"
    if any(
        x in name
        for x in ("password", "secret", "token", "client_id", "client_secret", "binddn")
    ) and typ == "Str" and "cache" not in name and "template" not in name:
        return "Policy"
    if name in ("rgw_admin_entry", "rgw_sts_entry", "rgw_swift_auth_entry") or (
        typ == "Bool" and any(x in name for x in ("enforce", "override", "compat", "relaxed"))
    ):
        return "Policy"
    if "quota" in name and ("max" in name or "default" in name):
        return "Policy"
    if name.startswith("rgw_dmclock"):
        return "Performance"
    if any(
        x in name
        for x in (
            "max_aio",
            "concurrent",
            "spawn_window",
            "thread_pool",
            "async_rados",
            "readahead",
            "chunk_size",
            "stripe_size",
            "window_size",
            "inflight",
            "batch_size",
            "max_worker",
            "connection_pool",
        )
    ):
        return "Performance"
    if ("cache" in name or "ttl" in name or "lru" in name) and "crypt" not in name:
        return "Performance"
    if any(
        x in name
        for x in ("interval", "period", "timeout", "delay", "wait", "sleep", "tick", "roll_time")
    ):
        return "Performance"
    if name.startswith(("rgw_zone", "rgw_realm", "rgw_region", "rgw_period")):
        return "Architecture"
    if typ == "Bool" and any(x in name for x in ("require", "verify", "ssl", "enable", "enabled")):
        return "Policy"
    if typ == "Bool":
        return "Policy"
    if opt.valid_values:
        return "Architecture"
    if typ in ("Int", "Uint", "Size") and ("max_" in name or "num" in name or "limit" in name):
        return "Policy"
    return "Performance"


def tuning_quick_answer(opt: Option) -> str:
    model = tuning_model(opt)
    default = opt.effective_default
    name = opt.name

    if model == "Dev":
        return f"Keep `{default}` in production"
    if model == "Architecture":
        if name == "rgw_backend_store":
            return "`rados` in production"
        return "Match deployment topology; use upstream default"
    if model == "Connectivity":
        return "Nearest stable endpoint from every RGW node"
    if model == "Capacity":
        return "Dedicated fast disk with growth headroom"
    if model == "Policy" and "quota" in name and "max" in name:
        return "Cluster capacity ÷ tenant plan; verify with test users"
    if model == "Policy":
        return f"Upstream default (`{default}`) unless client/compliance requires change"
    if "max_aio" in name or "concurrent" in name:
        return "Sweep up until OSD slow ops rise"
    if "cache" in name and opt.typ in ("Int", "Uint"):
        return "Size ≈ active working set; watch RGW memory"
    if "ttl" in name or "interval" in name:
        return "Balance freshness vs background load"
    return "Baseline → adjust → validate under real workload"


def _bounds_note(opt: Option) -> str:
    if opt.min_val or opt.max_val:
        return (
            f"\n\n**Bounds:** min `{opt.min_val or '—'}`, max `{opt.max_val or '—'}`."
        )
    return ""


def _monitor_commands(opt: Option, *extra: str) -> str:
    lines = [
        "",
        "```bash",
        f"ceph config get client.rgw {opt.name}",
        "ceph daemon rgw.<id> perf dump | jq '.rgw' | head",
        "radosgw-admin perf stats",
        "ceph -s  # cluster health, slow ops",
    ]
    lines.extend(extra)
    lines.append("```")
    return "\n".join(lines)


def render_finding_optimal_value(opt: Option) -> str:
    name, typ, level = opt.name, opt.typ, opt.level
    default = opt.effective_default
    model = tuning_model(opt)
    lines = [f"**Tuning model:** {model}", ""]

    if model == "Dev":
        lines.extend(
            [
                f"1. Keep the upstream default (`{default}`) on every production RGW.",
                "2. Enable or change only in a lab while reproducing a specific bug.",
                "3. Revert before returning the node to the production pool.",
                "",
                "**Signals:** assertion failures, injected errors, or trace noise in logs.",
            ]
        )
        return "\n".join(lines)

    if model == "Architecture":
        if name == "rgw_backend_store":
            lines.extend(
                [
                    "1. Production Ceph clusters: `rados` (default).",
                    "2. Other values (`dbstore`, `daos`, `motr`, `posix`) are experimental PoC only.",
                    "3. Changing backend requires migration — not an in-place performance tune.",
                ]
            )
        elif name.startswith(("rgw_zone", "rgw_realm", "rgw_region")):
            lines.extend(
                [
                    "1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.",
                    f"2. Value must match the active period object (`{default}` is the default OID/name).",
                    "3. Multisite: keep consistent across all zones in the same realm.",
                    "",
                    "```bash",
                    "radosgw-admin realm list",
                    "radosgw-admin zone get --rgw-zone=<zone>",
                    "```",
                ]
            )
        elif opt.valid_values:
            lines.extend(
                [
                    f"1. Valid values: {opt.valid_values}.",
                    f"2. Default `{default}` matches standard Ceph packaging.",
                    "3. Change only when your integration or backend explicitly requires another value.",
                ]
            )
        else:
            lines.extend(
                [
                    f"1. Treat as deployment metadata, not a throughput knob.",
                    f"2. Keep `{default}` unless documentation for your topology says otherwise.",
                    "3. Document the chosen value in runbooks — changing it can break multisite or auth.",
                ]
            )
        return "\n".join(lines) + _bounds_note(opt)

    if model == "Connectivity":
        lines.extend(
            [
                f"1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).",
                "2. From **each** RGW node: `curl -k <url>` or vendor health check.",
                "3. Pick the lowest-latency endpoint that stays healthy over 24h.",
                "4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).",
                f"5. Leave empty (`{default}`) if the integration is disabled.",
                _monitor_commands(opt),
            ]
        )
        return "\n".join(lines)

    if model == "Capacity":
        lines.extend(
            [
                "1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.",
                "2. Size for metadata growth + 30% free space (`df -h`, `iowait`).",
                f"3. Default path (`{default}`) is fine when it already sits on fast storage.",
                "4. dbstore/POSIX: all RGW instances sharing data must see the same path.",
                "",
                "```bash",
                "df -h $(ceph config get client.rgw " + name + ")",
                "iostat -x 5  # disk saturation",
                "```",
            ]
        )
        return "\n".join(lines)

    if model == "Policy":
        if "quota" in name and ("max" in name or "default" in name):
            lines.extend(
                [
                    "1. `ceph df detail` — usable cluster capacity.",
                    "2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.",
                    f"3. Set limit; `-1` means unlimited. Default: `{default}`.",
                    "4. Create a test user/account and confirm via `radosgw-admin quota get`.",
                    "5. Existing users/accounts are **not** retroactively changed.",
                    "",
                    "```bash",
                    "ceph df detail",
                    "radosgw-admin quota get --uid=testuser",
                    "radosgw-admin bucket stats --bucket=testbucket",
                    "```",
                ]
            )
        elif any(x in name for x in ("password", "secret", "token", "key")):
            lines.extend(
                [
                    "1. Not tuned numerically — supply from your secrets manager.",
                    "2. Rotate on schedule; never store in git or plain `ceph.conf`.",
                    "3. Use `ceph config set` at runtime or cephadm secrets where supported.",
                ]
            )
        elif typ == "Bool" and any(x in name for x in ("require", "verify", "ssl", "cleartext")):
            lines.extend(
                [
                    f"1. Production: prefer secure default (`{default}` for most security options).",
                    "2. Relax only on trusted private networks with documented risk acceptance.",
                    "3. Test client behavior (HTTPS redirects, presigned URLs) after changes.",
                ]
            )
        elif typ == "Bool":
            lines.extend(
                [
                    f"1. Default `{default}` matches upstream/AWS-compatible behavior.",
                    "2. Test with your S3/Swift SDKs and automation before changing.",
                    "3. Optimal = contract your clients expect, not maximum throughput.",
                ]
            )
        elif "max_" in name or "num" in name:
            lines.extend(
                [
                    f"1. Start at `{default}` (S3/AWS-aligned for most limits).",
                    "2. Raise only when clients return explicit limit errors in RGW logs.",
                    "3. Lower to harden against oversized requests or DoS.",
                ]
            )
        else:
            lines.extend(
                [
                    f"1. Upstream default (`{default}`) is the compatibility baseline.",
                    "2. Change only for documented client or compliance requirements.",
                    "3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.",
                ]
            )
        return "\n".join(lines) + _bounds_note(opt)

    # Performance (default for numeric tuning)
    if "max_aio" in name:
        workload = (
            "large bucket LIST, bulk DELETE, multipart completion"
            if "bucket" in name or "multi_obj" in name
            else "the workload that triggers RADOS aio on this path"
        )
        lines.extend(
            [
                f"1. Baseline at `{default}` with {workload}.",
                "2. Watch list/delete p99, RGW CPU, and OSD slow ops.",
                "3. Increase in steps (~25%: e.g. 128 → 160 → 192 → 256) until latency stops improving.",
                "4. **Decrease** under recovery pressure, `nearfull`, or sustained bucket-index pool load.",
                "",
                "**Signals:** OSD `slow requests`, rising `rgw` throttle counters, flat client throughput.",
                _monitor_commands(
                    opt,
                    "radosgw-admin bucket stats --bucket=BIG_BUCKET | jq '.num_shards'",
                ),
            ]
        )
    elif "concurrent" in name or "thread_pool" in name or "async_rados" in name:
        lines.extend(
            [
                f"1. Baseline at `{default}` under peak concurrent clients.",
                "2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.",
                "3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.",
                "4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.",
                "",
                "**Signals:** 503/slowdown responses, high `active_requests` vs `max_concurrent`.",
                _monitor_commands(opt),
            ]
        )
    elif "spawn_window" in name:
        lines.extend(
            [
                f"1. Default `{default}` limits parallel sync coroutines per bucket/zone.",
                "2. **Increase** when multisite lag grows and RGW CPU headroom exists.",
                "3. **Decrease** if sync threads starve client-facing requests or OSDs spike.",
                "",
                "**Signals:** `radosgw-admin sync status`, data/meta sync lag, RGW load average.",
                _monitor_commands(opt, "radosgw-admin sync status"),
            ]
        )
    elif "cache" in name and typ in ("Int", "Uint"):
        lines.extend(
            [
                f"1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.",
                f"2. Start at `{default}`; sweep upward in ~2× steps.",
                "3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.",
                "",
                "**Signals:** rising RGW memory, repeated metadata lookups in logs.",
                _monitor_commands(opt),
            ]
        )
    elif "cache" in name and typ == "Bool":
        lines.extend(
            [
                f"1. Default `{default}` — enable only when you consume the related per-label metrics.",
                "2. If enabling, set the paired `*_cache_size` to match monitored entities.",
                "3. Disable if memory is constrained and metrics are unused.",
            ]
        )
    elif "ttl" in name or "interval" in name or "period" in name or name.endswith("_roll_time"):
        lines.extend(
            [
                f"1. Default `{default}` balances freshness vs background CPU/network.",
                "2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.",
                "3. **Lengthen** if background sync/GC/LC dominates RGW CPU.",
                "",
                "**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.",
                _monitor_commands(opt),
            ]
        )
    elif "timeout" in name or name.endswith("_wait_time"):
        lines.extend(
            [
                f"1. Default `{default}` suits LAN RTT; WAN needs higher values.",
                "2. **Increase** when logs show client/broker timeouts under load.",
                "3. **Decrease** to fail fast and trigger retries upstream.",
                "",
                "**Signals:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.",
                _monitor_commands(opt),
            ]
        )
    elif name.startswith("rgw_dmclock"):
        lines.extend(
            [
                f"1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.",
                f"2. Start from defaults (`{default}`); identify saturated queue (admin/auth/data/metadata).",
                "3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.",
                "",
                "**Signals:** dmclock perf counters, queue delay histograms, admin API slowdown.",
                _monitor_commands(opt, "ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test(\"dmclock\"))'"),
            ]
        )
    elif "chunk" in name or "stripe" in name or "window" in name:
        lines.extend(
            [
                f"1. Baseline `{default}` with your object size distribution (small vs large objects).",
                "2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.",
                "3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.",
                "",
                "**Signals:** PUT/GET p99 by object size, RADOS op count per MB transferred.",
                _monitor_commands(opt),
            ]
        )
    else:
        lines.extend(
            [
                f"1. Baseline at upstream default `{default}`.",
                "2. Change **one** option per test window under representative load.",
                "3. Compare p50/p99 latency and throughput before/after.",
                "4. Roll back if OSD slow ops, recovery backlog, or error rate increases.",
                "",
                "**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.",
                _monitor_commands(opt),
            ]
        )

    return "\n".join(lines) + _bounds_note(opt)


def when_to_use_bullets(opt: Option) -> str | None:
    name = opt.name
    if "max_aio" in name:
        return (
            "- **Increase** when listings/deletes on sharded buckets are slow and OSDs have headroom.\n"
            "- **Decrease** when bucket-index pools show sustained load spikes or slow ops."
        )
    if "concurrent" in name or name == "rgw_thread_pool_size":
        return (
            "- **Increase** when RGW queues requests but CPU is not saturated.\n"
            "- **Decrease** when latency spikes or CPU context-switch overhead grows."
        )
    if "spawn_window" in name:
        return (
            "- **Increase** when multisite replication lag grows.\n"
            "- **Decrease** when sync load competes with client I/O."
        )
    if "cache" in name and opt.typ in ("Int", "Uint"):
        return (
            "- **Increase** when monitoring many active buckets/users and cache misses are visible.\n"
            "- **Decrease** when RGW memory is constrained."
        )
    if "ttl" in name or "interval" in name:
        return (
            "- **Shorten** for fresher stats or faster enforcement.\n"
            "- **Lengthen** to reduce background sync or GC cost."
        )
    return None


def optimal_value(opt: Option) -> str:
    return render_finding_optimal_value(opt)


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
    bullets = when_to_use_bullets(opt)
    if bullets:
        parts.extend(["**When to use:**", "", bullets, ""])
    else:
        parts.extend([f"**When to use:** {when_to_use(opt)}", ""])
    see = format_see_also(opt)
    if see:
        parts.append(see)
    parts.extend(["**Example:**", "", format_example(opt), ""])
    parts.extend(["**Finding optimal value:**", "", render_finding_optimal_value(opt), "", "---", ""])
    return "\n".join(parts)


def tuning_intro() -> str:
    return "\n".join(
        [
            "## Finding optimal values",
            "",
            "| Model | How to choose |",
            "|-------|---------------|",
            "| **Policy** | Security, API compatibility, tenant limits |",
            "| **Capacity** | Disk layout, paths, pool sizing |",
            "| **Performance** | Baseline → incremental change → monitor OSD/RGW |",
            "| **Connectivity** | Nearest stable external endpoint |",
            "| **Architecture** | Backend, multisite topology — not numeric sweeps |",
            "| **Dev** | Keep upstream default in production |",
            "",
            "**Shared tooling:**",
            "",
            "```bash",
            "ceph config get client.rgw <option>",
            "ceph daemon rgw.<id> perf dump | jq '.rgw' | head",
            "radosgw-admin perf stats",
            "ceph osd pool stats",
            "```",
            "",
            "---",
            "",
        ]
    )


def render_group(slug: str, options: list[Option]) -> str:
    title = GROUP_TITLES.get(slug, slug.replace("-", " ").title())
    batch_note = (
        " · [Curated batch 1](../rgw-config-options.md)"
        if any(o.name in BATCH1_NAMES for o in options)
        else ""
    )
    lines = [
        f"# {title}",
        "",
        f"RGW config deep dive — {len(options)} options. "
        f"[← RGW config overview](OVERVIEW.md){batch_note} · "
        f"[Tuning index](TUNING.md) · "
        f"[INDEX](../../config/rgw/INDEX.md)",
        "",
        "| Option | Default | Level | Tuning |",
        "|--------|---------|-------|--------|",
    ]
    for opt in options:
        lines.append(
            f"| [{opt.name}](#{opt.name}) | `{opt.effective_default}` | {opt.level} | "
            f"{tuning_model(opt)} |"
        )
    lines.extend(["", tuning_intro()])
    for opt in options:
        lines.append(render_option(opt))
    lines.extend(["", "[← RGW config overview](OVERVIEW.md)", ""])
    return "\n".join(lines)


def render_tuning_index(all_options: list[Option]) -> str:
    lines = [
        "# RGW Config — Tuning Quick Reference",
        "",
        f"All **{len(all_options)}** RGW options with tuning model and one-line guidance. "
        "Each topic page has step-by-step **Finding optimal value** sections.",
        "",
        "[← RGW config overview](OVERVIEW.md) · [Curated batch 1](../rgw-config-options.md)",
        "",
        "| Option | Default | Model | Quick answer | Topic |",
        "|--------|---------|-------|--------------|-------|",
    ]
    for opt in all_options:
        slug = group_for(opt.name)
        title = GROUP_TITLES.get(slug, slug)
        lines.append(
            f"| [`{opt.name}`]({slug}.md#{opt.name}) | `{opt.effective_default}` | "
            f"{tuning_model(opt)} | {tuning_quick_answer(opt)} | [{title}]({slug}.md) |"
        )
    lines.extend(["", "[← RGW config overview](OVERVIEW.md)", ""])
    return "\n".join(lines)


def render_overview(groups: dict[str, list[Option]], total: int) -> str:
    lines = [
        "# RGW Config Deep Dive — All Options",
        "",
        f"Extended reference for all **{total}** RADOS Gateway options with "
        "**Finding optimal value** tuning guidance (same format as "
        f"[curated batch 1](../rgw-config-options.md)). "
        "Generated from [config/rgw/INDEX.md](../../config/rgw/INDEX.md).",
        "",
        "```bash",
        "./scripts/lookup-config.sh <option-name>",
        "python3 scripts/generate-rgw-guide.py  # regenerate after config sync",
        "```",
        "",
        "## Tuning",
        "",
        "- [Tuning quick reference](TUNING.md) — all options, model, one-line answer",
        "- [Curated batch 1](../rgw-config-options.md) — first 19 options with extra narrative",
        "",
        "## Tuning models",
        "",
        "| Model | How to choose |",
        "|-------|---------------|",
        "| **Policy** | Security, API compatibility, tenant limits |",
        "| **Capacity** | Disk layout, paths, pool sizing |",
        "| **Performance** | Baseline → incremental change → monitor OSD/RGW |",
        "| **Connectivity** | Nearest stable external endpoint |",
        "| **Architecture** | Backend, multisite topology |",
        "| **Dev** | Upstream default only in production |",
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
            "[← Guides overview](../OVERVIEW.md)",
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
    all_options: list[Option] = []
    for name, _href in index_order:
        if name not in by_name:
            print(f"warning: {name} in INDEX but not parsed", file=sys.stderr)
            continue
        all_options.append(by_name[name])

    groups: dict[str, list[Option]] = defaultdict(list)
    for opt in all_options:
        groups[group_for(opt.name)].append(opt)

    GUIDES.mkdir(parents=True, exist_ok=True)
    (GUIDES / "OVERVIEW.md").write_text(
        render_overview(groups, len(all_options)), encoding="utf-8"
    )
    (GUIDES / "TUNING.md").write_text(
        render_tuning_index(all_options), encoding="utf-8"
    )
    for slug, options in sorted(groups.items()):
        (GUIDES / f"{slug}.md").write_text(
            render_group(slug, options), encoding="utf-8"
        )

    print(
        f"Wrote {len(groups)} topic files + OVERVIEW + TUNING ({len(all_options)} options)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
