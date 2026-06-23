# Objectstore

deep dive پیکربندی Global — 2 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [objectstore_blackhole](#objectstore_blackhole) | `False` | Advanced | Performance |
| [objectstore_debug_throw_on_failed_txc](#objectstore_debug_throw_on_failed_txc) | `False` | Dev | Dev |

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

### objectstore_blackhole

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [objectstore.md#SP_objectstore_blackhole](../../../config/global/objectstore.md#SP_objectstore_blackhole) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set global objectstore_blackhole true
ceph config get global objectstore_blackhole
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global objectstore_blackhole
ceph -s
```

---

### objectstore_debug_throw_on_failed_txc

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [objectstore.md#SP_objectstore_debug_throw_on_failed_txc](../../../config/global/objectstore.md#SP_objectstore_debug_throw_on_failed_txc) |

**کارکرد:** Enables exception throwing instead of process abort on transaction submission error.

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set global objectstore_debug_throw_on_failed_txc true
ceph config get global objectstore_debug_throw_on_failed_txc
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
