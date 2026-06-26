# Log

Global 配置深度指南 — 14 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [log_coarse_timestamps](#log_coarse_timestamps) | `True` | Advanced | 性能 |
| [log_file](#log_file) | `/var/log/ceph/$cluster-$name.log` | Basic | 容量 |
| [log_flush_on_exit](#log_flush_on_exit) | `False` | Advanced | 性能 |
| [log_graylog_host](#log_graylog_host) | `127.0.0.1` | Basic | 策略 |
| [log_graylog_port](#log_graylog_port) | `12201` | Basic | 策略 |
| [log_max_new](#log_max_new) | `1000` | Advanced | 性能 |
| [log_max_recent](#log_max_recent) | `10000` | Advanced | 性能 |
| [log_stderr_prefix](#log_stderr_prefix) | `(empty)` | Advanced | 性能 |
| [log_stop_at_utilization](#log_stop_at_utilization) | `0.97` | Basic | 策略 |
| [log_to_file](#log_to_file) | `True` | Basic | 容量 |
| [log_to_graylog](#log_to_graylog) | `False` | Basic | 策略 |
| [log_to_journald](#log_to_journald) | `False` | Basic | 策略 |
| [log_to_stderr](#log_to_stderr) | `False` | Basic | 策略 |
| [log_to_syslog](#log_to_syslog) | `False` | Basic | 策略 |

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

### log_coarse_timestamps

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [log.md#SP_log_coarse_timestamps](../../../config/global/log.md#SP_log_coarse_timestamps) |

**作用：** Timestamp log entries from coarse system clock to improve performance

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global log_coarse_timestamps false
ceph config get global log_coarse_timestamps
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global log_coarse_timestamps
ceph -s
```

---

### log_file

| | |
|---|---|
| 类型 | Str · default `/var/log/ceph/$cluster-$name.log` · **Basic** |
| 表格 | [log.md#SP_log_file](../../../config/global/log.md#SP_log_file) |

**作用：** path to log file

**何时使用：** 核心 Global 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set global log_file "/var/log/ceph/$cluster-$name.log"
ceph config get global log_file
```

**寻找最优值：**

**调优模型：** 容量

1. 以 `/var/log/ceph/$cluster-$name.log` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global log_file
ceph -s
```

---

### log_flush_on_exit

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [log.md#SP_log_flush_on_exit](../../../config/global/log.md#SP_log_flush_on_exit) |

**作用：** Set a process exit handler to ensure the log is flushed on exit

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global log_flush_on_exit true
ceph config get global log_flush_on_exit
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global log_flush_on_exit
ceph -s
```

---

### log_graylog_host

| | |
|---|---|
| 类型 | Str · default `127.0.0.1` · **Basic** |
| 表格 | [log.md#SP_log_graylog_host](../../../config/global/log.md#SP_log_graylog_host) |

**作用：** Address or hostname of Graylog server to log to

**何时使用：** 核心 Global 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set global log_graylog_host "127.0.0.1"
ceph config get global log_graylog_host
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `127.0.0.1` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global log_graylog_host
ceph -s
```

---

### log_graylog_port

| | |
|---|---|
| 类型 | Int · default `12201` · **Basic** |
| 表格 | [log.md#SP_log_graylog_port](../../../config/global/log.md#SP_log_graylog_port) |

**作用：** TCP port number for the remote Graylog server

**何时使用：** 核心 Global 行为 — 生产环境变更前请审阅。

**相关选项：**

- [`log_graylog_host`](../../../config/global/log.md#SP_log_graylog_host)

**示例：**

```bash
ceph config set global log_graylog_port 12201
ceph config get global log_graylog_port
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `12201` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global log_graylog_port
ceph -s
```

---

### log_max_new

| | |
|---|---|
| 类型 | Int · default `1000` · **Advanced** |
| 表格 | [log.md#SP_log_max_new](../../../config/global/log.md#SP_log_max_new) |

**作用：** Max unwritten log entries to allow before flushing

**何时使用：** 触及资源限制或保护集群容量时调整。

**相关选项：**

- [`log_max_recent`](../../../config/global/log.md#SP_log_max_recent)

**示例：**

```bash
ceph config set global log_max_new 1000
ceph config get global log_max_new
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global log_max_new
ceph -s
```

---

### log_max_recent

| | |
|---|---|
| 类型 | Int · default `10000` · **Advanced** |
| 表格 | [log.md#SP_log_max_recent](../../../config/global/log.md#SP_log_max_recent) |

**作用：** Recent log entries to keep in memory to dump in the event of a crash The purpose of this option is to log at a higher debug level only to the in-memory buffer, and write out the detailed log messages only if there is a crash. Only log entries below the lower log level will be written unconditionally to the log. For example, debug_osd=1/5 will write everything <= 1 to the log unconditionally but keep entries at levels 2-5 in memory. If there is a seg fault or assertion failure, all entries will be dumped to the log.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global log_max_recent 10000
ceph config get global log_max_recent
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global log_max_recent
ceph -s
```

---

### log_stderr_prefix

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [log.md#SP_log_stderr_prefix](../../../config/global/log.md#SP_log_stderr_prefix) |

**作用：** String to prefix log messages with when sent to stderr This is useful in container environments when combined with mon_cluster_log_to_stderr. The mon log prefixes each line with the channel name (e.g., 'default', 'audit'), while log_stderr_prefix can be set to 'debug '.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global log_stderr_prefix "example"
ceph config get global log_stderr_prefix
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global log_stderr_prefix
ceph -s
```

---

### log_stop_at_utilization

| | |
|---|---|
| 类型 | Float · default `0.97` · **Basic** |
| 表格 | [log.md#SP_log_stop_at_utilization](../../../config/global/log.md#SP_log_stop_at_utilization) |

**作用：** Stop writing to the log file when device utilization reaches this ratio

**何时使用：** 核心 Global 行为 — 生产环境变更前请审阅。

**相关选项：**

- [`log_file`](../../../config/global/log.md#SP_log_file)

**示例：**

```bash
ceph config set global log_stop_at_utilization 0.97
ceph config get global log_stop_at_utilization
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `0.97` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global log_stop_at_utilization
ceph -s
```

---

### log_to_file

| | |
|---|---|
| 类型 | Bool · default `True` · **Basic** |
| 表格 | [log.md#SP_log_to_file](../../../config/global/log.md#SP_log_to_file) |

**作用：** send log lines to a file

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**相关选项：**

- [`log_file`](../../../config/global/log.md#SP_log_file)

**示例：**

```bash
ceph config set global log_to_file false
ceph config get global log_to_file
```

**寻找最优值：**

**调优模型：** 容量

1. 以 `True` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global log_to_file
ceph -s
```

---

### log_to_graylog

| | |
|---|---|
| 类型 | Bool · default `False` · **Basic** |
| 表格 | [log.md#SP_log_to_graylog](../../../config/global/log.md#SP_log_to_graylog) |

**作用：** Send log lines to remote Graylog server

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global log_to_graylog true
ceph config get global log_to_graylog
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global log_to_graylog
ceph -s
```

---

### log_to_journald

| | |
|---|---|
| 类型 | Bool · default `False` · **Basic** |
| 表格 | [log.md#SP_log_to_journald](../../../config/global/log.md#SP_log_to_journald) |

**作用：** Send log lines to journald

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global log_to_journald true
ceph config get global log_to_journald
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global log_to_journald
ceph -s
```

---

### log_to_stderr

| | |
|---|---|
| 类型 | Bool · default `False` · **Basic** |
| 表格 | [log.md#SP_log_to_stderr](../../../config/global/log.md#SP_log_to_stderr) |

**作用：** send log lines to stderr When Ceph runs as a library (e.g., librados), the default value set to false because stderr may not be writable by the application. For daemons, the daemon_default of false is used instead.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global log_to_stderr true
ceph config get global log_to_stderr
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global log_to_stderr
ceph -s
```

---

### log_to_syslog

| | |
|---|---|
| 类型 | Bool · default `False` · **Basic** |
| 表格 | [log.md#SP_log_to_syslog](../../../config/global/log.md#SP_log_to_syslog) |

**作用：** Send log lines to syslog facility

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global log_to_syslog true
ceph config get global log_to_syslog
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global log_to_syslog
ceph -s
```

---


[← 概览](../OVERVIEW.md)
