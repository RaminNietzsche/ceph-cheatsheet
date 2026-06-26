# Bluefs

Global 配置深度指南 — 24 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [bluefs_alloc_size](#bluefs_alloc_size) | `1_M` | Advanced | 性能 |
| [bluefs_allocator](#bluefs_allocator) | `hybrid` | Dev | 开发 |
| [bluefs_buffered_io](#bluefs_buffered_io) | `True` | Advanced | 性能 |
| [bluefs_check_for_zeros](#bluefs_check_for_zeros) | `False` | Dev | 开发 |
| [bluefs_check_volume_selector_often](#bluefs_check_volume_selector_often) | `False` | Dev | 开发 |
| [bluefs_check_volume_selector_on_mount](#bluefs_check_volume_selector_on_mount) | `False` | Dev | 开发 |
| [bluefs_compact_log_sync](#bluefs_compact_log_sync) | `False` | Advanced | 性能 |
| [bluefs_debug_force_slow](#bluefs_debug_force_slow) | `False` | Dev | 开发 |
| [bluefs_failed_shared_alloc_cooldown](#bluefs_failed_shared_alloc_cooldown) | `600` | Advanced | 性能 |
| [bluefs_log_compact_min_ratio](#bluefs_log_compact_min_ratio) | `5` | Advanced | 性能 |
| [bluefs_log_compact_min_size](#bluefs_log_compact_min_size) | `16_M` | Advanced | 性能 |
| [bluefs_log_replay_check_allocations](#bluefs_log_replay_check_allocations) | `True` | Advanced | 性能 |
| [bluefs_max_log_runway](#bluefs_max_log_runway) | `4_M` | Advanced | 性能 |
| [bluefs_max_prefetch](#bluefs_max_prefetch) | `1_M` | Advanced | 性能 |
| [bluefs_min_flush_size](#bluefs_min_flush_size) | `512_K` | Advanced | 性能 |
| [bluefs_min_log_runway](#bluefs_min_log_runway) | `1_M` | Advanced | 性能 |
| [bluefs_replay_recovery](#bluefs_replay_recovery) | `False` | Dev | 开发 |
| [bluefs_replay_recovery_disable_compact](#bluefs_replay_recovery_disable_compact) | `False` | Advanced | 策略 |
| [bluefs_shared_alloc_size](#bluefs_shared_alloc_size) | `64_K` | Advanced | 性能 |
| [bluefs_spillover_cleaner](#bluefs_spillover_cleaner) | `False` | Advanced | 性能 |
| [bluefs_spillover_cleaner_work_ratio](#bluefs_spillover_cleaner_work_ratio) | `0.1` | Advanced | 性能 |
| [bluefs_spillover_idle_time](#bluefs_spillover_idle_time) | `1200` | Advanced | 性能 |
| [bluefs_sync_write](#bluefs_sync_write) | `False` | Advanced | 性能 |
| [bluefs_wal_envelope_mode](#bluefs_wal_envelope_mode) | `True` | Advanced | 性能 |

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

### bluefs_alloc_size

| | |
|---|---|
| 类型 | Size · default `1_M` · **Advanced** |
| 表格 | [bluefs.md#SP_bluefs_alloc_size](../../../config/global/bluefs.md#SP_bluefs_alloc_size) |

**作用：** Allocation unit size for DB and WAL devices

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluefs_alloc_size 1_M
ceph config get global bluefs_alloc_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluefs_alloc_size
ceph -s
```

---

### bluefs_allocator

| | |
|---|---|
| 类型 | Str · enum: ["bitmap", "stupid", "avl", "btree", "hybrid", "hybrid_btree2"] · default `hybrid` · **Dev** |
| 表格 | [bluefs.md#SP_bluefs_allocator](../../../config/global/bluefs.md#SP_bluefs_allocator) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluefs_allocator hybrid
ceph config get global bluefs_allocator
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`hybrid`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluefs_buffered_io

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [bluefs.md#SP_bluefs_buffered_io](../../../config/global/bluefs.md#SP_bluefs_buffered_io) |

**作用：** Enabled buffered IO for BlueFS reads. When this option is enabled, BlueFS will in some cases perform buffered reads. This allows the kernel page cache to act as a secondary cache for things like RocksDB block reads. For example, if the RocksDB block cache isn't large enough to hold all blocks during omap iteration, it may be possible to read them from page cache instead of from the device. This can dramatically improve performance when the osd_memory_target is too small to hold all entries in block cache but it does come with downsides. It has been reported to occasionally cause excessive kernel swapping (and associated stalls) under certain workloads. Currently the best and most consistent performing combination appears to be enabling bluefs_buffered_io and disabling system level swap. It is possible that this recommendation may change in the future however.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global bluefs_buffered_io false
ceph config get global bluefs_buffered_io
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluefs_buffered_io
ceph -s
```

---

### bluefs_check_for_zeros

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluefs.md#SP_bluefs_check_for_zeros](../../../config/global/bluefs.md#SP_bluefs_check_for_zeros) |

**作用：** Check data read for suspicious pages Looks into data read to check if there is a 4K block entirely filled with zeros. If this happens, we re-read data. If there is difference, we print error to log.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluefs_check_for_zeros true
ceph config get global bluefs_check_for_zeros
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluefs_check_volume_selector_often

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** · **STARTUP**（需重启） |
| 表格 | [bluefs.md#SP_bluefs_check_volume_selector_often](../../../config/global/bluefs.md#SP_bluefs_check_volume_selector_often) |

**作用：** Periodically check validity of volume selector Periodically checks if current volume selector does not diverge from the valid state. Reference is constructed from bluefs inode table. Asserts on inconsistency. This is debug feature.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**相关选项：**

- [`bluefs_check_volume_selector_on_mount`](../../../config/global/bluefs.md#SP_bluefs_check_volume_selector_on_mount)

**示例：**

```bash
ceph config set global bluefs_check_volume_selector_often true
ceph config get global bluefs_check_volume_selector_often
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluefs_check_volume_selector_on_mount

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluefs.md#SP_bluefs_check_volume_selector_on_mount](../../../config/global/bluefs.md#SP_bluefs_check_volume_selector_on_mount) |

**作用：** Check validity of volume selector on mount/umount Checks if volume selector did not diverge from the state it should be in. Reference is constructed from bluefs inode table. Asserts on inconsistency.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluefs_check_volume_selector_on_mount true
ceph config get global bluefs_check_volume_selector_on_mount
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluefs_compact_log_sync

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bluefs.md#SP_bluefs_compact_log_sync](../../../config/global/bluefs.md#SP_bluefs_compact_log_sync) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bluefs_compact_log_sync true
ceph config get global bluefs_compact_log_sync
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluefs_compact_log_sync
ceph -s
```

---

### bluefs_debug_force_slow

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluefs.md#SP_bluefs_debug_force_slow](../../../config/global/bluefs.md#SP_bluefs_debug_force_slow) |

**作用：** For testing. Force BlueFS to allocate files on slow device. When enabled, the RocksDBBlueFSVolumeSelector will ignore normal placement policy and redirect allocations to slow device.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluefs_debug_force_slow true
ceph config get global bluefs_debug_force_slow
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluefs_failed_shared_alloc_cooldown

| | |
|---|---|
| 类型 | Float · default `600` · **Advanced** |
| 表格 | [bluefs.md#SP_bluefs_failed_shared_alloc_cooldown](../../../config/global/bluefs.md#SP_bluefs_failed_shared_alloc_cooldown) |

**作用：** duration(in seconds) untill the next attempt to use 'bluefs_shared_alloc_size' after facing ENOSPC failure. Cooldown period(in seconds) when BlueFS uses shared/slow device allocation size instead of "bluefs_shared_alloc_size' one after facing recoverable (via fallback to smaller chunk size) ENOSPC failure. Intended primarily to avoid repetitive unsuccessful allocations which might be expensive.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluefs_failed_shared_alloc_cooldown 600
ceph config get global bluefs_failed_shared_alloc_cooldown
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `600` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluefs_failed_shared_alloc_cooldown
ceph -s
```

---

### bluefs_log_compact_min_ratio

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [bluefs.md#SP_bluefs_log_compact_min_ratio](../../../config/global/bluefs.md#SP_bluefs_log_compact_min_ratio) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluefs_log_compact_min_ratio 5
ceph config get global bluefs_log_compact_min_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluefs_log_compact_min_ratio
ceph -s
```

---

### bluefs_log_compact_min_size

| | |
|---|---|
| 类型 | Size · default `16_M` · **Advanced** |
| 表格 | [bluefs.md#SP_bluefs_log_compact_min_size](../../../config/global/bluefs.md#SP_bluefs_log_compact_min_size) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluefs_log_compact_min_size 16_M
ceph config get global bluefs_log_compact_min_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `16_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluefs_log_compact_min_size
ceph -s
```

---

### bluefs_log_replay_check_allocations

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [bluefs.md#SP_bluefs_log_replay_check_allocations](../../../config/global/bluefs.md#SP_bluefs_log_replay_check_allocations) |

**作用：** Enables checks for allocations consistency during log replay

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global bluefs_log_replay_check_allocations false
ceph config get global bluefs_log_replay_check_allocations
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluefs_log_replay_check_allocations
ceph -s
```

---

### bluefs_max_log_runway

| | |
|---|---|
| 类型 | Size · default `4_M` · **Advanced** |
| 表格 | [bluefs.md#SP_bluefs_max_log_runway](../../../config/global/bluefs.md#SP_bluefs_max_log_runway) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluefs_max_log_runway 4_M
ceph config get global bluefs_max_log_runway
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `4_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluefs_max_log_runway
ceph -s
```

---

### bluefs_max_prefetch

| | |
|---|---|
| 类型 | Size · default `1_M` · **Advanced** |
| 表格 | [bluefs.md#SP_bluefs_max_prefetch](../../../config/global/bluefs.md#SP_bluefs_max_prefetch) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluefs_max_prefetch 1_M
ceph config get global bluefs_max_prefetch
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluefs_max_prefetch
ceph -s
```

---

### bluefs_min_flush_size

| | |
|---|---|
| 类型 | Size · default `512_K` · **Advanced** |
| 表格 | [bluefs.md#SP_bluefs_min_flush_size](../../../config/global/bluefs.md#SP_bluefs_min_flush_size) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluefs_min_flush_size 512_K
ceph config get global bluefs_min_flush_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `512_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluefs_min_flush_size
ceph -s
```

---

### bluefs_min_log_runway

| | |
|---|---|
| 类型 | Size · default `1_M` · **Advanced** |
| 表格 | [bluefs.md#SP_bluefs_min_log_runway](../../../config/global/bluefs.md#SP_bluefs_min_log_runway) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bluefs_min_log_runway 1_M
ceph config get global bluefs_min_log_runway
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluefs_min_log_runway
ceph -s
```

---

### bluefs_replay_recovery

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bluefs.md#SP_bluefs_replay_recovery](../../../config/global/bluefs.md#SP_bluefs_replay_recovery) |

**作用：** Attempt to read bluefs log so large that it became unreadable. If BlueFS log grows to extreme sizes (200GB+) it is likely that it becames unreadable. This options enables heuristics that scans devices for missing data. DO NOT ENABLE BY DEFAULT

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bluefs_replay_recovery true
ceph config get global bluefs_replay_recovery
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bluefs_replay_recovery_disable_compact

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bluefs.md#SP_bluefs_replay_recovery_disable_compact](../../../config/global/bluefs.md#SP_bluefs_replay_recovery_disable_compact) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bluefs_replay_recovery_disable_compact true
ceph config get global bluefs_replay_recovery_disable_compact
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluefs_replay_recovery_disable_compact
ceph -s
```

---

### bluefs_shared_alloc_size

| | |
|---|---|
| 类型 | Size · default `64_K` · **Advanced** |
| 表格 | [bluefs.md#SP_bluefs_shared_alloc_size](../../../config/global/bluefs.md#SP_bluefs_shared_alloc_size) |

**作用：** Allocation unit size for primary/shared device

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluefs_shared_alloc_size 64_K
ceph config get global bluefs_shared_alloc_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluefs_shared_alloc_size
ceph -s
```

---

### bluefs_spillover_cleaner

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bluefs.md#SP_bluefs_spillover_cleaner](../../../config/global/bluefs.md#SP_bluefs_spillover_cleaner) |

**作用：** Enable Background BlueFS Spillover cleaner thread Enables a background cleaner thread in BlueFS that periodically scans files that spilled over to the slow device and attempts to migrate them back to the BlueFS DB device

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bluefs_spillover_cleaner true
ceph config get global bluefs_spillover_cleaner
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluefs_spillover_cleaner
ceph -s
```

---

### bluefs_spillover_cleaner_work_ratio

| | |
|---|---|
| 类型 | Float · default `0.1` · **Advanced** |
| 表格 | [bluefs.md#SP_bluefs_spillover_cleaner_work_ratio](../../../config/global/bluefs.md#SP_bluefs_spillover_cleaner_work_ratio) |

**作用：** Fraction of time the BlueFS spillover cleaner spends performing work. Controls the rate of spillover migration work. After each migration step, the cleaner targets to sleep proportionally to the time spent doing work This reduces interference with foreground IO. For example, if a migration step took 10 ms and the ratio is 0.1, the cleaner sleeps for ~90 ms before the next step. This results in approximately 10% work time and 90% sleep time.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bluefs_spillover_cleaner_work_ratio 0.1
ceph config get global bluefs_spillover_cleaner_work_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluefs_spillover_cleaner_work_ratio
ceph -s
```

---

### bluefs_spillover_idle_time

| | |
|---|---|
| 类型 | Uint · default `1200` · **Advanced** |
| 表格 | [bluefs.md#SP_bluefs_spillover_idle_time](../../../config/global/bluefs.md#SP_bluefs_spillover_idle_time) |

**作用：** Idle time in seconds before the BlueFS spillover cleaner wakes up for the next scan cycle. When no spillover files remain to migrate, the cleaner enters an idle sleep state for this duration. Once the idle period expires, it wakes up, scans for spillover files, and resumes migration if needed.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**相关选项：**

- [`bluefs_spillover_cleaner`](../../../config/global/bluefs.md#SP_bluefs_spillover_cleaner)

**示例：**

```bash
ceph config set global bluefs_spillover_idle_time 1200
ceph config get global bluefs_spillover_idle_time
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1200` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluefs_spillover_idle_time
ceph -s
```

---

### bluefs_sync_write

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bluefs.md#SP_bluefs_sync_write](../../../config/global/bluefs.md#SP_bluefs_sync_write) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bluefs_sync_write true
ceph config get global bluefs_sync_write
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluefs_sync_write
ceph -s
```

---

### bluefs_wal_envelope_mode

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [bluefs.md#SP_bluefs_wal_envelope_mode](../../../config/global/bluefs.md#SP_bluefs_wal_envelope_mode) |

**作用：** Enables a faster backend in BlueFS for WAL writes. In envelope mode BlueFS files do not need to update metadata. When applied to RocksDB WAL files, it reduces by ~50% the amount of fdatasync syscalls. Downgrading from an envelope mode to legacy mode requires `ceph-bluestore-tool --command downgrade-wal-to-v1`.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global bluefs_wal_envelope_mode false
ceph config get global bluefs_wal_envelope_mode
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bluefs_wal_envelope_mode
ceph -s
```

---


[← 概览](../OVERVIEW.md)
