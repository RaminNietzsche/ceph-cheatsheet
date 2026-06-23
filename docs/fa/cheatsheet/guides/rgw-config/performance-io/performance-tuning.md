# Concurrency & RADOS I/O

راهنمای عمیق پیکربندی RGW — 14 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_list_bucket_min_readahead](#rgw_list_bucket_min_readahead) | `1000` | Advanced | عملکرد |
| [rgw_max_concurrent_requests](#rgw_max_concurrent_requests) | `1024` | Basic | عملکرد |
| [rgw_max_copy_obj_concurrent_io](#rgw_max_copy_obj_concurrent_io) | `10` | Advanced | عملکرد |
| [rgw_max_objs_per_shard](#rgw_max_objs_per_shard) | `100000` | Basic | سیاست |
| [rgw_multi_obj_del_max_aio](#rgw_multi_obj_del_max_aio) | `16` | Advanced | عملکرد |
| [rgw_num_async_rados_threads](#rgw_num_async_rados_threads) | `32` | Advanced | عملکرد |
| [rgw_num_control_oids](#rgw_num_control_oids) | `8` | Advanced | سیاست |
| [rgw_obj_stripe_size](#rgw_obj_stripe_size) | `4_M` | Advanced | عملکرد |
| [rgw_op_thread_suicide_timeout](#rgw_op_thread_suicide_timeout) | `0` | Dev | توسعه |
| [rgw_op_thread_timeout](#rgw_op_thread_timeout) | `10_min` | Dev | توسعه |
| [rgw_redis_connection_pool_size](#rgw_redis_connection_pool_size) | `512` | Basic | عملکرد |
| [rgw_restore_max_objs](#rgw_restore_max_objs) | `32` | Advanced | سیاست |
| [rgw_restore_processor_period](#rgw_restore_processor_period) | `15_min` | Advanced | عملکرد |
| [rgw_thread_pool_size](#rgw_thread_pool_size) | `512` | Basic | عملکرد |

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

### rgw_list_bucket_min_readahead

| | |
|---|---|
| نوع | Int · default `1000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_list_bucket_min_readahead](../../../config/rgw/rgw.md#SP_rgw_list_bucket_min_readahead) |

**کارکرد:** Minimum number of entries to request from rados for bucket listing

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_list_bucket_min_readahead 1000
ceph config get client.rgw rgw_list_bucket_min_readahead
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_list_bucket_min_readahead
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_max_concurrent_requests

| | |
|---|---|
| نوع | Int · default `1024` · **Basic** |
| جدول | [rgw.md#SP_rgw_max_concurrent_requests](../../../config/rgw/rgw.md#SP_rgw_max_concurrent_requests) |

**کارکرد:** Maximum number of concurrent HTTP requests.

**زمان استفاده:**

- **Increase** when RGW queues requests but CPU is not saturated.
- **Decrease** when latency spikes or CPU context-switch overhead grows.

**مثال:**

```bash
ceph config set client.rgw rgw_max_concurrent_requests 1024
ceph config get client.rgw rgw_max_concurrent_requests
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at `1024` under peak concurrent clients.
2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.
3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.
4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.

**سیگنال‌ها:** 503/slowdown responses, high `active_requests` vs `max_concurrent`.

```bash
ceph config get client.rgw rgw_max_concurrent_requests
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_max_copy_obj_concurrent_io

| | |
|---|---|
| نوع | Int · default `10` · **Advanced** |
| جدول | [rgw.md#SP_rgw_max_copy_obj_concurrent_io](../../../config/rgw/rgw.md#SP_rgw_max_copy_obj_concurrent_io) |

**کارکرد:** Number of refcount operations to process concurrently when executing copy_obj

**زمان استفاده:**

- **Increase** when RGW queues requests but CPU is not saturated.
- **Decrease** when latency spikes or CPU context-switch overhead grows.

**مثال:**

```bash
ceph config set client.rgw rgw_max_copy_obj_concurrent_io 10
ceph config get client.rgw rgw_max_copy_obj_concurrent_io
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at `10` under peak concurrent clients.
2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.
3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.
4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.

**سیگنال‌ها:** 503/slowdown responses, high `active_requests` vs `max_concurrent`.

```bash
ceph config get client.rgw rgw_max_copy_obj_concurrent_io
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_max_objs_per_shard

| | |
|---|---|
| نوع | Uint · default `100000` · **Basic** |
| جدول | [rgw.md#SP_rgw_max_objs_per_shard](../../../config/rgw/rgw.md#SP_rgw_max_objs_per_shard) |

**کارکرد:** Max objects per shard for dynamic resharding

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_max_objs_per_shard 100000
ceph config get client.rgw rgw_max_objs_per_shard
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `100000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_multi_obj_del_max_aio

| | |
|---|---|
| نوع | Uint · default `16` · **Advanced** |
| جدول | [rgw.md#SP_rgw_multi_obj_del_max_aio](../../../config/rgw/rgw.md#SP_rgw_multi_obj_del_max_aio) |

**کارکرد:** Max number of concurrent RADOS requests per multi-object delete request.

**زمان استفاده:**

- **Increase** when listings/deletes on sharded buckets are slow and OSDs have headroom.
- **Decrease** when bucket-index pools show sustained load spikes or slow ops.

**مثال:**

```bash
ceph config set client.rgw rgw_multi_obj_del_max_aio 16
ceph config get client.rgw rgw_multi_obj_del_max_aio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at `16` with large bucket LIST, bulk DELETE, multipart completion.
2. Watch list/delete p99, RGW CPU, and OSD slow ops.
3. Increase in steps (~25%: e.g. 128 → 160 → 192 → 256) until latency stops improving.
4. **Decrease** under recovery pressure, `nearfull`, or sustained bucket-index pool load.

**سیگنال‌ها:** OSD `slow requests`, rising `rgw` throttle counters, flat client throughput.

```bash
ceph config get client.rgw rgw_multi_obj_del_max_aio
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
radosgw-admin bucket stats --bucket=BIG_BUCKET | jq '.num_shards'
```

---

### rgw_num_async_rados_threads

| | |
|---|---|
| نوع | Int · default `32` · **Advanced** |
| جدول | [rgw.md#SP_rgw_num_async_rados_threads](../../../config/rgw/rgw.md#SP_rgw_num_async_rados_threads) |

**کارکرد:** Number of concurrent RADOS operations in multisite sync

**زمان استفاده:** تنظیم replication و sync در محیط چندسایته — وقتی تأخیر (lag) یا بار sync مشکل‌ساز است.

**مثال:**

```bash
ceph config set client.rgw rgw_num_async_rados_threads 32
ceph config get client.rgw rgw_num_async_rados_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at `32` under peak concurrent clients.
2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.
3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.
4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.

**سیگنال‌ها:** 503/slowdown responses, high `active_requests` vs `max_concurrent`.

```bash
ceph config get client.rgw rgw_num_async_rados_threads
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_num_control_oids

| | |
|---|---|
| نوع | Int · default `8` · **Advanced** |
| جدول | [rgw.md#SP_rgw_num_control_oids](../../../config/rgw/rgw.md#SP_rgw_num_control_oids) |

**کارکرد:** Number of control objects used for cross-RGW communication.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_num_control_oids 8
ceph config get client.rgw rgw_num_control_oids
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `8` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_obj_stripe_size

| | |
|---|---|
| نوع | Size · default `4_M` · **Advanced** |
| جدول | [rgw.md#SP_rgw_obj_stripe_size](../../../config/rgw/rgw.md#SP_rgw_obj_stripe_size) |

**کارکرد:** RGW object stripe size

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_obj_stripe_size 4_M
ceph config get client.rgw rgw_obj_stripe_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline `4_M` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**سیگنال‌ها:** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_obj_stripe_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_op_thread_suicide_timeout

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [rgw.md#SP_rgw_op_thread_suicide_timeout](../../../config/rgw/rgw.md#SP_rgw_op_thread_suicide_timeout) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_op_thread_suicide_timeout 60
ceph config get client.rgw rgw_op_thread_suicide_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_op_thread_timeout

| | |
|---|---|
| نوع | Int · default `10_min` · **Dev** |
| جدول | [rgw.md#SP_rgw_op_thread_timeout](../../../config/rgw/rgw.md#SP_rgw_op_thread_timeout) |

**کارکرد:** Timeout for async rados coroutine operations.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_op_thread_timeout 10_min
ceph config get client.rgw rgw_op_thread_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`10_min`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_redis_connection_pool_size

| | |
|---|---|
| نوع | Int · default `512` · **Basic** |
| جدول | [rgw.md#SP_rgw_redis_connection_pool_size](../../../config/rgw/rgw.md#SP_rgw_redis_connection_pool_size) |

**کارکرد:** RGW connection pool size for Redis operation per D4N

**زمان استفاده:** رفتار اصلی RGW — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_redis_connection_pool_size 512
ceph config get client.rgw rgw_redis_connection_pool_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `512`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_redis_connection_pool_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_restore_max_objs

| | |
|---|---|
| نوع | Int · default `32` · **Advanced** |
| جدول | [rgw.md#SP_rgw_restore_max_objs](../../../config/rgw/rgw.md#SP_rgw_restore_max_objs) |

**کارکرد:** Number of shards for restore processing

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_restore_max_objs 32
ceph config get client.rgw rgw_restore_max_objs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `32` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_restore_processor_period

| | |
|---|---|
| نوع | Int · default `15_min` · **Advanced** |
| جدول | [rgw.md#SP_rgw_restore_processor_period](../../../config/rgw/rgw.md#SP_rgw_restore_processor_period) |

**کارکرد:** Restore cycle run time

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_restore_processor_period 15_min
ceph config get client.rgw rgw_restore_processor_period
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `15_min` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_restore_processor_period
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_thread_pool_size

| | |
|---|---|
| نوع | Int · default `512` · **Basic** |
| جدول | [rgw.md#SP_rgw_thread_pool_size](../../../config/rgw/rgw.md#SP_rgw_thread_pool_size) |

**کارکرد:** RGW requests handling thread pool size.

**زمان استفاده:**

- **Increase** when RGW queues requests but CPU is not saturated.
- **Decrease** when latency spikes or CPU context-switch overhead grows.

**مثال:**

```bash
ceph config set client.rgw rgw_thread_pool_size 512
ceph config get client.rgw rgw_thread_pool_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at `512` under peak concurrent clients.
2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.
3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.
4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.

**سیگنال‌ها:** 503/slowdown responses, high `active_requests` vs `max_concurrent`.

```bash
ceph config get client.rgw rgw_thread_pool_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
