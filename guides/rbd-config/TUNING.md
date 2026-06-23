# RBD Config — Tuning Quick Reference

All **97** options with tuning model and one-line guidance.

[← Overview](OVERVIEW.md)

| Option | Default | Model | Quick answer | Topic |
|--------|---------|-------|--------------|-------|
| [`rbd_atime_update_interval`](misc/atime.md#rbd_atime_update_interval) | `60` | Performance | Stay within documented bounds | [Atime](misc/atime.md) |
| [`rbd_auto_exclusive_lock_until_manual_request`](misc/auto.md#rbd_auto_exclusive_lock_until_manual_request) | `True` | Performance | Enable/disable based on measured need | [Auto](misc/auto.md) |
| [`rbd_balance_parent_reads`](misc/balance.md#rbd_balance_parent_reads) | `False` | Performance | Enable/disable based on measured need | [Balance](misc/balance.md) |
| [`rbd_balance_snap_reads`](misc/balance.md#rbd_balance_snap_reads) | `False` | Performance | Enable/disable based on measured need | [Balance](misc/balance.md) |
| [`rbd_blkin_trace_all`](misc/blkin.md#rbd_blkin_trace_all) | `False` | Performance | Enable/disable based on measured need | [Blkin](misc/blkin.md) |
| [`rbd_blocklist_expire_seconds`](misc/blocklist.md#rbd_blocklist_expire_seconds) | `0` | Performance | Baseline → adjust → validate under load | [Blocklist](misc/blocklist.md) |
| [`rbd_blocklist_on_break_lock`](misc/blocklist.md#rbd_blocklist_on_break_lock) | `True` | Performance | Enable/disable based on measured need | [Blocklist](misc/blocklist.md) |
| [`rbd_cache`](misc/general.md#rbd_cache) | `True` | Performance | Enable/disable based on measured need | [General](misc/general.md) |
| [`rbd_cache_block_writes_upfront`](performance/cache.md#rbd_cache_block_writes_upfront) | `False` | Performance | Enable/disable based on measured need | [Cache](performance/cache.md) |
| [`rbd_cache_max_dirty`](performance/cache.md#rbd_cache_max_dirty) | `24_M` | Performance | Baseline → adjust → validate under load | [Cache](performance/cache.md) |
| [`rbd_cache_max_dirty_age`](performance/cache.md#rbd_cache_max_dirty_age) | `1` | Performance | Baseline → adjust → validate under load | [Cache](performance/cache.md) |
| [`rbd_cache_max_dirty_object`](performance/cache.md#rbd_cache_max_dirty_object) | `0` | Performance | Baseline → adjust → validate under load | [Cache](performance/cache.md) |
| [`rbd_cache_policy`](performance/cache.md#rbd_cache_policy) | `writearound` | Performance | Baseline → adjust → validate under load | [Cache](performance/cache.md) |
| [`rbd_cache_size`](performance/cache.md#rbd_cache_size) | `32_M` | Performance | Baseline → adjust → validate under load | [Cache](performance/cache.md) |
| [`rbd_cache_target_dirty`](performance/cache.md#rbd_cache_target_dirty) | `16_M` | Performance | Baseline → adjust → validate under load | [Cache](performance/cache.md) |
| [`rbd_cache_writethrough_until_flush`](performance/cache.md#rbd_cache_writethrough_until_flush) | `True` | Performance | Enable/disable based on measured need | [Cache](performance/cache.md) |
| [`rbd_clone_copy_on_read`](misc/clone.md#rbd_clone_copy_on_read) | `False` | Performance | Enable/disable based on measured need | [Clone](misc/clone.md) |
| [`rbd_compression_hint`](misc/compression.md#rbd_compression_hint) | `none` | Policy | Align with security and compatibility policy | [Compression](misc/compression.md) |
| [`rbd_concurrent_management_ops`](misc/concurrent.md#rbd_concurrent_management_ops) | `10` | Performance | Stay within documented bounds | [Concurrent](misc/concurrent.md) |
| [`rbd_config_pool_override_update_timestamp`](misc/config.md#rbd_config_pool_override_update_timestamp) | `0` | Dev | Keep upstream default in production | [Config](misc/config.md) |
| [`rbd_default_clone_format`](misc/default.md#rbd_default_clone_format) | `auto` | Performance | Baseline → adjust → validate under load | [Defaults](misc/default.md) |
| [`rbd_default_data_pool`](misc/default.md#rbd_default_data_pool) | `(empty)` | Performance | Baseline → adjust → validate under load | [Defaults](misc/default.md) |
| [`rbd_default_features`](misc/default.md#rbd_default_features) | `layering,exclusive-lock,object-map,fast-diff,deep-flatten` | Performance | Baseline → adjust → validate under load | [Defaults](misc/default.md) |
| [`rbd_default_format`](misc/default.md#rbd_default_format) | `2` | Performance | Baseline → adjust → validate under load | [Defaults](misc/default.md) |
| [`rbd_default_map_options`](misc/default.md#rbd_default_map_options) | `(empty)` | Performance | Baseline → adjust → validate under load | [Defaults](misc/default.md) |
| [`rbd_default_order`](misc/default.md#rbd_default_order) | `22` | Performance | Baseline → adjust → validate under load | [Defaults](misc/default.md) |
| [`rbd_default_pool`](misc/default.md#rbd_default_pool) | `rbd` | Performance | Baseline → adjust → validate under load | [Defaults](misc/default.md) |
| [`rbd_default_snapshot_quiesce_mode`](misc/default.md#rbd_default_snapshot_quiesce_mode) | `required` | Performance | Baseline → adjust → validate under load | [Defaults](misc/default.md) |
| [`rbd_default_stripe_count`](misc/default.md#rbd_default_stripe_count) | `0` | Performance | Baseline → adjust → validate under load | [Defaults](misc/default.md) |
| [`rbd_default_stripe_unit`](misc/default.md#rbd_default_stripe_unit) | `0` | Performance | Baseline → adjust → validate under load | [Defaults](misc/default.md) |
| [`rbd_disable_zero_copy_writes`](misc/disable.md#rbd_disable_zero_copy_writes) | `True` | Policy | Align with security and compatibility policy | [Disable](misc/disable.md) |
| [`rbd_discard_granularity_bytes`](misc/discard.md#rbd_discard_granularity_bytes) | `64_K` | Performance | Stay within documented bounds | [Discard](misc/discard.md) |
| [`rbd_discard_on_zeroed_write_same`](misc/discard.md#rbd_discard_on_zeroed_write_same) | `True` | Performance | Enable/disable based on measured need | [Discard](misc/discard.md) |
| [`rbd_enable_alloc_hint`](misc/enable.md#rbd_enable_alloc_hint) | `True` | Policy | Align with security and compatibility policy | [Enable](misc/enable.md) |
| [`rbd_invalidate_object_map_on_timeout`](misc/invalidate.md#rbd_invalidate_object_map_on_timeout) | `True` | Dev | Keep upstream default in production | [Invalidate](misc/invalidate.md) |
| [`rbd_io_scheduler`](performance/io.md#rbd_io_scheduler) | `simple` | Performance | Baseline → adjust → validate under load | [Io](performance/io.md) |
| [`rbd_io_scheduler_simple_max_delay`](performance/io.md#rbd_io_scheduler_simple_max_delay) | `0` | Performance | Stay within documented bounds | [Io](performance/io.md) |
| [`rbd_journal_commit_age`](mirror/journal.md#rbd_journal_commit_age) | `5` | Performance | Baseline → adjust → validate under load | [Journal](mirror/journal.md) |
| [`rbd_journal_max_concurrent_object_sets`](mirror/journal.md#rbd_journal_max_concurrent_object_sets) | `0` | Performance | Baseline → adjust → validate under load | [Journal](mirror/journal.md) |
| [`rbd_journal_max_payload_bytes`](mirror/journal.md#rbd_journal_max_payload_bytes) | `16_K` | Performance | Baseline → adjust → validate under load | [Journal](mirror/journal.md) |
| [`rbd_journal_object_flush_age`](mirror/journal.md#rbd_journal_object_flush_age) | `0` | Performance | Baseline → adjust → validate under load | [Journal](mirror/journal.md) |
| [`rbd_journal_object_flush_bytes`](mirror/journal.md#rbd_journal_object_flush_bytes) | `1_M` | Performance | Baseline → adjust → validate under load | [Journal](mirror/journal.md) |
| [`rbd_journal_object_flush_interval`](mirror/journal.md#rbd_journal_object_flush_interval) | `0` | Performance | Baseline → adjust → validate under load | [Journal](mirror/journal.md) |
| [`rbd_journal_object_max_in_flight_appends`](mirror/journal.md#rbd_journal_object_max_in_flight_appends) | `0` | Performance | Baseline → adjust → validate under load | [Journal](mirror/journal.md) |
| [`rbd_journal_object_writethrough_until_flush`](mirror/journal.md#rbd_journal_object_writethrough_until_flush) | `True` | Performance | Enable/disable based on measured need | [Journal](mirror/journal.md) |
| [`rbd_journal_order`](mirror/journal.md#rbd_journal_order) | `24` | Performance | Stay within documented bounds | [Journal](mirror/journal.md) |
| [`rbd_journal_pool`](mirror/journal.md#rbd_journal_pool) | `(empty)` | Performance | Baseline → adjust → validate under load | [Journal](mirror/journal.md) |
| [`rbd_journal_splay_width`](mirror/journal.md#rbd_journal_splay_width) | `4` | Performance | Baseline → adjust → validate under load | [Journal](mirror/journal.md) |
| [`rbd_localize_parent_reads`](misc/localize.md#rbd_localize_parent_reads) | `False` | Performance | Enable/disable based on measured need | [Localize](misc/localize.md) |
| [`rbd_localize_snap_reads`](misc/localize.md#rbd_localize_snap_reads) | `False` | Performance | Enable/disable based on measured need | [Localize](misc/localize.md) |
| [`rbd_mirroring_delete_delay`](mirror/mirroring.md#rbd_mirroring_delete_delay) | `0` | Performance | Baseline → adjust → validate under load | [Mirroring](mirror/mirroring.md) |
| [`rbd_mirroring_max_mirroring_snapshots`](mirror/mirroring.md#rbd_mirroring_max_mirroring_snapshots) | `5` | Performance | Stay within documented bounds | [Mirroring](mirror/mirroring.md) |
| [`rbd_mirroring_replay_delay`](mirror/mirroring.md#rbd_mirroring_replay_delay) | `0` | Performance | Baseline → adjust → validate under load | [Mirroring](mirror/mirroring.md) |
| [`rbd_mirroring_resync_after_disconnect`](mirror/mirroring.md#rbd_mirroring_resync_after_disconnect) | `False` | Performance | Enable/disable based on measured need | [Mirroring](mirror/mirroring.md) |
| [`rbd_move_parent_to_trash_on_remove`](misc/move.md#rbd_move_parent_to_trash_on_remove) | `False` | Policy | Align with security and compatibility policy | [Move](misc/move.md) |
| [`rbd_move_to_trash_on_remove`](misc/move.md#rbd_move_to_trash_on_remove) | `False` | Policy | Align with security and compatibility policy | [Move](misc/move.md) |
| [`rbd_move_to_trash_on_remove_expire_seconds`](misc/move.md#rbd_move_to_trash_on_remove_expire_seconds) | `0` | Policy | Align with security and compatibility policy | [Move](misc/move.md) |
| [`rbd_mtime_update_interval`](misc/mtime.md#rbd_mtime_update_interval) | `60` | Performance | Stay within documented bounds | [Mtime](misc/mtime.md) |
| [`rbd_non_blocking_aio`](misc/non.md#rbd_non_blocking_aio) | `True` | Performance | Enable/disable based on measured need | [Non](misc/non.md) |
| [`rbd_op_thread_timeout`](misc/op.md#rbd_op_thread_timeout) | `60` | Performance | Baseline → adjust → validate under load | [Op](misc/op.md) |
| [`rbd_op_threads`](misc/op.md#rbd_op_threads) | `1` | Performance | Baseline → adjust → validate under load | [Op](misc/op.md) |
| [`rbd_parent_cache_enabled`](misc/parent.md#rbd_parent_cache_enabled) | `False` | Policy | Align with security and compatibility policy | [Parent](misc/parent.md) |
| [`rbd_persistent_cache_mode`](misc/persistent.md#rbd_persistent_cache_mode) | `disabled` | Performance | Baseline → adjust → validate under load | [Persistent](misc/persistent.md) |
| [`rbd_persistent_cache_path`](misc/persistent.md#rbd_persistent_cache_path) | `/tmp` | Capacity | Match filesystem layout and capacity plan | [Persistent](misc/persistent.md) |
| [`rbd_persistent_cache_size`](misc/persistent.md#rbd_persistent_cache_size) | `1_G` | Performance | Stay within documented bounds | [Persistent](misc/persistent.md) |
| [`rbd_plugins`](misc/general.md#rbd_plugins) | `(empty)` | Performance | Baseline → adjust → validate under load | [General](misc/general.md) |
| [`rbd_qos_bps_burst`](performance/qos.md#rbd_qos_bps_burst) | `0` | Performance | Baseline → adjust → validate under load | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_bps_burst_seconds`](performance/qos.md#rbd_qos_bps_burst_seconds) | `1` | Performance | Stay within documented bounds | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_bps_limit`](performance/qos.md#rbd_qos_bps_limit) | `0` | Performance | Baseline → adjust → validate under load | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_exclude_ops`](performance/qos.md#rbd_qos_exclude_ops) | `(empty)` | Performance | Baseline → adjust → validate under load | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_iops_burst`](performance/qos.md#rbd_qos_iops_burst) | `0` | Performance | Baseline → adjust → validate under load | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_iops_burst_seconds`](performance/qos.md#rbd_qos_iops_burst_seconds) | `1` | Performance | Stay within documented bounds | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_iops_limit`](performance/qos.md#rbd_qos_iops_limit) | `0` | Performance | Baseline → adjust → validate under load | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_read_bps_burst`](performance/qos.md#rbd_qos_read_bps_burst) | `0` | Performance | Baseline → adjust → validate under load | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_read_bps_burst_seconds`](performance/qos.md#rbd_qos_read_bps_burst_seconds) | `1` | Performance | Stay within documented bounds | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_read_bps_limit`](performance/qos.md#rbd_qos_read_bps_limit) | `0` | Performance | Baseline → adjust → validate under load | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_read_iops_burst`](performance/qos.md#rbd_qos_read_iops_burst) | `0` | Performance | Baseline → adjust → validate under load | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_read_iops_burst_seconds`](performance/qos.md#rbd_qos_read_iops_burst_seconds) | `1` | Performance | Stay within documented bounds | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_read_iops_limit`](performance/qos.md#rbd_qos_read_iops_limit) | `0` | Performance | Baseline → adjust → validate under load | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_schedule_tick_min`](performance/qos.md#rbd_qos_schedule_tick_min) | `50` | Performance | Stay within documented bounds | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_write_bps_burst`](performance/qos.md#rbd_qos_write_bps_burst) | `0` | Performance | Baseline → adjust → validate under load | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_write_bps_burst_seconds`](performance/qos.md#rbd_qos_write_bps_burst_seconds) | `1` | Performance | Stay within documented bounds | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_write_bps_limit`](performance/qos.md#rbd_qos_write_bps_limit) | `0` | Performance | Baseline → adjust → validate under load | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_write_iops_burst`](performance/qos.md#rbd_qos_write_iops_burst) | `0` | Performance | Baseline → adjust → validate under load | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_write_iops_burst_seconds`](performance/qos.md#rbd_qos_write_iops_burst_seconds) | `1` | Performance | Stay within documented bounds | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_write_iops_limit`](performance/qos.md#rbd_qos_write_iops_limit) | `0` | Performance | Baseline → adjust → validate under load | [QoS & throttling](performance/qos.md) |
| [`rbd_quiesce_notification_attempts`](misc/quiesce.md#rbd_quiesce_notification_attempts) | `10` | Dev | Keep upstream default in production | [Quiesce](misc/quiesce.md) |
| [`rbd_read_from_replica_policy`](misc/read.md#rbd_read_from_replica_policy) | `default` | Policy | Align with security and compatibility policy | [Read](misc/read.md) |
| [`rbd_readahead_disable_after_bytes`](performance/readahead.md#rbd_readahead_disable_after_bytes) | `50_M` | Performance | Baseline → adjust → validate under load | [Readahead](performance/readahead.md) |
| [`rbd_readahead_max_bytes`](performance/readahead.md#rbd_readahead_max_bytes) | `512_K` | Performance | Baseline → adjust → validate under load | [Readahead](performance/readahead.md) |
| [`rbd_readahead_trigger_requests`](performance/readahead.md#rbd_readahead_trigger_requests) | `10` | Performance | Baseline → adjust → validate under load | [Readahead](performance/readahead.md) |
| [`rbd_request_timed_out_seconds`](misc/request.md#rbd_request_timed_out_seconds) | `30` | Performance | Baseline → adjust → validate under load | [Request](misc/request.md) |
| [`rbd_skip_partial_discard`](misc/skip.md#rbd_skip_partial_discard) | `True` | Performance | Enable/disable based on measured need | [Skip](misc/skip.md) |
| [`rbd_sparse_read_threshold_bytes`](misc/sparse.md#rbd_sparse_read_threshold_bytes) | `64_K` | Performance | Baseline → adjust → validate under load | [Sparse](misc/sparse.md) |
| [`rbd_tracing`](misc/general.md#rbd_tracing) | `False` | Performance | Enable/disable based on measured need | [General](misc/general.md) |
| [`rbd_validate_names`](misc/validate.md#rbd_validate_names) | `True` | Performance | Enable/disable based on measured need | [Validate](misc/validate.md) |
| [`rbd_validate_pool`](misc/validate.md#rbd_validate_pool) | `True` | Dev | Keep upstream default in production | [Validate](misc/validate.md) |

[← Overview](OVERVIEW.md)
