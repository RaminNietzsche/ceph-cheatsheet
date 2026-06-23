# General

راهنمای عمیق پیکربندی MDS client — 1 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mds-client/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [fake_statfs_for_testing](#fake_statfs_for_testing) | `0` | Dev | Dev |

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
ceph config get <daemon> <option>  # e.g. mds-client
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### fake_statfs_for_testing

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [fake.md#SP_fake_statfs_for_testing](../../../config/mds-client/fake.md#SP_fake_statfs_for_testing) |

**کارکرد:** Set a value for kb and compute kb_used from total of num_bytes

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client fake_statfs_for_testing 64
ceph config get client fake_statfs_for_testing
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
