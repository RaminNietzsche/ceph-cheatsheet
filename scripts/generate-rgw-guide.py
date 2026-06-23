#!/usr/bin/env python3
"""Generate RGW config deep-dive guide pages from config/rgw/*.md tables."""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from i18n import (  # noqa: E402
    LOCALES,
    apply_inline_labels,
    cleanup_stale_markdown,
    model_label,
    set_locale,
    t,
    write_localized,
)
CONFIG_RGW = ROOT / "config" / "rgw"
GUIDES = ROOT / "guides" / "rgw-config"

# Extra narrative merged from the former batch-1 guide into per-option sections.
ENRICHMENTS: dict[str, dict[str, str]] = {
    "d4n_writecache_enabled": {
        "what": (
            "Enables the D4N (Data Delivery Network) **write-back cache**. When `true`, "
            "writes are staged in the local D4N cache layer (SSD path or Redis) before "
            "reaching the backend store."
        ),
        "when_to_use": (
            "Experimental edge/cache scenarios to reduce write latency. Requires "
            "`rgw_filter = d4n` — not for standard production RGW on RADOS alone."
        ),
        "related_extra": (
            "- `rgw_filter` = `d4n` (required)\n"
            "- `rgw_d4n_l1_datacache_persistent_path`, `rgw_d4n_address`, "
            "`rgw_d4n_l1_datacache_disk_reserve`, `rgw_d4n_cache_cleaning_interval`"
        ),
        "example": (
            "```bash\n"
            "ceph config set client.rgw rgw_filter d4n\n"
            "ceph config set client.rgw d4n_writecache_enabled true\n"
            "ceph config set client.rgw rgw_d4n_l1_datacache_persistent_path /var/cache/rgw_d4n/\n"
            "ceph orch restart rgw\n"
            "```"
        ),
    },
    "daos_pool": {
        "what": (
            "Name of the [DAOS](https://docs.daos.io/) pool RGW connects to when "
            "`rgw_backend_store = daos`."
        ),
        "when_to_use": (
            "Experimental DAOS-backed RGW (build with `-DWITH_RADOSGW_DAOS=ON`). "
            "Not used in standard Ceph clusters on RADOS."
        ),
        "example": (
            "```ini\n"
            "[client.rgw]\n"
            "rgw backend store = daos\n"
            "daos pool = mypool\n"
            "```\n\n"
            "Provision the DAOS pool with your site DAOS admin tools before setting this option."
        ),
    },
    "dbstore_config_uri": {
        "what": (
            "URI for the **configuration database** when using the experimental "
            "**dbstore** backend. URIs starting with `file:` point at a local SQLite file."
        ),
        "when_to_use": (
            "Standalone RGW without MON/OSD. See "
            "[dbstore README](https://github.com/ceph/ceph/blob/main/src/rgw/driver/dbstore/README.md)."
        ),
        "related_extra": (
            "- `rgw_backend_store` = `dbstore`\n"
            "- `rgw_config_store` = `dbstore`\n"
            "- `dbstore_db_dir`, `dbstore_db_name_prefix`"
        ),
        "example": (
            "```bash\n"
            "ceph config set client.rgw rgw_backend_store dbstore\n"
            "ceph config set client.rgw rgw_config_store dbstore\n"
            "ceph config set client.rgw dbstore_config_uri file:/var/lib/ceph/radosgw/dbstore-config.db\n"
            "```"
        ),
    },
    "dbstore_db_dir": {
        "what": (
            "Directory where dbstore writes SQLite files for object and metadata storage. "
            "Unlike `rados`, dbstore is **stateful** — every RGW instance must see the same files."
        ),
        "when_to_use": (
            "Isolate dbstore data on a dedicated filesystem. cephadm cannot freely move "
            "daemons without the data."
        ),
    },
    "dbstore_db_name_prefix": {
        "when_to_use": (
            "Multiple dbstore instances or tenants on one host without filename collisions."
        ),
    },
    "rgw_backend_store": {
        "what": (
            "Selects the **Storage Abstraction Layer (SAL)** — where RGW stores objects "
            "and metadata."
        ),
        "extra_body": (
            "| Value | Role |\n"
            "|-------|------|\n"
            "| `rados` | Production default — objects in RADOS pools |\n"
            "| `dbstore` | Experimental standalone SQLite backend |\n"
            "| `daos` | Experimental DAOS backend |\n"
            "| `motr` | Experimental Motr backend |\n"
            "| `posix` | Experimental POSIX filesystem backend |"
        ),
        "when_to_use": (
            "Leave `rados` in production. Other values are for development, testing, "
            "or specialized deployments."
        ),
        "related_extra": (
            "- `daos_pool`, `dbstore_*`, `rgw_config_store`, `rgw_filter`"
        ),
    },
    "rgw_account_default_quota_max_objects": {
        "what": (
            "Default cap on **total object count** across all buckets owned by a **new** "
            "S3 account. `-1` means unlimited."
        ),
        "when_to_use": (
            "Multi-tenant platforms using the account abstraction. Applies only when "
            "accounts are created — existing accounts are unchanged."
        ),
        "related_extra": (
            "- `rgw_account_default_quota_max_size`\n"
            "- `rgw_enable_quota_threads` (required on at least one RGW per zone)"
        ),
        "example": (
            "```bash\n"
            "ceph config set client rgw_account_default_quota_max_objects 1000000\n"
            'radosgw-admin user create --uid=alice --display-name="Alice"\n'
            "radosgw-admin quota get --quota-scope=user --uid=alice\n"
            "```\n\n"
            "Set in `[client]` or global so `radosgw-admin` picks it up."
        ),
    },
    "rgw_account_default_quota_max_size": {
        "what": "Default cap on **total stored bytes** for a new account.",
        "example": (
            "```bash\n"
            "# 10 TiB\n"
            "ceph config set client rgw_account_default_quota_max_size "
            "$((10*1024*1024*1024*1024))\n"
            "```"
        ),
    },
    "rgw_acl_grants_max_num": {
        "what": (
            "Maximum number of ACL grants in a single PutBucketAcl / PutObjectAcl request "
            "(aligned with S3 limits)."
        ),
        "when_to_use": (
            "Raise only if clients legitimately need more grants; lowering hardens against "
            "oversized ACL payloads."
        ),
        "related_extra": "- `rgw_cors_rules_max_num`, `rgw_user_policies_max_num`",
    },
    "rgw_admin_entry": {
        "what": (
            "URL path prefix for the **RGW Admin Ops REST API** (bucket/user introspection, "
            "usage, etc.). **Not runtime-updatable.**"
        ),
        "important": (
            "**Important:** Multisite replication **requires** the value `admin`. "
            "Do not change it on multisite clusters."
        ),
        "example": (
            "```bash\n"
            "# GET https://rgw.example.com/admin/bucket?bucket=mybucket&format=json\n"
            "curl -s -H \"Authorization: AWS ...\" \\\n"
            "  \"https://rgw.example.com/admin/bucket?bucket=mybucket&format=json\"\n"
            "```"
        ),
    },
    "rgw_allow_notification_secrets_in_cleartext": {
        "what": (
            "When `true`, allows bucket notification topics with broker passwords/secrets "
            "over plain HTTP. Default requires HTTPS for topics with secrets."
        ),
        "when_to_use": (
            "Trusted private lab only. **Never** enable on internet-facing or untrusted networks."
        ),
        "related_extra": "- `rgw_trust_forwarded_https` (if TLS terminates at a proxy)",
    },
    "rgw_barbican_url": {
        "what": (
            "Base URL of the **OpenStack Barbican** key manager for **SSE-KMS** server-side "
            "encryption."
        ),
        "when_to_use": (
            "Store encryption keys in Barbican instead of on-cluster secrets. Requires "
            "Keystone credentials for Barbican access."
        ),
        "related_extra": (
            "- `rgw_crypt_s3_kms_backend` = `barbican`\n"
            "- `rgw_keystone_barbican_*`, `rgw_crypt_s3_kms_cache_*`"
        ),
        "example": (
            "```bash\n"
            "ceph config set client.rgw rgw_crypt_s3_kms_backend barbican\n"
            "ceph config set client.rgw rgw_barbican_url https://barbican.example.com:9311/\n"
            "```\n\n"
            "See [Ceph RGW config ref — Barbican]"
            "(https://docs.ceph.com/en/latest/radosgw/config-ref/#barbican-settings)."
        ),
    },
    "rgw_asio_assert_yielding": {
        "what": (
            "Triggers an assertion if code on an asio/beast thread would block instead of "
            "yielding to coroutines. Development aid for finding blocking calls."
        ),
        "when_to_use": "RGW development/debugging only — keep `false` in production.",
        "related_extra": "- `rgw_beast_enable_async`",
    },
    "rgw_beast_enable_async": {
        "what": (
            "When `true`, the Beast HTTP frontend processes requests with **coroutines**, "
            "allowing multiple concurrent requests per thread."
        ),
        "when_to_use": (
            "Leave `true` for production throughput. Set `false` only when debugging "
            "request flow."
        ),
        "example": (
            "```bash\n"
            "ceph config set client.rgw rgw_beast_enable_async false\n"
            "ceph orch restart rgw\n"
            "```"
        ),
    },
    "rgw_bucket_counters_cache": {
        "what": (
            "Enables an in-memory cache for **perf counters** with a bucket label, so "
            "per-bucket metrics avoid repeated counter lookups."
        ),
        "related_extra": "- `rgw_bucket_counters_cache_size`",
        "example": (
            "```bash\n"
            "ceph config set client.rgw rgw_bucket_counters_cache true\n"
            "ceph config set client.rgw rgw_bucket_counters_cache_size 20000\n"
            "```"
        ),
    },
    "rgw_bucket_counters_cache_size": {
        "what": (
            "Maximum number of labeled per-bucket perf counter entries kept in the cache."
        ),
        "when_to_use": (
            "Increase on clusters with many active buckets and bucket-level monitoring enabled."
        ),
    },
    "rgw_bucket_default_quota_max_objects": {
        "what": (
            "Default maximum **objects per bucket** for **newly created users**. Does not "
            "retroactively change existing users."
        ),
        "when_to_use": (
            "Enforce per-bucket object limits for every new tenant without per-user "
            "`radosgw-admin quota` calls."
        ),
        "related_extra": (
            "- `rgw_bucket_default_quota_max_size`, `rgw_user_default_quota_*`"
        ),
        "example": (
            "```bash\n"
            "ceph config set client rgw_bucket_default_quota_max_objects 500000\n"
            "radosgw-admin user create --uid=newuser --display-name=\"New User\"\n"
            "```"
        ),
    },
    "rgw_bucket_default_quota_max_size": {
        "what": "Default maximum **bytes per bucket** for new users.",
        "example": (
            "```bash\n"
            "ceph config set client rgw_bucket_default_quota_max_size "
            "$((100*1024*1024*1024))\n\n"
            "radosgw-admin quota set --quota-scope=user --uid=alice "
            "--max-size=50G --max-objects=10000\n"
            "radosgw-admin quota enable --quota-scope=user --uid=alice\n"
            "```"
        ),
    },
    "rgw_bucket_eexist_override": {
        "what": (
            "When `true`, `CreateBucket` on an existing bucket (same owner) returns "
            "**HTTP 409 / EEXIST** instead of succeeding idempotently."
        ),
        "extra_body": (
            "**Default (`false`):** Matches AWS S3 — repeated CreateBucket by the same owner "
            "typically returns 200 OK."
        ),
        "when_to_use": (
            "Clients or automation that expect an error on duplicate bucket creation."
        ),
        "example": (
            "```bash\n"
            "ceph config set client.rgw rgw_bucket_eexist_override true\n"
            "# aws s3 mb s3://existing-bucket  →  409 BucketAlreadyExists\n"
            "```"
        ),
    },
    "rgw_bucket_index_max_aio": {
        "what": (
            "Limits **concurrent RADOS requests** across **bucket index shards** (list "
            "operations, index maintenance, multi-shard updates). Used in `svc_bi_rados.cc`."
        ),
        "related_extra": (
            "- [`rgw_multi_obj_del_max_aio`](../../../config/rgw/rgw.md#SP_rgw_multi_obj_del_max_aio) "
            "(default 16)\n"
            "- [`rgw_override_bucket_index_max_shards`]"
            "(../../../config/rgw/rgw.md#SP_rgw_override_bucket_index_max_shards)"
        ),
        "example": (
            "```bash\n"
            "ceph config set client.rgw rgw_bucket_index_max_aio 256\n"
            "```"
        ),
        "finding_note": (
            "More shards and faster OSDs tolerate higher values; during `nearfull` or heavy "
            "recovery, lower is safer."
        ),
    },
}

