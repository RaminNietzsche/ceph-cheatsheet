# Lockdep

deep dive پیکربندی Global — 2 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [lockdep](#lockdep) | `False` | Dev | Dev |
| [lockdep_force_backtrace](#lockdep_force_backtrace) | `False` | Dev | Dev |

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

### lockdep

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [lockdep.md#SP_lockdep](../../../config/global/lockdep.md#SP_lockdep) |

**کارکرد:** Enable the lockdep lock dependency analyzer

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set global lockdep true
ceph config get global lockdep
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### lockdep_force_backtrace

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [lockdep.md#SP_lockdep_force_backtrace](../../../config/global/lockdep.md#SP_lockdep_force_backtrace) |

**کارکرد:** Gather a current backtrace at every lock

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set global lockdep_force_backtrace true
ceph config get global lockdep_force_backtrace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
