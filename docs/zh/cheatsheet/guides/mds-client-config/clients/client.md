# CephFS client

MDS client 配置深度指南 — 53 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mds-client/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [client_acl_type](#client_acl_type) | `(empty)` | Advanced | 性能 |
| [client_asio_thread_count](#client_asio_thread_count) | `2` | Advanced | 性能 |
| [client_cache_mid](#client_cache_mid) | `0.75` | Advanced | 性能 |
| [client_cache_size](#client_cache_size) | `16_K` | Basic | 性能 |
| [client_caps_release_delay](#client_caps_release_delay) | `5` | Dev | 开发 |
| [client_check_pool_perm](#client_check_pool_perm) | `True` | Advanced | 性能 |
| [client_collect_and_send_global_metrics](#client_collect_and_send_global_metrics) | `False` | Advanced | 性能 |
| [client_debug_force_sync_read](#client_debug_force_sync_read) | `False` | Dev | 开发 |
| [client_debug_getattr_caps](#client_debug_getattr_caps) | `False` | Dev | 开发 |
| [client_debug_inject_features](#client_debug_inject_features) | `(empty)` | Dev | 开发 |
| [client_debug_inject_tick_delay](#client_debug_inject_tick_delay) | `0` | Dev | 开发 |
| [client_die_on_failed_dentry_invalidate](#client_die_on_failed_dentry_invalidate) | `True` | Advanced | 性能 |
| [client_die_on_failed_remount](#client_die_on_failed_remount) | `False` | Dev | 开发 |
| [client_dirsize_rbytes](#client_dirsize_rbytes) | `True` | Advanced | 性能 |
| [client_file_blockdiff_max_concurrent_object_scans](#client_file_blockdiff_max_concurrent_object_scans) | `16` | Advanced | 性能 |
| [client_force_lazyio](#client_force_lazyio) | `False` | Advanced | 性能 |
| [client_fs](#client_fs) | `(empty)` | Advanced | 性能 |
| [client_fscrypt_as](#client_fscrypt_as) | `True` | Advanced | 性能 |
| [client_fscrypt_dummy_encryption](#client_fscrypt_dummy_encryption) | `False` | Dev | 开发 |
| [client_inject_fixed_oldest_tid](#client_inject_fixed_oldest_tid) | `False` | Dev | 开发 |
| [client_inject_release_failure](#client_inject_release_failure) | `False` | Dev | 开发 |
| [client_inject_write_delay_secs](#client_inject_write_delay_secs) | `0` | Dev | 开发 |
| [client_max_inline_size](#client_max_inline_size) | `4_K` | Dev | 开发 |
| [client_max_retries_on_remount_failure](#client_max_retries_on_remount_failure) | `5` | Advanced | 性能 |
| [client_mds_namespace](#client_mds_namespace) | `(empty)` | Dev | 开发 |
| [client_metadata](#client_metadata) | `(empty)` | Advanced | 性能 |
| [client_mount_gid](#client_mount_gid) | `-1` | Advanced | 性能 |
| [client_mount_timeout](#client_mount_timeout) | `5_min` | Advanced | 性能 |
| [client_mount_uid](#client_mount_uid) | `-1` | Advanced | 性能 |
| [client_mountpoint](#client_mountpoint) | `/` | Advanced | 性能 |
| [client_notify_timeout](#client_notify_timeout) | `10` | Dev | 开发 |
| [client_oc](#client_oc) | `True` | Advanced | 性能 |
| [client_oc_max_dirty](#client_oc_max_dirty) | `100_M` | Advanced | 性能 |
| [client_oc_max_dirty_age](#client_oc_max_dirty_age) | `5` | Advanced | 性能 |
| [client_oc_max_objects](#client_oc_max_objects) | `1000` | Advanced | 性能 |
| [client_oc_size](#client_oc_size) | `200_M` | Advanced | 性能 |
| [client_oc_target_dirty](#client_oc_target_dirty) | `8_M` | Advanced | 性能 |
| [client_permissions](#client_permissions) | `True` | Advanced | 性能 |
| [client_quota](#client_quota) | `True` | Advanced | 性能 |
| [client_quota_df](#client_quota_df) | `True` | Advanced | 性能 |
| [client_readahead_max_bytes](#client_readahead_max_bytes) | `0` | Advanced | 性能 |
| [client_readahead_max_periods](#client_readahead_max_periods) | `4` | Advanced | 性能 |
| [client_readahead_min](#client_readahead_min) | `128_K` | Advanced | 性能 |
| [client_reconnect_stale](#client_reconnect_stale) | `False` | Advanced | 性能 |
| [client_respect_subvolume_snapshot_visibility](#client_respect_subvolume_snapshot_visibility) | `False` | Advanced | 性能 |
| [client_shutdown_timeout](#client_shutdown_timeout) | `30` | Advanced | 性能 |
| [client_snapdir](#client_snapdir) | `.snap` | Advanced | 性能 |
| [client_tick_interval](#client_tick_interval) | `1` | Dev | 开发 |
| [client_trace](#client_trace) | `(empty)` | Dev | 开发 |
| [client_try_dentry_invalidate](#client_try_dentry_invalidate) | `False` | Dev | 开发 |
| [client_use_faked_inos](#client_use_faked_inos) | `False` | Dev | 开发 |
| [client_use_random_mds](#client_use_random_mds) | `False` | Dev | 开发 |
| [osd_client_watch_timeout](#osd_client_watch_timeout) | `30` | Dev | 开发 |

## 寻找最优值

| 模型 | 如何选择 |
|-------|---------------|
| **策略** | 安全、兼容性、运维默认值 |
| **容量** | 磁盘布局、路径、容量规划 |
| **性能** | 基线 → 逐步调整 → 监控集群 |
| **连通性** | 最近且稳定的外部端点 |
| **开发** | 生产环境保持 upstream 默认值 |

**常用工具：**

```bash
ceph config get <daemon> <option>  # e.g. mds-client
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### client_acl_type

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [client.md#SP_client_acl_type](../../../config/mds-client/client.md#SP_client_acl_type) |

**作用：** ACL type to enforce (none or "posix_acl")

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client client_acl_type "example"
ceph config get client client_acl_type
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_acl_type
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_asio_thread_count

| | |
|---|---|
| 类型 | Uint · default `2` · **Advanced** |
| 表格 | [client.md#SP_client_asio_thread_count](../../../config/mds-client/client.md#SP_client_asio_thread_count) |

**作用：** Size of thread pool for ASIO completions

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client client_asio_thread_count 2
ceph config get client client_asio_thread_count
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_asio_thread_count
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_cache_mid

| | |
|---|---|
| 类型 | Float · default `0.75` · **Advanced** |
| 表格 | [client.md#SP_client_cache_mid](../../../config/mds-client/client.md#SP_client_cache_mid) |

**作用：** mid-point of client cache LRU

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client client_cache_mid 0.75
ceph config get client client_cache_mid
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.75` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_cache_mid
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_cache_size

| | |
|---|---|
| 类型 | Size · default `16_K` · **Basic** |
| 表格 | [client.md#SP_client_cache_size](../../../config/mds-client/client.md#SP_client_cache_size) |

**作用：** soft maximum number of directory entries in client cache

**何时使用：** 核心 MDS client 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set client client_cache_size 16_K
ceph config get client client_cache_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `16_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_cache_size
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_caps_release_delay

| | |
|---|---|
| 类型 | Secs · default `5` · **Dev** |
| 表格 | [client.md#SP_client_caps_release_delay](../../../config/mds-client/client.md#SP_client_caps_release_delay) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client client_caps_release_delay 5
ceph config get client client_caps_release_delay
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`5`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### client_check_pool_perm

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [client.md#SP_client_check_pool_perm](../../../config/mds-client/client.md#SP_client_check_pool_perm) |

**作用：** confirm access to inode's data pool/namespace described in file layout

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client client_check_pool_perm false
ceph config get client client_check_pool_perm
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_check_pool_perm
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_collect_and_send_global_metrics

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [client.md#SP_client_collect_and_send_global_metrics](../../../config/mds-client/client.md#SP_client_collect_and_send_global_metrics) |

**作用：** to enable and force collecting and sending the global metrics to MDS

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client client_collect_and_send_global_metrics true
ceph config get client client_collect_and_send_global_metrics
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_collect_and_send_global_metrics
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_debug_force_sync_read

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [client.md#SP_client_debug_force_sync_read](../../../config/mds-client/client.md#SP_client_debug_force_sync_read) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client client_debug_force_sync_read true
ceph config get client client_debug_force_sync_read
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### client_debug_getattr_caps

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [client.md#SP_client_debug_getattr_caps](../../../config/mds-client/client.md#SP_client_debug_getattr_caps) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client client_debug_getattr_caps true
ceph config get client client_debug_getattr_caps
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### client_debug_inject_features

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Dev** · **STARTUP**（需重启） |
| 表格 | [client.md#SP_client_debug_inject_features](../../../config/mds-client/client.md#SP_client_debug_inject_features) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client client_debug_inject_features "example"
ceph config get client client_debug_inject_features
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`(empty)`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### client_debug_inject_tick_delay

| | |
|---|---|
| 类型 | Secs · default `0` · **Dev** |
| 表格 | [client.md#SP_client_debug_inject_tick_delay](../../../config/mds-client/client.md#SP_client_debug_inject_tick_delay) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client client_debug_inject_tick_delay 0
ceph config get client client_debug_inject_tick_delay
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### client_die_on_failed_dentry_invalidate

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [client.md#SP_client_die_on_failed_dentry_invalidate](../../../config/mds-client/client.md#SP_client_die_on_failed_dentry_invalidate) |

**作用：** kill the client when no dentry invalidation options are available

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client client_die_on_failed_dentry_invalidate false
ceph config get client client_die_on_failed_dentry_invalidate
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_die_on_failed_dentry_invalidate
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_die_on_failed_remount

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [client.md#SP_client_die_on_failed_remount](../../../config/mds-client/client.md#SP_client_die_on_failed_remount) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client client_die_on_failed_remount true
ceph config get client client_die_on_failed_remount
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### client_dirsize_rbytes

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [client.md#SP_client_dirsize_rbytes](../../../config/mds-client/client.md#SP_client_dirsize_rbytes) |

**作用：** set the directory size as the number of file bytes recursively used

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client client_dirsize_rbytes false
ceph config get client client_dirsize_rbytes
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_dirsize_rbytes
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_file_blockdiff_max_concurrent_object_scans

| | |
|---|---|
| 类型 | Uint · default `16` · **Advanced** |
| 表格 | [client.md#SP_client_file_blockdiff_max_concurrent_object_scans](../../../config/mds-client/client.md#SP_client_file_blockdiff_max_concurrent_object_scans) |

**作用：** maximum number of concurrent object scans

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client client_file_blockdiff_max_concurrent_object_scans 16
ceph config get client client_file_blockdiff_max_concurrent_object_scans
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `16` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_file_blockdiff_max_concurrent_object_scans
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_force_lazyio

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [client.md#SP_client_force_lazyio](../../../config/mds-client/client.md#SP_client_force_lazyio) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client client_force_lazyio true
ceph config get client client_force_lazyio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_force_lazyio
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_fs

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [client.md#SP_client_fs](../../../config/mds-client/client.md#SP_client_fs) |

**作用：** CephFS file system name to mount

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client client_fs "example"
ceph config get client client_fs
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_fs
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_fscrypt_as

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [client.md#SP_client_fscrypt_as](../../../config/mds-client/client.md#SP_client_fscrypt_as) |

**作用：** Enable fscrypt access semantics

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client client_fscrypt_as false
ceph config get client client_fscrypt_as
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_fscrypt_as
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_fscrypt_dummy_encryption

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [client.md#SP_client_fscrypt_dummy_encryption](../../../config/mds-client/client.md#SP_client_fscrypt_dummy_encryption) |

**作用：** Enable fscrypt dummy encryption

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client client_fscrypt_dummy_encryption true
ceph config get client client_fscrypt_dummy_encryption
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### client_inject_fixed_oldest_tid

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [client.md#SP_client_inject_fixed_oldest_tid](../../../config/mds-client/client.md#SP_client_inject_fixed_oldest_tid) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client client_inject_fixed_oldest_tid true
ceph config get client client_inject_fixed_oldest_tid
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### client_inject_release_failure

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [client.md#SP_client_inject_release_failure](../../../config/mds-client/client.md#SP_client_inject_release_failure) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client client_inject_release_failure true
ceph config get client client_inject_release_failure
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### client_inject_write_delay_secs

| | |
|---|---|
| 类型 | Secs · default `0` · **Dev** |
| 表格 | [client.md#SP_client_inject_write_delay_secs](../../../config/mds-client/client.md#SP_client_inject_write_delay_secs) |

**作用：** induce delay in write operation for testing

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client client_inject_write_delay_secs 0
ceph config get client client_inject_write_delay_secs
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### client_max_inline_size

| | |
|---|---|
| 类型 | Size · default `4_K` · **Dev** |
| 表格 | [client.md#SP_client_max_inline_size](../../../config/mds-client/client.md#SP_client_max_inline_size) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client client_max_inline_size 4_K
ceph config get client client_max_inline_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`4_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### client_max_retries_on_remount_failure

| | |
|---|---|
| 类型 | Uint · default `5` · **Advanced** |
| 表格 | [client.md#SP_client_max_retries_on_remount_failure](../../../config/mds-client/client.md#SP_client_max_retries_on_remount_failure) |

**作用：** number of consecutive failed remount attempts for invalidating kernel dcache after which client would abort.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client client_max_retries_on_remount_failure 5
ceph config get client client_max_retries_on_remount_failure
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_max_retries_on_remount_failure
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_mds_namespace

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Dev** · **STARTUP**（需重启） |
| 表格 | [client.md#SP_client_mds_namespace](../../../config/mds-client/client.md#SP_client_mds_namespace) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client client_mds_namespace "example"
ceph config get client client_mds_namespace
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`(empty)`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### client_metadata

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [client.md#SP_client_metadata](../../../config/mds-client/client.md#SP_client_metadata) |

**作用：** metadata key=value comma-delimited pairs appended to session metadata

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client client_metadata "example"
ceph config get client client_metadata
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_metadata
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_mount_gid

| | |
|---|---|
| 类型 | Int · default `-1` · **Advanced** |
| 表格 | [client.md#SP_client_mount_gid](../../../config/mds-client/client.md#SP_client_mount_gid) |

**作用：** gid to mount as

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client client_mount_gid 128
ceph config get client client_mount_gid
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `-1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_mount_gid
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_mount_timeout

| | |
|---|---|
| 类型 | Secs · default `5_min` · **Advanced** |
| 表格 | [client.md#SP_client_mount_timeout](../../../config/mds-client/client.md#SP_client_mount_timeout) |

**作用：** timeout for mounting CephFS (seconds)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set client client_mount_timeout 5_min
ceph config get client client_mount_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_mount_timeout
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_mount_uid

| | |
|---|---|
| 类型 | Int · default `-1` · **Advanced** |
| 表格 | [client.md#SP_client_mount_uid](../../../config/mds-client/client.md#SP_client_mount_uid) |

**作用：** uid to mount as

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client client_mount_uid 128
ceph config get client client_mount_uid
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `-1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_mount_uid
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_mountpoint

| | |
|---|---|
| 类型 | Str · default `/` · **Advanced** |
| 表格 | [client.md#SP_client_mountpoint](../../../config/mds-client/client.md#SP_client_mountpoint) |

**作用：** default mount-point

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client client_mountpoint "/"
ceph config get client client_mountpoint
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `/` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_mountpoint
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_notify_timeout

| | |
|---|---|
| 类型 | Int · default `10` · **Dev** |
| 表格 | [client.md#SP_client_notify_timeout](../../../config/mds-client/client.md#SP_client_notify_timeout) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client client_notify_timeout 10
ceph config get client client_notify_timeout
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`10`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### client_oc

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [client.md#SP_client_oc](../../../config/mds-client/client.md#SP_client_oc) |

**作用：** enable object caching

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client client_oc false
ceph config get client client_oc
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_oc
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_oc_max_dirty

| | |
|---|---|
| 类型 | Size · default `100_M` · **Advanced** |
| 表格 | [client.md#SP_client_oc_max_dirty](../../../config/mds-client/client.md#SP_client_oc_max_dirty) |

**作用：** maximum size of dirty pages in object cache

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client client_oc_max_dirty 100_M
ceph config get client client_oc_max_dirty
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `100_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_oc_max_dirty
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_oc_max_dirty_age

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [client.md#SP_client_oc_max_dirty_age](../../../config/mds-client/client.md#SP_client_oc_max_dirty_age) |

**作用：** maximum age of dirty pages in object cache (seconds)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client client_oc_max_dirty_age 5
ceph config get client client_oc_max_dirty_age
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_oc_max_dirty_age
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_oc_max_objects

| | |
|---|---|
| 类型 | Int · default `1000` · **Advanced** |
| 表格 | [client.md#SP_client_oc_max_objects](../../../config/mds-client/client.md#SP_client_oc_max_objects) |

**作用：** maximum number of objects in cache

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client client_oc_max_objects 1000
ceph config get client client_oc_max_objects
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_oc_max_objects
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_oc_size

| | |
|---|---|
| 类型 | Size · default `200_M` · **Advanced** |
| 表格 | [client.md#SP_client_oc_size](../../../config/mds-client/client.md#SP_client_oc_size) |

**作用：** maximum size of object cache

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client client_oc_size 200_M
ceph config get client client_oc_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `200_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_oc_size
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_oc_target_dirty

| | |
|---|---|
| 类型 | Size · default `8_M` · **Advanced** |
| 表格 | [client.md#SP_client_oc_target_dirty](../../../config/mds-client/client.md#SP_client_oc_target_dirty) |

**作用：** target size of dirty pages object cache

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client client_oc_target_dirty 8_M
ceph config get client client_oc_target_dirty
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `8_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_oc_target_dirty
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_permissions

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [client.md#SP_client_permissions](../../../config/mds-client/client.md#SP_client_permissions) |

**作用：** client-enforced permission checking

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client client_permissions false
ceph config get client client_permissions
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_permissions
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_quota

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [client.md#SP_client_quota](../../../config/mds-client/client.md#SP_client_quota) |

**作用：** Enable quota enforcement

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client client_quota false
ceph config get client client_quota
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_quota
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_quota_df

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [client.md#SP_client_quota_df](../../../config/mds-client/client.md#SP_client_quota_df) |

**作用：** show quota usage for statfs (df)

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client client_quota_df false
ceph config get client client_quota_df
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_quota_df
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_readahead_max_bytes

| | |
|---|---|
| 类型 | Size · default `0` · **Advanced** |
| 表格 | [client.md#SP_client_readahead_max_bytes](../../../config/mds-client/client.md#SP_client_readahead_max_bytes) |

**作用：** maximum bytes to readahead in a file (zero is unlimited)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client client_readahead_max_bytes 64
ceph config get client client_readahead_max_bytes
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_readahead_max_bytes
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_readahead_max_periods

| | |
|---|---|
| 类型 | Int · default `4` · **Advanced** |
| 表格 | [client.md#SP_client_readahead_max_periods](../../../config/mds-client/client.md#SP_client_readahead_max_periods) |

**作用：** maximum stripe periods to readahead in a file

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client client_readahead_max_periods 4
ceph config get client client_readahead_max_periods
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `4` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_readahead_max_periods
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_readahead_min

| | |
|---|---|
| 类型 | Size · default `128_K` · **Advanced** |
| 表格 | [client.md#SP_client_readahead_min](../../../config/mds-client/client.md#SP_client_readahead_min) |

**作用：** minimum bytes to readahead in a file

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client client_readahead_min 128_K
ceph config get client client_readahead_min
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `128_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_readahead_min
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_reconnect_stale

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [client.md#SP_client_reconnect_stale](../../../config/mds-client/client.md#SP_client_reconnect_stale) |

**作用：** reconnect when the session becomes stale

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client client_reconnect_stale true
ceph config get client client_reconnect_stale
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_reconnect_stale
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_respect_subvolume_snapshot_visibility

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [client.md#SP_client_respect_subvolume_snapshot_visibility](../../../config/mds-client/client.md#SP_client_respect_subvolume_snapshot_visibility) |

**作用：** Respect subvolume snapshot visibility

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client client_respect_subvolume_snapshot_visibility true
ceph config get client client_respect_subvolume_snapshot_visibility
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_respect_subvolume_snapshot_visibility
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_shutdown_timeout

| | |
|---|---|
| 类型 | Secs · default `30` · **Advanced** |
| 表格 | [client.md#SP_client_shutdown_timeout](../../../config/mds-client/client.md#SP_client_shutdown_timeout) |

**作用：** timeout for shutting down CephFS

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set client client_shutdown_timeout 30
ceph config get client client_shutdown_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_shutdown_timeout
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_snapdir

| | |
|---|---|
| 类型 | Str · default `.snap` · **Advanced** |
| 表格 | [client.md#SP_client_snapdir](../../../config/mds-client/client.md#SP_client_snapdir) |

**作用：** pseudo directory for snapshot access to a directory

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client client_snapdir ".snap"
ceph config get client client_snapdir
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `.snap` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client client_snapdir
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### client_tick_interval

| | |
|---|---|
| 类型 | Secs · default `1` · **Dev** |
| 表格 | [client.md#SP_client_tick_interval](../../../config/mds-client/client.md#SP_client_tick_interval) |

**作用：** seconds between client upkeep ticks

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client client_tick_interval 1
ceph config get client client_tick_interval
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### client_trace

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Dev** |
| 表格 | [client.md#SP_client_trace](../../../config/mds-client/client.md#SP_client_trace) |

**作用：** file containing trace of client operations

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client client_trace "example"
ceph config get client client_trace
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`(empty)`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### client_try_dentry_invalidate

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [client.md#SP_client_try_dentry_invalidate](../../../config/mds-client/client.md#SP_client_try_dentry_invalidate) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client client_try_dentry_invalidate true
ceph config get client client_try_dentry_invalidate
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### client_use_faked_inos

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** · **STARTUP**（需重启） |
| 表格 | [client.md#SP_client_use_faked_inos](../../../config/mds-client/client.md#SP_client_use_faked_inos) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client client_use_faked_inos true
ceph config get client client_use_faked_inos
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### client_use_random_mds

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [client.md#SP_client_use_random_mds](../../../config/mds-client/client.md#SP_client_use_random_mds) |

**作用：** issue new requests to a random active MDS

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client client_use_random_mds true
ceph config get client client_use_random_mds
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_client_watch_timeout

| | |
|---|---|
| 类型 | Int · default `30` · **Dev** |
| 表格 | [osd.md#SP_osd_client_watch_timeout](../../../config/mds-client/osd.md#SP_osd_client_watch_timeout) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_client_watch_timeout 30
ceph config get osd osd_client_watch_timeout
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`30`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
