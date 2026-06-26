# CephFS mirror

CephFS mirror 配置深度指南 — 15 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/cephfs-mirror/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [cephfs_mirror_action_update_interval](#cephfs_mirror_action_update_interval) | `2` | Advanced | 性能 |
| [cephfs_mirror_blockdiff_min_file_size](#cephfs_mirror_blockdiff_min_file_size) | `16_M` | Advanced | 性能 |
| [cephfs_mirror_datasync_files_per_batch](#cephfs_mirror_datasync_files_per_batch) | `64` | Advanced | 性能 |
| [cephfs_mirror_directory_scan_interval](#cephfs_mirror_directory_scan_interval) | `10` | Advanced | 性能 |
| [cephfs_mirror_distribute_datasync_threads](#cephfs_mirror_distribute_datasync_threads) | `True` | Advanced | 性能 |
| [cephfs_mirror_max_concurrent_directory_syncs](#cephfs_mirror_max_concurrent_directory_syncs) | `3` | Advanced | 性能 |
| [cephfs_mirror_max_consecutive_failures_per_directory](#cephfs_mirror_max_consecutive_failures_per_directory) | `10` | Advanced | 性能 |
| [cephfs_mirror_max_datasync_threads](#cephfs_mirror_max_datasync_threads) | `6` | Advanced | 性能 |
| [cephfs_mirror_max_snapshot_sync_per_cycle](#cephfs_mirror_max_snapshot_sync_per_cycle) | `3` | Advanced | 性能 |
| [cephfs_mirror_mount_timeout](#cephfs_mirror_mount_timeout) | `10` | Advanced | 性能 |
| [cephfs_mirror_perf_stats_prio](#cephfs_mirror_perf_stats_prio) | `5` | Advanced | 性能 |
| [cephfs_mirror_restart_mirror_on_blocklist_interval](#cephfs_mirror_restart_mirror_on_blocklist_interval) | `30` | Advanced | 性能 |
| [cephfs_mirror_restart_mirror_on_failure_interval](#cephfs_mirror_restart_mirror_on_failure_interval) | `20` | Advanced | 性能 |
| [cephfs_mirror_retry_failed_directories_interval](#cephfs_mirror_retry_failed_directories_interval) | `60` | Advanced | 性能 |
| [cephfs_mirror_tick_interval](#cephfs_mirror_tick_interval) | `5` | Advanced | 性能 |

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
ceph config get <daemon> <option>  # e.g. cephfs-mirror
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### cephfs_mirror_action_update_interval

| | |
|---|---|
| 类型 | Secs · default `2` · **Advanced** |
| 表格 | [cephfs.md#SP_cephfs_mirror_action_update_interval](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_action_update_interval) |

**作用：** interval for driving asynchronous mirror actions Interval in seconds to process pending mirror update actions.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set cephfs_mirror cephfs_mirror_action_update_interval 2
ceph config get cephfs_mirror cephfs_mirror_action_update_interval
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
ceph config get cephfs_mirror cephfs_mirror_action_update_interval
ceph -s
```

---

### cephfs_mirror_blockdiff_min_file_size

| | |
|---|---|
| 类型 | Size · default `16_M` · **Advanced** |
| 表格 | [cephfs.md#SP_cephfs_mirror_blockdiff_min_file_size](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_blockdiff_min_file_size) |

**作用：** minimum file size threshold in bytes above which block-level diff is used during CephFS mirroring. defines the minimum file size, in bytes, required for CephFS mirroring to use block-level delta synchronization instead of performing a full file copy. When a file’s size is greater than to this threshold, the mirroring engine attempts to synchronize only the modified block extents between snapshots. For files smaller than or equal to this value, a full file copy is performed instead, as block-level diff may not provide meaningful performance benefits for small files.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set cephfs_mirror cephfs_mirror_blockdiff_min_file_size 16_M
ceph config get cephfs_mirror cephfs_mirror_blockdiff_min_file_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `16_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get cephfs_mirror cephfs_mirror_blockdiff_min_file_size
ceph -s
```

---

### cephfs_mirror_datasync_files_per_batch

| | |
|---|---|
| 类型 | Uint · default `64` · **Advanced** |
| 表格 | [cephfs.md#SP_cephfs_mirror_datasync_files_per_batch](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_datasync_files_per_batch) |

**作用：** maximum number of files processed by datasync threads per scheduling cycle before yielding. defines the maximum number of files a data synchronization thread will process for a specific snapshot before yielding the thread to re-check scheduling logic. This is applicable only when cephfs_mirror_distribute_datasync_threads is enabled. This batch size determines the granularity of thread distribution; smaller batches allow threads to rotate between snapshots more frequently, while larger batches improve throughput by minimizing the overhead of thread re-assignment.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set cephfs_mirror cephfs_mirror_datasync_files_per_batch 64
ceph config get cephfs_mirror cephfs_mirror_datasync_files_per_batch
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get cephfs_mirror cephfs_mirror_datasync_files_per_batch
ceph -s
```

---

### cephfs_mirror_directory_scan_interval

| | |
|---|---|
| 类型 | Uint · default `10` · **Advanced** |
| 表格 | [cephfs.md#SP_cephfs_mirror_directory_scan_interval](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_directory_scan_interval) |

**作用：** interval to scan directories to mirror snapshots interval in seconds to scan configured directories for snapshot mirroring.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set cephfs_mirror cephfs_mirror_directory_scan_interval 10
ceph config get cephfs_mirror cephfs_mirror_directory_scan_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get cephfs_mirror cephfs_mirror_directory_scan_interval
ceph -s
```

---

### cephfs_mirror_distribute_datasync_threads

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [cephfs.md#SP_cephfs_mirror_distribute_datasync_threads](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_distribute_datasync_threads) |

**作用：** distribute data synchronization threads evenly across multiple snapshots. controls how datasync worker threads are scheduled when multiple snapshots are queued for synchronization. When enabled, worker threads are distributed fairly across active snapshots, preventing a single large snapshot from monopolizing all available threads and causing other snapshots to starve. When disabled, datasync threads process one snapshot until completion before switching to another, which can improve throughput for individual large snapshots but may increase latency for other queued snapshots. Enabling this option improves responsiveness and reduces starvation in environments where multiple directories are configured to be mirrored.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set cephfs_mirror cephfs_mirror_distribute_datasync_threads false
ceph config get cephfs_mirror cephfs_mirror_distribute_datasync_threads
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get cephfs_mirror cephfs_mirror_distribute_datasync_threads
ceph -s
```

---

### cephfs_mirror_max_concurrent_directory_syncs

| | |
|---|---|
| 类型 | Uint · default `3` · **Advanced** |
| 表格 | [cephfs.md#SP_cephfs_mirror_max_concurrent_directory_syncs](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_max_concurrent_directory_syncs) |

**作用：** maximum number of concurrent snapshot synchronization crawler threads maximum number of directory snapshots that can be crawled concurrently by cephfs-mirror daemon. Controls the number of synchronization crawler threads. Note that the crawler threads also does entry operations like directory creations, file deletes and snapshot deletes/renames.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set cephfs_mirror cephfs_mirror_max_concurrent_directory_syncs 3
ceph config get cephfs_mirror cephfs_mirror_max_concurrent_directory_syncs
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get cephfs_mirror cephfs_mirror_max_concurrent_directory_syncs
ceph -s
```

---

### cephfs_mirror_max_consecutive_failures_per_directory

| | |
|---|---|
| 类型 | Uint · default `10` · **Advanced** |
| 表格 | [cephfs.md#SP_cephfs_mirror_max_consecutive_failures_per_directory](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_max_consecutive_failures_per_directory) |

**作用：** consecutive failed directory synchronization attempts before marking a directory as "failed" number of consecutive snapshot synchronization failures to mark a directory as "failed". failed directories are retried for synchronization less frequently.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set cephfs_mirror cephfs_mirror_max_consecutive_failures_per_directory 10
ceph config get cephfs_mirror cephfs_mirror_max_consecutive_failures_per_directory
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get cephfs_mirror cephfs_mirror_max_consecutive_failures_per_directory
ceph -s
```

---

### cephfs_mirror_max_datasync_threads

| | |
|---|---|
| 类型 | Uint · default `6` · **Advanced** |
| 表格 | [cephfs.md#SP_cephfs_mirror_max_datasync_threads](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_max_datasync_threads) |

**作用：** maximum number of concurrent snapshot data synchronization threads specifies the maximum number of worker threads in the CephFS mirror data synchronization thread pool. These threads process file synchronization tasks produced by crawler threads for mirrored directory snapshots.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set cephfs_mirror cephfs_mirror_max_datasync_threads 6
ceph config get cephfs_mirror cephfs_mirror_max_datasync_threads
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `6` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get cephfs_mirror cephfs_mirror_max_datasync_threads
ceph -s
```

---

### cephfs_mirror_max_snapshot_sync_per_cycle

| | |
|---|---|
| 类型 | Uint · default `3` · **Advanced** |
| 表格 | [cephfs.md#SP_cephfs_mirror_max_snapshot_sync_per_cycle](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_max_snapshot_sync_per_cycle) |

**作用：** number of snapshots to mirror in one cycle maximum number of snapshots to mirror when a directory is picked up for mirroring by worker threads.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set cephfs_mirror cephfs_mirror_max_snapshot_sync_per_cycle 3
ceph config get cephfs_mirror cephfs_mirror_max_snapshot_sync_per_cycle
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get cephfs_mirror cephfs_mirror_max_snapshot_sync_per_cycle
ceph -s
```

---

### cephfs_mirror_mount_timeout

| | |
|---|---|
| 类型 | Secs · default `10` · **Advanced** |
| 表格 | [cephfs.md#SP_cephfs_mirror_mount_timeout](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_mount_timeout) |

**作用：** timeout for mounting primary/secondary ceph file system Timeout in seconds for mounting primary or secondary (remote) ceph file system by the cephfs-mirror daemon. Setting this to a higher value could result in the mirror daemon getting stalled when mounting a file system if the cluster is not reachable. This option is used to override the usual client_mount_timeout.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set cephfs_mirror cephfs_mirror_mount_timeout 10
ceph config get cephfs_mirror cephfs_mirror_mount_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get cephfs_mirror cephfs_mirror_mount_timeout
ceph -s
```

---

### cephfs_mirror_perf_stats_prio

| | |
|---|---|
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [cephfs.md#SP_cephfs_mirror_perf_stats_prio](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_perf_stats_prio) |

**作用：** Priority level for mirror daemon replication perf counters The daemon will send perf counter data to the manager daemon if the priority is not lower than mgr_stats_threshold.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set cephfs_mirror cephfs_mirror_perf_stats_prio 5
ceph config get cephfs_mirror cephfs_mirror_perf_stats_prio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `11`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get cephfs_mirror cephfs_mirror_perf_stats_prio
ceph -s
```

---

### cephfs_mirror_restart_mirror_on_blocklist_interval

| | |
|---|---|
| 类型 | Secs · default `30` · **Advanced** |
| 表格 | [cephfs.md#SP_cephfs_mirror_restart_mirror_on_blocklist_interval](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_restart_mirror_on_blocklist_interval) |

**作用：** interval to restart blocklisted instances Interval in seconds to restart blocklisted mirror instances. Setting to zero (0) disables restarting blocklisted instances.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set cephfs_mirror cephfs_mirror_restart_mirror_on_blocklist_interval 30
ceph config get cephfs_mirror cephfs_mirror_restart_mirror_on_blocklist_interval
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
ceph config get cephfs_mirror cephfs_mirror_restart_mirror_on_blocklist_interval
ceph -s
```

---

### cephfs_mirror_restart_mirror_on_failure_interval

| | |
|---|---|
| 类型 | Secs · default `20` · **Advanced** |
| 表格 | [cephfs.md#SP_cephfs_mirror_restart_mirror_on_failure_interval](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_restart_mirror_on_failure_interval) |

**作用：** interval to restart failed mirror instances Interval in seconds to restart failed mirror instances. Setting to zero (0) disables restarting failed mirror instances.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set cephfs_mirror cephfs_mirror_restart_mirror_on_failure_interval 20
ceph config get cephfs_mirror cephfs_mirror_restart_mirror_on_failure_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `20` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get cephfs_mirror cephfs_mirror_restart_mirror_on_failure_interval
ceph -s
```

---

### cephfs_mirror_retry_failed_directories_interval

| | |
|---|---|
| 类型 | Uint · default `60` · **Advanced** |
| 表格 | [cephfs.md#SP_cephfs_mirror_retry_failed_directories_interval](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_retry_failed_directories_interval) |

**作用：** failed directory retry interval for synchronization interval in seconds to retry synchronization for failed directories.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set cephfs_mirror cephfs_mirror_retry_failed_directories_interval 60
ceph config get cephfs_mirror cephfs_mirror_retry_failed_directories_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `60` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get cephfs_mirror cephfs_mirror_retry_failed_directories_interval
ceph -s
```

---

### cephfs_mirror_tick_interval

| | |
|---|---|
| 类型 | Secs · default `5` · **Advanced** |
| 表格 | [cephfs.md#SP_cephfs_mirror_tick_interval](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_tick_interval) |

**作用：** interval for the per-peer mirroring tick thread interval in seconds for the per-peer tick thread that runs periodic mirroring work. The value is re-read each iteration so configuration changes take effect without restarting the daemon.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set cephfs_mirror cephfs_mirror_tick_interval 5
ceph config get cephfs_mirror cephfs_mirror_tick_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get cephfs_mirror cephfs_mirror_tick_interval
ceph -s
```

---


[← 概览](../OVERVIEW.md)
