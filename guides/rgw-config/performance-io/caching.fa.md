# Metadata & object caches

راهنمای عمیق پیکربندی RGW — 4 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_cache_enabled](#rgw_cache_enabled) | `True` | Advanced | Performance |
| [rgw_cache_expiry_interval](#rgw_cache_expiry_interval) | `900` | Advanced | Performance |
| [rgw_cache_lru_size](#rgw_cache_lru_size) | `25000` | Advanced | Performance |
| [rgw_obj_tombstone_cache_size](#rgw_obj_tombstone_cache_size) | `1000` | Advanced | Performance |

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

### rgw_cache_enabled

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_cache_enabled](../../../config/rgw/rgw.md#SP_rgw_cache_enabled) |

**کارکرد:** Enable RGW metadata cache.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_cache_enabled false
ceph config get client.rgw rgw_cache_enabled
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `True` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_cache_expiry_interval

| | |
|---|---|
| نوع | Uint · default `900` · **Advanced** |
| جدول | [rgw.md#SP_rgw_cache_expiry_interval](../../../config/rgw/rgw.md#SP_rgw_cache_expiry_interval) |

**کارکرد:** Number of seconds before entries in the cache are assumed stale and re-fetched. Zero is never.

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**مثال:**

```bash
ceph config set client.rgw rgw_cache_expiry_interval 900
ceph config get client.rgw rgw_cache_expiry_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `900`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**سیگنال‌ها:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_cache_expiry_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_cache_lru_size

| | |
|---|---|
| نوع | Int · default `25000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_cache_lru_size](../../../config/rgw/rgw.md#SP_rgw_cache_lru_size) |

**کارکرد:** Max number of items in RGW metadata cache.

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**مثال:**

```bash
ceph config set client.rgw rgw_cache_lru_size 25000
ceph config get client.rgw rgw_cache_lru_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `25000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**سیگنال‌ها:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_cache_lru_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_obj_tombstone_cache_size

| | |
|---|---|
| نوع | Int · default `1000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_obj_tombstone_cache_size](../../../config/rgw/rgw.md#SP_rgw_obj_tombstone_cache_size) |

**کارکرد:** Max number of entries to keep in tombstone cache

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**مثال:**

```bash
ceph config set client.rgw rgw_obj_tombstone_cache_size 1000
ceph config get client.rgw rgw_obj_tombstone_cache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `1000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**سیگنال‌ها:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_obj_tombstone_cache_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
