# Global Config — Tuning Quick Reference

All **852** options with tuning model and one-line guidance.

[← Overview](../OVERVIEW.md)

| Option | Default | Model | Quick answer | Topic |
|--------|---------|-------|--------------|-------|
| [`admin_socket`](runtime/admin.md#admin_socket) | `$run_dir/$cluster-$name.asok` | Performance | Baseline → adjust → validate under load | [Admin](runtime/admin.md) |
| [`admin_socket_mode`](runtime/admin.md#admin_socket_mode) | `(empty)` | Performance | Baseline → adjust → validate under load | [Admin](runtime/admin.md) |
| [`auth_allow_insecure_global_id_reclaim`](auth/auth.md#auth_allow_insecure_global_id_reclaim) | `True` | Policy | Align with security and compatibility policy | [Auth](auth/auth.md) |
| [`auth_client_required`](auth/auth.md#auth_client_required) | `cephx, none` | Performance | Baseline → adjust → validate under load | [Auth](auth/auth.md) |
| [`auth_cluster_required`](auth/auth.md#auth_cluster_required) | `cephx` | Performance | Baseline → adjust → validate under load | [Auth](auth/auth.md) |
| [`auth_debug`](auth/auth.md#auth_debug) | `False` | Dev | Keep upstream default in production | [Auth](auth/auth.md) |
| [`auth_expose_insecure_global_id_reclaim`](auth/auth.md#auth_expose_insecure_global_id_reclaim) | `True` | Policy | Align with security and compatibility policy | [Auth](auth/auth.md) |
| [`auth_mon_ticket_ttl`](auth/auth.md#auth_mon_ticket_ttl) | `72_hr` | Performance | Baseline → adjust → validate under load | [Auth](auth/auth.md) |
| [`auth_service_required`](auth/auth.md#auth_service_required) | `cephx` | Performance | Baseline → adjust → validate under load | [Auth](auth/auth.md) |
| [`auth_service_ticket_ttl`](auth/auth.md#auth_service_ticket_ttl) | `1_hr` | Performance | Baseline → adjust → validate under load | [Auth](auth/auth.md) |
| [`auth_supported`](auth/auth.md#auth_supported) | `(empty)` | Performance | Baseline → adjust → validate under load | [Auth](auth/auth.md) |
| [`bdev_aio`](storage/bdev.md#bdev_aio) | `True` | Performance | Enable/disable based on measured need | [Bdev](storage/bdev.md) |
| [`bdev_aio_max_queue_depth`](storage/bdev.md#bdev_aio_max_queue_depth) | `1024` | Performance | Baseline → adjust → validate under load | [Bdev](storage/bdev.md) |
| [`bdev_aio_poll_ms`](storage/bdev.md#bdev_aio_poll_ms) | `250` | Performance | Baseline → adjust → validate under load | [Bdev](storage/bdev.md) |
| [`bdev_aio_reap_max`](storage/bdev.md#bdev_aio_reap_max) | `16` | Performance | Baseline → adjust → validate under load | [Bdev](storage/bdev.md) |
| [`bdev_aio_submit_retry_initial_delay_us`](storage/bdev.md#bdev_aio_submit_retry_initial_delay_us) | `125` | Performance | Baseline → adjust → validate under load | [Bdev](storage/bdev.md) |
| [`bdev_aio_submit_retry_max`](storage/bdev.md#bdev_aio_submit_retry_max) | `16` | Performance | Baseline → adjust → validate under load | [Bdev](storage/bdev.md) |
| [`bdev_async_discard`](storage/bdev.md#bdev_async_discard) | `False` | Performance | Enable/disable based on measured need | [Bdev](storage/bdev.md) |
| [`bdev_async_discard_max_pending`](storage/bdev.md#bdev_async_discard_max_pending) | `1000000` | Performance | Stay within documented bounds | [Bdev](storage/bdev.md) |
| [`bdev_async_discard_threads`](storage/bdev.md#bdev_async_discard_threads) | `0` | Performance | Stay within documented bounds | [Bdev](storage/bdev.md) |
| [`bdev_block_size`](storage/bdev.md#bdev_block_size) | `4_K` | Performance | Baseline → adjust → validate under load | [Bdev](storage/bdev.md) |
| [`bdev_debug_aio`](storage/bdev.md#bdev_debug_aio) | `False` | Dev | Keep upstream default in production | [Bdev](storage/bdev.md) |
| [`bdev_debug_aio_log_age`](storage/bdev.md#bdev_debug_aio_log_age) | `5` | Dev | Keep upstream default in production | [Bdev](storage/bdev.md) |
| [`bdev_debug_aio_suicide_timeout`](storage/bdev.md#bdev_debug_aio_suicide_timeout) | `1_min` | Dev | Keep upstream default in production | [Bdev](storage/bdev.md) |
| [`bdev_debug_discard_sleep`](storage/bdev.md#bdev_debug_discard_sleep) | `0` | Dev | Keep upstream default in production | [Bdev](storage/bdev.md) |
| [`bdev_debug_inflight_ios`](storage/bdev.md#bdev_debug_inflight_ios) | `False` | Dev | Keep upstream default in production | [Bdev](storage/bdev.md) |
| [`bdev_discard_max_bytes`](storage/bdev.md#bdev_discard_max_bytes) | `10_G` | Performance | Baseline → adjust → validate under load | [Bdev](storage/bdev.md) |
| [`bdev_enable_discard`](storage/bdev.md#bdev_enable_discard) | `False` | Policy | Align with security and compatibility policy | [Bdev](storage/bdev.md) |
| [`bdev_flock_retry`](storage/bdev.md#bdev_flock_retry) | `3` | Performance | Baseline → adjust → validate under load | [Bdev](storage/bdev.md) |
| [`bdev_flock_retry_interval`](storage/bdev.md#bdev_flock_retry_interval) | `0.1` | Performance | Baseline → adjust → validate under load | [Bdev](storage/bdev.md) |
| [`bdev_inject_crash`](storage/bdev.md#bdev_inject_crash) | `0` | Dev | Keep upstream default in production | [Bdev](storage/bdev.md) |
| [`bdev_inject_crash_flush_delay`](storage/bdev.md#bdev_inject_crash_flush_delay) | `2` | Dev | Keep upstream default in production | [Bdev](storage/bdev.md) |
| [`bdev_ioring`](storage/bdev.md#bdev_ioring) | `False` | Performance | Enable/disable based on measured need | [Bdev](storage/bdev.md) |
| [`bdev_ioring_hipri`](storage/bdev.md#bdev_ioring_hipri) | `False` | Performance | Enable/disable based on measured need | [Bdev](storage/bdev.md) |
| [`bdev_ioring_sqthread_poll`](storage/bdev.md#bdev_ioring_sqthread_poll) | `False` | Performance | Enable/disable based on measured need | [Bdev](storage/bdev.md) |
| [`bdev_max_discard_length`](storage/bdev.md#bdev_max_discard_length) | `2147483648` | Performance | Baseline → adjust → validate under load | [Bdev](storage/bdev.md) |
| [`bdev_nvme_unbind_from_kernel`](storage/bdev.md#bdev_nvme_unbind_from_kernel) | `False` | Performance | Enable/disable based on measured need | [Bdev](storage/bdev.md) |
| [`bdev_read_buffer_alignment`](storage/bdev.md#bdev_read_buffer_alignment) | `4_K` | Performance | Baseline → adjust → validate under load | [Bdev](storage/bdev.md) |
| [`bdev_read_preallocated_huge_buffers`](storage/bdev.md#bdev_read_preallocated_huge_buffers) | `(empty)` | Performance | Baseline → adjust → validate under load | [Bdev](storage/bdev.md) |
| [`bdev_stalled_read_warn_lifetime`](storage/bdev.md#bdev_stalled_read_warn_lifetime) | `86400` | Performance | Baseline → adjust → validate under load | [Bdev](storage/bdev.md) |
| [`bdev_stalled_read_warn_threshold`](storage/bdev.md#bdev_stalled_read_warn_threshold) | `1` | Performance | Baseline → adjust → validate under load | [Bdev](storage/bdev.md) |
| [`bdev_type`](storage/bdev.md#bdev_type) | `(empty)` | Performance | Baseline → adjust → validate under load | [Bdev](storage/bdev.md) |
| [`bluefs_alloc_size`](storage/bluefs.md#bluefs_alloc_size) | `1_M` | Performance | Baseline → adjust → validate under load | [Bluefs](storage/bluefs.md) |
| [`bluefs_allocator`](storage/bluefs.md#bluefs_allocator) | `hybrid` | Dev | Keep upstream default in production | [Bluefs](storage/bluefs.md) |
| [`bluefs_buffered_io`](storage/bluefs.md#bluefs_buffered_io) | `True` | Performance | Enable/disable based on measured need | [Bluefs](storage/bluefs.md) |
| [`bluefs_check_for_zeros`](storage/bluefs.md#bluefs_check_for_zeros) | `False` | Dev | Keep upstream default in production | [Bluefs](storage/bluefs.md) |
| [`bluefs_check_volume_selector_often`](storage/bluefs.md#bluefs_check_volume_selector_often) | `False` | Dev | Keep upstream default in production | [Bluefs](storage/bluefs.md) |
| [`bluefs_check_volume_selector_on_mount`](storage/bluefs.md#bluefs_check_volume_selector_on_mount) | `False` | Dev | Keep upstream default in production | [Bluefs](storage/bluefs.md) |
| [`bluefs_compact_log_sync`](storage/bluefs.md#bluefs_compact_log_sync) | `False` | Performance | Enable/disable based on measured need | [Bluefs](storage/bluefs.md) |
| [`bluefs_debug_force_slow`](storage/bluefs.md#bluefs_debug_force_slow) | `False` | Dev | Keep upstream default in production | [Bluefs](storage/bluefs.md) |
| [`bluefs_failed_shared_alloc_cooldown`](storage/bluefs.md#bluefs_failed_shared_alloc_cooldown) | `600` | Performance | Baseline → adjust → validate under load | [Bluefs](storage/bluefs.md) |
| [`bluefs_log_compact_min_ratio`](storage/bluefs.md#bluefs_log_compact_min_ratio) | `5` | Performance | Baseline → adjust → validate under load | [Bluefs](storage/bluefs.md) |
| [`bluefs_log_compact_min_size`](storage/bluefs.md#bluefs_log_compact_min_size) | `16_M` | Performance | Baseline → adjust → validate under load | [Bluefs](storage/bluefs.md) |
| [`bluefs_log_replay_check_allocations`](storage/bluefs.md#bluefs_log_replay_check_allocations) | `True` | Performance | Enable/disable based on measured need | [Bluefs](storage/bluefs.md) |
| [`bluefs_max_log_runway`](storage/bluefs.md#bluefs_max_log_runway) | `4_M` | Performance | Baseline → adjust → validate under load | [Bluefs](storage/bluefs.md) |
| [`bluefs_max_prefetch`](storage/bluefs.md#bluefs_max_prefetch) | `1_M` | Performance | Baseline → adjust → validate under load | [Bluefs](storage/bluefs.md) |
| [`bluefs_min_flush_size`](storage/bluefs.md#bluefs_min_flush_size) | `512_K` | Performance | Baseline → adjust → validate under load | [Bluefs](storage/bluefs.md) |
| [`bluefs_min_log_runway`](storage/bluefs.md#bluefs_min_log_runway) | `1_M` | Performance | Baseline → adjust → validate under load | [Bluefs](storage/bluefs.md) |
| [`bluefs_replay_recovery`](storage/bluefs.md#bluefs_replay_recovery) | `False` | Dev | Keep upstream default in production | [Bluefs](storage/bluefs.md) |
| [`bluefs_replay_recovery_disable_compact`](storage/bluefs.md#bluefs_replay_recovery_disable_compact) | `False` | Policy | Align with security and compatibility policy | [Bluefs](storage/bluefs.md) |
| [`bluefs_shared_alloc_size`](storage/bluefs.md#bluefs_shared_alloc_size) | `64_K` | Performance | Baseline → adjust → validate under load | [Bluefs](storage/bluefs.md) |
| [`bluefs_spillover_cleaner`](storage/bluefs.md#bluefs_spillover_cleaner) | `False` | Performance | Enable/disable based on measured need | [Bluefs](storage/bluefs.md) |
| [`bluefs_spillover_cleaner_work_ratio`](storage/bluefs.md#bluefs_spillover_cleaner_work_ratio) | `0.1` | Performance | Baseline → adjust → validate under load | [Bluefs](storage/bluefs.md) |
| [`bluefs_spillover_idle_time`](storage/bluefs.md#bluefs_spillover_idle_time) | `1200` | Performance | Baseline → adjust → validate under load | [Bluefs](storage/bluefs.md) |
| [`bluefs_sync_write`](storage/bluefs.md#bluefs_sync_write) | `False` | Performance | Enable/disable based on measured need | [Bluefs](storage/bluefs.md) |
| [`bluefs_wal_envelope_mode`](storage/bluefs.md#bluefs_wal_envelope_mode) | `True` | Performance | Enable/disable based on measured need | [Bluefs](storage/bluefs.md) |
| [`bluestore_2q_cache_kin_ratio`](storage/bluestore.md#bluestore_2q_cache_kin_ratio) | `0.5` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_2q_cache_kout_ratio`](storage/bluestore.md#bluestore_2q_cache_kout_ratio) | `0.5` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_alloc_stats_dump_interval`](storage/bluestore.md#bluestore_alloc_stats_dump_interval) | `1_day` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_allocation_from_file`](storage/bluestore.md#bluestore_allocation_from_file) | `True` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_allocation_recovery_threads`](storage/bluestore.md#bluestore_allocation_recovery_threads) | `0` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_allocator`](storage/bluestore.md#bluestore_allocator) | `hybrid` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_allocator_lookup_policy`](storage/bluestore.md#bluestore_allocator_lookup_policy) | `auto` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_async_db_compaction`](storage/bluestore.md#bluestore_async_db_compaction) | `True` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_avl_alloc_bf_free_pct`](storage/bluestore.md#bluestore_avl_alloc_bf_free_pct) | `4` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_avl_alloc_bf_threshold`](storage/bluestore.md#bluestore_avl_alloc_bf_threshold) | `128_K` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_avl_alloc_ff_max_search_bytes`](storage/bluestore.md#bluestore_avl_alloc_ff_max_search_bytes) | `16_M` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_avl_alloc_ff_max_search_count`](storage/bluestore.md#bluestore_avl_alloc_ff_max_search_count) | `100` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_bdev_label_multi`](storage/bluestore.md#bluestore_bdev_label_multi) | `True` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_bdev_label_multi_upgrade`](storage/bluestore.md#bluestore_bdev_label_multi_upgrade) | `False` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_bdev_label_require_all`](storage/bluestore.md#bluestore_bdev_label_require_all) | `True` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_bitmapallocator_blocks_per_zone`](storage/bluestore.md#bluestore_bitmapallocator_blocks_per_zone) | `1_K` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_bitmapallocator_span_size`](storage/bluestore.md#bluestore_bitmapallocator_span_size) | `1_K` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_blobid_prealloc`](storage/bluestore.md#bluestore_blobid_prealloc) | `10_K` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_block_create`](storage/bluestore.md#bluestore_block_create) | `True` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_block_db_create`](storage/bluestore.md#bluestore_block_db_create) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_block_db_path`](storage/bluestore.md#bluestore_block_db_path) | `(empty)` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_block_db_size`](storage/bluestore.md#bluestore_block_db_size) | `0` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_block_path`](storage/bluestore.md#bluestore_block_path) | `(empty)` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_block_preallocate_file`](storage/bluestore.md#bluestore_block_preallocate_file) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_block_size`](storage/bluestore.md#bluestore_block_size) | `100_G` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_block_wal_create`](storage/bluestore.md#bluestore_block_wal_create) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_block_wal_path`](storage/bluestore.md#bluestore_block_wal_path) | `(empty)` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_block_wal_size`](storage/bluestore.md#bluestore_block_wal_size) | `96_M` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_bluefs`](storage/bluestore.md#bluestore_bluefs) | `True` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_bluefs_alloc_failure_dump_interval`](storage/bluestore.md#bluestore_bluefs_alloc_failure_dump_interval) | `0` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_bluefs_env_mirror`](storage/bluestore.md#bluestore_bluefs_env_mirror) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_bluefs_max_free`](storage/bluestore.md#bluestore_bluefs_max_free) | `10_G` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_bluefs_warn_ratio`](storage/bluestore.md#bluestore_bluefs_warn_ratio) | `0.06` | Policy | Align with security and compatibility policy | [Bluestore](storage/bluestore.md) |
| [`bluestore_btree2_alloc_weight_factor`](storage/bluestore.md#bluestore_btree2_alloc_weight_factor) | `2` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_cache_age_bin_interval`](storage/bluestore.md#bluestore_cache_age_bin_interval) | `1` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_cache_age_bins_data`](storage/bluestore.md#bluestore_cache_age_bins_data) | `1 2 6 24 120 720 0 0 0 0` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_cache_age_bins_kv`](storage/bluestore.md#bluestore_cache_age_bins_kv) | `1 2 6 24 120 720 0 0 0 0` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_cache_age_bins_kv_onode`](storage/bluestore.md#bluestore_cache_age_bins_kv_onode) | `0 0 0 0 0 0 0 0 0 720` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_cache_age_bins_meta`](storage/bluestore.md#bluestore_cache_age_bins_meta) | `1 2 6 24 120 720 0 0 0 0` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_cache_autotune`](storage/bluestore.md#bluestore_cache_autotune) | `True` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_cache_autotune_interval`](storage/bluestore.md#bluestore_cache_autotune_interval) | `5` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_cache_kv_onode_ratio`](storage/bluestore.md#bluestore_cache_kv_onode_ratio) | `0.04` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_cache_kv_ratio`](storage/bluestore.md#bluestore_cache_kv_ratio) | `0.45` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_cache_meta_evict_in_autotune`](storage/bluestore.md#bluestore_cache_meta_evict_in_autotune) | `True` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_cache_meta_evict_limit`](storage/bluestore.md#bluestore_cache_meta_evict_limit) | `10` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_cache_meta_ratio`](storage/bluestore.md#bluestore_cache_meta_ratio) | `0.45` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_cache_size`](storage/bluestore.md#bluestore_cache_size) | `0` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_cache_size_hdd`](storage/bluestore.md#bluestore_cache_size_hdd) | `1_G` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_cache_size_ssd`](storage/bluestore.md#bluestore_cache_size_ssd) | `3_G` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_cache_trim_interval`](storage/bluestore.md#bluestore_cache_trim_interval) | `0.05` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_cache_trim_max_skip_pinned`](storage/bluestore.md#bluestore_cache_trim_max_skip_pinned) | `1000` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_cache_type`](storage/bluestore.md#bluestore_cache_type) | `2q` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_cleaner_sleep_interval`](storage/bluestore.md#bluestore_cleaner_sleep_interval) | `5` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_clone_cow`](storage/bluestore.md#bluestore_clone_cow) | `True` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_compression_algorithm`](storage/bluestore.md#bluestore_compression_algorithm) | `snappy` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_compression_max_blob_size`](storage/bluestore.md#bluestore_compression_max_blob_size) | `0` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_compression_max_blob_size_hdd`](storage/bluestore.md#bluestore_compression_max_blob_size_hdd) | `64_K` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_compression_max_blob_size_ssd`](storage/bluestore.md#bluestore_compression_max_blob_size_ssd) | `64_K` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_compression_min_blob_size`](storage/bluestore.md#bluestore_compression_min_blob_size) | `0` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_compression_min_blob_size_hdd`](storage/bluestore.md#bluestore_compression_min_blob_size_hdd) | `64_K` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_compression_min_blob_size_ssd`](storage/bluestore.md#bluestore_compression_min_blob_size_ssd) | `64_K` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_compression_mode`](storage/bluestore.md#bluestore_compression_mode) | `none` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_compression_required_ratio`](storage/bluestore.md#bluestore_compression_required_ratio) | `0.875` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_csum_type`](storage/bluestore.md#bluestore_csum_type) | `crc32c` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_enforce_min_alloc_size`](storage/bluestore.md#bluestore_debug_enforce_min_alloc_size) | `0` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_enforce_settings`](storage/bluestore.md#bluestore_debug_enforce_settings) | `default` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_extent_map_encode_check`](storage/bluestore.md#bluestore_debug_extent_map_encode_check) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_fast_recovery_compare_chance`](storage/bluestore.md#bluestore_debug_fast_recovery_compare_chance) | `0` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_freelist`](storage/bluestore.md#bluestore_debug_freelist) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_fsck_abort`](storage/bluestore.md#bluestore_debug_fsck_abort) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_inject_allocation_from_file_failure`](storage/bluestore.md#bluestore_debug_inject_allocation_from_file_failure) | `0` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_inject_csum_err_probability`](storage/bluestore.md#bluestore_debug_inject_csum_err_probability) | `0` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_inject_read_err`](storage/bluestore.md#bluestore_debug_inject_read_err) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_legacy_omap`](storage/bluestore.md#bluestore_debug_legacy_omap) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_no_reuse_blocks`](storage/bluestore.md#bluestore_debug_no_reuse_blocks) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_omit_block_device_write`](storage/bluestore.md#bluestore_debug_omit_block_device_write) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_omit_kv_commit`](storage/bluestore.md#bluestore_debug_omit_kv_commit) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_onode_segmentation_random`](storage/bluestore.md#bluestore_debug_onode_segmentation_random) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_permit_any_bdev_label`](storage/bluestore.md#bluestore_debug_permit_any_bdev_label) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_prefragment_max`](storage/bluestore.md#bluestore_debug_prefragment_max) | `1_M` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_random_read_err`](storage/bluestore.md#bluestore_debug_random_read_err) | `0` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_randomize_serial_transaction`](storage/bluestore.md#bluestore_debug_randomize_serial_transaction) | `0` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_small_allocations`](storage/bluestore.md#bluestore_debug_small_allocations) | `0` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_debug_too_many_blobs_threshold`](storage/bluestore.md#bluestore_debug_too_many_blobs_threshold) | `24576` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_default_buffered_read`](storage/bluestore.md#bluestore_default_buffered_read) | `True` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_default_buffered_write`](storage/bluestore.md#bluestore_default_buffered_write) | `False` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_deferred_batch_ops`](storage/bluestore.md#bluestore_deferred_batch_ops) | `0` | Performance | Stay within documented bounds | [Bluestore](storage/bluestore.md) |
| [`bluestore_deferred_batch_ops_hdd`](storage/bluestore.md#bluestore_deferred_batch_ops_hdd) | `64` | Performance | Stay within documented bounds | [Bluestore](storage/bluestore.md) |
| [`bluestore_deferred_batch_ops_ssd`](storage/bluestore.md#bluestore_deferred_batch_ops_ssd) | `16` | Performance | Stay within documented bounds | [Bluestore](storage/bluestore.md) |
| [`bluestore_discard_on_mkfs`](storage/bluestore.md#bluestore_discard_on_mkfs) | `True` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_elastic_shared_blobs`](storage/bluestore.md#bluestore_elastic_shared_blobs) | `True` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_extent_map_inline_shard_prealloc_size`](storage/bluestore.md#bluestore_extent_map_inline_shard_prealloc_size) | `256` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_extent_map_shard_max_size`](storage/bluestore.md#bluestore_extent_map_shard_max_size) | `1200` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_extent_map_shard_min_size`](storage/bluestore.md#bluestore_extent_map_shard_min_size) | `150` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_extent_map_shard_target_size`](storage/bluestore.md#bluestore_extent_map_shard_target_size) | `500` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_extent_map_shard_target_size_slop`](storage/bluestore.md#bluestore_extent_map_shard_target_size_slop) | `0.2` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_fail_eio`](storage/bluestore.md#bluestore_fail_eio) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_frag_runtime`](storage/bluestore.md#bluestore_frag_runtime) | `False` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_frag_static`](storage/bluestore.md#bluestore_frag_static) | `False` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_fragmentation_check_period`](storage/bluestore.md#bluestore_fragmentation_check_period) | `3600` | Policy | Align with security and compatibility policy | [Bluestore](storage/bluestore.md) |
| [`bluestore_freelist_blocks_per_key`](storage/bluestore.md#bluestore_freelist_blocks_per_key) | `128` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_fsck_error_on_no_per_pg_omap`](storage/bluestore.md#bluestore_fsck_error_on_no_per_pg_omap) | `False` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_fsck_error_on_no_per_pool_omap`](storage/bluestore.md#bluestore_fsck_error_on_no_per_pool_omap) | `False` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_fsck_error_on_no_per_pool_stats`](storage/bluestore.md#bluestore_fsck_error_on_no_per_pool_stats) | `False` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_fsck_on_mkfs`](storage/bluestore.md#bluestore_fsck_on_mkfs) | `True` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_fsck_on_mkfs_deep`](storage/bluestore.md#bluestore_fsck_on_mkfs_deep) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_fsck_on_mount`](storage/bluestore.md#bluestore_fsck_on_mount) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_fsck_on_mount_deep`](storage/bluestore.md#bluestore_fsck_on_mount_deep) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_fsck_on_umount`](storage/bluestore.md#bluestore_fsck_on_umount) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_fsck_on_umount_deep`](storage/bluestore.md#bluestore_fsck_on_umount_deep) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_fsck_quick_fix_on_mount`](storage/bluestore.md#bluestore_fsck_quick_fix_on_mount) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_fsck_quick_fix_threads`](storage/bluestore.md#bluestore_fsck_quick_fix_threads) | `2` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_fsck_read_bytes_cap`](storage/bluestore.md#bluestore_fsck_read_bytes_cap) | `64_M` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_fsck_shared_blob_tracker_size`](storage/bluestore.md#bluestore_fsck_shared_blob_tracker_size) | `0.03125` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_gc_enable_blob_threshold`](storage/bluestore.md#bluestore_gc_enable_blob_threshold) | `0` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_gc_enable_total_threshold`](storage/bluestore.md#bluestore_gc_enable_total_threshold) | `0` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_hybrid_alloc_mem_cap`](storage/bluestore.md#bluestore_hybrid_alloc_mem_cap) | `64_M` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_ignore_data_csum`](storage/bluestore.md#bluestore_ignore_data_csum) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_kv_sync_util_logging_s`](storage/bluestore.md#bluestore_kv_sync_util_logging_s) | `10` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_kvbackend`](storage/bluestore.md#bluestore_kvbackend) | `rocksdb` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_log_collection_list_age`](storage/bluestore.md#bluestore_log_collection_list_age) | `1_min` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_log_omap_iterator_age`](storage/bluestore.md#bluestore_log_omap_iterator_age) | `5` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_log_op_age`](storage/bluestore.md#bluestore_log_op_age) | `5` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_log_scrub_op_age`](storage/bluestore.md#bluestore_log_scrub_op_age) | `5` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_max_alloc_size`](storage/bluestore.md#bluestore_max_alloc_size) | `0` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_max_blob_size`](storage/bluestore.md#bluestore_max_blob_size) | `0` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_max_blob_size_hdd`](storage/bluestore.md#bluestore_max_blob_size_hdd) | `64_K` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_max_blob_size_ssd`](storage/bluestore.md#bluestore_max_blob_size_ssd) | `64_K` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_max_defer_interval`](storage/bluestore.md#bluestore_max_defer_interval) | `3` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_max_deferred_txc`](storage/bluestore.md#bluestore_max_deferred_txc) | `32` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_min_alloc_size`](storage/bluestore.md#bluestore_min_alloc_size) | `0` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_min_alloc_size_hdd`](storage/bluestore.md#bluestore_min_alloc_size_hdd) | `4_K` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_min_alloc_size_ssd`](storage/bluestore.md#bluestore_min_alloc_size_ssd) | `4_K` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_nid_prealloc`](storage/bluestore.md#bluestore_nid_prealloc) | `1024` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_onode_segment_size`](storage/bluestore.md#bluestore_onode_segment_size) | `0` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_prefer_deferred_size`](storage/bluestore.md#bluestore_prefer_deferred_size) | `0` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_prefer_deferred_size_hdd`](storage/bluestore.md#bluestore_prefer_deferred_size_hdd) | `64_K` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_prefer_deferred_size_ssd`](storage/bluestore.md#bluestore_prefer_deferred_size_ssd) | `0` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_qfsck_on_mount`](storage/bluestore.md#bluestore_qfsck_on_mount) | `True` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_recompression_min_gain`](storage/bluestore.md#bluestore_recompression_min_gain) | `1.2` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_retry_disk_reads`](storage/bluestore.md#bluestore_retry_disk_reads) | `3` | Performance | Stay within documented bounds | [Bluestore](storage/bluestore.md) |
| [`bluestore_rocksdb_cf`](storage/bluestore.md#bluestore_rocksdb_cf) | `True` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_rocksdb_cfs`](storage/bluestore.md#bluestore_rocksdb_cfs) | `m(3) p(3,0-12) O(3,0-13)=block_cache={type=binned_lru} L=min_write_buffer_number_to_merge=32 P=min_write_buffer_number_to_merge=32` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_rocksdb_options`](storage/bluestore.md#bluestore_rocksdb_options) | `compression=kLZ4Compression,max_write_buffer_number=64,min_write_buffer_number_to_merge=6,compaction_style=kCompactionStyleLevel,write_buffer_size=16777216,max_background_jobs=4,level0_file_num_compaction_trigger=8,max_bytes_for_level_base=1073741824,max_bytes_for_level_multiplier=8,compaction_readahead_size=2MB,max_total_wal_size=1073741824,writable_file_max_buffer_size=0` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_rocksdb_options_annex`](storage/bluestore.md#bluestore_rocksdb_options_annex) | `(empty)` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_slow_ops_warn_lifetime`](storage/bluestore.md#bluestore_slow_ops_warn_lifetime) | `86400` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_slow_ops_warn_threshold`](storage/bluestore.md#bluestore_slow_ops_warn_threshold) | `1` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_slow_scrub_ops_warn_threshold`](storage/bluestore.md#bluestore_slow_scrub_ops_warn_threshold) | `1` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_spdk_coremask`](storage/bluestore.md#bluestore_spdk_coremask) | `0x1` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_spdk_io_sleep`](storage/bluestore.md#bluestore_spdk_io_sleep) | `5` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_spdk_max_io_completion`](storage/bluestore.md#bluestore_spdk_max_io_completion) | `0` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_spdk_mem`](storage/bluestore.md#bluestore_spdk_mem) | `512` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_sync_submit_transaction`](storage/bluestore.md#bluestore_sync_submit_transaction) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_throttle_bytes`](storage/bluestore.md#bluestore_throttle_bytes) | `64_M` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_throttle_cost_per_io`](storage/bluestore.md#bluestore_throttle_cost_per_io) | `0` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_throttle_cost_per_io_hdd`](storage/bluestore.md#bluestore_throttle_cost_per_io_hdd) | `670000` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_throttle_cost_per_io_ssd`](storage/bluestore.md#bluestore_throttle_cost_per_io_ssd) | `4000` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_throttle_deferred_bytes`](storage/bluestore.md#bluestore_throttle_deferred_bytes) | `128_M` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_throttle_trace_rate`](storage/bluestore.md#bluestore_throttle_trace_rate) | `0` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_tracing`](storage/bluestore.md#bluestore_tracing) | `False` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_use_ebd`](storage/bluestore.md#bluestore_use_ebd) | `True` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_use_optimal_io_size_for_min_alloc_size`](storage/bluestore.md#bluestore_use_optimal_io_size_for_min_alloc_size) | `False` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_volume_selection_policy`](storage/bluestore.md#bluestore_volume_selection_policy) | `use_some_extra` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`bluestore_volume_selection_reserved`](storage/bluestore.md#bluestore_volume_selection_reserved) | `0` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_volume_selection_reserved_factor`](storage/bluestore.md#bluestore_volume_selection_reserved_factor) | `2` | Performance | Baseline → adjust → validate under load | [Bluestore](storage/bluestore.md) |
| [`bluestore_warn_on_bluefs_spillover`](storage/bluestore.md#bluestore_warn_on_bluefs_spillover) | `True` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_warn_on_free_fragmentation`](storage/bluestore.md#bluestore_warn_on_free_fragmentation) | `0.8` | Policy | Align with security and compatibility policy | [Bluestore](storage/bluestore.md) |
| [`bluestore_warn_on_legacy_statfs`](storage/bluestore.md#bluestore_warn_on_legacy_statfs) | `True` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_warn_on_no_per_pg_omap`](storage/bluestore.md#bluestore_warn_on_no_per_pg_omap) | `False` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_warn_on_no_per_pool_omap`](storage/bluestore.md#bluestore_warn_on_no_per_pool_omap) | `True` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_warn_on_spurious_read_errors`](storage/bluestore.md#bluestore_warn_on_spurious_read_errors) | `True` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_write_v2`](storage/bluestore.md#bluestore_write_v2) | `False` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_write_v2_random`](storage/bluestore.md#bluestore_write_v2_random) | `False` | Performance | Enable/disable based on measured need | [Bluestore](storage/bluestore.md) |
| [`bluestore_zero_block_detection`](storage/bluestore.md#bluestore_zero_block_detection) | `False` | Dev | Keep upstream default in production | [Bluestore](storage/bluestore.md) |
| [`breakpad`](runtime/breakpad.md#breakpad) | `False` | Performance | Enable/disable based on measured need | [Breakpad](runtime/breakpad.md) |
| [`ceph_assert_supresssions`](cluster/ceph.md#ceph_assert_supresssions) | `(empty)` | Dev | Keep upstream default in production | [Ceph](cluster/ceph.md) |
| [`cephsqlite_blocklist_dead_locker`](runtime/cephsqlite.md#cephsqlite_blocklist_dead_locker) | `True` | Performance | Enable/disable based on measured need | [Cephsqlite](runtime/cephsqlite.md) |
| [`cephsqlite_lock_renewal_interval`](runtime/cephsqlite.md#cephsqlite_lock_renewal_interval) | `2000` | Performance | Stay within documented bounds | [Cephsqlite](runtime/cephsqlite.md) |
| [`cephsqlite_lock_renewal_timeout`](runtime/cephsqlite.md#cephsqlite_lock_renewal_timeout) | `30000` | Performance | Stay within documented bounds | [Cephsqlite](runtime/cephsqlite.md) |
| [`cephx_cluster_require_signatures`](auth/cephx.md#cephx_cluster_require_signatures) | `False` | Performance | Enable/disable based on measured need | [Cephx](auth/cephx.md) |
| [`cephx_cluster_require_version`](auth/cephx.md#cephx_cluster_require_version) | `2` | Performance | Baseline → adjust → validate under load | [Cephx](auth/cephx.md) |
| [`cephx_require_signatures`](auth/cephx.md#cephx_require_signatures) | `False` | Performance | Enable/disable based on measured need | [Cephx](auth/cephx.md) |
| [`cephx_require_version`](auth/cephx.md#cephx_require_version) | `2` | Performance | Baseline → adjust → validate under load | [Cephx](auth/cephx.md) |
| [`cephx_service_require_signatures`](auth/cephx.md#cephx_service_require_signatures) | `False` | Performance | Enable/disable based on measured need | [Cephx](auth/cephx.md) |
| [`cephx_service_require_version`](auth/cephx.md#cephx_service_require_version) | `2` | Performance | Baseline → adjust → validate under load | [Cephx](auth/cephx.md) |
| [`cephx_sign_messages`](auth/cephx.md#cephx_sign_messages) | `True` | Performance | Enable/disable based on measured need | [Cephx](auth/cephx.md) |
| [`chdir`](runtime/chdir.md#chdir) | `(empty)` | Performance | Baseline → adjust → validate under load | [Chdir](runtime/chdir.md) |
| [`clog_to_graylog`](debug/clog.md#clog_to_graylog) | `false` | Performance | Baseline → adjust → validate under load | [Clog](debug/clog.md) |
| [`clog_to_graylog_host`](debug/clog.md#clog_to_graylog_host) | `127.0.0.1` | Performance | Baseline → adjust → validate under load | [Clog](debug/clog.md) |
| [`clog_to_graylog_port`](debug/clog.md#clog_to_graylog_port) | `12201` | Performance | Baseline → adjust → validate under load | [Clog](debug/clog.md) |
| [`clog_to_monitors`](debug/clog.md#clog_to_monitors) | `default=true` | Performance | Baseline → adjust → validate under load | [Clog](debug/clog.md) |
| [`clog_to_syslog`](debug/clog.md#clog_to_syslog) | `false` | Performance | Baseline → adjust → validate under load | [Clog](debug/clog.md) |
| [`clog_to_syslog_facility`](debug/clog.md#clog_to_syslog_facility) | `default=daemon audit=local0` | Performance | Baseline → adjust → validate under load | [Clog](debug/clog.md) |
| [`clog_to_syslog_level`](debug/clog.md#clog_to_syslog_level) | `info` | Performance | Baseline → adjust → validate under load | [Clog](debug/clog.md) |
| [`cluster_addr`](cluster/cluster.md#cluster_addr) | `(empty)` | Connectivity | Use nearest stable endpoint | [Cluster](cluster/cluster.md) |
| [`cluster_network`](cluster/cluster.md#cluster_network) | `(empty)` | Performance | Baseline → adjust → validate under load | [Cluster](cluster/cluster.md) |
| [`cluster_network_interface`](cluster/cluster.md#cluster_network_interface) | `(empty)` | Performance | Baseline → adjust → validate under load | [Cluster](cluster/cluster.md) |
| [`compressor_zlib_isal`](storage/compressor.md#compressor_zlib_isal) | `False` | Performance | Enable/disable based on measured need | [Compressor](storage/compressor.md) |
| [`compressor_zlib_level`](storage/compressor.md#compressor_zlib_level) | `5` | Performance | Baseline → adjust → validate under load | [Compressor](storage/compressor.md) |
| [`compressor_zlib_winsize`](storage/compressor.md#compressor_zlib_winsize) | `-15` | Performance | Stay within documented bounds | [Compressor](storage/compressor.md) |
| [`compressor_zstd_level`](storage/compressor.md#compressor_zstd_level) | `1` | Performance | Baseline → adjust → validate under load | [Compressor](storage/compressor.md) |
| [`container_image`](runtime/container.md#container_image) | `docker.io/ceph/daemon-base:latest-master-devel` | Policy | Align with security and compatibility policy | [Container](runtime/container.md) |
| [`crash_dir`](runtime/crash.md#crash_dir) | `/var/lib/ceph/crash` | Capacity | Match filesystem layout and capacity plan | [Crash](runtime/crash.md) |
| [`crush_location`](cluster/crush.md#crush_location) | `(empty)` | Performance | Baseline → adjust → validate under load | [Crush](cluster/crush.md) |
| [`crush_location_hook`](cluster/crush.md#crush_location_hook) | `(empty)` | Performance | Baseline → adjust → validate under load | [Crush](cluster/crush.md) |
| [`crush_location_hook_timeout`](cluster/crush.md#crush_location_hook_timeout) | `10` | Performance | Baseline → adjust → validate under load | [Crush](cluster/crush.md) |
| [`daemonize`](runtime/daemonize.md#daemonize) | `True` | Performance | Enable/disable based on measured need | [Daemonize](runtime/daemonize.md) |
| [`debug_asok_assert_abort`](debug/debug.md#debug_asok_assert_abort) | `False` | Dev | Keep upstream default in production | [Debug](debug/debug.md) |
| [`debug_asserts_on_shutdown`](debug/debug.md#debug_asserts_on_shutdown) | `False` | Dev | Keep upstream default in production | [Debug](debug/debug.md) |
| [`debug_deliberately_leak_memory`](debug/debug.md#debug_deliberately_leak_memory) | `False` | Dev | Keep upstream default in production | [Debug](debug/debug.md) |
| [`debug_disable_randomized_ping`](debug/debug.md#debug_disable_randomized_ping) | `False` | Dev | Keep upstream default in production | [Debug](debug/debug.md) |
| [`debug_heartbeat_testing_span`](debug/debug.md#debug_heartbeat_testing_span) | `0` | Dev | Keep upstream default in production | [Debug](debug/debug.md) |
| [`device_failure_prediction_mode`](runtime/device.md#device_failure_prediction_mode) | `none` | Policy | Align with security and compatibility policy | [Device](runtime/device.md) |
| [`ec_extent_cache_size`](storage/ec.md#ec_extent_cache_size) | `10485760` | Performance | Baseline → adjust → validate under load | [Ec](storage/ec.md) |
| [`ec_pdw_write_mode`](storage/ec.md#ec_pdw_write_mode) | `0` | Dev | Keep upstream default in production | [Ec](storage/ec.md) |
| [`enable_experimental_unrecoverable_data_corrupting_features`](runtime/enable.md#enable_experimental_unrecoverable_data_corrupting_features) | `(empty)` | Performance | Baseline → adjust → validate under load | [Enable](runtime/enable.md) |
| [`erasure_code_dir`](storage/erasure.md#erasure_code_dir) | `0/erasure-code` | Capacity | Match filesystem layout and capacity plan | [Erasure](storage/erasure.md) |
| [`err_to_graylog`](debug/err.md#err_to_graylog) | `False` | Policy | Align with security and compatibility policy | [Err](debug/err.md) |
| [`err_to_journald`](debug/err.md#err_to_journald) | `False` | Policy | Align with security and compatibility policy | [Err](debug/err.md) |
| [`err_to_stderr`](debug/err.md#err_to_stderr) | `True` | Policy | Align with security and compatibility policy | [Err](debug/err.md) |
| [`err_to_syslog`](debug/err.md#err_to_syslog) | `False` | Policy | Align with security and compatibility policy | [Err](debug/err.md) |
| [`event_tracing`](debug/event.md#event_tracing) | `False` | Performance | Enable/disable based on measured need | [Event](debug/event.md) |
| [`fatal_signal_handlers`](runtime/fatal.md#fatal_signal_handlers) | `True` | Performance | Enable/disable based on measured need | [Fatal](runtime/fatal.md) |
| [`filer_max_purge_ops`](runtime/filer.md#filer_max_purge_ops) | `10` | Performance | Baseline → adjust → validate under load | [Filer](runtime/filer.md) |
| [`filer_max_truncate_ops`](runtime/filer.md#filer_max_truncate_ops) | `128` | Performance | Baseline → adjust → validate under load | [Filer](runtime/filer.md) |
| [`filestore_apply_finisher_threads`](storage/filestore.md#filestore_apply_finisher_threads) | `1` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_blackhole`](storage/filestore.md#filestore_blackhole) | `False` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_btrfs_clone_range`](storage/filestore.md#filestore_btrfs_clone_range) | `True` | Performance | Enable/disable based on measured need | [Filestore](storage/filestore.md) |
| [`filestore_btrfs_snap`](storage/filestore.md#filestore_btrfs_snap) | `True` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_caller_concurrency`](storage/filestore.md#filestore_caller_concurrency) | `10` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_collect_device_partition_information`](storage/filestore.md#filestore_collect_device_partition_information) | `True` | Performance | Enable/disable based on measured need | [Filestore](storage/filestore.md) |
| [`filestore_commit_timeout`](storage/filestore.md#filestore_commit_timeout) | `10_min` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_debug_inject_read_err`](storage/filestore.md#filestore_debug_inject_read_err) | `False` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_debug_omap_check`](storage/filestore.md#filestore_debug_omap_check) | `False` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_debug_verify_split`](storage/filestore.md#filestore_debug_verify_split) | `False` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_dump_file`](storage/filestore.md#filestore_dump_file) | `(empty)` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_expected_throughput_bytes`](storage/filestore.md#filestore_expected_throughput_bytes) | `209715200` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_expected_throughput_ops`](storage/filestore.md#filestore_expected_throughput_ops) | `200` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_fadvise`](storage/filestore.md#filestore_fadvise) | `True` | Performance | Enable/disable based on measured need | [Filestore](storage/filestore.md) |
| [`filestore_fail_eio`](storage/filestore.md#filestore_fail_eio) | `True` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_fd_cache_shards`](storage/filestore.md#filestore_fd_cache_shards) | `16` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_fd_cache_size`](storage/filestore.md#filestore_fd_cache_size) | `128` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_fiemap`](storage/filestore.md#filestore_fiemap) | `False` | Performance | Enable/disable based on measured need | [Filestore](storage/filestore.md) |
| [`filestore_fiemap_threshold`](storage/filestore.md#filestore_fiemap_threshold) | `4_K` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_fsync_flushes_journal_data`](storage/filestore.md#filestore_fsync_flushes_journal_data) | `False` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_index_retry_probability`](storage/filestore.md#filestore_index_retry_probability) | `0` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_inject_stall`](storage/filestore.md#filestore_inject_stall) | `0` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_journal_parallel`](storage/filestore.md#filestore_journal_parallel) | `False` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_journal_trailing`](storage/filestore.md#filestore_journal_trailing) | `False` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_journal_writeahead`](storage/filestore.md#filestore_journal_writeahead) | `False` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_kill_at`](storage/filestore.md#filestore_kill_at) | `0` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_max_alloc_hint_size`](storage/filestore.md#filestore_max_alloc_hint_size) | `1_M` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_max_inline_xattr_size`](storage/filestore.md#filestore_max_inline_xattr_size) | `0` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_max_inline_xattr_size_btrfs`](storage/filestore.md#filestore_max_inline_xattr_size_btrfs) | `2_K` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_max_inline_xattr_size_other`](storage/filestore.md#filestore_max_inline_xattr_size_other) | `512` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_max_inline_xattr_size_xfs`](storage/filestore.md#filestore_max_inline_xattr_size_xfs) | `64_K` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_max_inline_xattrs`](storage/filestore.md#filestore_max_inline_xattrs) | `0` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_max_inline_xattrs_btrfs`](storage/filestore.md#filestore_max_inline_xattrs_btrfs) | `10` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_max_inline_xattrs_other`](storage/filestore.md#filestore_max_inline_xattrs_other) | `2` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_max_inline_xattrs_xfs`](storage/filestore.md#filestore_max_inline_xattrs_xfs) | `10` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_max_sync_interval`](storage/filestore.md#filestore_max_sync_interval) | `5` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_max_xattr_value_size`](storage/filestore.md#filestore_max_xattr_value_size) | `0` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_max_xattr_value_size_btrfs`](storage/filestore.md#filestore_max_xattr_value_size_btrfs) | `64_K` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_max_xattr_value_size_other`](storage/filestore.md#filestore_max_xattr_value_size_other) | `1_K` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_max_xattr_value_size_xfs`](storage/filestore.md#filestore_max_xattr_value_size_xfs) | `64_K` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_merge_threshold`](storage/filestore.md#filestore_merge_threshold) | `-10` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_min_sync_interval`](storage/filestore.md#filestore_min_sync_interval) | `0.01` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_odsync_write`](storage/filestore.md#filestore_odsync_write) | `False` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_omap_backend`](storage/filestore.md#filestore_omap_backend) | `rocksdb` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_omap_backend_path`](storage/filestore.md#filestore_omap_backend_path) | `(empty)` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_omap_header_cache_size`](storage/filestore.md#filestore_omap_header_cache_size) | `1_K` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_ondisk_finisher_threads`](storage/filestore.md#filestore_ondisk_finisher_threads) | `1` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_op_thread_suicide_timeout`](storage/filestore.md#filestore_op_thread_suicide_timeout) | `3_min` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_op_thread_timeout`](storage/filestore.md#filestore_op_thread_timeout) | `1_min` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_op_threads`](storage/filestore.md#filestore_op_threads) | `2` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_punch_hole`](storage/filestore.md#filestore_punch_hole) | `False` | Performance | Enable/disable based on measured need | [Filestore](storage/filestore.md) |
| [`filestore_queue_high_delay_multiple`](storage/filestore.md#filestore_queue_high_delay_multiple) | `0` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_queue_high_delay_multiple_bytes`](storage/filestore.md#filestore_queue_high_delay_multiple_bytes) | `0` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_queue_high_delay_multiple_ops`](storage/filestore.md#filestore_queue_high_delay_multiple_ops) | `0` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_queue_high_threshhold`](storage/filestore.md#filestore_queue_high_threshhold) | `0.9` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_queue_low_threshhold`](storage/filestore.md#filestore_queue_low_threshhold) | `0.3` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_queue_max_bytes`](storage/filestore.md#filestore_queue_max_bytes) | `100_M` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_queue_max_delay_multiple`](storage/filestore.md#filestore_queue_max_delay_multiple) | `0` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_queue_max_delay_multiple_bytes`](storage/filestore.md#filestore_queue_max_delay_multiple_bytes) | `0` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_queue_max_delay_multiple_ops`](storage/filestore.md#filestore_queue_max_delay_multiple_ops) | `0` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_queue_max_ops`](storage/filestore.md#filestore_queue_max_ops) | `50` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_rocksdb_options`](storage/filestore.md#filestore_rocksdb_options) | `max_background_jobs=10,compaction_readahead_size=2097152,compression=kNoCompression` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_seek_data_hole`](storage/filestore.md#filestore_seek_data_hole) | `False` | Performance | Enable/disable based on measured need | [Filestore](storage/filestore.md) |
| [`filestore_sloppy_crc`](storage/filestore.md#filestore_sloppy_crc) | `False` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_sloppy_crc_block_size`](storage/filestore.md#filestore_sloppy_crc_block_size) | `64_K` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_splice`](storage/filestore.md#filestore_splice) | `False` | Performance | Enable/disable based on measured need | [Filestore](storage/filestore.md) |
| [`filestore_split_multiple`](storage/filestore.md#filestore_split_multiple) | `2` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_split_rand_factor`](storage/filestore.md#filestore_split_rand_factor) | `20` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_update_to`](storage/filestore.md#filestore_update_to) | `1000` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`filestore_wbthrottle_btrfs_bytes_hard_limit`](storage/filestore.md#filestore_wbthrottle_btrfs_bytes_hard_limit) | `400_M` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_wbthrottle_btrfs_bytes_start_flusher`](storage/filestore.md#filestore_wbthrottle_btrfs_bytes_start_flusher) | `40_M` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_wbthrottle_btrfs_inodes_hard_limit`](storage/filestore.md#filestore_wbthrottle_btrfs_inodes_hard_limit) | `5000` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_wbthrottle_btrfs_inodes_start_flusher`](storage/filestore.md#filestore_wbthrottle_btrfs_inodes_start_flusher) | `500` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_wbthrottle_btrfs_ios_hard_limit`](storage/filestore.md#filestore_wbthrottle_btrfs_ios_hard_limit) | `5000` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_wbthrottle_btrfs_ios_start_flusher`](storage/filestore.md#filestore_wbthrottle_btrfs_ios_start_flusher) | `500` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_wbthrottle_enable`](storage/filestore.md#filestore_wbthrottle_enable) | `True` | Policy | Align with security and compatibility policy | [Filestore](storage/filestore.md) |
| [`filestore_wbthrottle_xfs_bytes_hard_limit`](storage/filestore.md#filestore_wbthrottle_xfs_bytes_hard_limit) | `400_M` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_wbthrottle_xfs_bytes_start_flusher`](storage/filestore.md#filestore_wbthrottle_xfs_bytes_start_flusher) | `40_M` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_wbthrottle_xfs_inodes_hard_limit`](storage/filestore.md#filestore_wbthrottle_xfs_inodes_hard_limit) | `5000` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_wbthrottle_xfs_inodes_start_flusher`](storage/filestore.md#filestore_wbthrottle_xfs_inodes_start_flusher) | `500` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_wbthrottle_xfs_ios_hard_limit`](storage/filestore.md#filestore_wbthrottle_xfs_ios_hard_limit) | `5000` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_wbthrottle_xfs_ios_start_flusher`](storage/filestore.md#filestore_wbthrottle_xfs_ios_start_flusher) | `500` | Performance | Baseline → adjust → validate under load | [Filestore](storage/filestore.md) |
| [`filestore_xfs_extsize`](storage/filestore.md#filestore_xfs_extsize) | `False` | Performance | Enable/disable based on measured need | [Filestore](storage/filestore.md) |
| [`filestore_zfs_snap`](storage/filestore.md#filestore_zfs_snap) | `False` | Dev | Keep upstream default in production | [Filestore](storage/filestore.md) |
| [`fio_dir`](runtime/fio.md#fio_dir) | `/tmp/fio` | Capacity | Match filesystem layout and capacity plan | [Fio](runtime/fio.md) |
| [`fsid`](cluster/fsid.md#fsid) | `(empty)` | Policy | Align with security and compatibility policy | [Fsid](cluster/fsid.md) |
| [`gss_ktab_client_file`](auth/gss.md#gss_ktab_client_file) | `/var/lib/ceph/$name/gss_client_$name.ktab` | Capacity | Match filesystem layout and capacity plan | [Gss](auth/gss.md) |
| [`gss_target_name`](auth/gss.md#gss_target_name) | `ceph` | Performance | Baseline → adjust → validate under load | [Gss](auth/gss.md) |
| [`heartbeat_file`](network/heartbeat.md#heartbeat_file) | `(empty)` | Capacity | Match filesystem layout and capacity plan | [Heartbeat](network/heartbeat.md) |
| [`heartbeat_inject_failure`](network/heartbeat.md#heartbeat_inject_failure) | `0` | Dev | Keep upstream default in production | [Heartbeat](network/heartbeat.md) |
| [`heartbeat_interval`](network/heartbeat.md#heartbeat_interval) | `5` | Performance | Baseline → adjust → validate under load | [Heartbeat](network/heartbeat.md) |
| [`host`](runtime/host.md#host) | `(empty)` | Policy | Align with security and compatibility policy | [Host](runtime/host.md) |
| [`inject_early_sigterm`](debug/inject.md#inject_early_sigterm) | `False` | Dev | Keep upstream default in production | [Inject](debug/inject.md) |
| [`jaeger_agent_port`](runtime/jaeger.md#jaeger_agent_port) | `6799` | Performance | Baseline → adjust → validate under load | [Jaeger](runtime/jaeger.md) |
| [`jaeger_tracing_enable`](runtime/jaeger.md#jaeger_tracing_enable) | `False` | Policy | Align with security and compatibility policy | [Jaeger](runtime/jaeger.md) |
| [`journal_aio`](storage/journal.md#journal_aio) | `True` | Dev | Keep upstream default in production | [Journal](storage/journal.md) |
| [`journal_align_min_size`](storage/journal.md#journal_align_min_size) | `64_K` | Dev | Keep upstream default in production | [Journal](storage/journal.md) |
| [`journal_block_align`](storage/journal.md#journal_block_align) | `True` | Dev | Keep upstream default in production | [Journal](storage/journal.md) |
| [`journal_block_size`](storage/journal.md#journal_block_size) | `4_K` | Dev | Keep upstream default in production | [Journal](storage/journal.md) |
| [`journal_dio`](storage/journal.md#journal_dio) | `True` | Dev | Keep upstream default in production | [Journal](storage/journal.md) |
| [`journal_discard`](storage/journal.md#journal_discard) | `False` | Dev | Keep upstream default in production | [Journal](storage/journal.md) |
| [`journal_force_aio`](storage/journal.md#journal_force_aio) | `False` | Dev | Keep upstream default in production | [Journal](storage/journal.md) |
| [`journal_ignore_corruption`](storage/journal.md#journal_ignore_corruption) | `False` | Dev | Keep upstream default in production | [Journal](storage/journal.md) |
| [`journal_max_write_bytes`](storage/journal.md#journal_max_write_bytes) | `10_M` | Performance | Baseline → adjust → validate under load | [Journal](storage/journal.md) |
| [`journal_max_write_entries`](storage/journal.md#journal_max_write_entries) | `100` | Performance | Baseline → adjust → validate under load | [Journal](storage/journal.md) |
| [`journal_replay_from`](storage/journal.md#journal_replay_from) | `0` | Dev | Keep upstream default in production | [Journal](storage/journal.md) |
| [`journal_throttle_high_multiple`](storage/journal.md#journal_throttle_high_multiple) | `0` | Dev | Keep upstream default in production | [Journal](storage/journal.md) |
| [`journal_throttle_high_threshhold`](storage/journal.md#journal_throttle_high_threshhold) | `0.9` | Dev | Keep upstream default in production | [Journal](storage/journal.md) |
| [`journal_throttle_low_threshhold`](storage/journal.md#journal_throttle_low_threshhold) | `0.6` | Dev | Keep upstream default in production | [Journal](storage/journal.md) |
| [`journal_throttle_max_multiple`](storage/journal.md#journal_throttle_max_multiple) | `0` | Dev | Keep upstream default in production | [Journal](storage/journal.md) |
| [`journal_write_header_frequency`](storage/journal.md#journal_write_header_frequency) | `0` | Dev | Keep upstream default in production | [Journal](storage/journal.md) |
| [`journal_zero_on_create`](storage/journal.md#journal_zero_on_create) | `False` | Dev | Keep upstream default in production | [Journal](storage/journal.md) |
| [`journaler_prefetch_periods`](storage/journaler.md#journaler_prefetch_periods) | `10` | Performance | Stay within documented bounds | [Journaler](storage/journaler.md) |
| [`journaler_prezero_periods`](storage/journaler.md#journaler_prezero_periods) | `5` | Performance | Stay within documented bounds | [Journaler](storage/journaler.md) |
| [`journaler_write_head_interval`](storage/journaler.md#journaler_write_head_interval) | `15` | Performance | Baseline → adjust → validate under load | [Journaler](storage/journaler.md) |
| [`key`](auth/key.md#key) | `(empty)` | Performance | Baseline → adjust → validate under load | [Key](auth/key.md) |
| [`keyfile`](auth/keyfile.md#keyfile) | `(empty)` | Performance | Baseline → adjust → validate under load | [Keyfile](auth/keyfile.md) |
| [`keyring`](auth/keyring.md#keyring) | `0` | Performance | Baseline → adjust → validate under load | [Keyring](auth/keyring.md) |
| [`librados_thread_count`](runtime/librados.md#librados_thread_count) | `2` | Performance | Stay within documented bounds | [Librados](runtime/librados.md) |
| [`lockdep`](debug/lockdep.md#lockdep) | `False` | Dev | Keep upstream default in production | [Lockdep](debug/lockdep.md) |
| [`lockdep_force_backtrace`](debug/lockdep.md#lockdep_force_backtrace) | `False` | Dev | Keep upstream default in production | [Lockdep](debug/lockdep.md) |
| [`log_coarse_timestamps`](debug/log.md#log_coarse_timestamps) | `True` | Performance | Enable/disable based on measured need | [Log](debug/log.md) |
| [`log_file`](debug/log.md#log_file) | `/var/log/ceph/$cluster-$name.log` | Capacity | Match filesystem layout and capacity plan | [Log](debug/log.md) |
| [`log_flush_on_exit`](debug/log.md#log_flush_on_exit) | `False` | Performance | Enable/disable based on measured need | [Log](debug/log.md) |
| [`log_graylog_host`](debug/log.md#log_graylog_host) | `127.0.0.1` | Policy | Align with security and compatibility policy | [Log](debug/log.md) |
| [`log_graylog_port`](debug/log.md#log_graylog_port) | `12201` | Policy | Align with security and compatibility policy | [Log](debug/log.md) |
| [`log_max_new`](debug/log.md#log_max_new) | `1000` | Performance | Baseline → adjust → validate under load | [Log](debug/log.md) |
| [`log_max_recent`](debug/log.md#log_max_recent) | `10000` | Performance | Stay within documented bounds | [Log](debug/log.md) |
| [`log_stderr_prefix`](debug/log.md#log_stderr_prefix) | `(empty)` | Performance | Baseline → adjust → validate under load | [Log](debug/log.md) |
| [`log_stop_at_utilization`](debug/log.md#log_stop_at_utilization) | `0.97` | Policy | Align with security and compatibility policy | [Log](debug/log.md) |
| [`log_to_file`](debug/log.md#log_to_file) | `True` | Capacity | Match filesystem layout and capacity plan | [Log](debug/log.md) |
| [`log_to_graylog`](debug/log.md#log_to_graylog) | `False` | Policy | Align with security and compatibility policy | [Log](debug/log.md) |
| [`log_to_journald`](debug/log.md#log_to_journald) | `False` | Policy | Align with security and compatibility policy | [Log](debug/log.md) |
| [`log_to_stderr`](debug/log.md#log_to_stderr) | `False` | Policy | Align with security and compatibility policy | [Log](debug/log.md) |
| [`log_to_syslog`](debug/log.md#log_to_syslog) | `False` | Policy | Align with security and compatibility policy | [Log](debug/log.md) |
| [`max_rotating_auth_attempts`](runtime/max.md#max_rotating_auth_attempts) | `10` | Performance | Baseline → adjust → validate under load | [Max](runtime/max.md) |
| [`mempool_debug`](runtime/mempool.md#mempool_debug) | `False` | Dev | Keep upstream default in production | [Mempool](runtime/mempool.md) |
| [`memstore_debug_omit_block_device_write`](storage/memstore.md#memstore_debug_omit_block_device_write) | `False` | Dev | Keep upstream default in production | [Memstore](storage/memstore.md) |
| [`memstore_device_bytes`](storage/memstore.md#memstore_device_bytes) | `1_G` | Performance | Baseline → adjust → validate under load | [Memstore](storage/memstore.md) |
| [`memstore_page_set`](storage/memstore.md#memstore_page_set) | `False` | Performance | Enable/disable based on measured need | [Memstore](storage/memstore.md) |
| [`memstore_page_size`](storage/memstore.md#memstore_page_size) | `64_K` | Performance | Baseline → adjust → validate under load | [Memstore](storage/memstore.md) |
| [`mgr_client_service_daemon_unregister_timeout`](cluster/mgr.md#mgr_client_service_daemon_unregister_timeout) | `1` | Dev | Keep upstream default in production | [Mgr](cluster/mgr.md) |
| [`mgr_connect_retry_interval`](cluster/mgr.md#mgr_connect_retry_interval) | `1` | Dev | Keep upstream default in production | [Mgr](cluster/mgr.md) |
| [`mgr_enable_op_tracker`](cluster/mgr.md#mgr_enable_op_tracker) | `True` | Policy | Align with security and compatibility policy | [Mgr](cluster/mgr.md) |
| [`mgr_map_cache_enabled`](cluster/mgr.md#mgr_map_cache_enabled) | `True` | Dev | Keep upstream default in production | [Mgr](cluster/mgr.md) |
| [`mgr_num_op_tracker_shard`](cluster/mgr.md#mgr_num_op_tracker_shard) | `32` | Performance | Baseline → adjust → validate under load | [Mgr](cluster/mgr.md) |
| [`mgr_op_complaint_time`](cluster/mgr.md#mgr_op_complaint_time) | `30` | Performance | Baseline → adjust → validate under load | [Mgr](cluster/mgr.md) |
| [`mgr_op_history_duration`](cluster/mgr.md#mgr_op_history_duration) | `600` | Performance | Baseline → adjust → validate under load | [Mgr](cluster/mgr.md) |
| [`mgr_op_history_size`](cluster/mgr.md#mgr_op_history_size) | `20` | Performance | Baseline → adjust → validate under load | [Mgr](cluster/mgr.md) |
| [`mgr_op_history_slow_op_size`](cluster/mgr.md#mgr_op_history_slow_op_size) | `20` | Performance | Baseline → adjust → validate under load | [Mgr](cluster/mgr.md) |
| [`mgr_op_history_slow_op_threshold`](cluster/mgr.md#mgr_op_history_slow_op_threshold) | `10` | Performance | Baseline → adjust → validate under load | [Mgr](cluster/mgr.md) |
| [`mgr_op_log_threshold`](cluster/mgr.md#mgr_op_log_threshold) | `5` | Performance | Baseline → adjust → validate under load | [Mgr](cluster/mgr.md) |
| [`mon_allow_pool_delete`](cluster/mon.md#mon_allow_pool_delete) | `False` | Policy | Align with security and compatibility policy | [Mon](cluster/mon.md) |
| [`mon_client_bytes`](cluster/mon.md#mon_client_bytes) | `100_M` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_client_directed_command_retry`](cluster/mon.md#mon_client_directed_command_retry) | `2` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_client_hunt_interval`](cluster/mon.md#mon_client_hunt_interval) | `3` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_client_hunt_interval_backoff`](cluster/mon.md#mon_client_hunt_interval_backoff) | `1.5` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_client_hunt_interval_max_multiple`](cluster/mon.md#mon_client_hunt_interval_max_multiple) | `10` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_client_hunt_interval_min_multiple`](cluster/mon.md#mon_client_hunt_interval_min_multiple) | `1` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_client_hunt_on_resend`](cluster/mon.md#mon_client_hunt_on_resend) | `True` | Performance | Enable/disable based on measured need | [Mon](cluster/mon.md) |
| [`mon_client_hunt_parallel`](cluster/mon.md#mon_client_hunt_parallel) | `3` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_client_log_interval`](cluster/mon.md#mon_client_log_interval) | `1` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_client_max_log_entries_per_message`](cluster/mon.md#mon_client_max_log_entries_per_message) | `1000` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_client_ping_interval`](cluster/mon.md#mon_client_ping_interval) | `10` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_client_ping_timeout`](cluster/mon.md#mon_client_ping_timeout) | `30` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_client_target_rank`](cluster/mon.md#mon_client_target_rank) | `-1` | Performance | Stay within documented bounds | [Mon](cluster/mon.md) |
| [`mon_config_key_max_entry_size`](cluster/mon.md#mon_config_key_max_entry_size) | `64_K` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_debug_block_osdmap_trim`](cluster/mon.md#mon_debug_block_osdmap_trim) | `False` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_debug_deprecated_as_obsolete`](cluster/mon.md#mon_debug_deprecated_as_obsolete) | `False` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_debug_dump_json`](cluster/mon.md#mon_debug_dump_json) | `False` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_debug_dump_location`](cluster/mon.md#mon_debug_dump_location) | `/var/log/ceph/$cluster-$name.tdump` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_debug_dump_transactions`](cluster/mon.md#mon_debug_dump_transactions) | `False` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_debug_extra_checks`](cluster/mon.md#mon_debug_extra_checks) | `False` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_debug_no_initial_persistent_features`](cluster/mon.md#mon_debug_no_initial_persistent_features) | `False` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_debug_no_require_bluestore_for_ec_overwrites`](cluster/mon.md#mon_debug_no_require_bluestore_for_ec_overwrites) | `False` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_debug_no_require_tentacle`](cluster/mon.md#mon_debug_no_require_tentacle) | `False` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_debug_no_require_umbrella`](cluster/mon.md#mon_debug_no_require_umbrella) | `False` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_debug_unsafe_allow_tier_with_nonempty_snaps`](cluster/mon.md#mon_debug_unsafe_allow_tier_with_nonempty_snaps) | `False` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_dns_srv_name`](cluster/mon.md#mon_dns_srv_name) | `ceph-mon` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_fake_pool_delete`](cluster/mon.md#mon_fake_pool_delete) | `False` | Performance | Enable/disable based on measured need | [Mon](cluster/mon.md) |
| [`mon_force_quorum_join`](cluster/mon.md#mon_force_quorum_join) | `False` | Performance | Enable/disable based on measured need | [Mon](cluster/mon.md) |
| [`mon_globalid_prealloc`](cluster/mon.md#mon_globalid_prealloc) | `10000` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_host`](cluster/mon.md#mon_host) | `(empty)` | Policy | Align with security and compatibility policy | [Mon](cluster/mon.md) |
| [`mon_host_override`](cluster/mon.md#mon_host_override) | `(empty)` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_initial_members`](cluster/mon.md#mon_initial_members) | `(empty)` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_inject_pg_merge_bounce_probability`](cluster/mon.md#mon_inject_pg_merge_bounce_probability) | `0` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_inject_sync_get_chunk_delay`](cluster/mon.md#mon_inject_sync_get_chunk_delay) | `0` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_inject_transaction_delay_max`](cluster/mon.md#mon_inject_transaction_delay_max) | `10` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_inject_transaction_delay_probability`](cluster/mon.md#mon_inject_transaction_delay_probability) | `0` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_keyvaluedb`](cluster/mon.md#mon_keyvaluedb) | `rocksdb` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_max_log_epochs`](cluster/mon.md#mon_max_log_epochs) | `500` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_max_mdsmap_epochs`](cluster/mon.md#mon_max_mdsmap_epochs) | `500` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_max_mgrmap_epochs`](cluster/mon.md#mon_max_mgrmap_epochs) | `500` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_max_nvmeof_epochs`](cluster/mon.md#mon_max_nvmeof_epochs) | `500` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_max_osd`](cluster/mon.md#mon_max_osd) | `10000` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_max_pg_per_osd`](cluster/mon.md#mon_max_pg_per_osd) | `500` | Performance | Stay within documented bounds | [Mon](cluster/mon.md) |
| [`mon_max_snap_prune_per_epoch`](cluster/mon.md#mon_max_snap_prune_per_epoch) | `100` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_min_osdmap_epochs`](cluster/mon.md#mon_min_osdmap_epochs) | `500` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_osd_backfillfull_ratio`](cluster/mon.md#mon_osd_backfillfull_ratio) | `0.9` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_osd_force_trim_to`](cluster/mon.md#mon_osd_force_trim_to) | `0` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_osd_full_ratio`](cluster/mon.md#mon_osd_full_ratio) | `0.95` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_osd_initial_require_min_compat_client`](cluster/mon.md#mon_osd_initial_require_min_compat_client) | `luminous` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_osd_min_down_reporters`](cluster/mon.md#mon_osd_min_down_reporters) | `2` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_osd_nearfull_ratio`](cluster/mon.md#mon_osd_nearfull_ratio) | `0.85` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_osd_report_timeout`](cluster/mon.md#mon_osd_report_timeout) | `15_min` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_osd_reporter_subtree_level`](cluster/mon.md#mon_osd_reporter_subtree_level) | `host` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_osd_snap_trim_queue_warn_on`](cluster/mon.md#mon_osd_snap_trim_queue_warn_on) | `32768` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_probe_timeout`](cluster/mon.md#mon_probe_timeout) | `2` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_scrub_inject_crc_mismatch`](cluster/mon.md#mon_scrub_inject_crc_mismatch) | `0` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_scrub_inject_missing_keys`](cluster/mon.md#mon_scrub_inject_missing_keys) | `0` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_scrub_interval`](cluster/mon.md#mon_scrub_interval) | `1_day` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_scrub_max_keys`](cluster/mon.md#mon_scrub_max_keys) | `100` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_scrub_timeout`](cluster/mon.md#mon_scrub_timeout) | `5_min` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_sync_debug`](cluster/mon.md#mon_sync_debug) | `False` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_sync_max_payload_keys`](cluster/mon.md#mon_sync_max_payload_keys) | `2000` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_sync_max_payload_size`](cluster/mon.md#mon_sync_max_payload_size) | `1_M` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_sync_provider_kill_at`](cluster/mon.md#mon_sync_provider_kill_at) | `0` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_sync_requester_kill_at`](cluster/mon.md#mon_sync_requester_kill_at) | `0` | Dev | Keep upstream default in production | [Mon](cluster/mon.md) |
| [`mon_sync_timeout`](cluster/mon.md#mon_sync_timeout) | `1_min` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_warn_on_insecure_global_id_reclaim`](cluster/mon.md#mon_warn_on_insecure_global_id_reclaim) | `True` | Performance | Enable/disable based on measured need | [Mon](cluster/mon.md) |
| [`mon_warn_on_insecure_global_id_reclaim_allowed`](cluster/mon.md#mon_warn_on_insecure_global_id_reclaim_allowed) | `True` | Policy | Align with security and compatibility policy | [Mon](cluster/mon.md) |
| [`mon_warn_on_msgr2_not_enabled`](cluster/mon.md#mon_warn_on_msgr2_not_enabled) | `True` | Policy | Align with security and compatibility policy | [Mon](cluster/mon.md) |
| [`mon_warn_on_slow_ping_ratio`](cluster/mon.md#mon_warn_on_slow_ping_ratio) | `0.05` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_warn_on_slow_ping_time`](cluster/mon.md#mon_warn_on_slow_ping_time) | `0` | Performance | Baseline → adjust → validate under load | [Mon](cluster/mon.md) |
| [`mon_warn_pg_not_deep_scrubbed_ratio`](cluster/mon.md#mon_warn_pg_not_deep_scrubbed_ratio) | `0.75` | Performance | Stay within documented bounds | [Mon](cluster/mon.md) |
| [`mon_warn_pg_not_scrubbed_ratio`](cluster/mon.md#mon_warn_pg_not_scrubbed_ratio) | `0.5` | Performance | Stay within documented bounds | [Mon](cluster/mon.md) |
| [`monmap`](cluster/monmap.md#monmap) | `(empty)` | Performance | Baseline → adjust → validate under load | [Monmap](cluster/monmap.md) |
| [`ms_async_op_threads`](network/ms.md#ms_async_op_threads) | `3` | Performance | Stay within documented bounds | [Ms](network/ms.md) |
| [`ms_async_rdma_buffer_size`](network/ms.md#ms_async_rdma_buffer_size) | `128_K` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_async_rdma_cm`](network/ms.md#ms_async_rdma_cm) | `False` | Performance | Enable/disable based on measured need | [Ms](network/ms.md) |
| [`ms_async_rdma_device_name`](network/ms.md#ms_async_rdma_device_name) | `(empty)` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_async_rdma_dscp`](network/ms.md#ms_async_rdma_dscp) | `96` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_async_rdma_enable_hugepage`](network/ms.md#ms_async_rdma_enable_hugepage) | `False` | Policy | Align with security and compatibility policy | [Ms](network/ms.md) |
| [`ms_async_rdma_gid_idx`](network/ms.md#ms_async_rdma_gid_idx) | `0` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_async_rdma_local_gid`](network/ms.md#ms_async_rdma_local_gid) | `(empty)` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_async_rdma_polling_us`](network/ms.md#ms_async_rdma_polling_us) | `1000` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_async_rdma_port_num`](network/ms.md#ms_async_rdma_port_num) | `1` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_async_rdma_receive_buffers`](network/ms.md#ms_async_rdma_receive_buffers) | `32_K` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_async_rdma_receive_queue_len`](network/ms.md#ms_async_rdma_receive_queue_len) | `4_K` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_async_rdma_roce_ver`](network/ms.md#ms_async_rdma_roce_ver) | `1` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_async_rdma_send_buffers`](network/ms.md#ms_async_rdma_send_buffers) | `1_K` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_async_rdma_sl`](network/ms.md#ms_async_rdma_sl) | `3` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_async_rdma_support_srq`](network/ms.md#ms_async_rdma_support_srq) | `True` | Performance | Enable/disable based on measured need | [Ms](network/ms.md) |
| [`ms_async_rdma_type`](network/ms.md#ms_async_rdma_type) | `ib` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_async_reap_threshold`](network/ms.md#ms_async_reap_threshold) | `5` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_bind_before_connect`](network/ms.md#ms_bind_before_connect) | `False` | Performance | Enable/disable based on measured need | [Ms](network/ms.md) |
| [`ms_bind_ipv4`](network/ms.md#ms_bind_ipv4) | `True` | Performance | Enable/disable based on measured need | [Ms](network/ms.md) |
| [`ms_bind_ipv6`](network/ms.md#ms_bind_ipv6) | `False` | Performance | Enable/disable based on measured need | [Ms](network/ms.md) |
| [`ms_bind_msgr1`](network/ms.md#ms_bind_msgr1) | `True` | Performance | Enable/disable based on measured need | [Ms](network/ms.md) |
| [`ms_bind_msgr2`](network/ms.md#ms_bind_msgr2) | `True` | Performance | Enable/disable based on measured need | [Ms](network/ms.md) |
| [`ms_bind_port_max`](network/ms.md#ms_bind_port_max) | `7568` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_bind_port_min`](network/ms.md#ms_bind_port_min) | `6800` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_bind_prefer_ipv4`](network/ms.md#ms_bind_prefer_ipv4) | `False` | Performance | Enable/disable based on measured need | [Ms](network/ms.md) |
| [`ms_bind_retry_count`](network/ms.md#ms_bind_retry_count) | `0` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_bind_retry_delay`](network/ms.md#ms_bind_retry_delay) | `0` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_blackhole_client`](network/ms.md#ms_blackhole_client) | `False` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_blackhole_mds`](network/ms.md#ms_blackhole_mds) | `False` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_blackhole_mgr`](network/ms.md#ms_blackhole_mgr) | `False` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_blackhole_mon`](network/ms.md#ms_blackhole_mon) | `False` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_blackhole_osd`](network/ms.md#ms_blackhole_osd) | `False` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_client_mode`](network/ms.md#ms_client_mode) | `crc secure` | Policy | Align with security and compatibility policy | [Ms](network/ms.md) |
| [`ms_client_throttle_retry_time_interval`](network/ms.md#ms_client_throttle_retry_time_interval) | `5000` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_cluster_mode`](network/ms.md#ms_cluster_mode) | `crc secure` | Policy | Align with security and compatibility policy | [Ms](network/ms.md) |
| [`ms_cluster_type`](network/ms.md#ms_cluster_type) | `(empty)` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_compress_secure`](network/ms.md#ms_compress_secure) | `False` | Performance | Enable/disable based on measured need | [Ms](network/ms.md) |
| [`ms_connection_idle_timeout`](network/ms.md#ms_connection_idle_timeout) | `900` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_connection_ready_timeout`](network/ms.md#ms_connection_ready_timeout) | `10` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_crc_data`](network/ms.md#ms_crc_data) | `True` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_crc_header`](network/ms.md#ms_crc_header) | `True` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_die_on_bad_msg`](network/ms.md#ms_die_on_bad_msg) | `False` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_die_on_bug`](network/ms.md#ms_die_on_bug) | `False` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_die_on_old_message`](network/ms.md#ms_die_on_old_message) | `False` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_die_on_skipped_message`](network/ms.md#ms_die_on_skipped_message) | `False` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_die_on_unhandled_msg`](network/ms.md#ms_die_on_unhandled_msg) | `False` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_dispatch_throttle_bytes`](network/ms.md#ms_dispatch_throttle_bytes) | `100_M` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_dpdk_coremask`](network/ms.md#ms_dpdk_coremask) | `0xF` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_dpdk_debug_allow_loopback`](network/ms.md#ms_dpdk_debug_allow_loopback) | `False` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_dpdk_devs_allowlist`](network/ms.md#ms_dpdk_devs_allowlist) | `(empty)` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_dpdk_enable_tso`](network/ms.md#ms_dpdk_enable_tso) | `True` | Policy | Align with security and compatibility policy | [Ms](network/ms.md) |
| [`ms_dpdk_gateway_ipv4_addr`](network/ms.md#ms_dpdk_gateway_ipv4_addr) | `(empty)` | Connectivity | Use nearest stable endpoint | [Ms](network/ms.md) |
| [`ms_dpdk_host_ipv4_addr`](network/ms.md#ms_dpdk_host_ipv4_addr) | `(empty)` | Connectivity | Use nearest stable endpoint | [Ms](network/ms.md) |
| [`ms_dpdk_hugepages`](network/ms.md#ms_dpdk_hugepages) | `(empty)` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_dpdk_hw_flow_control`](network/ms.md#ms_dpdk_hw_flow_control) | `True` | Performance | Enable/disable based on measured need | [Ms](network/ms.md) |
| [`ms_dpdk_hw_queue_weight`](network/ms.md#ms_dpdk_hw_queue_weight) | `1` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_dpdk_lro`](network/ms.md#ms_dpdk_lro) | `True` | Performance | Enable/disable based on measured need | [Ms](network/ms.md) |
| [`ms_dpdk_memory_channel`](network/ms.md#ms_dpdk_memory_channel) | `4` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_dpdk_netmask_ipv4_addr`](network/ms.md#ms_dpdk_netmask_ipv4_addr) | `(empty)` | Connectivity | Use nearest stable endpoint | [Ms](network/ms.md) |
| [`ms_dpdk_pmd`](network/ms.md#ms_dpdk_pmd) | `(empty)` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_dpdk_port_id`](network/ms.md#ms_dpdk_port_id) | `0` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_dpdk_rx_buffer_count_per_core`](network/ms.md#ms_dpdk_rx_buffer_count_per_core) | `8192` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_dump_corrupt_message_level`](network/ms.md#ms_dump_corrupt_message_level) | `1` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_dump_on_send`](network/ms.md#ms_dump_on_send) | `False` | Performance | Enable/disable based on measured need | [Ms](network/ms.md) |
| [`ms_initial_backoff`](network/ms.md#ms_initial_backoff) | `0.2` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_inject_delay_max`](network/ms.md#ms_inject_delay_max) | `1` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_inject_delay_probability`](network/ms.md#ms_inject_delay_probability) | `0` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_inject_delay_type`](network/ms.md#ms_inject_delay_type) | `(empty)` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_inject_internal_delays`](network/ms.md#ms_inject_internal_delays) | `0` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_inject_network_congestion`](network/ms.md#ms_inject_network_congestion) | `0` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_inject_socket_failures`](network/ms.md#ms_inject_socket_failures) | `0` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_learn_addr_from_peer`](network/ms.md#ms_learn_addr_from_peer) | `True` | Performance | Enable/disable based on measured need | [Ms](network/ms.md) |
| [`ms_max_accept_failures`](network/ms.md#ms_max_accept_failures) | `4` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_max_backoff`](network/ms.md#ms_max_backoff) | `15` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_mon_client_mode`](network/ms.md#ms_mon_client_mode) | `secure crc` | Policy | Align with security and compatibility policy | [Ms](network/ms.md) |
| [`ms_mon_cluster_mode`](network/ms.md#ms_mon_cluster_mode) | `secure crc` | Policy | Align with security and compatibility policy | [Ms](network/ms.md) |
| [`ms_mon_service_mode`](network/ms.md#ms_mon_service_mode) | `secure crc` | Policy | Align with security and compatibility policy | [Ms](network/ms.md) |
| [`ms_osd_compress_min_size`](network/ms.md#ms_osd_compress_min_size) | `1_K` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_osd_compress_mode`](network/ms.md#ms_osd_compress_mode) | `none` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_osd_compression_algorithm`](network/ms.md#ms_osd_compression_algorithm) | `snappy` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_pq_max_tokens_per_priority`](network/ms.md#ms_pq_max_tokens_per_priority) | `16_M` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_pq_min_cost`](network/ms.md#ms_pq_min_cost) | `64_K` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_public_type`](network/ms.md#ms_public_type) | `(empty)` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_service_mode`](network/ms.md#ms_service_mode) | `crc secure` | Policy | Align with security and compatibility policy | [Ms](network/ms.md) |
| [`ms_tcp_listen_backlog`](network/ms.md#ms_tcp_listen_backlog) | `512` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_tcp_nodelay`](network/ms.md#ms_tcp_nodelay) | `True` | Performance | Enable/disable based on measured need | [Ms](network/ms.md) |
| [`ms_tcp_prefetch_max_size`](network/ms.md#ms_tcp_prefetch_max_size) | `64_K` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_tcp_rcvbuf`](network/ms.md#ms_tcp_rcvbuf) | `0` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`ms_time_events_min_wait_interval`](network/ms.md#ms_time_events_min_wait_interval) | `1000` | Dev | Keep upstream default in production | [Ms](network/ms.md) |
| [`ms_type`](network/ms.md#ms_type) | `async+posix` | Performance | Baseline → adjust → validate under load | [Ms](network/ms.md) |
| [`no_config_file`](runtime/no.md#no_config_file) | `False` | Capacity | Match filesystem layout and capacity plan | [No](runtime/no.md) |
| [`objecter_completion_locks_per_session`](network/objecter.md#objecter_completion_locks_per_session) | `32` | Dev | Keep upstream default in production | [Objecter](network/objecter.md) |
| [`objecter_debug_inject_relock_delay`](network/objecter.md#objecter_debug_inject_relock_delay) | `False` | Dev | Keep upstream default in production | [Objecter](network/objecter.md) |
| [`objecter_inflight_op_bytes`](network/objecter.md#objecter_inflight_op_bytes) | `100_M` | Performance | Baseline → adjust → validate under load | [Objecter](network/objecter.md) |
| [`objecter_inflight_ops`](network/objecter.md#objecter_inflight_ops) | `1_K` | Performance | Baseline → adjust → validate under load | [Objecter](network/objecter.md) |
| [`objecter_inject_no_watch_ping`](network/objecter.md#objecter_inject_no_watch_ping) | `False` | Dev | Keep upstream default in production | [Objecter](network/objecter.md) |
| [`objecter_retry_writes_after_first_reply`](network/objecter.md#objecter_retry_writes_after_first_reply) | `False` | Dev | Keep upstream default in production | [Objecter](network/objecter.md) |
| [`objecter_tick_interval`](network/objecter.md#objecter_tick_interval) | `5` | Dev | Keep upstream default in production | [Objecter](network/objecter.md) |
| [`objecter_timeout`](network/objecter.md#objecter_timeout) | `10` | Performance | Baseline → adjust → validate under load | [Objecter](network/objecter.md) |
| [`objectstore_blackhole`](storage/objectstore.md#objectstore_blackhole) | `False` | Performance | Enable/disable based on measured need | [Objectstore](storage/objectstore.md) |
| [`objectstore_debug_throw_on_failed_txc`](storage/objectstore.md#objectstore_debug_throw_on_failed_txc) | `False` | Dev | Keep upstream default in production | [Objectstore](storage/objectstore.md) |
| [`openssl_conf`](runtime/openssl.md#openssl_conf) | `(empty)` | Performance | Baseline → adjust → validate under load | [Openssl](runtime/openssl.md) |
| [`osd_asio_thread_count`](cluster/osd.md#osd_asio_thread_count) | `2` | Performance | Stay within documented bounds | [Osd](cluster/osd.md) |
| [`osd_async_recovery_min_cost`](cluster/osd.md#osd_async_recovery_min_cost) | `100` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_auto_mark_unfound_lost`](cluster/osd.md#osd_auto_mark_unfound_lost) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_backoff_on_degraded`](cluster/osd.md#osd_backoff_on_degraded) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_backoff_on_peering`](cluster/osd.md#osd_backoff_on_peering) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_backoff_on_unfound`](cluster/osd.md#osd_backoff_on_unfound) | `True` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_beacon_report_interval`](cluster/osd.md#osd_beacon_report_interval) | `5_min` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_bench_duration`](cluster/osd.md#osd_bench_duration) | `30` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_bench_large_size_max_throughput`](cluster/osd.md#osd_bench_large_size_max_throughput) | `100_M` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_bench_max_block_size`](cluster/osd.md#osd_bench_max_block_size) | `64_M` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_bench_small_size_max_iops`](cluster/osd.md#osd_bench_small_size_max_iops) | `100` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_blkin_trace_all`](cluster/osd.md#osd_blkin_trace_all) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_calc_pg_upmaps_aggressively`](cluster/osd.md#osd_calc_pg_upmaps_aggressively) | `True` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_calc_pg_upmaps_aggressively_fast`](cluster/osd.md#osd_calc_pg_upmaps_aggressively_fast) | `True` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_calc_pg_upmaps_local_fallback_retries`](cluster/osd.md#osd_calc_pg_upmaps_local_fallback_retries) | `100` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_check_for_log_corruption`](cluster/osd.md#osd_check_for_log_corruption) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_client_op_priority`](cluster/osd.md#osd_client_op_priority) | `63` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_command_max_records`](cluster/osd.md#osd_command_max_records) | `256` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_crush_chooseleaf_type`](cluster/osd.md#osd_crush_chooseleaf_type) | `1` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_crash_on_ignored_backoff`](cluster/osd.md#osd_debug_crash_on_ignored_backoff) | `False` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_deep_scrub_sleep`](cluster/osd.md#osd_debug_deep_scrub_sleep) | `0` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_drop_ping_duration`](cluster/osd.md#osd_debug_drop_ping_duration) | `0` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_drop_ping_probability`](cluster/osd.md#osd_debug_drop_ping_probability) | `0` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_inject_copyfrom_error`](cluster/osd.md#osd_debug_inject_copyfrom_error) | `False` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_inject_dispatch_delay_duration`](cluster/osd.md#osd_debug_inject_dispatch_delay_duration) | `0.1` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_inject_dispatch_delay_probability`](cluster/osd.md#osd_debug_inject_dispatch_delay_probability) | `0` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_misdirected_ops`](cluster/osd.md#osd_debug_misdirected_ops) | `False` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_no_acting_change`](cluster/osd.md#osd_debug_no_acting_change) | `False` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_no_purge_strays`](cluster/osd.md#osd_debug_no_purge_strays) | `False` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_op_order`](cluster/osd.md#osd_debug_op_order) | `False` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_pg_log_writeout`](cluster/osd.md#osd_debug_pg_log_writeout) | `False` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_pretend_recovery_active`](cluster/osd.md#osd_debug_pretend_recovery_active) | `False` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_random_push_read_error`](cluster/osd.md#osd_debug_random_push_read_error) | `0` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_reject_backfill_probability`](cluster/osd.md#osd_debug_reject_backfill_probability) | `0` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_shutdown`](cluster/osd.md#osd_debug_shutdown) | `False` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_skip_full_check_in_backfill_reservation`](cluster/osd.md#osd_debug_skip_full_check_in_backfill_reservation) | `False` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_skip_full_check_in_recovery`](cluster/osd.md#osd_debug_skip_full_check_in_recovery) | `False` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_verify_cached_snaps`](cluster/osd.md#osd_debug_verify_cached_snaps) | `False` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_verify_missing_on_start`](cluster/osd.md#osd_debug_verify_missing_on_start) | `False` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_verify_snaps`](cluster/osd.md#osd_debug_verify_snaps) | `False` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_debug_verify_stray_on_activate`](cluster/osd.md#osd_debug_verify_stray_on_activate) | `False` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_default_data_pool_replay_window`](cluster/osd.md#osd_default_data_pool_replay_window) | `45` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_default_notify_timeout`](cluster/osd.md#osd_default_notify_timeout) | `30` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_discard_disconnected_ops`](cluster/osd.md#osd_discard_disconnected_ops) | `True` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_enable_op_tracker`](cluster/osd.md#osd_enable_op_tracker) | `True` | Policy | Align with security and compatibility policy | [Osd](cluster/osd.md) |
| [`osd_erasure_code_plugins`](cluster/osd.md#osd_erasure_code_plugins) | `0` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_failsafe_full_ratio`](cluster/osd.md#osd_failsafe_full_ratio) | `0.97` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_fast_fail_on_connection_refused`](cluster/osd.md#osd_fast_fail_on_connection_refused) | `True` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_fast_info`](cluster/osd.md#osd_fast_info) | `True` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_fast_shutdown`](cluster/osd.md#osd_fast_shutdown) | `True` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_fast_shutdown_notify_mon`](cluster/osd.md#osd_fast_shutdown_notify_mon) | `True` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_fast_shutdown_timeout`](cluster/osd.md#osd_fast_shutdown_timeout) | `15` | Performance | Stay within documented bounds | [Osd](cluster/osd.md) |
| [`osd_force_auth_primary_missing_objects`](cluster/osd.md#osd_force_auth_primary_missing_objects) | `100` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_force_recovery_pg_log_entries_factor`](cluster/osd.md#osd_force_recovery_pg_log_entries_factor) | `1.3` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_function_tracing`](cluster/osd.md#osd_function_tracing) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_heartbeat_grace`](cluster/osd.md#osd_heartbeat_grace) | `20` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_heartbeat_interval`](cluster/osd.md#osd_heartbeat_interval) | `6` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_heartbeat_min_healthy_ratio`](cluster/osd.md#osd_heartbeat_min_healthy_ratio) | `0.33` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_heartbeat_min_size`](cluster/osd.md#osd_heartbeat_min_size) | `2000` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_heartbeat_stale`](cluster/osd.md#osd_heartbeat_stale) | `10_min` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_heartbeat_use_min_delay_socket`](cluster/osd.md#osd_heartbeat_use_min_delay_socket) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_hit_set_max_size`](cluster/osd.md#osd_hit_set_max_size) | `100000` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_hit_set_min_size`](cluster/osd.md#osd_hit_set_min_size) | `1000` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_hit_set_namespace`](cluster/osd.md#osd_hit_set_namespace) | `.ceph-internal` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_ignore_stale_divergent_priors`](cluster/osd.md#osd_ignore_stale_divergent_priors) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_kill_backfill_at`](cluster/osd.md#osd_kill_backfill_at) | `0` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_loop_before_reset_tphandle`](cluster/osd.md#osd_loop_before_reset_tphandle) | `64` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_map_dedup`](cluster/osd.md#osd_map_dedup) | `True` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_map_message_max`](cluster/osd.md#osd_map_message_max) | `40` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_map_message_max_bytes`](cluster/osd.md#osd_map_message_max_bytes) | `10_M` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_max_attr_name_len`](cluster/osd.md#osd_max_attr_name_len) | `100` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_max_attr_size`](cluster/osd.md#osd_max_attr_size) | `0` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_max_object_name_len`](cluster/osd.md#osd_max_object_name_len) | `2_K` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_max_object_namespace_len`](cluster/osd.md#osd_max_object_namespace_len) | `256` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_max_object_size`](cluster/osd.md#osd_max_object_size) | `128_M` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_max_omap_bytes_per_request`](cluster/osd.md#osd_max_omap_bytes_per_request) | `1_G` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_max_omap_entries_per_request`](cluster/osd.md#osd_max_omap_entries_per_request) | `1_K` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_max_pg_blocked_by`](cluster/osd.md#osd_max_pg_blocked_by) | `16` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_max_pg_log_entries`](cluster/osd.md#osd_max_pg_log_entries) | `10000` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_max_pg_per_osd_hard_ratio`](cluster/osd.md#osd_max_pg_per_osd_hard_ratio) | `3` | Performance | Stay within documented bounds | [Osd](cluster/osd.md) |
| [`osd_max_snap_prune_intervals_per_epoch`](cluster/osd.md#osd_max_snap_prune_intervals_per_epoch) | `512` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_max_trimming_pgs`](cluster/osd.md#osd_max_trimming_pgs) | `2` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_max_write_op_reply_len`](cluster/osd.md#osd_max_write_op_reply_len) | `64` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_memory_base`](cluster/osd.md#osd_memory_base) | `768_M` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_memory_cache_min`](cluster/osd.md#osd_memory_cache_min) | `128_M` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_memory_cache_resize_interval`](cluster/osd.md#osd_memory_cache_resize_interval) | `1` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_memory_expected_fragmentation`](cluster/osd.md#osd_memory_expected_fragmentation) | `0.15` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_memory_target`](cluster/osd.md#osd_memory_target) | `4_G` | Policy | Align with security and compatibility policy | [Osd](cluster/osd.md) |
| [`osd_memory_target_autotune`](cluster/osd.md#osd_memory_target_autotune) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_memory_target_cgroup_limit_ratio`](cluster/osd.md#osd_memory_target_cgroup_limit_ratio) | `0.8` | Performance | Stay within documented bounds | [Osd](cluster/osd.md) |
| [`osd_min_pg_log_entries`](cluster/osd.md#osd_min_pg_log_entries) | `250` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_min_split_replica_read_size`](cluster/osd.md#osd_min_split_replica_read_size) | `0` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_mon_heartbeat_interval`](cluster/osd.md#osd_mon_heartbeat_interval) | `30` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_mon_heartbeat_stat_stale`](cluster/osd.md#osd_mon_heartbeat_stat_stale) | `1_hr` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_mon_report_interval`](cluster/osd.md#osd_mon_report_interval) | `5` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_mon_report_max_in_flight`](cluster/osd.md#osd_mon_report_max_in_flight) | `2` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_mon_shutdown_timeout`](cluster/osd.md#osd_mon_shutdown_timeout) | `5` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_num_op_tracker_shard`](cluster/osd.md#osd_num_op_tracker_shard) | `32` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_object_clean_region_max_num_intervals`](cluster/osd.md#osd_object_clean_region_max_num_intervals) | `10` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_objecter_finishers`](cluster/osd.md#osd_objecter_finishers) | `1` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_objectstore`](cluster/osd.md#osd_objectstore) | `bluestore` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_objectstore_fuse`](cluster/osd.md#osd_objectstore_fuse) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_objectstore_ideal_list_max`](cluster/osd.md#osd_objectstore_ideal_list_max) | `64` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_objectstore_tracing`](cluster/osd.md#osd_objectstore_tracing) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_op_complaint_time`](cluster/osd.md#osd_op_complaint_time) | `30` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_op_history_duration`](cluster/osd.md#osd_op_history_duration) | `600` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_op_history_size`](cluster/osd.md#osd_op_history_size) | `20` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_op_history_slow_op_size`](cluster/osd.md#osd_op_history_slow_op_size) | `20` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_op_history_slow_op_threshold`](cluster/osd.md#osd_op_history_slow_op_threshold) | `10` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_op_log_threshold`](cluster/osd.md#osd_op_log_threshold) | `5` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_peering_op_priority`](cluster/osd.md#osd_peering_op_priority) | `255` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_pg_delete_cost`](cluster/osd.md#osd_pg_delete_cost) | `1_M` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pg_delete_priority`](cluster/osd.md#osd_pg_delete_priority) | `5` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pg_epoch_persisted_max_stale`](cluster/osd.md#osd_pg_epoch_persisted_max_stale) | `40` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pg_log_dups_tracked`](cluster/osd.md#osd_pg_log_dups_tracked) | `3000` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_pg_log_trim_max`](cluster/osd.md#osd_pg_log_trim_max) | `10000` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pg_log_trim_min`](cluster/osd.md#osd_pg_log_trim_min) | `100` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_pg_max_concurrent_snap_trims`](cluster/osd.md#osd_pg_max_concurrent_snap_trims) | `2` | Performance | Stay within documented bounds | [Osd](cluster/osd.md) |
| [`osd_pg_object_context_cache_count`](cluster/osd.md#osd_pg_object_context_cache_count) | `64` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pg_stat_report_interval_max_epochs`](cluster/osd.md#osd_pg_stat_report_interval_max_epochs) | `500` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pg_stat_report_interval_max_seconds`](cluster/osd.md#osd_pg_stat_report_interval_max_seconds) | `5` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pool_default_cache_max_evict_check_size`](cluster/osd.md#osd_pool_default_cache_max_evict_check_size) | `10` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pool_default_cache_min_evict_age`](cluster/osd.md#osd_pool_default_cache_min_evict_age) | `0` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pool_default_cache_min_flush_age`](cluster/osd.md#osd_pool_default_cache_min_flush_age) | `0` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pool_default_cache_target_dirty_high_ratio`](cluster/osd.md#osd_pool_default_cache_target_dirty_high_ratio) | `0.6` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pool_default_cache_target_dirty_ratio`](cluster/osd.md#osd_pool_default_cache_target_dirty_ratio) | `0.4` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pool_default_cache_target_full_ratio`](cluster/osd.md#osd_pool_default_cache_target_full_ratio) | `0.8` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pool_default_crush_rule`](cluster/osd.md#osd_pool_default_crush_rule) | `-1` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pool_default_ec_fast_read`](cluster/osd.md#osd_pool_default_ec_fast_read) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_pool_default_erasure_code_profile`](cluster/osd.md#osd_pool_default_erasure_code_profile) | `plugin=isa technique=reed_sol_van k=2 m=2` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pool_default_flag_bulk`](cluster/osd.md#osd_pool_default_flag_bulk) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_pool_default_flag_ec_optimizations`](cluster/osd.md#osd_pool_default_flag_ec_optimizations) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_pool_default_flag_hashpspool`](cluster/osd.md#osd_pool_default_flag_hashpspool) | `True` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_pool_default_flag_nodelete`](cluster/osd.md#osd_pool_default_flag_nodelete) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_pool_default_flag_nopgchange`](cluster/osd.md#osd_pool_default_flag_nopgchange) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_pool_default_flag_nosizechange`](cluster/osd.md#osd_pool_default_flag_nosizechange) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_pool_default_flags`](cluster/osd.md#osd_pool_default_flags) | `0` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_pool_default_hit_set_bloom_fpp`](cluster/osd.md#osd_pool_default_hit_set_bloom_fpp) | `0.05` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pool_default_min_size`](cluster/osd.md#osd_pool_default_min_size) | `0` | Performance | Stay within documented bounds | [Osd](cluster/osd.md) |
| [`osd_pool_default_pg_autoscale_mode`](cluster/osd.md#osd_pool_default_pg_autoscale_mode) | `on` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pool_default_pg_num`](cluster/osd.md#osd_pool_default_pg_num) | `32` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pool_default_pgp_num`](cluster/osd.md#osd_pool_default_pgp_num) | `0` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pool_default_read_lease_ratio`](cluster/osd.md#osd_pool_default_read_lease_ratio) | `0.8` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_pool_default_read_ratio`](cluster/osd.md#osd_pool_default_read_ratio) | `70` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pool_default_size`](cluster/osd.md#osd_pool_default_size) | `3` | Performance | Stay within documented bounds | [Osd](cluster/osd.md) |
| [`osd_pool_default_type`](cluster/osd.md#osd_pool_default_type) | `replicated` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_pool_use_gmt_hitset`](cluster/osd.md#osd_pool_use_gmt_hitset) | `True` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_recovery_cost`](cluster/osd.md#osd_recovery_cost) | `20_M` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_recovery_op_priority`](cluster/osd.md#osd_recovery_op_priority) | `3` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_recovery_op_warn_multiple`](cluster/osd.md#osd_recovery_op_warn_multiple) | `16` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_recovery_priority`](cluster/osd.md#osd_recovery_priority) | `5` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_requested_scrub_priority`](cluster/osd.md#osd_requested_scrub_priority) | `5` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_rollback_to_cluster_snap`](cluster/osd.md#osd_rollback_to_cluster_snap) | `(empty)` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_scrub_cost`](cluster/osd.md#osd_scrub_cost) | `50_M` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_scrub_event_cost`](cluster/osd.md#osd_scrub_event_cost) | `4_K` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_scrub_priority`](cluster/osd.md#osd_scrub_priority) | `5` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_shutdown_pgref_assert`](cluster/osd.md#osd_shutdown_pgref_assert) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_skip_check_past_interval_bounds`](cluster/osd.md#osd_skip_check_past_interval_bounds) | `False` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_snap_trim_cost`](cluster/osd.md#osd_snap_trim_cost) | `1_M` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_snap_trim_priority`](cluster/osd.md#osd_snap_trim_priority) | `5` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_target_pg_log_entries_per_osd`](cluster/osd.md#osd_target_pg_log_entries_per_osd) | `300000` | Dev | Keep upstream default in production | [Osd](cluster/osd.md) |
| [`osd_target_transaction_size`](cluster/osd.md#osd_target_transaction_size) | `30` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_tier_default_cache_hit_set_count`](cluster/osd.md#osd_tier_default_cache_hit_set_count) | `4` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_tier_default_cache_hit_set_grade_decay_rate`](cluster/osd.md#osd_tier_default_cache_hit_set_grade_decay_rate) | `20` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_tier_default_cache_hit_set_period`](cluster/osd.md#osd_tier_default_cache_hit_set_period) | `1200` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_tier_default_cache_hit_set_search_last_n`](cluster/osd.md#osd_tier_default_cache_hit_set_search_last_n) | `1` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_tier_default_cache_hit_set_type`](cluster/osd.md#osd_tier_default_cache_hit_set_type) | `bloom` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_tier_default_cache_min_read_recency_for_promote`](cluster/osd.md#osd_tier_default_cache_min_read_recency_for_promote) | `1` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_tier_default_cache_min_write_recency_for_promote`](cluster/osd.md#osd_tier_default_cache_min_write_recency_for_promote) | `1` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_tier_default_cache_mode`](cluster/osd.md#osd_tier_default_cache_mode) | `writeback` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_tier_promote_max_bytes_sec`](cluster/osd.md#osd_tier_promote_max_bytes_sec) | `5_M` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_tier_promote_max_objects_sec`](cluster/osd.md#osd_tier_promote_max_objects_sec) | `25` | Performance | Baseline → adjust → validate under load | [Osd](cluster/osd.md) |
| [`osd_tracing`](cluster/osd.md#osd_tracing) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osd_use_stale_snap`](cluster/osd.md#osd_use_stale_snap) | `False` | Performance | Enable/disable based on measured need | [Osd](cluster/osd.md) |
| [`osdc_blkin_trace_all`](network/osdc.md#osdc_blkin_trace_all) | `False` | Performance | Enable/disable based on measured need | [Osdc](network/osdc.md) |
| [`perf`](debug/perf.md#perf) | `True` | Performance | Enable/disable based on measured need | [Perf](debug/perf.md) |
| [`pid_file`](runtime/pid.md#pid_file) | `(empty)` | Capacity | Match filesystem layout and capacity plan | [Pid](runtime/pid.md) |
| [`plugin_crypto_accelerator`](runtime/plugin.md#plugin_crypto_accelerator) | `crypto_isal` | Performance | Baseline → adjust → validate under load | [Plugin](runtime/plugin.md) |
| [`plugin_dir`](runtime/plugin.md#plugin_dir) | `0` | Capacity | Match filesystem layout and capacity plan | [Plugin](runtime/plugin.md) |
| [`public_addr`](network/public.md#public_addr) | `(empty)` | Connectivity | Use nearest stable endpoint | [Public](network/public.md) |
| [`public_addrv`](network/public.md#public_addrv) | `(empty)` | Policy | Align with security and compatibility policy | [Public](network/public.md) |
| [`public_bind_addr`](network/public.md#public_bind_addr) | `(empty)` | Connectivity | Use nearest stable endpoint | [Public](network/public.md) |
| [`public_network`](network/public.md#public_network) | `(empty)` | Performance | Baseline → adjust → validate under load | [Public](network/public.md) |
| [`public_network_interface`](network/public.md#public_network_interface) | `(empty)` | Performance | Baseline → adjust → validate under load | [Public](network/public.md) |
| [`qat_compressor_busy_polling`](storage/qat.md#qat_compressor_busy_polling) | `False` | Performance | Enable/disable based on measured need | [Qat](storage/qat.md) |
| [`qat_compressor_enabled`](storage/qat.md#qat_compressor_enabled) | `False` | Policy | Align with security and compatibility policy | [Qat](storage/qat.md) |
| [`qat_compressor_session_max_number`](storage/qat.md#qat_compressor_session_max_number) | `256` | Performance | Baseline → adjust → validate under load | [Qat](storage/qat.md) |
| [`rados_mon_op_timeout`](cluster/rados.md#rados_mon_op_timeout) | `0` | Performance | Stay within documented bounds | [Rados](cluster/rados.md) |
| [`rados_osd_op_timeout`](cluster/rados.md#rados_osd_op_timeout) | `0` | Performance | Stay within documented bounds | [Rados](cluster/rados.md) |
| [`rados_replica_read_policy`](cluster/rados.md#rados_replica_read_policy) | `default` | Performance | Baseline → adjust → validate under load | [Rados](cluster/rados.md) |
| [`rados_replica_read_policy_on_objclass`](cluster/rados.md#rados_replica_read_policy_on_objclass) | `False` | Performance | Enable/disable based on measured need | [Rados](cluster/rados.md) |
| [`rados_tracing`](cluster/rados.md#rados_tracing) | `False` | Performance | Enable/disable based on measured need | [Rados](cluster/rados.md) |
| [`restapi_base_url`](runtime/restapi.md#restapi_base_url) | `(empty)` | Connectivity | Use nearest stable endpoint | [Restapi](runtime/restapi.md) |
| [`restapi_log_level`](runtime/restapi.md#restapi_log_level) | `(empty)` | Performance | Baseline → adjust → validate under load | [Restapi](runtime/restapi.md) |
| [`rocksdb_block_size`](storage/rocksdb.md#rocksdb_block_size) | `4_K` | Performance | Baseline → adjust → validate under load | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_bloom_bits_per_key`](storage/rocksdb.md#rocksdb_bloom_bits_per_key) | `20` | Performance | Baseline → adjust → validate under load | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_cache_index_and_filter_blocks`](storage/rocksdb.md#rocksdb_cache_index_and_filter_blocks) | `True` | Dev | Keep upstream default in production | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_cache_index_and_filter_blocks_with_high_priority`](storage/rocksdb.md#rocksdb_cache_index_and_filter_blocks_with_high_priority) | `False` | Dev | Keep upstream default in production | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_cache_row_ratio`](storage/rocksdb.md#rocksdb_cache_row_ratio) | `0` | Performance | Baseline → adjust → validate under load | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_cache_shard_bits`](storage/rocksdb.md#rocksdb_cache_shard_bits) | `4` | Performance | Baseline → adjust → validate under load | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_cache_size`](storage/rocksdb.md#rocksdb_cache_size) | `512_M` | Performance | Baseline → adjust → validate under load | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_cache_type`](storage/rocksdb.md#rocksdb_cache_type) | `binned_lru` | Performance | Baseline → adjust → validate under load | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_cf_compact_on_deletion`](storage/rocksdb.md#rocksdb_cf_compact_on_deletion) | `True` | Dev | Keep upstream default in production | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_cf_compact_on_deletion_sliding_window`](storage/rocksdb.md#rocksdb_cf_compact_on_deletion_sliding_window) | `32768` | Dev | Keep upstream default in production | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_cf_compact_on_deletion_trigger`](storage/rocksdb.md#rocksdb_cf_compact_on_deletion_trigger) | `16384` | Dev | Keep upstream default in production | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_collect_compaction_stats`](storage/rocksdb.md#rocksdb_collect_compaction_stats) | `False` | Performance | Enable/disable based on measured need | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_collect_extended_stats`](storage/rocksdb.md#rocksdb_collect_extended_stats) | `False` | Performance | Enable/disable based on measured need | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_collect_memory_stats`](storage/rocksdb.md#rocksdb_collect_memory_stats) | `False` | Performance | Enable/disable based on measured need | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_delete_range_threshold`](storage/rocksdb.md#rocksdb_delete_range_threshold) | `1_M` | Performance | Baseline → adjust → validate under load | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_index_type`](storage/rocksdb.md#rocksdb_index_type) | `binary_search` | Dev | Keep upstream default in production | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_log_to_ceph_log`](storage/rocksdb.md#rocksdb_log_to_ceph_log) | `True` | Performance | Enable/disable based on measured need | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_metadata_block_size`](storage/rocksdb.md#rocksdb_metadata_block_size) | `4_K` | Dev | Keep upstream default in production | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_partition_filters`](storage/rocksdb.md#rocksdb_partition_filters) | `False` | Dev | Keep upstream default in production | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_perf`](storage/rocksdb.md#rocksdb_perf) | `False` | Performance | Enable/disable based on measured need | [Rocksdb](storage/rocksdb.md) |
| [`rocksdb_pin_l0_filter_and_index_blocks_in_cache`](storage/rocksdb.md#rocksdb_pin_l0_filter_and_index_blocks_in_cache) | `False` | Dev | Keep upstream default in production | [Rocksdb](storage/rocksdb.md) |
| [`rotating_keys_bootstrap_timeout`](auth/rotating.md#rotating_keys_bootstrap_timeout) | `30` | Performance | Baseline → adjust → validate under load | [Rotating](auth/rotating.md) |
| [`rotating_keys_renewal_timeout`](auth/rotating.md#rotating_keys_renewal_timeout) | `10` | Performance | Baseline → adjust → validate under load | [Rotating](auth/rotating.md) |
| [`run_dir`](runtime/run.md#run_dir) | `/var/run/ceph` | Capacity | Match filesystem layout and capacity plan | [Run](runtime/run.md) |
| [`service_unique_id`](runtime/service.md#service_unique_id) | `(empty)` | Performance | Baseline → adjust → validate under load | [Service](runtime/service.md) |
| [`setgroup`](runtime/setgroup.md#setgroup) | `(empty)` | Performance | Baseline → adjust → validate under load | [Setgroup](runtime/setgroup.md) |
| [`setuser`](runtime/setuser.md#setuser) | `(empty)` | Performance | Baseline → adjust → validate under load | [Setuser](runtime/setuser.md) |
| [`setuser_match_path`](runtime/setuser.md#setuser_match_path) | `(empty)` | Capacity | Match filesystem layout and capacity plan | [Setuser](runtime/setuser.md) |
| [`target_max_misplaced_ratio`](runtime/target.md#target_max_misplaced_ratio) | `0.05` | Performance | Baseline → adjust → validate under load | [Target](runtime/target.md) |
| [`thp`](runtime/thp.md#thp) | `False` | Dev | Keep upstream default in production | [Thp](runtime/thp.md) |
| [`threadpool_default_timeout`](runtime/threadpool.md#threadpool_default_timeout) | `1_min` | Performance | Baseline → adjust → validate under load | [Threadpool](runtime/threadpool.md) |
| [`threadpool_empty_queue_max_wait`](runtime/threadpool.md#threadpool_empty_queue_max_wait) | `2` | Performance | Baseline → adjust → validate under load | [Threadpool](runtime/threadpool.md) |
| [`throttler_perf_counter`](runtime/throttler.md#throttler_perf_counter) | `True` | Performance | Enable/disable based on measured need | [Throttler](runtime/throttler.md) |
| [`tmp_dir`](runtime/tmp.md#tmp_dir) | `/tmp` | Capacity | Match filesystem layout and capacity plan | [Tmp](runtime/tmp.md) |
| [`tmp_file_template`](runtime/tmp.md#tmp_file_template) | `$tmp_dir/$cluster-$name.XXXXXX` | Performance | Baseline → adjust → validate under load | [Tmp](runtime/tmp.md) |
| [`uadk_compressor_enabled`](storage/uadk.md#uadk_compressor_enabled) | `False` | Policy | Align with security and compatibility policy | [Uadk](storage/uadk.md) |
| [`uadk_wd_sync_ctx_num`](storage/uadk.md#uadk_wd_sync_ctx_num) | `2` | Performance | Stay within documented bounds | [Uadk](storage/uadk.md) |

[← Overview](../OVERVIEW.md)
