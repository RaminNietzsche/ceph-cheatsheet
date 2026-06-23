# Garbage collection

RGW config deep dive — 7 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_gc_max_concurrent_io](#rgw_gc_max_concurrent_io) | `10` | Advanced | Performance |
| [rgw_gc_max_objs](#rgw_gc_max_objs) | `32` | Advanced | Policy |
| [rgw_gc_max_queue_size](#rgw_gc_max_queue_size) | `131071_K` | Advanced | Policy |
| [rgw_gc_max_trim_chunk](#rgw_gc_max_trim_chunk) | `16` | Advanced | Policy |
| [rgw_gc_obj_min_wait](#rgw_gc_obj_min_wait) | `2_hr` | Advanced | Performance |
| [rgw_gc_processor_max_time](#rgw_gc_processor_max_time) | `1_hr` | Advanced | Policy |
| [rgw_gc_processor_period](#rgw_gc_processor_period) | `1_hr` | Advanced | Performance |

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

### rgw_gc_max_concurrent_io

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [rgw.md#SP_rgw_gc_max_concurrent_io](../../config/rgw/rgw.md#SP_rgw_gc_max_concurrent_io) |

**What it does:** Max concurrent RADOS IO operations for garbage collection

**When to use:**

- **Increase** when RGW queues requests but CPU is not saturated.
- **Decrease** when latency spikes or CPU context-switch overhead grows.

**Example:**

```bash
ceph config set client.rgw rgw_gc_max_concurrent_io 10
ceph config get client.rgw rgw_gc_max_concurrent_io
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at `10` under peak concurrent clients.
2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.
3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.
4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.

**Signals:** 503/slowdown responses, high `active_requests` vs `max_concurrent`.

```bash
ceph config get client.rgw rgw_gc_max_concurrent_io
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_gc_max_objs

| | |
|---|---|
| Type | Int · default `32` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_gc_max_objs](../../config/rgw/rgw.md#SP_rgw_gc_max_objs) |

**What it does:** Number of shards for garbage collector data

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_gc_max_objs 32
ceph config get client.rgw rgw_gc_max_objs
ceph orch restart rgw
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `32` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_gc_max_queue_size

| | |
|---|---|
| Type | Uint · default `131071_K` · **Advanced** |
| Table | [rgw.md#SP_rgw_gc_max_queue_size](../../config/rgw/rgw.md#SP_rgw_gc_max_queue_size) |

**What it does:** Maximum allowed queue size for gc

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_gc_max_queue_size 131071_K
ceph config get client.rgw rgw_gc_max_queue_size
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `131071_K` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_gc_max_trim_chunk

| | |
|---|---|
| Type | Int · default `16` · **Advanced** |
| Table | [rgw.md#SP_rgw_gc_max_trim_chunk](../../config/rgw/rgw.md#SP_rgw_gc_max_trim_chunk) |

**What it does:** Max number of keys to remove from garbage collector log in a single operation

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_gc_max_trim_chunk 16
ceph config get client.rgw rgw_gc_max_trim_chunk
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `16` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_gc_obj_min_wait

| | |
|---|---|
| Type | Int · default `2_hr` · **Advanced** |
| Table | [rgw.md#SP_rgw_gc_obj_min_wait](../../config/rgw/rgw.md#SP_rgw_gc_obj_min_wait) |

**What it does:** Garbage collection object expiration time

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_gc_obj_min_wait 2_hr
ceph config get client.rgw rgw_gc_obj_min_wait
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2_hr`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_gc_obj_min_wait
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_gc_processor_max_time

| | |
|---|---|
| Type | Int · default `1_hr` · **Advanced** |
| Table | [rgw.md#SP_rgw_gc_processor_max_time](../../config/rgw/rgw.md#SP_rgw_gc_processor_max_time) |

**What it does:** Length of time GC processor can lease shard

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_gc_processor_max_time 1_hr
ceph config get client.rgw rgw_gc_processor_max_time
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `1_hr` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_gc_processor_period

| | |
|---|---|
| Type | Int · default `1_hr` · **Advanced** |
| Table | [rgw.md#SP_rgw_gc_processor_period](../../config/rgw/rgw.md#SP_rgw_gc_processor_period) |

**What it does:** Garbage collector cycle run time

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_gc_processor_period 1_hr
ceph config get client.rgw rgw_gc_processor_period
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `1_hr` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_gc_processor_period
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](OVERVIEW.md)
