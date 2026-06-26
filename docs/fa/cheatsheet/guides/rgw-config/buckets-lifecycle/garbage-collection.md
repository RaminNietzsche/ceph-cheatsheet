# Garbage collection

راهنمای عمیق پیکربندی RGW — 7 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_gc_max_concurrent_io](#rgw_gc_max_concurrent_io) | `10` | Advanced | عملکرد |
| [rgw_gc_max_objs](#rgw_gc_max_objs) | `32` | Advanced | سیاست |
| [rgw_gc_max_queue_size](#rgw_gc_max_queue_size) | `131071_K` | Advanced | سیاست |
| [rgw_gc_max_trim_chunk](#rgw_gc_max_trim_chunk) | `16` | Advanced | سیاست |
| [rgw_gc_obj_min_wait](#rgw_gc_obj_min_wait) | `2_hr` | Advanced | عملکرد |
| [rgw_gc_processor_max_time](#rgw_gc_processor_max_time) | `1_hr` | Advanced | سیاست |
| [rgw_gc_processor_period](#rgw_gc_processor_period) | `1_hr` | Advanced | عملکرد |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **سیاست** | امنیت، سازگاری API، محدودیت tenant |
| **ظرفیت** | چیدمان دیسک، مسیرها، اندازه pool |
| **عملکرد** | خط پایه → تغییر تدریجی → پایش OSD/RGW |
| **اتصال** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **معماری** | backend، توپولوژی چندسایته — نه جستجوی عددی |
| **توسعه** | در محیط عملیاتی همان پیش‌فرض upstream |

**ابزارهای مشترک:**

```bash
ceph config get client.rgw <option>
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph pg stat
```

---

### rgw_gc_max_concurrent_io

| | |
|---|---|
| نوع | Int · default `10` · **Advanced** |
| جدول | [rgw.md#SP_rgw_gc_max_concurrent_io](../../../config/rgw/rgw.md#SP_rgw_gc_max_concurrent_io) |

**کارکرد:** Max concurrent RADOS IO operations for garbage collection The maximum number of concurrent IO operations that the RGW garbage collection thread will use when purging old data.

**زمان استفاده:**

- **Increase** when RGW queues requests but CPU is not saturated.
- **Decrease** when latency spikes or CPU context-switch overhead grows.

**مثال:**

```bash
ceph config set client.rgw rgw_gc_max_concurrent_io 10
ceph config get client.rgw rgw_gc_max_concurrent_io
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at `10` under peak concurrent clients.
2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.
3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.
4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.

**سیگنال‌ها:** 503/slowdown responses, high `active_requests` vs `max_concurrent`.

```bash
ceph config get client.rgw rgw_gc_max_concurrent_io
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_gc_max_objs

| | |
|---|---|
| نوع | Int · default `32` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [rgw.md#SP_rgw_gc_max_objs](../../../config/rgw/rgw.md#SP_rgw_gc_max_objs) |

**کارکرد:** Number of shards for garbage collector data The number of garbage collector data shards, is the number of RADOS objects that RGW will use to store the garbage collection information on. This value is read once at daemon startup.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_gc_max_objs 32
ceph config get client.rgw rgw_gc_max_objs
ceph orch restart rgw
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `32` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_gc_max_queue_size

| | |
|---|---|
| نوع | Uint · default `131071_K` · **Advanced** |
| جدول | [rgw.md#SP_rgw_gc_max_queue_size](../../../config/rgw/rgw.md#SP_rgw_gc_max_queue_size) |

**کارکرد:** Maximum allowed queue size for gc The maximum allowed size of each gc queue, and its value should not be greater than osd_max_object_size - 1K.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_gc_max_queue_size 131071_K
ceph config get client.rgw rgw_gc_max_queue_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `131071_K` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_gc_max_trim_chunk

| | |
|---|---|
| نوع | Int · default `16` · **Advanced** |
| جدول | [rgw.md#SP_rgw_gc_max_trim_chunk](../../../config/rgw/rgw.md#SP_rgw_gc_max_trim_chunk) |

**کارکرد:** Max number of keys to remove from garbage collector log in a single operation

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_gc_max_trim_chunk 16
ceph config get client.rgw rgw_gc_max_trim_chunk
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `16` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_gc_obj_min_wait

| | |
|---|---|
| نوع | Int · default `2_hr` · **Advanced** |
| جدول | [rgw.md#SP_rgw_gc_obj_min_wait](../../../config/rgw/rgw.md#SP_rgw_gc_obj_min_wait) |

**کارکرد:** Garbage collection object expiration time The length of time (in seconds) that the RGW collector will wait before purging a deleted object's data. RGW will not remove object immediately, as object could still have readers. A mechanism exists to increase the object's expiration time when it's being read. The recommended value of its lower limit is 30 minutes

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_gc_obj_min_wait 2_hr
ceph config get client.rgw rgw_gc_obj_min_wait
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `2_hr`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_gc_obj_min_wait
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_gc_processor_max_time

| | |
|---|---|
| نوع | Int · default `1_hr` · **Advanced** |
| جدول | [rgw.md#SP_rgw_gc_processor_max_time](../../../config/rgw/rgw.md#SP_rgw_gc_processor_max_time) |

**کارکرد:** Length of time GC processor can lease shard Garbage collection thread in RGW process holds a lease on its data shards. These objects contain the information about the objects that need to be removed. RGW takes a lease in order to prevent multiple RGW processes from handling the same objects concurrently. This time signifies that maximum amount of time (in seconds) that RGW is allowed to hold that lease. In the case where RGW goes down uncleanly, this is the amount of time where processing of that data shard will be blocked.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_gc_processor_max_time 1_hr
ceph config get client.rgw rgw_gc_processor_max_time
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `1_hr` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_gc_processor_period

| | |
|---|---|
| نوع | Int · default `1_hr` · **Advanced** |
| جدول | [rgw.md#SP_rgw_gc_processor_period](../../../config/rgw/rgw.md#SP_rgw_gc_processor_period) |

**کارکرد:** Garbage collector cycle run time The amount of time between the start of consecutive runs of the garbage collector threads. If garbage collector runs takes more than this period, it will not wait before running again.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_gc_processor_period 1_hr
ceph config get client.rgw rgw_gc_processor_period
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `1_hr` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_gc_processor_period
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
