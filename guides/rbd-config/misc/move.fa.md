# Move

deep dive پیکربندی RBD — 3 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rbd_move_parent_to_trash_on_remove](#rbd_move_parent_to_trash_on_remove) | `False` | Basic | Policy |
| [rbd_move_to_trash_on_remove](#rbd_move_to_trash_on_remove) | `False` | Basic | Policy |
| [rbd_move_to_trash_on_remove_expire_seconds](#rbd_move_to_trash_on_remove_expire_seconds) | `0` | Basic | Policy |

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
ceph config get <daemon> <option>  # e.g. rbd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_move_parent_to_trash_on_remove

| | |
|---|---|
| نوع | Bool · default `False` · **Basic** |
| جدول | [rbd.md#SP_rbd_move_parent_to_trash_on_remove](../../../config/rbd/rbd.md#SP_rbd_move_parent_to_trash_on_remove) |

**کارکرد:** move parent with clone format v2 children to the trash when deleted

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client rbd_move_parent_to_trash_on_remove true
ceph config get client rbd_move_parent_to_trash_on_remove
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_move_parent_to_trash_on_remove
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_move_to_trash_on_remove

| | |
|---|---|
| نوع | Bool · default `False` · **Basic** |
| جدول | [rbd.md#SP_rbd_move_to_trash_on_remove](../../../config/rbd/rbd.md#SP_rbd_move_to_trash_on_remove) |

**کارکرد:** automatically move images to the trash when deleted

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client rbd_move_to_trash_on_remove true
ceph config get client rbd_move_to_trash_on_remove
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_move_to_trash_on_remove
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_move_to_trash_on_remove_expire_seconds

| | |
|---|---|
| نوع | Uint · default `0` · **Basic** |
| جدول | [rbd.md#SP_rbd_move_to_trash_on_remove_expire_seconds](../../../config/rbd/rbd.md#SP_rbd_move_to_trash_on_remove_expire_seconds) |

**کارکرد:** default number of seconds to protect deleted images in the trash

**زمان استفاده:** رفتار اصلی RBD — قبل از تغییر در production بررسی کنید.

**مثال:**

```bash
ceph config set client rbd_move_to_trash_on_remove_expire_seconds 64
ceph config get client rbd_move_to_trash_on_remove_expire_seconds
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `0` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_move_to_trash_on_remove_expire_seconds
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---


[← نمای کلی](../OVERVIEW.md)
