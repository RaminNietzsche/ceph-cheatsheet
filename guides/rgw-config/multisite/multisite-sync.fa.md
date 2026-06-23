# Replication & sync

deep dive پیکربندی RGW — 28 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_data_log_changes_size](#rgw_data_log_changes_size) | `1000` | Dev | Performance |
| [rgw_data_log_num_shards](#rgw_data_log_num_shards) | `128` | Advanced | Policy |
| [rgw_data_log_window](#rgw_data_log_window) | `30` | Advanced | Performance |
| [rgw_data_notify_interval_msec](#rgw_data_notify_interval_msec) | `0` | Advanced | Performance |
| [rgw_data_sync_poll_interval](#rgw_data_sync_poll_interval) | `20` | Dev | Performance |
| [rgw_data_sync_spawn_window](#rgw_data_sync_spawn_window) | `20` | Dev | Performance |
| [rgw_lfuda_sync_frequency](#rgw_lfuda_sync_frequency) | `60` | Advanced | Performance |
| [rgw_md_log_max_shards](#rgw_md_log_max_shards) | `64` | Advanced | Policy |
| [rgw_md_notify_interval_msec](#rgw_md_notify_interval_msec) | `200` | Advanced | Performance |
| [rgw_meta_sync_poll_interval](#rgw_meta_sync_poll_interval) | `20` | Dev | Performance |
| [rgw_meta_sync_spawn_window](#rgw_meta_sync_spawn_window) | `20` | Dev | Performance |
| [rgw_run_sync_thread](#rgw_run_sync_thread) | `True` | Advanced | Policy |
| [rgw_sync_data_full_inject_err_probability](#rgw_sync_data_full_inject_err_probability) | `0` | Dev | Dev |
| [rgw_sync_data_inject_err_probability](#rgw_sync_data_inject_err_probability) | `0` | Dev | Dev |
| [rgw_sync_lease_period](#rgw_sync_lease_period) | `2_min` | Dev | Performance |
| [rgw_sync_log_trim_concurrent_buckets](#rgw_sync_log_trim_concurrent_buckets) | `4` | Advanced | Performance |
| [rgw_sync_log_trim_interval](#rgw_sync_log_trim_interval) | `20_min` | Advanced | Performance |
| [rgw_sync_log_trim_max_buckets](#rgw_sync_log_trim_max_buckets) | `16` | Advanced | Policy |
| [rgw_sync_log_trim_min_cold_buckets](#rgw_sync_log_trim_min_cold_buckets) | `4` | Advanced | Performance |
| [rgw_sync_meta_inject_err_probability](#rgw_sync_meta_inject_err_probability) | `0` | Dev | Dev |
| [rgw_sync_obj_etag_verify](#rgw_sync_obj_etag_verify) | `False` | Advanced | Policy |
| [rgw_sync_trace_history_size](#rgw_sync_trace_history_size) | `4_K` | Advanced | Performance |
| [rgw_sync_trace_per_node_log_size](#rgw_sync_trace_per_node_log_size) | `32` | Advanced | Performance |
| [rgw_sync_trace_servicemap_update_interval](#rgw_sync_trace_servicemap_update_interval) | `10` | Advanced | Performance |
| [rgw_user_quota_bucket_sync_interval](#rgw_user_quota_bucket_sync_interval) | `3_min` | Advanced | Performance |
| [rgw_user_quota_sync_idle_users](#rgw_user_quota_sync_idle_users) | `False` | Advanced | Policy |
| [rgw_user_quota_sync_interval](#rgw_user_quota_sync_interval) | `1_day` | Advanced | Performance |
| [rgw_user_quota_sync_wait_time](#rgw_user_quota_sync_wait_time) | `1_day` | Advanced | Performance |

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

### rgw_data_log_changes_size

| | |
|---|---|
| نوع | Int · default `1000` · **Dev** |
| جدول | [rgw.md#SP_rgw_data_log_changes_size](../../../config/rgw/rgw.md#SP_rgw_data_log_changes_size) |

**کارکرد:** Max size of pending changes in data log

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set client.rgw rgw_data_log_changes_size 1000
ceph config get client.rgw rgw_data_log_changes_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_data_log_changes_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_data_log_num_shards

| | |
|---|---|
| نوع | Int · default `128` · **Advanced** |
| جدول | [rgw.md#SP_rgw_data_log_num_shards](../../../config/rgw/rgw.md#SP_rgw_data_log_num_shards) |

**کارکرد:** Number of data log shards

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_data_log_num_shards 128
ceph config get client.rgw rgw_data_log_num_shards
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `128` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_data_log_window

| | |
|---|---|
| نوع | Int · default `30` · **Advanced** |
| جدول | [rgw.md#SP_rgw_data_log_window](../../../config/rgw/rgw.md#SP_rgw_data_log_window) |

**کارکرد:** Data log time window

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_data_log_window 30
ceph config get client.rgw rgw_data_log_window
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline `30` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**سیگنال‌ها:** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_data_log_window
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_data_notify_interval_msec

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [rgw.md#SP_rgw_data_notify_interval_msec](../../../config/rgw/rgw.md#SP_rgw_data_notify_interval_msec) |

**کارکرد:** data changes notification interval to followers

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_data_notify_interval_msec 60
ceph config get client.rgw rgw_data_notify_interval_msec
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `0` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_data_notify_interval_msec
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_data_sync_poll_interval

| | |
|---|---|
| نوع | Int · default `20` · **Dev** |
| جدول | [rgw.md#SP_rgw_data_sync_poll_interval](../../../config/rgw/rgw.md#SP_rgw_data_sync_poll_interval) |

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_data_sync_poll_interval 20
ceph config get client.rgw rgw_data_sync_poll_interval
radosgw-admin sync status
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `20` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_data_sync_poll_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_data_sync_spawn_window

| | |
|---|---|
| نوع | Int · default `20` · **Dev** |
| جدول | [rgw.md#SP_rgw_data_sync_spawn_window](../../../config/rgw/rgw.md#SP_rgw_data_sync_spawn_window) |

**زمان استفاده:**

- **Increase** when multisite replication lag grows.
- **Decrease** when sync load competes with client I/O.

**مثال:**

```bash
ceph config set client.rgw rgw_data_sync_spawn_window 20
ceph config get client.rgw rgw_data_sync_spawn_window
radosgw-admin sync status
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `20` limits parallel sync coroutines per bucket/zone.
2. **Increase** when multisite lag grows and RGW CPU headroom exists.
3. **Decrease** if sync threads starve client-facing requests or OSDs spike.

**سیگنال‌ها:** `radosgw-admin sync status`, data/meta sync lag, RGW load average.

```bash
ceph config get client.rgw rgw_data_sync_spawn_window
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
radosgw-admin sync status
```

---

### rgw_lfuda_sync_frequency

| | |
|---|---|
| نوع | Int · default `60` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [rgw.md#SP_rgw_lfuda_sync_frequency](../../../config/rgw/rgw.md#SP_rgw_lfuda_sync_frequency) |

**کارکرد:** LFUDA variables' sync frequency in seconds

**زمان استفاده:** تنظیم replication و sync در multisite — وقتی lag یا بار sync مشکل‌ساز است.

**مثال:**

```bash
ceph config set client.rgw rgw_lfuda_sync_frequency 60
ceph config get client.rgw rgw_lfuda_sync_frequency
ceph orch restart rgw
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `60`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_lfuda_sync_frequency
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_md_log_max_shards

| | |
|---|---|
| نوع | Int · default `64` · **Advanced** |
| جدول | [rgw.md#SP_rgw_md_log_max_shards](../../../config/rgw/rgw.md#SP_rgw_md_log_max_shards) |

**کارکرد:** RGW number of metadata log shards

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه/concurrency می‌رسند یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_md_log_max_shards 64
ceph config get client.rgw rgw_md_log_max_shards
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `64` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_md_notify_interval_msec

| | |
|---|---|
| نوع | Int · default `200` · **Advanced** |
| جدول | [rgw.md#SP_rgw_md_notify_interval_msec](../../../config/rgw/rgw.md#SP_rgw_md_notify_interval_msec) |

**کارکرد:** Length of time to aggregate metadata changes

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_md_notify_interval_msec 200
ceph config get client.rgw rgw_md_notify_interval_msec
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `200` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_md_notify_interval_msec
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_meta_sync_poll_interval

| | |
|---|---|
| نوع | Int · default `20` · **Dev** |
| جدول | [rgw.md#SP_rgw_meta_sync_poll_interval](../../../config/rgw/rgw.md#SP_rgw_meta_sync_poll_interval) |

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_meta_sync_poll_interval 20
ceph config get client.rgw rgw_meta_sync_poll_interval
radosgw-admin sync status
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `20` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_meta_sync_poll_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_meta_sync_spawn_window

| | |
|---|---|
| نوع | Int · default `20` · **Dev** |
| جدول | [rgw.md#SP_rgw_meta_sync_spawn_window](../../../config/rgw/rgw.md#SP_rgw_meta_sync_spawn_window) |

**زمان استفاده:**

- **Increase** when multisite replication lag grows.
- **Decrease** when sync load competes with client I/O.

**مثال:**

```bash
ceph config set client.rgw rgw_meta_sync_spawn_window 20
ceph config get client.rgw rgw_meta_sync_spawn_window
radosgw-admin sync status
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `20` limits parallel sync coroutines per bucket/zone.
2. **Increase** when multisite lag grows and RGW CPU headroom exists.
3. **Decrease** if sync threads starve client-facing requests or OSDs spike.

**سیگنال‌ها:** `radosgw-admin sync status`, data/meta sync lag, RGW load average.

```bash
ceph config get client.rgw rgw_meta_sync_spawn_window
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
radosgw-admin sync status
```

---

### rgw_run_sync_thread

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_run_sync_thread](../../../config/rgw/rgw.md#SP_rgw_run_sync_thread) |

**کارکرد:** Should run sync thread

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_run_sync_thread false
ceph config get client.rgw rgw_run_sync_thread
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_sync_data_full_inject_err_probability

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [rgw.md#SP_rgw_sync_data_full_inject_err_probability](../../../config/rgw/rgw.md#SP_rgw_sync_data_full_inject_err_probability) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set client.rgw rgw_sync_data_full_inject_err_probability 0
ceph config get client.rgw rgw_sync_data_full_inject_err_probability
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_sync_data_inject_err_probability

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [rgw.md#SP_rgw_sync_data_inject_err_probability](../../../config/rgw/rgw.md#SP_rgw_sync_data_inject_err_probability) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set client.rgw rgw_sync_data_inject_err_probability 0
ceph config get client.rgw rgw_sync_data_inject_err_probability
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_sync_lease_period

| | |
|---|---|
| نوع | Int · default `2_min` · **Dev** |
| جدول | [rgw.md#SP_rgw_sync_lease_period](../../../config/rgw/rgw.md#SP_rgw_sync_lease_period) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set client.rgw rgw_sync_lease_period 2_min
ceph config get client.rgw rgw_sync_lease_period
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `2_min` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_sync_lease_period
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_sync_log_trim_concurrent_buckets

| | |
|---|---|
| نوع | Int · default `4` · **Advanced** |
| جدول | [rgw.md#SP_rgw_sync_log_trim_concurrent_buckets](../../../config/rgw/rgw.md#SP_rgw_sync_log_trim_concurrent_buckets) |

**کارکرد:** Maximum number of buckets to trim in parallel

**زمان استفاده:**

- **Increase** when RGW queues requests but CPU is not saturated.
- **Decrease** when latency spikes or CPU context-switch overhead grows.

**مثال:**

```bash
ceph config set client.rgw rgw_sync_log_trim_concurrent_buckets 4
ceph config get client.rgw rgw_sync_log_trim_concurrent_buckets
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at `4` under peak concurrent clients.
2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.
3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.
4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.

**سیگنال‌ها:** 503/slowdown responses, high `active_requests` vs `max_concurrent`.

```bash
ceph config get client.rgw rgw_sync_log_trim_concurrent_buckets
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_sync_log_trim_interval

| | |
|---|---|
| نوع | Int · default `20_min` · **Advanced** |
| جدول | [rgw.md#SP_rgw_sync_log_trim_interval](../../../config/rgw/rgw.md#SP_rgw_sync_log_trim_interval) |

**کارکرد:** Sync log trim interval

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_sync_log_trim_interval 20_min
ceph config get client.rgw rgw_sync_log_trim_interval
radosgw-admin sync status
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `20_min` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_sync_log_trim_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_sync_log_trim_max_buckets

| | |
|---|---|
| نوع | Int · default `16` · **Advanced** |
| جدول | [rgw.md#SP_rgw_sync_log_trim_max_buckets](../../../config/rgw/rgw.md#SP_rgw_sync_log_trim_max_buckets) |

**کارکرد:** Maximum number of buckets to trim per interval

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه/concurrency می‌رسند یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_sync_log_trim_max_buckets 16
ceph config get client.rgw rgw_sync_log_trim_max_buckets
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `16` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_sync_log_trim_min_cold_buckets

| | |
|---|---|
| نوع | Int · default `4` · **Advanced** |
| جدول | [rgw.md#SP_rgw_sync_log_trim_min_cold_buckets](../../../config/rgw/rgw.md#SP_rgw_sync_log_trim_min_cold_buckets) |

**کارکرد:** Minimum number of cold buckets to trim per interval

**زمان استفاده:** تنظیم replication و sync در multisite — وقتی lag یا بار sync مشکل‌ساز است.

**مثال:**

```bash
ceph config set client.rgw rgw_sync_log_trim_min_cold_buckets 4
ceph config get client.rgw rgw_sync_log_trim_min_cold_buckets
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_sync_log_trim_min_cold_buckets
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_sync_meta_inject_err_probability

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [rgw.md#SP_rgw_sync_meta_inject_err_probability](../../../config/rgw/rgw.md#SP_rgw_sync_meta_inject_err_probability) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set client.rgw rgw_sync_meta_inject_err_probability 0
ceph config get client.rgw rgw_sync_meta_inject_err_probability
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_sync_obj_etag_verify

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_sync_obj_etag_verify](../../../config/rgw/rgw.md#SP_rgw_sync_obj_etag_verify) |

**کارکرد:** Verify if the object copied from remote is identical to its source

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_sync_obj_etag_verify true
ceph config get client.rgw rgw_sync_obj_etag_verify
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Production: prefer secure default (`False` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---

### rgw_sync_trace_history_size

| | |
|---|---|
| نوع | Size · default `4_K` · **Advanced** |
| جدول | [rgw.md#SP_rgw_sync_trace_history_size](../../../config/rgw/rgw.md#SP_rgw_sync_trace_history_size) |

**کارکرد:** Sync trace history size

**زمان استفاده:** تنظیم replication و sync در multisite — وقتی lag یا بار sync مشکل‌ساز است.

**مثال:**

```bash
ceph config set client.rgw rgw_sync_trace_history_size 4_K
ceph config get client.rgw rgw_sync_trace_history_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `4_K`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_sync_trace_history_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_sync_trace_per_node_log_size

| | |
|---|---|
| نوع | Int · default `32` · **Advanced** |
| جدول | [rgw.md#SP_rgw_sync_trace_per_node_log_size](../../../config/rgw/rgw.md#SP_rgw_sync_trace_per_node_log_size) |

**کارکرد:** Sync trace per-node log size

**زمان استفاده:** تنظیم replication و sync در multisite — وقتی lag یا بار sync مشکل‌ساز است.

**مثال:**

```bash
ceph config set client.rgw rgw_sync_trace_per_node_log_size 32
ceph config get client.rgw rgw_sync_trace_per_node_log_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `32`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_sync_trace_per_node_log_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_sync_trace_servicemap_update_interval

| | |
|---|---|
| نوع | Int · default `10` · **Advanced** |
| جدول | [rgw.md#SP_rgw_sync_trace_servicemap_update_interval](../../../config/rgw/rgw.md#SP_rgw_sync_trace_servicemap_update_interval) |

**کارکرد:** Sync-trace service-map update interval

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_sync_trace_servicemap_update_interval 10
ceph config get client.rgw rgw_sync_trace_servicemap_update_interval
radosgw-admin sync status
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `10` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_sync_trace_servicemap_update_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_user_quota_bucket_sync_interval

| | |
|---|---|
| نوع | Int · default `3_min` · **Advanced** |
| جدول | [rgw.md#SP_rgw_user_quota_bucket_sync_interval](../../../config/rgw/rgw.md#SP_rgw_user_quota_bucket_sync_interval) |

**کارکرد:** User quota bucket sync interval

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_user_quota_bucket_sync_interval 3_min
ceph config get client.rgw rgw_user_quota_bucket_sync_interval
radosgw-admin sync status
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `3_min` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_user_quota_bucket_sync_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_user_quota_sync_idle_users

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_user_quota_sync_idle_users](../../../config/rgw/rgw.md#SP_rgw_user_quota_sync_idle_users) |

**کارکرد:** Should sync idle users quota

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_user_quota_sync_idle_users true
ceph config get client.rgw rgw_user_quota_sync_idle_users
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_user_quota_sync_interval

| | |
|---|---|
| نوع | Int · default `1_day` · **Advanced** |
| جدول | [rgw.md#SP_rgw_user_quota_sync_interval](../../../config/rgw/rgw.md#SP_rgw_user_quota_sync_interval) |

**کارکرد:** User quota sync interval

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_user_quota_sync_interval 1_day
ceph config get client.rgw rgw_user_quota_sync_interval
radosgw-admin sync status
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `1_day` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_user_quota_sync_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_user_quota_sync_wait_time

| | |
|---|---|
| نوع | Int · default `1_day` · **Advanced** |
| جدول | [rgw.md#SP_rgw_user_quota_sync_wait_time](../../../config/rgw/rgw.md#SP_rgw_user_quota_sync_wait_time) |

**کارکرد:** User quota full-sync wait time

**زمان استفاده:** تنظیم replication و sync در multisite — وقتی lag یا بار sync مشکل‌ساز است.

**مثال:**

```bash
ceph config set client.rgw rgw_user_quota_sync_wait_time 1_day
ceph config get client.rgw rgw_user_quota_sync_wait_time
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `1_day` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**سیگنال‌ها:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_user_quota_sync_wait_time
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
