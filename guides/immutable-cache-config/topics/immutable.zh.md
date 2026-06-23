# Immutable object cache

Immutable cache 配置深度指南 — 13 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/immutable-object-cache/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [immutable_object_cache_client_dedicated_thread_num](#immutable_object_cache_client_dedicated_thread_num) | `2` | Advanced | Performance |
| [immutable_object_cache_max_inflight_ops](#immutable_object_cache_max_inflight_ops) | `128` | Advanced | Performance |
| [immutable_object_cache_max_size](#immutable_object_cache_max_size) | `1_G` | Advanced | Performance |
| [immutable_object_cache_path](#immutable_object_cache_path) | `/tmp/ceph_immutable_object_cache` | Advanced | Capacity |
| [immutable_object_cache_qos_bps_burst](#immutable_object_cache_qos_bps_burst) | `0` | Advanced | Performance |
| [immutable_object_cache_qos_bps_burst_seconds](#immutable_object_cache_qos_bps_burst_seconds) | `1` | Advanced | Performance |
| [immutable_object_cache_qos_bps_limit](#immutable_object_cache_qos_bps_limit) | `0` | Advanced | Performance |
| [immutable_object_cache_qos_iops_burst](#immutable_object_cache_qos_iops_burst) | `0` | Advanced | Performance |
| [immutable_object_cache_qos_iops_burst_seconds](#immutable_object_cache_qos_iops_burst_seconds) | `1` | Advanced | Performance |
| [immutable_object_cache_qos_iops_limit](#immutable_object_cache_qos_iops_limit) | `0` | Advanced | Performance |
| [immutable_object_cache_qos_schedule_tick_min](#immutable_object_cache_qos_schedule_tick_min) | `50` | Advanced | Performance |
| [immutable_object_cache_sock](#immutable_object_cache_sock) | `/var/run/ceph/immutable_object_cache_sock` | Advanced | Performance |
| [immutable_object_cache_watermark](#immutable_object_cache_watermark) | `0.9` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. immutable-object-cache
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### immutable_object_cache_client_dedicated_thread_num

| | |
|---|---|
| 类型 | Uint · default `2` · **Advanced** |
| 表格 | [immutable.md#SP_immutable_object_cache_client_dedicated_thread_num](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_client_dedicated_thread_num) |

**作用：** immutable object cache client dedicated thread number

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set immutable_object_cache immutable_object_cache_client_dedicated_thread_num 2
ceph config get immutable_object_cache immutable_object_cache_client_dedicated_thread_num
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get immutable_object_cache immutable_object_cache_client_dedicated_thread_num
ceph -s
```

---

### immutable_object_cache_max_inflight_ops

| | |
|---|---|
| 类型 | Uint · default `128` · **Advanced** |
| 表格 | [immutable.md#SP_immutable_object_cache_max_inflight_ops](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_max_inflight_ops) |

**作用：** max inflight promoting requests for immutable object cache daemon

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set immutable_object_cache immutable_object_cache_max_inflight_ops 128
ceph config get immutable_object_cache immutable_object_cache_max_inflight_ops
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `128` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get immutable_object_cache immutable_object_cache_max_inflight_ops
ceph -s
```

---

### immutable_object_cache_max_size

| | |
|---|---|
| 类型 | Size · default `1_G` · **Advanced** |
| 表格 | [immutable.md#SP_immutable_object_cache_max_size](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_max_size) |

**作用：** max immutable object cache data size

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set immutable_object_cache immutable_object_cache_max_size 1_G
ceph config get immutable_object_cache immutable_object_cache_max_size
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1_G` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get immutable_object_cache immutable_object_cache_max_size
ceph -s
```

---

### immutable_object_cache_path

| | |
|---|---|
| 类型 | Str · default `/tmp/ceph_immutable_object_cache` · **Advanced** |
| 表格 | [immutable.md#SP_immutable_object_cache_path](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_path) |

**作用：** immutable object cache data dir

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set immutable_object_cache immutable_object_cache_path "/tmp/ceph_immutable_object_cache"
ceph config get immutable_object_cache immutable_object_cache_path
```

**寻找最优值：**

**调优模型：** Capacity

1. 以 `/tmp/ceph_immutable_object_cache` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get immutable_object_cache immutable_object_cache_path
ceph -s
```

---

### immutable_object_cache_qos_bps_burst

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [immutable.md#SP_immutable_object_cache_qos_bps_burst](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_bps_burst) |

**作用：** the desired burst limit of immutable object cache IO bytes

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_bps_burst 64
ceph config get immutable_object_cache immutable_object_cache_qos_bps_burst
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get immutable_object_cache immutable_object_cache_qos_bps_burst
ceph -s
```

---

### immutable_object_cache_qos_bps_burst_seconds

| | |
|---|---|
| 类型 | Secs · default `1` · **Advanced** |
| 表格 | [immutable.md#SP_immutable_object_cache_qos_bps_burst_seconds](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_bps_burst_seconds) |

**作用：** the desired burst duration in seconds of immutable object cache IO bytes

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_bps_burst_seconds 1
ceph config get immutable_object_cache immutable_object_cache_qos_bps_burst_seconds
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get immutable_object_cache immutable_object_cache_qos_bps_burst_seconds
ceph -s
```

---

### immutable_object_cache_qos_bps_limit

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [immutable.md#SP_immutable_object_cache_qos_bps_limit](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_bps_limit) |

**作用：** the desired immutable object cache IO bytes limit per second

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_bps_limit 64
ceph config get immutable_object_cache immutable_object_cache_qos_bps_limit
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get immutable_object_cache immutable_object_cache_qos_bps_limit
ceph -s
```

---

### immutable_object_cache_qos_iops_burst

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [immutable.md#SP_immutable_object_cache_qos_iops_burst](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_iops_burst) |

**作用：** the desired burst limit of immutable object cache IO operations

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_iops_burst 64
ceph config get immutable_object_cache immutable_object_cache_qos_iops_burst
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get immutable_object_cache immutable_object_cache_qos_iops_burst
ceph -s
```

---

### immutable_object_cache_qos_iops_burst_seconds

| | |
|---|---|
| 类型 | Secs · default `1` · **Advanced** |
| 表格 | [immutable.md#SP_immutable_object_cache_qos_iops_burst_seconds](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_iops_burst_seconds) |

**作用：** the desired burst duration in seconds of immutable object cache IO operations

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_iops_burst_seconds 1
ceph config get immutable_object_cache immutable_object_cache_qos_iops_burst_seconds
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get immutable_object_cache immutable_object_cache_qos_iops_burst_seconds
ceph -s
```

---

### immutable_object_cache_qos_iops_limit

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [immutable.md#SP_immutable_object_cache_qos_iops_limit](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_iops_limit) |

**作用：** the desired immutable object cache IO operations limit per second

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_iops_limit 64
ceph config get immutable_object_cache immutable_object_cache_qos_iops_limit
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get immutable_object_cache immutable_object_cache_qos_iops_limit
ceph -s
```

---

### immutable_object_cache_qos_schedule_tick_min

| | |
|---|---|
| 类型 | Millisecs · default `50` · **Advanced** |
| 表格 | [immutable.md#SP_immutable_object_cache_qos_schedule_tick_min](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_schedule_tick_min) |

**作用：** minimum schedule tick for immutable object cache

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_schedule_tick_min 50
ceph config get immutable_object_cache immutable_object_cache_qos_schedule_tick_min
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `50` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get immutable_object_cache immutable_object_cache_qos_schedule_tick_min
ceph -s
```

---

### immutable_object_cache_sock

| | |
|---|---|
| 类型 | Str · default `/var/run/ceph/immutable_object_cache_sock` · **Advanced** |
| 表格 | [immutable.md#SP_immutable_object_cache_sock](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_sock) |

**作用：** immutable object cache domain socket

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set immutable_object_cache immutable_object_cache_sock "/var/run/ceph/immutable_object_cache_sock"
ceph config get immutable_object_cache immutable_object_cache_sock
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `/var/run/ceph/immutable_object_cache_sock` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get immutable_object_cache immutable_object_cache_sock
ceph -s
```

---

### immutable_object_cache_watermark

| | |
|---|---|
| 类型 | Float · default `0.9` · **Advanced** |
| 表格 | [immutable.md#SP_immutable_object_cache_watermark](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_watermark) |

**作用：** immutable object cache water mark

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set immutable_object_cache immutable_object_cache_watermark 0.9
ceph config get immutable_object_cache immutable_object_cache_watermark
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.9` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get immutable_object_cache immutable_object_cache_watermark
ceph -s
```

---


[← 概览](../OVERVIEW.md)
