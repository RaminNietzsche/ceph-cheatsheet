# Auto

راهنمای عمیق پیکربندی RBD — 1 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rbd_auto_exclusive_lock_until_manual_request](#rbd_auto_exclusive_lock_until_manual_request) | `True` | Advanced | Performance |

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

### rbd_auto_exclusive_lock_until_manual_request

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rbd.md#SP_rbd_auto_exclusive_lock_until_manual_request](../../../config/rbd/rbd.md#SP_rbd_auto_exclusive_lock_until_manual_request) |

**کارکرد:** automatically acquire/release exclusive lock until it is explicitly requested

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client rbd_auto_exclusive_lock_until_manual_request false
ceph config get client rbd_auto_exclusive_lock_until_manual_request
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_auto_exclusive_lock_until_manual_request
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---


[← نمای کلی](../OVERVIEW.md)
