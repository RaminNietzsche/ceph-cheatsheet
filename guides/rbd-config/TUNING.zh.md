# RBD 配置 — 调优快速参考

全部 **97** 个选项的调优模型与一行建议。

[← 概览](../OVERVIEW.md)

| 选项 | 默认值 | 模型 | 快速建议 | 主题 |
|--------|---------|-------|--------------|-------|
| [`rbd_atime_update_interval`](misc/atime.md#rbd_atime_update_interval) | `60` | 性能 | 保持在文档边界内 | [Atime](misc/atime.md) |
| [`rbd_auto_exclusive_lock_until_manual_request`](misc/auto.md#rbd_auto_exclusive_lock_until_manual_request) | `True` | 性能 | 按实测需求启用/禁用 | [Auto](misc/auto.md) |
| [`rbd_balance_parent_reads`](misc/balance.md#rbd_balance_parent_reads) | `False` | 性能 | 按实测需求启用/禁用 | [Balance](misc/balance.md) |
| [`rbd_balance_snap_reads`](misc/balance.md#rbd_balance_snap_reads) | `False` | 性能 | 按实测需求启用/禁用 | [Balance](misc/balance.md) |
| [`rbd_blkin_trace_all`](misc/blkin.md#rbd_blkin_trace_all) | `False` | 性能 | 按实测需求启用/禁用 | [Blkin](misc/blkin.md) |
| [`rbd_blocklist_expire_seconds`](misc/blocklist.md#rbd_blocklist_expire_seconds) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Blocklist](misc/blocklist.md) |
| [`rbd_blocklist_on_break_lock`](misc/blocklist.md#rbd_blocklist_on_break_lock) | `True` | 性能 | 按实测需求启用/禁用 | [Blocklist](misc/blocklist.md) |
| [`rbd_cache`](misc/general.md#rbd_cache) | `True` | 性能 | 按实测需求启用/禁用 | [General](misc/general.md) |
| [`rbd_cache_block_writes_upfront`](performance/cache.md#rbd_cache_block_writes_upfront) | `False` | 性能 | 按实测需求启用/禁用 | [Cache](performance/cache.md) |
| [`rbd_cache_max_dirty`](performance/cache.md#rbd_cache_max_dirty) | `24_M` | 性能 | 基线 → 调整 → 负载下验证 | [Cache](performance/cache.md) |
| [`rbd_cache_max_dirty_age`](performance/cache.md#rbd_cache_max_dirty_age) | `1` | 性能 | 基线 → 调整 → 负载下验证 | [Cache](performance/cache.md) |
| [`rbd_cache_max_dirty_object`](performance/cache.md#rbd_cache_max_dirty_object) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Cache](performance/cache.md) |
| [`rbd_cache_policy`](performance/cache.md#rbd_cache_policy) | `writearound` | 性能 | 基线 → 调整 → 负载下验证 | [Cache](performance/cache.md) |
| [`rbd_cache_size`](performance/cache.md#rbd_cache_size) | `32_M` | 性能 | 基线 → 调整 → 负载下验证 | [Cache](performance/cache.md) |
| [`rbd_cache_target_dirty`](performance/cache.md#rbd_cache_target_dirty) | `16_M` | 性能 | 基线 → 调整 → 负载下验证 | [Cache](performance/cache.md) |
| [`rbd_cache_writethrough_until_flush`](performance/cache.md#rbd_cache_writethrough_until_flush) | `True` | 性能 | 按实测需求启用/禁用 | [Cache](performance/cache.md) |
| [`rbd_clone_copy_on_read`](misc/clone.md#rbd_clone_copy_on_read) | `False` | 性能 | 按实测需求启用/禁用 | [Clone](misc/clone.md) |
| [`rbd_compression_hint`](misc/compression.md#rbd_compression_hint) | `none` | 策略 | 符合安全与兼容性策略 | [Compression](misc/compression.md) |
| [`rbd_concurrent_management_ops`](misc/concurrent.md#rbd_concurrent_management_ops) | `10` | 性能 | 保持在文档边界内 | [Concurrent](misc/concurrent.md) |
| [`rbd_config_pool_override_update_timestamp`](misc/config.md#rbd_config_pool_override_update_timestamp) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Config](misc/config.md) |
| [`rbd_default_clone_format`](misc/default.md#rbd_default_clone_format) | `auto` | 性能 | 基线 → 调整 → 负载下验证 | [Defaults](misc/default.md) |
| [`rbd_default_data_pool`](misc/default.md#rbd_default_data_pool) | `(empty)` | 性能 | 基线 → 调整 → 负载下验证 | [Defaults](misc/default.md) |
| [`rbd_default_features`](misc/default.md#rbd_default_features) | `layering,exclusive-lock,object-map,fast-diff,deep-flatten` | 性能 | 基线 → 调整 → 负载下验证 | [Defaults](misc/default.md) |
| [`rbd_default_format`](misc/default.md#rbd_default_format) | `2` | 性能 | 基线 → 调整 → 负载下验证 | [Defaults](misc/default.md) |
| [`rbd_default_map_options`](misc/default.md#rbd_default_map_options) | `(empty)` | 性能 | 基线 → 调整 → 负载下验证 | [Defaults](misc/default.md) |
| [`rbd_default_order`](misc/default.md#rbd_default_order) | `22` | 性能 | 基线 → 调整 → 负载下验证 | [Defaults](misc/default.md) |
| [`rbd_default_pool`](misc/default.md#rbd_default_pool) | `rbd` | 性能 | 基线 → 调整 → 负载下验证 | [Defaults](misc/default.md) |
| [`rbd_default_snapshot_quiesce_mode`](misc/default.md#rbd_default_snapshot_quiesce_mode) | `required` | 性能 | 基线 → 调整 → 负载下验证 | [Defaults](misc/default.md) |
| [`rbd_default_stripe_count`](misc/default.md#rbd_default_stripe_count) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Defaults](misc/default.md) |
| [`rbd_default_stripe_unit`](misc/default.md#rbd_default_stripe_unit) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Defaults](misc/default.md) |
| [`rbd_disable_zero_copy_writes`](misc/disable.md#rbd_disable_zero_copy_writes) | `True` | 策略 | 符合安全与兼容性策略 | [Disable](misc/disable.md) |
| [`rbd_discard_granularity_bytes`](misc/discard.md#rbd_discard_granularity_bytes) | `64_K` | 性能 | 保持在文档边界内 | [Discard](misc/discard.md) |
| [`rbd_discard_on_zeroed_write_same`](misc/discard.md#rbd_discard_on_zeroed_write_same) | `True` | 性能 | 按实测需求启用/禁用 | [Discard](misc/discard.md) |
| [`rbd_enable_alloc_hint`](misc/enable.md#rbd_enable_alloc_hint) | `True` | 策略 | 符合安全与兼容性策略 | [Enable](misc/enable.md) |
| [`rbd_invalidate_object_map_on_timeout`](misc/invalidate.md#rbd_invalidate_object_map_on_timeout) | `True` | 开发 | 生产环境保持 upstream 默认值 | [Invalidate](misc/invalidate.md) |
| [`rbd_io_scheduler`](performance/io.md#rbd_io_scheduler) | `simple` | 性能 | 基线 → 调整 → 负载下验证 | [Io](performance/io.md) |
| [`rbd_io_scheduler_simple_max_delay`](performance/io.md#rbd_io_scheduler_simple_max_delay) | `0` | 性能 | 保持在文档边界内 | [Io](performance/io.md) |
| [`rbd_journal_commit_age`](mirror/journal.md#rbd_journal_commit_age) | `5` | 性能 | 基线 → 调整 → 负载下验证 | [Journal](mirror/journal.md) |
| [`rbd_journal_max_concurrent_object_sets`](mirror/journal.md#rbd_journal_max_concurrent_object_sets) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Journal](mirror/journal.md) |
| [`rbd_journal_max_payload_bytes`](mirror/journal.md#rbd_journal_max_payload_bytes) | `16_K` | 性能 | 基线 → 调整 → 负载下验证 | [Journal](mirror/journal.md) |
| [`rbd_journal_object_flush_age`](mirror/journal.md#rbd_journal_object_flush_age) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Journal](mirror/journal.md) |
| [`rbd_journal_object_flush_bytes`](mirror/journal.md#rbd_journal_object_flush_bytes) | `1_M` | 性能 | 基线 → 调整 → 负载下验证 | [Journal](mirror/journal.md) |
| [`rbd_journal_object_flush_interval`](mirror/journal.md#rbd_journal_object_flush_interval) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Journal](mirror/journal.md) |
| [`rbd_journal_object_max_in_flight_appends`](mirror/journal.md#rbd_journal_object_max_in_flight_appends) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Journal](mirror/journal.md) |
| [`rbd_journal_object_writethrough_until_flush`](mirror/journal.md#rbd_journal_object_writethrough_until_flush) | `True` | 性能 | 按实测需求启用/禁用 | [Journal](mirror/journal.md) |
| [`rbd_journal_order`](mirror/journal.md#rbd_journal_order) | `24` | 性能 | 保持在文档边界内 | [Journal](mirror/journal.md) |
| [`rbd_journal_pool`](mirror/journal.md#rbd_journal_pool) | `(empty)` | 性能 | 基线 → 调整 → 负载下验证 | [Journal](mirror/journal.md) |
| [`rbd_journal_splay_width`](mirror/journal.md#rbd_journal_splay_width) | `4` | 性能 | 基线 → 调整 → 负载下验证 | [Journal](mirror/journal.md) |
| [`rbd_localize_parent_reads`](misc/localize.md#rbd_localize_parent_reads) | `False` | 性能 | 按实测需求启用/禁用 | [Localize](misc/localize.md) |
| [`rbd_localize_snap_reads`](misc/localize.md#rbd_localize_snap_reads) | `False` | 性能 | 按实测需求启用/禁用 | [Localize](misc/localize.md) |
| [`rbd_mirroring_delete_delay`](mirror/mirroring.md#rbd_mirroring_delete_delay) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Mirroring](mirror/mirroring.md) |
| [`rbd_mirroring_max_mirroring_snapshots`](mirror/mirroring.md#rbd_mirroring_max_mirroring_snapshots) | `5` | 性能 | 保持在文档边界内 | [Mirroring](mirror/mirroring.md) |
| [`rbd_mirroring_replay_delay`](mirror/mirroring.md#rbd_mirroring_replay_delay) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Mirroring](mirror/mirroring.md) |
| [`rbd_mirroring_resync_after_disconnect`](mirror/mirroring.md#rbd_mirroring_resync_after_disconnect) | `False` | 性能 | 按实测需求启用/禁用 | [Mirroring](mirror/mirroring.md) |
| [`rbd_move_parent_to_trash_on_remove`](misc/move.md#rbd_move_parent_to_trash_on_remove) | `False` | 策略 | 符合安全与兼容性策略 | [Move](misc/move.md) |
| [`rbd_move_to_trash_on_remove`](misc/move.md#rbd_move_to_trash_on_remove) | `False` | 策略 | 符合安全与兼容性策略 | [Move](misc/move.md) |
| [`rbd_move_to_trash_on_remove_expire_seconds`](misc/move.md#rbd_move_to_trash_on_remove_expire_seconds) | `0` | 策略 | 符合安全与兼容性策略 | [Move](misc/move.md) |
| [`rbd_mtime_update_interval`](misc/mtime.md#rbd_mtime_update_interval) | `60` | 性能 | 保持在文档边界内 | [Mtime](misc/mtime.md) |
| [`rbd_non_blocking_aio`](misc/non.md#rbd_non_blocking_aio) | `True` | 性能 | 按实测需求启用/禁用 | [Non](misc/non.md) |
| [`rbd_op_thread_timeout`](misc/op.md#rbd_op_thread_timeout) | `60` | 性能 | 基线 → 调整 → 负载下验证 | [Op](misc/op.md) |
| [`rbd_op_threads`](misc/op.md#rbd_op_threads) | `1` | 性能 | 基线 → 调整 → 负载下验证 | [Op](misc/op.md) |
| [`rbd_parent_cache_enabled`](misc/parent.md#rbd_parent_cache_enabled) | `False` | 策略 | 符合安全与兼容性策略 | [Parent](misc/parent.md) |
| [`rbd_persistent_cache_mode`](misc/persistent.md#rbd_persistent_cache_mode) | `disabled` | 性能 | 基线 → 调整 → 负载下验证 | [Persistent](misc/persistent.md) |
| [`rbd_persistent_cache_path`](misc/persistent.md#rbd_persistent_cache_path) | `/tmp` | 容量 | 匹配文件系统布局与容量规划 | [Persistent](misc/persistent.md) |
| [`rbd_persistent_cache_size`](misc/persistent.md#rbd_persistent_cache_size) | `1_G` | 性能 | 保持在文档边界内 | [Persistent](misc/persistent.md) |
| [`rbd_plugins`](misc/general.md#rbd_plugins) | `(empty)` | 性能 | 基线 → 调整 → 负载下验证 | [General](misc/general.md) |
| [`rbd_qos_bps_burst`](performance/qos.md#rbd_qos_bps_burst) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_bps_burst_seconds`](performance/qos.md#rbd_qos_bps_burst_seconds) | `1` | 性能 | 保持在文档边界内 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_bps_limit`](performance/qos.md#rbd_qos_bps_limit) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_exclude_ops`](performance/qos.md#rbd_qos_exclude_ops) | `(empty)` | 性能 | 基线 → 调整 → 负载下验证 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_iops_burst`](performance/qos.md#rbd_qos_iops_burst) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_iops_burst_seconds`](performance/qos.md#rbd_qos_iops_burst_seconds) | `1` | 性能 | 保持在文档边界内 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_iops_limit`](performance/qos.md#rbd_qos_iops_limit) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_read_bps_burst`](performance/qos.md#rbd_qos_read_bps_burst) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_read_bps_burst_seconds`](performance/qos.md#rbd_qos_read_bps_burst_seconds) | `1` | 性能 | 保持在文档边界内 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_read_bps_limit`](performance/qos.md#rbd_qos_read_bps_limit) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_read_iops_burst`](performance/qos.md#rbd_qos_read_iops_burst) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_read_iops_burst_seconds`](performance/qos.md#rbd_qos_read_iops_burst_seconds) | `1` | 性能 | 保持在文档边界内 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_read_iops_limit`](performance/qos.md#rbd_qos_read_iops_limit) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_schedule_tick_min`](performance/qos.md#rbd_qos_schedule_tick_min) | `50` | 性能 | 保持在文档边界内 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_write_bps_burst`](performance/qos.md#rbd_qos_write_bps_burst) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_write_bps_burst_seconds`](performance/qos.md#rbd_qos_write_bps_burst_seconds) | `1` | 性能 | 保持在文档边界内 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_write_bps_limit`](performance/qos.md#rbd_qos_write_bps_limit) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_write_iops_burst`](performance/qos.md#rbd_qos_write_iops_burst) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_write_iops_burst_seconds`](performance/qos.md#rbd_qos_write_iops_burst_seconds) | `1` | 性能 | 保持在文档边界内 | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_write_iops_limit`](performance/qos.md#rbd_qos_write_iops_limit) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [QoS & throttling](performance/qos.md) |
| [`rbd_quiesce_notification_attempts`](misc/quiesce.md#rbd_quiesce_notification_attempts) | `10` | 开发 | 生产环境保持 upstream 默认值 | [Quiesce](misc/quiesce.md) |
| [`rbd_read_from_replica_policy`](misc/read.md#rbd_read_from_replica_policy) | `default` | 策略 | 符合安全与兼容性策略 | [Read](misc/read.md) |
| [`rbd_readahead_disable_after_bytes`](performance/readahead.md#rbd_readahead_disable_after_bytes) | `50_M` | 性能 | 基线 → 调整 → 负载下验证 | [Readahead](performance/readahead.md) |
| [`rbd_readahead_max_bytes`](performance/readahead.md#rbd_readahead_max_bytes) | `512_K` | 性能 | 基线 → 调整 → 负载下验证 | [Readahead](performance/readahead.md) |
| [`rbd_readahead_trigger_requests`](performance/readahead.md#rbd_readahead_trigger_requests) | `10` | 性能 | 基线 → 调整 → 负载下验证 | [Readahead](performance/readahead.md) |
| [`rbd_request_timed_out_seconds`](misc/request.md#rbd_request_timed_out_seconds) | `30` | 性能 | 基线 → 调整 → 负载下验证 | [Request](misc/request.md) |
| [`rbd_skip_partial_discard`](misc/skip.md#rbd_skip_partial_discard) | `True` | 性能 | 按实测需求启用/禁用 | [Skip](misc/skip.md) |
| [`rbd_sparse_read_threshold_bytes`](misc/sparse.md#rbd_sparse_read_threshold_bytes) | `64_K` | 性能 | 基线 → 调整 → 负载下验证 | [Sparse](misc/sparse.md) |
| [`rbd_tracing`](misc/general.md#rbd_tracing) | `False` | 性能 | 按实测需求启用/禁用 | [General](misc/general.md) |
| [`rbd_validate_names`](misc/validate.md#rbd_validate_names) | `True` | 性能 | 按实测需求启用/禁用 | [Validate](misc/validate.md) |
| [`rbd_validate_pool`](misc/validate.md#rbd_validate_pool) | `True` | 开发 | 生产环境保持 upstream 默认值 | [Validate](misc/validate.md) |

[← 概览](../OVERVIEW.md)
