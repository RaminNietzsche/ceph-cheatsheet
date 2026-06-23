# Qat

deep dive پیکربندی Global — 3 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [qat_compressor_busy_polling](#qat_compressor_busy_polling) | `False` | Advanced | Performance |
| [qat_compressor_enabled](#qat_compressor_enabled) | `False` | Advanced | Policy |
| [qat_compressor_session_max_number](#qat_compressor_session_max_number) | `256` | Advanced | Performance |

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

### qat_compressor_busy_polling

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [qat.md#SP_qat_compressor_busy_polling](../../../config/global/qat.md#SP_qat_compressor_busy_polling) |

**کارکرد:** Set QAT busy bolling to reduce latency at the cost of potentially increasing CPU usage

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set global qat_compressor_busy_polling true
ceph config get global qat_compressor_busy_polling
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

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

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set global qat_compressor_enabled true
ceph config get global qat_compressor_enabled
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

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

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `256`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global qat_compressor_session_max_number
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
