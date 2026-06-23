# Lifecycle (LC) workers

RGW config deep dive — 12 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_lc_counters_batch_size](#rgw_lc_counters_batch_size) | `5000` | Advanced | Performance |
| [rgw_lc_counters_cache](#rgw_lc_counters_cache) | `False` | Advanced | Performance |
| [rgw_lc_counters_cache_size](#rgw_lc_counters_cache_size) | `10000` | Advanced | Performance |
| [rgw_lc_debug_interval](#rgw_lc_debug_interval) | `-1` | Dev | Dev |
| [rgw_lc_list_cnt](#rgw_lc_list_cnt) | `1000` | Dev | Performance |
| [rgw_lc_lock_max_time](#rgw_lc_lock_max_time) | `90` | Dev | Policy |
| [rgw_lc_max_objs](#rgw_lc_max_objs) | `32` | Advanced | Policy |
| [rgw_lc_max_rules](#rgw_lc_max_rules) | `1000` | Advanced | Policy |
| [rgw_lc_max_worker](#rgw_lc_max_worker) | `3` | Advanced | Performance |
| [rgw_lc_max_wp_worker](#rgw_lc_max_wp_worker) | `128` | Advanced | Policy |
| [rgw_lc_ordered_list_threshold](#rgw_lc_ordered_list_threshold) | `500` | Dev | Performance |
| [rgw_lc_thread_delay](#rgw_lc_thread_delay) | `0` | Advanced | Performance |

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
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph osd pool stats
```

---

### rgw_lc_counters_batch_size

| | |
|---|---|
| Type | Uint · default `5000` · **Advanced** |
| Table | [rgw.md#SP_rgw_lc_counters_batch_size](../../config/rgw/rgw.md#SP_rgw_lc_counters_batch_size) |

**What it does:** Batch size for flushing LC per-bucket counters

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_lc_counters_batch_size 5000
ceph config get client.rgw rgw_lc_counters_batch_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5000`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_lc_counters_batch_size
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

**Bounds:** min `1`, max `—`.

---

### rgw_lc_counters_cache

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_lc_counters_cache](../../config/rgw/rgw.md#SP_rgw_lc_counters_cache) |

**What it does:** Enable per-bucket lifecycle performance counters cache

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_lc_counters_cache False
ceph config get client.rgw rgw_lc_counters_cache
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `False` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_lc_counters_cache_size

| | |
|---|---|
| Type | Uint · default `10000` · **Advanced** |
| Table | [rgw.md#SP_rgw_lc_counters_cache_size](../../config/rgw/rgw.md#SP_rgw_lc_counters_cache_size) |

**What it does:** Target size for lifecycle counters cache

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Example:**

```bash
ceph config set client.rgw rgw_lc_counters_cache_size 10000
ceph config get client.rgw rgw_lc_counters_cache_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**Signals:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_lc_counters_cache_size
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_lc_debug_interval

| | |
|---|---|
| Type | Int · default `-1` · **Dev** |
| Table | [rgw.md#SP_rgw_lc_debug_interval](../../config/rgw/rgw.md#SP_rgw_lc_debug_interval) |

**What it does:** The number of seconds that simulate one "day" in order to debug RGW LifeCycle. Do *not* modify for a production cluster.

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_lc_debug_interval -1
ceph config get client.rgw rgw_lc_debug_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`-1`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**Signals:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_lc_list_cnt

| | |
|---|---|
| Type | Uint · default `1000` · **Dev** |
| Table | [rgw.md#SP_rgw_lc_list_cnt](../../config/rgw/rgw.md#SP_rgw_lc_list_cnt) |

**What it does:** The count of number of objects in per listing of lc processing from each bucket.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_lc_list_cnt 1000
ceph config get client.rgw rgw_lc_list_cnt
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_lc_list_cnt
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

**Bounds:** min `100`, max `—`.

---

### rgw_lc_lock_max_time

| | |
|---|---|
| Type | Int · default `90` · **Dev** |
| Table | [rgw.md#SP_rgw_lc_lock_max_time](../../config/rgw/rgw.md#SP_rgw_lc_lock_max_time) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_lc_lock_max_time 90
ceph config get client.rgw rgw_lc_lock_max_time
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `90` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_lc_max_objs

| | |
|---|---|
| Type | Int · default `32` · **Advanced** |
| Table | [rgw.md#SP_rgw_lc_max_objs](../../config/rgw/rgw.md#SP_rgw_lc_max_objs) |

**What it does:** Number of lifecycle data shards

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_lc_max_objs 32
ceph config get client.rgw rgw_lc_max_objs
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `32` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_lc_max_rules

| | |
|---|---|
| Type | Uint · default `1000` · **Advanced** |
| Table | [rgw.md#SP_rgw_lc_max_rules](../../config/rgw/rgw.md#SP_rgw_lc_max_rules) |

**What it does:** Max number of lifecycle rules set on one bucket

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_lc_max_rules 1000
ceph config get client.rgw rgw_lc_max_rules
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_lc_max_worker

| | |
|---|---|
| Type | Int · default `3` · **Advanced** |
| Table | [rgw.md#SP_rgw_lc_max_worker](../../config/rgw/rgw.md#SP_rgw_lc_max_worker) |

**What it does:** Number of LCWorker tasks that will be run in parallel

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_lc_max_worker 3
ceph config get client.rgw rgw_lc_max_worker
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_lc_max_worker
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_lc_max_wp_worker

| | |
|---|---|
| Type | Int · default `128` · **Advanced** |
| Table | [rgw.md#SP_rgw_lc_max_wp_worker](../../config/rgw/rgw.md#SP_rgw_lc_max_wp_worker) |

**What it does:** Number of workpool coroutines per LCWorker

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_lc_max_wp_worker 128
ceph config get client.rgw rgw_lc_max_wp_worker
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `128` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_lc_ordered_list_threshold

| | |
|---|---|
| Type | Uint · default `500` · **Dev** |
| Table | [rgw.md#SP_rgw_lc_ordered_list_threshold](../../config/rgw/rgw.md#SP_rgw_lc_ordered_list_threshold) |

**What it does:** Threshold for enabling ordered listing in lifecycle processing.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_lc_ordered_list_threshold 500
ceph config get client.rgw rgw_lc_ordered_list_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_lc_ordered_list_threshold
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

**Bounds:** min `0`, max `—`.

---

### rgw_lc_thread_delay

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_lc_thread_delay](../../config/rgw/rgw.md#SP_rgw_lc_thread_delay) |

**What it does:** Delay after processing of bucket listing chunks (i.e., per 1000 entries) in milliseconds

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_lc_thread_delay 0
ceph config get client.rgw rgw_lc_thread_delay
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_lc_thread_delay
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](OVERVIEW.md)
