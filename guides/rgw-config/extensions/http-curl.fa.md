# HTTP / libcurl

deep dive پیکربندی RGW — 5 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_curl_buffersize](#rgw_curl_buffersize) | `524288` | Dev | Performance |
| [rgw_curl_low_speed_limit](#rgw_curl_low_speed_limit) | `1024` | Advanced | Policy |
| [rgw_curl_low_speed_time](#rgw_curl_low_speed_time) | `5_min` | Advanced | Performance |
| [rgw_curl_tcp_keepalive](#rgw_curl_tcp_keepalive) | `0` | Advanced | Architecture |
| [rgw_curl_wait_timeout_ms](#rgw_curl_wait_timeout_ms) | `1000` | Dev | Performance |

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

### rgw_curl_buffersize

| | |
|---|---|
| نوع | Int · default `524288` · **Dev** |
| جدول | [rgw.md#SP_rgw_curl_buffersize](../../../config/rgw/rgw.md#SP_rgw_curl_buffersize) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set client.rgw rgw_curl_buffersize 524288
ceph config get client.rgw rgw_curl_buffersize
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `524288`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_curl_buffersize
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**محدوده:** min `1024`, max `524288`.

---

### rgw_curl_low_speed_limit

| | |
|---|---|
| نوع | Int · default `1024` · **Advanced** |
| جدول | [rgw.md#SP_rgw_curl_low_speed_limit](../../../config/rgw/rgw.md#SP_rgw_curl_low_speed_limit) |

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه/concurrency می‌رسند یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_curl_low_speed_limit 1024
ceph config get client.rgw rgw_curl_low_speed_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Upstream default (`1024`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---

### rgw_curl_low_speed_time

| | |
|---|---|
| نوع | Int · default `5_min` · **Advanced** |
| جدول | [rgw.md#SP_rgw_curl_low_speed_time](../../../config/rgw/rgw.md#SP_rgw_curl_low_speed_time) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_curl_low_speed_time 5_min
ceph config get client.rgw rgw_curl_low_speed_time
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `5_min`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_curl_low_speed_time
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_curl_tcp_keepalive

| | |
|---|---|
| نوع | Int · enum: ["0", "1"] · default `0` · **Advanced** |
| جدول | [rgw.md#SP_rgw_curl_tcp_keepalive](../../../config/rgw/rgw.md#SP_rgw_curl_tcp_keepalive) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_curl_tcp_keepalive 0
ceph config get client.rgw rgw_curl_tcp_keepalive
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Valid values: ["0", "1"].
2. Default `0` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_curl_wait_timeout_ms

| | |
|---|---|
| نوع | Int · default `1000` · **Dev** |
| جدول | [rgw.md#SP_rgw_curl_wait_timeout_ms](../../../config/rgw/rgw.md#SP_rgw_curl_wait_timeout_ms) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set client.rgw rgw_curl_wait_timeout_ms 1000
ceph config get client.rgw rgw_curl_wait_timeout_ms
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `1000` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**سیگنال‌ها:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_curl_wait_timeout_ms
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
