# Mgr

Global 配置深度指南 — 11 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mgr_client_service_daemon_unregister_timeout](#mgr_client_service_daemon_unregister_timeout) | `1` | Dev | 开发 |
| [mgr_connect_retry_interval](#mgr_connect_retry_interval) | `1` | Dev | 开发 |
| [mgr_enable_op_tracker](#mgr_enable_op_tracker) | `True` | Advanced | 策略 |
| [mgr_map_cache_enabled](#mgr_map_cache_enabled) | `True` | Dev | 开发 |
| [mgr_num_op_tracker_shard](#mgr_num_op_tracker_shard) | `32` | Advanced | 性能 |
| [mgr_op_complaint_time](#mgr_op_complaint_time) | `30` | Advanced | 性能 |
| [mgr_op_history_duration](#mgr_op_history_duration) | `600` | Advanced | 性能 |
| [mgr_op_history_size](#mgr_op_history_size) | `20` | Advanced | 性能 |
| [mgr_op_history_slow_op_size](#mgr_op_history_slow_op_size) | `20` | Advanced | 性能 |
| [mgr_op_history_slow_op_threshold](#mgr_op_history_slow_op_threshold) | `10` | Advanced | 性能 |
| [mgr_op_log_threshold](#mgr_op_log_threshold) | `5` | Advanced | 性能 |

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

### mgr_client_service_daemon_unregister_timeout

| | |
|---|---|
| 类型 | Float · default `1` · **Dev** |
| 表格 | [mgr.md#SP_mgr_client_service_daemon_unregister_timeout](../../../config/global/mgr.md#SP_mgr_client_service_daemon_unregister_timeout) |

**作用：** Time to wait during shutdown to deregister a service with the Manager

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mgr mgr_client_service_daemon_unregister_timeout 1
ceph config get mgr mgr_client_service_daemon_unregister_timeout
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mgr_connect_retry_interval

| | |
|---|---|
| 类型 | Float · default `1` · **Dev** |
| 表格 | [mgr.md#SP_mgr_connect_retry_interval](../../../config/global/mgr.md#SP_mgr_connect_retry_interval) |

**作用：** Manager reconnect retry interval

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mgr mgr_connect_retry_interval 1
ceph config get mgr mgr_connect_retry_interval
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mgr_enable_op_tracker

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_enable_op_tracker](../../../config/global/mgr.md#SP_mgr_enable_op_tracker) |

**作用：** Enable / disable the Manager op tracker

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mgr mgr_enable_op_tracker false
ceph config get mgr mgr_enable_op_tracker
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_enable_op_tracker
ceph -s
ceph mgr stat
```

---

### mgr_map_cache_enabled

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [mgr.md#SP_mgr_map_cache_enabled](../../../config/global/mgr.md#SP_mgr_map_cache_enabled) |

**作用：** Enable the manager's map cache for API calls

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mgr mgr_map_cache_enabled false
ceph config get mgr mgr_map_cache_enabled
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mgr_num_op_tracker_shard

| | |
|---|---|
| 类型 | Uint · default `32` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_num_op_tracker_shard](../../../config/global/mgr.md#SP_mgr_num_op_tracker_shard) |

**作用：** The number of shards for Manager ops

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mgr mgr_num_op_tracker_shard 32
ceph config get mgr mgr_num_op_tracker_shard
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `32` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_num_op_tracker_shard
ceph -s
ceph mgr stat
```

---

### mgr_op_complaint_time

| | |
|---|---|
| 类型 | Float · default `30` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_op_complaint_time](../../../config/global/mgr.md#SP_mgr_op_complaint_time) |

**作用：** A Manager operation becomes complaint-worthy after the specified number of seconds have elapsed.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mgr mgr_op_complaint_time 30
ceph config get mgr mgr_op_complaint_time
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_op_complaint_time
ceph -s
ceph mgr stat
```

---

### mgr_op_history_duration

| | |
|---|---|
| 类型 | Uint · default `600` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_op_history_duration](../../../config/global/mgr.md#SP_mgr_op_history_duration) |

**作用：** The oldest completed Manager operation to track.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mgr mgr_op_history_duration 600
ceph config get mgr mgr_op_history_duration
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `600` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_op_history_duration
ceph -s
ceph mgr stat
```

---

### mgr_op_history_size

| | |
|---|---|
| 类型 | Uint · default `20` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_op_history_size](../../../config/global/mgr.md#SP_mgr_op_history_size) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mgr mgr_op_history_size 20
ceph config get mgr mgr_op_history_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `20` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_op_history_size
ceph -s
ceph mgr stat
```

---

### mgr_op_history_slow_op_size

| | |
|---|---|
| 类型 | Uint · default `20` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_op_history_slow_op_size](../../../config/global/mgr.md#SP_mgr_op_history_slow_op_size) |

**作用：** Max number of slow Manager ops to track

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mgr mgr_op_history_slow_op_size 20
ceph config get mgr mgr_op_history_slow_op_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `20` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_op_history_slow_op_size
ceph -s
ceph mgr stat
```

---

### mgr_op_history_slow_op_threshold

| | |
|---|---|
| 类型 | Float · default `10` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_op_history_slow_op_threshold](../../../config/global/mgr.md#SP_mgr_op_history_slow_op_threshold) |

**作用：** Duration of a Manager op to be considered as a historical slow op

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mgr mgr_op_history_slow_op_threshold 10
ceph config get mgr mgr_op_history_slow_op_threshold
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_op_history_slow_op_threshold
ceph -s
ceph mgr stat
```

---

### mgr_op_log_threshold

| | |
|---|---|
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_op_log_threshold](../../../config/global/mgr.md#SP_mgr_op_log_threshold) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mgr mgr_op_log_threshold 5
ceph config get mgr mgr_op_log_threshold
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_op_log_threshold
ceph -s
ceph mgr stat
```

---


[← 概览](../OVERVIEW.md)
