# پیکربندی RBD mirror — مرجع سریع تنظیم

هر **24** گزینه با مدل تنظیم و راهنمای یک‌خطی.

[← نمای کلی](../OVERVIEW.md)

| گزینه | پیش‌فرض | مدل | پاسخ سریع | موضوع |
|--------|---------|-------|--------------|-------|
| [`rbd_mirror_concurrent_image_deletions`](topics/mirror.md#rbd_mirror_concurrent_image_deletions) | `1` | عملکرد | در محدوده مستند بمانید | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_concurrent_image_syncs`](topics/mirror.md#rbd_mirror_concurrent_image_syncs) | `5` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_delete_retry_interval`](topics/mirror.md#rbd_mirror_delete_retry_interval) | `30` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_image_perf_stats_prio`](topics/mirror.md#rbd_mirror_image_perf_stats_prio) | `5` | عملکرد | در محدوده مستند بمانید | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_image_policy_migration_throttle`](topics/mirror.md#rbd_mirror_image_policy_migration_throttle) | `300` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_image_policy_rebalance_timeout`](topics/mirror.md#rbd_mirror_image_policy_rebalance_timeout) | `0` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_image_policy_type`](topics/mirror.md#rbd_mirror_image_policy_type) | `simple` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_image_policy_update_throttle_interval`](topics/mirror.md#rbd_mirror_image_policy_update_throttle_interval) | `1` | عملکرد | در محدوده مستند بمانید | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_image_state_check_interval`](topics/mirror.md#rbd_mirror_image_state_check_interval) | `30` | عملکرد | در محدوده مستند بمانید | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_journal_commit_age`](topics/mirror.md#rbd_mirror_journal_commit_age) | `5` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_journal_poll_age`](topics/mirror.md#rbd_mirror_journal_poll_age) | `5` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_leader_heartbeat_interval`](topics/mirror.md#rbd_mirror_leader_heartbeat_interval) | `5` | عملکرد | در محدوده مستند بمانید | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_leader_max_acquire_attempts_before_break`](topics/mirror.md#rbd_mirror_leader_max_acquire_attempts_before_break) | `3` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_leader_max_missed_heartbeats`](topics/mirror.md#rbd_mirror_leader_max_missed_heartbeats) | `2` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_memory_autotune`](topics/mirror.md#rbd_mirror_memory_autotune) | `True` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_memory_base`](topics/mirror.md#rbd_mirror_memory_base) | `768_M` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_memory_cache_autotune_interval`](topics/mirror.md#rbd_mirror_memory_cache_autotune_interval) | `30` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_memory_cache_min`](topics/mirror.md#rbd_mirror_memory_cache_min) | `128_M` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_memory_cache_resize_interval`](topics/mirror.md#rbd_mirror_memory_cache_resize_interval) | `5` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_memory_expected_fragmentation`](topics/mirror.md#rbd_mirror_memory_expected_fragmentation) | `0.15` | توسعه | در محیط عملیاتی همان پیش‌فرض upstream | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_memory_target`](topics/mirror.md#rbd_mirror_memory_target) | `4_G` | سیاست | مطابق سیاست امنیت و سازگاری | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_perf_stats_prio`](topics/mirror.md#rbd_mirror_perf_stats_prio) | `5` | عملکرد | در محدوده مستند بمانید | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_pool_replayers_refresh_interval`](topics/mirror.md#rbd_mirror_pool_replayers_refresh_interval) | `30` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_sync_point_update_age`](topics/mirror.md#rbd_mirror_sync_point_update_age) | `30` | عملکرد | خط پایه → تنظیم → اعتبارسنجی تحت بار | [RBD mirror](topics/mirror.md) |

[← نمای کلی](../OVERVIEW.md)
