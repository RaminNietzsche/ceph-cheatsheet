# MDS client Config — Tuning Quick Reference

All **70** options with tuning model and one-line guidance.

[← Overview](OVERVIEW.md)

| Option | Default | Model | Quick answer | Topic |
|--------|---------|-------|--------------|-------|
| [`client_acl_type`](clients/client.md#client_acl_type) | `(empty)` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_asio_thread_count`](clients/client.md#client_asio_thread_count) | `2` | Performance | Stay within documented bounds | [CephFS client](clients/client.md) |
| [`client_cache_mid`](clients/client.md#client_cache_mid) | `0.75` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_cache_size`](clients/client.md#client_cache_size) | `16_K` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_caps_release_delay`](clients/client.md#client_caps_release_delay) | `5` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |
| [`client_check_pool_perm`](clients/client.md#client_check_pool_perm) | `True` | Performance | Enable/disable based on measured need | [CephFS client](clients/client.md) |
| [`client_collect_and_send_global_metrics`](clients/client.md#client_collect_and_send_global_metrics) | `False` | Performance | Enable/disable based on measured need | [CephFS client](clients/client.md) |
| [`client_debug_force_sync_read`](clients/client.md#client_debug_force_sync_read) | `False` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |
| [`client_debug_getattr_caps`](clients/client.md#client_debug_getattr_caps) | `False` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |
| [`client_debug_inject_features`](clients/client.md#client_debug_inject_features) | `(empty)` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |
| [`client_debug_inject_tick_delay`](clients/client.md#client_debug_inject_tick_delay) | `0` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |
| [`client_die_on_failed_dentry_invalidate`](clients/client.md#client_die_on_failed_dentry_invalidate) | `True` | Performance | Enable/disable based on measured need | [CephFS client](clients/client.md) |
| [`client_die_on_failed_remount`](clients/client.md#client_die_on_failed_remount) | `False` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |
| [`client_dirsize_rbytes`](clients/client.md#client_dirsize_rbytes) | `True` | Performance | Enable/disable based on measured need | [CephFS client](clients/client.md) |
| [`client_file_blockdiff_max_concurrent_object_scans`](clients/client.md#client_file_blockdiff_max_concurrent_object_scans) | `16` | Performance | Stay within documented bounds | [CephFS client](clients/client.md) |
| [`client_force_lazyio`](clients/client.md#client_force_lazyio) | `False` | Performance | Enable/disable based on measured need | [CephFS client](clients/client.md) |
| [`client_fs`](clients/client.md#client_fs) | `(empty)` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_fscrypt_as`](clients/client.md#client_fscrypt_as) | `True` | Performance | Enable/disable based on measured need | [CephFS client](clients/client.md) |
| [`client_fscrypt_dummy_encryption`](clients/client.md#client_fscrypt_dummy_encryption) | `False` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |
| [`client_inject_fixed_oldest_tid`](clients/client.md#client_inject_fixed_oldest_tid) | `False` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |
| [`client_inject_release_failure`](clients/client.md#client_inject_release_failure) | `False` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |
| [`client_inject_write_delay_secs`](clients/client.md#client_inject_write_delay_secs) | `0` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |
| [`client_max_inline_size`](clients/client.md#client_max_inline_size) | `4_K` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |
| [`client_max_retries_on_remount_failure`](clients/client.md#client_max_retries_on_remount_failure) | `5` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_mds_namespace`](clients/client.md#client_mds_namespace) | `(empty)` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |
| [`client_metadata`](clients/client.md#client_metadata) | `(empty)` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_mount_gid`](clients/client.md#client_mount_gid) | `-1` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_mount_timeout`](clients/client.md#client_mount_timeout) | `5_min` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_mount_uid`](clients/client.md#client_mount_uid) | `-1` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_mountpoint`](clients/client.md#client_mountpoint) | `/` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_notify_timeout`](clients/client.md#client_notify_timeout) | `10` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |
| [`client_oc`](clients/client.md#client_oc) | `True` | Performance | Enable/disable based on measured need | [CephFS client](clients/client.md) |
| [`client_oc_max_dirty`](clients/client.md#client_oc_max_dirty) | `100_M` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_oc_max_dirty_age`](clients/client.md#client_oc_max_dirty_age) | `5` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_oc_max_objects`](clients/client.md#client_oc_max_objects) | `1000` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_oc_size`](clients/client.md#client_oc_size) | `200_M` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_oc_target_dirty`](clients/client.md#client_oc_target_dirty) | `8_M` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_permissions`](clients/client.md#client_permissions) | `True` | Performance | Enable/disable based on measured need | [CephFS client](clients/client.md) |
| [`client_quota`](clients/client.md#client_quota) | `True` | Performance | Enable/disable based on measured need | [CephFS client](clients/client.md) |
| [`client_quota_df`](clients/client.md#client_quota_df) | `True` | Performance | Enable/disable based on measured need | [CephFS client](clients/client.md) |
| [`client_readahead_max_bytes`](clients/client.md#client_readahead_max_bytes) | `0` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_readahead_max_periods`](clients/client.md#client_readahead_max_periods) | `4` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_readahead_min`](clients/client.md#client_readahead_min) | `128_K` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_reconnect_stale`](clients/client.md#client_reconnect_stale) | `False` | Performance | Enable/disable based on measured need | [CephFS client](clients/client.md) |
| [`client_respect_subvolume_snapshot_visibility`](clients/client.md#client_respect_subvolume_snapshot_visibility) | `False` | Performance | Enable/disable based on measured need | [CephFS client](clients/client.md) |
| [`client_shutdown_timeout`](clients/client.md#client_shutdown_timeout) | `30` | Performance | Stay within documented bounds | [CephFS client](clients/client.md) |
| [`client_snapdir`](clients/client.md#client_snapdir) | `.snap` | Performance | Baseline → adjust → validate under load | [CephFS client](clients/client.md) |
| [`client_tick_interval`](clients/client.md#client_tick_interval) | `1` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |
| [`client_trace`](clients/client.md#client_trace) | `(empty)` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |
| [`client_try_dentry_invalidate`](clients/client.md#client_try_dentry_invalidate) | `False` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |
| [`client_use_faked_inos`](clients/client.md#client_use_faked_inos) | `False` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |
| [`client_use_random_mds`](clients/client.md#client_use_random_mds) | `False` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |
| [`debug_allow_any_pool_priority`](other/debug.md#debug_allow_any_pool_priority) | `False` | Dev | Keep upstream default in production | [Debug](other/debug.md) |
| [`fake_statfs_for_testing`](other/general.md#fake_statfs_for_testing) | `0` | Dev | Keep upstream default in production | [General](other/general.md) |
| [`fuse_allow_other`](clients/fuse.md#fuse_allow_other) | `True` | Policy | Align with security and compatibility policy | [FUSE client](clients/fuse.md) |
| [`fuse_atomic_o_trunc`](clients/fuse.md#fuse_atomic_o_trunc) | `True` | Performance | Enable/disable based on measured need | [FUSE client](clients/fuse.md) |
| [`fuse_big_writes`](clients/fuse.md#fuse_big_writes) | `True` | Performance | Enable/disable based on measured need | [FUSE client](clients/fuse.md) |
| [`fuse_debug`](clients/fuse.md#fuse_debug) | `False` | Performance | Enable/disable based on measured need | [FUSE client](clients/fuse.md) |
| [`fuse_default_permissions`](clients/fuse.md#fuse_default_permissions) | `False` | Performance | Enable/disable based on measured need | [FUSE client](clients/fuse.md) |
| [`fuse_disable_pagecache`](clients/fuse.md#fuse_disable_pagecache) | `False` | Policy | Align with security and compatibility policy | [FUSE client](clients/fuse.md) |
| [`fuse_max_write`](clients/fuse.md#fuse_max_write) | `0` | Performance | Baseline → adjust → validate under load | [FUSE client](clients/fuse.md) |
| [`fuse_multithreaded`](clients/fuse.md#fuse_multithreaded) | `True` | Performance | Enable/disable based on measured need | [FUSE client](clients/fuse.md) |
| [`fuse_require_active_mds`](clients/fuse.md#fuse_require_active_mds) | `True` | Performance | Enable/disable based on measured need | [FUSE client](clients/fuse.md) |
| [`fuse_set_user_groups`](clients/fuse.md#fuse_set_user_groups) | `True` | Performance | Enable/disable based on measured need | [FUSE client](clients/fuse.md) |
| [`fuse_splice_move`](clients/fuse.md#fuse_splice_move) | `True` | Performance | Enable/disable based on measured need | [FUSE client](clients/fuse.md) |
| [`fuse_splice_read`](clients/fuse.md#fuse_splice_read) | `True` | Performance | Enable/disable based on measured need | [FUSE client](clients/fuse.md) |
| [`fuse_splice_write`](clients/fuse.md#fuse_splice_write) | `True` | Performance | Enable/disable based on measured need | [FUSE client](clients/fuse.md) |
| [`fuse_syncfs_on_mksnap`](clients/fuse.md#fuse_syncfs_on_mksnap) | `True` | Performance | Enable/disable based on measured need | [FUSE client](clients/fuse.md) |
| [`fuse_use_invalidate_cb`](clients/fuse.md#fuse_use_invalidate_cb) | `True` | Performance | Enable/disable based on measured need | [FUSE client](clients/fuse.md) |
| [`osd_client_watch_timeout`](clients/client.md#osd_client_watch_timeout) | `30` | Dev | Keep upstream default in production | [CephFS client](clients/client.md) |

[← Overview](OVERVIEW.md)