GROUP_TITLES = {
    "experimental-backends": "Experimental backends",
    "motr-experimental": "Motr backend",
    "posix-experimental": "POSIX backend",
    "d4n-cache": "D4N / D3N cache",
    "frontends": "Frontends & HTTP stack",
    "feature-toggles": "Feature toggles",
    "scheduler-dmclock": "Scheduler & dmclock",
    "s3-api": "S3 API & auth",
    "api-limits": "API limits & policies",
    "http-compat": "HTTP compatibility",
    "core-runtime": "Core runtime",
    "performance-tuning": "Concurrency & RADOS I/O",
    "object-io": "Object read/write windows",
    "multipart-copy": "Multipart & copy",
    "caching": "Metadata & object caches",
    "timeouts-intervals": "Timeouts & intervals",
    "limits-listing": "Listing limits",
    "ratelimit": "Rate limiting",
    "bucket-ops": "Bucket operations",
    "index-sharding": "Bucket index & sharding",
    "resharding": "Dynamic resharding",
    "object-expiry": "Object expiry hints",
    "garbage-collection": "Garbage collection",
    "quotas": "Quota sync & defaults",
    "users-quotas": "Users & per-user settings",
    "multisite-zones": "Zones, realm & region",
    "multisite-sync": "Replication & sync",
    "rest-connections": "REST connections",
    "encryption": "Encryption & KMS",
    "keystone-sts": "Keystone & STS",
    "ldap": "LDAP",
    "opa-authz": "OPA authorization",
    "swift": "Swift API",
    "notifications": "Bucket notifications",
    "lifecycle": "Lifecycle (LC)",
    "logging": "Access & object logging",
    "ops-logging": "Ops logging",
    "usage-logging": "Usage logging",
    "admin-cors": "Admin CORS",
    "nfs": "NFS gateway",
    "lua": "Lua scripting",
    "torrent": "BitTorrent",
    "http-curl": "HTTP / libcurl",
    "debug-inject": "Debug & fault injection",
}

