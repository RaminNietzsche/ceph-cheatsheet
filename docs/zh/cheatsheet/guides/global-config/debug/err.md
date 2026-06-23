# Err

Global 配置深度指南 — 4 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [err_to_graylog](#err_to_graylog) | `False` | Basic | 策略 |
| [err_to_journald](#err_to_journald) | `False` | Basic | 策略 |
| [err_to_stderr](#err_to_stderr) | `True` | Basic | 策略 |
| [err_to_syslog](#err_to_syslog) | `False` | Basic | 策略 |

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

### err_to_graylog

| | |
|---|---|
| 类型 | Bool · default `False` · **Basic** |
| 表格 | [err.md#SP_err_to_graylog](../../../config/global/err.md#SP_err_to_graylog) |

**作用：** Send critical error log lines to remote Graylog server

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global err_to_graylog true
ceph config get global err_to_graylog
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global err_to_graylog
ceph -s
```

---

### err_to_journald

| | |
|---|---|
| 类型 | Bool · default `False` · **Basic** |
| 表格 | [err.md#SP_err_to_journald](../../../config/global/err.md#SP_err_to_journald) |

**作用：** Send critical error log lines to journald

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global err_to_journald true
ceph config get global err_to_journald
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global err_to_journald
ceph -s
```

---

### err_to_stderr

| | |
|---|---|
| 类型 | Bool · default `True` · **Basic** |
| 表格 | [err.md#SP_err_to_stderr](../../../config/global/err.md#SP_err_to_stderr) |

**作用：** send critical error log lines to stderr

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global err_to_stderr false
ceph config get global err_to_stderr
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global err_to_stderr
ceph -s
```

---

### err_to_syslog

| | |
|---|---|
| 类型 | Bool · default `False` · **Basic** |
| 表格 | [err.md#SP_err_to_syslog](../../../config/global/err.md#SP_err_to_syslog) |

**作用：** Send critical error log lines to syslog facility

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global err_to_syslog true
ceph config get global err_to_syslog
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global err_to_syslog
ceph -s
```

---


[← 概览](../OVERVIEW.md)
