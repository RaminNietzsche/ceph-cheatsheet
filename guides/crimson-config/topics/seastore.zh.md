# Seastore

Crimson 配置深度指南 — 28 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/crimson/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [seastore_block_create](#seastore_block_create) | `True` | Dev | Dev |
| [seastore_cachepin_2q_in_ratio](#seastore_cachepin_2q_in_ratio) | `0.5` | Advanced | Performance |
| [seastore_cachepin_2q_out_ratio](#seastore_cachepin_2q_out_ratio) | `0.5` | Advanced | Performance |
| [seastore_cachepin_size_pershard](#seastore_cachepin_size_pershard) | `2_G` | Advanced | Performance |
| [seastore_cachepin_type](#seastore_cachepin_type) | `LRU` | Dev | Dev |
| [seastore_cbjournal_size](#seastore_cbjournal_size) | `5_G` | Dev | Dev |
| [seastore_cold_tier_generations](#seastore_cold_tier_generations) | `3` | Advanced | Performance |
| [seastore_data_delta_based_overwrite](#seastore_data_delta_based_overwrite) | `0` | Dev | Dev |
| [seastore_default_max_object_size](#seastore_default_max_object_size) | `16777216` | Dev | Dev |
| [seastore_device_size](#seastore_device_size) | `50_G` | Dev | Dev |
| [seastore_disable_end_to_end_data_protection](#seastore_disable_end_to_end_data_protection) | `True` | Dev | Dev |
| [seastore_full_integrity_check](#seastore_full_integrity_check) | `False` | Dev | Dev |
| [seastore_hot_tier_generations](#seastore_hot_tier_generations) | `5` | Advanced | Performance |
| [seastore_journal_batch_capacity](#seastore_journal_batch_capacity) | `16` | Dev | Dev |
| [seastore_journal_batch_flush_size](#seastore_journal_batch_flush_size) | `16_M` | Dev | Dev |
| [seastore_journal_batch_preferred_fullness](#seastore_journal_batch_preferred_fullness) | `0.95` | Dev | Dev |
| [seastore_journal_iodepth_limit](#seastore_journal_iodepth_limit) | `5` | Dev | Dev |
| [seastore_main_device_type](#seastore_main_device_type) | `SSD` | Dev | Dev |
| [seastore_max_concurrent_transactions](#seastore_max_concurrent_transactions) | `128` | Advanced | Performance |
| [seastore_max_data_allocation_size](#seastore_max_data_allocation_size) | `0` | Advanced | Performance |
| [seastore_multiple_tiers_default_evict_ratio](#seastore_multiple_tiers_default_evict_ratio) | `0.6` | Advanced | Performance |
| [seastore_multiple_tiers_fast_evict_ratio](#seastore_multiple_tiers_fast_evict_ratio) | `0.7` | Advanced | Performance |
| [seastore_multiple_tiers_stop_evict_ratio](#seastore_multiple_tiers_stop_evict_ratio) | `0.5` | Advanced | Performance |
| [seastore_require_partition_count_match_reactor_count](#seastore_require_partition_count_match_reactor_count) | `True` | Advanced | Performance |
| [seastore_segment_cleaner_gc_autotune](#seastore_segment_cleaner_gc_autotune) | `True` | Advanced | Performance |
| [seastore_segment_cleaner_gc_autotune_ratio](#seastore_segment_cleaner_gc_autotune_ratio) | `2.0` | Advanced | Performance |
| [seastore_segment_cleaner_gc_formula](#seastore_segment_cleaner_gc_formula) | `cost_benefit` | Advanced | Performance |
| [seastore_segment_size](#seastore_segment_size) | `64_M` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. crimson
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### seastore_block_create

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [seastore.md#SP_seastore_block_create](../../../config/crimson/seastore.md#SP_seastore_block_create) |

**作用：** Create SegmentManager file if it doesn't exist

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd seastore_block_create false
ceph config get osd seastore_block_create
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### seastore_cachepin_2q_in_ratio

| | |
|---|---|
| 类型 | Float · default `0.5` · **Advanced** |
| 表格 | [seastore.md#SP_seastore_cachepin_2q_in_ratio](../../../config/crimson/seastore.md#SP_seastore_cachepin_2q_in_ratio) |

**作用：** Ratio of A1_in queue size to cache size(seastore_cachepin_size_pershard) in 2Q cache algorithm. Note that the size of Am(primary) queue in 2Q is cache_size * (1 - in_ratio).

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd seastore_cachepin_2q_in_ratio 0.5
ceph config get osd seastore_cachepin_2q_in_ratio
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd seastore_cachepin_2q_in_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_cachepin_2q_out_ratio

| | |
|---|---|
| 类型 | Float · default `0.5` · **Advanced** |
| 表格 | [seastore.md#SP_seastore_cachepin_2q_out_ratio](../../../config/crimson/seastore.md#SP_seastore_cachepin_2q_out_ratio) |

**作用：** Ratio of A1_out queue size to cache size(seastore_cachepin_size_pershard) in 2Q cache algorithm. Note this size ratio does not reflect actual memory usage, as it represents the size of evicted pages from A1_in queue.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd seastore_cachepin_2q_out_ratio 0.5
ceph config get osd seastore_cachepin_2q_out_ratio
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd seastore_cachepin_2q_out_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_cachepin_size_pershard

| | |
|---|---|
| 类型 | Size · default `2_G` · **Advanced** |
| 表格 | [seastore.md#SP_seastore_cachepin_size_pershard](../../../config/crimson/seastore.md#SP_seastore_cachepin_size_pershard) |

**作用：** Size in bytes of extents to keep in cache (per reactor).

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd seastore_cachepin_size_pershard 2_G
ceph config get osd seastore_cachepin_size_pershard
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2_G` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd seastore_cachepin_size_pershard
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_cachepin_type

| | |
|---|---|
| 类型 | Str · enum: ["LRU", "2Q"] · default `LRU` · **Dev** |
| 表格 | [seastore.md#SP_seastore_cachepin_type](../../../config/crimson/seastore.md#SP_seastore_cachepin_type) |

**作用：** The cache replacement algorithm used by extent pinboard in seastore. (LRU/2Q)

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd seastore_cachepin_type LRU
ceph config get osd seastore_cachepin_type
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`LRU`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### seastore_cbjournal_size

| | |
|---|---|
| 类型 | Size · default `5_G` · **Dev** |
| 表格 | [seastore.md#SP_seastore_cbjournal_size](../../../config/crimson/seastore.md#SP_seastore_cbjournal_size) |

**作用：** Total size to use for CircularBoundedJournal if created, it is valid only if seastore_main_device_type is RANDOM_BLOCK

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd seastore_cbjournal_size 5_G
ceph config get osd seastore_cbjournal_size
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`5_G`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### seastore_cold_tier_generations

| | |
|---|---|
| 类型 | Uint · default `3` · **Advanced** |
| 表格 | [seastore.md#SP_seastore_cold_tier_generations](../../../config/crimson/seastore.md#SP_seastore_cold_tier_generations) |

**作用：** The number of generations in the cold tier if it exists.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd seastore_cold_tier_generations 3
ceph config get osd seastore_cold_tier_generations
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd seastore_cold_tier_generations
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_data_delta_based_overwrite

| | |
|---|---|
| 类型 | Size · default `0` · **Dev** |
| 表格 | [seastore.md#SP_seastore_data_delta_based_overwrite](../../../config/crimson/seastore.md#SP_seastore_data_delta_based_overwrite) |

**作用：** overwrite the existing data block based on delta if the overwrite size is equal to or less than the value, otherwise do overwrite based on remapping, set to 0 to enforce the remap-based overwrite.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd seastore_data_delta_based_overwrite 64
ceph config get osd seastore_data_delta_based_overwrite
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### seastore_default_max_object_size

| | |
|---|---|
| 类型 | Uint · default `16777216` · **Dev** |
| 表格 | [seastore.md#SP_seastore_default_max_object_size](../../../config/crimson/seastore.md#SP_seastore_default_max_object_size) |

**作用：** default logical address space reservation for seastore objects' data

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd seastore_default_max_object_size 16777216
ceph config get osd seastore_default_max_object_size
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`16777216`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### seastore_device_size

| | |
|---|---|
| 类型 | Size · default `50_G` · **Dev** |
| 表格 | [seastore.md#SP_seastore_device_size](../../../config/crimson/seastore.md#SP_seastore_device_size) |

**作用：** Total size to use for SegmentManager block file if created

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd seastore_device_size 50_G
ceph config get osd seastore_device_size
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`50_G`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### seastore_disable_end_to_end_data_protection

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [seastore.md#SP_seastore_disable_end_to_end_data_protection](../../../config/crimson/seastore.md#SP_seastore_disable_end_to_end_data_protection) |

**作用：** When false, upon mkfs, try to discover whether the nvme device supports internal checksum feature without using sever CPU then enable if available, set to true to disable unconditionally.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd seastore_disable_end_to_end_data_protection false
ceph config get osd seastore_disable_end_to_end_data_protection
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### seastore_full_integrity_check

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [seastore.md#SP_seastore_full_integrity_check](../../../config/crimson/seastore.md#SP_seastore_full_integrity_check) |

**作用：** Whether seastore need to fully check the integrity of each extent, non-full integrity check means the integrity check might be skipped during extent remapping for better performance, disable with caution

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd seastore_full_integrity_check true
ceph config get osd seastore_full_integrity_check
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### seastore_hot_tier_generations

| | |
|---|---|
| 类型 | Uint · default `5` · **Advanced** |
| 表格 | [seastore.md#SP_seastore_hot_tier_generations](../../../config/crimson/seastore.md#SP_seastore_hot_tier_generations) |

**作用：** The number of generations in the hot tier or the whole SeaStore instance if there's only one tier.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd seastore_hot_tier_generations 5
ceph config get osd seastore_hot_tier_generations
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `5`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd seastore_hot_tier_generations
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_journal_batch_capacity

| | |
|---|---|
| 类型 | Uint · default `16` · **Dev** |
| 表格 | [seastore.md#SP_seastore_journal_batch_capacity](../../../config/crimson/seastore.md#SP_seastore_journal_batch_capacity) |

**作用：** The number limit of records in a journal batch

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd seastore_journal_batch_capacity 16
ceph config get osd seastore_journal_batch_capacity
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`16`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### seastore_journal_batch_flush_size

| | |
|---|---|
| 类型 | Size · default `16_M` · **Dev** |
| 表格 | [seastore.md#SP_seastore_journal_batch_flush_size](../../../config/crimson/seastore.md#SP_seastore_journal_batch_flush_size) |

**作用：** The size threshold to force flush a journal batch

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd seastore_journal_batch_flush_size 16_M
ceph config get osd seastore_journal_batch_flush_size
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`16_M`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### seastore_journal_batch_preferred_fullness

| | |
|---|---|
| 类型 | Float · default `0.95` · **Dev** |
| 表格 | [seastore.md#SP_seastore_journal_batch_preferred_fullness](../../../config/crimson/seastore.md#SP_seastore_journal_batch_preferred_fullness) |

**作用：** The record fullness threshold to flush a journal batch

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd seastore_journal_batch_preferred_fullness 0.95
ceph config get osd seastore_journal_batch_preferred_fullness
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0.95`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### seastore_journal_iodepth_limit

| | |
|---|---|
| 类型 | Uint · default `5` · **Dev** |
| 表格 | [seastore.md#SP_seastore_journal_iodepth_limit](../../../config/crimson/seastore.md#SP_seastore_journal_iodepth_limit) |

**作用：** The io depth limit to submit journal records

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd seastore_journal_iodepth_limit 5
ceph config get osd seastore_journal_iodepth_limit
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`5`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### seastore_main_device_type

| | |
|---|---|
| 类型 | Str · default `SSD` · **Dev** |
| 表格 | [seastore.md#SP_seastore_main_device_type](../../../config/crimson/seastore.md#SP_seastore_main_device_type) |

**作用：** The main device type seastore uses (SSD or RANDOM_BLOCK_SSD)

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd seastore_main_device_type SSD
ceph config get osd seastore_main_device_type
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`SSD`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### seastore_max_concurrent_transactions

| | |
|---|---|
| 类型 | Uint · default `128` · **Advanced** |
| 表格 | [seastore.md#SP_seastore_max_concurrent_transactions](../../../config/crimson/seastore.md#SP_seastore_max_concurrent_transactions) |

**作用：** maximum concurrent transactions that seastore allows (per reactor)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd seastore_max_concurrent_transactions 128
ceph config get osd seastore_max_concurrent_transactions
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `128` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd seastore_max_concurrent_transactions
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_max_data_allocation_size

| | |
|---|---|
| 类型 | Size · default `0` · **Advanced** |
| 表格 | [seastore.md#SP_seastore_max_data_allocation_size](../../../config/crimson/seastore.md#SP_seastore_max_data_allocation_size) |

**作用：** Max size in bytes that an extent can be, 0 to disable

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd seastore_max_data_allocation_size 64
ceph config get osd seastore_max_data_allocation_size
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd seastore_max_data_allocation_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_multiple_tiers_default_evict_ratio

| | |
|---|---|
| 类型 | Float · default `0.6` · **Advanced** |
| 表格 | [seastore.md#SP_seastore_multiple_tiers_default_evict_ratio](../../../config/crimson/seastore.md#SP_seastore_multiple_tiers_default_evict_ratio) |

**作用：** Begin evicting cold data to the cold tier when the used ratio of the main tier reaches this value.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd seastore_multiple_tiers_default_evict_ratio 0.6
ceph config get osd seastore_multiple_tiers_default_evict_ratio
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.6` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd seastore_multiple_tiers_default_evict_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_multiple_tiers_fast_evict_ratio

| | |
|---|---|
| 类型 | Float · default `0.7` · **Advanced** |
| 表格 | [seastore.md#SP_seastore_multiple_tiers_fast_evict_ratio](../../../config/crimson/seastore.md#SP_seastore_multiple_tiers_fast_evict_ratio) |

**作用：** Begin fast eviction when the used ratio of the main tier reaches this value.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd seastore_multiple_tiers_fast_evict_ratio 0.7
ceph config get osd seastore_multiple_tiers_fast_evict_ratio
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.7` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd seastore_multiple_tiers_fast_evict_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_multiple_tiers_stop_evict_ratio

| | |
|---|---|
| 类型 | Float · default `0.5` · **Advanced** |
| 表格 | [seastore.md#SP_seastore_multiple_tiers_stop_evict_ratio](../../../config/crimson/seastore.md#SP_seastore_multiple_tiers_stop_evict_ratio) |

**作用：** When the used ratio of main tier is less than this value, then stop evict cold data to the cold tier.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd seastore_multiple_tiers_stop_evict_ratio 0.5
ceph config get osd seastore_multiple_tiers_stop_evict_ratio
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd seastore_multiple_tiers_stop_evict_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_require_partition_count_match_reactor_count

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [seastore.md#SP_seastore_require_partition_count_match_reactor_count](../../../config/crimson/seastore.md#SP_seastore_require_partition_count_match_reactor_count) |

**作用：** disable osd shards changes upon restart.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd seastore_require_partition_count_match_reactor_count false
ceph config get osd seastore_require_partition_count_match_reactor_count
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd seastore_require_partition_count_match_reactor_count
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_segment_cleaner_gc_autotune

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [seastore.md#SP_seastore_segment_cleaner_gc_autotune](../../../config/crimson/seastore.md#SP_seastore_segment_cleaner_gc_autotune) |

**作用：** When the configured gc formula (cost_benefit or benefit) picks a segment whose free-space fraction (1 - utilization) is at least seastore_segment_cleaner_gc_autotune_ratio times smaller than the lowest-utilization candidate, override the pick with the greedy choice.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd seastore_segment_cleaner_gc_autotune false
ceph config get osd seastore_segment_cleaner_gc_autotune
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd seastore_segment_cleaner_gc_autotune
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_segment_cleaner_gc_autotune_ratio

| | |
|---|---|
| 类型 | Float · default `2.0` · **Advanced** |
| 表格 | [seastore.md#SP_seastore_segment_cleaner_gc_autotune_ratio](../../../config/crimson/seastore.md#SP_seastore_segment_cleaner_gc_autotune_ratio) |

**作用：** Override threshold for the gc auto-tune. The configured formula's pick is overridden with the greedy candidate when greedy's free fraction is at least this ratio times the formula's pick's free fraction.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd seastore_segment_cleaner_gc_autotune_ratio 2.0
ceph config get osd seastore_segment_cleaner_gc_autotune_ratio
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2.0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1.0`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd seastore_segment_cleaner_gc_autotune_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_segment_cleaner_gc_formula

| | |
|---|---|
| 类型 | Str · enum: ["greedy", "cost_benefit", "benefit"] · default `cost_benefit` · **Advanced** |
| 表格 | [seastore.md#SP_seastore_segment_cleaner_gc_formula](../../../config/crimson/seastore.md#SP_seastore_segment_cleaner_gc_formula) |

**作用：** The algorithm that SegmentCleaner will use to select segments to reclaim

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd seastore_segment_cleaner_gc_formula cost_benefit
ceph config get osd seastore_segment_cleaner_gc_formula
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `cost_benefit` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd seastore_segment_cleaner_gc_formula
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_segment_size

| | |
|---|---|
| 类型 | Size · default `64_M` · **Advanced** |
| 表格 | [seastore.md#SP_seastore_segment_size](../../../config/crimson/seastore.md#SP_seastore_segment_size) |

**作用：** Segment size to use for SegmentManager

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd seastore_segment_size 64_M
ceph config get osd seastore_segment_size
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `64_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd seastore_segment_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← 概览](../OVERVIEW.md)