# Sidebar nav: (section title, topic slugs). Collapsible groups in MkDocs Material.
NAV_SECTIONS: list[tuple[str, list[str]]] = [
    (
        "Core gateway",
        [
            "frontends",
            "feature-toggles",
            "scheduler-dmclock",
            "http-compat",
            "core-runtime",
        ],
    ),
    (
        "Performance & I/O",
        [
            "performance-tuning",
            "object-io",
            "multipart-copy",
            "caching",
            "timeouts-intervals",
            "limits-listing",
        ],
    ),
    (
        "Buckets & data lifecycle",
        [
            "bucket-ops",
            "index-sharding",
            "resharding",
            "object-expiry",
            "garbage-collection",
            "lifecycle",
        ],
    ),
    ("Tenants & quotas", ["quotas", "users-quotas"]),
    (
        "Multisite",
        ["multisite-zones", "multisite-sync", "rest-connections"],
    ),
    (
        "Security & authentication",
        ["encryption", "keystone-sts", "ldap", "opa-authz", "swift", "s3-api"],
    ),
    ("Notifications", ["notifications"]),
    (
        "Logging & admin",
        ["logging", "ops-logging", "usage-logging", "admin-cors", "api-limits"],
    ),
    ("Extensions", ["nfs", "lua", "torrent", "http-curl"]),
    (
        "Experimental & debug",
        [
            "experimental-backends",
            "motr-experimental",
            "posix-experimental",
            "d4n-cache",
            "debug-inject",
        ],
    ),
]

# Folder names under guides/rgw-config/ — mirror MkDocs nav sections.
SECTION_SLUGS: dict[str, str] = {
    "Core gateway": "core-gateway",
    "Performance & I/O": "performance-io",
    "Buckets & data lifecycle": "buckets-lifecycle",
    "Tenants & quotas": "tenants-quotas",
    "Multisite": "multisite",
    "Security & authentication": "security-auth",
    "Notifications": "notifications",
    "Logging & admin": "logging-admin",
    "Extensions": "extensions",
    "Experimental & debug": "experimental-debug",
    "Other": "other",
}

