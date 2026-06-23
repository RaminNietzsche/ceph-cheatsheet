# Read

راهنمای عمیق پیکربندی RBD — 1 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rbd_read_from_replica_policy](#rbd_read_from_replica_policy) | `default` | Basic | سیاست |

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
ceph config get <daemon> <option>  # e.g. rbd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_read_from_replica_policy

| | |
|---|---|
| نوع | Str · enum: ["default", "balance", "localize"] · default `default` · **Basic** |
| جدول | [rbd.md#SP_rbd_read_from_replica_policy](../../../config/rbd/rbd.md#SP_rbd_read_from_replica_policy) |

**کارکرد:** Read replica policy send to the OSDS during reads

**زمان استفاده:** رفتار اصلی RBD — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set client rbd_read_from_replica_policy default
ceph config get client rbd_read_from_replica_policy
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `default` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_read_from_replica_policy
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---


[← نمای کلی](../OVERVIEW.md)
