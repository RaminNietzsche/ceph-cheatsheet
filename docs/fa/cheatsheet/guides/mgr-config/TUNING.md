# پیکربندی MGR — مرجع سریع تنظیم

هر **52** گزینه با مدل تنظیم و راهنمای یک‌خطی.

[← نمای کلی](../OVERVIEW.md)

| گزینه | پیش‌فرض | مدل | پاسخ سریع | موضوع |
|--------|---------|-------|--------------|-------|
| [`cephadm_path`](modules/mgr-modules.md#cephadm_path) | `/usr/sbin/cephadm` | ظرفیت | مطابق چیدمان filesystem و برنامه ظرفیت | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_client_bytes`](modules/mgr-modules.md#mgr_client_bytes) | `128_M` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_client_messages`](modules/mgr-modules.md#mgr_client_messages) | `512` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_data`](modules/mgr-modules.md#mgr_data) | `/var/lib/ceph/mgr/$cluster-$id` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_debug_aggressive_pg_num_changes`](modules/mgr-modules.md#mgr_debug_aggressive_pg_num_changes) | `False` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_disabled_modules`](modules/mgr-modules.md#mgr_disabled_modules) | `0` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_initial_modules`](modules/mgr-modules.md#mgr_initial_modules) | `iostat nfs nvmeof` | سیاست | مطابق سیاست امنیت و سازگاری | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_max_pg_creating`](modules/mgr-modules.md#mgr_max_pg_creating) | `1024` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_max_pg_num_change`](modules/mgr-modules.md#mgr_max_pg_num_change) | `128` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_mds_bytes`](modules/mgr-modules.md#mgr_mds_bytes) | `128_M` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_mds_messages`](modules/mgr-modules.md#mgr_mds_messages) | `128` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_module_load_delay`](modules/mgr-modules.md#mgr_module_load_delay) | `0` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_module_load_delay_name`](modules/mgr-modules.md#mgr_module_load_delay_name) | `(empty)` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_module_load_expiration`](modules/mgr-modules.md#mgr_module_load_expiration) | `20000` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_module_monitor_interval`](modules/mgr-modules.md#mgr_module_monitor_interval) | `5` | عملکرد | در محدوده مستند بمانید | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_module_path`](modules/mgr-modules.md#mgr_module_path) | `0/mgr` | ظرفیت | مطابق چیدمان filesystem و برنامه ظرفیت | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_mon_bytes`](modules/mgr-modules.md#mgr_mon_bytes) | `128_M` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_mon_messages`](modules/mgr-modules.md#mgr_mon_messages) | `128` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_osd_bytes`](modules/mgr-modules.md#mgr_osd_bytes) | `512_M` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_osd_messages`](modules/mgr-modules.md#mgr_osd_messages) | `8_K` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_osd_upgrade_check_convergence_factor`](modules/mgr-modules.md#mgr_osd_upgrade_check_convergence_factor) | `0.8` | عملکرد | در محدوده مستند بمانید | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_pool`](modules/mgr-modules.md#mgr_pool) | `True` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_service_beacon_grace`](modules/mgr-modules.md#mgr_service_beacon_grace) | `1_min` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_standby_modules`](modules/mgr-modules.md#mgr_standby_modules) | `True` | عملکرد | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_stats_period`](modules/mgr-modules.md#mgr_stats_period) | `5` | سیاست | مطابق سیاست امنیت و سازگاری | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_stats_period_autotune`](modules/mgr-modules.md#mgr_stats_period_autotune) | `True` | سیاست | مطابق سیاست امنیت و سازگاری | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_stats_period_autotune_queue_threshold`](modules/mgr-modules.md#mgr_stats_period_autotune_queue_threshold) | `100` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_stats_threshold`](modules/mgr-modules.md#mgr_stats_threshold) | `5` | عملکرد | در محدوده مستند بمانید | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_subinterpreter_modules`](modules/mgr-modules.md#mgr_subinterpreter_modules) | `0` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_test_metadata_error`](modules/mgr-modules.md#mgr_test_metadata_error) | `False` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_tick_period`](modules/mgr-modules.md#mgr_tick_period) | `2` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mon_cache_target_full_warn_ratio`](cluster/general.md#mon_cache_target_full_warn_ratio) | `0.66` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General manager](cluster/general.md) |
| [`mon_delta_reset_interval`](cluster/intervals.md#mon_delta_reset_interval) | `10` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals](cluster/intervals.md) |
| [`mon_osd_err_op_age_ratio`](cluster/general.md#mon_osd_err_op_age_ratio) | `128` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General manager](cluster/general.md) |
| [`mon_pg_check_down_all_threshold`](cluster/pg-pool.md#mon_pg_check_down_all_threshold) | `0.5` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_pg_stuck_threshold`](cluster/pg-pool.md#mon_pg_stuck_threshold) | `1_min` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_pg_warn_max_object_skew`](cluster/pg-pool.md#mon_pg_warn_max_object_skew) | `10` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_pg_warn_min_objects`](cluster/pg-pool.md#mon_pg_warn_min_objects) | `10000` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_pg_warn_min_per_osd`](cluster/pg-pool.md#mon_pg_warn_min_per_osd) | `0` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_pg_warn_min_pool_objects`](cluster/pg-pool.md#mon_pg_warn_min_pool_objects) | `1000` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_pool_quota_crit_threshold`](cluster/pg-pool.md#mon_pool_quota_crit_threshold) | `0` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_pool_quota_warn_threshold`](cluster/pg-pool.md#mon_pool_quota_warn_threshold) | `0` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_reweight_max_change`](cluster/general.md#mon_reweight_max_change) | `0.05` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General manager](cluster/general.md) |
| [`mon_reweight_max_osds`](cluster/general.md#mon_reweight_max_osds) | `4` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General manager](cluster/general.md) |
| [`mon_reweight_min_bytes_per_osd`](cluster/general.md#mon_reweight_min_bytes_per_osd) | `100_M` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General manager](cluster/general.md) |
| [`mon_reweight_min_pgs_per_osd`](cluster/general.md#mon_reweight_min_pgs_per_osd) | `10` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General manager](cluster/general.md) |
| [`mon_stat_smooth_intervals`](cluster/intervals.md#mon_stat_smooth_intervals) | `6` | عملکرد | در محدوده مستند بمانید | [Intervals](cluster/intervals.md) |
| [`mon_target_pg_per_osd`](cluster/pg-pool.md#mon_target_pg_per_osd) | `200` | عملکرد | در محدوده مستند بمانید | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_warn_on_misplaced`](cluster/general.md#mon_warn_on_misplaced) | `False` | عملکرد | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General manager](cluster/general.md) |
| [`mon_warn_on_pool_no_app`](cluster/pg-pool.md#mon_warn_on_pool_no_app) | `True` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_warn_on_pool_no_app_grace`](cluster/pg-pool.md#mon_warn_on_pool_no_app_grace) | `5_min` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_warn_on_too_few_osds`](cluster/general.md#mon_warn_on_too_few_osds) | `True` | عملکرد | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General manager](cluster/general.md) |

[← نمای کلی](../OVERVIEW.md)
