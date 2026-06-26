# HTTP / libcurl

راهنمای عمیق پیکربندی RGW — 5 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_curl_buffersize](#rgw_curl_buffersize) | `524288` | Dev | عملکرد |
| [rgw_curl_low_speed_limit](#rgw_curl_low_speed_limit) | `1024` | Advanced | سیاست |
| [rgw_curl_low_speed_time](#rgw_curl_low_speed_time) | `5_min` | Advanced | عملکرد |
| [rgw_curl_tcp_keepalive](#rgw_curl_tcp_keepalive) | `0` | Advanced | معماری |
| [rgw_curl_wait_timeout_ms](#rgw_curl_wait_timeout_ms) | `1000` | Dev | عملکرد |

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

### rgw_curl_buffersize

| | |
|---|---|
| نوع | Int · default `524288` · **Dev** |
| جدول | [rgw.md#SP_rgw_curl_buffersize](../../../config/rgw/rgw.md#SP_rgw_curl_buffersize) |

**کارکرد:** Pass a long specifying your preferred size (in bytes) for the receivebuffer in libcurl. See: https://curl.se/libcurl/c/CURLOPT_BUFFERSIZE.html

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

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

**کارکرد:** It contains the average transfer speed in bytes per second that the transfer should be below during rgw_curl_low_speed_time seconds for libcurl to consider it to be too slow and abort. Set it zero to disable this.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

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

**کارکرد:** It contains the time in number seconds that the transfer speed should be below the rgw_curl_low_speed_limit for the library to consider it too slow and abort. Set it zero to disable this.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

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

**کارکرد:** Enable TCP keepalive on the HTTP client sockets managed by libcurl. This does not apply to connections received by the HTTP frontend, but only to HTTP requests sent by radosgw. Examples include requests to Keystone for authentication, sync requests from multisite, and requests to key management servers for SSE.

**زمان استفاده:** تنظیم replication و sync در محیط چندسایته — وقتی تأخیر (lag) یا بار sync مشکل‌ساز است.

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

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

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
