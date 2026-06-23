# Crimson 配置 — 调优快速参考

全部 **42** 个选项的调优模型与一行建议。

[← 概览](../OVERVIEW.md)

| 选项 | 默认值 | 模型 | 快速建议 | 主题 |
|--------|---------|-------|--------------|-------|
| [`crimson_allow_pg_split`](topics/crimson.md#crimson_allow_pg_split) | `True` | Policy | 符合安全与兼容性策略 | [Crimson OSD](topics/crimson.md) |
| [`crimson_bluestore_cpu_set`](topics/crimson.md#crimson_bluestore_cpu_set) | `(empty)` | Performance | 基线 → 调整 → 负载下验证 | [Crimson OSD](topics/crimson.md) |
| [`crimson_bluestore_num_threads`](topics/crimson.md#crimson_bluestore_num_threads) | `6` | Performance | 基线 → 调整 → 负载下验证 | [Crimson OSD](topics/crimson.md) |
| [`crimson_cpu_num`](topics/crimson.md#crimson_cpu_num) | `0` | Performance | 保持在文档边界内 | [Crimson OSD](topics/crimson.md) |
| [`crimson_cpu_set`](topics/crimson.md#crimson_cpu_set) | `(empty)` | Performance | 基线 → 调整 → 负载下验证 | [Crimson OSD](topics/crimson.md) |
| [`crimson_memory`](topics/crimson.md#crimson_memory) | `0` | Performance | 基线 → 调整 → 负载下验证 | [Crimson OSD](topics/crimson.md) |
| [`crimson_osd_obc_lru_size`](topics/crimson.md#crimson_osd_obc_lru_size) | `512` | Performance | 基线 → 调整 → 负载下验证 | [Crimson OSD](topics/crimson.md) |
| [`crimson_osd_scheduler_concurrency`](topics/crimson.md#crimson_osd_scheduler_concurrency) | `0` | Performance | 基线 → 调整 → 负载下验证 | [Crimson OSD](topics/crimson.md) |
| [`crimson_osd_stat_interval`](topics/crimson.md#crimson_osd_stat_interval) | `0` | Performance | 基线 → 调整 → 负载下验证 | [Crimson OSD](topics/crimson.md) |
| [`crimson_poll_mode`](topics/crimson.md#crimson_poll_mode) | `False` | Performance | 按实测需求启用/禁用 | [Crimson OSD](topics/crimson.md) |
| [`crimson_reactor_backend`](topics/crimson.md#crimson_reactor_backend) | `(empty)` | Performance | 基线 → 调整 → 负载下验证 | [Crimson OSD](topics/crimson.md) |
| [`crimson_reactor_idle_poll_time_us`](topics/crimson.md#crimson_reactor_idle_poll_time_us) | `200` | Performance | 基线 → 调整 → 负载下验证 | [Crimson OSD](topics/crimson.md) |
| [`crimson_reactor_io_latency_goal_ms`](topics/crimson.md#crimson_reactor_io_latency_goal_ms) | `0` | Performance | 基线 → 调整 → 负载下验证 | [Crimson OSD](topics/crimson.md) |
| [`crimson_reactor_task_quota_ms`](topics/crimson.md#crimson_reactor_task_quota_ms) | `0.5` | Performance | 基线 → 调整 → 负载下验证 | [Crimson OSD](topics/crimson.md) |
| [`seastore_block_create`](topics/seastore.md#seastore_block_create) | `True` | Dev | 生产环境保持 upstream 默认值 | [Seastore](topics/seastore.md) |
| [`seastore_cachepin_2q_in_ratio`](topics/seastore.md#seastore_cachepin_2q_in_ratio) | `0.5` | Performance | 基线 → 调整 → 负载下验证 | [Seastore](topics/seastore.md) |
| [`seastore_cachepin_2q_out_ratio`](topics/seastore.md#seastore_cachepin_2q_out_ratio) | `0.5` | Performance | 基线 → 调整 → 负载下验证 | [Seastore](topics/seastore.md) |
| [`seastore_cachepin_size_pershard`](topics/seastore.md#seastore_cachepin_size_pershard) | `2_G` | Performance | 基线 → 调整 → 负载下验证 | [Seastore](topics/seastore.md) |
| [`seastore_cachepin_type`](topics/seastore.md#seastore_cachepin_type) | `LRU` | Dev | 生产环境保持 upstream 默认值 | [Seastore](topics/seastore.md) |
| [`seastore_cbjournal_size`](topics/seastore.md#seastore_cbjournal_size) | `5_G` | Dev | 生产环境保持 upstream 默认值 | [Seastore](topics/seastore.md) |
| [`seastore_cold_tier_generations`](topics/seastore.md#seastore_cold_tier_generations) | `3` | Performance | 基线 → 调整 → 负载下验证 | [Seastore](topics/seastore.md) |
| [`seastore_data_delta_based_overwrite`](topics/seastore.md#seastore_data_delta_based_overwrite) | `0` | Dev | 生产环境保持 upstream 默认值 | [Seastore](topics/seastore.md) |
| [`seastore_default_max_object_size`](topics/seastore.md#seastore_default_max_object_size) | `16777216` | Dev | 生产环境保持 upstream 默认值 | [Seastore](topics/seastore.md) |
| [`seastore_device_size`](topics/seastore.md#seastore_device_size) | `50_G` | Dev | 生产环境保持 upstream 默认值 | [Seastore](topics/seastore.md) |
| [`seastore_disable_end_to_end_data_protection`](topics/seastore.md#seastore_disable_end_to_end_data_protection) | `True` | Dev | 生产环境保持 upstream 默认值 | [Seastore](topics/seastore.md) |
| [`seastore_full_integrity_check`](topics/seastore.md#seastore_full_integrity_check) | `False` | Dev | 生产环境保持 upstream 默认值 | [Seastore](topics/seastore.md) |
| [`seastore_hot_tier_generations`](topics/seastore.md#seastore_hot_tier_generations) | `5` | Performance | 保持在文档边界内 | [Seastore](topics/seastore.md) |
| [`seastore_journal_batch_capacity`](topics/seastore.md#seastore_journal_batch_capacity) | `16` | Dev | 生产环境保持 upstream 默认值 | [Seastore](topics/seastore.md) |
| [`seastore_journal_batch_flush_size`](topics/seastore.md#seastore_journal_batch_flush_size) | `16_M` | Dev | 生产环境保持 upstream 默认值 | [Seastore](topics/seastore.md) |
| [`seastore_journal_batch_preferred_fullness`](topics/seastore.md#seastore_journal_batch_preferred_fullness) | `0.95` | Dev | 生产环境保持 upstream 默认值 | [Seastore](topics/seastore.md) |
| [`seastore_journal_iodepth_limit`](topics/seastore.md#seastore_journal_iodepth_limit) | `5` | Dev | 生产环境保持 upstream 默认值 | [Seastore](topics/seastore.md) |
| [`seastore_main_device_type`](topics/seastore.md#seastore_main_device_type) | `SSD` | Dev | 生产环境保持 upstream 默认值 | [Seastore](topics/seastore.md) |
| [`seastore_max_concurrent_transactions`](topics/seastore.md#seastore_max_concurrent_transactions) | `128` | Performance | 基线 → 调整 → 负载下验证 | [Seastore](topics/seastore.md) |
| [`seastore_max_data_allocation_size`](topics/seastore.md#seastore_max_data_allocation_size) | `0` | Performance | 基线 → 调整 → 负载下验证 | [Seastore](topics/seastore.md) |
| [`seastore_multiple_tiers_default_evict_ratio`](topics/seastore.md#seastore_multiple_tiers_default_evict_ratio) | `0.6` | Performance | 基线 → 调整 → 负载下验证 | [Seastore](topics/seastore.md) |
| [`seastore_multiple_tiers_fast_evict_ratio`](topics/seastore.md#seastore_multiple_tiers_fast_evict_ratio) | `0.7` | Performance | 基线 → 调整 → 负载下验证 | [Seastore](topics/seastore.md) |
| [`seastore_multiple_tiers_stop_evict_ratio`](topics/seastore.md#seastore_multiple_tiers_stop_evict_ratio) | `0.5` | Performance | 基线 → 调整 → 负载下验证 | [Seastore](topics/seastore.md) |
| [`seastore_require_partition_count_match_reactor_count`](topics/seastore.md#seastore_require_partition_count_match_reactor_count) | `True` | Performance | 按实测需求启用/禁用 | [Seastore](topics/seastore.md) |
| [`seastore_segment_cleaner_gc_autotune`](topics/seastore.md#seastore_segment_cleaner_gc_autotune) | `True` | Performance | 按实测需求启用/禁用 | [Seastore](topics/seastore.md) |
| [`seastore_segment_cleaner_gc_autotune_ratio`](topics/seastore.md#seastore_segment_cleaner_gc_autotune_ratio) | `2.0` | Performance | 保持在文档边界内 | [Seastore](topics/seastore.md) |
| [`seastore_segment_cleaner_gc_formula`](topics/seastore.md#seastore_segment_cleaner_gc_formula) | `cost_benefit` | Performance | 基线 → 调整 → 负载下验证 | [Seastore](topics/seastore.md) |
| [`seastore_segment_size`](topics/seastore.md#seastore_segment_size) | `64_M` | Performance | 基线 → 调整 → 负载下验证 | [Seastore](topics/seastore.md) |

[← 概览](../OVERVIEW.md)
