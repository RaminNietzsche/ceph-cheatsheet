# Lifecycle (LC)

راهنمای عمیق پیکربندی RGW — 17 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
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
| [rgw_lifecycle_work_time](#rgw_lifecycle_work_time) | `00:00-06:00` | Advanced | Performance |
| [rgw_mp_lock_max_time](#rgw_mp_lock_max_time) | `10_min` | Advanced | Policy |
| [rgw_restore_lock_max_time](#rgw_restore_lock_max_time) | `90` | Dev | Policy |
| [rgwlc_auto_session_clear](#rgwlc_auto_session_clear) | `True` | Advanced | Policy |
| [rgwlc_skip_bucket_step](#rgwlc_skip_bucket_step) | `False` | Advanced | Policy |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **Policy** | امنیت، سازگاری API، محدودیت tenant |
| **Capacity** | چیدمان دیسک، مسیرها، اندازه pool |
| **Performance** | خط پایه → تغییر تدریجی → پایش OSD/RGW |
| **Connectivity** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **Architecture** | backend، توپولوژی چندسایته — نه جستجوی عددی |
| **Dev** | در محیط عملیاتی همان پیش‌فرض upstream |

**ابزارهای مشترک:**

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
| نوع | Uint · default `5000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_lc_counters_batch_size](../../../config/rgw/rgw.md#SP_rgw_lc_counters_batch_size) |

**کارکرد:** Batch size for flushing LC per-bucket counters

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_lc_counters_batch_size 5000
ceph config get client.rgw rgw_lc_counters_batch_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `5000`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_lc_counters_batch_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**محدوده:** min `1`, max `—`.

---

### rgw_lc_counters_cache

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_lc_counters_cache](../../../config/rgw/rgw.md#SP_rgw_lc_counters_cache) |

**کارکرد:** Enable per-bucket lifecycle performance counters cache

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_lc_counters_cache true
ceph config get client.rgw rgw_lc_counters_cache
ceph config set client.rgw rgw_lc_counters_cache_size 20000
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `False` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_lc_counters_cache_size

| | |
|---|---|
| نوع | Uint · default `10000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_lc_counters_cache_size](../../../config/rgw/rgw.md#SP_rgw_lc_counters_cache_size) |

**کارکرد:** Target size for lifecycle counters cache

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**مثال:**

```bash
ceph config set client.rgw rgw_lc_counters_cache_size 10000
ceph config get client.rgw rgw_lc_counters_cache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**سیگنال‌ها:** rising RGW memory, repeated metadata lookups in logs.

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
| نوع | Int · default `-1` · **Dev** |
| جدول | [rgw.md#SP_rgw_lc_debug_interval](../../../config/rgw/rgw.md#SP_rgw_lc_debug_interval) |

**کارکرد:** The number of seconds that simulate one "day" in order to debug RGW LifeCycle. Do *not* modify for a production cluster.

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_lc_debug_interval -1
ceph config get client.rgw rgw_lc_debug_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`-1`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_lc_list_cnt

| | |
|---|---|
| نوع | Uint · default `1000` · **Dev** |
| جدول | [rgw.md#SP_rgw_lc_list_cnt](../../../config/rgw/rgw.md#SP_rgw_lc_list_cnt) |

**کارکرد:** The count of number of objects in per listing of lc processing from each bucket.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_lc_list_cnt 1000
ceph config get client.rgw rgw_lc_list_cnt
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_lc_list_cnt
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**محدوده:** min `100`, max `—`.

---

### rgw_lc_lock_max_time

| | |
|---|---|
| نوع | Int · default `90` · **Dev** |
| جدول | [rgw.md#SP_rgw_lc_lock_max_time](../../../config/rgw/rgw.md#SP_rgw_lc_lock_max_time) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_lc_lock_max_time 90
ceph config get client.rgw rgw_lc_lock_max_time
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `90` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_lc_max_objs

| | |
|---|---|
| نوع | Int · default `32` · **Advanced** |
| جدول | [rgw.md#SP_rgw_lc_max_objs](../../../config/rgw/rgw.md#SP_rgw_lc_max_objs) |

**کارکرد:** Number of lifecycle data shards

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_lc_max_objs 32
ceph config get client.rgw rgw_lc_max_objs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `32` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_lc_max_rules

| | |
|---|---|
| نوع | Uint · default `1000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_lc_max_rules](../../../config/rgw/rgw.md#SP_rgw_lc_max_rules) |

**کارکرد:** Max number of lifecycle rules set on one bucket

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_lc_max_rules 1000
ceph config get client.rgw rgw_lc_max_rules
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_lc_max_worker

| | |
|---|---|
| نوع | Int · default `3` · **Advanced** |
| جدول | [rgw.md#SP_rgw_lc_max_worker](../../../config/rgw/rgw.md#SP_rgw_lc_max_worker) |

**کارکرد:** Number of LCWorker tasks that will be run in parallel

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_lc_max_worker 3
ceph config get client.rgw rgw_lc_max_worker
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| نوع | Int · default `128` · **Advanced** |
| جدول | [rgw.md#SP_rgw_lc_max_wp_worker](../../../config/rgw/rgw.md#SP_rgw_lc_max_wp_worker) |

**کارکرد:** Number of workpool coroutines per LCWorker

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_lc_max_wp_worker 128
ceph config get client.rgw rgw_lc_max_wp_worker
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `128` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_lc_ordered_list_threshold

| | |
|---|---|
| نوع | Uint · default `500` · **Dev** |
| جدول | [rgw.md#SP_rgw_lc_ordered_list_threshold](../../../config/rgw/rgw.md#SP_rgw_lc_ordered_list_threshold) |

**کارکرد:** Threshold for enabling ordered listing in lifecycle processing.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_lc_ordered_list_threshold 500
ceph config get client.rgw rgw_lc_ordered_list_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_lc_ordered_list_threshold
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**محدوده:** min `0`, max `—`.

---

### rgw_lc_thread_delay

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [rgw.md#SP_rgw_lc_thread_delay](../../../config/rgw/rgw.md#SP_rgw_lc_thread_delay) |

**کارکرد:** Delay after processing of bucket listing chunks (i.e., per 1000 entries) in milliseconds

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_lc_thread_delay 0
ceph config get client.rgw rgw_lc_thread_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| نوع | Str · default `00:00-06:00` · **Advanced** |
| جدول | [rgw.md#SP_rgw_lifecycle_work_time](../../../config/rgw/rgw.md#SP_rgw_lifecycle_work_time) |

**کارکرد:** Lifecycle allowed work time

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_lifecycle_work_time "00:00-06:00"
ceph config get client.rgw rgw_lifecycle_work_time
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `00:00-06:00`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| نوع | Int · default `10_min` · **Advanced** |
| جدول | [rgw.md#SP_rgw_mp_lock_max_time](../../../config/rgw/rgw.md#SP_rgw_mp_lock_max_time) |

**کارکرد:** Multipart upload max completion time

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_mp_lock_max_time 10_min
ceph config get client.rgw rgw_mp_lock_max_time
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `10_min` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

**محدوده:** min `2_min`, max `—`.

---

### rgw_restore_lock_max_time

| | |
|---|---|
| نوع | Int · default `90` · **Dev** |
| جدول | [rgw.md#SP_rgw_restore_lock_max_time](../../../config/rgw/rgw.md#SP_rgw_restore_lock_max_time) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_restore_lock_max_time 90
ceph config get client.rgw rgw_restore_lock_max_time
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `90` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgwlc_auto_session_clear

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgwlc.md#SP_rgwlc_auto_session_clear](../../../config/rgw/rgwlc.md#SP_rgwlc_auto_session_clear) |

**کارکرد:** Automatically clear stale lifecycle sessions (i.e., after 2 idle processing cycles)

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgwlc_auto_session_clear false
ceph config get client.rgw rgwlc_auto_session_clear
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgwlc_skip_bucket_step

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgwlc.md#SP_rgwlc_skip_bucket_step](../../../config/rgw/rgwlc.md#SP_rgwlc_skip_bucket_step) |

**کارکرد:** Conditionally skip the processing (but not the scheduling) of bucket lifecycle

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgwlc_skip_bucket_step true
ceph config get client.rgw rgwlc_skip_bucket_step
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
