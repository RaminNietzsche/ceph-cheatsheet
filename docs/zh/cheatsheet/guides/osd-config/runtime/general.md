# General runtime

OSD 配置深度指南 — 26 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [osd_aggregated_slow_ops_logging](#osd_aggregated_slow_ops_logging) | `True` | Advanced | 性能 |
| [osd_compact_on_start](#osd_compact_on_start) | `False` | Advanced | 性能 |
| [osd_ec_partial_reads](#osd_ec_partial_reads) | `True` | Advanced | 性能 |
| [osd_extblkdev_plugins](#osd_extblkdev_plugins) | `vdo fcm` | Advanced | 性能 |
| [osd_find_best_info_ignore_history_les](#osd_find_best_info_ignore_history_les) | `False` | Dev | 开发 |
| [osd_journal](#osd_journal) | `/var/lib/ceph/osd/$cluster-$id/journal` | Advanced | 性能 |
| [osd_journal_flush_on_shutdown](#osd_journal_flush_on_shutdown) | `True` | Advanced | 性能 |
| [osd_journal_size](#osd_journal_size) | `5_K` | Advanced | 性能 |
| [osd_map_cache_size](#osd_map_cache_size) | `50` | Advanced | 性能 |
| [osd_num_cache_shards](#osd_num_cache_shards) | `32` | Advanced | 性能 |
| [osd_numa_auto_affinity](#osd_numa_auto_affinity) | `True` | Advanced | 性能 |
| [osd_numa_node](#osd_numa_node) | `-1` | Advanced | 性能 |
| [osd_numa_prefer_iface](#osd_numa_prefer_iface) | `True` | Advanced | 性能 |
| [osd_op_num_shards](#osd_op_num_shards) | `0` | Advanced | 性能 |
| [osd_op_num_shards_hdd](#osd_op_num_shards_hdd) | `1` | Advanced | 性能 |
| [osd_op_num_shards_ssd](#osd_op_num_shards_ssd) | `8` | Advanced | 性能 |
| [osd_op_num_threads_per_shard](#osd_op_num_threads_per_shard) | `0` | Advanced | 性能 |
| [osd_op_num_threads_per_shard_hdd](#osd_op_num_threads_per_shard_hdd) | `5` | Advanced | 性能 |
| [osd_op_num_threads_per_shard_ssd](#osd_op_num_threads_per_shard_ssd) | `2` | Advanced | 性能 |
| [osd_op_queue](#osd_op_queue) | `mclock_scheduler` | Advanced | 性能 |
| [osd_op_queue_cut_off](#osd_op_queue_cut_off) | `high` | Advanced | 性能 |
| [osd_os_flags](#osd_os_flags) | `0` | Dev | 开发 |
| [osd_push_per_object_cost](#osd_push_per_object_cost) | `1000` | Advanced | 性能 |
| [osd_read_ec_check_for_errors](#osd_read_ec_check_for_errors) | `False` | Advanced | 性能 |
| [osd_rocksdb_iterator_bounds_enabled](#osd_rocksdb_iterator_bounds_enabled) | `True` | Dev | 开发 |
| [osd_uuid](#osd_uuid) | `(empty)` | Advanced | 性能 |

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
ceph config get <daemon> <option>  # e.g. osd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_aggregated_slow_ops_logging

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_aggregated_slow_ops_logging](../../../config/osd/osd.md#SP_osd_aggregated_slow_ops_logging) |

**作用：** Allow OSD daemon to send an aggregated slow ops to the cluster log

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_aggregated_slow_ops_logging false
ceph config get osd osd_aggregated_slow_ops_logging
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_aggregated_slow_ops_logging
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_compact_on_start

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_compact_on_start](../../../config/osd/osd.md#SP_osd_compact_on_start) |

**作用：** compact OSD's object store's OMAP on start

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_compact_on_start true
ceph config get osd osd_compact_on_start
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_compact_on_start
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_ec_partial_reads

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_ec_partial_reads](../../../config/osd/osd.md#SP_osd_ec_partial_reads) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_ec_partial_reads false
ceph config get osd osd_ec_partial_reads
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_ec_partial_reads
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_extblkdev_plugins

| | |
|---|---|
| 类型 | Str · default `vdo fcm` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [osd.md#SP_osd_extblkdev_plugins](../../../config/osd/osd.md#SP_osd_extblkdev_plugins) |

**作用：** extended block device plugins to load, provide compression feedback at runtime

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_extblkdev_plugins "vdo fcm"
ceph config get osd osd_extblkdev_plugins
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `vdo fcm` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_extblkdev_plugins
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_find_best_info_ignore_history_les

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_find_best_info_ignore_history_les](../../../config/osd/osd.md#SP_osd_find_best_info_ignore_history_les) |

**作用：** ignore last_epoch_started value when peering AND PROBABLY LOSE DATA

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_find_best_info_ignore_history_les true
ceph config get osd osd_find_best_info_ignore_history_les
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_journal

| | |
|---|---|
| 类型 | Str · default `/var/lib/ceph/osd/$cluster-$id/journal` · **Advanced** |
| 表格 | [osd.md#SP_osd_journal](../../../config/osd/osd.md#SP_osd_journal) |

**作用：** path to OSD journal (when FileStore backend is in use)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_journal "/var/lib/ceph/osd/$cluster-$id/journal"
ceph config get osd osd_journal
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `/var/lib/ceph/osd/$cluster-$id/journal` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_journal
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_journal_flush_on_shutdown

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_journal_flush_on_shutdown](../../../config/osd/osd.md#SP_osd_journal_flush_on_shutdown) |

**作用：** flush FileStore journal contents during clean OSD shutdown

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_journal_flush_on_shutdown false
ceph config get osd osd_journal_flush_on_shutdown
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_journal_flush_on_shutdown
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_journal_size

| | |
|---|---|
| 类型 | Size · default `5_K` · **Advanced** |
| 表格 | [osd.md#SP_osd_journal_size](../../../config/osd/osd.md#SP_osd_journal_size) |

**作用：** size of FileStore journal (in MiB)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_journal_size 5_K
ceph config get osd osd_journal_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_journal_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_map_cache_size

| | |
|---|---|
| 类型 | Int · default `50` · **Advanced** |
| 表格 | [osd.md#SP_osd_map_cache_size](../../../config/osd/osd.md#SP_osd_map_cache_size) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_map_cache_size 50
ceph config get osd osd_map_cache_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `50` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_map_cache_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_num_cache_shards

| | |
|---|---|
| 类型 | Size · default `32` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [osd.md#SP_osd_num_cache_shards](../../../config/osd/osd.md#SP_osd_num_cache_shards) |

**作用：** The number of cache shards to use in the object store.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_num_cache_shards 32
ceph config get osd osd_num_cache_shards
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `32` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_num_cache_shards
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_numa_auto_affinity

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [osd.md#SP_osd_numa_auto_affinity](../../../config/osd/osd.md#SP_osd_numa_auto_affinity) |

**作用：** automatically set affinity to numa node when storage and network match

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_numa_auto_affinity false
ceph config get osd osd_numa_auto_affinity
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_numa_auto_affinity
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_numa_node

| | |
|---|---|
| 类型 | Int · default `-1` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [osd.md#SP_osd_numa_node](../../../config/osd/osd.md#SP_osd_numa_node) |

**作用：** set affinity to a numa node (-1 for none)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_numa_node 128
ceph config get osd osd_numa_node
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `-1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_numa_node
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_numa_prefer_iface

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [osd.md#SP_osd_numa_prefer_iface](../../../config/osd/osd.md#SP_osd_numa_prefer_iface) |

**作用：** prefer IP on network interface on same numa node as storage

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_numa_prefer_iface false
ceph config get osd osd_numa_prefer_iface
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_numa_prefer_iface
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_num_shards

| | |
|---|---|
| 类型 | Int · default `0` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [osd.md#SP_osd_op_num_shards](../../../config/osd/osd.md#SP_osd_op_num_shards) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_op_num_shards 64
ceph config get osd osd_op_num_shards
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_op_num_shards
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_num_shards_hdd

| | |
|---|---|
| 类型 | Int · default `1` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [osd.md#SP_osd_op_num_shards_hdd](../../../config/osd/osd.md#SP_osd_op_num_shards_hdd) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_op_num_shards_hdd 1
ceph config get osd osd_op_num_shards_hdd
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_op_num_shards_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_num_shards_ssd

| | |
|---|---|
| 类型 | Int · default `8` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [osd.md#SP_osd_op_num_shards_ssd](../../../config/osd/osd.md#SP_osd_op_num_shards_ssd) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_op_num_shards_ssd 8
ceph config get osd osd_op_num_shards_ssd
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `8` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_op_num_shards_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_num_threads_per_shard

| | |
|---|---|
| 类型 | Int · default `0` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [osd.md#SP_osd_op_num_threads_per_shard](../../../config/osd/osd.md#SP_osd_op_num_threads_per_shard) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_op_num_threads_per_shard 64
ceph config get osd osd_op_num_threads_per_shard
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_op_num_threads_per_shard
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_num_threads_per_shard_hdd

| | |
|---|---|
| 类型 | Int · default `5` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [osd.md#SP_osd_op_num_threads_per_shard_hdd](../../../config/osd/osd.md#SP_osd_op_num_threads_per_shard_hdd) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_op_num_threads_per_shard_hdd 5
ceph config get osd osd_op_num_threads_per_shard_hdd
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_op_num_threads_per_shard_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_num_threads_per_shard_ssd

| | |
|---|---|
| 类型 | Int · default `2` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [osd.md#SP_osd_op_num_threads_per_shard_ssd](../../../config/osd/osd.md#SP_osd_op_num_threads_per_shard_ssd) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_op_num_threads_per_shard_ssd 2
ceph config get osd osd_op_num_threads_per_shard_ssd
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_op_num_threads_per_shard_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_queue

| | |
|---|---|
| 类型 | Str · enum: ["wpq", "mclock_scheduler", "debug_random"] · default `mclock_scheduler` · **Advanced** |
| 表格 | [osd.md#SP_osd_op_queue](../../../config/osd/osd.md#SP_osd_op_queue) |

**作用：** OSD operation queue scheduler (`mclock_scheduler`, `wpq`, or `debug_random`). Production clusters should use mClock.

**何时使用：** Keep `mclock_scheduler` unless upstream support directs otherwise.

**示例：**

```bash
ceph config set osd osd_op_queue mclock_scheduler
ceph config get osd osd_op_queue
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `mclock_scheduler` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_op_queue
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_queue_cut_off

| | |
|---|---|
| 类型 | Str · enum: ["low", "high", "debug_random"] · default `high` · **Advanced** |
| 表格 | [osd.md#SP_osd_op_queue_cut_off](../../../config/osd/osd.md#SP_osd_op_queue_cut_off) |

**作用：** the threshold between high priority ops and low priority ops

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_op_queue_cut_off high
ceph config get osd osd_op_queue_cut_off
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `high` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_op_queue_cut_off
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_os_flags

| | |
|---|---|
| 类型 | Uint · default `0` · **Dev** |
| 表格 | [osd.md#SP_osd_os_flags](../../../config/osd/osd.md#SP_osd_os_flags) |

**作用：** flags to skip filestore omap or journal initialization

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_os_flags 64
ceph config get osd osd_os_flags
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_push_per_object_cost

| | |
|---|---|
| 类型 | Size · default `1000` · **Advanced** |
| 表格 | [osd.md#SP_osd_push_per_object_cost](../../../config/osd/osd.md#SP_osd_push_per_object_cost) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_push_per_object_cost 1000
ceph config get osd osd_push_per_object_cost
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_push_per_object_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_read_ec_check_for_errors

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_read_ec_check_for_errors](../../../config/osd/osd.md#SP_osd_read_ec_check_for_errors) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_read_ec_check_for_errors true
ceph config get osd osd_read_ec_check_for_errors
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_read_ec_check_for_errors
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_rocksdb_iterator_bounds_enabled

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [osd.md#SP_osd_rocksdb_iterator_bounds_enabled](../../../config/osd/osd.md#SP_osd_rocksdb_iterator_bounds_enabled) |

**作用：** Whether omap iterator bounds are applied to rocksdb iterator ReadOptions

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_rocksdb_iterator_bounds_enabled false
ceph config get osd osd_rocksdb_iterator_bounds_enabled
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_uuid

| | |
|---|---|
| 类型 | Uuid · default `(empty)` · **Advanced** |
| 表格 | [osd.md#SP_osd_uuid](../../../config/osd/osd.md#SP_osd_uuid) |

**作用：** uuid label for a new OSD

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_uuid (empty)
ceph config get osd osd_uuid
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_uuid
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← 概览](../OVERVIEW.md)
