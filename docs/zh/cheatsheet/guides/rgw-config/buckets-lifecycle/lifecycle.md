# Lifecycle (LC)

RGW 配置深度指南 — 17 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_lc_counters_batch_size](#rgw_lc_counters_batch_size) | `5000` | Advanced | 性能 |
| [rgw_lc_counters_cache](#rgw_lc_counters_cache) | `False` | Advanced | 性能 |
| [rgw_lc_counters_cache_size](#rgw_lc_counters_cache_size) | `10000` | Advanced | 性能 |
| [rgw_lc_debug_interval](#rgw_lc_debug_interval) | `-1` | Dev | 开发 |
| [rgw_lc_list_cnt](#rgw_lc_list_cnt) | `1000` | Dev | 性能 |
| [rgw_lc_lock_max_time](#rgw_lc_lock_max_time) | `90` | Dev | 策略 |
| [rgw_lc_max_objs](#rgw_lc_max_objs) | `32` | Advanced | 策略 |
| [rgw_lc_max_rules](#rgw_lc_max_rules) | `1000` | Advanced | 策略 |
| [rgw_lc_max_worker](#rgw_lc_max_worker) | `3` | Advanced | 性能 |
| [rgw_lc_max_wp_worker](#rgw_lc_max_wp_worker) | `128` | Advanced | 策略 |
| [rgw_lc_ordered_list_threshold](#rgw_lc_ordered_list_threshold) | `500` | Dev | 性能 |
| [rgw_lc_thread_delay](#rgw_lc_thread_delay) | `0` | Advanced | 性能 |
| [rgw_lifecycle_work_time](#rgw_lifecycle_work_time) | `00:00-06:00` | Advanced | 性能 |
| [rgw_mp_lock_max_time](#rgw_mp_lock_max_time) | `10_min` | Advanced | 策略 |
| [rgw_restore_lock_max_time](#rgw_restore_lock_max_time) | `90` | Dev | 策略 |
| [rgwlc_auto_session_clear](#rgwlc_auto_session_clear) | `True` | Advanced | 策略 |
| [rgwlc_skip_bucket_step](#rgwlc_skip_bucket_step) | `False` | Advanced | 策略 |

## 寻找最优值

| 模型 | 如何选择 |
|-------|---------------|
| **策略** | 安全、API 兼容性、租户限制 |
| **容量** | 磁盘布局、路径、池容量 |
| **性能** | 基线 → 逐步调整 → 监控 OSD/RGW |
| **连通性** | 最近且稳定的外部端点 |
| **架构** | 后端、多站点拓扑 — 非数值扫描 |
| **开发** | 生产环境保持 upstream 默认值 |

**常用工具：**

```bash
ceph config get client.rgw <option>
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph pg stat
```

---

### rgw_lc_counters_batch_size

| | |
|---|---|
| 类型 | Uint · default `5000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_lc_counters_batch_size](../../../config/rgw/rgw.md#SP_rgw_lc_counters_batch_size) |

**作用：** Batch size for flushing LC per-bucket counters LC per-bucket counters are flushed to cache every N objects processed. Lower values provide more frequent updates, higher values reduce overhead.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**相关选项：**

- [`rgw_lc_counters_cache`](../../../config/rgw/rgw.md#SP_rgw_lc_counters_cache)

**示例：**

```bash
ceph config set client.rgw rgw_lc_counters_batch_size 5000
ceph config get client.rgw rgw_lc_counters_batch_size
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `5000`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_lc_counters_batch_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**边界：** min `1`, max `—`.

---

### rgw_lc_counters_cache

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_lc_counters_cache](../../../config/rgw/rgw.md#SP_rgw_lc_counters_cache) |

**作用：** Enable per-bucket lifecycle performance counters cache When enabled, RGW will create and update per-bucket lifecycle performance counters and expose them via admin socket perf dump.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_lc_counters_cache true
ceph config get client.rgw rgw_lc_counters_cache
ceph config set client.rgw rgw_lc_counters_cache_size 20000
```

**寻找最优值：**

**调优模型：** Performance

1. Default `False` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_lc_counters_cache_size

| | |
|---|---|
| 类型 | Uint · default `10000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_lc_counters_cache_size](../../../config/rgw/rgw.md#SP_rgw_lc_counters_cache_size) |

**作用：** Target size for lifecycle counters cache Maximum number of per-bucket LC counter entries to maintain in cache

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_lc_counters_cache_size 10000
ceph config get client.rgw rgw_lc_counters_cache_size
```

**寻找最优值：**

**调优模型：** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**观测信号：** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_lc_counters_cache_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_lc_debug_interval

| | |
|---|---|
| 类型 | Int · default `-1` · **Dev** |
| 表格 | [rgw.md#SP_rgw_lc_debug_interval](../../../config/rgw/rgw.md#SP_rgw_lc_debug_interval) |

**作用：** The number of seconds that simulate one "day" in order to debug RGW LifeCycle. Do *not* modify for a production cluster. For debugging RGW LifeCycle, the number of seconds that are equivalent to one simulated "day". Values less than 1 are ignored and do not change LifeCycle behavior. For example, during debugging if one wanted every 10 minutes to be equivalent to one day, then this would be set to 600, the number of seconds in 10 minutes.

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_lc_debug_interval -1
ceph config get client.rgw rgw_lc_debug_interval
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`-1`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---

### rgw_lc_list_cnt

| | |
|---|---|
| 类型 | Uint · default `1000` · **Dev** |
| 表格 | [rgw.md#SP_rgw_lc_list_cnt](../../../config/rgw/rgw.md#SP_rgw_lc_list_cnt) |

**作用：** The count of number of objects in per listing of lc processing from each bucket. Number of objects that will be requested when performing a listing request of a bucket for lifecycle processing.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_lc_list_cnt 1000
ceph config get client.rgw rgw_lc_list_cnt
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_lc_list_cnt
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**边界：** min `100`, max `—`.

---

### rgw_lc_lock_max_time

| | |
|---|---|
| 类型 | Int · default `90` · **Dev** |
| 表格 | [rgw.md#SP_rgw_lc_lock_max_time](../../../config/rgw/rgw.md#SP_rgw_lc_lock_max_time) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_lc_lock_max_time 90
ceph config get client.rgw rgw_lc_lock_max_time
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `90` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_lc_max_objs

| | |
|---|---|
| 类型 | Int · default `32` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_lc_max_objs](../../../config/rgw/rgw.md#SP_rgw_lc_max_objs) |

**作用：** Number of lifecycle data shards Number of RADOS objects to use for storing lifecycle index. This affects concurrency of lifecycle maintenance, as shards can be processed in parallel.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_lc_max_objs 32
ceph config get client.rgw rgw_lc_max_objs
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `32` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_lc_max_rules

| | |
|---|---|
| 类型 | Uint · default `1000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_lc_max_rules](../../../config/rgw/rgw.md#SP_rgw_lc_max_rules) |

**作用：** Max number of lifecycle rules set on one bucket Number of lifecycle rules set on one bucket should be limited.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_lc_max_rules 1000
ceph config get client.rgw rgw_lc_max_rules
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_lc_max_worker

| | |
|---|---|
| 类型 | Int · default `3` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_lc_max_worker](../../../config/rgw/rgw.md#SP_rgw_lc_max_worker) |

**作用：** Number of LCWorker tasks that will be run in parallel Number of LCWorker tasks that will run in parallel--used to permit >1 bucket/index shards to be processed simultaneously

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_lc_max_worker 3
ceph config get client.rgw rgw_lc_max_worker
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_lc_max_worker
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_lc_max_wp_worker

| | |
|---|---|
| 类型 | Int · default `128` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_lc_max_wp_worker](../../../config/rgw/rgw.md#SP_rgw_lc_max_wp_worker) |

**作用：** Number of workpool coroutines per LCWorker Number of coroutines in per-LCWorker workpools--used to accelerate per-bucket processing

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_lc_max_wp_worker 128
ceph config get client.rgw rgw_lc_max_wp_worker
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `128` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_lc_ordered_list_threshold

| | |
|---|---|
| 类型 | Uint · default `500` · **Dev** |
| 表格 | [rgw.md#SP_rgw_lc_ordered_list_threshold](../../../config/rgw/rgw.md#SP_rgw_lc_ordered_list_threshold) |

**作用：** Threshold for enabling ordered listing in lifecycle processing. When bucket shard count is below this threshold, lifecycle processing will use ordered listing for better performance. Above this threshold, unordered listing is used to avoid excessive OSD requests. A value of 0 disables ordered listing entirely.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_lc_ordered_list_threshold 500
ceph config get client.rgw rgw_lc_ordered_list_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_lc_ordered_list_threshold
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**边界：** min `0`, max `—`.

---

### rgw_lc_thread_delay

| | |
|---|---|
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_lc_thread_delay](../../../config/rgw/rgw.md#SP_rgw_lc_thread_delay) |

**作用：** Delay after processing of bucket listing chunks (i.e., per 1000 entries) in milliseconds

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_lc_thread_delay 0
ceph config get client.rgw rgw_lc_thread_delay
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_lc_thread_delay
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_lifecycle_work_time

| | |
|---|---|
| 类型 | Str · default `00:00-06:00` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_lifecycle_work_time](../../../config/rgw/rgw.md#SP_rgw_lifecycle_work_time) |

**作用：** Lifecycle allowed work time Local time window in which the lifecycle maintenance thread can work. It expects 24-hour time notation. For example, "00:00-23:59" means starting at midnight lifecycle is allowed to run for the whole day (24 hours). When lifecycle completes, it waits for the next maintenance window. In this example, if it completes at 01:00, it will resume processing 23 hours later at the following midnight.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_lifecycle_work_time "00:00-06:00"
ceph config get client.rgw rgw_lifecycle_work_time
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `00:00-06:00`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_lifecycle_work_time
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_mp_lock_max_time

| | |
|---|---|
| 类型 | Int · default `10_min` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_mp_lock_max_time](../../../config/rgw/rgw.md#SP_rgw_mp_lock_max_time) |

**作用：** Multipart upload max completion time Time length to allow completion of a multipart upload operation. This is done to prevent concurrent completions on the same object with the same upload id.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_mp_lock_max_time 10_min
ceph config get client.rgw rgw_mp_lock_max_time
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `10_min` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

**边界：** min `2_min`, max `—`.

---

### rgw_restore_lock_max_time

| | |
|---|---|
| 类型 | Int · default `90` · **Dev** |
| 表格 | [rgw.md#SP_rgw_restore_lock_max_time](../../../config/rgw/rgw.md#SP_rgw_restore_lock_max_time) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_restore_lock_max_time 90
ceph config get client.rgw rgw_restore_lock_max_time
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `90` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgwlc_auto_session_clear

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgwlc.md#SP_rgwlc_auto_session_clear](../../../config/rgw/rgwlc.md#SP_rgwlc_auto_session_clear) |

**作用：** Automatically clear stale lifecycle sessions (i.e., after 2 idle processing cycles)

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgwlc_auto_session_clear false
ceph config get client.rgw rgwlc_auto_session_clear
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgwlc_skip_bucket_step

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgwlc.md#SP_rgwlc_skip_bucket_step](../../../config/rgw/rgwlc.md#SP_rgwlc_skip_bucket_step) |

**作用：** Conditionally skip the processing (but not the scheduling) of bucket lifecycle

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgwlc_skip_bucket_step true
ceph config get client.rgw rgwlc_skip_bucket_step
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← RGW 配置概览](../OVERVIEW.md)
