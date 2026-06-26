# Bucket index & sharding

راهنمای عمیق پیکربندی RGW — 4 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_override_bucket_index_max_shards](#rgw_override_bucket_index_max_shards) | `0` | Dev | سیاست |
| [rgw_pending_bucket_index_op_expiration](#rgw_pending_bucket_index_op_expiration) | `120` | Advanced | عملکرد |
| [rgw_safe_max_objects_per_shard](#rgw_safe_max_objects_per_shard) | `102400` | Advanced | سیاست |
| [rgw_shard_warning_threshold](#rgw_shard_warning_threshold) | `90` | Advanced | عملکرد |

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

### rgw_override_bucket_index_max_shards

| | |
|---|---|
| نوع | Uint · default `0` · **Dev** |
| جدول | [rgw.md#SP_rgw_override_bucket_index_max_shards](../../../config/rgw/rgw.md#SP_rgw_override_bucket_index_max_shards) |

**کارکرد:** The default number of bucket index shards for newly-created buckets. This value overrides bucket_index_max_shards stored in the zone. Setting this value in the zone is preferred, because it applies globally to all radosgw daemons running in the zone.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_override_bucket_index_max_shards 128
ceph config get client.rgw rgw_override_bucket_index_max_shards
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `0` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_pending_bucket_index_op_expiration

| | |
|---|---|
| نوع | Uint · default `120` · **Advanced** |
| جدول | [rgw.md#SP_rgw_pending_bucket_index_op_expiration](../../../config/rgw/rgw.md#SP_rgw_pending_bucket_index_op_expiration) |

**کارکرد:** Number of seconds a pending operation can remain in bucket index shard. Number of seconds a pending operation can remain in bucket index shard before it expires. Used for transactional bucket index operations, and if the operation does not complete in this time period, the operation will be dropped.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_pending_bucket_index_op_expiration 120
ceph config get client.rgw rgw_pending_bucket_index_op_expiration
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `120`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_pending_bucket_index_op_expiration
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_safe_max_objects_per_shard

| | |
|---|---|
| نوع | Int · default `102400` · **Advanced** |
| جدول | [rgw.md#SP_rgw_safe_max_objects_per_shard](../../../config/rgw/rgw.md#SP_rgw_safe_max_objects_per_shard) |

**کارکرد:** Safe number of objects per shard This is the max number of objects per bucket index shard that RGW considers safe. RGW will warn if it identifies a bucket where its per-shard count is higher than a percentage of this number.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**گزینه‌های مرتبط:**

- [`rgw_shard_warning_threshold`](../../../config/rgw/rgw.md#SP_rgw_shard_warning_threshold)

**مثال:**

```bash
ceph config set client.rgw rgw_safe_max_objects_per_shard 102400
ceph config get client.rgw rgw_safe_max_objects_per_shard
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `102400` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_shard_warning_threshold

| | |
|---|---|
| نوع | Float · default `90` · **Advanced** |
| جدول | [rgw.md#SP_rgw_shard_warning_threshold](../../../config/rgw/rgw.md#SP_rgw_shard_warning_threshold) |

**کارکرد:** Warn about max objects per shard Warn if number of objects per shard in a specific bucket passed this percentage of the safe number.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`rgw_safe_max_objects_per_shard`](../../../config/rgw/rgw.md#SP_rgw_safe_max_objects_per_shard)

**مثال:**

```bash
ceph config set client.rgw rgw_shard_warning_threshold 90
ceph config get client.rgw rgw_shard_warning_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `90`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_shard_warning_threshold
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
