"""Hand-tuned deep-dive text for high-traffic config options."""

OSD_ENRICHMENTS: dict[str, dict[str, str]] = {
    "osd_max_scrubs": {
        "what": (
            "Maximum concurrent scrub operations per OSD. Scrub reads object data "
            "to verify checksums — too many scrubs compete with client I/O."
        ),
        "when_to_use": (
            "Increase cautiously on fast media when scrubs lag behind the scrub interval. "
            "Decrease when `ceph -s` reports slow ops or OSD latency spikes during scrub windows."
        ),
        "finding_note": (
            "Pair with `osd_scrub_sleep` and deep-scrub intervals. "
            "HDD clusters often stay at 1; NVMe may tolerate 2–3 if load is low."
        ),
    },
    "osd_recovery_max_active": {
        "what": (
            "Cap on concurrent recovery/backfill operations per OSD (0 = derive from "
            "HDD/SSD/hybrid-specific settings)."
        ),
        "when_to_use": (
            "Raise temporarily after OSD replacement to rebuild faster; lower during "
            "production peaks to protect client latency."
        ),
        "finding_note": (
            "Watch `recovering`/`backfilling` PG count and client p99. "
            "See also `osd_recovery_max_active_hdd` / `_ssd` when set to 0."
        ),
    },
    "osd_recovery_sleep": {
        "what": (
            "Pause between recovery/backfill chunks (seconds). Non-zero values throttle "
            "recovery to leave headroom for application I/O."
        ),
        "when_to_use": (
            "Use on busy clusters during business hours; set to 0 for fastest rebuild "
            "in maintenance windows."
        ),
    },
    "osd_mclock_profile": {
        "what": (
            "Selects the mClock scheduler profile (`balanced`, `high_client_ops`, "
            "`high_recovery_ops`, or custom)."
        ),
        "when_to_use": (
            "Start with `balanced` on mixed workloads. Use `high_client_ops` when "
            "recovery dominates latency; `high_recovery_ops` for aggressive rebuild windows."
        ),
        "example": (
            "```bash\n"
            "ceph config set osd osd_mclock_profile high_client_ops\n"
            "ceph config get osd osd_mclock_profile\n"
            "ceph daemon osd.<id> config show | grep mclock\n"
            "```"
        ),
    },
    "osd_deep_scrub_interval": {
        "what": "Interval (seconds) between deep scrubs that verify full object checksums.",
        "when_to_use": (
            "Shorten for compliance-heavy environments; lengthen on large HDD pools "
            "where deep scrub IO is costly."
        ),
    },
    "osd_scrub_max_interval": {
        "what": "Maximum interval (seconds) between shallow scrubs for a PG.",
        "when_to_use": (
            "Align with maintenance policy. Monitor `mon_warn_pg_not_scrubbed_ratio` warnings."
        ),
    },
    "osd_op_queue": {
        "what": (
            "OSD operation queue scheduler (`mclock_scheduler`, `wpq`, or `debug_random`). "
            "Production clusters should use mClock."
        ),
        "when_to_use": "Keep `mclock_scheduler` unless upstream support directs otherwise.",
    },
}

MON_ENRICHMENTS: dict[str, dict[str, str]] = {
    "mon_osd_down_out_interval": {
        "what": (
            "Seconds an OSD can stay `down` before the monitor marks it `out` and "
            "CRUSH begins rebalancing."
        ),
        "when_to_use": (
            "Increase for flaky networks or long maintenance (avoid premature rebalance). "
            "Decrease when you want faster failover — at the cost of more data movement."
        ),
        "finding_note": (
            "Common production range: 600–3600 s. Coordinate with `mon_osd_min_down_reporters`."
        ),
    },
    "mon_osd_min_down_reporters": {
        "what": "Number of monitors that must report an OSD down before it is marked down.",
        "when_to_use": (
            "Rarely changed. Lower only in small test clusters; raise for split-brain protection."
        ),
    },
    "mon_target_pg_per_osd": {
        "what": (
            "Target PG count per OSD used by the PG autoscaler and health warnings "
            "(`mon_warn_pg_per_osd` family)."
        ),
        "when_to_use": (
            "Tune when autoscaler creates too many/few PGs for your OSD count and "
            "device classes."
        ),
    },
    "mon_allow_pool_size_one": {
        "what": "Allow pools with `size=1` (no redundancy).",
        "when_to_use": "Lab only. Keep `false` in production unless you accept data loss risk.",
    },
    "mon_clock_drift_allowed": {
        "what": "Maximum clock drift (seconds) between monitors before health warnings.",
        "when_to_use": (
            "Ensure NTP/chrony is stable first. Increase only as a temporary mitigation "
            "while fixing time sync."
        ),
    },
    "mon_warn_on_pool_no_redundancy": {
        "what": "Warn when any pool has no redundancy (`size=1` or `min_size=1`).",
        "when_to_use": "Leave enabled in production.",
    },
    "mon_pg_stuck_threshold": {
        "what": "Seconds a PG may remain in a non-active state before HEALTH_ERR.",
        "when_to_use": (
            "Increase briefly during large recovery events; default suits most clusters."
        ),
    },
}

