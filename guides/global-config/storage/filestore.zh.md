# Filestore

Global 配置深度指南 — 84 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
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

## 寻找最优值

| 模型 | 如何选择 |
|-------|---------------|
| **Policy** | 安全、兼容性、运维默认值 |
| **Capacity** | 磁盘布局、路径、容量规划 |
| **Performance** | 基线 → 逐步调整 → 监控集群 |
| **Connectivity** | 最近且稳定的外部端点 |
| **Dev** | 生产环境保持 upstream 默认值 |

**常用工具：**

```bash
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### filestore_apply_finisher_threads

| | |
|---|---|
| 类型 | Int · default `1` · **Dev** |
| 表格 | [filestore.md#SP_filestore_apply_finisher_threads](../../../config/global/filestore.md#SP_filestore_apply_finisher_threads) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_apply_finisher_threads 1
ceph config get global filestore_apply_finisher_threads
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_blackhole

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [filestore.md#SP_filestore_blackhole](../../../config/global/filestore.md#SP_filestore_blackhole) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_blackhole true
ceph config get global filestore_blackhole
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_btrfs_clone_range

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_btrfs_clone_range](../../../config/global/filestore.md#SP_filestore_btrfs_clone_range) |

**作用：** Use btrfs clone_range ioctl to efficiently duplicate objects (deprecated)

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global filestore_btrfs_clone_range false
ceph config get global filestore_btrfs_clone_range
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_btrfs_clone_range
ceph -s
```

---

