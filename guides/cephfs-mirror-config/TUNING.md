# CephFS mirror Config — Tuning Quick Reference

All **15** options with tuning model and one-line guidance.

[← Overview](OVERVIEW.md)

| Option | Default | Model | Quick answer | Topic |
|--------|---------|-------|--------------|-------|
| [`cephfs_mirror_action_update_interval`](topics/mirror.md#cephfs_mirror_action_update_interval) | `2` | Performance | Stay within documented bounds | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_blockdiff_min_file_size`](topics/mirror.md#cephfs_mirror_blockdiff_min_file_size) | `16_M` | Performance | Baseline → adjust → validate under load | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_datasync_files_per_batch`](topics/mirror.md#cephfs_mirror_datasync_files_per_batch) | `64` | Performance | Stay within documented bounds | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_directory_scan_interval`](topics/mirror.md#cephfs_mirror_directory_scan_interval) | `10` | Performance | Stay within documented bounds | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_distribute_datasync_threads`](topics/mirror.md#cephfs_mirror_distribute_datasync_threads) | `True` | Performance | Enable/disable based on measured need | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_max_concurrent_directory_syncs`](topics/mirror.md#cephfs_mirror_max_concurrent_directory_syncs) | `3` | Performance | Stay within documented bounds | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_max_consecutive_failures_per_directory`](topics/mirror.md#cephfs_mirror_max_consecutive_failures_per_directory) | `10` | Performance | Stay within documented bounds | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_max_datasync_threads`](topics/mirror.md#cephfs_mirror_max_datasync_threads) | `6` | Performance | Stay within documented bounds | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_max_snapshot_sync_per_cycle`](topics/mirror.md#cephfs_mirror_max_snapshot_sync_per_cycle) | `3` | Performance | Stay within documented bounds | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_mount_timeout`](topics/mirror.md#cephfs_mirror_mount_timeout) | `10` | Performance | Stay within documented bounds | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_perf_stats_prio`](topics/mirror.md#cephfs_mirror_perf_stats_prio) | `5` | Performance | Stay within documented bounds | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_restart_mirror_on_blocklist_interval`](topics/mirror.md#cephfs_mirror_restart_mirror_on_blocklist_interval) | `30` | Performance | Stay within documented bounds | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_restart_mirror_on_failure_interval`](topics/mirror.md#cephfs_mirror_restart_mirror_on_failure_interval) | `20` | Performance | Stay within documented bounds | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_retry_failed_directories_interval`](topics/mirror.md#cephfs_mirror_retry_failed_directories_interval) | `60` | Performance | Stay within documented bounds | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_tick_interval`](topics/mirror.md#cephfs_mirror_tick_interval) | `5` | Performance | Stay within documented bounds | [CephFS mirror](topics/mirror.md) |

[← Overview](OVERVIEW.md)
