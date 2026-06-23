# CephFS mirror

CephFS mirror config deep dive — 15 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/cephfs-mirror/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [cephfs_mirror_action_update_interval](#cephfs_mirror_action_update_interval) | `2` | Advanced | Performance |
| [cephfs_mirror_blockdiff_min_file_size](#cephfs_mirror_blockdiff_min_file_size) | `16_M` | Advanced | Performance |
| [cephfs_mirror_datasync_files_per_batch](#cephfs_mirror_datasync_files_per_batch) | `64` | Advanced | Performance |
| [cephfs_mirror_directory_scan_interval](#cephfs_mirror_directory_scan_interval) | `10` | Advanced | Performance |
| [cephfs_mirror_distribute_datasync_threads](#cephfs_mirror_distribute_datasync_threads) | `True` | Advanced | Performance |
| [cephfs_mirror_max_concurrent_directory_syncs](#cephfs_mirror_max_concurrent_directory_syncs) | `3` | Advanced | Performance |
| [cephfs_mirror_max_consecutive_failures_per_directory](#cephfs_mirror_max_consecutive_failures_per_directory) | `10` | Advanced | Performance |
| [cephfs_mirror_max_datasync_threads](#cephfs_mirror_max_datasync_threads) | `6` | Advanced | Performance |
| [cephfs_mirror_max_snapshot_sync_per_cycle](#cephfs_mirror_max_snapshot_sync_per_cycle) | `3` | Advanced | Performance |
| [cephfs_mirror_mount_timeout](#cephfs_mirror_mount_timeout) | `10` | Advanced | Performance |
| [cephfs_mirror_perf_stats_prio](#cephfs_mirror_perf_stats_prio) | `5` | Advanced | Performance |
| [cephfs_mirror_restart_mirror_on_blocklist_interval](#cephfs_mirror_restart_mirror_on_blocklist_interval) | `30` | Advanced | Performance |
| [cephfs_mirror_restart_mirror_on_failure_interval](#cephfs_mirror_restart_mirror_on_failure_interval) | `20` | Advanced | Performance |
| [cephfs_mirror_retry_failed_directories_interval](#cephfs_mirror_retry_failed_directories_interval) | `60` | Advanced | Performance |
| [cephfs_mirror_tick_interval](#cephfs_mirror_tick_interval) | `5` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. cephfs-mirror
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### cephfs_mirror_action_update_interval

| | |
|---|---|
| Type | Secs · default `2` · **Advanced** |
| Table | [cephfs.md#SP_cephfs_mirror_action_update_interval](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_action_update_interval) |

**What it does:** interval for driving asynchronous mirror actions

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set cephfs_mirror cephfs_mirror_action_update_interval 2
ceph config get cephfs_mirror cephfs_mirror_action_update_interval
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
ceph config get cephfs_mirror cephfs_mirror_action_update_interval
ceph -s
```

---

### cephfs_mirror_blockdiff_min_file_size

| | |
|---|---|
| Type | Size · default `16_M` · **Advanced** |
| Table | [cephfs.md#SP_cephfs_mirror_blockdiff_min_file_size](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_blockdiff_min_file_size) |

**What it does:** minimum file size threshold in bytes above which block-level diff is used during CephFS mirroring.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set cephfs_mirror cephfs_mirror_blockdiff_min_file_size 16_M
ceph config get cephfs_mirror cephfs_mirror_blockdiff_min_file_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `16_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get cephfs_mirror cephfs_mirror_blockdiff_min_file_size
ceph -s
```

---

### cephfs_mirror_datasync_files_per_batch

| | |
|---|---|
| Type | Uint · default `64` · **Advanced** |
| Table | [cephfs.md#SP_cephfs_mirror_datasync_files_per_batch](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_datasync_files_per_batch) |

**What it does:** maximum number of files processed by datasync threads per scheduling cycle before yielding.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set cephfs_mirror cephfs_mirror_datasync_files_per_batch 64
ceph config get cephfs_mirror cephfs_mirror_datasync_files_per_batch
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get cephfs_mirror cephfs_mirror_datasync_files_per_batch
ceph -s
```

---

### cephfs_mirror_directory_scan_interval

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [cephfs.md#SP_cephfs_mirror_directory_scan_interval](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_directory_scan_interval) |

**What it does:** interval to scan directories to mirror snapshots

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set cephfs_mirror cephfs_mirror_directory_scan_interval 10
ceph config get cephfs_mirror cephfs_mirror_directory_scan_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get cephfs_mirror cephfs_mirror_directory_scan_interval
ceph -s
```

---

### cephfs_mirror_distribute_datasync_threads

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [cephfs.md#SP_cephfs_mirror_distribute_datasync_threads](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_distribute_datasync_threads) |

**What it does:** distribute data synchronization threads evenly across multiple snapshots.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set cephfs_mirror cephfs_mirror_distribute_datasync_threads false
ceph config get cephfs_mirror cephfs_mirror_distribute_datasync_threads
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get cephfs_mirror cephfs_mirror_distribute_datasync_threads
ceph -s
```

---

### cephfs_mirror_max_concurrent_directory_syncs

| | |
|---|---|
| Type | Uint · default `3` · **Advanced** |
| Table | [cephfs.md#SP_cephfs_mirror_max_concurrent_directory_syncs](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_max_concurrent_directory_syncs) |

**What it does:** maximum number of concurrent snapshot synchronization crawler threads

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set cephfs_mirror cephfs_mirror_max_concurrent_directory_syncs 3
ceph config get cephfs_mirror cephfs_mirror_max_concurrent_directory_syncs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get cephfs_mirror cephfs_mirror_max_concurrent_directory_syncs
ceph -s
```

---

### cephfs_mirror_max_consecutive_failures_per_directory

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [cephfs.md#SP_cephfs_mirror_max_consecutive_failures_per_directory](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_max_consecutive_failures_per_directory) |

**What it does:** consecutive failed directory synchronization attempts before marking a directory as "failed"

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set cephfs_mirror cephfs_mirror_max_consecutive_failures_per_directory 10
ceph config get cephfs_mirror cephfs_mirror_max_consecutive_failures_per_directory
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get cephfs_mirror cephfs_mirror_max_consecutive_failures_per_directory
ceph -s
```

---

### cephfs_mirror_max_datasync_threads

| | |
|---|---|
| Type | Uint · default `6` · **Advanced** |
| Table | [cephfs.md#SP_cephfs_mirror_max_datasync_threads](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_max_datasync_threads) |

**What it does:** maximum number of concurrent snapshot data synchronization threads

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set cephfs_mirror cephfs_mirror_max_datasync_threads 6
ceph config get cephfs_mirror cephfs_mirror_max_datasync_threads
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `6`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get cephfs_mirror cephfs_mirror_max_datasync_threads
ceph -s
```

---

### cephfs_mirror_max_snapshot_sync_per_cycle

| | |
|---|---|
| Type | Uint · default `3` · **Advanced** |
| Table | [cephfs.md#SP_cephfs_mirror_max_snapshot_sync_per_cycle](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_max_snapshot_sync_per_cycle) |

**What it does:** number of snapshots to mirror in one cycle

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set cephfs_mirror cephfs_mirror_max_snapshot_sync_per_cycle 3
ceph config get cephfs_mirror cephfs_mirror_max_snapshot_sync_per_cycle
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get cephfs_mirror cephfs_mirror_max_snapshot_sync_per_cycle
ceph -s
```

---

### cephfs_mirror_mount_timeout

| | |
|---|---|
| Type | Secs · default `10` · **Advanced** |
| Table | [cephfs.md#SP_cephfs_mirror_mount_timeout](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_mount_timeout) |

**What it does:** timeout for mounting primary/secondary ceph file system

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set cephfs_mirror cephfs_mirror_mount_timeout 10
ceph config get cephfs_mirror cephfs_mirror_mount_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get cephfs_mirror cephfs_mirror_mount_timeout
ceph -s
```

---

### cephfs_mirror_perf_stats_prio

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [cephfs.md#SP_cephfs_mirror_perf_stats_prio](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_perf_stats_prio) |

**What it does:** Priority level for mirror daemon replication perf counters

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set cephfs_mirror cephfs_mirror_perf_stats_prio 5
ceph config get cephfs_mirror cephfs_mirror_perf_stats_prio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `11`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get cephfs_mirror cephfs_mirror_perf_stats_prio
ceph -s
```

---

### cephfs_mirror_restart_mirror_on_blocklist_interval

| | |
|---|---|
| Type | Secs · default `30` · **Advanced** |
| Table | [cephfs.md#SP_cephfs_mirror_restart_mirror_on_blocklist_interval](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_restart_mirror_on_blocklist_interval) |

**What it does:** interval to restart blocklisted instances

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set cephfs_mirror cephfs_mirror_restart_mirror_on_blocklist_interval 30
ceph config get cephfs_mirror cephfs_mirror_restart_mirror_on_blocklist_interval
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
ceph config get cephfs_mirror cephfs_mirror_restart_mirror_on_blocklist_interval
ceph -s
```

---

### cephfs_mirror_restart_mirror_on_failure_interval

| | |
|---|---|
| Type | Secs · default `20` · **Advanced** |
| Table | [cephfs.md#SP_cephfs_mirror_restart_mirror_on_failure_interval](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_restart_mirror_on_failure_interval) |

**What it does:** interval to restart failed mirror instances

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set cephfs_mirror cephfs_mirror_restart_mirror_on_failure_interval 20
ceph config get cephfs_mirror cephfs_mirror_restart_mirror_on_failure_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get cephfs_mirror cephfs_mirror_restart_mirror_on_failure_interval
ceph -s
```

---

### cephfs_mirror_retry_failed_directories_interval

| | |
|---|---|
| Type | Uint · default `60` · **Advanced** |
| Table | [cephfs.md#SP_cephfs_mirror_retry_failed_directories_interval](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_retry_failed_directories_interval) |

**What it does:** failed directory retry interval for synchronization

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set cephfs_mirror cephfs_mirror_retry_failed_directories_interval 60
ceph config get cephfs_mirror cephfs_mirror_retry_failed_directories_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `60`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get cephfs_mirror cephfs_mirror_retry_failed_directories_interval
ceph -s
```

---

### cephfs_mirror_tick_interval

| | |
|---|---|
| Type | Secs · default `5` · **Advanced** |
| Table | [cephfs.md#SP_cephfs_mirror_tick_interval](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_tick_interval) |

**What it does:** interval for the per-peer mirroring tick thread

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set cephfs_mirror cephfs_mirror_tick_interval 5
ceph config get cephfs_mirror cephfs_mirror_tick_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get cephfs_mirror cephfs_mirror_tick_interval
ceph -s
```

---


[← Overview](../OVERVIEW.md)
