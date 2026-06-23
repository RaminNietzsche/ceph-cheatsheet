# Scheduler & dmclock

راهنمای عمیق پیکربندی RGW — 13 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_dmclock_admin_lim](#rgw_dmclock_admin_lim) | `0` | Advanced | Performance |
| [rgw_dmclock_admin_res](#rgw_dmclock_admin_res) | `100` | Advanced | Performance |
| [rgw_dmclock_admin_wgt](#rgw_dmclock_admin_wgt) | `100` | Advanced | Performance |
| [rgw_dmclock_auth_lim](#rgw_dmclock_auth_lim) | `0` | Advanced | Performance |
| [rgw_dmclock_auth_res](#rgw_dmclock_auth_res) | `200` | Advanced | Performance |
| [rgw_dmclock_auth_wgt](#rgw_dmclock_auth_wgt) | `100` | Advanced | Performance |
| [rgw_dmclock_data_lim](#rgw_dmclock_data_lim) | `0` | Advanced | Performance |
| [rgw_dmclock_data_res](#rgw_dmclock_data_res) | `500` | Advanced | Performance |
| [rgw_dmclock_data_wgt](#rgw_dmclock_data_wgt) | `500` | Advanced | Performance |
| [rgw_dmclock_metadata_lim](#rgw_dmclock_metadata_lim) | `0` | Advanced | Performance |
| [rgw_dmclock_metadata_res](#rgw_dmclock_metadata_res) | `500` | Advanced | Performance |
| [rgw_dmclock_metadata_wgt](#rgw_dmclock_metadata_wgt) | `500` | Advanced | Performance |
| [rgw_scheduler_type](#rgw_scheduler_type) | `throttler` | Advanced | Performance |

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

### rgw_dmclock_admin_lim

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [rgw.md#SP_rgw_dmclock_admin_lim](../../../config/rgw/rgw.md#SP_rgw_dmclock_admin_lim) |

**کارکرد:** mclock limit for admin requests

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_dmclock_admin_lim 0
ceph config get client.rgw rgw_dmclock_admin_lim
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`0`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**سیگنال‌ها:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_admin_lim
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_admin_res

| | |
|---|---|
| نوع | Float · default `100` · **Advanced** |
| جدول | [rgw.md#SP_rgw_dmclock_admin_res](../../../config/rgw/rgw.md#SP_rgw_dmclock_admin_res) |

**کارکرد:** mclock reservation for admin requests

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_dmclock_admin_res 100
ceph config get client.rgw rgw_dmclock_admin_res
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`100`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**سیگنال‌ها:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_admin_res
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_admin_wgt

| | |
|---|---|
| نوع | Float · default `100` · **Advanced** |
| جدول | [rgw.md#SP_rgw_dmclock_admin_wgt](../../../config/rgw/rgw.md#SP_rgw_dmclock_admin_wgt) |

**کارکرد:** mclock weight for admin requests

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_dmclock_admin_wgt 100
ceph config get client.rgw rgw_dmclock_admin_wgt
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`100`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**سیگنال‌ها:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_admin_wgt
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_auth_lim

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [rgw.md#SP_rgw_dmclock_auth_lim](../../../config/rgw/rgw.md#SP_rgw_dmclock_auth_lim) |

**کارکرد:** mclock limit for object data requests

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_dmclock_auth_lim 0
ceph config get client.rgw rgw_dmclock_auth_lim
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`0`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**سیگنال‌ها:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_auth_lim
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_auth_res

| | |
|---|---|
| نوع | Float · default `200` · **Advanced** |
| جدول | [rgw.md#SP_rgw_dmclock_auth_res](../../../config/rgw/rgw.md#SP_rgw_dmclock_auth_res) |

**کارکرد:** mclock reservation for object data requests

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_dmclock_auth_res 200
ceph config get client.rgw rgw_dmclock_auth_res
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`200`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**سیگنال‌ها:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_auth_res
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_auth_wgt

| | |
|---|---|
| نوع | Float · default `100` · **Advanced** |
| جدول | [rgw.md#SP_rgw_dmclock_auth_wgt](../../../config/rgw/rgw.md#SP_rgw_dmclock_auth_wgt) |

**کارکرد:** mclock weight for object data requests

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_dmclock_auth_wgt 100
ceph config get client.rgw rgw_dmclock_auth_wgt
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`100`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**سیگنال‌ها:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_auth_wgt
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_data_lim

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [rgw.md#SP_rgw_dmclock_data_lim](../../../config/rgw/rgw.md#SP_rgw_dmclock_data_lim) |

**کارکرد:** mclock limit for object data requests

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_dmclock_data_lim 0
ceph config get client.rgw rgw_dmclock_data_lim
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`0`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**سیگنال‌ها:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_data_lim
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_data_res

| | |
|---|---|
| نوع | Float · default `500` · **Advanced** |
| جدول | [rgw.md#SP_rgw_dmclock_data_res](../../../config/rgw/rgw.md#SP_rgw_dmclock_data_res) |

**کارکرد:** mclock reservation for object data requests

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_dmclock_data_res 500
ceph config get client.rgw rgw_dmclock_data_res
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`500`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**سیگنال‌ها:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_data_res
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_data_wgt

| | |
|---|---|
| نوع | Float · default `500` · **Advanced** |
| جدول | [rgw.md#SP_rgw_dmclock_data_wgt](../../../config/rgw/rgw.md#SP_rgw_dmclock_data_wgt) |

**کارکرد:** mclock weight for object data requests

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_dmclock_data_wgt 500
ceph config get client.rgw rgw_dmclock_data_wgt
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`500`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**سیگنال‌ها:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_data_wgt
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_metadata_lim

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [rgw.md#SP_rgw_dmclock_metadata_lim](../../../config/rgw/rgw.md#SP_rgw_dmclock_metadata_lim) |

**کارکرد:** mclock limit for metadata requests

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_dmclock_metadata_lim 0
ceph config get client.rgw rgw_dmclock_metadata_lim
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`0`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**سیگنال‌ها:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_metadata_lim
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_metadata_res

| | |
|---|---|
| نوع | Float · default `500` · **Advanced** |
| جدول | [rgw.md#SP_rgw_dmclock_metadata_res](../../../config/rgw/rgw.md#SP_rgw_dmclock_metadata_res) |

**کارکرد:** mclock reservation for metadata requests

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_dmclock_metadata_res 500
ceph config get client.rgw rgw_dmclock_metadata_res
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`500`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**سیگنال‌ها:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_metadata_res
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_metadata_wgt

| | |
|---|---|
| نوع | Float · default `500` · **Advanced** |
| جدول | [rgw.md#SP_rgw_dmclock_metadata_wgt](../../../config/rgw/rgw.md#SP_rgw_dmclock_metadata_wgt) |

**کارکرد:** mclock weight for metadata requests

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_dmclock_metadata_wgt 500
ceph config get client.rgw rgw_dmclock_metadata_wgt
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`500`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**سیگنال‌ها:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_metadata_wgt
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_scheduler_type

| | |
|---|---|
| نوع | Str · default `throttler` · **Advanced** |
| جدول | [rgw.md#SP_rgw_scheduler_type](../../../config/rgw/rgw.md#SP_rgw_scheduler_type) |

**کارکرد:** Set the type of dmclock scheduler, defaults to throttler. Other valid value is dmclock which is experimental.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_scheduler_type throttler
ceph config get client.rgw rgw_scheduler_type
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `throttler`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_scheduler_type
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
