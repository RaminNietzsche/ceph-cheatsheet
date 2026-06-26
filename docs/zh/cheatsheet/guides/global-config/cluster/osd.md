# Osd

Global 配置深度指南 — 174 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [osd_asio_thread_count](#osd_asio_thread_count) | `2` | Advanced | 性能 |
| [osd_async_recovery_min_cost](#osd_async_recovery_min_cost) | `100` | Advanced | 性能 |
| [osd_auto_mark_unfound_lost](#osd_auto_mark_unfound_lost) | `False` | Advanced | 性能 |
| [osd_backoff_on_degraded](#osd_backoff_on_degraded) | `False` | Advanced | 性能 |
| [osd_backoff_on_peering](#osd_backoff_on_peering) | `False` | Advanced | 性能 |
| [osd_backoff_on_unfound](#osd_backoff_on_unfound) | `True` | Advanced | 性能 |
| [osd_beacon_report_interval](#osd_beacon_report_interval) | `5_min` | Advanced | 性能 |
| [osd_bench_duration](#osd_bench_duration) | `30` | Advanced | 性能 |
| [osd_bench_large_size_max_throughput](#osd_bench_large_size_max_throughput) | `100_M` | Advanced | 性能 |
| [osd_bench_max_block_size](#osd_bench_max_block_size) | `64_M` | Advanced | 性能 |
| [osd_bench_small_size_max_iops](#osd_bench_small_size_max_iops) | `100` | Advanced | 性能 |
| [osd_blkin_trace_all](#osd_blkin_trace_all) | `False` | Advanced | 性能 |
| [osd_calc_pg_upmaps_aggressively](#osd_calc_pg_upmaps_aggressively) | `True` | Advanced | 性能 |
| [osd_calc_pg_upmaps_aggressively_fast](#osd_calc_pg_upmaps_aggressively_fast) | `True` | Advanced | 性能 |
| [osd_calc_pg_upmaps_local_fallback_retries](#osd_calc_pg_upmaps_local_fallback_retries) | `100` | Advanced | 性能 |
| [osd_check_for_log_corruption](#osd_check_for_log_corruption) | `False` | Advanced | 性能 |
| [osd_client_op_priority](#osd_client_op_priority) | `63` | Advanced | 性能 |
| [osd_command_max_records](#osd_command_max_records) | `256` | Advanced | 性能 |
| [osd_crush_chooseleaf_type](#osd_crush_chooseleaf_type) | `1` | Dev | 开发 |
| [osd_debug_crash_on_ignored_backoff](#osd_debug_crash_on_ignored_backoff) | `False` | Dev | 开发 |
| [osd_debug_deep_scrub_sleep](#osd_debug_deep_scrub_sleep) | `0` | Dev | 开发 |
| [osd_debug_drop_ping_duration](#osd_debug_drop_ping_duration) | `0` | Dev | 开发 |
| [osd_debug_drop_ping_probability](#osd_debug_drop_ping_probability) | `0` | Dev | 开发 |
| [osd_debug_inject_copyfrom_error](#osd_debug_inject_copyfrom_error) | `False` | Dev | 开发 |
| [osd_debug_inject_dispatch_delay_duration](#osd_debug_inject_dispatch_delay_duration) | `0.1` | Dev | 开发 |
| [osd_debug_inject_dispatch_delay_probability](#osd_debug_inject_dispatch_delay_probability) | `0` | Dev | 开发 |
| [osd_debug_misdirected_ops](#osd_debug_misdirected_ops) | `False` | Dev | 开发 |
| [osd_debug_no_acting_change](#osd_debug_no_acting_change) | `False` | Dev | 开发 |
| [osd_debug_no_purge_strays](#osd_debug_no_purge_strays) | `False` | Dev | 开发 |
| [osd_debug_op_order](#osd_debug_op_order) | `False` | Dev | 开发 |
| [osd_debug_pg_log_writeout](#osd_debug_pg_log_writeout) | `False` | Dev | 开发 |
| [osd_debug_pretend_recovery_active](#osd_debug_pretend_recovery_active) | `False` | Dev | 开发 |
| [osd_debug_random_push_read_error](#osd_debug_random_push_read_error) | `0` | Dev | 开发 |
| [osd_debug_reject_backfill_probability](#osd_debug_reject_backfill_probability) | `0` | Dev | 开发 |
| [osd_debug_shutdown](#osd_debug_shutdown) | `False` | Dev | 开发 |
| [osd_debug_skip_full_check_in_backfill_reservation](#osd_debug_skip_full_check_in_backfill_reservation) | `False` | Dev | 开发 |
| [osd_debug_skip_full_check_in_recovery](#osd_debug_skip_full_check_in_recovery) | `False` | Dev | 开发 |
| [osd_debug_verify_cached_snaps](#osd_debug_verify_cached_snaps) | `False` | Dev | 开发 |
| [osd_debug_verify_missing_on_start](#osd_debug_verify_missing_on_start) | `False` | Dev | 开发 |
| [osd_debug_verify_snaps](#osd_debug_verify_snaps) | `False` | Dev | 开发 |
| [osd_debug_verify_stray_on_activate](#osd_debug_verify_stray_on_activate) | `False` | Dev | 开发 |
| [osd_default_data_pool_replay_window](#osd_default_data_pool_replay_window) | `45` | Advanced | 性能 |
| [osd_default_notify_timeout](#osd_default_notify_timeout) | `30` | Advanced | 性能 |
| [osd_discard_disconnected_ops](#osd_discard_disconnected_ops) | `True` | Advanced | 性能 |
| [osd_enable_op_tracker](#osd_enable_op_tracker) | `True` | Advanced | 策略 |
| [osd_erasure_code_plugins](#osd_erasure_code_plugins) | `0` | Advanced | 性能 |
| [osd_failsafe_full_ratio](#osd_failsafe_full_ratio) | `0.97` | Advanced | 性能 |
| [osd_fast_fail_on_connection_refused](#osd_fast_fail_on_connection_refused) | `True` | Advanced | 性能 |
| [osd_fast_info](#osd_fast_info) | `True` | Advanced | 性能 |
| [osd_fast_shutdown](#osd_fast_shutdown) | `True` | Advanced | 性能 |
| [osd_fast_shutdown_notify_mon](#osd_fast_shutdown_notify_mon) | `True` | Advanced | 性能 |
| [osd_fast_shutdown_timeout](#osd_fast_shutdown_timeout) | `15` | Advanced | 性能 |
| [osd_force_auth_primary_missing_objects](#osd_force_auth_primary_missing_objects) | `100` | Advanced | 性能 |
| [osd_force_recovery_pg_log_entries_factor](#osd_force_recovery_pg_log_entries_factor) | `1.3` | Dev | 开发 |
| [osd_function_tracing](#osd_function_tracing) | `False` | Advanced | 性能 |
| [osd_heartbeat_grace](#osd_heartbeat_grace) | `20` | Advanced | 性能 |
| [osd_heartbeat_interval](#osd_heartbeat_interval) | `6` | Dev | 开发 |
| [osd_heartbeat_min_healthy_ratio](#osd_heartbeat_min_healthy_ratio) | `0.33` | Advanced | 性能 |
| [osd_heartbeat_min_size](#osd_heartbeat_min_size) | `2000` | Advanced | 性能 |
| [osd_heartbeat_stale](#osd_heartbeat_stale) | `10_min` | Advanced | 性能 |
| [osd_heartbeat_use_min_delay_socket](#osd_heartbeat_use_min_delay_socket) | `False` | Advanced | 性能 |
| [osd_hit_set_max_size](#osd_hit_set_max_size) | `100000` | Advanced | 性能 |
| [osd_hit_set_min_size](#osd_hit_set_min_size) | `1000` | Advanced | 性能 |
| [osd_hit_set_namespace](#osd_hit_set_namespace) | `.ceph-internal` | Advanced | 性能 |
| [osd_ignore_stale_divergent_priors](#osd_ignore_stale_divergent_priors) | `False` | Advanced | 性能 |
| [osd_kill_backfill_at](#osd_kill_backfill_at) | `0` | Dev | 开发 |
| [osd_loop_before_reset_tphandle](#osd_loop_before_reset_tphandle) | `64` | Advanced | 性能 |
| [osd_map_dedup](#osd_map_dedup) | `True` | Advanced | 性能 |
| [osd_map_message_max](#osd_map_message_max) | `40` | Advanced | 性能 |
| [osd_map_message_max_bytes](#osd_map_message_max_bytes) | `10_M` | Advanced | 性能 |
| [osd_max_attr_name_len](#osd_max_attr_name_len) | `100` | Advanced | 性能 |
| [osd_max_attr_size](#osd_max_attr_size) | `0` | Advanced | 性能 |
| [osd_max_object_name_len](#osd_max_object_name_len) | `2_K` | Advanced | 性能 |
| [osd_max_object_namespace_len](#osd_max_object_namespace_len) | `256` | Advanced | 性能 |
| [osd_max_object_size](#osd_max_object_size) | `128_M` | Advanced | 性能 |
| [osd_max_omap_bytes_per_request](#osd_max_omap_bytes_per_request) | `1_G` | Advanced | 性能 |
| [osd_max_omap_entries_per_request](#osd_max_omap_entries_per_request) | `1_K` | Advanced | 性能 |
| [osd_max_pg_blocked_by](#osd_max_pg_blocked_by) | `16` | Advanced | 性能 |
| [osd_max_pg_log_entries](#osd_max_pg_log_entries) | `10000` | Dev | 开发 |
| [osd_max_pg_per_osd_hard_ratio](#osd_max_pg_per_osd_hard_ratio) | `3` | Advanced | 性能 |
| [osd_max_snap_prune_intervals_per_epoch](#osd_max_snap_prune_intervals_per_epoch) | `512` | Dev | 开发 |
| [osd_max_trimming_pgs](#osd_max_trimming_pgs) | `2` | Advanced | 性能 |
| [osd_max_write_op_reply_len](#osd_max_write_op_reply_len) | `64` | Advanced | 性能 |
| [osd_memory_base](#osd_memory_base) | `768_M` | Dev | 开发 |
| [osd_memory_cache_min](#osd_memory_cache_min) | `128_M` | Dev | 开发 |
| [osd_memory_cache_resize_interval](#osd_memory_cache_resize_interval) | `1` | Dev | 开发 |
| [osd_memory_expected_fragmentation](#osd_memory_expected_fragmentation) | `0.15` | Dev | 开发 |
| [osd_memory_target](#osd_memory_target) | `4_G` | Basic | 策略 |
| [osd_memory_target_autotune](#osd_memory_target_autotune) | `False` | Advanced | 性能 |
| [osd_memory_target_cgroup_limit_ratio](#osd_memory_target_cgroup_limit_ratio) | `0.8` | Advanced | 性能 |
| [osd_min_pg_log_entries](#osd_min_pg_log_entries) | `250` | Dev | 开发 |
| [osd_min_split_replica_read_size](#osd_min_split_replica_read_size) | `0` | Advanced | 性能 |
| [osd_mon_heartbeat_interval](#osd_mon_heartbeat_interval) | `30` | Advanced | 性能 |
| [osd_mon_heartbeat_stat_stale](#osd_mon_heartbeat_stat_stale) | `1_hr` | Advanced | 性能 |
| [osd_mon_report_interval](#osd_mon_report_interval) | `5` | Advanced | 性能 |
| [osd_mon_report_max_in_flight](#osd_mon_report_max_in_flight) | `2` | Advanced | 性能 |
| [osd_mon_shutdown_timeout](#osd_mon_shutdown_timeout) | `5` | Advanced | 性能 |
| [osd_num_op_tracker_shard](#osd_num_op_tracker_shard) | `32` | Advanced | 性能 |
| [osd_object_clean_region_max_num_intervals](#osd_object_clean_region_max_num_intervals) | `10` | Dev | 开发 |
| [osd_objecter_finishers](#osd_objecter_finishers) | `1` | Advanced | 性能 |
| [osd_objectstore](#osd_objectstore) | `bluestore` | Advanced | 性能 |
| [osd_objectstore_fuse](#osd_objectstore_fuse) | `False` | Advanced | 性能 |
| [osd_objectstore_ideal_list_max](#osd_objectstore_ideal_list_max) | `64` | Advanced | 性能 |
| [osd_objectstore_tracing](#osd_objectstore_tracing) | `False` | Advanced | 性能 |
| [osd_op_complaint_time](#osd_op_complaint_time) | `30` | Advanced | 性能 |
| [osd_op_history_duration](#osd_op_history_duration) | `600` | Advanced | 性能 |
| [osd_op_history_size](#osd_op_history_size) | `20` | Advanced | 性能 |
| [osd_op_history_slow_op_size](#osd_op_history_slow_op_size) | `20` | Advanced | 性能 |
| [osd_op_history_slow_op_threshold](#osd_op_history_slow_op_threshold) | `10` | Advanced | 性能 |
| [osd_op_log_threshold](#osd_op_log_threshold) | `5` | Advanced | 性能 |
| [osd_peering_op_priority](#osd_peering_op_priority) | `255` | Dev | 开发 |
| [osd_pg_delete_cost](#osd_pg_delete_cost) | `1_M` | Advanced | 性能 |
| [osd_pg_delete_priority](#osd_pg_delete_priority) | `5` | Advanced | 性能 |
| [osd_pg_epoch_persisted_max_stale](#osd_pg_epoch_persisted_max_stale) | `40` | Advanced | 性能 |
| [osd_pg_log_dups_tracked](#osd_pg_log_dups_tracked) | `3000` | Dev | 开发 |
| [osd_pg_log_trim_max](#osd_pg_log_trim_max) | `10000` | Advanced | 性能 |
| [osd_pg_log_trim_min](#osd_pg_log_trim_min) | `100` | Dev | 开发 |
| [osd_pg_max_concurrent_snap_trims](#osd_pg_max_concurrent_snap_trims) | `2` | Advanced | 性能 |
| [osd_pg_object_context_cache_count](#osd_pg_object_context_cache_count) | `64` | Advanced | 性能 |
| [osd_pg_stat_report_interval_max_epochs](#osd_pg_stat_report_interval_max_epochs) | `500` | Advanced | 性能 |
| [osd_pg_stat_report_interval_max_seconds](#osd_pg_stat_report_interval_max_seconds) | `5` | Advanced | 性能 |
| [osd_pool_default_cache_max_evict_check_size](#osd_pool_default_cache_max_evict_check_size) | `10` | Advanced | 性能 |
| [osd_pool_default_cache_min_evict_age](#osd_pool_default_cache_min_evict_age) | `0` | Advanced | 性能 |
| [osd_pool_default_cache_min_flush_age](#osd_pool_default_cache_min_flush_age) | `0` | Advanced | 性能 |
| [osd_pool_default_cache_target_dirty_high_ratio](#osd_pool_default_cache_target_dirty_high_ratio) | `0.6` | Advanced | 性能 |
| [osd_pool_default_cache_target_dirty_ratio](#osd_pool_default_cache_target_dirty_ratio) | `0.4` | Advanced | 性能 |
| [osd_pool_default_cache_target_full_ratio](#osd_pool_default_cache_target_full_ratio) | `0.8` | Advanced | 性能 |
| [osd_pool_default_crush_rule](#osd_pool_default_crush_rule) | `-1` | Advanced | 性能 |
| [osd_pool_default_ec_fast_read](#osd_pool_default_ec_fast_read) | `False` | Advanced | 性能 |
| [osd_pool_default_erasure_code_profile](#osd_pool_default_erasure_code_profile) | `plugin=isa technique=reed_sol_van k=2 m=2` | Advanced | 性能 |
| [osd_pool_default_flag_bulk](#osd_pool_default_flag_bulk) | `False` | Advanced | 性能 |
| [osd_pool_default_flag_ec_optimizations](#osd_pool_default_flag_ec_optimizations) | `False` | Advanced | 性能 |
| [osd_pool_default_flag_hashpspool](#osd_pool_default_flag_hashpspool) | `True` | Advanced | 性能 |
| [osd_pool_default_flag_nodelete](#osd_pool_default_flag_nodelete) | `False` | Advanced | 性能 |
| [osd_pool_default_flag_nopgchange](#osd_pool_default_flag_nopgchange) | `False` | Advanced | 性能 |
| [osd_pool_default_flag_nosizechange](#osd_pool_default_flag_nosizechange) | `False` | Advanced | 性能 |
| [osd_pool_default_flags](#osd_pool_default_flags) | `0` | Dev | 开发 |
| [osd_pool_default_hit_set_bloom_fpp](#osd_pool_default_hit_set_bloom_fpp) | `0.05` | Advanced | 性能 |
| [osd_pool_default_min_size](#osd_pool_default_min_size) | `0` | Advanced | 性能 |
| [osd_pool_default_pg_autoscale_mode](#osd_pool_default_pg_autoscale_mode) | `on` | Advanced | 性能 |
| [osd_pool_default_pg_num](#osd_pool_default_pg_num) | `32` | Advanced | 性能 |
| [osd_pool_default_pgp_num](#osd_pool_default_pgp_num) | `0` | Advanced | 性能 |
| [osd_pool_default_read_lease_ratio](#osd_pool_default_read_lease_ratio) | `0.8` | Dev | 开发 |
| [osd_pool_default_read_ratio](#osd_pool_default_read_ratio) | `70` | Advanced | 性能 |
| [osd_pool_default_size](#osd_pool_default_size) | `3` | Advanced | 性能 |
| [osd_pool_default_type](#osd_pool_default_type) | `replicated` | Advanced | 性能 |
| [osd_pool_use_gmt_hitset](#osd_pool_use_gmt_hitset) | `True` | Dev | 开发 |
| [osd_recovery_cost](#osd_recovery_cost) | `20_M` | Advanced | 性能 |
| [osd_recovery_op_priority](#osd_recovery_op_priority) | `3` | Advanced | 性能 |
| [osd_recovery_op_warn_multiple](#osd_recovery_op_warn_multiple) | `16` | Advanced | 性能 |
| [osd_recovery_priority](#osd_recovery_priority) | `5` | Advanced | 性能 |
| [osd_requested_scrub_priority](#osd_requested_scrub_priority) | `5` | Advanced | 性能 |
| [osd_rollback_to_cluster_snap](#osd_rollback_to_cluster_snap) | `(empty)` | Advanced | 性能 |
| [osd_scrub_cost](#osd_scrub_cost) | `50_M` | Advanced | 性能 |
| [osd_scrub_event_cost](#osd_scrub_event_cost) | `4_K` | Advanced | 性能 |
| [osd_scrub_priority](#osd_scrub_priority) | `5` | Advanced | 性能 |
| [osd_shutdown_pgref_assert](#osd_shutdown_pgref_assert) | `False` | Advanced | 性能 |
| [osd_skip_check_past_interval_bounds](#osd_skip_check_past_interval_bounds) | `False` | Dev | 开发 |
| [osd_snap_trim_cost](#osd_snap_trim_cost) | `1_M` | Advanced | 性能 |
| [osd_snap_trim_priority](#osd_snap_trim_priority) | `5` | Advanced | 性能 |
| [osd_target_pg_log_entries_per_osd](#osd_target_pg_log_entries_per_osd) | `300000` | Dev | 开发 |
| [osd_target_transaction_size](#osd_target_transaction_size) | `30` | Advanced | 性能 |
| [osd_tier_default_cache_hit_set_count](#osd_tier_default_cache_hit_set_count) | `4` | Advanced | 性能 |
| [osd_tier_default_cache_hit_set_grade_decay_rate](#osd_tier_default_cache_hit_set_grade_decay_rate) | `20` | Advanced | 性能 |
| [osd_tier_default_cache_hit_set_period](#osd_tier_default_cache_hit_set_period) | `1200` | Advanced | 性能 |
| [osd_tier_default_cache_hit_set_search_last_n](#osd_tier_default_cache_hit_set_search_last_n) | `1` | Advanced | 性能 |
| [osd_tier_default_cache_hit_set_type](#osd_tier_default_cache_hit_set_type) | `bloom` | Advanced | 性能 |
| [osd_tier_default_cache_min_read_recency_for_promote](#osd_tier_default_cache_min_read_recency_for_promote) | `1` | Advanced | 性能 |
| [osd_tier_default_cache_min_write_recency_for_promote](#osd_tier_default_cache_min_write_recency_for_promote) | `1` | Advanced | 性能 |
| [osd_tier_default_cache_mode](#osd_tier_default_cache_mode) | `writeback` | Advanced | 性能 |
| [osd_tier_promote_max_bytes_sec](#osd_tier_promote_max_bytes_sec) | `5_M` | Advanced | 性能 |
| [osd_tier_promote_max_objects_sec](#osd_tier_promote_max_objects_sec) | `25` | Advanced | 性能 |
| [osd_tracing](#osd_tracing) | `False` | Advanced | 性能 |
| [osd_use_stale_snap](#osd_use_stale_snap) | `False` | Advanced | 性能 |

## 寻找最优值

| 模型 | 如何选择 |
|-------|---------------|
| **策略** | 安全、兼容性、运维默认值 |
| **容量** | 磁盘布局、路径、容量规划 |
| **性能** | 基线 → 逐步调整 → 监控集群 |
| **连通性** | 最近且稳定的外部端点 |
| **开发** | 生产环境保持 upstream 默认值 |

**常用工具：**

```bash
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_asio_thread_count

| | |
|---|---|
| 类型 | Uint · default `2` · **Advanced** |
| 表格 | [osd.md#SP_osd_asio_thread_count](../../../config/global/osd.md#SP_osd_asio_thread_count) |

**作用：** Size of thread pool for ASIO completions

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_asio_thread_count 2
ceph config get osd osd_asio_thread_count
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `100` · **Advanced** |
| 表格 | [osd.md#SP_osd_async_recovery_min_cost](../../../config/global/osd.md#SP_osd_async_recovery_min_cost) |

**作用：** A mixture measure of number of current log entries difference and historical missing objects, above which we switch to use asynchronous recovery when appropriate

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_async_recovery_min_cost 100
ceph config get osd osd_async_recovery_min_cost
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `100` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_auto_mark_unfound_lost](../../../config/global/osd.md#SP_osd_auto_mark_unfound_lost) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_auto_mark_unfound_lost true
ceph config get osd osd_auto_mark_unfound_lost
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_backoff_on_degraded](../../../config/global/osd.md#SP_osd_backoff_on_degraded) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_backoff_on_degraded true
ceph config get osd osd_backoff_on_degraded
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_backoff_on_peering](../../../config/global/osd.md#SP_osd_backoff_on_peering) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_backoff_on_peering true
ceph config get osd osd_backoff_on_peering
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_backoff_on_unfound](../../../config/global/osd.md#SP_osd_backoff_on_unfound) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_backoff_on_unfound false
ceph config get osd osd_backoff_on_unfound
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `5_min` · **Advanced** |
| 表格 | [osd.md#SP_osd_beacon_report_interval](../../../config/global/osd.md#SP_osd_beacon_report_interval) |

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_beacon_report_interval 5_min
ceph config get osd osd_beacon_report_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `30` · **Advanced** |
| 表格 | [osd.md#SP_osd_bench_duration](../../../config/global/osd.md#SP_osd_bench_duration) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_bench_duration 30
ceph config get osd osd_bench_duration
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `100_M` · **Advanced** |
| 表格 | [osd.md#SP_osd_bench_large_size_max_throughput](../../../config/global/osd.md#SP_osd_bench_large_size_max_throughput) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_bench_large_size_max_throughput 100_M
ceph config get osd osd_bench_large_size_max_throughput
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `100_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `64_M` · **Advanced** |
| 表格 | [osd.md#SP_osd_bench_max_block_size](../../../config/global/osd.md#SP_osd_bench_max_block_size) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_bench_max_block_size 64_M
ceph config get osd osd_bench_max_block_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `100` · **Advanced** |
| 表格 | [osd.md#SP_osd_bench_small_size_max_iops](../../../config/global/osd.md#SP_osd_bench_small_size_max_iops) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_bench_small_size_max_iops 100
ceph config get osd osd_bench_small_size_max_iops
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `100` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_blkin_trace_all](../../../config/global/osd.md#SP_osd_blkin_trace_all) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_blkin_trace_all true
ceph config get osd osd_blkin_trace_all
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_calc_pg_upmaps_aggressively](../../../config/global/osd.md#SP_osd_calc_pg_upmaps_aggressively) |

**作用：** Try to calculate PG upmaps more aggressively, e.g., by doing a fairly exhaustive search of existing PGs that can be unmapped or upmapped

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_calc_pg_upmaps_aggressively false
ceph config get osd osd_calc_pg_upmaps_aggressively
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_calc_pg_upmaps_aggressively_fast](../../../config/global/osd.md#SP_osd_calc_pg_upmaps_aggressively_fast) |

**作用：** Prevent very long (>10 minutes) calculations in some extreme cases (applicable only to aggressive mode)

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_calc_pg_upmaps_aggressively_fast false
ceph config get osd osd_calc_pg_upmaps_aggressively_fast
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `100` · **Advanced** |
| 表格 | [osd.md#SP_osd_calc_pg_upmaps_local_fallback_retries](../../../config/global/osd.md#SP_osd_calc_pg_upmaps_local_fallback_retries) |

**作用：** Maximum number of PGs we can attempt to unmap or upmap for a specific overfull or underfull OSD per iteration

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_calc_pg_upmaps_local_fallback_retries 100
ceph config get osd osd_calc_pg_upmaps_local_fallback_retries
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `100` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_check_for_log_corruption](../../../config/global/osd.md#SP_osd_check_for_log_corruption) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_check_for_log_corruption true
ceph config get osd osd_check_for_log_corruption
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `63` · **Advanced** |
| 表格 | [osd.md#SP_osd_client_op_priority](../../../config/global/osd.md#SP_osd_client_op_priority) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_client_op_priority 63
ceph config get osd osd_client_op_priority
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `63` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `256` · **Advanced** |
| 表格 | [osd.md#SP_osd_command_max_records](../../../config/global/osd.md#SP_osd_command_max_records) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_command_max_records 256
ceph config get osd osd_command_max_records
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `256` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `1` · **Dev** |
| 表格 | [osd.md#SP_osd_crush_chooseleaf_type](../../../config/global/osd.md#SP_osd_crush_chooseleaf_type) |

**作用：** default chooseleaf type for osdmaptool --create

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_crush_chooseleaf_type 1
ceph config get osd osd_crush_chooseleaf_type
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_crash_on_ignored_backoff

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_crash_on_ignored_backoff](../../../config/global/osd.md#SP_osd_debug_crash_on_ignored_backoff) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_crash_on_ignored_backoff true
ceph config get osd osd_debug_crash_on_ignored_backoff
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_deep_scrub_sleep

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_deep_scrub_sleep](../../../config/global/osd.md#SP_osd_debug_deep_scrub_sleep) |

**作用：** Inject an expensive sleep during deep scrub IO to make it easier to induce preemption

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_deep_scrub_sleep 0
ceph config get osd osd_debug_deep_scrub_sleep
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_drop_ping_duration

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_drop_ping_duration](../../../config/global/osd.md#SP_osd_debug_drop_ping_duration) |

**作用：** N/A

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_drop_ping_duration 64
ceph config get osd osd_debug_drop_ping_duration
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_drop_ping_probability

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_drop_ping_probability](../../../config/global/osd.md#SP_osd_debug_drop_ping_probability) |

**作用：** N/A

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_drop_ping_probability 0
ceph config get osd osd_debug_drop_ping_probability
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_inject_copyfrom_error

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_inject_copyfrom_error](../../../config/global/osd.md#SP_osd_debug_inject_copyfrom_error) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_inject_copyfrom_error true
ceph config get osd osd_debug_inject_copyfrom_error
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_inject_dispatch_delay_duration

| | |
|---|---|
| 类型 | Float · default `0.1` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_inject_dispatch_delay_duration](../../../config/global/osd.md#SP_osd_debug_inject_dispatch_delay_duration) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_inject_dispatch_delay_duration 0.1
ceph config get osd osd_debug_inject_dispatch_delay_duration
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0.1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_inject_dispatch_delay_probability

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_inject_dispatch_delay_probability](../../../config/global/osd.md#SP_osd_debug_inject_dispatch_delay_probability) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_inject_dispatch_delay_probability 0
ceph config get osd osd_debug_inject_dispatch_delay_probability
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_misdirected_ops

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_misdirected_ops](../../../config/global/osd.md#SP_osd_debug_misdirected_ops) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_misdirected_ops true
ceph config get osd osd_debug_misdirected_ops
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_no_acting_change

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_no_acting_change](../../../config/global/osd.md#SP_osd_debug_no_acting_change) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_no_acting_change true
ceph config get osd osd_debug_no_acting_change
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_no_purge_strays

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_no_purge_strays](../../../config/global/osd.md#SP_osd_debug_no_purge_strays) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_no_purge_strays true
ceph config get osd osd_debug_no_purge_strays
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_op_order

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_op_order](../../../config/global/osd.md#SP_osd_debug_op_order) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_op_order true
ceph config get osd osd_debug_op_order
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_pg_log_writeout

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_pg_log_writeout](../../../config/global/osd.md#SP_osd_debug_pg_log_writeout) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_pg_log_writeout true
ceph config get osd osd_debug_pg_log_writeout
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_pretend_recovery_active

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_pretend_recovery_active](../../../config/global/osd.md#SP_osd_debug_pretend_recovery_active) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_pretend_recovery_active true
ceph config get osd osd_debug_pretend_recovery_active
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_random_push_read_error

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_random_push_read_error](../../../config/global/osd.md#SP_osd_debug_random_push_read_error) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_random_push_read_error 0
ceph config get osd osd_debug_random_push_read_error
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_reject_backfill_probability

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_reject_backfill_probability](../../../config/global/osd.md#SP_osd_debug_reject_backfill_probability) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_reject_backfill_probability 0
ceph config get osd osd_debug_reject_backfill_probability
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_shutdown

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_shutdown](../../../config/global/osd.md#SP_osd_debug_shutdown) |

**作用：** Turn up debug levels during shutdown

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_shutdown true
ceph config get osd osd_debug_shutdown
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_skip_full_check_in_backfill_reservation

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_skip_full_check_in_backfill_reservation](../../../config/global/osd.md#SP_osd_debug_skip_full_check_in_backfill_reservation) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_skip_full_check_in_backfill_reservation true
ceph config get osd osd_debug_skip_full_check_in_backfill_reservation
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_skip_full_check_in_recovery

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_skip_full_check_in_recovery](../../../config/global/osd.md#SP_osd_debug_skip_full_check_in_recovery) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_skip_full_check_in_recovery true
ceph config get osd osd_debug_skip_full_check_in_recovery
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_verify_cached_snaps

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_verify_cached_snaps](../../../config/global/osd.md#SP_osd_debug_verify_cached_snaps) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_verify_cached_snaps true
ceph config get osd osd_debug_verify_cached_snaps
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_verify_missing_on_start

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_verify_missing_on_start](../../../config/global/osd.md#SP_osd_debug_verify_missing_on_start) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_verify_missing_on_start true
ceph config get osd osd_debug_verify_missing_on_start
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_verify_snaps

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_verify_snaps](../../../config/global/osd.md#SP_osd_debug_verify_snaps) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_verify_snaps true
ceph config get osd osd_debug_verify_snaps
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_verify_stray_on_activate

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_verify_stray_on_activate](../../../config/global/osd.md#SP_osd_debug_verify_stray_on_activate) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_verify_stray_on_activate true
ceph config get osd osd_debug_verify_stray_on_activate
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_default_data_pool_replay_window

| | |
|---|---|
| 类型 | Int · default `45` · **Advanced** |
| 表格 | [osd.md#SP_osd_default_data_pool_replay_window](../../../config/global/osd.md#SP_osd_default_data_pool_replay_window) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_default_data_pool_replay_window 45
ceph config get osd osd_default_data_pool_replay_window
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `45` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `30` · **Advanced** |
| 表格 | [osd.md#SP_osd_default_notify_timeout](../../../config/global/osd.md#SP_osd_default_notify_timeout) |

**作用：** default number of seconds after which notify propagation times out. used if a client has not specified other value

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_default_notify_timeout 30
ceph config get osd osd_default_notify_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_discard_disconnected_ops](../../../config/global/osd.md#SP_osd_discard_disconnected_ops) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_discard_disconnected_ops false
ceph config get osd osd_discard_disconnected_ops
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_enable_op_tracker](../../../config/global/osd.md#SP_osd_enable_op_tracker) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_enable_op_tracker false
ceph config get osd osd_enable_op_tracker
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Str · default `0` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [osd.md#SP_osd_erasure_code_plugins](../../../config/global/osd.md#SP_osd_erasure_code_plugins) |

**作用：** Erasure code plugins to load

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_erasure_code_plugins "example"
ceph config get osd osd_erasure_code_plugins
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `0.97` · **Advanced** |
| 表格 | [osd.md#SP_osd_failsafe_full_ratio](../../../config/global/osd.md#SP_osd_failsafe_full_ratio) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_failsafe_full_ratio 0.97
ceph config get osd osd_failsafe_full_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.97` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_fast_fail_on_connection_refused](../../../config/global/osd.md#SP_osd_fast_fail_on_connection_refused) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_fast_fail_on_connection_refused false
ceph config get osd osd_fast_fail_on_connection_refused
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_fast_info](../../../config/global/osd.md#SP_osd_fast_info) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_fast_info false
ceph config get osd osd_fast_info
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_fast_shutdown](../../../config/global/osd.md#SP_osd_fast_shutdown) |

**作用：** Fast, immediate shutdown Setting this to false makes the OSD do a slower teardown of all state when it receives a SIGINT or SIGTERM or when shutting down for any other reason. That slow shutdown is primarilyy useful for doing memory leak checking with valgrind.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_fast_shutdown false
ceph config get osd osd_fast_shutdown
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_fast_shutdown_notify_mon](../../../config/global/osd.md#SP_osd_fast_shutdown_notify_mon) |

**作用：** Tell the Monitors about OSD shutdown on immediate shutdown Tell the Monitors the OSD is shutting down on immediate shutdown. This helps with cluster log messages from other OSDs reporting it immediately failed.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_fast_shutdown_notify_mon false
ceph config get osd osd_fast_shutdown_notify_mon
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `15` · **Advanced** |
| 表格 | [osd.md#SP_osd_fast_shutdown_timeout](../../../config/global/osd.md#SP_osd_fast_shutdown_timeout) |

**作用：** Timeout in seconds for osd fast-shutdown (0 is unlimited)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_fast_shutdown_timeout 15
ceph config get osd osd_fast_shutdown_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `15` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `100` · **Advanced** |
| 表格 | [osd.md#SP_osd_force_auth_primary_missing_objects](../../../config/global/osd.md#SP_osd_force_auth_primary_missing_objects) |

**作用：** Approximate missing objects above which to force auth_log_shard to be primary temporarily

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_force_auth_primary_missing_objects 100
ceph config get osd osd_force_auth_primary_missing_objects
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `100` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `1.3` · **Dev** |
| 表格 | [osd.md#SP_osd_force_recovery_pg_log_entries_factor](../../../config/global/osd.md#SP_osd_force_recovery_pg_log_entries_factor) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_force_recovery_pg_log_entries_factor 1.3
ceph config get osd osd_force_recovery_pg_log_entries_factor
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1.3`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_function_tracing

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_function_tracing](../../../config/global/osd.md#SP_osd_function_tracing) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_function_tracing true
ceph config get osd osd_function_tracing
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `20` · **Advanced** |
| 表格 | [osd.md#SP_osd_heartbeat_grace](../../../config/global/osd.md#SP_osd_heartbeat_grace) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_heartbeat_grace 20
ceph config get osd osd_heartbeat_grace
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `20` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `6` · **Dev** |
| 表格 | [osd.md#SP_osd_heartbeat_interval](../../../config/global/osd.md#SP_osd_heartbeat_interval) |

**作用：** Interval (in seconds) between peer pings

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_heartbeat_interval 6
ceph config get osd osd_heartbeat_interval
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`6`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_heartbeat_min_healthy_ratio

| | |
|---|---|
| 类型 | Float · default `0.33` · **Advanced** |
| 表格 | [osd.md#SP_osd_heartbeat_min_healthy_ratio](../../../config/global/osd.md#SP_osd_heartbeat_min_healthy_ratio) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_heartbeat_min_healthy_ratio 0.33
ceph config get osd osd_heartbeat_min_healthy_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.33` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `2000` · **Advanced** |
| 表格 | [osd.md#SP_osd_heartbeat_min_size](../../../config/global/osd.md#SP_osd_heartbeat_min_size) |

**作用：** Minimum heartbeat packet size in bytes. Will padd if the heartbeat packet is smaller than this. This helps identify host and switch MTU configuration issues when jumbo frames are in use.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_heartbeat_min_size 2000
ceph config get osd osd_heartbeat_min_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `10_min` · **Advanced** |
| 表格 | [osd.md#SP_osd_heartbeat_stale](../../../config/global/osd.md#SP_osd_heartbeat_stale) |

**作用：** Interval (in seconds) we mark an unresponsive heartbeat peer as stale. Automatically mark unresponsive heartbeat sessions as stale and tear them down. The primary benefit is that OSD doesn't need to keep a flood of blocked heartbeat messages around in memory.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_heartbeat_stale 10_min
ceph config get osd osd_heartbeat_stale
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_heartbeat_use_min_delay_socket](../../../config/global/osd.md#SP_osd_heartbeat_use_min_delay_socket) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_heartbeat_use_min_delay_socket true
ceph config get osd osd_heartbeat_use_min_delay_socket
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `100000` · **Advanced** |
| 表格 | [osd.md#SP_osd_hit_set_max_size](../../../config/global/osd.md#SP_osd_hit_set_max_size) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_hit_set_max_size 100000
ceph config get osd osd_hit_set_max_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `100000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `1000` · **Advanced** |
| 表格 | [osd.md#SP_osd_hit_set_min_size](../../../config/global/osd.md#SP_osd_hit_set_min_size) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_hit_set_min_size 1000
ceph config get osd osd_hit_set_min_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Str · default `.ceph-internal` · **Advanced** |
| 表格 | [osd.md#SP_osd_hit_set_namespace](../../../config/global/osd.md#SP_osd_hit_set_namespace) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_hit_set_namespace ".ceph-internal"
ceph config get osd osd_hit_set_namespace
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `.ceph-internal` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_ignore_stale_divergent_priors](../../../config/global/osd.md#SP_osd_ignore_stale_divergent_priors) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_ignore_stale_divergent_priors true
ceph config get osd osd_ignore_stale_divergent_priors
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `0` · **Dev** |
| 表格 | [osd.md#SP_osd_kill_backfill_at](../../../config/global/osd.md#SP_osd_kill_backfill_at) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_kill_backfill_at 64
ceph config get osd osd_kill_backfill_at
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_loop_before_reset_tphandle

| | |
|---|---|
| 类型 | Uint · default `64` · **Advanced** |
| 表格 | [osd.md#SP_osd_loop_before_reset_tphandle](../../../config/global/osd.md#SP_osd_loop_before_reset_tphandle) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_loop_before_reset_tphandle 64
ceph config get osd osd_loop_before_reset_tphandle
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_map_dedup](../../../config/global/osd.md#SP_osd_map_dedup) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_map_dedup false
ceph config get osd osd_map_dedup
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `40` · **Advanced** |
| 表格 | [osd.md#SP_osd_map_message_max](../../../config/global/osd.md#SP_osd_map_message_max) |

**作用：** Maximum number of OSDMaps to include in a single message

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_map_message_max 40
ceph config get osd osd_map_message_max
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `40` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `10_M` · **Advanced** |
| 表格 | [osd.md#SP_osd_map_message_max_bytes](../../../config/global/osd.md#SP_osd_map_message_max_bytes) |

**作用：** Maximum number of bytes worth of OSDMaps to include in a single message

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_map_message_max_bytes 10_M
ceph config get osd osd_map_message_max_bytes
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `100` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_attr_name_len](../../../config/global/osd.md#SP_osd_max_attr_name_len) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_max_attr_name_len 100
ceph config get osd osd_max_attr_name_len
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `100` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_attr_size](../../../config/global/osd.md#SP_osd_max_attr_size) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_max_attr_size 64
ceph config get osd osd_max_attr_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `2_K` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_object_name_len](../../../config/global/osd.md#SP_osd_max_object_name_len) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_max_object_name_len 2_K
ceph config get osd osd_max_object_name_len
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `256` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_object_namespace_len](../../../config/global/osd.md#SP_osd_max_object_namespace_len) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_max_object_namespace_len 256
ceph config get osd osd_max_object_namespace_len
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `256` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `128_M` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_object_size](../../../config/global/osd.md#SP_osd_max_object_size) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_max_object_size 128_M
ceph config get osd osd_max_object_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `128_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `1_G` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_omap_bytes_per_request](../../../config/global/osd.md#SP_osd_max_omap_bytes_per_request) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_max_omap_bytes_per_request 1_G
ceph config get osd osd_max_omap_bytes_per_request
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_G` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `1_K` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_omap_entries_per_request](../../../config/global/osd.md#SP_osd_max_omap_entries_per_request) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_max_omap_entries_per_request 1_K
ceph config get osd osd_max_omap_entries_per_request
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `16` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_pg_blocked_by](../../../config/global/osd.md#SP_osd_max_pg_blocked_by) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_max_pg_blocked_by 16
ceph config get osd osd_max_pg_blocked_by
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `16` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `10000` · **Dev** |
| 表格 | [osd.md#SP_osd_max_pg_log_entries](../../../config/global/osd.md#SP_osd_max_pg_log_entries) |

**作用：** Maximum number of entries to maintain in the PG log

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_max_pg_log_entries 10000
ceph config get osd osd_max_pg_log_entries
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`10000`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_max_pg_per_osd_hard_ratio

| | |
|---|---|
| 类型 | Float · default `3` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_pg_per_osd_hard_ratio](../../../config/global/osd.md#SP_osd_max_pg_per_osd_hard_ratio) |

**作用：** Maximum multiple of mon_max_pg_per_osd PGs an OSD will allow An OSD will refuse to instantiate a PG if the number of PGs it serves exceeds this number.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_max_pg_per_osd_hard_ratio 3
ceph config get osd osd_max_pg_per_osd_hard_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `512` · **Dev** |
| 表格 | [osd.md#SP_osd_max_snap_prune_intervals_per_epoch](../../../config/global/osd.md#SP_osd_max_snap_prune_intervals_per_epoch) |

**作用：** Max number of snap intervals to report to mgr in pg_stat_t

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_max_snap_prune_intervals_per_epoch 512
ceph config get osd osd_max_snap_prune_intervals_per_epoch
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`512`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_max_trimming_pgs

| | |
|---|---|
| 类型 | Uint · default `2` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_trimming_pgs](../../../config/global/osd.md#SP_osd_max_trimming_pgs) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_max_trimming_pgs 2
ceph config get osd osd_max_trimming_pgs
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `64` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_write_op_reply_len](../../../config/global/osd.md#SP_osd_max_write_op_reply_len) |

**作用：** Max size of the per-op payload for requests with the RETURNVEC flag set This value caps the amount of data (per op; a request may have many ops) that will be sent back to the client and recorded in the PG log.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_max_write_op_reply_len 64
ceph config get osd osd_max_write_op_reply_len
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `768_M` · **Dev** |
| 表格 | [osd.md#SP_osd_memory_base](../../../config/global/osd.md#SP_osd_memory_base) |

**作用：** When TCMalloc and cache autotuning are enabled, estimate the minimum amount of memory in bytes the OSD will need.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_memory_base 768_M
ceph config get osd osd_memory_base
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`768_M`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_memory_cache_min

| | |
|---|---|
| 类型 | Size · default `128_M` · **Dev** |
| 表格 | [osd.md#SP_osd_memory_cache_min](../../../config/global/osd.md#SP_osd_memory_cache_min) |

**作用：** When TCMalloc and cache autotuning are enabled, set the minimum amount of memory used for caches.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_memory_cache_min 128_M
ceph config get osd osd_memory_cache_min
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`128_M`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_memory_cache_resize_interval

| | |
|---|---|
| 类型 | Float · default `1` · **Dev** |
| 表格 | [osd.md#SP_osd_memory_cache_resize_interval](../../../config/global/osd.md#SP_osd_memory_cache_resize_interval) |

**作用：** When TCMalloc and cache autotuning are enabled, wait this many seconds between resizing caches.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_memory_cache_resize_interval 1
ceph config get osd osd_memory_cache_resize_interval
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_memory_expected_fragmentation

| | |
|---|---|
| 类型 | Float · default `0.15` · **Dev** |
| 表格 | [osd.md#SP_osd_memory_expected_fragmentation](../../../config/global/osd.md#SP_osd_memory_expected_fragmentation) |

**作用：** When TCMalloc and cache autotuning are enabled, estimate the percent of memory fragmentation.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_memory_expected_fragmentation 0.15
ceph config get osd osd_memory_expected_fragmentation
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0.15`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_memory_target

| | |
|---|---|
| 类型 | Size · default `4_G` · **Basic** |
| 表格 | [osd.md#SP_osd_memory_target](../../../config/global/osd.md#SP_osd_memory_target) |

**作用：** When TCMalloc and cache autotuning are enabled, try to keep this many bytes mapped in memory. The minimum value must be at least equal to osd_memory_base + osd_memory_cache_min.

**何时使用：** 核心 Global 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set osd osd_memory_target 4_G
ceph config get osd osd_memory_target
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `4_G` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_memory_target_autotune](../../../config/global/osd.md#SP_osd_memory_target_autotune) |

**作用：** If enabled, allow the orchestrator to automatically tune osd_memory_target at host granularity based on available memory, the number of OSDs provisioned on the host, other daemons provisioned on the host, and mgr/cephadm/autotune_memory_target_ratio

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**相关选项：**

- [`osd_memory_target`](../../../config/global/osd.md#SP_osd_memory_target)

**示例：**

```bash
ceph config set osd osd_memory_target_autotune true
ceph config get osd osd_memory_target_autotune
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `0.8` · **Advanced** |
| 表格 | [osd.md#SP_osd_memory_target_cgroup_limit_ratio](../../../config/global/osd.md#SP_osd_memory_target_cgroup_limit_ratio) |

**作用：** Set the default value for osd_memory_target to the cgroup memory limit (if set) times this value A value of 0 disables this feature.

**何时使用：** 触及资源限制或保护集群容量时调整。

**相关选项：**

- [`osd_memory_target`](../../../config/global/osd.md#SP_osd_memory_target)

**示例：**

```bash
ceph config set osd osd_memory_target_cgroup_limit_ratio 0.8
ceph config get osd osd_memory_target_cgroup_limit_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.8` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `1`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `250` · **Dev** |
| 表格 | [osd.md#SP_osd_min_pg_log_entries](../../../config/global/osd.md#SP_osd_min_pg_log_entries) |

**作用：** Minimum number of entries to maintain in the PG log

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_min_pg_log_entries 250
ceph config get osd osd_min_pg_log_entries
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`250`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_min_split_replica_read_size

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_min_split_replica_read_size](../../../config/global/osd.md#SP_osd_min_split_replica_read_size) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_min_split_replica_read_size 64
ceph config get osd osd_min_split_replica_read_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `30` · **Advanced** |
| 表格 | [osd.md#SP_osd_mon_heartbeat_interval](../../../config/global/osd.md#SP_osd_mon_heartbeat_interval) |

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_mon_heartbeat_interval 30
ceph config get osd osd_mon_heartbeat_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `1_hr` · **Advanced** |
| 表格 | [osd.md#SP_osd_mon_heartbeat_stat_stale](../../../config/global/osd.md#SP_osd_mon_heartbeat_stat_stale) |

**作用：** Stop reporting on heartbeat ping times not updated for this many seconds. Stop reporting on old heartbeat information unless this is set to zero

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_mon_heartbeat_stat_stale 1_hr
ceph config get osd osd_mon_heartbeat_stat_stale
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_hr` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [osd.md#SP_osd_mon_report_interval](../../../config/global/osd.md#SP_osd_mon_report_interval) |

**作用：** Frequency of OSD reports to mon for peer failures, fullness status changes

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_mon_report_interval 5
ceph config get osd osd_mon_report_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `2` · **Advanced** |
| 表格 | [osd.md#SP_osd_mon_report_max_in_flight](../../../config/global/osd.md#SP_osd_mon_report_max_in_flight) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_mon_report_max_in_flight 2
ceph config get osd osd_mon_report_max_in_flight
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [osd.md#SP_osd_mon_shutdown_timeout](../../../config/global/osd.md#SP_osd_mon_shutdown_timeout) |

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_mon_shutdown_timeout 5
ceph config get osd osd_mon_shutdown_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `32` · **Advanced** |
| 表格 | [osd.md#SP_osd_num_op_tracker_shard](../../../config/global/osd.md#SP_osd_num_op_tracker_shard) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_num_op_tracker_shard 32
ceph config get osd osd_num_op_tracker_shard
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `32` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `10` · **Dev** |
| 表格 | [osd.md#SP_osd_object_clean_region_max_num_intervals](../../../config/global/osd.md#SP_osd_object_clean_region_max_num_intervals) |

**作用：** Number of intervals in clean_offsets Partial recovery uses multiple intervals to record the clean part of the objectwhen the number of intervals is greater than osd_object_clean_region_max_num_intervals, minimum interval will be trimmed(0 will recovery the entire object data interval)

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_object_clean_region_max_num_intervals 10
ceph config get osd osd_object_clean_region_max_num_intervals
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`10`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_objecter_finishers

| | |
|---|---|
| 类型 | Int · default `1` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [osd.md#SP_osd_objecter_finishers](../../../config/global/osd.md#SP_osd_objecter_finishers) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_objecter_finishers 1
ceph config get osd osd_objecter_finishers
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Str · enum: ["bluestore", "filestore", "memstore", "seastore", "cyanstore"] · default `bluestore` · **Advanced** |
| 表格 | [osd.md#SP_osd_objectstore](../../../config/global/osd.md#SP_osd_objectstore) |

**作用：** Default back end for new OSDs

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_objectstore bluestore
ceph config get osd osd_objectstore
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `bluestore` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_objectstore_fuse](../../../config/global/osd.md#SP_osd_objectstore_fuse) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_objectstore_fuse true
ceph config get osd osd_objectstore_fuse
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `64` · **Advanced** |
| 表格 | [osd.md#SP_osd_objectstore_ideal_list_max](../../../config/global/osd.md#SP_osd_objectstore_ideal_list_max) |

**作用：** The max number of results of ObjectStore::collection_list() This value caps the maximal number of entries a single call to collection_list() can return. The configurable controls this aspect of PG deletion and OSD::clear_temp_objects(). Increasing it trade-offs less agressive chunking (and thus less CPU consumption overall) for higher memory pressure. Please note that in the case of PG deletion the chunking is steered by std::min of the this value and the value of osd_target_transaction_size.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**相关选项：**

- [`osd_memory_target`](../../../config/global/osd.md#SP_osd_memory_target)

**示例：**

```bash
ceph config set osd osd_objectstore_ideal_list_max 64
ceph config get osd osd_objectstore_ideal_list_max
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_objectstore_tracing](../../../config/global/osd.md#SP_osd_objectstore_tracing) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_objectstore_tracing true
ceph config get osd osd_objectstore_tracing
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `30` · **Advanced** |
| 表格 | [osd.md#SP_osd_op_complaint_time](../../../config/global/osd.md#SP_osd_op_complaint_time) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_op_complaint_time 30
ceph config get osd osd_op_complaint_time
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `600` · **Advanced** |
| 表格 | [osd.md#SP_osd_op_history_duration](../../../config/global/osd.md#SP_osd_op_history_duration) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_op_history_duration 600
ceph config get osd osd_op_history_duration
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `600` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `20` · **Advanced** |
| 表格 | [osd.md#SP_osd_op_history_size](../../../config/global/osd.md#SP_osd_op_history_size) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_op_history_size 20
ceph config get osd osd_op_history_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `20` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `20` · **Advanced** |
| 表格 | [osd.md#SP_osd_op_history_slow_op_size](../../../config/global/osd.md#SP_osd_op_history_slow_op_size) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_op_history_slow_op_size 20
ceph config get osd osd_op_history_slow_op_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `20` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `10` · **Advanced** |
| 表格 | [osd.md#SP_osd_op_history_slow_op_threshold](../../../config/global/osd.md#SP_osd_op_history_slow_op_threshold) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_op_history_slow_op_threshold 10
ceph config get osd osd_op_history_slow_op_threshold
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [osd.md#SP_osd_op_log_threshold](../../../config/global/osd.md#SP_osd_op_log_threshold) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_op_log_threshold 5
ceph config get osd osd_op_log_threshold
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `255` · **Dev** |
| 表格 | [osd.md#SP_osd_peering_op_priority](../../../config/global/osd.md#SP_osd_peering_op_priority) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_peering_op_priority 255
ceph config get osd osd_peering_op_priority
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`255`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_pg_delete_cost

| | |
|---|---|
| 类型 | Size · default `1_M` · **Advanced** |
| 表格 | [osd.md#SP_osd_pg_delete_cost](../../../config/global/osd.md#SP_osd_pg_delete_cost) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_pg_delete_cost 1_M
ceph config get osd osd_pg_delete_cost
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `5` · **Advanced** |
| 表格 | [osd.md#SP_osd_pg_delete_priority](../../../config/global/osd.md#SP_osd_pg_delete_priority) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_pg_delete_priority 5
ceph config get osd osd_pg_delete_priority
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `40` · **Advanced** |
| 表格 | [osd.md#SP_osd_pg_epoch_persisted_max_stale](../../../config/global/osd.md#SP_osd_pg_epoch_persisted_max_stale) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_pg_epoch_persisted_max_stale 40
ceph config get osd osd_pg_epoch_persisted_max_stale
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `40` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `3000` · **Dev** |
| 表格 | [osd.md#SP_osd_pg_log_dups_tracked](../../../config/global/osd.md#SP_osd_pg_log_dups_tracked) |

**作用：** How many versions back to track in order to detect duplicate ops; this is combined with both the regular pg log entries and additional minimal dup detection entries

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_pg_log_dups_tracked 3000
ceph config get osd osd_pg_log_dups_tracked
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`3000`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_pg_log_trim_max

| | |
|---|---|
| 类型 | Uint · default `10000` · **Advanced** |
| 表格 | [osd.md#SP_osd_pg_log_trim_max](../../../config/global/osd.md#SP_osd_pg_log_trim_max) |

**作用：** Maximum number of entries to remove at once from the PG log

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_pg_log_trim_max 10000
ceph config get osd osd_pg_log_trim_max
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `100` · **Dev** |
| 表格 | [osd.md#SP_osd_pg_log_trim_min](../../../config/global/osd.md#SP_osd_pg_log_trim_min) |

**作用：** Minimum number of log entries to trim at once. This lets us trim in larger batches rather than with each write.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_pg_log_trim_min 100
ceph config get osd osd_pg_log_trim_min
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`100`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_pg_max_concurrent_snap_trims

| | |
|---|---|
| 类型 | Uint · default `2` · **Advanced** |
| 表格 | [osd.md#SP_osd_pg_max_concurrent_snap_trims](../../../config/global/osd.md#SP_osd_pg_max_concurrent_snap_trims) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_pg_max_concurrent_snap_trims 2
ceph config get osd osd_pg_max_concurrent_snap_trims
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `64` · **Advanced** |
| 表格 | [osd.md#SP_osd_pg_object_context_cache_count](../../../config/global/osd.md#SP_osd_pg_object_context_cache_count) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_pg_object_context_cache_count 64
ceph config get osd osd_pg_object_context_cache_count
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `500` · **Advanced** |
| 表格 | [osd.md#SP_osd_pg_stat_report_interval_max_epochs](../../../config/global/osd.md#SP_osd_pg_stat_report_interval_max_epochs) |

**作用：** The maximum number of epochs allowed to pass before PG stats are collected.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_pg_stat_report_interval_max_epochs 500
ceph config get osd osd_pg_stat_report_interval_max_epochs
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `500` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [osd.md#SP_osd_pg_stat_report_interval_max_seconds](../../../config/global/osd.md#SP_osd_pg_stat_report_interval_max_seconds) |

**作用：** How often (in seconds) should PGs stats be collected.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_pg_stat_report_interval_max_seconds 5
ceph config get osd osd_pg_stat_report_interval_max_seconds
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `10` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_cache_max_evict_check_size](../../../config/global/osd.md#SP_osd_pool_default_cache_max_evict_check_size) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_pool_default_cache_max_evict_check_size 10
ceph config get osd osd_pool_default_cache_max_evict_check_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_cache_min_evict_age](../../../config/global/osd.md#SP_osd_pool_default_cache_min_evict_age) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_pool_default_cache_min_evict_age 64
ceph config get osd osd_pool_default_cache_min_evict_age
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_cache_min_flush_age](../../../config/global/osd.md#SP_osd_pool_default_cache_min_flush_age) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_pool_default_cache_min_flush_age 64
ceph config get osd osd_pool_default_cache_min_flush_age
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `0.6` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_cache_target_dirty_high_ratio](../../../config/global/osd.md#SP_osd_pool_default_cache_target_dirty_high_ratio) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_pool_default_cache_target_dirty_high_ratio 0.6
ceph config get osd osd_pool_default_cache_target_dirty_high_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.6` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `0.4` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_cache_target_dirty_ratio](../../../config/global/osd.md#SP_osd_pool_default_cache_target_dirty_ratio) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_pool_default_cache_target_dirty_ratio 0.4
ceph config get osd osd_pool_default_cache_target_dirty_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.4` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `0.8` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_cache_target_full_ratio](../../../config/global/osd.md#SP_osd_pool_default_cache_target_full_ratio) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_pool_default_cache_target_full_ratio 0.8
ceph config get osd osd_pool_default_cache_target_full_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.8` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `-1` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_crush_rule](../../../config/global/osd.md#SP_osd_pool_default_crush_rule) |

**作用：** CRUSH rule for newly created pools

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_pool_default_crush_rule 128
ceph config get osd osd_pool_default_crush_rule
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `-1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_ec_fast_read](../../../config/global/osd.md#SP_osd_pool_default_ec_fast_read) |

**作用：** set ec_fast_read for new erasure-coded pools

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_pool_default_ec_fast_read true
ceph config get osd osd_pool_default_ec_fast_read
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Str · default `plugin=isa technique=reed_sol_van k=2 m=2` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_erasure_code_profile](../../../config/global/osd.md#SP_osd_pool_default_erasure_code_profile) |

**作用：** Default EC profile for new erasure-coded pools

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_pool_default_erasure_code_profile "plugin=isa technique=reed_sol_van k=2 m=2"
ceph config get osd osd_pool_default_erasure_code_profile
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `plugin=isa technique=reed_sol_van k=2 m=2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_flag_bulk](../../../config/global/osd.md#SP_osd_pool_default_flag_bulk) |

**作用：** Set the bulk flag on new pools

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_pool_default_flag_bulk true
ceph config get osd osd_pool_default_flag_bulk
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_flag_ec_optimizations](../../../config/global/osd.md#SP_osd_pool_default_flag_ec_optimizations) |

**作用：** Control whether to create new erasure coded pools with EC optimizations turned on by default.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_pool_default_flag_ec_optimizations true
ceph config get osd osd_pool_default_flag_ec_optimizations
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_flag_hashpspool](../../../config/global/osd.md#SP_osd_pool_default_flag_hashpspool) |

**作用：** Set hashpspool (better hashing scheme) flag on new pools

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_pool_default_flag_hashpspool false
ceph config get osd osd_pool_default_flag_hashpspool
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_flag_nodelete](../../../config/global/osd.md#SP_osd_pool_default_flag_nodelete) |

**作用：** Set the nodelete flag on new pools

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_pool_default_flag_nodelete true
ceph config get osd osd_pool_default_flag_nodelete
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_flag_nopgchange](../../../config/global/osd.md#SP_osd_pool_default_flag_nopgchange) |

**作用：** Set the nopgchange flag on new pools

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_pool_default_flag_nopgchange true
ceph config get osd osd_pool_default_flag_nopgchange
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_flag_nosizechange](../../../config/global/osd.md#SP_osd_pool_default_flag_nosizechange) |

**作用：** Set the nosizechange flag on new pools

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_pool_default_flag_nosizechange true
ceph config get osd osd_pool_default_flag_nosizechange
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `0` · **Dev** |
| 表格 | [osd.md#SP_osd_pool_default_flags](../../../config/global/osd.md#SP_osd_pool_default_flags) |

**作用：** The (integer) flags to set on new pools

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_pool_default_flags 64
ceph config get osd osd_pool_default_flags
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_pool_default_hit_set_bloom_fpp

| | |
|---|---|
| 类型 | Float · default `0.05` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_hit_set_bloom_fpp](../../../config/global/osd.md#SP_osd_pool_default_hit_set_bloom_fpp) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**相关选项：**

- [`osd_tier_default_cache_hit_set_type`](../../../config/global/osd.md#SP_osd_tier_default_cache_hit_set_type)

**示例：**

```bash
ceph config set osd osd_pool_default_hit_set_bloom_fpp 0.05
ceph config get osd osd_pool_default_hit_set_bloom_fpp
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.05` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_min_size](../../../config/global/osd.md#SP_osd_pool_default_min_size) |

**作用：** The minimal number of copies allowed to write to a degraded pool for new replicated pools 0 means no specific default; ceph will use size-size/2

**何时使用：** 触及资源限制或保护集群容量时调整。

**相关选项：**

- [`osd_pool_default_size`](../../../config/global/osd.md#SP_osd_pool_default_size)

**示例：**

```bash
ceph config set osd osd_pool_default_min_size 64
ceph config get osd osd_pool_default_min_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `255`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Str · enum: ["off", "warn", "on"] · default `on` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_pg_autoscale_mode](../../../config/global/osd.md#SP_osd_pool_default_pg_autoscale_mode) |

**作用：** Default PG autoscaling behavior for new pools When 'on', the autoscaler assigns 1 pg to new pools unless the user specifies a value.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_pool_default_pg_autoscale_mode on
ceph config get osd osd_pool_default_pg_autoscale_mode
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `on` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `32` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_pg_num](../../../config/global/osd.md#SP_osd_pool_default_pg_num) |

**作用：** number of PGs for new pools With default value of `osd_pool_default_pg_autoscale_mode` being `on` the number of PGs for new pools will start out with 1 pg, unless the user specifies the pg_num.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**相关选项：**

- [`osd_pool_default_pg_autoscale_mode`](../../../config/global/osd.md#SP_osd_pool_default_pg_autoscale_mode)

**示例：**

```bash
ceph config set osd osd_pool_default_pg_num 32
ceph config get osd osd_pool_default_pg_num
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `32` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_pgp_num](../../../config/global/osd.md#SP_osd_pool_default_pgp_num) |

**作用：** number of PGs for placement purposes (0 to match pg_num)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_pool_default_pgp_num 64
ceph config get osd osd_pool_default_pgp_num
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `0.8` · **Dev** |
| 表格 | [osd.md#SP_osd_pool_default_read_lease_ratio](../../../config/global/osd.md#SP_osd_pool_default_read_lease_ratio) |

**作用：** Default read_lease_ratio for a pool, as a multiple of osd_heartbeat_grace This should be <= 1.0 so that the read lease will have expired by the time we decide to mark a peer OSD down.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**相关选项：**

- [`osd_heartbeat_grace`](../../../config/global/osd.md#SP_osd_heartbeat_grace)

**示例：**

```bash
ceph config set osd osd_pool_default_read_lease_ratio 0.8
ceph config get osd osd_pool_default_read_lease_ratio
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0.8`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_pool_default_read_ratio

| | |
|---|---|
| 类型 | Uint · default `70` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_read_ratio](../../../config/global/osd.md#SP_osd_pool_default_read_ratio) |

**作用：** Default read ratio (the percent of read IOs out of all IOs) for a pool. Default read ratio (the percent of read IOs out of all IOs) for a pool. applicable to replicated pools only. This value is used to improve read balancing when OSDs have different weights.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_pool_default_read_ratio 70
ceph config get osd osd_pool_default_read_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `70` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `3` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_size](../../../config/global/osd.md#SP_osd_pool_default_size) |

**作用：** the number of copies of an object for new replicated pools

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_pool_default_size 3
ceph config get osd osd_pool_default_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `10`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Str · enum: ["replicated", "erasure"] · default `replicated` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_type](../../../config/global/osd.md#SP_osd_pool_default_type) |

**作用：** Default data protection strategy type when creating a new pool

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_pool_default_type replicated
ceph config get osd osd_pool_default_type
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `replicated` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [osd.md#SP_osd_pool_use_gmt_hitset](../../../config/global/osd.md#SP_osd_pool_use_gmt_hitset) |

**作用：** use UTC for hitset timestamps This setting only exists for compatibility with hammer (and older) clusters.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_pool_use_gmt_hitset false
ceph config get osd osd_pool_use_gmt_hitset
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_recovery_cost

| | |
|---|---|
| 类型 | Size · default `20_M` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_cost](../../../config/global/osd.md#SP_osd_recovery_cost) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_recovery_cost 20_M
ceph config get osd osd_recovery_cost
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `20_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `3` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_op_priority](../../../config/global/osd.md#SP_osd_recovery_op_priority) |

**作用：** Priority to use for recovery operations if not specified for the pool

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_recovery_op_priority 3
ceph config get osd osd_recovery_op_priority
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `16` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_op_warn_multiple](../../../config/global/osd.md#SP_osd_recovery_op_warn_multiple) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_recovery_op_warn_multiple 16
ceph config get osd osd_recovery_op_warn_multiple
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `16` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `5` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_priority](../../../config/global/osd.md#SP_osd_recovery_priority) |

**作用：** Priority of recovery in the work queue Not related to a pool's recovery_priority

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_recovery_priority 5
ceph config get osd osd_recovery_priority
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `5` · **Advanced** |
| 表格 | [osd.md#SP_osd_requested_scrub_priority](../../../config/global/osd.md#SP_osd_requested_scrub_priority) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_requested_scrub_priority 5
ceph config get osd osd_requested_scrub_priority
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [osd.md#SP_osd_rollback_to_cluster_snap](../../../config/global/osd.md#SP_osd_rollback_to_cluster_snap) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_rollback_to_cluster_snap "example"
ceph config get osd osd_rollback_to_cluster_snap
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `50_M` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_cost](../../../config/global/osd.md#SP_osd_scrub_cost) |

**作用：** Cost for scrub operations in work queue

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_scrub_cost 50_M
ceph config get osd osd_scrub_cost
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `50_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `4_K` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_event_cost](../../../config/global/osd.md#SP_osd_scrub_event_cost) |

**作用：** Cost for each scrub operation, used when osd_op_queue=mclock_scheduler

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_scrub_event_cost 4_K
ceph config get osd osd_scrub_event_cost
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `4_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `5` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_priority](../../../config/global/osd.md#SP_osd_scrub_priority) |

**作用：** Priority for scrub operations in work queue

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_scrub_priority 5
ceph config get osd osd_scrub_priority
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_shutdown_pgref_assert](../../../config/global/osd.md#SP_osd_shutdown_pgref_assert) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_shutdown_pgref_assert true
ceph config get osd osd_shutdown_pgref_assert
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_skip_check_past_interval_bounds](../../../config/global/osd.md#SP_osd_skip_check_past_interval_bounds) |

**作用：** See https://tracker.ceph.com/issues/64002

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_skip_check_past_interval_bounds true
ceph config get osd osd_skip_check_past_interval_bounds
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_snap_trim_cost

| | |
|---|---|
| 类型 | Size · default `1_M` · **Advanced** |
| 表格 | [osd.md#SP_osd_snap_trim_cost](../../../config/global/osd.md#SP_osd_snap_trim_cost) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_snap_trim_cost 1_M
ceph config get osd osd_snap_trim_cost
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `5` · **Advanced** |
| 表格 | [osd.md#SP_osd_snap_trim_priority](../../../config/global/osd.md#SP_osd_snap_trim_priority) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_snap_trim_priority 5
ceph config get osd osd_snap_trim_priority
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `300000` · **Dev** |
| 表格 | [osd.md#SP_osd_target_pg_log_entries_per_osd](../../../config/global/osd.md#SP_osd_target_pg_log_entries_per_osd) |

**作用：** Target number of PG entries total on an OSD, limited per PG by the min and max options below

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_target_pg_log_entries_per_osd 300000
ceph config get osd osd_target_pg_log_entries_per_osd
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`300000`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_target_transaction_size

| | |
|---|---|
| 类型 | Uint · default `30` · **Advanced** |
| 表格 | [osd.md#SP_osd_target_transaction_size](../../../config/global/osd.md#SP_osd_target_transaction_size) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_target_transaction_size 30
ceph config get osd osd_target_transaction_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `4` · **Advanced** |
| 表格 | [osd.md#SP_osd_tier_default_cache_hit_set_count](../../../config/global/osd.md#SP_osd_tier_default_cache_hit_set_count) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_tier_default_cache_hit_set_count 4
ceph config get osd osd_tier_default_cache_hit_set_count
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `4` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `20` · **Advanced** |
| 表格 | [osd.md#SP_osd_tier_default_cache_hit_set_grade_decay_rate](../../../config/global/osd.md#SP_osd_tier_default_cache_hit_set_grade_decay_rate) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_tier_default_cache_hit_set_grade_decay_rate 20
ceph config get osd osd_tier_default_cache_hit_set_grade_decay_rate
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `20` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `1200` · **Advanced** |
| 表格 | [osd.md#SP_osd_tier_default_cache_hit_set_period](../../../config/global/osd.md#SP_osd_tier_default_cache_hit_set_period) |

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_tier_default_cache_hit_set_period 1200
ceph config get osd osd_tier_default_cache_hit_set_period
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1200` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [osd.md#SP_osd_tier_default_cache_hit_set_search_last_n](../../../config/global/osd.md#SP_osd_tier_default_cache_hit_set_search_last_n) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_tier_default_cache_hit_set_search_last_n 1
ceph config get osd osd_tier_default_cache_hit_set_search_last_n
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Str · enum: ["bloom", "explicit_hash", "explicit_object"] · default `bloom` · **Advanced** |
| 表格 | [osd.md#SP_osd_tier_default_cache_hit_set_type](../../../config/global/osd.md#SP_osd_tier_default_cache_hit_set_type) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_tier_default_cache_hit_set_type bloom
ceph config get osd osd_tier_default_cache_hit_set_type
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `bloom` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [osd.md#SP_osd_tier_default_cache_min_read_recency_for_promote](../../../config/global/osd.md#SP_osd_tier_default_cache_min_read_recency_for_promote) |

**作用：** Number of recent HitSets the object must appear in to be promoted (on read)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_tier_default_cache_min_read_recency_for_promote 1
ceph config get osd osd_tier_default_cache_min_read_recency_for_promote
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [osd.md#SP_osd_tier_default_cache_min_write_recency_for_promote](../../../config/global/osd.md#SP_osd_tier_default_cache_min_write_recency_for_promote) |

**作用：** Number of recent HitSets the object must appear in to be promoted (on write)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_tier_default_cache_min_write_recency_for_promote 1
ceph config get osd osd_tier_default_cache_min_write_recency_for_promote
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Str · enum: ["none", "writeback", "forward", "readonly", "readforward", "readproxy", "proxy"] · default `writeback` · **Advanced** |
| 表格 | [osd.md#SP_osd_tier_default_cache_mode](../../../config/global/osd.md#SP_osd_tier_default_cache_mode) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_tier_default_cache_mode writeback
ceph config get osd osd_tier_default_cache_mode
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `writeback` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `5_M` · **Advanced** |
| 表格 | [osd.md#SP_osd_tier_promote_max_bytes_sec](../../../config/global/osd.md#SP_osd_tier_promote_max_bytes_sec) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_tier_promote_max_bytes_sec 5_M
ceph config get osd osd_tier_promote_max_bytes_sec
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `25` · **Advanced** |
| 表格 | [osd.md#SP_osd_tier_promote_max_objects_sec](../../../config/global/osd.md#SP_osd_tier_promote_max_objects_sec) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_tier_promote_max_objects_sec 25
ceph config get osd osd_tier_promote_max_objects_sec
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `25` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_tracing](../../../config/global/osd.md#SP_osd_tracing) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_tracing true
ceph config get osd osd_tracing
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_use_stale_snap](../../../config/global/osd.md#SP_osd_use_stale_snap) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_use_stale_snap true
ceph config get osd osd_use_stale_snap
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_use_stale_snap
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← 概览](../OVERVIEW.md)
