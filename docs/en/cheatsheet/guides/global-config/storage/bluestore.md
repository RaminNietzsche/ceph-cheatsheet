# Bluestore

Global config deep dive — 174 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [bluestore_2q_cache_kin_ratio](#bluestore_2q_cache_kin_ratio) | `0.5` | Dev | Dev |
| [bluestore_2q_cache_kout_ratio](#bluestore_2q_cache_kout_ratio) | `0.5` | Dev | Dev |
| [bluestore_alloc_stats_dump_interval](#bluestore_alloc_stats_dump_interval) | `1_day` | Dev | Dev |
| [bluestore_allocation_from_file](#bluestore_allocation_from_file) | `True` | Dev | Dev |
| [bluestore_allocation_recovery_threads](#bluestore_allocation_recovery_threads) | `0` | Basic | Performance |
| [bluestore_allocator](#bluestore_allocator) | `hybrid` | Advanced | Performance |
| [bluestore_allocator_lookup_policy](#bluestore_allocator_lookup_policy) | `auto` | Advanced | Performance |
| [bluestore_async_db_compaction](#bluestore_async_db_compaction) | `True` | Dev | Dev |
| [bluestore_avl_alloc_bf_free_pct](#bluestore_avl_alloc_bf_free_pct) | `4` | Dev | Dev |
| [bluestore_avl_alloc_bf_threshold](#bluestore_avl_alloc_bf_threshold) | `128_K` | Dev | Dev |
| [bluestore_avl_alloc_ff_max_search_bytes](#bluestore_avl_alloc_ff_max_search_bytes) | `16_M` | Dev | Dev |
| [bluestore_avl_alloc_ff_max_search_count](#bluestore_avl_alloc_ff_max_search_count) | `100` | Dev | Dev |
| [bluestore_bdev_label_multi](#bluestore_bdev_label_multi) | `True` | Advanced | Performance |
| [bluestore_bdev_label_multi_upgrade](#bluestore_bdev_label_multi_upgrade) | `False` | Advanced | Performance |
| [bluestore_bdev_label_require_all](#bluestore_bdev_label_require_all) | `True` | Advanced | Performance |
| [bluestore_bitmapallocator_blocks_per_zone](#bluestore_bitmapallocator_blocks_per_zone) | `1_K` | Dev | Dev |
| [bluestore_bitmapallocator_span_size](#bluestore_bitmapallocator_span_size) | `1_K` | Dev | Dev |
| [bluestore_blobid_prealloc](#bluestore_blobid_prealloc) | `10_K` | Dev | Dev |
| [bluestore_block_create](#bluestore_block_create) | `True` | Dev | Dev |
| [bluestore_block_db_create](#bluestore_block_db_create) | `False` | Dev | Dev |
| [bluestore_block_db_path](#bluestore_block_db_path) | `(empty)` | Dev | Dev |
| [bluestore_block_db_size](#bluestore_block_db_size) | `0` | Dev | Dev |
| [bluestore_block_path](#bluestore_block_path) | `(empty)` | Dev | Dev |
| [bluestore_block_preallocate_file](#bluestore_block_preallocate_file) | `False` | Dev | Dev |
| [bluestore_block_size](#bluestore_block_size) | `100_G` | Dev | Dev |
| [bluestore_block_wal_create](#bluestore_block_wal_create) | `False` | Dev | Dev |
| [bluestore_block_wal_path](#bluestore_block_wal_path) | `(empty)` | Dev | Dev |
| [bluestore_block_wal_size](#bluestore_block_wal_size) | `96_M` | Dev | Dev |
| [bluestore_bluefs](#bluestore_bluefs) | `True` | Dev | Dev |
| [bluestore_bluefs_alloc_failure_dump_interval](#bluestore_bluefs_alloc_failure_dump_interval) | `0` | Advanced | Performance |
| [bluestore_bluefs_env_mirror](#bluestore_bluefs_env_mirror) | `False` | Dev | Dev |
| [bluestore_bluefs_max_free](#bluestore_bluefs_max_free) | `10_G` | Advanced | Performance |
| [bluestore_bluefs_warn_ratio](#bluestore_bluefs_warn_ratio) | `0.06` | Basic | Policy |
| [bluestore_btree2_alloc_weight_factor](#bluestore_btree2_alloc_weight_factor) | `2` | Dev | Dev |
| [bluestore_cache_age_bin_interval](#bluestore_cache_age_bin_interval) | `1` | Dev | Dev |
| [bluestore_cache_age_bins_data](#bluestore_cache_age_bins_data) | `1 2 6 24 120 720 0 0 0 0` | Dev | Dev |
| [bluestore_cache_age_bins_kv](#bluestore_cache_age_bins_kv) | `1 2 6 24 120 720 0 0 0 0` | Dev | Dev |
| [bluestore_cache_age_bins_kv_onode](#bluestore_cache_age_bins_kv_onode) | `0 0 0 0 0 0 0 0 0 720` | Dev | Dev |
| [bluestore_cache_age_bins_meta](#bluestore_cache_age_bins_meta) | `1 2 6 24 120 720 0 0 0 0` | Dev | Dev |
| [bluestore_cache_autotune](#bluestore_cache_autotune) | `True` | Dev | Dev |
| [bluestore_cache_autotune_interval](#bluestore_cache_autotune_interval) | `5` | Dev | Dev |
| [bluestore_cache_kv_onode_ratio](#bluestore_cache_kv_onode_ratio) | `0.04` | Dev | Dev |
| [bluestore_cache_kv_ratio](#bluestore_cache_kv_ratio) | `0.45` | Dev | Dev |
| [bluestore_cache_meta_evict_in_autotune](#bluestore_cache_meta_evict_in_autotune) | `True` | Advanced | Performance |
| [bluestore_cache_meta_evict_limit](#bluestore_cache_meta_evict_limit) | `10` | Advanced | Performance |
| [bluestore_cache_meta_ratio](#bluestore_cache_meta_ratio) | `0.45` | Dev | Dev |
| [bluestore_cache_size](#bluestore_cache_size) | `0` | Dev | Dev |
| [bluestore_cache_size_hdd](#bluestore_cache_size_hdd) | `1_G` | Dev | Dev |
| [bluestore_cache_size_ssd](#bluestore_cache_size_ssd) | `3_G` | Dev | Dev |
| [bluestore_cache_trim_interval](#bluestore_cache_trim_interval) | `0.05` | Advanced | Performance |
| [bluestore_cache_trim_max_skip_pinned](#bluestore_cache_trim_max_skip_pinned) | `1000` | Dev | Dev |
| [bluestore_cache_type](#bluestore_cache_type) | `2q` | Dev | Dev |
| [bluestore_cleaner_sleep_interval](#bluestore_cleaner_sleep_interval) | `5` | Advanced | Performance |
| [bluestore_clone_cow](#bluestore_clone_cow) | `True` | Advanced | Performance |
| [bluestore_compression_algorithm](#bluestore_compression_algorithm) | `snappy` | Advanced | Performance |
| [bluestore_compression_max_blob_size](#bluestore_compression_max_blob_size) | `0` | Advanced | Performance |
| [bluestore_compression_max_blob_size_hdd](#bluestore_compression_max_blob_size_hdd) | `64_K` | Advanced | Performance |
| [bluestore_compression_max_blob_size_ssd](#bluestore_compression_max_blob_size_ssd) | `64_K` | Advanced | Performance |
| [bluestore_compression_min_blob_size](#bluestore_compression_min_blob_size) | `0` | Advanced | Performance |
| [bluestore_compression_min_blob_size_hdd](#bluestore_compression_min_blob_size_hdd) | `64_K` | Advanced | Performance |
| [bluestore_compression_min_blob_size_ssd](#bluestore_compression_min_blob_size_ssd) | `64_K` | Advanced | Performance |
| [bluestore_compression_mode](#bluestore_compression_mode) | `none` | Advanced | Performance |
| [bluestore_compression_required_ratio](#bluestore_compression_required_ratio) | `0.875` | Advanced | Performance |
| [bluestore_csum_type](#bluestore_csum_type) | `crc32c` | Advanced | Performance |
| [bluestore_debug_enforce_min_alloc_size](#bluestore_debug_enforce_min_alloc_size) | `0` | Dev | Dev |
| [bluestore_debug_enforce_settings](#bluestore_debug_enforce_settings) | `default` | Dev | Dev |
| [bluestore_debug_extent_map_encode_check](#bluestore_debug_extent_map_encode_check) | `False` | Dev | Dev |
| [bluestore_debug_fast_recovery_compare_chance](#bluestore_debug_fast_recovery_compare_chance) | `0` | Dev | Dev |
| [bluestore_debug_freelist](#bluestore_debug_freelist) | `False` | Dev | Dev |
| [bluestore_debug_fsck_abort](#bluestore_debug_fsck_abort) | `False` | Dev | Dev |
| [bluestore_debug_inject_allocation_from_file_failure](#bluestore_debug_inject_allocation_from_file_failure) | `0` | Dev | Dev |
| [bluestore_debug_inject_csum_err_probability](#bluestore_debug_inject_csum_err_probability) | `0` | Dev | Dev |
| [bluestore_debug_inject_read_err](#bluestore_debug_inject_read_err) | `False` | Dev | Dev |
| [bluestore_debug_legacy_omap](#bluestore_debug_legacy_omap) | `False` | Dev | Dev |
| [bluestore_debug_no_reuse_blocks](#bluestore_debug_no_reuse_blocks) | `False` | Dev | Dev |
| [bluestore_debug_omit_block_device_write](#bluestore_debug_omit_block_device_write) | `False` | Dev | Dev |
| [bluestore_debug_omit_kv_commit](#bluestore_debug_omit_kv_commit) | `False` | Dev | Dev |
| [bluestore_debug_onode_segmentation_random](#bluestore_debug_onode_segmentation_random) | `False` | Dev | Dev |
| [bluestore_debug_permit_any_bdev_label](#bluestore_debug_permit_any_bdev_label) | `False` | Dev | Dev |
| [bluestore_debug_prefragment_max](#bluestore_debug_prefragment_max) | `1_M` | Dev | Dev |
| [bluestore_debug_random_read_err](#bluestore_debug_random_read_err) | `0` | Dev | Dev |
| [bluestore_debug_randomize_serial_transaction](#bluestore_debug_randomize_serial_transaction) | `0` | Dev | Dev |
| [bluestore_debug_small_allocations](#bluestore_debug_small_allocations) | `0` | Dev | Dev |
| [bluestore_debug_too_many_blobs_threshold](#bluestore_debug_too_many_blobs_threshold) | `24576` | Dev | Dev |
| [bluestore_default_buffered_read](#bluestore_default_buffered_read) | `True` | Advanced | Performance |
| [bluestore_default_buffered_write](#bluestore_default_buffered_write) | `False` | Advanced | Performance |
| [bluestore_deferred_batch_ops](#bluestore_deferred_batch_ops) | `0` | Advanced | Performance |
| [bluestore_deferred_batch_ops_hdd](#bluestore_deferred_batch_ops_hdd) | `64` | Advanced | Performance |
| [bluestore_deferred_batch_ops_ssd](#bluestore_deferred_batch_ops_ssd) | `16` | Advanced | Performance |
| [bluestore_discard_on_mkfs](#bluestore_discard_on_mkfs) | `True` | Advanced | Performance |
| [bluestore_elastic_shared_blobs](#bluestore_elastic_shared_blobs) | `True` | Advanced | Performance |
| [bluestore_extent_map_inline_shard_prealloc_size](#bluestore_extent_map_inline_shard_prealloc_size) | `256` | Dev | Dev |
| [bluestore_extent_map_shard_max_size](#bluestore_extent_map_shard_max_size) | `1200` | Dev | Dev |
| [bluestore_extent_map_shard_min_size](#bluestore_extent_map_shard_min_size) | `150` | Dev | Dev |
| [bluestore_extent_map_shard_target_size](#bluestore_extent_map_shard_target_size) | `500` | Dev | Dev |
| [bluestore_extent_map_shard_target_size_slop](#bluestore_extent_map_shard_target_size_slop) | `0.2` | Dev | Dev |
| [bluestore_fail_eio](#bluestore_fail_eio) | `False` | Dev | Dev |
| [bluestore_frag_runtime](#bluestore_frag_runtime) | `False` | Advanced | Performance |
| [bluestore_frag_static](#bluestore_frag_static) | `False` | Advanced | Performance |
| [bluestore_fragmentation_check_period](#bluestore_fragmentation_check_period) | `3600` | Basic | Policy |
| [bluestore_freelist_blocks_per_key](#bluestore_freelist_blocks_per_key) | `128` | Dev | Dev |
| [bluestore_fsck_error_on_no_per_pg_omap](#bluestore_fsck_error_on_no_per_pg_omap) | `False` | Advanced | Performance |
| [bluestore_fsck_error_on_no_per_pool_omap](#bluestore_fsck_error_on_no_per_pool_omap) | `False` | Advanced | Performance |
| [bluestore_fsck_error_on_no_per_pool_stats](#bluestore_fsck_error_on_no_per_pool_stats) | `False` | Advanced | Performance |
| [bluestore_fsck_on_mkfs](#bluestore_fsck_on_mkfs) | `True` | Dev | Dev |
| [bluestore_fsck_on_mkfs_deep](#bluestore_fsck_on_mkfs_deep) | `False` | Dev | Dev |
| [bluestore_fsck_on_mount](#bluestore_fsck_on_mount) | `False` | Dev | Dev |
| [bluestore_fsck_on_mount_deep](#bluestore_fsck_on_mount_deep) | `False` | Dev | Dev |
| [bluestore_fsck_on_umount](#bluestore_fsck_on_umount) | `False` | Dev | Dev |
| [bluestore_fsck_on_umount_deep](#bluestore_fsck_on_umount_deep) | `False` | Dev | Dev |
| [bluestore_fsck_quick_fix_on_mount](#bluestore_fsck_quick_fix_on_mount) | `False` | Dev | Dev |
| [bluestore_fsck_quick_fix_threads](#bluestore_fsck_quick_fix_threads) | `2` | Advanced | Performance |
| [bluestore_fsck_read_bytes_cap](#bluestore_fsck_read_bytes_cap) | `64_M` | Advanced | Performance |
| [bluestore_fsck_shared_blob_tracker_size](#bluestore_fsck_shared_blob_tracker_size) | `0.03125` | Dev | Dev |
| [bluestore_gc_enable_blob_threshold](#bluestore_gc_enable_blob_threshold) | `0` | Dev | Dev |
| [bluestore_gc_enable_total_threshold](#bluestore_gc_enable_total_threshold) | `0` | Dev | Dev |
| [bluestore_hybrid_alloc_mem_cap](#bluestore_hybrid_alloc_mem_cap) | `64_M` | Dev | Dev |
| [bluestore_ignore_data_csum](#bluestore_ignore_data_csum) | `False` | Dev | Dev |
| [bluestore_kv_sync_util_logging_s](#bluestore_kv_sync_util_logging_s) | `10` | Advanced | Performance |
| [bluestore_kvbackend](#bluestore_kvbackend) | `rocksdb` | Dev | Dev |
| [bluestore_log_collection_list_age](#bluestore_log_collection_list_age) | `1_min` | Advanced | Performance |
| [bluestore_log_omap_iterator_age](#bluestore_log_omap_iterator_age) | `5` | Advanced | Performance |
| [bluestore_log_op_age](#bluestore_log_op_age) | `5` | Advanced | Performance |
| [bluestore_log_scrub_op_age](#bluestore_log_scrub_op_age) | `5` | Advanced | Performance |
| [bluestore_max_alloc_size](#bluestore_max_alloc_size) | `0` | Advanced | Performance |
| [bluestore_max_blob_size](#bluestore_max_blob_size) | `0` | Dev | Dev |
| [bluestore_max_blob_size_hdd](#bluestore_max_blob_size_hdd) | `64_K` | Dev | Dev |
| [bluestore_max_blob_size_ssd](#bluestore_max_blob_size_ssd) | `64_K` | Dev | Dev |
| [bluestore_max_defer_interval](#bluestore_max_defer_interval) | `3` | Advanced | Performance |
| [bluestore_max_deferred_txc](#bluestore_max_deferred_txc) | `32` | Advanced | Performance |
| [bluestore_min_alloc_size](#bluestore_min_alloc_size) | `0` | Advanced | Performance |
| [bluestore_min_alloc_size_hdd](#bluestore_min_alloc_size_hdd) | `4_K` | Advanced | Performance |
| [bluestore_min_alloc_size_ssd](#bluestore_min_alloc_size_ssd) | `4_K` | Advanced | Performance |
| [bluestore_nid_prealloc](#bluestore_nid_prealloc) | `1024` | Dev | Dev |
| [bluestore_onode_segment_size](#bluestore_onode_segment_size) | `0` | Advanced | Performance |
| [bluestore_prefer_deferred_size](#bluestore_prefer_deferred_size) | `0` | Advanced | Performance |
| [bluestore_prefer_deferred_size_hdd](#bluestore_prefer_deferred_size_hdd) | `64_K` | Advanced | Performance |
| [bluestore_prefer_deferred_size_ssd](#bluestore_prefer_deferred_size_ssd) | `0` | Advanced | Performance |
| [bluestore_qfsck_on_mount](#bluestore_qfsck_on_mount) | `True` | Dev | Dev |
| [bluestore_recompression_min_gain](#bluestore_recompression_min_gain) | `1.2` | Advanced | Performance |
| [bluestore_retry_disk_reads](#bluestore_retry_disk_reads) | `3` | Advanced | Performance |
| [bluestore_rocksdb_cf](#bluestore_rocksdb_cf) | `True` | Advanced | Performance |
| [bluestore_rocksdb_cfs](#bluestore_rocksdb_cfs) | `m(3) p(3,0-12) O(3,0-13)=block_cache={type=binned_lru} L=min_write_buffer_number_to_merge=32 P=min_write_buffer_number_to_merge=32` | Dev | Dev |
| [bluestore_rocksdb_options](#bluestore_rocksdb_options) | `compression=kLZ4Compression,max_write_buffer_number=64,min_write_buffer_number_to_merge=6,compaction_style=kCompactionStyleLevel,write_buffer_size=16777216,max_background_jobs=4,level0_file_num_compaction_trigger=8,max_bytes_for_level_base=1073741824,max_bytes_for_level_multiplier=8,compaction_readahead_size=2MB,max_total_wal_size=1073741824,writable_file_max_buffer_size=0` | Advanced | Performance |
| [bluestore_rocksdb_options_annex](#bluestore_rocksdb_options_annex) | `(empty)` | Advanced | Performance |
| [bluestore_slow_ops_warn_lifetime](#bluestore_slow_ops_warn_lifetime) | `86400` | Advanced | Performance |
| [bluestore_slow_ops_warn_threshold](#bluestore_slow_ops_warn_threshold) | `1` | Advanced | Performance |
| [bluestore_slow_scrub_ops_warn_threshold](#bluestore_slow_scrub_ops_warn_threshold) | `1` | Advanced | Performance |
| [bluestore_spdk_coremask](#bluestore_spdk_coremask) | `0x1` | Dev | Dev |
| [bluestore_spdk_io_sleep](#bluestore_spdk_io_sleep) | `5` | Dev | Dev |
| [bluestore_spdk_max_io_completion](#bluestore_spdk_max_io_completion) | `0` | Dev | Dev |
| [bluestore_spdk_mem](#bluestore_spdk_mem) | `512` | Dev | Dev |
| [bluestore_sync_submit_transaction](#bluestore_sync_submit_transaction) | `False` | Dev | Dev |
| [bluestore_throttle_bytes](#bluestore_throttle_bytes) | `64_M` | Advanced | Performance |
| [bluestore_throttle_cost_per_io](#bluestore_throttle_cost_per_io) | `0` | Advanced | Performance |
| [bluestore_throttle_cost_per_io_hdd](#bluestore_throttle_cost_per_io_hdd) | `670000` | Advanced | Performance |
| [bluestore_throttle_cost_per_io_ssd](#bluestore_throttle_cost_per_io_ssd) | `4000` | Advanced | Performance |
| [bluestore_throttle_deferred_bytes](#bluestore_throttle_deferred_bytes) | `128_M` | Advanced | Performance |
| [bluestore_throttle_trace_rate](#bluestore_throttle_trace_rate) | `0` | Advanced | Performance |
| [bluestore_tracing](#bluestore_tracing) | `False` | Advanced | Performance |
| [bluestore_use_ebd](#bluestore_use_ebd) | `True` | Advanced | Performance |
| [bluestore_use_optimal_io_size_for_min_alloc_size](#bluestore_use_optimal_io_size_for_min_alloc_size) | `False` | Advanced | Performance |
| [bluestore_volume_selection_policy](#bluestore_volume_selection_policy) | `use_some_extra` | Dev | Dev |
| [bluestore_volume_selection_reserved](#bluestore_volume_selection_reserved) | `0` | Advanced | Performance |
| [bluestore_volume_selection_reserved_factor](#bluestore_volume_selection_reserved_factor) | `2` | Advanced | Performance |
| [bluestore_warn_on_bluefs_spillover](#bluestore_warn_on_bluefs_spillover) | `True` | Advanced | Performance |
| [bluestore_warn_on_free_fragmentation](#bluestore_warn_on_free_fragmentation) | `0.8` | Basic | Policy |
| [bluestore_warn_on_legacy_statfs](#bluestore_warn_on_legacy_statfs) | `True` | Advanced | Performance |
| [bluestore_warn_on_no_per_pg_omap](#bluestore_warn_on_no_per_pg_omap) | `False` | Advanced | Performance |
| [bluestore_warn_on_no_per_pool_omap](#bluestore_warn_on_no_per_pool_omap) | `True` | Advanced | Performance |
| [bluestore_warn_on_spurious_read_errors](#bluestore_warn_on_spurious_read_errors) | `True` | Advanced | Performance |
| [bluestore_write_v2](#bluestore_write_v2) | `False` | Advanced | Performance |
| [bluestore_write_v2_random](#bluestore_write_v2_random) | `False` | Advanced | Performance |
| [bluestore_zero_block_detection](#bluestore_zero_block_detection) | `False` | Dev | Dev |

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

### bluestore_2q_cache_kin_ratio

| | |
|---|---|
| Type | Float · default `0.5` · **Dev** |
| Table | [bluestore.md#SP_bluestore_2q_cache_kin_ratio](../../../config/global/bluestore.md#SP_bluestore_2q_cache_kin_ratio) |

**What it does:** 2Q paper suggests .5

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_2q_cache_kin_ratio 0.5
ceph config get global bluestore_2q_cache_kin_ratio
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.5`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_2q_cache_kout_ratio

| | |
|---|---|
| Type | Float · default `0.5` · **Dev** |
| Table | [bluestore.md#SP_bluestore_2q_cache_kout_ratio](../../../config/global/bluestore.md#SP_bluestore_2q_cache_kout_ratio) |

**What it does:** 2Q paper suggests .5

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_2q_cache_kout_ratio 0.5
ceph config get global bluestore_2q_cache_kout_ratio
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.5`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_alloc_stats_dump_interval

| | |
|---|---|
| Type | Float · default `1_day` · **Dev** |
| Table | [bluestore.md#SP_bluestore_alloc_stats_dump_interval](../../../config/global/bluestore.md#SP_bluestore_alloc_stats_dump_interval) |

**What it does:** The period (in second) for logging allocation statistics.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_alloc_stats_dump_interval 1_day
ceph config get global bluestore_alloc_stats_dump_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1_day`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_allocation_from_file

| | |
|---|---|
| Type | Bool · default `True` · **Dev** · **STARTUP** (restart required) |
| Table | [bluestore.md#SP_bluestore_allocation_from_file](../../../config/global/bluestore.md#SP_bluestore_allocation_from_file) |

**What it does:** Remove allocation info from RocksDB and store the info in a new allocation file

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_allocation_from_file false
ceph config get global bluestore_allocation_from_file
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_allocation_recovery_threads

| | |
|---|---|
| Type | Uint · default `0` · **Basic** · **STARTUP** (restart required) |
| Table | [bluestore.md#SP_bluestore_allocation_recovery_threads](../../../config/global/bluestore.md#SP_bluestore_allocation_recovery_threads) |

**What it does:** Amount of threads for allocation recovery after OSD crash.

**When to use:** Core Global behavior — review before changing in production.

**Example:**

```bash
ceph config set global bluestore_allocation_recovery_threads 64
ceph config get global bluestore_allocation_recovery_threads
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_allocation_recovery_threads
ceph -s
```

---

### bluestore_allocator

| | |
|---|---|
| Type | Str · enum: ["bitmap", "stupid", "avl", "btree", "hybrid", "hybrid_btree2"] · default `hybrid` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_allocator](../../../config/global/bluestore.md#SP_bluestore_allocator) |

**What it does:** Allocator policy

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_allocator hybrid
ceph config get global bluestore_allocator
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `hybrid`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_allocator
ceph -s
```

---

### bluestore_allocator_lookup_policy

| | |
|---|---|
| Type | Str · enum: ["hdd_optimized", "ssd_optimized", "auto"] · default `auto` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_allocator_lookup_policy](../../../config/global/bluestore.md#SP_bluestore_allocator_lookup_policy) |

**What it does:** Determines how to perform the next free extent lookup.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_allocator_lookup_policy auto
ceph config get global bluestore_allocator_lookup_policy
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `auto`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_allocator_lookup_policy
ceph -s
```

---

### bluestore_async_db_compaction

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [bluestore.md#SP_bluestore_async_db_compaction](../../../config/global/bluestore.md#SP_bluestore_async_db_compaction) |

**What it does:** Perform DB compaction requests asynchronously

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_async_db_compaction false
ceph config get global bluestore_async_db_compaction
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_avl_alloc_bf_free_pct

| | |
|---|---|
| Type | Uint · default `4` · **Dev** |
| Table | [bluestore.md#SP_bluestore_avl_alloc_bf_free_pct](../../../config/global/bluestore.md#SP_bluestore_avl_alloc_bf_free_pct) |

**What it does:** Sets the threshold at which shrinking free space (in %, integer) triggers enabling best-fit mode.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_avl_alloc_bf_free_pct 4
ceph config get global bluestore_avl_alloc_bf_free_pct
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`4`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_avl_alloc_bf_threshold

| | |
|---|---|
| Type | Uint · default `128_K` · **Dev** |
| Table | [bluestore.md#SP_bluestore_avl_alloc_bf_threshold](../../../config/global/bluestore.md#SP_bluestore_avl_alloc_bf_threshold) |

**What it does:** Sets threshold at which shrinking max free chunk size triggers enabling best-fit mode.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_avl_alloc_bf_threshold 128_K
ceph config get global bluestore_avl_alloc_bf_threshold
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`128_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_avl_alloc_ff_max_search_bytes

| | |
|---|---|
| Type | Size · default `16_M` · **Dev** |
| Table | [bluestore.md#SP_bluestore_avl_alloc_ff_max_search_bytes](../../../config/global/bluestore.md#SP_bluestore_avl_alloc_ff_max_search_bytes) |

**What it does:** Maximum distance to search in first-fit mode before switching over to to best-fit mode. 0 to iterate through all ranges for required chunk.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_avl_alloc_ff_max_search_bytes 16_M
ceph config get global bluestore_avl_alloc_ff_max_search_bytes
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`16_M`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_avl_alloc_ff_max_search_count

| | |
|---|---|
| Type | Uint · default `100` · **Dev** |
| Table | [bluestore.md#SP_bluestore_avl_alloc_ff_max_search_count](../../../config/global/bluestore.md#SP_bluestore_avl_alloc_ff_max_search_count) |

**What it does:** Search for this many ranges in first-fit mode before switching over to to best-fit mode. 0 to iterate through all ranges for required chunk.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_avl_alloc_ff_max_search_count 100
ceph config get global bluestore_avl_alloc_ff_max_search_count
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`100`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_bdev_label_multi

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_bdev_label_multi](../../../config/global/bluestore.md#SP_bluestore_bdev_label_multi) |

**What it does:** Keep multiple copies of block device label.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global bluestore_bdev_label_multi false
ceph config get global bluestore_bdev_label_multi
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_bdev_label_multi
ceph -s
```

---

### bluestore_bdev_label_multi_upgrade

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** · **STARTUP** (restart required) |
| Table | [bluestore.md#SP_bluestore_bdev_label_multi_upgrade](../../../config/global/bluestore.md#SP_bluestore_bdev_label_multi_upgrade) |

**What it does:** Let repair upgrade to multi label.

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bluestore_bdev_label_multi_upgrade true
ceph config get global bluestore_bdev_label_multi_upgrade
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_bdev_label_multi_upgrade
ceph -s
```

---

### bluestore_bdev_label_require_all

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_bdev_label_require_all](../../../config/global/bluestore.md#SP_bluestore_bdev_label_require_all) |

**What it does:** Require all copies to match.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global bluestore_bdev_label_require_all false
ceph config get global bluestore_bdev_label_require_all
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_bdev_label_require_all
ceph -s
```

---

### bluestore_bitmapallocator_blocks_per_zone

| | |
|---|---|
| Type | Size · default `1_K` · **Dev** |
| Table | [bluestore.md#SP_bluestore_bitmapallocator_blocks_per_zone](../../../config/global/bluestore.md#SP_bluestore_bitmapallocator_blocks_per_zone) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_bitmapallocator_blocks_per_zone 1_K
ceph config get global bluestore_bitmapallocator_blocks_per_zone
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_bitmapallocator_span_size

| | |
|---|---|
| Type | Size · default `1_K` · **Dev** |
| Table | [bluestore.md#SP_bluestore_bitmapallocator_span_size](../../../config/global/bluestore.md#SP_bluestore_bitmapallocator_span_size) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_bitmapallocator_span_size 1_K
ceph config get global bluestore_bitmapallocator_span_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_blobid_prealloc

| | |
|---|---|
| Type | Uint · default `10_K` · **Dev** |
| Table | [bluestore.md#SP_bluestore_blobid_prealloc](../../../config/global/bluestore.md#SP_bluestore_blobid_prealloc) |

**What it does:** Number of unique blob IDs to preallocate at a time

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_blobid_prealloc 10_K
ceph config get global bluestore_blobid_prealloc
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`10_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_block_create

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [bluestore.md#SP_bluestore_block_create](../../../config/global/bluestore.md#SP_bluestore_block_create) |

**What it does:** Create bluestore_block_path if it doesn't exist

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_block_create false
ceph config get global bluestore_block_create
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_block_db_create

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_block_db_create](../../../config/global/bluestore.md#SP_bluestore_block_db_create) |

**What it does:** Create bluestore_block_db_path if it doesn't exist

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_block_db_create true
ceph config get global bluestore_block_db_create
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_block_db_path

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** |
| Table | [bluestore.md#SP_bluestore_block_db_path](../../../config/global/bluestore.md#SP_bluestore_block_db_path) |

**What it does:** Path for DB block device

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_block_db_path "/var/lib/ceph/example"
ceph config get global bluestore_block_db_path
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`(empty)`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_block_db_size

| | |
|---|---|
| Type | Size · default `0` · **Dev** |
| Table | [bluestore.md#SP_bluestore_block_db_size](../../../config/global/bluestore.md#SP_bluestore_block_db_size) |

**What it does:** Size of file to create for bluestore_block_db_path

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_block_db_size 64
ceph config get global bluestore_block_db_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_block_path

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** |
| Table | [bluestore.md#SP_bluestore_block_path](../../../config/global/bluestore.md#SP_bluestore_block_path) |

**What it does:** Path to block device/file

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_block_path "/var/lib/ceph/example"
ceph config get global bluestore_block_path
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`(empty)`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_block_preallocate_file

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_block_preallocate_file](../../../config/global/bluestore.md#SP_bluestore_block_preallocate_file) |

**What it does:** Preallocate file created via bluestore_block*_create

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_block_preallocate_file true
ceph config get global bluestore_block_preallocate_file
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_block_size

| | |
|---|---|
| Type | Size · default `100_G` · **Dev** |
| Table | [bluestore.md#SP_bluestore_block_size](../../../config/global/bluestore.md#SP_bluestore_block_size) |

**What it does:** Size of file to create for backing BlueStore

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_block_size 100_G
ceph config get global bluestore_block_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`100_G`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_block_wal_create

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_block_wal_create](../../../config/global/bluestore.md#SP_bluestore_block_wal_create) |

**What it does:** Create bluestore_block_wal_path if it doesn't exist

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_block_wal_create true
ceph config get global bluestore_block_wal_create
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_block_wal_path

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** |
| Table | [bluestore.md#SP_bluestore_block_wal_path](../../../config/global/bluestore.md#SP_bluestore_block_wal_path) |

**What it does:** Path to block device/file backing the BlueFS WAL

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_block_wal_path "/var/lib/ceph/example"
ceph config get global bluestore_block_wal_path
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`(empty)`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_block_wal_size

| | |
|---|---|
| Type | Size · default `96_M` · **Dev** |
| Table | [bluestore.md#SP_bluestore_block_wal_size](../../../config/global/bluestore.md#SP_bluestore_block_wal_size) |

**What it does:** Size of file to create for bluestore_block_wal_path

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_block_wal_size 96_M
ceph config get global bluestore_block_wal_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`96_M`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_bluefs

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [bluestore.md#SP_bluestore_bluefs](../../../config/global/bluestore.md#SP_bluestore_bluefs) |

**What it does:** Use BlueFS to back RocksDB

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_bluefs false
ceph config get global bluestore_bluefs
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_bluefs_alloc_failure_dump_interval

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_bluefs_alloc_failure_dump_interval](../../../config/global/bluestore.md#SP_bluestore_bluefs_alloc_failure_dump_interval) |

**What it does:** How frequently (in seconds) to dump allocator on BlueFS space allocation failure

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global bluestore_bluefs_alloc_failure_dump_interval 0
ceph config get global bluestore_bluefs_alloc_failure_dump_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_bluefs_alloc_failure_dump_interval
ceph -s
```

---

### bluestore_bluefs_env_mirror

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_bluefs_env_mirror](../../../config/global/bluestore.md#SP_bluestore_bluefs_env_mirror) |

**What it does:** Mirror BlueFS data to file system for testing/validation

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_bluefs_env_mirror true
ceph config get global bluestore_bluefs_env_mirror
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_bluefs_max_free

| | |
|---|---|
| Type | Size · default `10_G` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_bluefs_max_free](../../../config/global/bluestore.md#SP_bluestore_bluefs_max_free) |

**What it does:** Maximum free space allocated to BlueFS

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluestore_bluefs_max_free 10_G
ceph config get global bluestore_bluefs_max_free
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10_G`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_bluefs_max_free
ceph -s
```

---

### bluestore_bluefs_warn_ratio

| | |
|---|---|
| Type | Float · default `0.06` · **Basic** |
| Table | [bluestore.md#SP_bluestore_bluefs_warn_ratio](../../../config/global/bluestore.md#SP_bluestore_bluefs_warn_ratio) |

**What it does:** The ratio at which BlueFS usage relative to the main device raises a health warning. Set to "1" to disable.

**When to use:** Core Global behavior — review before changing in production.

**Example:**

```bash
ceph config set global bluestore_bluefs_warn_ratio 0.06
ceph config get global bluestore_bluefs_warn_ratio
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `0.06` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_bluefs_warn_ratio
ceph -s
```

---

### bluestore_btree2_alloc_weight_factor

| | |
|---|---|
| Type | Float · default `2` · **Dev** |
| Table | [bluestore.md#SP_bluestore_btree2_alloc_weight_factor](../../../config/global/bluestore.md#SP_bluestore_btree2_alloc_weight_factor) |

**What it does:** Large continuous extents weight factor

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_btree2_alloc_weight_factor 2
ceph config get global bluestore_btree2_alloc_weight_factor
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`2`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_cache_age_bin_interval

| | |
|---|---|
| Type | Float · default `1` · **Dev** |
| Table | [bluestore.md#SP_bluestore_cache_age_bin_interval](../../../config/global/bluestore.md#SP_bluestore_cache_age_bin_interval) |

**What it does:** The duration (in seconds) represented by a single cache age bin.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_cache_age_bin_interval 1
ceph config get global bluestore_cache_age_bin_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_cache_age_bins_data

| | |
|---|---|
| Type | Str · default `1 2 6 24 120 720 0 0 0 0` · **Dev** |
| Table | [bluestore.md#SP_bluestore_cache_age_bins_data](../../../config/global/bluestore.md#SP_bluestore_cache_age_bins_data) |

**What it does:** A 10 element, space separated list of age bins for data cache

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_cache_age_bins_data "1 2 6 24 120 720 0 0 0 0"
ceph config get global bluestore_cache_age_bins_data
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1 2 6 24 120 720 0 0 0 0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_cache_age_bins_kv

| | |
|---|---|
| Type | Str · default `1 2 6 24 120 720 0 0 0 0` · **Dev** |
| Table | [bluestore.md#SP_bluestore_cache_age_bins_kv](../../../config/global/bluestore.md#SP_bluestore_cache_age_bins_kv) |

**What it does:** A 10 element, space separated list of age bins for kv cache

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_cache_age_bins_kv "1 2 6 24 120 720 0 0 0 0"
ceph config get global bluestore_cache_age_bins_kv
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1 2 6 24 120 720 0 0 0 0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_cache_age_bins_kv_onode

| | |
|---|---|
| Type | Str · default `0 0 0 0 0 0 0 0 0 720` · **Dev** |
| Table | [bluestore.md#SP_bluestore_cache_age_bins_kv_onode](../../../config/global/bluestore.md#SP_bluestore_cache_age_bins_kv_onode) |

**What it does:** A 10 element, space separated list of age bins for kv onode cache

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_cache_age_bins_kv_onode "0 0 0 0 0 0 0 0 0 720"
ceph config get global bluestore_cache_age_bins_kv_onode
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0 0 0 0 0 0 0 0 0 720`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_cache_age_bins_meta

| | |
|---|---|
| Type | Str · default `1 2 6 24 120 720 0 0 0 0` · **Dev** |
| Table | [bluestore.md#SP_bluestore_cache_age_bins_meta](../../../config/global/bluestore.md#SP_bluestore_cache_age_bins_meta) |

**What it does:** A 10 element, space separated list of age bins for onode cache

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_cache_age_bins_meta "1 2 6 24 120 720 0 0 0 0"
ceph config get global bluestore_cache_age_bins_meta
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1 2 6 24 120 720 0 0 0 0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_cache_autotune

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [bluestore.md#SP_bluestore_cache_autotune](../../../config/global/bluestore.md#SP_bluestore_cache_autotune) |

**What it does:** Automatically tune the ratio of caches while respecting min values.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_cache_autotune false
ceph config get global bluestore_cache_autotune
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_cache_autotune_interval

| | |
|---|---|
| Type | Float · default `5` · **Dev** |
| Table | [bluestore.md#SP_bluestore_cache_autotune_interval](../../../config/global/bluestore.md#SP_bluestore_cache_autotune_interval) |

**What it does:** The number of seconds to wait between rebalances when cache autotune is enabled.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_cache_autotune_interval 5
ceph config get global bluestore_cache_autotune_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`5`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_cache_kv_onode_ratio

| | |
|---|---|
| Type | Float · default `0.04` · **Dev** |
| Table | [bluestore.md#SP_bluestore_cache_kv_onode_ratio](../../../config/global/bluestore.md#SP_bluestore_cache_kv_onode_ratio) |

**What it does:** Ratio of BlueStore cache to devote to key/value onode column family (rocksdb)

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_cache_kv_onode_ratio 0.04
ceph config get global bluestore_cache_kv_onode_ratio
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.04`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_cache_kv_ratio

| | |
|---|---|
| Type | Float · default `0.45` · **Dev** |
| Table | [bluestore.md#SP_bluestore_cache_kv_ratio](../../../config/global/bluestore.md#SP_bluestore_cache_kv_ratio) |

**What it does:** Ratio of BlueStore cache to devote to key/value database (RocksDB)

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_cache_kv_ratio 0.45
ceph config get global bluestore_cache_kv_ratio
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.45`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_cache_meta_evict_in_autotune

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_cache_meta_evict_in_autotune](../../../config/global/bluestore.md#SP_bluestore_cache_meta_evict_in_autotune) |

**What it does:** Controls eviction of onodes from cache shards as part of autotune. When enabled (true), right after autotune memory allocation run onode cache tries to adapt. Depending on `bluestore_cache_meta_evict_limit` either some or all excess onodes are evicted. When disabled (false), cluster inactivity makes cache to keep its onode elements.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global bluestore_cache_meta_evict_in_autotune false
ceph config get global bluestore_cache_meta_evict_in_autotune
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_cache_meta_evict_in_autotune
ceph -s
```

---

### bluestore_cache_meta_evict_limit

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_cache_meta_evict_limit](../../../config/global/bluestore.md#SP_bluestore_cache_meta_evict_limit) |

**What it does:** Elements in onode cache shards are evicted when new element is inserted into the cache. In rare cases of cluster inactivity cache can be reduced, but not evicted. Adjusting size at once will cause stall first time cache shard is accessed. The setting limits how many onodes can get evicted in one go. Any value is less than 2 it is treated as request to adjust immediately.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluestore_cache_meta_evict_limit 10
ceph config get global bluestore_cache_meta_evict_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_cache_meta_evict_limit
ceph -s
```

---

### bluestore_cache_meta_ratio

| | |
|---|---|
| Type | Float · default `0.45` · **Dev** |
| Table | [bluestore.md#SP_bluestore_cache_meta_ratio](../../../config/global/bluestore.md#SP_bluestore_cache_meta_ratio) |

**What it does:** Ratio of BlueStore cache to devote to metadata

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_cache_meta_ratio 0.45
ceph config get global bluestore_cache_meta_ratio
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.45`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_cache_size

| | |
|---|---|
| Type | Size · default `0` · **Dev** |
| Table | [bluestore.md#SP_bluestore_cache_size](../../../config/global/bluestore.md#SP_bluestore_cache_size) |

**What it does:** Cache size (in bytes) for BlueStore

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_cache_size 64
ceph config get global bluestore_cache_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_cache_size_hdd

| | |
|---|---|
| Type | Size · default `1_G` · **Dev** |
| Table | [bluestore.md#SP_bluestore_cache_size_hdd](../../../config/global/bluestore.md#SP_bluestore_cache_size_hdd) |

**What it does:** Default bluestore_cache_size for rotational media

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_cache_size_hdd 1_G
ceph config get global bluestore_cache_size_hdd
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1_G`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_cache_size_ssd

| | |
|---|---|
| Type | Size · default `3_G` · **Dev** |
| Table | [bluestore.md#SP_bluestore_cache_size_ssd](../../../config/global/bluestore.md#SP_bluestore_cache_size_ssd) |

**What it does:** Default bluestore_cache_size for non-rotational (solid state) media

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_cache_size_ssd 3_G
ceph config get global bluestore_cache_size_ssd
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`3_G`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_cache_trim_interval

| | |
|---|---|
| Type | Float · default `0.05` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_cache_trim_interval](../../../config/global/bluestore.md#SP_bluestore_cache_trim_interval) |

**What it does:** How frequently we trim the bluestore cache

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global bluestore_cache_trim_interval 0.05
ceph config get global bluestore_cache_trim_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.05`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_cache_trim_interval
ceph -s
```

---

### bluestore_cache_trim_max_skip_pinned

| | |
|---|---|
| Type | Uint · default `1000` · **Dev** |
| Table | [bluestore.md#SP_bluestore_cache_trim_max_skip_pinned](../../../config/global/bluestore.md#SP_bluestore_cache_trim_max_skip_pinned) |

**What it does:** Max pinned cache entries we consider before giving up

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_cache_trim_max_skip_pinned 1000
ceph config get global bluestore_cache_trim_max_skip_pinned
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1000`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_cache_type

| | |
|---|---|
| Type | Str · enum: ["2q", "lru"] · default `2q` · **Dev** |
| Table | [bluestore.md#SP_bluestore_cache_type](../../../config/global/bluestore.md#SP_bluestore_cache_type) |

**What it does:** Cache replacement algorithm

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_cache_type 2q
ceph config get global bluestore_cache_type
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`2q`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_cleaner_sleep_interval

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_cleaner_sleep_interval](../../../config/global/bluestore.md#SP_bluestore_cleaner_sleep_interval) |

**What it does:** How long the BlueStore cleaner should sleep before re-checking utilization

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global bluestore_cleaner_sleep_interval 5
ceph config get global bluestore_cleaner_sleep_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_cleaner_sleep_interval
ceph -s
```

---

### bluestore_clone_cow

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_clone_cow](../../../config/global/bluestore.md#SP_bluestore_clone_cow) |

**What it does:** Use copy-on-write when cloning objects (versus reading and rewriting them at clone time)

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global bluestore_clone_cow false
ceph config get global bluestore_clone_cow
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_clone_cow
ceph -s
```

---

### bluestore_compression_algorithm

| | |
|---|---|
| Type | Str · enum: ["", "snappy", "zlib", "zstd", "lz4"] · default `snappy` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_compression_algorithm](../../../config/global/bluestore.md#SP_bluestore_compression_algorithm) |

**What it does:** Default compression algorithm to use when writing object data

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_compression_algorithm snappy
ceph config get global bluestore_compression_algorithm
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `snappy`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_compression_algorithm
ceph -s
```

---

### bluestore_compression_max_blob_size

| | |
|---|---|
| Type | Size · default `0` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_compression_max_blob_size](../../../config/global/bluestore.md#SP_bluestore_compression_max_blob_size) |

**What it does:** Maximum chunk size to apply compression to when non-random access is expected for an object.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluestore_compression_max_blob_size 64
ceph config get global bluestore_compression_max_blob_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_compression_max_blob_size
ceph -s
```

---

### bluestore_compression_max_blob_size_hdd

| | |
|---|---|
| Type | Size · default `64_K` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_compression_max_blob_size_hdd](../../../config/global/bluestore.md#SP_bluestore_compression_max_blob_size_hdd) |

**What it does:** Default value of bluestore_compression_max_blob_size for rotational media

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluestore_compression_max_blob_size_hdd 64_K
ceph config get global bluestore_compression_max_blob_size_hdd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_compression_max_blob_size_hdd
ceph -s
```

---

### bluestore_compression_max_blob_size_ssd

| | |
|---|---|
| Type | Size · default `64_K` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_compression_max_blob_size_ssd](../../../config/global/bluestore.md#SP_bluestore_compression_max_blob_size_ssd) |

**What it does:** Default value of bluestore_compression_max_blob_size for non-rotational (solid state) media

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluestore_compression_max_blob_size_ssd 64_K
ceph config get global bluestore_compression_max_blob_size_ssd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_compression_max_blob_size_ssd
ceph -s
```

---

### bluestore_compression_min_blob_size

| | |
|---|---|
| Type | Size · default `0` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_compression_min_blob_size](../../../config/global/bluestore.md#SP_bluestore_compression_min_blob_size) |

**What it does:** Maximum chunk size to apply compression to when random access is expected for an object.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluestore_compression_min_blob_size 64
ceph config get global bluestore_compression_min_blob_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_compression_min_blob_size
ceph -s
```

---

### bluestore_compression_min_blob_size_hdd

| | |
|---|---|
| Type | Size · default `64_K` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_compression_min_blob_size_hdd](../../../config/global/bluestore.md#SP_bluestore_compression_min_blob_size_hdd) |

**What it does:** Default value of bluestore_compression_min_blob_size for rotational media

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluestore_compression_min_blob_size_hdd 64_K
ceph config get global bluestore_compression_min_blob_size_hdd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_compression_min_blob_size_hdd
ceph -s
```

---

### bluestore_compression_min_blob_size_ssd

| | |
|---|---|
| Type | Size · default `64_K` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_compression_min_blob_size_ssd](../../../config/global/bluestore.md#SP_bluestore_compression_min_blob_size_ssd) |

**What it does:** Default value of bluestore_compression_min_blob_size for non-rotational (solid state) media

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluestore_compression_min_blob_size_ssd 64_K
ceph config get global bluestore_compression_min_blob_size_ssd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_compression_min_blob_size_ssd
ceph -s
```

---

### bluestore_compression_mode

| | |
|---|---|
| Type | Str · enum: ["none", "passive", "aggressive", "force"] · default `none` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_compression_mode](../../../config/global/bluestore.md#SP_bluestore_compression_mode) |

**What it does:** Default policy for using compression when pool does not specify

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_compression_mode none
ceph config get global bluestore_compression_mode
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `none`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_compression_mode
ceph -s
```

---

### bluestore_compression_required_ratio

| | |
|---|---|
| Type | Float · default `0.875` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_compression_required_ratio](../../../config/global/bluestore.md#SP_bluestore_compression_required_ratio) |

**What it does:** Compression ratio required to store compressed data

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_compression_required_ratio 0.875
ceph config get global bluestore_compression_required_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.875`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_compression_required_ratio
ceph -s
```

---

### bluestore_csum_type

| | |
|---|---|
| Type | Str · enum: ["none", "crc32c", "crc32c_16", "crc32c_8", "xxhash32", "xxhash64"] · default `crc32c` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_csum_type](../../../config/global/bluestore.md#SP_bluestore_csum_type) |

**What it does:** Default checksum algorithm to use

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_csum_type crc32c
ceph config get global bluestore_csum_type
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `crc32c`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_csum_type
ceph -s
```

---

### bluestore_debug_enforce_min_alloc_size

| | |
|---|---|
| Type | Uint · default `0` · **Dev** · **STARTUP** (restart required) |
| Table | [bluestore.md#SP_bluestore_debug_enforce_min_alloc_size](../../../config/global/bluestore.md#SP_bluestore_debug_enforce_min_alloc_size) |

**What it does:** Enforces specific min_alloc size usages

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_enforce_min_alloc_size 64
ceph config get global bluestore_debug_enforce_min_alloc_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_enforce_settings

| | |
|---|---|
| Type | Str · enum: ["default", "hdd", "ssd"] · default `default` · **Dev** |
| Table | [bluestore.md#SP_bluestore_debug_enforce_settings](../../../config/global/bluestore.md#SP_bluestore_debug_enforce_settings) |

**What it does:** Enforces specific hardware profile settings

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_enforce_settings default
ceph config get global bluestore_debug_enforce_settings
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`default`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_extent_map_encode_check

| | |
|---|---|
| Type | Bool · default `False` · **Dev** · **STARTUP** (restart required) |
| Table | [bluestore.md#SP_bluestore_debug_extent_map_encode_check](../../../config/global/bluestore.md#SP_bluestore_debug_extent_map_encode_check) |

**What it does:** Check correctness of extents in encode_some

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_extent_map_encode_check true
ceph config get global bluestore_debug_extent_map_encode_check
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_fast_recovery_compare_chance

| | |
|---|---|
| Type | Float · default `0` · **Dev** · **STARTUP** (restart required) |
| Table | [bluestore.md#SP_bluestore_debug_fast_recovery_compare_chance](../../../config/global/bluestore.md#SP_bluestore_debug_fast_recovery_compare_chance) |

**What it does:** For testing only. Compare legacy and multithread allocation recovery.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_fast_recovery_compare_chance 0
ceph config get global bluestore_debug_fast_recovery_compare_chance
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_freelist

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_debug_freelist](../../../config/global/bluestore.md#SP_bluestore_debug_freelist) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_freelist true
ceph config get global bluestore_debug_freelist
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_fsck_abort

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_debug_fsck_abort](../../../config/global/bluestore.md#SP_bluestore_debug_fsck_abort) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_fsck_abort true
ceph config get global bluestore_debug_fsck_abort
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_inject_allocation_from_file_failure

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [bluestore.md#SP_bluestore_debug_inject_allocation_from_file_failure](../../../config/global/bluestore.md#SP_bluestore_debug_inject_allocation_from_file_failure) |

**What it does:** Enables random error injections when restoring allocation map from file.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_inject_allocation_from_file_failure 0
ceph config get global bluestore_debug_inject_allocation_from_file_failure
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_inject_csum_err_probability

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [bluestore.md#SP_bluestore_debug_inject_csum_err_probability](../../../config/global/bluestore.md#SP_bluestore_debug_inject_csum_err_probability) |

**What it does:** Inject CRC verification errors into BlueStore device reads

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_inject_csum_err_probability 0
ceph config get global bluestore_debug_inject_csum_err_probability
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_inject_read_err

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_debug_inject_read_err](../../../config/global/bluestore.md#SP_bluestore_debug_inject_read_err) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_inject_read_err true
ceph config get global bluestore_debug_inject_read_err
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_legacy_omap

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_debug_legacy_omap](../../../config/global/bluestore.md#SP_bluestore_debug_legacy_omap) |

**What it does:** Allows mkfs to create OSDs with the legacy omap naming mode (neither per-pool nor per-pg). This is intended primarily for developers. The resulting OSDs might / would be transformed to the currrently default 'per-pg' format when BlueStore's quick-fix or repair are applied.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_legacy_omap true
ceph config get global bluestore_debug_legacy_omap
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_no_reuse_blocks

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_debug_no_reuse_blocks](../../../config/global/bluestore.md#SP_bluestore_debug_no_reuse_blocks) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_no_reuse_blocks true
ceph config get global bluestore_debug_no_reuse_blocks
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_omit_block_device_write

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_debug_omit_block_device_write](../../../config/global/bluestore.md#SP_bluestore_debug_omit_block_device_write) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_omit_block_device_write true
ceph config get global bluestore_debug_omit_block_device_write
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_omit_kv_commit

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_debug_omit_kv_commit](../../../config/global/bluestore.md#SP_bluestore_debug_omit_kv_commit) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_omit_kv_commit true
ceph config get global bluestore_debug_omit_kv_commit
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_onode_segmentation_random

| | |
|---|---|
| Type | Bool · default `False` · **Dev** · **STARTUP** (restart required) |
| Table | [bluestore.md#SP_bluestore_debug_onode_segmentation_random](../../../config/global/bluestore.md#SP_bluestore_debug_onode_segmentation_random) |

**What it does:** Random selection of onode segmentation

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_onode_segmentation_random true
ceph config get global bluestore_debug_onode_segmentation_random
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_permit_any_bdev_label

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_debug_permit_any_bdev_label](../../../config/global/bluestore.md#SP_bluestore_debug_permit_any_bdev_label) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_permit_any_bdev_label true
ceph config get global bluestore_debug_permit_any_bdev_label
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_prefragment_max

| | |
|---|---|
| Type | Size · default `1_M` · **Dev** |
| Table | [bluestore.md#SP_bluestore_debug_prefragment_max](../../../config/global/bluestore.md#SP_bluestore_debug_prefragment_max) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_prefragment_max 1_M
ceph config get global bluestore_debug_prefragment_max
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1_M`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_random_read_err

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [bluestore.md#SP_bluestore_debug_random_read_err](../../../config/global/bluestore.md#SP_bluestore_debug_random_read_err) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_random_read_err 0
ceph config get global bluestore_debug_random_read_err
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_randomize_serial_transaction

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [bluestore.md#SP_bluestore_debug_randomize_serial_transaction](../../../config/global/bluestore.md#SP_bluestore_debug_randomize_serial_transaction) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_randomize_serial_transaction 64
ceph config get global bluestore_debug_randomize_serial_transaction
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_small_allocations

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [bluestore.md#SP_bluestore_debug_small_allocations](../../../config/global/bluestore.md#SP_bluestore_debug_small_allocations) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_small_allocations 64
ceph config get global bluestore_debug_small_allocations
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_debug_too_many_blobs_threshold

| | |
|---|---|
| Type | Int · default `24576` · **Dev** |
| Table | [bluestore.md#SP_bluestore_debug_too_many_blobs_threshold](../../../config/global/bluestore.md#SP_bluestore_debug_too_many_blobs_threshold) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_debug_too_many_blobs_threshold 24576
ceph config get global bluestore_debug_too_many_blobs_threshold
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`24576`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_default_buffered_read

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_default_buffered_read](../../../config/global/bluestore.md#SP_bluestore_default_buffered_read) |

**What it does:** Cache read results by default (unless hinted NOCACHE or WONTNEED)

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global bluestore_default_buffered_read false
ceph config get global bluestore_default_buffered_read
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_default_buffered_read
ceph -s
```

---

### bluestore_default_buffered_write

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_default_buffered_write](../../../config/global/bluestore.md#SP_bluestore_default_buffered_write) |

**What it does:** Cache writes by default (unless hinted NOCACHE or WONTNEED)

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bluestore_default_buffered_write true
ceph config get global bluestore_default_buffered_write
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_default_buffered_write
ceph -s
```

---

### bluestore_deferred_batch_ops

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_deferred_batch_ops](../../../config/global/bluestore.md#SP_bluestore_deferred_batch_ops) |

**What it does:** Max number of deferred writes before we flush the deferred write queue

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_deferred_batch_ops 64
ceph config get global bluestore_deferred_batch_ops
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `65535`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_deferred_batch_ops
ceph -s
```

---

### bluestore_deferred_batch_ops_hdd

| | |
|---|---|
| Type | Uint · default `64` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_deferred_batch_ops_hdd](../../../config/global/bluestore.md#SP_bluestore_deferred_batch_ops_hdd) |

**What it does:** Default bluestore_deferred_batch_ops for rotational media (HDD)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_deferred_batch_ops_hdd 64
ceph config get global bluestore_deferred_batch_ops_hdd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `65535`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_deferred_batch_ops_hdd
ceph -s
```

---

### bluestore_deferred_batch_ops_ssd

| | |
|---|---|
| Type | Uint · default `16` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_deferred_batch_ops_ssd](../../../config/global/bluestore.md#SP_bluestore_deferred_batch_ops_ssd) |

**What it does:** Default bluestore_deferred_batch_ops for non-rotational (SSD) media

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_deferred_batch_ops_ssd 16
ceph config get global bluestore_deferred_batch_ops_ssd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `16`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `65535`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_deferred_batch_ops_ssd
ceph -s
```

---

### bluestore_discard_on_mkfs

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_discard_on_mkfs](../../../config/global/bluestore.md#SP_bluestore_discard_on_mkfs) |

**What it does:** Trim OSD devices after deployment

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global bluestore_discard_on_mkfs false
ceph config get global bluestore_discard_on_mkfs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_discard_on_mkfs
ceph -s
```

---

### bluestore_elastic_shared_blobs

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_elastic_shared_blobs](../../../config/global/bluestore.md#SP_bluestore_elastic_shared_blobs) |

**What it does:** Let BlueStore reuse existing shared blobs if possible

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global bluestore_elastic_shared_blobs false
ceph config get global bluestore_elastic_shared_blobs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_elastic_shared_blobs
ceph -s
```

---

### bluestore_extent_map_inline_shard_prealloc_size

| | |
|---|---|
| Type | Size · default `256` · **Dev** |
| Table | [bluestore.md#SP_bluestore_extent_map_inline_shard_prealloc_size](../../../config/global/bluestore.md#SP_bluestore_extent_map_inline_shard_prealloc_size) |

**What it does:** Preallocated buffer for inline shards

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_extent_map_inline_shard_prealloc_size 256
ceph config get global bluestore_extent_map_inline_shard_prealloc_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`256`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_extent_map_shard_max_size

| | |
|---|---|
| Type | Size · default `1200` · **Dev** |
| Table | [bluestore.md#SP_bluestore_extent_map_shard_max_size](../../../config/global/bluestore.md#SP_bluestore_extent_map_shard_max_size) |

**What it does:** Max size (bytes) for a single extent map shard before splitting

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_extent_map_shard_max_size 1200
ceph config get global bluestore_extent_map_shard_max_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1200`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_extent_map_shard_min_size

| | |
|---|---|
| Type | Size · default `150` · **Dev** |
| Table | [bluestore.md#SP_bluestore_extent_map_shard_min_size](../../../config/global/bluestore.md#SP_bluestore_extent_map_shard_min_size) |

**What it does:** Min size (bytes) for a single extent map shard before merging

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_extent_map_shard_min_size 150
ceph config get global bluestore_extent_map_shard_min_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`150`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_extent_map_shard_target_size

| | |
|---|---|
| Type | Size · default `500` · **Dev** |
| Table | [bluestore.md#SP_bluestore_extent_map_shard_target_size](../../../config/global/bluestore.md#SP_bluestore_extent_map_shard_target_size) |

**What it does:** Target size (bytes) for a single extent map shard

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_extent_map_shard_target_size 500
ceph config get global bluestore_extent_map_shard_target_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`500`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_extent_map_shard_target_size_slop

| | |
|---|---|
| Type | Float · default `0.2` · **Dev** |
| Table | [bluestore.md#SP_bluestore_extent_map_shard_target_size_slop](../../../config/global/bluestore.md#SP_bluestore_extent_map_shard_target_size_slop) |

**What it does:** Ratio above/below target for a shard when trying to align to an existing extent or blob boundary

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_extent_map_shard_target_size_slop 0.2
ceph config get global bluestore_extent_map_shard_target_size_slop
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.2`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_fail_eio

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_fail_eio](../../../config/global/bluestore.md#SP_bluestore_fail_eio) |

**What it does:** fail/crash on EIO

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_fail_eio true
ceph config get global bluestore_fail_eio
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_frag_runtime

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_frag_runtime](../../../config/global/bluestore.md#SP_bluestore_frag_runtime) |

**What it does:** Enable tracking of runtime object fragmentation during reads.

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bluestore_frag_runtime true
ceph config get global bluestore_frag_runtime
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_frag_runtime
ceph -s
```

---

### bluestore_frag_static

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_frag_static](../../../config/global/bluestore.md#SP_bluestore_frag_static) |

**What it does:** Enable tracking of static object fragmentation during scrub

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bluestore_frag_static true
ceph config get global bluestore_frag_static
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_frag_static
ceph -s
```

---

### bluestore_fragmentation_check_period

| | |
|---|---|
| Type | Uint · default `3600` · **Basic** |
| Table | [bluestore.md#SP_bluestore_fragmentation_check_period](../../../config/global/bluestore.md#SP_bluestore_fragmentation_check_period) |

**What it does:** The interval at which to perform a BlueStore free fragmentation check. Checking fragmentation is usually almost immediate. For highly fragmented storage, it can take several miliseconds and can cause a write operation to stall.

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global bluestore_fragmentation_check_period 3600
ceph config get global bluestore_fragmentation_check_period
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `3600` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_fragmentation_check_period
ceph -s
```

---

### bluestore_freelist_blocks_per_key

| | |
|---|---|
| Type | Size · default `128` · **Dev** |
| Table | [bluestore.md#SP_bluestore_freelist_blocks_per_key](../../../config/global/bluestore.md#SP_bluestore_freelist_blocks_per_key) |

**What it does:** Block (and bits) per database key

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_freelist_blocks_per_key 128
ceph config get global bluestore_freelist_blocks_per_key
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`128`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_fsck_error_on_no_per_pg_omap

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_fsck_error_on_no_per_pg_omap](../../../config/global/bluestore.md#SP_bluestore_fsck_error_on_no_per_pg_omap) |

**What it does:** Throw a fsck error (instead of a warning) when objects without per-pg omap are found

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bluestore_fsck_error_on_no_per_pg_omap true
ceph config get global bluestore_fsck_error_on_no_per_pg_omap
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_fsck_error_on_no_per_pg_omap
ceph -s
```

---

### bluestore_fsck_error_on_no_per_pool_omap

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_fsck_error_on_no_per_pool_omap](../../../config/global/bluestore.md#SP_bluestore_fsck_error_on_no_per_pool_omap) |

**What it does:** Throw a fsck error (instead of a warning) when objects without per-pool omap are found

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bluestore_fsck_error_on_no_per_pool_omap true
ceph config get global bluestore_fsck_error_on_no_per_pool_omap
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_fsck_error_on_no_per_pool_omap
ceph -s
```

---

### bluestore_fsck_error_on_no_per_pool_stats

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_fsck_error_on_no_per_pool_stats](../../../config/global/bluestore.md#SP_bluestore_fsck_error_on_no_per_pool_stats) |

**What it does:** Direct that fsck throws an error (instead of raising a warning) when BlueStore OSDs lack per-pool stats, for example after an upgrade

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bluestore_fsck_error_on_no_per_pool_stats true
ceph config get global bluestore_fsck_error_on_no_per_pool_stats
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_fsck_error_on_no_per_pool_stats
ceph -s
```

---

### bluestore_fsck_on_mkfs

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [bluestore.md#SP_bluestore_fsck_on_mkfs](../../../config/global/bluestore.md#SP_bluestore_fsck_on_mkfs) |

**What it does:** Run fsck after mkfs

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_fsck_on_mkfs false
ceph config get global bluestore_fsck_on_mkfs
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_fsck_on_mkfs_deep

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_fsck_on_mkfs_deep](../../../config/global/bluestore.md#SP_bluestore_fsck_on_mkfs_deep) |

**What it does:** Run deep fsck after mkfs

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_fsck_on_mkfs_deep true
ceph config get global bluestore_fsck_on_mkfs_deep
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_fsck_on_mount

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_fsck_on_mount](../../../config/global/bluestore.md#SP_bluestore_fsck_on_mount) |

**What it does:** Run fsck at mount

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_fsck_on_mount true
ceph config get global bluestore_fsck_on_mount
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_fsck_on_mount_deep

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_fsck_on_mount_deep](../../../config/global/bluestore.md#SP_bluestore_fsck_on_mount_deep) |

**What it does:** Run deep fsck at mount when bluestore_fsck_on_mount is set to true

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_fsck_on_mount_deep true
ceph config get global bluestore_fsck_on_mount_deep
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_fsck_on_umount

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_fsck_on_umount](../../../config/global/bluestore.md#SP_bluestore_fsck_on_umount) |

**What it does:** Run fsck at umount

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_fsck_on_umount true
ceph config get global bluestore_fsck_on_umount
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_fsck_on_umount_deep

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_fsck_on_umount_deep](../../../config/global/bluestore.md#SP_bluestore_fsck_on_umount_deep) |

**What it does:** Run deep fsck at umount when bluestore_fsck_on_umount is set to true

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_fsck_on_umount_deep true
ceph config get global bluestore_fsck_on_umount_deep
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_fsck_quick_fix_on_mount

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_fsck_quick_fix_on_mount](../../../config/global/bluestore.md#SP_bluestore_fsck_quick_fix_on_mount) |

**What it does:** Do quick-fix for the store at mount

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_fsck_quick_fix_on_mount true
ceph config get global bluestore_fsck_quick_fix_on_mount
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_fsck_quick_fix_threads

| | |
|---|---|
| Type | Int · default `2` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_fsck_quick_fix_threads](../../../config/global/bluestore.md#SP_bluestore_fsck_quick_fix_threads) |

**What it does:** Number of additional threads to perform quick-fix (shallow fsck) command

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_fsck_quick_fix_threads 2
ceph config get global bluestore_fsck_quick_fix_threads
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_fsck_quick_fix_threads
ceph -s
```

---

### bluestore_fsck_read_bytes_cap

| | |
|---|---|
| Type | Size · default `64_M` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_fsck_read_bytes_cap](../../../config/global/bluestore.md#SP_bluestore_fsck_read_bytes_cap) |

**What it does:** Maximum bytes read at once by deep fsck

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluestore_fsck_read_bytes_cap 64_M
ceph config get global bluestore_fsck_read_bytes_cap
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_fsck_read_bytes_cap
ceph -s
```

---

### bluestore_fsck_shared_blob_tracker_size

| | |
|---|---|
| Type | Float · default `0.03125` · **Dev** |
| Table | [bluestore.md#SP_bluestore_fsck_shared_blob_tracker_size](../../../config/global/bluestore.md#SP_bluestore_fsck_shared_blob_tracker_size) |

**What it does:** Size (a fraction of osd_memory_target, defaults to 128MB) of a hash table that tracks shared blob ref counts. A higher value makes the the tracker more precise and reduces overhead during repairs.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_fsck_shared_blob_tracker_size 0.03125
ceph config get global bluestore_fsck_shared_blob_tracker_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.03125`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_gc_enable_blob_threshold

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [bluestore.md#SP_bluestore_gc_enable_blob_threshold](../../../config/global/bluestore.md#SP_bluestore_gc_enable_blob_threshold) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_gc_enable_blob_threshold 64
ceph config get global bluestore_gc_enable_blob_threshold
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_gc_enable_total_threshold

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [bluestore.md#SP_bluestore_gc_enable_total_threshold](../../../config/global/bluestore.md#SP_bluestore_gc_enable_total_threshold) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_gc_enable_total_threshold 64
ceph config get global bluestore_gc_enable_total_threshold
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_hybrid_alloc_mem_cap

| | |
|---|---|
| Type | Uint · default `64_M` · **Dev** |
| Table | [bluestore.md#SP_bluestore_hybrid_alloc_mem_cap](../../../config/global/bluestore.md#SP_bluestore_hybrid_alloc_mem_cap) |

**What it does:** The maximum amount of memory the hybrid allocator should use before enabling bitmap supplement

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_hybrid_alloc_mem_cap 64_M
ceph config get global bluestore_hybrid_alloc_mem_cap
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`64_M`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_ignore_data_csum

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_ignore_data_csum](../../../config/global/bluestore.md#SP_bluestore_ignore_data_csum) |

**What it does:** Ignore checksum errors on read and do not generate an EIO error

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_ignore_data_csum true
ceph config get global bluestore_ignore_data_csum
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_kv_sync_util_logging_s

| | |
|---|---|
| Type | Float · default `10` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_kv_sync_util_logging_s](../../../config/global/bluestore.md#SP_bluestore_kv_sync_util_logging_s) |

**What it does:** KV sync thread utilization logging period

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_kv_sync_util_logging_s 10
ceph config get global bluestore_kv_sync_util_logging_s
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_kv_sync_util_logging_s
ceph -s
```

---

### bluestore_kvbackend

| | |
|---|---|
| Type | Str · default `rocksdb` · **Dev** |
| Table | [bluestore.md#SP_bluestore_kvbackend](../../../config/global/bluestore.md#SP_bluestore_kvbackend) |

**What it does:** Key value database to use for BlueStore

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_kvbackend rocksdb
ceph config get global bluestore_kvbackend
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`rocksdb`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_log_collection_list_age

| | |
|---|---|
| Type | Float · default `1_min` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_log_collection_list_age](../../../config/global/bluestore.md#SP_bluestore_log_collection_list_age) |

**What it does:** Log a collection list operation if it is slower than this age (seconds)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_log_collection_list_age 1_min
ceph config get global bluestore_log_collection_list_age
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_log_collection_list_age
ceph -s
```

---

### bluestore_log_omap_iterator_age

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_log_omap_iterator_age](../../../config/global/bluestore.md#SP_bluestore_log_omap_iterator_age) |

**What it does:** Log an omap iteration operation if it is slower than this age (seconds)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_log_omap_iterator_age 5
ceph config get global bluestore_log_omap_iterator_age
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_log_omap_iterator_age
ceph -s
```

---

### bluestore_log_op_age

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_log_op_age](../../../config/global/bluestore.md#SP_bluestore_log_op_age) |

**What it does:** Log a BlueStore operation if it is slower than this age (seconds)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_log_op_age 5
ceph config get global bluestore_log_op_age
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_log_op_age
ceph -s
```

---

### bluestore_log_scrub_op_age

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_log_scrub_op_age](../../../config/global/bluestore.md#SP_bluestore_log_scrub_op_age) |

**What it does:** Log a BlueStore Scrub operation if it is slower than this age (seconds)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_log_scrub_op_age 5
ceph config get global bluestore_log_scrub_op_age
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_log_scrub_op_age
ceph -s
```

---

### bluestore_max_alloc_size

| | |
|---|---|
| Type | Size · default `0` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_max_alloc_size](../../../config/global/bluestore.md#SP_bluestore_max_alloc_size) |

**What it does:** Maximum size of a single allocation (0 for no max)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluestore_max_alloc_size 64
ceph config get global bluestore_max_alloc_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_max_alloc_size
ceph -s
```

---

### bluestore_max_blob_size

| | |
|---|---|
| Type | Size · default `0` · **Dev** |
| Table | [bluestore.md#SP_bluestore_max_blob_size](../../../config/global/bluestore.md#SP_bluestore_max_blob_size) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_max_blob_size 64
ceph config get global bluestore_max_blob_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_max_blob_size_hdd

| | |
|---|---|
| Type | Size · default `64_K` · **Dev** |
| Table | [bluestore.md#SP_bluestore_max_blob_size_hdd](../../../config/global/bluestore.md#SP_bluestore_max_blob_size_hdd) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_max_blob_size_hdd 64_K
ceph config get global bluestore_max_blob_size_hdd
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`64_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_max_blob_size_ssd

| | |
|---|---|
| Type | Size · default `64_K` · **Dev** |
| Table | [bluestore.md#SP_bluestore_max_blob_size_ssd](../../../config/global/bluestore.md#SP_bluestore_max_blob_size_ssd) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_max_blob_size_ssd 64_K
ceph config get global bluestore_max_blob_size_ssd
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`64_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_max_defer_interval

| | |
|---|---|
| Type | Float · default `3` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_max_defer_interval](../../../config/global/bluestore.md#SP_bluestore_max_defer_interval) |

**What it does:** Max duration to force deferred submit

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluestore_max_defer_interval 3
ceph config get global bluestore_max_defer_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_max_defer_interval
ceph -s
```

---

### bluestore_max_deferred_txc

| | |
|---|---|
| Type | Uint · default `32` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_max_deferred_txc](../../../config/global/bluestore.md#SP_bluestore_max_deferred_txc) |

**What it does:** Max transactions with deferred writes that can accumulate before we force flush deferred writes

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluestore_max_deferred_txc 32
ceph config get global bluestore_max_deferred_txc
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `32`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_max_deferred_txc
ceph -s
```

---

### bluestore_min_alloc_size

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_min_alloc_size](../../../config/global/bluestore.md#SP_bluestore_min_alloc_size) |

**What it does:** Minimum allocation size to allocate for an object

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluestore_min_alloc_size 64
ceph config get global bluestore_min_alloc_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_min_alloc_size
ceph -s
```

---

### bluestore_min_alloc_size_hdd

| | |
|---|---|
| Type | Size · default `4_K` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_min_alloc_size_hdd](../../../config/global/bluestore.md#SP_bluestore_min_alloc_size_hdd) |

**What it does:** Default min_alloc_size value for rotational media

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluestore_min_alloc_size_hdd 4_K
ceph config get global bluestore_min_alloc_size_hdd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_min_alloc_size_hdd
ceph -s
```

---

### bluestore_min_alloc_size_ssd

| | |
|---|---|
| Type | Size · default `4_K` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_min_alloc_size_ssd](../../../config/global/bluestore.md#SP_bluestore_min_alloc_size_ssd) |

**What it does:** Default min_alloc_size value for non-rotational (solid state) media

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluestore_min_alloc_size_ssd 4_K
ceph config get global bluestore_min_alloc_size_ssd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_min_alloc_size_ssd
ceph -s
```

---

### bluestore_nid_prealloc

| | |
|---|---|
| Type | Int · default `1024` · **Dev** |
| Table | [bluestore.md#SP_bluestore_nid_prealloc](../../../config/global/bluestore.md#SP_bluestore_nid_prealloc) |

**What it does:** Number of unique object IDs to preallocate at a time

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_nid_prealloc 1024
ceph config get global bluestore_nid_prealloc
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1024`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_onode_segment_size

| | |
|---|---|
| Type | Size · default `0` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_onode_segment_size](../../../config/global/bluestore.md#SP_bluestore_onode_segment_size) |

**What it does:** Size of segment for onode.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_onode_segment_size 64
ceph config get global bluestore_onode_segment_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_onode_segment_size
ceph -s
```

---

### bluestore_prefer_deferred_size

| | |
|---|---|
| Type | Size · default `0` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_prefer_deferred_size](../../../config/global/bluestore.md#SP_bluestore_prefer_deferred_size) |

**What it does:** Writes smaller than this size will be written to the WAL and then asynchronously written to the block (slow) device. This can be beneficial when using rotational media where seeks are expensive, and is helpful both with and without SSD WAL. devices.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_prefer_deferred_size 64
ceph config get global bluestore_prefer_deferred_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_prefer_deferred_size
ceph -s
```

---

### bluestore_prefer_deferred_size_hdd

| | |
|---|---|
| Type | Size · default `64_K` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_prefer_deferred_size_hdd](../../../config/global/bluestore.md#SP_bluestore_prefer_deferred_size_hdd) |

**What it does:** Default bluestore_prefer_deferred_size for rotational media

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_prefer_deferred_size_hdd 64_K
ceph config get global bluestore_prefer_deferred_size_hdd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_prefer_deferred_size_hdd
ceph -s
```

---

### bluestore_prefer_deferred_size_ssd

| | |
|---|---|
| Type | Size · default `0` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_prefer_deferred_size_ssd](../../../config/global/bluestore.md#SP_bluestore_prefer_deferred_size_ssd) |

**What it does:** Default bluestore_prefer_deferred_size for non-rotational (SSD) media

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_prefer_deferred_size_ssd 64
ceph config get global bluestore_prefer_deferred_size_ssd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_prefer_deferred_size_ssd
ceph -s
```

---

### bluestore_qfsck_on_mount

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [bluestore.md#SP_bluestore_qfsck_on_mount](../../../config/global/bluestore.md#SP_bluestore_qfsck_on_mount) |

**What it does:** Run quick-fsck at mount comparing allocation-file to RocksDB allocation state

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_qfsck_on_mount false
ceph config get global bluestore_qfsck_on_mount
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_recompression_min_gain

| | |
|---|---|
| Type | Float · default `1.2` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_recompression_min_gain](../../../config/global/bluestore.md#SP_bluestore_recompression_min_gain) |

**What it does:** Required estimated gain for accepting extents for recompressing.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluestore_recompression_min_gain 1.2
ceph config get global bluestore_recompression_min_gain
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1.2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_recompression_min_gain
ceph -s
```

---

### bluestore_retry_disk_reads

| | |
|---|---|
| Type | Uint · default `3` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_retry_disk_reads](../../../config/global/bluestore.md#SP_bluestore_retry_disk_reads) |

**What it does:** Number of read retries on checksum validation error

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_retry_disk_reads 3
ceph config get global bluestore_retry_disk_reads
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `255`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_retry_disk_reads
ceph -s
```

---

### bluestore_rocksdb_cf

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_rocksdb_cf](../../../config/global/bluestore.md#SP_bluestore_rocksdb_cf) |

**What it does:** Enable use of RocksDB column families for BlueStore metadata

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global bluestore_rocksdb_cf false
ceph config get global bluestore_rocksdb_cf
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_rocksdb_cf
ceph -s
```

---

### bluestore_rocksdb_cfs

| | |
|---|---|
| Type | Str · default `m(3) p(3,0-12) O(3,0-13)=block_cache={type=binned_lru} L=min_write_buffer_number_to_merge=32 P=min_write_buffer_number_to_merge=32` · **Dev** |
| Table | [bluestore.md#SP_bluestore_rocksdb_cfs](../../../config/global/bluestore.md#SP_bluestore_rocksdb_cfs) |

**What it does:** Definition of column families and their sharding

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_rocksdb_cfs "m(3) p(3,0-12) O(3,0-13)=block_cache={type=binned_lru} L=min_write_buffer_number_to_merge=32 P=min_write_buffer_number_to_merge=32"
ceph config get global bluestore_rocksdb_cfs
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`m(3) p(3,0-12) O(3,0-13)=block_cache={type=binned_lru} L=min_write_buffer_number_to_merge=32 P=min_write_buffer_number_to_merge=32`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_rocksdb_options

| | |
|---|---|
| Type | Str · default `compression=kLZ4Compression,max_write_buffer_number=64,min_write_buffer_number_to_merge=6,compaction_style=kCompactionStyleLevel,write_buffer_size=16777216,max_background_jobs=4,level0_file_num_compaction_trigger=8,max_bytes_for_level_base=1073741824,max_bytes_for_level_multiplier=8,compaction_readahead_size=2MB,max_total_wal_size=1073741824,writable_file_max_buffer_size=0` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_rocksdb_options](../../../config/global/bluestore.md#SP_bluestore_rocksdb_options) |

**What it does:** Full set of RocksDB settings to override

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_rocksdb_options "compression=kLZ4Compression,max_write_buffer_number=64,min_write_buffer_number_to_merge=6,compaction_style=kCompactionStyleLevel,write_buffer_size=16777216,max_background_jobs=4,level0_file_num_compaction_trigger=8,max_bytes_for_level_base=1073741824,max_bytes_for_level_multiplier=8,compaction_readahead_size=2MB,max_total_wal_size=1073741824,writable_file_max_buffer_size=0"
ceph config get global bluestore_rocksdb_options
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `compression=kLZ4Compression,max_write_buffer_number=64,min_write_buffer_number_to_merge=6,compaction_style=kCompactionStyleLevel,write_buffer_size=16777216,max_background_jobs=4,level0_file_num_compaction_trigger=8,max_bytes_for_level_base=1073741824,max_bytes_for_level_multiplier=8,compaction_readahead_size=2MB,max_total_wal_size=1073741824,writable_file_max_buffer_size=0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_rocksdb_options
ceph -s
```

---

### bluestore_rocksdb_options_annex

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_rocksdb_options_annex](../../../config/global/bluestore.md#SP_bluestore_rocksdb_options_annex) |

**What it does:** An addition to bluestore_rocksdb_options. Allows setting RocksDB options without repeating the existing defaults.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_rocksdb_options_annex "example"
ceph config get global bluestore_rocksdb_options_annex
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_rocksdb_options_annex
ceph -s
```

---

### bluestore_slow_ops_warn_lifetime

| | |
|---|---|
| Type | Uint · default `86400` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_slow_ops_warn_lifetime](../../../config/global/bluestore.md#SP_bluestore_slow_ops_warn_lifetime) |

**What it does:** Set the duration after which BlueStore slow ops warnings clear after being raised by exceeding the `bluestore_slow_ops_warn_threshold`. This is not the same as `osd_op_complaint_time`, which is about RADOS ops at the OSD level.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_slow_ops_warn_lifetime 86400
ceph config get global bluestore_slow_ops_warn_lifetime
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `86400`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_slow_ops_warn_lifetime
ceph -s
```

---

### bluestore_slow_ops_warn_threshold

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_slow_ops_warn_threshold](../../../config/global/bluestore.md#SP_bluestore_slow_ops_warn_threshold) |

**What it does:** Set the minimum number of BlueStore slow ops before raising a health warning

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_slow_ops_warn_threshold 1
ceph config get global bluestore_slow_ops_warn_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_slow_ops_warn_threshold
ceph -s
```

---

### bluestore_slow_scrub_ops_warn_threshold

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_slow_scrub_ops_warn_threshold](../../../config/global/bluestore.md#SP_bluestore_slow_scrub_ops_warn_threshold) |

**What it does:** Set the minimum number of BlueStore slow scrub ops before raising a health warning

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_slow_scrub_ops_warn_threshold 1
ceph config get global bluestore_slow_scrub_ops_warn_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_slow_scrub_ops_warn_threshold
ceph -s
```

---

### bluestore_spdk_coremask

| | |
|---|---|
| Type | Str · default `0x1` · **Dev** |
| Table | [bluestore.md#SP_bluestore_spdk_coremask](../../../config/global/bluestore.md#SP_bluestore_spdk_coremask) |

**What it does:** A hexadecimal bit mask of the cores to run on. Note the core numbering can change between platforms and should be determined beforehand

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_spdk_coremask 0x1
ceph config get global bluestore_spdk_coremask
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0x1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_spdk_io_sleep

| | |
|---|---|
| Type | Uint · default `5` · **Dev** |
| Table | [bluestore.md#SP_bluestore_spdk_io_sleep](../../../config/global/bluestore.md#SP_bluestore_spdk_io_sleep) |

**What it does:** Time period to wait if there is no completed I/O from polling

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_spdk_io_sleep 5
ceph config get global bluestore_spdk_io_sleep
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`5`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_spdk_max_io_completion

| | |
|---|---|
| Type | Uint · default `0` · **Dev** |
| Table | [bluestore.md#SP_bluestore_spdk_max_io_completion](../../../config/global/bluestore.md#SP_bluestore_spdk_max_io_completion) |

**What it does:** Maximum number of operations to be batched completed while checking queue pair completions, 0 means to let the SPDK library determine the value

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_spdk_max_io_completion 64
ceph config get global bluestore_spdk_max_io_completion
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_spdk_mem

| | |
|---|---|
| Type | Size · default `512` · **Dev** |
| Table | [bluestore.md#SP_bluestore_spdk_mem](../../../config/global/bluestore.md#SP_bluestore_spdk_mem) |

**What it does:** Amount of dpdk memory size in MB

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_spdk_mem 512
ceph config get global bluestore_spdk_mem
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`512`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_sync_submit_transaction

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_sync_submit_transaction](../../../config/global/bluestore.md#SP_bluestore_sync_submit_transaction) |

**What it does:** Try to submit metadata transaction to RocksDB in queuing thread context

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_sync_submit_transaction true
ceph config get global bluestore_sync_submit_transaction
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_throttle_bytes

| | |
|---|---|
| Type | Size · default `64_M` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_throttle_bytes](../../../config/global/bluestore.md#SP_bluestore_throttle_bytes) |

**What it does:** Maximum bytes in flight before we throttle IO submission

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_throttle_bytes 64_M
ceph config get global bluestore_throttle_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_throttle_bytes
ceph -s
```

---

### bluestore_throttle_cost_per_io

| | |
|---|---|
| Type | Size · default `0` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_throttle_cost_per_io](../../../config/global/bluestore.md#SP_bluestore_throttle_cost_per_io) |

**What it does:** Overhead added to transaction cost (in bytes) for each IO

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_throttle_cost_per_io 64
ceph config get global bluestore_throttle_cost_per_io
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_throttle_cost_per_io
ceph -s
```

---

### bluestore_throttle_cost_per_io_hdd

| | |
|---|---|
| Type | Uint · default `670000` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_throttle_cost_per_io_hdd](../../../config/global/bluestore.md#SP_bluestore_throttle_cost_per_io_hdd) |

**What it does:** Default bluestore_throttle_cost_per_io for rotational media (HDDs)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_throttle_cost_per_io_hdd 670000
ceph config get global bluestore_throttle_cost_per_io_hdd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `670000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_throttle_cost_per_io_hdd
ceph -s
```

---

### bluestore_throttle_cost_per_io_ssd

| | |
|---|---|
| Type | Uint · default `4000` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_throttle_cost_per_io_ssd](../../../config/global/bluestore.md#SP_bluestore_throttle_cost_per_io_ssd) |

**What it does:** Default bluestore_throttle_cost_per_io for non-rotation (SSD) media

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_throttle_cost_per_io_ssd 4000
ceph config get global bluestore_throttle_cost_per_io_ssd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_throttle_cost_per_io_ssd
ceph -s
```

---

### bluestore_throttle_deferred_bytes

| | |
|---|---|
| Type | Size · default `128_M` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_throttle_deferred_bytes](../../../config/global/bluestore.md#SP_bluestore_throttle_deferred_bytes) |

**What it does:** Maximum bytes for deferred writes before we throttle IO submission

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_throttle_deferred_bytes 128_M
ceph config get global bluestore_throttle_deferred_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `128_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_throttle_deferred_bytes
ceph -s
```

---

### bluestore_throttle_trace_rate

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_throttle_trace_rate](../../../config/global/bluestore.md#SP_bluestore_throttle_trace_rate) |

**What it does:** Rate at which to sample BlueStore transactions (per second)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_throttle_trace_rate 0
ceph config get global bluestore_throttle_trace_rate
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_throttle_trace_rate
ceph -s
```

---

### bluestore_tracing

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_tracing](../../../config/global/bluestore.md#SP_bluestore_tracing) |

**What it does:** Enable BlueStore event tracing.

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bluestore_tracing true
ceph config get global bluestore_tracing
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_tracing
ceph -s
```

---

### bluestore_use_ebd

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_use_ebd](../../../config/global/bluestore.md#SP_bluestore_use_ebd) |

**What it does:** EBD plugin used during mkfs is required for mounts.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global bluestore_use_ebd false
ceph config get global bluestore_use_ebd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_use_ebd
ceph -s
```

---

### bluestore_use_optimal_io_size_for_min_alloc_size

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_use_optimal_io_size_for_min_alloc_size](../../../config/global/bluestore.md#SP_bluestore_use_optimal_io_size_for_min_alloc_size) |

**What it does:** Discover media optimal IO size and use for min_alloc_size. This is useful when OSDs are created on coarse-IU QLC SSDs or other novel types of underlyinng block device. It is a no-op for conventional media.

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bluestore_use_optimal_io_size_for_min_alloc_size true
ceph config get global bluestore_use_optimal_io_size_for_min_alloc_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_use_optimal_io_size_for_min_alloc_size
ceph -s
```

---

### bluestore_volume_selection_policy

| | |
|---|---|
| Type | Str · enum: ["rocksdb_original", "use_some_extra", "use_some_extra_enforced", "fit_to_fast"] · default `use_some_extra` · **Dev** |
| Table | [bluestore.md#SP_bluestore_volume_selection_policy](../../../config/global/bluestore.md#SP_bluestore_volume_selection_policy) |

**What it does:** Determine the BlueFS volume selection policy

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_volume_selection_policy use_some_extra
ceph config get global bluestore_volume_selection_policy
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`use_some_extra`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluestore_volume_selection_reserved

| | |
|---|---|
| Type | Int · default `0` · **Advanced** · **STARTUP** (restart required) |
| Table | [bluestore.md#SP_bluestore_volume_selection_reserved](../../../config/global/bluestore.md#SP_bluestore_volume_selection_reserved) |

**What it does:** Space reserved on the DB device and not allowed for 'use some extra' policy usage. Overrides the 'bluestore_volume_selection_reserved_factor' setting and introduces a straightforward limit.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_volume_selection_reserved 64
ceph config get global bluestore_volume_selection_reserved
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_volume_selection_reserved
ceph -s
```

---

### bluestore_volume_selection_reserved_factor

| | |
|---|---|
| Type | Float · default `2` · **Advanced** · **STARTUP** (restart required) |
| Table | [bluestore.md#SP_bluestore_volume_selection_reserved_factor](../../../config/global/bluestore.md#SP_bluestore_volume_selection_reserved_factor) |

**What it does:** RocksDB level size multiplier. Determines amount of space at DB device to bar from the usage when 'use some extra' policy is in action. The reserved size is determined by sum(L_max_size&#91;0&#93;, L_max_size&#91;L-1&#93;) + L_max_size&#91;L&#93; * this_factor

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluestore_volume_selection_reserved_factor 2
ceph config get global bluestore_volume_selection_reserved_factor
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_volume_selection_reserved_factor
ceph -s
```

---

### bluestore_warn_on_bluefs_spillover

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_warn_on_bluefs_spillover](../../../config/global/bluestore.md#SP_bluestore_warn_on_bluefs_spillover) |

**What it does:** Raise a health warning on BlueFS slow device spillover

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global bluestore_warn_on_bluefs_spillover false
ceph config get global bluestore_warn_on_bluefs_spillover
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_warn_on_bluefs_spillover
ceph -s
```

---

### bluestore_warn_on_free_fragmentation

| | |
|---|---|
| Type | Float · default `0.8` · **Basic** |
| Table | [bluestore.md#SP_bluestore_warn_on_free_fragmentation](../../../config/global/bluestore.md#SP_bluestore_warn_on_free_fragmentation) |

**What it does:** The level at which BlueStore block device free fragmentation raises a health warning. Set to "1" to disable. This is the value reported by the admin socket command "bluestore allocator score block".

**When to use:** Core Global behavior — review before changing in production.

**Example:**

```bash
ceph config set global bluestore_warn_on_free_fragmentation 0.8
ceph config get global bluestore_warn_on_free_fragmentation
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `0.8` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_warn_on_free_fragmentation
ceph -s
```

---

### bluestore_warn_on_legacy_statfs

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_warn_on_legacy_statfs](../../../config/global/bluestore.md#SP_bluestore_warn_on_legacy_statfs) |

**What it does:** Raise a health warning on the lack of per-pool statfs reporting from a BlueStore OSD

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global bluestore_warn_on_legacy_statfs false
ceph config get global bluestore_warn_on_legacy_statfs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_warn_on_legacy_statfs
ceph -s
```

---

### bluestore_warn_on_no_per_pg_omap

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_warn_on_no_per_pg_omap](../../../config/global/bluestore.md#SP_bluestore_warn_on_no_per_pg_omap) |

**What it does:** Raise a health warning on lack of per-pg omap

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bluestore_warn_on_no_per_pg_omap true
ceph config get global bluestore_warn_on_no_per_pg_omap
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_warn_on_no_per_pg_omap
ceph -s
```

---

### bluestore_warn_on_no_per_pool_omap

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_warn_on_no_per_pool_omap](../../../config/global/bluestore.md#SP_bluestore_warn_on_no_per_pool_omap) |

**What it does:** Raise a health warning on lack of per-pool omap

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global bluestore_warn_on_no_per_pool_omap false
ceph config get global bluestore_warn_on_no_per_pool_omap
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_warn_on_no_per_pool_omap
ceph -s
```

---

### bluestore_warn_on_spurious_read_errors

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [bluestore.md#SP_bluestore_warn_on_spurious_read_errors](../../../config/global/bluestore.md#SP_bluestore_warn_on_spurious_read_errors) |

**What it does:** Raise a health warning when spurious read errors are observed by an OSD

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global bluestore_warn_on_spurious_read_errors false
ceph config get global bluestore_warn_on_spurious_read_errors
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_warn_on_spurious_read_errors
ceph -s
```

---

### bluestore_write_v2

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** · **STARTUP** (restart required) |
| Table | [bluestore.md#SP_bluestore_write_v2](../../../config/global/bluestore.md#SP_bluestore_write_v2) |

**What it does:** Use faster write path

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bluestore_write_v2 true
ceph config get global bluestore_write_v2
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_write_v2
ceph -s
```

---

### bluestore_write_v2_random

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** · **STARTUP** (restart required) |
| Table | [bluestore.md#SP_bluestore_write_v2_random](../../../config/global/bluestore.md#SP_bluestore_write_v2_random) |

**What it does:** Random selection of write path mode

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bluestore_write_v2_random true
ceph config get global bluestore_write_v2_random
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluestore_write_v2_random
ceph -s
```

---

### bluestore_zero_block_detection

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluestore.md#SP_bluestore_zero_block_detection](../../../config/global/bluestore.md#SP_bluestore_zero_block_detection) |

**What it does:** punch holes instead of writing zeros

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluestore_zero_block_detection true
ceph config get global bluestore_zero_block_detection
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
