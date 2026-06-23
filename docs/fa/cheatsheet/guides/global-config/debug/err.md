# Err

راهنمای عمیق پیکربندی Global — 4 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [err_to_graylog](#err_to_graylog) | `False` | Basic | سیاست |
| [err_to_journald](#err_to_journald) | `False` | Basic | سیاست |
| [err_to_stderr](#err_to_stderr) | `True` | Basic | سیاست |
| [err_to_syslog](#err_to_syslog) | `False` | Basic | سیاست |

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

### err_to_graylog

| | |
|---|---|
| نوع | Bool · default `False` · **Basic** |
| جدول | [err.md#SP_err_to_graylog](../../../config/global/err.md#SP_err_to_graylog) |

**کارکرد:** Send critical error log lines to remote Graylog server

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global err_to_graylog true
ceph config get global err_to_graylog
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global err_to_graylog
ceph -s
```

---

### err_to_journald

| | |
|---|---|
| نوع | Bool · default `False` · **Basic** |
| جدول | [err.md#SP_err_to_journald](../../../config/global/err.md#SP_err_to_journald) |

**کارکرد:** Send critical error log lines to journald

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global err_to_journald true
ceph config get global err_to_journald
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global err_to_journald
ceph -s
```

---

### err_to_stderr

| | |
|---|---|
| نوع | Bool · default `True` · **Basic** |
| جدول | [err.md#SP_err_to_stderr](../../../config/global/err.md#SP_err_to_stderr) |

**کارکرد:** send critical error log lines to stderr

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global err_to_stderr false
ceph config get global err_to_stderr
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global err_to_stderr
ceph -s
```

---

### err_to_syslog

| | |
|---|---|
| نوع | Bool · default `False` · **Basic** |
| جدول | [err.md#SP_err_to_syslog](../../../config/global/err.md#SP_err_to_syslog) |

**کارکرد:** Send critical error log lines to syslog facility

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global err_to_syslog true
ceph config get global err_to_syslog
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global err_to_syslog
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
