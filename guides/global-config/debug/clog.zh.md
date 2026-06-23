# Clog

Global 配置深度指南 — 7 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [clog_to_graylog](#clog_to_graylog) | `false` | Advanced | 性能 |
| [clog_to_graylog_host](#clog_to_graylog_host) | `127.0.0.1` | Advanced | 性能 |
| [clog_to_graylog_port](#clog_to_graylog_port) | `12201` | Advanced | 性能 |
| [clog_to_monitors](#clog_to_monitors) | `default=true` | Advanced | 性能 |
| [clog_to_syslog](#clog_to_syslog) | `false` | Advanced | 性能 |
| [clog_to_syslog_facility](#clog_to_syslog_facility) | `default=daemon audit=local0` | Advanced | 性能 |
| [clog_to_syslog_level](#clog_to_syslog_level) | `info` | Advanced | 性能 |

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

### clog_to_graylog

| | |
|---|---|
| 类型 | Str · default `false` · **Advanced** |
| 表格 | [clog.md#SP_clog_to_graylog](../../../config/global/clog.md#SP_clog_to_graylog) |

**作用：** Make daemons send cluster log to graylog

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global clog_to_graylog false
ceph config get global clog_to_graylog
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `false` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global clog_to_graylog
ceph -s
```

---

### clog_to_graylog_host

| | |
|---|---|
| 类型 | Str · default `127.0.0.1` · **Advanced** |
| 表格 | [clog.md#SP_clog_to_graylog_host](../../../config/global/clog.md#SP_clog_to_graylog_host) |

**作用：** Graylog host to cluster log messages

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global clog_to_graylog_host "127.0.0.1"
ceph config get global clog_to_graylog_host
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `127.0.0.1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global clog_to_graylog_host
ceph -s
```

---

### clog_to_graylog_port

| | |
|---|---|
| 类型 | Str · default `12201` · **Advanced** |
| 表格 | [clog.md#SP_clog_to_graylog_port](../../../config/global/clog.md#SP_clog_to_graylog_port) |

**作用：** Graylog port number for cluster log messages

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global clog_to_graylog_port 12201
ceph config get global clog_to_graylog_port
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `12201` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global clog_to_graylog_port
ceph -s
```

---

### clog_to_monitors

| | |
|---|---|
| 类型 | Str · default `default=true` · **Advanced** |
| 表格 | [clog.md#SP_clog_to_monitors](../../../config/global/clog.md#SP_clog_to_monitors) |

**作用：** Make daemons send cluster log messages to monitors

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global clog_to_monitors "default=true"
ceph config get global clog_to_monitors
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `default=true` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global clog_to_monitors
ceph -s
```

---

### clog_to_syslog

| | |
|---|---|
| 类型 | Str · default `false` · **Advanced** |
| 表格 | [clog.md#SP_clog_to_syslog](../../../config/global/clog.md#SP_clog_to_syslog) |

**作用：** Make daemons send cluster log messages to syslog

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global clog_to_syslog false
ceph config get global clog_to_syslog
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `false` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global clog_to_syslog
ceph -s
```

---

### clog_to_syslog_facility

| | |
|---|---|
| 类型 | Str · default `default=daemon audit=local0` · **Advanced** |
| 表格 | [clog.md#SP_clog_to_syslog_facility](../../../config/global/clog.md#SP_clog_to_syslog_facility) |

**作用：** Syslog facility for cluster log messages

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global clog_to_syslog_facility "default=daemon audit=local0"
ceph config get global clog_to_syslog_facility
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `default=daemon audit=local0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global clog_to_syslog_facility
ceph -s
```

---

### clog_to_syslog_level

| | |
|---|---|
| 类型 | Str · default `info` · **Advanced** |
| 表格 | [clog.md#SP_clog_to_syslog_level](../../../config/global/clog.md#SP_clog_to_syslog_level) |

**作用：** Syslog level for cluster log messages

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global clog_to_syslog_level info
ceph config get global clog_to_syslog_level
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `info` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global clog_to_syslog_level
ceph -s
```

---


[← 概览](../OVERVIEW.md)
