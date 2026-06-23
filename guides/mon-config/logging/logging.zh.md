# Cluster logging

MON 配置深度指南 — 20 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mon_cluster_log_file](#mon_cluster_log_file) | `default=/var/log/ceph/$cluster.$channel.log cluster=/var/log/ceph/$cluster.log` | Advanced | Capacity |
| [mon_cluster_log_level](#mon_cluster_log_level) | `debug` | Advanced | Performance |
| [mon_cluster_log_to_file](#mon_cluster_log_to_file) | `True` | Advanced | Capacity |
| [mon_cluster_log_to_graylog](#mon_cluster_log_to_graylog) | `false` | Advanced | Performance |
| [mon_cluster_log_to_graylog_host](#mon_cluster_log_to_graylog_host) | `127.0.0.1` | Advanced | Performance |
| [mon_cluster_log_to_graylog_port](#mon_cluster_log_to_graylog_port) | `12201` | Advanced | Performance |
| [mon_cluster_log_to_journald](#mon_cluster_log_to_journald) | `false` | Advanced | Performance |
| [mon_cluster_log_to_stderr](#mon_cluster_log_to_stderr) | `False` | Advanced | Performance |
| [mon_cluster_log_to_syslog](#mon_cluster_log_to_syslog) | `default=false` | Advanced | Performance |
| [mon_cluster_log_to_syslog_facility](#mon_cluster_log_to_syslog_facility) | `daemon` | Advanced | Performance |
| [mon_health_detail_to_clog](#mon_health_detail_to_clog) | `True` | Dev | Dev |
| [mon_health_log_update_period](#mon_health_log_update_period) | `5` | Dev | Dev |
| [mon_health_to_clog](#mon_health_to_clog) | `True` | Advanced | Performance |
| [mon_health_to_clog_interval](#mon_health_to_clog_interval) | `10_min` | Advanced | Performance |
| [mon_health_to_clog_tick_interval](#mon_health_to_clog_tick_interval) | `1_min` | Dev | Dev |
| [mon_log_full_interval](#mon_log_full_interval) | `50` | Advanced | Performance |
| [mon_log_max](#mon_log_max) | `10000` | Advanced | Performance |
| [mon_log_max_summary](#mon_log_max_summary) | `50` | Advanced | Performance |
| [mon_max_log_entries_per_event](#mon_max_log_entries_per_event) | `4096` | Advanced | Performance |
| [mon_op_log_threshold](#mon_op_log_threshold) | `5` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_cluster_log_file

| | |
|---|---|
| 类型 | Str · default `default=/var/log/ceph/$cluster.$channel.log cluster=/var/log/ceph/$cluster.log` · **Advanced** |
| 表格 | [mon.md#SP_mon_cluster_log_file](../../../config/mon/mon.md#SP_mon_cluster_log_file) |

**作用：** File(s) to write cluster log to

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_cluster_log_file "default=/var/log/ceph/$cluster.$channel.log cluster=/var/log/ceph/$cluster.log"
ceph config get mon mon_cluster_log_file
```

**寻找最优值：**

**调优模型：** Capacity

1. 以 `default=/var/log/ceph/$cluster.$channel.log cluster=/var/log/ceph/$cluster.log` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_cluster_log_file
ceph -s
ceph mon stat
```

---

### mon_cluster_log_level

| | |
|---|---|
| 类型 | Str · default `debug` · **Advanced** |
| 表格 | [mon.md#SP_mon_cluster_log_level](../../../config/mon/mon.md#SP_mon_cluster_log_level) |

**作用：** Lowest level to include in cluster log file and/or in external log server

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_cluster_log_level debug
ceph config get mon mon_cluster_log_level
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `debug` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_cluster_log_level
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_file

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_cluster_log_to_file](../../../config/mon/mon.md#SP_mon_cluster_log_to_file) |

**作用：** Make monitor send cluster log messages to file

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_cluster_log_to_file false
ceph config get mon mon_cluster_log_to_file
```

**寻找最优值：**

**调优模型：** Capacity

1. 以 `True` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_cluster_log_to_file
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_graylog

| | |
|---|---|
| 类型 | Str · default `false` · **Advanced** |
| 表格 | [mon.md#SP_mon_cluster_log_to_graylog](../../../config/mon/mon.md#SP_mon_cluster_log_to_graylog) |

**作用：** Make monitor send cluster log to graylog

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_cluster_log_to_graylog false
ceph config get mon mon_cluster_log_to_graylog
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `false` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_cluster_log_to_graylog
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_graylog_host

| | |
|---|---|
| 类型 | Str · default `127.0.0.1` · **Advanced** |
| 表格 | [mon.md#SP_mon_cluster_log_to_graylog_host](../../../config/mon/mon.md#SP_mon_cluster_log_to_graylog_host) |

**作用：** Graylog host for cluster log messages

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_cluster_log_to_graylog_host "127.0.0.1"
ceph config get mon mon_cluster_log_to_graylog_host
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `127.0.0.1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_cluster_log_to_graylog_host
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_graylog_port

| | |
|---|---|
| 类型 | Str · default `12201` · **Advanced** |
| 表格 | [mon.md#SP_mon_cluster_log_to_graylog_port](../../../config/mon/mon.md#SP_mon_cluster_log_to_graylog_port) |

**作用：** Graylog port for cluster log messages

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_cluster_log_to_graylog_port 12201
ceph config get mon mon_cluster_log_to_graylog_port
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `12201` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_cluster_log_to_graylog_port
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_journald

| | |
|---|---|
| 类型 | Str · default `false` · **Advanced** |
| 表格 | [mon.md#SP_mon_cluster_log_to_journald](../../../config/mon/mon.md#SP_mon_cluster_log_to_journald) |

**作用：** Make monitor send cluster log to journald

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_cluster_log_to_journald false
ceph config get mon mon_cluster_log_to_journald
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `false` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_cluster_log_to_journald
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_stderr

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [mon.md#SP_mon_cluster_log_to_stderr](../../../config/mon/mon.md#SP_mon_cluster_log_to_stderr) |

**作用：** Make monitor send cluster log messages to stderr (prefixed by channel)

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mon mon_cluster_log_to_stderr true
ceph config get mon mon_cluster_log_to_stderr
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_cluster_log_to_stderr
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_syslog

| | |
|---|---|
| 类型 | Str · default `default=false` · **Advanced** |
| 表格 | [mon.md#SP_mon_cluster_log_to_syslog](../../../config/mon/mon.md#SP_mon_cluster_log_to_syslog) |

**作用：** Make monitor send cluster log messages to syslog

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_cluster_log_to_syslog "default=false"
ceph config get mon mon_cluster_log_to_syslog
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `default=false` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_cluster_log_to_syslog
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_syslog_facility

| | |
|---|---|
| 类型 | Str · default `daemon` · **Advanced** |
| 表格 | [mon.md#SP_mon_cluster_log_to_syslog_facility](../../../config/mon/mon.md#SP_mon_cluster_log_to_syslog_facility) |

**作用：** Syslog facility for cluster log messages

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_cluster_log_to_syslog_facility daemon
ceph config get mon mon_cluster_log_to_syslog_facility
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `daemon` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_cluster_log_to_syslog_facility
ceph -s
ceph mon stat
```

---

### mon_health_detail_to_clog

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [mon.md#SP_mon_health_detail_to_clog](../../../config/mon/mon.md#SP_mon_health_detail_to_clog) |

**作用：** log health detail to cluster log

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_health_detail_to_clog false
ceph config get mon mon_health_detail_to_clog
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_health_log_update_period

| | |
|---|---|
| 类型 | Int · default `5` · **Dev** |
| 表格 | [mon.md#SP_mon_health_log_update_period](../../../config/mon/mon.md#SP_mon_health_log_update_period) |

**作用：** minimum time in seconds between log messages about each health check

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_health_log_update_period 5
ceph config get mon mon_health_log_update_period
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`5`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_health_to_clog

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_health_to_clog](../../../config/mon/mon.md#SP_mon_health_to_clog) |

**作用：** log monitor health to cluster log

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_health_to_clog false
ceph config get mon mon_health_to_clog
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_health_to_clog
ceph -s
ceph mon stat
```

---

### mon_health_to_clog_interval

| | |
|---|---|
| 类型 | Int · default `10_min` · **Advanced** |
| 表格 | [mon.md#SP_mon_health_to_clog_interval](../../../config/mon/mon.md#SP_mon_health_to_clog_interval) |

**作用：** frequency to log monitor health to cluster log

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_health_to_clog_interval 10_min
ceph config get mon mon_health_to_clog_interval
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_health_to_clog_interval
ceph -s
ceph mon stat
```

---

### mon_health_to_clog_tick_interval

| | |
|---|---|
| 类型 | Float · default `1_min` · **Dev** |
| 表格 | [mon.md#SP_mon_health_to_clog_tick_interval](../../../config/mon/mon.md#SP_mon_health_to_clog_tick_interval) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_health_to_clog_tick_interval 1_min
ceph config get mon mon_health_to_clog_tick_interval
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`1_min`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_log_full_interval

| | |
|---|---|
| 类型 | Uint · default `50` · **Advanced** |
| 表格 | [mon.md#SP_mon_log_full_interval](../../../config/mon/mon.md#SP_mon_log_full_interval) |

**作用：** how many epochs before we encode a full copy of recent log keys

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_log_full_interval 50
ceph config get mon mon_log_full_interval
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `50` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_log_full_interval
ceph -s
ceph mon stat
```

---

### mon_log_max

| | |
|---|---|
| 类型 | Uint · default `10000` · **Advanced** |
| 表格 | [mon.md#SP_mon_log_max](../../../config/mon/mon.md#SP_mon_log_max) |

**作用：** number of recent cluster log messages to retain

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_log_max 10000
ceph config get mon mon_log_max
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_log_max
ceph -s
ceph mon stat
```

---

### mon_log_max_summary

| | |
|---|---|
| 类型 | Uint · default `50` · **Advanced** |
| 表格 | [mon.md#SP_mon_log_max_summary](../../../config/mon/mon.md#SP_mon_log_max_summary) |

**作用：** number of recent cluster log messages to dedup against

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_log_max_summary 50
ceph config get mon mon_log_max_summary
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `50` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_log_max_summary
ceph -s
ceph mon stat
```

---

### mon_max_log_entries_per_event

| | |
|---|---|
| 类型 | Int · default `4096` · **Advanced** |
| 表格 | [mon.md#SP_mon_max_log_entries_per_event](../../../config/mon/mon.md#SP_mon_max_log_entries_per_event) |

**作用：** max cluster log entries per paxos event

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_max_log_entries_per_event 4096
ceph config get mon mon_max_log_entries_per_event
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `4096` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_max_log_entries_per_event
ceph -s
ceph mon stat
```

---

### mon_op_log_threshold

| | |
|---|---|
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [mon.md#SP_mon_op_log_threshold](../../../config/mon/mon.md#SP_mon_op_log_threshold) |

**作用：** max number of slow ops to display

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_op_log_threshold 5
ceph config get mon mon_op_log_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_op_log_threshold
ceph -s
ceph mon stat
```

---


[← 概览](../OVERVIEW.md)
