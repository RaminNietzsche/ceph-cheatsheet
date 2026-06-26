# Usage logging

راهنمای عمیق پیکربندی RGW — 4 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_usage_log_flush_threshold](#rgw_usage_log_flush_threshold) | `1024` | Advanced | عملکرد |
| [rgw_usage_log_key_transition](#rgw_usage_log_key_transition) | `True` | Advanced | سیاست |
| [rgw_usage_max_shards](#rgw_usage_max_shards) | `32` | Advanced | سیاست |
| [rgw_usage_max_user_shards](#rgw_usage_max_user_shards) | `1` | Advanced | سیاست |

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

### rgw_usage_log_flush_threshold

| | |
|---|---|
| نوع | Int · default `1024` · **Advanced** |
| جدول | [rgw.md#SP_rgw_usage_log_flush_threshold](../../../config/rgw/rgw.md#SP_rgw_usage_log_flush_threshold) |

**کارکرد:** Number of entries in usage log before flushing This is the max number of entries that will be held in the usage log, before it will be flushed to the backend. Note that the usage log is periodically flushed, even if number of entries does not reach this threshold. A usage log entry corresponds to one or more operations on a single bucket.i

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_usage_log_flush_threshold 1024
ceph config get client.rgw rgw_usage_log_flush_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `1024`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_usage_log_flush_threshold
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_usage_log_key_transition

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_usage_log_key_transition](../../../config/rgw/rgw.md#SP_rgw_usage_log_key_transition) |

**کارکرد:** Handle the co-existence of both old and new name-by-user keys The new usage log keyed by owner/payer ID has the prefix of "~" for IDs starting with '0'. This prefix is absent from the old scheme. This option instructs RGW to handle the old keys if they still exist. It should be set false when the old keys no longer exist to avoid performance penalty.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**گزینه‌های مرتبط:**

- [`rgw_enable_usage_log`](../../../config/rgw/rgw.md#SP_rgw_enable_usage_log)

**مثال:**

```bash
ceph config set client.rgw rgw_usage_log_key_transition false
ceph config get client.rgw rgw_usage_log_key_transition
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_usage_max_shards

| | |
|---|---|
| نوع | Int · default `32` · **Advanced** |
| جدول | [rgw.md#SP_rgw_usage_max_shards](../../../config/rgw/rgw.md#SP_rgw_usage_max_shards) |

**کارکرد:** Number of shards for usage log. The number of RADOS objects that RGW will use in order to store the usage log data. All RGW daemons and radosgw-admin commands must use the same value for this option. If values differ, writes and reads/clears will target different objects, causing usage data to appear empty or not be cleared. Use ``ceph config set global rgw_usage_max_shards <N>`` to ensure consistency across the cluster. Alternatively, ``radosgw-admin`` supports the ``--rgw-usage-max-shards`` command-line parameter.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**گزینه‌های مرتبط:**

- [`rgw_enable_usage_log`](../../../config/rgw/rgw.md#SP_rgw_enable_usage_log)

**مثال:**

```bash
ceph config set global rgw_usage_max_shards 32
ceph config get global rgw_usage_max_shards
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `32` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_usage_max_user_shards

| | |
|---|---|
| نوع | Int · default `1` · **Advanced** |
| جدول | [rgw.md#SP_rgw_usage_max_user_shards](../../../config/rgw/rgw.md#SP_rgw_usage_max_user_shards) |

**کارکرد:** Number of shards for single user in usage log The number of shards that a single user will span over in the usage log.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**گزینه‌های مرتبط:**

- [`rgw_enable_usage_log`](../../../config/rgw/rgw.md#SP_rgw_enable_usage_log)

**مثال:**

```bash
ceph config set client.rgw rgw_usage_max_user_shards 1
ceph config get client.rgw rgw_usage_max_user_shards
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `1` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

**محدوده:** min `1`, max `—`.

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
