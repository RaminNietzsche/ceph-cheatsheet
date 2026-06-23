# Fsid

deep dive پیکربندی Global — 1 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [fsid](#fsid) | `(empty)` | Basic | Policy |

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

### fsid

| | |
|---|---|
| نوع | Uuid · default `(empty)` · **Basic** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [fsid.md#SP_fsid](../../../config/global/fsid.md#SP_fsid) |

**کارکرد:** cluster fsid (uuid)

**زمان استفاده:** رفتار اصلی Global — قبل از تغییر در production بررسی کنید.

**مثال:**

```bash
ceph config set global fsid (empty)
ceph config get global fsid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `(empty)` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global fsid
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
