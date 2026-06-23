# MDS 配置 — 调优快速参考

全部 **194** 个选项的调优模型与一行建议。

[← 概览](../OVERVIEW.md)

| 选项 | 默认值 | 模型 | 快速建议 | 主题 |
|--------|---------|-------|--------------|-------|
| [`defer_client_eviction_on_laggy_osds`](ops/general.md#defer_client_eviction_on_laggy_osds) | `False` | 性能 | 按实测需求启用/禁用 | [General](ops/general.md) |
| [`mds_abort_on_newly_corrupt_dentry`](mds-core/mds-core.md#mds_abort_on_newly_corrupt_dentry) | `True` | 性能 | 按实测需求启用/禁用 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_action_on_write_error`](mds-core/mds-core.md#mds_action_on_write_error) | `1` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_allow_async_dirops`](mds-core/mds-core.md#mds_allow_async_dirops) | `True` | 策略 | 符合安全与兼容性策略 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_allow_batched_ops`](mds-core/mds-core.md#mds_allow_batched_ops) | `True` | 策略 | 符合安全与兼容性策略 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_alternate_name_max`](mds-core/mds-core.md#mds_alternate_name_max) | `8_K` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_asio_thread_count`](mds-core/mds-core.md#mds_asio_thread_count) | `2` | 性能 | 保持在文档边界内 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_export_pin`](mds-core/mds-core.md#mds_bal_export_pin) | `True` | 性能 | 按实测需求启用/禁用 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_fragment_dirs`](mds-core/mds-core.md#mds_bal_fragment_dirs) | `True` | 性能 | 按实测需求启用/禁用 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_fragment_fast_factor`](mds-core/mds-core.md#mds_bal_fragment_fast_factor) | `1.5` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_fragment_interval`](ops/intervals.md#mds_bal_fragment_interval) | `5` | 性能 | 基线 → 调整 → 负载下验证 | [Intervals](ops/intervals.md) |
| [`mds_bal_fragment_size_max`](mds-core/mds-core.md#mds_bal_fragment_size_max) | `100000` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_idle_threshold`](mds-core/mds-core.md#mds_bal_idle_threshold) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_interval`](ops/intervals.md#mds_bal_interval) | `10` | 性能 | 基线 → 调整 → 负载下验证 | [Intervals](ops/intervals.md) |
| [`mds_bal_max`](mds-core/mds-core.md#mds_bal_max) | `-1` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_max_until`](mds-core/mds-core.md#mds_bal_max_until) | `-1` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_merge_size`](mds-core/mds-core.md#mds_bal_merge_size) | `50` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_midchunk`](mds-core/mds-core.md#mds_bal_midchunk) | `0.3` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_min_rebalance`](mds-core/mds-core.md#mds_bal_min_rebalance) | `0.1` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_min_start`](mds-core/mds-core.md#mds_bal_min_start) | `0.2` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_minchunk`](mds-core/mds-core.md#mds_bal_minchunk) | `0.001` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_mode`](mds-core/mds-core.md#mds_bal_mode) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_need_max`](mds-core/mds-core.md#mds_bal_need_max) | `1.2` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_need_min`](mds-core/mds-core.md#mds_bal_need_min) | `0.8` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_overload_epochs`](mds-core/mds-core.md#mds_bal_overload_epochs) | `2` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_replicate_threshold`](mds-core/mds-core.md#mds_bal_replicate_threshold) | `8000` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_sample_interval`](ops/intervals.md#mds_bal_sample_interval) | `3` | 性能 | 基线 → 调整 → 负载下验证 | [Intervals](ops/intervals.md) |
| [`mds_bal_split_bits`](mds-core/mds-core.md#mds_bal_split_bits) | `3` | 性能 | 保持在文档边界内 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_split_rd`](mds-core/mds-core.md#mds_bal_split_rd) | `25000` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_split_size`](mds-core/mds-core.md#mds_bal_split_size) | `10000` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_split_wr`](mds-core/mds-core.md#mds_bal_split_wr) | `10000` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_target_decay`](mds-core/mds-core.md#mds_bal_target_decay) | `10` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_bal_unreplicate_threshold`](mds-core/mds-core.md#mds_bal_unreplicate_threshold) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_beacon_grace`](mds-core/mds-core.md#mds_beacon_grace) | `15` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_beacon_interval`](ops/intervals.md#mds_beacon_interval) | `4` | 性能 | 基线 → 调整 → 负载下验证 | [Intervals](ops/intervals.md) |
| [`mds_cache_memory_limit`](mds-core/mds-core.md#mds_cache_memory_limit) | `4_G` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_cache_mid`](mds-core/mds-core.md#mds_cache_mid) | `0.7` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_cache_quiesce_decay_rate`](mds-core/mds-core.md#mds_cache_quiesce_decay_rate) | `1` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_cache_quiesce_delay`](mds-core/mds-core.md#mds_cache_quiesce_delay) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_cache_quiesce_sleep`](mds-core/mds-core.md#mds_cache_quiesce_sleep) | `200` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_cache_quiesce_splitauth`](auth-logging/auth.md#mds_cache_quiesce_splitauth) | `True` | 策略 | 符合安全与兼容性策略 | [Auth & capabilities](auth-logging/auth.md) |
| [`mds_cache_quiesce_threshold`](mds-core/mds-core.md#mds_cache_quiesce_threshold) | `512_K` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_cache_release_free_interval`](ops/intervals.md#mds_cache_release_free_interval) | `10` | 开发 | 生产环境保持 upstream 默认值 | [Intervals](ops/intervals.md) |
| [`mds_cache_reservation`](mds-core/mds-core.md#mds_cache_reservation) | `0.05` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_cache_trim_decay_rate`](mds-core/mds-core.md#mds_cache_trim_decay_rate) | `1` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_cache_trim_interval`](ops/intervals.md#mds_cache_trim_interval) | `1` | 性能 | 基线 → 调整 → 负载下验证 | [Intervals](ops/intervals.md) |
| [`mds_cache_trim_threshold`](mds-core/mds-core.md#mds_cache_trim_threshold) | `256_K` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_cap_acquisition_throttle_retry_request_timeout`](auth-logging/auth.md#mds_cap_acquisition_throttle_retry_request_timeout) | `0.5` | 性能 | 基线 → 调整 → 负载下验证 | [Auth & capabilities](auth-logging/auth.md) |
| [`mds_cap_revoke_eviction_timeout`](auth-logging/auth.md#mds_cap_revoke_eviction_timeout) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Auth & capabilities](auth-logging/auth.md) |
| [`mds_client_delegate_inos_pct`](mds-core/mds-core.md#mds_client_delegate_inos_pct) | `50` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_client_prealloc_inos`](mds-core/mds-core.md#mds_client_prealloc_inos) | `1000` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_client_writeable_range_max_inc_objs`](mds-core/mds-core.md#mds_client_writeable_range_max_inc_objs) | `1_K` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_connect_bootstrapping`](mds-core/mds-core.md#mds_connect_bootstrapping) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_damage_table_max_entries`](mds-core/mds-core.md#mds_damage_table_max_entries) | `10000` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_data`](mds-core/mds-core.md#mds_data) | `/var/lib/ceph/mds/$cluster-$id` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_debug_auth_pins`](auth-logging/auth.md#mds_debug_auth_pins) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Auth & capabilities](auth-logging/auth.md) |
| [`mds_debug_frag`](ops/debug.md#mds_debug_frag) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Debug](ops/debug.md) |
| [`mds_debug_scatterstat`](ops/debug.md#mds_debug_scatterstat) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Debug](ops/debug.md) |
| [`mds_debug_subtrees`](ops/debug.md#mds_debug_subtrees) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Debug](ops/debug.md) |
| [`mds_decay_halflife`](mds-core/mds-core.md#mds_decay_halflife) | `5` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_default_dir_hash`](mds-core/mds-core.md#mds_default_dir_hash) | `2` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_defer_session_stale`](mds-core/mds-core.md#mds_defer_session_stale) | `True` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_delay_journal_replay_for_testing`](mds-core/mds-core.md#mds_delay_journal_replay_for_testing) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_deny_all_reconnect`](mds-core/mds-core.md#mds_deny_all_reconnect) | `False` | 性能 | 按实测需求启用/禁用 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_dir_keys_per_op`](mds-core/mds-core.md#mds_dir_keys_per_op) | `16384` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_dir_max_commit_size`](mds-core/mds-core.md#mds_dir_max_commit_size) | `10` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_dir_max_entries`](mds-core/mds-core.md#mds_dir_max_entries) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_dir_prefetch`](mds-core/mds-core.md#mds_dir_prefetch) | `True` | 性能 | 按实测需求启用/禁用 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_dirstat_min_interval`](ops/intervals.md#mds_dirstat_min_interval) | `1` | 开发 | 生产环境保持 upstream 默认值 | [Intervals](ops/intervals.md) |
| [`mds_dump_cache_after_rejoin`](mds-core/mds-core.md#mds_dump_cache_after_rejoin) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_dump_cache_on_map`](mds-core/mds-core.md#mds_dump_cache_on_map) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_dump_cache_threshold_file`](mds-core/mds-core.md#mds_dump_cache_threshold_file) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_dump_cache_threshold_formatter`](mds-core/mds-core.md#mds_dump_cache_threshold_formatter) | `1_G` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_early_reply`](mds-core/mds-core.md#mds_early_reply) | `True` | 性能 | 按实测需求启用/禁用 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_enable_op_tracker`](mds-core/mds-core.md#mds_enable_op_tracker) | `True` | 策略 | 符合安全与兼容性策略 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_enforce_unique_name`](mds-core/mds-core.md#mds_enforce_unique_name) | `True` | 策略 | 符合安全与兼容性策略 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_export_ephemeral_distributed`](mds-core/mds-core.md#mds_export_ephemeral_distributed) | `True` | 性能 | 按实测需求启用/禁用 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_export_ephemeral_distributed_factor`](mds-core/mds-core.md#mds_export_ephemeral_distributed_factor) | `2` | 性能 | 保持在文档边界内 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_export_ephemeral_random`](mds-core/mds-core.md#mds_export_ephemeral_random) | `True` | 性能 | 按实测需求启用/禁用 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_export_ephemeral_random_max`](mds-core/mds-core.md#mds_export_ephemeral_random_max) | `0.01` | 性能 | 保持在文档边界内 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_extraordinary_events_dump_interval`](ops/intervals.md#mds_extraordinary_events_dump_interval) | `0` | 性能 | 保持在文档边界内 | [Intervals](ops/intervals.md) |
| [`mds_file_blockdiff_max_concurrent_object_scans`](mds-core/mds-core.md#mds_file_blockdiff_max_concurrent_object_scans) | `16` | 性能 | 保持在文档边界内 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_forward_all_requests_to_auth`](auth-logging/auth.md#mds_forward_all_requests_to_auth) | `False` | 策略 | 符合安全与兼容性策略 | [Auth & capabilities](auth-logging/auth.md) |
| [`mds_freeze_tree_timeout`](ops/intervals.md#mds_freeze_tree_timeout) | `30` | 开发 | 生产环境保持 upstream 默认值 | [Intervals](ops/intervals.md) |
| [`mds_fscrypt_last_block_max_size`](mds-core/mds-core.md#mds_fscrypt_last_block_max_size) | `4_K` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_go_bad_corrupt_dentry`](mds-core/mds-core.md#mds_go_bad_corrupt_dentry) | `True` | 性能 | 按实测需求启用/禁用 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_hack_allow_loading_invalid_metadata`](mds-core/mds-core.md#mds_hack_allow_loading_invalid_metadata) | `False` | 策略 | 符合安全与兼容性策略 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_health_cache_threshold`](mds-core/mds-core.md#mds_health_cache_threshold) | `1.5` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_health_summarize_threshold`](mds-core/mds-core.md#mds_health_summarize_threshold) | `10` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_heartbeat_grace`](mds-core/mds-core.md#mds_heartbeat_grace) | `15` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_heartbeat_reset_grace`](mds-core/mds-core.md#mds_heartbeat_reset_grace) | `1000` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_inject_health_dummy`](ops/debug.md#mds_inject_health_dummy) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Debug](ops/debug.md) |
| [`mds_inject_journal_corrupt_dentry_first`](ops/debug.md#mds_inject_journal_corrupt_dentry_first) | `0.0` | 开发 | 生产环境保持 upstream 默认值 | [Debug](ops/debug.md) |
| [`mds_inject_migrator_session_race`](ops/debug.md#mds_inject_migrator_session_race) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Debug](ops/debug.md) |
| [`mds_inject_rename_corrupt_dentry_first`](ops/debug.md#mds_inject_rename_corrupt_dentry_first) | `0.0` | 开发 | 生产环境保持 upstream 默认值 | [Debug](ops/debug.md) |
| [`mds_inject_skip_replaying_inotable`](ops/debug.md#mds_inject_skip_replaying_inotable) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Debug](ops/debug.md) |
| [`mds_inject_traceless_reply_probability`](ops/debug.md#mds_inject_traceless_reply_probability) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Debug](ops/debug.md) |
| [`mds_join_fs`](mds-core/mds-core.md#mds_join_fs) | `(empty)` | 策略 | 符合安全与兼容性策略 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_journal_format`](mds-core/mds-core.md#mds_journal_format) | `1` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_kill_after_journal_logs_flushed`](auth-logging/logging.md#mds_kill_after_journal_logs_flushed) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Logging](auth-logging/logging.md) |
| [`mds_kill_create_at`](mds-core/mds-core.md#mds_kill_create_at) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_kill_dirfrag_at`](mds-core/mds-core.md#mds_kill_dirfrag_at) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_kill_export_at`](mds-core/mds-core.md#mds_kill_export_at) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_kill_import_at`](mds-core/mds-core.md#mds_kill_import_at) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_kill_journal_at`](mds-core/mds-core.md#mds_kill_journal_at) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_kill_journal_expire_at`](mds-core/mds-core.md#mds_kill_journal_expire_at) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_kill_journal_replay_at`](mds-core/mds-core.md#mds_kill_journal_replay_at) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_kill_link_at`](mds-core/mds-core.md#mds_kill_link_at) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_kill_mdstable_at`](mds-core/mds-core.md#mds_kill_mdstable_at) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_kill_openc_at`](mds-core/mds-core.md#mds_kill_openc_at) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_kill_rename_at`](mds-core/mds-core.md#mds_kill_rename_at) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_kill_shutdown_at`](mds-core/mds-core.md#mds_kill_shutdown_at) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_log_event_large_threshold`](auth-logging/logging.md#mds_log_event_large_threshold) | `512_K` | 性能 | 保持在文档边界内 | [Logging](auth-logging/logging.md) |
| [`mds_log_events_per_segment`](auth-logging/logging.md#mds_log_events_per_segment) | `1024` | 性能 | 保持在文档边界内 | [Logging](auth-logging/logging.md) |
| [`mds_log_max_events`](auth-logging/logging.md#mds_log_max_events) | `-1` | 性能 | 基线 → 调整 → 负载下验证 | [Logging](auth-logging/logging.md) |
| [`mds_log_max_segments`](auth-logging/logging.md#mds_log_max_segments) | `128` | 性能 | 保持在文档边界内 | [Logging](auth-logging/logging.md) |
| [`mds_log_minor_segments_per_major_segment`](auth-logging/logging.md#mds_log_minor_segments_per_major_segment) | `16` | 性能 | 保持在文档边界内 | [Logging](auth-logging/logging.md) |
| [`mds_log_pause`](auth-logging/logging.md#mds_log_pause) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Logging](auth-logging/logging.md) |
| [`mds_log_segment_size`](auth-logging/logging.md#mds_log_segment_size) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Logging](auth-logging/logging.md) |
| [`mds_log_skip_corrupt_events`](auth-logging/logging.md#mds_log_skip_corrupt_events) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Logging](auth-logging/logging.md) |
| [`mds_log_skip_unbounded_events`](auth-logging/logging.md#mds_log_skip_unbounded_events) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Logging](auth-logging/logging.md) |
| [`mds_log_trim_decay_rate`](auth-logging/logging.md#mds_log_trim_decay_rate) | `1.0` | 性能 | 保持在文档边界内 | [Logging](auth-logging/logging.md) |
| [`mds_log_trim_threshold`](auth-logging/logging.md#mds_log_trim_threshold) | `128` | 性能 | 保持在文档边界内 | [Logging](auth-logging/logging.md) |
| [`mds_log_trim_upkeep_interval`](auth-logging/logging.md#mds_log_trim_upkeep_interval) | `1000` | 性能 | 基线 → 调整 → 负载下验证 | [Logging](auth-logging/logging.md) |
| [`mds_log_warn_factor`](auth-logging/logging.md#mds_log_warn_factor) | `2` | 性能 | 保持在文档边界内 | [Logging](auth-logging/logging.md) |
| [`mds_max_caps_per_client`](auth-logging/auth.md#mds_max_caps_per_client) | `1_M` | 性能 | 基线 → 调整 → 负载下验证 | [Auth & capabilities](auth-logging/auth.md) |
| [`mds_max_completed_flushes`](mds-core/mds-core.md#mds_max_completed_flushes) | `100000` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_max_completed_requests`](mds-core/mds-core.md#mds_max_completed_requests) | `100000` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_max_export_size`](mds-core/mds-core.md#mds_max_export_size) | `20_M` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_max_file_recover`](mds-core/mds-core.md#mds_max_file_recover) | `32` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_max_purge_files`](mds-core/mds-core.md#mds_max_purge_files) | `64` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_max_purge_ops`](mds-core/mds-core.md#mds_max_purge_ops) | `8_K` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_max_purge_ops_per_pg`](mds-core/mds-core.md#mds_max_purge_ops_per_pg) | `0.5` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_max_scrub_ops_in_progress`](mds-core/mds-core.md#mds_max_scrub_ops_in_progress) | `5` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_max_snaps_per_dir`](mds-core/mds-core.md#mds_max_snaps_per_dir) | `100` | 容量 | 匹配文件系统布局与容量规划 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_metrics_update_interval`](ops/intervals.md#mds_metrics_update_interval) | `2` | 性能 | 基线 → 调整 → 负载下验证 | [Intervals](ops/intervals.md) |
| [`mds_min_caps_per_client`](auth-logging/auth.md#mds_min_caps_per_client) | `100` | 性能 | 基线 → 调整 → 负载下验证 | [Auth & capabilities](auth-logging/auth.md) |
| [`mds_min_caps_working_set`](auth-logging/auth.md#mds_min_caps_working_set) | `10000` | 性能 | 基线 → 调整 → 负载下验证 | [Auth & capabilities](auth-logging/auth.md) |
| [`mds_mon_shutdown_timeout`](ops/intervals.md#mds_mon_shutdown_timeout) | `5` | 性能 | 基线 → 调整 → 负载下验证 | [Intervals](ops/intervals.md) |
| [`mds_numa_node`](mds-core/mds-core.md#mds_numa_node) | `-1` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_oft_prefetch_dirfrags`](mds-core/mds-core.md#mds_oft_prefetch_dirfrags) | `False` | 性能 | 按实测需求启用/禁用 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_op_complaint_time`](mds-core/mds-core.md#mds_op_complaint_time) | `30` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_op_history_duration`](mds-core/mds-core.md#mds_op_history_duration) | `600` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_op_history_size`](mds-core/mds-core.md#mds_op_history_size) | `20` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_op_history_slow_op_size`](mds-core/mds-core.md#mds_op_history_slow_op_size) | `20` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_op_history_slow_op_threshold`](mds-core/mds-core.md#mds_op_history_slow_op_threshold) | `10` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_op_log_threshold`](auth-logging/logging.md#mds_op_log_threshold) | `5` | 开发 | 生产环境保持 upstream 默认值 | [Logging](auth-logging/logging.md) |
| [`mds_ping_grace`](mds-core/mds-core.md#mds_ping_grace) | `15` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_ping_interval`](ops/intervals.md#mds_ping_interval) | `5` | 性能 | 基线 → 调整 → 负载下验证 | [Intervals](ops/intervals.md) |
| [`mds_purge_queue_busy_flush_period`](mds-core/mds-core.md#mds_purge_queue_busy_flush_period) | `1` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_recall_global_max_decay_threshold`](mds-core/mds-core.md#mds_recall_global_max_decay_threshold) | `128_K` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_recall_max_caps`](auth-logging/auth.md#mds_recall_max_caps) | `30000` | 性能 | 基线 → 调整 → 负载下验证 | [Auth & capabilities](auth-logging/auth.md) |
| [`mds_recall_max_decay_rate`](mds-core/mds-core.md#mds_recall_max_decay_rate) | `1.5` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_recall_max_decay_threshold`](mds-core/mds-core.md#mds_recall_max_decay_threshold) | `128_K` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_recall_warning_decay_rate`](mds-core/mds-core.md#mds_recall_warning_decay_rate) | `60` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_recall_warning_threshold`](mds-core/mds-core.md#mds_recall_warning_threshold) | `256_K` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_reconnect_timeout`](ops/intervals.md#mds_reconnect_timeout) | `45` | 性能 | 基线 → 调整 → 负载下验证 | [Intervals](ops/intervals.md) |
| [`mds_replay_interval`](ops/intervals.md#mds_replay_interval) | `1` | 性能 | 基线 → 调整 → 负载下验证 | [Intervals](ops/intervals.md) |
| [`mds_replay_unsafe_with_closed_session`](mds-core/mds-core.md#mds_replay_unsafe_with_closed_session) | `False` | 性能 | 按实测需求启用/禁用 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_request_load_average_decay_rate`](mds-core/mds-core.md#mds_request_load_average_decay_rate) | `1_min` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_root_ino_gid`](mds-core/mds-core.md#mds_root_ino_gid) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_root_ino_uid`](mds-core/mds-core.md#mds_root_ino_uid) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_scatter_nudge_interval`](ops/intervals.md#mds_scatter_nudge_interval) | `5` | 性能 | 基线 → 调整 → 负载下验证 | [Intervals](ops/intervals.md) |
| [`mds_scrub_stats_review_period`](mds-core/mds-core.md#mds_scrub_stats_review_period) | `1` | 性能 | 保持在文档边界内 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_server_dispatch_client_request_delay`](mds-core/mds-core.md#mds_server_dispatch_client_request_delay) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_server_dispatch_killpoint_random`](mds-core/mds-core.md#mds_server_dispatch_killpoint_random) | `0.0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_session_blocklist_on_evict`](mds-core/mds-core.md#mds_session_blocklist_on_evict) | `True` | 性能 | 按实测需求启用/禁用 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_session_blocklist_on_timeout`](ops/intervals.md#mds_session_blocklist_on_timeout) | `True` | 性能 | 按实测需求启用/禁用 | [Intervals](ops/intervals.md) |
| [`mds_session_cache_liveness_decay_rate`](mds-core/mds-core.md#mds_session_cache_liveness_decay_rate) | `5_min` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_session_cache_liveness_magnitude`](mds-core/mds-core.md#mds_session_cache_liveness_magnitude) | `10` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_session_cap_acquisition_decay_rate`](auth-logging/auth.md#mds_session_cap_acquisition_decay_rate) | `30` | 性能 | 基线 → 调整 → 负载下验证 | [Auth & capabilities](auth-logging/auth.md) |
| [`mds_session_cap_acquisition_throttle`](auth-logging/auth.md#mds_session_cap_acquisition_throttle) | `100000` | 性能 | 基线 → 调整 → 负载下验证 | [Auth & capabilities](auth-logging/auth.md) |
| [`mds_session_max_caps_throttle_ratio`](auth-logging/auth.md#mds_session_max_caps_throttle_ratio) | `1.1` | 性能 | 基线 → 调整 → 负载下验证 | [Auth & capabilities](auth-logging/auth.md) |
| [`mds_session_metadata_threshold`](mds-core/mds-core.md#mds_session_metadata_threshold) | `16_M` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_sessionmap_keys_per_op`](mds-core/mds-core.md#mds_sessionmap_keys_per_op) | `1_K` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_shutdown_check`](mds-core/mds-core.md#mds_shutdown_check) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_skip_ino`](mds-core/mds-core.md#mds_skip_ino) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_sleep_rank_change`](mds-core/mds-core.md#mds_sleep_rank_change) | `0.0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_snap_max_uid`](mds-core/mds-core.md#mds_snap_max_uid) | `4294967294` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_snap_min_uid`](mds-core/mds-core.md#mds_snap_min_uid) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_snap_rstat`](mds-core/mds-core.md#mds_snap_rstat) | `False` | 性能 | 按实测需求启用/禁用 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_standby_replay_damaged`](mds-core/mds-core.md#mds_standby_replay_damaged) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_symlink_recovery`](mds-core/mds-core.md#mds_symlink_recovery) | `True` | 性能 | 按实测需求启用/禁用 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_task_status_update_interval`](ops/intervals.md#mds_task_status_update_interval) | `2` | 开发 | 生产环境保持 upstream 默认值 | [Intervals](ops/intervals.md) |
| [`mds_thrash_exports`](mds-core/mds-core.md#mds_thrash_exports) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_thrash_fragments`](mds-core/mds-core.md#mds_thrash_fragments) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_tick_interval`](ops/intervals.md#mds_tick_interval) | `5` | 性能 | 基线 → 调整 → 负载下验证 | [Intervals](ops/intervals.md) |
| [`mds_use_global_snaprealm_seq_for_subvol`](mds-core/mds-core.md#mds_use_global_snaprealm_seq_for_subvol) | `True` | 性能 | 按实测需求启用/禁用 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_valgrind_exit`](mds-core/mds-core.md#mds_valgrind_exit) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_verify_backtrace`](mds-core/mds-core.md#mds_verify_backtrace) | `1` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_verify_scatter`](mds-core/mds-core.md#mds_verify_scatter) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_wipe_ino_prealloc`](mds-core/mds-core.md#mds_wipe_ino_prealloc) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`mds_wipe_sessions`](mds-core/mds-core.md#mds_wipe_sessions) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Metadata server core](mds-core/mds-core.md) |
| [`subv_metrics_window_interval`](ops/intervals.md#subv_metrics_window_interval) | `30` | 开发 | 生产环境保持 upstream 默认值 | [Intervals](ops/intervals.md) |

[← 概览](../OVERVIEW.md)
