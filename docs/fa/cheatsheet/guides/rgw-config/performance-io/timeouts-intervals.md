# Timeouts & intervals

راهنمای عمیق پیکربندی RGW — 8 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_exit_timeout_secs](#rgw_exit_timeout_secs) | `2_min` | Advanced | عملکرد |
| [rgw_init_timeout](#rgw_init_timeout) | `5_min` | Basic | عملکرد |
| [rgw_objexp_gc_interval](#rgw_objexp_gc_interval) | `600` | Advanced | عملکرد |
| [rgw_olh_pending_timeout_sec](#rgw_olh_pending_timeout_sec) | `1_hr` | Dev | عملکرد |
| [rgw_ratelimit_interval](#rgw_ratelimit_interval) | `60` | Advanced | عملکرد |
| [rgw_read_through_timeout_ms](#rgw_read_through_timeout_ms) | `10000` | Advanced | عملکرد |
| [rgw_restore_debug_interval](#rgw_restore_debug_interval) | `-1` | Dev | توسعه |
| [rgw_usage_log_tick_interval](#rgw_usage_log_tick_interval) | `30` | Advanced | عملکرد |

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

### rgw_exit_timeout_secs

| | |
|---|---|
| نوع | Int · default `2_min` · **Advanced** |
| جدول | [rgw.md#SP_rgw_exit_timeout_secs](../../../config/rgw/rgw.md#SP_rgw_exit_timeout_secs) |

**کارکرد:** RGW shutdown timeout Number of seconds to wait for a process before exiting unconditionally.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_exit_timeout_secs 2_min
ceph config get client.rgw rgw_exit_timeout_secs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `2_min` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**سیگنال‌ها:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_exit_timeout_secs
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_init_timeout

| | |
|---|---|
| نوع | Int · default `5_min` · **Basic** |
| جدول | [rgw.md#SP_rgw_init_timeout](../../../config/rgw/rgw.md#SP_rgw_init_timeout) |

**کارکرد:** Initialization timeout The time length (in seconds) that RGW will allow for its initialization. RGW process will give up and quit if initialization is not complete after this amount of time.

**زمان استفاده:** رفتار اصلی RGW — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_init_timeout 5_min
ceph config get client.rgw rgw_init_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `5_min` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**سیگنال‌ها:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_init_timeout
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_objexp_gc_interval

| | |
|---|---|
| نوع | Uint · default `600` · **Advanced** |
| جدول | [rgw.md#SP_rgw_objexp_gc_interval](../../../config/rgw/rgw.md#SP_rgw_objexp_gc_interval) |

**کارکرد:** Swift objects expirer garbage collector interval

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_objexp_gc_interval 600
ceph config get client.rgw rgw_objexp_gc_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `600` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_objexp_gc_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_olh_pending_timeout_sec

| | |
|---|---|
| نوع | Int · default `1_hr` · **Dev** |
| جدول | [rgw.md#SP_rgw_olh_pending_timeout_sec](../../../config/rgw/rgw.md#SP_rgw_olh_pending_timeout_sec) |

**کارکرد:** Max time for pending OLH change to complete OLH is a versioned object's logical head. Operations on it are journaled and as pending before completion. If an operation doesn't complete with this amount of seconds, we remove the operation from the journal.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_olh_pending_timeout_sec 1_hr
ceph config get client.rgw rgw_olh_pending_timeout_sec
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `1_hr` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**سیگنال‌ها:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_olh_pending_timeout_sec
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_ratelimit_interval

| | |
|---|---|
| نوع | Uint · default `60` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [rgw.md#SP_rgw_ratelimit_interval](../../../config/rgw/rgw.md#SP_rgw_ratelimit_interval) |

**کارکرد:** Time window for rate limiting in seconds This option sets the time window for rate limiting accumulation in seconds. Requests that exceed the configured rate limits within this time window will be rejected. The default is a 60 second token bucket.

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_ratelimit_interval 60
ceph config get client.rgw rgw_ratelimit_interval
ceph orch restart rgw
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `60` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_ratelimit_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**محدوده:** min `1`, max `—`.

---

### rgw_read_through_timeout_ms

| | |
|---|---|
| نوع | Int · default `10000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_read_through_timeout_ms](../../../config/rgw/rgw.md#SP_rgw_read_through_timeout_ms) |

**کارکرد:** Maximum time in milliseconds for read-through GET requests to wait for cloud object restore completion When a GET request is made for a cloud-tiered object that must be restored, the request will wait up to this many milliseconds for the restore to complete. If the restore completes within this time, the GET request succeeds and returns the object data. If the time is exceeded, the request fails with ERR_REQUEST_TIMEOUT. Set to 0 to fail immediately without waiting.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_read_through_timeout_ms 10000
ceph config get client.rgw rgw_read_through_timeout_ms
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `10000` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**سیگنال‌ها:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_read_through_timeout_ms
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**محدوده:** min `0`, max `—`.

---

### rgw_restore_debug_interval

| | |
|---|---|
| نوع | Int · default `-1` · **Dev** |
| جدول | [rgw.md#SP_rgw_restore_debug_interval](../../../config/rgw/rgw.md#SP_rgw_restore_debug_interval) |

**کارکرد:** The number of seconds that simulate one "day" in order to debug RGW CloudRestore. Do *not* modify for a production cluster. For debugging RGW Cloud Restore, the number of seconds that are equivalent to one simulated "day". Values less than 1 are ignored and do not change Restore behavior. For example, during debugging if one wanted every 10 minutes to be equivalent to one day, then this would be set to 600, the number of seconds in 10 minutes.

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_restore_debug_interval -1
ceph config get client.rgw rgw_restore_debug_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`-1`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_usage_log_tick_interval

| | |
|---|---|
| نوع | Int · default `30` · **Advanced** |
| جدول | [rgw.md#SP_rgw_usage_log_tick_interval](../../../config/rgw/rgw.md#SP_rgw_usage_log_tick_interval) |

**کارکرد:** Number of seconds between usage log flush cycles The number of seconds between consecutive usage log flushes. The usage log will also flush itself to the backend if the number of pending entries reaches a certain threshold.

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_usage_log_tick_interval 30
ceph config get client.rgw rgw_usage_log_tick_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `30` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_usage_log_tick_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
