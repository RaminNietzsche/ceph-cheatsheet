# Zones, realm & region

راهنمای عمیق پیکربندی RGW — 19 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_default_realm_info_oid](#rgw_default_realm_info_oid) | `default.realm` | Advanced | Performance |
| [rgw_default_region_info_oid](#rgw_default_region_info_oid) | `default.region` | Advanced | Performance |
| [rgw_default_zone_info_oid](#rgw_default_zone_info_oid) | `default.zone` | Advanced | Performance |
| [rgw_default_zonegroup_info_oid](#rgw_default_zonegroup_info_oid) | `default.zonegroup` | Advanced | Performance |
| [rgw_period_latest_epoch_info_oid](#rgw_period_latest_epoch_info_oid) | `.latest_epoch` | Dev | Performance |
| [rgw_period_push_interval](#rgw_period_push_interval) | `2` | Advanced | Performance |
| [rgw_period_push_interval_max](#rgw_period_push_interval_max) | `30` | Advanced | Performance |
| [rgw_period_root_pool](#rgw_period_root_pool) | `.rgw.root` | Advanced | Performance |
| [rgw_realm](#rgw_realm) | `(empty)` | Advanced | Architecture |
| [rgw_realm_id](#rgw_realm_id) | `(empty)` | Advanced | Architecture |
| [rgw_realm_root_pool](#rgw_realm_root_pool) | `.rgw.root` | Advanced | Architecture |
| [rgw_region](#rgw_region) | `(empty)` | Advanced | Architecture |
| [rgw_region_root_pool](#rgw_region_root_pool) | `.rgw.root` | Advanced | Architecture |
| [rgw_zone](#rgw_zone) | `(empty)` | Advanced | Architecture |
| [rgw_zone_id](#rgw_zone_id) | `(empty)` | Advanced | Architecture |
| [rgw_zone_root_pool](#rgw_zone_root_pool) | `.rgw.root` | Advanced | Architecture |
| [rgw_zonegroup](#rgw_zonegroup) | `(empty)` | Advanced | Architecture |
| [rgw_zonegroup_id](#rgw_zonegroup_id) | `(empty)` | Advanced | Architecture |
| [rgw_zonegroup_root_pool](#rgw_zonegroup_root_pool) | `.rgw.root` | Advanced | Architecture |

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

### rgw_default_realm_info_oid

| | |
|---|---|
| نوع | Str · default `default.realm` · **Advanced** |
| جدول | [rgw.md#SP_rgw_default_realm_info_oid](../../../config/rgw/rgw.md#SP_rgw_default_realm_info_oid) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_default_realm_info_oid "default.realm"
ceph config get client.rgw rgw_default_realm_info_oid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `default.realm`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_default_realm_info_oid
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_default_region_info_oid

| | |
|---|---|
| نوع | Str · default `default.region` · **Advanced** |
| جدول | [rgw.md#SP_rgw_default_region_info_oid](../../../config/rgw/rgw.md#SP_rgw_default_region_info_oid) |

**کارکرد:** Default region info object id

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_default_region_info_oid "default.region"
ceph config get client.rgw rgw_default_region_info_oid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `default.region`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_default_region_info_oid
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_default_zone_info_oid

| | |
|---|---|
| نوع | Str · default `default.zone` · **Advanced** |
| جدول | [rgw.md#SP_rgw_default_zone_info_oid](../../../config/rgw/rgw.md#SP_rgw_default_zone_info_oid) |

**کارکرد:** Default zone info object id

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_default_zone_info_oid "default.zone"
ceph config get client.rgw rgw_default_zone_info_oid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `default.zone`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_default_zone_info_oid
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_default_zonegroup_info_oid

| | |
|---|---|
| نوع | Str · default `default.zonegroup` · **Advanced** |
| جدول | [rgw.md#SP_rgw_default_zonegroup_info_oid](../../../config/rgw/rgw.md#SP_rgw_default_zonegroup_info_oid) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_default_zonegroup_info_oid "default.zonegroup"
ceph config get client.rgw rgw_default_zonegroup_info_oid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `default.zonegroup`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_default_zonegroup_info_oid
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_period_latest_epoch_info_oid

| | |
|---|---|
| نوع | Str · default `.latest_epoch` · **Dev** |
| جدول | [rgw.md#SP_rgw_period_latest_epoch_info_oid](../../../config/rgw/rgw.md#SP_rgw_period_latest_epoch_info_oid) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_period_latest_epoch_info_oid ".latest_epoch"
ceph config get client.rgw rgw_period_latest_epoch_info_oid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `.latest_epoch` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_period_latest_epoch_info_oid
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_period_push_interval

| | |
|---|---|
| نوع | Float · default `2` · **Advanced** |
| جدول | [rgw.md#SP_rgw_period_push_interval](../../../config/rgw/rgw.md#SP_rgw_period_push_interval) |

**کارکرد:** Period push interval

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_period_push_interval 2
ceph config get client.rgw rgw_period_push_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `2` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_period_push_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_period_push_interval_max

| | |
|---|---|
| نوع | Float · default `30` · **Advanced** |
| جدول | [rgw.md#SP_rgw_period_push_interval_max](../../../config/rgw/rgw.md#SP_rgw_period_push_interval_max) |

**کارکرد:** Period push maximum interval

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_period_push_interval_max 30
ceph config get client.rgw rgw_period_push_interval_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `30` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_period_push_interval_max
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_period_root_pool

| | |
|---|---|
| نوع | Str · default `.rgw.root` · **Advanced** |
| جدول | [rgw.md#SP_rgw_period_root_pool](../../../config/rgw/rgw.md#SP_rgw_period_root_pool) |

**کارکرد:** Period root pool

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_period_root_pool ".rgw.root"
ceph config get client.rgw rgw_period_root_pool
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `.rgw.root` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_period_root_pool
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_realm

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_realm](../../../config/rgw/rgw.md#SP_rgw_realm) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_realm "default"
ceph config get client.rgw rgw_realm
radosgw-admin realm list
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_realm_id

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_realm_id](../../../config/rgw/rgw.md#SP_rgw_realm_id) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_realm_id <value>
ceph config get client.rgw rgw_realm_id
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_realm_root_pool

| | |
|---|---|
| نوع | Str · default `.rgw.root` · **Advanced** |
| جدول | [rgw.md#SP_rgw_realm_root_pool](../../../config/rgw/rgw.md#SP_rgw_realm_root_pool) |

**کارکرد:** Realm root pool

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_realm_root_pool ".rgw.root"
ceph config get client.rgw rgw_realm_root_pool
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`.rgw.root` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_region

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_region](../../../config/rgw/rgw.md#SP_rgw_region) |

**کارکرد:** Region name

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_region "us-east-1"
ceph config get client.rgw rgw_region
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_region_root_pool

| | |
|---|---|
| نوع | Str · default `.rgw.root` · **Advanced** |
| جدول | [rgw.md#SP_rgw_region_root_pool](../../../config/rgw/rgw.md#SP_rgw_region_root_pool) |

**کارکرد:** Region root pool

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_region_root_pool ".rgw.root"
ceph config get client.rgw rgw_region_root_pool
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`.rgw.root` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_zone

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_zone](../../../config/rgw/rgw.md#SP_rgw_zone) |

**کارکرد:** Zone name

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_zone "us-east-1"
ceph config get client.rgw rgw_zone
ceph config get client.rgw rgw_zone
radosgw-admin sync status
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_zone_id

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_zone_id](../../../config/rgw/rgw.md#SP_rgw_zone_id) |

**کارکرد:** Zone ID

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_zone_id <value>
ceph config get client.rgw rgw_zone_id
radosgw-admin sync status
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_zone_root_pool

| | |
|---|---|
| نوع | Str · default `.rgw.root` · **Advanced** |
| جدول | [rgw.md#SP_rgw_zone_root_pool](../../../config/rgw/rgw.md#SP_rgw_zone_root_pool) |

**کارکرد:** Zone root pool name

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_zone_root_pool ".rgw.root"
ceph config get client.rgw rgw_zone_root_pool
radosgw-admin sync status
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`.rgw.root` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_zonegroup

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_zonegroup](../../../config/rgw/rgw.md#SP_rgw_zonegroup) |

**کارکرد:** Zonegroup name

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_zonegroup "default"
ceph config get client.rgw rgw_zonegroup
ceph config get client.rgw rgw_zonegroup
radosgw-admin sync status
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_zonegroup_id

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_zonegroup_id](../../../config/rgw/rgw.md#SP_rgw_zonegroup_id) |

**کارکرد:** Zonegroup ID

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_zonegroup_id <value>
ceph config get client.rgw rgw_zonegroup_id
radosgw-admin sync status
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_zonegroup_root_pool

| | |
|---|---|
| نوع | Str · default `.rgw.root` · **Advanced** |
| جدول | [rgw.md#SP_rgw_zonegroup_root_pool](../../../config/rgw/rgw.md#SP_rgw_zonegroup_root_pool) |

**کارکرد:** Zonegroup root pool

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_zonegroup_root_pool ".rgw.root"
ceph config get client.rgw rgw_zonegroup_root_pool
radosgw-admin sync status
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`.rgw.root` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
