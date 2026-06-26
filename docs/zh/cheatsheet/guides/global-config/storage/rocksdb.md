# Rocksdb

Global 配置深度指南 — 21 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rocksdb_block_size](#rocksdb_block_size) | `4_K` | Advanced | 性能 |
| [rocksdb_bloom_bits_per_key](#rocksdb_bloom_bits_per_key) | `20` | Advanced | 性能 |
| [rocksdb_cache_index_and_filter_blocks](#rocksdb_cache_index_and_filter_blocks) | `True` | Dev | 开发 |
| [rocksdb_cache_index_and_filter_blocks_with_high_priority](#rocksdb_cache_index_and_filter_blocks_with_high_priority) | `False` | Dev | 开发 |
| [rocksdb_cache_row_ratio](#rocksdb_cache_row_ratio) | `0` | Advanced | 性能 |
| [rocksdb_cache_shard_bits](#rocksdb_cache_shard_bits) | `4` | Advanced | 性能 |
| [rocksdb_cache_size](#rocksdb_cache_size) | `512_M` | Advanced | 性能 |
| [rocksdb_cache_type](#rocksdb_cache_type) | `binned_lru` | Advanced | 性能 |
| [rocksdb_cf_compact_on_deletion](#rocksdb_cf_compact_on_deletion) | `True` | Dev | 开发 |
| [rocksdb_cf_compact_on_deletion_sliding_window](#rocksdb_cf_compact_on_deletion_sliding_window) | `32768` | Dev | 开发 |
| [rocksdb_cf_compact_on_deletion_trigger](#rocksdb_cf_compact_on_deletion_trigger) | `16384` | Dev | 开发 |
| [rocksdb_collect_compaction_stats](#rocksdb_collect_compaction_stats) | `False` | Advanced | 性能 |
| [rocksdb_collect_extended_stats](#rocksdb_collect_extended_stats) | `False` | Advanced | 性能 |
| [rocksdb_collect_memory_stats](#rocksdb_collect_memory_stats) | `False` | Advanced | 性能 |
| [rocksdb_delete_range_threshold](#rocksdb_delete_range_threshold) | `1_M` | Advanced | 性能 |
| [rocksdb_index_type](#rocksdb_index_type) | `binary_search` | Dev | 开发 |
| [rocksdb_log_to_ceph_log](#rocksdb_log_to_ceph_log) | `True` | Advanced | 性能 |
| [rocksdb_metadata_block_size](#rocksdb_metadata_block_size) | `4_K` | Dev | 开发 |
| [rocksdb_partition_filters](#rocksdb_partition_filters) | `False` | Dev | 开发 |
| [rocksdb_perf](#rocksdb_perf) | `False` | Advanced | 性能 |
| [rocksdb_pin_l0_filter_and_index_blocks_in_cache](#rocksdb_pin_l0_filter_and_index_blocks_in_cache) | `False` | Dev | 开发 |

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

### rocksdb_block_size

| | |
|---|---|
| 类型 | Size · default `4_K` · **Advanced** |
| 表格 | [rocksdb.md#SP_rocksdb_block_size](../../../config/global/rocksdb.md#SP_rocksdb_block_size) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global rocksdb_block_size 4_K
ceph config get global rocksdb_block_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `4_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global rocksdb_block_size
ceph -s
```

---

### rocksdb_bloom_bits_per_key

| | |
|---|---|
| 类型 | Uint · default `20` · **Advanced** |
| 表格 | [rocksdb.md#SP_rocksdb_bloom_bits_per_key](../../../config/global/rocksdb.md#SP_rocksdb_bloom_bits_per_key) |

**作用：** Number of bits per key to use for RocksDB's bloom filters. RocksDB bloom filters can be used to quickly answer the question of whether or not a key may exist or definitely does not exist in a given RocksDB SST file without having to read all keys into memory. Using a higher bit value decreases the likelihood of false positives at the expense of additional disk space and memory consumption when the filter is loaded into RAM. The current default value of 20 was found to provide significant performance gains when getattr calls are made (such as during new object creation in BlueStore) without significant memory overhead or cache pollution when combined with rocksdb partitioned index filters. See: https://github.com/facebook/rocksdb/wiki/Partitioned-Index-Filters for more information.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global rocksdb_bloom_bits_per_key 20
ceph config get global rocksdb_bloom_bits_per_key
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `20` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global rocksdb_bloom_bits_per_key
ceph -s
```

---

### rocksdb_cache_index_and_filter_blocks

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [rocksdb.md#SP_rocksdb_cache_index_and_filter_blocks](../../../config/global/rocksdb.md#SP_rocksdb_cache_index_and_filter_blocks) |

**作用：** Whether to cache indices and filters in block cache By default RocksDB will load an SST file's index and bloom filters into memory when it is opened and remove them from memory when an SST file is closed. Thus, memory consumption by indices and bloom filters is directly tied to the number of concurrent SST files allowed to be kept open. This option instead stores cached indicies and filters in the block cache where they directly compete with other cached data. By default we set this option to true to better account for and bound rocksdb memory usage and keep filters in memory even when an SST file is closed.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global rocksdb_cache_index_and_filter_blocks false
ceph config get global rocksdb_cache_index_and_filter_blocks
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### rocksdb_cache_index_and_filter_blocks_with_high_priority

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [rocksdb.md#SP_rocksdb_cache_index_and_filter_blocks_with_high_priority](../../../config/global/rocksdb.md#SP_rocksdb_cache_index_and_filter_blocks_with_high_priority) |

**作用：** Whether to cache indices and filters in the block cache with high priority A downside of setting rocksdb_cache_index_and_filter_blocks to true is that regular data can push indices and filters out of memory. Setting this option to true means they are cached with higher priority than other data and should typically stay in the block cache.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global rocksdb_cache_index_and_filter_blocks_with_high_priority true
ceph config get global rocksdb_cache_index_and_filter_blocks_with_high_priority
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### rocksdb_cache_row_ratio

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [rocksdb.md#SP_rocksdb_cache_row_ratio](../../../config/global/rocksdb.md#SP_rocksdb_cache_row_ratio) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global rocksdb_cache_row_ratio 0
ceph config get global rocksdb_cache_row_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global rocksdb_cache_row_ratio
ceph -s
```

---

### rocksdb_cache_shard_bits

| | |
|---|---|
| 类型 | Int · default `4` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [rocksdb.md#SP_rocksdb_cache_shard_bits](../../../config/global/rocksdb.md#SP_rocksdb_cache_shard_bits) |

**作用：** Specifies the number of shards by designating the number of significant bits in hash keys. 4 bits -> 16 shards.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global rocksdb_cache_shard_bits 4
ceph config get global rocksdb_cache_shard_bits
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `4` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global rocksdb_cache_shard_bits
ceph -s
```

---

### rocksdb_cache_size

| | |
|---|---|
| 类型 | Size · default `512_M` · **Advanced** |
| 表格 | [rocksdb.md#SP_rocksdb_cache_size](../../../config/global/rocksdb.md#SP_rocksdb_cache_size) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global rocksdb_cache_size 512_M
ceph config get global rocksdb_cache_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `512_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global rocksdb_cache_size
ceph -s
```

---

### rocksdb_cache_type

| | |
|---|---|
| 类型 | Str · default `binned_lru` · **Advanced** |
| 表格 | [rocksdb.md#SP_rocksdb_cache_type](../../../config/global/rocksdb.md#SP_rocksdb_cache_type) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global rocksdb_cache_type binned_lru
ceph config get global rocksdb_cache_type
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `binned_lru` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global rocksdb_cache_type
ceph -s
```

---

### rocksdb_cf_compact_on_deletion

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [rocksdb.md#SP_rocksdb_cf_compact_on_deletion](../../../config/global/rocksdb.md#SP_rocksdb_cf_compact_on_deletion) |

**作用：** Compact the column family when a certain number of tombstones are observed within a given window. This setting instructs RocksDB to compact a column family when a certain number of tombstones are observed during iteration within a certain sliding window. For instance if rocksdb_cf_compact_on_deletion_sliding_window is 8192 and rocksdb_cf_compact_on_deletion_trigger is 4096, then once 4096 tombstones are observed after iteration over 8192 entries, the column family will be compacted.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global rocksdb_cf_compact_on_deletion false
ceph config get global rocksdb_cf_compact_on_deletion
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### rocksdb_cf_compact_on_deletion_sliding_window

| | |
|---|---|
| 类型 | Int · default `32768` · **Dev** |
| 表格 | [rocksdb.md#SP_rocksdb_cf_compact_on_deletion_sliding_window](../../../config/global/rocksdb.md#SP_rocksdb_cf_compact_on_deletion_sliding_window) |

**作用：** The sliding window to use when rocksdb_cf_compact_on_deletion is enabled.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**相关选项：**

- [`rocksdb_cf_compact_on_deletion`](../../../config/global/rocksdb.md#SP_rocksdb_cf_compact_on_deletion)

**示例：**

```bash
ceph config set global rocksdb_cf_compact_on_deletion_sliding_window 32768
ceph config get global rocksdb_cf_compact_on_deletion_sliding_window
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`32768`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### rocksdb_cf_compact_on_deletion_trigger

| | |
|---|---|
| 类型 | Int · default `16384` · **Dev** |
| 表格 | [rocksdb.md#SP_rocksdb_cf_compact_on_deletion_trigger](../../../config/global/rocksdb.md#SP_rocksdb_cf_compact_on_deletion_trigger) |

**作用：** The trigger to use when rocksdb_cf_compact_on_deletion is enabled.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**相关选项：**

- [`rocksdb_cf_compact_on_deletion`](../../../config/global/rocksdb.md#SP_rocksdb_cf_compact_on_deletion)

**示例：**

```bash
ceph config set global rocksdb_cf_compact_on_deletion_trigger 16384
ceph config get global rocksdb_cf_compact_on_deletion_trigger
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`16384`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### rocksdb_collect_compaction_stats

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rocksdb.md#SP_rocksdb_collect_compaction_stats](../../../config/global/rocksdb.md#SP_rocksdb_collect_compaction_stats) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global rocksdb_collect_compaction_stats true
ceph config get global rocksdb_collect_compaction_stats
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global rocksdb_collect_compaction_stats
ceph -s
```

---

### rocksdb_collect_extended_stats

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rocksdb.md#SP_rocksdb_collect_extended_stats](../../../config/global/rocksdb.md#SP_rocksdb_collect_extended_stats) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global rocksdb_collect_extended_stats true
ceph config get global rocksdb_collect_extended_stats
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global rocksdb_collect_extended_stats
ceph -s
```

---

### rocksdb_collect_memory_stats

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rocksdb.md#SP_rocksdb_collect_memory_stats](../../../config/global/rocksdb.md#SP_rocksdb_collect_memory_stats) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global rocksdb_collect_memory_stats true
ceph config get global rocksdb_collect_memory_stats
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global rocksdb_collect_memory_stats
ceph -s
```

---

### rocksdb_delete_range_threshold

| | |
|---|---|
| 类型 | Uint · default `1_M` · **Advanced** |
| 表格 | [rocksdb.md#SP_rocksdb_delete_range_threshold](../../../config/global/rocksdb.md#SP_rocksdb_delete_range_threshold) |

**作用：** The number of keys required to invoke DeleteRange when deleting muliple keys.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global rocksdb_delete_range_threshold 1_M
ceph config get global rocksdb_delete_range_threshold
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global rocksdb_delete_range_threshold
ceph -s
```

---

### rocksdb_index_type

| | |
|---|---|
| 类型 | Str · default `binary_search` · **Dev** |
| 表格 | [rocksdb.md#SP_rocksdb_index_type](../../../config/global/rocksdb.md#SP_rocksdb_index_type) |

**作用：** Type of index for SST files: binary_search, hash_search, two_level This option controls the table index type. binary_search is a space efficient index block that is optimized for block-search-based index. hash_search may improve prefix lookup performance at the expense of higher disk and memory usage and potentially slower compactions. two_level is an experimental index type that uses two binary search indexes and works in conjunction with partition filters. See: http://rocksdb.org/blog/2017/05/12/partitioned-index-filter.html

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global rocksdb_index_type binary_search
ceph config get global rocksdb_index_type
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`binary_search`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### rocksdb_log_to_ceph_log

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rocksdb.md#SP_rocksdb_log_to_ceph_log](../../../config/global/rocksdb.md#SP_rocksdb_log_to_ceph_log) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global rocksdb_log_to_ceph_log false
ceph config get global rocksdb_log_to_ceph_log
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global rocksdb_log_to_ceph_log
ceph -s
```

---

### rocksdb_metadata_block_size

| | |
|---|---|
| 类型 | Size · default `4_K` · **Dev** |
| 表格 | [rocksdb.md#SP_rocksdb_metadata_block_size](../../../config/global/rocksdb.md#SP_rocksdb_metadata_block_size) |

**作用：** The block size for index partitions. (0 = rocksdb default)

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global rocksdb_metadata_block_size 4_K
ceph config get global rocksdb_metadata_block_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`4_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### rocksdb_partition_filters

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [rocksdb.md#SP_rocksdb_partition_filters](../../../config/global/rocksdb.md#SP_rocksdb_partition_filters) |

**作用：** (Experimental) partition SST index/filters into smaller blocks This is an experimental option for RocksDB that works in conjunction with two_level indices to avoid having to keep the entire filter/index in cache when cache_index_and_filter_blocks is true. The idea is to keep a much smaller top-level index in heap/cache and then opportunistically cache the lower level indices. See: https://github.com/facebook/rocksdb/wiki/Partitioned-Index-Filters

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global rocksdb_partition_filters true
ceph config get global rocksdb_partition_filters
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### rocksdb_perf

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rocksdb.md#SP_rocksdb_perf](../../../config/global/rocksdb.md#SP_rocksdb_perf) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global rocksdb_perf true
ceph config get global rocksdb_perf
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global rocksdb_perf
ceph -s
```

---

### rocksdb_pin_l0_filter_and_index_blocks_in_cache

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [rocksdb.md#SP_rocksdb_pin_l0_filter_and_index_blocks_in_cache](../../../config/global/rocksdb.md#SP_rocksdb_pin_l0_filter_and_index_blocks_in_cache) |

**作用：** Whether to pin Level 0 indices and bloom filters in the block cache A downside of setting rocksdb_cache_index_and_filter_blocks to true is that regular data can push indices and filters out of memory. Setting this option to true means that level 0 SST files will always have their indices and filters pinned in the block cache.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global rocksdb_pin_l0_filter_and_index_blocks_in_cache true
ceph config get global rocksdb_pin_l0_filter_and_index_blocks_in_cache
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
