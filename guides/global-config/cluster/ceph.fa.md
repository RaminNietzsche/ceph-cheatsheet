# Ceph

deep dive پیکربندی Global — 1 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [ceph_assert_supresssions](#ceph_assert_supresssions) | `(empty)` | Dev | Dev |

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

### ceph_assert_supresssions

| | |
|---|---|
| نوع | Str · default `(empty)` · **Dev** |
| جدول | [ceph.md#SP_ceph_assert_supresssions](../../../config/global/ceph.md#SP_ceph_assert_supresssions) |

**کارکرد:** Suppress specific ceph_assert instances to let the execution continue with unknown, potentially DESTRUCTIVE consequences.

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set global ceph_assert_supresssions "example"
ceph config get global ceph_assert_supresssions
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`(empty)`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
