# mClock scheduler

OSD 配置深度指南 — 18 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [osd_mclock_force_run_benchmark_on_init](#osd_mclock_force_run_benchmark_on_init) | `False` | Advanced | 性能 |
| [osd_mclock_iops_capacity_low_threshold_hdd](#osd_mclock_iops_capacity_low_threshold_hdd) | `50` | Basic | 性能 |
| [osd_mclock_iops_capacity_low_threshold_ssd](#osd_mclock_iops_capacity_low_threshold_ssd) | `1000` | Basic | 性能 |
| [osd_mclock_iops_capacity_threshold_hdd](#osd_mclock_iops_capacity_threshold_hdd) | `500` | Basic | 性能 |
| [osd_mclock_iops_capacity_threshold_ssd](#osd_mclock_iops_capacity_threshold_ssd) | `80000` | Basic | 性能 |
| [osd_mclock_max_capacity_iops_hdd](#osd_mclock_max_capacity_iops_hdd) | `315` | Basic | 性能 |
| [osd_mclock_max_capacity_iops_ssd](#osd_mclock_max_capacity_iops_ssd) | `21500` | Basic | 性能 |
| [osd_mclock_max_sequential_bandwidth_hdd](#osd_mclock_max_sequential_bandwidth_hdd) | `150_M` | Basic | 性能 |
| [osd_mclock_max_sequential_bandwidth_ssd](#osd_mclock_max_sequential_bandwidth_ssd) | `1200_M` | Basic | 性能 |
| [osd_mclock_profile](#osd_mclock_profile) | `balanced` | Advanced | 性能 |
| [osd_mclock_scheduler_anticipation_timeout](#osd_mclock_scheduler_anticipation_timeout) | `0` | Advanced | 性能 |
| [osd_mclock_scheduler_background_best_effort_lim](#osd_mclock_scheduler_background_best_effort_lim) | `0` | Advanced | 性能 |
| [osd_mclock_scheduler_background_best_effort_res](#osd_mclock_scheduler_background_best_effort_res) | `0` | Advanced | 性能 |
| [osd_mclock_scheduler_background_best_effort_wgt](#osd_mclock_scheduler_background_best_effort_wgt) | `1` | Advanced | 性能 |
| [osd_mclock_scheduler_client_lim](#osd_mclock_scheduler_client_lim) | `0` | Advanced | 性能 |
| [osd_mclock_scheduler_client_res](#osd_mclock_scheduler_client_res) | `0` | Advanced | 性能 |
| [osd_mclock_scheduler_client_wgt](#osd_mclock_scheduler_client_wgt) | `1` | Advanced | 性能 |
| [osd_mclock_skip_benchmark](#osd_mclock_skip_benchmark) | `False` | Dev | 开发 |

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

### osd_mclock_force_run_benchmark_on_init

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [osd.md#SP_osd_mclock_force_run_benchmark_on_init](../../../config/osd/osd.md#SP_osd_mclock_force_run_benchmark_on_init) |

**作用：** Force run the OSD benchmark on OSD initialization/boot-up This option specifies whether the OSD benchmark must be run during the OSD boot-up sequence even if historical data about the OSD iops capacity is available in the MON config store. Enable this to refresh the OSD iops capacity if the underlying device's performance characteristics have changed significantly. Only considered for osd_op_queue = mclock_scheduler.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_mclock_force_run_benchmark_on_init true
ceph config get osd osd_mclock_force_run_benchmark_on_init
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_mclock_force_run_benchmark_on_init
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_iops_capacity_low_threshold_hdd

| | |
|---|---|
| 类型 | Float · default `50` · **Basic** |
| 表格 | [osd.md#SP_osd_mclock_iops_capacity_low_threshold_hdd](../../../config/osd/osd.md#SP_osd_mclock_iops_capacity_low_threshold_hdd) |

**作用：** The threshold IOPs capacity (at 4KiB block size) below which to ignore the OSD bench results for an OSD (for rotational media) This option specifies the low threshold IOPS capacity of an OSD above which the OSD bench results can be considered for QoS calculations. Only considered when osd_op_queue = mclock_scheduler

**何时使用：** 触及资源限制或保护集群容量时调整。

**相关选项：**

- [`osd_mclock_max_capacity_iops_hdd`](../../../config/osd/osd.md#SP_osd_mclock_max_capacity_iops_hdd)

**示例：**

```bash
ceph config set osd osd_mclock_iops_capacity_low_threshold_hdd 50
ceph config get osd osd_mclock_iops_capacity_low_threshold_hdd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `50` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_mclock_iops_capacity_low_threshold_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_iops_capacity_low_threshold_ssd

| | |
|---|---|
| 类型 | Float · default `1000` · **Basic** |
| 表格 | [osd.md#SP_osd_mclock_iops_capacity_low_threshold_ssd](../../../config/osd/osd.md#SP_osd_mclock_iops_capacity_low_threshold_ssd) |

**作用：** The threshold IOPs capacity (at 4KiB block size) below which to ignore the OSD bench results for an OSD (for solid state media) This option specifies the low threshold IOPS capacity for an OSD above which the OSD bench results can be considered for QoS calculations. Only considered when osd_op_queue = mclock_scheduler

**何时使用：** 触及资源限制或保护集群容量时调整。

**相关选项：**

- [`osd_mclock_max_capacity_iops_ssd`](../../../config/osd/osd.md#SP_osd_mclock_max_capacity_iops_ssd)

**示例：**

```bash
ceph config set osd osd_mclock_iops_capacity_low_threshold_ssd 1000
ceph config get osd osd_mclock_iops_capacity_low_threshold_ssd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_mclock_iops_capacity_low_threshold_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_iops_capacity_threshold_hdd

| | |
|---|---|
| 类型 | Float · default `500` · **Basic** |
| 表格 | [osd.md#SP_osd_mclock_iops_capacity_threshold_hdd](../../../config/osd/osd.md#SP_osd_mclock_iops_capacity_threshold_hdd) |

**作用：** The threshold IOPs capacity (at 4KiB block size) beyond which to ignore the OSD bench results for an OSD (for rotational media) This option specifies the high threshold IOPS capacity for an OSD below which the OSD bench results can be considered for QoS calculations. Only considered when osd_op_queue = mclock_scheduler

**何时使用：** 触及资源限制或保护集群容量时调整。

**相关选项：**

- [`osd_mclock_max_capacity_iops_hdd`](../../../config/osd/osd.md#SP_osd_mclock_max_capacity_iops_hdd)

**示例：**

```bash
ceph config set osd osd_mclock_iops_capacity_threshold_hdd 500
ceph config get osd osd_mclock_iops_capacity_threshold_hdd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `500` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_mclock_iops_capacity_threshold_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_iops_capacity_threshold_ssd

| | |
|---|---|
| 类型 | Float · default `80000` · **Basic** |
| 表格 | [osd.md#SP_osd_mclock_iops_capacity_threshold_ssd](../../../config/osd/osd.md#SP_osd_mclock_iops_capacity_threshold_ssd) |

**作用：** The threshold IOPs capacity (at 4KiB block size) beyond which to ignore the OSD bench results for an OSD (for solid state media) This option specifies the high threshold IOPS capacity for an OSD below which the OSD bench results can be considered for QoS calculations. Only considered when osd_op_queue = mclock_scheduler

**何时使用：** 触及资源限制或保护集群容量时调整。

**相关选项：**

- [`osd_mclock_max_capacity_iops_ssd`](../../../config/osd/osd.md#SP_osd_mclock_max_capacity_iops_ssd)

**示例：**

```bash
ceph config set osd osd_mclock_iops_capacity_threshold_ssd 80000
ceph config get osd osd_mclock_iops_capacity_threshold_ssd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `80000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_mclock_iops_capacity_threshold_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_max_capacity_iops_hdd

| | |
|---|---|
| 类型 | Float · default `315` · **Basic** |
| 表格 | [osd.md#SP_osd_mclock_max_capacity_iops_hdd](../../../config/osd/osd.md#SP_osd_mclock_max_capacity_iops_hdd) |

**作用：** Max random write IOPS capacity (at 4KiB block size) to consider per OSD (for rotational media) This option specifies the max OSD random write IOPS capacity per OSD. Contributes in QoS calculations when enabling a dmclock profile. Only considered for osd_op_queue = mclock_scheduler

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_mclock_max_capacity_iops_hdd 315
ceph config get osd osd_mclock_max_capacity_iops_hdd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `315` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_mclock_max_capacity_iops_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_max_capacity_iops_ssd

| | |
|---|---|
| 类型 | Float · default `21500` · **Basic** |
| 表格 | [osd.md#SP_osd_mclock_max_capacity_iops_ssd](../../../config/osd/osd.md#SP_osd_mclock_max_capacity_iops_ssd) |

**作用：** Max random write IOPS capacity (at 4 KiB block size) to consider per OSD (for solid state media) This option specifies the max OSD random write IOPS capacity per OSD. Contributes in QoS calculations when enabling a dmclock profile. Only considered for osd_op_queue = mclock_scheduler

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_mclock_max_capacity_iops_ssd 21500
ceph config get osd osd_mclock_max_capacity_iops_ssd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `21500` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_mclock_max_capacity_iops_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_max_sequential_bandwidth_hdd

| | |
|---|---|
| 类型 | Size · default `150_M` · **Basic** |
| 表格 | [osd.md#SP_osd_mclock_max_sequential_bandwidth_hdd](../../../config/osd/osd.md#SP_osd_mclock_max_sequential_bandwidth_hdd) |

**作用：** The maximum sequential bandwidth in bytes/second of the OSD (for rotational media) This option specifies the maximum sequential bandwidth to consider for an OSD whose underlying device type is rotational media. This is considered by the mclock scheduler to derive the cost factor to be used in QoS calculations. Only considered for osd_op_queue = mclock_scheduler

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_mclock_max_sequential_bandwidth_hdd 150_M
ceph config get osd osd_mclock_max_sequential_bandwidth_hdd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `150_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_mclock_max_sequential_bandwidth_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_max_sequential_bandwidth_ssd

| | |
|---|---|
| 类型 | Size · default `1200_M` · **Basic** |
| 表格 | [osd.md#SP_osd_mclock_max_sequential_bandwidth_ssd](../../../config/osd/osd.md#SP_osd_mclock_max_sequential_bandwidth_ssd) |

**作用：** The maximum sequential bandwidth in bytes/second of the OSD (for solid state media) This option specifies the maximum sequential bandwidth to consider for an OSD whose underlying device type is solid state media. This is considered by the mclock scheduler to derive the cost factor to be used in QoS calculations. Only considered for osd_op_queue = mclock_scheduler

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_mclock_max_sequential_bandwidth_ssd 1200_M
ceph config get osd osd_mclock_max_sequential_bandwidth_ssd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1200_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_mclock_max_sequential_bandwidth_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_profile

| | |
|---|---|
| 类型 | Str · enum: ["balanced", "high_recovery_ops", "high_client_ops", "custom"] · default `balanced` · **Advanced** |
| 表格 | [osd.md#SP_osd_mclock_profile](../../../config/osd/osd.md#SP_osd_mclock_profile) |

**作用：** Selects the mClock scheduler profile (`balanced`, `high_client_ops`, `high_recovery_ops`, or custom).

**何时使用：** Start with `balanced` on mixed workloads. Use `high_client_ops` when recovery dominates latency; `high_recovery_ops` for aggressive rebuild windows.

**相关选项：**

- [`osd_op_queue`](../../../config/osd/osd.md#SP_osd_op_queue)

**示例：**

```bash
ceph config set osd osd_mclock_profile high_client_ops
ceph config get osd osd_mclock_profile
ceph daemon osd.<id> config show | grep mclock
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `balanced` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_mclock_profile
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_anticipation_timeout

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_mclock_scheduler_anticipation_timeout](../../../config/osd/osd.md#SP_osd_mclock_scheduler_anticipation_timeout) |

**作用：** mclock anticipation timeout in seconds the amount of time that mclock waits until the unused resource is forfeited

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_mclock_scheduler_anticipation_timeout 0
ceph config get osd osd_mclock_scheduler_anticipation_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_mclock_scheduler_anticipation_timeout
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_background_best_effort_lim

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_mclock_scheduler_background_best_effort_lim](../../../config/osd/osd.md#SP_osd_mclock_scheduler_background_best_effort_lim) |

**作用：** IO limit for background best_effort over reservation. The default value of 0 specifies no limit enforcement, which means background best_effort operation can use the maximum possible IOPS capacity of the OSD. Any value greater than 0 and up to 1.0 specifies the upper IO limit over reservation that background best_effort operation receives in terms of a fraction of the OSD's maximum IOPS capacity. Ignored unless osd_mclock_profile is set to 'custom'. Only considered for osd_op_queue = mclock_scheduler

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_mclock_scheduler_background_best_effort_lim 0
ceph config get osd osd_mclock_scheduler_background_best_effort_lim
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
ceph config get osd osd_mclock_scheduler_background_best_effort_lim
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_background_best_effort_res

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_mclock_scheduler_background_best_effort_res](../../../config/osd/osd.md#SP_osd_mclock_scheduler_background_best_effort_res) |

**作用：** IO proportion reserved for background best_effort (default). The default value of 0 specifies the lowest possible reservation. Any value greater than 0 and up to 1.0 specifies the minimum IO proportion to reserve for background best_effort operations in terms of a fraction of the OSD's maximum IOPS capacity. Ignored unless osd_mclock_profile is set to 'custom'. Only considered for osd_op_queue = mclock_scheduler

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_mclock_scheduler_background_best_effort_res 0
ceph config get osd osd_mclock_scheduler_background_best_effort_res
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
ceph config get osd osd_mclock_scheduler_background_best_effort_res
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_background_best_effort_wgt

| | |
|---|---|
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [osd.md#SP_osd_mclock_scheduler_background_best_effort_wgt](../../../config/osd/osd.md#SP_osd_mclock_scheduler_background_best_effort_wgt) |

**作用：** IO share for each background best_effort over reservation Ignored unless osd_mclock_profile is set to 'custom'. Only considered for osd_op_queue = mclock_scheduler

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_mclock_scheduler_background_best_effort_wgt 1
ceph config get osd osd_mclock_scheduler_background_best_effort_wgt
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_mclock_scheduler_background_best_effort_wgt
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_client_lim

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_mclock_scheduler_client_lim](../../../config/osd/osd.md#SP_osd_mclock_scheduler_client_lim) |

**作用：** IO limit for each client (default) over reservation. The default value of 0 specifies no limit enforcement, which means each client can use the maximum possible IOPS capacity of the OSD. Any value greater than 0 and up to 1.0 specifies the upper IO limit over reservation that each client receives in terms of a fraction of the OSD's maximum IOPS capacity. Ignored unless osd_mclock_profile is set to 'custom'. Only considered for osd_op_queue = mclock_scheduler

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_mclock_scheduler_client_lim 0
ceph config get osd osd_mclock_scheduler_client_lim
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
ceph config get osd osd_mclock_scheduler_client_lim
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_client_res

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_mclock_scheduler_client_res](../../../config/osd/osd.md#SP_osd_mclock_scheduler_client_res) |

**作用：** IO proportion reserved for each client (default). The default value of 0 specifies the lowest possible reservation. Any value greater than 0 and up to 1.0 specifies the minimum IO proportion to reserve for each client in terms of a fraction of the OSD's maximum IOPS capacity. Ignored unless osd_mclock_profile is set to 'custom'. Only considered for osd_op_queue = mclock_scheduler

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_mclock_scheduler_client_res 0
ceph config get osd osd_mclock_scheduler_client_res
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
ceph config get osd osd_mclock_scheduler_client_res
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_client_wgt

| | |
|---|---|
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [osd.md#SP_osd_mclock_scheduler_client_wgt](../../../config/osd/osd.md#SP_osd_mclock_scheduler_client_wgt) |

**作用：** IO share for each client (default) over reservation Ignored unless osd_mclock_profile is set to 'custom'. Only considered for osd_op_queue = mclock_scheduler

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_mclock_scheduler_client_wgt 1
ceph config get osd osd_mclock_scheduler_client_wgt
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_mclock_scheduler_client_wgt
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_skip_benchmark

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_mclock_skip_benchmark](../../../config/osd/osd.md#SP_osd_mclock_skip_benchmark) |

**作用：** Skip the OSD benchmark on OSD initialization/boot-up This option specifies whether the OSD benchmark must be skipped during the OSD boot-up sequence. Only considered for osd_op_queue = mclock_scheduler.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_mclock_skip_benchmark true
ceph config get osd osd_mclock_skip_benchmark
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
