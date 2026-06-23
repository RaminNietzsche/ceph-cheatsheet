# Persistent

deep dive پیکربندی RBD — 3 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rbd_persistent_cache_mode](#rbd_persistent_cache_mode) | `disabled` | Advanced | Performance |
| [rbd_persistent_cache_path](#rbd_persistent_cache_path) | `/tmp` | Advanced | Capacity |
| [rbd_persistent_cache_size](#rbd_persistent_cache_size) | `1_G` | Advanced | Performance |

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

### rbd_persistent_cache_mode

| | |
|---|---|
| نوع | Str · enum: ["disabled", "rwl", "ssd"] · default `disabled` · **Advanced** |
| جدول | [rbd.md#SP_rbd_persistent_cache_mode](../../../config/rbd/rbd.md#SP_rbd_persistent_cache_mode) |

**کارکرد:** enable persistent write back cache for this volume

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client rbd_persistent_cache_mode disabled
ceph config get client rbd_persistent_cache_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `disabled`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_persistent_cache_mode
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_persistent_cache_path

| | |
|---|---|
| نوع | Str · default `/tmp` · **Advanced** |
| جدول | [rbd.md#SP_rbd_persistent_cache_path](../../../config/rbd/rbd.md#SP_rbd_persistent_cache_path) |

**کارکرد:** location of the persistent write back cache in a DAX-enabled filesystem on persistent memory

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client rbd_persistent_cache_path "/tmp"
ceph config get client rbd_persistent_cache_path
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. خط پایه روی `/tmp`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_persistent_cache_path
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_persistent_cache_size

| | |
|---|---|
| نوع | Uint · default `1_G` · **Advanced** |
| جدول | [rbd.md#SP_rbd_persistent_cache_size](../../../config/rbd/rbd.md#SP_rbd_persistent_cache_size) |

**کارکرد:** size of the persistent write back cache for this volume

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client rbd_persistent_cache_size 1_G
ceph config get client rbd_persistent_cache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1_G`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.

**محدوده:** حداقل `1_G`، حداکثر `—`.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_persistent_cache_size
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---


[← نمای کلی](../OVERVIEW.md)
