# General

راهنمای عمیق پیکربندی RBD — 3 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rbd_cache](#rbd_cache) | `True` | Advanced | Performance |
| [rbd_plugins](#rbd_plugins) | `(empty)` | Advanced | Performance |
| [rbd_tracing](#rbd_tracing) | `False` | Advanced | Performance |

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

### rbd_cache

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rbd.md#SP_rbd_cache](../../../config/rbd/rbd.md#SP_rbd_cache) |

**کارکرد:** whether to enable caching (writeback unless rbd_cache_max_dirty is 0)

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client rbd_cache false
ceph config get client rbd_cache
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_cache
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_plugins

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rbd.md#SP_rbd_plugins](../../../config/rbd/rbd.md#SP_rbd_plugins) |

**کارکرد:** comma-delimited list of librbd plugins to enable

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_plugins "example"
ceph config get client rbd_plugins
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_plugins
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_tracing

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rbd.md#SP_rbd_tracing](../../../config/rbd/rbd.md#SP_rbd_tracing) |

**کارکرد:** true if LTTng-UST tracepoints should be enabled

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client rbd_tracing true
ceph config get client rbd_tracing
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_tracing
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---


[← نمای کلی](../OVERVIEW.md)
