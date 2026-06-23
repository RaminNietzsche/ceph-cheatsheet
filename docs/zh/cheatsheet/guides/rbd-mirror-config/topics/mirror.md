# RBD mirror

RBD mirror 配置深度指南 — 24 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rbd-mirror/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rbd_mirror_concurrent_image_deletions](#rbd_mirror_concurrent_image_deletions) | `1` | Advanced | 性能 |
| [rbd_mirror_concurrent_image_syncs](#rbd_mirror_concurrent_image_syncs) | `5` | Advanced | 性能 |
| [rbd_mirror_delete_retry_interval](#rbd_mirror_delete_retry_interval) | `30` | Advanced | 性能 |
| [rbd_mirror_image_perf_stats_prio](#rbd_mirror_image_perf_stats_prio) | `5` | Advanced | 性能 |
| [rbd_mirror_image_policy_migration_throttle](#rbd_mirror_image_policy_migration_throttle) | `300` | Advanced | 性能 |
| [rbd_mirror_image_policy_rebalance_timeout](#rbd_mirror_image_policy_rebalance_timeout) | `0` | Advanced | 性能 |
| [rbd_mirror_image_policy_type](#rbd_mirror_image_policy_type) | `simple` | Advanced | 性能 |
| [rbd_mirror_image_policy_update_throttle_interval](#rbd_mirror_image_policy_update_throttle_interval) | `1` | Advanced | 性能 |
| [rbd_mirror_image_state_check_interval](#rbd_mirror_image_state_check_interval) | `30` | Advanced | 性能 |
| [rbd_mirror_journal_commit_age](#rbd_mirror_journal_commit_age) | `5` | Advanced | 性能 |
| [rbd_mirror_journal_poll_age](#rbd_mirror_journal_poll_age) | `5` | Advanced | 性能 |
| [rbd_mirror_leader_heartbeat_interval](#rbd_mirror_leader_heartbeat_interval) | `5` | Advanced | 性能 |
| [rbd_mirror_leader_max_acquire_attempts_before_break](#rbd_mirror_leader_max_acquire_attempts_before_break) | `3` | Advanced | 性能 |
| [rbd_mirror_leader_max_missed_heartbeats](#rbd_mirror_leader_max_missed_heartbeats) | `2` | Advanced | 性能 |
| [rbd_mirror_memory_autotune](#rbd_mirror_memory_autotune) | `True` | Dev | 开发 |
| [rbd_mirror_memory_base](#rbd_mirror_memory_base) | `768_M` | Dev | 开发 |
| [rbd_mirror_memory_cache_autotune_interval](#rbd_mirror_memory_cache_autotune_interval) | `30` | Dev | 开发 |
| [rbd_mirror_memory_cache_min](#rbd_mirror_memory_cache_min) | `128_M` | Dev | 开发 |
| [rbd_mirror_memory_cache_resize_interval](#rbd_mirror_memory_cache_resize_interval) | `5` | Dev | 开发 |
| [rbd_mirror_memory_expected_fragmentation](#rbd_mirror_memory_expected_fragmentation) | `0.15` | Dev | 开发 |
| [rbd_mirror_memory_target](#rbd_mirror_memory_target) | `4_G` | Basic | 策略 |
| [rbd_mirror_perf_stats_prio](#rbd_mirror_perf_stats_prio) | `5` | Advanced | 性能 |
| [rbd_mirror_pool_replayers_refresh_interval](#rbd_mirror_pool_replayers_refresh_interval) | `30` | Advanced | 性能 |
| [rbd_mirror_sync_point_update_age](#rbd_mirror_sync_point_update_age) | `30` | Advanced | 性能 |

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
ceph config get <daemon> <option>  # e.g. rbd-mirror
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_mirror_concurrent_image_deletions

| | |
|---|---|
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirror_concurrent_image_deletions](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_concurrent_image_deletions) |

**作用：** maximum number of image deletions in parallel

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_mirror_concurrent_image_deletions 1
ceph config get client rbd_mirror_concurrent_image_deletions
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirror_concurrent_image_deletions
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirror_concurrent_image_syncs

| | |
|---|---|
| 类型 | Uint · default `5` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirror_concurrent_image_syncs](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_concurrent_image_syncs) |

**作用：** maximum number of image syncs in parallel

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_mirror_concurrent_image_syncs 5
ceph config get client rbd_mirror_concurrent_image_syncs
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirror_concurrent_image_syncs
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirror_delete_retry_interval

| | |
|---|---|
| 类型 | Float · default `30` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirror_delete_retry_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_delete_retry_interval) |

**作用：** interval to check and retry the failed deletion requests

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set client rbd_mirror_delete_retry_interval 30
ceph config get client rbd_mirror_delete_retry_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirror_delete_retry_interval
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirror_image_perf_stats_prio

| | |
|---|---|
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirror_image_perf_stats_prio](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_image_perf_stats_prio) |

**作用：** Priority level for mirror daemon per-image replication perf counters

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_mirror_image_perf_stats_prio 5
ceph config get client rbd_mirror_image_perf_stats_prio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `11`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirror_image_perf_stats_prio
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirror_image_policy_migration_throttle

| | |
|---|---|
| 类型 | Uint · default `300` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirror_image_policy_migration_throttle](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_image_policy_migration_throttle) |

**作用：** number of seconds after which an image can be reshuffled (migrated) again

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_mirror_image_policy_migration_throttle 300
ceph config get client rbd_mirror_image_policy_migration_throttle
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `300` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirror_image_policy_migration_throttle
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirror_image_policy_rebalance_timeout

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirror_image_policy_rebalance_timeout](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_image_policy_rebalance_timeout) |

**作用：** number of seconds policy should be idle before triggering reshuffle (rebalance) of images

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set client rbd_mirror_image_policy_rebalance_timeout 0
ceph config get client rbd_mirror_image_policy_rebalance_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirror_image_policy_rebalance_timeout
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirror_image_policy_type

| | |
|---|---|
| 类型 | Str · enum: ["none", "simple"] · default `simple` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirror_image_policy_type](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_image_policy_type) |

**作用：** active/active policy type for mapping images to instances

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_mirror_image_policy_type simple
ceph config get client rbd_mirror_image_policy_type
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `simple` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirror_image_policy_type
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirror_image_policy_update_throttle_interval

| | |
|---|---|
| 类型 | Float · default `1` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirror_image_policy_update_throttle_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_image_policy_update_throttle_interval) |

**作用：** interval (in seconds) to throttle images for mirror daemon peer updates

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set client rbd_mirror_image_policy_update_throttle_interval 1
ceph config get client rbd_mirror_image_policy_update_throttle_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirror_image_policy_update_throttle_interval
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirror_image_state_check_interval

| | |
|---|---|
| 类型 | Uint · default `30` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirror_image_state_check_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_image_state_check_interval) |

**作用：** interval to get images from pool watcher and set sources in replayer

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set client rbd_mirror_image_state_check_interval 30
ceph config get client rbd_mirror_image_state_check_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirror_image_state_check_interval
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirror_journal_commit_age

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirror_journal_commit_age](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_journal_commit_age) |

**作用：** commit time interval, seconds

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_mirror_journal_commit_age 5
ceph config get client rbd_mirror_journal_commit_age
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirror_journal_commit_age
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirror_journal_poll_age

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirror_journal_poll_age](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_journal_poll_age) |

**作用：** maximum age (in seconds) between successive journal polls

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_mirror_journal_poll_age 5
ceph config get client rbd_mirror_journal_poll_age
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirror_journal_poll_age
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirror_leader_heartbeat_interval

| | |
|---|---|
| 类型 | Uint · default `5` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirror_leader_heartbeat_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_leader_heartbeat_interval) |

**作用：** interval (in seconds) between mirror leader heartbeats

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set client rbd_mirror_leader_heartbeat_interval 5
ceph config get client rbd_mirror_leader_heartbeat_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirror_leader_heartbeat_interval
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirror_leader_max_acquire_attempts_before_break

| | |
|---|---|
| 类型 | Uint · default `3` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirror_leader_max_acquire_attempts_before_break](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_leader_max_acquire_attempts_before_break) |

**作用：** number of failed attempts to acquire lock after missing heartbeats before breaking lock

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client rbd_mirror_leader_max_acquire_attempts_before_break 3
ceph config get client rbd_mirror_leader_max_acquire_attempts_before_break
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirror_leader_max_acquire_attempts_before_break
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirror_leader_max_missed_heartbeats

| | |
|---|---|
| 类型 | Uint · default `2` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirror_leader_max_missed_heartbeats](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_leader_max_missed_heartbeats) |

**作用：** number of missed heartbeats for non-lock owner to attempt to acquire lock

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client rbd_mirror_leader_max_missed_heartbeats 2
ceph config get client rbd_mirror_leader_max_missed_heartbeats
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirror_leader_max_missed_heartbeats
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirror_memory_autotune

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [rbd.md#SP_rbd_mirror_memory_autotune](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_autotune) |

**作用：** Automatically tune the ratio of caches while respecting min values.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client rbd_mirror_memory_autotune false
ceph config get client rbd_mirror_memory_autotune
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### rbd_mirror_memory_base

| | |
|---|---|
| 类型 | Size · default `768_M` · **Dev** |
| 表格 | [rbd.md#SP_rbd_mirror_memory_base](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_base) |

**作用：** When tcmalloc and cache autotuning is enabled, estimate the minimum amount of memory in bytes the rbd-mirror daemon will need.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client rbd_mirror_memory_base 768_M
ceph config get client rbd_mirror_memory_base
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`768_M`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### rbd_mirror_memory_cache_autotune_interval

| | |
|---|---|
| 类型 | Float · default `30` · **Dev** |
| 表格 | [rbd.md#SP_rbd_mirror_memory_cache_autotune_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_cache_autotune_interval) |

**作用：** The number of seconds to wait between rebalances when cache autotune is enabled.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client rbd_mirror_memory_cache_autotune_interval 30
ceph config get client rbd_mirror_memory_cache_autotune_interval
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`30`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### rbd_mirror_memory_cache_min

| | |
|---|---|
| 类型 | Size · default `128_M` · **Dev** |
| 表格 | [rbd.md#SP_rbd_mirror_memory_cache_min](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_cache_min) |

**作用：** When tcmalloc and cache autotuning is enabled, set the minimum amount of memory used for cache.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client rbd_mirror_memory_cache_min 128_M
ceph config get client rbd_mirror_memory_cache_min
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`128_M`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### rbd_mirror_memory_cache_resize_interval

| | |
|---|---|
| 类型 | Float · default `5` · **Dev** |
| 表格 | [rbd.md#SP_rbd_mirror_memory_cache_resize_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_cache_resize_interval) |

**作用：** When tcmalloc and cache autotuning is enabled, wait this many seconds between resizing caches.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client rbd_mirror_memory_cache_resize_interval 5
ceph config get client rbd_mirror_memory_cache_resize_interval
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`5`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### rbd_mirror_memory_expected_fragmentation

| | |
|---|---|
| 类型 | Float · default `0.15` · **Dev** |
| 表格 | [rbd.md#SP_rbd_mirror_memory_expected_fragmentation](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_expected_fragmentation) |

**作用：** When tcmalloc and cache autotuning is enabled, estimate the percent of memory fragmentation.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client rbd_mirror_memory_expected_fragmentation 0.15
ceph config get client rbd_mirror_memory_expected_fragmentation
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0.15`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### rbd_mirror_memory_target

| | |
|---|---|
| 类型 | Size · default `4_G` · **Basic** |
| 表格 | [rbd.md#SP_rbd_mirror_memory_target](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_target) |

**作用：** When tcmalloc and cache autotuning is enabled, try to keep this many bytes mapped in memory.

**何时使用：** 核心 RBD mirror 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set client rbd_mirror_memory_target 4_G
ceph config get client rbd_mirror_memory_target
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `4_G` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirror_memory_target
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirror_perf_stats_prio

| | |
|---|---|
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirror_perf_stats_prio](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_perf_stats_prio) |

**作用：** Priority level for mirror daemon replication perf counters

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_mirror_perf_stats_prio 5
ceph config get client rbd_mirror_perf_stats_prio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `11`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirror_perf_stats_prio
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirror_pool_replayers_refresh_interval

| | |
|---|---|
| 类型 | Uint · default `30` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirror_pool_replayers_refresh_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_pool_replayers_refresh_interval) |

**作用：** interval to refresh peers in rbd-mirror daemon

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set client rbd_mirror_pool_replayers_refresh_interval 30
ceph config get client rbd_mirror_pool_replayers_refresh_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirror_pool_replayers_refresh_interval
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirror_sync_point_update_age

| | |
|---|---|
| 类型 | Float · default `30` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirror_sync_point_update_age](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_sync_point_update_age) |

**作用：** number of seconds between each update of the image sync point object number

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_mirror_sync_point_update_age 30
ceph config get client rbd_mirror_sync_point_update_age
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirror_sync_point_update_age
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---


[← 概览](../OVERVIEW.md)
