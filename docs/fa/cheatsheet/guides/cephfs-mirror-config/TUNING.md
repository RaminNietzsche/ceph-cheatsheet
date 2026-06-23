# پیکربندی CephFS mirror — مرجع سریع تنظیم

هر **15** گزینه با مدل تنظیم و راهنمای یک‌خطی.

[← نمای کلی](../OVERVIEW.md)

| گزینه | پیش‌فرض | مدل | پاسخ سریع | موضوع |
|--------|---------|-------|--------------|-------|
| [`cephfs_mirror_action_update_interval`](topics/mirror.md#cephfs_mirror_action_update_interval) | `2` | عملکرد | در محدوده مستند بمانید | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_blockdiff_min_file_size`](topics/mirror.md#cephfs_mirror_blockdiff_min_file_size) | `16_M` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_datasync_files_per_batch`](topics/mirror.md#cephfs_mirror_datasync_files_per_batch) | `64` | عملکرد | در محدوده مستند بمانید | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_directory_scan_interval`](topics/mirror.md#cephfs_mirror_directory_scan_interval) | `10` | عملکرد | در محدوده مستند بمانید | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_distribute_datasync_threads`](topics/mirror.md#cephfs_mirror_distribute_datasync_threads) | `True` | عملکرد | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_max_concurrent_directory_syncs`](topics/mirror.md#cephfs_mirror_max_concurrent_directory_syncs) | `3` | عملکرد | در محدوده مستند بمانید | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_max_consecutive_failures_per_directory`](topics/mirror.md#cephfs_mirror_max_consecutive_failures_per_directory) | `10` | عملکرد | در محدوده مستند بمانید | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_max_datasync_threads`](topics/mirror.md#cephfs_mirror_max_datasync_threads) | `6` | عملکرد | در محدوده مستند بمانید | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_max_snapshot_sync_per_cycle`](topics/mirror.md#cephfs_mirror_max_snapshot_sync_per_cycle) | `3` | عملکرد | در محدوده مستند بمانید | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_mount_timeout`](topics/mirror.md#cephfs_mirror_mount_timeout) | `10` | عملکرد | در محدوده مستند بمانید | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_perf_stats_prio`](topics/mirror.md#cephfs_mirror_perf_stats_prio) | `5` | عملکرد | در محدوده مستند بمانید | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_restart_mirror_on_blocklist_interval`](topics/mirror.md#cephfs_mirror_restart_mirror_on_blocklist_interval) | `30` | عملکرد | در محدوده مستند بمانید | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_restart_mirror_on_failure_interval`](topics/mirror.md#cephfs_mirror_restart_mirror_on_failure_interval) | `20` | عملکرد | در محدوده مستند بمانید | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_retry_failed_directories_interval`](topics/mirror.md#cephfs_mirror_retry_failed_directories_interval) | `60` | عملکرد | در محدوده مستند بمانید | [CephFS mirror](topics/mirror.md) |
| [`cephfs_mirror_tick_interval`](topics/mirror.md#cephfs_mirror_tick_interval) | `5` | عملکرد | در محدوده مستند بمانید | [CephFS mirror](topics/mirror.md) |

[← نمای کلی](../OVERVIEW.md)
