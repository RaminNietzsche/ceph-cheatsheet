# Logging

MDS 配置深度指南 — 15 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mds/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mds_kill_after_journal_logs_flushed](#mds_kill_after_journal_logs_flushed) | `False` | Dev | 开发 |
| [mds_log_event_large_threshold](#mds_log_event_large_threshold) | `512_K` | Advanced | 性能 |
| [mds_log_events_per_segment](#mds_log_events_per_segment) | `1024` | Advanced | 性能 |
| [mds_log_max_events](#mds_log_max_events) | `-1` | Advanced | 性能 |
| [mds_log_max_segments](#mds_log_max_segments) | `128` | Advanced | 性能 |
| [mds_log_minor_segments_per_major_segment](#mds_log_minor_segments_per_major_segment) | `16` | Advanced | 性能 |
| [mds_log_pause](#mds_log_pause) | `False` | Dev | 开发 |
| [mds_log_segment_size](#mds_log_segment_size) | `0` | Advanced | 性能 |
| [mds_log_skip_corrupt_events](#mds_log_skip_corrupt_events) | `False` | Dev | 开发 |
| [mds_log_skip_unbounded_events](#mds_log_skip_unbounded_events) | `False` | Dev | 开发 |
| [mds_log_trim_decay_rate](#mds_log_trim_decay_rate) | `1.0` | Advanced | 性能 |
| [mds_log_trim_threshold](#mds_log_trim_threshold) | `128` | Advanced | 性能 |
| [mds_log_trim_upkeep_interval](#mds_log_trim_upkeep_interval) | `1000` | Advanced | 性能 |
| [mds_log_warn_factor](#mds_log_warn_factor) | `2` | Advanced | 性能 |
| [mds_op_log_threshold](#mds_op_log_threshold) | `5` | Dev | 开发 |

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
ceph config get <daemon> <option>  # e.g. mds
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mds_kill_after_journal_logs_flushed

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_kill_after_journal_logs_flushed](../../../config/mds/mds.md#SP_mds_kill_after_journal_logs_flushed) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_kill_after_journal_logs_flushed true
ceph config get mds mds_kill_after_journal_logs_flushed
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_log_event_large_threshold

| | |
|---|---|
| 类型 | Uint · default `512_K` · **Advanced** |
| 表格 | [mds.md#SP_mds_log_event_large_threshold](../../../config/mds/mds.md#SP_mds_log_event_large_threshold) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_log_event_large_threshold 512_K
ceph config get mds mds_log_event_large_threshold
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `512_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1_K`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_log_event_large_threshold
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_log_events_per_segment

| | |
|---|---|
| 类型 | Uint · default `1024` · **Advanced** |
| 表格 | [mds.md#SP_mds_log_events_per_segment](../../../config/mds/mds.md#SP_mds_log_events_per_segment) |

**作用：** maximum number of events in an MDS journal segment

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_log_events_per_segment 1024
ceph config get mds mds_log_events_per_segment
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1024` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_log_events_per_segment
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_log_max_events

| | |
|---|---|
| 类型 | Int · default `-1` · **Advanced** |
| 表格 | [mds.md#SP_mds_log_max_events](../../../config/mds/mds.md#SP_mds_log_max_events) |

**作用：** Maximum journal events before the MDS forces a segment rollover.

**何时使用：** Advanced — affects journal segmentation and recovery time after crash.

**示例：**

```bash
ceph config set mds mds_log_max_events 128
ceph config get mds mds_log_max_events
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `-1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_log_max_events
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_log_max_segments

| | |
|---|---|
| 类型 | Uint · default `128` · **Advanced** |
| 表格 | [mds.md#SP_mds_log_max_segments](../../../config/mds/mds.md#SP_mds_log_max_segments) |

**作用：** maximum number of segments which may be untrimmed

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_log_max_segments 128
ceph config get mds mds_log_max_segments
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `128` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `8`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_log_max_segments
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_log_minor_segments_per_major_segment

| | |
|---|---|
| 类型 | Uint · default `16` · **Advanced** |
| 表格 | [mds.md#SP_mds_log_minor_segments_per_major_segment](../../../config/mds/mds.md#SP_mds_log_minor_segments_per_major_segment) |

**作用：** Number of minor segments per major segment.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_log_minor_segments_per_major_segment 16
ceph config get mds mds_log_minor_segments_per_major_segment
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `16` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `4`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_log_minor_segments_per_major_segment
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_log_pause

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_log_pause](../../../config/mds/mds.md#SP_mds_log_pause) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_log_pause true
ceph config get mds mds_log_pause
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_log_segment_size

| | |
|---|---|
| 类型 | Size · default `0` · **Advanced** |
| 表格 | [mds.md#SP_mds_log_segment_size](../../../config/mds/mds.md#SP_mds_log_segment_size) |

**作用：** size in bytes of each MDS log segment

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_log_segment_size 64
ceph config get mds mds_log_segment_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_log_segment_size
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_log_skip_corrupt_events

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_log_skip_corrupt_events](../../../config/mds/mds.md#SP_mds_log_skip_corrupt_events) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_log_skip_corrupt_events true
ceph config get mds mds_log_skip_corrupt_events
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_log_skip_unbounded_events

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_log_skip_unbounded_events](../../../config/mds/mds.md#SP_mds_log_skip_unbounded_events) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_log_skip_unbounded_events true
ceph config get mds mds_log_skip_unbounded_events
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_log_trim_decay_rate

| | |
|---|---|
| 类型 | Float · default `1.0` · **Advanced** |
| 表格 | [mds.md#SP_mds_log_trim_decay_rate](../../../config/mds/mds.md#SP_mds_log_trim_decay_rate) |

**作用：** MDS log trim decay rate

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_log_trim_decay_rate 1.0
ceph config get mds mds_log_trim_decay_rate
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1.0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0.01`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_log_trim_decay_rate
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_log_trim_threshold

| | |
|---|---|
| 类型 | Size · default `128` · **Advanced** |
| 表格 | [mds.md#SP_mds_log_trim_threshold](../../../config/mds/mds.md#SP_mds_log_trim_threshold) |

**作用：** MDS log trim threshold

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_log_trim_threshold 128
ceph config get mds mds_log_trim_threshold
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `128` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_log_trim_threshold
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_log_trim_upkeep_interval

| | |
|---|---|
| 类型 | Millisecs · default `1000` · **Advanced** |
| 表格 | [mds.md#SP_mds_log_trim_upkeep_interval](../../../config/mds/mds.md#SP_mds_log_trim_upkeep_interval) |

**作用：** MDS log trimming interval

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mds mds_log_trim_upkeep_interval 1000
ceph config get mds mds_log_trim_upkeep_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_log_trim_upkeep_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_log_warn_factor

| | |
|---|---|
| 类型 | Float · default `2` · **Advanced** |
| 表格 | [mds.md#SP_mds_log_warn_factor](../../../config/mds/mds.md#SP_mds_log_warn_factor) |

**作用：** trigger MDS_HEALTH_TRIM warning when the mds log is longer than mds_log_max_segments * mds_log_warn_factor

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_log_warn_factor 2
ceph config get mds mds_log_warn_factor
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_log_warn_factor
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_op_log_threshold

| | |
|---|---|
| 类型 | Int · default `5` · **Dev** |
| 表格 | [mds.md#SP_mds_op_log_threshold](../../../config/mds/mds.md#SP_mds_op_log_threshold) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_op_log_threshold 5
ceph config get mds mds_op_log_threshold
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`5`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
