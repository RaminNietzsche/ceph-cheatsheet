# NFS gateway

RGW config deep dive — 14 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_nfs_fhcache_partitions](#rgw_nfs_fhcache_partitions) | `3` | Advanced | Performance |
| [rgw_nfs_fhcache_size](#rgw_nfs_fhcache_size) | `2017` | Advanced | Performance |
| [rgw_nfs_frontends](#rgw_nfs_frontends) | `rgw-nfs` | Basic | Performance |
| [rgw_nfs_lru_lane_hiwat](#rgw_nfs_lru_lane_hiwat) | `911` | Advanced | Performance |
| [rgw_nfs_lru_lanes](#rgw_nfs_lru_lanes) | `5` | Advanced | Performance |
| [rgw_nfs_max_gc](#rgw_nfs_max_gc) | `5_min` | Advanced | Policy |
| [rgw_nfs_namespace_expire_secs](#rgw_nfs_namespace_expire_secs) | `5_min` | Advanced | Performance |
| [rgw_nfs_run_gc_threads](#rgw_nfs_run_gc_threads) | `False` | Advanced | Policy |
| [rgw_nfs_run_lc_threads](#rgw_nfs_run_lc_threads) | `False` | Advanced | Policy |
| [rgw_nfs_run_quota_threads](#rgw_nfs_run_quota_threads) | `True` | Advanced | Policy |
| [rgw_nfs_run_restore_threads](#rgw_nfs_run_restore_threads) | `False` | Advanced | Policy |
| [rgw_nfs_run_sync_thread](#rgw_nfs_run_sync_thread) | `False` | Advanced | Policy |
| [rgw_nfs_s3_fast_attrs](#rgw_nfs_s3_fast_attrs) | `False` | Advanced | Policy |
| [rgw_nfs_write_completion_interval_s](#rgw_nfs_write_completion_interval_s) | `10` | Advanced | Performance |

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

### rgw_nfs_fhcache_partitions

| | |
|---|---|
| Type | Int · default `3` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_fhcache_partitions](../../../config/rgw/rgw.md#SP_rgw_nfs_fhcache_partitions) |

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_fhcache_partitions 3
ceph config get client.rgw rgw_nfs_fhcache_partitions
```

**Finding optimal value:**

**Tuning model:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `3`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**Signals:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_nfs_fhcache_partitions
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_nfs_fhcache_size

| | |
|---|---|
| Type | Int · default `2017` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_fhcache_size](../../../config/rgw/rgw.md#SP_rgw_nfs_fhcache_size) |

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_fhcache_size 2017
ceph config get client.rgw rgw_nfs_fhcache_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `2017`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**Signals:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_nfs_fhcache_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_nfs_frontends

| | |
|---|---|
| Type | Str · default `rgw-nfs` · **Basic** |
| Table | [rgw.md#SP_rgw_nfs_frontends](../../../config/rgw/rgw.md#SP_rgw_nfs_frontends) |

**What it does:** RGW frontends configuration when running as librgw/nfs A comma-delimited list of frontends configuration. Each configuration contains the type of the frontend followed by an optional space delimited set of key=value config parameters.

**When to use:** Core RGW behavior — review before changing in production.

**Related options:**

- [`rgw_frontends`](../../../config/rgw/rgw.md#SP_rgw_frontends)

**Example:**

```bash
ceph config set client.rgw rgw_nfs_frontends "rgw-nfs"
ceph config get client.rgw rgw_nfs_frontends
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `rgw-nfs`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_nfs_frontends
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_nfs_lru_lane_hiwat

| | |
|---|---|
| Type | Int · default `911` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_lru_lane_hiwat](../../../config/rgw/rgw.md#SP_rgw_nfs_lru_lane_hiwat) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_lru_lane_hiwat 911
ceph config get client.rgw rgw_nfs_lru_lane_hiwat
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `911`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_nfs_lru_lane_hiwat
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_nfs_lru_lanes

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_lru_lanes](../../../config/rgw/rgw.md#SP_rgw_nfs_lru_lanes) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_lru_lanes 5
ceph config get client.rgw rgw_nfs_lru_lanes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_nfs_lru_lanes
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_nfs_max_gc

| | |
|---|---|
| Type | Int · default `5_min` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_max_gc](../../../config/rgw/rgw.md#SP_rgw_nfs_max_gc) |

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_max_gc 5_min
ceph config get client.rgw rgw_nfs_max_gc
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `5_min` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

**Bounds:** min `1`, max `—`.

---

### rgw_nfs_namespace_expire_secs

| | |
|---|---|
| Type | Int · default `5_min` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_namespace_expire_secs](../../../config/rgw/rgw.md#SP_rgw_nfs_namespace_expire_secs) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_namespace_expire_secs 5_min
ceph config get client.rgw rgw_nfs_namespace_expire_secs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5_min`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_nfs_namespace_expire_secs
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**Bounds:** min `1`, max `—`.

---

### rgw_nfs_run_gc_threads

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_run_gc_threads](../../../config/rgw/rgw.md#SP_rgw_nfs_run_gc_threads) |

**What it does:** run GC threads in librgw (default off)

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_run_gc_threads true
ceph config get client.rgw rgw_nfs_run_gc_threads
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_nfs_run_lc_threads

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_run_lc_threads](../../../config/rgw/rgw.md#SP_rgw_nfs_run_lc_threads) |

**What it does:** run lifecycle threads in librgw (default off)

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_run_lc_threads true
ceph config get client.rgw rgw_nfs_run_lc_threads
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_nfs_run_quota_threads

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_run_quota_threads](../../../config/rgw/rgw.md#SP_rgw_nfs_run_quota_threads) |

**What it does:** run quota threads in librgw (default on)

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_run_quota_threads false
ceph config get client.rgw rgw_nfs_run_quota_threads
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_nfs_run_restore_threads

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_run_restore_threads](../../../config/rgw/rgw.md#SP_rgw_nfs_run_restore_threads) |

**What it does:** run objects' restore threads in librgw (default off)

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_run_restore_threads true
ceph config get client.rgw rgw_nfs_run_restore_threads
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_nfs_run_sync_thread

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_run_sync_thread](../../../config/rgw/rgw.md#SP_rgw_nfs_run_sync_thread) |

**What it does:** run sync thread in librgw (default off)

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_run_sync_thread true
ceph config get client.rgw rgw_nfs_run_sync_thread
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_nfs_s3_fast_attrs

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_s3_fast_attrs](../../../config/rgw/rgw.md#SP_rgw_nfs_s3_fast_attrs) |

**What it does:** use fast S3 attrs from bucket index (immutable only) use fast S3 attrs from bucket index (assumes NFS mounts are immutable)

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_s3_fast_attrs true
ceph config get client.rgw rgw_nfs_s3_fast_attrs
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_nfs_write_completion_interval_s

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [rgw.md#SP_rgw_nfs_write_completion_interval_s](../../../config/rgw/rgw.md#SP_rgw_nfs_write_completion_interval_s) |

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_nfs_write_completion_interval_s 10
ceph config get client.rgw rgw_nfs_write_completion_interval_s
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `10` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_nfs_write_completion_interval_s
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](../OVERVIEW.md)
