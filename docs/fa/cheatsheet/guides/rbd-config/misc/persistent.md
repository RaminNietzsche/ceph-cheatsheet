# Persistent

راهنمای عمیق پیکربندی RBD — 3 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rbd_persistent_cache_mode](#rbd_persistent_cache_mode) | `disabled` | Advanced | عملکرد |
| [rbd_persistent_cache_path](#rbd_persistent_cache_path) | `/tmp` | Advanced | ظرفیت |
| [rbd_persistent_cache_size](#rbd_persistent_cache_size) | `1_G` | Advanced | عملکرد |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **سیاست** | امنیت، سازگاری، پیش‌فرض‌های عملیاتی |
| **ظرفیت** | چیدمان دیسک، مسیرها، اندازه‌گیری |
| **عملکرد** | خط پایه → تغییر تدریجی → پایش کلاستر |
| **اتصال** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **توسعه** | در محیط عملیاتی همان پیش‌فرض upstream |

**ابزارهای مشترک:**

```bash
ceph config get <daemon> <option>  # e.g. rbd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_persistent_cache_mode

| | |
|---|---|
| نوع | Str · enum: ["disabled", "rwl", "ssd"] · default `disabled` · **Advanced** |
| جدول | [rbd.md#SP_rbd_persistent_cache_mode](../../../config/rbd/rbd.md#SP_rbd_persistent_cache_mode) |

**کارکرد:** enable persistent write back cache for this volume

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_persistent_cache_mode disabled
ceph config get client rbd_persistent_cache_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `disabled`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_persistent_cache_mode
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_persistent_cache_path

| | |
|---|---|
| نوع | Str · default `/tmp` · **Advanced** |
| جدول | [rbd.md#SP_rbd_persistent_cache_path](../../../config/rbd/rbd.md#SP_rbd_persistent_cache_path) |

**کارکرد:** location of the persistent write back cache in a DAX-enabled filesystem on persistent memory

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_persistent_cache_path "/tmp"
ceph config get client rbd_persistent_cache_path
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** ظرفیت

1. خط پایه روی `/tmp`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_persistent_cache_path
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_persistent_cache_size

| | |
|---|---|
| نوع | Uint · default `1_G` · **Advanced** |
| جدول | [rbd.md#SP_rbd_persistent_cache_size](../../../config/rbd/rbd.md#SP_rbd_persistent_cache_size) |

**کارکرد:** size of the persistent write back cache for this volume

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_persistent_cache_size 1_G
ceph config get client rbd_persistent_cache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_G`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1_G`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_persistent_cache_size
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---


[← نمای کلی](../OVERVIEW.md)
