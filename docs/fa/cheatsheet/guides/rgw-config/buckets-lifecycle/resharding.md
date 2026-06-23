# Dynamic resharding

راهنمای عمیق پیکربندی RGW — 12 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_dynamic_resharding](#rgw_dynamic_resharding) | `True` | Basic | سیاست |
| [rgw_dynamic_resharding_may_reduce](#rgw_dynamic_resharding_may_reduce) | `True` | Advanced | سیاست |
| [rgw_dynamic_resharding_reduction_wait](#rgw_dynamic_resharding_reduction_wait) | `120` | Advanced | عملکرد |
| [rgw_reshard_batch_size](#rgw_reshard_batch_size) | `64` | Advanced | عملکرد |
| [rgw_reshard_bucket_lock_duration](#rgw_reshard_bucket_lock_duration) | `360` | Advanced | عملکرد |
| [rgw_reshard_debug_interval](#rgw_reshard_debug_interval) | `-1` | Dev | توسعه |
| [rgw_reshard_max_aio](#rgw_reshard_max_aio) | `128` | Advanced | عملکرد |
| [rgw_reshard_num_logs](#rgw_reshard_num_logs) | `16` | Advanced | سیاست |
| [rgw_reshard_progress_judge_interval](#rgw_reshard_progress_judge_interval) | `120` | Dev | عملکرد |
| [rgw_reshard_progress_judge_ratio](#rgw_reshard_progress_judge_ratio) | `0.5` | Dev | عملکرد |
| [rgw_reshard_thread_interval](#rgw_reshard_thread_interval) | `600` | Advanced | عملکرد |
| [rgw_reshardlog_threshold](#rgw_reshardlog_threshold) | `30000` | Dev | عملکرد |

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

### rgw_dynamic_resharding

| | |
|---|---|
| نوع | Bool · default `True` · **Basic** |
| جدول | [rgw.md#SP_rgw_dynamic_resharding](../../../config/rgw/rgw.md#SP_rgw_dynamic_resharding) |

**کارکرد:** Enable dynamic resharding

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_dynamic_resharding false
ceph config get client.rgw rgw_dynamic_resharding
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_dynamic_resharding_may_reduce

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_dynamic_resharding_may_reduce](../../../config/rgw/rgw.md#SP_rgw_dynamic_resharding_may_reduce) |

**کارکرد:** Whether dynamic resharding can reduce the number of shards

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_dynamic_resharding_may_reduce false
ceph config get client.rgw rgw_dynamic_resharding_may_reduce
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_dynamic_resharding_reduction_wait

| | |
|---|---|
| نوع | Uint · default `120` · **Advanced** |
| جدول | [rgw.md#SP_rgw_dynamic_resharding_reduction_wait](../../../config/rgw/rgw.md#SP_rgw_dynamic_resharding_reduction_wait) |

**کارکرد:** Number of hours to delay bucket index shard reduction.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_dynamic_resharding_reduction_wait 120
ceph config get client.rgw rgw_dynamic_resharding_reduction_wait
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `120`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_dynamic_resharding_reduction_wait
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**محدوده:** min `0`, max `—`.

---

### rgw_reshard_batch_size

| | |
|---|---|
| نوع | Uint · default `64` · **Advanced** |
| جدول | [rgw.md#SP_rgw_reshard_batch_size](../../../config/rgw/rgw.md#SP_rgw_reshard_batch_size) |

**کارکرد:** Number of reshard entries to batch together before sending the operations to the CLS back-end

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_reshard_batch_size 64
ceph config get client.rgw rgw_reshard_batch_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `64`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_reshard_batch_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**محدوده:** min `8`, max `—`.

---

### rgw_reshard_bucket_lock_duration

| | |
|---|---|
| نوع | Uint · default `360` · **Advanced** |
| جدول | [rgw.md#SP_rgw_reshard_bucket_lock_duration](../../../config/rgw/rgw.md#SP_rgw_reshard_bucket_lock_duration) |

**کارکرد:** Number of seconds the timeout on the reshard locks (bucket reshard lock and reshard log lock) are set to. As a reshard proceeds these locks can be renewed/extended. If too short, reshards cannot complete and will fail, causing a future reshard attempt. If too long a hung or crashed reshard attempt will keep the bucket locked for an extended period, not allowing RGW to detect the failed reshard attempt and recover.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_reshard_bucket_lock_duration 360
ceph config get client.rgw rgw_reshard_bucket_lock_duration
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `360`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_reshard_bucket_lock_duration
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**محدوده:** min `30`, max `—`.

---

### rgw_reshard_debug_interval

| | |
|---|---|
| نوع | Int · default `-1` · **Dev** |
| جدول | [rgw.md#SP_rgw_reshard_debug_interval](../../../config/rgw/rgw.md#SP_rgw_reshard_debug_interval) |

**کارکرد:** The number of seconds that simulate one "day" in order to debug RGW dynamic resharding. Do *not* modify for a production cluster.

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_reshard_debug_interval -1
ceph config get client.rgw rgw_reshard_debug_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`-1`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_reshard_max_aio

| | |
|---|---|
| نوع | Uint · default `128` · **Advanced** |
| جدول | [rgw.md#SP_rgw_reshard_max_aio](../../../config/rgw/rgw.md#SP_rgw_reshard_max_aio) |

**کارکرد:** Maximum number of outstanding asynchronous I/O operations to allow at a time during resharding

**زمان استفاده:**

- **Increase** when listings/deletes on sharded buckets are slow and OSDs have headroom.
- **Decrease** when bucket-index pools show sustained load spikes or slow ops.

**مثال:**

```bash
ceph config set client.rgw rgw_reshard_max_aio 128
ceph config get client.rgw rgw_reshard_max_aio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at `128` with the workload that triggers RADOS aio on this path.
2. Watch list/delete p99, RGW CPU, and OSD slow ops.
3. Increase in steps (~25%: e.g. 128 → 160 → 192 → 256) until latency stops improving.
4. **Decrease** under recovery pressure, `nearfull`, or sustained bucket-index pool load.

**سیگنال‌ها:** OSD `slow requests`, rising `rgw` throttle counters, flat client throughput.

```bash
ceph config get client.rgw rgw_reshard_max_aio
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
radosgw-admin bucket stats --bucket=BIG_BUCKET | jq '.num_shards'
```

**محدوده:** min `16`, max `—`.

---

### rgw_reshard_num_logs

| | |
|---|---|
| نوع | Uint · default `16` · **Advanced** |
| جدول | [rgw.md#SP_rgw_reshard_num_logs](../../../config/rgw/rgw.md#SP_rgw_reshard_num_logs) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_reshard_num_logs 16
ceph config get client.rgw rgw_reshard_num_logs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `16` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

**محدوده:** min `1`, max `—`.

---

### rgw_reshard_progress_judge_interval

| | |
|---|---|
| نوع | Uint · default `120` · **Dev** |
| جدول | [rgw.md#SP_rgw_reshard_progress_judge_interval](../../../config/rgw/rgw.md#SP_rgw_reshard_progress_judge_interval) |

**کارکرد:** interval (in seconds) of judging if bucket reshard failed in block state

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_reshard_progress_judge_interval 120
ceph config get client.rgw rgw_reshard_progress_judge_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `120` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_reshard_progress_judge_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_reshard_progress_judge_ratio

| | |
|---|---|
| نوع | Float · default `0.5` · **Dev** |
| جدول | [rgw.md#SP_rgw_reshard_progress_judge_ratio](../../../config/rgw/rgw.md#SP_rgw_reshard_progress_judge_ratio) |

**کارکرد:** ratio of reshard progress judge interval to randomly vary

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_reshard_progress_judge_ratio 0.5
ceph config get client.rgw rgw_reshard_progress_judge_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `0.5`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_reshard_progress_judge_ratio
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_reshard_thread_interval

| | |
|---|---|
| نوع | Uint · default `600` · **Advanced** |
| جدول | [rgw.md#SP_rgw_reshard_thread_interval](../../../config/rgw/rgw.md#SP_rgw_reshard_thread_interval) |

**کارکرد:** Number of seconds between processing of reshard log entries

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_reshard_thread_interval 600
ceph config get client.rgw rgw_reshard_thread_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `600` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_reshard_thread_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**محدوده:** min `10`, max `—`.

---

### rgw_reshardlog_threshold

| | |
|---|---|
| نوع | Uint · default `30000` · **Dev** |
| جدول | [rgw.md#SP_rgw_reshardlog_threshold](../../../config/rgw/rgw.md#SP_rgw_reshardlog_threshold) |

**کارکرد:** threshold for a shard to record log before blocking writes

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_reshardlog_threshold 30000
ceph config get client.rgw rgw_reshardlog_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `30000`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_reshardlog_threshold
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
