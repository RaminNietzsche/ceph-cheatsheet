# CephFS mirror 配置 — 调优快速参考

全部 **15** 个选项的调优模型与一行建议。

[← 概览](../OVERVIEW.md)

| 选项 | 默认值 | 模型 | 快速建议 | 主题 |
|--------|---------|-------|--------------|-------|
| [`cephfs_mirror_action_update_interval`](topics/mirror.md#cephfs_mirror_action_update_interval) | `2` | 性能 | 保持在文档边界内 | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_blockdiff_min_file_size`](topics/mirror.md#cephfs_mirror_blockdiff_min_file_size) | `16_M` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_datasync_files_per_batch`](topics/mirror.md#cephfs_mirror_datasync_files_per_batch) | `64` | 性能 | 保持在文档边界内 | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_directory_scan_interval`](topics/mirror.md#cephfs_mirror_directory_scan_interval) | `10` | 性能 | 保持在文档边界内 | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_distribute_datasync_threads`](topics/mirror.md#cephfs_mirror_distribute_datasync_threads) | `True` | 性能 | 按实测需求启用/禁用 | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_max_concurrent_directory_syncs`](topics/mirror.md#cephfs_mirror_max_concurrent_directory_syncs) | `3` | 性能 | 保持在文档边界内 | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_max_consecutive_failures_per_directory`](topics/mirror.md#cephfs_mirror_max_consecutive_failures_per_directory) | `10` | 性能 | 保持在文档边界内 | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_max_datasync_threads`](topics/mirror.md#cephfs_mirror_max_datasync_threads) | `6` | 性能 | 保持在文档边界内 | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_max_snapshot_sync_per_cycle`](topics/mirror.md#cephfs_mirror_max_snapshot_sync_per_cycle) | `3` | 性能 | 保持在文档边界内 | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_mount_timeout`](topics/mirror.md#cephfs_mirror_mount_timeout) | `10` | 性能 | 保持在文档边界内 | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_perf_stats_prio`](topics/mirror.md#cephfs_mirror_perf_stats_prio) | `5` | 性能 | 保持在文档边界内 | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_restart_mirror_on_blocklist_interval`](topics/mirror.md#cephfs_mirror_restart_mirror_on_blocklist_interval) | `30` | 性能 | 保持在文档边界内 | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_restart_mirror_on_failure_interval`](topics/mirror.md#cephfs_mirror_restart_mirror_on_failure_interval) | `20` | 性能 | 保持在文档边界内 | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_retry_failed_directories_interval`](topics/mirror.md#cephfs_mirror_retry_failed_directories_interval) | `60` | 性能 | 保持在文档边界内 | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_tick_interval`](topics/mirror.md#cephfs_mirror_tick_interval) | `5` | 性能 | 保持在文档边界内 | [CephFS mirror](topics/mirror.md) |

[← 概览](../OVERVIEW.md)
