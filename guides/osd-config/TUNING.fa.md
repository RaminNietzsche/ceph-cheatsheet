# پیکربندی OSD — مرجع سریع تنظیم

هر **158** گزینه با مدل تنظیم و راهنمای یک‌خطی.

[← نمای کلی](../OVERVIEW.md)

| گزینه | پیش‌فرض | مدل | پاسخ سریع | موضوع |
|--------|---------|-------|--------------|-------|
| [`osd_agent_delay_time`](runtime/agent.md#osd_agent_delay_time) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cache agent](runtime/agent.md) |
| [`osd_agent_hist_halflife`](runtime/agent.md#osd_agent_hist_halflife) | `1000` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cache agent](runtime/agent.md) |
| [`osd_agent_max_low_ops`](runtime/agent.md#osd_agent_max_low_ops) | `2` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cache agent](runtime/agent.md) |
| [`osd_agent_max_ops`](runtime/agent.md#osd_agent_max_ops) | `4` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cache agent](runtime/agent.md) |
| [`osd_agent_min_evict_effort`](runtime/agent.md#osd_agent_min_evict_effort) | `0.1` | Performance | در محدوده مستند بمانید | [Cache agent](runtime/agent.md) |
| [`osd_agent_quantize_effort`](runtime/agent.md#osd_agent_quantize_effort) | `0.1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cache agent](runtime/agent.md) |
| [`osd_agent_slop`](runtime/agent.md#osd_agent_slop) | `0.02` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cache agent](runtime/agent.md) |
| [`osd_aggregated_slow_ops_logging`](runtime/general.md#osd_aggregated_slow_ops_logging) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General runtime](runtime/general.md) |
| [`osd_allow_recovery_below_min_size`](recovery/recovery.md#osd_allow_recovery_below_min_size) | `True` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [Recovery & backfill](recovery/recovery.md) |
| [`osd_backfill_retry_interval`](recovery/recovery.md#osd_backfill_retry_interval) | `30` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_backfill_scan_max`](recovery/recovery.md#osd_backfill_scan_max) | `512` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_backfill_scan_min`](recovery/recovery.md#osd_backfill_scan_min) | `64` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_blocked_scrub_grace_period`](scrub/scrub.md#osd_blocked_scrub_grace_period) | `120` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_check_max_object_name_len_on_startup`](limits-intervals/limits.md#osd_check_max_object_name_len_on_startup) | `True` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [Limits & caps](limits-intervals/limits.md) |
| [`osd_class_default_list`](runtime/classes.md#osd_class_default_list) | `cephfs hello journal lock log numops otp rbd refcount rgw rgw_gc timeindex user version cas cmpomap queue 2pc_queue fifo sem_set` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Object classes](runtime/classes.md) |
| [`osd_class_dir`](runtime/classes.md#osd_class_dir) | `0/rados-classes` | Capacity | مطابق چیدمان filesystem و برنامه ظرفیت | [Object classes](runtime/classes.md) |
| [`osd_class_load_list`](runtime/classes.md#osd_class_load_list) | `cephfs hello journal lock log numops otp rbd refcount rgw rgw_gc timeindex user version cas cmpomap queue 2pc_queue fifo sem_set` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Object classes](runtime/classes.md) |
| [`osd_class_update_on_start`](runtime/classes.md#osd_class_update_on_start) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Object classes](runtime/classes.md) |
| [`osd_client_message_cap`](limits-intervals/limits.md#osd_client_message_cap) | `256` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Limits & caps](limits-intervals/limits.md) |
| [`osd_client_message_size_cap`](limits-intervals/limits.md#osd_client_message_size_cap) | `500_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Limits & caps](limits-intervals/limits.md) |
| [`osd_compact_on_start`](runtime/general.md#osd_compact_on_start) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General runtime](runtime/general.md) |
| [`osd_copyfrom_max_chunk`](limits-intervals/limits.md#osd_copyfrom_max_chunk) | `8_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Limits & caps](limits-intervals/limits.md) |
| [`osd_crush_initial_weight`](runtime/crush.md#osd_crush_initial_weight) | `-1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CRUSH & weight](runtime/crush.md) |
| [`osd_crush_update_on_start`](runtime/crush.md#osd_crush_update_on_start) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [CRUSH & weight](runtime/crush.md) |
| [`osd_data`](runtime/paths.md#osd_data) | `/var/lib/ceph/osd/$cluster-$id` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Paths & data dirs](runtime/paths.md) |
| [`osd_debug_feed_pullee`](debug/debug.md#osd_debug_feed_pullee) | `-1` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [Debug & injection](debug/debug.md) |
| [`osd_debug_trim_objects`](debug/debug.md#osd_debug_trim_objects) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Debug & injection](debug/debug.md) |
| [`osd_deep_scrub_interval`](scrub/scrub.md#osd_deep_scrub_interval) | `7_day` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_deep_scrub_interval_cv`](scrub/scrub.md#osd_deep_scrub_interval_cv) | `0.2` | Performance | در محدوده مستند بمانید | [Scrub](scrub/scrub.md) |
| [`osd_deep_scrub_keys`](scrub/scrub.md#osd_deep_scrub_keys) | `1024` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_deep_scrub_large_omap_object_key_threshold`](scrub/scrub.md#osd_deep_scrub_large_omap_object_key_threshold) | `200000` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_deep_scrub_large_omap_object_value_sum_threshold`](scrub/scrub.md#osd_deep_scrub_large_omap_object_value_sum_threshold) | `1_G` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_deep_scrub_randomize_ratio`](scrub/scrub.md#osd_deep_scrub_randomize_ratio) | `0.15` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_deep_scrub_stride`](scrub/scrub.md#osd_deep_scrub_stride) | `4_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_deep_scrub_update_digest_min_age`](scrub/scrub.md#osd_deep_scrub_update_digest_min_age) | `2_hr` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_delete_sleep`](limits-intervals/intervals.md#osd_delete_sleep) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & throttling](limits-intervals/intervals.md) |
| [`osd_delete_sleep_hdd`](limits-intervals/intervals.md#osd_delete_sleep_hdd) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & throttling](limits-intervals/intervals.md) |
| [`osd_delete_sleep_hybrid`](limits-intervals/intervals.md#osd_delete_sleep_hybrid) | `1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & throttling](limits-intervals/intervals.md) |
| [`osd_delete_sleep_ssd`](limits-intervals/intervals.md#osd_delete_sleep_ssd) | `1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & throttling](limits-intervals/intervals.md) |
| [`osd_ec_partial_reads`](runtime/general.md#osd_ec_partial_reads) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General runtime](runtime/general.md) |
| [`osd_extblkdev_plugins`](runtime/general.md#osd_extblkdev_plugins) | `vdo fcm` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General runtime](runtime/general.md) |
| [`osd_find_best_info_ignore_history_les`](runtime/general.md#osd_find_best_info_ignore_history_les) | `False` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [General runtime](runtime/general.md) |
| [`osd_heartbeat_min_peers`](limits-intervals/limits.md#osd_heartbeat_min_peers) | `10` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Limits & caps](limits-intervals/limits.md) |
| [`osd_inject_bad_map_crc_probability`](debug/debug.md#osd_inject_bad_map_crc_probability) | `0` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [Debug & injection](debug/debug.md) |
| [`osd_inject_failure_on_pg_removal`](debug/debug.md#osd_inject_failure_on_pg_removal) | `False` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [Debug & injection](debug/debug.md) |
| [`osd_journal`](runtime/general.md#osd_journal) | `/var/lib/ceph/osd/$cluster-$id/journal` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General runtime](runtime/general.md) |
| [`osd_journal_flush_on_shutdown`](runtime/general.md#osd_journal_flush_on_shutdown) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General runtime](runtime/general.md) |
| [`osd_journal_size`](runtime/general.md#osd_journal_size) | `5_K` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General runtime](runtime/general.md) |
| [`osd_map_cache_size`](runtime/general.md#osd_map_cache_size) | `50` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General runtime](runtime/general.md) |
| [`osd_map_share_max_epochs`](limits-intervals/limits.md#osd_map_share_max_epochs) | `40` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Limits & caps](limits-intervals/limits.md) |
| [`osd_max_backfills`](recovery/recovery.md#osd_max_backfills) | `1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_max_markdown_count`](limits-intervals/limits.md#osd_max_markdown_count) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Limits & caps](limits-intervals/limits.md) |
| [`osd_max_markdown_period`](limits-intervals/intervals.md#osd_max_markdown_period) | `10_min` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & throttling](limits-intervals/intervals.md) |
| [`osd_max_pgls`](limits-intervals/limits.md#osd_max_pgls) | `1_K` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Limits & caps](limits-intervals/limits.md) |
| [`osd_max_push_cost`](limits-intervals/limits.md#osd_max_push_cost) | `8_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Limits & caps](limits-intervals/limits.md) |
| [`osd_max_push_objects`](limits-intervals/limits.md#osd_max_push_objects) | `10` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Limits & caps](limits-intervals/limits.md) |
| [`osd_max_scrubs`](scrub/scrub.md#osd_max_scrubs) | `3` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_max_write_size`](limits-intervals/limits.md#osd_max_write_size) | `90` | Performance | در محدوده مستند بمانید | [Limits & caps](limits-intervals/limits.md) |
| [`osd_mclock_force_run_benchmark_on_init`](mclock/mclock.md#osd_mclock_force_run_benchmark_on_init) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [mClock scheduler](mclock/mclock.md) |
| [`osd_mclock_iops_capacity_low_threshold_hdd`](mclock/mclock.md#osd_mclock_iops_capacity_low_threshold_hdd) | `50` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [mClock scheduler](mclock/mclock.md) |
| [`osd_mclock_iops_capacity_low_threshold_ssd`](mclock/mclock.md#osd_mclock_iops_capacity_low_threshold_ssd) | `1000` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [mClock scheduler](mclock/mclock.md) |
| [`osd_mclock_iops_capacity_threshold_hdd`](mclock/mclock.md#osd_mclock_iops_capacity_threshold_hdd) | `500` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [mClock scheduler](mclock/mclock.md) |
| [`osd_mclock_iops_capacity_threshold_ssd`](mclock/mclock.md#osd_mclock_iops_capacity_threshold_ssd) | `80000` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [mClock scheduler](mclock/mclock.md) |
| [`osd_mclock_max_capacity_iops_hdd`](mclock/mclock.md#osd_mclock_max_capacity_iops_hdd) | `315` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [mClock scheduler](mclock/mclock.md) |
| [`osd_mclock_max_capacity_iops_ssd`](mclock/mclock.md#osd_mclock_max_capacity_iops_ssd) | `21500` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [mClock scheduler](mclock/mclock.md) |
| [`osd_mclock_max_sequential_bandwidth_hdd`](mclock/mclock.md#osd_mclock_max_sequential_bandwidth_hdd) | `150_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [mClock scheduler](mclock/mclock.md) |
| [`osd_mclock_max_sequential_bandwidth_ssd`](mclock/mclock.md#osd_mclock_max_sequential_bandwidth_ssd) | `1200_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [mClock scheduler](mclock/mclock.md) |
| [`osd_mclock_override_recovery_settings`](recovery/recovery.md#osd_mclock_override_recovery_settings) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Recovery & backfill](recovery/recovery.md) |
| [`osd_mclock_profile`](mclock/mclock.md#osd_mclock_profile) | `balanced` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [mClock scheduler](mclock/mclock.md) |
| [`osd_mclock_scheduler_anticipation_timeout`](mclock/mclock.md#osd_mclock_scheduler_anticipation_timeout) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [mClock scheduler](mclock/mclock.md) |
| [`osd_mclock_scheduler_background_best_effort_lim`](mclock/mclock.md#osd_mclock_scheduler_background_best_effort_lim) | `0` | Performance | در محدوده مستند بمانید | [mClock scheduler](mclock/mclock.md) |
| [`osd_mclock_scheduler_background_best_effort_res`](mclock/mclock.md#osd_mclock_scheduler_background_best_effort_res) | `0` | Performance | در محدوده مستند بمانید | [mClock scheduler](mclock/mclock.md) |
| [`osd_mclock_scheduler_background_best_effort_wgt`](mclock/mclock.md#osd_mclock_scheduler_background_best_effort_wgt) | `1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [mClock scheduler](mclock/mclock.md) |
| [`osd_mclock_scheduler_background_recovery_lim`](recovery/recovery.md#osd_mclock_scheduler_background_recovery_lim) | `0` | Performance | در محدوده مستند بمانید | [Recovery & backfill](recovery/recovery.md) |
| [`osd_mclock_scheduler_background_recovery_res`](recovery/recovery.md#osd_mclock_scheduler_background_recovery_res) | `0` | Performance | در محدوده مستند بمانید | [Recovery & backfill](recovery/recovery.md) |
| [`osd_mclock_scheduler_background_recovery_wgt`](recovery/recovery.md#osd_mclock_scheduler_background_recovery_wgt) | `1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_mclock_scheduler_client_lim`](mclock/mclock.md#osd_mclock_scheduler_client_lim) | `0` | Performance | در محدوده مستند بمانید | [mClock scheduler](mclock/mclock.md) |
| [`osd_mclock_scheduler_client_res`](mclock/mclock.md#osd_mclock_scheduler_client_res) | `0` | Performance | در محدوده مستند بمانید | [mClock scheduler](mclock/mclock.md) |
| [`osd_mclock_scheduler_client_wgt`](mclock/mclock.md#osd_mclock_scheduler_client_wgt) | `1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [mClock scheduler](mclock/mclock.md) |
| [`osd_mclock_skip_benchmark`](mclock/mclock.md#osd_mclock_skip_benchmark) | `False` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [mClock scheduler](mclock/mclock.md) |
| [`osd_min_recovery_priority`](recovery/recovery.md#osd_min_recovery_priority) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_num_cache_shards`](runtime/general.md#osd_num_cache_shards) | `32` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General runtime](runtime/general.md) |
| [`osd_numa_auto_affinity`](runtime/general.md#osd_numa_auto_affinity) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General runtime](runtime/general.md) |
| [`osd_numa_node`](runtime/general.md#osd_numa_node) | `-1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General runtime](runtime/general.md) |
| [`osd_numa_prefer_iface`](runtime/general.md#osd_numa_prefer_iface) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General runtime](runtime/general.md) |
| [`osd_op_num_shards`](runtime/general.md#osd_op_num_shards) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General runtime](runtime/general.md) |
| [`osd_op_num_shards_hdd`](runtime/general.md#osd_op_num_shards_hdd) | `1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General runtime](runtime/general.md) |
| [`osd_op_num_shards_ssd`](runtime/general.md#osd_op_num_shards_ssd) | `8` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General runtime](runtime/general.md) |
| [`osd_op_num_threads_per_shard`](runtime/general.md#osd_op_num_threads_per_shard) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General runtime](runtime/general.md) |
| [`osd_op_num_threads_per_shard_hdd`](runtime/general.md#osd_op_num_threads_per_shard_hdd) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General runtime](runtime/general.md) |
| [`osd_op_num_threads_per_shard_ssd`](runtime/general.md#osd_op_num_threads_per_shard_ssd) | `2` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General runtime](runtime/general.md) |
| [`osd_op_pq_max_tokens_per_priority`](limits-intervals/limits.md#osd_op_pq_max_tokens_per_priority) | `4_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Limits & caps](limits-intervals/limits.md) |
| [`osd_op_pq_min_cost`](limits-intervals/limits.md#osd_op_pq_min_cost) | `64_K` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Limits & caps](limits-intervals/limits.md) |
| [`osd_op_queue`](runtime/general.md#osd_op_queue) | `mclock_scheduler` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General runtime](runtime/general.md) |
| [`osd_op_queue_cut_off`](runtime/general.md#osd_op_queue_cut_off) | `high` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General runtime](runtime/general.md) |
| [`osd_op_thread_suicide_timeout`](limits-intervals/intervals.md#osd_op_thread_suicide_timeout) | `150` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & throttling](limits-intervals/intervals.md) |
| [`osd_op_thread_timeout`](limits-intervals/intervals.md#osd_op_thread_timeout) | `15` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & throttling](limits-intervals/intervals.md) |
| [`osd_open_classes_on_start`](runtime/classes.md#osd_open_classes_on_start) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Object classes](runtime/classes.md) |
| [`osd_os_flags`](runtime/general.md#osd_os_flags) | `0` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [General runtime](runtime/general.md) |
| [`osd_pg_epoch_max_lag_factor`](limits-intervals/limits.md#osd_pg_epoch_max_lag_factor) | `2` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Limits & caps](limits-intervals/limits.md) |
| [`osd_push_per_object_cost`](runtime/general.md#osd_push_per_object_cost) | `1000` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General runtime](runtime/general.md) |
| [`osd_read_ec_check_for_errors`](runtime/general.md#osd_read_ec_check_for_errors) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General runtime](runtime/general.md) |
| [`osd_recover_clone_overlap`](recovery/recovery.md#osd_recover_clone_overlap) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Recovery & backfill](recovery/recovery.md) |
| [`osd_recover_clone_overlap_limit`](recovery/recovery.md#osd_recover_clone_overlap_limit) | `10` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_recovery_delay_start`](recovery/recovery.md#osd_recovery_delay_start) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_recovery_max_active`](recovery/recovery.md#osd_recovery_max_active) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_recovery_max_active_hdd`](recovery/recovery.md#osd_recovery_max_active_hdd) | `3` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_recovery_max_active_ssd`](recovery/recovery.md#osd_recovery_max_active_ssd) | `10` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_recovery_max_chunk`](recovery/recovery.md#osd_recovery_max_chunk) | `8_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_recovery_max_omap_entries_per_chunk`](recovery/recovery.md#osd_recovery_max_omap_entries_per_chunk) | `8096` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_recovery_max_single_start`](recovery/recovery.md#osd_recovery_max_single_start) | `1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_recovery_retry_interval`](recovery/recovery.md#osd_recovery_retry_interval) | `30` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_recovery_sleep`](recovery/recovery.md#osd_recovery_sleep) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_recovery_sleep_degraded`](recovery/recovery.md#osd_recovery_sleep_degraded) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_recovery_sleep_degraded_hdd`](recovery/recovery.md#osd_recovery_sleep_degraded_hdd) | `0.1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_recovery_sleep_degraded_hybrid`](recovery/recovery.md#osd_recovery_sleep_degraded_hybrid) | `0.025` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_recovery_sleep_degraded_ssd`](recovery/recovery.md#osd_recovery_sleep_degraded_ssd) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_recovery_sleep_hdd`](recovery/recovery.md#osd_recovery_sleep_hdd) | `0.1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_recovery_sleep_hybrid`](recovery/recovery.md#osd_recovery_sleep_hybrid) | `0.025` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_recovery_sleep_ssd`](recovery/recovery.md#osd_recovery_sleep_ssd) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Recovery & backfill](recovery/recovery.md) |
| [`osd_rocksdb_iterator_bounds_enabled`](runtime/general.md#osd_rocksdb_iterator_bounds_enabled) | `True` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [General runtime](runtime/general.md) |
| [`osd_scrub_auto_repair`](scrub/scrub.md#osd_scrub_auto_repair) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Scrub](scrub/scrub.md) |
| [`osd_scrub_auto_repair_num_errors`](scrub/scrub.md#osd_scrub_auto_repair_num_errors) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_scrub_backoff_ratio`](scrub/scrub.md#osd_scrub_backoff_ratio) | `0.66` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [Scrub](scrub/scrub.md) |
| [`osd_scrub_begin_hour`](scrub/scrub.md#osd_scrub_begin_hour) | `0` | Performance | در محدوده مستند بمانید | [Scrub](scrub/scrub.md) |
| [`osd_scrub_begin_week_day`](scrub/scrub.md#osd_scrub_begin_week_day) | `0` | Performance | در محدوده مستند بمانید | [Scrub](scrub/scrub.md) |
| [`osd_scrub_chunk_max`](scrub/scrub.md#osd_scrub_chunk_max) | `15` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_scrub_chunk_min`](scrub/scrub.md#osd_scrub_chunk_min) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_scrub_disable_reservation_queuing`](scrub/scrub.md#osd_scrub_disable_reservation_queuing) | `False` | Policy | مطابق سیاست امنیت و سازگاری | [Scrub](scrub/scrub.md) |
| [`osd_scrub_during_recovery`](scrub/scrub.md#osd_scrub_during_recovery) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Scrub](scrub/scrub.md) |
| [`osd_scrub_end_hour`](scrub/scrub.md#osd_scrub_end_hour) | `0` | Performance | در محدوده مستند بمانید | [Scrub](scrub/scrub.md) |
| [`osd_scrub_end_week_day`](scrub/scrub.md#osd_scrub_end_week_day) | `0` | Performance | در محدوده مستند بمانید | [Scrub](scrub/scrub.md) |
| [`osd_scrub_extended_sleep`](scrub/scrub.md#osd_scrub_extended_sleep) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_scrub_interval_randomize_ratio`](scrub/scrub.md#osd_scrub_interval_randomize_ratio) | `0.5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_scrub_invalid_stats`](scrub/scrub.md#osd_scrub_invalid_stats) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Scrub](scrub/scrub.md) |
| [`osd_scrub_load_threshold`](scrub/scrub.md#osd_scrub_load_threshold) | `10.0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_scrub_max_interval`](scrub/scrub.md#osd_scrub_max_interval) | `7_day` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_scrub_max_preemptions`](scrub/scrub.md#osd_scrub_max_preemptions) | `5` | Performance | در محدوده مستند بمانید | [Scrub](scrub/scrub.md) |
| [`osd_scrub_min_interval`](scrub/scrub.md#osd_scrub_min_interval) | `1_day` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_scrub_queued_snaptrims_limit`](scrub/scrub.md#osd_scrub_queued_snaptrims_limit) | `500` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_scrub_retry_after_noscrub`](scrub/scrub.md#osd_scrub_retry_after_noscrub) | `60` | Performance | در محدوده مستند بمانید | [Scrub](scrub/scrub.md) |
| [`osd_scrub_retry_delay`](scrub/scrub.md#osd_scrub_retry_delay) | `30` | Performance | در محدوده مستند بمانید | [Scrub](scrub/scrub.md) |
| [`osd_scrub_retry_new_interval`](scrub/scrub.md#osd_scrub_retry_new_interval) | `10` | Performance | در محدوده مستند بمانید | [Scrub](scrub/scrub.md) |
| [`osd_scrub_retry_pg_state`](scrub/scrub.md#osd_scrub_retry_pg_state) | `60` | Performance | در محدوده مستند بمانید | [Scrub](scrub/scrub.md) |
| [`osd_scrub_retry_trimming`](scrub/scrub.md#osd_scrub_retry_trimming) | `10` | Performance | در محدوده مستند بمانید | [Scrub](scrub/scrub.md) |
| [`osd_scrub_sleep`](scrub/scrub.md#osd_scrub_sleep) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_shallow_scrub_chunk_max`](scrub/scrub.md#osd_shallow_scrub_chunk_max) | `100` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_shallow_scrub_chunk_min`](scrub/scrub.md#osd_shallow_scrub_chunk_min) | `50` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_skip_data_digest`](runtime/paths.md#osd_skip_data_digest) | `False` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [Paths & data dirs](runtime/paths.md) |
| [`osd_smart_report_timeout`](limits-intervals/intervals.md#osd_smart_report_timeout) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & throttling](limits-intervals/intervals.md) |
| [`osd_snap_trim_sleep`](limits-intervals/intervals.md#osd_snap_trim_sleep) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & throttling](limits-intervals/intervals.md) |
| [`osd_snap_trim_sleep_hdd`](limits-intervals/intervals.md#osd_snap_trim_sleep_hdd) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & throttling](limits-intervals/intervals.md) |
| [`osd_snap_trim_sleep_hybrid`](limits-intervals/intervals.md#osd_snap_trim_sleep_hybrid) | `2` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & throttling](limits-intervals/intervals.md) |
| [`osd_snap_trim_sleep_ssd`](limits-intervals/intervals.md#osd_snap_trim_sleep_ssd) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & throttling](limits-intervals/intervals.md) |
| [`osd_stats_update_period_not_scrubbing`](scrub/scrub.md#osd_stats_update_period_not_scrubbing) | `120` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_stats_update_period_scrubbing`](scrub/scrub.md#osd_stats_update_period_scrubbing) | `15` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Scrub](scrub/scrub.md) |
| [`osd_uuid`](runtime/general.md#osd_uuid) | `(empty)` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General runtime](runtime/general.md) |
| [`set_keepcaps`](limits-intervals/limits.md#set_keepcaps) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Limits & caps](limits-intervals/limits.md) |

[← نمای کلی](../OVERVIEW.md)
