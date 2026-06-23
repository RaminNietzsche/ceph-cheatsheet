# Qat

Global 配置深度指南 — 3 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [qat_compressor_busy_polling](#qat_compressor_busy_polling) | `False` | Advanced | Performance |
| [qat_compressor_enabled](#qat_compressor_enabled) | `False` | Advanced | Policy |
| [qat_compressor_session_max_number](#qat_compressor_session_max_number) | `256` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### qat_compressor_busy_polling

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [qat.md#SP_qat_compressor_busy_polling](../../../config/global/qat.md#SP_qat_compressor_busy_polling) |

**作用：** Set QAT busy bolling to reduce latency at the cost of potentially increasing CPU usage

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global qat_compressor_busy_polling true
ceph config get global qat_compressor_busy_polling
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global qat_compressor_busy_polling
ceph -s
```

---

### qat_compressor_enabled

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [qat.md#SP_qat_compressor_enabled](../../../config/global/qat.md#SP_qat_compressor_enabled) |

**作用：** Enable Intel QAT acceleration support for compression if available

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global qat_compressor_enabled true
ceph config get global qat_compressor_enabled
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global qat_compressor_enabled
ceph -s
```

---

### qat_compressor_session_max_number

| | |
|---|---|
| 类型 | Uint · default `256` · **Advanced** |
| 表格 | [qat.md#SP_qat_compressor_session_max_number](../../../config/global/qat.md#SP_qat_compressor_session_max_number) |

**作用：** Set the maximum number of session within Qatzip when using QAT compressor

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global qat_compressor_session_max_number 256
ceph config get global qat_compressor_session_max_number
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `256` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global qat_compressor_session_max_number
ceph -s
```

---


[← 概览](../OVERVIEW.md)
