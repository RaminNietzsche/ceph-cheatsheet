# Compressor

deep dive پیکربندی Global — 4 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [compressor_zlib_isal](#compressor_zlib_isal) | `False` | Advanced | Performance |
| [compressor_zlib_level](#compressor_zlib_level) | `5` | Advanced | Performance |
| [compressor_zlib_winsize](#compressor_zlib_winsize) | `-15` | Advanced | Performance |
| [compressor_zstd_level](#compressor_zstd_level) | `1` | Advanced | Performance |

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

### compressor_zlib_isal

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [compressor.md#SP_compressor_zlib_isal](../../../config/global/compressor.md#SP_compressor_zlib_isal) |

**کارکرد:** Use Intel ISA-L accelerated zlib implementation if available

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set global compressor_zlib_isal true
ceph config get global compressor_zlib_isal
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global compressor_zlib_isal
ceph -s
```

---

### compressor_zlib_level

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [compressor.md#SP_compressor_zlib_level](../../../config/global/compressor.md#SP_compressor_zlib_level) |

**کارکرد:** Zlib compression level to use

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global compressor_zlib_level 5
ceph config get global compressor_zlib_level
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global compressor_zlib_level
ceph -s
```

---

### compressor_zlib_winsize

| | |
|---|---|
| نوع | Int · default `-15` · **Advanced** |
| جدول | [compressor.md#SP_compressor_zlib_winsize](../../../config/global/compressor.md#SP_compressor_zlib_winsize) |

**کارکرد:** Zlib compression winsize to use

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global compressor_zlib_winsize -15
ceph config get global compressor_zlib_winsize
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `-15`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.

**محدوده:** حداقل `-15`، حداکثر `32`.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global compressor_zlib_winsize
ceph -s
```

---

### compressor_zstd_level

| | |
|---|---|
| نوع | Int · default `1` · **Advanced** |
| جدول | [compressor.md#SP_compressor_zstd_level](../../../config/global/compressor.md#SP_compressor_zstd_level) |

**کارکرد:** Zstd compression level to use

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global compressor_zstd_level 1
ceph config get global compressor_zstd_level
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global compressor_zstd_level
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
