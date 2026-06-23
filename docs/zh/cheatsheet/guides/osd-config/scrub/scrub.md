# Scrub

OSD 配置深度指南 — 39 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [osd_blocked_scrub_grace_period](#osd_blocked_scrub_grace_period) | `120` | Advanced | 性能 |
| [osd_deep_scrub_interval](#osd_deep_scrub_interval) | `7_day` | Advanced | 性能 |
| [osd_deep_scrub_interval_cv](#osd_deep_scrub_interval_cv) | `0.2` | Advanced | 性能 |
| [osd_deep_scrub_keys](#osd_deep_scrub_keys) | `1024` | Advanced | 性能 |
| [osd_deep_scrub_large_omap_object_key_threshold](#osd_deep_scrub_large_omap_object_key_threshold) | `200000` | Advanced | 性能 |
| [osd_deep_scrub_large_omap_object_value_sum_threshold](#osd_deep_scrub_large_omap_object_value_sum_threshold) | `1_G` | Advanced | 性能 |
| [osd_deep_scrub_randomize_ratio](#osd_deep_scrub_randomize_ratio) | `0.15` | Advanced | 性能 |
| [osd_deep_scrub_stride](#osd_deep_scrub_stride) | `4_M` | Advanced | 性能 |
| [osd_deep_scrub_update_digest_min_age](#osd_deep_scrub_update_digest_min_age) | `2_hr` | Advanced | 性能 |
| [osd_max_scrubs](#osd_max_scrubs) | `3` | Advanced | 性能 |
| [osd_scrub_auto_repair](#osd_scrub_auto_repair) | `False` | Advanced | 性能 |
| [osd_scrub_auto_repair_num_errors](#osd_scrub_auto_repair_num_errors) | `5` | Advanced | 性能 |
| [osd_scrub_backoff_ratio](#osd_scrub_backoff_ratio) | `0.66` | Dev | 开发 |
| [osd_scrub_begin_hour](#osd_scrub_begin_hour) | `0` | Advanced | 性能 |
| [osd_scrub_begin_week_day](#osd_scrub_begin_week_day) | `0` | Advanced | 性能 |
| [osd_scrub_chunk_max](#osd_scrub_chunk_max) | `15` | Advanced | 性能 |
| [osd_scrub_chunk_min](#osd_scrub_chunk_min) | `5` | Advanced | 性能 |
| [osd_scrub_disable_reservation_queuing](#osd_scrub_disable_reservation_queuing) | `False` | Advanced | 策略 |
| [osd_scrub_during_recovery](#osd_scrub_during_recovery) | `False` | Advanced | 性能 |
| [osd_scrub_end_hour](#osd_scrub_end_hour) | `0` | Advanced | 性能 |
| [osd_scrub_end_week_day](#osd_scrub_end_week_day) | `0` | Advanced | 性能 |
| [osd_scrub_extended_sleep](#osd_scrub_extended_sleep) | `0` | Advanced | 性能 |
| [osd_scrub_interval_randomize_ratio](#osd_scrub_interval_randomize_ratio) | `0.5` | Advanced | 性能 |
| [osd_scrub_invalid_stats](#osd_scrub_invalid_stats) | `True` | Advanced | 性能 |
| [osd_scrub_load_threshold](#osd_scrub_load_threshold) | `10.0` | Advanced | 性能 |
| [osd_scrub_max_interval](#osd_scrub_max_interval) | `7_day` | Advanced | 性能 |
| [osd_scrub_max_preemptions](#osd_scrub_max_preemptions) | `5` | Advanced | 性能 |
| [osd_scrub_min_interval](#osd_scrub_min_interval) | `1_day` | Advanced | 性能 |
| [osd_scrub_queued_snaptrims_limit](#osd_scrub_queued_snaptrims_limit) | `500` | Advanced | 性能 |
| [osd_scrub_retry_after_noscrub](#osd_scrub_retry_after_noscrub) | `60` | Advanced | 性能 |
| [osd_scrub_retry_delay](#osd_scrub_retry_delay) | `30` | Advanced | 性能 |
| [osd_scrub_retry_new_interval](#osd_scrub_retry_new_interval) | `10` | Advanced | 性能 |
| [osd_scrub_retry_pg_state](#osd_scrub_retry_pg_state) | `60` | Advanced | 性能 |
| [osd_scrub_retry_trimming](#osd_scrub_retry_trimming) | `10` | Advanced | 性能 |
| [osd_scrub_sleep](#osd_scrub_sleep) | `0` | Advanced | 性能 |
| [osd_shallow_scrub_chunk_max](#osd_shallow_scrub_chunk_max) | `100` | Advanced | 性能 |
| [osd_shallow_scrub_chunk_min](#osd_shallow_scrub_chunk_min) | `50` | Advanced | 性能 |
| [osd_stats_update_period_not_scrubbing](#osd_stats_update_period_not_scrubbing) | `120` | Advanced | 性能 |
| [osd_stats_update_period_scrubbing](#osd_stats_update_period_scrubbing) | `15` | Advanced | 性能 |

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

### osd_blocked_scrub_grace_period

| | |
|---|---|
| 类型 | Int · default `120` · **Advanced** |
| 表格 | [osd.md#SP_osd_blocked_scrub_grace_period](../../../config/osd/osd.md#SP_osd_blocked_scrub_grace_period) |

**作用：** Time (seconds) before issuing a cluster-log warning

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_blocked_scrub_grace_period 120
ceph config get osd osd_blocked_scrub_grace_period
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `120` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_blocked_scrub_grace_period
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_deep_scrub_interval

| | |
|---|---|
| 类型 | Float · default `7_day` · **Advanced** |
| 表格 | [osd.md#SP_osd_deep_scrub_interval](../../../config/osd/osd.md#SP_osd_deep_scrub_interval) |

**作用：** Interval (seconds) between deep scrubs that verify full object checksums.

**何时使用：** Shorten for compliance-heavy environments; lengthen on large HDD pools where deep scrub IO is costly.

**示例：**

```bash
ceph config set osd osd_deep_scrub_interval 7_day
ceph config get osd osd_deep_scrub_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `7_day` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_deep_scrub_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_deep_scrub_interval_cv

| | |
|---|---|
| 类型 | Float · default `0.2` · **Advanced** |
| 表格 | [osd.md#SP_osd_deep_scrub_interval_cv](../../../config/osd/osd.md#SP_osd_deep_scrub_interval_cv) |

**作用：** Determines the amount of variation in the deep scrub interval

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_deep_scrub_interval_cv 0.2
ceph config get osd osd_deep_scrub_interval_cv
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `0.4`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_deep_scrub_interval_cv
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_deep_scrub_keys

| | |
|---|---|
| 类型 | Int · default `1024` · **Advanced** |
| 表格 | [osd.md#SP_osd_deep_scrub_keys](../../../config/osd/osd.md#SP_osd_deep_scrub_keys) |

**作用：** Number of keys to read from an object at a time during deep scrub

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_deep_scrub_keys 1024
ceph config get osd osd_deep_scrub_keys
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1024` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_deep_scrub_keys
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_deep_scrub_large_omap_object_key_threshold

| | |
|---|---|
| 类型 | Uint · default `200000` · **Advanced** |
| 表格 | [osd.md#SP_osd_deep_scrub_large_omap_object_key_threshold](../../../config/osd/osd.md#SP_osd_deep_scrub_large_omap_object_key_threshold) |

**作用：** Warn when we encounter an object with more omap keys than this

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_deep_scrub_large_omap_object_key_threshold 200000
ceph config get osd osd_deep_scrub_large_omap_object_key_threshold
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `200000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_deep_scrub_large_omap_object_key_threshold
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_deep_scrub_large_omap_object_value_sum_threshold

| | |
|---|---|
| 类型 | Size · default `1_G` · **Advanced** |
| 表格 | [osd.md#SP_osd_deep_scrub_large_omap_object_value_sum_threshold](../../../config/osd/osd.md#SP_osd_deep_scrub_large_omap_object_value_sum_threshold) |

**作用：** Warn when we encounter an object with more omap key bytes than this

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_deep_scrub_large_omap_object_value_sum_threshold 1_G
ceph config get osd osd_deep_scrub_large_omap_object_value_sum_threshold
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_G` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_deep_scrub_large_omap_object_value_sum_threshold
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_deep_scrub_randomize_ratio

| | |
|---|---|
| 类型 | Float · default `0.15` · **Advanced** |
| 表格 | [osd.md#SP_osd_deep_scrub_randomize_ratio](../../../config/osd/osd.md#SP_osd_deep_scrub_randomize_ratio) |

**作用：** deprecated. Has no effect.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_deep_scrub_randomize_ratio 0.15
ceph config get osd osd_deep_scrub_randomize_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.15` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_deep_scrub_randomize_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_deep_scrub_stride

| | |
|---|---|
| 类型 | Size · default `4_M` · **Advanced** |
| 表格 | [osd.md#SP_osd_deep_scrub_stride](../../../config/osd/osd.md#SP_osd_deep_scrub_stride) |

**作用：** Number of bytes to read from an object at a time during deep scrub

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_deep_scrub_stride 4_M
ceph config get osd osd_deep_scrub_stride
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `4_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_deep_scrub_stride
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_deep_scrub_update_digest_min_age

| | |
|---|---|
| 类型 | Int · default `2_hr` · **Advanced** |
| 表格 | [osd.md#SP_osd_deep_scrub_update_digest_min_age](../../../config/osd/osd.md#SP_osd_deep_scrub_update_digest_min_age) |

**作用：** Update overall object digest only if object was last modified longer ago than this

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_deep_scrub_update_digest_min_age 2_hr
ceph config get osd osd_deep_scrub_update_digest_min_age
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2_hr` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_deep_scrub_update_digest_min_age
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_scrubs

| | |
|---|---|
| 类型 | Int · default `3` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_scrubs](../../../config/osd/osd.md#SP_osd_max_scrubs) |

**作用：** Maximum concurrent scrub operations per OSD. Scrub reads object data to verify checksums — too many scrubs compete with client I/O.

**何时使用：** Increase cautiously on fast media when scrubs lag behind the scrub interval. Decrease when `ceph -s` reports slow ops or OSD latency spikes during scrub windows.

**示例：**

```bash
ceph config set osd osd_max_scrubs 3
ceph config get osd osd_max_scrubs
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_max_scrubs
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

Pair with `osd_scrub_sleep` and deep-scrub intervals. HDD clusters often stay at 1; NVMe may tolerate 2–3 if load is low.

---

### osd_scrub_auto_repair

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_auto_repair](../../../config/osd/osd.md#SP_osd_scrub_auto_repair) |

**作用：** Automatically repair damaged objects detected during scrub

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_scrub_auto_repair true
ceph config get osd osd_scrub_auto_repair
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_auto_repair
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_auto_repair_num_errors

| | |
|---|---|
| 类型 | Uint · default `5` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_auto_repair_num_errors](../../../config/osd/osd.md#SP_osd_scrub_auto_repair_num_errors) |

**作用：** Maximum number of damaged objects to automatically repair

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_scrub_auto_repair_num_errors 5
ceph config get osd osd_scrub_auto_repair_num_errors
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_auto_repair_num_errors
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_backoff_ratio

| | |
|---|---|
| 类型 | Float · default `0.66` · **Dev** |
| 表格 | [osd.md#SP_osd_scrub_backoff_ratio](../../../config/osd/osd.md#SP_osd_scrub_backoff_ratio) |

**作用：** Backoff ratio for scheduling scrubs

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_scrub_backoff_ratio 0.66
ceph config get osd osd_scrub_backoff_ratio
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0.66`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_scrub_begin_hour

| | |
|---|---|
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_begin_hour](../../../config/osd/osd.md#SP_osd_scrub_begin_hour) |

**作用：** Restrict scrubbing to this hour of the day or later

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_scrub_begin_hour 64
ceph config get osd osd_scrub_begin_hour
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `23`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_begin_hour
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_begin_week_day

| | |
|---|---|
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_begin_week_day](../../../config/osd/osd.md#SP_osd_scrub_begin_week_day) |

**作用：** Restrict scrubbing to this day of the week or later

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_scrub_begin_week_day 64
ceph config get osd osd_scrub_begin_week_day
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `6`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_begin_week_day
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_chunk_max

| | |
|---|---|
| 类型 | Int · default `15` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_chunk_max](../../../config/osd/osd.md#SP_osd_scrub_chunk_max) |

**作用：** Maximum number of objects to deep-scrub in a single chunk

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_scrub_chunk_max 15
ceph config get osd osd_scrub_chunk_max
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `15` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_chunk_max
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_chunk_min

| | |
|---|---|
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_chunk_min](../../../config/osd/osd.md#SP_osd_scrub_chunk_min) |

**作用：** Minimum number of objects to deep-scrub in a single chunk

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_scrub_chunk_min 5
ceph config get osd osd_scrub_chunk_min
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_chunk_min
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_disable_reservation_queuing

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_disable_reservation_queuing](../../../config/osd/osd.md#SP_osd_scrub_disable_reservation_queuing) |

**作用：** Disable queuing of scrub reservations

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_scrub_disable_reservation_queuing true
ceph config get osd osd_scrub_disable_reservation_queuing
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_disable_reservation_queuing
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_during_recovery

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_during_recovery](../../../config/osd/osd.md#SP_osd_scrub_during_recovery) |

**作用：** Allow scrubbing when PGs on the OSD are undergoing recovery

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_scrub_during_recovery true
ceph config get osd osd_scrub_during_recovery
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_during_recovery
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_end_hour

| | |
|---|---|
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_end_hour](../../../config/osd/osd.md#SP_osd_scrub_end_hour) |

**作用：** Restrict scrubbing to hours of the day earlier than this

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_scrub_end_hour 64
ceph config get osd osd_scrub_end_hour
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `23`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_end_hour
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_end_week_day

| | |
|---|---|
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_end_week_day](../../../config/osd/osd.md#SP_osd_scrub_end_week_day) |

**作用：** Restrict scrubbing to days of the week earlier than this

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_scrub_end_week_day 64
ceph config get osd osd_scrub_end_week_day
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `6`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_end_week_day
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_extended_sleep

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_extended_sleep](../../../config/osd/osd.md#SP_osd_scrub_extended_sleep) |

**作用：** Duration (in seconds) of delay injected between chunks when scrubbing out of scrubbing hours

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_scrub_extended_sleep 0
ceph config get osd osd_scrub_extended_sleep
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_extended_sleep
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_interval_randomize_ratio

| | |
|---|---|
| 类型 | Float · default `0.5` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_interval_randomize_ratio](../../../config/osd/osd.md#SP_osd_scrub_interval_randomize_ratio) |

**作用：** Ratio of scrub interval to randomly vary

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_scrub_interval_randomize_ratio 0.5
ceph config get osd osd_scrub_interval_randomize_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_interval_randomize_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_invalid_stats

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_invalid_stats](../../../config/osd/osd.md#SP_osd_scrub_invalid_stats) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_scrub_invalid_stats false
ceph config get osd osd_scrub_invalid_stats
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_invalid_stats
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_load_threshold

| | |
|---|---|
| 类型 | Float · default `10.0` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_load_threshold](../../../config/osd/osd.md#SP_osd_scrub_load_threshold) |

**作用：** Allow scrubbing when system load divided by number of CPUs is below this value

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_scrub_load_threshold 10.0
ceph config get osd osd_scrub_load_threshold
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10.0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_load_threshold
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_max_interval

| | |
|---|---|
| 类型 | Float · default `7_day` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_max_interval](../../../config/osd/osd.md#SP_osd_scrub_max_interval) |

**作用：** Maximum interval (seconds) between shallow scrubs for a PG.

**何时使用：** Align with maintenance policy. Monitor `mon_warn_pg_not_scrubbed_ratio` warnings.

**示例：**

```bash
ceph config set osd osd_scrub_max_interval 7_day
ceph config get osd osd_scrub_max_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `7_day` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_max_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_max_preemptions

| | |
|---|---|
| 类型 | Uint · default `5` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_max_preemptions](../../../config/osd/osd.md#SP_osd_scrub_max_preemptions) |

**作用：** Set the maximum number of times we will preempt a deep scrub due to a client operation before blocking client IO to complete the scrub

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_scrub_max_preemptions 5
ceph config get osd osd_scrub_max_preemptions
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `30`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_max_preemptions
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_min_interval

| | |
|---|---|
| 类型 | Float · default `1_day` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_min_interval](../../../config/osd/osd.md#SP_osd_scrub_min_interval) |

**作用：** The desired interval between scrubs of a specific PG. Note that this option must be set at ``global`` scope, or for both ``mgr`` and``osd``.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_scrub_min_interval 1_day
ceph config get osd osd_scrub_min_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_day` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_min_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_queued_snaptrims_limit

| | |
|---|---|
| 类型 | Uint · default `500` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_queued_snaptrims_limit](../../../config/osd/osd.md#SP_osd_scrub_queued_snaptrims_limit) |

**作用：** Do not initiate periodic scrubs when the total snap-trim queues across all PGs exceeds this value. A value of '0' disables this limit.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_scrub_queued_snaptrims_limit 500
ceph config get osd osd_scrub_queued_snaptrims_limit
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `500` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_queued_snaptrims_limit
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_retry_after_noscrub

| | |
|---|---|
| 类型 | Int · default `60` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_retry_after_noscrub](../../../config/osd/osd.md#SP_osd_scrub_retry_after_noscrub) |

**作用：** Period (in seconds) before retrying to scrub a PG at a specific level after detecting a no-scrub or no-deep-scrub flag

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_scrub_retry_after_noscrub 60
ceph config get osd osd_scrub_retry_after_noscrub
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `60` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_retry_after_noscrub
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_retry_delay

| | |
|---|---|
| 类型 | Int · default `30` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_retry_delay](../../../config/osd/osd.md#SP_osd_scrub_retry_delay) |

**作用：** Period (in seconds) before retrying a PG that has failed a prior scrub.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_scrub_retry_delay 30
ceph config get osd osd_scrub_retry_delay
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_retry_delay
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_retry_new_interval

| | |
|---|---|
| 类型 | Int · default `10` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_retry_new_interval](../../../config/osd/osd.md#SP_osd_scrub_retry_new_interval) |

**作用：** Period (in seconds) before retrying a scrub aborted on a new interval

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_scrub_retry_new_interval 10
ceph config get osd osd_scrub_retry_new_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_retry_new_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_retry_pg_state

| | |
|---|---|
| 类型 | Int · default `60` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_retry_pg_state](../../../config/osd/osd.md#SP_osd_scrub_retry_pg_state) |

**作用：** Period (in seconds) before retrying to scrub a previously inactive/not-clean PG

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_scrub_retry_pg_state 60
ceph config get osd osd_scrub_retry_pg_state
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `60` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_retry_pg_state
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_retry_trimming

| | |
|---|---|
| 类型 | Int · default `10` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_retry_trimming](../../../config/osd/osd.md#SP_osd_scrub_retry_trimming) |

**作用：** Period (in seconds) before retrying to scrub a previously snap-trimming PG

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_scrub_retry_trimming 10
ceph config get osd osd_scrub_retry_trimming
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_retry_trimming
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_sleep

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_scrub_sleep](../../../config/osd/osd.md#SP_osd_scrub_sleep) |

**作用：** Duration (in seconds) of delay injected between chunks when scrubbing

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_scrub_sleep 0
ceph config get osd osd_scrub_sleep
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_scrub_sleep
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_shallow_scrub_chunk_max

| | |
|---|---|
| 类型 | Int · default `100` · **Advanced** |
| 表格 | [osd.md#SP_osd_shallow_scrub_chunk_max](../../../config/osd/osd.md#SP_osd_shallow_scrub_chunk_max) |

**作用：** Maximum number of objects to scrub in a single chunk

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_shallow_scrub_chunk_max 100
ceph config get osd osd_shallow_scrub_chunk_max
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `100` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_shallow_scrub_chunk_max
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_shallow_scrub_chunk_min

| | |
|---|---|
| 类型 | Int · default `50` · **Advanced** |
| 表格 | [osd.md#SP_osd_shallow_scrub_chunk_min](../../../config/osd/osd.md#SP_osd_shallow_scrub_chunk_min) |

**作用：** Minimum number of objects to scrub in a single chunk

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_shallow_scrub_chunk_min 50
ceph config get osd osd_shallow_scrub_chunk_min
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `50` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_shallow_scrub_chunk_min
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_stats_update_period_not_scrubbing

| | |
|---|---|
| 类型 | Int · default `120` · **Advanced** |
| 表格 | [osd.md#SP_osd_stats_update_period_not_scrubbing](../../../config/osd/osd.md#SP_osd_stats_update_period_not_scrubbing) |

**作用：** Stats update period (seconds) when not scrubbing

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_stats_update_period_not_scrubbing 120
ceph config get osd osd_stats_update_period_not_scrubbing
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `120` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_stats_update_period_not_scrubbing
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_stats_update_period_scrubbing

| | |
|---|---|
| 类型 | Int · default `15` · **Advanced** |
| 表格 | [osd.md#SP_osd_stats_update_period_scrubbing](../../../config/osd/osd.md#SP_osd_stats_update_period_scrubbing) |

**作用：** Stats update period (seconds) when scrubbing

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_stats_update_period_scrubbing 15
ceph config get osd osd_stats_update_period_scrubbing
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `15` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_stats_update_period_scrubbing
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← 概览](../OVERVIEW.md)
