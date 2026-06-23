# Crimson OSD

Crimson 配置深度指南 — 14 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/crimson/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [crimson_allow_pg_split](#crimson_allow_pg_split) | `True` | Advanced | 策略 |
| [crimson_bluestore_cpu_set](#crimson_bluestore_cpu_set) | `(empty)` | Advanced | 性能 |
| [crimson_bluestore_num_threads](#crimson_bluestore_num_threads) | `6` | Advanced | 性能 |
| [crimson_cpu_num](#crimson_cpu_num) | `0` | Advanced | 性能 |
| [crimson_cpu_set](#crimson_cpu_set) | `(empty)` | Advanced | 性能 |
| [crimson_memory](#crimson_memory) | `0` | Advanced | 性能 |
| [crimson_osd_obc_lru_size](#crimson_osd_obc_lru_size) | `512` | Advanced | 性能 |
| [crimson_osd_scheduler_concurrency](#crimson_osd_scheduler_concurrency) | `0` | Advanced | 性能 |
| [crimson_osd_stat_interval](#crimson_osd_stat_interval) | `0` | Advanced | 性能 |
| [crimson_poll_mode](#crimson_poll_mode) | `False` | Advanced | 性能 |
| [crimson_reactor_backend](#crimson_reactor_backend) | `(empty)` | Advanced | 性能 |
| [crimson_reactor_idle_poll_time_us](#crimson_reactor_idle_poll_time_us) | `200` | Advanced | 性能 |
| [crimson_reactor_io_latency_goal_ms](#crimson_reactor_io_latency_goal_ms) | `0` | Advanced | 性能 |
| [crimson_reactor_task_quota_ms](#crimson_reactor_task_quota_ms) | `0.5` | Advanced | 性能 |

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
ceph config get <daemon> <option>  # e.g. crimson
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### crimson_allow_pg_split

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [crimson.md#SP_crimson_allow_pg_split](../../../config/crimson/crimson.md#SP_crimson_allow_pg_split) |

**作用：** Allow Crimson pools to increase their PG count (split)

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd crimson_allow_pg_split false
ceph config get osd crimson_allow_pg_split
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd crimson_allow_pg_split
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_bluestore_cpu_set

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [crimson.md#SP_crimson_bluestore_cpu_set](../../../config/crimson/crimson.md#SP_crimson_bluestore_cpu_set) |

**作用：** CPU cores on which POSIX threads alienized to seastar will run in cpuset(7) format

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd crimson_bluestore_cpu_set "example"
ceph config get osd crimson_bluestore_cpu_set
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd crimson_bluestore_cpu_set
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_bluestore_num_threads

| | |
|---|---|
| 类型 | Uint · default `6` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [crimson.md#SP_crimson_bluestore_num_threads](../../../config/crimson/crimson.md#SP_crimson_bluestore_num_threads) |

**作用：** The number of POSIX threads alienized to seastar for serving Bluestore

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd crimson_bluestore_num_threads 6
ceph config get osd crimson_bluestore_num_threads
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `6` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd crimson_bluestore_num_threads
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_cpu_num

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [crimson.md#SP_crimson_cpu_num](../../../config/crimson/crimson.md#SP_crimson_cpu_num) |

**作用：** The number of CPUs to use for serving seastar reactors per OSD without CPU pinning.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd crimson_cpu_num 64
ceph config get osd crimson_cpu_num
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `32`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd crimson_cpu_num
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_cpu_set

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [crimson.md#SP_crimson_cpu_set](../../../config/crimson/crimson.md#SP_crimson_cpu_set) |

**作用：** CPU cores on which seastar reactor threads will run in cpuset(7) format per OSD with pinning.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd crimson_cpu_set "example"
ceph config get osd crimson_cpu_set
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd crimson_cpu_set
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_memory

| | |
|---|---|
| 类型 | Size · default `0` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [crimson.md#SP_crimson_memory](../../../config/crimson/crimson.md#SP_crimson_memory) |

**作用：** Total memory to use for the seastar allocator per OSD.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd crimson_memory 64
ceph config get osd crimson_memory
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd crimson_memory
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_osd_obc_lru_size

| | |
|---|---|
| 类型 | Uint · default `512` · **Advanced** |
| 表格 | [crimson.md#SP_crimson_osd_obc_lru_size](../../../config/crimson/crimson.md#SP_crimson_osd_obc_lru_size) |

**作用：** Number of obcs to cache

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd crimson_osd_obc_lru_size 512
ceph config get osd crimson_osd_obc_lru_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `512` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd crimson_osd_obc_lru_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_osd_scheduler_concurrency

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [crimson.md#SP_crimson_osd_scheduler_concurrency](../../../config/crimson/crimson.md#SP_crimson_osd_scheduler_concurrency) |

**作用：** The maximum number concurrent IO operations, 0 for unlimited

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd crimson_osd_scheduler_concurrency 64
ceph config get osd crimson_osd_scheduler_concurrency
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd crimson_osd_scheduler_concurrency
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_osd_stat_interval

| | |
|---|---|
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [crimson.md#SP_crimson_osd_stat_interval](../../../config/crimson/crimson.md#SP_crimson_osd_stat_interval) |

**作用：** Report OSD status periodically in seconds, 0 to disable

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd crimson_osd_stat_interval 64
ceph config get osd crimson_osd_stat_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd crimson_osd_stat_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_poll_mode

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [crimson.md#SP_crimson_poll_mode](../../../config/crimson/crimson.md#SP_crimson_poll_mode) |

**作用：** Let the seastar reactor poll continuously without sleeping at the expense of 100% cpu usage.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd crimson_poll_mode true
ceph config get osd crimson_poll_mode
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd crimson_poll_mode
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_reactor_backend

| | |
|---|---|
| 类型 | Str · enum: ["io_uring", "linux-aio", "epoll"] · default `(empty)` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [crimson.md#SP_crimson_reactor_backend](../../../config/crimson/crimson.md#SP_crimson_reactor_backend) |

**作用：** Select which Seastar's internal reactor implementation

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd crimson_reactor_backend "example"
ceph config get osd crimson_reactor_backend
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd crimson_reactor_backend
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_reactor_idle_poll_time_us

| | |
|---|---|
| 类型 | Uint · default `200` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [crimson.md#SP_crimson_reactor_idle_poll_time_us](../../../config/crimson/crimson.md#SP_crimson_reactor_idle_poll_time_us) |

**作用：** Seastar's reactor idle polling time (ms) before going back to sleep.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd crimson_reactor_idle_poll_time_us 200
ceph config get osd crimson_reactor_idle_poll_time_us
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `200` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd crimson_reactor_idle_poll_time_us
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_reactor_io_latency_goal_ms

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [crimson.md#SP_crimson_reactor_io_latency_goal_ms](../../../config/crimson/crimson.md#SP_crimson_reactor_io_latency_goal_ms) |

**作用：** The maximum time (ms) Seastar's reactor IO operations must take. If not set(0 mean not set), defaults to 1.5 * crimson_reactor_task_quota_ms

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd crimson_reactor_io_latency_goal_ms 0
ceph config get osd crimson_reactor_io_latency_goal_ms
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd crimson_reactor_io_latency_goal_ms
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_reactor_task_quota_ms

| | |
|---|---|
| 类型 | Float · default `0.5` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [crimson.md#SP_crimson_reactor_task_quota_ms](../../../config/crimson/crimson.md#SP_crimson_reactor_task_quota_ms) |

**作用：** The maximum time (ms) Seastar reactors will wait between polls.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd crimson_reactor_task_quota_ms 0.5
ceph config get osd crimson_reactor_task_quota_ms
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd crimson_reactor_task_quota_ms
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← 概览](../OVERVIEW.md)
