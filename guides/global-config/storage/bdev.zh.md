# Bdev

Global 配置深度指南 — 31 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [bdev_aio](#bdev_aio) | `True` | Advanced | Performance |
| [bdev_aio_max_queue_depth](#bdev_aio_max_queue_depth) | `1024` | Advanced | Performance |
| [bdev_aio_poll_ms](#bdev_aio_poll_ms) | `250` | Advanced | Performance |
| [bdev_aio_reap_max](#bdev_aio_reap_max) | `16` | Advanced | Performance |
| [bdev_aio_submit_retry_initial_delay_us](#bdev_aio_submit_retry_initial_delay_us) | `125` | Advanced | Performance |
| [bdev_aio_submit_retry_max](#bdev_aio_submit_retry_max) | `16` | Advanced | Performance |
| [bdev_async_discard](#bdev_async_discard) | `False` | Advanced | Performance |
| [bdev_async_discard_max_pending](#bdev_async_discard_max_pending) | `1000000` | Advanced | Performance |
| [bdev_async_discard_threads](#bdev_async_discard_threads) | `0` | Advanced | Performance |
| [bdev_block_size](#bdev_block_size) | `4_K` | Advanced | Performance |
| [bdev_debug_aio](#bdev_debug_aio) | `False` | Dev | Dev |
| [bdev_debug_aio_log_age](#bdev_debug_aio_log_age) | `5` | Dev | Dev |
| [bdev_debug_aio_suicide_timeout](#bdev_debug_aio_suicide_timeout) | `1_min` | Dev | Dev |
| [bdev_debug_discard_sleep](#bdev_debug_discard_sleep) | `0` | Dev | Dev |
| [bdev_debug_inflight_ios](#bdev_debug_inflight_ios) | `False` | Dev | Dev |
| [bdev_discard_max_bytes](#bdev_discard_max_bytes) | `10_G` | Advanced | Performance |
| [bdev_enable_discard](#bdev_enable_discard) | `False` | Advanced | Policy |
| [bdev_flock_retry](#bdev_flock_retry) | `3` | Advanced | Performance |
| [bdev_flock_retry_interval](#bdev_flock_retry_interval) | `0.1` | Advanced | Performance |
| [bdev_inject_crash](#bdev_inject_crash) | `0` | Dev | Dev |
| [bdev_inject_crash_flush_delay](#bdev_inject_crash_flush_delay) | `2` | Dev | Dev |
| [bdev_ioring](#bdev_ioring) | `False` | Advanced | Performance |
| [bdev_ioring_hipri](#bdev_ioring_hipri) | `False` | Advanced | Performance |
| [bdev_ioring_sqthread_poll](#bdev_ioring_sqthread_poll) | `False` | Advanced | Performance |
| [bdev_max_discard_length](#bdev_max_discard_length) | `2147483648` | Advanced | Performance |
| [bdev_nvme_unbind_from_kernel](#bdev_nvme_unbind_from_kernel) | `False` | Advanced | Performance |
| [bdev_read_buffer_alignment](#bdev_read_buffer_alignment) | `4_K` | Advanced | Performance |
| [bdev_read_preallocated_huge_buffers](#bdev_read_preallocated_huge_buffers) | `(empty)` | Advanced | Performance |
| [bdev_stalled_read_warn_lifetime](#bdev_stalled_read_warn_lifetime) | `86400` | Advanced | Performance |
| [bdev_stalled_read_warn_threshold](#bdev_stalled_read_warn_threshold) | `1` | Advanced | Performance |
| [bdev_type](#bdev_type) | `(empty)` | Advanced | Performance |

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

### bdev_aio

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_aio](../../../config/global/bdev.md#SP_bdev_aio) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global bdev_aio false
ceph config get global bdev_aio
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_aio
ceph -s
```

---

### bdev_aio_max_queue_depth

| | |
|---|---|
| 类型 | Int · default `1024` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_aio_max_queue_depth](../../../config/global/bdev.md#SP_bdev_aio_max_queue_depth) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bdev_aio_max_queue_depth 1024
ceph config get global bdev_aio_max_queue_depth
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1024` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_aio_max_queue_depth
ceph -s
```

---

### bdev_aio_poll_ms

| | |
|---|---|
| 类型 | Int · default `250` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_aio_poll_ms](../../../config/global/bdev.md#SP_bdev_aio_poll_ms) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bdev_aio_poll_ms 250
ceph config get global bdev_aio_poll_ms
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `250` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_aio_poll_ms
ceph -s
```

---

### bdev_aio_reap_max

| | |
|---|---|
| 类型 | Int · default `16` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_aio_reap_max](../../../config/global/bdev.md#SP_bdev_aio_reap_max) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bdev_aio_reap_max 16
ceph config get global bdev_aio_reap_max
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `16` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_aio_reap_max
ceph -s
```

---

### bdev_aio_submit_retry_initial_delay_us

| | |
|---|---|
| 类型 | Int · default `125` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_aio_submit_retry_initial_delay_us](../../../config/global/bdev.md#SP_bdev_aio_submit_retry_initial_delay_us) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bdev_aio_submit_retry_initial_delay_us 125
ceph config get global bdev_aio_submit_retry_initial_delay_us
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `125` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_aio_submit_retry_initial_delay_us
ceph -s
```

---

### bdev_aio_submit_retry_max

| | |
|---|---|
| 类型 | Int · default `16` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_aio_submit_retry_max](../../../config/global/bdev.md#SP_bdev_aio_submit_retry_max) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bdev_aio_submit_retry_max 16
ceph config get global bdev_aio_submit_retry_max
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `16` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_aio_submit_retry_max
ceph -s
```

---

### bdev_async_discard

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_async_discard](../../../config/global/bdev.md#SP_bdev_async_discard) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bdev_async_discard true
ceph config get global bdev_async_discard
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_async_discard
ceph -s
```

---

### bdev_async_discard_max_pending

| | |
|---|---|
| 类型 | Uint · default `1000000` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_async_discard_max_pending](../../../config/global/bdev.md#SP_bdev_async_discard_max_pending) |

**作用：** maximum number of pending discards

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bdev_async_discard_max_pending 1000000
ceph config get global bdev_async_discard_max_pending
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1000000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_async_discard_max_pending
ceph -s
```

---

### bdev_async_discard_threads

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_async_discard_threads](../../../config/global/bdev.md#SP_bdev_async_discard_threads) |

**作用：** Number of discard threads used to issue discards to the device

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bdev_async_discard_threads 64
ceph config get global bdev_async_discard_threads
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_async_discard_threads
ceph -s
```

---

### bdev_block_size

| | |
|---|---|
| 类型 | Size · default `4_K` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_block_size](../../../config/global/bdev.md#SP_bdev_block_size) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bdev_block_size 4_K
ceph config get global bdev_block_size
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `4_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_block_size
ceph -s
```

---

### bdev_debug_aio

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bdev.md#SP_bdev_debug_aio](../../../config/global/bdev.md#SP_bdev_debug_aio) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bdev_debug_aio true
ceph config get global bdev_debug_aio
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bdev_debug_aio_log_age

| | |
|---|---|
| 类型 | Float · default `5` · **Dev** |
| 表格 | [bdev.md#SP_bdev_debug_aio_log_age](../../../config/global/bdev.md#SP_bdev_debug_aio_log_age) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bdev_debug_aio_log_age 5
ceph config get global bdev_debug_aio_log_age
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`5`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bdev_debug_aio_suicide_timeout

| | |
|---|---|
| 类型 | Float · default `1_min` · **Dev** |
| 表格 | [bdev.md#SP_bdev_debug_aio_suicide_timeout](../../../config/global/bdev.md#SP_bdev_debug_aio_suicide_timeout) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bdev_debug_aio_suicide_timeout 1_min
ceph config get global bdev_debug_aio_suicide_timeout
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`1_min`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bdev_debug_discard_sleep

| | |
|---|---|
| 类型 | Uint · default `0` · **Dev** |
| 表格 | [bdev.md#SP_bdev_debug_discard_sleep](../../../config/global/bdev.md#SP_bdev_debug_discard_sleep) |

**作用：** A debugging tool to simulate slow discard operations by introducing a delay of `bdev_debug_discard_sleep` milliseconds

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bdev_debug_discard_sleep 64
ceph config get global bdev_debug_discard_sleep
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bdev_debug_inflight_ios

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [bdev.md#SP_bdev_debug_inflight_ios](../../../config/global/bdev.md#SP_bdev_debug_inflight_ios) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bdev_debug_inflight_ios true
ceph config get global bdev_debug_inflight_ios
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bdev_discard_max_bytes

| | |
|---|---|
| 类型 | Size · default `10_G` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_discard_max_bytes](../../../config/global/bdev.md#SP_bdev_discard_max_bytes) |

**作用：** Discard queue size in bytes that triggers health warning

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bdev_discard_max_bytes 10_G
ceph config get global bdev_discard_max_bytes
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10_G` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_discard_max_bytes
ceph -s
```

---

### bdev_enable_discard

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_enable_discard](../../../config/global/bdev.md#SP_bdev_enable_discard) |

**作用：** Enable OSD devices trimming during in runtime

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bdev_enable_discard true
ceph config get global bdev_enable_discard
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_enable_discard
ceph -s
```

---

### bdev_flock_retry

| | |
|---|---|
| 类型 | Uint · default `3` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_flock_retry](../../../config/global/bdev.md#SP_bdev_flock_retry) |

**作用：** times to retry the flock

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bdev_flock_retry 3
ceph config get global bdev_flock_retry
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_flock_retry
ceph -s
```

---

### bdev_flock_retry_interval

| | |
|---|---|
| 类型 | Float · default `0.1` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_flock_retry_interval](../../../config/global/bdev.md#SP_bdev_flock_retry_interval) |

**作用：** Interval after which to retry flock

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global bdev_flock_retry_interval 0.1
ceph config get global bdev_flock_retry_interval
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_flock_retry_interval
ceph -s
```

---

### bdev_inject_crash

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [bdev.md#SP_bdev_inject_crash](../../../config/global/bdev.md#SP_bdev_inject_crash) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bdev_inject_crash 64
ceph config get global bdev_inject_crash
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bdev_inject_crash_flush_delay

| | |
|---|---|
| 类型 | Int · default `2` · **Dev** |
| 表格 | [bdev.md#SP_bdev_inject_crash_flush_delay](../../../config/global/bdev.md#SP_bdev_inject_crash_flush_delay) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global bdev_inject_crash_flush_delay 2
ceph config get global bdev_inject_crash_flush_delay
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`2`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### bdev_ioring

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_ioring](../../../config/global/bdev.md#SP_bdev_ioring) |

**作用：** Enables the Linux io_uring API instead of libaio

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bdev_ioring true
ceph config get global bdev_ioring
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_ioring
ceph -s
```

---

### bdev_ioring_hipri

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_ioring_hipri](../../../config/global/bdev.md#SP_bdev_ioring_hipri) |

**作用：** Enables Linux io_uring API Use polled IO completions

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bdev_ioring_hipri true
ceph config get global bdev_ioring_hipri
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_ioring_hipri
ceph -s
```

---

### bdev_ioring_sqthread_poll

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_ioring_sqthread_poll](../../../config/global/bdev.md#SP_bdev_ioring_sqthread_poll) |

**作用：** Enables Linux io_uring API Offload submission/completion to kernel thread

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bdev_ioring_sqthread_poll true
ceph config get global bdev_ioring_sqthread_poll
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_ioring_sqthread_poll
ceph -s
```

---

### bdev_max_discard_length

| | |
|---|---|
| 类型 | Uint · default `2147483648` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_max_discard_length](../../../config/global/bdev.md#SP_bdev_max_discard_length) |

**作用：** Maximum length of a single discard request

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global bdev_max_discard_length 2147483648
ceph config get global bdev_max_discard_length
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2147483648` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_max_discard_length
ceph -s
```

---

### bdev_nvme_unbind_from_kernel

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_nvme_unbind_from_kernel](../../../config/global/bdev.md#SP_bdev_nvme_unbind_from_kernel) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global bdev_nvme_unbind_from_kernel true
ceph config get global bdev_nvme_unbind_from_kernel
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_nvme_unbind_from_kernel
ceph -s
```

---

### bdev_read_buffer_alignment

| | |
|---|---|
| 类型 | Size · default `4_K` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_read_buffer_alignment](../../../config/global/bdev.md#SP_bdev_read_buffer_alignment) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bdev_read_buffer_alignment 4_K
ceph config get global bdev_read_buffer_alignment
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `4_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_read_buffer_alignment
ceph -s
```

---

### bdev_read_preallocated_huge_buffers

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_read_preallocated_huge_buffers](../../../config/global/bdev.md#SP_bdev_read_preallocated_huge_buffers) |

**作用：** description of pools arrangement for huge page-based read buffers

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bdev_read_preallocated_huge_buffers "example"
ceph config get global bdev_read_preallocated_huge_buffers
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_read_preallocated_huge_buffers
ceph -s
```

---

### bdev_stalled_read_warn_lifetime

| | |
|---|---|
| 类型 | Uint · default `86400` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_stalled_read_warn_lifetime](../../../config/global/bdev.md#SP_bdev_stalled_read_warn_lifetime) |

**作用：** A configurable duration for a stalled read warning to be raised when the number of stalled reads passes the `bdev_stalled_read_warn_threshold` in `bdev_stalled_read_warn_lifetime` seconds

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bdev_stalled_read_warn_lifetime 86400
ceph config get global bdev_stalled_read_warn_lifetime
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `86400` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_stalled_read_warn_lifetime
ceph -s
```

---

### bdev_stalled_read_warn_threshold

| | |
|---|---|
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_stalled_read_warn_threshold](../../../config/global/bdev.md#SP_bdev_stalled_read_warn_threshold) |

**作用：** A configurable number for stalled read warnings to be raised if the number of stalled reads passes the `bdev_stalled_read_warn_threshold` in `bdev_stalled_read_warn_lifetime` seconds

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bdev_stalled_read_warn_threshold 1
ceph config get global bdev_stalled_read_warn_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_stalled_read_warn_threshold
ceph -s
```

---

### bdev_type

| | |
|---|---|
| 类型 | Str · enum: ["aio", "spdk", "pmem"] · default `(empty)` · **Advanced** |
| 表格 | [bdev.md#SP_bdev_type](../../../config/global/bdev.md#SP_bdev_type) |

**作用：** Explicitly set the device type to select the driver if needed

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global bdev_type "example"
ceph config get global bdev_type
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global bdev_type
ceph -s
```

---


[← 概览](../OVERVIEW.md)
