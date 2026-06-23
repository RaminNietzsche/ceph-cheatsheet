# Compressor

راهنمای عمیق پیکربندی Global — 4 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [compressor_zlib_isal](#compressor_zlib_isal) | `False` | Advanced | عملکرد |
| [compressor_zlib_level](#compressor_zlib_level) | `5` | Advanced | عملکرد |
| [compressor_zlib_winsize](#compressor_zlib_winsize) | `-15` | Advanced | عملکرد |
| [compressor_zstd_level](#compressor_zstd_level) | `1` | Advanced | عملکرد |

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

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global compressor_zlib_isal true
ceph config get global compressor_zlib_isal
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

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

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global compressor_zlib_level 5
ceph config get global compressor_zlib_level
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

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

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global compressor_zlib_winsize -15
ceph config get global compressor_zlib_winsize
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `-15`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `-15`، حداکثر `32`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

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

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global compressor_zstd_level 1
ceph config get global compressor_zstd_level
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global compressor_zstd_level
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
