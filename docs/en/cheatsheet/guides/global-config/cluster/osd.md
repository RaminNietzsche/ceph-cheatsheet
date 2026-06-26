# Osd

Global config deep dive — 174 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [osd_asio_thread_count](#osd_asio_thread_count) | `2` | Advanced | Performance |
| [osd_async_recovery_min_cost](#osd_async_recovery_min_cost) | `100` | Advanced | Performance |
| [osd_auto_mark_unfound_lost](#osd_auto_mark_unfound_lost) | `False` | Advanced | Performance |
| [osd_backoff_on_degraded](#osd_backoff_on_degraded) | `False` | Advanced | Performance |
| [osd_backoff_on_peering](#osd_backoff_on_peering) | `False` | Advanced | Performance |
| [osd_backoff_on_unfound](#osd_backoff_on_unfound) | `True` | Advanced | Performance |
| [osd_beacon_report_interval](#osd_beacon_report_interval) | `5_min` | Advanced | Performance |
| [osd_bench_duration](#osd_bench_duration) | `30` | Advanced | Performance |
| [osd_bench_large_size_max_throughput](#osd_bench_large_size_max_throughput) | `100_M` | Advanced | Performance |
| [osd_bench_max_block_size](#osd_bench_max_block_size) | `64_M` | Advanced | Performance |
| [osd_bench_small_size_max_iops](#osd_bench_small_size_max_iops) | `100` | Advanced | Performance |
| [osd_blkin_trace_all](#osd_blkin_trace_all) | `False` | Advanced | Performance |
| [osd_calc_pg_upmaps_aggressively](#osd_calc_pg_upmaps_aggressively) | `True` | Advanced | Performance |
| [osd_calc_pg_upmaps_aggressively_fast](#osd_calc_pg_upmaps_aggressively_fast) | `True` | Advanced | Performance |
| [osd_calc_pg_upmaps_local_fallback_retries](#osd_calc_pg_upmaps_local_fallback_retries) | `100` | Advanced | Performance |
| [osd_check_for_log_corruption](#osd_check_for_log_corruption) | `False` | Advanced | Performance |
| [osd_client_op_priority](#osd_client_op_priority) | `63` | Advanced | Performance |
| [osd_command_max_records](#osd_command_max_records) | `256` | Advanced | Performance |
| [osd_crush_chooseleaf_type](#osd_crush_chooseleaf_type) | `1` | Dev | Dev |
| [osd_debug_crash_on_ignored_backoff](#osd_debug_crash_on_ignored_backoff) | `False` | Dev | Dev |
| [osd_debug_deep_scrub_sleep](#osd_debug_deep_scrub_sleep) | `0` | Dev | Dev |
| [osd_debug_drop_ping_duration](#osd_debug_drop_ping_duration) | `0` | Dev | Dev |
| [osd_debug_drop_ping_probability](#osd_debug_drop_ping_probability) | `0` | Dev | Dev |
| [osd_debug_inject_copyfrom_error](#osd_debug_inject_copyfrom_error) | `False` | Dev | Dev |
| [osd_debug_inject_dispatch_delay_duration](#osd_debug_inject_dispatch_delay_duration) | `0.1` | Dev | Dev |
| [osd_debug_inject_dispatch_delay_probability](#osd_debug_inject_dispatch_delay_probability) | `0` | Dev | Dev |
| [osd_debug_misdirected_ops](#osd_debug_misdirected_ops) | `False` | Dev | Dev |
| [osd_debug_no_acting_change](#osd_debug_no_acting_change) | `False` | Dev | Dev |
| [osd_debug_no_purge_strays](#osd_debug_no_purge_strays) | `False` | Dev | Dev |
| [osd_debug_op_order](#osd_debug_op_order) | `False` | Dev | Dev |
| [osd_debug_pg_log_writeout](#osd_debug_pg_log_writeout) | `False` | Dev | Dev |
| [osd_debug_pretend_recovery_active](#osd_debug_pretend_recovery_active) | `False` | Dev | Dev |
| [osd_debug_random_push_read_error](#osd_debug_random_push_read_error) | `0` | Dev | Dev |
| [osd_debug_reject_backfill_probability](#osd_debug_reject_backfill_probability) | `0` | Dev | Dev |
| [osd_debug_shutdown](#osd_debug_shutdown) | `False` | Dev | Dev |
| [osd_debug_skip_full_check_in_backfill_reservation](#osd_debug_skip_full_check_in_backfill_reservation) | `False` | Dev | Dev |
| [osd_debug_skip_full_check_in_recovery](#osd_debug_skip_full_check_in_recovery) | `False` | Dev | Dev |
| [osd_debug_verify_cached_snaps](#osd_debug_verify_cached_snaps) | `False` | Dev | Dev |
| [osd_debug_verify_missing_on_start](#osd_debug_verify_missing_on_start) | `False` | Dev | Dev |
| [osd_debug_verify_snaps](#osd_debug_verify_snaps) | `False` | Dev | Dev |
| [osd_debug_verify_stray_on_activate](#osd_debug_verify_stray_on_activate) | `False` | Dev | Dev |
| [osd_default_data_pool_replay_window](#osd_default_data_pool_replay_window) | `45` | Advanced | Performance |
| [osd_default_notify_timeout](#osd_default_notify_timeout) | `30` | Advanced | Performance |
| [osd_discard_disconnected_ops](#osd_discard_disconnected_ops) | `True` | Advanced | Performance |
| [osd_enable_op_tracker](#osd_enable_op_tracker) | `True` | Advanced | Policy |
| [osd_erasure_code_plugins](#osd_erasure_code_plugins) | `0` | Advanced | Performance |
| [osd_failsafe_full_ratio](#osd_failsafe_full_ratio) | `0.97` | Advanced | Performance |
| [osd_fast_fail_on_connection_refused](#osd_fast_fail_on_connection_refused) | `True` | Advanced | Performance |
| [osd_fast_info](#osd_fast_info) | `True` | Advanced | Performance |
| [osd_fast_shutdown](#osd_fast_shutdown) | `True` | Advanced | Performance |
| [osd_fast_shutdown_notify_mon](#osd_fast_shutdown_notify_mon) | `True` | Advanced | Performance |
| [osd_fast_shutdown_timeout](#osd_fast_shutdown_timeout) | `15` | Advanced | Performance |
| [osd_force_auth_primary_missing_objects](#osd_force_auth_primary_missing_objects) | `100` | Advanced | Performance |
| [osd_force_recovery_pg_log_entries_factor](#osd_force_recovery_pg_log_entries_factor) | `1.3` | Dev | Dev |
| [osd_function_tracing](#osd_function_tracing) | `False` | Advanced | Performance |
| [osd_heartbeat_grace](#osd_heartbeat_grace) | `20` | Advanced | Performance |
| [osd_heartbeat_interval](#osd_heartbeat_interval) | `6` | Dev | Dev |
| [osd_heartbeat_min_healthy_ratio](#osd_heartbeat_min_healthy_ratio) | `0.33` | Advanced | Performance |
| [osd_heartbeat_min_size](#osd_heartbeat_min_size) | `2000` | Advanced | Performance |
| [osd_heartbeat_stale](#osd_heartbeat_stale) | `10_min` | Advanced | Performance |
| [osd_heartbeat_use_min_delay_socket](#osd_heartbeat_use_min_delay_socket) | `False` | Advanced | Performance |
| [osd_hit_set_max_size](#osd_hit_set_max_size) | `100000` | Advanced | Performance |
| [osd_hit_set_min_size](#osd_hit_set_min_size) | `1000` | Advanced | Performance |
| [osd_hit_set_namespace](#osd_hit_set_namespace) | `.ceph-internal` | Advanced | Performance |
| [osd_ignore_stale_divergent_priors](#osd_ignore_stale_divergent_priors) | `False` | Advanced | Performance |
| [osd_kill_backfill_at](#osd_kill_backfill_at) | `0` | Dev | Dev |
| [osd_loop_before_reset_tphandle](#osd_loop_before_reset_tphandle) | `64` | Advanced | Performance |
| [osd_map_dedup](#osd_map_dedup) | `True` | Advanced | Performance |
| [osd_map_message_max](#osd_map_message_max) | `40` | Advanced | Performance |
| [osd_map_message_max_bytes](#osd_map_message_max_bytes) | `10_M` | Advanced | Performance |
| [osd_max_attr_name_len](#osd_max_attr_name_len) | `100` | Advanced | Performance |
| [osd_max_attr_size](#osd_max_attr_size) | `0` | Advanced | Performance |
| [osd_max_object_name_len](#osd_max_object_name_len) | `2_K` | Advanced | Performance |
| [osd_max_object_namespace_len](#osd_max_object_namespace_len) | `256` | Advanced | Performance |
| [osd_max_object_size](#osd_max_object_size) | `128_M` | Advanced | Performance |
| [osd_max_omap_bytes_per_request](#osd_max_omap_bytes_per_request) | `1_G` | Advanced | Performance |
| [osd_max_omap_entries_per_request](#osd_max_omap_entries_per_request) | `1_K` | Advanced | Performance |
| [osd_max_pg_blocked_by](#osd_max_pg_blocked_by) | `16` | Advanced | Performance |
| [osd_max_pg_log_entries](#osd_max_pg_log_entries) | `10000` | Dev | Dev |
| [osd_max_pg_per_osd_hard_ratio](#osd_max_pg_per_osd_hard_ratio) | `3` | Advanced | Performance |
| [osd_max_snap_prune_intervals_per_epoch](#osd_max_snap_prune_intervals_per_epoch) | `512` | Dev | Dev |
| [osd_max_trimming_pgs](#osd_max_trimming_pgs) | `2` | Advanced | Performance |
| [osd_max_write_op_reply_len](#osd_max_write_op_reply_len) | `64` | Advanced | Performance |
| [osd_memory_base](#osd_memory_base) | `768_M` | Dev | Dev |
| [osd_memory_cache_min](#osd_memory_cache_min) | `128_M` | Dev | Dev |
| [osd_memory_cache_resize_interval](#osd_memory_cache_resize_interval) | `1` | Dev | Dev |
| [osd_memory_expected_fragmentation](#osd_memory_expected_fragmentation) | `0.15` | Dev | Dev |
| [osd_memory_target](#osd_memory_target) | `4_G` | Basic | Policy |
| [osd_memory_target_autotune](#osd_memory_target_autotune) | `False` | Advanced | Performance |
| [osd_memory_target_cgroup_limit_ratio](#osd_memory_target_cgroup_limit_ratio) | `0.8` | Advanced | Performance |
| [osd_min_pg_log_entries](#osd_min_pg_log_entries) | `250` | Dev | Dev |
| [osd_min_split_replica_read_size](#osd_min_split_replica_read_size) | `0` | Advanced | Performance |
| [osd_mon_heartbeat_interval](#osd_mon_heartbeat_interval) | `30` | Advanced | Performance |
| [osd_mon_heartbeat_stat_stale](#osd_mon_heartbeat_stat_stale) | `1_hr` | Advanced | Performance |
| [osd_mon_report_interval](#osd_mon_report_interval) | `5` | Advanced | Performance |
| [osd_mon_report_max_in_flight](#osd_mon_report_max_in_flight) | `2` | Advanced | Performance |
| [osd_mon_shutdown_timeout](#osd_mon_shutdown_timeout) | `5` | Advanced | Performance |
| [osd_num_op_tracker_shard](#osd_num_op_tracker_shard) | `32` | Advanced | Performance |
| [osd_object_clean_region_max_num_intervals](#osd_object_clean_region_max_num_intervals) | `10` | Dev | Dev |
| [osd_objecter_finishers](#osd_objecter_finishers) | `1` | Advanced | Performance |
| [osd_objectstore](#osd_objectstore) | `bluestore` | Advanced | Performance |
| [osd_objectstore_fuse](#osd_objectstore_fuse) | `False` | Advanced | Performance |
| [osd_objectstore_ideal_list_max](#osd_objectstore_ideal_list_max) | `64` | Advanced | Performance |
| [osd_objectstore_tracing](#osd_objectstore_tracing) | `False` | Advanced | Performance |
| [osd_op_complaint_time](#osd_op_complaint_time) | `30` | Advanced | Performance |
| [osd_op_history_duration](#osd_op_history_duration) | `600` | Advanced | Performance |
| [osd_op_history_size](#osd_op_history_size) | `20` | Advanced | Performance |
| [osd_op_history_slow_op_size](#osd_op_history_slow_op_size) | `20` | Advanced | Performance |
| [osd_op_history_slow_op_threshold](#osd_op_history_slow_op_threshold) | `10` | Advanced | Performance |
| [osd_op_log_threshold](#osd_op_log_threshold) | `5` | Advanced | Performance |
| [osd_peering_op_priority](#osd_peering_op_priority) | `255` | Dev | Dev |
| [osd_pg_delete_cost](#osd_pg_delete_cost) | `1_M` | Advanced | Performance |
| [osd_pg_delete_priority](#osd_pg_delete_priority) | `5` | Advanced | Performance |
| [osd_pg_epoch_persisted_max_stale](#osd_pg_epoch_persisted_max_stale) | `40` | Advanced | Performance |
| [osd_pg_log_dups_tracked](#osd_pg_log_dups_tracked) | `3000` | Dev | Dev |
| [osd_pg_log_trim_max](#osd_pg_log_trim_max) | `10000` | Advanced | Performance |
| [osd_pg_log_trim_min](#osd_pg_log_trim_min) | `100` | Dev | Dev |
| [osd_pg_max_concurrent_snap_trims](#osd_pg_max_concurrent_snap_trims) | `2` | Advanced | Performance |
| [osd_pg_object_context_cache_count](#osd_pg_object_context_cache_count) | `64` | Advanced | Performance |
| [osd_pg_stat_report_interval_max_epochs](#osd_pg_stat_report_interval_max_epochs) | `500` | Advanced | Performance |
| [osd_pg_stat_report_interval_max_seconds](#osd_pg_stat_report_interval_max_seconds) | `5` | Advanced | Performance |
| [osd_pool_default_cache_max_evict_check_size](#osd_pool_default_cache_max_evict_check_size) | `10` | Advanced | Performance |
| [osd_pool_default_cache_min_evict_age](#osd_pool_default_cache_min_evict_age) | `0` | Advanced | Performance |
| [osd_pool_default_cache_min_flush_age](#osd_pool_default_cache_min_flush_age) | `0` | Advanced | Performance |
| [osd_pool_default_cache_target_dirty_high_ratio](#osd_pool_default_cache_target_dirty_high_ratio) | `0.6` | Advanced | Performance |
| [osd_pool_default_cache_target_dirty_ratio](#osd_pool_default_cache_target_dirty_ratio) | `0.4` | Advanced | Performance |
| [osd_pool_default_cache_target_full_ratio](#osd_pool_default_cache_target_full_ratio) | `0.8` | Advanced | Performance |
| [osd_pool_default_crush_rule](#osd_pool_default_crush_rule) | `-1` | Advanced | Performance |
| [osd_pool_default_ec_fast_read](#osd_pool_default_ec_fast_read) | `False` | Advanced | Performance |
| [osd_pool_default_erasure_code_profile](#osd_pool_default_erasure_code_profile) | `plugin=isa technique=reed_sol_van k=2 m=2` | Advanced | Performance |
| [osd_pool_default_flag_bulk](#osd_pool_default_flag_bulk) | `False` | Advanced | Performance |
| [osd_pool_default_flag_ec_optimizations](#osd_pool_default_flag_ec_optimizations) | `False` | Advanced | Performance |
| [osd_pool_default_flag_hashpspool](#osd_pool_default_flag_hashpspool) | `True` | Advanced | Performance |
| [osd_pool_default_flag_nodelete](#osd_pool_default_flag_nodelete) | `False` | Advanced | Performance |
| [osd_pool_default_flag_nopgchange](#osd_pool_default_flag_nopgchange) | `False` | Advanced | Performance |
| [osd_pool_default_flag_nosizechange](#osd_pool_default_flag_nosizechange) | `False` | Advanced | Performance |
| [osd_pool_default_flags](#osd_pool_default_flags) | `0` | Dev | Dev |
| [osd_pool_default_hit_set_bloom_fpp](#osd_pool_default_hit_set_bloom_fpp) | `0.05` | Advanced | Performance |
| [osd_pool_default_min_size](#osd_pool_default_min_size) | `0` | Advanced | Performance |
| [osd_pool_default_pg_autoscale_mode](#osd_pool_default_pg_autoscale_mode) | `on` | Advanced | Performance |
| [osd_pool_default_pg_num](#osd_pool_default_pg_num) | `32` | Advanced | Performance |
| [osd_pool_default_pgp_num](#osd_pool_default_pgp_num) | `0` | Advanced | Performance |
| [osd_pool_default_read_lease_ratio](#osd_pool_default_read_lease_ratio) | `0.8` | Dev | Dev |
| [osd_pool_default_read_ratio](#osd_pool_default_read_ratio) | `70` | Advanced | Performance |
| [osd_pool_default_size](#osd_pool_default_size) | `3` | Advanced | Performance |
| [osd_pool_default_type](#osd_pool_default_type) | `replicated` | Advanced | Performance |
| [osd_pool_use_gmt_hitset](#osd_pool_use_gmt_hitset) | `True` | Dev | Dev |
| [osd_recovery_cost](#osd_recovery_cost) | `20_M` | Advanced | Performance |
| [osd_recovery_op_priority](#osd_recovery_op_priority) | `3` | Advanced | Performance |
| [osd_recovery_op_warn_multiple](#osd_recovery_op_warn_multiple) | `16` | Advanced | Performance |
| [osd_recovery_priority](#osd_recovery_priority) | `5` | Advanced | Performance |
| [osd_requested_scrub_priority](#osd_requested_scrub_priority) | `5` | Advanced | Performance |
| [osd_rollback_to_cluster_snap](#osd_rollback_to_cluster_snap) | `(empty)` | Advanced | Performance |
| [osd_scrub_cost](#osd_scrub_cost) | `50_M` | Advanced | Performance |
| [osd_scrub_event_cost](#osd_scrub_event_cost) | `4_K` | Advanced | Performance |
| [osd_scrub_priority](#osd_scrub_priority) | `5` | Advanced | Performance |
| [osd_shutdown_pgref_assert](#osd_shutdown_pgref_assert) | `False` | Advanced | Performance |
| [osd_skip_check_past_interval_bounds](#osd_skip_check_past_interval_bounds) | `False` | Dev | Dev |
| [osd_snap_trim_cost](#osd_snap_trim_cost) | `1_M` | Advanced | Performance |
| [osd_snap_trim_priority](#osd_snap_trim_priority) | `5` | Advanced | Performance |
| [osd_target_pg_log_entries_per_osd](#osd_target_pg_log_entries_per_osd) | `300000` | Dev | Dev |
| [osd_target_transaction_size](#osd_target_transaction_size) | `30` | Advanced | Performance |
| [osd_tier_default_cache_hit_set_count](#osd_tier_default_cache_hit_set_count) | `4` | Advanced | Performance |
| [osd_tier_default_cache_hit_set_grade_decay_rate](#osd_tier_default_cache_hit_set_grade_decay_rate) | `20` | Advanced | Performance |
| [osd_tier_default_cache_hit_set_period](#osd_tier_default_cache_hit_set_period) | `1200` | Advanced | Performance |
| [osd_tier_default_cache_hit_set_search_last_n](#osd_tier_default_cache_hit_set_search_last_n) | `1` | Advanced | Performance |
| [osd_tier_default_cache_hit_set_type](#osd_tier_default_cache_hit_set_type) | `bloom` | Advanced | Performance |
| [osd_tier_default_cache_min_read_recency_for_promote](#osd_tier_default_cache_min_read_recency_for_promote) | `1` | Advanced | Performance |
| [osd_tier_default_cache_min_write_recency_for_promote](#osd_tier_default_cache_min_write_recency_for_promote) | `1` | Advanced | Performance |
| [osd_tier_default_cache_mode](#osd_tier_default_cache_mode) | `writeback` | Advanced | Performance |
| [osd_tier_promote_max_bytes_sec](#osd_tier_promote_max_bytes_sec) | `5_M` | Advanced | Performance |
| [osd_tier_promote_max_objects_sec](#osd_tier_promote_max_objects_sec) | `25` | Advanced | Performance |
| [osd_tracing](#osd_tracing) | `False` | Advanced | Performance |
| [osd_use_stale_snap](#osd_use_stale_snap) | `False` | Advanced | Performance |

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, compatibility, operational defaults |
| **Capacity** | Disk layout, paths, sizing |
| **Performance** | Baseline → incremental change → monitor cluster |
| **Connectivity** | Nearest stable external endpoint |
| **Dev** | Keep upstream default in production |

**Shared tooling:**

```bash
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_asio_thread_count

| | |
|---|---|
| Type | Uint · default `2` · **Advanced** |
| Table | [osd.md#SP_osd_asio_thread_count](../../../config/global/osd.md#SP_osd_asio_thread_count) |

**What it does:** Size of thread pool for ASIO completions

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_asio_thread_count 2
ceph config get osd osd_asio_thread_count
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_asio_thread_count
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_async_recovery_min_cost

| | |
|---|---|
| Type | Uint · default `100` · **Advanced** |
| Table | [osd.md#SP_osd_async_recovery_min_cost](../../../config/global/osd.md#SP_osd_async_recovery_min_cost) |

**What it does:** A mixture measure of number of current log entries difference and historical missing objects, above which we switch to use asynchronous recovery when appropriate

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_async_recovery_min_cost 100
ceph config get osd osd_async_recovery_min_cost
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_async_recovery_min_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_auto_mark_unfound_lost

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_auto_mark_unfound_lost](../../../config/global/osd.md#SP_osd_auto_mark_unfound_lost) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_auto_mark_unfound_lost true
ceph config get osd osd_auto_mark_unfound_lost
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_auto_mark_unfound_lost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_backoff_on_degraded

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_backoff_on_degraded](../../../config/global/osd.md#SP_osd_backoff_on_degraded) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_backoff_on_degraded true
ceph config get osd osd_backoff_on_degraded
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_backoff_on_degraded
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_backoff_on_peering

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_backoff_on_peering](../../../config/global/osd.md#SP_osd_backoff_on_peering) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_backoff_on_peering true
ceph config get osd osd_backoff_on_peering
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_backoff_on_peering
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_backoff_on_unfound

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_backoff_on_unfound](../../../config/global/osd.md#SP_osd_backoff_on_unfound) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_backoff_on_unfound false
ceph config get osd osd_backoff_on_unfound
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_backoff_on_unfound
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_beacon_report_interval

| | |
|---|---|
| Type | Int · default `5_min` · **Advanced** |
| Table | [osd.md#SP_osd_beacon_report_interval](../../../config/global/osd.md#SP_osd_beacon_report_interval) |

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_beacon_report_interval 5_min
ceph config get osd osd_beacon_report_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_beacon_report_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_bench_duration

| | |
|---|---|
| Type | Uint · default `30` · **Advanced** |
| Table | [osd.md#SP_osd_bench_duration](../../../config/global/osd.md#SP_osd_bench_duration) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_bench_duration 30
ceph config get osd osd_bench_duration
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_bench_duration
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_bench_large_size_max_throughput

| | |
|---|---|
| Type | Size · default `100_M` · **Advanced** |
| Table | [osd.md#SP_osd_bench_large_size_max_throughput](../../../config/global/osd.md#SP_osd_bench_large_size_max_throughput) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_bench_large_size_max_throughput 100_M
ceph config get osd osd_bench_large_size_max_throughput
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_bench_large_size_max_throughput
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_bench_max_block_size

| | |
|---|---|
| Type | Size · default `64_M` · **Advanced** |
| Table | [osd.md#SP_osd_bench_max_block_size](../../../config/global/osd.md#SP_osd_bench_max_block_size) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_bench_max_block_size 64_M
ceph config get osd osd_bench_max_block_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_bench_max_block_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_bench_small_size_max_iops

| | |
|---|---|
| Type | Uint · default `100` · **Advanced** |
| Table | [osd.md#SP_osd_bench_small_size_max_iops](../../../config/global/osd.md#SP_osd_bench_small_size_max_iops) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_bench_small_size_max_iops 100
ceph config get osd osd_bench_small_size_max_iops
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_bench_small_size_max_iops
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_blkin_trace_all

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_blkin_trace_all](../../../config/global/osd.md#SP_osd_blkin_trace_all) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_blkin_trace_all true
ceph config get osd osd_blkin_trace_all
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_blkin_trace_all
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_calc_pg_upmaps_aggressively

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_calc_pg_upmaps_aggressively](../../../config/global/osd.md#SP_osd_calc_pg_upmaps_aggressively) |

**What it does:** Try to calculate PG upmaps more aggressively, e.g., by doing a fairly exhaustive search of existing PGs that can be unmapped or upmapped

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_calc_pg_upmaps_aggressively false
ceph config get osd osd_calc_pg_upmaps_aggressively
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_calc_pg_upmaps_aggressively
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_calc_pg_upmaps_aggressively_fast

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_calc_pg_upmaps_aggressively_fast](../../../config/global/osd.md#SP_osd_calc_pg_upmaps_aggressively_fast) |

**What it does:** Prevent very long (>10 minutes) calculations in some extreme cases (applicable only to aggressive mode)

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_calc_pg_upmaps_aggressively_fast false
ceph config get osd osd_calc_pg_upmaps_aggressively_fast
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_calc_pg_upmaps_aggressively_fast
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_calc_pg_upmaps_local_fallback_retries

| | |
|---|---|
| Type | Uint · default `100` · **Advanced** |
| Table | [osd.md#SP_osd_calc_pg_upmaps_local_fallback_retries](../../../config/global/osd.md#SP_osd_calc_pg_upmaps_local_fallback_retries) |

**What it does:** Maximum number of PGs we can attempt to unmap or upmap for a specific overfull or underfull OSD per iteration

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_calc_pg_upmaps_local_fallback_retries 100
ceph config get osd osd_calc_pg_upmaps_local_fallback_retries
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_calc_pg_upmaps_local_fallback_retries
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_check_for_log_corruption

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_check_for_log_corruption](../../../config/global/osd.md#SP_osd_check_for_log_corruption) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_check_for_log_corruption true
ceph config get osd osd_check_for_log_corruption
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_check_for_log_corruption
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_client_op_priority

| | |
|---|---|
| Type | Uint · default `63` · **Advanced** |
| Table | [osd.md#SP_osd_client_op_priority](../../../config/global/osd.md#SP_osd_client_op_priority) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_client_op_priority 63
ceph config get osd osd_client_op_priority
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `63`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_client_op_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_command_max_records

| | |
|---|---|
| Type | Int · default `256` · **Advanced** |
| Table | [osd.md#SP_osd_command_max_records](../../../config/global/osd.md#SP_osd_command_max_records) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_command_max_records 256
ceph config get osd osd_command_max_records
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `256`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_command_max_records
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_crush_chooseleaf_type

| | |
|---|---|
| Type | Int · default `1` · **Dev** |
| Table | [osd.md#SP_osd_crush_chooseleaf_type](../../../config/global/osd.md#SP_osd_crush_chooseleaf_type) |

**What it does:** default chooseleaf type for osdmaptool --create

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_crush_chooseleaf_type 1
ceph config get osd osd_crush_chooseleaf_type
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_crash_on_ignored_backoff

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_debug_crash_on_ignored_backoff](../../../config/global/osd.md#SP_osd_debug_crash_on_ignored_backoff) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_crash_on_ignored_backoff true
ceph config get osd osd_debug_crash_on_ignored_backoff
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_deep_scrub_sleep

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [osd.md#SP_osd_debug_deep_scrub_sleep](../../../config/global/osd.md#SP_osd_debug_deep_scrub_sleep) |

**What it does:** Inject an expensive sleep during deep scrub IO to make it easier to induce preemption

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_deep_scrub_sleep 0
ceph config get osd osd_debug_deep_scrub_sleep
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_drop_ping_duration

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [osd.md#SP_osd_debug_drop_ping_duration](../../../config/global/osd.md#SP_osd_debug_drop_ping_duration) |

**What it does:** N/A

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_drop_ping_duration 64
ceph config get osd osd_debug_drop_ping_duration
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_drop_ping_probability

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [osd.md#SP_osd_debug_drop_ping_probability](../../../config/global/osd.md#SP_osd_debug_drop_ping_probability) |

**What it does:** N/A

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_drop_ping_probability 0
ceph config get osd osd_debug_drop_ping_probability
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_inject_copyfrom_error

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_debug_inject_copyfrom_error](../../../config/global/osd.md#SP_osd_debug_inject_copyfrom_error) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_inject_copyfrom_error true
ceph config get osd osd_debug_inject_copyfrom_error
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_inject_dispatch_delay_duration

| | |
|---|---|
| Type | Float · default `0.1` · **Dev** |
| Table | [osd.md#SP_osd_debug_inject_dispatch_delay_duration](../../../config/global/osd.md#SP_osd_debug_inject_dispatch_delay_duration) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_inject_dispatch_delay_duration 0.1
ceph config get osd osd_debug_inject_dispatch_delay_duration
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_inject_dispatch_delay_probability

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [osd.md#SP_osd_debug_inject_dispatch_delay_probability](../../../config/global/osd.md#SP_osd_debug_inject_dispatch_delay_probability) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_inject_dispatch_delay_probability 0
ceph config get osd osd_debug_inject_dispatch_delay_probability
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_misdirected_ops

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_debug_misdirected_ops](../../../config/global/osd.md#SP_osd_debug_misdirected_ops) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_misdirected_ops true
ceph config get osd osd_debug_misdirected_ops
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_no_acting_change

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_debug_no_acting_change](../../../config/global/osd.md#SP_osd_debug_no_acting_change) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_no_acting_change true
ceph config get osd osd_debug_no_acting_change
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_no_purge_strays

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_debug_no_purge_strays](../../../config/global/osd.md#SP_osd_debug_no_purge_strays) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_no_purge_strays true
ceph config get osd osd_debug_no_purge_strays
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_op_order

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_debug_op_order](../../../config/global/osd.md#SP_osd_debug_op_order) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_op_order true
ceph config get osd osd_debug_op_order
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_pg_log_writeout

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_debug_pg_log_writeout](../../../config/global/osd.md#SP_osd_debug_pg_log_writeout) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_pg_log_writeout true
ceph config get osd osd_debug_pg_log_writeout
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_pretend_recovery_active

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_debug_pretend_recovery_active](../../../config/global/osd.md#SP_osd_debug_pretend_recovery_active) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_pretend_recovery_active true
ceph config get osd osd_debug_pretend_recovery_active
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_random_push_read_error

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [osd.md#SP_osd_debug_random_push_read_error](../../../config/global/osd.md#SP_osd_debug_random_push_read_error) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_random_push_read_error 0
ceph config get osd osd_debug_random_push_read_error
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_reject_backfill_probability

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [osd.md#SP_osd_debug_reject_backfill_probability](../../../config/global/osd.md#SP_osd_debug_reject_backfill_probability) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_reject_backfill_probability 0
ceph config get osd osd_debug_reject_backfill_probability
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_shutdown

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_debug_shutdown](../../../config/global/osd.md#SP_osd_debug_shutdown) |

**What it does:** Turn up debug levels during shutdown

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_shutdown true
ceph config get osd osd_debug_shutdown
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_skip_full_check_in_backfill_reservation

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_debug_skip_full_check_in_backfill_reservation](../../../config/global/osd.md#SP_osd_debug_skip_full_check_in_backfill_reservation) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_skip_full_check_in_backfill_reservation true
ceph config get osd osd_debug_skip_full_check_in_backfill_reservation
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_skip_full_check_in_recovery

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_debug_skip_full_check_in_recovery](../../../config/global/osd.md#SP_osd_debug_skip_full_check_in_recovery) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_skip_full_check_in_recovery true
ceph config get osd osd_debug_skip_full_check_in_recovery
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_verify_cached_snaps

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_debug_verify_cached_snaps](../../../config/global/osd.md#SP_osd_debug_verify_cached_snaps) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_verify_cached_snaps true
ceph config get osd osd_debug_verify_cached_snaps
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_verify_missing_on_start

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_debug_verify_missing_on_start](../../../config/global/osd.md#SP_osd_debug_verify_missing_on_start) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_verify_missing_on_start true
ceph config get osd osd_debug_verify_missing_on_start
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_verify_snaps

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_debug_verify_snaps](../../../config/global/osd.md#SP_osd_debug_verify_snaps) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_verify_snaps true
ceph config get osd osd_debug_verify_snaps
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_verify_stray_on_activate

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_debug_verify_stray_on_activate](../../../config/global/osd.md#SP_osd_debug_verify_stray_on_activate) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_verify_stray_on_activate true
ceph config get osd osd_debug_verify_stray_on_activate
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_default_data_pool_replay_window

| | |
|---|---|
| Type | Int · default `45` · **Advanced** |
| Table | [osd.md#SP_osd_default_data_pool_replay_window](../../../config/global/osd.md#SP_osd_default_data_pool_replay_window) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_default_data_pool_replay_window 45
ceph config get osd osd_default_data_pool_replay_window
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `45`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_default_data_pool_replay_window
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_default_notify_timeout

| | |
|---|---|
| Type | Uint · default `30` · **Advanced** |
| Table | [osd.md#SP_osd_default_notify_timeout](../../../config/global/osd.md#SP_osd_default_notify_timeout) |

**What it does:** default number of seconds after which notify propagation times out. used if a client has not specified other value

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_default_notify_timeout 30
ceph config get osd osd_default_notify_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_default_notify_timeout
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_discard_disconnected_ops

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_discard_disconnected_ops](../../../config/global/osd.md#SP_osd_discard_disconnected_ops) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_discard_disconnected_ops false
ceph config get osd osd_discard_disconnected_ops
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_discard_disconnected_ops
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_enable_op_tracker

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_enable_op_tracker](../../../config/global/osd.md#SP_osd_enable_op_tracker) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_enable_op_tracker false
ceph config get osd osd_enable_op_tracker
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_enable_op_tracker
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_erasure_code_plugins

| | |
|---|---|
| Type | Str · default `0` · **Advanced** · **STARTUP** (restart required) |
| Table | [osd.md#SP_osd_erasure_code_plugins](../../../config/global/osd.md#SP_osd_erasure_code_plugins) |

**What it does:** Erasure code plugins to load

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_erasure_code_plugins "example"
ceph config get osd osd_erasure_code_plugins
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_erasure_code_plugins
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_failsafe_full_ratio

| | |
|---|---|
| Type | Float · default `0.97` · **Advanced** |
| Table | [osd.md#SP_osd_failsafe_full_ratio](../../../config/global/osd.md#SP_osd_failsafe_full_ratio) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_failsafe_full_ratio 0.97
ceph config get osd osd_failsafe_full_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.97`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_failsafe_full_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_fast_fail_on_connection_refused

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_fast_fail_on_connection_refused](../../../config/global/osd.md#SP_osd_fast_fail_on_connection_refused) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_fast_fail_on_connection_refused false
ceph config get osd osd_fast_fail_on_connection_refused
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_fast_fail_on_connection_refused
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_fast_info

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_fast_info](../../../config/global/osd.md#SP_osd_fast_info) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_fast_info false
ceph config get osd osd_fast_info
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_fast_info
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_fast_shutdown

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_fast_shutdown](../../../config/global/osd.md#SP_osd_fast_shutdown) |

**What it does:** Fast, immediate shutdown Setting this to false makes the OSD do a slower teardown of all state when it receives a SIGINT or SIGTERM or when shutting down for any other reason. That slow shutdown is primarilyy useful for doing memory leak checking with valgrind.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_fast_shutdown false
ceph config get osd osd_fast_shutdown
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_fast_shutdown
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_fast_shutdown_notify_mon

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_fast_shutdown_notify_mon](../../../config/global/osd.md#SP_osd_fast_shutdown_notify_mon) |

**What it does:** Tell the Monitors about OSD shutdown on immediate shutdown Tell the Monitors the OSD is shutting down on immediate shutdown. This helps with cluster log messages from other OSDs reporting it immediately failed.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_fast_shutdown_notify_mon false
ceph config get osd osd_fast_shutdown_notify_mon
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_fast_shutdown_notify_mon
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_fast_shutdown_timeout

| | |
|---|---|
| Type | Int · default `15` · **Advanced** |
| Table | [osd.md#SP_osd_fast_shutdown_timeout](../../../config/global/osd.md#SP_osd_fast_shutdown_timeout) |

**What it does:** Timeout in seconds for osd fast-shutdown (0 is unlimited)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_fast_shutdown_timeout 15
ceph config get osd osd_fast_shutdown_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `15`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_fast_shutdown_timeout
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_force_auth_primary_missing_objects

| | |
|---|---|
| Type | Uint · default `100` · **Advanced** |
| Table | [osd.md#SP_osd_force_auth_primary_missing_objects](../../../config/global/osd.md#SP_osd_force_auth_primary_missing_objects) |

**What it does:** Approximate missing objects above which to force auth_log_shard to be primary temporarily

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_force_auth_primary_missing_objects 100
ceph config get osd osd_force_auth_primary_missing_objects
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_force_auth_primary_missing_objects
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_force_recovery_pg_log_entries_factor

| | |
|---|---|
| Type | Float · default `1.3` · **Dev** |
| Table | [osd.md#SP_osd_force_recovery_pg_log_entries_factor](../../../config/global/osd.md#SP_osd_force_recovery_pg_log_entries_factor) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_force_recovery_pg_log_entries_factor 1.3
ceph config get osd osd_force_recovery_pg_log_entries_factor
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1.3`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_function_tracing

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_function_tracing](../../../config/global/osd.md#SP_osd_function_tracing) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_function_tracing true
ceph config get osd osd_function_tracing
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_function_tracing
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_heartbeat_grace

| | |
|---|---|
| Type | Int · default `20` · **Advanced** |
| Table | [osd.md#SP_osd_heartbeat_grace](../../../config/global/osd.md#SP_osd_heartbeat_grace) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_heartbeat_grace 20
ceph config get osd osd_heartbeat_grace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_heartbeat_grace
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_heartbeat_interval

| | |
|---|---|
| Type | Int · default `6` · **Dev** |
| Table | [osd.md#SP_osd_heartbeat_interval](../../../config/global/osd.md#SP_osd_heartbeat_interval) |

**What it does:** Interval (in seconds) between peer pings

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_heartbeat_interval 6
ceph config get osd osd_heartbeat_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`6`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_heartbeat_min_healthy_ratio

| | |
|---|---|
| Type | Float · default `0.33` · **Advanced** |
| Table | [osd.md#SP_osd_heartbeat_min_healthy_ratio](../../../config/global/osd.md#SP_osd_heartbeat_min_healthy_ratio) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_heartbeat_min_healthy_ratio 0.33
ceph config get osd osd_heartbeat_min_healthy_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.33`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_heartbeat_min_healthy_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_heartbeat_min_size

| | |
|---|---|
| Type | Size · default `2000` · **Advanced** |
| Table | [osd.md#SP_osd_heartbeat_min_size](../../../config/global/osd.md#SP_osd_heartbeat_min_size) |

**What it does:** Minimum heartbeat packet size in bytes. Will padd if the heartbeat packet is smaller than this. This helps identify host and switch MTU configuration issues when jumbo frames are in use.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_heartbeat_min_size 2000
ceph config get osd osd_heartbeat_min_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_heartbeat_min_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_heartbeat_stale

| | |
|---|---|
| Type | Int · default `10_min` · **Advanced** |
| Table | [osd.md#SP_osd_heartbeat_stale](../../../config/global/osd.md#SP_osd_heartbeat_stale) |

**What it does:** Interval (in seconds) we mark an unresponsive heartbeat peer as stale. Automatically mark unresponsive heartbeat sessions as stale and tear them down. The primary benefit is that OSD doesn't need to keep a flood of blocked heartbeat messages around in memory.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_heartbeat_stale 10_min
ceph config get osd osd_heartbeat_stale
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_heartbeat_stale
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_heartbeat_use_min_delay_socket

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_heartbeat_use_min_delay_socket](../../../config/global/osd.md#SP_osd_heartbeat_use_min_delay_socket) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_heartbeat_use_min_delay_socket true
ceph config get osd osd_heartbeat_use_min_delay_socket
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_heartbeat_use_min_delay_socket
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_hit_set_max_size

| | |
|---|---|
| Type | Int · default `100000` · **Advanced** |
| Table | [osd.md#SP_osd_hit_set_max_size](../../../config/global/osd.md#SP_osd_hit_set_max_size) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_hit_set_max_size 100000
ceph config get osd osd_hit_set_max_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_hit_set_max_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_hit_set_min_size

| | |
|---|---|
| Type | Int · default `1000` · **Advanced** |
| Table | [osd.md#SP_osd_hit_set_min_size](../../../config/global/osd.md#SP_osd_hit_set_min_size) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_hit_set_min_size 1000
ceph config get osd osd_hit_set_min_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_hit_set_min_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_hit_set_namespace

| | |
|---|---|
| Type | Str · default `.ceph-internal` · **Advanced** |
| Table | [osd.md#SP_osd_hit_set_namespace](../../../config/global/osd.md#SP_osd_hit_set_namespace) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_hit_set_namespace ".ceph-internal"
ceph config get osd osd_hit_set_namespace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `.ceph-internal`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_hit_set_namespace
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_ignore_stale_divergent_priors

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_ignore_stale_divergent_priors](../../../config/global/osd.md#SP_osd_ignore_stale_divergent_priors) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_ignore_stale_divergent_priors true
ceph config get osd osd_ignore_stale_divergent_priors
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_ignore_stale_divergent_priors
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_kill_backfill_at

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [osd.md#SP_osd_kill_backfill_at](../../../config/global/osd.md#SP_osd_kill_backfill_at) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_kill_backfill_at 64
ceph config get osd osd_kill_backfill_at
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_loop_before_reset_tphandle

| | |
|---|---|
| Type | Uint · default `64` · **Advanced** |
| Table | [osd.md#SP_osd_loop_before_reset_tphandle](../../../config/global/osd.md#SP_osd_loop_before_reset_tphandle) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_loop_before_reset_tphandle 64
ceph config get osd osd_loop_before_reset_tphandle
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_loop_before_reset_tphandle
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_map_dedup

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_map_dedup](../../../config/global/osd.md#SP_osd_map_dedup) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_map_dedup false
ceph config get osd osd_map_dedup
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_map_dedup
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_map_message_max

| | |
|---|---|
| Type | Int · default `40` · **Advanced** |
| Table | [osd.md#SP_osd_map_message_max](../../../config/global/osd.md#SP_osd_map_message_max) |

**What it does:** Maximum number of OSDMaps to include in a single message

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_map_message_max 40
ceph config get osd osd_map_message_max
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `40`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_map_message_max
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_map_message_max_bytes

| | |
|---|---|
| Type | Size · default `10_M` · **Advanced** |
| Table | [osd.md#SP_osd_map_message_max_bytes](../../../config/global/osd.md#SP_osd_map_message_max_bytes) |

**What it does:** Maximum number of bytes worth of OSDMaps to include in a single message

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_map_message_max_bytes 10_M
ceph config get osd osd_map_message_max_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_map_message_max_bytes
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_attr_name_len

| | |
|---|---|
| Type | Uint · default `100` · **Advanced** |
| Table | [osd.md#SP_osd_max_attr_name_len](../../../config/global/osd.md#SP_osd_max_attr_name_len) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_max_attr_name_len 100
ceph config get osd osd_max_attr_name_len
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_attr_name_len
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_attr_size

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_max_attr_size](../../../config/global/osd.md#SP_osd_max_attr_size) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_max_attr_size 64
ceph config get osd osd_max_attr_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_attr_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_object_name_len

| | |
|---|---|
| Type | Uint · default `2_K` · **Advanced** |
| Table | [osd.md#SP_osd_max_object_name_len](../../../config/global/osd.md#SP_osd_max_object_name_len) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_max_object_name_len 2_K
ceph config get osd osd_max_object_name_len
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_object_name_len
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_object_namespace_len

| | |
|---|---|
| Type | Uint · default `256` · **Advanced** |
| Table | [osd.md#SP_osd_max_object_namespace_len](../../../config/global/osd.md#SP_osd_max_object_namespace_len) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_max_object_namespace_len 256
ceph config get osd osd_max_object_namespace_len
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `256`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_object_namespace_len
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_object_size

| | |
|---|---|
| Type | Size · default `128_M` · **Advanced** |
| Table | [osd.md#SP_osd_max_object_size](../../../config/global/osd.md#SP_osd_max_object_size) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_max_object_size 128_M
ceph config get osd osd_max_object_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `128_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_object_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_omap_bytes_per_request

| | |
|---|---|
| Type | Size · default `1_G` · **Advanced** |
| Table | [osd.md#SP_osd_max_omap_bytes_per_request](../../../config/global/osd.md#SP_osd_max_omap_bytes_per_request) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_max_omap_bytes_per_request 1_G
ceph config get osd osd_max_omap_bytes_per_request
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_G`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_omap_bytes_per_request
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_omap_entries_per_request

| | |
|---|---|
| Type | Uint · default `1_K` · **Advanced** |
| Table | [osd.md#SP_osd_max_omap_entries_per_request](../../../config/global/osd.md#SP_osd_max_omap_entries_per_request) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_max_omap_entries_per_request 1_K
ceph config get osd osd_max_omap_entries_per_request
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_omap_entries_per_request
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_pg_blocked_by

| | |
|---|---|
| Type | Uint · default `16` · **Advanced** |
| Table | [osd.md#SP_osd_max_pg_blocked_by](../../../config/global/osd.md#SP_osd_max_pg_blocked_by) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_max_pg_blocked_by 16
ceph config get osd osd_max_pg_blocked_by
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `16`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_pg_blocked_by
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_pg_log_entries

| | |
|---|---|
| Type | Uint · default `10000` · **Dev** |
| Table | [osd.md#SP_osd_max_pg_log_entries](../../../config/global/osd.md#SP_osd_max_pg_log_entries) |

**What it does:** Maximum number of entries to maintain in the PG log

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_max_pg_log_entries 10000
ceph config get osd osd_max_pg_log_entries
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`10000`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_max_pg_per_osd_hard_ratio

| | |
|---|---|
| Type | Float · default `3` · **Advanced** |
| Table | [osd.md#SP_osd_max_pg_per_osd_hard_ratio](../../../config/global/osd.md#SP_osd_max_pg_per_osd_hard_ratio) |

**What it does:** Maximum multiple of mon_max_pg_per_osd PGs an OSD will allow An OSD will refuse to instantiate a PG if the number of PGs it serves exceeds this number.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_max_pg_per_osd_hard_ratio 3
ceph config get osd osd_max_pg_per_osd_hard_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_pg_per_osd_hard_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_snap_prune_intervals_per_epoch

| | |
|---|---|
| Type | Uint · default `512` · **Dev** |
| Table | [osd.md#SP_osd_max_snap_prune_intervals_per_epoch](../../../config/global/osd.md#SP_osd_max_snap_prune_intervals_per_epoch) |

**What it does:** Max number of snap intervals to report to mgr in pg_stat_t

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_max_snap_prune_intervals_per_epoch 512
ceph config get osd osd_max_snap_prune_intervals_per_epoch
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`512`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_max_trimming_pgs

| | |
|---|---|
| Type | Uint · default `2` · **Advanced** |
| Table | [osd.md#SP_osd_max_trimming_pgs](../../../config/global/osd.md#SP_osd_max_trimming_pgs) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_max_trimming_pgs 2
ceph config get osd osd_max_trimming_pgs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_trimming_pgs
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_write_op_reply_len

| | |
|---|---|
| Type | Size · default `64` · **Advanced** |
| Table | [osd.md#SP_osd_max_write_op_reply_len](../../../config/global/osd.md#SP_osd_max_write_op_reply_len) |

**What it does:** Max size of the per-op payload for requests with the RETURNVEC flag set This value caps the amount of data (per op; a request may have many ops) that will be sent back to the client and recorded in the PG log.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_max_write_op_reply_len 64
ceph config get osd osd_max_write_op_reply_len
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_write_op_reply_len
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_memory_base

| | |
|---|---|
| Type | Size · default `768_M` · **Dev** |
| Table | [osd.md#SP_osd_memory_base](../../../config/global/osd.md#SP_osd_memory_base) |

**What it does:** When TCMalloc and cache autotuning are enabled, estimate the minimum amount of memory in bytes the OSD will need.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_memory_base 768_M
ceph config get osd osd_memory_base
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`768_M`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_memory_cache_min

| | |
|---|---|
| Type | Size · default `128_M` · **Dev** |
| Table | [osd.md#SP_osd_memory_cache_min](../../../config/global/osd.md#SP_osd_memory_cache_min) |

**What it does:** When TCMalloc and cache autotuning are enabled, set the minimum amount of memory used for caches.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_memory_cache_min 128_M
ceph config get osd osd_memory_cache_min
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`128_M`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_memory_cache_resize_interval

| | |
|---|---|
| Type | Float · default `1` · **Dev** |
| Table | [osd.md#SP_osd_memory_cache_resize_interval](../../../config/global/osd.md#SP_osd_memory_cache_resize_interval) |

**What it does:** When TCMalloc and cache autotuning are enabled, wait this many seconds between resizing caches.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_memory_cache_resize_interval 1
ceph config get osd osd_memory_cache_resize_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_memory_expected_fragmentation

| | |
|---|---|
| Type | Float · default `0.15` · **Dev** |
| Table | [osd.md#SP_osd_memory_expected_fragmentation](../../../config/global/osd.md#SP_osd_memory_expected_fragmentation) |

**What it does:** When TCMalloc and cache autotuning are enabled, estimate the percent of memory fragmentation.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_memory_expected_fragmentation 0.15
ceph config get osd osd_memory_expected_fragmentation
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.15`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_memory_target

| | |
|---|---|
| Type | Size · default `4_G` · **Basic** |
| Table | [osd.md#SP_osd_memory_target](../../../config/global/osd.md#SP_osd_memory_target) |

**What it does:** When TCMalloc and cache autotuning are enabled, try to keep this many bytes mapped in memory. The minimum value must be at least equal to osd_memory_base + osd_memory_cache_min.

**When to use:** Core Global behavior — review before changing in production.

**Example:**

```bash
ceph config set osd osd_memory_target 4_G
ceph config get osd osd_memory_target
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `4_G` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_memory_target
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_memory_target_autotune

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_memory_target_autotune](../../../config/global/osd.md#SP_osd_memory_target_autotune) |

**What it does:** If enabled, allow the orchestrator to automatically tune osd_memory_target at host granularity based on available memory, the number of OSDs provisioned on the host, other daemons provisioned on the host, and mgr/cephadm/autotune_memory_target_ratio

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Related options:**

- [`osd_memory_target`](../../../config/global/osd.md#SP_osd_memory_target)

**Example:**

```bash
ceph config set osd osd_memory_target_autotune true
ceph config get osd osd_memory_target_autotune
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_memory_target_autotune
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_memory_target_cgroup_limit_ratio

| | |
|---|---|
| Type | Float · default `0.8` · **Advanced** |
| Table | [osd.md#SP_osd_memory_target_cgroup_limit_ratio](../../../config/global/osd.md#SP_osd_memory_target_cgroup_limit_ratio) |

**What it does:** Set the default value for osd_memory_target to the cgroup memory limit (if set) times this value A value of 0 disables this feature.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Related options:**

- [`osd_memory_target`](../../../config/global/osd.md#SP_osd_memory_target)

**Example:**

```bash
ceph config set osd osd_memory_target_cgroup_limit_ratio 0.8
ceph config get osd osd_memory_target_cgroup_limit_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.8`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `1`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_memory_target_cgroup_limit_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_min_pg_log_entries

| | |
|---|---|
| Type | Uint · default `250` · **Dev** |
| Table | [osd.md#SP_osd_min_pg_log_entries](../../../config/global/osd.md#SP_osd_min_pg_log_entries) |

**What it does:** Minimum number of entries to maintain in the PG log

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_min_pg_log_entries 250
ceph config get osd osd_min_pg_log_entries
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`250`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_min_split_replica_read_size

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_min_split_replica_read_size](../../../config/global/osd.md#SP_osd_min_split_replica_read_size) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_min_split_replica_read_size 64
ceph config get osd osd_min_split_replica_read_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_min_split_replica_read_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mon_heartbeat_interval

| | |
|---|---|
| Type | Int · default `30` · **Advanced** |
| Table | [osd.md#SP_osd_mon_heartbeat_interval](../../../config/global/osd.md#SP_osd_mon_heartbeat_interval) |

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_mon_heartbeat_interval 30
ceph config get osd osd_mon_heartbeat_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mon_heartbeat_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mon_heartbeat_stat_stale

| | |
|---|---|
| Type | Int · default `1_hr` · **Advanced** |
| Table | [osd.md#SP_osd_mon_heartbeat_stat_stale](../../../config/global/osd.md#SP_osd_mon_heartbeat_stat_stale) |

**What it does:** Stop reporting on heartbeat ping times not updated for this many seconds. Stop reporting on old heartbeat information unless this is set to zero

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_mon_heartbeat_stat_stale 1_hr
ceph config get osd osd_mon_heartbeat_stat_stale
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_hr`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mon_heartbeat_stat_stale
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mon_report_interval

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [osd.md#SP_osd_mon_report_interval](../../../config/global/osd.md#SP_osd_mon_report_interval) |

**What it does:** Frequency of OSD reports to mon for peer failures, fullness status changes

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_mon_report_interval 5
ceph config get osd osd_mon_report_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mon_report_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mon_report_max_in_flight

| | |
|---|---|
| Type | Int · default `2` · **Advanced** |
| Table | [osd.md#SP_osd_mon_report_max_in_flight](../../../config/global/osd.md#SP_osd_mon_report_max_in_flight) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_mon_report_max_in_flight 2
ceph config get osd osd_mon_report_max_in_flight
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mon_report_max_in_flight
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mon_shutdown_timeout

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [osd.md#SP_osd_mon_shutdown_timeout](../../../config/global/osd.md#SP_osd_mon_shutdown_timeout) |

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_mon_shutdown_timeout 5
ceph config get osd osd_mon_shutdown_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mon_shutdown_timeout
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_num_op_tracker_shard

| | |
|---|---|
| Type | Uint · default `32` · **Advanced** |
| Table | [osd.md#SP_osd_num_op_tracker_shard](../../../config/global/osd.md#SP_osd_num_op_tracker_shard) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_num_op_tracker_shard 32
ceph config get osd osd_num_op_tracker_shard
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `32`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_num_op_tracker_shard
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_object_clean_region_max_num_intervals

| | |
|---|---|
| Type | Int · default `10` · **Dev** |
| Table | [osd.md#SP_osd_object_clean_region_max_num_intervals](../../../config/global/osd.md#SP_osd_object_clean_region_max_num_intervals) |

**What it does:** Number of intervals in clean_offsets Partial recovery uses multiple intervals to record the clean part of the objectwhen the number of intervals is greater than osd_object_clean_region_max_num_intervals, minimum interval will be trimmed(0 will recovery the entire object data interval)

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_object_clean_region_max_num_intervals 10
ceph config get osd osd_object_clean_region_max_num_intervals
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`10`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_objecter_finishers

| | |
|---|---|
| Type | Int · default `1` · **Advanced** · **STARTUP** (restart required) |
| Table | [osd.md#SP_osd_objecter_finishers](../../../config/global/osd.md#SP_osd_objecter_finishers) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_objecter_finishers 1
ceph config get osd osd_objecter_finishers
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_objecter_finishers
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_objectstore

| | |
|---|---|
| Type | Str · enum: ["bluestore", "filestore", "memstore", "seastore", "cyanstore"] · default `bluestore` · **Advanced** |
| Table | [osd.md#SP_osd_objectstore](../../../config/global/osd.md#SP_osd_objectstore) |

**What it does:** Default back end for new OSDs

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_objectstore bluestore
ceph config get osd osd_objectstore
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `bluestore`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_objectstore
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_objectstore_fuse

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_objectstore_fuse](../../../config/global/osd.md#SP_osd_objectstore_fuse) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_objectstore_fuse true
ceph config get osd osd_objectstore_fuse
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_objectstore_fuse
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_objectstore_ideal_list_max

| | |
|---|---|
| Type | Uint · default `64` · **Advanced** |
| Table | [osd.md#SP_osd_objectstore_ideal_list_max](../../../config/global/osd.md#SP_osd_objectstore_ideal_list_max) |

**What it does:** The max number of results of ObjectStore::collection_list() This value caps the maximal number of entries a single call to collection_list() can return. The configurable controls this aspect of PG deletion and OSD::clear_temp_objects(). Increasing it trade-offs less agressive chunking (and thus less CPU consumption overall) for higher memory pressure. Please note that in the case of PG deletion the chunking is steered by std::min of the this value and the value of osd_target_transaction_size.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`osd_memory_target`](../../../config/global/osd.md#SP_osd_memory_target)

**Example:**

```bash
ceph config set osd osd_objectstore_ideal_list_max 64
ceph config get osd osd_objectstore_ideal_list_max
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_objectstore_ideal_list_max
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_objectstore_tracing

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_objectstore_tracing](../../../config/global/osd.md#SP_osd_objectstore_tracing) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_objectstore_tracing true
ceph config get osd osd_objectstore_tracing
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_objectstore_tracing
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_complaint_time

| | |
|---|---|
| Type | Float · default `30` · **Advanced** |
| Table | [osd.md#SP_osd_op_complaint_time](../../../config/global/osd.md#SP_osd_op_complaint_time) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_op_complaint_time 30
ceph config get osd osd_op_complaint_time
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_op_complaint_time
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_history_duration

| | |
|---|---|
| Type | Uint · default `600` · **Advanced** |
| Table | [osd.md#SP_osd_op_history_duration](../../../config/global/osd.md#SP_osd_op_history_duration) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_op_history_duration 600
ceph config get osd osd_op_history_duration
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `600`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_op_history_duration
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_history_size

| | |
|---|---|
| Type | Uint · default `20` · **Advanced** |
| Table | [osd.md#SP_osd_op_history_size](../../../config/global/osd.md#SP_osd_op_history_size) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_op_history_size 20
ceph config get osd osd_op_history_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_op_history_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_history_slow_op_size

| | |
|---|---|
| Type | Uint · default `20` · **Advanced** |
| Table | [osd.md#SP_osd_op_history_slow_op_size](../../../config/global/osd.md#SP_osd_op_history_slow_op_size) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_op_history_slow_op_size 20
ceph config get osd osd_op_history_slow_op_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_op_history_slow_op_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_history_slow_op_threshold

| | |
|---|---|
| Type | Float · default `10` · **Advanced** |
| Table | [osd.md#SP_osd_op_history_slow_op_threshold](../../../config/global/osd.md#SP_osd_op_history_slow_op_threshold) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_op_history_slow_op_threshold 10
ceph config get osd osd_op_history_slow_op_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_op_history_slow_op_threshold
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_log_threshold

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [osd.md#SP_osd_op_log_threshold](../../../config/global/osd.md#SP_osd_op_log_threshold) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_op_log_threshold 5
ceph config get osd osd_op_log_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_op_log_threshold
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_peering_op_priority

| | |
|---|---|
| Type | Uint · default `255` · **Dev** |
| Table | [osd.md#SP_osd_peering_op_priority](../../../config/global/osd.md#SP_osd_peering_op_priority) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_peering_op_priority 255
ceph config get osd osd_peering_op_priority
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`255`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_pg_delete_cost

| | |
|---|---|
| Type | Size · default `1_M` · **Advanced** |
| Table | [osd.md#SP_osd_pg_delete_cost](../../../config/global/osd.md#SP_osd_pg_delete_cost) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_pg_delete_cost 1_M
ceph config get osd osd_pg_delete_cost
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pg_delete_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pg_delete_priority

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [osd.md#SP_osd_pg_delete_priority](../../../config/global/osd.md#SP_osd_pg_delete_priority) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_pg_delete_priority 5
ceph config get osd osd_pg_delete_priority
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pg_delete_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pg_epoch_persisted_max_stale

| | |
|---|---|
| Type | Uint · default `40` · **Advanced** |
| Table | [osd.md#SP_osd_pg_epoch_persisted_max_stale](../../../config/global/osd.md#SP_osd_pg_epoch_persisted_max_stale) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_pg_epoch_persisted_max_stale 40
ceph config get osd osd_pg_epoch_persisted_max_stale
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `40`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pg_epoch_persisted_max_stale
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pg_log_dups_tracked

| | |
|---|---|
| Type | Uint · default `3000` · **Dev** |
| Table | [osd.md#SP_osd_pg_log_dups_tracked](../../../config/global/osd.md#SP_osd_pg_log_dups_tracked) |

**What it does:** How many versions back to track in order to detect duplicate ops; this is combined with both the regular pg log entries and additional minimal dup detection entries

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_pg_log_dups_tracked 3000
ceph config get osd osd_pg_log_dups_tracked
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`3000`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_pg_log_trim_max

| | |
|---|---|
| Type | Uint · default `10000` · **Advanced** |
| Table | [osd.md#SP_osd_pg_log_trim_max](../../../config/global/osd.md#SP_osd_pg_log_trim_max) |

**What it does:** Maximum number of entries to remove at once from the PG log

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_pg_log_trim_max 10000
ceph config get osd osd_pg_log_trim_max
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pg_log_trim_max
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pg_log_trim_min

| | |
|---|---|
| Type | Uint · default `100` · **Dev** |
| Table | [osd.md#SP_osd_pg_log_trim_min](../../../config/global/osd.md#SP_osd_pg_log_trim_min) |

**What it does:** Minimum number of log entries to trim at once. This lets us trim in larger batches rather than with each write.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_pg_log_trim_min 100
ceph config get osd osd_pg_log_trim_min
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`100`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_pg_max_concurrent_snap_trims

| | |
|---|---|
| Type | Uint · default `2` · **Advanced** |
| Table | [osd.md#SP_osd_pg_max_concurrent_snap_trims](../../../config/global/osd.md#SP_osd_pg_max_concurrent_snap_trims) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_pg_max_concurrent_snap_trims 2
ceph config get osd osd_pg_max_concurrent_snap_trims
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pg_max_concurrent_snap_trims
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pg_object_context_cache_count

| | |
|---|---|
| Type | Int · default `64` · **Advanced** |
| Table | [osd.md#SP_osd_pg_object_context_cache_count](../../../config/global/osd.md#SP_osd_pg_object_context_cache_count) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_pg_object_context_cache_count 64
ceph config get osd osd_pg_object_context_cache_count
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pg_object_context_cache_count
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pg_stat_report_interval_max_epochs

| | |
|---|---|
| Type | Int · default `500` · **Advanced** |
| Table | [osd.md#SP_osd_pg_stat_report_interval_max_epochs](../../../config/global/osd.md#SP_osd_pg_stat_report_interval_max_epochs) |

**What it does:** The maximum number of epochs allowed to pass before PG stats are collected.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_pg_stat_report_interval_max_epochs 500
ceph config get osd osd_pg_stat_report_interval_max_epochs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pg_stat_report_interval_max_epochs
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pg_stat_report_interval_max_seconds

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [osd.md#SP_osd_pg_stat_report_interval_max_seconds](../../../config/global/osd.md#SP_osd_pg_stat_report_interval_max_seconds) |

**What it does:** How often (in seconds) should PGs stats be collected.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_pg_stat_report_interval_max_seconds 5
ceph config get osd osd_pg_stat_report_interval_max_seconds
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pg_stat_report_interval_max_seconds
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_cache_max_evict_check_size

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_cache_max_evict_check_size](../../../config/global/osd.md#SP_osd_pool_default_cache_max_evict_check_size) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_pool_default_cache_max_evict_check_size 10
ceph config get osd osd_pool_default_cache_max_evict_check_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_cache_max_evict_check_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_cache_min_evict_age

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_cache_min_evict_age](../../../config/global/osd.md#SP_osd_pool_default_cache_min_evict_age) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_pool_default_cache_min_evict_age 64
ceph config get osd osd_pool_default_cache_min_evict_age
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_cache_min_evict_age
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_cache_min_flush_age

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_cache_min_flush_age](../../../config/global/osd.md#SP_osd_pool_default_cache_min_flush_age) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_pool_default_cache_min_flush_age 64
ceph config get osd osd_pool_default_cache_min_flush_age
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_cache_min_flush_age
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_cache_target_dirty_high_ratio

| | |
|---|---|
| Type | Float · default `0.6` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_cache_target_dirty_high_ratio](../../../config/global/osd.md#SP_osd_pool_default_cache_target_dirty_high_ratio) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_pool_default_cache_target_dirty_high_ratio 0.6
ceph config get osd osd_pool_default_cache_target_dirty_high_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.6`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_cache_target_dirty_high_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_cache_target_dirty_ratio

| | |
|---|---|
| Type | Float · default `0.4` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_cache_target_dirty_ratio](../../../config/global/osd.md#SP_osd_pool_default_cache_target_dirty_ratio) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_pool_default_cache_target_dirty_ratio 0.4
ceph config get osd osd_pool_default_cache_target_dirty_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.4`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_cache_target_dirty_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_cache_target_full_ratio

| | |
|---|---|
| Type | Float · default `0.8` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_cache_target_full_ratio](../../../config/global/osd.md#SP_osd_pool_default_cache_target_full_ratio) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_pool_default_cache_target_full_ratio 0.8
ceph config get osd osd_pool_default_cache_target_full_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.8`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_cache_target_full_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_crush_rule

| | |
|---|---|
| Type | Int · default `-1` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_crush_rule](../../../config/global/osd.md#SP_osd_pool_default_crush_rule) |

**What it does:** CRUSH rule for newly created pools

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_pool_default_crush_rule 128
ceph config get osd osd_pool_default_crush_rule
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `-1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_crush_rule
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_ec_fast_read

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_ec_fast_read](../../../config/global/osd.md#SP_osd_pool_default_ec_fast_read) |

**What it does:** set ec_fast_read for new erasure-coded pools

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_pool_default_ec_fast_read true
ceph config get osd osd_pool_default_ec_fast_read
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_ec_fast_read
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_erasure_code_profile

| | |
|---|---|
| Type | Str · default `plugin=isa technique=reed_sol_van k=2 m=2` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_erasure_code_profile](../../../config/global/osd.md#SP_osd_pool_default_erasure_code_profile) |

**What it does:** Default EC profile for new erasure-coded pools

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_pool_default_erasure_code_profile "plugin=isa technique=reed_sol_van k=2 m=2"
ceph config get osd osd_pool_default_erasure_code_profile
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `plugin=isa technique=reed_sol_van k=2 m=2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_erasure_code_profile
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_flag_bulk

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_flag_bulk](../../../config/global/osd.md#SP_osd_pool_default_flag_bulk) |

**What it does:** Set the bulk flag on new pools

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_pool_default_flag_bulk true
ceph config get osd osd_pool_default_flag_bulk
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_flag_bulk
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_flag_ec_optimizations

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_flag_ec_optimizations](../../../config/global/osd.md#SP_osd_pool_default_flag_ec_optimizations) |

**What it does:** Control whether to create new erasure coded pools with EC optimizations turned on by default.

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_pool_default_flag_ec_optimizations true
ceph config get osd osd_pool_default_flag_ec_optimizations
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_flag_ec_optimizations
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_flag_hashpspool

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_flag_hashpspool](../../../config/global/osd.md#SP_osd_pool_default_flag_hashpspool) |

**What it does:** Set hashpspool (better hashing scheme) flag on new pools

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_pool_default_flag_hashpspool false
ceph config get osd osd_pool_default_flag_hashpspool
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_flag_hashpspool
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_flag_nodelete

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_flag_nodelete](../../../config/global/osd.md#SP_osd_pool_default_flag_nodelete) |

**What it does:** Set the nodelete flag on new pools

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_pool_default_flag_nodelete true
ceph config get osd osd_pool_default_flag_nodelete
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_flag_nodelete
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_flag_nopgchange

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_flag_nopgchange](../../../config/global/osd.md#SP_osd_pool_default_flag_nopgchange) |

**What it does:** Set the nopgchange flag on new pools

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_pool_default_flag_nopgchange true
ceph config get osd osd_pool_default_flag_nopgchange
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_flag_nopgchange
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_flag_nosizechange

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_flag_nosizechange](../../../config/global/osd.md#SP_osd_pool_default_flag_nosizechange) |

**What it does:** Set the nosizechange flag on new pools

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_pool_default_flag_nosizechange true
ceph config get osd osd_pool_default_flag_nosizechange
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_flag_nosizechange
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_flags

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [osd.md#SP_osd_pool_default_flags](../../../config/global/osd.md#SP_osd_pool_default_flags) |

**What it does:** The (integer) flags to set on new pools

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_pool_default_flags 64
ceph config get osd osd_pool_default_flags
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_pool_default_hit_set_bloom_fpp

| | |
|---|---|
| Type | Float · default `0.05` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_hit_set_bloom_fpp](../../../config/global/osd.md#SP_osd_pool_default_hit_set_bloom_fpp) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`osd_tier_default_cache_hit_set_type`](../../../config/global/osd.md#SP_osd_tier_default_cache_hit_set_type)

**Example:**

```bash
ceph config set osd osd_pool_default_hit_set_bloom_fpp 0.05
ceph config get osd osd_pool_default_hit_set_bloom_fpp
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.05`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_hit_set_bloom_fpp
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_min_size

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_min_size](../../../config/global/osd.md#SP_osd_pool_default_min_size) |

**What it does:** The minimal number of copies allowed to write to a degraded pool for new replicated pools 0 means no specific default; ceph will use size-size/2

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Related options:**

- [`osd_pool_default_size`](../../../config/global/osd.md#SP_osd_pool_default_size)

**Example:**

```bash
ceph config set osd osd_pool_default_min_size 64
ceph config get osd osd_pool_default_min_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `255`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_min_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_pg_autoscale_mode

| | |
|---|---|
| Type | Str · enum: ["off", "warn", "on"] · default `on` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_pg_autoscale_mode](../../../config/global/osd.md#SP_osd_pool_default_pg_autoscale_mode) |

**What it does:** Default PG autoscaling behavior for new pools When 'on', the autoscaler assigns 1 pg to new pools unless the user specifies a value.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_pool_default_pg_autoscale_mode on
ceph config get osd osd_pool_default_pg_autoscale_mode
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `on`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_pg_autoscale_mode
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_pg_num

| | |
|---|---|
| Type | Uint · default `32` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_pg_num](../../../config/global/osd.md#SP_osd_pool_default_pg_num) |

**What it does:** number of PGs for new pools With default value of `osd_pool_default_pg_autoscale_mode` being `on` the number of PGs for new pools will start out with 1 pg, unless the user specifies the pg_num.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`osd_pool_default_pg_autoscale_mode`](../../../config/global/osd.md#SP_osd_pool_default_pg_autoscale_mode)

**Example:**

```bash
ceph config set osd osd_pool_default_pg_num 32
ceph config get osd osd_pool_default_pg_num
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `32`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_pg_num
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_pgp_num

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_pgp_num](../../../config/global/osd.md#SP_osd_pool_default_pgp_num) |

**What it does:** number of PGs for placement purposes (0 to match pg_num)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_pool_default_pgp_num 64
ceph config get osd osd_pool_default_pgp_num
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_pgp_num
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_read_lease_ratio

| | |
|---|---|
| Type | Float · default `0.8` · **Dev** |
| Table | [osd.md#SP_osd_pool_default_read_lease_ratio](../../../config/global/osd.md#SP_osd_pool_default_read_lease_ratio) |

**What it does:** Default read_lease_ratio for a pool, as a multiple of osd_heartbeat_grace This should be <= 1.0 so that the read lease will have expired by the time we decide to mark a peer OSD down.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Related options:**

- [`osd_heartbeat_grace`](../../../config/global/osd.md#SP_osd_heartbeat_grace)

**Example:**

```bash
ceph config set osd osd_pool_default_read_lease_ratio 0.8
ceph config get osd osd_pool_default_read_lease_ratio
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.8`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_pool_default_read_ratio

| | |
|---|---|
| Type | Uint · default `70` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_read_ratio](../../../config/global/osd.md#SP_osd_pool_default_read_ratio) |

**What it does:** Default read ratio (the percent of read IOs out of all IOs) for a pool. Default read ratio (the percent of read IOs out of all IOs) for a pool. applicable to replicated pools only. This value is used to improve read balancing when OSDs have different weights.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_pool_default_read_ratio 70
ceph config get osd osd_pool_default_read_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `70`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_read_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_size

| | |
|---|---|
| Type | Uint · default `3` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_size](../../../config/global/osd.md#SP_osd_pool_default_size) |

**What it does:** the number of copies of an object for new replicated pools

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_pool_default_size 3
ceph config get osd osd_pool_default_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `10`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_type

| | |
|---|---|
| Type | Str · enum: ["replicated", "erasure"] · default `replicated` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_type](../../../config/global/osd.md#SP_osd_pool_default_type) |

**What it does:** Default data protection strategy type when creating a new pool

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_pool_default_type replicated
ceph config get osd osd_pool_default_type
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `replicated`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_type
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_use_gmt_hitset

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [osd.md#SP_osd_pool_use_gmt_hitset](../../../config/global/osd.md#SP_osd_pool_use_gmt_hitset) |

**What it does:** use UTC for hitset timestamps This setting only exists for compatibility with hammer (and older) clusters.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_pool_use_gmt_hitset false
ceph config get osd osd_pool_use_gmt_hitset
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_recovery_cost

| | |
|---|---|
| Type | Size · default `20_M` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_cost](../../../config/global/osd.md#SP_osd_recovery_cost) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_recovery_cost 20_M
ceph config get osd osd_recovery_cost
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `20_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_op_priority

| | |
|---|---|
| Type | Uint · default `3` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_op_priority](../../../config/global/osd.md#SP_osd_recovery_op_priority) |

**What it does:** Priority to use for recovery operations if not specified for the pool

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_recovery_op_priority 3
ceph config get osd osd_recovery_op_priority
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_op_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_op_warn_multiple

| | |
|---|---|
| Type | Uint · default `16` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_op_warn_multiple](../../../config/global/osd.md#SP_osd_recovery_op_warn_multiple) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_recovery_op_warn_multiple 16
ceph config get osd osd_recovery_op_warn_multiple
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `16`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_op_warn_multiple
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_priority

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_priority](../../../config/global/osd.md#SP_osd_recovery_priority) |

**What it does:** Priority of recovery in the work queue Not related to a pool's recovery_priority

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_recovery_priority 5
ceph config get osd osd_recovery_priority
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_requested_scrub_priority

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [osd.md#SP_osd_requested_scrub_priority](../../../config/global/osd.md#SP_osd_requested_scrub_priority) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_requested_scrub_priority 5
ceph config get osd osd_requested_scrub_priority
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_requested_scrub_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_rollback_to_cluster_snap

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [osd.md#SP_osd_rollback_to_cluster_snap](../../../config/global/osd.md#SP_osd_rollback_to_cluster_snap) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_rollback_to_cluster_snap "example"
ceph config get osd osd_rollback_to_cluster_snap
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_rollback_to_cluster_snap
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_cost

| | |
|---|---|
| Type | Size · default `50_M` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_cost](../../../config/global/osd.md#SP_osd_scrub_cost) |

**What it does:** Cost for scrub operations in work queue

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_scrub_cost 50_M
ceph config get osd osd_scrub_cost
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `50_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_event_cost

| | |
|---|---|
| Type | Size · default `4_K` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_event_cost](../../../config/global/osd.md#SP_osd_scrub_event_cost) |

**What it does:** Cost for each scrub operation, used when osd_op_queue=mclock_scheduler

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_scrub_event_cost 4_K
ceph config get osd osd_scrub_event_cost
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_event_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_priority

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_priority](../../../config/global/osd.md#SP_osd_scrub_priority) |

**What it does:** Priority for scrub operations in work queue

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_scrub_priority 5
ceph config get osd osd_scrub_priority
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_shutdown_pgref_assert

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_shutdown_pgref_assert](../../../config/global/osd.md#SP_osd_shutdown_pgref_assert) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_shutdown_pgref_assert true
ceph config get osd osd_shutdown_pgref_assert
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_shutdown_pgref_assert
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_skip_check_past_interval_bounds

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_skip_check_past_interval_bounds](../../../config/global/osd.md#SP_osd_skip_check_past_interval_bounds) |

**What it does:** See https://tracker.ceph.com/issues/64002

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_skip_check_past_interval_bounds true
ceph config get osd osd_skip_check_past_interval_bounds
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_snap_trim_cost

| | |
|---|---|
| Type | Size · default `1_M` · **Advanced** |
| Table | [osd.md#SP_osd_snap_trim_cost](../../../config/global/osd.md#SP_osd_snap_trim_cost) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_snap_trim_cost 1_M
ceph config get osd osd_snap_trim_cost
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_snap_trim_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_snap_trim_priority

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [osd.md#SP_osd_snap_trim_priority](../../../config/global/osd.md#SP_osd_snap_trim_priority) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_snap_trim_priority 5
ceph config get osd osd_snap_trim_priority
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_snap_trim_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_target_pg_log_entries_per_osd

| | |
|---|---|
| Type | Uint · default `300000` · **Dev** |
| Table | [osd.md#SP_osd_target_pg_log_entries_per_osd](../../../config/global/osd.md#SP_osd_target_pg_log_entries_per_osd) |

**What it does:** Target number of PG entries total on an OSD, limited per PG by the min and max options below

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_target_pg_log_entries_per_osd 300000
ceph config get osd osd_target_pg_log_entries_per_osd
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`300000`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_target_transaction_size

| | |
|---|---|
| Type | Uint · default `30` · **Advanced** |
| Table | [osd.md#SP_osd_target_transaction_size](../../../config/global/osd.md#SP_osd_target_transaction_size) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_target_transaction_size 30
ceph config get osd osd_target_transaction_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_target_transaction_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_default_cache_hit_set_count

| | |
|---|---|
| Type | Uint · default `4` · **Advanced** |
| Table | [osd.md#SP_osd_tier_default_cache_hit_set_count](../../../config/global/osd.md#SP_osd_tier_default_cache_hit_set_count) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_tier_default_cache_hit_set_count 4
ceph config get osd osd_tier_default_cache_hit_set_count
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_tier_default_cache_hit_set_count
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_default_cache_hit_set_grade_decay_rate

| | |
|---|---|
| Type | Uint · default `20` · **Advanced** |
| Table | [osd.md#SP_osd_tier_default_cache_hit_set_grade_decay_rate](../../../config/global/osd.md#SP_osd_tier_default_cache_hit_set_grade_decay_rate) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_tier_default_cache_hit_set_grade_decay_rate 20
ceph config get osd osd_tier_default_cache_hit_set_grade_decay_rate
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_tier_default_cache_hit_set_grade_decay_rate
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_default_cache_hit_set_period

| | |
|---|---|
| Type | Uint · default `1200` · **Advanced** |
| Table | [osd.md#SP_osd_tier_default_cache_hit_set_period](../../../config/global/osd.md#SP_osd_tier_default_cache_hit_set_period) |

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_tier_default_cache_hit_set_period 1200
ceph config get osd osd_tier_default_cache_hit_set_period
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1200`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_tier_default_cache_hit_set_period
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_default_cache_hit_set_search_last_n

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [osd.md#SP_osd_tier_default_cache_hit_set_search_last_n](../../../config/global/osd.md#SP_osd_tier_default_cache_hit_set_search_last_n) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_tier_default_cache_hit_set_search_last_n 1
ceph config get osd osd_tier_default_cache_hit_set_search_last_n
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_tier_default_cache_hit_set_search_last_n
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_default_cache_hit_set_type

| | |
|---|---|
| Type | Str · enum: ["bloom", "explicit_hash", "explicit_object"] · default `bloom` · **Advanced** |
| Table | [osd.md#SP_osd_tier_default_cache_hit_set_type](../../../config/global/osd.md#SP_osd_tier_default_cache_hit_set_type) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_tier_default_cache_hit_set_type bloom
ceph config get osd osd_tier_default_cache_hit_set_type
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `bloom`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_tier_default_cache_hit_set_type
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_default_cache_min_read_recency_for_promote

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [osd.md#SP_osd_tier_default_cache_min_read_recency_for_promote](../../../config/global/osd.md#SP_osd_tier_default_cache_min_read_recency_for_promote) |

**What it does:** Number of recent HitSets the object must appear in to be promoted (on read)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_tier_default_cache_min_read_recency_for_promote 1
ceph config get osd osd_tier_default_cache_min_read_recency_for_promote
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_tier_default_cache_min_read_recency_for_promote
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_default_cache_min_write_recency_for_promote

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [osd.md#SP_osd_tier_default_cache_min_write_recency_for_promote](../../../config/global/osd.md#SP_osd_tier_default_cache_min_write_recency_for_promote) |

**What it does:** Number of recent HitSets the object must appear in to be promoted (on write)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_tier_default_cache_min_write_recency_for_promote 1
ceph config get osd osd_tier_default_cache_min_write_recency_for_promote
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_tier_default_cache_min_write_recency_for_promote
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_default_cache_mode

| | |
|---|---|
| Type | Str · enum: ["none", "writeback", "forward", "readonly", "readforward", "readproxy", "proxy"] · default `writeback` · **Advanced** |
| Table | [osd.md#SP_osd_tier_default_cache_mode](../../../config/global/osd.md#SP_osd_tier_default_cache_mode) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_tier_default_cache_mode writeback
ceph config get osd osd_tier_default_cache_mode
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `writeback`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_tier_default_cache_mode
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_promote_max_bytes_sec

| | |
|---|---|
| Type | Size · default `5_M` · **Advanced** |
| Table | [osd.md#SP_osd_tier_promote_max_bytes_sec](../../../config/global/osd.md#SP_osd_tier_promote_max_bytes_sec) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_tier_promote_max_bytes_sec 5_M
ceph config get osd osd_tier_promote_max_bytes_sec
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_tier_promote_max_bytes_sec
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_promote_max_objects_sec

| | |
|---|---|
| Type | Uint · default `25` · **Advanced** |
| Table | [osd.md#SP_osd_tier_promote_max_objects_sec](../../../config/global/osd.md#SP_osd_tier_promote_max_objects_sec) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_tier_promote_max_objects_sec 25
ceph config get osd osd_tier_promote_max_objects_sec
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `25`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_tier_promote_max_objects_sec
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tracing

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_tracing](../../../config/global/osd.md#SP_osd_tracing) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_tracing true
ceph config get osd osd_tracing
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_tracing
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_use_stale_snap

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_use_stale_snap](../../../config/global/osd.md#SP_osd_use_stale_snap) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_use_stale_snap true
ceph config get osd osd_use_stale_snap
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_use_stale_snap
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← Overview](../OVERVIEW.md)
