# Auth & caps

راهنمای عمیق پیکربندی MON — 1 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mon_auth_validate_all_caps](#mon_auth_validate_all_caps) | `True` | Advanced | Policy |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_auth_validate_all_caps

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_auth_validate_all_caps](../../../config/mon/mon.md#SP_mon_auth_validate_all_caps) |

**کارکرد:** Whether to parse non-monitor capabilities set by the 'ceph auth ...' commands. Disabling this saves CPU on the monitor, but allows invalid capabilities to be set, and only be rejected later, when they are used.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_auth_validate_all_caps false
ceph config get mon mon_auth_validate_all_caps
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_auth_validate_all_caps
ceph -s
ceph mon stat
```

---


[← نمای کلی](../OVERVIEW.md)
