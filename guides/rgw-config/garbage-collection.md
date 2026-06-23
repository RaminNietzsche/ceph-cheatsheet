# Garbage collection

RGW config deep dive — 7 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_gc_max_concurrent_io](#rgw_gc_max_concurrent_io) | `10` | Advanced |
| [rgw_gc_max_objs](#rgw_gc_max_objs) | `32` | Advanced |
| [rgw_gc_max_queue_size](#rgw_gc_max_queue_size) | `131071_K` | Advanced |
| [rgw_gc_max_trim_chunk](#rgw_gc_max_trim_chunk) | `16` | Advanced |
| [rgw_gc_obj_min_wait](#rgw_gc_obj_min_wait) | `2_hr` | Advanced |
| [rgw_gc_processor_max_time](#rgw_gc_processor_max_time) | `1_hr` | Advanced |
| [rgw_gc_processor_period](#rgw_gc_processor_period) | `1_hr` | Advanced |

---

### rgw_gc_max_concurrent_io

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [rgw.md#SP_rgw_gc_max_concurrent_io](../../config/rgw/rgw.md#SP_rgw_gc_max_concurrent_io) |

**What it does:** Max concurrent RADOS IO operations for garbage collection

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_gc_max_concurrent_io 10
ceph config get client.rgw rgw_gc_max_concurrent_io
```

**Finding optimal value:** Performance sweep: baseline at default, then increase in steps while watching RGW CPU, request p99, and OSD slow ops. Optimal is the highest value before OSD or network saturation. Default: `10`.

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

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`32`) matches S3 compatibility for most workloads.

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

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`131071_K`) matches S3 compatibility for most workloads.

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

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`16`) matches S3 compatibility for most workloads.

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

**Finding optimal value:** Start from upstream default (`2_hr`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`1_hr`) matches S3 compatibility for most workloads.

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

**Finding optimal value:** Lower for fresher behavior / faster reaction; higher to reduce background load. Adjust from default (`1_hr`) only when logs show sync, cache, or timeout issues.

---


[← RGW config overview](OVERVIEW.md)