MGR_ENRICHMENTS: dict[str, dict[str, str]] = {
    "mgr_standby_modules": {
        "what": (
            "When `true`, standby MGR daemons serve the dashboard/API via HTTP redirect "
            "to the active manager."
        ),
        "when_to_use": (
            "Disable (`false`) when a load balancer fronts MGR endpoints — redirects "
            "often break behind LB private IPs."
        ),
        "example": (
            "```bash\n"
            "ceph config set mgr mgr_standby_modules false\n"
            "ceph config get mgr mgr_standby_modules\n"
            "```"
        ),
    },
    "mgr_stats_period": {
        "what": "Interval (seconds) between MGR cluster stat refreshes.",
        "when_to_use": (
            "Shorten for fresher dashboard metrics; lengthen on very large clusters "
            "to reduce MGR CPU load."
        ),
    },
    "mgr_module_path": {
        "what": "Directory where Ceph manager modules are loaded from.",
        "when_to_use": "Change only for custom module paths or non-packaged installs.",
    },
    "cephadm_path": {
        "what": "Path to the `cephadm` binary used by the cephadm orchestrator module.",
        "when_to_use": (
            "Set when cephadm is not in `$PATH` for the mgr daemon user "
            "(common with custom installs)."
        ),
        "example": (
            "```bash\n"
            'ceph config set mgr cephadm_path "/usr/sbin/cephadm"\n'
            "ceph config get mgr cephadm_path\n"
            "```"
        ),
    },
    "mgr_disabled_modules": {
        "what": "Comma-separated list of manager modules that must not be loaded.",
        "when_to_use": (
            "Disable unused modules to reduce attack surface and MGR startup time."
        ),
    },
    "mgr_max_pg_num_change": {
        "what": "Maximum PG count change the MGR balancer/autoscaler applies per iteration.",
        "when_to_use": (
            "Lower on busy clusters to avoid large placement churn; raise for faster "
            "PG convergence after expansion."
        ),
    },
    "mon_target_pg_per_osd": {
        "what": (
            "Target PGs per OSD for autoscaler and PG health warnings (also listed under "
            "MON cross-daemon settings in mgr config tables)."
        ),
        "when_to_use": (
            "Adjust when autoscaler consistently over/under-shards pools for your OSD count."
        ),
    },
}

MDS_ENRICHMENTS: dict[str, dict[str, str]] = {
    "mds_cache_memory_limit": {
        "what": (
            "Soft limit on MDS metadata cache memory (bytes). When exceeded, the MDS "
            "trims caps and may evict client sessions."
        ),
        "when_to_use": (
            "Raise for large working sets and many files; lower if MDS RSS causes OOM "
            "on constrained nodes."
        ),
        "finding_note": (
            "Watch `ceph fs status`, slow requests, and `mds_cache_trim_*` counters. "
            "Size MDS RAM ≥ 2× this limit in production."
        ),
    },
    "mds_bal_mode": {
        "what": (
            "MDS subtree balancer mode (`none`, `normal`, `aggressive`). Controls "
            "how aggressively metadata load is migrated between active MDS ranks."
        ),
        "when_to_use": (
            "Use `normal` for multi-active CephFS; `none` for single-MDS or while "
            "debugging balance churn."
        ),
        "example": (
            "```bash\n"
            "ceph config set mds mds_bal_mode normal\n"
            "ceph fs status\n"
            "```"
        ),
    },
    "mds_beacon_grace": {
        "what": (
            "Seconds the monitor waits after a missed MDS beacon before marking "
            "the rank laggy/failed."
        ),
        "when_to_use": (
            "Increase during network maintenance; decrease for faster MDS failover "
            "at the cost of false positives on slow nodes."
        ),
    },
    "mds_beacon_interval": {
        "what": "How often (seconds) an MDS sends beacons to monitors.",
        "when_to_use": "Rarely changed; must stay well below `mds_beacon_grace`.",
    },
    "mds_max_export_size": {
        "what": "Maximum size (bytes) of a single subtree export during MDS rebalancing.",
        "when_to_use": (
            "Lower to reduce latency spikes during balance; raise for faster migration "
            "on high-bandwidth networks."
        ),
    },
    "mds_session_cap_acquisition_throttle": {
        "what": "Throttle cap acquisition rate per client session to protect the MDS.",
        "when_to_use": (
            "Tune when clients stampede caps after MDS restart or when many small "
            "files are opened concurrently."
        ),
    },
    "mds_cap_revoke_eviction_timeout": {
        "what": (
            "Seconds to wait before evicting a client that holds caps after revoke."
        ),
        "when_to_use": (
            "Increase for legacy clients that respond slowly to cap revokes; decrease "
            "to reclaim metadata cache faster."
        ),
    },
    "mds_log_max_events": {
        "what": "Maximum journal events before the MDS forces a segment rollover.",
        "when_to_use": (
            "Advanced — affects journal segmentation and recovery time after crash."
        ),
    },
}

SUBSYSTEM_ENRICHMENTS: dict[str, dict[str, dict[str, str]]] = {
    "osd": OSD_ENRICHMENTS,
    "mon": MON_ENRICHMENTS,
    "mgr": MGR_ENRICHMENTS,
    "mds": MDS_ENRICHMENTS,
    "rgw": {
        "rgw_enable_apis": {
            "what": "Comma-separated list of enabled RGW APIs (s3, swift, admin, …).",
            "when_to_use": "Production: enable only APIs you expose. Lab: broader set for testing.",
            "important": "**Risk: High (security)** — exposing `admin` or unused APIs increases attack surface.",
            "finding_note": "Pair with firewall/LB rules and `rgw frontends` binding.",
        },
        "rgw_enable_rate_limit": {
            "what": "Enables per-user/bucket rate limiting in RGW.",
            "when_to_use": "Enable on public multi-tenant clusters; tune after observing 503 SlowDown rates.",
            "important": "**Risk: Medium** — misconfigured limits cause client-visible throttling.",
        },
        "rgw_cache_enabled": {
            "what": "In-memory metadata cache for RGW (users, buckets, stats).",
            "when_to_use": "Enable on most production RGW nodes; size with `rgw_cache_lru_size`.",
            "important": "**Risk: Low–Medium** — stale cache rarely affects correctness; watch memory.",
        },
    },
}