### filestore_btrfs_snap

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [filestore.md#SP_filestore_btrfs_snap](../../../config/global/filestore.md#SP_filestore_btrfs_snap) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_btrfs_snap false
ceph config get global filestore_btrfs_snap
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_caller_concurrency

| | |
|---|---|
| 类型 | Int · default `10` · **Dev** |
| 表格 | [filestore.md#SP_filestore_caller_concurrency](../../../config/global/filestore.md#SP_filestore_caller_concurrency) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_caller_concurrency 10
ceph config get global filestore_caller_concurrency
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`10`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_collect_device_partition_information

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_collect_device_partition_information](../../../config/global/filestore.md#SP_filestore_collect_device_partition_information) |

**作用：** Collect metadata about the backing file system on OSD startup (deprecated)

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global filestore_collect_device_partition_information false
ceph config get global filestore_collect_device_partition_information
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_collect_device_partition_information
ceph -s
```

---

### filestore_commit_timeout

| | |
|---|---|
| 类型 | Float · default `10_min` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_commit_timeout](../../../config/global/filestore.md#SP_filestore_commit_timeout) |

**作用：** Seconds before backing file system is considered hung (deprecated)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global filestore_commit_timeout 10_min
ceph config get global filestore_commit_timeout
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_commit_timeout
ceph -s
```

---

### filestore_debug_inject_read_err

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [filestore.md#SP_filestore_debug_inject_read_err](../../../config/global/filestore.md#SP_filestore_debug_inject_read_err) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_debug_inject_read_err true
ceph config get global filestore_debug_inject_read_err
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_debug_omap_check

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [filestore.md#SP_filestore_debug_omap_check](../../../config/global/filestore.md#SP_filestore_debug_omap_check) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_debug_omap_check true
ceph config get global filestore_debug_omap_check
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_debug_verify_split

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [filestore.md#SP_filestore_debug_verify_split](../../../config/global/filestore.md#SP_filestore_debug_verify_split) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_debug_verify_split true
ceph config get global filestore_debug_verify_split
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_dump_file

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Dev** |
| 表格 | [filestore.md#SP_filestore_dump_file](../../../config/global/filestore.md#SP_filestore_dump_file) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_dump_file "example"
ceph config get global filestore_dump_file
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`(empty)`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_expected_throughput_bytes

| | |
|---|---|
| 类型 | Float · default `209715200` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_expected_throughput_bytes](../../../config/global/filestore.md#SP_filestore_expected_throughput_bytes) |

**作用：** Expected throughput of backend device (aids throttling calculations) (deprecated)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global filestore_expected_throughput_bytes 209715200
ceph config get global filestore_expected_throughput_bytes
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `209715200` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_expected_throughput_bytes
ceph -s
```

---

### filestore_expected_throughput_ops

| | |
|---|---|
| 类型 | Float · default `200` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_expected_throughput_ops](../../../config/global/filestore.md#SP_filestore_expected_throughput_ops) |

**作用：** Expected through of backend device in IOPS (aids throttling calculations) (deprecated)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global filestore_expected_throughput_ops 200
ceph config get global filestore_expected_throughput_ops
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `200` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_expected_throughput_ops
ceph -s
```

---

### filestore_fadvise

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_fadvise](../../../config/global/filestore.md#SP_filestore_fadvise) |

**作用：** Use posix_fadvise(2) to pass hints to file system (deprecated)

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global filestore_fadvise false
ceph config get global filestore_fadvise
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_fadvise
ceph -s
```

---

### filestore_fail_eio

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [filestore.md#SP_filestore_fail_eio](../../../config/global/filestore.md#SP_filestore_fail_eio) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_fail_eio false
ceph config get global filestore_fail_eio
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_fd_cache_shards

| | |
|---|---|
| 类型 | Int · default `16` · **Dev** |
| 表格 | [filestore.md#SP_filestore_fd_cache_shards](../../../config/global/filestore.md#SP_filestore_fd_cache_shards) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_fd_cache_shards 16
ceph config get global filestore_fd_cache_shards
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`16`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_fd_cache_size

| | |
|---|---|
| 类型 | Int · default `128` · **Dev** |
| 表格 | [filestore.md#SP_filestore_fd_cache_size](../../../config/global/filestore.md#SP_filestore_fd_cache_size) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_fd_cache_size 128
ceph config get global filestore_fd_cache_size
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`128`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_fiemap

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_fiemap](../../../config/global/filestore.md#SP_filestore_fiemap) |

**作用：** Use fiemap ioctl(2) to determine which parts of objects are sparse (deprecated)

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global filestore_fiemap true
ceph config get global filestore_fiemap
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_fiemap
ceph -s
```

---

### filestore_fiemap_threshold

| | |
|---|---|
| 类型 | Size · default `4_K` · **Dev** |
| 表格 | [filestore.md#SP_filestore_fiemap_threshold](../../../config/global/filestore.md#SP_filestore_fiemap_threshold) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_fiemap_threshold 4_K
ceph config get global filestore_fiemap_threshold
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`4_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_fsync_flushes_journal_data

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [filestore.md#SP_filestore_fsync_flushes_journal_data](../../../config/global/filestore.md#SP_filestore_fsync_flushes_journal_data) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_fsync_flushes_journal_data true
ceph config get global filestore_fsync_flushes_journal_data
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_index_retry_probability

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [filestore.md#SP_filestore_index_retry_probability](../../../config/global/filestore.md#SP_filestore_index_retry_probability) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_index_retry_probability 0
ceph config get global filestore_index_retry_probability
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_inject_stall

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [filestore.md#SP_filestore_inject_stall](../../../config/global/filestore.md#SP_filestore_inject_stall) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_inject_stall 64
ceph config get global filestore_inject_stall
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_journal_parallel

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [filestore.md#SP_filestore_journal_parallel](../../../config/global/filestore.md#SP_filestore_journal_parallel) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_journal_parallel true
ceph config get global filestore_journal_parallel
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_journal_trailing

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [filestore.md#SP_filestore_journal_trailing](../../../config/global/filestore.md#SP_filestore_journal_trailing) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_journal_trailing true
ceph config get global filestore_journal_trailing
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_journal_writeahead

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [filestore.md#SP_filestore_journal_writeahead](../../../config/global/filestore.md#SP_filestore_journal_writeahead) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_journal_writeahead true
ceph config get global filestore_journal_writeahead
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_kill_at

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [filestore.md#SP_filestore_kill_at](../../../config/global/filestore.md#SP_filestore_kill_at) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_kill_at 64
ceph config get global filestore_kill_at
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_max_alloc_hint_size

| | |
|---|---|
| 类型 | Size · default `1_M` · **Dev** |
| 表格 | [filestore.md#SP_filestore_max_alloc_hint_size](../../../config/global/filestore.md#SP_filestore_max_alloc_hint_size) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_max_alloc_hint_size 1_M
ceph config get global filestore_max_alloc_hint_size
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`1_M`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_max_inline_xattr_size

| | |
|---|---|
| 类型 | Size · default `0` · **Dev** |
| 表格 | [filestore.md#SP_filestore_max_inline_xattr_size](../../../config/global/filestore.md#SP_filestore_max_inline_xattr_size) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_max_inline_xattr_size 64
ceph config get global filestore_max_inline_xattr_size
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_max_inline_xattr_size_btrfs

| | |
|---|---|
| 类型 | Size · default `2_K` · **Dev** |
| 表格 | [filestore.md#SP_filestore_max_inline_xattr_size_btrfs](../../../config/global/filestore.md#SP_filestore_max_inline_xattr_size_btrfs) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_max_inline_xattr_size_btrfs 2_K
ceph config get global filestore_max_inline_xattr_size_btrfs
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`2_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_max_inline_xattr_size_other

| | |
|---|---|
| 类型 | Size · default `512` · **Dev** |
| 表格 | [filestore.md#SP_filestore_max_inline_xattr_size_other](../../../config/global/filestore.md#SP_filestore_max_inline_xattr_size_other) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_max_inline_xattr_size_other 512
ceph config get global filestore_max_inline_xattr_size_other
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`512`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_max_inline_xattr_size_xfs

| | |
|---|---|
| 类型 | Size · default `64_K` · **Dev** |
| 表格 | [filestore.md#SP_filestore_max_inline_xattr_size_xfs](../../../config/global/filestore.md#SP_filestore_max_inline_xattr_size_xfs) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_max_inline_xattr_size_xfs 64_K
ceph config get global filestore_max_inline_xattr_size_xfs
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`64_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_max_inline_xattrs

| | |
|---|---|
| 类型 | Uint · default `0` · **Dev** |
| 表格 | [filestore.md#SP_filestore_max_inline_xattrs](../../../config/global/filestore.md#SP_filestore_max_inline_xattrs) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_max_inline_xattrs 64
ceph config get global filestore_max_inline_xattrs
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_max_inline_xattrs_btrfs

| | |
|---|---|
| 类型 | Uint · default `10` · **Dev** |
| 表格 | [filestore.md#SP_filestore_max_inline_xattrs_btrfs](../../../config/global/filestore.md#SP_filestore_max_inline_xattrs_btrfs) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_max_inline_xattrs_btrfs 10
ceph config get global filestore_max_inline_xattrs_btrfs
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`10`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_max_inline_xattrs_other

| | |
|---|---|
| 类型 | Uint · default `2` · **Dev** |
| 表格 | [filestore.md#SP_filestore_max_inline_xattrs_other](../../../config/global/filestore.md#SP_filestore_max_inline_xattrs_other) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_max_inline_xattrs_other 2
ceph config get global filestore_max_inline_xattrs_other
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`2`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_max_inline_xattrs_xfs

| | |
|---|---|
| 类型 | Uint · default `10` · **Dev** |
| 表格 | [filestore.md#SP_filestore_max_inline_xattrs_xfs](../../../config/global/filestore.md#SP_filestore_max_inline_xattrs_xfs) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_max_inline_xattrs_xfs 10
ceph config get global filestore_max_inline_xattrs_xfs
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`10`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_max_sync_interval

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_max_sync_interval](../../../config/global/filestore.md#SP_filestore_max_sync_interval) |

**作用：** Period between calls to syncfs(2) and journal trims (seconds)(Deprecated)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global filestore_max_sync_interval 5
ceph config get global filestore_max_sync_interval
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_max_sync_interval
ceph -s
```

---

### filestore_max_xattr_value_size

| | |
|---|---|
| 类型 | Size · default `0` · **Dev** |
| 表格 | [filestore.md#SP_filestore_max_xattr_value_size](../../../config/global/filestore.md#SP_filestore_max_xattr_value_size) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_max_xattr_value_size 64
ceph config get global filestore_max_xattr_value_size
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_max_xattr_value_size_btrfs

| | |
|---|---|
| 类型 | Size · default `64_K` · **Dev** |
| 表格 | [filestore.md#SP_filestore_max_xattr_value_size_btrfs](../../../config/global/filestore.md#SP_filestore_max_xattr_value_size_btrfs) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_max_xattr_value_size_btrfs 64_K
ceph config get global filestore_max_xattr_value_size_btrfs
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`64_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_max_xattr_value_size_other

| | |
|---|---|
| 类型 | Size · default `1_K` · **Dev** |
| 表格 | [filestore.md#SP_filestore_max_xattr_value_size_other](../../../config/global/filestore.md#SP_filestore_max_xattr_value_size_other) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_max_xattr_value_size_other 1_K
ceph config get global filestore_max_xattr_value_size_other
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`1_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_max_xattr_value_size_xfs

| | |
|---|---|
| 类型 | Size · default `64_K` · **Dev** |
| 表格 | [filestore.md#SP_filestore_max_xattr_value_size_xfs](../../../config/global/filestore.md#SP_filestore_max_xattr_value_size_xfs) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_max_xattr_value_size_xfs 64_K
ceph config get global filestore_max_xattr_value_size_xfs
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`64_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_merge_threshold

| | |
|---|---|
| 类型 | Int · default `-10` · **Dev** |
| 表格 | [filestore.md#SP_filestore_merge_threshold](../../../config/global/filestore.md#SP_filestore_merge_threshold) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_merge_threshold -10
ceph config get global filestore_merge_threshold
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`-10`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_min_sync_interval

| | |
|---|---|
| 类型 | Float · default `0.01` · **Dev** |
| 表格 | [filestore.md#SP_filestore_min_sync_interval](../../../config/global/filestore.md#SP_filestore_min_sync_interval) |

**作用：** Minimum period between calls to syncfs(2) (deprecated)

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_min_sync_interval 0.01
ceph config get global filestore_min_sync_interval
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0.01`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_odsync_write

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [filestore.md#SP_filestore_odsync_write](../../../config/global/filestore.md#SP_filestore_odsync_write) |

**作用：** Write with O_DSYNC (deprecated)

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_odsync_write true
ceph config get global filestore_odsync_write
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_omap_backend

| | |
|---|---|
| 类型 | Str · enum: ["leveldb", "rocksdb"] · default `rocksdb` · **Dev** |
| 表格 | [filestore.md#SP_filestore_omap_backend](../../../config/global/filestore.md#SP_filestore_omap_backend) |

**作用：** The KeyValueDB to use for Filestore metadata (that is, omaps) (deprecated).

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_omap_backend rocksdb
ceph config get global filestore_omap_backend
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`rocksdb`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_omap_backend_path

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Dev** |
| 表格 | [filestore.md#SP_filestore_omap_backend_path](../../../config/global/filestore.md#SP_filestore_omap_backend_path) |

**作用：** The path where the Filestore KeyValueDB should store its database(s) (deprecated)

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_omap_backend_path "/var/lib/ceph/example"
ceph config get global filestore_omap_backend_path
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`(empty)`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_omap_header_cache_size

| | |
|---|---|
| 类型 | Size · default `1_K` · **Dev** |
| 表格 | [filestore.md#SP_filestore_omap_header_cache_size](../../../config/global/filestore.md#SP_filestore_omap_header_cache_size) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_omap_header_cache_size 1_K
ceph config get global filestore_omap_header_cache_size
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`1_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_ondisk_finisher_threads

| | |
|---|---|
| 类型 | Int · default `1` · **Dev** |
| 表格 | [filestore.md#SP_filestore_ondisk_finisher_threads](../../../config/global/filestore.md#SP_filestore_ondisk_finisher_threads) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_ondisk_finisher_threads 1
ceph config get global filestore_ondisk_finisher_threads
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_op_thread_suicide_timeout

| | |
|---|---|
| 类型 | Int · default `3_min` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_op_thread_suicide_timeout](../../../config/global/filestore.md#SP_filestore_op_thread_suicide_timeout) |

**作用：** Seconds before a worker thread is considered dead (deprecated)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global filestore_op_thread_suicide_timeout 3_min
ceph config get global filestore_op_thread_suicide_timeout
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `3_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_op_thread_suicide_timeout
ceph -s
```

---

### filestore_op_thread_timeout

| | |
|---|---|
| 类型 | Int · default `1_min` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_op_thread_timeout](../../../config/global/filestore.md#SP_filestore_op_thread_timeout) |

**作用：** Seconds before a worker thread is considered stalled (deprecated)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global filestore_op_thread_timeout 1_min
ceph config get global filestore_op_thread_timeout
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_op_thread_timeout
ceph -s
```

---

### filestore_op_threads

| | |
|---|---|
| 类型 | Int · default `2` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_op_threads](../../../config/global/filestore.md#SP_filestore_op_threads) |

**作用：** Threads used to apply changes to backing file system (deprecated)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global filestore_op_threads 2
ceph config get global filestore_op_threads
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_op_threads
ceph -s
```

---

### filestore_punch_hole

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_punch_hole](../../../config/global/filestore.md#SP_filestore_punch_hole) |

**作用：** Use fallocate(2) FALLOC_FL_PUNCH_HOLE to efficiently zero ranges of objects (deprecated)

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global filestore_punch_hole true
ceph config get global filestore_punch_hole
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_punch_hole
ceph -s
```

---

### filestore_queue_high_delay_multiple

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [filestore.md#SP_filestore_queue_high_delay_multiple](../../../config/global/filestore.md#SP_filestore_queue_high_delay_multiple) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_queue_high_delay_multiple 0
ceph config get global filestore_queue_high_delay_multiple
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_queue_high_delay_multiple_bytes

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [filestore.md#SP_filestore_queue_high_delay_multiple_bytes](../../../config/global/filestore.md#SP_filestore_queue_high_delay_multiple_bytes) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_queue_high_delay_multiple_bytes 0
ceph config get global filestore_queue_high_delay_multiple_bytes
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_queue_high_delay_multiple_ops

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [filestore.md#SP_filestore_queue_high_delay_multiple_ops](../../../config/global/filestore.md#SP_filestore_queue_high_delay_multiple_ops) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_queue_high_delay_multiple_ops 0
ceph config get global filestore_queue_high_delay_multiple_ops
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_queue_high_threshhold

| | |
|---|---|
| 类型 | Float · default `0.9` · **Dev** |
| 表格 | [filestore.md#SP_filestore_queue_high_threshhold](../../../config/global/filestore.md#SP_filestore_queue_high_threshhold) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_queue_high_threshhold 0.9
ceph config get global filestore_queue_high_threshhold
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0.9`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_queue_low_threshhold

| | |
|---|---|
| 类型 | Float · default `0.3` · **Dev** |
| 表格 | [filestore.md#SP_filestore_queue_low_threshhold](../../../config/global/filestore.md#SP_filestore_queue_low_threshhold) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_queue_low_threshhold 0.3
ceph config get global filestore_queue_low_threshhold
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0.3`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_queue_max_bytes

| | |
|---|---|
| 类型 | Size · default `100_M` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_queue_max_bytes](../../../config/global/filestore.md#SP_filestore_queue_max_bytes) |

**作用：** Max (written) bytes in flight (deprecated)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global filestore_queue_max_bytes 100_M
ceph config get global filestore_queue_max_bytes
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `100_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_queue_max_bytes
ceph -s
```

---

### filestore_queue_max_delay_multiple

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [filestore.md#SP_filestore_queue_max_delay_multiple](../../../config/global/filestore.md#SP_filestore_queue_max_delay_multiple) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_queue_max_delay_multiple 0
ceph config get global filestore_queue_max_delay_multiple
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_queue_max_delay_multiple_bytes

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [filestore.md#SP_filestore_queue_max_delay_multiple_bytes](../../../config/global/filestore.md#SP_filestore_queue_max_delay_multiple_bytes) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_queue_max_delay_multiple_bytes 0
ceph config get global filestore_queue_max_delay_multiple_bytes
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_queue_max_delay_multiple_ops

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [filestore.md#SP_filestore_queue_max_delay_multiple_ops](../../../config/global/filestore.md#SP_filestore_queue_max_delay_multiple_ops) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_queue_max_delay_multiple_ops 0
ceph config get global filestore_queue_max_delay_multiple_ops
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_queue_max_ops

| | |
|---|---|
| 类型 | Uint · default `50` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_queue_max_ops](../../../config/global/filestore.md#SP_filestore_queue_max_ops) |

**作用：** Max IO operations in flight (deprecated)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global filestore_queue_max_ops 50
ceph config get global filestore_queue_max_ops
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `50` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_queue_max_ops
ceph -s
```

---

### filestore_rocksdb_options

| | |
|---|---|
| 类型 | Str · default `max_background_jobs=10,compaction_readahead_size=2097152,compression=kNoCompression` · **Dev** |
| 表格 | [filestore.md#SP_filestore_rocksdb_options](../../../config/global/filestore.md#SP_filestore_rocksdb_options) |

**作用：** Options to pass through when RocksDB is used as the KeyValueDB for (deprecated) Filestore.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_rocksdb_options "max_background_jobs=10,compaction_readahead_size=2097152,compression=kNoCompression"
ceph config get global filestore_rocksdb_options
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`max_background_jobs=10,compaction_readahead_size=2097152,compression=kNoCompression`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_seek_data_hole

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_seek_data_hole](../../../config/global/filestore.md#SP_filestore_seek_data_hole) |

**作用：** Use lseek(2) SEEK_HOLE and SEEK_DATA to determine which parts of objects are sparse (deprecated)

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global filestore_seek_data_hole true
ceph config get global filestore_seek_data_hole
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_seek_data_hole
ceph -s
```

---

### filestore_sloppy_crc

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [filestore.md#SP_filestore_sloppy_crc](../../../config/global/filestore.md#SP_filestore_sloppy_crc) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_sloppy_crc true
ceph config get global filestore_sloppy_crc
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_sloppy_crc_block_size

| | |
|---|---|
| 类型 | Size · default `64_K` · **Dev** |
| 表格 | [filestore.md#SP_filestore_sloppy_crc_block_size](../../../config/global/filestore.md#SP_filestore_sloppy_crc_block_size) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_sloppy_crc_block_size 64_K
ceph config get global filestore_sloppy_crc_block_size
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`64_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_splice

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_splice](../../../config/global/filestore.md#SP_filestore_splice) |

**作用：** Use splice(2) to more efficiently copy data between files (deprecated)

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global filestore_splice true
ceph config get global filestore_splice
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_splice
ceph -s
```

---

### filestore_split_multiple

| | |
|---|---|
| 类型 | Int · default `2` · **Dev** |
| 表格 | [filestore.md#SP_filestore_split_multiple](../../../config/global/filestore.md#SP_filestore_split_multiple) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_split_multiple 2
ceph config get global filestore_split_multiple
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`2`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_split_rand_factor

| | |
|---|---|
| 类型 | Uint · default `20` · **Dev** |
| 表格 | [filestore.md#SP_filestore_split_rand_factor](../../../config/global/filestore.md#SP_filestore_split_rand_factor) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_split_rand_factor 20
ceph config get global filestore_split_rand_factor
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`20`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_update_to

| | |
|---|---|
| 类型 | Int · default `1000` · **Dev** |
| 表格 | [filestore.md#SP_filestore_update_to](../../../config/global/filestore.md#SP_filestore_update_to) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_update_to 1000
ceph config get global filestore_update_to
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`1000`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### filestore_wbthrottle_btrfs_bytes_hard_limit

| | |
|---|---|
| 类型 | Size · default `400_M` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_wbthrottle_btrfs_bytes_hard_limit](../../../config/global/filestore.md#SP_filestore_wbthrottle_btrfs_bytes_hard_limit) |

**作用：** Block writes when this many bytes haven't been flushed (fsynced) (btrfs, deprecated)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global filestore_wbthrottle_btrfs_bytes_hard_limit 400_M
ceph config get global filestore_wbthrottle_btrfs_bytes_hard_limit
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `400_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_wbthrottle_btrfs_bytes_hard_limit
ceph -s
```

---

### filestore_wbthrottle_btrfs_bytes_start_flusher

| | |
|---|---|
| 类型 | Size · default `40_M` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_wbthrottle_btrfs_bytes_start_flusher](../../../config/global/filestore.md#SP_filestore_wbthrottle_btrfs_bytes_start_flusher) |

**作用：** Start flushing (fsyncing) when this many bytes are written (btrfs, deprecated)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global filestore_wbthrottle_btrfs_bytes_start_flusher 40_M
ceph config get global filestore_wbthrottle_btrfs_bytes_start_flusher
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `40_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_wbthrottle_btrfs_bytes_start_flusher
ceph -s
```

---

### filestore_wbthrottle_btrfs_inodes_hard_limit

| | |
|---|---|
| 类型 | Uint · default `5000` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_wbthrottle_btrfs_inodes_hard_limit](../../../config/global/filestore.md#SP_filestore_wbthrottle_btrfs_inodes_hard_limit) |

**作用：** Block writing when this many inodes have outstanding writes (btrfs, deprecated)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global filestore_wbthrottle_btrfs_inodes_hard_limit 5000
ceph config get global filestore_wbthrottle_btrfs_inodes_hard_limit
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_wbthrottle_btrfs_inodes_hard_limit
ceph -s
```

---

### filestore_wbthrottle_btrfs_inodes_start_flusher

| | |
|---|---|
| 类型 | Uint · default `500` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_wbthrottle_btrfs_inodes_start_flusher](../../../config/global/filestore.md#SP_filestore_wbthrottle_btrfs_inodes_start_flusher) |

**作用：** Start flushing (fsyncing) when this many distinct inodes have been modified (deprecated) (btrfs)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global filestore_wbthrottle_btrfs_inodes_start_flusher 500
ceph config get global filestore_wbthrottle_btrfs_inodes_start_flusher
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `500` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_wbthrottle_btrfs_inodes_start_flusher
ceph -s
```

---

### filestore_wbthrottle_btrfs_ios_hard_limit

| | |
|---|---|
| 类型 | Uint · default `5000` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_wbthrottle_btrfs_ios_hard_limit](../../../config/global/filestore.md#SP_filestore_wbthrottle_btrfs_ios_hard_limit) |

**作用：** Block writes when this many IOs haven't been flushed (fsynced) (btrfs,deprecated)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global filestore_wbthrottle_btrfs_ios_hard_limit 5000
ceph config get global filestore_wbthrottle_btrfs_ios_hard_limit
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_wbthrottle_btrfs_ios_hard_limit
ceph -s
```

---

### filestore_wbthrottle_btrfs_ios_start_flusher

| | |
|---|---|
| 类型 | Uint · default `500` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_wbthrottle_btrfs_ios_start_flusher](../../../config/global/filestore.md#SP_filestore_wbthrottle_btrfs_ios_start_flusher) |

**作用：** Start flushing (fsyncing) when this many IOs are written (brtrfs, deprecated)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global filestore_wbthrottle_btrfs_ios_start_flusher 500
ceph config get global filestore_wbthrottle_btrfs_ios_start_flusher
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `500` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_wbthrottle_btrfs_ios_start_flusher
ceph -s
```

---

### filestore_wbthrottle_enable

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_wbthrottle_enable](../../../config/global/filestore.md#SP_filestore_wbthrottle_enable) |

**作用：** Enabling throttling of operations to backing file system (deprecated)

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global filestore_wbthrottle_enable false
ceph config get global filestore_wbthrottle_enable
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_wbthrottle_enable
ceph -s
```

---

### filestore_wbthrottle_xfs_bytes_hard_limit

| | |
|---|---|
| 类型 | Size · default `400_M` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_wbthrottle_xfs_bytes_hard_limit](../../../config/global/filestore.md#SP_filestore_wbthrottle_xfs_bytes_hard_limit) |

**作用：** Block writes when this many bytes haven't been flushed (fsynced) (xfs, deprecated)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global filestore_wbthrottle_xfs_bytes_hard_limit 400_M
ceph config get global filestore_wbthrottle_xfs_bytes_hard_limit
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `400_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_wbthrottle_xfs_bytes_hard_limit
ceph -s
```

---

### filestore_wbthrottle_xfs_bytes_start_flusher

| | |
|---|---|
| 类型 | Size · default `40_M` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_wbthrottle_xfs_bytes_start_flusher](../../../config/global/filestore.md#SP_filestore_wbthrottle_xfs_bytes_start_flusher) |

**作用：** Start flushing (fsyncing) when this many bytes are written (xfs, deprecated)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global filestore_wbthrottle_xfs_bytes_start_flusher 40_M
ceph config get global filestore_wbthrottle_xfs_bytes_start_flusher
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `40_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_wbthrottle_xfs_bytes_start_flusher
ceph -s
```

---

### filestore_wbthrottle_xfs_inodes_hard_limit

| | |
|---|---|
| 类型 | Uint · default `5000` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_wbthrottle_xfs_inodes_hard_limit](../../../config/global/filestore.md#SP_filestore_wbthrottle_xfs_inodes_hard_limit) |

**作用：** Block writing when this many inodes have outstanding writes (xfs, deprecated)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global filestore_wbthrottle_xfs_inodes_hard_limit 5000
ceph config get global filestore_wbthrottle_xfs_inodes_hard_limit
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_wbthrottle_xfs_inodes_hard_limit
ceph -s
```

---

### filestore_wbthrottle_xfs_inodes_start_flusher

| | |
|---|---|
| 类型 | Uint · default `500` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_wbthrottle_xfs_inodes_start_flusher](../../../config/global/filestore.md#SP_filestore_wbthrottle_xfs_inodes_start_flusher) |

**作用：** Start flushing (fsyncing) when this many distinct inodes have been modified (xfs, deprecated)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global filestore_wbthrottle_xfs_inodes_start_flusher 500
ceph config get global filestore_wbthrottle_xfs_inodes_start_flusher
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `500` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_wbthrottle_xfs_inodes_start_flusher
ceph -s
```

---

### filestore_wbthrottle_xfs_ios_hard_limit

| | |
|---|---|
| 类型 | Uint · default `5000` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_wbthrottle_xfs_ios_hard_limit](../../../config/global/filestore.md#SP_filestore_wbthrottle_xfs_ios_hard_limit) |

**作用：** Block writes when this many IOs haven't been flushed (fsynced) (xfs, deprecated)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global filestore_wbthrottle_xfs_ios_hard_limit 5000
ceph config get global filestore_wbthrottle_xfs_ios_hard_limit
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_wbthrottle_xfs_ios_hard_limit
ceph -s
```

---

### filestore_wbthrottle_xfs_ios_start_flusher

| | |
|---|---|
| 类型 | Uint · default `500` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_wbthrottle_xfs_ios_start_flusher](../../../config/global/filestore.md#SP_filestore_wbthrottle_xfs_ios_start_flusher) |

**作用：** Start flushing (fsyncing) when this many IOs are written (xfs, deprecated)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global filestore_wbthrottle_xfs_ios_start_flusher 500
ceph config get global filestore_wbthrottle_xfs_ios_start_flusher
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `500` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_wbthrottle_xfs_ios_start_flusher
ceph -s
```

---

### filestore_xfs_extsize

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [filestore.md#SP_filestore_xfs_extsize](../../../config/global/filestore.md#SP_filestore_xfs_extsize) |

**作用：** Use XFS extsize ioctl(2) to hint allocator about expected write sizes (deprecated)

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global filestore_xfs_extsize true
ceph config get global filestore_xfs_extsize
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filestore_xfs_extsize
ceph -s
```

---

### filestore_zfs_snap

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [filestore.md#SP_filestore_zfs_snap](../../../config/global/filestore.md#SP_filestore_zfs_snap) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global filestore_zfs_snap true
ceph config get global filestore_zfs_snap
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