CONFIG_RGW_FROM_TOPIC = "../../../config/rgw"
CONFIG_RGW_FROM_ROOT = "../../config/rgw"

MKDOCS = ROOT / "mkdocs.yml"
NAV_BEGIN = "# rgw-nav:start"
NAV_END = "# rgw-nav:end"

API_LIMITS = {
    "rgw_acl_grants_max_num",
    "rgw_cors_rules_max_num",
    "rgw_website_routing_rules_max_num",
    "rgw_policy_reject_invalid_principals",
    "rgw_topic_require_publish_policy",
}

HTTP_COMPAT = {
    "rgw_content_length_compat",
    "rgw_cross_domain_policy",
    "rgw_defer_to_bucket_acls",
    "rgw_enforce_swift_acls",
    "rgw_ignore_get_invalid_range",
    "rgw_extended_http_attrs",
    "rgw_print_continue",
    "rgw_print_prohibited_content_length",
    "rgw_relaxed_region_enforcement",
    "rgw_relaxed_s3_bucket_names",
    "rgw_relaxed_topic_names",
    "rgw_remote_addr_param",
    "rgw_request_uri",
    "rgw_resolve_cname",
    "rgw_trust_forwarded_https",
    "rgw_verify_ssl",
    "rgw_service_provider_name",
}

CORE_RUNTIME = {
    "rgw_data",
    "rgw_filter",
    "rgw_graceful_stop",
    "rgw_healthcheck_disabling_path",
    "rgw_json_config",
    "rgw_numa_node",
    "rgw_expose_bucket",
    "rgw_script_uri",
    "rgw_rados_pool_autoscale_bias",
    "rgw_rados_pool_recovery_priority",
    "rgw_rados_tracing",
    "rgw_op_tracing",
    "rgw_dedup_min_obj_size_for_dedup",
    "rgw_dedup_split_obj_head",
    "rgw_parquet_buffer_size",
    "rgw_mime_types_file",
}

INDEX_SHARDING = {
    "rgw_override_bucket_index_max_shards",
    "rgw_safe_max_objects_per_shard",
    "rgw_shard_warning_threshold",
    "rgw_pending_bucket_index_op_expiration",
}

