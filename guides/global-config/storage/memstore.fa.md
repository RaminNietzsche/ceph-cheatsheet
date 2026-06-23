# Memstore

deep dive پیکربندی Global — 4 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [memstore_debug_omit_block_device_write](#memstore_debug_omit_block_device_write) | `False` | Dev | Dev |
| [memstore_device_bytes](#memstore_device_bytes) | `1_G` | Advanced | Performance |
| [memstore_page_set](#memstore_page_set) | `False` | Advanced | Performance |
| [memstore_page_size](#memstore_page_size) | `64_K` | Advanced | Performance |

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

### memstore_debug_omit_block_device_write

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [memstore.md#SP_memstore_debug_omit_block_device_write](../../../config/global/memstore.md#SP_memstore_debug_omit_block_device_write) |

**کارکرد:** write metadata only

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set global memstore_debug_omit_block_device_write true
ceph config get global memstore_debug_omit_block_device_write
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### memstore_device_bytes

| | |
|---|---|
| نوع | Size · default `1_G` · **Advanced** |
| جدول | [memstore.md#SP_memstore_device_bytes](../../../config/global/memstore.md#SP_memstore_device_bytes) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global memstore_device_bytes 1_G
ceph config get global memstore_device_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1_G`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global memstore_device_bytes
ceph -s
```

---

### memstore_page_set

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [memstore.md#SP_memstore_page_set](../../../config/global/memstore.md#SP_memstore_page_set) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set global memstore_page_set true
ceph config get global memstore_page_set
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global memstore_page_set
ceph -s
```

---

### memstore_page_size

| | |
|---|---|
| نوع | Size · default `64_K` · **Advanced** |
| جدول | [memstore.md#SP_memstore_page_size](../../../config/global/memstore.md#SP_memstore_page_size) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global memstore_page_size 64_K
ceph config get global memstore_page_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `64_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global memstore_page_size
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
