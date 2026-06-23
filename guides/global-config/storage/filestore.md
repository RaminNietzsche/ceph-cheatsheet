# Filestore

Global config deep dive — 84 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [filestore_apply_finisher_threads](#filestore_apply_finisher_threads) | `1` | Dev | Dev |
| [filestore_blackhole](#filestore_blackhole) | `False` | Dev | Dev |
| [filestore_btrfs_clone_range](#filestore_btrfs_clone_range) | `True` | Advanced | Performance |
| [filestore_btrfs_snap](#filestore_btrfs_snap) | `True` | Dev | Dev |
| [filestore_caller_concurrency](#filestore_caller_concurrency) | `10` | Dev | Dev |
| [filestore_collect_device_partition_information](#filestore_collect_device_partition_information) | `True` | Advanced | Performance |
| [filestore_commit_timeout](#filestore_commit_timeout) | `10_min` | Advanced | Performance |
| [filestore_debug_inject_read_err](#filestore_debug_inject_read_err) | `False` | Dev | Dev |
| [filestore_debug_omap_check](#filestore_debug_omap_check) | `False` | Dev | Dev |
| [filestore_debug_verify_split](#filestore_debug_verify_split) | `False` | Dev | Dev |
| [filestore_dump_file](#filestore_dump_file) | `(empty)` | Dev | Dev |
| [filestore_expected_throughput_bytes](#filestore_expected_throughput_bytes) | `209715200` | Advanced | Performance |
| [filestore_expected_throughput_ops](#filestore_expected_throughput_ops) | `200` | Advanced | Performance |
| [filestore_fadvise](#filestore_fadvise) | `True` | Advanced | Performance |
| [filestore_fail_eio](#filestore_fail_eio) | `True` | Dev | Dev |
| [filestore_fd_cache_shards](#filestore_fd_cache_shards) | `16` | Dev | Dev |
| [filestore_fd_cache_size](#filestore_fd_cache_size) | `128` | Dev | Dev |
| [filestore_fiemap](#filestore_fiemap) | `False` | Advanced | Performance |
| [filestore_fiemap_threshold](#filestore_fiemap_threshold) | `4_K` | Dev | Dev |
| [filestore_fsync_flushes_journal_data](#filestore_fsync_flushes_journal_data) | `False` | Dev | Dev |
| [filestore_index_retry_probability](#filestore_index_retry_probability) | `0` | Dev | Dev |
| [filestore_inject_stall](#filestore_inject_stall) | `0` | Dev | Dev |
| [filestore_journal_parallel](#filestore_journal_parallel) | `False` | Dev | Dev |
| [filestore_journal_trailing](#filestore_journal_trailing) | `False` | Dev | Dev |
| [filestore_journal_writeahead](#filestore_journal_writeahead) | `False` | Dev | Dev |
| [filestore_kill_at](#filestore_kill_at) | `0` | Dev | Dev |
| [filestore_max_alloc_hint_size](#filestore_max_alloc_hint_size) | `1_M` | Dev | Dev |
| [filestore_max_inline_xattr_size](#filestore_max_inline_xattr_size) | `0` | Dev | Dev |
| [filestore_max_inline_xattr_size_btrfs](#filestore_max_inline_xattr_size_btrfs) | `2_K` | Dev | Dev |
| [filestore_max_inline_xattr_size_other](#filestore_max_inline_xattr_size_other) | `512` | Dev | Dev |
| [filestore_max_inline_xattr_size_xfs](#filestore_max_inline_xattr_size_xfs) | `64_K` | Dev | Dev |
| [filestore_max_inline_xattrs](#filestore_max_inline_xattrs) | `0` | Dev | Dev |
| [filestore_max_inline_xattrs_btrfs](#filestore_max_inline_xattrs_btrfs) | `10` | Dev | Dev |
| [filestore_max_inline_xattrs_other](#filestore_max_inline_xattrs_other) | `2` | Dev | Dev |
| [filestore_max_inline_xattrs_xfs](#filestore_max_inline_xattrs_xfs) | `10` | Dev | Dev |
| [filestore_max_sync_interval](#filestore_max_sync_interval) | `5` | Advanced | Performance |
| [filestore_max_xattr_value_size](#filestore_max_xattr_value_size) | `0` | Dev | Dev |
| [filestore_max_xattr_value_size_btrfs](#filestore_max_xattr_value_size_btrfs) | `64_K` | Dev | Dev |
| [filestore_max_xattr_value_size_other](#filestore_max_xattr_value_size_other) | `1_K` | Dev | Dev |
| [filestore_max_xattr_value_size_xfs](#filestore_max_xattr_value_size_xfs) | `64_K` | Dev | Dev |
| [filestore_merge_threshold](#filestore_merge_threshold) | `-10` | Dev | Dev |
| [filestore_min_sync_interval](#filestore_min_sync_interval) | `0.01` | Dev | Dev |
| [filestore_odsync_write](#filestore_odsync_write) | `False` | Dev | Dev |
| [filestore_omap_backend](#filestore_omap_backend) | `rocksdb` | Dev | Dev |
| [filestore_omap_backend_path](#filestore_omap_backend_path) | `(empty)` | Dev | Dev |
| [filestore_omap_header_cache_size](#filestore_omap_header_cache_size) | `1_K` | Dev | Dev |
| [filestore_ondisk_finisher_threads](#filestore_ondisk_finisher_threads) | `1` | Dev | Dev |
| [filestore_op_thread_suicide_timeout](#filestore_op_thread_suicide_timeout) | `3_min` | Advanced | Performance |
| [filestore_op_thread_timeout](#filestore_op_thread_timeout) | `1_min` | Advanced | Performance |
| [filestore_op_threads](#filestore_op_threads) | `2` | Advanced | Performance |
| [filestore_punch_hole](#filestore_punch_hole) | `False` | Advanced | Performance |
| [filestore_queue_high_delay_multiple](#filestore_queue_high_delay_multiple) | `0` | Dev | Dev |
| [filestore_queue_high_delay_multiple_bytes](#filestore_queue_high_delay_multiple_bytes) | `0` | Dev | Dev |
| [filestore_queue_high_delay_multiple_ops](#filestore_queue_high_delay_multiple_ops) | `0` | Dev | Dev |
| [filestore_queue_high_threshhold](#filestore_queue_high_threshhold) | `0.9` | Dev | Dev |
| [filestore_queue_low_threshhold](#filestore_queue_low_threshhold) | `0.3` | Dev | Dev |
| [filestore_queue_max_bytes](#filestore_queue_max_bytes) | `100_M` | Advanced | Performance |
| [filestore_queue_max_delay_multiple](#filestore_queue_max_delay_multiple) | `0` | Dev | Dev |
| [filestore_queue_max_delay_multiple_bytes](#filestore_queue_max_delay_multiple_bytes) | `0` | Dev | Dev |
| [filestore_queue_max_delay_multiple_ops](#filestore_queue_max_delay_multiple_ops) | `0` | Dev | Dev |
| [filestore_queue_max_ops](#filestore_queue_max_ops) | `50` | Advanced | Performance |
| [filestore_rocksdb_options](#filestore_rocksdb_options) | `max_background_jobs=10,compaction_readahead_size=2097152,compression=kNoCompression` | Dev | Dev |
| [filestore_seek_data_hole](#filestore_seek_data_hole) | `False` | Advanced | Performance |
| [filestore_sloppy_crc](#filestore_sloppy_crc) | `False` | Dev | Dev |
| [filestore_sloppy_crc_block_size](#filestore_sloppy_crc_block_size) | `64_K` | Dev | Dev |
| [filestore_splice](#filestore_splice) | `False` | Advanced | Performance |
| [filestore_split_multiple](#filestore_split_multiple) | `2` | Dev | Dev |
| [filestore_split_rand_factor](#filestore_split_rand_factor) | `20` | Dev | Dev |
| [filestore_update_to](#filestore_update_to) | `1000` | Dev | Dev |
| [filestore_wbthrottle_btrfs_bytes_hard_limit](#filestore_wbthrottle_btrfs_bytes_hard_limit) | `400_M` | Advanced | Performance |
| [filestore_wbthrottle_btrfs_bytes_start_flusher](#filestore_wbthrottle_btrfs_bytes_start_flusher) | `40_M` | Advanced | Performance |
| [filestore_wbthrottle_btrfs_inodes_hard_limit](#filestore_wbthrottle_btrfs_inodes_hard_limit) | `5000` | Advanced | Performance |
| [filestore_wbthrottle_btrfs_inodes_start_flusher](#filestore_wbthrottle_btrfs_inodes_start_flusher) | `500` | Advanced | Performance |
| [filestore_wbthrottle_btrfs_ios_hard_limit](#filestore_wbthrottle_btrfs_ios_hard_limit) | `5000` | Advanced | Performance |
| [filestore_wbthrottle_btrfs_ios_start_flusher](#filestore_wbthrottle_btrfs_ios_start_flusher) | `500` | Advanced | Performance |
| [filestore_wbthrottle_enable](#filestore_wbthrottle_enable) | `True` | Advanced | Policy |
| [filestore_wbthrottle_xfs_bytes_hard_limit](#filestore_wbthrottle_xfs_bytes_hard_limit) | `400_M` | Advanced | Performance |
| [filestore_wbthrottle_xfs_bytes_start_flusher](#filestore_wbthrottle_xfs_bytes_start_flusher) | `40_M` | Advanced | Performance |
| [filestore_wbthrottle_xfs_inodes_hard_limit](#filestore_wbthrottle_xfs_inodes_hard_limit) | `5000` | Advanced | Performance |
| [filestore_wbthrottle_xfs_inodes_start_flusher](#filestore_wbthrottle_xfs_inodes_start_flusher) | `500` | Advanced | Performance |
| [filestore_wbthrottle_xfs_ios_hard_limit](#filestore_wbthrottle_xfs_ios_hard_limit) | `5000` | Advanced | Performance |
| [filestore_wbthrottle_xfs_ios_start_flusher](#filestore_wbthrottle_xfs_ios_start_flusher) | `500` | Advanced | Performance |
| [filestore_xfs_extsize](#filestore_xfs_extsize) | `False` | Advanced | Performance |
| [filestore_zfs_snap](#filestore_zfs_snap) | `False` | Dev | Dev |

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

### filestore_apply_finisher_threads

| | |
|---|---|
| Type | Int · default `1` · **Dev** |
| Table | [filestore.md#SP_filestore_apply_finisher_threads](../../../config/global/filestore.md#SP_filestore_apply_finisher_threads) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_apply_finisher_threads 1
ceph config get global filestore_apply_finisher_threads
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_blackhole

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [filestore.md#SP_filestore_blackhole](../../../config/global/filestore.md#SP_filestore_blackhole) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_blackhole true
ceph config get global filestore_blackhole
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_btrfs_clone_range

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [filestore.md#SP_filestore_btrfs_clone_range](../../../config/global/filestore.md#SP_filestore_btrfs_clone_range) |

**What it does:** Use btrfs clone_range ioctl to efficiently duplicate objects (deprecated)

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global filestore_btrfs_clone_range false
ceph config get global filestore_btrfs_clone_range
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_btrfs_clone_range
ceph -s
```

---

### filestore_btrfs_snap

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [filestore.md#SP_filestore_btrfs_snap](../../../config/global/filestore.md#SP_filestore_btrfs_snap) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_btrfs_snap false
ceph config get global filestore_btrfs_snap
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_caller_concurrency

| | |
|---|---|
| Type | Int · default `10` · **Dev** |
| Table | [filestore.md#SP_filestore_caller_concurrency](../../../config/global/filestore.md#SP_filestore_caller_concurrency) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_caller_concurrency 10
ceph config get global filestore_caller_concurrency
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`10`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_collect_device_partition_information

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [filestore.md#SP_filestore_collect_device_partition_information](../../../config/global/filestore.md#SP_filestore_collect_device_partition_information) |

**What it does:** Collect metadata about the backing file system on OSD startup (deprecated)

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global filestore_collect_device_partition_information false
ceph config get global filestore_collect_device_partition_information
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_collect_device_partition_information
ceph -s
```

---

### filestore_commit_timeout

| | |
|---|---|
| Type | Float · default `10_min` · **Advanced** |
| Table | [filestore.md#SP_filestore_commit_timeout](../../../config/global/filestore.md#SP_filestore_commit_timeout) |

**What it does:** Seconds before backing file system is considered hung (deprecated)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global filestore_commit_timeout 10_min
ceph config get global filestore_commit_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_commit_timeout
ceph -s
```

---

### filestore_debug_inject_read_err

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [filestore.md#SP_filestore_debug_inject_read_err](../../../config/global/filestore.md#SP_filestore_debug_inject_read_err) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_debug_inject_read_err true
ceph config get global filestore_debug_inject_read_err
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_debug_omap_check

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [filestore.md#SP_filestore_debug_omap_check](../../../config/global/filestore.md#SP_filestore_debug_omap_check) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_debug_omap_check true
ceph config get global filestore_debug_omap_check
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_debug_verify_split

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [filestore.md#SP_filestore_debug_verify_split](../../../config/global/filestore.md#SP_filestore_debug_verify_split) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_debug_verify_split true
ceph config get global filestore_debug_verify_split
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_dump_file

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** |
| Table | [filestore.md#SP_filestore_dump_file](../../../config/global/filestore.md#SP_filestore_dump_file) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_dump_file "example"
ceph config get global filestore_dump_file
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`(empty)`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_expected_throughput_bytes

| | |
|---|---|
| Type | Float · default `209715200` · **Advanced** |
| Table | [filestore.md#SP_filestore_expected_throughput_bytes](../../../config/global/filestore.md#SP_filestore_expected_throughput_bytes) |

**What it does:** Expected throughput of backend device (aids throttling calculations) (deprecated)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global filestore_expected_throughput_bytes 209715200
ceph config get global filestore_expected_throughput_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `209715200`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_expected_throughput_bytes
ceph -s
```

---

### filestore_expected_throughput_ops

| | |
|---|---|
| Type | Float · default `200` · **Advanced** |
| Table | [filestore.md#SP_filestore_expected_throughput_ops](../../../config/global/filestore.md#SP_filestore_expected_throughput_ops) |

**What it does:** Expected through of backend device in IOPS (aids throttling calculations) (deprecated)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global filestore_expected_throughput_ops 200
ceph config get global filestore_expected_throughput_ops
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `200`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_expected_throughput_ops
ceph -s
```

---

### filestore_fadvise

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [filestore.md#SP_filestore_fadvise](../../../config/global/filestore.md#SP_filestore_fadvise) |

**What it does:** Use posix_fadvise(2) to pass hints to file system (deprecated)

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global filestore_fadvise false
ceph config get global filestore_fadvise
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_fadvise
ceph -s
```

---

### filestore_fail_eio

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [filestore.md#SP_filestore_fail_eio](../../../config/global/filestore.md#SP_filestore_fail_eio) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_fail_eio false
ceph config get global filestore_fail_eio
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_fd_cache_shards

| | |
|---|---|
| Type | Int · default `16` · **Dev** |
| Table | [filestore.md#SP_filestore_fd_cache_shards](../../../config/global/filestore.md#SP_filestore_fd_cache_shards) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_fd_cache_shards 16
ceph config get global filestore_fd_cache_shards
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`16`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_fd_cache_size

| | |
|---|---|
| Type | Int · default `128` · **Dev** |
| Table | [filestore.md#SP_filestore_fd_cache_size](../../../config/global/filestore.md#SP_filestore_fd_cache_size) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_fd_cache_size 128
ceph config get global filestore_fd_cache_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`128`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_fiemap

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [filestore.md#SP_filestore_fiemap](../../../config/global/filestore.md#SP_filestore_fiemap) |

**What it does:** Use fiemap ioctl(2) to determine which parts of objects are sparse (deprecated)

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global filestore_fiemap true
ceph config get global filestore_fiemap
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_fiemap
ceph -s
```

---

### filestore_fiemap_threshold

| | |
|---|---|
| Type | Size · default `4_K` · **Dev** |
| Table | [filestore.md#SP_filestore_fiemap_threshold](../../../config/global/filestore.md#SP_filestore_fiemap_threshold) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_fiemap_threshold 4_K
ceph config get global filestore_fiemap_threshold
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`4_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_fsync_flushes_journal_data

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [filestore.md#SP_filestore_fsync_flushes_journal_data](../../../config/global/filestore.md#SP_filestore_fsync_flushes_journal_data) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_fsync_flushes_journal_data true
ceph config get global filestore_fsync_flushes_journal_data
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_index_retry_probability

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [filestore.md#SP_filestore_index_retry_probability](../../../config/global/filestore.md#SP_filestore_index_retry_probability) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_index_retry_probability 0
ceph config get global filestore_index_retry_probability
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_inject_stall

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [filestore.md#SP_filestore_inject_stall](../../../config/global/filestore.md#SP_filestore_inject_stall) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_inject_stall 64
ceph config get global filestore_inject_stall
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_journal_parallel

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [filestore.md#SP_filestore_journal_parallel](../../../config/global/filestore.md#SP_filestore_journal_parallel) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_journal_parallel true
ceph config get global filestore_journal_parallel
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_journal_trailing

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [filestore.md#SP_filestore_journal_trailing](../../../config/global/filestore.md#SP_filestore_journal_trailing) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_journal_trailing true
ceph config get global filestore_journal_trailing
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_journal_writeahead

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [filestore.md#SP_filestore_journal_writeahead](../../../config/global/filestore.md#SP_filestore_journal_writeahead) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_journal_writeahead true
ceph config get global filestore_journal_writeahead
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_kill_at

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [filestore.md#SP_filestore_kill_at](../../../config/global/filestore.md#SP_filestore_kill_at) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_kill_at 64
ceph config get global filestore_kill_at
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_max_alloc_hint_size

| | |
|---|---|
| Type | Size · default `1_M` · **Dev** |
| Table | [filestore.md#SP_filestore_max_alloc_hint_size](../../../config/global/filestore.md#SP_filestore_max_alloc_hint_size) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_max_alloc_hint_size 1_M
ceph config get global filestore_max_alloc_hint_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1_M`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_max_inline_xattr_size

| | |
|---|---|
| Type | Size · default `0` · **Dev** |
| Table | [filestore.md#SP_filestore_max_inline_xattr_size](../../../config/global/filestore.md#SP_filestore_max_inline_xattr_size) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_max_inline_xattr_size 64
ceph config get global filestore_max_inline_xattr_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_max_inline_xattr_size_btrfs

| | |
|---|---|
| Type | Size · default `2_K` · **Dev** |
| Table | [filestore.md#SP_filestore_max_inline_xattr_size_btrfs](../../../config/global/filestore.md#SP_filestore_max_inline_xattr_size_btrfs) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_max_inline_xattr_size_btrfs 2_K
ceph config get global filestore_max_inline_xattr_size_btrfs
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`2_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_max_inline_xattr_size_other

| | |
|---|---|
| Type | Size · default `512` · **Dev** |
| Table | [filestore.md#SP_filestore_max_inline_xattr_size_other](../../../config/global/filestore.md#SP_filestore_max_inline_xattr_size_other) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_max_inline_xattr_size_other 512
ceph config get global filestore_max_inline_xattr_size_other
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`512`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_max_inline_xattr_size_xfs

| | |
|---|---|
| Type | Size · default `64_K` · **Dev** |
| Table | [filestore.md#SP_filestore_max_inline_xattr_size_xfs](../../../config/global/filestore.md#SP_filestore_max_inline_xattr_size_xfs) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_max_inline_xattr_size_xfs 64_K
ceph config get global filestore_max_inline_xattr_size_xfs
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`64_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_max_inline_xattrs

| | |
|---|---|
| Type | Uint · default `0` · **Dev** |
| Table | [filestore.md#SP_filestore_max_inline_xattrs](../../../config/global/filestore.md#SP_filestore_max_inline_xattrs) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_max_inline_xattrs 64
ceph config get global filestore_max_inline_xattrs
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_max_inline_xattrs_btrfs

| | |
|---|---|
| Type | Uint · default `10` · **Dev** |
| Table | [filestore.md#SP_filestore_max_inline_xattrs_btrfs](../../../config/global/filestore.md#SP_filestore_max_inline_xattrs_btrfs) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_max_inline_xattrs_btrfs 10
ceph config get global filestore_max_inline_xattrs_btrfs
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`10`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_max_inline_xattrs_other

| | |
|---|---|
| Type | Uint · default `2` · **Dev** |
| Table | [filestore.md#SP_filestore_max_inline_xattrs_other](../../../config/global/filestore.md#SP_filestore_max_inline_xattrs_other) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_max_inline_xattrs_other 2
ceph config get global filestore_max_inline_xattrs_other
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`2`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_max_inline_xattrs_xfs

| | |
|---|---|
| Type | Uint · default `10` · **Dev** |
| Table | [filestore.md#SP_filestore_max_inline_xattrs_xfs](../../../config/global/filestore.md#SP_filestore_max_inline_xattrs_xfs) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_max_inline_xattrs_xfs 10
ceph config get global filestore_max_inline_xattrs_xfs
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`10`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_max_sync_interval

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [filestore.md#SP_filestore_max_sync_interval](../../../config/global/filestore.md#SP_filestore_max_sync_interval) |

**What it does:** Period between calls to syncfs(2) and journal trims (seconds)(Deprecated)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global filestore_max_sync_interval 5
ceph config get global filestore_max_sync_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_max_sync_interval
ceph -s
```

---

### filestore_max_xattr_value_size

| | |
|---|---|
| Type | Size · default `0` · **Dev** |
| Table | [filestore.md#SP_filestore_max_xattr_value_size](../../../config/global/filestore.md#SP_filestore_max_xattr_value_size) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_max_xattr_value_size 64
ceph config get global filestore_max_xattr_value_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_max_xattr_value_size_btrfs

| | |
|---|---|
| Type | Size · default `64_K` · **Dev** |
| Table | [filestore.md#SP_filestore_max_xattr_value_size_btrfs](../../../config/global/filestore.md#SP_filestore_max_xattr_value_size_btrfs) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_max_xattr_value_size_btrfs 64_K
ceph config get global filestore_max_xattr_value_size_btrfs
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`64_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_max_xattr_value_size_other

| | |
|---|---|
| Type | Size · default `1_K` · **Dev** |
| Table | [filestore.md#SP_filestore_max_xattr_value_size_other](../../../config/global/filestore.md#SP_filestore_max_xattr_value_size_other) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_max_xattr_value_size_other 1_K
ceph config get global filestore_max_xattr_value_size_other
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_max_xattr_value_size_xfs

| | |
|---|---|
| Type | Size · default `64_K` · **Dev** |
| Table | [filestore.md#SP_filestore_max_xattr_value_size_xfs](../../../config/global/filestore.md#SP_filestore_max_xattr_value_size_xfs) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_max_xattr_value_size_xfs 64_K
ceph config get global filestore_max_xattr_value_size_xfs
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`64_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_merge_threshold

| | |
|---|---|
| Type | Int · default `-10` · **Dev** |
| Table | [filestore.md#SP_filestore_merge_threshold](../../../config/global/filestore.md#SP_filestore_merge_threshold) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_merge_threshold -10
ceph config get global filestore_merge_threshold
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`-10`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_min_sync_interval

| | |
|---|---|
| Type | Float · default `0.01` · **Dev** |
| Table | [filestore.md#SP_filestore_min_sync_interval](../../../config/global/filestore.md#SP_filestore_min_sync_interval) |

**What it does:** Minimum period between calls to syncfs(2) (deprecated)

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_min_sync_interval 0.01
ceph config get global filestore_min_sync_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.01`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_odsync_write

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [filestore.md#SP_filestore_odsync_write](../../../config/global/filestore.md#SP_filestore_odsync_write) |

**What it does:** Write with O_DSYNC (deprecated)

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_odsync_write true
ceph config get global filestore_odsync_write
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_omap_backend

| | |
|---|---|
| Type | Str · enum: ["leveldb", "rocksdb"] · default `rocksdb` · **Dev** |
| Table | [filestore.md#SP_filestore_omap_backend](../../../config/global/filestore.md#SP_filestore_omap_backend) |

**What it does:** The KeyValueDB to use for Filestore metadata (that is, omaps) (deprecated).

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_omap_backend rocksdb
ceph config get global filestore_omap_backend
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`rocksdb`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_omap_backend_path

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** |
| Table | [filestore.md#SP_filestore_omap_backend_path](../../../config/global/filestore.md#SP_filestore_omap_backend_path) |

**What it does:** The path where the Filestore KeyValueDB should store its database(s) (deprecated)

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_omap_backend_path "/var/lib/ceph/example"
ceph config get global filestore_omap_backend_path
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`(empty)`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_omap_header_cache_size

| | |
|---|---|
| Type | Size · default `1_K` · **Dev** |
| Table | [filestore.md#SP_filestore_omap_header_cache_size](../../../config/global/filestore.md#SP_filestore_omap_header_cache_size) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_omap_header_cache_size 1_K
ceph config get global filestore_omap_header_cache_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_ondisk_finisher_threads

| | |
|---|---|
| Type | Int · default `1` · **Dev** |
| Table | [filestore.md#SP_filestore_ondisk_finisher_threads](../../../config/global/filestore.md#SP_filestore_ondisk_finisher_threads) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_ondisk_finisher_threads 1
ceph config get global filestore_ondisk_finisher_threads
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_op_thread_suicide_timeout

| | |
|---|---|
| Type | Int · default `3_min` · **Advanced** |
| Table | [filestore.md#SP_filestore_op_thread_suicide_timeout](../../../config/global/filestore.md#SP_filestore_op_thread_suicide_timeout) |

**What it does:** Seconds before a worker thread is considered dead (deprecated)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global filestore_op_thread_suicide_timeout 3_min
ceph config get global filestore_op_thread_suicide_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_op_thread_suicide_timeout
ceph -s
```

---

### filestore_op_thread_timeout

| | |
|---|---|
| Type | Int · default `1_min` · **Advanced** |
| Table | [filestore.md#SP_filestore_op_thread_timeout](../../../config/global/filestore.md#SP_filestore_op_thread_timeout) |

**What it does:** Seconds before a worker thread is considered stalled (deprecated)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global filestore_op_thread_timeout 1_min
ceph config get global filestore_op_thread_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_op_thread_timeout
ceph -s
```

---

### filestore_op_threads

| | |
|---|---|
| Type | Int · default `2` · **Advanced** |
| Table | [filestore.md#SP_filestore_op_threads](../../../config/global/filestore.md#SP_filestore_op_threads) |

**What it does:** Threads used to apply changes to backing file system (deprecated)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global filestore_op_threads 2
ceph config get global filestore_op_threads
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_op_threads
ceph -s
```

---

### filestore_punch_hole

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [filestore.md#SP_filestore_punch_hole](../../../config/global/filestore.md#SP_filestore_punch_hole) |

**What it does:** Use fallocate(2) FALLOC_FL_PUNCH_HOLE to efficiently zero ranges of objects (deprecated)

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global filestore_punch_hole true
ceph config get global filestore_punch_hole
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_punch_hole
ceph -s
```

---

### filestore_queue_high_delay_multiple

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [filestore.md#SP_filestore_queue_high_delay_multiple](../../../config/global/filestore.md#SP_filestore_queue_high_delay_multiple) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_queue_high_delay_multiple 0
ceph config get global filestore_queue_high_delay_multiple
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_queue_high_delay_multiple_bytes

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [filestore.md#SP_filestore_queue_high_delay_multiple_bytes](../../../config/global/filestore.md#SP_filestore_queue_high_delay_multiple_bytes) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_queue_high_delay_multiple_bytes 0
ceph config get global filestore_queue_high_delay_multiple_bytes
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_queue_high_delay_multiple_ops

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [filestore.md#SP_filestore_queue_high_delay_multiple_ops](../../../config/global/filestore.md#SP_filestore_queue_high_delay_multiple_ops) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_queue_high_delay_multiple_ops 0
ceph config get global filestore_queue_high_delay_multiple_ops
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_queue_high_threshhold

| | |
|---|---|
| Type | Float · default `0.9` · **Dev** |
| Table | [filestore.md#SP_filestore_queue_high_threshhold](../../../config/global/filestore.md#SP_filestore_queue_high_threshhold) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_queue_high_threshhold 0.9
ceph config get global filestore_queue_high_threshhold
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.9`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_queue_low_threshhold

| | |
|---|---|
| Type | Float · default `0.3` · **Dev** |
| Table | [filestore.md#SP_filestore_queue_low_threshhold](../../../config/global/filestore.md#SP_filestore_queue_low_threshhold) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_queue_low_threshhold 0.3
ceph config get global filestore_queue_low_threshhold
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.3`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_queue_max_bytes

| | |
|---|---|
| Type | Size · default `100_M` · **Advanced** |
| Table | [filestore.md#SP_filestore_queue_max_bytes](../../../config/global/filestore.md#SP_filestore_queue_max_bytes) |

**What it does:** Max (written) bytes in flight (deprecated)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global filestore_queue_max_bytes 100_M
ceph config get global filestore_queue_max_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_queue_max_bytes
ceph -s
```

---

### filestore_queue_max_delay_multiple

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [filestore.md#SP_filestore_queue_max_delay_multiple](../../../config/global/filestore.md#SP_filestore_queue_max_delay_multiple) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_queue_max_delay_multiple 0
ceph config get global filestore_queue_max_delay_multiple
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_queue_max_delay_multiple_bytes

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [filestore.md#SP_filestore_queue_max_delay_multiple_bytes](../../../config/global/filestore.md#SP_filestore_queue_max_delay_multiple_bytes) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_queue_max_delay_multiple_bytes 0
ceph config get global filestore_queue_max_delay_multiple_bytes
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_queue_max_delay_multiple_ops

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [filestore.md#SP_filestore_queue_max_delay_multiple_ops](../../../config/global/filestore.md#SP_filestore_queue_max_delay_multiple_ops) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_queue_max_delay_multiple_ops 0
ceph config get global filestore_queue_max_delay_multiple_ops
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_queue_max_ops

| | |
|---|---|
| Type | Uint · default `50` · **Advanced** |
| Table | [filestore.md#SP_filestore_queue_max_ops](../../../config/global/filestore.md#SP_filestore_queue_max_ops) |

**What it does:** Max IO operations in flight (deprecated)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global filestore_queue_max_ops 50
ceph config get global filestore_queue_max_ops
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `50`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_queue_max_ops
ceph -s
```

---

### filestore_rocksdb_options

| | |
|---|---|
| Type | Str · default `max_background_jobs=10,compaction_readahead_size=2097152,compression=kNoCompression` · **Dev** |
| Table | [filestore.md#SP_filestore_rocksdb_options](../../../config/global/filestore.md#SP_filestore_rocksdb_options) |

**What it does:** Options to pass through when RocksDB is used as the KeyValueDB for (deprecated) Filestore.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_rocksdb_options "max_background_jobs=10,compaction_readahead_size=2097152,compression=kNoCompression"
ceph config get global filestore_rocksdb_options
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`max_background_jobs=10,compaction_readahead_size=2097152,compression=kNoCompression`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_seek_data_hole

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [filestore.md#SP_filestore_seek_data_hole](../../../config/global/filestore.md#SP_filestore_seek_data_hole) |

**What it does:** Use lseek(2) SEEK_HOLE and SEEK_DATA to determine which parts of objects are sparse (deprecated)

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global filestore_seek_data_hole true
ceph config get global filestore_seek_data_hole
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_seek_data_hole
ceph -s
```

---

### filestore_sloppy_crc

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [filestore.md#SP_filestore_sloppy_crc](../../../config/global/filestore.md#SP_filestore_sloppy_crc) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_sloppy_crc true
ceph config get global filestore_sloppy_crc
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_sloppy_crc_block_size

| | |
|---|---|
| Type | Size · default `64_K` · **Dev** |
| Table | [filestore.md#SP_filestore_sloppy_crc_block_size](../../../config/global/filestore.md#SP_filestore_sloppy_crc_block_size) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_sloppy_crc_block_size 64_K
ceph config get global filestore_sloppy_crc_block_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`64_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_splice

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [filestore.md#SP_filestore_splice](../../../config/global/filestore.md#SP_filestore_splice) |

**What it does:** Use splice(2) to more efficiently copy data between files (deprecated)

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global filestore_splice true
ceph config get global filestore_splice
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_splice
ceph -s
```

---

### filestore_split_multiple

| | |
|---|---|
| Type | Int · default `2` · **Dev** |
| Table | [filestore.md#SP_filestore_split_multiple](../../../config/global/filestore.md#SP_filestore_split_multiple) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_split_multiple 2
ceph config get global filestore_split_multiple
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`2`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_split_rand_factor

| | |
|---|---|
| Type | Uint · default `20` · **Dev** |
| Table | [filestore.md#SP_filestore_split_rand_factor](../../../config/global/filestore.md#SP_filestore_split_rand_factor) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_split_rand_factor 20
ceph config get global filestore_split_rand_factor
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`20`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_update_to

| | |
|---|---|
| Type | Int · default `1000` · **Dev** |
| Table | [filestore.md#SP_filestore_update_to](../../../config/global/filestore.md#SP_filestore_update_to) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_update_to 1000
ceph config get global filestore_update_to
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1000`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### filestore_wbthrottle_btrfs_bytes_hard_limit

| | |
|---|---|
| Type | Size · default `400_M` · **Advanced** |
| Table | [filestore.md#SP_filestore_wbthrottle_btrfs_bytes_hard_limit](../../../config/global/filestore.md#SP_filestore_wbthrottle_btrfs_bytes_hard_limit) |

**What it does:** Block writes when this many bytes haven't been flushed (fsynced) (btrfs, deprecated)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global filestore_wbthrottle_btrfs_bytes_hard_limit 400_M
ceph config get global filestore_wbthrottle_btrfs_bytes_hard_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `400_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_wbthrottle_btrfs_bytes_hard_limit
ceph -s
```

---

### filestore_wbthrottle_btrfs_bytes_start_flusher

| | |
|---|---|
| Type | Size · default `40_M` · **Advanced** |
| Table | [filestore.md#SP_filestore_wbthrottle_btrfs_bytes_start_flusher](../../../config/global/filestore.md#SP_filestore_wbthrottle_btrfs_bytes_start_flusher) |

**What it does:** Start flushing (fsyncing) when this many bytes are written (btrfs, deprecated)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global filestore_wbthrottle_btrfs_bytes_start_flusher 40_M
ceph config get global filestore_wbthrottle_btrfs_bytes_start_flusher
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `40_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_wbthrottle_btrfs_bytes_start_flusher
ceph -s
```

---

### filestore_wbthrottle_btrfs_inodes_hard_limit

| | |
|---|---|
| Type | Uint · default `5000` · **Advanced** |
| Table | [filestore.md#SP_filestore_wbthrottle_btrfs_inodes_hard_limit](../../../config/global/filestore.md#SP_filestore_wbthrottle_btrfs_inodes_hard_limit) |

**What it does:** Block writing when this many inodes have outstanding writes (btrfs, deprecated)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global filestore_wbthrottle_btrfs_inodes_hard_limit 5000
ceph config get global filestore_wbthrottle_btrfs_inodes_hard_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_wbthrottle_btrfs_inodes_hard_limit
ceph -s
```

---

### filestore_wbthrottle_btrfs_inodes_start_flusher

| | |
|---|---|
| Type | Uint · default `500` · **Advanced** |
| Table | [filestore.md#SP_filestore_wbthrottle_btrfs_inodes_start_flusher](../../../config/global/filestore.md#SP_filestore_wbthrottle_btrfs_inodes_start_flusher) |

**What it does:** Start flushing (fsyncing) when this many distinct inodes have been modified (deprecated) (btrfs)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global filestore_wbthrottle_btrfs_inodes_start_flusher 500
ceph config get global filestore_wbthrottle_btrfs_inodes_start_flusher
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_wbthrottle_btrfs_inodes_start_flusher
ceph -s
```

---

### filestore_wbthrottle_btrfs_ios_hard_limit

| | |
|---|---|
| Type | Uint · default `5000` · **Advanced** |
| Table | [filestore.md#SP_filestore_wbthrottle_btrfs_ios_hard_limit](../../../config/global/filestore.md#SP_filestore_wbthrottle_btrfs_ios_hard_limit) |

**What it does:** Block writes when this many IOs haven't been flushed (fsynced) (btrfs,deprecated)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global filestore_wbthrottle_btrfs_ios_hard_limit 5000
ceph config get global filestore_wbthrottle_btrfs_ios_hard_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_wbthrottle_btrfs_ios_hard_limit
ceph -s
```

---

### filestore_wbthrottle_btrfs_ios_start_flusher

| | |
|---|---|
| Type | Uint · default `500` · **Advanced** |
| Table | [filestore.md#SP_filestore_wbthrottle_btrfs_ios_start_flusher](../../../config/global/filestore.md#SP_filestore_wbthrottle_btrfs_ios_start_flusher) |

**What it does:** Start flushing (fsyncing) when this many IOs are written (brtrfs, deprecated)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global filestore_wbthrottle_btrfs_ios_start_flusher 500
ceph config get global filestore_wbthrottle_btrfs_ios_start_flusher
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_wbthrottle_btrfs_ios_start_flusher
ceph -s
```

---

### filestore_wbthrottle_enable

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [filestore.md#SP_filestore_wbthrottle_enable](../../../config/global/filestore.md#SP_filestore_wbthrottle_enable) |

**What it does:** Enabling throttling of operations to backing file system (deprecated)

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global filestore_wbthrottle_enable false
ceph config get global filestore_wbthrottle_enable
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_wbthrottle_enable
ceph -s
```

---

### filestore_wbthrottle_xfs_bytes_hard_limit

| | |
|---|---|
| Type | Size · default `400_M` · **Advanced** |
| Table | [filestore.md#SP_filestore_wbthrottle_xfs_bytes_hard_limit](../../../config/global/filestore.md#SP_filestore_wbthrottle_xfs_bytes_hard_limit) |

**What it does:** Block writes when this many bytes haven't been flushed (fsynced) (xfs, deprecated)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global filestore_wbthrottle_xfs_bytes_hard_limit 400_M
ceph config get global filestore_wbthrottle_xfs_bytes_hard_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `400_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_wbthrottle_xfs_bytes_hard_limit
ceph -s
```

---

### filestore_wbthrottle_xfs_bytes_start_flusher

| | |
|---|---|
| Type | Size · default `40_M` · **Advanced** |
| Table | [filestore.md#SP_filestore_wbthrottle_xfs_bytes_start_flusher](../../../config/global/filestore.md#SP_filestore_wbthrottle_xfs_bytes_start_flusher) |

**What it does:** Start flushing (fsyncing) when this many bytes are written (xfs, deprecated)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global filestore_wbthrottle_xfs_bytes_start_flusher 40_M
ceph config get global filestore_wbthrottle_xfs_bytes_start_flusher
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `40_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_wbthrottle_xfs_bytes_start_flusher
ceph -s
```

---

### filestore_wbthrottle_xfs_inodes_hard_limit

| | |
|---|---|
| Type | Uint · default `5000` · **Advanced** |
| Table | [filestore.md#SP_filestore_wbthrottle_xfs_inodes_hard_limit](../../../config/global/filestore.md#SP_filestore_wbthrottle_xfs_inodes_hard_limit) |

**What it does:** Block writing when this many inodes have outstanding writes (xfs, deprecated)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global filestore_wbthrottle_xfs_inodes_hard_limit 5000
ceph config get global filestore_wbthrottle_xfs_inodes_hard_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_wbthrottle_xfs_inodes_hard_limit
ceph -s
```

---

### filestore_wbthrottle_xfs_inodes_start_flusher

| | |
|---|---|
| Type | Uint · default `500` · **Advanced** |
| Table | [filestore.md#SP_filestore_wbthrottle_xfs_inodes_start_flusher](../../../config/global/filestore.md#SP_filestore_wbthrottle_xfs_inodes_start_flusher) |

**What it does:** Start flushing (fsyncing) when this many distinct inodes have been modified (xfs, deprecated)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global filestore_wbthrottle_xfs_inodes_start_flusher 500
ceph config get global filestore_wbthrottle_xfs_inodes_start_flusher
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_wbthrottle_xfs_inodes_start_flusher
ceph -s
```

---

### filestore_wbthrottle_xfs_ios_hard_limit

| | |
|---|---|
| Type | Uint · default `5000` · **Advanced** |
| Table | [filestore.md#SP_filestore_wbthrottle_xfs_ios_hard_limit](../../../config/global/filestore.md#SP_filestore_wbthrottle_xfs_ios_hard_limit) |

**What it does:** Block writes when this many IOs haven't been flushed (fsynced) (xfs, deprecated)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global filestore_wbthrottle_xfs_ios_hard_limit 5000
ceph config get global filestore_wbthrottle_xfs_ios_hard_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_wbthrottle_xfs_ios_hard_limit
ceph -s
```

---

### filestore_wbthrottle_xfs_ios_start_flusher

| | |
|---|---|
| Type | Uint · default `500` · **Advanced** |
| Table | [filestore.md#SP_filestore_wbthrottle_xfs_ios_start_flusher](../../../config/global/filestore.md#SP_filestore_wbthrottle_xfs_ios_start_flusher) |

**What it does:** Start flushing (fsyncing) when this many IOs are written (xfs, deprecated)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global filestore_wbthrottle_xfs_ios_start_flusher 500
ceph config get global filestore_wbthrottle_xfs_ios_start_flusher
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_wbthrottle_xfs_ios_start_flusher
ceph -s
```

---

### filestore_xfs_extsize

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [filestore.md#SP_filestore_xfs_extsize](../../../config/global/filestore.md#SP_filestore_xfs_extsize) |

**What it does:** Use XFS extsize ioctl(2) to hint allocator about expected write sizes (deprecated)

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global filestore_xfs_extsize true
ceph config get global filestore_xfs_extsize
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filestore_xfs_extsize
ceph -s
```

---

### filestore_zfs_snap

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [filestore.md#SP_filestore_zfs_snap](../../../config/global/filestore.md#SP_filestore_zfs_snap) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global filestore_zfs_snap true
ceph config get global filestore_zfs_snap
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
