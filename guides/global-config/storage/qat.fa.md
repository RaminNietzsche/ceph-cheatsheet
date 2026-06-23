# Qat

راهنمای عمیق پیکربندی Global — 3 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [qat_compressor_busy_polling](#qat_compressor_busy_polling) | `False` | Advanced | عملکرد |
| [qat_compressor_enabled](#qat_compressor_enabled) | `False` | Advanced | سیاست |
| [qat_compressor_session_max_number](#qat_compressor_session_max_number) | `256` | Advanced | عملکرد |

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

### qat_compressor_busy_polling

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [qat.md#SP_qat_compressor_busy_polling](../../../config/global/qat.md#SP_qat_compressor_busy_polling) |

**کارکرد:** Set QAT busy bolling to reduce latency at the cost of potentially increasing CPU usage

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global qat_compressor_busy_polling true
ceph config get global qat_compressor_busy_polling
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global qat_compressor_busy_polling
ceph -s
```

---

### qat_compressor_enabled

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [qat.md#SP_qat_compressor_enabled](../../../config/global/qat.md#SP_qat_compressor_enabled) |

**کارکرد:** Enable Intel QAT acceleration support for compression if available

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global qat_compressor_enabled true
ceph config get global qat_compressor_enabled
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global qat_compressor_enabled
ceph -s
```

---

### qat_compressor_session_max_number

| | |
|---|---|
| نوع | Uint · default `256` · **Advanced** |
| جدول | [qat.md#SP_qat_compressor_session_max_number](../../../config/global/qat.md#SP_qat_compressor_session_max_number) |

**کارکرد:** Set the maximum number of session within Qatzip when using QAT compressor

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global qat_compressor_session_max_number 256
ceph config get global qat_compressor_session_max_number
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `256`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global qat_compressor_session_max_number
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
