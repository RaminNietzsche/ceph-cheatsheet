# Objecter

Global 配置深度指南 — 8 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [objecter_completion_locks_per_session](#objecter_completion_locks_per_session) | `32` | Dev | 开发 |
| [objecter_debug_inject_relock_delay](#objecter_debug_inject_relock_delay) | `False` | Dev | 开发 |
| [objecter_inflight_op_bytes](#objecter_inflight_op_bytes) | `100_M` | Advanced | 性能 |
| [objecter_inflight_ops](#objecter_inflight_ops) | `1_K` | Advanced | 性能 |
| [objecter_inject_no_watch_ping](#objecter_inject_no_watch_ping) | `False` | Dev | 开发 |
| [objecter_retry_writes_after_first_reply](#objecter_retry_writes_after_first_reply) | `False` | Dev | 开发 |
| [objecter_tick_interval](#objecter_tick_interval) | `5` | Dev | 开发 |
| [objecter_timeout](#objecter_timeout) | `10` | Advanced | 性能 |

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

### objecter_completion_locks_per_session

| | |
|---|---|
| 类型 | Uint · default `32` · **Dev** |
| 表格 | [objecter.md#SP_objecter_completion_locks_per_session](../../../config/global/objecter.md#SP_objecter_completion_locks_per_session) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global objecter_completion_locks_per_session 32
ceph config get global objecter_completion_locks_per_session
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`32`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### objecter_debug_inject_relock_delay

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [objecter.md#SP_objecter_debug_inject_relock_delay](../../../config/global/objecter.md#SP_objecter_debug_inject_relock_delay) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global objecter_debug_inject_relock_delay true
ceph config get global objecter_debug_inject_relock_delay
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### objecter_inflight_op_bytes

| | |
|---|---|
| 类型 | Size · default `100_M` · **Advanced** |
| 表格 | [objecter.md#SP_objecter_inflight_op_bytes](../../../config/global/objecter.md#SP_objecter_inflight_op_bytes) |

**作用：** Max in-flight data in bytes (both directions)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global objecter_inflight_op_bytes 100_M
ceph config get global objecter_inflight_op_bytes
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `100_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global objecter_inflight_op_bytes
ceph -s
```

---

### objecter_inflight_ops

| | |
|---|---|
| 类型 | Uint · default `1_K` · **Advanced** |
| 表格 | [objecter.md#SP_objecter_inflight_ops](../../../config/global/objecter.md#SP_objecter_inflight_ops) |

**作用：** Max in-flight operations

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global objecter_inflight_ops 1_K
ceph config get global objecter_inflight_ops
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global objecter_inflight_ops
ceph -s
```

---

### objecter_inject_no_watch_ping

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [objecter.md#SP_objecter_inject_no_watch_ping](../../../config/global/objecter.md#SP_objecter_inject_no_watch_ping) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global objecter_inject_no_watch_ping true
ceph config get global objecter_inject_no_watch_ping
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### objecter_retry_writes_after_first_reply

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [objecter.md#SP_objecter_retry_writes_after_first_reply](../../../config/global/objecter.md#SP_objecter_retry_writes_after_first_reply) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global objecter_retry_writes_after_first_reply true
ceph config get global objecter_retry_writes_after_first_reply
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### objecter_tick_interval

| | |
|---|---|
| 类型 | Float · default `5` · **Dev** |
| 表格 | [objecter.md#SP_objecter_tick_interval](../../../config/global/objecter.md#SP_objecter_tick_interval) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global objecter_tick_interval 5
ceph config get global objecter_tick_interval
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`5`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### objecter_timeout

| | |
|---|---|
| 类型 | Float · default `10` · **Advanced** |
| 表格 | [objecter.md#SP_objecter_timeout](../../../config/global/objecter.md#SP_objecter_timeout) |

**作用：** Seconds before in-flight op is considered laggy and we query the Monitors for the latest OSDMap

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global objecter_timeout 10
ceph config get global objecter_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global objecter_timeout
ceph -s
```

---


[← 概览](../OVERVIEW.md)
