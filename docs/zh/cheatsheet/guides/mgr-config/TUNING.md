# MGR 配置 — 调优快速参考

全部 **52** 个选项的调优模型与一行建议。

[← 概览](../OVERVIEW.md)

| 选项 | 默认值 | 模型 | 快速建议 | 主题 |
|--------|---------|-------|--------------|-------|
| [`cephadm_path`](modules/mgr-modules.md#cephadm_path) | `/usr/sbin/cephadm` | 容量 | 匹配文件系统布局与容量规划 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_client_bytes`](modules/mgr-modules.md#mgr_client_bytes) | `128_M` | 开发 | 生产环境保持 upstream 默认值 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_client_messages`](modules/mgr-modules.md#mgr_client_messages) | `512` | 开发 | 生产环境保持 upstream 默认值 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_data`](modules/mgr-modules.md#mgr_data) | `/var/lib/ceph/mgr/$cluster-$id` | 性能 | 基线 → 调整 → 负载下验证 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_debug_aggressive_pg_num_changes`](modules/mgr-modules.md#mgr_debug_aggressive_pg_num_changes) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_disabled_modules`](modules/mgr-modules.md#mgr_disabled_modules) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_initial_modules`](modules/mgr-modules.md#mgr_initial_modules) | `iostat nfs nvmeof` | 策略 | 符合安全与兼容性策略 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_max_pg_creating`](modules/mgr-modules.md#mgr_max_pg_creating) | `1024` | 性能 | 基线 → 调整 → 负载下验证 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_max_pg_num_change`](modules/mgr-modules.md#mgr_max_pg_num_change) | `128` | 性能 | 基线 → 调整 → 负载下验证 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_mds_bytes`](modules/mgr-modules.md#mgr_mds_bytes) | `128_M` | 开发 | 生产环境保持 upstream 默认值 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_mds_messages`](modules/mgr-modules.md#mgr_mds_messages) | `128` | 开发 | 生产环境保持 upstream 默认值 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_module_load_delay`](modules/mgr-modules.md#mgr_module_load_delay) | `0` | 开发 | 生产环境保持 upstream 默认值 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_module_load_delay_name`](modules/mgr-modules.md#mgr_module_load_delay_name) | `(empty)` | 开发 | 生产环境保持 upstream 默认值 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_module_load_expiration`](modules/mgr-modules.md#mgr_module_load_expiration) | `20000` | 开发 | 生产环境保持 upstream 默认值 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_module_monitor_interval`](modules/mgr-modules.md#mgr_module_monitor_interval) | `5` | 性能 | 保持在文档边界内 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_module_path`](modules/mgr-modules.md#mgr_module_path) | `0/mgr` | 容量 | 匹配文件系统布局与容量规划 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_mon_bytes`](modules/mgr-modules.md#mgr_mon_bytes) | `128_M` | 开发 | 生产环境保持 upstream 默认值 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_mon_messages`](modules/mgr-modules.md#mgr_mon_messages) | `128` | 开发 | 生产环境保持 upstream 默认值 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_osd_bytes`](modules/mgr-modules.md#mgr_osd_bytes) | `512_M` | 开发 | 生产环境保持 upstream 默认值 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_osd_messages`](modules/mgr-modules.md#mgr_osd_messages) | `8_K` | 开发 | 生产环境保持 upstream 默认值 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_osd_upgrade_check_convergence_factor`](modules/mgr-modules.md#mgr_osd_upgrade_check_convergence_factor) | `0.8` | 性能 | 保持在文档边界内 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_pool`](modules/mgr-modules.md#mgr_pool) | `True` | 开发 | 生产环境保持 upstream 默认值 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_service_beacon_grace`](modules/mgr-modules.md#mgr_service_beacon_grace) | `1_min` | 性能 | 基线 → 调整 → 负载下验证 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_standby_modules`](modules/mgr-modules.md#mgr_standby_modules) | `True` | 性能 | 按实测需求启用/禁用 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_stats_period`](modules/mgr-modules.md#mgr_stats_period) | `5` | 策略 | 符合安全与兼容性策略 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_stats_period_autotune`](modules/mgr-modules.md#mgr_stats_period_autotune) | `True` | 策略 | 符合安全与兼容性策略 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_stats_period_autotune_queue_threshold`](modules/mgr-modules.md#mgr_stats_period_autotune_queue_threshold) | `100` | 性能 | 基线 → 调整 → 负载下验证 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_stats_threshold`](modules/mgr-modules.md#mgr_stats_threshold) | `5` | 性能 | 保持在文档边界内 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_subinterpreter_modules`](modules/mgr-modules.md#mgr_subinterpreter_modules) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_test_metadata_error`](modules/mgr-modules.md#mgr_test_metadata_error) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mgr_tick_period`](modules/mgr-modules.md#mgr_tick_period) | `2` | 性能 | 基线 → 调整 → 负载下验证 | [Manager & cephadm modules](modules/mgr-modules.md) |
| [`mon_cache_target_full_warn_ratio`](cluster/general.md#mon_cache_target_full_warn_ratio) | `0.66` | 性能 | 基线 → 调整 → 负载下验证 | [General manager](cluster/general.md) |
| [`mon_delta_reset_interval`](cluster/intervals.md#mon_delta_reset_interval) | `10` | 性能 | 基线 → 调整 → 负载下验证 | [Intervals](cluster/intervals.md) |
| [`mon_osd_err_op_age_ratio`](cluster/general.md#mon_osd_err_op_age_ratio) | `128` | 性能 | 基线 → 调整 → 负载下验证 | [General manager](cluster/general.md) |
| [`mon_pg_check_down_all_threshold`](cluster/pg-pool.md#mon_pg_check_down_all_threshold) | `0.5` | 性能 | 基线 → 调整 → 负载下验证 | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_pg_stuck_threshold`](cluster/pg-pool.md#mon_pg_stuck_threshold) | `1_min` | 性能 | 基线 → 调整 → 负载下验证 | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_pg_warn_max_object_skew`](cluster/pg-pool.md#mon_pg_warn_max_object_skew) | `10` | 性能 | 基线 → 调整 → 负载下验证 | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_pg_warn_min_objects`](cluster/pg-pool.md#mon_pg_warn_min_objects) | `10000` | 性能 | 基线 → 调整 → 负载下验证 | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_pg_warn_min_per_osd`](cluster/pg-pool.md#mon_pg_warn_min_per_osd) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_pg_warn_min_pool_objects`](cluster/pg-pool.md#mon_pg_warn_min_pool_objects) | `1000` | 性能 | 基线 → 调整 → 负载下验证 | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_pool_quota_crit_threshold`](cluster/pg-pool.md#mon_pool_quota_crit_threshold) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_pool_quota_warn_threshold`](cluster/pg-pool.md#mon_pool_quota_warn_threshold) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_reweight_max_change`](cluster/general.md#mon_reweight_max_change) | `0.05` | 性能 | 基线 → 调整 → 负载下验证 | [General manager](cluster/general.md) |
| [`mon_reweight_max_osds`](cluster/general.md#mon_reweight_max_osds) | `4` | 性能 | 基线 → 调整 → 负载下验证 | [General manager](cluster/general.md) |
| [`mon_reweight_min_bytes_per_osd`](cluster/general.md#mon_reweight_min_bytes_per_osd) | `100_M` | 性能 | 基线 → 调整 → 负载下验证 | [General manager](cluster/general.md) |
| [`mon_reweight_min_pgs_per_osd`](cluster/general.md#mon_reweight_min_pgs_per_osd) | `10` | 性能 | 基线 → 调整 → 负载下验证 | [General manager](cluster/general.md) |
| [`mon_stat_smooth_intervals`](cluster/intervals.md#mon_stat_smooth_intervals) | `6` | 性能 | 保持在文档边界内 | [Intervals](cluster/intervals.md) |
| [`mon_target_pg_per_osd`](cluster/pg-pool.md#mon_target_pg_per_osd) | `200` | 性能 | 保持在文档边界内 | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_warn_on_misplaced`](cluster/general.md#mon_warn_on_misplaced) | `False` | 性能 | 按实测需求启用/禁用 | [General manager](cluster/general.md) |
| [`mon_warn_on_pool_no_app`](cluster/pg-pool.md#mon_warn_on_pool_no_app) | `True` | 开发 | 生产环境保持 upstream 默认值 | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_warn_on_pool_no_app_grace`](cluster/pg-pool.md#mon_warn_on_pool_no_app_grace) | `5_min` | 开发 | 生产环境保持 upstream 默认值 | [PG & pool settings](cluster/pg-pool.md) |
| [`mon_warn_on_too_few_osds`](cluster/general.md#mon_warn_on_too_few_osds) | `True` | 性能 | 按实测需求启用/禁用 | [General manager](cluster/general.md) |

[← 概览](../OVERVIEW.md)
