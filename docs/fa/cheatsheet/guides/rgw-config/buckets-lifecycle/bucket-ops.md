# Bucket operations

راهنمای عمیق پیکربندی RGW — 12 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_bucket_counters_cache](#rgw_bucket_counters_cache) | `False` | Dev | عملکرد |
| [rgw_bucket_counters_cache_size](#rgw_bucket_counters_cache_size) | `10000` | Advanced | عملکرد |
| [rgw_bucket_default_quota_max_objects](#rgw_bucket_default_quota_max_objects) | `-1` | Basic | سیاست |
| [rgw_bucket_default_quota_max_size](#rgw_bucket_default_quota_max_size) | `-1` | Advanced | سیاست |
| [rgw_bucket_eexist_override](#rgw_bucket_eexist_override) | `False` | Advanced | سیاست |
| [rgw_bucket_index_max_aio](#rgw_bucket_index_max_aio) | `128` | Advanced | عملکرد |
| [rgw_bucket_index_transaction_instrumentation](#rgw_bucket_index_transaction_instrumentation) | `False` | Dev | توسعه |
| [rgw_bucket_logging_obj_roll_time](#rgw_bucket_logging_obj_roll_time) | `300` | Advanced | عملکرد |
| [rgw_bucket_persistent_notif_num_shards](#rgw_bucket_persistent_notif_num_shards) | `11` | Advanced | سیاست |
| [rgw_bucket_quota_cache_size](#rgw_bucket_quota_cache_size) | `10000` | Advanced | عملکرد |
| [rgw_bucket_quota_ttl](#rgw_bucket_quota_ttl) | `10_min` | Advanced | عملکرد |
| [rgw_bucket_sync_spawn_window](#rgw_bucket_sync_spawn_window) | `20` | Dev | عملکرد |

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

### rgw_bucket_counters_cache

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [rgw.md#SP_rgw_bucket_counters_cache](../../../config/rgw/rgw.md#SP_rgw_bucket_counters_cache) |

**کارکرد:** Enables an in-memory cache for **perf counters** with a bucket label, so per-bucket metrics avoid repeated counter lookups.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**گزینه‌های مرتبط:**

- `rgw_bucket_counters_cache_size`
- [`rgw_bucket_counters_cache_size`](../../../config/rgw/rgw.md#SP_rgw_bucket_counters_cache_size)

**مثال:**

```bash
ceph config set client.rgw rgw_bucket_counters_cache true
ceph config set client.rgw rgw_bucket_counters_cache_size 20000
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `False` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_bucket_counters_cache_size

| | |
|---|---|
| نوع | Uint · default `10000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_bucket_counters_cache_size](../../../config/rgw/rgw.md#SP_rgw_bucket_counters_cache_size) |

**کارکرد:** Maximum number of labeled per-bucket perf counter entries kept in the cache.

**زمان استفاده:** Increase on clusters with many active buckets and bucket-level monitoring enabled.

**گزینه‌های مرتبط:**

- [`rgw_bucket_counters_cache`](../../../config/rgw/rgw.md#SP_rgw_bucket_counters_cache)

**مثال:**

```bash
ceph config set client.rgw rgw_bucket_counters_cache_size 10000
ceph config get client.rgw rgw_bucket_counters_cache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**سیگنال‌ها:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_bucket_counters_cache_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_bucket_default_quota_max_objects

| | |
|---|---|
| نوع | Int · default `-1` · **Basic** |
| جدول | [rgw.md#SP_rgw_bucket_default_quota_max_objects](../../../config/rgw/rgw.md#SP_rgw_bucket_default_quota_max_objects) |

**کارکرد:** Default maximum **objects per bucket** for **newly created users**. Does not retroactively change existing users.

**زمان استفاده:** Enforce per-bucket object limits for every new tenant without per-user `radosgw-admin quota` calls.

**گزینه‌های مرتبط:**

- `rgw_bucket_default_quota_max_size`, `rgw_user_default_quota_*`

**مثال:**

```bash
ceph config set client rgw_bucket_default_quota_max_objects 500000
radosgw-admin user create --uid=newuser --display-name="New User"
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. `ceph df detail` — usable cluster capacity.
2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.
3. Set limit; `-1` means unlimited. Default: `-1`.
4. Create a test user and confirm via `radosgw-admin quota get --quota-scope=user --uid=<uid>`.
5. Existing users/accounts are **not** retroactively changed.

```bash
ceph df detail
radosgw-admin quota get --quota-scope=user --uid=testuser
radosgw-admin bucket stats --bucket=testbucket
```

---

### rgw_bucket_default_quota_max_size

| | |
|---|---|
| نوع | Int · default `-1` · **Advanced** |
| جدول | [rgw.md#SP_rgw_bucket_default_quota_max_size](../../../config/rgw/rgw.md#SP_rgw_bucket_default_quota_max_size) |

**کارکرد:** Default maximum **bytes per bucket** for new users.

**زمان استفاده:** محدودیت پیش‌فرض tenant یا پلتفرم برای کاربران، account یا bucket جدید.

**مثال:**

```bash
ceph config set client rgw_bucket_default_quota_max_size $((100*1024*1024*1024))

radosgw-admin quota set --quota-scope=user --uid=alice --max-size=50G --max-objects=10000
radosgw-admin quota enable --quota-scope=user --uid=alice
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. `ceph df detail` — usable cluster capacity.
2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.
3. Set limit; `-1` means unlimited. Default: `-1`.
4. Create a test user and confirm via `radosgw-admin quota get --quota-scope=user --uid=<uid>`.
5. Existing users/accounts are **not** retroactively changed.

```bash
ceph df detail
radosgw-admin quota get --quota-scope=user --uid=testuser
radosgw-admin bucket stats --bucket=testbucket
```

---

### rgw_bucket_eexist_override

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_bucket_eexist_override](../../../config/rgw/rgw.md#SP_rgw_bucket_eexist_override) |

**کارکرد:** When `true`, `CreateBucket` on an existing bucket (same owner) returns **HTTP 409 / EEXIST** instead of succeeding idempotently.

**Default (`false`):** Matches AWS S3 — repeated CreateBucket by the same owner typically returns 200 OK.

**زمان استفاده:** Clients or automation that expect an error on duplicate bucket creation.

**مثال:**

```bash
ceph config set client.rgw rgw_bucket_eexist_override true
# aws s3 mb s3://existing-bucket  →  409 BucketAlreadyExists
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_bucket_index_max_aio

| | |
|---|---|
| نوع | Uint · default `128` · **Advanced** |
| جدول | [rgw.md#SP_rgw_bucket_index_max_aio](../../../config/rgw/rgw.md#SP_rgw_bucket_index_max_aio) |

**کارکرد:** Limits **concurrent RADOS requests** across **bucket index shards** (list operations, index maintenance, multi-shard updates). Used in `svc_bi_rados.cc`.

**زمان استفاده:**

- **Increase** when listings/deletes on sharded buckets are slow and OSDs have headroom.
- **Decrease** when bucket-index pools show sustained load spikes or slow ops.

**گزینه‌های مرتبط:**

- [`rgw_multi_obj_del_max_aio`](../../../config/rgw/rgw.md#SP_rgw_multi_obj_del_max_aio) (default 16)
- [`rgw_override_bucket_index_max_shards`](../../../config/rgw/rgw.md#SP_rgw_override_bucket_index_max_shards)

**مثال:**

```bash
ceph config set client.rgw rgw_bucket_index_max_aio 256
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at `128` with large bucket LIST, bulk DELETE, multipart completion.
2. Watch list/delete p99, RGW CPU, and OSD slow ops.
3. Increase in steps (~25%: e.g. 128 → 160 → 192 → 256) until latency stops improving.
4. **Decrease** under recovery pressure, `nearfull`, or sustained bucket-index pool load.

**سیگنال‌ها:** OSD `slow requests`, rising `rgw` throttle counters, flat client throughput.

```bash
ceph config get client.rgw rgw_bucket_index_max_aio
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
radosgw-admin bucket stats --bucket=BIG_BUCKET | jq '.num_shards'
```

More shards and faster OSDs tolerate higher values; during `nearfull` or heavy recovery, lower is safer.

---

### rgw_bucket_index_transaction_instrumentation

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [rgw.md#SP_rgw_bucket_index_transaction_instrumentation](../../../config/rgw/rgw.md#SP_rgw_bucket_index_transaction_instrumentation) |

**کارکرد:** Turns on extra instrumentation surrounding bucket index transactions.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_bucket_index_transaction_instrumentation true
ceph config get client.rgw rgw_bucket_index_transaction_instrumentation
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`False`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_bucket_logging_obj_roll_time

| | |
|---|---|
| نوع | Uint · default `300` · **Advanced** |
| جدول | [rgw.md#SP_rgw_bucket_logging_obj_roll_time](../../../config/rgw/rgw.md#SP_rgw_bucket_logging_obj_roll_time) |

**کارکرد:** Default time in seconds for the bucket logging object to roll Object roll time can be provided in the bucket logging configuration. If not provided, this value will be used.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_bucket_logging_obj_roll_time 300
ceph config get client.rgw rgw_bucket_logging_obj_roll_time
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `300` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_bucket_logging_obj_roll_time
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_bucket_persistent_notif_num_shards

| | |
|---|---|
| نوع | Uint · default `11` · **Advanced** |
| جدول | [rgw.md#SP_rgw_bucket_persistent_notif_num_shards](../../../config/rgw/rgw.md#SP_rgw_bucket_persistent_notif_num_shards) |

**کارکرد:** Number of shards for a persistent topic. Number of shards of persistent topics. The notifications will be sharded by a combination of the bucket and key name. Changing the number effect only new topics and does not change exiting ones.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_bucket_persistent_notif_num_shards 11
ceph config get client.rgw rgw_bucket_persistent_notif_num_shards
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `11` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_bucket_quota_cache_size

| | |
|---|---|
| نوع | Int · default `10000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_bucket_quota_cache_size](../../../config/rgw/rgw.md#SP_rgw_bucket_quota_cache_size) |

**کارکرد:** RGW quota stats cache size Maximum number of entries in the quota stats cache.

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**مثال:**

```bash
ceph config set client.rgw rgw_bucket_quota_cache_size 10000
ceph config get client.rgw rgw_bucket_quota_cache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**سیگنال‌ها:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_bucket_quota_cache_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_bucket_quota_ttl

| | |
|---|---|
| نوع | Int · default `10_min` · **Advanced** |
| جدول | [rgw.md#SP_rgw_bucket_quota_ttl](../../../config/rgw/rgw.md#SP_rgw_bucket_quota_ttl) |

**کارکرد:** Bucket quota stats cache TTL Length of time for bucket stats to be cached within RGW instance.

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_bucket_quota_ttl 10_min
ceph config get client.rgw rgw_bucket_quota_ttl
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `10_min` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_bucket_quota_ttl
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_bucket_sync_spawn_window

| | |
|---|---|
| نوع | Int · default `20` · **Dev** |
| جدول | [rgw.md#SP_rgw_bucket_sync_spawn_window](../../../config/rgw/rgw.md#SP_rgw_bucket_sync_spawn_window) |

**زمان استفاده:**

- **Increase** when multisite replication lag grows.
- **Decrease** when sync load competes with client I/O.

**مثال:**

```bash
ceph config set client.rgw rgw_bucket_sync_spawn_window 20
ceph config get client.rgw rgw_bucket_sync_spawn_window
radosgw-admin sync status
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `20` limits parallel sync coroutines per bucket/zone.
2. **Increase** when multisite lag grows and RGW CPU headroom exists.
3. **Decrease** if sync threads starve client-facing requests or OSDs spike.

**سیگنال‌ها:** `radosgw-admin sync status`, data/meta sync lag, RGW load average.

```bash
ceph config get client.rgw rgw_bucket_sync_spawn_window
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
radosgw-admin sync status
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
