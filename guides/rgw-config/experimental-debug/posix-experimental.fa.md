# POSIX backend

deep dive پیکربندی RGW — 7 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_posix_base_path](#rgw_posix_base_path) | `/tmp/rgw_posix_driver` | Advanced | Architecture |
| [rgw_posix_cache_lanes](#rgw_posix_cache_lanes) | `3` | Advanced | Architecture |
| [rgw_posix_cache_lmdb_count](#rgw_posix_cache_lmdb_count) | `3` | Advanced | Architecture |
| [rgw_posix_cache_max_buckets](#rgw_posix_cache_max_buckets) | `100` | Advanced | Architecture |
| [rgw_posix_cache_partitions](#rgw_posix_cache_partitions) | `3` | Advanced | Architecture |
| [rgw_posix_database_root](#rgw_posix_database_root) | `/var/lib/ceph/radosgw` | Advanced | Architecture |
| [rgw_posix_userdb_dir](#rgw_posix_userdb_dir) | `/var/lib/ceph/radosgw` | Advanced | Architecture |

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

### rgw_posix_base_path

| | |
|---|---|
| نوع | Str · default `/tmp/rgw_posix_driver` · **Advanced** |
| جدول | [rgw.md#SP_rgw_posix_base_path](../../../config/rgw/rgw.md#SP_rgw_posix_base_path) |

**کارکرد:** experimental Option to set base path for POSIX Driver

**زمان استفاده:** backendهای آزمایشی Motr/POSIX RGW — فقط در استقرار PoC تخصصی.

**مثال:**

```bash
ceph config set client.rgw rgw_posix_base_path "/tmp/rgw_posix_driver"
ceph config get client.rgw rgw_posix_base_path
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `/tmp/rgw_posix_driver` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### rgw_posix_cache_lanes

| | |
|---|---|
| نوع | Int · default `3` · **Advanced** |
| جدول | [rgw.md#SP_rgw_posix_cache_lanes](../../../config/rgw/rgw.md#SP_rgw_posix_cache_lanes) |

**کارکرد:** experimental Number of lanes in cache LRU

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**مثال:**

```bash
ceph config set client.rgw rgw_posix_cache_lanes 3
ceph config get client.rgw rgw_posix_cache_lanes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `3` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### rgw_posix_cache_lmdb_count

| | |
|---|---|
| نوع | Int · default `3` · **Advanced** |
| جدول | [rgw.md#SP_rgw_posix_cache_lmdb_count](../../../config/rgw/rgw.md#SP_rgw_posix_cache_lmdb_count) |

**کارکرد:** experimental Number of lmdb partitions in the ordered listing cache

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**مثال:**

```bash
ceph config set client.rgw rgw_posix_cache_lmdb_count 3
ceph config get client.rgw rgw_posix_cache_lmdb_count
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `3` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### rgw_posix_cache_max_buckets

| | |
|---|---|
| نوع | Int · default `100` · **Advanced** |
| جدول | [rgw.md#SP_rgw_posix_cache_max_buckets](../../../config/rgw/rgw.md#SP_rgw_posix_cache_max_buckets) |

**کارکرد:** experimental Number of buckets to maintain in the ordered listing cache

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**مثال:**

```bash
ceph config set client.rgw rgw_posix_cache_max_buckets 100
ceph config get client.rgw rgw_posix_cache_max_buckets
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `100` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### rgw_posix_cache_partitions

| | |
|---|---|
| نوع | Int · default `3` · **Advanced** |
| جدول | [rgw.md#SP_rgw_posix_cache_partitions](../../../config/rgw/rgw.md#SP_rgw_posix_cache_partitions) |

**کارکرد:** experimental Number of partitions in cache AVL

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**مثال:**

```bash
ceph config set client.rgw rgw_posix_cache_partitions 3
ceph config get client.rgw rgw_posix_cache_partitions
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `3` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### rgw_posix_database_root

| | |
|---|---|
| نوع | Str · default `/var/lib/ceph/radosgw` · **Advanced** |
| جدول | [rgw.md#SP_rgw_posix_database_root](../../../config/rgw/rgw.md#SP_rgw_posix_database_root) |

**کارکرد:** experimental Path to parent of POSIX Driver LMDB bucket listing cache

**زمان استفاده:** backendهای آزمایشی Motr/POSIX RGW — فقط در استقرار PoC تخصصی.

**مثال:**

```bash
ceph config set client.rgw rgw_posix_database_root "/var/lib/ceph/radosgw"
ceph config get client.rgw rgw_posix_database_root
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `/var/lib/ceph/radosgw` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### rgw_posix_userdb_dir

| | |
|---|---|
| نوع | Str · default `/var/lib/ceph/radosgw` · **Advanced** |
| جدول | [rgw.md#SP_rgw_posix_userdb_dir](../../../config/rgw/rgw.md#SP_rgw_posix_userdb_dir) |

**کارکرد:** path for the directory for storing the User db

**زمان استفاده:** backendهای آزمایشی Motr/POSIX RGW — فقط در استقرار PoC تخصصی.

**مثال:**

```bash
ceph config set client.rgw rgw_posix_userdb_dir "/var/lib/ceph/radosgw"
ceph config get client.rgw rgw_posix_userdb_dir
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `/var/lib/ceph/radosgw` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
