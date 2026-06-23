# Journaler

Global 配置深度指南 — 3 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [journaler_prefetch_periods](#journaler_prefetch_periods) | `10` | Advanced | Performance |
| [journaler_prezero_periods](#journaler_prezero_periods) | `5` | Advanced | Performance |
| [journaler_write_head_interval](#journaler_write_head_interval) | `15` | Advanced | Performance |

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

### journaler_prefetch_periods

| | |
|---|---|
| 类型 | Uint · default `10` · **Advanced** |
| 表格 | [journaler.md#SP_journaler_prefetch_periods](../../../config/global/journaler.md#SP_journaler_prefetch_periods) |

**作用：** Number of striping periods to prefetch while reading MDS journal

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global journaler_prefetch_periods 10
ceph config get global journaler_prefetch_periods
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `2`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global journaler_prefetch_periods
ceph -s
```

---

### journaler_prezero_periods

| | |
|---|---|
| 类型 | Uint · default `5` · **Advanced** |
| 表格 | [journaler.md#SP_journaler_prezero_periods](../../../config/global/journaler.md#SP_journaler_prezero_periods) |

**作用：** Number of striping periods to zero head of MDS journal write position

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global journaler_prezero_periods 5
ceph config get global journaler_prezero_periods
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `2`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global journaler_prezero_periods
ceph -s
```

---

### journaler_write_head_interval

| | |
|---|---|
| 类型 | Int · default `15` · **Advanced** |
| 表格 | [journaler.md#SP_journaler_write_head_interval](../../../config/global/journaler.md#SP_journaler_write_head_interval) |

**作用：** Interval in seconds between journal header updates (to help bound replay time)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global journaler_write_head_interval 15
ceph config get global journaler_write_head_interval
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `15` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global journaler_write_head_interval
ceph -s
```

---


[← 概览](../OVERVIEW.md)
