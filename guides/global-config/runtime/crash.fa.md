# Crash

راهنمای عمیق پیکربندی Global — 1 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [crash_dir](#crash_dir) | `/var/lib/ceph/crash` | Advanced | Capacity |

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

### crash_dir

| | |
|---|---|
| نوع | Str · default `/var/lib/ceph/crash` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [crash.md#SP_crash_dir](../../../config/global/crash.md#SP_crash_dir) |

**کارکرد:** Directory where crash reports are archived

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global crash_dir "/var/lib/ceph/crash"
ceph config get global crash_dir
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. خط پایه روی `/var/lib/ceph/crash`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global crash_dir
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
