# Objectstore

راهنمای عمیق پیکربندی Global — 2 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

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
| **Connectivity** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **Dev** | در محیط عملیاتی همان پیش‌فرض upstream |

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

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global objectstore_blackhole true
ceph config get global objectstore_blackhole
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

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

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global objectstore_debug_throw_on_failed_txc true
ceph config get global objectstore_debug_throw_on_failed_txc
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
