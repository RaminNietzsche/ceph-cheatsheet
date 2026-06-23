# Motr backend

راهنمای عمیق پیکربندی RGW — 7 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [motr_admin_endpoint](#motr_admin_endpoint) | `192.168.180.182@tcp:12345:4:1` | Advanced | Architecture |
| [motr_admin_fid](#motr_admin_fid) | `0x7200000000000001:0x0` | Advanced | Architecture |
| [motr_ha_endpoint](#motr_ha_endpoint) | `192.168.180.182@tcp:12345:1:1` | Advanced | Architecture |
| [motr_my_endpoint](#motr_my_endpoint) | `192.168.180.182@tcp:12345:4:1` | Advanced | Architecture |
| [motr_my_fid](#motr_my_fid) | `0x7200000000000001:0x0` | Advanced | Architecture |
| [motr_profile_fid](#motr_profile_fid) | `0x7000000000000001:0x0` | Advanced | Architecture |
| [motr_tracing_enabled](#motr_tracing_enabled) | `False` | Advanced | Dev |

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

### motr_admin_endpoint

| | |
|---|---|
| نوع | Str · default `192.168.180.182@tcp:12345:4:1` · **Advanced** |
| جدول | [motr.md#SP_motr_admin_endpoint](../../../config/rgw/motr.md#SP_motr_admin_endpoint) |

**کارکرد:** experimental Option to set Admin Motr endpoint address

**زمان استفاده:** backendهای آزمایشی Motr/POSIX RGW — فقط در استقرار PoC تخصصی.

**مثال:**

```bash
ceph config set client.rgw motr_admin_endpoint "192.168.180.182@tcp:12345:4:1"
ceph config get client.rgw motr_admin_endpoint
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `192.168.180.182@tcp:12345:4:1` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### motr_admin_fid

| | |
|---|---|
| نوع | Str · default `0x7200000000000001:0x0` · **Advanced** |
| جدول | [motr.md#SP_motr_admin_fid](../../../config/rgw/motr.md#SP_motr_admin_fid) |

**کارکرد:** Admin Tool Motr FID for admin-level access.

**زمان استفاده:** backendهای آزمایشی Motr/POSIX RGW — فقط در استقرار PoC تخصصی.

**مثال:**

```bash
ceph config set client.rgw motr_admin_fid "0x7200000000000001:0x0"
ceph config get client.rgw motr_admin_fid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `0x7200000000000001:0x0` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### motr_ha_endpoint

| | |
|---|---|
| نوع | Str · default `192.168.180.182@tcp:12345:1:1` · **Advanced** |
| جدول | [motr.md#SP_motr_ha_endpoint](../../../config/rgw/motr.md#SP_motr_ha_endpoint) |

**کارکرد:** experimental Option to set Motr HA agent endpoint address

**زمان استفاده:** backendهای آزمایشی Motr/POSIX RGW — فقط در استقرار PoC تخصصی.

**مثال:**

```bash
ceph config set client.rgw motr_ha_endpoint "192.168.180.182@tcp:12345:1:1"
ceph config get client.rgw motr_ha_endpoint
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `192.168.180.182@tcp:12345:1:1` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### motr_my_endpoint

| | |
|---|---|
| نوع | Str · default `192.168.180.182@tcp:12345:4:1` · **Advanced** |
| جدول | [motr.md#SP_motr_my_endpoint](../../../config/rgw/motr.md#SP_motr_my_endpoint) |

**کارکرد:** experimental Option to set my Motr endpoint address

**زمان استفاده:** backendهای آزمایشی Motr/POSIX RGW — فقط در استقرار PoC تخصصی.

**مثال:**

```bash
ceph config set client.rgw motr_my_endpoint "192.168.180.182@tcp:12345:4:1"
ceph config get client.rgw motr_my_endpoint
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `192.168.180.182@tcp:12345:4:1` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### motr_my_fid

| | |
|---|---|
| نوع | Str · default `0x7200000000000001:0x0` · **Advanced** |
| جدول | [motr.md#SP_motr_my_fid](../../../config/rgw/motr.md#SP_motr_my_fid) |

**کارکرد:** experimental Option to set my Motr fid

**زمان استفاده:** backendهای آزمایشی Motr/POSIX RGW — فقط در استقرار PoC تخصصی.

**مثال:**

```bash
ceph config set client.rgw motr_my_fid "0x7200000000000001:0x0"
ceph config get client.rgw motr_my_fid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `0x7200000000000001:0x0` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### motr_profile_fid

| | |
|---|---|
| نوع | Str · default `0x7000000000000001:0x0` · **Advanced** |
| جدول | [motr.md#SP_motr_profile_fid](../../../config/rgw/motr.md#SP_motr_profile_fid) |

**کارکرد:** experimental Option to set Motr profile fid

**زمان استفاده:** backendهای آزمایشی Motr/POSIX RGW — فقط در استقرار PoC تخصصی.

**مثال:**

```bash
ceph config set client.rgw motr_profile_fid "0x7000000000000001:0x0"
ceph config get client.rgw motr_profile_fid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `0x7000000000000001:0x0` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### motr_tracing_enabled

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [motr.md#SP_motr_tracing_enabled](../../../config/rgw/motr.md#SP_motr_tracing_enabled) |

**کارکرد:** Set to true when Motr client debugging is needed

**زمان استفاده:** backendهای آزمایشی Motr/POSIX RGW — فقط در استقرار PoC تخصصی.

**مثال:**

```bash
ceph config set client.rgw motr_tracing_enabled true
ceph config get client.rgw motr_tracing_enabled
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`False`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
