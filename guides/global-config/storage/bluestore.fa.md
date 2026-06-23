# Bluestore

راهنمای عمیق پیکربندی Global — 174 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [bluestore_2q_cache_kin_ratio](#bluestore_2q_cache_kin_ratio) | `0.5` | Dev | توسعه |
| [bluestore_2q_cache_kout_ratio](#bluestore_2q_cache_kout_ratio) | `0.5` | Dev | توسعه |
| [bluestore_alloc_stats_dump_interval](#bluestore_alloc_stats_dump_interval) | `1_day` | Dev | توسعه |
| [bluestore_allocation_from_file](#bluestore_allocation_from_file) | `True` | Dev | توسعه |
| [bluestore_allocation_recovery_threads](#bluestore_allocation_recovery_threads) | `0` | Basic | عملکرد |
| [bluestore_allocator](#bluestore_allocator) | `hybrid` | Advanced | عملکرد |
| [bluestore_allocator_lookup_policy](#bluestore_allocator_lookup_policy) | `auto` | Advanced | عملکرد |
| [bluestore_async_db_compaction](#bluestore_async_db_compaction) | `True` | Dev | توسعه |
| [bluestore_avl_alloc_bf_free_pct](#bluestore_avl_alloc_bf_free_pct) | `4` | Dev | توسعه |
| [bluestore_avl_alloc_bf_threshold](#bluestore_avl_alloc_bf_threshold) | `128_K` | Dev | توسعه |
| [bluestore_avl_alloc_ff_max_search_bytes](#bluestore_avl_alloc_ff_max_search_bytes) | `16_M` | Dev | توسعه |
| [bluestore_avl_alloc_ff_max_search_count](#bluestore_avl_alloc_ff_max_search_count) | `100` | Dev | توسعه |
| [bluestore_bdev_label_multi](#bluestore_bdev_label_multi) | `True` | Advanced | عملکرد |
| [bluestore_bdev_label_multi_upgrade](#bluestore_bdev_label_multi_upgrade) | `False` | Advanced | عملکرد |
| [bluestore_bdev_label_require_all](#bluestore_bdev_label_require_all) | `True` | Advanced | عملکرد |
| [bluestore_bitmapallocator_blocks_per_zone](#bluestore_bitmapallocator_blocks_per_zone) | `1_K` | Dev | توسعه |
| [bluestore_bitmapallocator_span_size](#bluestore_bitmapallocator_span_size) | `1_K` | Dev | توسعه |
| [bluestore_blobid_prealloc](#bluestore_blobid_prealloc) | `10_K` | Dev | توسعه |
| [bluestore_block_create](#bluestore_block_create) | `True` | Dev | توسعه |
| [bluestore_block_db_create](#bluestore_block_db_create) | `False` | Dev | توسعه |
| [bluestore_block_db_path](#bluestore_block_db_path) | `(empty)` | Dev | توسعه |
| [bluestore_block_db_size](#bluestore_block_db_size) | `0` | Dev | توسعه |
| [bluestore_block_path](#bluestore_block_path) | `(empty)` | Dev | توسعه |
| [bluestore_block_preallocate_file](#bluestore_block_preallocate_file) | `False` | Dev | توسعه |
| [bluestore_block_size](#bluestore_block_size) | `100_G` | Dev | توسعه |
| [bluestore_block_wal_create](#bluestore_block_wal_create) | `False` | Dev | توسعه |
| [bluestore_block_wal_path](#bluestore_block_wal_path) | `(empty)` | Dev | توسعه |
| [bluestore_block_wal_size](#bluestore_block_wal_size) | `96_M` | Dev | توسعه |
| [bluestore_bluefs](#bluestore_bluefs) | `True` | Dev | توسعه |
| [bluestore_bluefs_alloc_failure_dump_interval](#bluestore_bluefs_alloc_failure_dump_interval) | `0` | Advanced | عملکرد |
| [bluestore_bluefs_env_mirror](#bluestore_bluefs_env_mirror) | `False` | Dev | توسعه |
| [bluestore_bluefs_max_free](#bluestore_bluefs_max_free) | `10_G` | Advanced | عملکرد |
| [bluestore_bluefs_warn_ratio](#bluestore_bluefs_warn_ratio) | `0.06` | Basic | سیاست |
| [bluestore_btree2_alloc_weight_factor](#bluestore_btree2_alloc_weight_factor) | `2` | Dev | توسعه |
| [bluestore_cache_age_bin_interval](#bluestore_cache_age_bin_interval) | `1` | Dev | توسعه |
| [bluestore_cache_age_bins_data](#bluestore_cache_age_bins_data) | `1 2 6 24 120 720 0 0 0 0` | Dev | توسعه |
| [bluestore_cache_age_bins_kv](#bluestore_cache_age_bins_kv) | `1 2 6 24 120 720 0 0 0 0` | Dev | توسعه |
| [bluestore_cache_age_bins_kv_onode](#bluestore_cache_age_bins_kv_onode) | `0 0 0 0 0 0 0 0 0 720` | Dev | توسعه |
| [bluestore_cache_age_bins_meta](#bluestore_cache_age_bins_meta) | `1 2 6 24 120 720 0 0 0 0` | Dev | توسعه |
| [bluestore_cache_autotune](#bluestore_cache_autotune) | `True` | Dev | توسعه |
| [bluestore_cache_autotune_interval](#bluestore_cache_autotune_interval) | `5` | Dev | توسعه |
| [bluestore_cache_kv_onode_ratio](#bluestore_cache_kv_onode_ratio) | `0.04` | Dev | توسعه |
| [bluestore_cache_kv_ratio](#bluestore_cache_kv_ratio) | `0.45` | Dev | توسعه |
| [bluestore_cache_meta_evict_in_autotune](#bluestore_cache_meta_evict_in_autotune) | `True` | Advanced | عملکرد |
| [bluestore_cache_meta_evict_limit](#bluestore_cache_meta_evict_limit) | `10` | Advanced | عملکرد |
| [bluestore_cache_meta_ratio](#bluestore_cache_meta_ratio) | `0.45` | Dev | توسعه |
| [bluestore_cache_size](#bluestore_cache_size) | `0` | Dev | توسعه |
| [bluestore_cache_size_hdd](#bluestore_cache_size_hdd) | `1_G` | Dev | توسعه |
| [bluestore_cache_size_ssd](#bluestore_cache_size_ssd) | `3_G` | Dev | توسعه |
| [bluestore_cache_trim_interval](#bluestore_cache_trim_interval) | `0.05` | Advanced | عملکرد |
| [bluestore_cache_trim_max_skip_pinned](#bluestore_cache_trim_max_skip_pinned) | `1000` | Dev | توسعه |
| [bluestore_cache_type](#bluestore_cache_type) | `2q` | Dev | توسعه |
| [bluestore_cleaner_sleep_interval](#bluestore_cleaner_sleep_interval) | `5` | Advanced | عملکرد |
| [bluestore_clone_cow](#bluestore_clone_cow) | `True` | Advanced | عملکرد |
| [bluestore_compression_algorithm](#bluestore_compression_algorithm) | `snappy` | Advanced | عملکرد |
| [bluestore_compression_max_blob_size](#bluestore_compression_max_blob_size) | `0` | Advanced | عملکرد |
| [bluestore_compression_max_blob_size_hdd](#bluestore_compression_max_blob_size_hdd) | `64_K` | Advanced | عملکرد |
| [bluestore_compression_max_blob_size_ssd](#bluestore_compression_max_blob_size_ssd) | `64_K` | Advanced | عملکرد |
| [bluestore_compression_min_blob_size](#bluestore_compression_min_blob_size) | `0` | Advanced | عملکرد |
| [bluestore_compression_min_blob_size_hdd](#bluestore_compression_min_blob_size_hdd) | `64_K` | Advanced | عملکرد |
| [bluestore_compression_min_blob_size_ssd](#bluestore_compression_min_blob_size_ssd) | `64_K` | Advanced | عملکرد |
| [bluestore_compression_mode](#bluestore_compression_mode) | `none` | Advanced | عملکرد |
| [bluestore_compression_required_ratio](#bluestore_compression_required_ratio) | `0.875` | Advanced | عملکرد |
| [bluestore_csum_type](#bluestore_csum_type) | `crc32c` | Advanced | عملکرد |
| [bluestore_debug_enforce_min_alloc_size](#bluestore_debug_enforce_min_alloc_size) | `0` | Dev | توسعه |
| [bluestore_debug_enforce_settings](#bluestore_debug_enforce_settings) | `default` | Dev | توسعه |
| [bluestore_debug_extent_map_encode_check](#bluestore_debug_extent_map_encode_check) | `False` | Dev | توسعه |
| [bluestore_debug_fast_recovery_compare_chance](#bluestore_debug_fast_recovery_compare_chance) | `0` | Dev | توسعه |
| [bluestore_debug_freelist](#bluestore_debug_freelist) | `False` | Dev | توسعه |
| [bluestore_debug_fsck_abort](#bluestore_debug_fsck_abort) | `False` | Dev | توسعه |
| [bluestore_debug_inject_allocation_from_file_failure](#bluestore_debug_inject_allocation_from_file_failure) | `0` | Dev | توسعه |
| [bluestore_debug_inject_csum_err_probability](#bluestore_debug_inject_csum_err_probability) | `0` | Dev | توسعه |
| [bluestore_debug_inject_read_err](#bluestore_debug_inject_read_err) | `False` | Dev | توسعه |
| [bluestore_debug_legacy_omap](#bluestore_debug_legacy_omap) | `False` | Dev | توسعه |
| [bluestore_debug_no_reuse_blocks](#bluestore_debug_no_reuse_blocks) | `False` | Dev | توسعه |
| [bluestore_debug_omit_block_device_write](#bluestore_debug_omit_block_device_write) | `False` | Dev | توسعه |
| [bluestore_debug_omit_kv_commit](#bluestore_debug_omit_kv_commit) | `False` | Dev | توسعه |
| [bluestore_debug_onode_segmentation_random](#bluestore_debug_onode_segmentation_random) | `False` | Dev | توسعه |
| [bluestore_debug_permit_any_bdev_label](#bluestore_debug_permit_any_bdev_label) | `False` | Dev | توسعه |
| [bluestore_debug_prefragment_max](#bluestore_debug_prefragment_max) | `1_M` | Dev | توسعه |
| [bluestore_debug_random_read_err](#bluestore_debug_random_read_err) | `0` | Dev | توسعه |
| [bluestore_debug_randomize_serial_transaction](#bluestore_debug_randomize_serial_transaction) | `0` | Dev | توسعه |
| [bluestore_debug_small_allocations](#bluestore_debug_small_allocations) | `0` | Dev | توسعه |
| [bluestore_debug_too_many_blobs_threshold](#bluestore_debug_too_many_blobs_threshold) | `24576` | Dev | توسعه |
| [bluestore_default_buffered_read](#bluestore_default_buffered_read) | `True` | Advanced | عملکرد |
| [bluestore_default_buffered_write](#bluestore_default_buffered_write) | `False` | Advanced | عملکرد |
| [bluestore_deferred_batch_ops](#bluestore_deferred_batch_ops) | `0` | Advanced | عملکرد |
| [bluestore_deferred_batch_ops_hdd](#bluestore_deferred_batch_ops_hdd) | `64` | Advanced | عملکرد |
| [bluestore_deferred_batch_ops_ssd](#bluestore_deferred_batch_ops_ssd) | `16` | Advanced | عملکرد |
| [bluestore_discard_on_mkfs](#bluestore_discard_on_mkfs) | `True` | Advanced | عملکرد |
| [bluestore_elastic_shared_blobs](#bluestore_elastic_shared_blobs) | `True` | Advanced | عملکرد |
| [bluestore_extent_map_inline_shard_prealloc_size](#bluestore_extent_map_inline_shard_prealloc_size) | `256` | Dev | توسعه |
| [bluestore_extent_map_shard_max_size](#bluestore_extent_map_shard_max_size) | `1200` | Dev | توسعه |
| [bluestore_extent_map_shard_min_size](#bluestore_extent_map_shard_min_size) | `150` | Dev | توسعه |
| [bluestore_extent_map_shard_target_size](#bluestore_extent_map_shard_target_size) | `500` | Dev | توسعه |
| [bluestore_extent_map_shard_target_size_slop](#bluestore_extent_map_shard_target_size_slop) | `0.2` | Dev | توسعه |
| [bluestore_fail_eio](#bluestore_fail_eio) | `False` | Dev | توسعه |
| [bluestore_frag_runtime](#bluestore_frag_runtime) | `False` | Advanced | عملکرد |
| [bluestore_frag_static](#bluestore_frag_static) | `False` | Advanced | عملکرد |
| [bluestore_fragmentation_check_period](#bluestore_fragmentation_check_period) | `3600` | Basic | سیاست |
| [bluestore_freelist_blocks_per_key](#bluestore_freelist_blocks_per_key) | `128` | Dev | توسعه |
| [bluestore_fsck_error_on_no_per_pg_omap](#bluestore_fsck_error_on_no_per_pg_omap) | `False` | Advanced | عملکرد |
| [bluestore_fsck_error_on_no_per_pool_omap](#bluestore_fsck_error_on_no_per_pool_omap) | `False` | Advanced | عملکرد |
| [bluestore_fsck_error_on_no_per_pool_stats](#bluestore_fsck_error_on_no_per_pool_stats) | `False` | Advanced | عملکرد |
| [bluestore_fsck_on_mkfs](#bluestore_fsck_on_mkfs) | `True` | Dev | توسعه |
| [bluestore_fsck_on_mkfs_deep](#bluestore_fsck_on_mkfs_deep) | `False` | Dev | توسعه |
| [bluestore_fsck_on_mount](#bluestore_fsck_on_mount) | `False` | Dev | توسعه |
| [bluestore_fsck_on_mount_deep](#bluestore_fsck_on_mount_deep) | `False` | Dev | توسعه |
| [bluestore_fsck_on_umount](#bluestore_fsck_on_umount) | `False` | Dev | توسعه |
| [bluestore_fsck_on_umount_deep](#bluestore_fsck_on_umount_deep) | `False` | Dev | توسعه |
| [bluestore_fsck_quick_fix_on_mount](#bluestore_fsck_quick_fix_on_mount) | `False` | Dev | توسعه |
| [bluestore_fsck_quick_fix_threads](#bluestore_fsck_quick_fix_threads) | `2` | Advanced | عملکرد |
| [bluestore_fsck_read_bytes_cap](#bluestore_fsck_read_bytes_cap) | `64_M` | Advanced | عملکرد |
| [bluestore_fsck_shared_blob_tracker_size](#bluestore_fsck_shared_blob_tracker_size) | `0.03125` | Dev | توسعه |
| [bluestore_gc_enable_blob_threshold](#bluestore_gc_enable_blob_threshold) | `0` | Dev | توسعه |
| [bluestore_gc_enable_total_threshold](#bluestore_gc_enable_total_threshold) | `0` | Dev | توسعه |
| [bluestore_hybrid_alloc_mem_cap](#bluestore_hybrid_alloc_mem_cap) | `64_M` | Dev | توسعه |
| [bluestore_ignore_data_csum](#bluestore_ignore_data_csum) | `False` | Dev | توسعه |
| [bluestore_kv_sync_util_logging_s](#bluestore_kv_sync_util_logging_s) | `10` | Advanced | عملکرد |
| [bluestore_kvbackend](#bluestore_kvbackend) | `rocksdb` | Dev | توسعه |
| [bluestore_log_collection_list_age](#bluestore_log_collection_list_age) | `1_min` | Advanced | عملکرد |
| [bluestore_log_omap_iterator_age](#bluestore_log_omap_iterator_age) | `5` | Advanced | عملکرد |
| [bluestore_log_op_age](#bluestore_log_op_age) | `5` | Advanced | عملکرد |
| [bluestore_log_scrub_op_age](#bluestore_log_scrub_op_age) | `5` | Advanced | عملکرد |
| [bluestore_max_alloc_size](#bluestore_max_alloc_size) | `0` | Advanced | عملکرد |
| [bluestore_max_blob_size](#bluestore_max_blob_size) | `0` | Dev | توسعه |
| [bluestore_max_blob_size_hdd](#bluestore_max_blob_size_hdd) | `64_K` | Dev | توسعه |
| [bluestore_max_blob_size_ssd](#bluestore_max_blob_size_ssd) | `64_K` | Dev | توسعه |
| [bluestore_max_defer_interval](#bluestore_max_defer_interval) | `3` | Advanced | عملکرد |
| [bluestore_max_deferred_txc](#bluestore_max_deferred_txc) | `32` | Advanced | عملکرد |
| [bluestore_min_alloc_size](#bluestore_min_alloc_size) | `0` | Advanced | عملکرد |
| [bluestore_min_alloc_size_hdd](#bluestore_min_alloc_size_hdd) | `4_K` | Advanced | عملکرد |
| [bluestore_min_alloc_size_ssd](#bluestore_min_alloc_size_ssd) | `4_K` | Advanced | عملکرد |
| [bluestore_nid_prealloc](#bluestore_nid_prealloc) | `1024` | Dev | توسعه |
| [bluestore_onode_segment_size](#bluestore_onode_segment_size) | `0` | Advanced | عملکرد |
| [bluestore_prefer_deferred_size](#bluestore_prefer_deferred_size) | `0` | Advanced | عملکرد |
| [bluestore_prefer_deferred_size_hdd](#bluestore_prefer_deferred_size_hdd) | `64_K` | Advanced | عملکرد |
| [bluestore_prefer_deferred_size_ssd](#bluestore_prefer_deferred_size_ssd) | `0` | Advanced | عملکرد |
| [bluestore_qfsck_on_mount](#bluestore_qfsck_on_mount) | `True` | Dev | توسعه |
| [bluestore_recompression_min_gain](#bluestore_recompression_min_gain) | `1.2` | Advanced | عملکرد |
| [bluestore_retry_disk_reads](#bluestore_retry_disk_reads) | `3` | Advanced | عملکرد |
| [bluestore_rocksdb_cf](#bluestore_rocksdb_cf) | `True` | Advanced | عملکرد |
| [bluestore_rocksdb_cfs](#bluestore_rocksdb_cfs) | `m(3) p(3,0-12) O(3,0-13)=block_cache={type=binned_lru} L=min_write_buffer_number_to_merge=32 P=min_write_buffer_number_to_merge=32` | Dev | توسعه |
| [bluestore_rocksdb_options](#bluestore_rocksdb_options) | `compression=kLZ4Compression,max_write_buffer_number=64,min_write_buffer_number_to_merge=6,compaction_style=kCompactionStyleLevel,write_buffer_size=16777216,max_background_jobs=4,level0_file_num_compaction_trigger=8,max_bytes_for_level_base=1073741824,max_bytes_for_level_multiplier=8,compaction_readahead_size=2MB,max_total_wal_size=1073741824,writable_file_max_buffer_size=0` | Advanced | عملکرد |
| [bluestore_rocksdb_options_annex](#bluestore_rocksdb_options_annex) | `(empty)` | Advanced | عملکرد |
| [bluestore_slow_ops_warn_lifetime](#bluestore_slow_ops_warn_lifetime) | `86400` | Advanced | عملکرد |
| [bluestore_slow_ops_warn_threshold](#bluestore_slow_ops_warn_threshold) | `1` | Advanced | عملکرد |
| [bluestore_slow_scrub_ops_warn_threshold](#bluestore_slow_scrub_ops_warn_threshold) | `1` | Advanced | عملکرد |
| [bluestore_spdk_coremask](#bluestore_spdk_coremask) | `0x1` | Dev | توسعه |
| [bluestore_spdk_io_sleep](#bluestore_spdk_io_sleep) | `5` | Dev | توسعه |
| [bluestore_spdk_max_io_completion](#bluestore_spdk_max_io_completion) | `0` | Dev | توسعه |
| [bluestore_spdk_mem](#bluestore_spdk_mem) | `512` | Dev | توسعه |
| [bluestore_sync_submit_transaction](#bluestore_sync_submit_transaction) | `False` | Dev | توسعه |
| [bluestore_throttle_bytes](#bluestore_throttle_bytes) | `64_M` | Advanced | عملکرد |
| [bluestore_throttle_cost_per_io](#bluestore_throttle_cost_per_io) | `0` | Advanced | عملکرد |
| [bluestore_throttle_cost_per_io_hdd](#bluestore_throttle_cost_per_io_hdd) | `670000` | Advanced | عملکرد |
| [bluestore_throttle_cost_per_io_ssd](#bluestore_throttle_cost_per_io_ssd) | `4000` | Advanced | عملکرد |
| [bluestore_throttle_deferred_bytes](#bluestore_throttle_deferred_bytes) | `128_M` | Advanced | عملکرد |
| [bluestore_throttle_trace_rate](#bluestore_throttle_trace_rate) | `0` | Advanced | عملکرد |
| [bluestore_tracing](#bluestore_tracing) | `False` | Advanced | عملکرد |
| [bluestore_use_ebd](#bluestore_use_ebd) | `True` | Advanced | عملکرد |
| [bluestore_use_optimal_io_size_for_min_alloc_size](#bluestore_use_optimal_io_size_for_min_alloc_size) | `False` | Advanced | عملکرد |
| [bluestore_volume_selection_policy](#bluestore_volume_selection_policy) | `use_some_extra` | Dev | توسعه |
| [bluestore_volume_selection_reserved](#bluestore_volume_selection_reserved) | `0` | Advanced | عملکرد |
| [bluestore_volume_selection_reserved_factor](#bluestore_volume_selection_reserved_factor) | `2` | Advanced | عملکرد |
| [bluestore_warn_on_bluefs_spillover](#bluestore_warn_on_bluefs_spillover) | `True` | Advanced | عملکرد |
| [bluestore_warn_on_free_fragmentation](#bluestore_warn_on_free_fragmentation) | `0.8` | Basic | سیاست |
| [bluestore_warn_on_legacy_statfs](#bluestore_warn_on_legacy_statfs) | `True` | Advanced | عملکرد |
| [bluestore_warn_on_no_per_pg_omap](#bluestore_warn_on_no_per_pg_omap) | `False` | Advanced | عملکرد |
| [bluestore_warn_on_no_per_pool_omap](#bluestore_warn_on_no_per_pool_omap) | `True` | Advanced | عملکرد |
| [bluestore_warn_on_spurious_read_errors](#bluestore_warn_on_spurious_read_errors) | `True` | Advanced | عملکرد |
| [bluestore_write_v2](#bluestore_write_v2) | `False` | Advanced | عملکرد |
| [bluestore_write_v2_random](#bluestore_write_v2_random) | `False` | Advanced | عملکرد |
| [bluestore_zero_block_detection](#bluestore_zero_block_detection) | `False` | Dev | توسعه |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **سیاست** | امنیت، سازگاری، پیش‌فرض‌های عملیاتی |
| **ظرفیت** | چیدمان دیسک، مسیرها، اندازه‌گیری |
| **عملکرد** | خط پایه → تغییر تدریجی → پایش کلاستر |
| **اتصال** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **توسعه** | در محیط عملیاتی همان پیش‌فرض upstream |

**ابزارهای مشترک:**

```bash
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### bluestore_2q_cache_kin_ratio

| | |
|---|---|
| نوع | Float · default `0.5` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_2q_cache_kin_ratio](../../../config/global/bluestore.md#SP_bluestore_2q_cache_kin_ratio) |

**کارکرد:** 2Q paper suggests .5

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_2q_cache_kin_ratio 0.5
ceph config get global bluestore_2q_cache_kin_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.5`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_2q_cache_kout_ratio

| | |
|---|---|
| نوع | Float · default `0.5` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_2q_cache_kout_ratio](../../../config/global/bluestore.md#SP_bluestore_2q_cache_kout_ratio) |

**کارکرد:** 2Q paper suggests .5

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_2q_cache_kout_ratio 0.5
ceph config get global bluestore_2q_cache_kout_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.5`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_alloc_stats_dump_interval

| | |
|---|---|
| نوع | Float · default `1_day` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_alloc_stats_dump_interval](../../../config/global/bluestore.md#SP_bluestore_alloc_stats_dump_interval) |

**کارکرد:** The period (in second) for logging allocation statistics.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_alloc_stats_dump_interval 1_day
ceph config get global bluestore_alloc_stats_dump_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1_day`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_allocation_from_file

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [bluestore.md#SP_bluestore_allocation_from_file](../../../config/global/bluestore.md#SP_bluestore_allocation_from_file) |

**کارکرد:** Remove allocation info from RocksDB and store the info in a new allocation file

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_allocation_from_file false
ceph config get global bluestore_allocation_from_file
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_allocation_recovery_threads

| | |
|---|---|
| نوع | Uint · default `0` · **Basic** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [bluestore.md#SP_bluestore_allocation_recovery_threads](../../../config/global/bluestore.md#SP_bluestore_allocation_recovery_threads) |

**کارکرد:** Amount of threads for allocation recovery after OSD crash.

**زمان استفاده:** رفتار اصلی Global — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set global bluestore_allocation_recovery_threads 64
ceph config get global bluestore_allocation_recovery_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_allocation_recovery_threads
ceph -s
```

---

### bluestore_allocator

| | |
|---|---|
| نوع | Str · enum: ["bitmap", "stupid", "avl", "btree", "hybrid", "hybrid_btree2"] · default `hybrid` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_allocator](../../../config/global/bluestore.md#SP_bluestore_allocator) |

**کارکرد:** Allocator policy

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_allocator hybrid
ceph config get global bluestore_allocator
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `hybrid`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_allocator
ceph -s
```

---

### bluestore_allocator_lookup_policy

| | |
|---|---|
| نوع | Str · enum: ["hdd_optimized", "ssd_optimized", "auto"] · default `auto` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_allocator_lookup_policy](../../../config/global/bluestore.md#SP_bluestore_allocator_lookup_policy) |

**کارکرد:** Determines how to perform the next free extent lookup.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_allocator_lookup_policy auto
ceph config get global bluestore_allocator_lookup_policy
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `auto`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_allocator_lookup_policy
ceph -s
```

---

### bluestore_async_db_compaction

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_async_db_compaction](../../../config/global/bluestore.md#SP_bluestore_async_db_compaction) |

**کارکرد:** Perform DB compaction requests asynchronously

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_async_db_compaction false
ceph config get global bluestore_async_db_compaction
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_avl_alloc_bf_free_pct

| | |
|---|---|
| نوع | Uint · default `4` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_avl_alloc_bf_free_pct](../../../config/global/bluestore.md#SP_bluestore_avl_alloc_bf_free_pct) |

**کارکرد:** Sets the threshold at which shrinking free space (in %, integer) triggers enabling best-fit mode.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_avl_alloc_bf_free_pct 4
ceph config get global bluestore_avl_alloc_bf_free_pct
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`4`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_avl_alloc_bf_threshold

| | |
|---|---|
| نوع | Uint · default `128_K` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_avl_alloc_bf_threshold](../../../config/global/bluestore.md#SP_bluestore_avl_alloc_bf_threshold) |

**کارکرد:** Sets threshold at which shrinking max free chunk size triggers enabling best-fit mode.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_avl_alloc_bf_threshold 128_K
ceph config get global bluestore_avl_alloc_bf_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`128_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_avl_alloc_ff_max_search_bytes

| | |
|---|---|
| نوع | Size · default `16_M` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_avl_alloc_ff_max_search_bytes](../../../config/global/bluestore.md#SP_bluestore_avl_alloc_ff_max_search_bytes) |

**کارکرد:** Maximum distance to search in first-fit mode before switching over to to best-fit mode. 0 to iterate through all ranges for required chunk.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_avl_alloc_ff_max_search_bytes 16_M
ceph config get global bluestore_avl_alloc_ff_max_search_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`16_M`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_avl_alloc_ff_max_search_count

| | |
|---|---|
| نوع | Uint · default `100` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_avl_alloc_ff_max_search_count](../../../config/global/bluestore.md#SP_bluestore_avl_alloc_ff_max_search_count) |

**کارکرد:** Search for this many ranges in first-fit mode before switching over to to best-fit mode. 0 to iterate through all ranges for required chunk.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_avl_alloc_ff_max_search_count 100
ceph config get global bluestore_avl_alloc_ff_max_search_count
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`100`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_bdev_label_multi

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_bdev_label_multi](../../../config/global/bluestore.md#SP_bluestore_bdev_label_multi) |

**کارکرد:** Keep multiple copies of block device label.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global bluestore_bdev_label_multi false
ceph config get global bluestore_bdev_label_multi
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_bdev_label_multi
ceph -s
```

---

### bluestore_bdev_label_multi_upgrade

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [bluestore.md#SP_bluestore_bdev_label_multi_upgrade](../../../config/global/bluestore.md#SP_bluestore_bdev_label_multi_upgrade) |

**کارکرد:** Let repair upgrade to multi label.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bluestore_bdev_label_multi_upgrade true
ceph config get global bluestore_bdev_label_multi_upgrade
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_bdev_label_multi_upgrade
ceph -s
```

---

### bluestore_bdev_label_require_all

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_bdev_label_require_all](../../../config/global/bluestore.md#SP_bluestore_bdev_label_require_all) |

**کارکرد:** Require all copies to match.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global bluestore_bdev_label_require_all false
ceph config get global bluestore_bdev_label_require_all
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_bdev_label_require_all
ceph -s
```

---

### bluestore_bitmapallocator_blocks_per_zone

| | |
|---|---|
| نوع | Size · default `1_K` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_bitmapallocator_blocks_per_zone](../../../config/global/bluestore.md#SP_bluestore_bitmapallocator_blocks_per_zone) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_bitmapallocator_blocks_per_zone 1_K
ceph config get global bluestore_bitmapallocator_blocks_per_zone
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_bitmapallocator_span_size

| | |
|---|---|
| نوع | Size · default `1_K` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_bitmapallocator_span_size](../../../config/global/bluestore.md#SP_bluestore_bitmapallocator_span_size) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_bitmapallocator_span_size 1_K
ceph config get global bluestore_bitmapallocator_span_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_blobid_prealloc

| | |
|---|---|
| نوع | Uint · default `10_K` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_blobid_prealloc](../../../config/global/bluestore.md#SP_bluestore_blobid_prealloc) |

**کارکرد:** Number of unique blob IDs to preallocate at a time

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_blobid_prealloc 10_K
ceph config get global bluestore_blobid_prealloc
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`10_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_block_create

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_block_create](../../../config/global/bluestore.md#SP_bluestore_block_create) |

**کارکرد:** Create bluestore_block_path if it doesn't exist

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_block_create false
ceph config get global bluestore_block_create
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_block_db_create

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_block_db_create](../../../config/global/bluestore.md#SP_bluestore_block_db_create) |

**کارکرد:** Create bluestore_block_db_path if it doesn't exist

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_block_db_create true
ceph config get global bluestore_block_db_create
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_block_db_path

| | |
|---|---|
| نوع | Str · default `(empty)` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_block_db_path](../../../config/global/bluestore.md#SP_bluestore_block_db_path) |

**کارکرد:** Path for DB block device

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_block_db_path "/var/lib/ceph/example"
ceph config get global bluestore_block_db_path
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`(empty)`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_block_db_size

| | |
|---|---|
| نوع | Size · default `0` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_block_db_size](../../../config/global/bluestore.md#SP_bluestore_block_db_size) |

**کارکرد:** Size of file to create for bluestore_block_db_path

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_block_db_size 64
ceph config get global bluestore_block_db_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_block_path

| | |
|---|---|
| نوع | Str · default `(empty)` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_block_path](../../../config/global/bluestore.md#SP_bluestore_block_path) |

**کارکرد:** Path to block device/file

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_block_path "/var/lib/ceph/example"
ceph config get global bluestore_block_path
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`(empty)`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_block_preallocate_file

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_block_preallocate_file](../../../config/global/bluestore.md#SP_bluestore_block_preallocate_file) |

**کارکرد:** Preallocate file created via bluestore_block*_create

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_block_preallocate_file true
ceph config get global bluestore_block_preallocate_file
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_block_size

| | |
|---|---|
| نوع | Size · default `100_G` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_block_size](../../../config/global/bluestore.md#SP_bluestore_block_size) |

**کارکرد:** Size of file to create for backing BlueStore

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_block_size 100_G
ceph config get global bluestore_block_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`100_G`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_block_wal_create

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_block_wal_create](../../../config/global/bluestore.md#SP_bluestore_block_wal_create) |

**کارکرد:** Create bluestore_block_wal_path if it doesn't exist

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_block_wal_create true
ceph config get global bluestore_block_wal_create
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_block_wal_path

| | |
|---|---|
| نوع | Str · default `(empty)` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_block_wal_path](../../../config/global/bluestore.md#SP_bluestore_block_wal_path) |

**کارکرد:** Path to block device/file backing the BlueFS WAL

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_block_wal_path "/var/lib/ceph/example"
ceph config get global bluestore_block_wal_path
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`(empty)`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_block_wal_size

| | |
|---|---|
| نوع | Size · default `96_M` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_block_wal_size](../../../config/global/bluestore.md#SP_bluestore_block_wal_size) |

**کارکرد:** Size of file to create for bluestore_block_wal_path

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_block_wal_size 96_M
ceph config get global bluestore_block_wal_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`96_M`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_bluefs

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_bluefs](../../../config/global/bluestore.md#SP_bluestore_bluefs) |

**کارکرد:** Use BlueFS to back RocksDB

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_bluefs false
ceph config get global bluestore_bluefs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_bluefs_alloc_failure_dump_interval

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_bluefs_alloc_failure_dump_interval](../../../config/global/bluestore.md#SP_bluestore_bluefs_alloc_failure_dump_interval) |

**کارکرد:** How frequently (in seconds) to dump allocator on BlueFS space allocation failure

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global bluestore_bluefs_alloc_failure_dump_interval 0
ceph config get global bluestore_bluefs_alloc_failure_dump_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_bluefs_alloc_failure_dump_interval
ceph -s
```

---

### bluestore_bluefs_env_mirror

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_bluefs_env_mirror](../../../config/global/bluestore.md#SP_bluestore_bluefs_env_mirror) |

**کارکرد:** Mirror BlueFS data to file system for testing/validation

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_bluefs_env_mirror true
ceph config get global bluestore_bluefs_env_mirror
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_bluefs_max_free

| | |
|---|---|
| نوع | Size · default `10_G` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_bluefs_max_free](../../../config/global/bluestore.md#SP_bluestore_bluefs_max_free) |

**کارکرد:** Maximum free space allocated to BlueFS

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluestore_bluefs_max_free 10_G
ceph config get global bluestore_bluefs_max_free
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10_G`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_bluefs_max_free
ceph -s
```

---

### bluestore_bluefs_warn_ratio

| | |
|---|---|
| نوع | Float · default `0.06` · **Basic** |
| جدول | [bluestore.md#SP_bluestore_bluefs_warn_ratio](../../../config/global/bluestore.md#SP_bluestore_bluefs_warn_ratio) |

**کارکرد:** The ratio at which BlueFS usage relative to the main device raises a health warning. Set to "1" to disable.

**زمان استفاده:** رفتار اصلی Global — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set global bluestore_bluefs_warn_ratio 0.06
ceph config get global bluestore_bluefs_warn_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `0.06` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_bluefs_warn_ratio
ceph -s
```

---

### bluestore_btree2_alloc_weight_factor

| | |
|---|---|
| نوع | Float · default `2` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_btree2_alloc_weight_factor](../../../config/global/bluestore.md#SP_bluestore_btree2_alloc_weight_factor) |

**کارکرد:** Large continuous extents weight factor

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_btree2_alloc_weight_factor 2
ceph config get global bluestore_btree2_alloc_weight_factor
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`2`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_cache_age_bin_interval

| | |
|---|---|
| نوع | Float · default `1` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_cache_age_bin_interval](../../../config/global/bluestore.md#SP_bluestore_cache_age_bin_interval) |

**کارکرد:** The duration (in seconds) represented by a single cache age bin.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_cache_age_bin_interval 1
ceph config get global bluestore_cache_age_bin_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_cache_age_bins_data

| | |
|---|---|
| نوع | Str · default `1 2 6 24 120 720 0 0 0 0` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_cache_age_bins_data](../../../config/global/bluestore.md#SP_bluestore_cache_age_bins_data) |

**کارکرد:** A 10 element, space separated list of age bins for data cache

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_cache_age_bins_data "1 2 6 24 120 720 0 0 0 0"
ceph config get global bluestore_cache_age_bins_data
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1 2 6 24 120 720 0 0 0 0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_cache_age_bins_kv

| | |
|---|---|
| نوع | Str · default `1 2 6 24 120 720 0 0 0 0` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_cache_age_bins_kv](../../../config/global/bluestore.md#SP_bluestore_cache_age_bins_kv) |

**کارکرد:** A 10 element, space separated list of age bins for kv cache

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_cache_age_bins_kv "1 2 6 24 120 720 0 0 0 0"
ceph config get global bluestore_cache_age_bins_kv
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1 2 6 24 120 720 0 0 0 0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_cache_age_bins_kv_onode

| | |
|---|---|
| نوع | Str · default `0 0 0 0 0 0 0 0 0 720` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_cache_age_bins_kv_onode](../../../config/global/bluestore.md#SP_bluestore_cache_age_bins_kv_onode) |

**کارکرد:** A 10 element, space separated list of age bins for kv onode cache

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_cache_age_bins_kv_onode "0 0 0 0 0 0 0 0 0 720"
ceph config get global bluestore_cache_age_bins_kv_onode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0 0 0 0 0 0 0 0 0 720`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_cache_age_bins_meta

| | |
|---|---|
| نوع | Str · default `1 2 6 24 120 720 0 0 0 0` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_cache_age_bins_meta](../../../config/global/bluestore.md#SP_bluestore_cache_age_bins_meta) |

**کارکرد:** A 10 element, space separated list of age bins for onode cache

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_cache_age_bins_meta "1 2 6 24 120 720 0 0 0 0"
ceph config get global bluestore_cache_age_bins_meta
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1 2 6 24 120 720 0 0 0 0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_cache_autotune

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_cache_autotune](../../../config/global/bluestore.md#SP_bluestore_cache_autotune) |

**کارکرد:** Automatically tune the ratio of caches while respecting min values.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_cache_autotune false
ceph config get global bluestore_cache_autotune
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_cache_autotune_interval

| | |
|---|---|
| نوع | Float · default `5` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_cache_autotune_interval](../../../config/global/bluestore.md#SP_bluestore_cache_autotune_interval) |

**کارکرد:** The number of seconds to wait between rebalances when cache autotune is enabled.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_cache_autotune_interval 5
ceph config get global bluestore_cache_autotune_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`5`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_cache_kv_onode_ratio

| | |
|---|---|
| نوع | Float · default `0.04` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_cache_kv_onode_ratio](../../../config/global/bluestore.md#SP_bluestore_cache_kv_onode_ratio) |

**کارکرد:** Ratio of BlueStore cache to devote to key/value onode column family (rocksdb)

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_cache_kv_onode_ratio 0.04
ceph config get global bluestore_cache_kv_onode_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.04`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_cache_kv_ratio

| | |
|---|---|
| نوع | Float · default `0.45` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_cache_kv_ratio](../../../config/global/bluestore.md#SP_bluestore_cache_kv_ratio) |

**کارکرد:** Ratio of BlueStore cache to devote to key/value database (RocksDB)

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_cache_kv_ratio 0.45
ceph config get global bluestore_cache_kv_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.45`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_cache_meta_evict_in_autotune

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_cache_meta_evict_in_autotune](../../../config/global/bluestore.md#SP_bluestore_cache_meta_evict_in_autotune) |

**کارکرد:** Controls eviction of onodes from cache shards as part of autotune. When enabled (true), right after autotune memory allocation run onode cache tries to adapt. Depending on `bluestore_cache_meta_evict_limit` either some or all excess onodes are evicted. When disabled (false), cluster inactivity makes cache to keep its onode elements.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global bluestore_cache_meta_evict_in_autotune false
ceph config get global bluestore_cache_meta_evict_in_autotune
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_cache_meta_evict_in_autotune
ceph -s
```

---

### bluestore_cache_meta_evict_limit

| | |
|---|---|
| نوع | Int · default `10` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_cache_meta_evict_limit](../../../config/global/bluestore.md#SP_bluestore_cache_meta_evict_limit) |

**کارکرد:** Elements in onode cache shards are evicted when new element is inserted into the cache. In rare cases of cluster inactivity cache can be reduced, but not evicted. Adjusting size at once will cause stall first time cache shard is accessed. The setting limits how many onodes can get evicted in one go. Any value is less than 2 it is treated as request to adjust immediately.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluestore_cache_meta_evict_limit 10
ceph config get global bluestore_cache_meta_evict_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_cache_meta_evict_limit
ceph -s
```

---

### bluestore_cache_meta_ratio

| | |
|---|---|
| نوع | Float · default `0.45` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_cache_meta_ratio](../../../config/global/bluestore.md#SP_bluestore_cache_meta_ratio) |

**کارکرد:** Ratio of BlueStore cache to devote to metadata

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_cache_meta_ratio 0.45
ceph config get global bluestore_cache_meta_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.45`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_cache_size

| | |
|---|---|
| نوع | Size · default `0` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_cache_size](../../../config/global/bluestore.md#SP_bluestore_cache_size) |

**کارکرد:** Cache size (in bytes) for BlueStore

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_cache_size 64
ceph config get global bluestore_cache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_cache_size_hdd

| | |
|---|---|
| نوع | Size · default `1_G` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_cache_size_hdd](../../../config/global/bluestore.md#SP_bluestore_cache_size_hdd) |

**کارکرد:** Default bluestore_cache_size for rotational media

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_cache_size_hdd 1_G
ceph config get global bluestore_cache_size_hdd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1_G`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_cache_size_ssd

| | |
|---|---|
| نوع | Size · default `3_G` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_cache_size_ssd](../../../config/global/bluestore.md#SP_bluestore_cache_size_ssd) |

**کارکرد:** Default bluestore_cache_size for non-rotational (solid state) media

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_cache_size_ssd 3_G
ceph config get global bluestore_cache_size_ssd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`3_G`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_cache_trim_interval

| | |
|---|---|
| نوع | Float · default `0.05` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_cache_trim_interval](../../../config/global/bluestore.md#SP_bluestore_cache_trim_interval) |

**کارکرد:** How frequently we trim the bluestore cache

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global bluestore_cache_trim_interval 0.05
ceph config get global bluestore_cache_trim_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.05`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_cache_trim_interval
ceph -s
```

---

### bluestore_cache_trim_max_skip_pinned

| | |
|---|---|
| نوع | Uint · default `1000` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_cache_trim_max_skip_pinned](../../../config/global/bluestore.md#SP_bluestore_cache_trim_max_skip_pinned) |

**کارکرد:** Max pinned cache entries we consider before giving up

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_cache_trim_max_skip_pinned 1000
ceph config get global bluestore_cache_trim_max_skip_pinned
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1000`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_cache_type

| | |
|---|---|
| نوع | Str · enum: ["2q", "lru"] · default `2q` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_cache_type](../../../config/global/bluestore.md#SP_bluestore_cache_type) |

**کارکرد:** Cache replacement algorithm

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_cache_type 2q
ceph config get global bluestore_cache_type
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`2q`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_cleaner_sleep_interval

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_cleaner_sleep_interval](../../../config/global/bluestore.md#SP_bluestore_cleaner_sleep_interval) |

**کارکرد:** How long the BlueStore cleaner should sleep before re-checking utilization

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global bluestore_cleaner_sleep_interval 5
ceph config get global bluestore_cleaner_sleep_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_cleaner_sleep_interval
ceph -s
```

---

### bluestore_clone_cow

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_clone_cow](../../../config/global/bluestore.md#SP_bluestore_clone_cow) |

**کارکرد:** Use copy-on-write when cloning objects (versus reading and rewriting them at clone time)

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global bluestore_clone_cow false
ceph config get global bluestore_clone_cow
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_clone_cow
ceph -s
```

---

### bluestore_compression_algorithm

| | |
|---|---|
| نوع | Str · enum: ["", "snappy", "zlib", "zstd", "lz4"] · default `snappy` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_compression_algorithm](../../../config/global/bluestore.md#SP_bluestore_compression_algorithm) |

**کارکرد:** Default compression algorithm to use when writing object data

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_compression_algorithm snappy
ceph config get global bluestore_compression_algorithm
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `snappy`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_compression_algorithm
ceph -s
```

---

### bluestore_compression_max_blob_size

| | |
|---|---|
| نوع | Size · default `0` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_compression_max_blob_size](../../../config/global/bluestore.md#SP_bluestore_compression_max_blob_size) |

**کارکرد:** Maximum chunk size to apply compression to when non-random access is expected for an object.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluestore_compression_max_blob_size 64
ceph config get global bluestore_compression_max_blob_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_compression_max_blob_size
ceph -s
```

---

### bluestore_compression_max_blob_size_hdd

| | |
|---|---|
| نوع | Size · default `64_K` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_compression_max_blob_size_hdd](../../../config/global/bluestore.md#SP_bluestore_compression_max_blob_size_hdd) |

**کارکرد:** Default value of bluestore_compression_max_blob_size for rotational media

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluestore_compression_max_blob_size_hdd 64_K
ceph config get global bluestore_compression_max_blob_size_hdd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_compression_max_blob_size_hdd
ceph -s
```

---

### bluestore_compression_max_blob_size_ssd

| | |
|---|---|
| نوع | Size · default `64_K` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_compression_max_blob_size_ssd](../../../config/global/bluestore.md#SP_bluestore_compression_max_blob_size_ssd) |

**کارکرد:** Default value of bluestore_compression_max_blob_size for non-rotational (solid state) media

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluestore_compression_max_blob_size_ssd 64_K
ceph config get global bluestore_compression_max_blob_size_ssd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_compression_max_blob_size_ssd
ceph -s
```

---

### bluestore_compression_min_blob_size

| | |
|---|---|
| نوع | Size · default `0` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_compression_min_blob_size](../../../config/global/bluestore.md#SP_bluestore_compression_min_blob_size) |

**کارکرد:** Maximum chunk size to apply compression to when random access is expected for an object.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluestore_compression_min_blob_size 64
ceph config get global bluestore_compression_min_blob_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_compression_min_blob_size
ceph -s
```

---

### bluestore_compression_min_blob_size_hdd

| | |
|---|---|
| نوع | Size · default `64_K` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_compression_min_blob_size_hdd](../../../config/global/bluestore.md#SP_bluestore_compression_min_blob_size_hdd) |

**کارکرد:** Default value of bluestore_compression_min_blob_size for rotational media

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluestore_compression_min_blob_size_hdd 64_K
ceph config get global bluestore_compression_min_blob_size_hdd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_compression_min_blob_size_hdd
ceph -s
```

---

### bluestore_compression_min_blob_size_ssd

| | |
|---|---|
| نوع | Size · default `64_K` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_compression_min_blob_size_ssd](../../../config/global/bluestore.md#SP_bluestore_compression_min_blob_size_ssd) |

**کارکرد:** Default value of bluestore_compression_min_blob_size for non-rotational (solid state) media

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluestore_compression_min_blob_size_ssd 64_K
ceph config get global bluestore_compression_min_blob_size_ssd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_compression_min_blob_size_ssd
ceph -s
```

---

### bluestore_compression_mode

| | |
|---|---|
| نوع | Str · enum: ["none", "passive", "aggressive", "force"] · default `none` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_compression_mode](../../../config/global/bluestore.md#SP_bluestore_compression_mode) |

**کارکرد:** Default policy for using compression when pool does not specify

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_compression_mode none
ceph config get global bluestore_compression_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `none`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_compression_mode
ceph -s
```

---

### bluestore_compression_required_ratio

| | |
|---|---|
| نوع | Float · default `0.875` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_compression_required_ratio](../../../config/global/bluestore.md#SP_bluestore_compression_required_ratio) |

**کارکرد:** Compression ratio required to store compressed data

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_compression_required_ratio 0.875
ceph config get global bluestore_compression_required_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.875`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_compression_required_ratio
ceph -s
```

---

### bluestore_csum_type

| | |
|---|---|
| نوع | Str · enum: ["none", "crc32c", "crc32c_16", "crc32c_8", "xxhash32", "xxhash64"] · default `crc32c` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_csum_type](../../../config/global/bluestore.md#SP_bluestore_csum_type) |

**کارکرد:** Default checksum algorithm to use

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_csum_type crc32c
ceph config get global bluestore_csum_type
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `crc32c`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_csum_type
ceph -s
```

---

### bluestore_debug_enforce_min_alloc_size

| | |
|---|---|
| نوع | Uint · default `0` · **Dev** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [bluestore.md#SP_bluestore_debug_enforce_min_alloc_size](../../../config/global/bluestore.md#SP_bluestore_debug_enforce_min_alloc_size) |

**کارکرد:** Enforces specific min_alloc size usages

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_enforce_min_alloc_size 64
ceph config get global bluestore_debug_enforce_min_alloc_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_enforce_settings

| | |
|---|---|
| نوع | Str · enum: ["default", "hdd", "ssd"] · default `default` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_debug_enforce_settings](../../../config/global/bluestore.md#SP_bluestore_debug_enforce_settings) |

**کارکرد:** Enforces specific hardware profile settings

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_enforce_settings default
ceph config get global bluestore_debug_enforce_settings
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`default`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_extent_map_encode_check

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [bluestore.md#SP_bluestore_debug_extent_map_encode_check](../../../config/global/bluestore.md#SP_bluestore_debug_extent_map_encode_check) |

**کارکرد:** Check correctness of extents in encode_some

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_extent_map_encode_check true
ceph config get global bluestore_debug_extent_map_encode_check
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_fast_recovery_compare_chance

| | |
|---|---|
| نوع | Float · default `0` · **Dev** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [bluestore.md#SP_bluestore_debug_fast_recovery_compare_chance](../../../config/global/bluestore.md#SP_bluestore_debug_fast_recovery_compare_chance) |

**کارکرد:** For testing only. Compare legacy and multithread allocation recovery.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_fast_recovery_compare_chance 0
ceph config get global bluestore_debug_fast_recovery_compare_chance
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_freelist

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_debug_freelist](../../../config/global/bluestore.md#SP_bluestore_debug_freelist) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_freelist true
ceph config get global bluestore_debug_freelist
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_fsck_abort

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_debug_fsck_abort](../../../config/global/bluestore.md#SP_bluestore_debug_fsck_abort) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_fsck_abort true
ceph config get global bluestore_debug_fsck_abort
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_inject_allocation_from_file_failure

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_debug_inject_allocation_from_file_failure](../../../config/global/bluestore.md#SP_bluestore_debug_inject_allocation_from_file_failure) |

**کارکرد:** Enables random error injections when restoring allocation map from file.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_inject_allocation_from_file_failure 0
ceph config get global bluestore_debug_inject_allocation_from_file_failure
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_inject_csum_err_probability

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_debug_inject_csum_err_probability](../../../config/global/bluestore.md#SP_bluestore_debug_inject_csum_err_probability) |

**کارکرد:** Inject CRC verification errors into BlueStore device reads

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_inject_csum_err_probability 0
ceph config get global bluestore_debug_inject_csum_err_probability
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_inject_read_err

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_debug_inject_read_err](../../../config/global/bluestore.md#SP_bluestore_debug_inject_read_err) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_inject_read_err true
ceph config get global bluestore_debug_inject_read_err
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_legacy_omap

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_debug_legacy_omap](../../../config/global/bluestore.md#SP_bluestore_debug_legacy_omap) |

**کارکرد:** Allows mkfs to create OSDs with the legacy omap naming mode (neither per-pool nor per-pg). This is intended primarily for developers. The resulting OSDs might / would be transformed to the currrently default 'per-pg' format when BlueStore's quick-fix or repair are applied.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_legacy_omap true
ceph config get global bluestore_debug_legacy_omap
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_no_reuse_blocks

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_debug_no_reuse_blocks](../../../config/global/bluestore.md#SP_bluestore_debug_no_reuse_blocks) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_no_reuse_blocks true
ceph config get global bluestore_debug_no_reuse_blocks
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_omit_block_device_write

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_debug_omit_block_device_write](../../../config/global/bluestore.md#SP_bluestore_debug_omit_block_device_write) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_omit_block_device_write true
ceph config get global bluestore_debug_omit_block_device_write
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_omit_kv_commit

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_debug_omit_kv_commit](../../../config/global/bluestore.md#SP_bluestore_debug_omit_kv_commit) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_omit_kv_commit true
ceph config get global bluestore_debug_omit_kv_commit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_onode_segmentation_random

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [bluestore.md#SP_bluestore_debug_onode_segmentation_random](../../../config/global/bluestore.md#SP_bluestore_debug_onode_segmentation_random) |

**کارکرد:** Random selection of onode segmentation

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_onode_segmentation_random true
ceph config get global bluestore_debug_onode_segmentation_random
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_permit_any_bdev_label

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_debug_permit_any_bdev_label](../../../config/global/bluestore.md#SP_bluestore_debug_permit_any_bdev_label) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_permit_any_bdev_label true
ceph config get global bluestore_debug_permit_any_bdev_label
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_prefragment_max

| | |
|---|---|
| نوع | Size · default `1_M` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_debug_prefragment_max](../../../config/global/bluestore.md#SP_bluestore_debug_prefragment_max) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_prefragment_max 1_M
ceph config get global bluestore_debug_prefragment_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1_M`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_random_read_err

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_debug_random_read_err](../../../config/global/bluestore.md#SP_bluestore_debug_random_read_err) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_random_read_err 0
ceph config get global bluestore_debug_random_read_err
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_randomize_serial_transaction

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_debug_randomize_serial_transaction](../../../config/global/bluestore.md#SP_bluestore_debug_randomize_serial_transaction) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_randomize_serial_transaction 64
ceph config get global bluestore_debug_randomize_serial_transaction
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_small_allocations

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_debug_small_allocations](../../../config/global/bluestore.md#SP_bluestore_debug_small_allocations) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_small_allocations 64
ceph config get global bluestore_debug_small_allocations
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_debug_too_many_blobs_threshold

| | |
|---|---|
| نوع | Int · default `24576` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_debug_too_many_blobs_threshold](../../../config/global/bluestore.md#SP_bluestore_debug_too_many_blobs_threshold) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_debug_too_many_blobs_threshold 24576
ceph config get global bluestore_debug_too_many_blobs_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`24576`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_default_buffered_read

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_default_buffered_read](../../../config/global/bluestore.md#SP_bluestore_default_buffered_read) |

**کارکرد:** Cache read results by default (unless hinted NOCACHE or WONTNEED)

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global bluestore_default_buffered_read false
ceph config get global bluestore_default_buffered_read
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_default_buffered_read
ceph -s
```

---

### bluestore_default_buffered_write

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_default_buffered_write](../../../config/global/bluestore.md#SP_bluestore_default_buffered_write) |

**کارکرد:** Cache writes by default (unless hinted NOCACHE or WONTNEED)

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bluestore_default_buffered_write true
ceph config get global bluestore_default_buffered_write
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_default_buffered_write
ceph -s
```

---

### bluestore_deferred_batch_ops

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_deferred_batch_ops](../../../config/global/bluestore.md#SP_bluestore_deferred_batch_ops) |

**کارکرد:** Max number of deferred writes before we flush the deferred write queue

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_deferred_batch_ops 64
ceph config get global bluestore_deferred_batch_ops
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `65535`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_deferred_batch_ops
ceph -s
```

---

### bluestore_deferred_batch_ops_hdd

| | |
|---|---|
| نوع | Uint · default `64` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_deferred_batch_ops_hdd](../../../config/global/bluestore.md#SP_bluestore_deferred_batch_ops_hdd) |

**کارکرد:** Default bluestore_deferred_batch_ops for rotational media (HDD)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_deferred_batch_ops_hdd 64
ceph config get global bluestore_deferred_batch_ops_hdd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `65535`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_deferred_batch_ops_hdd
ceph -s
```

---

### bluestore_deferred_batch_ops_ssd

| | |
|---|---|
| نوع | Uint · default `16` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_deferred_batch_ops_ssd](../../../config/global/bluestore.md#SP_bluestore_deferred_batch_ops_ssd) |

**کارکرد:** Default bluestore_deferred_batch_ops for non-rotational (SSD) media

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_deferred_batch_ops_ssd 16
ceph config get global bluestore_deferred_batch_ops_ssd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `16`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `65535`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_deferred_batch_ops_ssd
ceph -s
```

---

### bluestore_discard_on_mkfs

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_discard_on_mkfs](../../../config/global/bluestore.md#SP_bluestore_discard_on_mkfs) |

**کارکرد:** Trim OSD devices after deployment

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global bluestore_discard_on_mkfs false
ceph config get global bluestore_discard_on_mkfs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_discard_on_mkfs
ceph -s
```

---

### bluestore_elastic_shared_blobs

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_elastic_shared_blobs](../../../config/global/bluestore.md#SP_bluestore_elastic_shared_blobs) |

**کارکرد:** Let BlueStore reuse existing shared blobs if possible

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global bluestore_elastic_shared_blobs false
ceph config get global bluestore_elastic_shared_blobs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_elastic_shared_blobs
ceph -s
```

---

### bluestore_extent_map_inline_shard_prealloc_size

| | |
|---|---|
| نوع | Size · default `256` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_extent_map_inline_shard_prealloc_size](../../../config/global/bluestore.md#SP_bluestore_extent_map_inline_shard_prealloc_size) |

**کارکرد:** Preallocated buffer for inline shards

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_extent_map_inline_shard_prealloc_size 256
ceph config get global bluestore_extent_map_inline_shard_prealloc_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`256`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_extent_map_shard_max_size

| | |
|---|---|
| نوع | Size · default `1200` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_extent_map_shard_max_size](../../../config/global/bluestore.md#SP_bluestore_extent_map_shard_max_size) |

**کارکرد:** Max size (bytes) for a single extent map shard before splitting

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_extent_map_shard_max_size 1200
ceph config get global bluestore_extent_map_shard_max_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1200`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_extent_map_shard_min_size

| | |
|---|---|
| نوع | Size · default `150` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_extent_map_shard_min_size](../../../config/global/bluestore.md#SP_bluestore_extent_map_shard_min_size) |

**کارکرد:** Min size (bytes) for a single extent map shard before merging

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_extent_map_shard_min_size 150
ceph config get global bluestore_extent_map_shard_min_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`150`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_extent_map_shard_target_size

| | |
|---|---|
| نوع | Size · default `500` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_extent_map_shard_target_size](../../../config/global/bluestore.md#SP_bluestore_extent_map_shard_target_size) |

**کارکرد:** Target size (bytes) for a single extent map shard

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_extent_map_shard_target_size 500
ceph config get global bluestore_extent_map_shard_target_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`500`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_extent_map_shard_target_size_slop

| | |
|---|---|
| نوع | Float · default `0.2` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_extent_map_shard_target_size_slop](../../../config/global/bluestore.md#SP_bluestore_extent_map_shard_target_size_slop) |

**کارکرد:** Ratio above/below target for a shard when trying to align to an existing extent or blob boundary

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_extent_map_shard_target_size_slop 0.2
ceph config get global bluestore_extent_map_shard_target_size_slop
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.2`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_fail_eio

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_fail_eio](../../../config/global/bluestore.md#SP_bluestore_fail_eio) |

**کارکرد:** fail/crash on EIO

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_fail_eio true
ceph config get global bluestore_fail_eio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_frag_runtime

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_frag_runtime](../../../config/global/bluestore.md#SP_bluestore_frag_runtime) |

**کارکرد:** Enable tracking of runtime object fragmentation during reads.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bluestore_frag_runtime true
ceph config get global bluestore_frag_runtime
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_frag_runtime
ceph -s
```

---

### bluestore_frag_static

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_frag_static](../../../config/global/bluestore.md#SP_bluestore_frag_static) |

**کارکرد:** Enable tracking of static object fragmentation during scrub

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bluestore_frag_static true
ceph config get global bluestore_frag_static
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_frag_static
ceph -s
```

---

### bluestore_fragmentation_check_period

| | |
|---|---|
| نوع | Uint · default `3600` · **Basic** |
| جدول | [bluestore.md#SP_bluestore_fragmentation_check_period](../../../config/global/bluestore.md#SP_bluestore_fragmentation_check_period) |

**کارکرد:** The interval at which to perform a BlueStore free fragmentation check. Checking fragmentation is usually almost immediate. For highly fragmented storage, it can take several miliseconds and can cause a write operation to stall.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global bluestore_fragmentation_check_period 3600
ceph config get global bluestore_fragmentation_check_period
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `3600` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_fragmentation_check_period
ceph -s
```

---

### bluestore_freelist_blocks_per_key

| | |
|---|---|
| نوع | Size · default `128` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_freelist_blocks_per_key](../../../config/global/bluestore.md#SP_bluestore_freelist_blocks_per_key) |

**کارکرد:** Block (and bits) per database key

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_freelist_blocks_per_key 128
ceph config get global bluestore_freelist_blocks_per_key
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`128`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_fsck_error_on_no_per_pg_omap

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_fsck_error_on_no_per_pg_omap](../../../config/global/bluestore.md#SP_bluestore_fsck_error_on_no_per_pg_omap) |

**کارکرد:** Throw a fsck error (instead of a warning) when objects without per-pg omap are found

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bluestore_fsck_error_on_no_per_pg_omap true
ceph config get global bluestore_fsck_error_on_no_per_pg_omap
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_fsck_error_on_no_per_pg_omap
ceph -s
```

---

### bluestore_fsck_error_on_no_per_pool_omap

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_fsck_error_on_no_per_pool_omap](../../../config/global/bluestore.md#SP_bluestore_fsck_error_on_no_per_pool_omap) |

**کارکرد:** Throw a fsck error (instead of a warning) when objects without per-pool omap are found

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bluestore_fsck_error_on_no_per_pool_omap true
ceph config get global bluestore_fsck_error_on_no_per_pool_omap
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_fsck_error_on_no_per_pool_omap
ceph -s
```

---

### bluestore_fsck_error_on_no_per_pool_stats

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_fsck_error_on_no_per_pool_stats](../../../config/global/bluestore.md#SP_bluestore_fsck_error_on_no_per_pool_stats) |

**کارکرد:** Direct that fsck throws an error (instead of raising a warning) when BlueStore OSDs lack per-pool stats, for example after an upgrade

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bluestore_fsck_error_on_no_per_pool_stats true
ceph config get global bluestore_fsck_error_on_no_per_pool_stats
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_fsck_error_on_no_per_pool_stats
ceph -s
```

---

### bluestore_fsck_on_mkfs

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_fsck_on_mkfs](../../../config/global/bluestore.md#SP_bluestore_fsck_on_mkfs) |

**کارکرد:** Run fsck after mkfs

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_fsck_on_mkfs false
ceph config get global bluestore_fsck_on_mkfs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_fsck_on_mkfs_deep

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_fsck_on_mkfs_deep](../../../config/global/bluestore.md#SP_bluestore_fsck_on_mkfs_deep) |

**کارکرد:** Run deep fsck after mkfs

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_fsck_on_mkfs_deep true
ceph config get global bluestore_fsck_on_mkfs_deep
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_fsck_on_mount

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_fsck_on_mount](../../../config/global/bluestore.md#SP_bluestore_fsck_on_mount) |

**کارکرد:** Run fsck at mount

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_fsck_on_mount true
ceph config get global bluestore_fsck_on_mount
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_fsck_on_mount_deep

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_fsck_on_mount_deep](../../../config/global/bluestore.md#SP_bluestore_fsck_on_mount_deep) |

**کارکرد:** Run deep fsck at mount when bluestore_fsck_on_mount is set to true

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_fsck_on_mount_deep true
ceph config get global bluestore_fsck_on_mount_deep
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_fsck_on_umount

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_fsck_on_umount](../../../config/global/bluestore.md#SP_bluestore_fsck_on_umount) |

**کارکرد:** Run fsck at umount

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_fsck_on_umount true
ceph config get global bluestore_fsck_on_umount
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_fsck_on_umount_deep

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_fsck_on_umount_deep](../../../config/global/bluestore.md#SP_bluestore_fsck_on_umount_deep) |

**کارکرد:** Run deep fsck at umount when bluestore_fsck_on_umount is set to true

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_fsck_on_umount_deep true
ceph config get global bluestore_fsck_on_umount_deep
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_fsck_quick_fix_on_mount

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_fsck_quick_fix_on_mount](../../../config/global/bluestore.md#SP_bluestore_fsck_quick_fix_on_mount) |

**کارکرد:** Do quick-fix for the store at mount

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_fsck_quick_fix_on_mount true
ceph config get global bluestore_fsck_quick_fix_on_mount
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_fsck_quick_fix_threads

| | |
|---|---|
| نوع | Int · default `2` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_fsck_quick_fix_threads](../../../config/global/bluestore.md#SP_bluestore_fsck_quick_fix_threads) |

**کارکرد:** Number of additional threads to perform quick-fix (shallow fsck) command

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_fsck_quick_fix_threads 2
ceph config get global bluestore_fsck_quick_fix_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_fsck_quick_fix_threads
ceph -s
```

---

### bluestore_fsck_read_bytes_cap

| | |
|---|---|
| نوع | Size · default `64_M` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_fsck_read_bytes_cap](../../../config/global/bluestore.md#SP_bluestore_fsck_read_bytes_cap) |

**کارکرد:** Maximum bytes read at once by deep fsck

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluestore_fsck_read_bytes_cap 64_M
ceph config get global bluestore_fsck_read_bytes_cap
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_fsck_read_bytes_cap
ceph -s
```

---

### bluestore_fsck_shared_blob_tracker_size

| | |
|---|---|
| نوع | Float · default `0.03125` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_fsck_shared_blob_tracker_size](../../../config/global/bluestore.md#SP_bluestore_fsck_shared_blob_tracker_size) |

**کارکرد:** Size (a fraction of osd_memory_target, defaults to 128MB) of a hash table that tracks shared blob ref counts. A higher value makes the the tracker more precise and reduces overhead during repairs.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_fsck_shared_blob_tracker_size 0.03125
ceph config get global bluestore_fsck_shared_blob_tracker_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.03125`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_gc_enable_blob_threshold

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_gc_enable_blob_threshold](../../../config/global/bluestore.md#SP_bluestore_gc_enable_blob_threshold) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_gc_enable_blob_threshold 64
ceph config get global bluestore_gc_enable_blob_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_gc_enable_total_threshold

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_gc_enable_total_threshold](../../../config/global/bluestore.md#SP_bluestore_gc_enable_total_threshold) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_gc_enable_total_threshold 64
ceph config get global bluestore_gc_enable_total_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_hybrid_alloc_mem_cap

| | |
|---|---|
| نوع | Uint · default `64_M` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_hybrid_alloc_mem_cap](../../../config/global/bluestore.md#SP_bluestore_hybrid_alloc_mem_cap) |

**کارکرد:** The maximum amount of memory the hybrid allocator should use before enabling bitmap supplement

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_hybrid_alloc_mem_cap 64_M
ceph config get global bluestore_hybrid_alloc_mem_cap
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`64_M`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_ignore_data_csum

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_ignore_data_csum](../../../config/global/bluestore.md#SP_bluestore_ignore_data_csum) |

**کارکرد:** Ignore checksum errors on read and do not generate an EIO error

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_ignore_data_csum true
ceph config get global bluestore_ignore_data_csum
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_kv_sync_util_logging_s

| | |
|---|---|
| نوع | Float · default `10` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_kv_sync_util_logging_s](../../../config/global/bluestore.md#SP_bluestore_kv_sync_util_logging_s) |

**کارکرد:** KV sync thread utilization logging period

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_kv_sync_util_logging_s 10
ceph config get global bluestore_kv_sync_util_logging_s
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_kv_sync_util_logging_s
ceph -s
```

---

### bluestore_kvbackend

| | |
|---|---|
| نوع | Str · default `rocksdb` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_kvbackend](../../../config/global/bluestore.md#SP_bluestore_kvbackend) |

**کارکرد:** Key value database to use for BlueStore

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_kvbackend rocksdb
ceph config get global bluestore_kvbackend
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`rocksdb`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_log_collection_list_age

| | |
|---|---|
| نوع | Float · default `1_min` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_log_collection_list_age](../../../config/global/bluestore.md#SP_bluestore_log_collection_list_age) |

**کارکرد:** Log a collection list operation if it is slower than this age (seconds)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_log_collection_list_age 1_min
ceph config get global bluestore_log_collection_list_age
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_log_collection_list_age
ceph -s
```

---

### bluestore_log_omap_iterator_age

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_log_omap_iterator_age](../../../config/global/bluestore.md#SP_bluestore_log_omap_iterator_age) |

**کارکرد:** Log an omap iteration operation if it is slower than this age (seconds)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_log_omap_iterator_age 5
ceph config get global bluestore_log_omap_iterator_age
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_log_omap_iterator_age
ceph -s
```

---

### bluestore_log_op_age

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_log_op_age](../../../config/global/bluestore.md#SP_bluestore_log_op_age) |

**کارکرد:** Log a BlueStore operation if it is slower than this age (seconds)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_log_op_age 5
ceph config get global bluestore_log_op_age
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_log_op_age
ceph -s
```

---

### bluestore_log_scrub_op_age

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_log_scrub_op_age](../../../config/global/bluestore.md#SP_bluestore_log_scrub_op_age) |

**کارکرد:** Log a BlueStore Scrub operation if it is slower than this age (seconds)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_log_scrub_op_age 5
ceph config get global bluestore_log_scrub_op_age
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_log_scrub_op_age
ceph -s
```

---

### bluestore_max_alloc_size

| | |
|---|---|
| نوع | Size · default `0` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_max_alloc_size](../../../config/global/bluestore.md#SP_bluestore_max_alloc_size) |

**کارکرد:** Maximum size of a single allocation (0 for no max)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluestore_max_alloc_size 64
ceph config get global bluestore_max_alloc_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_max_alloc_size
ceph -s
```

---

### bluestore_max_blob_size

| | |
|---|---|
| نوع | Size · default `0` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_max_blob_size](../../../config/global/bluestore.md#SP_bluestore_max_blob_size) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_max_blob_size 64
ceph config get global bluestore_max_blob_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_max_blob_size_hdd

| | |
|---|---|
| نوع | Size · default `64_K` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_max_blob_size_hdd](../../../config/global/bluestore.md#SP_bluestore_max_blob_size_hdd) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_max_blob_size_hdd 64_K
ceph config get global bluestore_max_blob_size_hdd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`64_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_max_blob_size_ssd

| | |
|---|---|
| نوع | Size · default `64_K` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_max_blob_size_ssd](../../../config/global/bluestore.md#SP_bluestore_max_blob_size_ssd) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_max_blob_size_ssd 64_K
ceph config get global bluestore_max_blob_size_ssd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`64_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_max_defer_interval

| | |
|---|---|
| نوع | Float · default `3` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_max_defer_interval](../../../config/global/bluestore.md#SP_bluestore_max_defer_interval) |

**کارکرد:** Max duration to force deferred submit

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluestore_max_defer_interval 3
ceph config get global bluestore_max_defer_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_max_defer_interval
ceph -s
```

---

### bluestore_max_deferred_txc

| | |
|---|---|
| نوع | Uint · default `32` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_max_deferred_txc](../../../config/global/bluestore.md#SP_bluestore_max_deferred_txc) |

**کارکرد:** Max transactions with deferred writes that can accumulate before we force flush deferred writes

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluestore_max_deferred_txc 32
ceph config get global bluestore_max_deferred_txc
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `32`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_max_deferred_txc
ceph -s
```

---

### bluestore_min_alloc_size

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_min_alloc_size](../../../config/global/bluestore.md#SP_bluestore_min_alloc_size) |

**کارکرد:** Minimum allocation size to allocate for an object

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluestore_min_alloc_size 64
ceph config get global bluestore_min_alloc_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_min_alloc_size
ceph -s
```

---

### bluestore_min_alloc_size_hdd

| | |
|---|---|
| نوع | Size · default `4_K` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_min_alloc_size_hdd](../../../config/global/bluestore.md#SP_bluestore_min_alloc_size_hdd) |

**کارکرد:** Default min_alloc_size value for rotational media

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluestore_min_alloc_size_hdd 4_K
ceph config get global bluestore_min_alloc_size_hdd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `4_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_min_alloc_size_hdd
ceph -s
```

---

### bluestore_min_alloc_size_ssd

| | |
|---|---|
| نوع | Size · default `4_K` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_min_alloc_size_ssd](../../../config/global/bluestore.md#SP_bluestore_min_alloc_size_ssd) |

**کارکرد:** Default min_alloc_size value for non-rotational (solid state) media

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluestore_min_alloc_size_ssd 4_K
ceph config get global bluestore_min_alloc_size_ssd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `4_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_min_alloc_size_ssd
ceph -s
```

---

### bluestore_nid_prealloc

| | |
|---|---|
| نوع | Int · default `1024` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_nid_prealloc](../../../config/global/bluestore.md#SP_bluestore_nid_prealloc) |

**کارکرد:** Number of unique object IDs to preallocate at a time

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_nid_prealloc 1024
ceph config get global bluestore_nid_prealloc
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1024`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_onode_segment_size

| | |
|---|---|
| نوع | Size · default `0` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_onode_segment_size](../../../config/global/bluestore.md#SP_bluestore_onode_segment_size) |

**کارکرد:** Size of segment for onode.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_onode_segment_size 64
ceph config get global bluestore_onode_segment_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_onode_segment_size
ceph -s
```

---

### bluestore_prefer_deferred_size

| | |
|---|---|
| نوع | Size · default `0` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_prefer_deferred_size](../../../config/global/bluestore.md#SP_bluestore_prefer_deferred_size) |

**کارکرد:** Writes smaller than this size will be written to the WAL and then asynchronously written to the block (slow) device. This can be beneficial when using rotational media where seeks are expensive, and is helpful both with and without SSD WAL. devices.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_prefer_deferred_size 64
ceph config get global bluestore_prefer_deferred_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_prefer_deferred_size
ceph -s
```

---

### bluestore_prefer_deferred_size_hdd

| | |
|---|---|
| نوع | Size · default `64_K` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_prefer_deferred_size_hdd](../../../config/global/bluestore.md#SP_bluestore_prefer_deferred_size_hdd) |

**کارکرد:** Default bluestore_prefer_deferred_size for rotational media

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_prefer_deferred_size_hdd 64_K
ceph config get global bluestore_prefer_deferred_size_hdd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_prefer_deferred_size_hdd
ceph -s
```

---

### bluestore_prefer_deferred_size_ssd

| | |
|---|---|
| نوع | Size · default `0` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_prefer_deferred_size_ssd](../../../config/global/bluestore.md#SP_bluestore_prefer_deferred_size_ssd) |

**کارکرد:** Default bluestore_prefer_deferred_size for non-rotational (SSD) media

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_prefer_deferred_size_ssd 64
ceph config get global bluestore_prefer_deferred_size_ssd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_prefer_deferred_size_ssd
ceph -s
```

---

### bluestore_qfsck_on_mount

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_qfsck_on_mount](../../../config/global/bluestore.md#SP_bluestore_qfsck_on_mount) |

**کارکرد:** Run quick-fsck at mount comparing allocation-file to RocksDB allocation state

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_qfsck_on_mount false
ceph config get global bluestore_qfsck_on_mount
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_recompression_min_gain

| | |
|---|---|
| نوع | Float · default `1.2` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_recompression_min_gain](../../../config/global/bluestore.md#SP_bluestore_recompression_min_gain) |

**کارکرد:** Required estimated gain for accepting extents for recompressing.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluestore_recompression_min_gain 1.2
ceph config get global bluestore_recompression_min_gain
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1.2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_recompression_min_gain
ceph -s
```

---

### bluestore_retry_disk_reads

| | |
|---|---|
| نوع | Uint · default `3` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_retry_disk_reads](../../../config/global/bluestore.md#SP_bluestore_retry_disk_reads) |

**کارکرد:** Number of read retries on checksum validation error

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_retry_disk_reads 3
ceph config get global bluestore_retry_disk_reads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `255`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_retry_disk_reads
ceph -s
```

---

### bluestore_rocksdb_cf

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_rocksdb_cf](../../../config/global/bluestore.md#SP_bluestore_rocksdb_cf) |

**کارکرد:** Enable use of RocksDB column families for BlueStore metadata

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global bluestore_rocksdb_cf false
ceph config get global bluestore_rocksdb_cf
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_rocksdb_cf
ceph -s
```

---

### bluestore_rocksdb_cfs

| | |
|---|---|
| نوع | Str · default `m(3) p(3,0-12) O(3,0-13)=block_cache={type=binned_lru} L=min_write_buffer_number_to_merge=32 P=min_write_buffer_number_to_merge=32` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_rocksdb_cfs](../../../config/global/bluestore.md#SP_bluestore_rocksdb_cfs) |

**کارکرد:** Definition of column families and their sharding

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_rocksdb_cfs "m(3) p(3,0-12) O(3,0-13)=block_cache={type=binned_lru} L=min_write_buffer_number_to_merge=32 P=min_write_buffer_number_to_merge=32"
ceph config get global bluestore_rocksdb_cfs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`m(3) p(3,0-12) O(3,0-13)=block_cache={type=binned_lru} L=min_write_buffer_number_to_merge=32 P=min_write_buffer_number_to_merge=32`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_rocksdb_options

| | |
|---|---|
| نوع | Str · default `compression=kLZ4Compression,max_write_buffer_number=64,min_write_buffer_number_to_merge=6,compaction_style=kCompactionStyleLevel,write_buffer_size=16777216,max_background_jobs=4,level0_file_num_compaction_trigger=8,max_bytes_for_level_base=1073741824,max_bytes_for_level_multiplier=8,compaction_readahead_size=2MB,max_total_wal_size=1073741824,writable_file_max_buffer_size=0` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_rocksdb_options](../../../config/global/bluestore.md#SP_bluestore_rocksdb_options) |

**کارکرد:** Full set of RocksDB settings to override

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_rocksdb_options "compression=kLZ4Compression,max_write_buffer_number=64,min_write_buffer_number_to_merge=6,compaction_style=kCompactionStyleLevel,write_buffer_size=16777216,max_background_jobs=4,level0_file_num_compaction_trigger=8,max_bytes_for_level_base=1073741824,max_bytes_for_level_multiplier=8,compaction_readahead_size=2MB,max_total_wal_size=1073741824,writable_file_max_buffer_size=0"
ceph config get global bluestore_rocksdb_options
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `compression=kLZ4Compression,max_write_buffer_number=64,min_write_buffer_number_to_merge=6,compaction_style=kCompactionStyleLevel,write_buffer_size=16777216,max_background_jobs=4,level0_file_num_compaction_trigger=8,max_bytes_for_level_base=1073741824,max_bytes_for_level_multiplier=8,compaction_readahead_size=2MB,max_total_wal_size=1073741824,writable_file_max_buffer_size=0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_rocksdb_options
ceph -s
```

---

### bluestore_rocksdb_options_annex

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_rocksdb_options_annex](../../../config/global/bluestore.md#SP_bluestore_rocksdb_options_annex) |

**کارکرد:** An addition to bluestore_rocksdb_options. Allows setting RocksDB options without repeating the existing defaults.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_rocksdb_options_annex "example"
ceph config get global bluestore_rocksdb_options_annex
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_rocksdb_options_annex
ceph -s
```

---

### bluestore_slow_ops_warn_lifetime

| | |
|---|---|
| نوع | Uint · default `86400` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_slow_ops_warn_lifetime](../../../config/global/bluestore.md#SP_bluestore_slow_ops_warn_lifetime) |

**کارکرد:** Set the duration after which BlueStore slow ops warnings clear after being raised by exceeding the `bluestore_slow_ops_warn_threshold`. This is not the same as `osd_op_complaint_time`, which is about RADOS ops at the OSD level.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_slow_ops_warn_lifetime 86400
ceph config get global bluestore_slow_ops_warn_lifetime
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `86400`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_slow_ops_warn_lifetime
ceph -s
```

---

### bluestore_slow_ops_warn_threshold

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_slow_ops_warn_threshold](../../../config/global/bluestore.md#SP_bluestore_slow_ops_warn_threshold) |

**کارکرد:** Set the minimum number of BlueStore slow ops before raising a health warning

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_slow_ops_warn_threshold 1
ceph config get global bluestore_slow_ops_warn_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_slow_ops_warn_threshold
ceph -s
```

---

### bluestore_slow_scrub_ops_warn_threshold

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_slow_scrub_ops_warn_threshold](../../../config/global/bluestore.md#SP_bluestore_slow_scrub_ops_warn_threshold) |

**کارکرد:** Set the minimum number of BlueStore slow scrub ops before raising a health warning

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_slow_scrub_ops_warn_threshold 1
ceph config get global bluestore_slow_scrub_ops_warn_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_slow_scrub_ops_warn_threshold
ceph -s
```

---

### bluestore_spdk_coremask

| | |
|---|---|
| نوع | Str · default `0x1` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_spdk_coremask](../../../config/global/bluestore.md#SP_bluestore_spdk_coremask) |

**کارکرد:** A hexadecimal bit mask of the cores to run on. Note the core numbering can change between platforms and should be determined beforehand

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_spdk_coremask 0x1
ceph config get global bluestore_spdk_coremask
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0x1`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_spdk_io_sleep

| | |
|---|---|
| نوع | Uint · default `5` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_spdk_io_sleep](../../../config/global/bluestore.md#SP_bluestore_spdk_io_sleep) |

**کارکرد:** Time period to wait if there is no completed I/O from polling

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_spdk_io_sleep 5
ceph config get global bluestore_spdk_io_sleep
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`5`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_spdk_max_io_completion

| | |
|---|---|
| نوع | Uint · default `0` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_spdk_max_io_completion](../../../config/global/bluestore.md#SP_bluestore_spdk_max_io_completion) |

**کارکرد:** Maximum number of operations to be batched completed while checking queue pair completions, 0 means to let the SPDK library determine the value

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_spdk_max_io_completion 64
ceph config get global bluestore_spdk_max_io_completion
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_spdk_mem

| | |
|---|---|
| نوع | Size · default `512` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_spdk_mem](../../../config/global/bluestore.md#SP_bluestore_spdk_mem) |

**کارکرد:** Amount of dpdk memory size in MB

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_spdk_mem 512
ceph config get global bluestore_spdk_mem
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`512`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_sync_submit_transaction

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_sync_submit_transaction](../../../config/global/bluestore.md#SP_bluestore_sync_submit_transaction) |

**کارکرد:** Try to submit metadata transaction to RocksDB in queuing thread context

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_sync_submit_transaction true
ceph config get global bluestore_sync_submit_transaction
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_throttle_bytes

| | |
|---|---|
| نوع | Size · default `64_M` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_throttle_bytes](../../../config/global/bluestore.md#SP_bluestore_throttle_bytes) |

**کارکرد:** Maximum bytes in flight before we throttle IO submission

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_throttle_bytes 64_M
ceph config get global bluestore_throttle_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_throttle_bytes
ceph -s
```

---

### bluestore_throttle_cost_per_io

| | |
|---|---|
| نوع | Size · default `0` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_throttle_cost_per_io](../../../config/global/bluestore.md#SP_bluestore_throttle_cost_per_io) |

**کارکرد:** Overhead added to transaction cost (in bytes) for each IO

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_throttle_cost_per_io 64
ceph config get global bluestore_throttle_cost_per_io
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_throttle_cost_per_io
ceph -s
```

---

### bluestore_throttle_cost_per_io_hdd

| | |
|---|---|
| نوع | Uint · default `670000` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_throttle_cost_per_io_hdd](../../../config/global/bluestore.md#SP_bluestore_throttle_cost_per_io_hdd) |

**کارکرد:** Default bluestore_throttle_cost_per_io for rotational media (HDDs)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_throttle_cost_per_io_hdd 670000
ceph config get global bluestore_throttle_cost_per_io_hdd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `670000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_throttle_cost_per_io_hdd
ceph -s
```

---

### bluestore_throttle_cost_per_io_ssd

| | |
|---|---|
| نوع | Uint · default `4000` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_throttle_cost_per_io_ssd](../../../config/global/bluestore.md#SP_bluestore_throttle_cost_per_io_ssd) |

**کارکرد:** Default bluestore_throttle_cost_per_io for non-rotation (SSD) media

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_throttle_cost_per_io_ssd 4000
ceph config get global bluestore_throttle_cost_per_io_ssd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `4000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_throttle_cost_per_io_ssd
ceph -s
```

---

### bluestore_throttle_deferred_bytes

| | |
|---|---|
| نوع | Size · default `128_M` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_throttle_deferred_bytes](../../../config/global/bluestore.md#SP_bluestore_throttle_deferred_bytes) |

**کارکرد:** Maximum bytes for deferred writes before we throttle IO submission

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_throttle_deferred_bytes 128_M
ceph config get global bluestore_throttle_deferred_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `128_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_throttle_deferred_bytes
ceph -s
```

---

### bluestore_throttle_trace_rate

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_throttle_trace_rate](../../../config/global/bluestore.md#SP_bluestore_throttle_trace_rate) |

**کارکرد:** Rate at which to sample BlueStore transactions (per second)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_throttle_trace_rate 0
ceph config get global bluestore_throttle_trace_rate
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_throttle_trace_rate
ceph -s
```

---

### bluestore_tracing

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_tracing](../../../config/global/bluestore.md#SP_bluestore_tracing) |

**کارکرد:** Enable BlueStore event tracing.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bluestore_tracing true
ceph config get global bluestore_tracing
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_tracing
ceph -s
```

---

### bluestore_use_ebd

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_use_ebd](../../../config/global/bluestore.md#SP_bluestore_use_ebd) |

**کارکرد:** EBD plugin used during mkfs is required for mounts.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global bluestore_use_ebd false
ceph config get global bluestore_use_ebd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_use_ebd
ceph -s
```

---

### bluestore_use_optimal_io_size_for_min_alloc_size

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_use_optimal_io_size_for_min_alloc_size](../../../config/global/bluestore.md#SP_bluestore_use_optimal_io_size_for_min_alloc_size) |

**کارکرد:** Discover media optimal IO size and use for min_alloc_size. This is useful when OSDs are created on coarse-IU QLC SSDs or other novel types of underlyinng block device. It is a no-op for conventional media.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bluestore_use_optimal_io_size_for_min_alloc_size true
ceph config get global bluestore_use_optimal_io_size_for_min_alloc_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_use_optimal_io_size_for_min_alloc_size
ceph -s
```

---

### bluestore_volume_selection_policy

| | |
|---|---|
| نوع | Str · enum: ["rocksdb_original", "use_some_extra", "use_some_extra_enforced", "fit_to_fast"] · default `use_some_extra` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_volume_selection_policy](../../../config/global/bluestore.md#SP_bluestore_volume_selection_policy) |

**کارکرد:** Determine the BlueFS volume selection policy

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_volume_selection_policy use_some_extra
ceph config get global bluestore_volume_selection_policy
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`use_some_extra`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluestore_volume_selection_reserved

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [bluestore.md#SP_bluestore_volume_selection_reserved](../../../config/global/bluestore.md#SP_bluestore_volume_selection_reserved) |

**کارکرد:** Space reserved on the DB device and not allowed for 'use some extra' policy usage. Overrides the 'bluestore_volume_selection_reserved_factor' setting and introduces a straightforward limit.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_volume_selection_reserved 64
ceph config get global bluestore_volume_selection_reserved
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_volume_selection_reserved
ceph -s
```

---

### bluestore_volume_selection_reserved_factor

| | |
|---|---|
| نوع | Float · default `2` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [bluestore.md#SP_bluestore_volume_selection_reserved_factor](../../../config/global/bluestore.md#SP_bluestore_volume_selection_reserved_factor) |

**کارکرد:** RocksDB level size multiplier. Determines amount of space at DB device to bar from the usage when 'use some extra' policy is in action. The reserved size is determined by sum(L_max_size&#91;0&#93;, L_max_size&#91;L-1&#93;) + L_max_size&#91;L&#93; * this_factor

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluestore_volume_selection_reserved_factor 2
ceph config get global bluestore_volume_selection_reserved_factor
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_volume_selection_reserved_factor
ceph -s
```

---

### bluestore_warn_on_bluefs_spillover

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_warn_on_bluefs_spillover](../../../config/global/bluestore.md#SP_bluestore_warn_on_bluefs_spillover) |

**کارکرد:** Raise a health warning on BlueFS slow device spillover

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global bluestore_warn_on_bluefs_spillover false
ceph config get global bluestore_warn_on_bluefs_spillover
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_warn_on_bluefs_spillover
ceph -s
```

---

### bluestore_warn_on_free_fragmentation

| | |
|---|---|
| نوع | Float · default `0.8` · **Basic** |
| جدول | [bluestore.md#SP_bluestore_warn_on_free_fragmentation](../../../config/global/bluestore.md#SP_bluestore_warn_on_free_fragmentation) |

**کارکرد:** The level at which BlueStore block device free fragmentation raises a health warning. Set to "1" to disable. This is the value reported by the admin socket command "bluestore allocator score block".

**زمان استفاده:** رفتار اصلی Global — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set global bluestore_warn_on_free_fragmentation 0.8
ceph config get global bluestore_warn_on_free_fragmentation
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `0.8` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_warn_on_free_fragmentation
ceph -s
```

---

### bluestore_warn_on_legacy_statfs

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_warn_on_legacy_statfs](../../../config/global/bluestore.md#SP_bluestore_warn_on_legacy_statfs) |

**کارکرد:** Raise a health warning on the lack of per-pool statfs reporting from a BlueStore OSD

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global bluestore_warn_on_legacy_statfs false
ceph config get global bluestore_warn_on_legacy_statfs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_warn_on_legacy_statfs
ceph -s
```

---

### bluestore_warn_on_no_per_pg_omap

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_warn_on_no_per_pg_omap](../../../config/global/bluestore.md#SP_bluestore_warn_on_no_per_pg_omap) |

**کارکرد:** Raise a health warning on lack of per-pg omap

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bluestore_warn_on_no_per_pg_omap true
ceph config get global bluestore_warn_on_no_per_pg_omap
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_warn_on_no_per_pg_omap
ceph -s
```

---

### bluestore_warn_on_no_per_pool_omap

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_warn_on_no_per_pool_omap](../../../config/global/bluestore.md#SP_bluestore_warn_on_no_per_pool_omap) |

**کارکرد:** Raise a health warning on lack of per-pool omap

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global bluestore_warn_on_no_per_pool_omap false
ceph config get global bluestore_warn_on_no_per_pool_omap
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_warn_on_no_per_pool_omap
ceph -s
```

---

### bluestore_warn_on_spurious_read_errors

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [bluestore.md#SP_bluestore_warn_on_spurious_read_errors](../../../config/global/bluestore.md#SP_bluestore_warn_on_spurious_read_errors) |

**کارکرد:** Raise a health warning when spurious read errors are observed by an OSD

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global bluestore_warn_on_spurious_read_errors false
ceph config get global bluestore_warn_on_spurious_read_errors
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_warn_on_spurious_read_errors
ceph -s
```

---

### bluestore_write_v2

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [bluestore.md#SP_bluestore_write_v2](../../../config/global/bluestore.md#SP_bluestore_write_v2) |

**کارکرد:** Use faster write path

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bluestore_write_v2 true
ceph config get global bluestore_write_v2
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_write_v2
ceph -s
```

---

### bluestore_write_v2_random

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [bluestore.md#SP_bluestore_write_v2_random](../../../config/global/bluestore.md#SP_bluestore_write_v2_random) |

**کارکرد:** Random selection of write path mode

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bluestore_write_v2_random true
ceph config get global bluestore_write_v2_random
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluestore_write_v2_random
ceph -s
```

---

### bluestore_zero_block_detection

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluestore.md#SP_bluestore_zero_block_detection](../../../config/global/bluestore.md#SP_bluestore_zero_block_detection) |

**کارکرد:** punch holes instead of writing zeros

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluestore_zero_block_detection true
ceph config get global bluestore_zero_block_detection
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
