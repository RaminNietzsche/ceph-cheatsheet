# Device

راهنمای عمیق پیکربندی Global — 1 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [device_failure_prediction_mode](#device_failure_prediction_mode) | `none` | Basic | سیاست |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **سیاست** | امنیت، سازگاری، پیش‌فرض‌های عملیاتی |
| **ظرفیت** | چیدمان دیسک، مسیرها، اندازه‌گیری |
| **عملکرد** | خط پایه → تغییر تدریجی → پایش کلاستر |
| **اتصال** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **توسعه** | در محیط عملیاتی همان پیش‌فرض upstream |

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

**کارکرد:** Method used to predict device failures To disable prediction, use 'none', 'local' uses a prediction model that runs inside the mgr daemon. 'cloud' will share metrics with a cloud service and query the service for devicelife expectancy.

**زمان استفاده:** رفتار اصلی Global — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set global device_failure_prediction_mode none
ceph config get global device_failure_prediction_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `none` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global device_failure_prediction_mode
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
