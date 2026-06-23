# Bluestore

Global 配置深度指南 — 174 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [bluestore_2q_cache_kin_ratio](#bluestore_2q_cache_kin_ratio) | `0.5` | Dev | 开发 |
| [bluestore_2q_cache_kout_ratio](#bluestore_2q_cache_kout_ratio) | `0.5` | Dev | 开发 |
| [bluestore_alloc_stats_dump_interval](#bluestore_alloc_stats_dump_interval) | `1_day` | Dev | 开发 |
| [bluestore_allocation_from_file](#bluestore_allocation_from_file) | `True` | Dev | 开发 |
| [bluestore_allocation_recovery_threads](#bluestore_allocation_recovery_threads) | `0` | Basic | 性能 |
| [bluestore_allocator](#bluestore_allocator) | `hybrid` | Advanced | 性能 |
| [bluestore_allocator_lookup_policy](#bluestore_allocator_lookup_policy) | `auto` | Advanced | 性能 |
| [bluestore_async_db_compaction](#bluestore_async_db_compaction) | `True` | Dev | 开发 |
| [bluestore_avl_alloc_bf_free_pct](#bluestore_avl_alloc_bf_free_pct) | `4` | Dev | 开发 |
| [bluestore_avl_alloc_bf_threshold](#bluestore_avl_alloc_bf_threshold) | `128_K` | Dev | 开发 |
| [bluestore_avl_alloc_ff_max_search_bytes](#bluestore_avl_alloc_ff_max_search_bytes) | `16_M` | Dev | 开发 |
| [bluestore_avl_alloc_ff_max_search_count](#bluestore_avl_alloc_ff_max_search_count) | `100` | Dev | 开发 |
| [bluestore_bdev_label_multi](#bluestore_bdev_label_multi) | `True` | Advanced | 性能 |
| [bluestore_bdev_label_multi_upgrade](#bluestore_bdev_label_multi_upgrade) | `False` | Advanced | 性能 |
| [bluestore_bdev_label_require_all](#bluestore_bdev_label_require_all) | `True` | Advanced | 性能 |
| [bluestore_bitmapallocator_blocks_per_zone](#bluestore_bitmapallocator_blocks_per_zone) | `1_K` | Dev | 开发 |
| [bluestore_bitmapallocator_span_size](#bluestore_bitmapallocator_span_size) | `1_K` | Dev | 开发 |
| [bluestore_blobid_prealloc](#bluestore_blobid_prealloc) | `10_K` | Dev | 开发 |
| [bluestore_block_create](#bluestore_block_create) | `True` | Dev | 开发 |
| [bluestore_block_db_create](#bluestore_block_db_create) | `False` | Dev | 开发 |
| [bluestore_block_db_path](#bluestore_block_db_path) | `(empty)` | Dev | 开发 |
| [bluestore_block_db_size](#bluestore_block_db_size) | `0` | Dev | 开发 |
| [bluestore_block_path](#bluestore_block_path) | `(empty)` | Dev | 开发 |
| [bluestore_block_preallocate_file](#bluestore_block_preallocate_file) | `False` | Dev | 开发 |
| [bluestore_block_size](#bluestore_block_size) | `100_G` | Dev | 开发 |
| [bluestore_block_wal_create](#bluestore_block_wal_create) | `False` | Dev | 开发 |
| [bluestore_block_wal_path](#bluestore_block_wal_path) | `(empty)` | Dev | 开发 |
| [bluestore_block_wal_size](#bluestore_block_wal_size) | `96_M` | Dev | 开发 |
| [bluestore_bluefs](#bluestore_bluefs) | `True` | Dev | 开发 |
| [bluestore_bluefs_alloc_failure_dump_interval](#bluestore_bluefs_alloc_failure_dump_interval) | `0` | Advanced | 性能 |
| [bluestore_bluefs_env_mirror](#bluestore_bluefs_env_mirror) | `False` | Dev | 开发 |
| [bluestore_bluefs_max_free](#bluestore_bluefs_max_free) | `10_G` | Advanced | 性能 |
| [bluestore_bluefs_warn_ratio](#bluestore_bluefs_warn_ratio) | `0.06` | Basic | 策略 |
| [bluestore_btree2_alloc_weight_factor](#bluestore_btree2_alloc_weight_factor) | `2` | Dev | 开发 |
| [bluestore_cache_age_bin_interval](#bluestore_cache_age_bin_interval) | `1` | Dev | 开发 |
| [bluestore_cache_age_bins_data](#bluestore_cache_age_bins_data) | `1 2 6 24 120 720 0 0 0 0` | Dev | 开发 |
| [bluestore_cache_age_bins_kv](#bluestore_cache_age_bins_kv) | `1 2 6 24 120 720 0 0 0 0` | Dev | 开发 |
| [bluestore_cache_age_bins_kv_onode](#bluestore_cache_age_bins_kv_onode) | `0 0 0 0 0 0 0 0 0 720` | Dev | 开发 |
| [bluestore_cache_age_bins_meta](#bluestore_cache_age_bins_meta) | `1 2 6 24 120 720 0 0 0 0` | Dev | 开发 |
| [bluestore_cache_autotune](#bluestore_cache_autotune) | `True` | Dev | 开发 |
| [bluestore_cache_autotune_interval](#bluestore_cache_autotune_interval) | `5` | Dev | 开发 |
| [bluestore_cache_kv_onode_ratio](#bluestore_cache_kv_onode_ratio) | `0.04` | Dev | 开发 |
| [bluestore_cache_kv_ratio](#bluestore_cache_kv_ratio) | `0.45` | Dev | 开发 |
| [bluestore_cache_meta_evict_in_autotune](#bluestore_cache_meta_evict_in_autotune) | `True` | Advanced | 性能 |
| [bluestore_cache_meta_evict_limit](#bluestore_cache_meta_evict_limit) | `10` | Advanced | 性能 |
| [bluestore_cache_meta_ratio](#bluestore_cache_meta_ratio) | `0.45` | Dev | 开发 |
| [bluestore_cache_size](#bluestore_cache_size) | `0` | Dev | 开发 |
| [bluestore_cache_size_hdd](#bluestore_cache_size_hdd) | `1_G` | Dev | 开发 |
| [bluestore_cache_size_ssd](#bluestore_cache_size_ssd) | `3_G` | Dev | 开发 |
| [bluestore_cache_trim_interval](#bluestore_cache_trim_interval) | `0.05` | Advanced | 性能 |
| [bluestore_cache_trim_max_skip_pinned](#bluestore_cache_trim_max_skip_pinned) | `1000` | Dev | 开发 |
| [bluestore_cache_type](#bluestore_cache_type) | `2q` | Dev | 开发 |
| [bluestore_cleaner_sleep_interval](#bluestore_cleaner_sleep_interval) | `5` | Advanced | 性能 |
| [bluestore_clone_cow](#bluestore_clone_cow) | `True` | Advanced | 性能 |
| [bluestore_compression_algorithm](#bluestore_compression_algorithm) | `snappy` | Advanced | 性能 |
| [bluestore_compression_max_blob_size](#bluestore_compression_max_blob_size) | `0` | Advanced | 性能 |
| [bluestore_compression_max_blob_size_hdd](#bluestore_compression_max_blob_size_hdd) | `64_K` | Advanced | 性能 |
| [bluestore_compression_max_blob_size_ssd](#bluestore_compression_max_blob_size_ssd) | `64_K` | Advanced | 性能 |
| [bluestore_compression_min_blob_size](#bluestore_compression_min_blob_size) | `0` | Advanced | 性能 |
| [bluestore_compression_min_blob_size_hdd](#bluestore_compression_min_blob_size_hdd) | `64_K` | Advanced | 性能 |
| [bluestore_compression_min_blob_size_ssd](#bluestore_compression_min_blob_size_ssd) | `64_K` | Advanced | 性能 |
| [bluestore_compression_mode](#bluestore_compression_mode) | `none` | Advanced | 性能 |
| [bluestore_compression_required_ratio](#bluestore_compression_required_ratio) | `0.875` | Advanced | 性能 |
| [bluestore_csum_type](#bluestore_csum_type) | `crc32c` | Advanced | 性能 |
| [bluestore_debug_enforce_min_alloc_size](#bluestore_debug_enforce_min_alloc_size) | `0` | Dev | 开发 |
| [bluestore_debug_enforce_settings](#bluestore_debug_enforce_settings) | `default` | Dev | 开发 |
| [bluestore_debug_extent_map_encode_check](#bluestore_debug_extent_map_encode_check) | `False` | Dev | 开发 |
| [bluestore_debug_fast_recovery_compare_chance](#bluestore_debug_fast_recovery_compare_chance) | `0` | Dev | 开发 |
| [bluestore_debug_freelist](#bluestore_debug_freelist) | `False` | Dev | 开发 |
| [bluestore_debug_fsck_abort](#bluestore_debug_fsck_abort) | `False` | Dev | 开发 |
| [bluestore_debug_inject_allocation_from_file_failure](#bluestore_debug_inject_allocation_from_file_failure) | `0` | Dev | 开发 |
| [bluestore_debug_inject_csum_err_probability](#bluestore_debug_inject_csum_err_probability) | `0` | Dev | 开发 |
| [bluestore_debug_inject_read_err](#bluestore_debug_inject_read_err) | `False` | Dev | 开发 |
| [bluestore_debug_legacy_omap](#bluestore_debug_legacy_omap) | `False` | Dev | 开发 |
| [bluestore_debug_no_reuse_blocks](#bluestore_debug_no_reuse_blocks) | `False` | Dev | 开发 |
| [bluestore_debug_omit_block_device_write](#bluestore_debug_omit_block_device_write) | `False` | Dev | 开发 |
| [bluestore_debug_omit_kv_commit](#bluestore_debug_omit_kv_commit) | `False` | Dev | 开发 |
| [bluestore_debug_onode_segmentation_random](#bluestore_debug_onode_segmentation_random) | `False` | Dev | 开发 |
| [bluestore_debug_permit_any_bdev_label](#bluestore_debug_permit_any_bdev_label) | `False` | Dev | 开发 |
| [bluestore_debug_prefragment_max](#bluestore_debug_prefragment_max) | `1_M` | Dev | 开发 |
| [bluestore_debug_random_read_err](#bluestore_debug_random_read_err) | `0` | Dev | 开发 |
| [bluestore_debug_randomize_serial_transaction](#bluestore_debug_randomize_serial_transaction) | `0` | Dev | 开发 |
| [bluestore_debug_small_allocations](#bluestore_debug_small_allocations) | `0` | Dev | 开发 |
| [bluestore_debug_too_many_blobs_threshold](#bluestore_debug_too_many_blobs_threshold) | `24576` | Dev | 开发 |
| [bluestore_default_buffered_read](#bluestore_default_buffered_read) | `True` | Advanced | 性能 |
| [bluestore_default_buffered_write](#bluestore_default_buffered_write) | `False` | Advanced | 性能 |
| [bluestore_deferred_batch_ops](#bluestore_deferred_batch_ops) | `0` | Advanced | 性能 |
| [bluestore_deferred_batch_ops_hdd](#bluestore_deferred_batch_ops_hdd) | `64` | Advanced | 性能 |
| [bluestore_deferred_batch_ops_ssd](#bluestore_deferred_batch_ops_ssd) | `16` | Advanced | 性能 |
| [bluestore_discard_on_mkfs](#bluestore_discard_on_mkfs) | `True` | Advanced | 性能 |
| [bluestore_elastic_shared_blobs](#bluestore_elastic_shared_blobs) | `True` | Advanced | 性能 |
| [bluestore_extent_map_inline_shard_prealloc_size](#bluestore_extent_map_inline_shard_prealloc_size) | `256` | Dev | 开发 |
| [bluestore_extent_map_shard_max_size](#bluestore_extent_map_shard_max_size) | `1200` | Dev | 开发 |
| [bluestore_extent_map_shard_min_size](#bluestore_extent_map_shard_min_size) | `150` | Dev | 开发 |
| [bluestore_extent_map_shard_target_size](#bluestore_extent_map_shard_target_size) | `500` | Dev | 开发 |
| [bluestore_extent_map_shard_target_size_slop](#bluestore_extent_map_shard_target_size_slop) | `0.2` | Dev | 开发 |
| [bluestore_fail_eio](#bluestore_fail_eio) | `False` | Dev | 开发 |
| [bluestore_frag_runtime](#bluestore_frag_runtime) | `False` | Advanced | 性能 |
| [bluestore_frag_static](#bluestore_frag_static) | `False` | Advanced | 性能 |
| [bluestore_fragmentation_check_period](#bluestore_fragmentation_check_period) | `3600` | Basic | 策略 |
| [bluestore_freelist_blocks_per_key](#bluestore_freelist_blocks_per_key) | `128` | Dev | 开发 |
| [bluestore_fsck_error_on_no_per_pg_omap](#bluestore_fsck_error_on_no_per_pg_omap) | `False` | Advanced | 性能 |
| [bluestore_fsck_error_on_no_per_pool_omap](#bluestore_fsck_error_on_no_per_pool_omap) | `False` | Advanced | 性能 |
| [bluestore_fsck_error_on_no_per_pool_stats](#bluestore_fsck_error_on_no_per_pool_stats) | `False` | Advanced | 性能 |
| [bluestore_fsck_on_mkfs](#bluestore_fsck_on_mkfs) | `True` | Dev | 开发 |
| [bluestore_fsck_on_mkfs_deep](#bluestore_fsck_on_mkfs_deep) | `False` | Dev | 开发 |
| [bluestore_fsck_on_mount](#bluestore_fsck_on_mount) | `False` | Dev | 开发 |
| [bluestore_fsck_on_mount_deep](#bluestore_fsck_on_mount_deep) | `False` | Dev | 开发 |
| [bluestore_fsck_on_umount](#bluestore_fsck_on_umount) | `False` | Dev | 开发 |
| [bluestore_fsck_on_umount_deep](#bluestore_fsck_on_umount_deep) | `False` | Dev | 开发 |
| [bluestore_fsck_quick_fix_on_mount](#bluestore_fsck_quick_fix_on_mount) | `False` | Dev | 开发 |
| [bluestore_fsck_quick_fix_threads](#bluestore_fsck_quick_fix_threads) | `2` | Advanced | 性能 |
| [bluestore_fsck_read_bytes_cap](#bluestore_fsck_read_bytes_cap) | `64_M` | Advanced | 性能 |
| [bluestore_fsck_shared_blob_tracker_size](#bluestore_fsck_shared_blob_tracker_size) | `0.03125` | Dev | 开发 |
| [bluestore_gc_enable_blob_threshold](#bluestore_gc_enable_blob_threshold) | `0` | Dev | 开发 |
| [bluestore_gc_enable_total_threshold](#bluestore_gc_enable_total_threshold) | `0` | Dev | 开发 |
| [bluestore_hybrid_alloc_mem_cap](#bluestore_hybrid_alloc_mem_cap) | `64_M` | Dev | 开发 |
| [bluestore_ignore_data_csum](#bluestore_ignore_data_csum) | `False` | Dev | 开发 |
| [bluestore_kv_sync_util_logging_s](#bluestore_kv_sync_util_logging_s) | `10` | Advanced | 性能 |
| [bluestore_kvbackend](#bluestore_kvbackend) | `rocksdb` | Dev | 开发 |
| [bluestore_log_collection_list_age](#bluestore_log_collection_list_age) | `1_min` | Advanced | 性能 |
| [bluestore_log_omap_iterator_age](#bluestore_log_omap_iterator_age) | `5` | Advanced | 性能 |
| [bluestore_log_op_age](#bluestore_log_op_age) | `5` | Advanced | 性能 |
| [bluestore_log_scrub_op_age](#bluestore_log_scrub_op_age) | `5` | Advanced | 性能 |
| [bluestore_max_alloc_size](#bluestore_max_alloc_size) | `0` | Advanced | 性能 |
| [bluestore_max_blob_size](#bluestore_max_blob_size) | `0` | Dev | 开发 |
| [bluestore_max_blob_size_hdd](#bluestore_max_blob_size_hdd) | `64_K` | Dev | 开发 |
| [bluestore_max_blob_size_ssd](#bluestore_max_blob_size_ssd) | `64_K` | Dev | 开发 |
| [bluestore_max_defer_interval](#bluestore_max_defer_interval) | `3` | Advanced | 性能 |
| [bluestore_max_deferred_txc](#bluestore_max_deferred_txc) | `32` | Advanced | 性能 |
| [bluestore_min_alloc_size](#bluestore_min_alloc_size) | `0` | Advanced | 性能 |
| [bluestore_min_alloc_size_hdd](#bluestore_min_alloc_size_hdd) | `4_K` | Advanced | 性能 |
| [bluestore_min_alloc_size_ssd](#bluestore_min_alloc_size_ssd) | `4_K` | Advanced | 性能 |
| [bluestore_nid_prealloc](#bluestore_nid_prealloc) | `1024` | Dev | 开发 |
| [bluestore_onode_segment_size](#bluestore_onode_segment_size) | `0` | Advanced | 性能 |
| [bluestore_prefer_deferred_size](#bluestore_prefer_deferred_size) | `0` | Advanced | 性能 |
| [bluestore_prefer_deferred_size_hdd](#bluestore_prefer_deferred_size_hdd) | `64_K` | Advanced | 性能 |
| [bluestore_prefer_deferred_size_ssd](#bluestore_prefer_deferred_size_ssd) | `0` | Advanced | 性能 |
| [bluestore_qfsck_on_mount](#bluestore_qfsck_on_mount) | `True` | Dev | 开发 |
| [bluestore_recompression_min_gain](#bluestore_recompression_min_gain) | `1.2` | Advanced | 性能 |
| [bluestore_retry_disk_reads](#bluestore_retry_disk_reads) | `3` | Advanced | 性能 |
| [bluestore_rocksdb_cf](#bluestore_rocksdb_cf) | `True` | Advanced | 性能 |
| [bluestore_rocksdb_cfs](#bluestore_rocksdb_cfs) | `m(3) p(3,0-12) O(3,0-13)=block_cache={type=binned_lru} L=min_write_buffer_number_to_merge=32 P=min_write_buffer_number_to_merge=32` | Dev | 开发 |
| [bluestore_rocksdb_options](#bluestore_rocksdb_options) | `compression=kLZ4Compression,max_write_buffer_number=64,min_write_buffer_number_to_merge=6,compaction_style=kCompactionStyleLevel,write_buffer_size=16777216,max_background_jobs=4,level0_file_num_compaction_trigger=8,max_bytes_for_level_base=1073741824,max_bytes_for_level_multiplier=8,compaction_readahead_size=2MB,max_total_wal_size=1073741824,writable_file_max_buffer_size=0` | Advanced | 性能 |
| [bluestore_rocksdb_options_annex](#bluestore_rocksdb_options_annex) | `(empty)` | Advanced | 性能 |
| [bluestore_slow_ops_warn_lifetime](#bluestore_slow_ops_warn_lifetime) | `86400` | Advanced | 性能 |
| [bluestore_slow_ops_warn_threshold](#bluestore_slow_ops_warn_threshold) | `1` | Advanced | 性能 |
| [bluestore_slow_scrub_ops_warn_threshold](#bluestore_slow_scrub_ops_warn_threshold) | `1` | Advanced | 性能 |
| [bluestore_spdk_coremask](#bluestore_spdk_coremask) | `0x1` | Dev | 开发 |
| [bluestore_spdk_io_sleep](#bluestore_spdk_io_sleep) | `5` | Dev | 开发 |
| [bluestore_spdk_max_io_completion](#bluestore_spdk_max_io_completion) | `0` | Dev | 开发 |
| [bluestore_spdk_mem](#bluestore_spdk_mem) | `512` | Dev | 开发 |
| [bluestore_sync_submit_transaction](#bluestore_sync_submit_transaction) | `False` | Dev | 开发 |
| [bluestore_throttle_bytes](#bluestore_throttle_bytes) | `64_M` | Advanced | 性能 |
| [bluestore_throttle_cost_per_io](#bluestore_throttle_cost_per_io) | `0` | Advanced | 性能 |
| [bluestore_throttle_cost_per_io_hdd](#bluestore_throttle_cost_per_io_hdd) | `670000` | Advanced | 性能 |
| [bluestore_throttle_cost_per_io_ssd](#bluestore_throttle_cost_per_io_ssd) | `4000` | Advanced | 性能 |
| [bluestore_throttle_deferred_bytes](#bluestore_throttle_deferred_bytes) | `128_M` | Advanced | 性能 |
| [bluestore_throttle_trace_rate](#bluestore_throttle_trace_rate) | `0` | Advanced | 性能 |
| [bluestore_tracing](#bluestore_tracing) | `False` | Advanced | 性能 |
| [bluestore_use_ebd](#bluestore_use_ebd) | `True` | Advanced | 性能 |
| [bluestore_use_optimal_io_size_for_min_alloc_size](#bluestore_use_optimal_io_size_for_min_alloc_size) | `False` | Advanced | 性能 |
| [bluestore_volume_selection_policy](#bluestore_volume_selection_policy) | `use_some_extra` | Dev | 开发 |
| [bluestore_volume_selection_reserved](#bluestore_volume_selection_reserved) | `0` | Advanced | 性能 |
| [bluestore_volume_selection_reserved_factor](#bluestore_volume_selection_reserved_factor) | `2` | Advanced | 性能 |
| [bluestore_warn_on_bluefs_spillover](#bluestore_warn_on_bluefs_spillover) | `True` | Advanced | 性能 |
| [bluestore_warn_on_free_fragmentation](#bluestore_warn_on_free_fragmentation) | `0.8` | Basic | 策略 |
| [bluestore_warn_on_legacy_statfs](#bluestore_warn_on_legacy_statfs) | `True` | Advanced | 性能 |
| [bluestore_warn_on_no_per_pg_omap](#bluestore_warn_on_no_per_pg_omap) | `False` | Advanced | 性能 |
| [bluestore_warn_on_no_per_pool_omap](#bluestore_warn_on_no_per_pool_omap) | `True` | Advanced | 性能 |
| [bluestore_warn_on_spurious_read_errors](#bluestore_warn_on_spurious_read_errors) | `True` | Advanced | 性能 |
| [bluestore_write_v2](#bluestore_write_v2) | `False` | Advanced | 性能 |
| [bluestore_write_v2_random](#bluestore_write_v2_random) | `False` | Advanced | 性能 |
| [bluestore_zero_block_detection](#bluestore_zero_block_detection) | `False` | Dev | 开发 |

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

### bluestore_2q_cache_kin_ratio

| | |
|---|---|
| 类型 | Float · default `0.5` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_2q_cache_kin_ratio](../../../config/global/bluestore.md#SP_bluestore_2q_cache_kin_ratio) |

**作用：** 2Q paper suggests .5

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_2q_cache_kin_ratio 0.5
ceph config get global bluestore_2q_cache_kin_ratio
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0.5`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_2q_cache_kout_ratio

| | |
|---|---|
| 类型 | Float · default `0.5` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_2q_cache_kout_ratio](../../../config/global/bluestore.md#SP_bluestore_2q_cache_kout_ratio) |

**作用：** 2Q paper suggests .5

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_2q_cache_kout_ratio 0.5
ceph config get global bluestore_2q_cache_kout_ratio
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0.5`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_alloc_stats_dump_interval

| | |
|---|---|
| 类型 | Float · default `1_day` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_alloc_stats_dump_interval](../../../config/global/bluestore.md#SP_bluestore_alloc_stats_dump_interval) |

**作用：** The period (in second) for logging allocation statistics.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_alloc_stats_dump_interval 1_day
ceph config get global bluestore_alloc_stats_dump_interval
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1_day`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_allocation_from_file

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** · **STARTUP**（需重启） |
| 表格 | [bluestore.md#SP_bluestore_allocation_from_file](../../../config/global/bluestore.md#SP_bluestore_allocation_from_file) |

**作用：** Remove allocation info from RocksDB and store the info in a new allocation file

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_allocation_from_file false
ceph config get global bluestore_allocation_from_file
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_allocation_recovery_threads

| | |
|---|---|
| 类型 | Uint · default `0` · **Basic** · **STARTUP**（需重启） |
| 表格 | [bluestore.md#SP_bluestore_allocation_recovery_threads](../../../config/global/bluestore.md#SP_bluestore_allocation_recovery_threads) |

**作用：** Amount of threads for allocation recovery after OSD crash.

**何时使用：** 核心 Global 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set global bluestore_allocation_recovery_threads 64
ceph config get global bluestore_allocation_recovery_threads
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_allocation_recovery_threads
ceph -s
```

---

### bluestore_allocator

| | |
|---|---|
| 类型 | Str · enum: ["bitmap", "stupid", "avl", "btree", "hybrid", "hybrid_btree2"] · default `hybrid` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_allocator](../../../config/global/bluestore.md#SP_bluestore_allocator) |

**作用：** Allocator policy

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_allocator hybrid
ceph config get global bluestore_allocator
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `hybrid` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_allocator
ceph -s
```

---

### bluestore_allocator_lookup_policy

| | |
|---|---|
| 类型 | Str · enum: ["hdd_optimized", "ssd_optimized", "auto"] · default `auto` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_allocator_lookup_policy](../../../config/global/bluestore.md#SP_bluestore_allocator_lookup_policy) |

**作用：** Determines how to perform the next free extent lookup.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_allocator_lookup_policy auto
ceph config get global bluestore_allocator_lookup_policy
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `auto` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_allocator_lookup_policy
ceph -s
```

---

### bluestore_async_db_compaction

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_async_db_compaction](../../../config/global/bluestore.md#SP_bluestore_async_db_compaction) |

**作用：** Perform DB compaction requests asynchronously

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_async_db_compaction false
ceph config get global bluestore_async_db_compaction
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_avl_alloc_bf_free_pct

| | |
|---|---|
| 类型 | Uint · default `4` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_avl_alloc_bf_free_pct](../../../config/global/bluestore.md#SP_bluestore_avl_alloc_bf_free_pct) |

**作用：** Sets the threshold at which shrinking free space (in %, integer) triggers enabling best-fit mode.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_avl_alloc_bf_free_pct 4
ceph config get global bluestore_avl_alloc_bf_free_pct
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`4`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_avl_alloc_bf_threshold

| | |
|---|---|
| 类型 | Uint · default `128_K` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_avl_alloc_bf_threshold](../../../config/global/bluestore.md#SP_bluestore_avl_alloc_bf_threshold) |

**作用：** Sets threshold at which shrinking max free chunk size triggers enabling best-fit mode.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_avl_alloc_bf_threshold 128_K
ceph config get global bluestore_avl_alloc_bf_threshold
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`128_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_avl_alloc_ff_max_search_bytes

| | |
|---|---|
| 类型 | Size · default `16_M` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_avl_alloc_ff_max_search_bytes](../../../config/global/bluestore.md#SP_bluestore_avl_alloc_ff_max_search_bytes) |

**作用：** Maximum distance to search in first-fit mode before switching over to to best-fit mode. 0 to iterate through all ranges for required chunk.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_avl_alloc_ff_max_search_bytes 16_M
ceph config get global bluestore_avl_alloc_ff_max_search_bytes
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`16_M`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_avl_alloc_ff_max_search_count

| | |
|---|---|
| 类型 | Uint · default `100` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_avl_alloc_ff_max_search_count](../../../config/global/bluestore.md#SP_bluestore_avl_alloc_ff_max_search_count) |

**作用：** Search for this many ranges in first-fit mode before switching over to to best-fit mode. 0 to iterate through all ranges for required chunk.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_avl_alloc_ff_max_search_count 100
ceph config get global bluestore_avl_alloc_ff_max_search_count
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`100`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_bdev_label_multi

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_bdev_label_multi](../../../config/global/bluestore.md#SP_bluestore_bdev_label_multi) |

**作用：** Keep multiple copies of block device label.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global bluestore_bdev_label_multi false
ceph config get global bluestore_bdev_label_multi
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_bdev_label_multi
ceph -s
```

---

### bluestore_bdev_label_multi_upgrade

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [bluestore.md#SP_bluestore_bdev_label_multi_upgrade](../../../config/global/bluestore.md#SP_bluestore_bdev_label_multi_upgrade) |

**作用：** Let repair upgrade to multi label.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bluestore_bdev_label_multi_upgrade true
ceph config get global bluestore_bdev_label_multi_upgrade
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_bdev_label_multi_upgrade
ceph -s
```

---

### bluestore_bdev_label_require_all

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_bdev_label_require_all](../../../config/global/bluestore.md#SP_bluestore_bdev_label_require_all) |

**作用：** Require all copies to match.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global bluestore_bdev_label_require_all false
ceph config get global bluestore_bdev_label_require_all
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_bdev_label_require_all
ceph -s
```

---

### bluestore_bitmapallocator_blocks_per_zone

| | |
|---|---|
| 类型 | Size · default `1_K` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_bitmapallocator_blocks_per_zone](../../../config/global/bluestore.md#SP_bluestore_bitmapallocator_blocks_per_zone) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_bitmapallocator_blocks_per_zone 1_K
ceph config get global bluestore_bitmapallocator_blocks_per_zone
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_bitmapallocator_span_size

| | |
|---|---|
| 类型 | Size · default `1_K` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_bitmapallocator_span_size](../../../config/global/bluestore.md#SP_bluestore_bitmapallocator_span_size) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_bitmapallocator_span_size 1_K
ceph config get global bluestore_bitmapallocator_span_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_blobid_prealloc

| | |
|---|---|
| 类型 | Uint · default `10_K` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_blobid_prealloc](../../../config/global/bluestore.md#SP_bluestore_blobid_prealloc) |

**作用：** Number of unique blob IDs to preallocate at a time

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_blobid_prealloc 10_K
ceph config get global bluestore_blobid_prealloc
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`10_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_block_create

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_block_create](../../../config/global/bluestore.md#SP_bluestore_block_create) |

**作用：** Create bluestore_block_path if it doesn't exist

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_block_create false
ceph config get global bluestore_block_create
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_block_db_create

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_block_db_create](../../../config/global/bluestore.md#SP_bluestore_block_db_create) |

**作用：** Create bluestore_block_db_path if it doesn't exist

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_block_db_create true
ceph config get global bluestore_block_db_create
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_block_db_path

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_block_db_path](../../../config/global/bluestore.md#SP_bluestore_block_db_path) |

**作用：** Path for DB block device

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_block_db_path "/var/lib/ceph/example"
ceph config get global bluestore_block_db_path
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`(empty)`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_block_db_size

| | |
|---|---|
| 类型 | Size · default `0` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_block_db_size](../../../config/global/bluestore.md#SP_bluestore_block_db_size) |

**作用：** Size of file to create for bluestore_block_db_path

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_block_db_size 64
ceph config get global bluestore_block_db_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_block_path

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_block_path](../../../config/global/bluestore.md#SP_bluestore_block_path) |

**作用：** Path to block device/file

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_block_path "/var/lib/ceph/example"
ceph config get global bluestore_block_path
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`(empty)`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_block_preallocate_file

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_block_preallocate_file](../../../config/global/bluestore.md#SP_bluestore_block_preallocate_file) |

**作用：** Preallocate file created via bluestore_block*_create

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_block_preallocate_file true
ceph config get global bluestore_block_preallocate_file
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_block_size

| | |
|---|---|
| 类型 | Size · default `100_G` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_block_size](../../../config/global/bluestore.md#SP_bluestore_block_size) |

**作用：** Size of file to create for backing BlueStore

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_block_size 100_G
ceph config get global bluestore_block_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`100_G`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_block_wal_create

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_block_wal_create](../../../config/global/bluestore.md#SP_bluestore_block_wal_create) |

**作用：** Create bluestore_block_wal_path if it doesn't exist

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_block_wal_create true
ceph config get global bluestore_block_wal_create
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_block_wal_path

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_block_wal_path](../../../config/global/bluestore.md#SP_bluestore_block_wal_path) |

**作用：** Path to block device/file backing the BlueFS WAL

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_block_wal_path "/var/lib/ceph/example"
ceph config get global bluestore_block_wal_path
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`(empty)`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_block_wal_size

| | |
|---|---|
| 类型 | Size · default `96_M` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_block_wal_size](../../../config/global/bluestore.md#SP_bluestore_block_wal_size) |

**作用：** Size of file to create for bluestore_block_wal_path

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_block_wal_size 96_M
ceph config get global bluestore_block_wal_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`96_M`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_bluefs

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_bluefs](../../../config/global/bluestore.md#SP_bluestore_bluefs) |

**作用：** Use BlueFS to back RocksDB

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_bluefs false
ceph config get global bluestore_bluefs
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_bluefs_alloc_failure_dump_interval

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_bluefs_alloc_failure_dump_interval](../../../config/global/bluestore.md#SP_bluestore_bluefs_alloc_failure_dump_interval) |

**作用：** How frequently (in seconds) to dump allocator on BlueFS space allocation failure

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global bluestore_bluefs_alloc_failure_dump_interval 0
ceph config get global bluestore_bluefs_alloc_failure_dump_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_bluefs_alloc_failure_dump_interval
ceph -s
```

---

### bluestore_bluefs_env_mirror

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_bluefs_env_mirror](../../../config/global/bluestore.md#SP_bluestore_bluefs_env_mirror) |

**作用：** Mirror BlueFS data to file system for testing/validation

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_bluefs_env_mirror true
ceph config get global bluestore_bluefs_env_mirror
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_bluefs_max_free

| | |
|---|---|
| 类型 | Size · default `10_G` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_bluefs_max_free](../../../config/global/bluestore.md#SP_bluestore_bluefs_max_free) |

**作用：** Maximum free space allocated to BlueFS

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluestore_bluefs_max_free 10_G
ceph config get global bluestore_bluefs_max_free
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10_G` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_bluefs_max_free
ceph -s
```

---

### bluestore_bluefs_warn_ratio

| | |
|---|---|
| 类型 | Float · default `0.06` · **Basic** |
| 表格 | [bluestore.md#SP_bluestore_bluefs_warn_ratio](../../../config/global/bluestore.md#SP_bluestore_bluefs_warn_ratio) |

**作用：** The ratio at which BlueFS usage relative to the main device raises a health warning. Set to "1" to disable.

**何时使用：** 核心 Global 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set global bluestore_bluefs_warn_ratio 0.06
ceph config get global bluestore_bluefs_warn_ratio
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `0.06` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_bluefs_warn_ratio
ceph -s
```

---

### bluestore_btree2_alloc_weight_factor

| | |
|---|---|
| 类型 | Float · default `2` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_btree2_alloc_weight_factor](../../../config/global/bluestore.md#SP_bluestore_btree2_alloc_weight_factor) |

**作用：** Large continuous extents weight factor

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_btree2_alloc_weight_factor 2
ceph config get global bluestore_btree2_alloc_weight_factor
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`2`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_cache_age_bin_interval

| | |
|---|---|
| 类型 | Float · default `1` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_cache_age_bin_interval](../../../config/global/bluestore.md#SP_bluestore_cache_age_bin_interval) |

**作用：** The duration (in seconds) represented by a single cache age bin.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_cache_age_bin_interval 1
ceph config get global bluestore_cache_age_bin_interval
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_cache_age_bins_data

| | |
|---|---|
| 类型 | Str · default `1 2 6 24 120 720 0 0 0 0` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_cache_age_bins_data](../../../config/global/bluestore.md#SP_bluestore_cache_age_bins_data) |

**作用：** A 10 element, space separated list of age bins for data cache

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_cache_age_bins_data "1 2 6 24 120 720 0 0 0 0"
ceph config get global bluestore_cache_age_bins_data
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1 2 6 24 120 720 0 0 0 0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_cache_age_bins_kv

| | |
|---|---|
| 类型 | Str · default `1 2 6 24 120 720 0 0 0 0` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_cache_age_bins_kv](../../../config/global/bluestore.md#SP_bluestore_cache_age_bins_kv) |

**作用：** A 10 element, space separated list of age bins for kv cache

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_cache_age_bins_kv "1 2 6 24 120 720 0 0 0 0"
ceph config get global bluestore_cache_age_bins_kv
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1 2 6 24 120 720 0 0 0 0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_cache_age_bins_kv_onode

| | |
|---|---|
| 类型 | Str · default `0 0 0 0 0 0 0 0 0 720` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_cache_age_bins_kv_onode](../../../config/global/bluestore.md#SP_bluestore_cache_age_bins_kv_onode) |

**作用：** A 10 element, space separated list of age bins for kv onode cache

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_cache_age_bins_kv_onode "0 0 0 0 0 0 0 0 0 720"
ceph config get global bluestore_cache_age_bins_kv_onode
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0 0 0 0 0 0 0 0 0 720`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_cache_age_bins_meta

| | |
|---|---|
| 类型 | Str · default `1 2 6 24 120 720 0 0 0 0` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_cache_age_bins_meta](../../../config/global/bluestore.md#SP_bluestore_cache_age_bins_meta) |

**作用：** A 10 element, space separated list of age bins for onode cache

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_cache_age_bins_meta "1 2 6 24 120 720 0 0 0 0"
ceph config get global bluestore_cache_age_bins_meta
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1 2 6 24 120 720 0 0 0 0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_cache_autotune

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_cache_autotune](../../../config/global/bluestore.md#SP_bluestore_cache_autotune) |

**作用：** Automatically tune the ratio of caches while respecting min values.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_cache_autotune false
ceph config get global bluestore_cache_autotune
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_cache_autotune_interval

| | |
|---|---|
| 类型 | Float · default `5` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_cache_autotune_interval](../../../config/global/bluestore.md#SP_bluestore_cache_autotune_interval) |

**作用：** The number of seconds to wait between rebalances when cache autotune is enabled.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_cache_autotune_interval 5
ceph config get global bluestore_cache_autotune_interval
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`5`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_cache_kv_onode_ratio

| | |
|---|---|
| 类型 | Float · default `0.04` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_cache_kv_onode_ratio](../../../config/global/bluestore.md#SP_bluestore_cache_kv_onode_ratio) |

**作用：** Ratio of BlueStore cache to devote to key/value onode column family (rocksdb)

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_cache_kv_onode_ratio 0.04
ceph config get global bluestore_cache_kv_onode_ratio
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0.04`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_cache_kv_ratio

| | |
|---|---|
| 类型 | Float · default `0.45` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_cache_kv_ratio](../../../config/global/bluestore.md#SP_bluestore_cache_kv_ratio) |

**作用：** Ratio of BlueStore cache to devote to key/value database (RocksDB)

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_cache_kv_ratio 0.45
ceph config get global bluestore_cache_kv_ratio
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0.45`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_cache_meta_evict_in_autotune

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_cache_meta_evict_in_autotune](../../../config/global/bluestore.md#SP_bluestore_cache_meta_evict_in_autotune) |

**作用：** Controls eviction of onodes from cache shards as part of autotune. When enabled (true), right after autotune memory allocation run onode cache tries to adapt. Depending on `bluestore_cache_meta_evict_limit` either some or all excess onodes are evicted. When disabled (false), cluster inactivity makes cache to keep its onode elements.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global bluestore_cache_meta_evict_in_autotune false
ceph config get global bluestore_cache_meta_evict_in_autotune
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_cache_meta_evict_in_autotune
ceph -s
```

---

### bluestore_cache_meta_evict_limit

| | |
|---|---|
| 类型 | Int · default `10` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_cache_meta_evict_limit](../../../config/global/bluestore.md#SP_bluestore_cache_meta_evict_limit) |

**作用：** Elements in onode cache shards are evicted when new element is inserted into the cache. In rare cases of cluster inactivity cache can be reduced, but not evicted. Adjusting size at once will cause stall first time cache shard is accessed. The setting limits how many onodes can get evicted in one go. Any value is less than 2 it is treated as request to adjust immediately.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluestore_cache_meta_evict_limit 10
ceph config get global bluestore_cache_meta_evict_limit
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_cache_meta_evict_limit
ceph -s
```

---

### bluestore_cache_meta_ratio

| | |
|---|---|
| 类型 | Float · default `0.45` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_cache_meta_ratio](../../../config/global/bluestore.md#SP_bluestore_cache_meta_ratio) |

**作用：** Ratio of BlueStore cache to devote to metadata

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_cache_meta_ratio 0.45
ceph config get global bluestore_cache_meta_ratio
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0.45`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_cache_size

| | |
|---|---|
| 类型 | Size · default `0` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_cache_size](../../../config/global/bluestore.md#SP_bluestore_cache_size) |

**作用：** Cache size (in bytes) for BlueStore

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_cache_size 64
ceph config get global bluestore_cache_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_cache_size_hdd

| | |
|---|---|
| 类型 | Size · default `1_G` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_cache_size_hdd](../../../config/global/bluestore.md#SP_bluestore_cache_size_hdd) |

**作用：** Default bluestore_cache_size for rotational media

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_cache_size_hdd 1_G
ceph config get global bluestore_cache_size_hdd
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1_G`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_cache_size_ssd

| | |
|---|---|
| 类型 | Size · default `3_G` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_cache_size_ssd](../../../config/global/bluestore.md#SP_bluestore_cache_size_ssd) |

**作用：** Default bluestore_cache_size for non-rotational (solid state) media

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_cache_size_ssd 3_G
ceph config get global bluestore_cache_size_ssd
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`3_G`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_cache_trim_interval

| | |
|---|---|
| 类型 | Float · default `0.05` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_cache_trim_interval](../../../config/global/bluestore.md#SP_bluestore_cache_trim_interval) |

**作用：** How frequently we trim the bluestore cache

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global bluestore_cache_trim_interval 0.05
ceph config get global bluestore_cache_trim_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.05` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_cache_trim_interval
ceph -s
```

---

### bluestore_cache_trim_max_skip_pinned

| | |
|---|---|
| 类型 | Uint · default `1000` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_cache_trim_max_skip_pinned](../../../config/global/bluestore.md#SP_bluestore_cache_trim_max_skip_pinned) |

**作用：** Max pinned cache entries we consider before giving up

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_cache_trim_max_skip_pinned 1000
ceph config get global bluestore_cache_trim_max_skip_pinned
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1000`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_cache_type

| | |
|---|---|
| 类型 | Str · enum: ["2q", "lru"] · default `2q` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_cache_type](../../../config/global/bluestore.md#SP_bluestore_cache_type) |

**作用：** Cache replacement algorithm

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_cache_type 2q
ceph config get global bluestore_cache_type
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`2q`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_cleaner_sleep_interval

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_cleaner_sleep_interval](../../../config/global/bluestore.md#SP_bluestore_cleaner_sleep_interval) |

**作用：** How long the BlueStore cleaner should sleep before re-checking utilization

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global bluestore_cleaner_sleep_interval 5
ceph config get global bluestore_cleaner_sleep_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_cleaner_sleep_interval
ceph -s
```

---

### bluestore_clone_cow

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_clone_cow](../../../config/global/bluestore.md#SP_bluestore_clone_cow) |

**作用：** Use copy-on-write when cloning objects (versus reading and rewriting them at clone time)

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global bluestore_clone_cow false
ceph config get global bluestore_clone_cow
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_clone_cow
ceph -s
```

---

### bluestore_compression_algorithm

| | |
|---|---|
| 类型 | Str · enum: ["", "snappy", "zlib", "zstd", "lz4"] · default `snappy` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_compression_algorithm](../../../config/global/bluestore.md#SP_bluestore_compression_algorithm) |

**作用：** Default compression algorithm to use when writing object data

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_compression_algorithm snappy
ceph config get global bluestore_compression_algorithm
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `snappy` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_compression_algorithm
ceph -s
```

---

### bluestore_compression_max_blob_size

| | |
|---|---|
| 类型 | Size · default `0` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_compression_max_blob_size](../../../config/global/bluestore.md#SP_bluestore_compression_max_blob_size) |

**作用：** Maximum chunk size to apply compression to when non-random access is expected for an object.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluestore_compression_max_blob_size 64
ceph config get global bluestore_compression_max_blob_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_compression_max_blob_size
ceph -s
```

---

### bluestore_compression_max_blob_size_hdd

| | |
|---|---|
| 类型 | Size · default `64_K` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_compression_max_blob_size_hdd](../../../config/global/bluestore.md#SP_bluestore_compression_max_blob_size_hdd) |

**作用：** Default value of bluestore_compression_max_blob_size for rotational media

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluestore_compression_max_blob_size_hdd 64_K
ceph config get global bluestore_compression_max_blob_size_hdd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_compression_max_blob_size_hdd
ceph -s
```

---

### bluestore_compression_max_blob_size_ssd

| | |
|---|---|
| 类型 | Size · default `64_K` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_compression_max_blob_size_ssd](../../../config/global/bluestore.md#SP_bluestore_compression_max_blob_size_ssd) |

**作用：** Default value of bluestore_compression_max_blob_size for non-rotational (solid state) media

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluestore_compression_max_blob_size_ssd 64_K
ceph config get global bluestore_compression_max_blob_size_ssd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_compression_max_blob_size_ssd
ceph -s
```

---

### bluestore_compression_min_blob_size

| | |
|---|---|
| 类型 | Size · default `0` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_compression_min_blob_size](../../../config/global/bluestore.md#SP_bluestore_compression_min_blob_size) |

**作用：** Maximum chunk size to apply compression to when random access is expected for an object.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluestore_compression_min_blob_size 64
ceph config get global bluestore_compression_min_blob_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_compression_min_blob_size
ceph -s
```

---

### bluestore_compression_min_blob_size_hdd

| | |
|---|---|
| 类型 | Size · default `64_K` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_compression_min_blob_size_hdd](../../../config/global/bluestore.md#SP_bluestore_compression_min_blob_size_hdd) |

**作用：** Default value of bluestore_compression_min_blob_size for rotational media

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluestore_compression_min_blob_size_hdd 64_K
ceph config get global bluestore_compression_min_blob_size_hdd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_compression_min_blob_size_hdd
ceph -s
```

---

### bluestore_compression_min_blob_size_ssd

| | |
|---|---|
| 类型 | Size · default `64_K` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_compression_min_blob_size_ssd](../../../config/global/bluestore.md#SP_bluestore_compression_min_blob_size_ssd) |

**作用：** Default value of bluestore_compression_min_blob_size for non-rotational (solid state) media

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluestore_compression_min_blob_size_ssd 64_K
ceph config get global bluestore_compression_min_blob_size_ssd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_compression_min_blob_size_ssd
ceph -s
```

---

### bluestore_compression_mode

| | |
|---|---|
| 类型 | Str · enum: ["none", "passive", "aggressive", "force"] · default `none` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_compression_mode](../../../config/global/bluestore.md#SP_bluestore_compression_mode) |

**作用：** Default policy for using compression when pool does not specify

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_compression_mode none
ceph config get global bluestore_compression_mode
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `none` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_compression_mode
ceph -s
```

---

### bluestore_compression_required_ratio

| | |
|---|---|
| 类型 | Float · default `0.875` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_compression_required_ratio](../../../config/global/bluestore.md#SP_bluestore_compression_required_ratio) |

**作用：** Compression ratio required to store compressed data

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_compression_required_ratio 0.875
ceph config get global bluestore_compression_required_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.875` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_compression_required_ratio
ceph -s
```

---

### bluestore_csum_type

| | |
|---|---|
| 类型 | Str · enum: ["none", "crc32c", "crc32c_16", "crc32c_8", "xxhash32", "xxhash64"] · default `crc32c` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_csum_type](../../../config/global/bluestore.md#SP_bluestore_csum_type) |

**作用：** Default checksum algorithm to use

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_csum_type crc32c
ceph config get global bluestore_csum_type
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `crc32c` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_csum_type
ceph -s
```

---

### bluestore_debug_enforce_min_alloc_size

| | |
|---|---|
| 类型 | Uint · default `0` · **Dev** · **STARTUP**（需重启） |
| 表格 | [bluestore.md#SP_bluestore_debug_enforce_min_alloc_size](../../../config/global/bluestore.md#SP_bluestore_debug_enforce_min_alloc_size) |

**作用：** Enforces specific min_alloc size usages

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_enforce_min_alloc_size 64
ceph config get global bluestore_debug_enforce_min_alloc_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_enforce_settings

| | |
|---|---|
| 类型 | Str · enum: ["default", "hdd", "ssd"] · default `default` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_debug_enforce_settings](../../../config/global/bluestore.md#SP_bluestore_debug_enforce_settings) |

**作用：** Enforces specific hardware profile settings

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_enforce_settings default
ceph config get global bluestore_debug_enforce_settings
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`default`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_extent_map_encode_check

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** · **STARTUP**（需重启） |
| 表格 | [bluestore.md#SP_bluestore_debug_extent_map_encode_check](../../../config/global/bluestore.md#SP_bluestore_debug_extent_map_encode_check) |

**作用：** Check correctness of extents in encode_some

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_extent_map_encode_check true
ceph config get global bluestore_debug_extent_map_encode_check
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_fast_recovery_compare_chance

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** · **STARTUP**（需重启） |
| 表格 | [bluestore.md#SP_bluestore_debug_fast_recovery_compare_chance](../../../config/global/bluestore.md#SP_bluestore_debug_fast_recovery_compare_chance) |

**作用：** For testing only. Compare legacy and multithread allocation recovery.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_fast_recovery_compare_chance 0
ceph config get global bluestore_debug_fast_recovery_compare_chance
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_freelist

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_debug_freelist](../../../config/global/bluestore.md#SP_bluestore_debug_freelist) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_freelist true
ceph config get global bluestore_debug_freelist
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_fsck_abort

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_debug_fsck_abort](../../../config/global/bluestore.md#SP_bluestore_debug_fsck_abort) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_fsck_abort true
ceph config get global bluestore_debug_fsck_abort
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_inject_allocation_from_file_failure

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_debug_inject_allocation_from_file_failure](../../../config/global/bluestore.md#SP_bluestore_debug_inject_allocation_from_file_failure) |

**作用：** Enables random error injections when restoring allocation map from file.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_inject_allocation_from_file_failure 0
ceph config get global bluestore_debug_inject_allocation_from_file_failure
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_inject_csum_err_probability

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_debug_inject_csum_err_probability](../../../config/global/bluestore.md#SP_bluestore_debug_inject_csum_err_probability) |

**作用：** Inject CRC verification errors into BlueStore device reads

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_inject_csum_err_probability 0
ceph config get global bluestore_debug_inject_csum_err_probability
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_inject_read_err

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_debug_inject_read_err](../../../config/global/bluestore.md#SP_bluestore_debug_inject_read_err) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_inject_read_err true
ceph config get global bluestore_debug_inject_read_err
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_legacy_omap

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_debug_legacy_omap](../../../config/global/bluestore.md#SP_bluestore_debug_legacy_omap) |

**作用：** Allows mkfs to create OSDs with the legacy omap naming mode (neither per-pool nor per-pg). This is intended primarily for developers. The resulting OSDs might / would be transformed to the currrently default 'per-pg' format when BlueStore's quick-fix or repair are applied.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_legacy_omap true
ceph config get global bluestore_debug_legacy_omap
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_no_reuse_blocks

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_debug_no_reuse_blocks](../../../config/global/bluestore.md#SP_bluestore_debug_no_reuse_blocks) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_no_reuse_blocks true
ceph config get global bluestore_debug_no_reuse_blocks
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_omit_block_device_write

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_debug_omit_block_device_write](../../../config/global/bluestore.md#SP_bluestore_debug_omit_block_device_write) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_omit_block_device_write true
ceph config get global bluestore_debug_omit_block_device_write
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_omit_kv_commit

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_debug_omit_kv_commit](../../../config/global/bluestore.md#SP_bluestore_debug_omit_kv_commit) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_omit_kv_commit true
ceph config get global bluestore_debug_omit_kv_commit
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_onode_segmentation_random

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** · **STARTUP**（需重启） |
| 表格 | [bluestore.md#SP_bluestore_debug_onode_segmentation_random](../../../config/global/bluestore.md#SP_bluestore_debug_onode_segmentation_random) |

**作用：** Random selection of onode segmentation

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_onode_segmentation_random true
ceph config get global bluestore_debug_onode_segmentation_random
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_permit_any_bdev_label

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_debug_permit_any_bdev_label](../../../config/global/bluestore.md#SP_bluestore_debug_permit_any_bdev_label) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_permit_any_bdev_label true
ceph config get global bluestore_debug_permit_any_bdev_label
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_prefragment_max

| | |
|---|---|
| 类型 | Size · default `1_M` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_debug_prefragment_max](../../../config/global/bluestore.md#SP_bluestore_debug_prefragment_max) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_prefragment_max 1_M
ceph config get global bluestore_debug_prefragment_max
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1_M`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_random_read_err

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_debug_random_read_err](../../../config/global/bluestore.md#SP_bluestore_debug_random_read_err) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_random_read_err 0
ceph config get global bluestore_debug_random_read_err
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_randomize_serial_transaction

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_debug_randomize_serial_transaction](../../../config/global/bluestore.md#SP_bluestore_debug_randomize_serial_transaction) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_randomize_serial_transaction 64
ceph config get global bluestore_debug_randomize_serial_transaction
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_small_allocations

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_debug_small_allocations](../../../config/global/bluestore.md#SP_bluestore_debug_small_allocations) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_small_allocations 64
ceph config get global bluestore_debug_small_allocations
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_debug_too_many_blobs_threshold

| | |
|---|---|
| 类型 | Int · default `24576` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_debug_too_many_blobs_threshold](../../../config/global/bluestore.md#SP_bluestore_debug_too_many_blobs_threshold) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_debug_too_many_blobs_threshold 24576
ceph config get global bluestore_debug_too_many_blobs_threshold
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`24576`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_default_buffered_read

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_default_buffered_read](../../../config/global/bluestore.md#SP_bluestore_default_buffered_read) |

**作用：** Cache read results by default (unless hinted NOCACHE or WONTNEED)

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global bluestore_default_buffered_read false
ceph config get global bluestore_default_buffered_read
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_default_buffered_read
ceph -s
```

---

### bluestore_default_buffered_write

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_default_buffered_write](../../../config/global/bluestore.md#SP_bluestore_default_buffered_write) |

**作用：** Cache writes by default (unless hinted NOCACHE or WONTNEED)

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bluestore_default_buffered_write true
ceph config get global bluestore_default_buffered_write
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_default_buffered_write
ceph -s
```

---

### bluestore_deferred_batch_ops

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_deferred_batch_ops](../../../config/global/bluestore.md#SP_bluestore_deferred_batch_ops) |

**作用：** Max number of deferred writes before we flush the deferred write queue

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_deferred_batch_ops 64
ceph config get global bluestore_deferred_batch_ops
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `65535`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_deferred_batch_ops
ceph -s
```

---

### bluestore_deferred_batch_ops_hdd

| | |
|---|---|
| 类型 | Uint · default `64` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_deferred_batch_ops_hdd](../../../config/global/bluestore.md#SP_bluestore_deferred_batch_ops_hdd) |

**作用：** Default bluestore_deferred_batch_ops for rotational media (HDD)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_deferred_batch_ops_hdd 64
ceph config get global bluestore_deferred_batch_ops_hdd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `65535`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_deferred_batch_ops_hdd
ceph -s
```

---

### bluestore_deferred_batch_ops_ssd

| | |
|---|---|
| 类型 | Uint · default `16` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_deferred_batch_ops_ssd](../../../config/global/bluestore.md#SP_bluestore_deferred_batch_ops_ssd) |

**作用：** Default bluestore_deferred_batch_ops for non-rotational (SSD) media

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_deferred_batch_ops_ssd 16
ceph config get global bluestore_deferred_batch_ops_ssd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `16` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `65535`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_deferred_batch_ops_ssd
ceph -s
```

---

### bluestore_discard_on_mkfs

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_discard_on_mkfs](../../../config/global/bluestore.md#SP_bluestore_discard_on_mkfs) |

**作用：** Trim OSD devices after deployment

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global bluestore_discard_on_mkfs false
ceph config get global bluestore_discard_on_mkfs
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_discard_on_mkfs
ceph -s
```

---

### bluestore_elastic_shared_blobs

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_elastic_shared_blobs](../../../config/global/bluestore.md#SP_bluestore_elastic_shared_blobs) |

**作用：** Let BlueStore reuse existing shared blobs if possible

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global bluestore_elastic_shared_blobs false
ceph config get global bluestore_elastic_shared_blobs
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_elastic_shared_blobs
ceph -s
```

---

### bluestore_extent_map_inline_shard_prealloc_size

| | |
|---|---|
| 类型 | Size · default `256` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_extent_map_inline_shard_prealloc_size](../../../config/global/bluestore.md#SP_bluestore_extent_map_inline_shard_prealloc_size) |

**作用：** Preallocated buffer for inline shards

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_extent_map_inline_shard_prealloc_size 256
ceph config get global bluestore_extent_map_inline_shard_prealloc_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`256`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_extent_map_shard_max_size

| | |
|---|---|
| 类型 | Size · default `1200` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_extent_map_shard_max_size](../../../config/global/bluestore.md#SP_bluestore_extent_map_shard_max_size) |

**作用：** Max size (bytes) for a single extent map shard before splitting

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_extent_map_shard_max_size 1200
ceph config get global bluestore_extent_map_shard_max_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1200`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_extent_map_shard_min_size

| | |
|---|---|
| 类型 | Size · default `150` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_extent_map_shard_min_size](../../../config/global/bluestore.md#SP_bluestore_extent_map_shard_min_size) |

**作用：** Min size (bytes) for a single extent map shard before merging

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_extent_map_shard_min_size 150
ceph config get global bluestore_extent_map_shard_min_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`150`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_extent_map_shard_target_size

| | |
|---|---|
| 类型 | Size · default `500` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_extent_map_shard_target_size](../../../config/global/bluestore.md#SP_bluestore_extent_map_shard_target_size) |

**作用：** Target size (bytes) for a single extent map shard

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_extent_map_shard_target_size 500
ceph config get global bluestore_extent_map_shard_target_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`500`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_extent_map_shard_target_size_slop

| | |
|---|---|
| 类型 | Float · default `0.2` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_extent_map_shard_target_size_slop](../../../config/global/bluestore.md#SP_bluestore_extent_map_shard_target_size_slop) |

**作用：** Ratio above/below target for a shard when trying to align to an existing extent or blob boundary

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_extent_map_shard_target_size_slop 0.2
ceph config get global bluestore_extent_map_shard_target_size_slop
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0.2`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_fail_eio

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_fail_eio](../../../config/global/bluestore.md#SP_bluestore_fail_eio) |

**作用：** fail/crash on EIO

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_fail_eio true
ceph config get global bluestore_fail_eio
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_frag_runtime

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_frag_runtime](../../../config/global/bluestore.md#SP_bluestore_frag_runtime) |

**作用：** Enable tracking of runtime object fragmentation during reads.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bluestore_frag_runtime true
ceph config get global bluestore_frag_runtime
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_frag_runtime
ceph -s
```

---

### bluestore_frag_static

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_frag_static](../../../config/global/bluestore.md#SP_bluestore_frag_static) |

**作用：** Enable tracking of static object fragmentation during scrub

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bluestore_frag_static true
ceph config get global bluestore_frag_static
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_frag_static
ceph -s
```

---

### bluestore_fragmentation_check_period

| | |
|---|---|
| 类型 | Uint · default `3600` · **Basic** |
| 表格 | [bluestore.md#SP_bluestore_fragmentation_check_period](../../../config/global/bluestore.md#SP_bluestore_fragmentation_check_period) |

**作用：** The interval at which to perform a BlueStore free fragmentation check. Checking fragmentation is usually almost immediate. For highly fragmented storage, it can take several miliseconds and can cause a write operation to stall.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global bluestore_fragmentation_check_period 3600
ceph config get global bluestore_fragmentation_check_period
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `3600` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_fragmentation_check_period
ceph -s
```

---

### bluestore_freelist_blocks_per_key

| | |
|---|---|
| 类型 | Size · default `128` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_freelist_blocks_per_key](../../../config/global/bluestore.md#SP_bluestore_freelist_blocks_per_key) |

**作用：** Block (and bits) per database key

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_freelist_blocks_per_key 128
ceph config get global bluestore_freelist_blocks_per_key
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`128`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_fsck_error_on_no_per_pg_omap

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_fsck_error_on_no_per_pg_omap](../../../config/global/bluestore.md#SP_bluestore_fsck_error_on_no_per_pg_omap) |

**作用：** Throw a fsck error (instead of a warning) when objects without per-pg omap are found

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bluestore_fsck_error_on_no_per_pg_omap true
ceph config get global bluestore_fsck_error_on_no_per_pg_omap
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_fsck_error_on_no_per_pg_omap
ceph -s
```

---

### bluestore_fsck_error_on_no_per_pool_omap

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_fsck_error_on_no_per_pool_omap](../../../config/global/bluestore.md#SP_bluestore_fsck_error_on_no_per_pool_omap) |

**作用：** Throw a fsck error (instead of a warning) when objects without per-pool omap are found

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bluestore_fsck_error_on_no_per_pool_omap true
ceph config get global bluestore_fsck_error_on_no_per_pool_omap
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_fsck_error_on_no_per_pool_omap
ceph -s
```

---

### bluestore_fsck_error_on_no_per_pool_stats

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_fsck_error_on_no_per_pool_stats](../../../config/global/bluestore.md#SP_bluestore_fsck_error_on_no_per_pool_stats) |

**作用：** Direct that fsck throws an error (instead of raising a warning) when BlueStore OSDs lack per-pool stats, for example after an upgrade

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bluestore_fsck_error_on_no_per_pool_stats true
ceph config get global bluestore_fsck_error_on_no_per_pool_stats
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_fsck_error_on_no_per_pool_stats
ceph -s
```

---

### bluestore_fsck_on_mkfs

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_fsck_on_mkfs](../../../config/global/bluestore.md#SP_bluestore_fsck_on_mkfs) |

**作用：** Run fsck after mkfs

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_fsck_on_mkfs false
ceph config get global bluestore_fsck_on_mkfs
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_fsck_on_mkfs_deep

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_fsck_on_mkfs_deep](../../../config/global/bluestore.md#SP_bluestore_fsck_on_mkfs_deep) |

**作用：** Run deep fsck after mkfs

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_fsck_on_mkfs_deep true
ceph config get global bluestore_fsck_on_mkfs_deep
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_fsck_on_mount

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_fsck_on_mount](../../../config/global/bluestore.md#SP_bluestore_fsck_on_mount) |

**作用：** Run fsck at mount

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_fsck_on_mount true
ceph config get global bluestore_fsck_on_mount
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_fsck_on_mount_deep

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_fsck_on_mount_deep](../../../config/global/bluestore.md#SP_bluestore_fsck_on_mount_deep) |

**作用：** Run deep fsck at mount when bluestore_fsck_on_mount is set to true

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_fsck_on_mount_deep true
ceph config get global bluestore_fsck_on_mount_deep
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_fsck_on_umount

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_fsck_on_umount](../../../config/global/bluestore.md#SP_bluestore_fsck_on_umount) |

**作用：** Run fsck at umount

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_fsck_on_umount true
ceph config get global bluestore_fsck_on_umount
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_fsck_on_umount_deep

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_fsck_on_umount_deep](../../../config/global/bluestore.md#SP_bluestore_fsck_on_umount_deep) |

**作用：** Run deep fsck at umount when bluestore_fsck_on_umount is set to true

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_fsck_on_umount_deep true
ceph config get global bluestore_fsck_on_umount_deep
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_fsck_quick_fix_on_mount

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_fsck_quick_fix_on_mount](../../../config/global/bluestore.md#SP_bluestore_fsck_quick_fix_on_mount) |

**作用：** Do quick-fix for the store at mount

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_fsck_quick_fix_on_mount true
ceph config get global bluestore_fsck_quick_fix_on_mount
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_fsck_quick_fix_threads

| | |
|---|---|
| 类型 | Int · default `2` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_fsck_quick_fix_threads](../../../config/global/bluestore.md#SP_bluestore_fsck_quick_fix_threads) |

**作用：** Number of additional threads to perform quick-fix (shallow fsck) command

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_fsck_quick_fix_threads 2
ceph config get global bluestore_fsck_quick_fix_threads
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_fsck_quick_fix_threads
ceph -s
```

---

### bluestore_fsck_read_bytes_cap

| | |
|---|---|
| 类型 | Size · default `64_M` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_fsck_read_bytes_cap](../../../config/global/bluestore.md#SP_bluestore_fsck_read_bytes_cap) |

**作用：** Maximum bytes read at once by deep fsck

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluestore_fsck_read_bytes_cap 64_M
ceph config get global bluestore_fsck_read_bytes_cap
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_fsck_read_bytes_cap
ceph -s
```

---

### bluestore_fsck_shared_blob_tracker_size

| | |
|---|---|
| 类型 | Float · default `0.03125` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_fsck_shared_blob_tracker_size](../../../config/global/bluestore.md#SP_bluestore_fsck_shared_blob_tracker_size) |

**作用：** Size (a fraction of osd_memory_target, defaults to 128MB) of a hash table that tracks shared blob ref counts. A higher value makes the the tracker more precise and reduces overhead during repairs.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_fsck_shared_blob_tracker_size 0.03125
ceph config get global bluestore_fsck_shared_blob_tracker_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0.03125`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_gc_enable_blob_threshold

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_gc_enable_blob_threshold](../../../config/global/bluestore.md#SP_bluestore_gc_enable_blob_threshold) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_gc_enable_blob_threshold 64
ceph config get global bluestore_gc_enable_blob_threshold
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_gc_enable_total_threshold

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_gc_enable_total_threshold](../../../config/global/bluestore.md#SP_bluestore_gc_enable_total_threshold) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_gc_enable_total_threshold 64
ceph config get global bluestore_gc_enable_total_threshold
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_hybrid_alloc_mem_cap

| | |
|---|---|
| 类型 | Uint · default `64_M` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_hybrid_alloc_mem_cap](../../../config/global/bluestore.md#SP_bluestore_hybrid_alloc_mem_cap) |

**作用：** The maximum amount of memory the hybrid allocator should use before enabling bitmap supplement

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_hybrid_alloc_mem_cap 64_M
ceph config get global bluestore_hybrid_alloc_mem_cap
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`64_M`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_ignore_data_csum

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_ignore_data_csum](../../../config/global/bluestore.md#SP_bluestore_ignore_data_csum) |

**作用：** Ignore checksum errors on read and do not generate an EIO error

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_ignore_data_csum true
ceph config get global bluestore_ignore_data_csum
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_kv_sync_util_logging_s

| | |
|---|---|
| 类型 | Float · default `10` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_kv_sync_util_logging_s](../../../config/global/bluestore.md#SP_bluestore_kv_sync_util_logging_s) |

**作用：** KV sync thread utilization logging period

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_kv_sync_util_logging_s 10
ceph config get global bluestore_kv_sync_util_logging_s
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_kv_sync_util_logging_s
ceph -s
```

---

### bluestore_kvbackend

| | |
|---|---|
| 类型 | Str · default `rocksdb` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_kvbackend](../../../config/global/bluestore.md#SP_bluestore_kvbackend) |

**作用：** Key value database to use for BlueStore

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_kvbackend rocksdb
ceph config get global bluestore_kvbackend
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`rocksdb`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_log_collection_list_age

| | |
|---|---|
| 类型 | Float · default `1_min` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_log_collection_list_age](../../../config/global/bluestore.md#SP_bluestore_log_collection_list_age) |

**作用：** Log a collection list operation if it is slower than this age (seconds)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_log_collection_list_age 1_min
ceph config get global bluestore_log_collection_list_age
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_log_collection_list_age
ceph -s
```

---

### bluestore_log_omap_iterator_age

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_log_omap_iterator_age](../../../config/global/bluestore.md#SP_bluestore_log_omap_iterator_age) |

**作用：** Log an omap iteration operation if it is slower than this age (seconds)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_log_omap_iterator_age 5
ceph config get global bluestore_log_omap_iterator_age
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_log_omap_iterator_age
ceph -s
```

---

### bluestore_log_op_age

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_log_op_age](../../../config/global/bluestore.md#SP_bluestore_log_op_age) |

**作用：** Log a BlueStore operation if it is slower than this age (seconds)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_log_op_age 5
ceph config get global bluestore_log_op_age
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_log_op_age
ceph -s
```

---

### bluestore_log_scrub_op_age

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_log_scrub_op_age](../../../config/global/bluestore.md#SP_bluestore_log_scrub_op_age) |

**作用：** Log a BlueStore Scrub operation if it is slower than this age (seconds)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_log_scrub_op_age 5
ceph config get global bluestore_log_scrub_op_age
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_log_scrub_op_age
ceph -s
```

---

### bluestore_max_alloc_size

| | |
|---|---|
| 类型 | Size · default `0` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_max_alloc_size](../../../config/global/bluestore.md#SP_bluestore_max_alloc_size) |

**作用：** Maximum size of a single allocation (0 for no max)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluestore_max_alloc_size 64
ceph config get global bluestore_max_alloc_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_max_alloc_size
ceph -s
```

---

### bluestore_max_blob_size

| | |
|---|---|
| 类型 | Size · default `0` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_max_blob_size](../../../config/global/bluestore.md#SP_bluestore_max_blob_size) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_max_blob_size 64
ceph config get global bluestore_max_blob_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_max_blob_size_hdd

| | |
|---|---|
| 类型 | Size · default `64_K` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_max_blob_size_hdd](../../../config/global/bluestore.md#SP_bluestore_max_blob_size_hdd) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_max_blob_size_hdd 64_K
ceph config get global bluestore_max_blob_size_hdd
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`64_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_max_blob_size_ssd

| | |
|---|---|
| 类型 | Size · default `64_K` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_max_blob_size_ssd](../../../config/global/bluestore.md#SP_bluestore_max_blob_size_ssd) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_max_blob_size_ssd 64_K
ceph config get global bluestore_max_blob_size_ssd
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`64_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_max_defer_interval

| | |
|---|---|
| 类型 | Float · default `3` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_max_defer_interval](../../../config/global/bluestore.md#SP_bluestore_max_defer_interval) |

**作用：** Max duration to force deferred submit

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluestore_max_defer_interval 3
ceph config get global bluestore_max_defer_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_max_defer_interval
ceph -s
```

---

### bluestore_max_deferred_txc

| | |
|---|---|
| 类型 | Uint · default `32` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_max_deferred_txc](../../../config/global/bluestore.md#SP_bluestore_max_deferred_txc) |

**作用：** Max transactions with deferred writes that can accumulate before we force flush deferred writes

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluestore_max_deferred_txc 32
ceph config get global bluestore_max_deferred_txc
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `32` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_max_deferred_txc
ceph -s
```

---

### bluestore_min_alloc_size

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_min_alloc_size](../../../config/global/bluestore.md#SP_bluestore_min_alloc_size) |

**作用：** Minimum allocation size to allocate for an object

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluestore_min_alloc_size 64
ceph config get global bluestore_min_alloc_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_min_alloc_size
ceph -s
```

---

### bluestore_min_alloc_size_hdd

| | |
|---|---|
| 类型 | Size · default `4_K` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_min_alloc_size_hdd](../../../config/global/bluestore.md#SP_bluestore_min_alloc_size_hdd) |

**作用：** Default min_alloc_size value for rotational media

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluestore_min_alloc_size_hdd 4_K
ceph config get global bluestore_min_alloc_size_hdd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `4_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_min_alloc_size_hdd
ceph -s
```

---

### bluestore_min_alloc_size_ssd

| | |
|---|---|
| 类型 | Size · default `4_K` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_min_alloc_size_ssd](../../../config/global/bluestore.md#SP_bluestore_min_alloc_size_ssd) |

**作用：** Default min_alloc_size value for non-rotational (solid state) media

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluestore_min_alloc_size_ssd 4_K
ceph config get global bluestore_min_alloc_size_ssd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `4_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_min_alloc_size_ssd
ceph -s
```

---

### bluestore_nid_prealloc

| | |
|---|---|
| 类型 | Int · default `1024` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_nid_prealloc](../../../config/global/bluestore.md#SP_bluestore_nid_prealloc) |

**作用：** Number of unique object IDs to preallocate at a time

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_nid_prealloc 1024
ceph config get global bluestore_nid_prealloc
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1024`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_onode_segment_size

| | |
|---|---|
| 类型 | Size · default `0` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_onode_segment_size](../../../config/global/bluestore.md#SP_bluestore_onode_segment_size) |

**作用：** Size of segment for onode.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_onode_segment_size 64
ceph config get global bluestore_onode_segment_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_onode_segment_size
ceph -s
```

---

### bluestore_prefer_deferred_size

| | |
|---|---|
| 类型 | Size · default `0` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_prefer_deferred_size](../../../config/global/bluestore.md#SP_bluestore_prefer_deferred_size) |

**作用：** Writes smaller than this size will be written to the WAL and then asynchronously written to the block (slow) device. This can be beneficial when using rotational media where seeks are expensive, and is helpful both with and without SSD WAL. devices.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_prefer_deferred_size 64
ceph config get global bluestore_prefer_deferred_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_prefer_deferred_size
ceph -s
```

---

### bluestore_prefer_deferred_size_hdd

| | |
|---|---|
| 类型 | Size · default `64_K` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_prefer_deferred_size_hdd](../../../config/global/bluestore.md#SP_bluestore_prefer_deferred_size_hdd) |

**作用：** Default bluestore_prefer_deferred_size for rotational media

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_prefer_deferred_size_hdd 64_K
ceph config get global bluestore_prefer_deferred_size_hdd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_prefer_deferred_size_hdd
ceph -s
```

---

### bluestore_prefer_deferred_size_ssd

| | |
|---|---|
| 类型 | Size · default `0` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_prefer_deferred_size_ssd](../../../config/global/bluestore.md#SP_bluestore_prefer_deferred_size_ssd) |

**作用：** Default bluestore_prefer_deferred_size for non-rotational (SSD) media

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_prefer_deferred_size_ssd 64
ceph config get global bluestore_prefer_deferred_size_ssd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_prefer_deferred_size_ssd
ceph -s
```

---

### bluestore_qfsck_on_mount

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_qfsck_on_mount](../../../config/global/bluestore.md#SP_bluestore_qfsck_on_mount) |

**作用：** Run quick-fsck at mount comparing allocation-file to RocksDB allocation state

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_qfsck_on_mount false
ceph config get global bluestore_qfsck_on_mount
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_recompression_min_gain

| | |
|---|---|
| 类型 | Float · default `1.2` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_recompression_min_gain](../../../config/global/bluestore.md#SP_bluestore_recompression_min_gain) |

**作用：** Required estimated gain for accepting extents for recompressing.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluestore_recompression_min_gain 1.2
ceph config get global bluestore_recompression_min_gain
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1.2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_recompression_min_gain
ceph -s
```

---

### bluestore_retry_disk_reads

| | |
|---|---|
| 类型 | Uint · default `3` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_retry_disk_reads](../../../config/global/bluestore.md#SP_bluestore_retry_disk_reads) |

**作用：** Number of read retries on checksum validation error

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_retry_disk_reads 3
ceph config get global bluestore_retry_disk_reads
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `255`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_retry_disk_reads
ceph -s
```

---

### bluestore_rocksdb_cf

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_rocksdb_cf](../../../config/global/bluestore.md#SP_bluestore_rocksdb_cf) |

**作用：** Enable use of RocksDB column families for BlueStore metadata

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global bluestore_rocksdb_cf false
ceph config get global bluestore_rocksdb_cf
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_rocksdb_cf
ceph -s
```

---

### bluestore_rocksdb_cfs

| | |
|---|---|
| 类型 | Str · default `m(3) p(3,0-12) O(3,0-13)=block_cache={type=binned_lru} L=min_write_buffer_number_to_merge=32 P=min_write_buffer_number_to_merge=32` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_rocksdb_cfs](../../../config/global/bluestore.md#SP_bluestore_rocksdb_cfs) |

**作用：** Definition of column families and their sharding

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_rocksdb_cfs "m(3) p(3,0-12) O(3,0-13)=block_cache={type=binned_lru} L=min_write_buffer_number_to_merge=32 P=min_write_buffer_number_to_merge=32"
ceph config get global bluestore_rocksdb_cfs
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`m(3) p(3,0-12) O(3,0-13)=block_cache={type=binned_lru} L=min_write_buffer_number_to_merge=32 P=min_write_buffer_number_to_merge=32`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_rocksdb_options

| | |
|---|---|
| 类型 | Str · default `compression=kLZ4Compression,max_write_buffer_number=64,min_write_buffer_number_to_merge=6,compaction_style=kCompactionStyleLevel,write_buffer_size=16777216,max_background_jobs=4,level0_file_num_compaction_trigger=8,max_bytes_for_level_base=1073741824,max_bytes_for_level_multiplier=8,compaction_readahead_size=2MB,max_total_wal_size=1073741824,writable_file_max_buffer_size=0` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_rocksdb_options](../../../config/global/bluestore.md#SP_bluestore_rocksdb_options) |

**作用：** Full set of RocksDB settings to override

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_rocksdb_options "compression=kLZ4Compression,max_write_buffer_number=64,min_write_buffer_number_to_merge=6,compaction_style=kCompactionStyleLevel,write_buffer_size=16777216,max_background_jobs=4,level0_file_num_compaction_trigger=8,max_bytes_for_level_base=1073741824,max_bytes_for_level_multiplier=8,compaction_readahead_size=2MB,max_total_wal_size=1073741824,writable_file_max_buffer_size=0"
ceph config get global bluestore_rocksdb_options
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `compression=kLZ4Compression,max_write_buffer_number=64,min_write_buffer_number_to_merge=6,compaction_style=kCompactionStyleLevel,write_buffer_size=16777216,max_background_jobs=4,level0_file_num_compaction_trigger=8,max_bytes_for_level_base=1073741824,max_bytes_for_level_multiplier=8,compaction_readahead_size=2MB,max_total_wal_size=1073741824,writable_file_max_buffer_size=0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_rocksdb_options
ceph -s
```

---

### bluestore_rocksdb_options_annex

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_rocksdb_options_annex](../../../config/global/bluestore.md#SP_bluestore_rocksdb_options_annex) |

**作用：** An addition to bluestore_rocksdb_options. Allows setting RocksDB options without repeating the existing defaults.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_rocksdb_options_annex "example"
ceph config get global bluestore_rocksdb_options_annex
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_rocksdb_options_annex
ceph -s
```

---

### bluestore_slow_ops_warn_lifetime

| | |
|---|---|
| 类型 | Uint · default `86400` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_slow_ops_warn_lifetime](../../../config/global/bluestore.md#SP_bluestore_slow_ops_warn_lifetime) |

**作用：** Set the duration after which BlueStore slow ops warnings clear after being raised by exceeding the `bluestore_slow_ops_warn_threshold`. This is not the same as `osd_op_complaint_time`, which is about RADOS ops at the OSD level.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_slow_ops_warn_lifetime 86400
ceph config get global bluestore_slow_ops_warn_lifetime
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `86400` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_slow_ops_warn_lifetime
ceph -s
```

---

### bluestore_slow_ops_warn_threshold

| | |
|---|---|
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_slow_ops_warn_threshold](../../../config/global/bluestore.md#SP_bluestore_slow_ops_warn_threshold) |

**作用：** Set the minimum number of BlueStore slow ops before raising a health warning

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_slow_ops_warn_threshold 1
ceph config get global bluestore_slow_ops_warn_threshold
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_slow_ops_warn_threshold
ceph -s
```

---

### bluestore_slow_scrub_ops_warn_threshold

| | |
|---|---|
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_slow_scrub_ops_warn_threshold](../../../config/global/bluestore.md#SP_bluestore_slow_scrub_ops_warn_threshold) |

**作用：** Set the minimum number of BlueStore slow scrub ops before raising a health warning

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_slow_scrub_ops_warn_threshold 1
ceph config get global bluestore_slow_scrub_ops_warn_threshold
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_slow_scrub_ops_warn_threshold
ceph -s
```

---

### bluestore_spdk_coremask

| | |
|---|---|
| 类型 | Str · default `0x1` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_spdk_coremask](../../../config/global/bluestore.md#SP_bluestore_spdk_coremask) |

**作用：** A hexadecimal bit mask of the cores to run on. Note the core numbering can change between platforms and should be determined beforehand

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_spdk_coremask 0x1
ceph config get global bluestore_spdk_coremask
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0x1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_spdk_io_sleep

| | |
|---|---|
| 类型 | Uint · default `5` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_spdk_io_sleep](../../../config/global/bluestore.md#SP_bluestore_spdk_io_sleep) |

**作用：** Time period to wait if there is no completed I/O from polling

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_spdk_io_sleep 5
ceph config get global bluestore_spdk_io_sleep
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`5`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_spdk_max_io_completion

| | |
|---|---|
| 类型 | Uint · default `0` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_spdk_max_io_completion](../../../config/global/bluestore.md#SP_bluestore_spdk_max_io_completion) |

**作用：** Maximum number of operations to be batched completed while checking queue pair completions, 0 means to let the SPDK library determine the value

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_spdk_max_io_completion 64
ceph config get global bluestore_spdk_max_io_completion
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_spdk_mem

| | |
|---|---|
| 类型 | Size · default `512` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_spdk_mem](../../../config/global/bluestore.md#SP_bluestore_spdk_mem) |

**作用：** Amount of dpdk memory size in MB

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_spdk_mem 512
ceph config get global bluestore_spdk_mem
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`512`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_sync_submit_transaction

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_sync_submit_transaction](../../../config/global/bluestore.md#SP_bluestore_sync_submit_transaction) |

**作用：** Try to submit metadata transaction to RocksDB in queuing thread context

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_sync_submit_transaction true
ceph config get global bluestore_sync_submit_transaction
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_throttle_bytes

| | |
|---|---|
| 类型 | Size · default `64_M` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_throttle_bytes](../../../config/global/bluestore.md#SP_bluestore_throttle_bytes) |

**作用：** Maximum bytes in flight before we throttle IO submission

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_throttle_bytes 64_M
ceph config get global bluestore_throttle_bytes
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_throttle_bytes
ceph -s
```

---

### bluestore_throttle_cost_per_io

| | |
|---|---|
| 类型 | Size · default `0` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_throttle_cost_per_io](../../../config/global/bluestore.md#SP_bluestore_throttle_cost_per_io) |

**作用：** Overhead added to transaction cost (in bytes) for each IO

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_throttle_cost_per_io 64
ceph config get global bluestore_throttle_cost_per_io
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_throttle_cost_per_io
ceph -s
```

---

### bluestore_throttle_cost_per_io_hdd

| | |
|---|---|
| 类型 | Uint · default `670000` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_throttle_cost_per_io_hdd](../../../config/global/bluestore.md#SP_bluestore_throttle_cost_per_io_hdd) |

**作用：** Default bluestore_throttle_cost_per_io for rotational media (HDDs)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_throttle_cost_per_io_hdd 670000
ceph config get global bluestore_throttle_cost_per_io_hdd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `670000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_throttle_cost_per_io_hdd
ceph -s
```

---

### bluestore_throttle_cost_per_io_ssd

| | |
|---|---|
| 类型 | Uint · default `4000` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_throttle_cost_per_io_ssd](../../../config/global/bluestore.md#SP_bluestore_throttle_cost_per_io_ssd) |

**作用：** Default bluestore_throttle_cost_per_io for non-rotation (SSD) media

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_throttle_cost_per_io_ssd 4000
ceph config get global bluestore_throttle_cost_per_io_ssd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `4000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_throttle_cost_per_io_ssd
ceph -s
```

---

### bluestore_throttle_deferred_bytes

| | |
|---|---|
| 类型 | Size · default `128_M` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_throttle_deferred_bytes](../../../config/global/bluestore.md#SP_bluestore_throttle_deferred_bytes) |

**作用：** Maximum bytes for deferred writes before we throttle IO submission

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_throttle_deferred_bytes 128_M
ceph config get global bluestore_throttle_deferred_bytes
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `128_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_throttle_deferred_bytes
ceph -s
```

---

### bluestore_throttle_trace_rate

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_throttle_trace_rate](../../../config/global/bluestore.md#SP_bluestore_throttle_trace_rate) |

**作用：** Rate at which to sample BlueStore transactions (per second)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_throttle_trace_rate 0
ceph config get global bluestore_throttle_trace_rate
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_throttle_trace_rate
ceph -s
```

---

### bluestore_tracing

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_tracing](../../../config/global/bluestore.md#SP_bluestore_tracing) |

**作用：** Enable BlueStore event tracing.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bluestore_tracing true
ceph config get global bluestore_tracing
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_tracing
ceph -s
```

---

### bluestore_use_ebd

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_use_ebd](../../../config/global/bluestore.md#SP_bluestore_use_ebd) |

**作用：** EBD plugin used during mkfs is required for mounts.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global bluestore_use_ebd false
ceph config get global bluestore_use_ebd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_use_ebd
ceph -s
```

---

### bluestore_use_optimal_io_size_for_min_alloc_size

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_use_optimal_io_size_for_min_alloc_size](../../../config/global/bluestore.md#SP_bluestore_use_optimal_io_size_for_min_alloc_size) |

**作用：** Discover media optimal IO size and use for min_alloc_size. This is useful when OSDs are created on coarse-IU QLC SSDs or other novel types of underlyinng block device. It is a no-op for conventional media.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bluestore_use_optimal_io_size_for_min_alloc_size true
ceph config get global bluestore_use_optimal_io_size_for_min_alloc_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_use_optimal_io_size_for_min_alloc_size
ceph -s
```

---

### bluestore_volume_selection_policy

| | |
|---|---|
| 类型 | Str · enum: ["rocksdb_original", "use_some_extra", "use_some_extra_enforced", "fit_to_fast"] · default `use_some_extra` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_volume_selection_policy](../../../config/global/bluestore.md#SP_bluestore_volume_selection_policy) |

**作用：** Determine the BlueFS volume selection policy

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_volume_selection_policy use_some_extra
ceph config get global bluestore_volume_selection_policy
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`use_some_extra`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluestore_volume_selection_reserved

| | |
|---|---|
| 类型 | Int · default `0` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [bluestore.md#SP_bluestore_volume_selection_reserved](../../../config/global/bluestore.md#SP_bluestore_volume_selection_reserved) |

**作用：** Space reserved on the DB device and not allowed for 'use some extra' policy usage. Overrides the 'bluestore_volume_selection_reserved_factor' setting and introduces a straightforward limit.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_volume_selection_reserved 64
ceph config get global bluestore_volume_selection_reserved
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_volume_selection_reserved
ceph -s
```

---

### bluestore_volume_selection_reserved_factor

| | |
|---|---|
| 类型 | Float · default `2` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [bluestore.md#SP_bluestore_volume_selection_reserved_factor](../../../config/global/bluestore.md#SP_bluestore_volume_selection_reserved_factor) |

**作用：** RocksDB level size multiplier. Determines amount of space at DB device to bar from the usage when 'use some extra' policy is in action. The reserved size is determined by sum(L_max_size&#91;0&#93;, L_max_size&#91;L-1&#93;) + L_max_size&#91;L&#93; * this_factor

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluestore_volume_selection_reserved_factor 2
ceph config get global bluestore_volume_selection_reserved_factor
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_volume_selection_reserved_factor
ceph -s
```

---

### bluestore_warn_on_bluefs_spillover

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_warn_on_bluefs_spillover](../../../config/global/bluestore.md#SP_bluestore_warn_on_bluefs_spillover) |

**作用：** Raise a health warning on BlueFS slow device spillover

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global bluestore_warn_on_bluefs_spillover false
ceph config get global bluestore_warn_on_bluefs_spillover
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_warn_on_bluefs_spillover
ceph -s
```

---

### bluestore_warn_on_free_fragmentation

| | |
|---|---|
| 类型 | Float · default `0.8` · **Basic** |
| 表格 | [bluestore.md#SP_bluestore_warn_on_free_fragmentation](../../../config/global/bluestore.md#SP_bluestore_warn_on_free_fragmentation) |

**作用：** The level at which BlueStore block device free fragmentation raises a health warning. Set to "1" to disable. This is the value reported by the admin socket command "bluestore allocator score block".

**何时使用：** 核心 Global 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set global bluestore_warn_on_free_fragmentation 0.8
ceph config get global bluestore_warn_on_free_fragmentation
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `0.8` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_warn_on_free_fragmentation
ceph -s
```

---

### bluestore_warn_on_legacy_statfs

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_warn_on_legacy_statfs](../../../config/global/bluestore.md#SP_bluestore_warn_on_legacy_statfs) |

**作用：** Raise a health warning on the lack of per-pool statfs reporting from a BlueStore OSD

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global bluestore_warn_on_legacy_statfs false
ceph config get global bluestore_warn_on_legacy_statfs
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_warn_on_legacy_statfs
ceph -s
```

---

### bluestore_warn_on_no_per_pg_omap

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_warn_on_no_per_pg_omap](../../../config/global/bluestore.md#SP_bluestore_warn_on_no_per_pg_omap) |

**作用：** Raise a health warning on lack of per-pg omap

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bluestore_warn_on_no_per_pg_omap true
ceph config get global bluestore_warn_on_no_per_pg_omap
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_warn_on_no_per_pg_omap
ceph -s
```

---

### bluestore_warn_on_no_per_pool_omap

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_warn_on_no_per_pool_omap](../../../config/global/bluestore.md#SP_bluestore_warn_on_no_per_pool_omap) |

**作用：** Raise a health warning on lack of per-pool omap

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global bluestore_warn_on_no_per_pool_omap false
ceph config get global bluestore_warn_on_no_per_pool_omap
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_warn_on_no_per_pool_omap
ceph -s
```

---

### bluestore_warn_on_spurious_read_errors

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [bluestore.md#SP_bluestore_warn_on_spurious_read_errors](../../../config/global/bluestore.md#SP_bluestore_warn_on_spurious_read_errors) |

**作用：** Raise a health warning when spurious read errors are observed by an OSD

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global bluestore_warn_on_spurious_read_errors false
ceph config get global bluestore_warn_on_spurious_read_errors
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_warn_on_spurious_read_errors
ceph -s
```

---

### bluestore_write_v2

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [bluestore.md#SP_bluestore_write_v2](../../../config/global/bluestore.md#SP_bluestore_write_v2) |

**作用：** Use faster write path

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bluestore_write_v2 true
ceph config get global bluestore_write_v2
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_write_v2
ceph -s
```

---

### bluestore_write_v2_random

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [bluestore.md#SP_bluestore_write_v2_random](../../../config/global/bluestore.md#SP_bluestore_write_v2_random) |

**作用：** Random selection of write path mode

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bluestore_write_v2_random true
ceph config get global bluestore_write_v2_random
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluestore_write_v2_random
ceph -s
```

---

### bluestore_zero_block_detection

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluestore.md#SP_bluestore_zero_block_detection](../../../config/global/bluestore.md#SP_bluestore_zero_block_detection) |

**作用：** punch holes instead of writing zeros

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluestore_zero_block_detection true
ceph config get global bluestore_zero_block_detection
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