ADMIN_API = {
    "rgw_admin_entry",
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
        return "lifecycle"
    if name in API_LIMITS:
        return "api-limits"
    if name in HTTP_COMPAT:
        return "http-compat"
    if name in CORE_RUNTIME:
        return "core-runtime"
    if name in INDEX_SHARDING:
        return "index-sharding"
    if name in ADMIN_API:
        return "api-limits"
    if name == "rgw_barbican_url":
        return "encryption"
    if name in ("rgw_asio_assert_yielding", "rgw_beast_enable_async"):
        return "frontends"
    if name.startswith("rgw_default_") and name.endswith("_oid"):
        return "multisite-zones"
    if name in (
        "rgw_lifecycle_work_time",
        "rgw_mp_lock_max_time",
        "rgw_restore_lock_max_time",
    ):
        return "lifecycle"
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
    if name.startswith("rgw_scheduler") or name.startswith("rgw_dmclock"):
        return "scheduler-dmclock"
    if name.startswith("rgw_bucket_"):
        return "bucket-ops"
    if name.startswith(("rgw_d4n", "rgw_d3n")) or name.startswith("d4n_"):
        return "d4n-cache"
    if name.startswith("rgw_cache"):
        return "caching"
    if name in ("rgw_obj_tombstone_cache_size",):
        return "caching"
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
    if name.startswith("rgw_opa") or name == "rgw_use_opa_authz":
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
    if name in ("rgw_user_counters_cache", "rgw_user_counters_cache_size"):
        return "users-quotas"
    if any(
        x in name
        for x in ("cache", "ttl", "lru")
    ) and "crypt" not in name and "quota" not in name:
        return "caching"
    if any(
        x in name
        for x in ("timeout", "interval", "period", "delay", "wait", "sleep", "tick")
    ):
        return "timeouts-intervals"
    if name.startswith(("rgw_frontends", "rgw_frontend", "rgw_dns")):
        return "frontends"
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
    if name.startswith("rgw_multipart") or name.startswith("rgw_copy_obj"):
        return "multipart-copy"
    if name.startswith(("rgw_get_obj", "rgw_put_obj")):
        return "object-io"
    if name.startswith("rgw_user_"):
        return "users-quotas"
    if name.startswith(("rgw_max_", "rgw_list_", "rgw_delete_", "rgw_multi_obj")):
        return "limits-listing"
    return "core-runtime"


def when_to_use(opt: Option) -> str:
    name, level, typ = opt.name, opt.level, opt.typ
    if level == "Dev" or "inject" in name or "debug" in name:
        return t("when_use_dev")
    if name.startswith("motr_") or name.startswith("rgw_posix"):
        return t("when_use_motr")
    if typ == "Bool" and opt.effective_default.lower() in ("true", "false"):
        default = opt.effective_default.lower()
        if default == "true":
            return t("when_use_bool_true")
        return t("when_use_bool_false")
    if "_url" in name or "_uri" in name or name.endswith("_addr"):
        return t("when_use_rgw_external")
    if "quota" in name and "max" in name:
        return t("when_use_quota")
    if "max_" in name or "limit" in name:
        return t("when_use_max_limit")
    if "cache" in name or "ttl" in name:
        return t("when_use_cache")
    if "sync" in name or "multisite" in opt.full_desc.lower():
        return t("when_use_sync")
    if level == "Basic":
        return t("when_use_rgw_basic")
    return t("when_use_advanced")


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
        "radosgw-admin sync status",
        "ceph config show client.rgw.<instance>",
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
                    "radosgw-admin sync status",
                    "ceph config get client.rgw rgw_zone",
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
                    "4. Create a test user and confirm via "
                    "`radosgw-admin quota get --quota-scope=user --uid=<uid>`.",
                    "5. Existing users/accounts are **not** retroactively changed.",
                    "",
                    "```bash",
                    "ceph df detail",
                    "radosgw-admin quota get --quota-scope=user --uid=testuser",
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
        lines.append(f"- [`{ref}`]({CONFIG_RGW_FROM_TOPIC}/{opt.source_file}#SP_{ref})")
    lines.append("")
    return "\n".join(lines)


def config_target(opt: Option) -> str:
    if opt.name == "rgw_usage_max_shards":
        return "global"
    if opt.name.startswith(
        ("rgw_account_default_", "rgw_bucket_default_", "rgw_user_default_")
    ):
        return "client"
    return "client.rgw"


def quote_config_value(opt: Option, value: str) -> str:
    if opt.typ != "Str":
        return value
    if value.startswith('"') and value.endswith('"'):
        return value
    if any(c in value for c in (' ', '/', '@', ':', '.', '-', '<', '>', '=')):
        return f'"{value}"'
    return value


def example_value(opt: Option) -> str:
    """Demonstration value for ceph config set (may differ from default when -1/empty)."""
    default = opt.effective_default
    name = opt.name

    if default not in ("(empty)", ""):
        return quote_config_value(opt, default)

    if name.endswith("_url") or name.endswith("_uri"):
        if "keystone" in name:
            return '"https://keystone.example.com:5000/v3/"'
        if "barbican" in name:
            return '"https://barbican.example.com:9311/"'
        if "vault" in name or "crypt_sse" in name:
            return '"https://vault.example.com:8200/"'
        if "ldap" in name:
            return '"ldaps://ldap.example.com/"'
        if "opa" in name:
            return '"https://opa.example.com:8181/v1/data/ceph/authz"'
        if "swift" in name:
            return '"https://swift.example.com/auth/v1.0"'
        if "sts" in name and "introspection" in name:
            return '"https://idp.example.com/oauth2/introspect"'
        return '"https://service.example.com/"'

    if name.endswith("_addr") or name.endswith("_address"):
        if "d4n" in name or "d3n" in name:
            return '"127.0.0.1:6379"'
        if "kmip" in name:
            return '"kmip.example.com:5696"'
        return '"192.0.2.10:7480"'

    if name.endswith(("_path", "_dir", "_base_path")):
        if "d4n" in name or "d3n" in name or "cache" in name:
            return '"/var/cache/rgw"'
        if "posix" in name:
            return '"/data/rgw/posix"'
        return '"/var/lib/ceph/radosgw"'

    if name.endswith("_file"):
        if "token" in name:
            return '"/etc/ceph/rgw-vault-token"'
        if "clientcert" in name or "clientkey" in name:
            return '"/etc/ceph/ssl/rgw-client.crt"'
        if "cacert" in name or "ssl_cacert" in name:
            return '"/etc/ceph/ssl/ca.crt"'
        return '"/etc/ceph/rgw.conf"'

    if name.endswith("_pool") or name.endswith("_root_pool"):
        return ".rgw.root"

    if name.endswith("_oid"):
        return '"zone.info"'

    if name == "rgw_zone":
        return '"us-east-1"'
    if name == "rgw_zonegroup":
        return '"default"'
    if name == "rgw_realm":
        return '"default"'
    if name == "rgw_region":
        return '"us-east-1"'

    if "password" in name or "secret" in name or name.endswith("_key"):
        if "template" in name:
            return '"vault/secret/data/ceph/{{key}}"'
        return '"<from-secrets-manager>"'

    if name.endswith("_endpoint") or name.endswith("_fid"):
        return '"192.168.1.10@tcp:12345:1:1"'

    if name == "rgw_dns_name":
        return '"s3.example.com"'
    if name == "rgw_dns_s3website_name":
        return '"website.s3.example.com"'

    if name == "rgw_frontends":
        return '"beast port=7480"'

    if name == "rgw_run_sync_thread" or name.startswith("rgw_enable_"):
        return "true"

    return "<value>"


def bool_example_value(opt: Option) -> str:
    default = opt.effective_default.lower()
    if default == "true":
        return "false"
    return "true"


def numeric_example_value(opt: Option) -> str:
    default = opt.effective_default
    name = opt.name
    if default == "-1" and "quota" in name and "max" in name:
        if "size" in name:
            return "$((100*1024*1024*1024))"
        return "1000000"
    if default == "0" and ("timeout" in name or "interval" in name):
        return "60"
    if default == "0" and "max" in name:
        return "128"
    return default


def example_followups(opt: Option) -> list[str]:
    name = opt.name
    lines: list[str] = []

    if "quota" in name and "max" in name:
        lines.append("radosgw-admin quota get --quota-scope=user --uid=testuser")
    elif name.startswith("rgw_user_default_quota") or name == "rgw_user_max_buckets":
        lines.append('radosgw-admin user create --uid=newuser --display-name="New User"')
    elif name.startswith("rgw_bucket_default_quota"):
        lines.append('radosgw-admin user create --uid=newuser --display-name="New User"')
    elif name == "rgw_realm":
        lines.append("radosgw-admin realm list")
    elif name in ("rgw_zone", "rgw_zonegroup"):
        lines.append(f"ceph config get client.rgw {name}")
        lines.append("radosgw-admin sync status")
    elif name.startswith("rgw_zone"):
        lines.append("radosgw-admin sync status")
    elif "sync" in name and ("interval" in name or "poll" in name or "spawn" in name):
        lines.append("radosgw-admin sync status")
    elif name.endswith("_url") or name.endswith("_uri") or name.endswith("_addr"):
        lines.append("# curl -k <url>  # from each RGW node")
    elif name == "rgw_bucket_index_max_aio":
        lines.append("radosgw-admin bucket stats --bucket=BIG_BUCKET | jq '.num_shards'")
    elif name == "rgw_bucket_eexist_override":
        lines.append("# aws s3 mb s3://existing-bucket  →  409 if bucket exists")
    elif name == "rgw_admin_entry":
        lines.append(
            'curl -s "https://rgw.example.com/admin/bucket?bucket=mybucket&format=json" '
            '-H "Authorization: AWS ..."'
        )
    elif name == "rgw_barbican_url":
        lines.append("ceph config set client.rgw rgw_crypt_s3_kms_backend barbican")
    elif name == "rgw_backend_store" and opt.effective_default == "rados":
        lines.append("# Production: keep rados; PoC only: dbstore | daos | motr | posix")
    elif name == "d4n_writecache_enabled":
        lines.extend(
            [
                "ceph config set client.rgw rgw_filter d4n",
                "ceph config set client.rgw rgw_d4n_l1_datacache_persistent_path /var/cache/rgw_d4n/",
            ]
        )
    elif name == "rgw_bucket_counters_cache":
        lines.append("ceph config set client.rgw rgw_bucket_counters_cache_size 20000")
    elif name == "rgw_user_counters_cache":
        lines.append("ceph config set client.rgw rgw_user_counters_cache_size 20000")
    elif name == "rgw_lc_counters_cache":
        lines.append("ceph config set client.rgw rgw_lc_counters_cache_size 20000")
    elif name == "rgw_enable_quota_threads":
        lines.append("radosgw-admin quota get --quota-scope=user --uid=testuser")
    elif name == "rgw_crypt_s3_kms_backend":
        lines.append("ceph config set client.rgw rgw_barbican_url https://barbican.example.com:9311/")
    elif name.startswith("rgw_ldap_"):
        lines.append("ceph config set client.rgw rgw_s3_auth_use_ldap true")
    elif name == "rgw_use_opa_authz":
        lines.append('ceph config set client.rgw rgw_opa_url "https://opa.example.com:8181/v1/data/ceph/authz"')

    return lines


def render_example(opt: Option) -> str:
    enrich = ENRICHMENTS.get(opt.name, {})
    if enrich.get("example"):
        return enrich["example"]

    if opt.name == "daos_pool":
        return (
            "```ini\n"
            "[client.rgw]\n"
            "rgw backend store = daos\n"
            "daos pool = mypool\n"
            "```\n\n"
            "Provision the DAOS pool with your site DAOS admin tools before setting this option."
        )

    if opt.name == "rgw_admin_entry":
        return enrich.get("example") or (
            "```bash\n"
            "ceph config get client.rgw rgw_admin_entry\n"
            "# Default admin URL:\n"
            "curl -s -H \"Authorization: AWS ...\" \\\n"
            '  "https://rgw.example.com/admin/bucket?bucket=mybucket&format=json"\n'
            "```"
        )

    target = config_target(opt)
    restart = "\nceph orch restart rgw" if opt.flags and "STARTUP" in opt.flags else ""

    if opt.typ == "Bool":
        val = bool_example_value(opt)
    elif opt.typ in ("Int", "Uint", "Size"):
        val = numeric_example_value(opt)
    else:
        val = example_value(opt)

    lines = [f"ceph config set {target} {opt.name} {val}", f"ceph config get {target} {opt.name}"]
    lines.extend(example_followups(opt))

    return f"```bash\n" + "\n".join(lines) + restart + "\n```"


def format_example(opt: Option) -> str:
    return render_example(opt)


def format_related_extra(opt: Option, extra: str) -> str:
    lines = ["**Related options:**", "", extra]
    for ref in related_options(opt):
        lines.append(f"- [`{ref}`]({CONFIG_RGW_FROM_TOPIC}/{opt.source_file}#SP_{ref})")
    lines.append("")
    return "\n".join(lines)


def render_option(opt: Option) -> str:
    enrich = ENRICHMENTS.get(opt.name, {})
    startup = t("label_startup") if opt.flags and "STARTUP" in opt.flags else ""
    table_link = f"{CONFIG_RGW_FROM_TOPIC}/{opt.source_file}#SP_{opt.name}"
    type_bits = [opt.typ, f"default `{opt.effective_default}`", f"**{opt.level}**"]
    if opt.valid_values:
        type_bits.insert(1, f"enum: {opt.valid_values}")
    parts = [
        f"### {opt.name}",
        "",
        "| | |",
        "|---|---|",
        f"{t('label_type')} {' · '.join(type_bits)}{startup} |",
        f"{t('label_table')} [{opt.source_file}#SP_{opt.name}]({table_link}) |",
        "",
    ]
    what = enrich.get("what") or opt.full_desc
    if what:
        parts.extend([f"{t('label_what_it_does')} {what}", ""])
    if enrich.get("extra_body"):
        parts.extend([enrich["extra_body"], ""])
    if enrich.get("important"):
        parts.extend([enrich["important"], ""])
    bullets = when_to_use_bullets(opt)
    if enrich.get("when_to_use"):
        parts.extend([f"{t('label_when_to_use')} {enrich['when_to_use']}", ""])
    elif bullets:
        parts.extend([t("label_when_to_use"), "", bullets, ""])
    else:
        parts.extend([f"{t('label_when_to_use')} {when_to_use(opt)}", ""])
    if enrich.get("related_extra"):
        parts.append(format_related_extra(opt, enrich["related_extra"]))
    else:
        see = format_see_also(opt)
        if see:
            parts.append(see)
    parts.extend([t("label_example"), "", render_example(opt), ""])
    finding = render_finding_optimal_value(opt)
    if enrich.get("finding_note"):
        finding = f"{finding}\n\n{enrich['finding_note']}"
    parts.extend([t("label_finding_optimal"), "", finding, "", "---", ""])
    return "\n".join(parts)


def tuning_intro() -> str:
    return "\n".join(
        [
            t("finding_intro_title"),
            "",
            t("finding_intro_table"),
            "|-------|---------------|",
            t("finding_policy_rgw_row"),
            t("finding_capacity_rgw_row"),
            t("finding_performance_rgw_row"),
            t("finding_connectivity_row"),
            t("finding_architecture_row"),
            t("finding_dev_row"),
            "",
            t("label_shared_tooling"),
            "",
            "```bash",
            "ceph config get client.rgw <option>",
            "radosgw-admin sync status",
            "ceph config show client.rgw.<instance>",
            "ceph pg stat",
            "```",
            "",
            "---",
            "",
        ]
    )


def render_group(slug: str, options: list[Option]) -> str:
    title = GROUP_TITLES.get(slug, slug.replace("-", " ").title())
    lines = [
        f"# {title}",
        "",
        t(
            "rgw_group_intro",
            count=len(options),
            overview=t("back_rgw_overview"),
            tuning=t("tuning_index_link"),
            index=f"[INDEX]({CONFIG_RGW_FROM_TOPIC}/INDEX.md)",
        ),
        "",
    ]
    if slug == "quotas":
        lines.extend(
            [
                t(
                    "rgw_quota_note",
                    href=f"{CONFIG_RGW_FROM_TOPIC}/rgw.md#SP_rgw_enable_quota_threads",
                ),
                "",
            ]
        )
    lines.extend(
        [
            t("option_summary_header"),
            "|--------|---------|-------|--------|",
        ]
    )
    for opt in options:
        lines.append(
            f"| [{opt.name}](#{opt.name}) | `{opt.effective_default}` | {opt.level} | "
            f"{model_label(tuning_model(opt))} |"
        )
    lines.extend(["", tuning_intro()])
    for opt in options:
        lines.append(render_option(opt))
    lines.extend(["", t("back_rgw_overview"), ""])
    return "\n".join(lines)


def render_tuning_index(all_options: list[Option]) -> str:
    lines = [
        t("rgw_tuning_title"),
        "",
        t("rgw_tuning_blurb", count=len(all_options)),
        "",
        f"{t('back_rgw_overview')} · {t('tuning_quick_link')}",
        "",
        t("tuning_summary_header"),
        "|--------|---------|-------|--------------|-------|",
    ]
    for opt in all_options:
        slug = group_for(opt.name)
        title = GROUP_TITLES.get(slug, slug)
        lines.append(
            f"| [`{opt.name}`]({topic_href(slug)}#{opt.name}) | `{opt.effective_default}` | "
            f"{model_label(tuning_model(opt))} | {tuning_quick_answer(opt)} | [{title}]({topic_href(slug)}) |"
        )
    lines.extend(["", t("back_rgw_overview"), ""])
    return "\n".join(lines)


def section_for_slug(slug: str) -> str:
    for title, slugs in NAV_SECTIONS:
        if slug in slugs:
            return title
    return "Other"


def section_dir_for_slug(slug: str) -> str:
    return SECTION_SLUGS.get(section_for_slug(slug), "other")


def topic_path(slug: str) -> Path:
    return GUIDES / section_dir_for_slug(slug) / f"{slug}.md"


def topic_href(slug: str) -> str:
    """Relative link from OVERVIEW.md or TUNING.md at guides/rgw-config/."""
    return f"{section_dir_for_slug(slug)}/{slug}.md"


def nav_slugs_in_order(groups: dict[str, list[Option]]) -> list[str]:
    """All topic slugs in nav order; append any slug missing from NAV_SECTIONS."""
    ordered: list[str] = []
    seen: set[str] = set()
    for _title, slugs in NAV_SECTIONS:
        for slug in slugs:
            if slug in groups and slug not in seen:
                ordered.append(slug)
                seen.add(slug)
    for slug in sorted(groups):
        if slug not in seen:
            ordered.append(slug)
    return ordered


def render_overview(groups: dict[str, list[Option]], total: int) -> str:
    lines = [
        t("rgw_overview_title"),
        "",
        t("rgw_overview_blurb", count=total, href=f"{CONFIG_RGW_FROM_ROOT}/INDEX.md"),
        "",
        "```bash",
        "./scripts/lookup-config.sh <option-name>",
        "python3 scripts/generate-rgw-guide.py  # regenerate after config sync",
        "```",
        "",
        t("rgw_overview_tuning_section"),
        "",
        t("tuning_quick_link") + " — all options, model, one-line answer",
        "",
        t("finding_intro_title"),
        "",
        t("finding_intro_table"),
        "|-------|---------------|",
        t("finding_policy_rgw_row"),
        t("finding_capacity_rgw_row"),
        t("finding_performance_rgw_row"),
        t("finding_connectivity_row"),
        t("finding_architecture_row"),
        t("finding_dev_row"),
        "",
        t("topics_by_category"),
        "",
    ]
    current_section = ""
    for slug in nav_slugs_in_order(groups):
        section = section_for_slug(slug)
        if section != current_section:
            current_section = section
            lines.extend(["", f"### {section}", "", t("topic_summary_header"), "|-------|---------|"])
        title = GROUP_TITLES.get(slug, slug)
        lines.append(f"| [{title}]({topic_href(slug)}) | {len(groups[slug])} |")
    lines.extend(["", t("back_guides_overview"), ""])
    return "\n".join(lines)


def render_all_locales_rgw(fn, *args, **kwargs) -> dict[str, str]:
    out: dict[str, str] = {}
    for locale in LOCALES:
        set_locale(locale)
        out[locale] = apply_inline_labels(fn(*args, **kwargs), locale)
    set_locale("en")
    return out


def build_mkdocs_nav_yaml(groups: dict[str, list[Option]]) -> str:
    lines = [
        "    - RGW config deep dive:",
        "      - Start here:",
        "        - Overview: guides/rgw-config/OVERVIEW.md",
        "        - Tuning quick reference: guides/rgw-config/TUNING.md",
    ]
    for section_title, slugs in NAV_SECTIONS:
        present = [s for s in slugs if s in groups]
        if not present:
            continue
        lines.append(f"      - {section_title}:")
        for slug in present:
            title = GROUP_TITLES.get(slug, slug.replace("-", " ").title())
            lines.append(
                f"        - {title}: guides/rgw-config/{section_dir_for_slug(slug)}/{slug}.md"
            )
    extra = [s for s in sorted(groups) if section_for_slug(s) == "Other"]
    if extra:
        lines.append("      - Other:")
        for slug in extra:
            title = GROUP_TITLES.get(slug, slug)
            lines.append(
                f"        - {title}: guides/rgw-config/{section_dir_for_slug(slug)}/{slug}.md"
            )
    return "\n".join(lines)


def indent_nav_block(block: str) -> str:
    return "\n".join(f"  {line}" if line.strip() else line for line in block.splitlines())


def build_rgw_redirect_yaml() -> str:
    lines = [
        "        'guides/rgw-config-options.md': 'guides/rgw-config/OVERVIEW.md'",
    ]
    for section_title, slugs in NAV_SECTIONS:
        section_dir = SECTION_SLUGS.get(section_title, "other")
        for slug in slugs:
            lines.append(
                f"        'guides/rgw-config/{slug}.md': "
                f"'guides/rgw-config/{section_dir}/{slug}.md'"
            )
    return "\n".join(lines)


REDIRECT_BEGIN = "# rgw-redirects:start"
REDIRECT_END = "# rgw-redirects:end"


def patch_mkdocs_redirects() -> None:
    if not MKDOCS.exists():
        return
    text = MKDOCS.read_text(encoding="utf-8")
    if REDIRECT_BEGIN not in text or REDIRECT_END not in text:
        print(f"warning: {MKDOCS} missing redirect markers", file=sys.stderr)
        return
    before, rest = text.split(REDIRECT_BEGIN, 1)
    _old, after = rest.split(REDIRECT_END, 1)
    block = build_rgw_redirect_yaml()
    MKDOCS.write_text(f"{before}{REDIRECT_BEGIN}\n{block}\n{REDIRECT_END}{after}", encoding="utf-8")
    print(f"Patched RGW redirects in {MKDOCS.relative_to(ROOT)}")


def patch_mkdocs_nav(groups: dict[str, list[Option]]) -> None:
    if not MKDOCS.exists():
        print(f"warning: {MKDOCS} not found, skipping nav patch", file=sys.stderr)
        return
    text = MKDOCS.read_text(encoding="utf-8")
    if NAV_BEGIN not in text or NAV_END not in text:
        print(
            f"warning: {MKDOCS} missing {NAV_BEGIN}/{NAV_END} markers",
            file=sys.stderr,
        )
        return
    before, rest = text.split(NAV_BEGIN, 1)
    _old, after = rest.split(NAV_END, 1)
    nav_block = indent_nav_block(build_mkdocs_nav_yaml(groups))
    MKDOCS.write_text(
        f"{before}{NAV_BEGIN}\n{nav_block}\n{NAV_END}{after}",
        encoding="utf-8",
    )
    print(f"Patched RGW nav in {MKDOCS.relative_to(ROOT)}")
    patch_mkdocs_redirects()


def main() -> int:
    by_name: dict[str, Option] = {}
    for md in sorted(CONFIG_RGW.glob("*.md")):
        if md.name in ("INDEX.md", "README.md") or md.name.endswith((".fa.md", ".zh.md")):
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

    overview_base = GUIDES / "OVERVIEW.md"
    tuning_base = GUIDES / "TUNING.md"
    write_localized(overview_base, render_all_locales_rgw(render_overview, groups, len(all_options)))
    write_localized(tuning_base, render_all_locales_rgw(render_tuning_index, all_options))

    keep_bases: set[Path] = {overview_base, tuning_base}
    for slug, options in sorted(groups.items()):
        base = topic_path(slug)
        base.parent.mkdir(parents=True, exist_ok=True)
        write_localized(base, render_all_locales_rgw(render_group, slug, options))
        keep_bases.add(base)

    cleanup_stale_markdown(GUIDES, keep_bases)

    patch_mkdocs_nav(groups)

    print(
        f"Wrote {len(groups)} topic files + OVERVIEW + TUNING ({len(all_options)} options)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
