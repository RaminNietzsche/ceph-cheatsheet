# Clog

راهنمای عمیق پیکربندی Global — 7 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [clog_to_graylog](#clog_to_graylog) | `false` | Advanced | عملکرد |
| [clog_to_graylog_host](#clog_to_graylog_host) | `127.0.0.1` | Advanced | عملکرد |
| [clog_to_graylog_port](#clog_to_graylog_port) | `12201` | Advanced | عملکرد |
| [clog_to_monitors](#clog_to_monitors) | `default=true` | Advanced | عملکرد |
| [clog_to_syslog](#clog_to_syslog) | `false` | Advanced | عملکرد |
| [clog_to_syslog_facility](#clog_to_syslog_facility) | `default=daemon audit=local0` | Advanced | عملکرد |
| [clog_to_syslog_level](#clog_to_syslog_level) | `info` | Advanced | عملکرد |

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

### clog_to_graylog

| | |
|---|---|
| نوع | Str · default `false` · **Advanced** |
| جدول | [clog.md#SP_clog_to_graylog](../../../config/global/clog.md#SP_clog_to_graylog) |

**کارکرد:** Make daemons send cluster log to graylog

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global clog_to_graylog false
ceph config get global clog_to_graylog
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `false`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global clog_to_graylog
ceph -s
```

---

### clog_to_graylog_host

| | |
|---|---|
| نوع | Str · default `127.0.0.1` · **Advanced** |
| جدول | [clog.md#SP_clog_to_graylog_host](../../../config/global/clog.md#SP_clog_to_graylog_host) |

**کارکرد:** Graylog host to cluster log messages

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global clog_to_graylog_host "127.0.0.1"
ceph config get global clog_to_graylog_host
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `127.0.0.1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global clog_to_graylog_host
ceph -s
```

---

### clog_to_graylog_port

| | |
|---|---|
| نوع | Str · default `12201` · **Advanced** |
| جدول | [clog.md#SP_clog_to_graylog_port](../../../config/global/clog.md#SP_clog_to_graylog_port) |

**کارکرد:** Graylog port number for cluster log messages

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global clog_to_graylog_port 12201
ceph config get global clog_to_graylog_port
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `12201`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global clog_to_graylog_port
ceph -s
```

---

### clog_to_monitors

| | |
|---|---|
| نوع | Str · default `default=true` · **Advanced** |
| جدول | [clog.md#SP_clog_to_monitors](../../../config/global/clog.md#SP_clog_to_monitors) |

**کارکرد:** Make daemons send cluster log messages to monitors

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global clog_to_monitors "default=true"
ceph config get global clog_to_monitors
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `default=true`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global clog_to_monitors
ceph -s
```

---

### clog_to_syslog

| | |
|---|---|
| نوع | Str · default `false` · **Advanced** |
| جدول | [clog.md#SP_clog_to_syslog](../../../config/global/clog.md#SP_clog_to_syslog) |

**کارکرد:** Make daemons send cluster log messages to syslog

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global clog_to_syslog false
ceph config get global clog_to_syslog
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `false`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global clog_to_syslog
ceph -s
```

---

### clog_to_syslog_facility

| | |
|---|---|
| نوع | Str · default `default=daemon audit=local0` · **Advanced** |
| جدول | [clog.md#SP_clog_to_syslog_facility](../../../config/global/clog.md#SP_clog_to_syslog_facility) |

**کارکرد:** Syslog facility for cluster log messages

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global clog_to_syslog_facility "default=daemon audit=local0"
ceph config get global clog_to_syslog_facility
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `default=daemon audit=local0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global clog_to_syslog_facility
ceph -s
```

---

### clog_to_syslog_level

| | |
|---|---|
| نوع | Str · default `info` · **Advanced** |
| جدول | [clog.md#SP_clog_to_syslog_level](../../../config/global/clog.md#SP_clog_to_syslog_level) |

**کارکرد:** Syslog level for cluster log messages

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global clog_to_syslog_level info
ceph config get global clog_to_syslog_level
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `info`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global clog_to_syslog_level
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
