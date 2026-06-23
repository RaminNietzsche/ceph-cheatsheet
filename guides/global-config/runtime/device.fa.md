# Device

deep dive پیکربندی Global — 1 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [device_failure_prediction_mode](#device_failure_prediction_mode) | `none` | Basic | Policy |

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

### device_failure_prediction_mode

| | |
|---|---|
| نوع | Str · enum: ["none", "local", "cloud"] · default `none` · **Basic** |
| جدول | [device.md#SP_device_failure_prediction_mode](../../../config/global/device.md#SP_device_failure_prediction_mode) |

**کارکرد:** Method used to predict device failures

**زمان استفاده:** رفتار اصلی Global — قبل از تغییر در production بررسی کنید.

**مثال:**

```bash
ceph config set global device_failure_prediction_mode none
ceph config get global device_failure_prediction_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `none` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global device_failure_prediction_mode
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
