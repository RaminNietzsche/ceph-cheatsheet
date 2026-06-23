# Quorum & Paxos

MON 配置深度指南 — 14 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mon_accept_timeout_factor](#mon_accept_timeout_factor) | `2` | Advanced | 性能 |
| [mon_election_default_strategy](#mon_election_default_strategy) | `1` | Advanced | 性能 |
| [mon_election_timeout](#mon_election_timeout) | `5` | Advanced | 性能 |
| [paxos_kill_at](#paxos_kill_at) | `0` | Dev | 开发 |
| [paxos_max_join_drift](#paxos_max_join_drift) | `10` | Advanced | 性能 |
| [paxos_min](#paxos_min) | `500` | Advanced | 性能 |
| [paxos_min_wait](#paxos_min_wait) | `0.05` | Advanced | 性能 |
| [paxos_propose_interval](#paxos_propose_interval) | `1` | Advanced | 性能 |
| [paxos_service_trim_max](#paxos_service_trim_max) | `500` | Advanced | 性能 |
| [paxos_service_trim_max_multiplier](#paxos_service_trim_max_multiplier) | `20` | Advanced | 性能 |
| [paxos_service_trim_min](#paxos_service_trim_min) | `250` | Advanced | 性能 |
| [paxos_stash_full_interval](#paxos_stash_full_interval) | `25` | Advanced | 性能 |
| [paxos_trim_max](#paxos_trim_max) | `500` | Advanced | 性能 |
| [paxos_trim_min](#paxos_trim_min) | `250` | Advanced | 性能 |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_accept_timeout_factor

| | |
|---|---|
| 类型 | Float · default `2` · **Advanced** |
| 表格 | [mon.md#SP_mon_accept_timeout_factor](../../../config/mon/mon.md#SP_mon_accept_timeout_factor) |

**作用：** multiple of mon_lease for follower mons to accept proposed state changes before calling a new election

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_accept_timeout_factor 2
ceph config get mon mon_accept_timeout_factor
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_accept_timeout_factor
ceph -s
ceph mon stat
```

---

### mon_election_default_strategy

| | |
|---|---|
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [mon.md#SP_mon_election_default_strategy](../../../config/mon/mon.md#SP_mon_election_default_strategy) |

**作用：** The election strategy to set when constructing the first monmap.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_election_default_strategy 1
ceph config get mon mon_election_default_strategy
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `3`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_election_default_strategy
ceph -s
ceph mon stat
```

---

### mon_election_timeout

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [mon.md#SP_mon_election_timeout](../../../config/mon/mon.md#SP_mon_election_timeout) |

**作用：** maximum time for a mon election (seconds)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_election_timeout 5
ceph config get mon mon_election_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_election_timeout
ceph -s
ceph mon stat
```

---

### paxos_kill_at

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [paxos.md#SP_paxos_kill_at](../../../config/mon/paxos.md#SP_paxos_kill_at) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon paxos_kill_at 64
ceph config get mon paxos_kill_at
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### paxos_max_join_drift

| | |
|---|---|
| 类型 | Int · default `10` · **Advanced** |
| 表格 | [paxos.md#SP_paxos_max_join_drift](../../../config/mon/paxos.md#SP_paxos_max_join_drift) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon paxos_max_join_drift 10
ceph config get mon paxos_max_join_drift
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon paxos_max_join_drift
ceph -s
ceph mon stat
```

---

### paxos_min

| | |
|---|---|
| 类型 | Int · default `500` · **Advanced** |
| 表格 | [paxos.md#SP_paxos_min](../../../config/mon/paxos.md#SP_paxos_min) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon paxos_min 500
ceph config get mon paxos_min
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `500` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon paxos_min
ceph -s
ceph mon stat
```

---

### paxos_min_wait

| | |
|---|---|
| 类型 | Float · default `0.05` · **Advanced** |
| 表格 | [paxos.md#SP_paxos_min_wait](../../../config/mon/paxos.md#SP_paxos_min_wait) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon paxos_min_wait 0.05
ceph config get mon paxos_min_wait
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.05` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon paxos_min_wait
ceph -s
ceph mon stat
```

---

### paxos_propose_interval

| | |
|---|---|
| 类型 | Float · default `1` · **Advanced** |
| 表格 | [paxos.md#SP_paxos_propose_interval](../../../config/mon/paxos.md#SP_paxos_propose_interval) |

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon paxos_propose_interval 1
ceph config get mon paxos_propose_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon paxos_propose_interval
ceph -s
ceph mon stat
```

---

### paxos_service_trim_max

| | |
|---|---|
| 类型 | Uint · default `500` · **Advanced** |
| 表格 | [paxos.md#SP_paxos_service_trim_max](../../../config/mon/paxos.md#SP_paxos_service_trim_max) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon paxos_service_trim_max 500
ceph config get mon paxos_service_trim_max
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `500` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon paxos_service_trim_max
ceph -s
ceph mon stat
```

---

### paxos_service_trim_max_multiplier

| | |
|---|---|
| 类型 | Uint · default `20` · **Advanced** |
| 表格 | [paxos.md#SP_paxos_service_trim_max_multiplier](../../../config/mon/paxos.md#SP_paxos_service_trim_max_multiplier) |

**作用：** factor by which paxos_service_trim_max will be multiplied to get a new upper bound when trim sizes are high (0 disables it)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon paxos_service_trim_max_multiplier 20
ceph config get mon paxos_service_trim_max_multiplier
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `20` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon paxos_service_trim_max_multiplier
ceph -s
ceph mon stat
```

---

### paxos_service_trim_min

| | |
|---|---|
| 类型 | Uint · default `250` · **Advanced** |
| 表格 | [paxos.md#SP_paxos_service_trim_min](../../../config/mon/paxos.md#SP_paxos_service_trim_min) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon paxos_service_trim_min 250
ceph config get mon paxos_service_trim_min
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `250` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon paxos_service_trim_min
ceph -s
ceph mon stat
```

---

### paxos_stash_full_interval

| | |
|---|---|
| 类型 | Int · default `25` · **Advanced** |
| 表格 | [paxos.md#SP_paxos_stash_full_interval](../../../config/mon/paxos.md#SP_paxos_stash_full_interval) |

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon paxos_stash_full_interval 25
ceph config get mon paxos_stash_full_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `25` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon paxos_stash_full_interval
ceph -s
ceph mon stat
```

---

### paxos_trim_max

| | |
|---|---|
| 类型 | Int · default `500` · **Advanced** |
| 表格 | [paxos.md#SP_paxos_trim_max](../../../config/mon/paxos.md#SP_paxos_trim_max) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon paxos_trim_max 500
ceph config get mon paxos_trim_max
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `500` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon paxos_trim_max
ceph -s
ceph mon stat
```

---

### paxos_trim_min

| | |
|---|---|
| 类型 | Int · default `250` · **Advanced** |
| 表格 | [paxos.md#SP_paxos_trim_min](../../../config/mon/paxos.md#SP_paxos_trim_min) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon paxos_trim_min 250
ceph config get mon paxos_trim_min
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `250` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon paxos_trim_min
ceph -s
ceph mon stat
```

---


[← 概览](../OVERVIEW.md)
