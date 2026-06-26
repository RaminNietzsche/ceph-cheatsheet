# Osd

راهنمای عمیق پیکربندی Global — 174 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [osd_asio_thread_count](#osd_asio_thread_count) | `2` | Advanced | عملکرد |
| [osd_async_recovery_min_cost](#osd_async_recovery_min_cost) | `100` | Advanced | عملکرد |
| [osd_auto_mark_unfound_lost](#osd_auto_mark_unfound_lost) | `False` | Advanced | عملکرد |
| [osd_backoff_on_degraded](#osd_backoff_on_degraded) | `False` | Advanced | عملکرد |
| [osd_backoff_on_peering](#osd_backoff_on_peering) | `False` | Advanced | عملکرد |
| [osd_backoff_on_unfound](#osd_backoff_on_unfound) | `True` | Advanced | عملکرد |
| [osd_beacon_report_interval](#osd_beacon_report_interval) | `5_min` | Advanced | عملکرد |
| [osd_bench_duration](#osd_bench_duration) | `30` | Advanced | عملکرد |
| [osd_bench_large_size_max_throughput](#osd_bench_large_size_max_throughput) | `100_M` | Advanced | عملکرد |
| [osd_bench_max_block_size](#osd_bench_max_block_size) | `64_M` | Advanced | عملکرد |
| [osd_bench_small_size_max_iops](#osd_bench_small_size_max_iops) | `100` | Advanced | عملکرد |
| [osd_blkin_trace_all](#osd_blkin_trace_all) | `False` | Advanced | عملکرد |
| [osd_calc_pg_upmaps_aggressively](#osd_calc_pg_upmaps_aggressively) | `True` | Advanced | عملکرد |
| [osd_calc_pg_upmaps_aggressively_fast](#osd_calc_pg_upmaps_aggressively_fast) | `True` | Advanced | عملکرد |
| [osd_calc_pg_upmaps_local_fallback_retries](#osd_calc_pg_upmaps_local_fallback_retries) | `100` | Advanced | عملکرد |
| [osd_check_for_log_corruption](#osd_check_for_log_corruption) | `False` | Advanced | عملکرد |
| [osd_client_op_priority](#osd_client_op_priority) | `63` | Advanced | عملکرد |
| [osd_command_max_records](#osd_command_max_records) | `256` | Advanced | عملکرد |
| [osd_crush_chooseleaf_type](#osd_crush_chooseleaf_type) | `1` | Dev | توسعه |
| [osd_debug_crash_on_ignored_backoff](#osd_debug_crash_on_ignored_backoff) | `False` | Dev | توسعه |
| [osd_debug_deep_scrub_sleep](#osd_debug_deep_scrub_sleep) | `0` | Dev | توسعه |
| [osd_debug_drop_ping_duration](#osd_debug_drop_ping_duration) | `0` | Dev | توسعه |
| [osd_debug_drop_ping_probability](#osd_debug_drop_ping_probability) | `0` | Dev | توسعه |
| [osd_debug_inject_copyfrom_error](#osd_debug_inject_copyfrom_error) | `False` | Dev | توسعه |
| [osd_debug_inject_dispatch_delay_duration](#osd_debug_inject_dispatch_delay_duration) | `0.1` | Dev | توسعه |
| [osd_debug_inject_dispatch_delay_probability](#osd_debug_inject_dispatch_delay_probability) | `0` | Dev | توسعه |
| [osd_debug_misdirected_ops](#osd_debug_misdirected_ops) | `False` | Dev | توسعه |
| [osd_debug_no_acting_change](#osd_debug_no_acting_change) | `False` | Dev | توسعه |
| [osd_debug_no_purge_strays](#osd_debug_no_purge_strays) | `False` | Dev | توسعه |
| [osd_debug_op_order](#osd_debug_op_order) | `False` | Dev | توسعه |
| [osd_debug_pg_log_writeout](#osd_debug_pg_log_writeout) | `False` | Dev | توسعه |
| [osd_debug_pretend_recovery_active](#osd_debug_pretend_recovery_active) | `False` | Dev | توسعه |
| [osd_debug_random_push_read_error](#osd_debug_random_push_read_error) | `0` | Dev | توسعه |
| [osd_debug_reject_backfill_probability](#osd_debug_reject_backfill_probability) | `0` | Dev | توسعه |
| [osd_debug_shutdown](#osd_debug_shutdown) | `False` | Dev | توسعه |
| [osd_debug_skip_full_check_in_backfill_reservation](#osd_debug_skip_full_check_in_backfill_reservation) | `False` | Dev | توسعه |
| [osd_debug_skip_full_check_in_recovery](#osd_debug_skip_full_check_in_recovery) | `False` | Dev | توسعه |
| [osd_debug_verify_cached_snaps](#osd_debug_verify_cached_snaps) | `False` | Dev | توسعه |
| [osd_debug_verify_missing_on_start](#osd_debug_verify_missing_on_start) | `False` | Dev | توسعه |
| [osd_debug_verify_snaps](#osd_debug_verify_snaps) | `False` | Dev | توسعه |
| [osd_debug_verify_stray_on_activate](#osd_debug_verify_stray_on_activate) | `False` | Dev | توسعه |
| [osd_default_data_pool_replay_window](#osd_default_data_pool_replay_window) | `45` | Advanced | عملکرد |
| [osd_default_notify_timeout](#osd_default_notify_timeout) | `30` | Advanced | عملکرد |
| [osd_discard_disconnected_ops](#osd_discard_disconnected_ops) | `True` | Advanced | عملکرد |
| [osd_enable_op_tracker](#osd_enable_op_tracker) | `True` | Advanced | سیاست |
| [osd_erasure_code_plugins](#osd_erasure_code_plugins) | `0` | Advanced | عملکرد |
| [osd_failsafe_full_ratio](#osd_failsafe_full_ratio) | `0.97` | Advanced | عملکرد |
| [osd_fast_fail_on_connection_refused](#osd_fast_fail_on_connection_refused) | `True` | Advanced | عملکرد |
| [osd_fast_info](#osd_fast_info) | `True` | Advanced | عملکرد |
| [osd_fast_shutdown](#osd_fast_shutdown) | `True` | Advanced | عملکرد |
| [osd_fast_shutdown_notify_mon](#osd_fast_shutdown_notify_mon) | `True` | Advanced | عملکرد |
| [osd_fast_shutdown_timeout](#osd_fast_shutdown_timeout) | `15` | Advanced | عملکرد |
| [osd_force_auth_primary_missing_objects](#osd_force_auth_primary_missing_objects) | `100` | Advanced | عملکرد |
| [osd_force_recovery_pg_log_entries_factor](#osd_force_recovery_pg_log_entries_factor) | `1.3` | Dev | توسعه |
| [osd_function_tracing](#osd_function_tracing) | `False` | Advanced | عملکرد |
| [osd_heartbeat_grace](#osd_heartbeat_grace) | `20` | Advanced | عملکرد |
| [osd_heartbeat_interval](#osd_heartbeat_interval) | `6` | Dev | توسعه |
| [osd_heartbeat_min_healthy_ratio](#osd_heartbeat_min_healthy_ratio) | `0.33` | Advanced | عملکرد |
| [osd_heartbeat_min_size](#osd_heartbeat_min_size) | `2000` | Advanced | عملکرد |
| [osd_heartbeat_stale](#osd_heartbeat_stale) | `10_min` | Advanced | عملکرد |
| [osd_heartbeat_use_min_delay_socket](#osd_heartbeat_use_min_delay_socket) | `False` | Advanced | عملکرد |
| [osd_hit_set_max_size](#osd_hit_set_max_size) | `100000` | Advanced | عملکرد |
| [osd_hit_set_min_size](#osd_hit_set_min_size) | `1000` | Advanced | عملکرد |
| [osd_hit_set_namespace](#osd_hit_set_namespace) | `.ceph-internal` | Advanced | عملکرد |
| [osd_ignore_stale_divergent_priors](#osd_ignore_stale_divergent_priors) | `False` | Advanced | عملکرد |
| [osd_kill_backfill_at](#osd_kill_backfill_at) | `0` | Dev | توسعه |
| [osd_loop_before_reset_tphandle](#osd_loop_before_reset_tphandle) | `64` | Advanced | عملکرد |
| [osd_map_dedup](#osd_map_dedup) | `True` | Advanced | عملکرد |
| [osd_map_message_max](#osd_map_message_max) | `40` | Advanced | عملکرد |
| [osd_map_message_max_bytes](#osd_map_message_max_bytes) | `10_M` | Advanced | عملکرد |
| [osd_max_attr_name_len](#osd_max_attr_name_len) | `100` | Advanced | عملکرد |
| [osd_max_attr_size](#osd_max_attr_size) | `0` | Advanced | عملکرد |
| [osd_max_object_name_len](#osd_max_object_name_len) | `2_K` | Advanced | عملکرد |
| [osd_max_object_namespace_len](#osd_max_object_namespace_len) | `256` | Advanced | عملکرد |
| [osd_max_object_size](#osd_max_object_size) | `128_M` | Advanced | عملکرد |
| [osd_max_omap_bytes_per_request](#osd_max_omap_bytes_per_request) | `1_G` | Advanced | عملکرد |
| [osd_max_omap_entries_per_request](#osd_max_omap_entries_per_request) | `1_K` | Advanced | عملکرد |
| [osd_max_pg_blocked_by](#osd_max_pg_blocked_by) | `16` | Advanced | عملکرد |
| [osd_max_pg_log_entries](#osd_max_pg_log_entries) | `10000` | Dev | توسعه |
| [osd_max_pg_per_osd_hard_ratio](#osd_max_pg_per_osd_hard_ratio) | `3` | Advanced | عملکرد |
| [osd_max_snap_prune_intervals_per_epoch](#osd_max_snap_prune_intervals_per_epoch) | `512` | Dev | توسعه |
| [osd_max_trimming_pgs](#osd_max_trimming_pgs) | `2` | Advanced | عملکرد |
| [osd_max_write_op_reply_len](#osd_max_write_op_reply_len) | `64` | Advanced | عملکرد |
| [osd_memory_base](#osd_memory_base) | `768_M` | Dev | توسعه |
| [osd_memory_cache_min](#osd_memory_cache_min) | `128_M` | Dev | توسعه |
| [osd_memory_cache_resize_interval](#osd_memory_cache_resize_interval) | `1` | Dev | توسعه |
| [osd_memory_expected_fragmentation](#osd_memory_expected_fragmentation) | `0.15` | Dev | توسعه |
| [osd_memory_target](#osd_memory_target) | `4_G` | Basic | سیاست |
| [osd_memory_target_autotune](#osd_memory_target_autotune) | `False` | Advanced | عملکرد |
| [osd_memory_target_cgroup_limit_ratio](#osd_memory_target_cgroup_limit_ratio) | `0.8` | Advanced | عملکرد |
| [osd_min_pg_log_entries](#osd_min_pg_log_entries) | `250` | Dev | توسعه |
| [osd_min_split_replica_read_size](#osd_min_split_replica_read_size) | `0` | Advanced | عملکرد |
| [osd_mon_heartbeat_interval](#osd_mon_heartbeat_interval) | `30` | Advanced | عملکرد |
| [osd_mon_heartbeat_stat_stale](#osd_mon_heartbeat_stat_stale) | `1_hr` | Advanced | عملکرد |
| [osd_mon_report_interval](#osd_mon_report_interval) | `5` | Advanced | عملکرد |
| [osd_mon_report_max_in_flight](#osd_mon_report_max_in_flight) | `2` | Advanced | عملکرد |
| [osd_mon_shutdown_timeout](#osd_mon_shutdown_timeout) | `5` | Advanced | عملکرد |
| [osd_num_op_tracker_shard](#osd_num_op_tracker_shard) | `32` | Advanced | عملکرد |
| [osd_object_clean_region_max_num_intervals](#osd_object_clean_region_max_num_intervals) | `10` | Dev | توسعه |
| [osd_objecter_finishers](#osd_objecter_finishers) | `1` | Advanced | عملکرد |
| [osd_objectstore](#osd_objectstore) | `bluestore` | Advanced | عملکرد |
| [osd_objectstore_fuse](#osd_objectstore_fuse) | `False` | Advanced | عملکرد |
| [osd_objectstore_ideal_list_max](#osd_objectstore_ideal_list_max) | `64` | Advanced | عملکرد |
| [osd_objectstore_tracing](#osd_objectstore_tracing) | `False` | Advanced | عملکرد |
| [osd_op_complaint_time](#osd_op_complaint_time) | `30` | Advanced | عملکرد |
| [osd_op_history_duration](#osd_op_history_duration) | `600` | Advanced | عملکرد |
| [osd_op_history_size](#osd_op_history_size) | `20` | Advanced | عملکرد |
| [osd_op_history_slow_op_size](#osd_op_history_slow_op_size) | `20` | Advanced | عملکرد |
| [osd_op_history_slow_op_threshold](#osd_op_history_slow_op_threshold) | `10` | Advanced | عملکرد |
| [osd_op_log_threshold](#osd_op_log_threshold) | `5` | Advanced | عملکرد |
| [osd_peering_op_priority](#osd_peering_op_priority) | `255` | Dev | توسعه |
| [osd_pg_delete_cost](#osd_pg_delete_cost) | `1_M` | Advanced | عملکرد |
| [osd_pg_delete_priority](#osd_pg_delete_priority) | `5` | Advanced | عملکرد |
| [osd_pg_epoch_persisted_max_stale](#osd_pg_epoch_persisted_max_stale) | `40` | Advanced | عملکرد |
| [osd_pg_log_dups_tracked](#osd_pg_log_dups_tracked) | `3000` | Dev | توسعه |
| [osd_pg_log_trim_max](#osd_pg_log_trim_max) | `10000` | Advanced | عملکرد |
| [osd_pg_log_trim_min](#osd_pg_log_trim_min) | `100` | Dev | توسعه |
| [osd_pg_max_concurrent_snap_trims](#osd_pg_max_concurrent_snap_trims) | `2` | Advanced | عملکرد |
| [osd_pg_object_context_cache_count](#osd_pg_object_context_cache_count) | `64` | Advanced | عملکرد |
| [osd_pg_stat_report_interval_max_epochs](#osd_pg_stat_report_interval_max_epochs) | `500` | Advanced | عملکرد |
| [osd_pg_stat_report_interval_max_seconds](#osd_pg_stat_report_interval_max_seconds) | `5` | Advanced | عملکرد |
| [osd_pool_default_cache_max_evict_check_size](#osd_pool_default_cache_max_evict_check_size) | `10` | Advanced | عملکرد |
| [osd_pool_default_cache_min_evict_age](#osd_pool_default_cache_min_evict_age) | `0` | Advanced | عملکرد |
| [osd_pool_default_cache_min_flush_age](#osd_pool_default_cache_min_flush_age) | `0` | Advanced | عملکرد |
| [osd_pool_default_cache_target_dirty_high_ratio](#osd_pool_default_cache_target_dirty_high_ratio) | `0.6` | Advanced | عملکرد |
| [osd_pool_default_cache_target_dirty_ratio](#osd_pool_default_cache_target_dirty_ratio) | `0.4` | Advanced | عملکرد |
| [osd_pool_default_cache_target_full_ratio](#osd_pool_default_cache_target_full_ratio) | `0.8` | Advanced | عملکرد |
| [osd_pool_default_crush_rule](#osd_pool_default_crush_rule) | `-1` | Advanced | عملکرد |
| [osd_pool_default_ec_fast_read](#osd_pool_default_ec_fast_read) | `False` | Advanced | عملکرد |
| [osd_pool_default_erasure_code_profile](#osd_pool_default_erasure_code_profile) | `plugin=isa technique=reed_sol_van k=2 m=2` | Advanced | عملکرد |
| [osd_pool_default_flag_bulk](#osd_pool_default_flag_bulk) | `False` | Advanced | عملکرد |
| [osd_pool_default_flag_ec_optimizations](#osd_pool_default_flag_ec_optimizations) | `False` | Advanced | عملکرد |
| [osd_pool_default_flag_hashpspool](#osd_pool_default_flag_hashpspool) | `True` | Advanced | عملکرد |
| [osd_pool_default_flag_nodelete](#osd_pool_default_flag_nodelete) | `False` | Advanced | عملکرد |
| [osd_pool_default_flag_nopgchange](#osd_pool_default_flag_nopgchange) | `False` | Advanced | عملکرد |
| [osd_pool_default_flag_nosizechange](#osd_pool_default_flag_nosizechange) | `False` | Advanced | عملکرد |
| [osd_pool_default_flags](#osd_pool_default_flags) | `0` | Dev | توسعه |
| [osd_pool_default_hit_set_bloom_fpp](#osd_pool_default_hit_set_bloom_fpp) | `0.05` | Advanced | عملکرد |
| [osd_pool_default_min_size](#osd_pool_default_min_size) | `0` | Advanced | عملکرد |
| [osd_pool_default_pg_autoscale_mode](#osd_pool_default_pg_autoscale_mode) | `on` | Advanced | عملکرد |
| [osd_pool_default_pg_num](#osd_pool_default_pg_num) | `32` | Advanced | عملکرد |
| [osd_pool_default_pgp_num](#osd_pool_default_pgp_num) | `0` | Advanced | عملکرد |
| [osd_pool_default_read_lease_ratio](#osd_pool_default_read_lease_ratio) | `0.8` | Dev | توسعه |
| [osd_pool_default_read_ratio](#osd_pool_default_read_ratio) | `70` | Advanced | عملکرد |
| [osd_pool_default_size](#osd_pool_default_size) | `3` | Advanced | عملکرد |
| [osd_pool_default_type](#osd_pool_default_type) | `replicated` | Advanced | عملکرد |
| [osd_pool_use_gmt_hitset](#osd_pool_use_gmt_hitset) | `True` | Dev | توسعه |
| [osd_recovery_cost](#osd_recovery_cost) | `20_M` | Advanced | عملکرد |
| [osd_recovery_op_priority](#osd_recovery_op_priority) | `3` | Advanced | عملکرد |
| [osd_recovery_op_warn_multiple](#osd_recovery_op_warn_multiple) | `16` | Advanced | عملکرد |
| [osd_recovery_priority](#osd_recovery_priority) | `5` | Advanced | عملکرد |
| [osd_requested_scrub_priority](#osd_requested_scrub_priority) | `5` | Advanced | عملکرد |
| [osd_rollback_to_cluster_snap](#osd_rollback_to_cluster_snap) | `(empty)` | Advanced | عملکرد |
| [osd_scrub_cost](#osd_scrub_cost) | `50_M` | Advanced | عملکرد |
| [osd_scrub_event_cost](#osd_scrub_event_cost) | `4_K` | Advanced | عملکرد |
| [osd_scrub_priority](#osd_scrub_priority) | `5` | Advanced | عملکرد |
| [osd_shutdown_pgref_assert](#osd_shutdown_pgref_assert) | `False` | Advanced | عملکرد |
| [osd_skip_check_past_interval_bounds](#osd_skip_check_past_interval_bounds) | `False` | Dev | توسعه |
| [osd_snap_trim_cost](#osd_snap_trim_cost) | `1_M` | Advanced | عملکرد |
| [osd_snap_trim_priority](#osd_snap_trim_priority) | `5` | Advanced | عملکرد |
| [osd_target_pg_log_entries_per_osd](#osd_target_pg_log_entries_per_osd) | `300000` | Dev | توسعه |
| [osd_target_transaction_size](#osd_target_transaction_size) | `30` | Advanced | عملکرد |
| [osd_tier_default_cache_hit_set_count](#osd_tier_default_cache_hit_set_count) | `4` | Advanced | عملکرد |
| [osd_tier_default_cache_hit_set_grade_decay_rate](#osd_tier_default_cache_hit_set_grade_decay_rate) | `20` | Advanced | عملکرد |
| [osd_tier_default_cache_hit_set_period](#osd_tier_default_cache_hit_set_period) | `1200` | Advanced | عملکرد |
| [osd_tier_default_cache_hit_set_search_last_n](#osd_tier_default_cache_hit_set_search_last_n) | `1` | Advanced | عملکرد |
| [osd_tier_default_cache_hit_set_type](#osd_tier_default_cache_hit_set_type) | `bloom` | Advanced | عملکرد |
| [osd_tier_default_cache_min_read_recency_for_promote](#osd_tier_default_cache_min_read_recency_for_promote) | `1` | Advanced | عملکرد |
| [osd_tier_default_cache_min_write_recency_for_promote](#osd_tier_default_cache_min_write_recency_for_promote) | `1` | Advanced | عملکرد |
| [osd_tier_default_cache_mode](#osd_tier_default_cache_mode) | `writeback` | Advanced | عملکرد |
| [osd_tier_promote_max_bytes_sec](#osd_tier_promote_max_bytes_sec) | `5_M` | Advanced | عملکرد |
| [osd_tier_promote_max_objects_sec](#osd_tier_promote_max_objects_sec) | `25` | Advanced | عملکرد |
| [osd_tracing](#osd_tracing) | `False` | Advanced | عملکرد |
| [osd_use_stale_snap](#osd_use_stale_snap) | `False` | Advanced | عملکرد |

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

### osd_asio_thread_count

| | |
|---|---|
| نوع | Uint · default `2` · **Advanced** |
| جدول | [osd.md#SP_osd_asio_thread_count](../../../config/global/osd.md#SP_osd_asio_thread_count) |

**کارکرد:** Size of thread pool for ASIO completions

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_asio_thread_count 2
ceph config get osd osd_asio_thread_count
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_asio_thread_count
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_async_recovery_min_cost

| | |
|---|---|
| نوع | Uint · default `100` · **Advanced** |
| جدول | [osd.md#SP_osd_async_recovery_min_cost](../../../config/global/osd.md#SP_osd_async_recovery_min_cost) |

**کارکرد:** A mixture measure of number of current log entries difference and historical missing objects, above which we switch to use asynchronous recovery when appropriate

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_async_recovery_min_cost 100
ceph config get osd osd_async_recovery_min_cost
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `100`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_async_recovery_min_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_auto_mark_unfound_lost

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_auto_mark_unfound_lost](../../../config/global/osd.md#SP_osd_auto_mark_unfound_lost) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_auto_mark_unfound_lost true
ceph config get osd osd_auto_mark_unfound_lost
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_auto_mark_unfound_lost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_backoff_on_degraded

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_backoff_on_degraded](../../../config/global/osd.md#SP_osd_backoff_on_degraded) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_backoff_on_degraded true
ceph config get osd osd_backoff_on_degraded
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_backoff_on_degraded
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_backoff_on_peering

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_backoff_on_peering](../../../config/global/osd.md#SP_osd_backoff_on_peering) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_backoff_on_peering true
ceph config get osd osd_backoff_on_peering
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_backoff_on_peering
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_backoff_on_unfound

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [osd.md#SP_osd_backoff_on_unfound](../../../config/global/osd.md#SP_osd_backoff_on_unfound) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_backoff_on_unfound false
ceph config get osd osd_backoff_on_unfound
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_backoff_on_unfound
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_beacon_report_interval

| | |
|---|---|
| نوع | Int · default `5_min` · **Advanced** |
| جدول | [osd.md#SP_osd_beacon_report_interval](../../../config/global/osd.md#SP_osd_beacon_report_interval) |

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_beacon_report_interval 5_min
ceph config get osd osd_beacon_report_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_beacon_report_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_bench_duration

| | |
|---|---|
| نوع | Uint · default `30` · **Advanced** |
| جدول | [osd.md#SP_osd_bench_duration](../../../config/global/osd.md#SP_osd_bench_duration) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_bench_duration 30
ceph config get osd osd_bench_duration
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_bench_duration
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_bench_large_size_max_throughput

| | |
|---|---|
| نوع | Size · default `100_M` · **Advanced** |
| جدول | [osd.md#SP_osd_bench_large_size_max_throughput](../../../config/global/osd.md#SP_osd_bench_large_size_max_throughput) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_bench_large_size_max_throughput 100_M
ceph config get osd osd_bench_large_size_max_throughput
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `100_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_bench_large_size_max_throughput
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_bench_max_block_size

| | |
|---|---|
| نوع | Size · default `64_M` · **Advanced** |
| جدول | [osd.md#SP_osd_bench_max_block_size](../../../config/global/osd.md#SP_osd_bench_max_block_size) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_bench_max_block_size 64_M
ceph config get osd osd_bench_max_block_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_bench_max_block_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_bench_small_size_max_iops

| | |
|---|---|
| نوع | Uint · default `100` · **Advanced** |
| جدول | [osd.md#SP_osd_bench_small_size_max_iops](../../../config/global/osd.md#SP_osd_bench_small_size_max_iops) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_bench_small_size_max_iops 100
ceph config get osd osd_bench_small_size_max_iops
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `100`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_bench_small_size_max_iops
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_blkin_trace_all

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_blkin_trace_all](../../../config/global/osd.md#SP_osd_blkin_trace_all) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_blkin_trace_all true
ceph config get osd osd_blkin_trace_all
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_blkin_trace_all
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_calc_pg_upmaps_aggressively

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [osd.md#SP_osd_calc_pg_upmaps_aggressively](../../../config/global/osd.md#SP_osd_calc_pg_upmaps_aggressively) |

**کارکرد:** Try to calculate PG upmaps more aggressively, e.g., by doing a fairly exhaustive search of existing PGs that can be unmapped or upmapped

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_calc_pg_upmaps_aggressively false
ceph config get osd osd_calc_pg_upmaps_aggressively
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_calc_pg_upmaps_aggressively
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_calc_pg_upmaps_aggressively_fast

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [osd.md#SP_osd_calc_pg_upmaps_aggressively_fast](../../../config/global/osd.md#SP_osd_calc_pg_upmaps_aggressively_fast) |

**کارکرد:** Prevent very long (>10 minutes) calculations in some extreme cases (applicable only to aggressive mode)

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_calc_pg_upmaps_aggressively_fast false
ceph config get osd osd_calc_pg_upmaps_aggressively_fast
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_calc_pg_upmaps_aggressively_fast
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_calc_pg_upmaps_local_fallback_retries

| | |
|---|---|
| نوع | Uint · default `100` · **Advanced** |
| جدول | [osd.md#SP_osd_calc_pg_upmaps_local_fallback_retries](../../../config/global/osd.md#SP_osd_calc_pg_upmaps_local_fallback_retries) |

**کارکرد:** Maximum number of PGs we can attempt to unmap or upmap for a specific overfull or underfull OSD per iteration

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_calc_pg_upmaps_local_fallback_retries 100
ceph config get osd osd_calc_pg_upmaps_local_fallback_retries
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `100`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_calc_pg_upmaps_local_fallback_retries
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_check_for_log_corruption

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_check_for_log_corruption](../../../config/global/osd.md#SP_osd_check_for_log_corruption) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_check_for_log_corruption true
ceph config get osd osd_check_for_log_corruption
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_check_for_log_corruption
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_client_op_priority

| | |
|---|---|
| نوع | Uint · default `63` · **Advanced** |
| جدول | [osd.md#SP_osd_client_op_priority](../../../config/global/osd.md#SP_osd_client_op_priority) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_client_op_priority 63
ceph config get osd osd_client_op_priority
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `63`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_client_op_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_command_max_records

| | |
|---|---|
| نوع | Int · default `256` · **Advanced** |
| جدول | [osd.md#SP_osd_command_max_records](../../../config/global/osd.md#SP_osd_command_max_records) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_command_max_records 256
ceph config get osd osd_command_max_records
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `256`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_command_max_records
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_crush_chooseleaf_type

| | |
|---|---|
| نوع | Int · default `1` · **Dev** |
| جدول | [osd.md#SP_osd_crush_chooseleaf_type](../../../config/global/osd.md#SP_osd_crush_chooseleaf_type) |

**کارکرد:** default chooseleaf type for osdmaptool --create

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_crush_chooseleaf_type 1
ceph config get osd osd_crush_chooseleaf_type
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_crash_on_ignored_backoff

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_debug_crash_on_ignored_backoff](../../../config/global/osd.md#SP_osd_debug_crash_on_ignored_backoff) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_crash_on_ignored_backoff true
ceph config get osd osd_debug_crash_on_ignored_backoff
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_deep_scrub_sleep

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [osd.md#SP_osd_debug_deep_scrub_sleep](../../../config/global/osd.md#SP_osd_debug_deep_scrub_sleep) |

**کارکرد:** Inject an expensive sleep during deep scrub IO to make it easier to induce preemption

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_deep_scrub_sleep 0
ceph config get osd osd_debug_deep_scrub_sleep
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_drop_ping_duration

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [osd.md#SP_osd_debug_drop_ping_duration](../../../config/global/osd.md#SP_osd_debug_drop_ping_duration) |

**کارکرد:** N/A

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_drop_ping_duration 64
ceph config get osd osd_debug_drop_ping_duration
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_drop_ping_probability

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [osd.md#SP_osd_debug_drop_ping_probability](../../../config/global/osd.md#SP_osd_debug_drop_ping_probability) |

**کارکرد:** N/A

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_drop_ping_probability 0
ceph config get osd osd_debug_drop_ping_probability
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_inject_copyfrom_error

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_debug_inject_copyfrom_error](../../../config/global/osd.md#SP_osd_debug_inject_copyfrom_error) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_inject_copyfrom_error true
ceph config get osd osd_debug_inject_copyfrom_error
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_inject_dispatch_delay_duration

| | |
|---|---|
| نوع | Float · default `0.1` · **Dev** |
| جدول | [osd.md#SP_osd_debug_inject_dispatch_delay_duration](../../../config/global/osd.md#SP_osd_debug_inject_dispatch_delay_duration) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_inject_dispatch_delay_duration 0.1
ceph config get osd osd_debug_inject_dispatch_delay_duration
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.1`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_inject_dispatch_delay_probability

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [osd.md#SP_osd_debug_inject_dispatch_delay_probability](../../../config/global/osd.md#SP_osd_debug_inject_dispatch_delay_probability) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_inject_dispatch_delay_probability 0
ceph config get osd osd_debug_inject_dispatch_delay_probability
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_misdirected_ops

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_debug_misdirected_ops](../../../config/global/osd.md#SP_osd_debug_misdirected_ops) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_misdirected_ops true
ceph config get osd osd_debug_misdirected_ops
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_no_acting_change

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_debug_no_acting_change](../../../config/global/osd.md#SP_osd_debug_no_acting_change) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_no_acting_change true
ceph config get osd osd_debug_no_acting_change
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_no_purge_strays

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_debug_no_purge_strays](../../../config/global/osd.md#SP_osd_debug_no_purge_strays) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_no_purge_strays true
ceph config get osd osd_debug_no_purge_strays
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_op_order

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_debug_op_order](../../../config/global/osd.md#SP_osd_debug_op_order) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_op_order true
ceph config get osd osd_debug_op_order
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_pg_log_writeout

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_debug_pg_log_writeout](../../../config/global/osd.md#SP_osd_debug_pg_log_writeout) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_pg_log_writeout true
ceph config get osd osd_debug_pg_log_writeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_pretend_recovery_active

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_debug_pretend_recovery_active](../../../config/global/osd.md#SP_osd_debug_pretend_recovery_active) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_pretend_recovery_active true
ceph config get osd osd_debug_pretend_recovery_active
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_random_push_read_error

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [osd.md#SP_osd_debug_random_push_read_error](../../../config/global/osd.md#SP_osd_debug_random_push_read_error) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_random_push_read_error 0
ceph config get osd osd_debug_random_push_read_error
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_reject_backfill_probability

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [osd.md#SP_osd_debug_reject_backfill_probability](../../../config/global/osd.md#SP_osd_debug_reject_backfill_probability) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_reject_backfill_probability 0
ceph config get osd osd_debug_reject_backfill_probability
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_shutdown

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_debug_shutdown](../../../config/global/osd.md#SP_osd_debug_shutdown) |

**کارکرد:** Turn up debug levels during shutdown

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_shutdown true
ceph config get osd osd_debug_shutdown
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_skip_full_check_in_backfill_reservation

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_debug_skip_full_check_in_backfill_reservation](../../../config/global/osd.md#SP_osd_debug_skip_full_check_in_backfill_reservation) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_skip_full_check_in_backfill_reservation true
ceph config get osd osd_debug_skip_full_check_in_backfill_reservation
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_skip_full_check_in_recovery

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_debug_skip_full_check_in_recovery](../../../config/global/osd.md#SP_osd_debug_skip_full_check_in_recovery) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_skip_full_check_in_recovery true
ceph config get osd osd_debug_skip_full_check_in_recovery
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_verify_cached_snaps

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_debug_verify_cached_snaps](../../../config/global/osd.md#SP_osd_debug_verify_cached_snaps) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_verify_cached_snaps true
ceph config get osd osd_debug_verify_cached_snaps
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_verify_missing_on_start

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_debug_verify_missing_on_start](../../../config/global/osd.md#SP_osd_debug_verify_missing_on_start) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_verify_missing_on_start true
ceph config get osd osd_debug_verify_missing_on_start
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_verify_snaps

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_debug_verify_snaps](../../../config/global/osd.md#SP_osd_debug_verify_snaps) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_verify_snaps true
ceph config get osd osd_debug_verify_snaps
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_verify_stray_on_activate

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_debug_verify_stray_on_activate](../../../config/global/osd.md#SP_osd_debug_verify_stray_on_activate) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_verify_stray_on_activate true
ceph config get osd osd_debug_verify_stray_on_activate
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_default_data_pool_replay_window

| | |
|---|---|
| نوع | Int · default `45` · **Advanced** |
| جدول | [osd.md#SP_osd_default_data_pool_replay_window](../../../config/global/osd.md#SP_osd_default_data_pool_replay_window) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_default_data_pool_replay_window 45
ceph config get osd osd_default_data_pool_replay_window
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `45`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_default_data_pool_replay_window
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_default_notify_timeout

| | |
|---|---|
| نوع | Uint · default `30` · **Advanced** |
| جدول | [osd.md#SP_osd_default_notify_timeout](../../../config/global/osd.md#SP_osd_default_notify_timeout) |

**کارکرد:** default number of seconds after which notify propagation times out. used if a client has not specified other value

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_default_notify_timeout 30
ceph config get osd osd_default_notify_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_default_notify_timeout
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_discard_disconnected_ops

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [osd.md#SP_osd_discard_disconnected_ops](../../../config/global/osd.md#SP_osd_discard_disconnected_ops) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_discard_disconnected_ops false
ceph config get osd osd_discard_disconnected_ops
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_discard_disconnected_ops
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_enable_op_tracker

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [osd.md#SP_osd_enable_op_tracker](../../../config/global/osd.md#SP_osd_enable_op_tracker) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_enable_op_tracker false
ceph config get osd osd_enable_op_tracker
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_enable_op_tracker
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_erasure_code_plugins

| | |
|---|---|
| نوع | Str · default `0` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [osd.md#SP_osd_erasure_code_plugins](../../../config/global/osd.md#SP_osd_erasure_code_plugins) |

**کارکرد:** Erasure code plugins to load

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_erasure_code_plugins "example"
ceph config get osd osd_erasure_code_plugins
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_erasure_code_plugins
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_failsafe_full_ratio

| | |
|---|---|
| نوع | Float · default `0.97` · **Advanced** |
| جدول | [osd.md#SP_osd_failsafe_full_ratio](../../../config/global/osd.md#SP_osd_failsafe_full_ratio) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_failsafe_full_ratio 0.97
ceph config get osd osd_failsafe_full_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.97`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_failsafe_full_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_fast_fail_on_connection_refused

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [osd.md#SP_osd_fast_fail_on_connection_refused](../../../config/global/osd.md#SP_osd_fast_fail_on_connection_refused) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_fast_fail_on_connection_refused false
ceph config get osd osd_fast_fail_on_connection_refused
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_fast_fail_on_connection_refused
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_fast_info

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [osd.md#SP_osd_fast_info](../../../config/global/osd.md#SP_osd_fast_info) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_fast_info false
ceph config get osd osd_fast_info
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_fast_info
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_fast_shutdown

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [osd.md#SP_osd_fast_shutdown](../../../config/global/osd.md#SP_osd_fast_shutdown) |

**کارکرد:** Fast, immediate shutdown Setting this to false makes the OSD do a slower teardown of all state when it receives a SIGINT or SIGTERM or when shutting down for any other reason. That slow shutdown is primarilyy useful for doing memory leak checking with valgrind.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_fast_shutdown false
ceph config get osd osd_fast_shutdown
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_fast_shutdown
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_fast_shutdown_notify_mon

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [osd.md#SP_osd_fast_shutdown_notify_mon](../../../config/global/osd.md#SP_osd_fast_shutdown_notify_mon) |

**کارکرد:** Tell the Monitors about OSD shutdown on immediate shutdown Tell the Monitors the OSD is shutting down on immediate shutdown. This helps with cluster log messages from other OSDs reporting it immediately failed.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_fast_shutdown_notify_mon false
ceph config get osd osd_fast_shutdown_notify_mon
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_fast_shutdown_notify_mon
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_fast_shutdown_timeout

| | |
|---|---|
| نوع | Int · default `15` · **Advanced** |
| جدول | [osd.md#SP_osd_fast_shutdown_timeout](../../../config/global/osd.md#SP_osd_fast_shutdown_timeout) |

**کارکرد:** Timeout in seconds for osd fast-shutdown (0 is unlimited)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_fast_shutdown_timeout 15
ceph config get osd osd_fast_shutdown_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `15`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_fast_shutdown_timeout
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_force_auth_primary_missing_objects

| | |
|---|---|
| نوع | Uint · default `100` · **Advanced** |
| جدول | [osd.md#SP_osd_force_auth_primary_missing_objects](../../../config/global/osd.md#SP_osd_force_auth_primary_missing_objects) |

**کارکرد:** Approximate missing objects above which to force auth_log_shard to be primary temporarily

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_force_auth_primary_missing_objects 100
ceph config get osd osd_force_auth_primary_missing_objects
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `100`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_force_auth_primary_missing_objects
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_force_recovery_pg_log_entries_factor

| | |
|---|---|
| نوع | Float · default `1.3` · **Dev** |
| جدول | [osd.md#SP_osd_force_recovery_pg_log_entries_factor](../../../config/global/osd.md#SP_osd_force_recovery_pg_log_entries_factor) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_force_recovery_pg_log_entries_factor 1.3
ceph config get osd osd_force_recovery_pg_log_entries_factor
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1.3`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_function_tracing

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_function_tracing](../../../config/global/osd.md#SP_osd_function_tracing) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_function_tracing true
ceph config get osd osd_function_tracing
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_function_tracing
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_heartbeat_grace

| | |
|---|---|
| نوع | Int · default `20` · **Advanced** |
| جدول | [osd.md#SP_osd_heartbeat_grace](../../../config/global/osd.md#SP_osd_heartbeat_grace) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_heartbeat_grace 20
ceph config get osd osd_heartbeat_grace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `20`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_heartbeat_grace
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_heartbeat_interval

| | |
|---|---|
| نوع | Int · default `6` · **Dev** |
| جدول | [osd.md#SP_osd_heartbeat_interval](../../../config/global/osd.md#SP_osd_heartbeat_interval) |

**کارکرد:** Interval (in seconds) between peer pings

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_heartbeat_interval 6
ceph config get osd osd_heartbeat_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`6`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_heartbeat_min_healthy_ratio

| | |
|---|---|
| نوع | Float · default `0.33` · **Advanced** |
| جدول | [osd.md#SP_osd_heartbeat_min_healthy_ratio](../../../config/global/osd.md#SP_osd_heartbeat_min_healthy_ratio) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_heartbeat_min_healthy_ratio 0.33
ceph config get osd osd_heartbeat_min_healthy_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.33`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_heartbeat_min_healthy_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_heartbeat_min_size

| | |
|---|---|
| نوع | Size · default `2000` · **Advanced** |
| جدول | [osd.md#SP_osd_heartbeat_min_size](../../../config/global/osd.md#SP_osd_heartbeat_min_size) |

**کارکرد:** Minimum heartbeat packet size in bytes. Will padd if the heartbeat packet is smaller than this. This helps identify host and switch MTU configuration issues when jumbo frames are in use.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_heartbeat_min_size 2000
ceph config get osd osd_heartbeat_min_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_heartbeat_min_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_heartbeat_stale

| | |
|---|---|
| نوع | Int · default `10_min` · **Advanced** |
| جدول | [osd.md#SP_osd_heartbeat_stale](../../../config/global/osd.md#SP_osd_heartbeat_stale) |

**کارکرد:** Interval (in seconds) we mark an unresponsive heartbeat peer as stale. Automatically mark unresponsive heartbeat sessions as stale and tear them down. The primary benefit is that OSD doesn't need to keep a flood of blocked heartbeat messages around in memory.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_heartbeat_stale 10_min
ceph config get osd osd_heartbeat_stale
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_heartbeat_stale
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_heartbeat_use_min_delay_socket

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_heartbeat_use_min_delay_socket](../../../config/global/osd.md#SP_osd_heartbeat_use_min_delay_socket) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_heartbeat_use_min_delay_socket true
ceph config get osd osd_heartbeat_use_min_delay_socket
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_heartbeat_use_min_delay_socket
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_hit_set_max_size

| | |
|---|---|
| نوع | Int · default `100000` · **Advanced** |
| جدول | [osd.md#SP_osd_hit_set_max_size](../../../config/global/osd.md#SP_osd_hit_set_max_size) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_hit_set_max_size 100000
ceph config get osd osd_hit_set_max_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `100000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_hit_set_max_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_hit_set_min_size

| | |
|---|---|
| نوع | Int · default `1000` · **Advanced** |
| جدول | [osd.md#SP_osd_hit_set_min_size](../../../config/global/osd.md#SP_osd_hit_set_min_size) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_hit_set_min_size 1000
ceph config get osd osd_hit_set_min_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_hit_set_min_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_hit_set_namespace

| | |
|---|---|
| نوع | Str · default `.ceph-internal` · **Advanced** |
| جدول | [osd.md#SP_osd_hit_set_namespace](../../../config/global/osd.md#SP_osd_hit_set_namespace) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_hit_set_namespace ".ceph-internal"
ceph config get osd osd_hit_set_namespace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `.ceph-internal`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_hit_set_namespace
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_ignore_stale_divergent_priors

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_ignore_stale_divergent_priors](../../../config/global/osd.md#SP_osd_ignore_stale_divergent_priors) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_ignore_stale_divergent_priors true
ceph config get osd osd_ignore_stale_divergent_priors
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_ignore_stale_divergent_priors
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_kill_backfill_at

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [osd.md#SP_osd_kill_backfill_at](../../../config/global/osd.md#SP_osd_kill_backfill_at) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_kill_backfill_at 64
ceph config get osd osd_kill_backfill_at
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_loop_before_reset_tphandle

| | |
|---|---|
| نوع | Uint · default `64` · **Advanced** |
| جدول | [osd.md#SP_osd_loop_before_reset_tphandle](../../../config/global/osd.md#SP_osd_loop_before_reset_tphandle) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_loop_before_reset_tphandle 64
ceph config get osd osd_loop_before_reset_tphandle
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_loop_before_reset_tphandle
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_map_dedup

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [osd.md#SP_osd_map_dedup](../../../config/global/osd.md#SP_osd_map_dedup) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_map_dedup false
ceph config get osd osd_map_dedup
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_map_dedup
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_map_message_max

| | |
|---|---|
| نوع | Int · default `40` · **Advanced** |
| جدول | [osd.md#SP_osd_map_message_max](../../../config/global/osd.md#SP_osd_map_message_max) |

**کارکرد:** Maximum number of OSDMaps to include in a single message

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_map_message_max 40
ceph config get osd osd_map_message_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `40`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_map_message_max
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_map_message_max_bytes

| | |
|---|---|
| نوع | Size · default `10_M` · **Advanced** |
| جدول | [osd.md#SP_osd_map_message_max_bytes](../../../config/global/osd.md#SP_osd_map_message_max_bytes) |

**کارکرد:** Maximum number of bytes worth of OSDMaps to include in a single message

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_map_message_max_bytes 10_M
ceph config get osd osd_map_message_max_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_map_message_max_bytes
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_attr_name_len

| | |
|---|---|
| نوع | Uint · default `100` · **Advanced** |
| جدول | [osd.md#SP_osd_max_attr_name_len](../../../config/global/osd.md#SP_osd_max_attr_name_len) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_max_attr_name_len 100
ceph config get osd osd_max_attr_name_len
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `100`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_max_attr_name_len
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_attr_size

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_max_attr_size](../../../config/global/osd.md#SP_osd_max_attr_size) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_max_attr_size 64
ceph config get osd osd_max_attr_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_max_attr_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_object_name_len

| | |
|---|---|
| نوع | Uint · default `2_K` · **Advanced** |
| جدول | [osd.md#SP_osd_max_object_name_len](../../../config/global/osd.md#SP_osd_max_object_name_len) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_max_object_name_len 2_K
ceph config get osd osd_max_object_name_len
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_max_object_name_len
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_object_namespace_len

| | |
|---|---|
| نوع | Uint · default `256` · **Advanced** |
| جدول | [osd.md#SP_osd_max_object_namespace_len](../../../config/global/osd.md#SP_osd_max_object_namespace_len) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_max_object_namespace_len 256
ceph config get osd osd_max_object_namespace_len
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `256`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_max_object_namespace_len
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_object_size

| | |
|---|---|
| نوع | Size · default `128_M` · **Advanced** |
| جدول | [osd.md#SP_osd_max_object_size](../../../config/global/osd.md#SP_osd_max_object_size) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_max_object_size 128_M
ceph config get osd osd_max_object_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `128_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_max_object_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_omap_bytes_per_request

| | |
|---|---|
| نوع | Size · default `1_G` · **Advanced** |
| جدول | [osd.md#SP_osd_max_omap_bytes_per_request](../../../config/global/osd.md#SP_osd_max_omap_bytes_per_request) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_max_omap_bytes_per_request 1_G
ceph config get osd osd_max_omap_bytes_per_request
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_G`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_max_omap_bytes_per_request
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_omap_entries_per_request

| | |
|---|---|
| نوع | Uint · default `1_K` · **Advanced** |
| جدول | [osd.md#SP_osd_max_omap_entries_per_request](../../../config/global/osd.md#SP_osd_max_omap_entries_per_request) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_max_omap_entries_per_request 1_K
ceph config get osd osd_max_omap_entries_per_request
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_max_omap_entries_per_request
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_pg_blocked_by

| | |
|---|---|
| نوع | Uint · default `16` · **Advanced** |
| جدول | [osd.md#SP_osd_max_pg_blocked_by](../../../config/global/osd.md#SP_osd_max_pg_blocked_by) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_max_pg_blocked_by 16
ceph config get osd osd_max_pg_blocked_by
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `16`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_max_pg_blocked_by
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_pg_log_entries

| | |
|---|---|
| نوع | Uint · default `10000` · **Dev** |
| جدول | [osd.md#SP_osd_max_pg_log_entries](../../../config/global/osd.md#SP_osd_max_pg_log_entries) |

**کارکرد:** Maximum number of entries to maintain in the PG log

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_max_pg_log_entries 10000
ceph config get osd osd_max_pg_log_entries
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`10000`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_max_pg_per_osd_hard_ratio

| | |
|---|---|
| نوع | Float · default `3` · **Advanced** |
| جدول | [osd.md#SP_osd_max_pg_per_osd_hard_ratio](../../../config/global/osd.md#SP_osd_max_pg_per_osd_hard_ratio) |

**کارکرد:** Maximum multiple of mon_max_pg_per_osd PGs an OSD will allow An OSD will refuse to instantiate a PG if the number of PGs it serves exceeds this number.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_max_pg_per_osd_hard_ratio 3
ceph config get osd osd_max_pg_per_osd_hard_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_max_pg_per_osd_hard_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_snap_prune_intervals_per_epoch

| | |
|---|---|
| نوع | Uint · default `512` · **Dev** |
| جدول | [osd.md#SP_osd_max_snap_prune_intervals_per_epoch](../../../config/global/osd.md#SP_osd_max_snap_prune_intervals_per_epoch) |

**کارکرد:** Max number of snap intervals to report to mgr in pg_stat_t

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_max_snap_prune_intervals_per_epoch 512
ceph config get osd osd_max_snap_prune_intervals_per_epoch
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`512`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_max_trimming_pgs

| | |
|---|---|
| نوع | Uint · default `2` · **Advanced** |
| جدول | [osd.md#SP_osd_max_trimming_pgs](../../../config/global/osd.md#SP_osd_max_trimming_pgs) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_max_trimming_pgs 2
ceph config get osd osd_max_trimming_pgs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_max_trimming_pgs
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_write_op_reply_len

| | |
|---|---|
| نوع | Size · default `64` · **Advanced** |
| جدول | [osd.md#SP_osd_max_write_op_reply_len](../../../config/global/osd.md#SP_osd_max_write_op_reply_len) |

**کارکرد:** Max size of the per-op payload for requests with the RETURNVEC flag set This value caps the amount of data (per op; a request may have many ops) that will be sent back to the client and recorded in the PG log.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_max_write_op_reply_len 64
ceph config get osd osd_max_write_op_reply_len
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_max_write_op_reply_len
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_memory_base

| | |
|---|---|
| نوع | Size · default `768_M` · **Dev** |
| جدول | [osd.md#SP_osd_memory_base](../../../config/global/osd.md#SP_osd_memory_base) |

**کارکرد:** When TCMalloc and cache autotuning are enabled, estimate the minimum amount of memory in bytes the OSD will need.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_memory_base 768_M
ceph config get osd osd_memory_base
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`768_M`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_memory_cache_min

| | |
|---|---|
| نوع | Size · default `128_M` · **Dev** |
| جدول | [osd.md#SP_osd_memory_cache_min](../../../config/global/osd.md#SP_osd_memory_cache_min) |

**کارکرد:** When TCMalloc and cache autotuning are enabled, set the minimum amount of memory used for caches.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_memory_cache_min 128_M
ceph config get osd osd_memory_cache_min
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`128_M`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_memory_cache_resize_interval

| | |
|---|---|
| نوع | Float · default `1` · **Dev** |
| جدول | [osd.md#SP_osd_memory_cache_resize_interval](../../../config/global/osd.md#SP_osd_memory_cache_resize_interval) |

**کارکرد:** When TCMalloc and cache autotuning are enabled, wait this many seconds between resizing caches.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_memory_cache_resize_interval 1
ceph config get osd osd_memory_cache_resize_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_memory_expected_fragmentation

| | |
|---|---|
| نوع | Float · default `0.15` · **Dev** |
| جدول | [osd.md#SP_osd_memory_expected_fragmentation](../../../config/global/osd.md#SP_osd_memory_expected_fragmentation) |

**کارکرد:** When TCMalloc and cache autotuning are enabled, estimate the percent of memory fragmentation.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_memory_expected_fragmentation 0.15
ceph config get osd osd_memory_expected_fragmentation
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.15`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_memory_target

| | |
|---|---|
| نوع | Size · default `4_G` · **Basic** |
| جدول | [osd.md#SP_osd_memory_target](../../../config/global/osd.md#SP_osd_memory_target) |

**کارکرد:** When TCMalloc and cache autotuning are enabled, try to keep this many bytes mapped in memory. The minimum value must be at least equal to osd_memory_base + osd_memory_cache_min.

**زمان استفاده:** رفتار اصلی Global — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set osd osd_memory_target 4_G
ceph config get osd osd_memory_target
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `4_G` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_memory_target
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_memory_target_autotune

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_memory_target_autotune](../../../config/global/osd.md#SP_osd_memory_target_autotune) |

**کارکرد:** If enabled, allow the orchestrator to automatically tune osd_memory_target at host granularity based on available memory, the number of OSDs provisioned on the host, other daemons provisioned on the host, and mgr/cephadm/autotune_memory_target_ratio

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**گزینه‌های مرتبط:**

- [`osd_memory_target`](../../../config/global/osd.md#SP_osd_memory_target)

**مثال:**

```bash
ceph config set osd osd_memory_target_autotune true
ceph config get osd osd_memory_target_autotune
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_memory_target_autotune
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_memory_target_cgroup_limit_ratio

| | |
|---|---|
| نوع | Float · default `0.8` · **Advanced** |
| جدول | [osd.md#SP_osd_memory_target_cgroup_limit_ratio](../../../config/global/osd.md#SP_osd_memory_target_cgroup_limit_ratio) |

**کارکرد:** Set the default value for osd_memory_target to the cgroup memory limit (if set) times this value A value of 0 disables this feature.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**گزینه‌های مرتبط:**

- [`osd_memory_target`](../../../config/global/osd.md#SP_osd_memory_target)

**مثال:**

```bash
ceph config set osd osd_memory_target_cgroup_limit_ratio 0.8
ceph config get osd osd_memory_target_cgroup_limit_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.8`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `1`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_memory_target_cgroup_limit_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_min_pg_log_entries

| | |
|---|---|
| نوع | Uint · default `250` · **Dev** |
| جدول | [osd.md#SP_osd_min_pg_log_entries](../../../config/global/osd.md#SP_osd_min_pg_log_entries) |

**کارکرد:** Minimum number of entries to maintain in the PG log

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_min_pg_log_entries 250
ceph config get osd osd_min_pg_log_entries
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`250`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_min_split_replica_read_size

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_min_split_replica_read_size](../../../config/global/osd.md#SP_osd_min_split_replica_read_size) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_min_split_replica_read_size 64
ceph config get osd osd_min_split_replica_read_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_min_split_replica_read_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mon_heartbeat_interval

| | |
|---|---|
| نوع | Int · default `30` · **Advanced** |
| جدول | [osd.md#SP_osd_mon_heartbeat_interval](../../../config/global/osd.md#SP_osd_mon_heartbeat_interval) |

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_mon_heartbeat_interval 30
ceph config get osd osd_mon_heartbeat_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mon_heartbeat_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mon_heartbeat_stat_stale

| | |
|---|---|
| نوع | Int · default `1_hr` · **Advanced** |
| جدول | [osd.md#SP_osd_mon_heartbeat_stat_stale](../../../config/global/osd.md#SP_osd_mon_heartbeat_stat_stale) |

**کارکرد:** Stop reporting on heartbeat ping times not updated for this many seconds. Stop reporting on old heartbeat information unless this is set to zero

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_mon_heartbeat_stat_stale 1_hr
ceph config get osd osd_mon_heartbeat_stat_stale
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_hr`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mon_heartbeat_stat_stale
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mon_report_interval

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [osd.md#SP_osd_mon_report_interval](../../../config/global/osd.md#SP_osd_mon_report_interval) |

**کارکرد:** Frequency of OSD reports to mon for peer failures, fullness status changes

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_mon_report_interval 5
ceph config get osd osd_mon_report_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mon_report_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mon_report_max_in_flight

| | |
|---|---|
| نوع | Int · default `2` · **Advanced** |
| جدول | [osd.md#SP_osd_mon_report_max_in_flight](../../../config/global/osd.md#SP_osd_mon_report_max_in_flight) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_mon_report_max_in_flight 2
ceph config get osd osd_mon_report_max_in_flight
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mon_report_max_in_flight
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mon_shutdown_timeout

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [osd.md#SP_osd_mon_shutdown_timeout](../../../config/global/osd.md#SP_osd_mon_shutdown_timeout) |

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_mon_shutdown_timeout 5
ceph config get osd osd_mon_shutdown_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mon_shutdown_timeout
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_num_op_tracker_shard

| | |
|---|---|
| نوع | Uint · default `32` · **Advanced** |
| جدول | [osd.md#SP_osd_num_op_tracker_shard](../../../config/global/osd.md#SP_osd_num_op_tracker_shard) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_num_op_tracker_shard 32
ceph config get osd osd_num_op_tracker_shard
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `32`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_num_op_tracker_shard
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_object_clean_region_max_num_intervals

| | |
|---|---|
| نوع | Int · default `10` · **Dev** |
| جدول | [osd.md#SP_osd_object_clean_region_max_num_intervals](../../../config/global/osd.md#SP_osd_object_clean_region_max_num_intervals) |

**کارکرد:** Number of intervals in clean_offsets Partial recovery uses multiple intervals to record the clean part of the objectwhen the number of intervals is greater than osd_object_clean_region_max_num_intervals, minimum interval will be trimmed(0 will recovery the entire object data interval)

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_object_clean_region_max_num_intervals 10
ceph config get osd osd_object_clean_region_max_num_intervals
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`10`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_objecter_finishers

| | |
|---|---|
| نوع | Int · default `1` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [osd.md#SP_osd_objecter_finishers](../../../config/global/osd.md#SP_osd_objecter_finishers) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_objecter_finishers 1
ceph config get osd osd_objecter_finishers
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_objecter_finishers
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_objectstore

| | |
|---|---|
| نوع | Str · enum: ["bluestore", "filestore", "memstore", "seastore", "cyanstore"] · default `bluestore` · **Advanced** |
| جدول | [osd.md#SP_osd_objectstore](../../../config/global/osd.md#SP_osd_objectstore) |

**کارکرد:** Default back end for new OSDs

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_objectstore bluestore
ceph config get osd osd_objectstore
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `bluestore`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_objectstore
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_objectstore_fuse

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_objectstore_fuse](../../../config/global/osd.md#SP_osd_objectstore_fuse) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_objectstore_fuse true
ceph config get osd osd_objectstore_fuse
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_objectstore_fuse
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_objectstore_ideal_list_max

| | |
|---|---|
| نوع | Uint · default `64` · **Advanced** |
| جدول | [osd.md#SP_osd_objectstore_ideal_list_max](../../../config/global/osd.md#SP_osd_objectstore_ideal_list_max) |

**کارکرد:** The max number of results of ObjectStore::collection_list() This value caps the maximal number of entries a single call to collection_list() can return. The configurable controls this aspect of PG deletion and OSD::clear_temp_objects(). Increasing it trade-offs less agressive chunking (and thus less CPU consumption overall) for higher memory pressure. Please note that in the case of PG deletion the chunking is steered by std::min of the this value and the value of osd_target_transaction_size.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`osd_memory_target`](../../../config/global/osd.md#SP_osd_memory_target)

**مثال:**

```bash
ceph config set osd osd_objectstore_ideal_list_max 64
ceph config get osd osd_objectstore_ideal_list_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_objectstore_ideal_list_max
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_objectstore_tracing

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_objectstore_tracing](../../../config/global/osd.md#SP_osd_objectstore_tracing) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_objectstore_tracing true
ceph config get osd osd_objectstore_tracing
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_objectstore_tracing
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_complaint_time

| | |
|---|---|
| نوع | Float · default `30` · **Advanced** |
| جدول | [osd.md#SP_osd_op_complaint_time](../../../config/global/osd.md#SP_osd_op_complaint_time) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_op_complaint_time 30
ceph config get osd osd_op_complaint_time
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_op_complaint_time
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_history_duration

| | |
|---|---|
| نوع | Uint · default `600` · **Advanced** |
| جدول | [osd.md#SP_osd_op_history_duration](../../../config/global/osd.md#SP_osd_op_history_duration) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_op_history_duration 600
ceph config get osd osd_op_history_duration
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `600`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_op_history_duration
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_history_size

| | |
|---|---|
| نوع | Uint · default `20` · **Advanced** |
| جدول | [osd.md#SP_osd_op_history_size](../../../config/global/osd.md#SP_osd_op_history_size) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_op_history_size 20
ceph config get osd osd_op_history_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `20`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_op_history_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_history_slow_op_size

| | |
|---|---|
| نوع | Uint · default `20` · **Advanced** |
| جدول | [osd.md#SP_osd_op_history_slow_op_size](../../../config/global/osd.md#SP_osd_op_history_slow_op_size) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_op_history_slow_op_size 20
ceph config get osd osd_op_history_slow_op_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `20`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_op_history_slow_op_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_history_slow_op_threshold

| | |
|---|---|
| نوع | Float · default `10` · **Advanced** |
| جدول | [osd.md#SP_osd_op_history_slow_op_threshold](../../../config/global/osd.md#SP_osd_op_history_slow_op_threshold) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_op_history_slow_op_threshold 10
ceph config get osd osd_op_history_slow_op_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_op_history_slow_op_threshold
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_log_threshold

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [osd.md#SP_osd_op_log_threshold](../../../config/global/osd.md#SP_osd_op_log_threshold) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_op_log_threshold 5
ceph config get osd osd_op_log_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_op_log_threshold
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_peering_op_priority

| | |
|---|---|
| نوع | Uint · default `255` · **Dev** |
| جدول | [osd.md#SP_osd_peering_op_priority](../../../config/global/osd.md#SP_osd_peering_op_priority) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_peering_op_priority 255
ceph config get osd osd_peering_op_priority
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`255`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_pg_delete_cost

| | |
|---|---|
| نوع | Size · default `1_M` · **Advanced** |
| جدول | [osd.md#SP_osd_pg_delete_cost](../../../config/global/osd.md#SP_osd_pg_delete_cost) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_pg_delete_cost 1_M
ceph config get osd osd_pg_delete_cost
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pg_delete_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pg_delete_priority

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [osd.md#SP_osd_pg_delete_priority](../../../config/global/osd.md#SP_osd_pg_delete_priority) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_pg_delete_priority 5
ceph config get osd osd_pg_delete_priority
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pg_delete_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pg_epoch_persisted_max_stale

| | |
|---|---|
| نوع | Uint · default `40` · **Advanced** |
| جدول | [osd.md#SP_osd_pg_epoch_persisted_max_stale](../../../config/global/osd.md#SP_osd_pg_epoch_persisted_max_stale) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_pg_epoch_persisted_max_stale 40
ceph config get osd osd_pg_epoch_persisted_max_stale
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `40`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pg_epoch_persisted_max_stale
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pg_log_dups_tracked

| | |
|---|---|
| نوع | Uint · default `3000` · **Dev** |
| جدول | [osd.md#SP_osd_pg_log_dups_tracked](../../../config/global/osd.md#SP_osd_pg_log_dups_tracked) |

**کارکرد:** How many versions back to track in order to detect duplicate ops; this is combined with both the regular pg log entries and additional minimal dup detection entries

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_pg_log_dups_tracked 3000
ceph config get osd osd_pg_log_dups_tracked
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`3000`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_pg_log_trim_max

| | |
|---|---|
| نوع | Uint · default `10000` · **Advanced** |
| جدول | [osd.md#SP_osd_pg_log_trim_max](../../../config/global/osd.md#SP_osd_pg_log_trim_max) |

**کارکرد:** Maximum number of entries to remove at once from the PG log

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_pg_log_trim_max 10000
ceph config get osd osd_pg_log_trim_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pg_log_trim_max
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pg_log_trim_min

| | |
|---|---|
| نوع | Uint · default `100` · **Dev** |
| جدول | [osd.md#SP_osd_pg_log_trim_min](../../../config/global/osd.md#SP_osd_pg_log_trim_min) |

**کارکرد:** Minimum number of log entries to trim at once. This lets us trim in larger batches rather than with each write.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_pg_log_trim_min 100
ceph config get osd osd_pg_log_trim_min
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`100`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_pg_max_concurrent_snap_trims

| | |
|---|---|
| نوع | Uint · default `2` · **Advanced** |
| جدول | [osd.md#SP_osd_pg_max_concurrent_snap_trims](../../../config/global/osd.md#SP_osd_pg_max_concurrent_snap_trims) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_pg_max_concurrent_snap_trims 2
ceph config get osd osd_pg_max_concurrent_snap_trims
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pg_max_concurrent_snap_trims
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pg_object_context_cache_count

| | |
|---|---|
| نوع | Int · default `64` · **Advanced** |
| جدول | [osd.md#SP_osd_pg_object_context_cache_count](../../../config/global/osd.md#SP_osd_pg_object_context_cache_count) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_pg_object_context_cache_count 64
ceph config get osd osd_pg_object_context_cache_count
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pg_object_context_cache_count
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pg_stat_report_interval_max_epochs

| | |
|---|---|
| نوع | Int · default `500` · **Advanced** |
| جدول | [osd.md#SP_osd_pg_stat_report_interval_max_epochs](../../../config/global/osd.md#SP_osd_pg_stat_report_interval_max_epochs) |

**کارکرد:** The maximum number of epochs allowed to pass before PG stats are collected.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_pg_stat_report_interval_max_epochs 500
ceph config get osd osd_pg_stat_report_interval_max_epochs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `500`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pg_stat_report_interval_max_epochs
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pg_stat_report_interval_max_seconds

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [osd.md#SP_osd_pg_stat_report_interval_max_seconds](../../../config/global/osd.md#SP_osd_pg_stat_report_interval_max_seconds) |

**کارکرد:** How often (in seconds) should PGs stats be collected.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_pg_stat_report_interval_max_seconds 5
ceph config get osd osd_pg_stat_report_interval_max_seconds
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pg_stat_report_interval_max_seconds
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_cache_max_evict_check_size

| | |
|---|---|
| نوع | Int · default `10` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_cache_max_evict_check_size](../../../config/global/osd.md#SP_osd_pool_default_cache_max_evict_check_size) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_pool_default_cache_max_evict_check_size 10
ceph config get osd osd_pool_default_cache_max_evict_check_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_cache_max_evict_check_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_cache_min_evict_age

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_cache_min_evict_age](../../../config/global/osd.md#SP_osd_pool_default_cache_min_evict_age) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_pool_default_cache_min_evict_age 64
ceph config get osd osd_pool_default_cache_min_evict_age
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_cache_min_evict_age
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_cache_min_flush_age

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_cache_min_flush_age](../../../config/global/osd.md#SP_osd_pool_default_cache_min_flush_age) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_pool_default_cache_min_flush_age 64
ceph config get osd osd_pool_default_cache_min_flush_age
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_cache_min_flush_age
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_cache_target_dirty_high_ratio

| | |
|---|---|
| نوع | Float · default `0.6` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_cache_target_dirty_high_ratio](../../../config/global/osd.md#SP_osd_pool_default_cache_target_dirty_high_ratio) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_pool_default_cache_target_dirty_high_ratio 0.6
ceph config get osd osd_pool_default_cache_target_dirty_high_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.6`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_cache_target_dirty_high_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_cache_target_dirty_ratio

| | |
|---|---|
| نوع | Float · default `0.4` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_cache_target_dirty_ratio](../../../config/global/osd.md#SP_osd_pool_default_cache_target_dirty_ratio) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_pool_default_cache_target_dirty_ratio 0.4
ceph config get osd osd_pool_default_cache_target_dirty_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.4`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_cache_target_dirty_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_cache_target_full_ratio

| | |
|---|---|
| نوع | Float · default `0.8` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_cache_target_full_ratio](../../../config/global/osd.md#SP_osd_pool_default_cache_target_full_ratio) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_pool_default_cache_target_full_ratio 0.8
ceph config get osd osd_pool_default_cache_target_full_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.8`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_cache_target_full_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_crush_rule

| | |
|---|---|
| نوع | Int · default `-1` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_crush_rule](../../../config/global/osd.md#SP_osd_pool_default_crush_rule) |

**کارکرد:** CRUSH rule for newly created pools

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_pool_default_crush_rule 128
ceph config get osd osd_pool_default_crush_rule
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `-1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_crush_rule
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_ec_fast_read

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_ec_fast_read](../../../config/global/osd.md#SP_osd_pool_default_ec_fast_read) |

**کارکرد:** set ec_fast_read for new erasure-coded pools

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_pool_default_ec_fast_read true
ceph config get osd osd_pool_default_ec_fast_read
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_ec_fast_read
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_erasure_code_profile

| | |
|---|---|
| نوع | Str · default `plugin=isa technique=reed_sol_van k=2 m=2` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_erasure_code_profile](../../../config/global/osd.md#SP_osd_pool_default_erasure_code_profile) |

**کارکرد:** Default EC profile for new erasure-coded pools

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_pool_default_erasure_code_profile "plugin=isa technique=reed_sol_van k=2 m=2"
ceph config get osd osd_pool_default_erasure_code_profile
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `plugin=isa technique=reed_sol_van k=2 m=2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_erasure_code_profile
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_flag_bulk

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_flag_bulk](../../../config/global/osd.md#SP_osd_pool_default_flag_bulk) |

**کارکرد:** Set the bulk flag on new pools

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_pool_default_flag_bulk true
ceph config get osd osd_pool_default_flag_bulk
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_flag_bulk
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_flag_ec_optimizations

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_flag_ec_optimizations](../../../config/global/osd.md#SP_osd_pool_default_flag_ec_optimizations) |

**کارکرد:** Control whether to create new erasure coded pools with EC optimizations turned on by default.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_pool_default_flag_ec_optimizations true
ceph config get osd osd_pool_default_flag_ec_optimizations
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_flag_ec_optimizations
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_flag_hashpspool

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_flag_hashpspool](../../../config/global/osd.md#SP_osd_pool_default_flag_hashpspool) |

**کارکرد:** Set hashpspool (better hashing scheme) flag on new pools

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_pool_default_flag_hashpspool false
ceph config get osd osd_pool_default_flag_hashpspool
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_flag_hashpspool
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_flag_nodelete

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_flag_nodelete](../../../config/global/osd.md#SP_osd_pool_default_flag_nodelete) |

**کارکرد:** Set the nodelete flag on new pools

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_pool_default_flag_nodelete true
ceph config get osd osd_pool_default_flag_nodelete
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_flag_nodelete
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_flag_nopgchange

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_flag_nopgchange](../../../config/global/osd.md#SP_osd_pool_default_flag_nopgchange) |

**کارکرد:** Set the nopgchange flag on new pools

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_pool_default_flag_nopgchange true
ceph config get osd osd_pool_default_flag_nopgchange
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_flag_nopgchange
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_flag_nosizechange

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_flag_nosizechange](../../../config/global/osd.md#SP_osd_pool_default_flag_nosizechange) |

**کارکرد:** Set the nosizechange flag on new pools

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_pool_default_flag_nosizechange true
ceph config get osd osd_pool_default_flag_nosizechange
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_flag_nosizechange
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_flags

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [osd.md#SP_osd_pool_default_flags](../../../config/global/osd.md#SP_osd_pool_default_flags) |

**کارکرد:** The (integer) flags to set on new pools

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_pool_default_flags 64
ceph config get osd osd_pool_default_flags
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_pool_default_hit_set_bloom_fpp

| | |
|---|---|
| نوع | Float · default `0.05` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_hit_set_bloom_fpp](../../../config/global/osd.md#SP_osd_pool_default_hit_set_bloom_fpp) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`osd_tier_default_cache_hit_set_type`](../../../config/global/osd.md#SP_osd_tier_default_cache_hit_set_type)

**مثال:**

```bash
ceph config set osd osd_pool_default_hit_set_bloom_fpp 0.05
ceph config get osd osd_pool_default_hit_set_bloom_fpp
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.05`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_hit_set_bloom_fpp
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_min_size

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_min_size](../../../config/global/osd.md#SP_osd_pool_default_min_size) |

**کارکرد:** The minimal number of copies allowed to write to a degraded pool for new replicated pools 0 means no specific default; ceph will use size-size/2

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**گزینه‌های مرتبط:**

- [`osd_pool_default_size`](../../../config/global/osd.md#SP_osd_pool_default_size)

**مثال:**

```bash
ceph config set osd osd_pool_default_min_size 64
ceph config get osd osd_pool_default_min_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `255`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_min_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_pg_autoscale_mode

| | |
|---|---|
| نوع | Str · enum: ["off", "warn", "on"] · default `on` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_pg_autoscale_mode](../../../config/global/osd.md#SP_osd_pool_default_pg_autoscale_mode) |

**کارکرد:** Default PG autoscaling behavior for new pools When 'on', the autoscaler assigns 1 pg to new pools unless the user specifies a value.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_pool_default_pg_autoscale_mode on
ceph config get osd osd_pool_default_pg_autoscale_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `on`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_pg_autoscale_mode
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_pg_num

| | |
|---|---|
| نوع | Uint · default `32` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_pg_num](../../../config/global/osd.md#SP_osd_pool_default_pg_num) |

**کارکرد:** number of PGs for new pools With default value of `osd_pool_default_pg_autoscale_mode` being `on` the number of PGs for new pools will start out with 1 pg, unless the user specifies the pg_num.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`osd_pool_default_pg_autoscale_mode`](../../../config/global/osd.md#SP_osd_pool_default_pg_autoscale_mode)

**مثال:**

```bash
ceph config set osd osd_pool_default_pg_num 32
ceph config get osd osd_pool_default_pg_num
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `32`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_pg_num
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_pgp_num

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_pgp_num](../../../config/global/osd.md#SP_osd_pool_default_pgp_num) |

**کارکرد:** number of PGs for placement purposes (0 to match pg_num)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_pool_default_pgp_num 64
ceph config get osd osd_pool_default_pgp_num
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_pgp_num
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_read_lease_ratio

| | |
|---|---|
| نوع | Float · default `0.8` · **Dev** |
| جدول | [osd.md#SP_osd_pool_default_read_lease_ratio](../../../config/global/osd.md#SP_osd_pool_default_read_lease_ratio) |

**کارکرد:** Default read_lease_ratio for a pool, as a multiple of osd_heartbeat_grace This should be <= 1.0 so that the read lease will have expired by the time we decide to mark a peer OSD down.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**گزینه‌های مرتبط:**

- [`osd_heartbeat_grace`](../../../config/global/osd.md#SP_osd_heartbeat_grace)

**مثال:**

```bash
ceph config set osd osd_pool_default_read_lease_ratio 0.8
ceph config get osd osd_pool_default_read_lease_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.8`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_pool_default_read_ratio

| | |
|---|---|
| نوع | Uint · default `70` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_read_ratio](../../../config/global/osd.md#SP_osd_pool_default_read_ratio) |

**کارکرد:** Default read ratio (the percent of read IOs out of all IOs) for a pool. Default read ratio (the percent of read IOs out of all IOs) for a pool. applicable to replicated pools only. This value is used to improve read balancing when OSDs have different weights.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_pool_default_read_ratio 70
ceph config get osd osd_pool_default_read_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `70`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_read_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_size

| | |
|---|---|
| نوع | Uint · default `3` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_size](../../../config/global/osd.md#SP_osd_pool_default_size) |

**کارکرد:** the number of copies of an object for new replicated pools

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_pool_default_size 3
ceph config get osd osd_pool_default_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `10`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_default_type

| | |
|---|---|
| نوع | Str · enum: ["replicated", "erasure"] · default `replicated` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_type](../../../config/global/osd.md#SP_osd_pool_default_type) |

**کارکرد:** Default data protection strategy type when creating a new pool

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_pool_default_type replicated
ceph config get osd osd_pool_default_type
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `replicated`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pool_default_type
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_use_gmt_hitset

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [osd.md#SP_osd_pool_use_gmt_hitset](../../../config/global/osd.md#SP_osd_pool_use_gmt_hitset) |

**کارکرد:** use UTC for hitset timestamps This setting only exists for compatibility with hammer (and older) clusters.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_pool_use_gmt_hitset false
ceph config get osd osd_pool_use_gmt_hitset
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_recovery_cost

| | |
|---|---|
| نوع | Size · default `20_M` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_cost](../../../config/global/osd.md#SP_osd_recovery_cost) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_recovery_cost 20_M
ceph config get osd osd_recovery_cost
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `20_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_op_priority

| | |
|---|---|
| نوع | Uint · default `3` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_op_priority](../../../config/global/osd.md#SP_osd_recovery_op_priority) |

**کارکرد:** Priority to use for recovery operations if not specified for the pool

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_recovery_op_priority 3
ceph config get osd osd_recovery_op_priority
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_op_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_op_warn_multiple

| | |
|---|---|
| نوع | Uint · default `16` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_op_warn_multiple](../../../config/global/osd.md#SP_osd_recovery_op_warn_multiple) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_recovery_op_warn_multiple 16
ceph config get osd osd_recovery_op_warn_multiple
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `16`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_op_warn_multiple
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_priority

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_priority](../../../config/global/osd.md#SP_osd_recovery_priority) |

**کارکرد:** Priority of recovery in the work queue Not related to a pool's recovery_priority

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_recovery_priority 5
ceph config get osd osd_recovery_priority
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_requested_scrub_priority

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [osd.md#SP_osd_requested_scrub_priority](../../../config/global/osd.md#SP_osd_requested_scrub_priority) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_requested_scrub_priority 5
ceph config get osd osd_requested_scrub_priority
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_requested_scrub_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_rollback_to_cluster_snap

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [osd.md#SP_osd_rollback_to_cluster_snap](../../../config/global/osd.md#SP_osd_rollback_to_cluster_snap) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_rollback_to_cluster_snap "example"
ceph config get osd osd_rollback_to_cluster_snap
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_rollback_to_cluster_snap
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_cost

| | |
|---|---|
| نوع | Size · default `50_M` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_cost](../../../config/global/osd.md#SP_osd_scrub_cost) |

**کارکرد:** Cost for scrub operations in work queue

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_scrub_cost 50_M
ceph config get osd osd_scrub_cost
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `50_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_event_cost

| | |
|---|---|
| نوع | Size · default `4_K` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_event_cost](../../../config/global/osd.md#SP_osd_scrub_event_cost) |

**کارکرد:** Cost for each scrub operation, used when osd_op_queue=mclock_scheduler

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_scrub_event_cost 4_K
ceph config get osd osd_scrub_event_cost
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `4_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_event_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_priority

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_priority](../../../config/global/osd.md#SP_osd_scrub_priority) |

**کارکرد:** Priority for scrub operations in work queue

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_scrub_priority 5
ceph config get osd osd_scrub_priority
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_shutdown_pgref_assert

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_shutdown_pgref_assert](../../../config/global/osd.md#SP_osd_shutdown_pgref_assert) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_shutdown_pgref_assert true
ceph config get osd osd_shutdown_pgref_assert
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_shutdown_pgref_assert
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_skip_check_past_interval_bounds

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_skip_check_past_interval_bounds](../../../config/global/osd.md#SP_osd_skip_check_past_interval_bounds) |

**کارکرد:** See https://tracker.ceph.com/issues/64002

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_skip_check_past_interval_bounds true
ceph config get osd osd_skip_check_past_interval_bounds
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_snap_trim_cost

| | |
|---|---|
| نوع | Size · default `1_M` · **Advanced** |
| جدول | [osd.md#SP_osd_snap_trim_cost](../../../config/global/osd.md#SP_osd_snap_trim_cost) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_snap_trim_cost 1_M
ceph config get osd osd_snap_trim_cost
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_snap_trim_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_snap_trim_priority

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [osd.md#SP_osd_snap_trim_priority](../../../config/global/osd.md#SP_osd_snap_trim_priority) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_snap_trim_priority 5
ceph config get osd osd_snap_trim_priority
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_snap_trim_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_target_pg_log_entries_per_osd

| | |
|---|---|
| نوع | Uint · default `300000` · **Dev** |
| جدول | [osd.md#SP_osd_target_pg_log_entries_per_osd](../../../config/global/osd.md#SP_osd_target_pg_log_entries_per_osd) |

**کارکرد:** Target number of PG entries total on an OSD, limited per PG by the min and max options below

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_target_pg_log_entries_per_osd 300000
ceph config get osd osd_target_pg_log_entries_per_osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`300000`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_target_transaction_size

| | |
|---|---|
| نوع | Uint · default `30` · **Advanced** |
| جدول | [osd.md#SP_osd_target_transaction_size](../../../config/global/osd.md#SP_osd_target_transaction_size) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_target_transaction_size 30
ceph config get osd osd_target_transaction_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_target_transaction_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_default_cache_hit_set_count

| | |
|---|---|
| نوع | Uint · default `4` · **Advanced** |
| جدول | [osd.md#SP_osd_tier_default_cache_hit_set_count](../../../config/global/osd.md#SP_osd_tier_default_cache_hit_set_count) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_tier_default_cache_hit_set_count 4
ceph config get osd osd_tier_default_cache_hit_set_count
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `4`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_tier_default_cache_hit_set_count
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_default_cache_hit_set_grade_decay_rate

| | |
|---|---|
| نوع | Uint · default `20` · **Advanced** |
| جدول | [osd.md#SP_osd_tier_default_cache_hit_set_grade_decay_rate](../../../config/global/osd.md#SP_osd_tier_default_cache_hit_set_grade_decay_rate) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_tier_default_cache_hit_set_grade_decay_rate 20
ceph config get osd osd_tier_default_cache_hit_set_grade_decay_rate
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `20`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_tier_default_cache_hit_set_grade_decay_rate
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_default_cache_hit_set_period

| | |
|---|---|
| نوع | Uint · default `1200` · **Advanced** |
| جدول | [osd.md#SP_osd_tier_default_cache_hit_set_period](../../../config/global/osd.md#SP_osd_tier_default_cache_hit_set_period) |

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_tier_default_cache_hit_set_period 1200
ceph config get osd osd_tier_default_cache_hit_set_period
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1200`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_tier_default_cache_hit_set_period
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_default_cache_hit_set_search_last_n

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [osd.md#SP_osd_tier_default_cache_hit_set_search_last_n](../../../config/global/osd.md#SP_osd_tier_default_cache_hit_set_search_last_n) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_tier_default_cache_hit_set_search_last_n 1
ceph config get osd osd_tier_default_cache_hit_set_search_last_n
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_tier_default_cache_hit_set_search_last_n
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_default_cache_hit_set_type

| | |
|---|---|
| نوع | Str · enum: ["bloom", "explicit_hash", "explicit_object"] · default `bloom` · **Advanced** |
| جدول | [osd.md#SP_osd_tier_default_cache_hit_set_type](../../../config/global/osd.md#SP_osd_tier_default_cache_hit_set_type) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_tier_default_cache_hit_set_type bloom
ceph config get osd osd_tier_default_cache_hit_set_type
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `bloom`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_tier_default_cache_hit_set_type
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_default_cache_min_read_recency_for_promote

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [osd.md#SP_osd_tier_default_cache_min_read_recency_for_promote](../../../config/global/osd.md#SP_osd_tier_default_cache_min_read_recency_for_promote) |

**کارکرد:** Number of recent HitSets the object must appear in to be promoted (on read)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_tier_default_cache_min_read_recency_for_promote 1
ceph config get osd osd_tier_default_cache_min_read_recency_for_promote
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_tier_default_cache_min_read_recency_for_promote
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_default_cache_min_write_recency_for_promote

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [osd.md#SP_osd_tier_default_cache_min_write_recency_for_promote](../../../config/global/osd.md#SP_osd_tier_default_cache_min_write_recency_for_promote) |

**کارکرد:** Number of recent HitSets the object must appear in to be promoted (on write)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_tier_default_cache_min_write_recency_for_promote 1
ceph config get osd osd_tier_default_cache_min_write_recency_for_promote
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_tier_default_cache_min_write_recency_for_promote
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_default_cache_mode

| | |
|---|---|
| نوع | Str · enum: ["none", "writeback", "forward", "readonly", "readforward", "readproxy", "proxy"] · default `writeback` · **Advanced** |
| جدول | [osd.md#SP_osd_tier_default_cache_mode](../../../config/global/osd.md#SP_osd_tier_default_cache_mode) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_tier_default_cache_mode writeback
ceph config get osd osd_tier_default_cache_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `writeback`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_tier_default_cache_mode
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_promote_max_bytes_sec

| | |
|---|---|
| نوع | Size · default `5_M` · **Advanced** |
| جدول | [osd.md#SP_osd_tier_promote_max_bytes_sec](../../../config/global/osd.md#SP_osd_tier_promote_max_bytes_sec) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_tier_promote_max_bytes_sec 5_M
ceph config get osd osd_tier_promote_max_bytes_sec
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_tier_promote_max_bytes_sec
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tier_promote_max_objects_sec

| | |
|---|---|
| نوع | Uint · default `25` · **Advanced** |
| جدول | [osd.md#SP_osd_tier_promote_max_objects_sec](../../../config/global/osd.md#SP_osd_tier_promote_max_objects_sec) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_tier_promote_max_objects_sec 25
ceph config get osd osd_tier_promote_max_objects_sec
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `25`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_tier_promote_max_objects_sec
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_tracing

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_tracing](../../../config/global/osd.md#SP_osd_tracing) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_tracing true
ceph config get osd osd_tracing
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_tracing
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_use_stale_snap

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_use_stale_snap](../../../config/global/osd.md#SP_osd_use_stale_snap) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_use_stale_snap true
ceph config get osd osd_use_stale_snap
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_use_stale_snap
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← نمای کلی](../OVERVIEW.md)
