# پیکربندی MON — مرجع سریع تنظیم

هر **156** گزینه با مدل تنظیم و راهنمای یک‌خطی.

[← نمای کلی](../OVERVIEW.md)

| گزینه | پیش‌فرض | مدل | پاسخ سریع | موضوع |
|--------|---------|-------|--------------|-------|
| [`mds_beacon_mon_down_grace`](cross-daemon/mds-related.md#mds_beacon_mon_down_grace) | `1_min` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [MDS-related settings](cross-daemon/mds-related.md) |
| [`enable_availability_tracking`](runtime/general.md#enable_availability_tracking) | `False` | Policy | مطابق سیاست امنیت و سازگاری | [General monitor](runtime/general.md) |
| [`mon_accept_timeout_factor`](quorum/quorum-paxos.md#mon_accept_timeout_factor) | `2` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Quorum & Paxos](quorum/quorum-paxos.md) |
| [`mon_allow_pool_size_one`](pg-pool/pg-pool.md#mon_allow_pool_size_one) | `False` | Policy | مطابق سیاست امنیت و سازگاری | [PG & pool health](pg-pool/pg-pool.md) |
| [`mon_auth_validate_all_caps`](runtime/auth.md#mon_auth_validate_all_caps) | `True` | Policy | مطابق سیاست امنیت و سازگاری | [Auth & caps](runtime/auth.md) |
| [`mon_backup_cleanup_interval`](logging/backup.md#mon_backup_cleanup_interval) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Monitor backup](logging/backup.md) |
| [`mon_backup_interval`](logging/backup.md#mon_backup_interval) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Monitor backup](logging/backup.md) |
| [`mon_backup_keep_daily`](logging/backup.md#mon_backup_keep_daily) | `7` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Monitor backup](logging/backup.md) |
| [`mon_backup_keep_hourly`](logging/backup.md#mon_backup_keep_hourly) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Monitor backup](logging/backup.md) |
| [`mon_backup_keep_last`](logging/backup.md#mon_backup_keep_last) | `6` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Monitor backup](logging/backup.md) |
| [`mon_backup_min_avail`](logging/backup.md#mon_backup_min_avail) | `10` | Performance | در محدوده مستند بمانید | [Monitor backup](logging/backup.md) |
| [`mon_backup_path`](logging/backup.md#mon_backup_path) | `/var/backups/ceph/mon/$cluster-$id` | Capacity | مطابق چیدمان filesystem و برنامه ظرفیت | [Monitor backup](logging/backup.md) |
| [`mon_clean_pg_upmaps_per_chunk`](pg-pool/pg-pool.md#mon_clean_pg_upmaps_per_chunk) | `256` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [PG & pool health](pg-pool/pg-pool.md) |
| [`mon_clock_drift_allowed`](runtime/general.md#mon_clock_drift_allowed) | `0.05` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_clock_drift_warn_backoff`](runtime/general.md#mon_clock_drift_warn_backoff) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_cluster_log_file`](logging/logging.md#mon_cluster_log_file) | `default=/var/log/ceph/$cluster.$channel.log cluster=/var/log/ceph/$cluster.log` | Capacity | مطابق چیدمان filesystem و برنامه ظرفیت | [Cluster logging](logging/logging.md) |
| [`mon_cluster_log_level`](logging/logging.md#mon_cluster_log_level) | `debug` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cluster logging](logging/logging.md) |
| [`mon_cluster_log_to_file`](logging/logging.md#mon_cluster_log_to_file) | `True` | Capacity | مطابق چیدمان filesystem و برنامه ظرفیت | [Cluster logging](logging/logging.md) |
| [`mon_cluster_log_to_graylog`](logging/logging.md#mon_cluster_log_to_graylog) | `false` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cluster logging](logging/logging.md) |
| [`mon_cluster_log_to_graylog_host`](logging/logging.md#mon_cluster_log_to_graylog_host) | `127.0.0.1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cluster logging](logging/logging.md) |
| [`mon_cluster_log_to_graylog_port`](logging/logging.md#mon_cluster_log_to_graylog_port) | `12201` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cluster logging](logging/logging.md) |
| [`mon_cluster_log_to_journald`](logging/logging.md#mon_cluster_log_to_journald) | `false` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cluster logging](logging/logging.md) |
| [`mon_cluster_log_to_stderr`](logging/logging.md#mon_cluster_log_to_stderr) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Cluster logging](logging/logging.md) |
| [`mon_cluster_log_to_syslog`](logging/logging.md#mon_cluster_log_to_syslog) | `default=false` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cluster logging](logging/logging.md) |
| [`mon_cluster_log_to_syslog_facility`](logging/logging.md#mon_cluster_log_to_syslog_facility) | `daemon` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cluster logging](logging/logging.md) |
| [`mon_compact_on_bootstrap`](runtime/general.md#mon_compact_on_bootstrap) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General monitor](runtime/general.md) |
| [`mon_compact_on_start`](runtime/general.md#mon_compact_on_start) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General monitor](runtime/general.md) |
| [`mon_compact_on_trim`](runtime/general.md#mon_compact_on_trim) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General monitor](runtime/general.md) |
| [`mon_con_tracker_persist_interval`](runtime/intervals.md#mon_con_tracker_persist_interval) | `10` | Performance | در محدوده مستند بمانید | [Intervals & timeouts](runtime/intervals.md) |
| [`mon_con_tracker_score_halflife`](runtime/general.md#mon_con_tracker_score_halflife) | `43200` | Performance | در محدوده مستند بمانید | [General monitor](runtime/general.md) |
| [`mon_cpu_threads`](runtime/general.md#mon_cpu_threads) | `4` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_crush_min_required_version`](runtime/general.md#mon_crush_min_required_version) | `hammer` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_daemon_bytes`](runtime/general.md#mon_daemon_bytes) | `400_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_data`](runtime/paths.md#mon_data) | `/var/lib/ceph/mon/$cluster-$id` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Paths & storage](runtime/paths.md) |
| [`mon_data_avail_crit`](runtime/paths.md#mon_data_avail_crit) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Paths & storage](runtime/paths.md) |
| [`mon_data_avail_warn`](runtime/paths.md#mon_data_avail_warn) | `30` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Paths & storage](runtime/paths.md) |
| [`mon_data_size_warn`](runtime/paths.md#mon_data_size_warn) | `15_G` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Paths & storage](runtime/paths.md) |
| [`mon_down_added_grace`](runtime/general.md#mon_down_added_grace) | `3_min` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_down_mkfs_grace`](runtime/general.md#mon_down_mkfs_grace) | `1_min` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_down_uptime_grace`](runtime/general.md#mon_down_uptime_grace) | `1_min` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_election_default_strategy`](quorum/quorum-paxos.md#mon_election_default_strategy) | `1` | Performance | در محدوده مستند بمانید | [Quorum & Paxos](quorum/quorum-paxos.md) |
| [`mon_election_timeout`](quorum/quorum-paxos.md#mon_election_timeout) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Quorum & Paxos](quorum/quorum-paxos.md) |
| [`mon_elector_ignore_propose_margin`](runtime/general.md#mon_elector_ignore_propose_margin) | `0.0005` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_elector_ping_divisor`](runtime/general.md#mon_elector_ping_divisor) | `2` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_elector_ping_timeout`](runtime/intervals.md#mon_elector_ping_timeout) | `2` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & timeouts](runtime/intervals.md) |
| [`mon_enable_op_tracker`](runtime/general.md#mon_enable_op_tracker) | `True` | Policy | مطابق سیاست امنیت و سازگاری | [General monitor](runtime/general.md) |
| [`mon_fsmap_prune_threshold`](runtime/general.md#mon_fsmap_prune_threshold) | `300` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_health_detail_to_clog`](logging/logging.md#mon_health_detail_to_clog) | `True` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [Cluster logging](logging/logging.md) |
| [`mon_health_log_update_period`](logging/logging.md#mon_health_log_update_period) | `5` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [Cluster logging](logging/logging.md) |
| [`mon_health_max_detail`](runtime/general.md#mon_health_max_detail) | `50` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_health_to_clog`](logging/logging.md#mon_health_to_clog) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Cluster logging](logging/logging.md) |
| [`mon_health_to_clog_interval`](logging/logging.md#mon_health_to_clog_interval) | `10_min` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cluster logging](logging/logging.md) |
| [`mon_health_to_clog_tick_interval`](logging/logging.md#mon_health_to_clog_tick_interval) | `1_min` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [Cluster logging](logging/logging.md) |
| [`mon_lease`](runtime/general.md#mon_lease) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_lease_ack_timeout_factor`](runtime/intervals.md#mon_lease_ack_timeout_factor) | `2` | Performance | در محدوده مستند بمانید | [Intervals & timeouts](runtime/intervals.md) |
| [`mon_lease_renew_interval_factor`](runtime/intervals.md#mon_lease_renew_interval_factor) | `0.6` | Performance | در محدوده مستند بمانید | [Intervals & timeouts](runtime/intervals.md) |
| [`mon_log_full_interval`](logging/logging.md#mon_log_full_interval) | `50` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cluster logging](logging/logging.md) |
| [`mon_log_max`](logging/logging.md#mon_log_max) | `10000` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cluster logging](logging/logging.md) |
| [`mon_log_max_summary`](logging/logging.md#mon_log_max_summary) | `50` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cluster logging](logging/logging.md) |
| [`mon_max_log_entries_per_event`](logging/logging.md#mon_max_log_entries_per_event) | `4096` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cluster logging](logging/logging.md) |
| [`mon_max_pool_pg_num`](pg-pool/pg-pool.md#mon_max_pool_pg_num) | `64_K` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [PG & pool health](pg-pool/pg-pool.md) |
| [`mon_mds_blocklist_interval`](runtime/intervals.md#mon_mds_blocklist_interval) | `1_day` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [Intervals & timeouts](runtime/intervals.md) |
| [`mon_mds_force_trim_to`](runtime/general.md#mon_mds_force_trim_to) | `0` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [General monitor](runtime/general.md) |
| [`mon_mds_skip_sanity`](runtime/general.md#mon_mds_skip_sanity) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General monitor](runtime/general.md) |
| [`mon_memory_autotune`](runtime/general.md#mon_memory_autotune) | `True` | Policy | مطابق سیاست امنیت و سازگاری | [General monitor](runtime/general.md) |
| [`mon_memory_target`](runtime/general.md#mon_memory_target) | `2_G` | Policy | مطابق سیاست امنیت و سازگاری | [General monitor](runtime/general.md) |
| [`mon_mgr_beacon_grace`](cross-daemon/mgr-related.md#mon_mgr_beacon_grace) | `30` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [MGR-related settings](cross-daemon/mgr-related.md) |
| [`mon_mgr_blocklist_interval`](cross-daemon/mgr-related.md#mon_mgr_blocklist_interval) | `1_day` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [MGR-related settings](cross-daemon/mgr-related.md) |
| [`mon_mgr_digest_period`](cross-daemon/mgr-related.md#mon_mgr_digest_period) | `5` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [MGR-related settings](cross-daemon/mgr-related.md) |
| [`mon_mgr_inactive_grace`](cross-daemon/mgr-related.md#mon_mgr_inactive_grace) | `1_min` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [MGR-related settings](cross-daemon/mgr-related.md) |
| [`mon_mgr_mkfs_grace`](cross-daemon/mgr-related.md#mon_mgr_mkfs_grace) | `2_min` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [MGR-related settings](cross-daemon/mgr-related.md) |
| [`mon_mgr_proxy_client_bytes_ratio`](cross-daemon/mgr-related.md#mon_mgr_proxy_client_bytes_ratio) | `0.3` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [MGR-related settings](cross-daemon/mgr-related.md) |
| [`mon_netsplit_grace_period`](runtime/intervals.md#mon_netsplit_grace_period) | `9` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & timeouts](runtime/intervals.md) |
| [`mon_nvmeofgw_beacon_grace`](runtime/general.md#mon_nvmeofgw_beacon_grace) | `7` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_nvmeofgw_beacons_till_ack`](runtime/general.md#mon_nvmeofgw_beacons_till_ack) | `15` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_nvmeofgw_delete_grace`](runtime/general.md#mon_nvmeofgw_delete_grace) | `15_min` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_nvmeofgw_failback_delay`](runtime/intervals.md#mon_nvmeofgw_failback_delay) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & timeouts](runtime/intervals.md) |
| [`mon_nvmeofgw_set_group_id_retry`](runtime/general.md#mon_nvmeofgw_set_group_id_retry) | `1000` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_nvmeofgw_skip_failovers_interval`](runtime/intervals.md#mon_nvmeofgw_skip_failovers_interval) | `16` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & timeouts](runtime/intervals.md) |
| [`mon_nvmeofgw_wrong_map_ignore_sec`](runtime/general.md#mon_nvmeofgw_wrong_map_ignore_sec) | `15` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_op_complaint_time`](runtime/general.md#mon_op_complaint_time) | `30` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_op_history_duration`](runtime/general.md#mon_op_history_duration) | `10_min` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_op_history_size`](runtime/general.md#mon_op_history_size) | `20` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_op_history_slow_op_size`](runtime/general.md#mon_op_history_slow_op_size) | `20` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_op_history_slow_op_threshold`](runtime/general.md#mon_op_history_slow_op_threshold) | `10` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_op_log_threshold`](logging/logging.md#mon_op_log_threshold) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Cluster logging](logging/logging.md) |
| [`mon_osd_adjust_down_out_interval`](cross-daemon/osd-related.md#mon_osd_adjust_down_out_interval) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_adjust_heartbeat_grace`](cross-daemon/osd-related.md#mon_osd_adjust_heartbeat_grace) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_auto_mark_auto_out_in`](cross-daemon/osd-related.md#mon_osd_auto_mark_auto_out_in) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_auto_mark_in`](cross-daemon/osd-related.md#mon_osd_auto_mark_in) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_auto_mark_new_in`](cross-daemon/osd-related.md#mon_osd_auto_mark_new_in) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_blocklist_default_expire`](cross-daemon/osd-related.md#mon_osd_blocklist_default_expire) | `1_hr` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_cache_size`](cross-daemon/osd-related.md#mon_osd_cache_size) | `500` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_cache_size_min`](cross-daemon/osd-related.md#mon_osd_cache_size_min) | `128_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_crush_smoke_test`](cross-daemon/osd-related.md#mon_osd_crush_smoke_test) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_destroyed_out_interval`](cross-daemon/osd-related.md#mon_osd_destroyed_out_interval) | `10_min` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_down_out_interval`](cross-daemon/osd-related.md#mon_osd_down_out_interval) | `10_min` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_down_out_subtree_limit`](cross-daemon/osd-related.md#mon_osd_down_out_subtree_limit) | `rack` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_laggy_halflife`](cross-daemon/osd-related.md#mon_osd_laggy_halflife) | `1_hr` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_laggy_max_interval`](cross-daemon/osd-related.md#mon_osd_laggy_max_interval) | `5_min` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_laggy_weight`](cross-daemon/osd-related.md#mon_osd_laggy_weight) | `0.3` | Performance | در محدوده مستند بمانید | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_mapping_pgs_per_chunk`](cross-daemon/osd-related.md#mon_osd_mapping_pgs_per_chunk) | `4096` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_max_initial_pgs`](cross-daemon/osd-related.md#mon_osd_max_initial_pgs) | `1024` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_min_in_ratio`](cross-daemon/osd-related.md#mon_osd_min_in_ratio) | `0.75` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_min_up_ratio`](cross-daemon/osd-related.md#mon_osd_min_up_ratio) | `0.3` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_prime_pg_temp`](pg-pool/pg-pool.md#mon_osd_prime_pg_temp) | `True` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [PG & pool health](pg-pool/pg-pool.md) |
| [`mon_osd_prime_pg_temp_max_estimate`](pg-pool/pg-pool.md#mon_osd_prime_pg_temp_max_estimate) | `0.25` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [PG & pool health](pg-pool/pg-pool.md) |
| [`mon_osd_prime_pg_temp_max_time`](pg-pool/pg-pool.md#mon_osd_prime_pg_temp_max_time) | `0.5` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [PG & pool health](pg-pool/pg-pool.md) |
| [`mon_osd_warn_num_repaired`](cross-daemon/osd-related.md#mon_osd_warn_num_repaired) | `10` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osd_warn_op_age`](cross-daemon/osd-related.md#mon_osd_warn_op_age) | `32` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osdmap_full_prune_enabled`](cross-daemon/osd-related.md#mon_osdmap_full_prune_enabled) | `True` | Policy | مطابق سیاست امنیت و سازگاری | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osdmap_full_prune_interval`](cross-daemon/osd-related.md#mon_osdmap_full_prune_interval) | `10` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osdmap_full_prune_min`](cross-daemon/osd-related.md#mon_osdmap_full_prune_min) | `10000` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_osdmap_full_prune_txsize`](cross-daemon/osd-related.md#mon_osdmap_full_prune_txsize) | `100` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_rocksdb_options`](runtime/general.md#mon_rocksdb_options) | `write_buffer_size=33554432,compression=kNoCompression,level_compaction_dynamic_level_bytes=true` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`mon_session_timeout`](runtime/intervals.md#mon_session_timeout) | `5_min` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & timeouts](runtime/intervals.md) |
| [`mon_smart_report_timeout`](runtime/intervals.md#mon_smart_report_timeout) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & timeouts](runtime/intervals.md) |
| [`mon_stretch_cluster_recovery_ratio`](runtime/general.md#mon_stretch_cluster_recovery_ratio) | `0.6` | Performance | در محدوده مستند بمانید | [General monitor](runtime/general.md) |
| [`mon_stretch_max_bucket_weight_delta`](runtime/general.md#mon_stretch_max_bucket_weight_delta) | `0.1` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [General monitor](runtime/general.md) |
| [`mon_stretch_pool_min_size`](pg-pool/pg-pool.md#mon_stretch_pool_min_size) | `2` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [PG & pool health](pg-pool/pg-pool.md) |
| [`mon_stretch_pool_size`](pg-pool/pg-pool.md#mon_stretch_pool_size) | `4` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [PG & pool health](pg-pool/pg-pool.md) |
| [`mon_stretch_recovery_min_wait`](runtime/general.md#mon_stretch_recovery_min_wait) | `15` | Performance | در محدوده مستند بمانید | [General monitor](runtime/general.md) |
| [`mon_subscribe_interval`](runtime/intervals.md#mon_subscribe_interval) | `1_day` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [Intervals & timeouts](runtime/intervals.md) |
| [`mon_tick_interval`](runtime/intervals.md#mon_tick_interval) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & timeouts](runtime/intervals.md) |
| [`mon_timecheck_interval`](runtime/intervals.md#mon_timecheck_interval) | `5_min` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & timeouts](runtime/intervals.md) |
| [`mon_timecheck_skew_interval`](runtime/intervals.md#mon_timecheck_skew_interval) | `30` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & timeouts](runtime/intervals.md) |
| [`mon_use_min_delay_socket`](runtime/intervals.md#mon_use_min_delay_socket) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [Intervals & timeouts](runtime/intervals.md) |
| [`mon_warn_older_version_delay`](runtime/intervals.md#mon_warn_older_version_delay) | `7_day` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & timeouts](runtime/intervals.md) |
| [`mon_warn_on_cache_pools_without_hit_sets`](pg-pool/pg-pool.md#mon_warn_on_cache_pools_without_hit_sets) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [PG & pool health](pg-pool/pg-pool.md) |
| [`mon_warn_on_colocated_monitors`](runtime/general.md#mon_warn_on_colocated_monitors) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General monitor](runtime/general.md) |
| [`mon_warn_on_crush_straw_calc_version_zero`](runtime/general.md#mon_warn_on_crush_straw_calc_version_zero) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General monitor](runtime/general.md) |
| [`mon_warn_on_degraded_stretch_mode`](runtime/general.md#mon_warn_on_degraded_stretch_mode) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General monitor](runtime/general.md) |
| [`mon_warn_on_filestore_osds`](cross-daemon/osd-related.md#mon_warn_on_filestore_osds) | `True` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_warn_on_legacy_crush_tunables`](runtime/general.md#mon_warn_on_legacy_crush_tunables) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General monitor](runtime/general.md) |
| [`mon_warn_on_older_version`](runtime/general.md#mon_warn_on_older_version) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [General monitor](runtime/general.md) |
| [`mon_warn_on_osd_down_out_interval_zero`](cross-daemon/osd-related.md#mon_warn_on_osd_down_out_interval_zero) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [OSD-related settings](cross-daemon/osd-related.md) |
| [`mon_warn_on_pool_no_redundancy`](pg-pool/pg-pool.md#mon_warn_on_pool_no_redundancy) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [PG & pool health](pg-pool/pg-pool.md) |
| [`mon_warn_on_pool_pg_num_not_power_of_two`](pg-pool/pg-pool.md#mon_warn_on_pool_pg_num_not_power_of_two) | `True` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [PG & pool health](pg-pool/pg-pool.md) |
| [`nvmeof_mon_client_connect_panic`](runtime/general.md#nvmeof_mon_client_connect_panic) | `30` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`nvmeof_mon_client_disconnect_panic`](runtime/general.md#nvmeof_mon_client_disconnect_panic) | `100` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [General monitor](runtime/general.md) |
| [`nvmeof_mon_client_tick_period`](runtime/intervals.md#nvmeof_mon_client_tick_period) | `1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Intervals & timeouts](runtime/intervals.md) |
| [`pool_availability_update_interval`](pg-pool/pg-pool.md#pool_availability_update_interval) | `1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [PG & pool health](pg-pool/pg-pool.md) |
| [`osd_crush_update_weight_set`](cross-daemon/osd-related.md#osd_crush_update_weight_set) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [OSD-related settings](cross-daemon/osd-related.md) |
| [`osd_pool_default_crimson`](pg-pool/pg-pool.md#osd_pool_default_crimson) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [PG & pool health](pg-pool/pg-pool.md) |
| [`osd_pool_erasure_code_stripe_unit`](pg-pool/pg-pool.md#osd_pool_erasure_code_stripe_unit) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [PG & pool health](pg-pool/pg-pool.md) |
| [`paxos_kill_at`](quorum/quorum-paxos.md#paxos_kill_at) | `0` | Dev | در محیط عملیاتی همان پیش‌فرض upstream | [Quorum & Paxos](quorum/quorum-paxos.md) |
| [`paxos_max_join_drift`](quorum/quorum-paxos.md#paxos_max_join_drift) | `10` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Quorum & Paxos](quorum/quorum-paxos.md) |
| [`paxos_min`](quorum/quorum-paxos.md#paxos_min) | `500` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Quorum & Paxos](quorum/quorum-paxos.md) |
| [`paxos_min_wait`](quorum/quorum-paxos.md#paxos_min_wait) | `0.05` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Quorum & Paxos](quorum/quorum-paxos.md) |
| [`paxos_propose_interval`](quorum/quorum-paxos.md#paxos_propose_interval) | `1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Quorum & Paxos](quorum/quorum-paxos.md) |
| [`paxos_service_trim_max`](quorum/quorum-paxos.md#paxos_service_trim_max) | `500` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Quorum & Paxos](quorum/quorum-paxos.md) |
| [`paxos_service_trim_max_multiplier`](quorum/quorum-paxos.md#paxos_service_trim_max_multiplier) | `20` | Performance | در محدوده مستند بمانید | [Quorum & Paxos](quorum/quorum-paxos.md) |
| [`paxos_service_trim_min`](quorum/quorum-paxos.md#paxos_service_trim_min) | `250` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Quorum & Paxos](quorum/quorum-paxos.md) |
| [`paxos_stash_full_interval`](quorum/quorum-paxos.md#paxos_stash_full_interval) | `25` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Quorum & Paxos](quorum/quorum-paxos.md) |
| [`paxos_trim_max`](quorum/quorum-paxos.md#paxos_trim_max) | `500` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Quorum & Paxos](quorum/quorum-paxos.md) |
| [`paxos_trim_min`](quorum/quorum-paxos.md#paxos_trim_min) | `250` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [Quorum & Paxos](quorum/quorum-paxos.md) |

[← نمای کلی](../OVERVIEW.md)
