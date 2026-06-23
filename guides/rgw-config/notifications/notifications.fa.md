# Bucket notifications

deep dive پیکربندی RGW — 13 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_allow_notification_secrets_in_cleartext](#rgw_allow_notification_secrets_in_cleartext) | `False` | Advanced | Policy |
| [rgw_http_notif_connection_timeout](#rgw_http_notif_connection_timeout) | `5` | Advanced | Performance |
| [rgw_http_notif_max_inflight](#rgw_http_notif_max_inflight) | `8192` | Advanced | Performance |
| [rgw_http_notif_message_timeout](#rgw_http_notif_message_timeout) | `10` | Advanced | Performance |
| [rgw_inject_notify_timeout_probability](#rgw_inject_notify_timeout_probability) | `0` | Dev | Dev |
| [rgw_kafka_connection_idle](#rgw_kafka_connection_idle) | `300` | Advanced | Performance |
| [rgw_kafka_max_batch_size](#rgw_kafka_max_batch_size) | `0` | Advanced | Performance |
| [rgw_kafka_message_timeout](#rgw_kafka_message_timeout) | `5000` | Advanced | Performance |
| [rgw_kafka_sleep_timeout](#rgw_kafka_sleep_timeout) | `10` | Advanced | Performance |
| [rgw_max_notify_retries](#rgw_max_notify_retries) | `10` | Advanced | Policy |
| [rgw_topic_persistency_max_retries](#rgw_topic_persistency_max_retries) | `0` | Advanced | Policy |
| [rgw_topic_persistency_sleep_duration](#rgw_topic_persistency_sleep_duration) | `0` | Advanced | Performance |
| [rgw_topic_persistency_time_to_live](#rgw_topic_persistency_time_to_live) | `0` | Advanced | Performance |

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

### rgw_allow_notification_secrets_in_cleartext

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_allow_notification_secrets_in_cleartext](../../../config/rgw/rgw.md#SP_rgw_allow_notification_secrets_in_cleartext) |

**کارکرد:** When `true`, allows bucket notification topics with broker passwords/secrets over plain HTTP. Default requires HTTPS for topics with secrets.

**زمان استفاده:** Trusted private lab only. **Never** enable on internet-facing or untrusted networks.

**گزینه‌های مرتبط:**

- `rgw_trust_forwarded_https` (if TLS terminates at a proxy)

**مثال:**

```bash
ceph config set client.rgw rgw_allow_notification_secrets_in_cleartext true
ceph config get client.rgw rgw_allow_notification_secrets_in_cleartext
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_http_notif_connection_timeout

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [rgw.md#SP_rgw_http_notif_connection_timeout](../../../config/rgw/rgw.md#SP_rgw_http_notif_connection_timeout) |

**کارکرد:** This is the maximum time in seconds to connect to an endpoint

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_http_notif_connection_timeout 5
ceph config get client.rgw rgw_http_notif_connection_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `5` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**سیگنال‌ها:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_http_notif_connection_timeout
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_http_notif_max_inflight

| | |
|---|---|
| نوع | Uint · default `8192` · **Advanced** |
| جدول | [rgw.md#SP_rgw_http_notif_max_inflight](../../../config/rgw/rgw.md#SP_rgw_http_notif_max_inflight) |

**کارکرد:** This is the maximum number of messages in-flight (across all http endpoints)

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه/concurrency می‌رسند یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_http_notif_max_inflight 8192
ceph config get client.rgw rgw_http_notif_max_inflight
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `8192`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_http_notif_max_inflight
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_http_notif_message_timeout

| | |
|---|---|
| نوع | Uint · default `10` · **Advanced** |
| جدول | [rgw.md#SP_rgw_http_notif_message_timeout](../../../config/rgw/rgw.md#SP_rgw_http_notif_message_timeout) |

**کارکرد:** This is the maximum time in seconds to deliver a notification

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_http_notif_message_timeout 10
ceph config get client.rgw rgw_http_notif_message_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `10` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**سیگنال‌ها:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_http_notif_message_timeout
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_inject_notify_timeout_probability

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [rgw.md#SP_rgw_inject_notify_timeout_probability](../../../config/rgw/rgw.md#SP_rgw_inject_notify_timeout_probability) |

**کارکرد:** Likelihood of ignoring a notify

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set client.rgw rgw_inject_notify_timeout_probability 0
ceph config get client.rgw rgw_inject_notify_timeout_probability
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_kafka_connection_idle

| | |
|---|---|
| نوع | Uint · default `300` · **Advanced** |
| جدول | [rgw.md#SP_rgw_kafka_connection_idle](../../../config/rgw/rgw.md#SP_rgw_kafka_connection_idle) |

**کارکرد:** Time in seconds to delete idle kafka connections

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_kafka_connection_idle 300
ceph config get client.rgw rgw_kafka_connection_idle
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `300`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_kafka_connection_idle
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_kafka_max_batch_size

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rgw.md#SP_rgw_kafka_max_batch_size](../../../config/rgw/rgw.md#SP_rgw_kafka_max_batch_size) |

**کارکرد:** This is the maximum size in bytes of a batch of messages sent to kafka

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه/concurrency می‌رسند یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_kafka_max_batch_size 128
ceph config get client.rgw rgw_kafka_max_batch_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_kafka_max_batch_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_kafka_message_timeout

| | |
|---|---|
| نوع | Uint · default `5000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_kafka_message_timeout](../../../config/rgw/rgw.md#SP_rgw_kafka_message_timeout) |

**کارکرد:** This is the maximum time in milliseconds to deliver a message (including retries)

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_kafka_message_timeout 5000
ceph config get client.rgw rgw_kafka_message_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `5000` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**سیگنال‌ها:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_kafka_message_timeout
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_kafka_sleep_timeout

| | |
|---|---|
| نوع | Uint · default `10` · **Advanced** |
| جدول | [rgw.md#SP_rgw_kafka_sleep_timeout](../../../config/rgw/rgw.md#SP_rgw_kafka_sleep_timeout) |

**کارکرد:** Time in milliseconds to sleep while polling for kafka replies

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_kafka_sleep_timeout 10
ceph config get client.rgw rgw_kafka_sleep_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `10` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**سیگنال‌ها:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_kafka_sleep_timeout
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_max_notify_retries

| | |
|---|---|
| نوع | Uint · default `10` · **Advanced** |
| جدول | [rgw.md#SP_rgw_max_notify_retries](../../../config/rgw/rgw.md#SP_rgw_max_notify_retries) |

**کارکرد:** Number of attempts to notify peers before giving up.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه/concurrency می‌رسند یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_max_notify_retries 10
ceph config get client.rgw rgw_max_notify_retries
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `10` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_topic_persistency_max_retries

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [rgw.md#SP_rgw_topic_persistency_max_retries](../../../config/rgw/rgw.md#SP_rgw_topic_persistency_max_retries) |

**کارکرد:** The maximum number sending a persistent notification would be tried. Note that the value of one would mean no retries, and the value of zero would mean that the notification would be tried indefinitely

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه/concurrency می‌رسند یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_topic_persistency_max_retries 128
ceph config get client.rgw rgw_topic_persistency_max_retries
ceph orch restart rgw
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `0` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_topic_persistency_sleep_duration

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [rgw.md#SP_rgw_topic_persistency_sleep_duration](../../../config/rgw/rgw.md#SP_rgw_topic_persistency_sleep_duration) |

**کارکرد:** The minimum time (in seconds) between two tries of the same persistent notification. note that the actual time between the tries may be longer

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_topic_persistency_sleep_duration 0
ceph config get client.rgw rgw_topic_persistency_sleep_duration
ceph orch restart rgw
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_topic_persistency_sleep_duration
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_topic_persistency_time_to_live

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [rgw.md#SP_rgw_topic_persistency_time_to_live](../../../config/rgw/rgw.md#SP_rgw_topic_persistency_time_to_live) |

**کارکرد:** The rgw retention of persistent topics by time (seconds)

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_topic_persistency_time_to_live 0
ceph config get client.rgw rgw_topic_persistency_time_to_live
ceph orch restart rgw
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_topic_persistency_time_to_live
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
