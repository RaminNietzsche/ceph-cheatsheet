"""Hand-tuned deep-dive text for high-traffic OSD and MON options."""

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

SUBSYSTEM_ENRICHMENTS: dict[str, dict[str, dict[str, str]]] = {
    "osd": OSD_ENRICHMENTS,
    "mon": MON_ENRICHMENTS,
}
