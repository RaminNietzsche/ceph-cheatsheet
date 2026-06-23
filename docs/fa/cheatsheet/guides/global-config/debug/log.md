# Log

راهنمای عمیق پیکربندی Global — 14 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [log_coarse_timestamps](#log_coarse_timestamps) | `True` | Advanced | عملکرد |
| [log_file](#log_file) | `/var/log/ceph/$cluster-$name.log` | Basic | ظرفیت |
| [log_flush_on_exit](#log_flush_on_exit) | `False` | Advanced | عملکرد |
| [log_graylog_host](#log_graylog_host) | `127.0.0.1` | Basic | سیاست |
| [log_graylog_port](#log_graylog_port) | `12201` | Basic | سیاست |
| [log_max_new](#log_max_new) | `1000` | Advanced | عملکرد |
| [log_max_recent](#log_max_recent) | `10000` | Advanced | عملکرد |
| [log_stderr_prefix](#log_stderr_prefix) | `(empty)` | Advanced | عملکرد |
| [log_stop_at_utilization](#log_stop_at_utilization) | `0.97` | Basic | سیاست |
| [log_to_file](#log_to_file) | `True` | Basic | ظرفیت |
| [log_to_graylog](#log_to_graylog) | `False` | Basic | سیاست |
| [log_to_journald](#log_to_journald) | `False` | Basic | سیاست |
| [log_to_stderr](#log_to_stderr) | `False` | Basic | سیاست |
| [log_to_syslog](#log_to_syslog) | `False` | Basic | سیاست |

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

### log_coarse_timestamps

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [log.md#SP_log_coarse_timestamps](../../../config/global/log.md#SP_log_coarse_timestamps) |

**کارکرد:** Timestamp log entries from coarse system clock to improve performance

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global log_coarse_timestamps false
ceph config get global log_coarse_timestamps
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global log_coarse_timestamps
ceph -s
```

---

### log_file

| | |
|---|---|
| نوع | Str · default `/var/log/ceph/$cluster-$name.log` · **Basic** |
| جدول | [log.md#SP_log_file](../../../config/global/log.md#SP_log_file) |

**کارکرد:** path to log file

**زمان استفاده:** رفتار اصلی Global — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set global log_file "/var/log/ceph/$cluster-$name.log"
ceph config get global log_file
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** ظرفیت

1. خط پایه روی `/var/log/ceph/$cluster-$name.log`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global log_file
ceph -s
```

---

### log_flush_on_exit

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [log.md#SP_log_flush_on_exit](../../../config/global/log.md#SP_log_flush_on_exit) |

**کارکرد:** Set a process exit handler to ensure the log is flushed on exit

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global log_flush_on_exit true
ceph config get global log_flush_on_exit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global log_flush_on_exit
ceph -s
```

---

### log_graylog_host

| | |
|---|---|
| نوع | Str · default `127.0.0.1` · **Basic** |
| جدول | [log.md#SP_log_graylog_host](../../../config/global/log.md#SP_log_graylog_host) |

**کارکرد:** Address or hostname of Graylog server to log to

**زمان استفاده:** رفتار اصلی Global — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set global log_graylog_host "127.0.0.1"
ceph config get global log_graylog_host
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `127.0.0.1` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global log_graylog_host
ceph -s
```

---

### log_graylog_port

| | |
|---|---|
| نوع | Int · default `12201` · **Basic** |
| جدول | [log.md#SP_log_graylog_port](../../../config/global/log.md#SP_log_graylog_port) |

**کارکرد:** TCP port number for the remote Graylog server

**زمان استفاده:** رفتار اصلی Global — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set global log_graylog_port 12201
ceph config get global log_graylog_port
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `12201` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global log_graylog_port
ceph -s
```

---

### log_max_new

| | |
|---|---|
| نوع | Int · default `1000` · **Advanced** |
| جدول | [log.md#SP_log_max_new](../../../config/global/log.md#SP_log_max_new) |

**کارکرد:** Max unwritten log entries to allow before flushing

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global log_max_new 1000
ceph config get global log_max_new
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global log_max_new
ceph -s
```

---

### log_max_recent

| | |
|---|---|
| نوع | Int · default `10000` · **Advanced** |
| جدول | [log.md#SP_log_max_recent](../../../config/global/log.md#SP_log_max_recent) |

**کارکرد:** Recent log entries to keep in memory to dump in the event of a crash

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global log_max_recent 10000
ceph config get global log_max_recent
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global log_max_recent
ceph -s
```

---

### log_stderr_prefix

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [log.md#SP_log_stderr_prefix](../../../config/global/log.md#SP_log_stderr_prefix) |

**کارکرد:** String to prefix log messages with when sent to stderr

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global log_stderr_prefix "example"
ceph config get global log_stderr_prefix
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global log_stderr_prefix
ceph -s
```

---

### log_stop_at_utilization

| | |
|---|---|
| نوع | Float · default `0.97` · **Basic** |
| جدول | [log.md#SP_log_stop_at_utilization](../../../config/global/log.md#SP_log_stop_at_utilization) |

**کارکرد:** Stop writing to the log file when device utilization reaches this ratio

**زمان استفاده:** رفتار اصلی Global — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set global log_stop_at_utilization 0.97
ceph config get global log_stop_at_utilization
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `0.97` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global log_stop_at_utilization
ceph -s
```

---

### log_to_file

| | |
|---|---|
| نوع | Bool · default `True` · **Basic** |
| جدول | [log.md#SP_log_to_file](../../../config/global/log.md#SP_log_to_file) |

**کارکرد:** send log lines to a file

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global log_to_file false
ceph config get global log_to_file
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** ظرفیت

1. خط پایه روی `True`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global log_to_file
ceph -s
```

---

### log_to_graylog

| | |
|---|---|
| نوع | Bool · default `False` · **Basic** |
| جدول | [log.md#SP_log_to_graylog](../../../config/global/log.md#SP_log_to_graylog) |

**کارکرد:** Send log lines to remote Graylog server

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global log_to_graylog true
ceph config get global log_to_graylog
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global log_to_graylog
ceph -s
```

---

### log_to_journald

| | |
|---|---|
| نوع | Bool · default `False` · **Basic** |
| جدول | [log.md#SP_log_to_journald](../../../config/global/log.md#SP_log_to_journald) |

**کارکرد:** Send log lines to journald

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global log_to_journald true
ceph config get global log_to_journald
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global log_to_journald
ceph -s
```

---

### log_to_stderr

| | |
|---|---|
| نوع | Bool · default `False` · **Basic** |
| جدول | [log.md#SP_log_to_stderr](../../../config/global/log.md#SP_log_to_stderr) |

**کارکرد:** send log lines to stderr

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global log_to_stderr true
ceph config get global log_to_stderr
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global log_to_stderr
ceph -s
```

---

### log_to_syslog

| | |
|---|---|
| نوع | Bool · default `False` · **Basic** |
| جدول | [log.md#SP_log_to_syslog](../../../config/global/log.md#SP_log_to_syslog) |

**کارکرد:** Send log lines to syslog facility

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global log_to_syslog true
ceph config get global log_to_syslog
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global log_to_syslog
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
