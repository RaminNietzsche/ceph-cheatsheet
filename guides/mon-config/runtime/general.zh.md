# General monitor

MON 配置深度指南 — 44 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [enable_availability_tracking](#enable_availability_tracking) | `False` | Advanced | Policy |
| [mon_clock_drift_allowed](#mon_clock_drift_allowed) | `0.05` | Advanced | Performance |
| [mon_clock_drift_warn_backoff](#mon_clock_drift_warn_backoff) | `5` | Advanced | Performance |
| [mon_compact_on_bootstrap](#mon_compact_on_bootstrap) | `False` | Advanced | Performance |
| [mon_compact_on_start](#mon_compact_on_start) | `False` | Advanced | Performance |
| [mon_compact_on_trim](#mon_compact_on_trim) | `True` | Advanced | Performance |
| [mon_con_tracker_score_halflife](#mon_con_tracker_score_halflife) | `43200` | Advanced | Performance |
| [mon_cpu_threads](#mon_cpu_threads) | `4` | Advanced | Performance |
| [mon_crush_min_required_version](#mon_crush_min_required_version) | `hammer` | Advanced | Performance |
| [mon_daemon_bytes](#mon_daemon_bytes) | `400_M` | Advanced | Performance |
| [mon_down_added_grace](#mon_down_added_grace) | `3_min` | Advanced | Performance |
| [mon_down_mkfs_grace](#mon_down_mkfs_grace) | `1_min` | Advanced | Performance |
| [mon_down_uptime_grace](#mon_down_uptime_grace) | `1_min` | Advanced | Performance |
| [mon_elector_ignore_propose_margin](#mon_elector_ignore_propose_margin) | `0.0005` | Advanced | Performance |
| [mon_elector_ping_divisor](#mon_elector_ping_divisor) | `2` | Advanced | Performance |
| [mon_enable_op_tracker](#mon_enable_op_tracker) | `True` | Advanced | Policy |
| [mon_fsmap_prune_threshold](#mon_fsmap_prune_threshold) | `300` | Advanced | Performance |
| [mon_health_max_detail](#mon_health_max_detail) | `50` | Advanced | Performance |
| [mon_lease](#mon_lease) | `5` | Advanced | Performance |
| [mon_mds_force_trim_to](#mon_mds_force_trim_to) | `0` | Dev | Dev |
| [mon_mds_skip_sanity](#mon_mds_skip_sanity) | `False` | Advanced | Performance |
| [mon_memory_autotune](#mon_memory_autotune) | `True` | Basic | Policy |
| [mon_memory_target](#mon_memory_target) | `2_G` | Basic | Policy |
| [mon_nvmeofgw_beacon_grace](#mon_nvmeofgw_beacon_grace) | `7` | Advanced | Performance |
| [mon_nvmeofgw_beacons_till_ack](#mon_nvmeofgw_beacons_till_ack) | `15` | Advanced | Performance |
| [mon_nvmeofgw_delete_grace](#mon_nvmeofgw_delete_grace) | `15_min` | Advanced | Performance |
| [mon_nvmeofgw_set_group_id_retry](#mon_nvmeofgw_set_group_id_retry) | `1000` | Advanced | Performance |
| [mon_nvmeofgw_wrong_map_ignore_sec](#mon_nvmeofgw_wrong_map_ignore_sec) | `15` | Advanced | Performance |
| [mon_op_complaint_time](#mon_op_complaint_time) | `30` | Advanced | Performance |
| [mon_op_history_duration](#mon_op_history_duration) | `10_min` | Advanced | Performance |
| [mon_op_history_size](#mon_op_history_size) | `20` | Advanced | Performance |
| [mon_op_history_slow_op_size](#mon_op_history_slow_op_size) | `20` | Advanced | Performance |
| [mon_op_history_slow_op_threshold](#mon_op_history_slow_op_threshold) | `10` | Advanced | Performance |
| [mon_rocksdb_options](#mon_rocksdb_options) | `write_buffer_size=33554432,compression=kNoCompression,level_compaction_dynamic_level_bytes=true` | Advanced | Performance |
| [mon_stretch_cluster_recovery_ratio](#mon_stretch_cluster_recovery_ratio) | `0.6` | Advanced | Performance |
| [mon_stretch_max_bucket_weight_delta](#mon_stretch_max_bucket_weight_delta) | `0.1` | Dev | Dev |
| [mon_stretch_recovery_min_wait](#mon_stretch_recovery_min_wait) | `15` | Advanced | Performance |
| [mon_warn_on_colocated_monitors](#mon_warn_on_colocated_monitors) | `False` | Advanced | Performance |
| [mon_warn_on_crush_straw_calc_version_zero](#mon_warn_on_crush_straw_calc_version_zero) | `True` | Advanced | Performance |
| [mon_warn_on_degraded_stretch_mode](#mon_warn_on_degraded_stretch_mode) | `True` | Advanced | Performance |
| [mon_warn_on_legacy_crush_tunables](#mon_warn_on_legacy_crush_tunables) | `True` | Advanced | Performance |
| [mon_warn_on_older_version](#mon_warn_on_older_version) | `True` | Advanced | Performance |
| [nvmeof_mon_client_connect_panic](#nvmeof_mon_client_connect_panic) | `30` | Advanced | Performance |
| [nvmeof_mon_client_disconnect_panic](#nvmeof_mon_client_disconnect_panic) | `100` | Advanced | Performance |

## 寻找最优值

| 模型 | 如何选择 |
|-------|---------------|
| **Policy** | 安全、兼容性、运维默认值 |
| **Capacity** | 磁盘布局、路径、容量规划 |
| **Performance** | 基线 → 逐步调整 → 监控集群 |
| **Connectivity** | 最近且稳定的外部端点 |
| **Dev** | 生产环境保持 upstream 默认值 |

**常用工具：**

```bash
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### enable_availability_tracking

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [mon.md#SP_enable_availability_tracking](../../../config/mon/mon.md#SP_enable_availability_tracking) |

**作用：** Calculate and store availablity score for each pool in the cluster at regular intervals

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mon enable_availability_tracking true
ceph config get mon enable_availability_tracking
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon enable_availability_tracking
ceph -s
ceph mon stat
```

---

### mon_clock_drift_allowed

| | |
|---|---|
| 类型 | Float · default `0.05` · **Advanced** |
| 表格 | [mon.md#SP_mon_clock_drift_allowed](../../../config/mon/mon.md#SP_mon_clock_drift_allowed) |

**作用：** Maximum clock drift (seconds) between monitors before health warnings.

**何时使用：** Ensure NTP/chrony is stable first. Increase only as a temporary mitigation while fixing time sync.

**示例：**

```bash
ceph config set mon mon_clock_drift_allowed 0.05
ceph config get mon mon_clock_drift_allowed
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.05` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_clock_drift_allowed
ceph -s
ceph mon stat
```

---

### mon_clock_drift_warn_backoff

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [mon.md#SP_mon_clock_drift_warn_backoff](../../../config/mon/mon.md#SP_mon_clock_drift_warn_backoff) |

**作用：** exponential backoff factor for logging clock drift warnings in the cluster log

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_clock_drift_warn_backoff 5
ceph config get mon mon_clock_drift_warn_backoff
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_clock_drift_warn_backoff
ceph -s
ceph mon stat
```

---

### mon_compact_on_bootstrap

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [mon.md#SP_mon_compact_on_bootstrap](../../../config/mon/mon.md#SP_mon_compact_on_bootstrap) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mon mon_compact_on_bootstrap true
ceph config get mon mon_compact_on_bootstrap
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_compact_on_bootstrap
ceph -s
ceph mon stat
```

---

### mon_compact_on_start

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [mon.md#SP_mon_compact_on_start](../../../config/mon/mon.md#SP_mon_compact_on_start) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mon mon_compact_on_start true
ceph config get mon mon_compact_on_start
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_compact_on_start
ceph -s
ceph mon stat
```

---

### mon_compact_on_trim

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_compact_on_trim](../../../config/mon/mon.md#SP_mon_compact_on_trim) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_compact_on_trim false
ceph config get mon mon_compact_on_trim
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_compact_on_trim
ceph -s
ceph mon stat
```

---

### mon_con_tracker_score_halflife

| | |
|---|---|
| 类型 | Uint · default `43200` · **Advanced** |
| 表格 | [mon.md#SP_mon_con_tracker_score_halflife](../../../config/mon/mon.md#SP_mon_con_tracker_score_halflife) |

**作用：** The 'halflife' used when updating/calculating peer connection scores

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_con_tracker_score_halflife 43200
ceph config get mon mon_con_tracker_score_halflife
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `43200` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `60`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_con_tracker_score_halflife
ceph -s
ceph mon stat
```

---

### mon_cpu_threads

| | |
|---|---|
| 类型 | Int · default `4` · **Advanced** |
| 表格 | [mon.md#SP_mon_cpu_threads](../../../config/mon/mon.md#SP_mon_cpu_threads) |

**作用：** worker threads for CPU intensive background work

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_cpu_threads 4
ceph config get mon mon_cpu_threads
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `4` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_cpu_threads
ceph -s
ceph mon stat
```

---

### mon_crush_min_required_version

| | |
|---|---|
| 类型 | Str · default `hammer` · **Advanced** |
| 表格 | [mon.md#SP_mon_crush_min_required_version](../../../config/mon/mon.md#SP_mon_crush_min_required_version) |

**作用：** minimum ceph release to use for mon_warn_on_legacy_crush_tunables

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_crush_min_required_version hammer
ceph config get mon mon_crush_min_required_version
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `hammer` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_crush_min_required_version
ceph -s
ceph mon stat
```

---

### mon_daemon_bytes

| | |
|---|---|
| 类型 | Size · default `400_M` · **Advanced** |
| 表格 | [mon.md#SP_mon_daemon_bytes](../../../config/mon/mon.md#SP_mon_daemon_bytes) |

**作用：** max bytes of outstanding mon messages mon will read off the network

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_daemon_bytes 400_M
ceph config get mon mon_daemon_bytes
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `400_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_daemon_bytes
ceph -s
ceph mon stat
```

---

### mon_down_added_grace

| | |
|---|---|
| 类型 | Secs · default `3_min` · **Advanced** |
| 表格 | [mon.md#SP_mon_down_added_grace](../../../config/mon/mon.md#SP_mon_down_added_grace) |

**作用：** Period in seconds that the cluster may have a newly added mon down

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_down_added_grace 3_min
ceph config get mon mon_down_added_grace
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `3_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_down_added_grace
ceph -s
ceph mon stat
```

---

### mon_down_mkfs_grace

| | |
|---|---|
| 类型 | Secs · default `1_min` · **Advanced** |
| 表格 | [mon.md#SP_mon_down_mkfs_grace](../../../config/mon/mon.md#SP_mon_down_mkfs_grace) |

**作用：** Period in seconds that the cluster may have a mon down after cluster creation

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_down_mkfs_grace 1_min
ceph config get mon mon_down_mkfs_grace
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_down_mkfs_grace
ceph -s
ceph mon stat
```

---

### mon_down_uptime_grace

| | |
|---|---|
| 类型 | Secs · default `1_min` · **Advanced** |
| 表格 | [mon.md#SP_mon_down_uptime_grace](../../../config/mon/mon.md#SP_mon_down_uptime_grace) |

**作用：** Period in seconds that the cluster may have a mon down after this (leader) monitor comes up.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_down_uptime_grace 1_min
ceph config get mon mon_down_uptime_grace
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_down_uptime_grace
ceph -s
ceph mon stat
```

---

### mon_elector_ignore_propose_margin

| | |
|---|---|
| 类型 | Float · default `0.0005` · **Advanced** |
| 表格 | [mon.md#SP_mon_elector_ignore_propose_margin](../../../config/mon/mon.md#SP_mon_elector_ignore_propose_margin) |

**作用：** The difference in connection score allowed before a peon stops ignoring out-of-quorum PROPOSEs

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_elector_ignore_propose_margin 0.0005
ceph config get mon mon_elector_ignore_propose_margin
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.0005` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_elector_ignore_propose_margin
ceph -s
ceph mon stat
```

---

### mon_elector_ping_divisor

| | |
|---|---|
| 类型 | Uint · default `2` · **Advanced** |
| 表格 | [mon.md#SP_mon_elector_ping_divisor](../../../config/mon/mon.md#SP_mon_elector_ping_divisor) |

**作用：** We will send a ping up to this many times per timeout per

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_elector_ping_divisor 2
ceph config get mon mon_elector_ping_divisor
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_elector_ping_divisor
ceph -s
ceph mon stat
```

---

### mon_enable_op_tracker

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_enable_op_tracker](../../../config/mon/mon.md#SP_mon_enable_op_tracker) |

**作用：** enable/disable MON op tracking

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_enable_op_tracker false
ceph config get mon mon_enable_op_tracker
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_enable_op_tracker
ceph -s
ceph mon stat
```

---

### mon_fsmap_prune_threshold

| | |
|---|---|
| 类型 | Secs · default `300` · **Advanced** |
| 表格 | [mon.md#SP_mon_fsmap_prune_threshold](../../../config/mon/mon.md#SP_mon_fsmap_prune_threshold) |

**作用：** prune fsmap older than this threshold in seconds

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_fsmap_prune_threshold 300
ceph config get mon mon_fsmap_prune_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `300` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_fsmap_prune_threshold
ceph -s
ceph mon stat
```

---

### mon_health_max_detail

| | |
|---|---|
| 类型 | Uint · default `50` · **Advanced** |
| 表格 | [mon.md#SP_mon_health_max_detail](../../../config/mon/mon.md#SP_mon_health_max_detail) |

**作用：** max detailed pgs to report in health detail

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_health_max_detail 50
ceph config get mon mon_health_max_detail
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `50` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_health_max_detail
ceph -s
ceph mon stat
```

---

### mon_lease

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [mon.md#SP_mon_lease](../../../config/mon/mon.md#SP_mon_lease) |

**作用：** lease interval between quorum monitors (seconds)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_lease 5
ceph config get mon mon_lease
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_lease
ceph -s
ceph mon stat
```

---

### mon_mds_force_trim_to

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mon.md#SP_mon_mds_force_trim_to](../../../config/mon/mon.md#SP_mon_mds_force_trim_to) |

**作用：** force mons to trim mdsmaps/fsmaps up to this epoch

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_mds_force_trim_to 64
ceph config get mon mon_mds_force_trim_to
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_mds_skip_sanity

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [mon.md#SP_mon_mds_skip_sanity](../../../config/mon/mon.md#SP_mon_mds_skip_sanity) |

**作用：** skip sanity checks on fsmap/mdsmap

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mon mon_mds_skip_sanity true
ceph config get mon mon_mds_skip_sanity
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_mds_skip_sanity
ceph -s
ceph mon stat
```

---

### mon_memory_autotune

| | |
|---|---|
| 类型 | Bool · default `True` · **Basic** |
| 表格 | [mon.md#SP_mon_memory_autotune](../../../config/mon/mon.md#SP_mon_memory_autotune) |

**作用：** Autotune the cache memory being used for osd monitors and kv database

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_memory_autotune false
ceph config get mon mon_memory_autotune
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_memory_autotune
ceph -s
ceph mon stat
```

---

### mon_memory_target

| | |
|---|---|
| 类型 | Size · default `2_G` · **Basic** |
| 表格 | [mon.md#SP_mon_memory_target](../../../config/mon/mon.md#SP_mon_memory_target) |

**作用：** The amount of bytes pertaining to osd monitor caches and kv cache to be kept mapped in memory with cache auto-tuning enabled

**何时使用：** 核心 MON 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set mon mon_memory_target 2_G
ceph config get mon mon_memory_target
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `2_G` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_memory_target
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_beacon_grace

| | |
|---|---|
| 类型 | Secs · default `7` · **Advanced** |
| 表格 | [mon.md#SP_mon_nvmeofgw_beacon_grace](../../../config/mon/mon.md#SP_mon_nvmeofgw_beacon_grace) |

**作用：** Period in seconds from last beacon to monitor marking a NVMeoF gateway as failed

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_nvmeofgw_beacon_grace 7
ceph config get mon mon_nvmeofgw_beacon_grace
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `7` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_nvmeofgw_beacon_grace
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_beacons_till_ack

| | |
|---|---|
| 类型 | Uint · default `15` · **Advanced** |
| 表格 | [mon.md#SP_mon_nvmeofgw_beacons_till_ack](../../../config/mon/mon.md#SP_mon_nvmeofgw_beacons_till_ack) |

**作用：** Number of beacons from MonClient before NVMeofGwMon sends ack-map to it

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_nvmeofgw_beacons_till_ack 15
ceph config get mon mon_nvmeofgw_beacons_till_ack
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `15` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_nvmeofgw_beacons_till_ack
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_delete_grace

| | |
|---|---|
| 类型 | Secs · default `15_min` · **Advanced** |
| 表格 | [mon.md#SP_mon_nvmeofgw_delete_grace](../../../config/mon/mon.md#SP_mon_nvmeofgw_delete_grace) |

**作用：** Issue NVMEOF_GATEWAY_DELETING health warning after this amount of time has elapsed

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_nvmeofgw_delete_grace 15_min
ceph config get mon mon_nvmeofgw_delete_grace
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `15_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_nvmeofgw_delete_grace
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_set_group_id_retry

| | |
|---|---|
| 类型 | Uint · default `1000` · **Advanced** |
| 表格 | [mon.md#SP_mon_nvmeofgw_set_group_id_retry](../../../config/mon/mon.md#SP_mon_nvmeofgw_set_group_id_retry) |

**作用：** Retry wait time in microsecond for set group id between the monitor client and gateway

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_nvmeofgw_set_group_id_retry 1000
ceph config get mon mon_nvmeofgw_set_group_id_retry
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_nvmeofgw_set_group_id_retry
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_wrong_map_ignore_sec

| | |
|---|---|
| 类型 | Uint · default `15` · **Advanced** |
| 表格 | [mon.md#SP_mon_nvmeofgw_wrong_map_ignore_sec](../../../config/mon/mon.md#SP_mon_nvmeofgw_wrong_map_ignore_sec) |

**作用：** Period in seconds from MonClient startup to ignore wrong maps from Monitor

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_nvmeofgw_wrong_map_ignore_sec 15
ceph config get mon mon_nvmeofgw_wrong_map_ignore_sec
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `15` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_nvmeofgw_wrong_map_ignore_sec
ceph -s
ceph mon stat
```

---

### mon_op_complaint_time

| | |
|---|---|
| 类型 | Secs · default `30` · **Advanced** |
| 表格 | [mon.md#SP_mon_op_complaint_time](../../../config/mon/mon.md#SP_mon_op_complaint_time) |

**作用：** time after which to consider a monitor operation blocked after no updates

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_op_complaint_time 30
ceph config get mon mon_op_complaint_time
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_op_complaint_time
ceph -s
ceph mon stat
```

---

### mon_op_history_duration

| | |
|---|---|
| 类型 | Secs · default `10_min` · **Advanced** |
| 表格 | [mon.md#SP_mon_op_history_duration](../../../config/mon/mon.md#SP_mon_op_history_duration) |

**作用：** expiration time in seconds of historical MON OPS

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_op_history_duration 10_min
ceph config get mon mon_op_history_duration
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_op_history_duration
ceph -s
ceph mon stat
```

---

### mon_op_history_size

| | |
|---|---|
| 类型 | Uint · default `20` · **Advanced** |
| 表格 | [mon.md#SP_mon_op_history_size](../../../config/mon/mon.md#SP_mon_op_history_size) |

**作用：** max number of completed ops to track

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_op_history_size 20
ceph config get mon mon_op_history_size
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `20` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_op_history_size
ceph -s
ceph mon stat
```

---

### mon_op_history_slow_op_size

| | |
|---|---|
| 类型 | Uint · default `20` · **Advanced** |
| 表格 | [mon.md#SP_mon_op_history_slow_op_size](../../../config/mon/mon.md#SP_mon_op_history_slow_op_size) |

**作用：** max number of slow historical MON OPS to keep

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_op_history_slow_op_size 20
ceph config get mon mon_op_history_slow_op_size
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `20` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_op_history_slow_op_size
ceph -s
ceph mon stat
```

---

### mon_op_history_slow_op_threshold

| | |
|---|---|
| 类型 | Secs · default `10` · **Advanced** |
| 表格 | [mon.md#SP_mon_op_history_slow_op_threshold](../../../config/mon/mon.md#SP_mon_op_history_slow_op_threshold) |

**作用：** duration of an op to be considered as a historical slow op

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_op_history_slow_op_threshold 10
ceph config get mon mon_op_history_slow_op_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_op_history_slow_op_threshold
ceph -s
ceph mon stat
```

---

### mon_rocksdb_options

| | |
|---|---|
| 类型 | Str · default `write_buffer_size=33554432,compression=kNoCompression,level_compaction_dynamic_level_bytes=true` · **Advanced** |
| 表格 | [mon.md#SP_mon_rocksdb_options](../../../config/mon/mon.md#SP_mon_rocksdb_options) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_rocksdb_options "write_buffer_size=33554432,compression=kNoCompression,level_compaction_dynamic_level_bytes=true"
ceph config get mon mon_rocksdb_options
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `write_buffer_size=33554432,compression=kNoCompression,level_compaction_dynamic_level_bytes=true` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_rocksdb_options
ceph -s
ceph mon stat
```

---

### mon_stretch_cluster_recovery_ratio

| | |
|---|---|
| 类型 | Float · default `0.6` · **Advanced** |
| 表格 | [mon.md#SP_mon_stretch_cluster_recovery_ratio](../../../config/mon/mon.md#SP_mon_stretch_cluster_recovery_ratio) |

**作用：** the ratio of up OSDs at which a degraded stretch cluster enters recovery

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_stretch_cluster_recovery_ratio 0.6
ceph config get mon mon_stretch_cluster_recovery_ratio
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.6` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0.51`，最大 `1`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_stretch_cluster_recovery_ratio
ceph -s
ceph mon stat
```

---

### mon_stretch_max_bucket_weight_delta

| | |
|---|---|
| 类型 | Float · default `0.1` · **Dev** |
| 表格 | [mon.md#SP_mon_stretch_max_bucket_weight_delta](../../../config/mon/mon.md#SP_mon_stretch_max_bucket_weight_delta) |

**作用：** Max difference allowed among CRUSH bucket weights when in stretch mode. The value is a percentage expressed as a real number between 0.0 and 1.0.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_stretch_max_bucket_weight_delta 0.1
ceph config get mon mon_stretch_max_bucket_weight_delta
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0.1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_stretch_recovery_min_wait

| | |
|---|---|
| 类型 | Float · default `15` · **Advanced** |
| 表格 | [mon.md#SP_mon_stretch_recovery_min_wait](../../../config/mon/mon.md#SP_mon_stretch_recovery_min_wait) |

**作用：** how long the monitors wait before considering fully-healthy PGs as evidence the stretch mode is repaired

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_stretch_recovery_min_wait 15
ceph config get mon mon_stretch_recovery_min_wait
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `15` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_stretch_recovery_min_wait
ceph -s
ceph mon stat
```

---

### mon_warn_on_colocated_monitors

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [mon.md#SP_mon_warn_on_colocated_monitors](../../../config/mon/mon.md#SP_mon_warn_on_colocated_monitors) |

**作用：** Issue MON_COLOCATED health warning if two or more Monitors have the same IP address

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mon mon_warn_on_colocated_monitors true
ceph config get mon mon_warn_on_colocated_monitors
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_warn_on_colocated_monitors
ceph -s
ceph mon stat
```

---

### mon_warn_on_crush_straw_calc_version_zero

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_warn_on_crush_straw_calc_version_zero](../../../config/mon/mon.md#SP_mon_warn_on_crush_straw_calc_version_zero) |

**作用：** issue OLD_CRUSH_STRAW_CALC_VERSION health warning if the CRUSH map's straw_calc_version is zero

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_warn_on_crush_straw_calc_version_zero false
ceph config get mon mon_warn_on_crush_straw_calc_version_zero
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_warn_on_crush_straw_calc_version_zero
ceph -s
ceph mon stat
```

---

### mon_warn_on_degraded_stretch_mode

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_warn_on_degraded_stretch_mode](../../../config/mon/mon.md#SP_mon_warn_on_degraded_stretch_mode) |

**作用：** Issue a health warning if we are in degraded stretch mode

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_warn_on_degraded_stretch_mode false
ceph config get mon mon_warn_on_degraded_stretch_mode
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_warn_on_degraded_stretch_mode
ceph -s
ceph mon stat
```

---

### mon_warn_on_legacy_crush_tunables

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_warn_on_legacy_crush_tunables](../../../config/mon/mon.md#SP_mon_warn_on_legacy_crush_tunables) |

**作用：** issue OLD_CRUSH_TUNABLES health warning if CRUSH tunables are older than mon_crush_min_required_version

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_warn_on_legacy_crush_tunables false
ceph config get mon mon_warn_on_legacy_crush_tunables
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_warn_on_legacy_crush_tunables
ceph -s
ceph mon stat
```

---

### mon_warn_on_older_version

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_warn_on_older_version](../../../config/mon/mon.md#SP_mon_warn_on_older_version) |

**作用：** issue DAEMON_OLD_VERSION health warning if daemons are not all running the same version

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_warn_on_older_version false
ceph config get mon mon_warn_on_older_version
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_warn_on_older_version
ceph -s
ceph mon stat
```

---

### nvmeof_mon_client_connect_panic

| | |
|---|---|
| 类型 | Secs · default `30` · **Advanced** |
| 表格 | [mon.md#SP_nvmeof_mon_client_connect_panic](../../../config/mon/mon.md#SP_nvmeof_mon_client_connect_panic) |

**作用：** The duration, expressed in seconds, after which the nvmeof gateway should trigger a panic if it does not receive the initial map from the monitor

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon nvmeof_mon_client_connect_panic 30
ceph config get mon nvmeof_mon_client_connect_panic
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon nvmeof_mon_client_connect_panic
ceph -s
ceph mon stat
```

---

### nvmeof_mon_client_disconnect_panic

| | |
|---|---|
| 类型 | Secs · default `100` · **Advanced** |
| 表格 | [mon.md#SP_nvmeof_mon_client_disconnect_panic](../../../config/mon/mon.md#SP_nvmeof_mon_client_disconnect_panic) |

**作用：** The duration, expressed in seconds, after which the nvmeof gateway should trigger a panic if it loses connection to the monitor

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon nvmeof_mon_client_disconnect_panic 100
ceph config get mon nvmeof_mon_client_disconnect_panic
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `100` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon nvmeof_mon_client_disconnect_panic
ceph -s
ceph mon stat
```

---


[← 概览](../OVERVIEW.md)
