# NFS gateway

RGW config deep dive — 14 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_nfs_fhcache_partitions](#rgw_nfs_fhcache_partitions) | `3` | Advanced |
| [rgw_nfs_fhcache_size](#rgw_nfs_fhcache_size) | `2017` | Advanced |
| [rgw_nfs_frontends](#rgw_nfs_frontends) | `rgw-nfs` | Basic |
| [rgw_nfs_lru_lane_hiwat](#rgw_nfs_lru_lane_hiwat) | `911` | Advanced |
| [rgw_nfs_lru_lanes](#rgw_nfs_lru_lanes) | `5` | Advanced |
| [rgw_nfs_max_gc](#rgw_nfs_max_gc) | `5_min` | Advanced |
| [rgw_nfs_namespace_expire_secs](#rgw_nfs_namespace_expire_secs) | `5_min` | Advanced |
| [rgw_nfs_run_gc_threads](#rgw_nfs_run_gc_threads) | `False` | Advanced |
| [rgw_nfs_run_lc_threads](#rgw_nfs_run_lc_threads) | `False` | Advanced |
| [rgw_nfs_run_quota_threads](#rgw_nfs_run_quota_threads) | `True` | Advanced |
| [rgw_nfs_run_restore_threads](#rgw_nfs_run_restore_threads) | `False` | Advanced |
| [rgw_nfs_run_sync_thread](#rgw_nfs_run_sync_thread) | `False` | Advanced |
| [rgw_nfs_s3_fast_attrs](#rgw_nfs_s3_fast_attrs) | `False` | Advanced |
| [rgw_nfs_write_completion_interval_s](#rgw_nfs_write_completion_interval_s) | `10` | Advanced |

---

### rgw_nfs_fhcache_partitions

| | |
|---|---|
| Type | Int · default `3` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_fhcache_partitions](../../config/rgw/rgw.md#SP_rgw_nfs_fhcache_partitions) |

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_fhcache_partitions 3
ceph config get client.rgw rgw_nfs_fhcache_partitions
```

**Finding optimal value:** Size to active working set (accounts, buckets, or keys you monitor). Sweep around default (`3`) while watching RGW RSS.

---

### rgw_nfs_fhcache_size

| | |
|---|---|
| Type | Int · default `2017` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_fhcache_size](../../config/rgw/rgw.md#SP_rgw_nfs_fhcache_size) |

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_fhcache_size 2017
ceph config get client.rgw rgw_nfs_fhcache_size
```

**Finding optimal value:** Size to active working set (accounts, buckets, or keys you monitor). Sweep around default (`2017`) while watching RGW RSS.

---

### rgw_nfs_frontends

| | |
|---|---|
| Type | Str · default `rgw-nfs` · **Basic** |
| Table | [rgw.md#SP_rgw_nfs_frontends](../../config/rgw/rgw.md#SP_rgw_nfs_frontends) |

**What it does:** RGW frontends configuration when running as librgw/nfs

**When to use:** Core RGW behavior — review before changing in production.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_frontends rgw-nfs
ceph config get client.rgw rgw_nfs_frontends
```

**Finding optimal value:** Start from upstream default (`rgw-nfs`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_nfs_lru_lane_hiwat

| | |
|---|---|
| Type | Int · default `911` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_lru_lane_hiwat](../../config/rgw/rgw.md#SP_rgw_nfs_lru_lane_hiwat) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_lru_lane_hiwat 911
ceph config get client.rgw rgw_nfs_lru_lane_hiwat
```

**Finding optimal value:** Start from upstream default (`911`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_nfs_lru_lanes

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_lru_lanes](../../config/rgw/rgw.md#SP_rgw_nfs_lru_lanes) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_lru_lanes 5
ceph config get client.rgw rgw_nfs_lru_lanes
```

**Finding optimal value:** Start from upstream default (`5`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_nfs_max_gc

| | |
|---|---|
| Type | Int · default `5_min` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_max_gc](../../config/rgw/rgw.md#SP_rgw_nfs_max_gc) |

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_max_gc 5_min
ceph config get client.rgw rgw_nfs_max_gc
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`5_min`) matches S3 compatibility for most workloads. Valid range: min=1, max=—.

---

### rgw_nfs_namespace_expire_secs

| | |
|---|---|
| Type | Int · default `5_min` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_namespace_expire_secs](../../config/rgw/rgw.md#SP_rgw_nfs_namespace_expire_secs) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_namespace_expire_secs 5_min
ceph config get client.rgw rgw_nfs_namespace_expire_secs
```

**Finding optimal value:** Start from upstream default (`5_min`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_nfs_run_gc_threads

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_run_gc_threads](../../config/rgw/rgw.md#SP_rgw_nfs_run_gc_threads) |

**What it does:** run GC threads in librgw (default off)

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_run_gc_threads False
ceph config get client.rgw rgw_nfs_run_gc_threads
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

---

### rgw_nfs_run_lc_threads

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_run_lc_threads](../../config/rgw/rgw.md#SP_rgw_nfs_run_lc_threads) |

**What it does:** run lifecycle threads in librgw (default off)

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_run_lc_threads False
ceph config get client.rgw rgw_nfs_run_lc_threads
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

---

### rgw_nfs_run_quota_threads

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_run_quota_threads](../../config/rgw/rgw.md#SP_rgw_nfs_run_quota_threads) |

**What it does:** run quota threads in librgw (default on)

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_run_quota_threads True
ceph config get client.rgw rgw_nfs_run_quota_threads
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`True`) matches upstream.

---

### rgw_nfs_run_restore_threads

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_run_restore_threads](../../config/rgw/rgw.md#SP_rgw_nfs_run_restore_threads) |

**What it does:** run objects' restore threads in librgw (default off)

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_run_restore_threads False
ceph config get client.rgw rgw_nfs_run_restore_threads
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

---

### rgw_nfs_run_sync_thread

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_run_sync_thread](../../config/rgw/rgw.md#SP_rgw_nfs_run_sync_thread) |

**What it does:** run sync thread in librgw (default off)

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_run_sync_thread False
ceph config get client.rgw rgw_nfs_run_sync_thread
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

---

### rgw_nfs_s3_fast_attrs

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_s3_fast_attrs](../../config/rgw/rgw.md#SP_rgw_nfs_s3_fast_attrs) |

**What it does:** use fast S3 attrs from bucket index (immutable only)

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_s3_fast_attrs False
ceph config get client.rgw rgw_nfs_s3_fast_attrs
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

---

### rgw_nfs_write_completion_interval_s

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_write_completion_interval_s](../../config/rgw/rgw.md#SP_rgw_nfs_write_completion_interval_s) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_write_completion_interval_s 10
ceph config get client.rgw rgw_nfs_write_completion_interval_s
```

**Finding optimal value:** Lower for fresher behavior / faster reaction; higher to reduce background load. Adjust from default (`10`) only when logs show sync, cache, or timeout issues.

---


[← RGW config overview](OVERVIEW.md)
