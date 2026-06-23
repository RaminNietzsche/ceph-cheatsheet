# پیکربندی Immutable cache — مرجع سریع تنظیم

هر **13** گزینه با مدل تنظیم و راهنمای یک‌خطی.

[← نمای کلی](../OVERVIEW.md)

| گزینه | پیش‌فرض | مدل | پاسخ سریع | موضوع |
|--------|---------|-------|--------------|-------|
| [`immutable_object_cache_client_dedicated_thread_num`](topics/immutable.md#immutable_object_cache_client_dedicated_thread_num) | `2` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_max_inflight_ops`](topics/immutable.md#immutable_object_cache_max_inflight_ops) | `128` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_max_size`](topics/immutable.md#immutable_object_cache_max_size) | `1_G` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_path`](topics/immutable.md#immutable_object_cache_path) | `/tmp/ceph_immutable_object_cache` | ظرفیت | مطابق چیدمان filesystem و برنامه ظرفیت | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_bps_burst`](topics/immutable.md#immutable_object_cache_qos_bps_burst) | `0` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_bps_burst_seconds`](topics/immutable.md#immutable_object_cache_qos_bps_burst_seconds) | `1` | عملکرد | در محدوده مستند بمانید | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_bps_limit`](topics/immutable.md#immutable_object_cache_qos_bps_limit) | `0` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_iops_burst`](topics/immutable.md#immutable_object_cache_qos_iops_burst) | `0` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_iops_burst_seconds`](topics/immutable.md#immutable_object_cache_qos_iops_burst_seconds) | `1` | عملکرد | در محدوده مستند بمانید | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_iops_limit`](topics/immutable.md#immutable_object_cache_qos_iops_limit) | `0` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_schedule_tick_min`](topics/immutable.md#immutable_object_cache_qos_schedule_tick_min) | `50` | عملکرد | در محدوده مستند بمانید | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_sock`](topics/immutable.md#immutable_object_cache_sock) | `/var/run/ceph/immutable_object_cache_sock` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_watermark`](topics/immutable.md#immutable_object_cache_watermark) | `0.9` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Immutable object cache](topics/immutable.md) |

[← نمای کلی](../OVERVIEW.md)
