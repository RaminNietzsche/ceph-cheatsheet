# Auth

deep dive پیکربندی Global — 9 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [auth_allow_insecure_global_id_reclaim](#auth_allow_insecure_global_id_reclaim) | `True` | Advanced | Policy |
| [auth_client_required](#auth_client_required) | `cephx, none` | Advanced | Performance |
| [auth_cluster_required](#auth_cluster_required) | `cephx` | Advanced | Performance |
| [auth_debug](#auth_debug) | `False` | Dev | Dev |
| [auth_expose_insecure_global_id_reclaim](#auth_expose_insecure_global_id_reclaim) | `True` | Advanced | Policy |
| [auth_mon_ticket_ttl](#auth_mon_ticket_ttl) | `72_hr` | Advanced | Performance |
| [auth_service_required](#auth_service_required) | `cephx` | Advanced | Performance |
| [auth_service_ticket_ttl](#auth_service_ticket_ttl) | `1_hr` | Advanced | Performance |
| [auth_supported](#auth_supported) | `(empty)` | Advanced | Performance |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **Policy** | امنیت، سازگاری، پیش‌فرض‌های عملیاتی |
| **Capacity** | چیدمان دیسک، مسیرها، اندازه‌گیری |
| **Performance** | خط پایه → تغییر تدریجی → پایش کلاستر |
| **Connectivity** | نزدیک‌ترین endpoint پایدار خارجی |
| **Dev** | پیش‌فرض upstream در production |

**ابزارهای مشترک:**

```bash
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### auth_allow_insecure_global_id_reclaim

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [auth.md#SP_auth_allow_insecure_global_id_reclaim](../../../config/global/auth.md#SP_auth_allow_insecure_global_id_reclaim) |

**کارکرد:** Allow reclaiming global_id without presenting a valid ticket proving previous possession of that global_id

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global auth_allow_insecure_global_id_reclaim false
ceph config get global auth_allow_insecure_global_id_reclaim
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global auth_allow_insecure_global_id_reclaim
ceph -s
```

---

### auth_client_required

| | |
|---|---|
| نوع | Str · default `cephx, none` · **Advanced** |
| جدول | [auth.md#SP_auth_client_required](../../../config/global/auth.md#SP_auth_client_required) |

**کارکرد:** Authentication methods allowed by clients

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global auth_client_required "cephx, none"
ceph config get global auth_client_required
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `cephx, none`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global auth_client_required
ceph -s
```

---

### auth_cluster_required

| | |
|---|---|
| نوع | Str · default `cephx` · **Advanced** |
| جدول | [auth.md#SP_auth_cluster_required](../../../config/global/auth.md#SP_auth_cluster_required) |

**کارکرد:** Authentication methods required by the cluster

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global auth_cluster_required cephx
ceph config get global auth_cluster_required
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `cephx`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global auth_cluster_required
ceph -s
```

---

### auth_debug

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [auth.md#SP_auth_debug](../../../config/global/auth.md#SP_auth_debug) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set global auth_debug true
ceph config get global auth_debug
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### auth_expose_insecure_global_id_reclaim

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [auth.md#SP_auth_expose_insecure_global_id_reclaim](../../../config/global/auth.md#SP_auth_expose_insecure_global_id_reclaim) |

**کارکرد:** Force older clients that may omit their ticket on reconnects to reconnect as part of establishing a session

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global auth_expose_insecure_global_id_reclaim false
ceph config get global auth_expose_insecure_global_id_reclaim
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global auth_expose_insecure_global_id_reclaim
ceph -s
```

---

### auth_mon_ticket_ttl

| | |
|---|---|
| نوع | Float · default `72_hr` · **Advanced** |
| جدول | [auth.md#SP_auth_mon_ticket_ttl](../../../config/global/auth.md#SP_auth_mon_ticket_ttl) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global auth_mon_ticket_ttl 72_hr
ceph config get global auth_mon_ticket_ttl
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `72_hr`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global auth_mon_ticket_ttl
ceph -s
```

---

### auth_service_required

| | |
|---|---|
| نوع | Str · default `cephx` · **Advanced** |
| جدول | [auth.md#SP_auth_service_required](../../../config/global/auth.md#SP_auth_service_required) |

**کارکرد:** Authentication methods required by service daemons

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global auth_service_required cephx
ceph config get global auth_service_required
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `cephx`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global auth_service_required
ceph -s
```

---

### auth_service_ticket_ttl

| | |
|---|---|
| نوع | Float · default `1_hr` · **Advanced** |
| جدول | [auth.md#SP_auth_service_ticket_ttl](../../../config/global/auth.md#SP_auth_service_ticket_ttl) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global auth_service_ticket_ttl 1_hr
ceph config get global auth_service_ticket_ttl
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1_hr`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global auth_service_ticket_ttl
ceph -s
```

---

### auth_supported

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [auth.md#SP_auth_supported](../../../config/global/auth.md#SP_auth_supported) |

**کارکرد:** Authentication methods required (deprecated)

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global auth_supported "example"
ceph config get global auth_supported
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global auth_supported
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
