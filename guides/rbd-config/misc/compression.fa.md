# Compression

راهنمای عمیق پیکربندی RBD — 1 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rbd_compression_hint](#rbd_compression_hint) | `none` | Basic | Policy |

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
ceph config get <daemon> <option>  # e.g. rbd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_compression_hint

| | |
|---|---|
| نوع | Str · enum: ["none", "compressible", "incompressible"] · default `none` · **Basic** |
| جدول | [rbd.md#SP_rbd_compression_hint](../../../config/rbd/rbd.md#SP_rbd_compression_hint) |

**کارکرد:** Compression hint to send to the OSDs during writes

**زمان استفاده:** رفتار اصلی RBD — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set client rbd_compression_hint none
ceph config get client rbd_compression_hint
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `none` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_compression_hint
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---


[← نمای کلی](../OVERVIEW.md)
