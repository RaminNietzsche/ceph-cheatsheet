# Intervals

MDS 配置深度指南 — 19 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mds/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mds_bal_fragment_interval](#mds_bal_fragment_interval) | `5` | Advanced | 性能 |
| [mds_bal_interval](#mds_bal_interval) | `10` | Advanced | 性能 |
| [mds_bal_sample_interval](#mds_bal_sample_interval) | `3` | Advanced | 性能 |
| [mds_beacon_interval](#mds_beacon_interval) | `4` | Advanced | 性能 |
| [mds_cache_release_free_interval](#mds_cache_release_free_interval) | `10` | Dev | 开发 |
| [mds_cache_trim_interval](#mds_cache_trim_interval) | `1` | Advanced | 性能 |
| [mds_dirstat_min_interval](#mds_dirstat_min_interval) | `1` | Dev | 开发 |
| [mds_extraordinary_events_dump_interval](#mds_extraordinary_events_dump_interval) | `0` | Advanced | 性能 |
| [mds_freeze_tree_timeout](#mds_freeze_tree_timeout) | `30` | Dev | 开发 |
| [mds_metrics_update_interval](#mds_metrics_update_interval) | `2` | Advanced | 性能 |
| [mds_mon_shutdown_timeout](#mds_mon_shutdown_timeout) | `5` | Advanced | 性能 |
| [mds_ping_interval](#mds_ping_interval) | `5` | Advanced | 性能 |
| [mds_reconnect_timeout](#mds_reconnect_timeout) | `45` | Advanced | 性能 |
| [mds_replay_interval](#mds_replay_interval) | `1` | Advanced | 性能 |
| [mds_scatter_nudge_interval](#mds_scatter_nudge_interval) | `5` | Advanced | 性能 |
| [mds_session_blocklist_on_timeout](#mds_session_blocklist_on_timeout) | `True` | Advanced | 性能 |
| [mds_task_status_update_interval](#mds_task_status_update_interval) | `2` | Dev | 开发 |
| [mds_tick_interval](#mds_tick_interval) | `5` | Advanced | 性能 |
| [subv_metrics_window_interval](#subv_metrics_window_interval) | `30` | Dev | 开发 |

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

### mds_bal_fragment_interval

| | |
|---|---|
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [mds.md#SP_mds_bal_fragment_interval](../../../config/mds/mds.md#SP_mds_bal_fragment_interval) |

**作用：** delay in seconds before interrupting client IO to perform splits

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mds mds_bal_fragment_interval 5
ceph config get mds mds_bal_fragment_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_bal_fragment_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_interval

| | |
|---|---|
| 类型 | Int · default `10` · **Advanced** |
| 表格 | [mds.md#SP_mds_bal_interval](../../../config/mds/mds.md#SP_mds_bal_interval) |

**作用：** interval between MDS balancer cycles

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mds mds_bal_interval 10
ceph config get mds mds_bal_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_bal_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_sample_interval

| | |
|---|---|
| 类型 | Float · default `3` · **Advanced** |
| 表格 | [mds.md#SP_mds_bal_sample_interval](../../../config/mds/mds.md#SP_mds_bal_sample_interval) |

**作用：** interval in seconds between balancer ticks

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mds mds_bal_sample_interval 3
ceph config get mds mds_bal_sample_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_bal_sample_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_beacon_interval

| | |
|---|---|
| 类型 | Float · default `4` · **Advanced** |
| 表格 | [mds.md#SP_mds_beacon_interval](../../../config/mds/mds.md#SP_mds_beacon_interval) |

**作用：** How often (seconds) an MDS sends beacons to monitors.

**何时使用：** Rarely changed; must stay well below `mds_beacon_grace`.

**示例：**

```bash
ceph config set mds mds_beacon_interval 4
ceph config get mds mds_beacon_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `4` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_beacon_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_cache_release_free_interval

| | |
|---|---|
| 类型 | Secs · default `10` · **Dev** |
| 表格 | [mds.md#SP_mds_cache_release_free_interval](../../../config/mds/mds.md#SP_mds_cache_release_free_interval) |

**作用：** Interval in seconds between heap releases

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_cache_release_free_interval 10
ceph config get mds mds_cache_release_free_interval
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`10`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_cache_trim_interval

| | |
|---|---|
| 类型 | Secs · default `1` · **Advanced** |
| 表格 | [mds.md#SP_mds_cache_trim_interval](../../../config/mds/mds.md#SP_mds_cache_trim_interval) |

**作用：** Interval in seconds between cache trims

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mds mds_cache_trim_interval 1
ceph config get mds mds_cache_trim_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_cache_trim_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_dirstat_min_interval

| | |
|---|---|
| 类型 | Float · default `1` · **Dev** |
| 表格 | [mds.md#SP_mds_dirstat_min_interval](../../../config/mds/mds.md#SP_mds_dirstat_min_interval) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_dirstat_min_interval 1
ceph config get mds mds_dirstat_min_interval
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_extraordinary_events_dump_interval

| | |
|---|---|
| 类型 | Secs · default `0` · **Advanced** |
| 表格 | [mds.md#SP_mds_extraordinary_events_dump_interval](../../../config/mds/mds.md#SP_mds_extraordinary_events_dump_interval) |

**作用：** Interval in seconds for dumping the recent in-memory logs when there is an extra-ordinary event. Interval in seconds for dumping the recent in-memory logs when there is an extra-ordinary event. The default is ``0`` (disabled). The log level should be ``< 10`` and the gather level should be ``>=10`` in debug_mds for enabling this option.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mds mds_extraordinary_events_dump_interval 0
ceph config get mds mds_extraordinary_events_dump_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `60`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_extraordinary_events_dump_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_freeze_tree_timeout

| | |
|---|---|
| 类型 | Float · default `30` · **Dev** |
| 表格 | [mds.md#SP_mds_freeze_tree_timeout](../../../config/mds/mds.md#SP_mds_freeze_tree_timeout) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_freeze_tree_timeout 30
ceph config get mds mds_freeze_tree_timeout
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`30`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_metrics_update_interval

| | |
|---|---|
| 类型 | Secs · default `2` · **Advanced** |
| 表格 | [mds.md#SP_mds_metrics_update_interval](../../../config/mds/mds.md#SP_mds_metrics_update_interval) |

**作用：** interval in seconds for metrics data update. interval in seconds after which active MDSs send client metrics data to rank 0.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mds mds_metrics_update_interval 2
ceph config get mds mds_metrics_update_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_metrics_update_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_mon_shutdown_timeout

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [mds.md#SP_mds_mon_shutdown_timeout](../../../config/mds/mds.md#SP_mds_mon_shutdown_timeout) |

**作用：** time to wait for mon to receive damaged MDS rank notification

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mds mds_mon_shutdown_timeout 5
ceph config get mds mds_mon_shutdown_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_mon_shutdown_timeout
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_ping_interval

| | |
|---|---|
| 类型 | Secs · default `5` · **Advanced** |
| 表格 | [mds.md#SP_mds_ping_interval](../../../config/mds/mds.md#SP_mds_ping_interval) |

**作用：** interval in seconds for sending ping messages to active MDSs. interval in seconds for rank 0 to send ping messages to all active MDSs.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mds mds_ping_interval 5
ceph config get mds mds_ping_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_ping_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_reconnect_timeout

| | |
|---|---|
| 类型 | Float · default `45` · **Advanced** |
| 表格 | [mds.md#SP_mds_reconnect_timeout](../../../config/mds/mds.md#SP_mds_reconnect_timeout) |

**作用：** Timeout in seconds to wait for clients to reconnect during MDS reconnect recovery state

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mds mds_reconnect_timeout 45
ceph config get mds mds_reconnect_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `45` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_reconnect_timeout
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_replay_interval

| | |
|---|---|
| 类型 | Float · default `1` · **Advanced** |
| 表格 | [mds.md#SP_mds_replay_interval](../../../config/mds/mds.md#SP_mds_replay_interval) |

**作用：** time in seconds between replay of updates to journal by standby replay MDS

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mds mds_replay_interval 1
ceph config get mds mds_replay_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_replay_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_scatter_nudge_interval

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [mds.md#SP_mds_scatter_nudge_interval](../../../config/mds/mds.md#SP_mds_scatter_nudge_interval) |

**作用：** minimum interval between scatter lock updates

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mds mds_scatter_nudge_interval 5
ceph config get mds mds_scatter_nudge_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_scatter_nudge_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_session_blocklist_on_timeout

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mds.md#SP_mds_session_blocklist_on_timeout](../../../config/mds/mds.md#SP_mds_session_blocklist_on_timeout) |

**作用：** Blocklist clients whose sessions have become stale

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mds mds_session_blocklist_on_timeout false
ceph config get mds mds_session_blocklist_on_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_session_blocklist_on_timeout
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_task_status_update_interval

| | |
|---|---|
| 类型 | Float · default `2` · **Dev** |
| 表格 | [mds.md#SP_mds_task_status_update_interval](../../../config/mds/mds.md#SP_mds_task_status_update_interval) |

**作用：** task status update interval to manager interval (in seconds) for sending mds task status to ceph manager

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_task_status_update_interval 2
ceph config get mds mds_task_status_update_interval
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`2`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_tick_interval

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [mds.md#SP_mds_tick_interval](../../../config/mds/mds.md#SP_mds_tick_interval) |

**作用：** time in seconds between upkeep tasks

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mds mds_tick_interval 5
ceph config get mds mds_tick_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_tick_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### subv_metrics_window_interval

| | |
|---|---|
| 类型 | Secs · default `30` · **Dev** |
| 表格 | [mds.md#SP_subv_metrics_window_interval](../../../config/mds/mds.md#SP_subv_metrics_window_interval) |

**作用：** subvolume metrics sliding window interval, seconds interval in seconds to hold values in sliding window for subvolume metrics

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds subv_metrics_window_interval 30
ceph config get mds subv_metrics_window_interval
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`30`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
