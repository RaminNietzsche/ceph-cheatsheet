# Host

راهنمای عمیق پیکربندی Global — 1 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [host](#host) | `(empty)` | Basic | Policy |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **Policy** | امنیت، سازگاری، پیش‌فرض‌های عملیاتی |
| **Capacity** | چیدمان دیسک، مسیرها، اندازه‌گیری |
| **Performance** | خط پایه → تغییر تدریجی → پایش کلاستر |
| **Connectivity** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **Dev** | در محیط عملیاتی همان پیش‌فرض upstream |

**ابزارهای مشترک:**

```bash
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### host

| | |
|---|---|
| نوع | Str · default `(empty)` · **Basic** |
| جدول | [host.md#SP_host](../../../config/global/host.md#SP_host) |

**کارکرد:** local hostname

**زمان استفاده:** رفتار اصلی Global — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set global host "example"
ceph config get global host
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `(empty)` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global host
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
