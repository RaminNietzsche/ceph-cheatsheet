# پیکربندی MDS client — مرجع سریع تنظیم

هر **70** گزینه با مدل تنظیم و راهنمای یک‌خطی.

[← نمای کلی](../OVERVIEW.md)

| گزینه | پیش‌فرض | مدل | پاسخ سریع | موضوع |
|--------|---------|-------|--------------|-------|
| [`client_acl_type`](clients/client.md#client_acl_type) | `(empty)` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_asio_thread_count`](clients/client.md#client_asio_thread_count) | `2` | Performance | در محدوده مستند بمانید | [CephFS client](clients/client.md) |
| [`client_cache_mid`](clients/client.md#client_cache_mid) | `0.75` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_cache_size`](clients/client.md#client_cache_size) | `16_K` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_caps_release_delay`](clients/client.md#client_caps_release_delay) | `5` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |
| [`client_check_pool_perm`](clients/client.md#client_check_pool_perm) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [CephFS client](clients/client.md) |
| [`client_collect_and_send_global_metrics`](clients/client.md#client_collect_and_send_global_metrics) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [CephFS client](clients/client.md) |
| [`client_debug_force_sync_read`](clients/client.md#client_debug_force_sync_read) | `False` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |
| [`client_debug_getattr_caps`](clients/client.md#client_debug_getattr_caps) | `False` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |
| [`client_debug_inject_features`](clients/client.md#client_debug_inject_features) | `(empty)` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |
| [`client_debug_inject_tick_delay`](clients/client.md#client_debug_inject_tick_delay) | `0` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |
| [`client_die_on_failed_dentry_invalidate`](clients/client.md#client_die_on_failed_dentry_invalidate) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [CephFS client](clients/client.md) |
| [`client_die_on_failed_remount`](clients/client.md#client_die_on_failed_remount) | `False` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |
| [`client_dirsize_rbytes`](clients/client.md#client_dirsize_rbytes) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [CephFS client](clients/client.md) |
| [`client_file_blockdiff_max_concurrent_object_scans`](clients/client.md#client_file_blockdiff_max_concurrent_object_scans) | `16` | Performance | در محدوده مستند بمانید | [CephFS client](clients/client.md) |
| [`client_force_lazyio`](clients/client.md#client_force_lazyio) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [CephFS client](clients/client.md) |
| [`client_fs`](clients/client.md#client_fs) | `(empty)` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_fscrypt_as`](clients/client.md#client_fscrypt_as) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [CephFS client](clients/client.md) |
| [`client_fscrypt_dummy_encryption`](clients/client.md#client_fscrypt_dummy_encryption) | `False` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |
| [`client_inject_fixed_oldest_tid`](clients/client.md#client_inject_fixed_oldest_tid) | `False` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |
| [`client_inject_release_failure`](clients/client.md#client_inject_release_failure) | `False` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |
| [`client_inject_write_delay_secs`](clients/client.md#client_inject_write_delay_secs) | `0` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |
| [`client_max_inline_size`](clients/client.md#client_max_inline_size) | `4_K` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |
| [`client_max_retries_on_remount_failure`](clients/client.md#client_max_retries_on_remount_failure) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_mds_namespace`](clients/client.md#client_mds_namespace) | `(empty)` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |
| [`client_metadata`](clients/client.md#client_metadata) | `(empty)` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_mount_gid`](clients/client.md#client_mount_gid) | `-1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_mount_timeout`](clients/client.md#client_mount_timeout) | `5_min` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_mount_uid`](clients/client.md#client_mount_uid) | `-1` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_mountpoint`](clients/client.md#client_mountpoint) | `/` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_notify_timeout`](clients/client.md#client_notify_timeout) | `10` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |
| [`client_oc`](clients/client.md#client_oc) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [CephFS client](clients/client.md) |
| [`client_oc_max_dirty`](clients/client.md#client_oc_max_dirty) | `100_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_oc_max_dirty_age`](clients/client.md#client_oc_max_dirty_age) | `5` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_oc_max_objects`](clients/client.md#client_oc_max_objects) | `1000` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_oc_size`](clients/client.md#client_oc_size) | `200_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_oc_target_dirty`](clients/client.md#client_oc_target_dirty) | `8_M` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_permissions`](clients/client.md#client_permissions) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [CephFS client](clients/client.md) |
| [`client_quota`](clients/client.md#client_quota) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [CephFS client](clients/client.md) |
| [`client_quota_df`](clients/client.md#client_quota_df) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [CephFS client](clients/client.md) |
| [`client_readahead_max_bytes`](clients/client.md#client_readahead_max_bytes) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_readahead_max_periods`](clients/client.md#client_readahead_max_periods) | `4` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_readahead_min`](clients/client.md#client_readahead_min) | `128_K` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_reconnect_stale`](clients/client.md#client_reconnect_stale) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [CephFS client](clients/client.md) |
| [`client_respect_subvolume_snapshot_visibility`](clients/client.md#client_respect_subvolume_snapshot_visibility) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [CephFS client](clients/client.md) |
| [`client_shutdown_timeout`](clients/client.md#client_shutdown_timeout) | `30` | Performance | در محدوده مستند بمانید | [CephFS client](clients/client.md) |
| [`client_snapdir`](clients/client.md#client_snapdir) | `.snap` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [CephFS client](clients/client.md) |
| [`client_tick_interval`](clients/client.md#client_tick_interval) | `1` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |
| [`client_trace`](clients/client.md#client_trace) | `(empty)` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |
| [`client_try_dentry_invalidate`](clients/client.md#client_try_dentry_invalidate) | `False` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |
| [`client_use_faked_inos`](clients/client.md#client_use_faked_inos) | `False` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |
| [`client_use_random_mds`](clients/client.md#client_use_random_mds) | `False` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |
| [`debug_allow_any_pool_priority`](other/debug.md#debug_allow_any_pool_priority) | `False` | Dev | پیش‌فرض upstream در production | [Debug](other/debug.md) |
| [`fake_statfs_for_testing`](other/general.md#fake_statfs_for_testing) | `0` | Dev | پیش‌فرض upstream در production | [General](other/general.md) |
| [`fuse_allow_other`](clients/fuse.md#fuse_allow_other) | `True` | Policy | مطابق سیاست امنیت و سازگاری | [FUSE client](clients/fuse.md) |
| [`fuse_atomic_o_trunc`](clients/fuse.md#fuse_atomic_o_trunc) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [FUSE client](clients/fuse.md) |
| [`fuse_big_writes`](clients/fuse.md#fuse_big_writes) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [FUSE client](clients/fuse.md) |
| [`fuse_debug`](clients/fuse.md#fuse_debug) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [FUSE client](clients/fuse.md) |
| [`fuse_default_permissions`](clients/fuse.md#fuse_default_permissions) | `False` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [FUSE client](clients/fuse.md) |
| [`fuse_disable_pagecache`](clients/fuse.md#fuse_disable_pagecache) | `False` | Policy | مطابق سیاست امنیت و سازگاری | [FUSE client](clients/fuse.md) |
| [`fuse_max_write`](clients/fuse.md#fuse_max_write) | `0` | Performance | خط پایه → تنظیم → اعتبارسنجی تحت بار | [FUSE client](clients/fuse.md) |
| [`fuse_multithreaded`](clients/fuse.md#fuse_multithreaded) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [FUSE client](clients/fuse.md) |
| [`fuse_require_active_mds`](clients/fuse.md#fuse_require_active_mds) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [FUSE client](clients/fuse.md) |
| [`fuse_set_user_groups`](clients/fuse.md#fuse_set_user_groups) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [FUSE client](clients/fuse.md) |
| [`fuse_splice_move`](clients/fuse.md#fuse_splice_move) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [FUSE client](clients/fuse.md) |
| [`fuse_splice_read`](clients/fuse.md#fuse_splice_read) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [FUSE client](clients/fuse.md) |
| [`fuse_splice_write`](clients/fuse.md#fuse_splice_write) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [FUSE client](clients/fuse.md) |
| [`fuse_syncfs_on_mksnap`](clients/fuse.md#fuse_syncfs_on_mksnap) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [FUSE client](clients/fuse.md) |
| [`fuse_use_invalidate_cb`](clients/fuse.md#fuse_use_invalidate_cb) | `True` | Performance | فعال/غیرفعال بر اساس نیاز اندازه‌گیری‌شده | [FUSE client](clients/fuse.md) |
| [`osd_client_watch_timeout`](clients/client.md#osd_client_watch_timeout) | `30` | Dev | پیش‌فرض upstream در production | [CephFS client](clients/client.md) |

[← نمای کلی](../OVERVIEW.md)
