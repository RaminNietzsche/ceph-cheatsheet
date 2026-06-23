# NFS gateway

deep dive پیکربندی RGW — 14 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
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

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **Policy** | امنیت، سازگاری API، محدودیت tenant |
| **Capacity** | چیدمان دیسک، مسیرها، اندازه pool |
| **Performance** | خط پایه → تغییر تدریجی → پایش OSD/RGW |
| **Connectivity** | نزدیک‌ترین endpoint پایدار خارجی |
| **Architecture** | backend، توپولوژی multisite — نه sweep عددی |
| **Dev** | پیش‌فرض upstream در production |

**ابزارهای مشترک:**

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
| نوع | Int · default `3` · **Advanced** |
| جدول | [rgw.md#SP_rgw_nfs_fhcache_partitions](../../../config/rgw/rgw.md#SP_rgw_nfs_fhcache_partitions) |

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**مثال:**

```bash
ceph config set client.rgw rgw_nfs_fhcache_partitions 3
ceph config get client.rgw rgw_nfs_fhcache_partitions
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `3`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**سیگنال‌ها:** rising RGW memory, repeated metadata lookups in logs.

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
| نوع | Int · default `2017` · **Advanced** |
| جدول | [rgw.md#SP_rgw_nfs_fhcache_size](../../../config/rgw/rgw.md#SP_rgw_nfs_fhcache_size) |

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**مثال:**

```bash
ceph config set client.rgw rgw_nfs_fhcache_size 2017
ceph config get client.rgw rgw_nfs_fhcache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `2017`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**سیگنال‌ها:** rising RGW memory, repeated metadata lookups in logs.

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
| نوع | Str · default `rgw-nfs` · **Basic** |
| جدول | [rgw.md#SP_rgw_nfs_frontends](../../../config/rgw/rgw.md#SP_rgw_nfs_frontends) |

**کارکرد:** RGW frontends configuration when running as librgw/nfs

**زمان استفاده:** رفتار اصلی RGW — قبل از تغییر در production بررسی کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_nfs_frontends "rgw-nfs"
ceph config get client.rgw rgw_nfs_frontends
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `rgw-nfs`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| نوع | Int · default `911` · **Advanced** |
| جدول | [rgw.md#SP_rgw_nfs_lru_lane_hiwat](../../../config/rgw/rgw.md#SP_rgw_nfs_lru_lane_hiwat) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_nfs_lru_lane_hiwat 911
ceph config get client.rgw rgw_nfs_lru_lane_hiwat
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `911`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| نوع | Int · default `5` · **Advanced** |
| جدول | [rgw.md#SP_rgw_nfs_lru_lanes](../../../config/rgw/rgw.md#SP_rgw_nfs_lru_lanes) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_nfs_lru_lanes 5
ceph config get client.rgw rgw_nfs_lru_lanes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| نوع | Int · default `5_min` · **Advanced** |
| جدول | [rgw.md#SP_rgw_nfs_max_gc](../../../config/rgw/rgw.md#SP_rgw_nfs_max_gc) |

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه/concurrency می‌رسند یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_nfs_max_gc 5_min
ceph config get client.rgw rgw_nfs_max_gc
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `5_min` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

**محدوده:** min `1`, max `—`.

---

### rgw_nfs_namespace_expire_secs

| | |
|---|---|
| نوع | Int · default `5_min` · **Advanced** |
| جدول | [rgw.md#SP_rgw_nfs_namespace_expire_secs](../../../config/rgw/rgw.md#SP_rgw_nfs_namespace_expire_secs) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_nfs_namespace_expire_secs 5_min
ceph config get client.rgw rgw_nfs_namespace_expire_secs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `5_min`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_nfs_namespace_expire_secs
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**محدوده:** min `1`, max `—`.

---

### rgw_nfs_run_gc_threads

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_nfs_run_gc_threads](../../../config/rgw/rgw.md#SP_rgw_nfs_run_gc_threads) |

**کارکرد:** run GC threads in librgw (default off)

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_nfs_run_gc_threads true
ceph config get client.rgw rgw_nfs_run_gc_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_nfs_run_lc_threads

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_nfs_run_lc_threads](../../../config/rgw/rgw.md#SP_rgw_nfs_run_lc_threads) |

**کارکرد:** run lifecycle threads in librgw (default off)

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_nfs_run_lc_threads true
ceph config get client.rgw rgw_nfs_run_lc_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_nfs_run_quota_threads

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_nfs_run_quota_threads](../../../config/rgw/rgw.md#SP_rgw_nfs_run_quota_threads) |

**کارکرد:** run quota threads in librgw (default on)

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_nfs_run_quota_threads false
ceph config get client.rgw rgw_nfs_run_quota_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_nfs_run_restore_threads

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_nfs_run_restore_threads](../../../config/rgw/rgw.md#SP_rgw_nfs_run_restore_threads) |

**کارکرد:** run objects' restore threads in librgw (default off)

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_nfs_run_restore_threads true
ceph config get client.rgw rgw_nfs_run_restore_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_nfs_run_sync_thread

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_nfs_run_sync_thread](../../../config/rgw/rgw.md#SP_rgw_nfs_run_sync_thread) |

**کارکرد:** run sync thread in librgw (default off)

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_nfs_run_sync_thread true
ceph config get client.rgw rgw_nfs_run_sync_thread
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_nfs_s3_fast_attrs

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_nfs_s3_fast_attrs](../../../config/rgw/rgw.md#SP_rgw_nfs_s3_fast_attrs) |

**کارکرد:** use fast S3 attrs from bucket index (immutable only)

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_nfs_s3_fast_attrs true
ceph config get client.rgw rgw_nfs_s3_fast_attrs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_nfs_write_completion_interval_s

| | |
|---|---|
| نوع | Int · default `10` · **Advanced** |
| جدول | [rgw.md#SP_rgw_nfs_write_completion_interval_s](../../../config/rgw/rgw.md#SP_rgw_nfs_write_completion_interval_s) |

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_nfs_write_completion_interval_s 10
ceph config get client.rgw rgw_nfs_write_completion_interval_s
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `10` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_nfs_write_completion_interval_s
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
