# Dynamic resharding

RGW config deep dive — 12 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_dynamic_resharding](#rgw_dynamic_resharding) | `True` | Basic | Policy |
| [rgw_dynamic_resharding_may_reduce](#rgw_dynamic_resharding_may_reduce) | `True` | Advanced | Policy |
| [rgw_dynamic_resharding_reduction_wait](#rgw_dynamic_resharding_reduction_wait) | `120` | Advanced | Performance |
| [rgw_reshard_batch_size](#rgw_reshard_batch_size) | `64` | Advanced | Performance |
| [rgw_reshard_bucket_lock_duration](#rgw_reshard_bucket_lock_duration) | `360` | Advanced | Performance |
| [rgw_reshard_debug_interval](#rgw_reshard_debug_interval) | `-1` | Dev | Dev |
| [rgw_reshard_max_aio](#rgw_reshard_max_aio) | `128` | Advanced | Performance |
| [rgw_reshard_num_logs](#rgw_reshard_num_logs) | `16` | Advanced | Policy |
| [rgw_reshard_progress_judge_interval](#rgw_reshard_progress_judge_interval) | `120` | Dev | Performance |
| [rgw_reshard_progress_judge_ratio](#rgw_reshard_progress_judge_ratio) | `0.5` | Dev | Performance |
| [rgw_reshard_thread_interval](#rgw_reshard_thread_interval) | `600` | Advanced | Performance |
| [rgw_reshardlog_threshold](#rgw_reshardlog_threshold) | `30000` | Dev | Performance |

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, API compatibility, tenant limits |
| **Capacity** | Disk layout, paths, pool sizing |
| **Performance** | Baseline → incremental change → monitor OSD/RGW |
| **Connectivity** | Nearest stable external endpoint |
| **Architecture** | Backend, multisite topology — not numeric sweeps |
| **Dev** | Keep upstream default in production |

**Shared tooling:**

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
| Type | Bool · default `True` · **Basic** |
| Table | [rgw.md#SP_rgw_dynamic_resharding](../../../config/rgw/rgw.md#SP_rgw_dynamic_resharding) |

**What it does:** Enable dynamic resharding If true, RGW will dynamically increase the number of shards in buckets that have a high number of objects per shard.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_dynamic_resharding false
ceph config get client.rgw rgw_dynamic_resharding
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_dynamic_resharding_may_reduce

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_dynamic_resharding_may_reduce](../../../config/rgw/rgw.md#SP_rgw_dynamic_resharding_may_reduce) |

**What it does:** Whether dynamic resharding can reduce the number of shards If true, RGW's dynamic resharding ability is allowed to reduce the number of shards if it appears there are too many.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Related options:**

- [`rgw_dynamic_resharding`](../../../config/rgw/rgw.md#SP_rgw_dynamic_resharding)

**Example:**

```bash
ceph config set client.rgw rgw_dynamic_resharding_may_reduce false
ceph config get client.rgw rgw_dynamic_resharding_may_reduce
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_dynamic_resharding_reduction_wait

| | |
|---|---|
| Type | Uint · default `120` · **Advanced** |
| Table | [rgw.md#SP_rgw_dynamic_resharding_reduction_wait](../../../config/rgw/rgw.md#SP_rgw_dynamic_resharding_reduction_wait) |

**What it does:** Number of hours to delay bucket index shard reduction. In order to avoid resharding buckets with object counts that fluctuate up and down regularly, we implement a delay between noting a shard reduction might be appropriate and when it's actually done. This allows us to cancel the reshard operation if the number of object significantly increases during this delay. WARNING: Setting this value too low could result in significantly reduced cluster performance.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dynamic_resharding_reduction_wait 120
ceph config get client.rgw rgw_dynamic_resharding_reduction_wait
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `120`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_dynamic_resharding_reduction_wait
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**Bounds:** min `0`, max `—`.

---

### rgw_reshard_batch_size

| | |
|---|---|
| Type | Uint · default `64` · **Advanced** |
| Table | [rgw.md#SP_rgw_reshard_batch_size](../../../config/rgw/rgw.md#SP_rgw_reshard_batch_size) |

**What it does:** Number of reshard entries to batch together before sending the operations to the CLS back-end

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_reshard_batch_size 64
ceph config get client.rgw rgw_reshard_batch_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_reshard_batch_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**Bounds:** min `8`, max `—`.

---

### rgw_reshard_bucket_lock_duration

| | |
|---|---|
| Type | Uint · default `360` · **Advanced** |
| Table | [rgw.md#SP_rgw_reshard_bucket_lock_duration](../../../config/rgw/rgw.md#SP_rgw_reshard_bucket_lock_duration) |

**What it does:** Number of seconds the timeout on the reshard locks (bucket reshard lock and reshard log lock) are set to. As a reshard proceeds these locks can be renewed/extended. If too short, reshards cannot complete and will fail, causing a future reshard attempt. If too long a hung or crashed reshard attempt will keep the bucket locked for an extended period, not allowing RGW to detect the failed reshard attempt and recover.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_reshard_bucket_lock_duration 360
ceph config get client.rgw rgw_reshard_bucket_lock_duration
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `360`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_reshard_bucket_lock_duration
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**Bounds:** min `30`, max `—`.

---

### rgw_reshard_debug_interval

| | |
|---|---|
| Type | Int · default `-1` · **Dev** |
| Table | [rgw.md#SP_rgw_reshard_debug_interval](../../../config/rgw/rgw.md#SP_rgw_reshard_debug_interval) |

**What it does:** The number of seconds that simulate one "day" in order to debug RGW dynamic resharding. Do *not* modify for a production cluster. For debugging RGW dynamic resharding, the number of seconds that are equivalent to one simulated "day". Values less than 1 are ignored and do not change dynamic resharding behavior. For example, during debugging if one wanted every 10 minutes to be equivalent to one day, then this would be set to 600, the number of seconds in 10 minutes.

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_reshard_debug_interval -1
ceph config get client.rgw rgw_reshard_debug_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`-1`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**Signals:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_reshard_max_aio

| | |
|---|---|
| Type | Uint · default `128` · **Advanced** |
| Table | [rgw.md#SP_rgw_reshard_max_aio](../../../config/rgw/rgw.md#SP_rgw_reshard_max_aio) |

**What it does:** Maximum number of outstanding asynchronous I/O operations to allow at a time during resharding

**When to use:**

- **Increase** when listings/deletes on sharded buckets are slow and OSDs have headroom.
- **Decrease** when bucket-index pools show sustained load spikes or slow ops.

**Example:**

```bash
ceph config set client.rgw rgw_reshard_max_aio 128
ceph config get client.rgw rgw_reshard_max_aio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at `128` with the workload that triggers RADOS aio on this path.
2. Watch list/delete p99, RGW CPU, and OSD slow ops.
3. Increase in steps (~25%: e.g. 128 → 160 → 192 → 256) until latency stops improving.
4. **Decrease** under recovery pressure, `nearfull`, or sustained bucket-index pool load.

**Signals:** OSD `slow requests`, rising `rgw` throttle counters, flat client throughput.

```bash
ceph config get client.rgw rgw_reshard_max_aio
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
radosgw-admin bucket stats --bucket=BIG_BUCKET | jq '.num_shards'
```

**Bounds:** min `16`, max `—`.

---

### rgw_reshard_num_logs

| | |
|---|---|
| Type | Uint · default `16` · **Advanced** |
| Table | [rgw.md#SP_rgw_reshard_num_logs](../../../config/rgw/rgw.md#SP_rgw_reshard_num_logs) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_reshard_num_logs 16
ceph config get client.rgw rgw_reshard_num_logs
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `16` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

**Bounds:** min `1`, max `—`.

---

### rgw_reshard_progress_judge_interval

| | |
|---|---|
| Type | Uint · default `120` · **Dev** |
| Table | [rgw.md#SP_rgw_reshard_progress_judge_interval](../../../config/rgw/rgw.md#SP_rgw_reshard_progress_judge_interval) |

**What it does:** interval (in seconds) of judging if bucket reshard failed in block state

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_reshard_progress_judge_interval 120
ceph config get client.rgw rgw_reshard_progress_judge_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `120` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

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
| Type | Float · default `0.5` · **Dev** |
| Table | [rgw.md#SP_rgw_reshard_progress_judge_ratio](../../../config/rgw/rgw.md#SP_rgw_reshard_progress_judge_ratio) |

**What it does:** ratio of reshard progress judge interval to randomly vary Add a random delay to rgw_reshard_progress_judge_interval for deciding when to judge the reshard process. The default setting spreads judge time window of &#91;1, 1.5&#93; * rgw_reshard_progress_judge_interval.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Related options:**

- [`rgw_reshard_progress_judge_interval`](../../../config/rgw/rgw.md#SP_rgw_reshard_progress_judge_interval)

**Example:**

```bash
ceph config set client.rgw rgw_reshard_progress_judge_ratio 0.5
ceph config get client.rgw rgw_reshard_progress_judge_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.5`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Uint · default `600` · **Advanced** |
| Table | [rgw.md#SP_rgw_reshard_thread_interval](../../../config/rgw/rgw.md#SP_rgw_reshard_thread_interval) |

**What it does:** Number of seconds between processing of reshard log entries

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_reshard_thread_interval 600
ceph config get client.rgw rgw_reshard_thread_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `600` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_reshard_thread_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**Bounds:** min `10`, max `—`.

---

### rgw_reshardlog_threshold

| | |
|---|---|
| Type | Uint · default `30000` · **Dev** |
| Table | [rgw.md#SP_rgw_reshardlog_threshold](../../../config/rgw/rgw.md#SP_rgw_reshardlog_threshold) |

**What it does:** threshold for a shard to record log before blocking writes

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Related options:**

- [`rgw_reshard_progress_judge_interval`](../../../config/rgw/rgw.md#SP_rgw_reshard_progress_judge_interval)

**Example:**

```bash
ceph config set client.rgw rgw_reshardlog_threshold 30000
ceph config get client.rgw rgw_reshardlog_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30000`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_reshardlog_threshold
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](../OVERVIEW.md)
