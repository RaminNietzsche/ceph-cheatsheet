# Cache agent

OSD 配置深度指南 — 7 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [osd_agent_delay_time](#osd_agent_delay_time) | `5` | Advanced | 性能 |
| [osd_agent_hist_halflife](#osd_agent_hist_halflife) | `1000` | Advanced | 性能 |
| [osd_agent_max_low_ops](#osd_agent_max_low_ops) | `2` | Advanced | 性能 |
| [osd_agent_max_ops](#osd_agent_max_ops) | `4` | Advanced | 性能 |
| [osd_agent_min_evict_effort](#osd_agent_min_evict_effort) | `0.1` | Advanced | 性能 |
| [osd_agent_quantize_effort](#osd_agent_quantize_effort) | `0.1` | Advanced | 性能 |
| [osd_agent_slop](#osd_agent_slop) | `0.02` | Advanced | 性能 |

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

### osd_agent_delay_time

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [osd.md#SP_osd_agent_delay_time](../../../config/osd/osd.md#SP_osd_agent_delay_time) |

**作用：** how long agent should sleep if it has no work to do

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_agent_delay_time 5
ceph config get osd osd_agent_delay_time
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_agent_delay_time
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_agent_hist_halflife

| | |
|---|---|
| 类型 | Int · default `1000` · **Advanced** |
| 表格 | [osd.md#SP_osd_agent_hist_halflife](../../../config/osd/osd.md#SP_osd_agent_hist_halflife) |

**作用：** halflife of agent atime and temp histograms

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_agent_hist_halflife 1000
ceph config get osd osd_agent_hist_halflife
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_agent_hist_halflife
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_agent_max_low_ops

| | |
|---|---|
| 类型 | Int · default `2` · **Advanced** |
| 表格 | [osd.md#SP_osd_agent_max_low_ops](../../../config/osd/osd.md#SP_osd_agent_max_low_ops) |

**作用：** maximum concurrent low-priority tiering operations for tiering agent

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_agent_max_low_ops 2
ceph config get osd osd_agent_max_low_ops
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_agent_max_low_ops
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_agent_max_ops

| | |
|---|---|
| 类型 | Int · default `4` · **Advanced** |
| 表格 | [osd.md#SP_osd_agent_max_ops](../../../config/osd/osd.md#SP_osd_agent_max_ops) |

**作用：** maximum concurrent tiering operations for tiering agent

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_agent_max_ops 4
ceph config get osd osd_agent_max_ops
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `4` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_agent_max_ops
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_agent_min_evict_effort

| | |
|---|---|
| 类型 | Float · default `0.1` · **Advanced** |
| 表格 | [osd.md#SP_osd_agent_min_evict_effort](../../../config/osd/osd.md#SP_osd_agent_min_evict_effort) |

**作用：** minimum effort to expend evicting clean objects

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_agent_min_evict_effort 0.1
ceph config get osd osd_agent_min_evict_effort
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `0.99`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_agent_min_evict_effort
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_agent_quantize_effort

| | |
|---|---|
| 类型 | Float · default `0.1` · **Advanced** |
| 表格 | [osd.md#SP_osd_agent_quantize_effort](../../../config/osd/osd.md#SP_osd_agent_quantize_effort) |

**作用：** size of quantize unit for eviction effort

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_agent_quantize_effort 0.1
ceph config get osd osd_agent_quantize_effort
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_agent_quantize_effort
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_agent_slop

| | |
|---|---|
| 类型 | Float · default `0.02` · **Advanced** |
| 表格 | [osd.md#SP_osd_agent_slop](../../../config/osd/osd.md#SP_osd_agent_slop) |

**作用：** slop factor to avoid switching tiering flush and eviction mode

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_agent_slop 0.02
ceph config get osd osd_agent_slop
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.02` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_agent_slop
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← 概览](../OVERVIEW.md)
