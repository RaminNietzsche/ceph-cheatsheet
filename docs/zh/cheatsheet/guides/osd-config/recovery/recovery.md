# Recovery & backfill

OSD 配置深度指南 — 28 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [osd_allow_recovery_below_min_size](#osd_allow_recovery_below_min_size) | `True` | Dev | 开发 |
| [osd_backfill_retry_interval](#osd_backfill_retry_interval) | `30` | Advanced | 性能 |
| [osd_backfill_scan_max](#osd_backfill_scan_max) | `512` | Advanced | 性能 |
| [osd_backfill_scan_min](#osd_backfill_scan_min) | `64` | Advanced | 性能 |
| [osd_max_backfills](#osd_max_backfills) | `1` | Advanced | 性能 |
| [osd_mclock_override_recovery_settings](#osd_mclock_override_recovery_settings) | `False` | Advanced | 性能 |
| [osd_mclock_scheduler_background_recovery_lim](#osd_mclock_scheduler_background_recovery_lim) | `0` | Advanced | 性能 |
| [osd_mclock_scheduler_background_recovery_res](#osd_mclock_scheduler_background_recovery_res) | `0` | Advanced | 性能 |
| [osd_mclock_scheduler_background_recovery_wgt](#osd_mclock_scheduler_background_recovery_wgt) | `1` | Advanced | 性能 |
| [osd_min_recovery_priority](#osd_min_recovery_priority) | `0` | Advanced | 性能 |
| [osd_recover_clone_overlap](#osd_recover_clone_overlap) | `True` | Advanced | 性能 |
| [osd_recover_clone_overlap_limit](#osd_recover_clone_overlap_limit) | `10` | Advanced | 性能 |
| [osd_recovery_delay_start](#osd_recovery_delay_start) | `0` | Advanced | 性能 |
| [osd_recovery_max_active](#osd_recovery_max_active) | `0` | Advanced | 性能 |
| [osd_recovery_max_active_hdd](#osd_recovery_max_active_hdd) | `3` | Advanced | 性能 |
| [osd_recovery_max_active_ssd](#osd_recovery_max_active_ssd) | `10` | Advanced | 性能 |
| [osd_recovery_max_chunk](#osd_recovery_max_chunk) | `8_M` | Advanced | 性能 |
| [osd_recovery_max_omap_entries_per_chunk](#osd_recovery_max_omap_entries_per_chunk) | `8096` | Advanced | 性能 |
| [osd_recovery_max_single_start](#osd_recovery_max_single_start) | `1` | Advanced | 性能 |
| [osd_recovery_retry_interval](#osd_recovery_retry_interval) | `30` | Advanced | 性能 |
| [osd_recovery_sleep](#osd_recovery_sleep) | `0` | Advanced | 性能 |
| [osd_recovery_sleep_degraded](#osd_recovery_sleep_degraded) | `0` | Advanced | 性能 |
| [osd_recovery_sleep_degraded_hdd](#osd_recovery_sleep_degraded_hdd) | `0.1` | Advanced | 性能 |
| [osd_recovery_sleep_degraded_hybrid](#osd_recovery_sleep_degraded_hybrid) | `0.025` | Advanced | 性能 |
| [osd_recovery_sleep_degraded_ssd](#osd_recovery_sleep_degraded_ssd) | `0` | Advanced | 性能 |
| [osd_recovery_sleep_hdd](#osd_recovery_sleep_hdd) | `0.1` | Advanced | 性能 |
| [osd_recovery_sleep_hybrid](#osd_recovery_sleep_hybrid) | `0.025` | Advanced | 性能 |
| [osd_recovery_sleep_ssd](#osd_recovery_sleep_ssd) | `0` | Advanced | 性能 |

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
ceph config get <daemon> <option>  # e.g. osd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_allow_recovery_below_min_size

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [osd.md#SP_osd_allow_recovery_below_min_size](../../../config/osd/osd.md#SP_osd_allow_recovery_below_min_size) |

**作用：** allow replicated pools to recover with < min_size active members

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_allow_recovery_below_min_size false
ceph config get osd osd_allow_recovery_below_min_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_backfill_retry_interval

| | |
|---|---|
| 类型 | Float · default `30` · **Advanced** |
| 表格 | [osd.md#SP_osd_backfill_retry_interval](../../../config/osd/osd.md#SP_osd_backfill_retry_interval) |

**作用：** how frequently to retry backfill reservations after being denied (e.g., due to a full OSD)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_backfill_retry_interval 30
ceph config get osd osd_backfill_retry_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_backfill_retry_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_backfill_scan_max

| | |
|---|---|
| 类型 | Int · default `512` · **Advanced** |
| 表格 | [osd.md#SP_osd_backfill_scan_max](../../../config/osd/osd.md#SP_osd_backfill_scan_max) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_backfill_scan_max 512
ceph config get osd osd_backfill_scan_max
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `512` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_backfill_scan_max
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_backfill_scan_min

| | |
|---|---|
| 类型 | Int · default `64` · **Advanced** |
| 表格 | [osd.md#SP_osd_backfill_scan_min](../../../config/osd/osd.md#SP_osd_backfill_scan_min) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_backfill_scan_min 64
ceph config get osd osd_backfill_scan_min
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_backfill_scan_min
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_backfills

| | |
|---|---|
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_backfills](../../../config/osd/osd.md#SP_osd_max_backfills) |

**作用：** Maximum number of concurrent local and remote backfills or recoveries per OSD

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_max_backfills 1
ceph config get osd osd_max_backfills
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_max_backfills
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_override_recovery_settings

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_mclock_override_recovery_settings](../../../config/osd/osd.md#SP_osd_mclock_override_recovery_settings) |

**作用：** Setting this option enables the override of recovery/backfill limits for the mClock scheduler.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_mclock_override_recovery_settings true
ceph config get osd osd_mclock_override_recovery_settings
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_mclock_override_recovery_settings
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_background_recovery_lim

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_mclock_scheduler_background_recovery_lim](../../../config/osd/osd.md#SP_osd_mclock_scheduler_background_recovery_lim) |

**作用：** IO limit for background recovery over reservation. The default value of 0 specifies no limit enforcement, which means background recovery operation can use the maximum possible IOPS capacity of the OSD. Any value greater than 0 and up to 1.0 specifies the upper IO limit over reservation that background recovery operation receives in terms of a fraction of the OSD's maximum IOPS capacity. Ignored unless osd_mclock_profile is set to 'custom'.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_mclock_scheduler_background_recovery_lim 0
ceph config get osd osd_mclock_scheduler_background_recovery_lim
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `1.0`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_mclock_scheduler_background_recovery_lim
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_background_recovery_res

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_mclock_scheduler_background_recovery_res](../../../config/osd/osd.md#SP_osd_mclock_scheduler_background_recovery_res) |

**作用：** IO proportion reserved for background recovery (default). The default value of 0 specifies the lowest possible reservation. Any value greater than 0 and up to 1.0 specifies the minimum IO proportion to reserve for background recovery operations in terms of a fraction of the OSD's maximum IOPS capacity. Ignored unless osd_mclock_profile is set to 'custom'.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_mclock_scheduler_background_recovery_res 0
ceph config get osd osd_mclock_scheduler_background_recovery_res
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `1.0`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_mclock_scheduler_background_recovery_res
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_background_recovery_wgt

| | |
|---|---|
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [osd.md#SP_osd_mclock_scheduler_background_recovery_wgt](../../../config/osd/osd.md#SP_osd_mclock_scheduler_background_recovery_wgt) |

**作用：** IO share for each background recovery over reservation Ignored unless osd_mclock_profile is set to 'custom'.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_mclock_scheduler_background_recovery_wgt 1
ceph config get osd osd_mclock_scheduler_background_recovery_wgt
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_mclock_scheduler_background_recovery_wgt
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_min_recovery_priority

| | |
|---|---|
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_min_recovery_priority](../../../config/osd/osd.md#SP_osd_min_recovery_priority) |

**作用：** Minimum priority below which recovery is not performed

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_min_recovery_priority 64
ceph config get osd osd_min_recovery_priority
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_min_recovery_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recover_clone_overlap

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_recover_clone_overlap](../../../config/osd/osd.md#SP_osd_recover_clone_overlap) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_recover_clone_overlap false
ceph config get osd osd_recover_clone_overlap
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_recover_clone_overlap
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recover_clone_overlap_limit

| | |
|---|---|
| 类型 | Uint · default `10` · **Advanced** |
| 表格 | [osd.md#SP_osd_recover_clone_overlap_limit](../../../config/osd/osd.md#SP_osd_recover_clone_overlap_limit) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_recover_clone_overlap_limit 10
ceph config get osd osd_recover_clone_overlap_limit
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_recover_clone_overlap_limit
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_delay_start

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_delay_start](../../../config/osd/osd.md#SP_osd_recovery_delay_start) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_recovery_delay_start 0
ceph config get osd osd_recovery_delay_start
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_recovery_delay_start
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_max_active

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_max_active](../../../config/osd/osd.md#SP_osd_recovery_max_active) |

**作用：** Cap on concurrent recovery/backfill operations per OSD (0 = derive from HDD/SSD/hybrid-specific settings).

**何时使用：** Raise temporarily after OSD replacement to rebuild faster; lower during production peaks to protect client latency.

**示例：**

```bash
ceph config set osd osd_recovery_max_active 64
ceph config get osd osd_recovery_max_active
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_recovery_max_active
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

Watch `recovering`/`backfilling` PG count and client p99. See also `osd_recovery_max_active_hdd` / `_ssd` when set to 0.

---

### osd_recovery_max_active_hdd

| | |
|---|---|
| 类型 | Uint · default `3` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_max_active_hdd](../../../config/osd/osd.md#SP_osd_recovery_max_active_hdd) |

**作用：** Number of simultaneous active recovery operations per OSD (for rotational devices)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_recovery_max_active_hdd 3
ceph config get osd osd_recovery_max_active_hdd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_recovery_max_active_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_max_active_ssd

| | |
|---|---|
| 类型 | Uint · default `10` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_max_active_ssd](../../../config/osd/osd.md#SP_osd_recovery_max_active_ssd) |

**作用：** Number of simultaneous active recovery operations per OSD (for non-rotational solid state devices)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_recovery_max_active_ssd 10
ceph config get osd osd_recovery_max_active_ssd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_recovery_max_active_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_max_chunk

| | |
|---|---|
| 类型 | Size · default `8_M` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_max_chunk](../../../config/osd/osd.md#SP_osd_recovery_max_chunk) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_recovery_max_chunk 8_M
ceph config get osd osd_recovery_max_chunk
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `8_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_recovery_max_chunk
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_max_omap_entries_per_chunk

| | |
|---|---|
| 类型 | Uint · default `8096` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_max_omap_entries_per_chunk](../../../config/osd/osd.md#SP_osd_recovery_max_omap_entries_per_chunk) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_recovery_max_omap_entries_per_chunk 8096
ceph config get osd osd_recovery_max_omap_entries_per_chunk
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `8096` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_recovery_max_omap_entries_per_chunk
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_max_single_start

| | |
|---|---|
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_max_single_start](../../../config/osd/osd.md#SP_osd_recovery_max_single_start) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_recovery_max_single_start 1
ceph config get osd osd_recovery_max_single_start
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_recovery_max_single_start
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_retry_interval

| | |
|---|---|
| 类型 | Float · default `30` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_retry_interval](../../../config/osd/osd.md#SP_osd_recovery_retry_interval) |

**作用：** how frequently to retry recovery reservations after being denied (e.g., due to a full OSD)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_recovery_retry_interval 30
ceph config get osd osd_recovery_retry_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_recovery_retry_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_sleep

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_sleep](../../../config/osd/osd.md#SP_osd_recovery_sleep) |

**作用：** Pause between recovery/backfill chunks (seconds). Non-zero values throttle recovery to leave headroom for application I/O.

**何时使用：** Use on busy clusters during business hours; set to 0 for fastest rebuild in maintenance windows.

**示例：**

```bash
ceph config set osd osd_recovery_sleep 0
ceph config get osd osd_recovery_sleep
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_recovery_sleep
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_sleep_degraded

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_sleep_degraded](../../../config/osd/osd.md#SP_osd_recovery_sleep_degraded) |

**作用：** Time in seconds to sleep before next recovery or backfill op when PGs are degraded. This setting overrides _ssd, _hdd, and _hybrid if non-zero.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_recovery_sleep_degraded 0
ceph config get osd osd_recovery_sleep_degraded
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_recovery_sleep_degraded
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_sleep_degraded_hdd

| | |
|---|---|
| 类型 | Float · default `0.1` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_sleep_degraded_hdd](../../../config/osd/osd.md#SP_osd_recovery_sleep_degraded_hdd) |

**作用：** Time in seconds to sleep before next recovery or backfill op for HDDs when PGs is degraded.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_recovery_sleep_degraded_hdd 0.1
ceph config get osd osd_recovery_sleep_degraded_hdd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_recovery_sleep_degraded_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_sleep_degraded_hybrid

| | |
|---|---|
| 类型 | Float · default `0.025` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_sleep_degraded_hybrid](../../../config/osd/osd.md#SP_osd_recovery_sleep_degraded_hybrid) |

**作用：** Time in seconds to sleep before next recovery or backfill op when PGs are degraded and data is on HDD and journal is on SSD

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_recovery_sleep_degraded_hybrid 0.025
ceph config get osd osd_recovery_sleep_degraded_hybrid
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.025` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_recovery_sleep_degraded_hybrid
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_sleep_degraded_ssd

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_sleep_degraded_ssd](../../../config/osd/osd.md#SP_osd_recovery_sleep_degraded_ssd) |

**作用：** Time in seconds to sleep before next recovery or backfill op for SSDs when PGs are degraded.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_recovery_sleep_degraded_ssd 0
ceph config get osd osd_recovery_sleep_degraded_ssd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_recovery_sleep_degraded_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_sleep_hdd

| | |
|---|---|
| 类型 | Float · default `0.1` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_sleep_hdd](../../../config/osd/osd.md#SP_osd_recovery_sleep_hdd) |

**作用：** Time in seconds to sleep before next recovery or backfill op for HDDs

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_recovery_sleep_hdd 0.1
ceph config get osd osd_recovery_sleep_hdd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_recovery_sleep_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_sleep_hybrid

| | |
|---|---|
| 类型 | Float · default `0.025` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_sleep_hybrid](../../../config/osd/osd.md#SP_osd_recovery_sleep_hybrid) |

**作用：** Time in seconds to sleep before next recovery or backfill op when data is on HDD and journal is on SSD

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_recovery_sleep_hybrid 0.025
ceph config get osd osd_recovery_sleep_hybrid
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.025` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_recovery_sleep_hybrid
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_sleep_ssd

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_recovery_sleep_ssd](../../../config/osd/osd.md#SP_osd_recovery_sleep_ssd) |

**作用：** Time in seconds to sleep before next recovery or backfill op for SSDs

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_recovery_sleep_ssd 0
ceph config get osd osd_recovery_sleep_ssd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_recovery_sleep_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← 概览](../OVERVIEW.md)
