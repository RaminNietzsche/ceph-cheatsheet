# Users & per-user settings

راهنمای عمیق پیکربندی RGW — 5 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_user_counters_cache](#rgw_user_counters_cache) | `False` | Dev | Performance |
| [rgw_user_counters_cache_size](#rgw_user_counters_cache_size) | `10000` | Advanced | Performance |
| [rgw_user_max_buckets](#rgw_user_max_buckets) | `1000` | Basic | Policy |
| [rgw_user_policies_max_num](#rgw_user_policies_max_num) | `100` | Advanced | Policy |
| [rgw_user_unique_email](#rgw_user_unique_email) | `True` | Basic | Policy |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **Policy** | امنیت، سازگاری API، محدودیت tenant |
| **Capacity** | چیدمان دیسک، مسیرها، اندازه pool |
| **Performance** | خط پایه → تغییر تدریجی → پایش OSD/RGW |
| **Connectivity** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **Architecture** | backend، توپولوژی چندسایته — نه جستجوی عددی |
| **Dev** | در محیط عملیاتی همان پیش‌فرض upstream |

**ابزارهای مشترک:**

```bash
ceph config get client.rgw <option>
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph pg stat
```

---

### rgw_user_counters_cache

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [rgw.md#SP_rgw_user_counters_cache](../../../config/rgw/rgw.md#SP_rgw_user_counters_cache) |

**کارکرد:** enable a rgw perf counters cache for counters with user label

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_user_counters_cache true
ceph config get client.rgw rgw_user_counters_cache
ceph config set client.rgw rgw_user_counters_cache_size 20000
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `False` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_user_counters_cache_size

| | |
|---|---|
| نوع | Uint · default `10000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_user_counters_cache_size](../../../config/rgw/rgw.md#SP_rgw_user_counters_cache_size) |

**کارکرد:** Number of labeled perf counters the user perf counters cache can store

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**مثال:**

```bash
ceph config set client.rgw rgw_user_counters_cache_size 10000
ceph config get client.rgw rgw_user_counters_cache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**سیگنال‌ها:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_user_counters_cache_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_user_max_buckets

| | |
|---|---|
| نوع | Int · default `1000` · **Basic** |
| جدول | [rgw.md#SP_rgw_user_max_buckets](../../../config/rgw/rgw.md#SP_rgw_user_max_buckets) |

**کارکرد:** Max number of buckets per user

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_user_max_buckets 1000
ceph config get client.rgw rgw_user_max_buckets
radosgw-admin user create --uid=newuser --display-name="New User"
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_user_policies_max_num

| | |
|---|---|
| نوع | Int · default `100` · **Advanced** |
| جدول | [rgw.md#SP_rgw_user_policies_max_num](../../../config/rgw/rgw.md#SP_rgw_user_policies_max_num) |

**کارکرد:** The maximum number of IAM user policies for a single user.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_user_policies_max_num 100
ceph config get client.rgw rgw_user_policies_max_num
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `100` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_user_unique_email

| | |
|---|---|
| نوع | Bool · default `True` · **Basic** |
| جدول | [rgw.md#SP_rgw_user_unique_email](../../../config/rgw/rgw.md#SP_rgw_user_unique_email) |

**کارکرد:** Require local RGW users to have unique email addresses

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_user_unique_email false
ceph config get client.rgw rgw_user_unique_email
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
