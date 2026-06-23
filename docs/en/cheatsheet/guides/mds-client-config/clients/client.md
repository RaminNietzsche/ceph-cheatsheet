# CephFS client

MDS client config deep dive — 53 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mds-client/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [client_acl_type](#client_acl_type) | `(empty)` | Advanced | Performance |
| [client_asio_thread_count](#client_asio_thread_count) | `2` | Advanced | Performance |
| [client_cache_mid](#client_cache_mid) | `0.75` | Advanced | Performance |
| [client_cache_size](#client_cache_size) | `16_K` | Basic | Performance |
| [client_caps_release_delay](#client_caps_release_delay) | `5` | Dev | Dev |
| [client_check_pool_perm](#client_check_pool_perm) | `True` | Advanced | Performance |
| [client_collect_and_send_global_metrics](#client_collect_and_send_global_metrics) | `False` | Advanced | Performance |
| [client_debug_force_sync_read](#client_debug_force_sync_read) | `False` | Dev | Dev |
| [client_debug_getattr_caps](#client_debug_getattr_caps) | `False` | Dev | Dev |
| [client_debug_inject_features](#client_debug_inject_features) | `(empty)` | Dev | Dev |
| [client_debug_inject_tick_delay](#client_debug_inject_tick_delay) | `0` | Dev | Dev |
| [client_die_on_failed_dentry_invalidate](#client_die_on_failed_dentry_invalidate) | `True` | Advanced | Performance |
| [client_die_on_failed_remount](#client_die_on_failed_remount) | `False` | Dev | Dev |
| [client_dirsize_rbytes](#client_dirsize_rbytes) | `True` | Advanced | Performance |
| [client_file_blockdiff_max_concurrent_object_scans](#client_file_blockdiff_max_concurrent_object_scans) | `16` | Advanced | Performance |
| [client_force_lazyio](#client_force_lazyio) | `False` | Advanced | Performance |
| [client_fs](#client_fs) | `(empty)` | Advanced | Performance |
| [client_fscrypt_as](#client_fscrypt_as) | `True` | Advanced | Performance |
| [client_fscrypt_dummy_encryption](#client_fscrypt_dummy_encryption) | `False` | Dev | Dev |
| [client_inject_fixed_oldest_tid](#client_inject_fixed_oldest_tid) | `False` | Dev | Dev |
| [client_inject_release_failure](#client_inject_release_failure) | `False` | Dev | Dev |
| [client_inject_write_delay_secs](#client_inject_write_delay_secs) | `0` | Dev | Dev |
| [client_max_inline_size](#client_max_inline_size) | `4_K` | Dev | Dev |
| [client_max_retries_on_remount_failure](#client_max_retries_on_remount_failure) | `5` | Advanced | Performance |
| [client_mds_namespace](#client_mds_namespace) | `(empty)` | Dev | Dev |
| [client_metadata](#client_metadata) | `(empty)` | Advanced | Performance |
| [client_mount_gid](#client_mount_gid) | `-1` | Advanced | Performance |
| [client_mount_timeout](#client_mount_timeout) | `5_min` | Advanced | Performance |
| [client_mount_uid](#client_mount_uid) | `-1` | Advanced | Performance |
| [client_mountpoint](#client_mountpoint) | `/` | Advanced | Performance |
| [client_notify_timeout](#client_notify_timeout) | `10` | Dev | Dev |
| [client_oc](#client_oc) | `True` | Advanced | Performance |
| [client_oc_max_dirty](#client_oc_max_dirty) | `100_M` | Advanced | Performance |
| [client_oc_max_dirty_age](#client_oc_max_dirty_age) | `5` | Advanced | Performance |
| [client_oc_max_objects](#client_oc_max_objects) | `1000` | Advanced | Performance |
| [client_oc_size](#client_oc_size) | `200_M` | Advanced | Performance |
| [client_oc_target_dirty](#client_oc_target_dirty) | `8_M` | Advanced | Performance |
| [client_permissions](#client_permissions) | `True` | Advanced | Performance |
| [client_quota](#client_quota) | `True` | Advanced | Performance |
| [client_quota_df](#client_quota_df) | `True` | Advanced | Performance |
| [client_readahead_max_bytes](#client_readahead_max_bytes) | `0` | Advanced | Performance |
| [client_readahead_max_periods](#client_readahead_max_periods) | `4` | Advanced | Performance |
| [client_readahead_min](#client_readahead_min) | `128_K` | Advanced | Performance |
| [client_reconnect_stale](#client_reconnect_stale) | `False` | Advanced | Performance |
| [client_respect_subvolume_snapshot_visibility](#client_respect_subvolume_snapshot_visibility) | `False` | Advanced | Performance |
| [client_shutdown_timeout](#client_shutdown_timeout) | `30` | Advanced | Performance |
| [client_snapdir](#client_snapdir) | `.snap` | Advanced | Performance |
| [client_tick_interval](#client_tick_interval) | `1` | Dev | Dev |
| [client_trace](#client_trace) | `(empty)` | Dev | Dev |
| [client_try_dentry_invalidate](#client_try_dentry_invalidate) | `False` | Dev | Dev |
| [client_use_faked_inos](#client_use_faked_inos) | `False` | Dev | Dev |
| [client_use_random_mds](#client_use_random_mds) | `False` | Dev | Dev |
| [osd_client_watch_timeout](#osd_client_watch_timeout) | `30` | Dev | Dev |

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, compatibility, operational defaults |
| **Capacity** | Disk layout, paths, sizing |
| **Performance** | Baseline → incremental change → monitor cluster |
| **Connectivity** | Nearest stable external endpoint |
| **Dev** | Keep upstream default in production |

**Shared tooling:**

```bash
ceph config get <daemon> <option>  # e.g. mds-client
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### client_acl_type

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [client.md#SP_client_acl_type](../../../config/mds-client/client.md#SP_client_acl_type) |

**What it does:** ACL type to enforce (none or "posix_acl")

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client client_acl_type "example"
ceph config get client client_acl_type
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_acl_type
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_asio_thread_count

| | |
|---|---|
| Type | Uint · default `2` · **Advanced** |
| Table | [client.md#SP_client_asio_thread_count](../../../config/mds-client/client.md#SP_client_asio_thread_count) |

**What it does:** Size of thread pool for ASIO completions

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client client_asio_thread_count 2
ceph config get client client_asio_thread_count
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_asio_thread_count
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_cache_mid

| | |
|---|---|
| Type | Float · default `0.75` · **Advanced** |
| Table | [client.md#SP_client_cache_mid](../../../config/mds-client/client.md#SP_client_cache_mid) |

**What it does:** mid-point of client cache LRU

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client client_cache_mid 0.75
ceph config get client client_cache_mid
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.75`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_cache_mid
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_cache_size

| | |
|---|---|
| Type | Size · default `16_K` · **Basic** |
| Table | [client.md#SP_client_cache_size](../../../config/mds-client/client.md#SP_client_cache_size) |

**What it does:** soft maximum number of directory entries in client cache

**When to use:** Core MDS client behavior — review before changing in production.

**Example:**

```bash
ceph config set client client_cache_size 16_K
ceph config get client client_cache_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `16_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_cache_size
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_caps_release_delay

| | |
|---|---|
| Type | Secs · default `5` · **Dev** |
| Table | [client.md#SP_client_caps_release_delay](../../../config/mds-client/client.md#SP_client_caps_release_delay) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client client_caps_release_delay 5
ceph config get client client_caps_release_delay
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`5`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### client_check_pool_perm

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [client.md#SP_client_check_pool_perm](../../../config/mds-client/client.md#SP_client_check_pool_perm) |

**What it does:** confirm access to inode's data pool/namespace described in file layout

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client client_check_pool_perm false
ceph config get client client_check_pool_perm
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_check_pool_perm
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_collect_and_send_global_metrics

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [client.md#SP_client_collect_and_send_global_metrics](../../../config/mds-client/client.md#SP_client_collect_and_send_global_metrics) |

**What it does:** to enable and force collecting and sending the global metrics to MDS

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client client_collect_and_send_global_metrics true
ceph config get client client_collect_and_send_global_metrics
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_collect_and_send_global_metrics
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_debug_force_sync_read

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [client.md#SP_client_debug_force_sync_read](../../../config/mds-client/client.md#SP_client_debug_force_sync_read) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client client_debug_force_sync_read true
ceph config get client client_debug_force_sync_read
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### client_debug_getattr_caps

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [client.md#SP_client_debug_getattr_caps](../../../config/mds-client/client.md#SP_client_debug_getattr_caps) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client client_debug_getattr_caps true
ceph config get client client_debug_getattr_caps
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### client_debug_inject_features

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** · **STARTUP** (restart required) |
| Table | [client.md#SP_client_debug_inject_features](../../../config/mds-client/client.md#SP_client_debug_inject_features) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client client_debug_inject_features "example"
ceph config get client client_debug_inject_features
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`(empty)`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### client_debug_inject_tick_delay

| | |
|---|---|
| Type | Secs · default `0` · **Dev** |
| Table | [client.md#SP_client_debug_inject_tick_delay](../../../config/mds-client/client.md#SP_client_debug_inject_tick_delay) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client client_debug_inject_tick_delay 0
ceph config get client client_debug_inject_tick_delay
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### client_die_on_failed_dentry_invalidate

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [client.md#SP_client_die_on_failed_dentry_invalidate](../../../config/mds-client/client.md#SP_client_die_on_failed_dentry_invalidate) |

**What it does:** kill the client when no dentry invalidation options are available

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client client_die_on_failed_dentry_invalidate false
ceph config get client client_die_on_failed_dentry_invalidate
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_die_on_failed_dentry_invalidate
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_die_on_failed_remount

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [client.md#SP_client_die_on_failed_remount](../../../config/mds-client/client.md#SP_client_die_on_failed_remount) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client client_die_on_failed_remount true
ceph config get client client_die_on_failed_remount
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### client_dirsize_rbytes

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** · **STARTUP** (restart required) |
| Table | [client.md#SP_client_dirsize_rbytes](../../../config/mds-client/client.md#SP_client_dirsize_rbytes) |

**What it does:** set the directory size as the number of file bytes recursively used

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client client_dirsize_rbytes false
ceph config get client client_dirsize_rbytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_dirsize_rbytes
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_file_blockdiff_max_concurrent_object_scans

| | |
|---|---|
| Type | Uint · default `16` · **Advanced** |
| Table | [client.md#SP_client_file_blockdiff_max_concurrent_object_scans](../../../config/mds-client/client.md#SP_client_file_blockdiff_max_concurrent_object_scans) |

**What it does:** maximum number of concurrent object scans

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client client_file_blockdiff_max_concurrent_object_scans 16
ceph config get client client_file_blockdiff_max_concurrent_object_scans
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `16`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_file_blockdiff_max_concurrent_object_scans
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_force_lazyio

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** · **STARTUP** (restart required) |
| Table | [client.md#SP_client_force_lazyio](../../../config/mds-client/client.md#SP_client_force_lazyio) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client client_force_lazyio true
ceph config get client client_force_lazyio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_force_lazyio
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_fs

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** · **STARTUP** (restart required) |
| Table | [client.md#SP_client_fs](../../../config/mds-client/client.md#SP_client_fs) |

**What it does:** CephFS file system name to mount

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client client_fs "example"
ceph config get client client_fs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_fs
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_fscrypt_as

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [client.md#SP_client_fscrypt_as](../../../config/mds-client/client.md#SP_client_fscrypt_as) |

**What it does:** Enable fscrypt access semantics

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client client_fscrypt_as false
ceph config get client client_fscrypt_as
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_fscrypt_as
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_fscrypt_dummy_encryption

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [client.md#SP_client_fscrypt_dummy_encryption](../../../config/mds-client/client.md#SP_client_fscrypt_dummy_encryption) |

**What it does:** Enable fscrypt dummy encryption

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client client_fscrypt_dummy_encryption true
ceph config get client client_fscrypt_dummy_encryption
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### client_inject_fixed_oldest_tid

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [client.md#SP_client_inject_fixed_oldest_tid](../../../config/mds-client/client.md#SP_client_inject_fixed_oldest_tid) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client client_inject_fixed_oldest_tid true
ceph config get client client_inject_fixed_oldest_tid
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### client_inject_release_failure

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [client.md#SP_client_inject_release_failure](../../../config/mds-client/client.md#SP_client_inject_release_failure) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client client_inject_release_failure true
ceph config get client client_inject_release_failure
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### client_inject_write_delay_secs

| | |
|---|---|
| Type | Secs · default `0` · **Dev** |
| Table | [client.md#SP_client_inject_write_delay_secs](../../../config/mds-client/client.md#SP_client_inject_write_delay_secs) |

**What it does:** induce delay in write operation for testing

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client client_inject_write_delay_secs 0
ceph config get client client_inject_write_delay_secs
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### client_max_inline_size

| | |
|---|---|
| Type | Size · default `4_K` · **Dev** |
| Table | [client.md#SP_client_max_inline_size](../../../config/mds-client/client.md#SP_client_max_inline_size) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client client_max_inline_size 4_K
ceph config get client client_max_inline_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`4_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### client_max_retries_on_remount_failure

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [client.md#SP_client_max_retries_on_remount_failure](../../../config/mds-client/client.md#SP_client_max_retries_on_remount_failure) |

**What it does:** number of consecutive failed remount attempts for invalidating kernel dcache after which client would abort.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client client_max_retries_on_remount_failure 5
ceph config get client client_max_retries_on_remount_failure
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_max_retries_on_remount_failure
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_mds_namespace

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** · **STARTUP** (restart required) |
| Table | [client.md#SP_client_mds_namespace](../../../config/mds-client/client.md#SP_client_mds_namespace) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client client_mds_namespace "example"
ceph config get client client_mds_namespace
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`(empty)`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### client_metadata

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [client.md#SP_client_metadata](../../../config/mds-client/client.md#SP_client_metadata) |

**What it does:** metadata key=value comma-delimited pairs appended to session metadata

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client client_metadata "example"
ceph config get client client_metadata
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_metadata
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_mount_gid

| | |
|---|---|
| Type | Int · default `-1` · **Advanced** |
| Table | [client.md#SP_client_mount_gid](../../../config/mds-client/client.md#SP_client_mount_gid) |

**What it does:** gid to mount as

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client client_mount_gid 128
ceph config get client client_mount_gid
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `-1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_mount_gid
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_mount_timeout

| | |
|---|---|
| Type | Secs · default `5_min` · **Advanced** |
| Table | [client.md#SP_client_mount_timeout](../../../config/mds-client/client.md#SP_client_mount_timeout) |

**What it does:** timeout for mounting CephFS (seconds)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set client client_mount_timeout 5_min
ceph config get client client_mount_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_mount_timeout
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_mount_uid

| | |
|---|---|
| Type | Int · default `-1` · **Advanced** |
| Table | [client.md#SP_client_mount_uid](../../../config/mds-client/client.md#SP_client_mount_uid) |

**What it does:** uid to mount as

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client client_mount_uid 128
ceph config get client client_mount_uid
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `-1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_mount_uid
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_mountpoint

| | |
|---|---|
| Type | Str · default `/` · **Advanced** |
| Table | [client.md#SP_client_mountpoint](../../../config/mds-client/client.md#SP_client_mountpoint) |

**What it does:** default mount-point

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client client_mountpoint "/"
ceph config get client client_mountpoint
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `/`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_mountpoint
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_notify_timeout

| | |
|---|---|
| Type | Int · default `10` · **Dev** |
| Table | [client.md#SP_client_notify_timeout](../../../config/mds-client/client.md#SP_client_notify_timeout) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client client_notify_timeout 10
ceph config get client client_notify_timeout
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`10`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### client_oc

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [client.md#SP_client_oc](../../../config/mds-client/client.md#SP_client_oc) |

**What it does:** enable object caching

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client client_oc false
ceph config get client client_oc
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_oc
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_oc_max_dirty

| | |
|---|---|
| Type | Size · default `100_M` · **Advanced** |
| Table | [client.md#SP_client_oc_max_dirty](../../../config/mds-client/client.md#SP_client_oc_max_dirty) |

**What it does:** maximum size of dirty pages in object cache

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client client_oc_max_dirty 100_M
ceph config get client client_oc_max_dirty
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_oc_max_dirty
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_oc_max_dirty_age

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [client.md#SP_client_oc_max_dirty_age](../../../config/mds-client/client.md#SP_client_oc_max_dirty_age) |

**What it does:** maximum age of dirty pages in object cache (seconds)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client client_oc_max_dirty_age 5
ceph config get client client_oc_max_dirty_age
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_oc_max_dirty_age
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_oc_max_objects

| | |
|---|---|
| Type | Int · default `1000` · **Advanced** |
| Table | [client.md#SP_client_oc_max_objects](../../../config/mds-client/client.md#SP_client_oc_max_objects) |

**What it does:** maximum number of objects in cache

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client client_oc_max_objects 1000
ceph config get client client_oc_max_objects
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_oc_max_objects
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_oc_size

| | |
|---|---|
| Type | Size · default `200_M` · **Advanced** |
| Table | [client.md#SP_client_oc_size](../../../config/mds-client/client.md#SP_client_oc_size) |

**What it does:** maximum size of object cache

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client client_oc_size 200_M
ceph config get client client_oc_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `200_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_oc_size
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_oc_target_dirty

| | |
|---|---|
| Type | Size · default `8_M` · **Advanced** |
| Table | [client.md#SP_client_oc_target_dirty](../../../config/mds-client/client.md#SP_client_oc_target_dirty) |

**What it does:** target size of dirty pages object cache

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client client_oc_target_dirty 8_M
ceph config get client client_oc_target_dirty
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `8_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_oc_target_dirty
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_permissions

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [client.md#SP_client_permissions](../../../config/mds-client/client.md#SP_client_permissions) |

**What it does:** client-enforced permission checking

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client client_permissions false
ceph config get client client_permissions
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_permissions
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_quota

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [client.md#SP_client_quota](../../../config/mds-client/client.md#SP_client_quota) |

**What it does:** Enable quota enforcement

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client client_quota false
ceph config get client client_quota
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_quota
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_quota_df

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [client.md#SP_client_quota_df](../../../config/mds-client/client.md#SP_client_quota_df) |

**What it does:** show quota usage for statfs (df)

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client client_quota_df false
ceph config get client client_quota_df
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_quota_df
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_readahead_max_bytes

| | |
|---|---|
| Type | Size · default `0` · **Advanced** |
| Table | [client.md#SP_client_readahead_max_bytes](../../../config/mds-client/client.md#SP_client_readahead_max_bytes) |

**What it does:** maximum bytes to readahead in a file (zero is unlimited)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client client_readahead_max_bytes 64
ceph config get client client_readahead_max_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_readahead_max_bytes
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_readahead_max_periods

| | |
|---|---|
| Type | Int · default `4` · **Advanced** |
| Table | [client.md#SP_client_readahead_max_periods](../../../config/mds-client/client.md#SP_client_readahead_max_periods) |

**What it does:** maximum stripe periods to readahead in a file

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client client_readahead_max_periods 4
ceph config get client client_readahead_max_periods
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_readahead_max_periods
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_readahead_min

| | |
|---|---|
| Type | Size · default `128_K` · **Advanced** |
| Table | [client.md#SP_client_readahead_min](../../../config/mds-client/client.md#SP_client_readahead_min) |

**What it does:** minimum bytes to readahead in a file

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client client_readahead_min 128_K
ceph config get client client_readahead_min
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `128_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_readahead_min
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_reconnect_stale

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [client.md#SP_client_reconnect_stale](../../../config/mds-client/client.md#SP_client_reconnect_stale) |

**What it does:** reconnect when the session becomes stale

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client client_reconnect_stale true
ceph config get client client_reconnect_stale
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_reconnect_stale
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_respect_subvolume_snapshot_visibility

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [client.md#SP_client_respect_subvolume_snapshot_visibility](../../../config/mds-client/client.md#SP_client_respect_subvolume_snapshot_visibility) |

**What it does:** Respect subvolume snapshot visibility

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client client_respect_subvolume_snapshot_visibility true
ceph config get client client_respect_subvolume_snapshot_visibility
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_respect_subvolume_snapshot_visibility
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_shutdown_timeout

| | |
|---|---|
| Type | Secs · default `30` · **Advanced** |
| Table | [client.md#SP_client_shutdown_timeout](../../../config/mds-client/client.md#SP_client_shutdown_timeout) |

**What it does:** timeout for shutting down CephFS

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set client client_shutdown_timeout 30
ceph config get client client_shutdown_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_shutdown_timeout
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_snapdir

| | |
|---|---|
| Type | Str · default `.snap` · **Advanced** |
| Table | [client.md#SP_client_snapdir](../../../config/mds-client/client.md#SP_client_snapdir) |

**What it does:** pseudo directory for snapshot access to a directory

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client client_snapdir ".snap"
ceph config get client client_snapdir
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `.snap`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client client_snapdir
ceph -s
# client options: set on client section or ceph.conf
```

---

### client_tick_interval

| | |
|---|---|
| Type | Secs · default `1` · **Dev** |
| Table | [client.md#SP_client_tick_interval](../../../config/mds-client/client.md#SP_client_tick_interval) |

**What it does:** seconds between client upkeep ticks

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client client_tick_interval 1
ceph config get client client_tick_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### client_trace

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** |
| Table | [client.md#SP_client_trace](../../../config/mds-client/client.md#SP_client_trace) |

**What it does:** file containing trace of client operations

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client client_trace "example"
ceph config get client client_trace
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`(empty)`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### client_try_dentry_invalidate

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [client.md#SP_client_try_dentry_invalidate](../../../config/mds-client/client.md#SP_client_try_dentry_invalidate) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client client_try_dentry_invalidate true
ceph config get client client_try_dentry_invalidate
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### client_use_faked_inos

| | |
|---|---|
| Type | Bool · default `False` · **Dev** · **STARTUP** (restart required) |
| Table | [client.md#SP_client_use_faked_inos](../../../config/mds-client/client.md#SP_client_use_faked_inos) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client client_use_faked_inos true
ceph config get client client_use_faked_inos
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### client_use_random_mds

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [client.md#SP_client_use_random_mds](../../../config/mds-client/client.md#SP_client_use_random_mds) |

**What it does:** issue new requests to a random active MDS

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client client_use_random_mds true
ceph config get client client_use_random_mds
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_client_watch_timeout

| | |
|---|---|
| Type | Int · default `30` · **Dev** |
| Table | [osd.md#SP_osd_client_watch_timeout](../../../config/mds-client/osd.md#SP_osd_client_watch_timeout) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_client_watch_timeout 30
ceph config get osd osd_client_watch_timeout
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`30`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
