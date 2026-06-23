# Dynamic resharding

RGW config deep dive — 12 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_dynamic_resharding](#rgw_dynamic_resharding) | `True` | Basic |
| [rgw_dynamic_resharding_may_reduce](#rgw_dynamic_resharding_may_reduce) | `True` | Advanced |
| [rgw_dynamic_resharding_reduction_wait](#rgw_dynamic_resharding_reduction_wait) | `120` | Advanced |
| [rgw_reshard_batch_size](#rgw_reshard_batch_size) | `64` | Advanced |
| [rgw_reshard_bucket_lock_duration](#rgw_reshard_bucket_lock_duration) | `360` | Advanced |
| [rgw_reshard_debug_interval](#rgw_reshard_debug_interval) | `-1` | Dev |
| [rgw_reshard_max_aio](#rgw_reshard_max_aio) | `128` | Advanced |
| [rgw_reshard_num_logs](#rgw_reshard_num_logs) | `16` | Advanced |
| [rgw_reshard_progress_judge_interval](#rgw_reshard_progress_judge_interval) | `120` | Dev |
| [rgw_reshard_progress_judge_ratio](#rgw_reshard_progress_judge_ratio) | `0.5` | Dev |
| [rgw_reshard_thread_interval](#rgw_reshard_thread_interval) | `600` | Advanced |
| [rgw_reshardlog_threshold](#rgw_reshardlog_threshold) | `30000` | Dev |

---

### rgw_dynamic_resharding

| | |
|---|---|
| Type | Bool · default `True` · **Basic** |
| Table | [rgw.md#SP_rgw_dynamic_resharding](../../config/rgw/rgw.md#SP_rgw_dynamic_resharding) |

**What it does:** Enable dynamic resharding

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_dynamic_resharding True
ceph config get client.rgw rgw_dynamic_resharding
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`True`) matches upstream.

---

### rgw_dynamic_resharding_may_reduce

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_dynamic_resharding_may_reduce](../../config/rgw/rgw.md#SP_rgw_dynamic_resharding_may_reduce) |

**What it does:** Whether dynamic resharding can reduce the number of shards

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_dynamic_resharding_may_reduce True
ceph config get client.rgw rgw_dynamic_resharding_may_reduce
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`True`) matches upstream.

---

### rgw_dynamic_resharding_reduction_wait

| | |
|---|---|
| Type | Uint · default `120` · **Advanced** |
| Table | [rgw.md#SP_rgw_dynamic_resharding_reduction_wait](../../config/rgw/rgw.md#SP_rgw_dynamic_resharding_reduction_wait) |

**What it does:** Number of hours to delay bucket index shard reduction.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dynamic_resharding_reduction_wait 120
ceph config get client.rgw rgw_dynamic_resharding_reduction_wait
```

**Finding optimal value:** Start from upstream default (`120`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_reshard_batch_size

| | |
|---|---|
| Type | Uint · default `64` · **Advanced** |
| Table | [rgw.md#SP_rgw_reshard_batch_size](../../config/rgw/rgw.md#SP_rgw_reshard_batch_size) |

**What it does:** Number of reshard entries to batch together before sending the operations to the CLS back-end

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_reshard_batch_size 64
ceph config get client.rgw rgw_reshard_batch_size
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`64`) matches S3 compatibility for most workloads. Valid range: min=8, max=—.

---

### rgw_reshard_bucket_lock_duration

| | |
|---|---|
| Type | Uint · default `360` · **Advanced** |
| Table | [rgw.md#SP_rgw_reshard_bucket_lock_duration](../../config/rgw/rgw.md#SP_rgw_reshard_bucket_lock_duration) |

**What it does:** Number of seconds the timeout on the reshard locks (bucket reshard lock and reshard log lock) are set to. As a reshard proceeds these locks can be renewed/extended. If too short, reshards cannot complete and will fail, causing a future reshard attempt. If too long a hung or crashed reshard attempt will keep the bucket locked for an extended period, not allowing RGW to detect the failed reshard attempt and recover.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_reshard_bucket_lock_duration 360
ceph config get client.rgw rgw_reshard_bucket_lock_duration
```

**Finding optimal value:** Start from upstream default (`360`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_reshard_debug_interval

| | |
|---|---|
| Type | Int · default `-1` · **Dev** |
| Table | [rgw.md#SP_rgw_reshard_debug_interval](../../config/rgw/rgw.md#SP_rgw_reshard_debug_interval) |

**What it does:** The number of seconds that simulate one "day" in order to debug RGW dynamic resharding. Do *not* modify for a production cluster.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_reshard_debug_interval -1
ceph config get client.rgw rgw_reshard_debug_interval
```

**Finding optimal value:** Keep the upstream default (`-1`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_reshard_max_aio

| | |
|---|---|
| Type | Uint · default `128` · **Advanced** |
| Table | [rgw.md#SP_rgw_reshard_max_aio](../../config/rgw/rgw.md#SP_rgw_reshard_max_aio) |

**What it does:** Maximum number of outstanding asynchronous I/O operations to allow at a time during resharding

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_reshard_max_aio 128
ceph config get client.rgw rgw_reshard_max_aio
```

**Finding optimal value:** Performance sweep: baseline at default, then increase in steps while watching RGW CPU, request p99, and OSD slow ops. Optimal is the highest value before OSD or network saturation. Valid range: min=16, max=—. Default: `128`.

---

### rgw_reshard_num_logs

| | |
|---|---|
| Type | Uint · default `16` · **Advanced** |
| Table | [rgw.md#SP_rgw_reshard_num_logs](../../config/rgw/rgw.md#SP_rgw_reshard_num_logs) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_reshard_num_logs 16
ceph config get client.rgw rgw_reshard_num_logs
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`16`) matches S3 compatibility for most workloads. Valid range: min=1, max=—.

---

### rgw_reshard_progress_judge_interval

| | |
|---|---|
| Type | Uint · default `120` · **Dev** |
| Table | [rgw.md#SP_rgw_reshard_progress_judge_interval](../../config/rgw/rgw.md#SP_rgw_reshard_progress_judge_interval) |

**What it does:** interval (in seconds) of judging if bucket reshard failed in block state

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_reshard_progress_judge_interval 120
ceph config get client.rgw rgw_reshard_progress_judge_interval
```

**Finding optimal value:** Keep the upstream default (`120`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_reshard_progress_judge_ratio

| | |
|---|---|
| Type | Float · default `0.5` · **Dev** |
| Table | [rgw.md#SP_rgw_reshard_progress_judge_ratio](../../config/rgw/rgw.md#SP_rgw_reshard_progress_judge_ratio) |

**What it does:** ratio of reshard progress judge interval to randomly vary

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_reshard_progress_judge_ratio 0.5
ceph config get client.rgw rgw_reshard_progress_judge_ratio
```

**Finding optimal value:** Keep the upstream default (`0.5`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_reshard_thread_interval

| | |
|---|---|
| Type | Uint · default `600` · **Advanced** |
| Table | [rgw.md#SP_rgw_reshard_thread_interval](../../config/rgw/rgw.md#SP_rgw_reshard_thread_interval) |

**What it does:** Number of seconds between processing of reshard log entries

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_reshard_thread_interval 600
ceph config get client.rgw rgw_reshard_thread_interval
```

**Finding optimal value:** Lower for fresher behavior / faster reaction; higher to reduce background load. Adjust from default (`600`) only when logs show sync, cache, or timeout issues. Valid range: min=10, max=—.

---

### rgw_reshardlog_threshold

| | |
|---|---|
| Type | Uint · default `30000` · **Dev** |
| Table | [rgw.md#SP_rgw_reshardlog_threshold](../../config/rgw/rgw.md#SP_rgw_reshardlog_threshold) |

**What it does:** threshold for a shard to record log before blocking writes

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_reshardlog_threshold 30000
ceph config get client.rgw rgw_reshardlog_threshold
```

**Finding optimal value:** Keep the upstream default (`30000`) in production. Enable or change only during targeted debugging sessions.

---


[← RGW config overview](OVERVIEW.md)
