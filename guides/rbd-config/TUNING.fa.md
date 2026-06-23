# پیکربندی RBD — مرجع سریع تنظیم

هر **97** گزینه با مدل تنظیم و راهنمای یک‌خطی.

[← نمای کلی](../OVERVIEW.md)

| گزینه | پیش‌فرض | مدل | پاسخ سریع | موضوع |
|--------|---------|-------|--------------|-------|
| [`rbd_atime_update_interval`](misc/atime.md#rbd_atime_update_interval) | `60` | Performance | در محدوده مستند بمانید | [Atime](misc/atime.md) |
| [`rbd_auto_exclusive_lock_until_manual_request`](misc/auto.md#rbd_auto_exclusive_lock_until_manual_request) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Auto](misc/auto.md) |
| [`rbd_balance_parent_reads`](misc/balance.md#rbd_balance_parent_reads) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Balance](misc/balance.md) |
| [`rbd_balance_snap_reads`](misc/balance.md#rbd_balance_snap_reads) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Balance](misc/balance.md) |
| [`rbd_blkin_trace_all`](misc/blkin.md#rbd_blkin_trace_all) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Blkin](misc/blkin.md) |
| [`rbd_blocklist_expire_seconds`](misc/blocklist.md#rbd_blocklist_expire_seconds) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Blocklist](misc/blocklist.md) |
| [`rbd_blocklist_on_break_lock`](misc/blocklist.md#rbd_blocklist_on_break_lock) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Blocklist](misc/blocklist.md) |
| [`rbd_cache`](misc/general.md#rbd_cache) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General](misc/general.md) |
| [`rbd_cache_block_writes_upfront`](performance/cache.md#rbd_cache_block_writes_upfront) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Cache](performance/cache.md) |
| [`rbd_cache_max_dirty`](performance/cache.md#rbd_cache_max_dirty) | `24_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cache](performance/cache.md) |
| [`rbd_cache_max_dirty_age`](performance/cache.md#rbd_cache_max_dirty_age) | `1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cache](performance/cache.md) |
| [`rbd_cache_max_dirty_object`](performance/cache.md#rbd_cache_max_dirty_object) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cache](performance/cache.md) |
| [`rbd_cache_policy`](performance/cache.md#rbd_cache_policy) | `writearound` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cache](performance/cache.md) |
| [`rbd_cache_size`](performance/cache.md#rbd_cache_size) | `32_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cache](performance/cache.md) |
| [`rbd_cache_target_dirty`](performance/cache.md#rbd_cache_target_dirty) | `16_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cache](performance/cache.md) |
| [`rbd_cache_writethrough_until_flush`](performance/cache.md#rbd_cache_writethrough_until_flush) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Cache](performance/cache.md) |
| [`rbd_clone_copy_on_read`](misc/clone.md#rbd_clone_copy_on_read) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Clone](misc/clone.md) |
| [`rbd_compression_hint`](misc/compression.md#rbd_compression_hint) | `none` | Policy | مطابق سیاست امنیت و سازگاری | [Compression](misc/compression.md) |
| [`rbd_concurrent_management_ops`](misc/concurrent.md#rbd_concurrent_management_ops) | `10` | Performance | در محدوده مستند بمانید | [Concurrent](misc/concurrent.md) |
| [`rbd_config_pool_override_update_timestamp`](misc/config.md#rbd_config_pool_override_update_timestamp) | `0` | Dev | پیش‌فرض upstream در production | [Config](misc/config.md) |
| [`rbd_default_clone_format`](misc/default.md#rbd_default_clone_format) | `auto` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Defaults](misc/default.md) |
| [`rbd_default_data_pool`](misc/default.md#rbd_default_data_pool) | `(empty)` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Defaults](misc/default.md) |
| [`rbd_default_features`](misc/default.md#rbd_default_features) | `layering,exclusive-lock,object-map,fast-diff,deep-flatten` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Defaults](misc/default.md) |
| [`rbd_default_format`](misc/default.md#rbd_default_format) | `2` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Defaults](misc/default.md) |
| [`rbd_default_map_options`](misc/default.md#rbd_default_map_options) | `(empty)` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Defaults](misc/default.md) |
| [`rbd_default_order`](misc/default.md#rbd_default_order) | `22` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Defaults](misc/default.md) |
| [`rbd_default_pool`](misc/default.md#rbd_default_pool) | `rbd` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Defaults](misc/default.md) |
| [`rbd_default_snapshot_quiesce_mode`](misc/default.md#rbd_default_snapshot_quiesce_mode) | `required` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Defaults](misc/default.md) |
| [`rbd_default_stripe_count`](misc/default.md#rbd_default_stripe_count) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Defaults](misc/default.md) |
| [`rbd_default_stripe_unit`](misc/default.md#rbd_default_stripe_unit) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Defaults](misc/default.md) |
| [`rbd_disable_zero_copy_writes`](misc/disable.md#rbd_disable_zero_copy_writes) | `True` | Policy | مطابق سیاست امنیت و سازگاری | [Disable](misc/disable.md) |
| [`rbd_discard_granularity_bytes`](misc/discard.md#rbd_discard_granularity_bytes) | `64_K` | Performance | در محدوده مستند بمانید | [Discard](misc/discard.md) |
| [`rbd_discard_on_zeroed_write_same`](misc/discard.md#rbd_discard_on_zeroed_write_same) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Discard](misc/discard.md) |
| [`rbd_enable_alloc_hint`](misc/enable.md#rbd_enable_alloc_hint) | `True` | Policy | مطابق سیاست امنیت و سازگاری | [Enable](misc/enable.md) |
| [`rbd_invalidate_object_map_on_timeout`](misc/invalidate.md#rbd_invalidate_object_map_on_timeout) | `True` | Dev | پیش‌فرض upstream در production | [Invalidate](misc/invalidate.md) |
| [`rbd_io_scheduler`](performance/io.md#rbd_io_scheduler) | `simple` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Io](performance/io.md) |
| [`rbd_io_scheduler_simple_max_delay`](performance/io.md#rbd_io_scheduler_simple_max_delay) | `0` | Performance | در محدوده مستند بمانید | [Io](performance/io.md) |
| [`rbd_journal_commit_age`](mirror/journal.md#rbd_journal_commit_age) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Journal](mirror/journal.md) |
| [`rbd_journal_max_concurrent_object_sets`](mirror/journal.md#rbd_journal_max_concurrent_object_sets) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Journal](mirror/journal.md) |
| [`rbd_journal_max_payload_bytes`](mirror/journal.md#rbd_journal_max_payload_bytes) | `16_K` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Journal](mirror/journal.md) |
| [`rbd_journal_object_flush_age`](mirror/journal.md#rbd_journal_object_flush_age) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Journal](mirror/journal.md) |
| [`rbd_journal_object_flush_bytes`](mirror/journal.md#rbd_journal_object_flush_bytes) | `1_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Journal](mirror/journal.md) |
| [`rbd_journal_object_flush_interval`](mirror/journal.md#rbd_journal_object_flush_interval) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Journal](mirror/journal.md) |
| [`rbd_journal_object_max_in_flight_appends`](mirror/journal.md#rbd_journal_object_max_in_flight_appends) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Journal](mirror/journal.md) |
| [`rbd_journal_object_writethrough_until_flush`](mirror/journal.md#rbd_journal_object_writethrough_until_flush) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Journal](mirror/journal.md) |
| [`rbd_journal_order`](mirror/journal.md#rbd_journal_order) | `24` | Performance | در محدوده مستند بمانید | [Journal](mirror/journal.md) |
| [`rbd_journal_pool`](mirror/journal.md#rbd_journal_pool) | `(empty)` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Journal](mirror/journal.md) |
| [`rbd_journal_splay_width`](mirror/journal.md#rbd_journal_splay_width) | `4` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Journal](mirror/journal.md) |
| [`rbd_localize_parent_reads`](misc/localize.md#rbd_localize_parent_reads) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Localize](misc/localize.md) |
| [`rbd_localize_snap_reads`](misc/localize.md#rbd_localize_snap_reads) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Localize](misc/localize.md) |
| [`rbd_mirroring_delete_delay`](mirror/mirroring.md#rbd_mirroring_delete_delay) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Mirroring](mirror/mirroring.md) |
| [`rbd_mirroring_max_mirroring_snapshots`](mirror/mirroring.md#rbd_mirroring_max_mirroring_snapshots) | `5` | Performance | در محدوده مستند بمانید | [Mirroring](mirror/mirroring.md) |
| [`rbd_mirroring_replay_delay`](mirror/mirroring.md#rbd_mirroring_replay_delay) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Mirroring](mirror/mirroring.md) |
| [`rbd_mirroring_resync_after_disconnect`](mirror/mirroring.md#rbd_mirroring_resync_after_disconnect) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Mirroring](mirror/mirroring.md) |
| [`rbd_move_parent_to_trash_on_remove`](misc/move.md#rbd_move_parent_to_trash_on_remove) | `False` | Policy | مطابق سیاست امنیت و سازگاری | [Move](misc/move.md) |
| [`rbd_move_to_trash_on_remove`](misc/move.md#rbd_move_to_trash_on_remove) | `False` | Policy | مطابق سیاست امنیت و سازگاری | [Move](misc/move.md) |
| [`rbd_move_to_trash_on_remove_expire_seconds`](misc/move.md#rbd_move_to_trash_on_remove_expire_seconds) | `0` | Policy | مطابق سیاست امنیت و سازگاری | [Move](misc/move.md) |
| [`rbd_mtime_update_interval`](misc/mtime.md#rbd_mtime_update_interval) | `60` | Performance | در محدوده مستند بمانید | [Mtime](misc/mtime.md) |
| [`rbd_non_blocking_aio`](misc/non.md#rbd_non_blocking_aio) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Non](misc/non.md) |
| [`rbd_op_thread_timeout`](misc/op.md#rbd_op_thread_timeout) | `60` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Op](misc/op.md) |
| [`rbd_op_threads`](misc/op.md#rbd_op_threads) | `1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Op](misc/op.md) |
| [`rbd_parent_cache_enabled`](misc/parent.md#rbd_parent_cache_enabled) | `False` | Policy | مطابق سیاست امنیت و سازگاری | [Parent](misc/parent.md) |
| [`rbd_persistent_cache_mode`](misc/persistent.md#rbd_persistent_cache_mode) | `disabled` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Persistent](misc/persistent.md) |
| [`rbd_persistent_cache_path`](misc/persistent.md#rbd_persistent_cache_path) | `/tmp` | Capacity | مطابق چیدمان filesystem و برنامه ظرفیت | [Persistent](misc/persistent.md) |
| [`rbd_persistent_cache_size`](misc/persistent.md#rbd_persistent_cache_size) | `1_G` | Performance | در محدوده مستند بمانید | [Persistent](misc/persistent.md) |
| [`rbd_plugins`](misc/general.md#rbd_plugins) | `(empty)` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General](misc/general.md) |
| [`rbd_qos_bps_burst`](performance/qos.md#rbd_qos_bps_burst) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_bps_burst_seconds`](performance/qos.md#rbd_qos_bps_burst_seconds) | `1` | Performance | در محدوده مستند بمانید | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_bps_limit`](performance/qos.md#rbd_qos_bps_limit) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_exclude_ops`](performance/qos.md#rbd_qos_exclude_ops) | `(empty)` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_iops_burst`](performance/qos.md#rbd_qos_iops_burst) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_iops_burst_seconds`](performance/qos.md#rbd_qos_iops_burst_seconds) | `1` | Performance | در محدوده مستند بمانید | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_iops_limit`](performance/qos.md#rbd_qos_iops_limit) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_read_bps_burst`](performance/qos.md#rbd_qos_read_bps_burst) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_read_bps_burst_seconds`](performance/qos.md#rbd_qos_read_bps_burst_seconds) | `1` | Performance | در محدوده مستند بمانید | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_read_bps_limit`](performance/qos.md#rbd_qos_read_bps_limit) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_read_iops_burst`](performance/qos.md#rbd_qos_read_iops_burst) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_read_iops_burst_seconds`](performance/qos.md#rbd_qos_read_iops_burst_seconds) | `1` | Performance | در محدوده مستند بمانید | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_read_iops_limit`](performance/qos.md#rbd_qos_read_iops_limit) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_schedule_tick_min`](performance/qos.md#rbd_qos_schedule_tick_min) | `50` | Performance | در محدوده مستند بمانید | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_write_bps_burst`](performance/qos.md#rbd_qos_write_bps_burst) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_write_bps_burst_seconds`](performance/qos.md#rbd_qos_write_bps_burst_seconds) | `1` | Performance | در محدوده مستند بمانید | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_write_bps_limit`](performance/qos.md#rbd_qos_write_bps_limit) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_write_iops_burst`](performance/qos.md#rbd_qos_write_iops_burst) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_write_iops_burst_seconds`](performance/qos.md#rbd_qos_write_iops_burst_seconds) | `1` | Performance | در محدوده مستند بمانید | [QoS & throttling](performance/qos.md) |
| [`rbd_qos_write_iops_limit`](performance/qos.md#rbd_qos_write_iops_limit) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [QoS & throttling](performance/qos.md) |
| [`rbd_quiesce_notification_attempts`](misc/quiesce.md#rbd_quiesce_notification_attempts) | `10` | Dev | پیش‌فرض upstream در production | [Quiesce](misc/quiesce.md) |
| [`rbd_read_from_replica_policy`](misc/read.md#rbd_read_from_replica_policy) | `default` | Policy | مطابق سیاست امنیت و سازگاری | [Read](misc/read.md) |
| [`rbd_readahead_disable_after_bytes`](performance/readahead.md#rbd_readahead_disable_after_bytes) | `50_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Readahead](performance/readahead.md) |
| [`rbd_readahead_max_bytes`](performance/readahead.md#rbd_readahead_max_bytes) | `512_K` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Readahead](performance/readahead.md) |
| [`rbd_readahead_trigger_requests`](performance/readahead.md#rbd_readahead_trigger_requests) | `10` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Readahead](performance/readahead.md) |
| [`rbd_request_timed_out_seconds`](misc/request.md#rbd_request_timed_out_seconds) | `30` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Request](misc/request.md) |
| [`rbd_skip_partial_discard`](misc/skip.md#rbd_skip_partial_discard) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Skip](misc/skip.md) |
| [`rbd_sparse_read_threshold_bytes`](misc/sparse.md#rbd_sparse_read_threshold_bytes) | `64_K` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Sparse](misc/sparse.md) |
| [`rbd_tracing`](misc/general.md#rbd_tracing) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General](misc/general.md) |
| [`rbd_validate_names`](misc/validate.md#rbd_validate_names) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Validate](misc/validate.md) |
| [`rbd_validate_pool`](misc/validate.md#rbd_validate_pool) | `True` | Dev | پیش‌فرض upstream در production | [Validate](misc/validate.md) |

[← نمای کلی](../OVERVIEW.md)
