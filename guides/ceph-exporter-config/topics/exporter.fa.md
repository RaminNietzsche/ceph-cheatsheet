# ceph-exporter

راهنمای عمیق پیکربندی Ceph exporter — 8 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/ceph-exporter/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [exporter_addr](#exporter_addr) | `0.0.0.0` | Advanced | Connectivity |
| [exporter_cert_file](#exporter_cert_file) | `(empty)` | Advanced | Capacity |
| [exporter_http_port](#exporter_http_port) | `9926` | Advanced | Performance |
| [exporter_key_file](#exporter_key_file) | `(empty)` | Advanced | Capacity |
| [exporter_prio_limit](#exporter_prio_limit) | `5` | Advanced | Performance |
| [exporter_sock_dir](#exporter_sock_dir) | `/var/run/ceph/` | Advanced | Capacity |
| [exporter_sort_metrics](#exporter_sort_metrics) | `True` | Advanced | Performance |
| [exporter_stats_period](#exporter_stats_period) | `5` | Advanced | Performance |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **Policy** | امنیت، سازگاری، پیش‌فرض‌های عملیاتی |
| **Capacity** | چیدمان دیسک، مسیرها، اندازه‌گیری |
| **Performance** | خط پایه → تغییر تدریجی → پایش کلاستر |
| **Connectivity** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **Dev** | در محیط عملیاتی همان پیش‌فرض upstream |

**ابزارهای مشترک:**

```bash
ceph config get <daemon> <option>  # e.g. ceph-exporter
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### exporter_addr

| | |
|---|---|
| نوع | Str · default `0.0.0.0` · **Advanced** |
| جدول | [ceph-exporter.md#SP_exporter_addr](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_addr) |

**کارکرد:** Host ip address where exporter is deployed

**زمان استفاده:** هنگام یکپارچه‌سازی با سرویس خارجی تنظیم کنید؛ اگر استفاده نمی‌شود خالی بگذارید.

**مثال:**

```bash
ceph config set mgr exporter_addr "0.0.0.0"
ceph config get mgr exporter_addr
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Connectivity

1. نقاط پایانی (endpoint) کاندید را از محیط خود فهرست کنید.
2. دسترسی‌پذیری از هر نودی که دیمن روی آن اجرا می‌شود را بررسی کنید.
3. پایدارترین نقطهٔ پایانی با کمترین تأخیر (latency) را انتخاب کنید.
4. اگر یکپارچه‌سازی غیرفعال است خالی (`0.0.0.0`) بگذارید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr exporter_addr
ceph -s
ceph mgr stat
```

---

### exporter_cert_file

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [ceph-exporter.md#SP_exporter_cert_file](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_cert_file) |

**کارکرد:** Certificate file for TLS.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mgr exporter_cert_file "example"
ceph config get mgr exporter_cert_file
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. خط پایه روی `(empty)`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr exporter_cert_file
ceph -s
ceph mgr stat
```

---

### exporter_http_port

| | |
|---|---|
| نوع | Int · default `9926` · **Advanced** |
| جدول | [ceph-exporter.md#SP_exporter_http_port](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_http_port) |

**کارکرد:** Port to deploy exporter on. Default is 9926

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mgr exporter_http_port 9926
ceph config get mgr exporter_http_port
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `9926`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr exporter_http_port
ceph -s
ceph mgr stat
```

---

### exporter_key_file

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [ceph-exporter.md#SP_exporter_key_file](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_key_file) |

**کارکرد:** Key certificate file for TLS.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mgr exporter_key_file "example"
ceph config get mgr exporter_key_file
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. خط پایه روی `(empty)`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr exporter_key_file
ceph -s
ceph mgr stat
```

---

### exporter_prio_limit

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [ceph-exporter.md#SP_exporter_prio_limit](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_prio_limit) |

**کارکرد:** Only perf counters greater than or equal to exporter_prio_limit are fetched

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mgr exporter_prio_limit 5
ceph config get mgr exporter_prio_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr exporter_prio_limit
ceph -s
ceph mgr stat
```

---

### exporter_sock_dir

| | |
|---|---|
| نوع | Str · default `/var/run/ceph/` · **Advanced** |
| جدول | [ceph-exporter.md#SP_exporter_sock_dir](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_sock_dir) |

**کارکرد:** The path to ceph daemons socket files dir

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mgr exporter_sock_dir "/var/run/ceph/"
ceph config get mgr exporter_sock_dir
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. خط پایه روی `/var/run/ceph/`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr exporter_sock_dir
ceph -s
ceph mgr stat
```

---

### exporter_sort_metrics

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [ceph-exporter.md#SP_exporter_sort_metrics](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_sort_metrics) |

**کارکرد:** If true it will sort the metrics and group them.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mgr exporter_sort_metrics false
ceph config get mgr exporter_sort_metrics
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr exporter_sort_metrics
ceph -s
ceph mgr stat
```

---

### exporter_stats_period

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [ceph-exporter.md#SP_exporter_stats_period](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_stats_period) |

**کارکرد:** Time to wait before sending requests again to exporter server (seconds)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mgr exporter_stats_period 5
ceph config get mgr exporter_stats_period
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr exporter_stats_period
ceph -s
ceph mgr stat
```

---


[← نمای کلی](../OVERVIEW.md)
