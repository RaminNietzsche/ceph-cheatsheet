# Cluster logging

deep dive پیکربندی MON — 20 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mon_cluster_log_file](#mon_cluster_log_file) | `default=/var/log/ceph/$cluster.$channel.log cluster=/var/log/ceph/$cluster.log` | Advanced | Capacity |
| [mon_cluster_log_level](#mon_cluster_log_level) | `debug` | Advanced | Performance |
| [mon_cluster_log_to_file](#mon_cluster_log_to_file) | `True` | Advanced | Capacity |
| [mon_cluster_log_to_graylog](#mon_cluster_log_to_graylog) | `false` | Advanced | Performance |
| [mon_cluster_log_to_graylog_host](#mon_cluster_log_to_graylog_host) | `127.0.0.1` | Advanced | Performance |
| [mon_cluster_log_to_graylog_port](#mon_cluster_log_to_graylog_port) | `12201` | Advanced | Performance |
| [mon_cluster_log_to_journald](#mon_cluster_log_to_journald) | `false` | Advanced | Performance |
| [mon_cluster_log_to_stderr](#mon_cluster_log_to_stderr) | `False` | Advanced | Performance |
| [mon_cluster_log_to_syslog](#mon_cluster_log_to_syslog) | `default=false` | Advanced | Performance |
| [mon_cluster_log_to_syslog_facility](#mon_cluster_log_to_syslog_facility) | `daemon` | Advanced | Performance |
| [mon_health_detail_to_clog](#mon_health_detail_to_clog) | `True` | Dev | Dev |
| [mon_health_log_update_period](#mon_health_log_update_period) | `5` | Dev | Dev |
| [mon_health_to_clog](#mon_health_to_clog) | `True` | Advanced | Performance |
| [mon_health_to_clog_interval](#mon_health_to_clog_interval) | `10_min` | Advanced | Performance |
| [mon_health_to_clog_tick_interval](#mon_health_to_clog_tick_interval) | `1_min` | Dev | Dev |
| [mon_log_full_interval](#mon_log_full_interval) | `50` | Advanced | Performance |
| [mon_log_max](#mon_log_max) | `10000` | Advanced | Performance |
| [mon_log_max_summary](#mon_log_max_summary) | `50` | Advanced | Performance |
| [mon_max_log_entries_per_event](#mon_max_log_entries_per_event) | `4096` | Advanced | Performance |
| [mon_op_log_threshold](#mon_op_log_threshold) | `5` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_cluster_log_file

| | |
|---|---|
| نوع | Str · default `default=/var/log/ceph/$cluster.$channel.log cluster=/var/log/ceph/$cluster.log` · **Advanced** |
| جدول | [mon.md#SP_mon_cluster_log_file](../../../config/mon/mon.md#SP_mon_cluster_log_file) |

**کارکرد:** File(s) to write cluster log to

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_cluster_log_file "default=/var/log/ceph/$cluster.$channel.log cluster=/var/log/ceph/$cluster.log"
ceph config get mon mon_cluster_log_file
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. خط پایه روی `default=/var/log/ceph/$cluster.$channel.log cluster=/var/log/ceph/$cluster.log`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_cluster_log_file
ceph -s
ceph mon stat
```

---

### mon_cluster_log_level

| | |
|---|---|
| نوع | Str · default `debug` · **Advanced** |
| جدول | [mon.md#SP_mon_cluster_log_level](../../../config/mon/mon.md#SP_mon_cluster_log_level) |

**کارکرد:** Lowest level to include in cluster log file and/or in external log server

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_cluster_log_level debug
ceph config get mon mon_cluster_log_level
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `debug`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_cluster_log_level
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_file

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_cluster_log_to_file](../../../config/mon/mon.md#SP_mon_cluster_log_to_file) |

**کارکرد:** Make monitor send cluster log messages to file

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_cluster_log_to_file false
ceph config get mon mon_cluster_log_to_file
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. خط پایه روی `True`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_cluster_log_to_file
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_graylog

| | |
|---|---|
| نوع | Str · default `false` · **Advanced** |
| جدول | [mon.md#SP_mon_cluster_log_to_graylog](../../../config/mon/mon.md#SP_mon_cluster_log_to_graylog) |

**کارکرد:** Make monitor send cluster log to graylog

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_cluster_log_to_graylog false
ceph config get mon mon_cluster_log_to_graylog
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `false`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_cluster_log_to_graylog
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_graylog_host

| | |
|---|---|
| نوع | Str · default `127.0.0.1` · **Advanced** |
| جدول | [mon.md#SP_mon_cluster_log_to_graylog_host](../../../config/mon/mon.md#SP_mon_cluster_log_to_graylog_host) |

**کارکرد:** Graylog host for cluster log messages

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_cluster_log_to_graylog_host "127.0.0.1"
ceph config get mon mon_cluster_log_to_graylog_host
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `127.0.0.1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_cluster_log_to_graylog_host
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_graylog_port

| | |
|---|---|
| نوع | Str · default `12201` · **Advanced** |
| جدول | [mon.md#SP_mon_cluster_log_to_graylog_port](../../../config/mon/mon.md#SP_mon_cluster_log_to_graylog_port) |

**کارکرد:** Graylog port for cluster log messages

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_cluster_log_to_graylog_port 12201
ceph config get mon mon_cluster_log_to_graylog_port
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `12201`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_cluster_log_to_graylog_port
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_journald

| | |
|---|---|
| نوع | Str · default `false` · **Advanced** |
| جدول | [mon.md#SP_mon_cluster_log_to_journald](../../../config/mon/mon.md#SP_mon_cluster_log_to_journald) |

**کارکرد:** Make monitor send cluster log to journald

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_cluster_log_to_journald false
ceph config get mon mon_cluster_log_to_journald
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `false`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_cluster_log_to_journald
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_stderr

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [mon.md#SP_mon_cluster_log_to_stderr](../../../config/mon/mon.md#SP_mon_cluster_log_to_stderr) |

**کارکرد:** Make monitor send cluster log messages to stderr (prefixed by channel)

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set mon mon_cluster_log_to_stderr true
ceph config get mon mon_cluster_log_to_stderr
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_cluster_log_to_stderr
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_syslog

| | |
|---|---|
| نوع | Str · default `default=false` · **Advanced** |
| جدول | [mon.md#SP_mon_cluster_log_to_syslog](../../../config/mon/mon.md#SP_mon_cluster_log_to_syslog) |

**کارکرد:** Make monitor send cluster log messages to syslog

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_cluster_log_to_syslog "default=false"
ceph config get mon mon_cluster_log_to_syslog
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `default=false`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_cluster_log_to_syslog
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_syslog_facility

| | |
|---|---|
| نوع | Str · default `daemon` · **Advanced** |
| جدول | [mon.md#SP_mon_cluster_log_to_syslog_facility](../../../config/mon/mon.md#SP_mon_cluster_log_to_syslog_facility) |

**کارکرد:** Syslog facility for cluster log messages

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_cluster_log_to_syslog_facility daemon
ceph config get mon mon_cluster_log_to_syslog_facility
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `daemon`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_cluster_log_to_syslog_facility
ceph -s
ceph mon stat
```

---

### mon_health_detail_to_clog

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [mon.md#SP_mon_health_detail_to_clog](../../../config/mon/mon.md#SP_mon_health_detail_to_clog) |

**کارکرد:** log health detail to cluster log

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_health_detail_to_clog false
ceph config get mon mon_health_detail_to_clog
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`True`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_health_log_update_period

| | |
|---|---|
| نوع | Int · default `5` · **Dev** |
| جدول | [mon.md#SP_mon_health_log_update_period](../../../config/mon/mon.md#SP_mon_health_log_update_period) |

**کارکرد:** minimum time in seconds between log messages about each health check

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_health_log_update_period 5
ceph config get mon mon_health_log_update_period
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`5`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_health_to_clog

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_health_to_clog](../../../config/mon/mon.md#SP_mon_health_to_clog) |

**کارکرد:** log monitor health to cluster log

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_health_to_clog false
ceph config get mon mon_health_to_clog
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_health_to_clog
ceph -s
ceph mon stat
```

---

### mon_health_to_clog_interval

| | |
|---|---|
| نوع | Int · default `10_min` · **Advanced** |
| جدول | [mon.md#SP_mon_health_to_clog_interval](../../../config/mon/mon.md#SP_mon_health_to_clog_interval) |

**کارکرد:** frequency to log monitor health to cluster log

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_health_to_clog_interval 10_min
ceph config get mon mon_health_to_clog_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_health_to_clog_interval
ceph -s
ceph mon stat
```

---

### mon_health_to_clog_tick_interval

| | |
|---|---|
| نوع | Float · default `1_min` · **Dev** |
| جدول | [mon.md#SP_mon_health_to_clog_tick_interval](../../../config/mon/mon.md#SP_mon_health_to_clog_tick_interval) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_health_to_clog_tick_interval 1_min
ceph config get mon mon_health_to_clog_tick_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`1_min`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_log_full_interval

| | |
|---|---|
| نوع | Uint · default `50` · **Advanced** |
| جدول | [mon.md#SP_mon_log_full_interval](../../../config/mon/mon.md#SP_mon_log_full_interval) |

**کارکرد:** how many epochs before we encode a full copy of recent log keys

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_log_full_interval 50
ceph config get mon mon_log_full_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `50`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_log_full_interval
ceph -s
ceph mon stat
```

---

### mon_log_max

| | |
|---|---|
| نوع | Uint · default `10000` · **Advanced** |
| جدول | [mon.md#SP_mon_log_max](../../../config/mon/mon.md#SP_mon_log_max) |

**کارکرد:** number of recent cluster log messages to retain

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_log_max 10000
ceph config get mon mon_log_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_log_max
ceph -s
ceph mon stat
```

---

### mon_log_max_summary

| | |
|---|---|
| نوع | Uint · default `50` · **Advanced** |
| جدول | [mon.md#SP_mon_log_max_summary](../../../config/mon/mon.md#SP_mon_log_max_summary) |

**کارکرد:** number of recent cluster log messages to dedup against

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_log_max_summary 50
ceph config get mon mon_log_max_summary
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `50`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_log_max_summary
ceph -s
ceph mon stat
```

---

### mon_max_log_entries_per_event

| | |
|---|---|
| نوع | Int · default `4096` · **Advanced** |
| جدول | [mon.md#SP_mon_max_log_entries_per_event](../../../config/mon/mon.md#SP_mon_max_log_entries_per_event) |

**کارکرد:** max cluster log entries per paxos event

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_max_log_entries_per_event 4096
ceph config get mon mon_max_log_entries_per_event
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `4096`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_max_log_entries_per_event
ceph -s
ceph mon stat
```

---

### mon_op_log_threshold

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [mon.md#SP_mon_op_log_threshold](../../../config/mon/mon.md#SP_mon_op_log_threshold) |

**کارکرد:** max number of slow ops to display

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_op_log_threshold 5
ceph config get mon mon_op_log_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_op_log_threshold
ceph -s
ceph mon stat
```

---


[← نمای کلی](../OVERVIEW.md)
