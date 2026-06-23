# پیکربندی Ceph exporter — مرجع سریع تنظیم

هر **8** گزینه با مدل تنظیم و راهنمای یک‌خطی.

[← نمای کلی](../OVERVIEW.md)

| گزینه | پیش‌فرض | مدل | پاسخ سریع | موضوع |
|--------|---------|-------|--------------|-------|
| [`exporter_addr`](topics/exporter.md#exporter_addr) | `0.0.0.0` | Connectivity | نزدیک‌ترین endpoint پایدار | [ceph-exporter](topics/exporter.md) |
| [`exporter_cert_file`](topics/exporter.md#exporter_cert_file) | `(empty)` | Capacity | مطابق چیدمان filesystem و برنامه ظرفیت | [ceph-exporter](topics/exporter.md) |
| [`exporter_http_port`](topics/exporter.md#exporter_http_port) | `9926` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [ceph-exporter](topics/exporter.md) |
| [`exporter_key_file`](topics/exporter.md#exporter_key_file) | `(empty)` | Capacity | مطابق چیدمان filesystem و برنامه ظرفیت | [ceph-exporter](topics/exporter.md) |
| [`exporter_prio_limit`](topics/exporter.md#exporter_prio_limit) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [ceph-exporter](topics/exporter.md) |
| [`exporter_sock_dir`](topics/exporter.md#exporter_sock_dir) | `/var/run/ceph/` | Capacity | مطابق چیدمان filesystem و برنامه ظرفیت | [ceph-exporter](topics/exporter.md) |
| [`exporter_sort_metrics`](topics/exporter.md#exporter_sort_metrics) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [ceph-exporter](topics/exporter.md) |
| [`exporter_stats_period`](topics/exporter.md#exporter_stats_period) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [ceph-exporter](topics/exporter.md) |

[← نمای کلی](../OVERVIEW.md)
