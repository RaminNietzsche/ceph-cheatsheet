# پیکربندی Crimson — مرجع سریع تنظیم

هر **42** گزینه با مدل تنظیم و راهنمای یک‌خطی.

[← نمای کلی](../OVERVIEW.md)

| گزینه | پیش‌فرض | مدل | پاسخ سریع | موضوع |
|--------|---------|-------|--------------|-------|
| [`crimson_allow_pg_split`](topics/crimson.md#crimson_allow_pg_split) | `True` | Policy | مطابق سیاست امنیت و سازگاری | [Crimson OSD](topics/crimson.md) |
| [`crimson_bluestore_cpu_set`](topics/crimson.md#crimson_bluestore_cpu_set) | `(empty)` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Crimson OSD](topics/crimson.md) |
| [`crimson_bluestore_num_threads`](topics/crimson.md#crimson_bluestore_num_threads) | `6` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Crimson OSD](topics/crimson.md) |
| [`crimson_cpu_num`](topics/crimson.md#crimson_cpu_num) | `0` | Performance | در محدوده مستند بمانید | [Crimson OSD](topics/crimson.md) |
| [`crimson_cpu_set`](topics/crimson.md#crimson_cpu_set) | `(empty)` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Crimson OSD](topics/crimson.md) |
| [`crimson_memory`](topics/crimson.md#crimson_memory) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Crimson OSD](topics/crimson.md) |
| [`crimson_osd_obc_lru_size`](topics/crimson.md#crimson_osd_obc_lru_size) | `512` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Crimson OSD](topics/crimson.md) |
| [`crimson_osd_scheduler_concurrency`](topics/crimson.md#crimson_osd_scheduler_concurrency) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Crimson OSD](topics/crimson.md) |
| [`crimson_osd_stat_interval`](topics/crimson.md#crimson_osd_stat_interval) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Crimson OSD](topics/crimson.md) |
| [`crimson_poll_mode`](topics/crimson.md#crimson_poll_mode) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Crimson OSD](topics/crimson.md) |
| [`crimson_reactor_backend`](topics/crimson.md#crimson_reactor_backend) | `(empty)` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Crimson OSD](topics/crimson.md) |
| [`crimson_reactor_idle_poll_time_us`](topics/crimson.md#crimson_reactor_idle_poll_time_us) | `200` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Crimson OSD](topics/crimson.md) |
| [`crimson_reactor_io_latency_goal_ms`](topics/crimson.md#crimson_reactor_io_latency_goal_ms) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Crimson OSD](topics/crimson.md) |
| [`crimson_reactor_task_quota_ms`](topics/crimson.md#crimson_reactor_task_quota_ms) | `0.5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Crimson OSD](topics/crimson.md) |
| [`seastore_block_create`](topics/seastore.md#seastore_block_create) | `True` | Dev | پیش‌فرض upstream در production | [Seastore](topics/seastore.md) |
| [`seastore_cachepin_2q_in_ratio`](topics/seastore.md#seastore_cachepin_2q_in_ratio) | `0.5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Seastore](topics/seastore.md) |
| [`seastore_cachepin_2q_out_ratio`](topics/seastore.md#seastore_cachepin_2q_out_ratio) | `0.5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Seastore](topics/seastore.md) |
| [`seastore_cachepin_size_pershard`](topics/seastore.md#seastore_cachepin_size_pershard) | `2_G` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Seastore](topics/seastore.md) |
| [`seastore_cachepin_type`](topics/seastore.md#seastore_cachepin_type) | `LRU` | Dev | پیش‌فرض upstream در production | [Seastore](topics/seastore.md) |
| [`seastore_cbjournal_size`](topics/seastore.md#seastore_cbjournal_size) | `5_G` | Dev | پیش‌فرض upstream در production | [Seastore](topics/seastore.md) |
| [`seastore_cold_tier_generations`](topics/seastore.md#seastore_cold_tier_generations) | `3` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Seastore](topics/seastore.md) |
| [`seastore_data_delta_based_overwrite`](topics/seastore.md#seastore_data_delta_based_overwrite) | `0` | Dev | پیش‌فرض upstream در production | [Seastore](topics/seastore.md) |
| [`seastore_default_max_object_size`](topics/seastore.md#seastore_default_max_object_size) | `16777216` | Dev | پیش‌فرض upstream در production | [Seastore](topics/seastore.md) |
| [`seastore_device_size`](topics/seastore.md#seastore_device_size) | `50_G` | Dev | پیش‌فرض upstream در production | [Seastore](topics/seastore.md) |
| [`seastore_disable_end_to_end_data_protection`](topics/seastore.md#seastore_disable_end_to_end_data_protection) | `True` | Dev | پیش‌فرض upstream در production | [Seastore](topics/seastore.md) |
| [`seastore_full_integrity_check`](topics/seastore.md#seastore_full_integrity_check) | `False` | Dev | پیش‌فرض upstream در production | [Seastore](topics/seastore.md) |
| [`seastore_hot_tier_generations`](topics/seastore.md#seastore_hot_tier_generations) | `5` | Performance | در محدوده مستند بمانید | [Seastore](topics/seastore.md) |
| [`seastore_journal_batch_capacity`](topics/seastore.md#seastore_journal_batch_capacity) | `16` | Dev | پیش‌فرض upstream در production | [Seastore](topics/seastore.md) |
| [`seastore_journal_batch_flush_size`](topics/seastore.md#seastore_journal_batch_flush_size) | `16_M` | Dev | پیش‌فرض upstream در production | [Seastore](topics/seastore.md) |
| [`seastore_journal_batch_preferred_fullness`](topics/seastore.md#seastore_journal_batch_preferred_fullness) | `0.95` | Dev | پیش‌فرض upstream در production | [Seastore](topics/seastore.md) |
| [`seastore_journal_iodepth_limit`](topics/seastore.md#seastore_journal_iodepth_limit) | `5` | Dev | پیش‌فرض upstream در production | [Seastore](topics/seastore.md) |
| [`seastore_main_device_type`](topics/seastore.md#seastore_main_device_type) | `SSD` | Dev | پیش‌فرض upstream در production | [Seastore](topics/seastore.md) |
| [`seastore_max_concurrent_transactions`](topics/seastore.md#seastore_max_concurrent_transactions) | `128` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Seastore](topics/seastore.md) |
| [`seastore_max_data_allocation_size`](topics/seastore.md#seastore_max_data_allocation_size) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Seastore](topics/seastore.md) |
| [`seastore_multiple_tiers_default_evict_ratio`](topics/seastore.md#seastore_multiple_tiers_default_evict_ratio) | `0.6` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Seastore](topics/seastore.md) |
| [`seastore_multiple_tiers_fast_evict_ratio`](topics/seastore.md#seastore_multiple_tiers_fast_evict_ratio) | `0.7` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Seastore](topics/seastore.md) |
| [`seastore_multiple_tiers_stop_evict_ratio`](topics/seastore.md#seastore_multiple_tiers_stop_evict_ratio) | `0.5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Seastore](topics/seastore.md) |
| [`seastore_require_partition_count_match_reactor_count`](topics/seastore.md#seastore_require_partition_count_match_reactor_count) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Seastore](topics/seastore.md) |
| [`seastore_segment_cleaner_gc_autotune`](topics/seastore.md#seastore_segment_cleaner_gc_autotune) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Seastore](topics/seastore.md) |
| [`seastore_segment_cleaner_gc_autotune_ratio`](topics/seastore.md#seastore_segment_cleaner_gc_autotune_ratio) | `2.0` | Performance | در محدوده مستند بمانید | [Seastore](topics/seastore.md) |
| [`seastore_segment_cleaner_gc_formula`](topics/seastore.md#seastore_segment_cleaner_gc_formula) | `cost_benefit` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Seastore](topics/seastore.md) |
| [`seastore_segment_size`](topics/seastore.md#seastore_segment_size) | `64_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Seastore](topics/seastore.md) |

[← نمای کلی](../OVERVIEW.md)
