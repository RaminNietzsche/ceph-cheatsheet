# MDS client 配置 — 调优快速参考

全部 **70** 个选项的调优模型与一行建议。

[← 概览](../OVERVIEW.md)

| 选项 | 默认值 | 模型 | 快速建议 | 主题 |
|--------|---------|-------|--------------|-------|
| [`client_acl_type`](clients/client.md#client_acl_type) | `(empty)` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_asio_thread_count`](clients/client.md#client_asio_thread_count) | `2` | 性能 | 保持在文档边界内 | [CephFS client](clients/client.md) |
| [`client_cache_mid`](clients/client.md#client_cache_mid) | `0.75` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_cache_size`](clients/client.md#client_cache_size) | `16_K` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_caps_release_delay`](clients/client.md#client_caps_release_delay) | `5` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |
| [`client_check_pool_perm`](clients/client.md#client_check_pool_perm) | `True` | 性能 | 按实测需求启用/禁用 | [CephFS client](clients/client.md) |
| [`client_collect_and_send_global_metrics`](clients/client.md#client_collect_and_send_global_metrics) | `False` | 性能 | 按实测需求启用/禁用 | [CephFS client](clients/client.md) |
| [`client_debug_force_sync_read`](clients/client.md#client_debug_force_sync_read) | `False` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |
| [`client_debug_getattr_caps`](clients/client.md#client_debug_getattr_caps) | `False` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |
| [`client_debug_inject_features`](clients/client.md#client_debug_inject_features) | `(empty)` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |
| [`client_debug_inject_tick_delay`](clients/client.md#client_debug_inject_tick_delay) | `0` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |
| [`client_die_on_failed_dentry_invalidate`](clients/client.md#client_die_on_failed_dentry_invalidate) | `True` | 性能 | 按实测需求启用/禁用 | [CephFS client](clients/client.md) |
| [`client_die_on_failed_remount`](clients/client.md#client_die_on_failed_remount) | `False` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |
| [`client_dirsize_rbytes`](clients/client.md#client_dirsize_rbytes) | `True` | 性能 | 按实测需求启用/禁用 | [CephFS client](clients/client.md) |
| [`client_file_blockdiff_max_concurrent_object_scans`](clients/client.md#client_file_blockdiff_max_concurrent_object_scans) | `16` | 性能 | 保持在文档边界内 | [CephFS client](clients/client.md) |
| [`client_force_lazyio`](clients/client.md#client_force_lazyio) | `False` | 性能 | 按实测需求启用/禁用 | [CephFS client](clients/client.md) |
| [`client_fs`](clients/client.md#client_fs) | `(empty)` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_fscrypt_as`](clients/client.md#client_fscrypt_as) | `True` | 性能 | 按实测需求启用/禁用 | [CephFS client](clients/client.md) |
| [`client_fscrypt_dummy_encryption`](clients/client.md#client_fscrypt_dummy_encryption) | `False` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |
| [`client_inject_fixed_oldest_tid`](clients/client.md#client_inject_fixed_oldest_tid) | `False` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |
| [`client_inject_release_failure`](clients/client.md#client_inject_release_failure) | `False` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |
| [`client_inject_write_delay_secs`](clients/client.md#client_inject_write_delay_secs) | `0` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |
| [`client_max_inline_size`](clients/client.md#client_max_inline_size) | `4_K` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |
| [`client_max_retries_on_remount_failure`](clients/client.md#client_max_retries_on_remount_failure) | `5` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_mds_namespace`](clients/client.md#client_mds_namespace) | `(empty)` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |
| [`client_metadata`](clients/client.md#client_metadata) | `(empty)` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_mount_gid`](clients/client.md#client_mount_gid) | `-1` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_mount_timeout`](clients/client.md#client_mount_timeout) | `5_min` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_mount_uid`](clients/client.md#client_mount_uid) | `-1` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_mountpoint`](clients/client.md#client_mountpoint) | `/` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_notify_timeout`](clients/client.md#client_notify_timeout) | `10` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |
| [`client_oc`](clients/client.md#client_oc) | `True` | 性能 | 按实测需求启用/禁用 | [CephFS client](clients/client.md) |
| [`client_oc_max_dirty`](clients/client.md#client_oc_max_dirty) | `100_M` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_oc_max_dirty_age`](clients/client.md#client_oc_max_dirty_age) | `5` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_oc_max_objects`](clients/client.md#client_oc_max_objects) | `1000` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_oc_size`](clients/client.md#client_oc_size) | `200_M` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_oc_target_dirty`](clients/client.md#client_oc_target_dirty) | `8_M` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_permissions`](clients/client.md#client_permissions) | `True` | 性能 | 按实测需求启用/禁用 | [CephFS client](clients/client.md) |
| [`client_quota`](clients/client.md#client_quota) | `True` | 性能 | 按实测需求启用/禁用 | [CephFS client](clients/client.md) |
| [`client_quota_df`](clients/client.md#client_quota_df) | `True` | 性能 | 按实测需求启用/禁用 | [CephFS client](clients/client.md) |
| [`client_readahead_max_bytes`](clients/client.md#client_readahead_max_bytes) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_readahead_max_periods`](clients/client.md#client_readahead_max_periods) | `4` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_readahead_min`](clients/client.md#client_readahead_min) | `128_K` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_reconnect_stale`](clients/client.md#client_reconnect_stale) | `False` | 性能 | 按实测需求启用/禁用 | [CephFS client](clients/client.md) |
| [`client_respect_subvolume_snapshot_visibility`](clients/client.md#client_respect_subvolume_snapshot_visibility) | `False` | 性能 | 按实测需求启用/禁用 | [CephFS client](clients/client.md) |
| [`client_shutdown_timeout`](clients/client.md#client_shutdown_timeout) | `30` | 性能 | 保持在文档边界内 | [CephFS client](clients/client.md) |
| [`client_snapdir`](clients/client.md#client_snapdir) | `.snap` | 性能 | 基线 → 调整 → 负载下验证 | [CephFS client](clients/client.md) |
| [`client_tick_interval`](clients/client.md#client_tick_interval) | `1` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |
| [`client_trace`](clients/client.md#client_trace) | `(empty)` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |
| [`client_try_dentry_invalidate`](clients/client.md#client_try_dentry_invalidate) | `False` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |
| [`client_use_faked_inos`](clients/client.md#client_use_faked_inos) | `False` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |
| [`client_use_random_mds`](clients/client.md#client_use_random_mds) | `False` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |
| [`debug_allow_any_pool_priority`](other/debug.md#debug_allow_any_pool_priority) | `False` | 开发 | 生产环境保持 upstream 默认值 | [Debug](other/debug.md) |
| [`fake_statfs_for_testing`](other/general.md#fake_statfs_for_testing) | `0` | 开发 | 生产环境保持 upstream 默认值 | [General](other/general.md) |
| [`fuse_allow_other`](clients/fuse.md#fuse_allow_other) | `True` | 策略 | 符合安全与兼容性策略 | [FUSE client](clients/fuse.md) |
| [`fuse_atomic_o_trunc`](clients/fuse.md#fuse_atomic_o_trunc) | `True` | 性能 | 按实测需求启用/禁用 | [FUSE client](clients/fuse.md) |
| [`fuse_big_writes`](clients/fuse.md#fuse_big_writes) | `True` | 性能 | 按实测需求启用/禁用 | [FUSE client](clients/fuse.md) |
| [`fuse_debug`](clients/fuse.md#fuse_debug) | `False` | 性能 | 按实测需求启用/禁用 | [FUSE client](clients/fuse.md) |
| [`fuse_default_permissions`](clients/fuse.md#fuse_default_permissions) | `False` | 性能 | 按实测需求启用/禁用 | [FUSE client](clients/fuse.md) |
| [`fuse_disable_pagecache`](clients/fuse.md#fuse_disable_pagecache) | `False` | 策略 | 符合安全与兼容性策略 | [FUSE client](clients/fuse.md) |
| [`fuse_max_write`](clients/fuse.md#fuse_max_write) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [FUSE client](clients/fuse.md) |
| [`fuse_multithreaded`](clients/fuse.md#fuse_multithreaded) | `True` | 性能 | 按实测需求启用/禁用 | [FUSE client](clients/fuse.md) |
| [`fuse_require_active_mds`](clients/fuse.md#fuse_require_active_mds) | `True` | 性能 | 按实测需求启用/禁用 | [FUSE client](clients/fuse.md) |
| [`fuse_set_user_groups`](clients/fuse.md#fuse_set_user_groups) | `True` | 性能 | 按实测需求启用/禁用 | [FUSE client](clients/fuse.md) |
| [`fuse_splice_move`](clients/fuse.md#fuse_splice_move) | `True` | 性能 | 按实测需求启用/禁用 | [FUSE client](clients/fuse.md) |
| [`fuse_splice_read`](clients/fuse.md#fuse_splice_read) | `True` | 性能 | 按实测需求启用/禁用 | [FUSE client](clients/fuse.md) |
| [`fuse_splice_write`](clients/fuse.md#fuse_splice_write) | `True` | 性能 | 按实测需求启用/禁用 | [FUSE client](clients/fuse.md) |
| [`fuse_syncfs_on_mksnap`](clients/fuse.md#fuse_syncfs_on_mksnap) | `True` | 性能 | 按实测需求启用/禁用 | [FUSE client](clients/fuse.md) |
| [`fuse_use_invalidate_cb`](clients/fuse.md#fuse_use_invalidate_cb) | `True` | 性能 | 按实测需求启用/禁用 | [FUSE client](clients/fuse.md) |
| [`osd_client_watch_timeout`](clients/client.md#osd_client_watch_timeout) | `30` | 开发 | 生产环境保持 upstream 默认值 | [CephFS client](clients/client.md) |

[← 概览](../OVERVIEW.md)
