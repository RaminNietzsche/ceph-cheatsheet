# Dynamic resharding

RGW 配置深度指南 — 12 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_dynamic_resharding](#rgw_dynamic_resharding) | `True` | Basic | 策略 |
| [rgw_dynamic_resharding_may_reduce](#rgw_dynamic_resharding_may_reduce) | `True` | Advanced | 策略 |
| [rgw_dynamic_resharding_reduction_wait](#rgw_dynamic_resharding_reduction_wait) | `120` | Advanced | 性能 |
| [rgw_reshard_batch_size](#rgw_reshard_batch_size) | `64` | Advanced | 性能 |
| [rgw_reshard_bucket_lock_duration](#rgw_reshard_bucket_lock_duration) | `360` | Advanced | 性能 |
| [rgw_reshard_debug_interval](#rgw_reshard_debug_interval) | `-1` | Dev | 开发 |
| [rgw_reshard_max_aio](#rgw_reshard_max_aio) | `128` | Advanced | 性能 |
| [rgw_reshard_num_logs](#rgw_reshard_num_logs) | `16` | Advanced | 策略 |
| [rgw_reshard_progress_judge_interval](#rgw_reshard_progress_judge_interval) | `120` | Dev | 性能 |
| [rgw_reshard_progress_judge_ratio](#rgw_reshard_progress_judge_ratio) | `0.5` | Dev | 性能 |
| [rgw_reshard_thread_interval](#rgw_reshard_thread_interval) | `600` | Advanced | 性能 |
| [rgw_reshardlog_threshold](#rgw_reshardlog_threshold) | `30000` | Dev | 性能 |

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

### rgw_dynamic_resharding

| | |
|---|---|
| 类型 | Bool · default `True` · **Basic** |
| 表格 | [rgw.md#SP_rgw_dynamic_resharding](../../../config/rgw/rgw.md#SP_rgw_dynamic_resharding) |

**作用：** Enable dynamic resharding If true, RGW will dynamically increase the number of shards in buckets that have a high number of objects per shard.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_dynamic_resharding false
ceph config get client.rgw rgw_dynamic_resharding
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_dynamic_resharding_may_reduce

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_dynamic_resharding_may_reduce](../../../config/rgw/rgw.md#SP_rgw_dynamic_resharding_may_reduce) |

**作用：** Whether dynamic resharding can reduce the number of shards If true, RGW's dynamic resharding ability is allowed to reduce the number of shards if it appears there are too many.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**相关选项：**

- [`rgw_dynamic_resharding`](../../../config/rgw/rgw.md#SP_rgw_dynamic_resharding)

**示例：**

```bash
ceph config set client.rgw rgw_dynamic_resharding_may_reduce false
ceph config get client.rgw rgw_dynamic_resharding_may_reduce
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_dynamic_resharding_reduction_wait

| | |
|---|---|
| 类型 | Uint · default `120` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_dynamic_resharding_reduction_wait](../../../config/rgw/rgw.md#SP_rgw_dynamic_resharding_reduction_wait) |

**作用：** Number of hours to delay bucket index shard reduction. In order to avoid resharding buckets with object counts that fluctuate up and down regularly, we implement a delay between noting a shard reduction might be appropriate and when it's actually done. This allows us to cancel the reshard operation if the number of object significantly increases during this delay. WARNING: Setting this value too low could result in significantly reduced cluster performance.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_dynamic_resharding_reduction_wait 120
ceph config get client.rgw rgw_dynamic_resharding_reduction_wait
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `120`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_dynamic_resharding_reduction_wait
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**边界：** min `0`, max `—`.

---

### rgw_reshard_batch_size

| | |
|---|---|
| 类型 | Uint · default `64` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_reshard_batch_size](../../../config/rgw/rgw.md#SP_rgw_reshard_batch_size) |

**作用：** Number of reshard entries to batch together before sending the operations to the CLS back-end

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_reshard_batch_size 64
ceph config get client.rgw rgw_reshard_batch_size
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `64`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_reshard_batch_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**边界：** min `8`, max `—`.

---

### rgw_reshard_bucket_lock_duration

| | |
|---|---|
| 类型 | Uint · default `360` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_reshard_bucket_lock_duration](../../../config/rgw/rgw.md#SP_rgw_reshard_bucket_lock_duration) |

**作用：** Number of seconds the timeout on the reshard locks (bucket reshard lock and reshard log lock) are set to. As a reshard proceeds these locks can be renewed/extended. If too short, reshards cannot complete and will fail, causing a future reshard attempt. If too long a hung or crashed reshard attempt will keep the bucket locked for an extended period, not allowing RGW to detect the failed reshard attempt and recover.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_reshard_bucket_lock_duration 360
ceph config get client.rgw rgw_reshard_bucket_lock_duration
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `360`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_reshard_bucket_lock_duration
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**边界：** min `30`, max `—`.

---

### rgw_reshard_debug_interval

| | |
|---|---|
| 类型 | Int · default `-1` · **Dev** |
| 表格 | [rgw.md#SP_rgw_reshard_debug_interval](../../../config/rgw/rgw.md#SP_rgw_reshard_debug_interval) |

**作用：** The number of seconds that simulate one "day" in order to debug RGW dynamic resharding. Do *not* modify for a production cluster. For debugging RGW dynamic resharding, the number of seconds that are equivalent to one simulated "day". Values less than 1 are ignored and do not change dynamic resharding behavior. For example, during debugging if one wanted every 10 minutes to be equivalent to one day, then this would be set to 600, the number of seconds in 10 minutes.

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_reshard_debug_interval -1
ceph config get client.rgw rgw_reshard_debug_interval
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`-1`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---

### rgw_reshard_max_aio

| | |
|---|---|
| 类型 | Uint · default `128` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_reshard_max_aio](../../../config/rgw/rgw.md#SP_rgw_reshard_max_aio) |

**作用：** Maximum number of outstanding asynchronous I/O operations to allow at a time during resharding

**何时使用：**

- **Increase** when listings/deletes on sharded buckets are slow and OSDs have headroom.
- **Decrease** when bucket-index pools show sustained load spikes or slow ops.

**示例：**

```bash
ceph config set client.rgw rgw_reshard_max_aio 128
ceph config get client.rgw rgw_reshard_max_aio
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at `128` with the workload that triggers RADOS aio on this path.
2. Watch list/delete p99, RGW CPU, and OSD slow ops.
3. Increase in steps (~25%: e.g. 128 → 160 → 192 → 256) until latency stops improving.
4. **Decrease** under recovery pressure, `nearfull`, or sustained bucket-index pool load.

**观测信号：** OSD `slow requests`, rising `rgw` throttle counters, flat client throughput.

```bash
ceph config get client.rgw rgw_reshard_max_aio
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
radosgw-admin bucket stats --bucket=BIG_BUCKET | jq '.num_shards'
```

**边界：** min `16`, max `—`.

---

### rgw_reshard_num_logs

| | |
|---|---|
| 类型 | Uint · default `16` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_reshard_num_logs](../../../config/rgw/rgw.md#SP_rgw_reshard_num_logs) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_reshard_num_logs 16
ceph config get client.rgw rgw_reshard_num_logs
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `16` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

**边界：** min `1`, max `—`.

---

### rgw_reshard_progress_judge_interval

| | |
|---|---|
| 类型 | Uint · default `120` · **Dev** |
| 表格 | [rgw.md#SP_rgw_reshard_progress_judge_interval](../../../config/rgw/rgw.md#SP_rgw_reshard_progress_judge_interval) |

**作用：** interval (in seconds) of judging if bucket reshard failed in block state

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_reshard_progress_judge_interval 120
ceph config get client.rgw rgw_reshard_progress_judge_interval
```

**寻找最优值：**

**调优模型：** Performance

1. Default `120` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_reshard_progress_judge_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_reshard_progress_judge_ratio

| | |
|---|---|
| 类型 | Float · default `0.5` · **Dev** |
| 表格 | [rgw.md#SP_rgw_reshard_progress_judge_ratio](../../../config/rgw/rgw.md#SP_rgw_reshard_progress_judge_ratio) |

**作用：** ratio of reshard progress judge interval to randomly vary Add a random delay to rgw_reshard_progress_judge_interval for deciding when to judge the reshard process. The default setting spreads judge time window of &#91;1, 1.5&#93; * rgw_reshard_progress_judge_interval.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**相关选项：**

- [`rgw_reshard_progress_judge_interval`](../../../config/rgw/rgw.md#SP_rgw_reshard_progress_judge_interval)

**示例：**

```bash
ceph config set client.rgw rgw_reshard_progress_judge_ratio 0.5
ceph config get client.rgw rgw_reshard_progress_judge_ratio
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `0.5`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_reshard_progress_judge_ratio
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_reshard_thread_interval

| | |
|---|---|
| 类型 | Uint · default `600` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_reshard_thread_interval](../../../config/rgw/rgw.md#SP_rgw_reshard_thread_interval) |

**作用：** Number of seconds between processing of reshard log entries

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_reshard_thread_interval 600
ceph config get client.rgw rgw_reshard_thread_interval
```

**寻找最优值：**

**调优模型：** Performance

1. Default `600` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_reshard_thread_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**边界：** min `10`, max `—`.

---

### rgw_reshardlog_threshold

| | |
|---|---|
| 类型 | Uint · default `30000` · **Dev** |
| 表格 | [rgw.md#SP_rgw_reshardlog_threshold](../../../config/rgw/rgw.md#SP_rgw_reshardlog_threshold) |

**作用：** threshold for a shard to record log before blocking writes

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**相关选项：**

- [`rgw_reshard_progress_judge_interval`](../../../config/rgw/rgw.md#SP_rgw_reshard_progress_judge_interval)

**示例：**

```bash
ceph config set client.rgw rgw_reshardlog_threshold 30000
ceph config get client.rgw rgw_reshardlog_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `30000`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_reshardlog_threshold
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
