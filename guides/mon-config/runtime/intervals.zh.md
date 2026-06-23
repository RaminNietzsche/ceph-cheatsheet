# Intervals & timeouts

MON 配置深度指南 — 17 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mon_con_tracker_persist_interval](#mon_con_tracker_persist_interval) | `10` | Advanced | Performance |
| [mon_elector_ping_timeout](#mon_elector_ping_timeout) | `2` | Advanced | Performance |
| [mon_lease_ack_timeout_factor](#mon_lease_ack_timeout_factor) | `2` | Advanced | Performance |
| [mon_lease_renew_interval_factor](#mon_lease_renew_interval_factor) | `0.6` | Advanced | Performance |
| [mon_mds_blocklist_interval](#mon_mds_blocklist_interval) | `1_day` | Dev | Dev |
| [mon_netsplit_grace_period](#mon_netsplit_grace_period) | `9` | Advanced | Performance |
| [mon_nvmeofgw_failback_delay](#mon_nvmeofgw_failback_delay) | `0` | Advanced | Performance |
| [mon_nvmeofgw_skip_failovers_interval](#mon_nvmeofgw_skip_failovers_interval) | `16` | Advanced | Performance |
| [mon_session_timeout](#mon_session_timeout) | `5_min` | Advanced | Performance |
| [mon_smart_report_timeout](#mon_smart_report_timeout) | `5` | Advanced | Performance |
| [mon_subscribe_interval](#mon_subscribe_interval) | `1_day` | Dev | Dev |
| [mon_tick_interval](#mon_tick_interval) | `5` | Advanced | Performance |
| [mon_timecheck_interval](#mon_timecheck_interval) | `5_min` | Advanced | Performance |
| [mon_timecheck_skew_interval](#mon_timecheck_skew_interval) | `30` | Advanced | Performance |
| [mon_use_min_delay_socket](#mon_use_min_delay_socket) | `False` | Advanced | Performance |
| [mon_warn_older_version_delay](#mon_warn_older_version_delay) | `7_day` | Advanced | Performance |
| [nvmeof_mon_client_tick_period](#nvmeof_mon_client_tick_period) | `1` | Advanced | Performance |

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

### mon_con_tracker_persist_interval

| | |
|---|---|
| 类型 | Uint · default `10` · **Advanced** |
| 表格 | [mon.md#SP_mon_con_tracker_persist_interval](../../../config/mon/mon.md#SP_mon_con_tracker_persist_interval) |

**作用：** how many updates the ConnectionTracker takes before it persists to disk

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_con_tracker_persist_interval 10
ceph config get mon mon_con_tracker_persist_interval
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `100000`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_con_tracker_persist_interval
ceph -s
ceph mon stat
```

---

### mon_elector_ping_timeout

| | |
|---|---|
| 类型 | Float · default `2` · **Advanced** |
| 表格 | [mon.md#SP_mon_elector_ping_timeout](../../../config/mon/mon.md#SP_mon_elector_ping_timeout) |

**作用：** The time after which a ping 'times out' and a connection is considered down

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_elector_ping_timeout 2
ceph config get mon mon_elector_ping_timeout
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_elector_ping_timeout
ceph -s
ceph mon stat
```

---

### mon_lease_ack_timeout_factor

| | |
|---|---|
| 类型 | Float · default `2` · **Advanced** |
| 表格 | [mon.md#SP_mon_lease_ack_timeout_factor](../../../config/mon/mon.md#SP_mon_lease_ack_timeout_factor) |

**作用：** multiple of mon_lease for the lease ack interval before calling new election

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_lease_ack_timeout_factor 2
ceph config get mon mon_lease_ack_timeout_factor
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1.0001`，最大 `100`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_lease_ack_timeout_factor
ceph -s
ceph mon stat
```

---

### mon_lease_renew_interval_factor

| | |
|---|---|
| 类型 | Float · default `0.6` · **Advanced** |
| 表格 | [mon.md#SP_mon_lease_renew_interval_factor](../../../config/mon/mon.md#SP_mon_lease_renew_interval_factor) |

**作用：** multiple of mon_lease for the lease renewal interval

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_lease_renew_interval_factor 0.6
ceph config get mon mon_lease_renew_interval_factor
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.6` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `0.9999999`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_lease_renew_interval_factor
ceph -s
ceph mon stat
```

---

### mon_mds_blocklist_interval

| | |
|---|---|
| 类型 | Float · default `1_day` · **Dev** |
| 表格 | [mon.md#SP_mon_mds_blocklist_interval](../../../config/mon/mon.md#SP_mon_mds_blocklist_interval) |

**作用：** Duration in seconds that blocklist entries for MDS daemons remain in the OSD map

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_mds_blocklist_interval 1_day
ceph config get mon mon_mds_blocklist_interval
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`1_day`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_netsplit_grace_period

| | |
|---|---|
| 类型 | Secs · default `9` · **Advanced** |
| 表格 | [mon.md#SP_mon_netsplit_grace_period](../../../config/mon/mon.md#SP_mon_netsplit_grace_period) |

**作用：** Time (in seconds) to wait before emitting a MON_NETSPLIT health warning.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_netsplit_grace_period 9
ceph config get mon mon_netsplit_grace_period
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `9` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_netsplit_grace_period
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_failback_delay

| | |
|---|---|
| 类型 | Secs · default `0` · **Advanced** |
| 表格 | [mon.md#SP_mon_nvmeofgw_failback_delay](../../../config/mon/mon.md#SP_mon_nvmeofgw_failback_delay) |

**作用：** Period in seconds to delay HA failback of the gateway

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_nvmeofgw_failback_delay 0
ceph config get mon mon_nvmeofgw_failback_delay
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_nvmeofgw_failback_delay
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_skip_failovers_interval

| | |
|---|---|
| 类型 | Secs · default `16` · **Advanced** |
| 表格 | [mon.md#SP_mon_nvmeofgw_skip_failovers_interval](../../../config/mon/mon.md#SP_mon_nvmeofgw_skip_failovers_interval) |

**作用：** Period in seconds in which no failovers are performed in GW's pool-group this is equal to max GW redeploy interval

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_nvmeofgw_skip_failovers_interval 16
ceph config get mon mon_nvmeofgw_skip_failovers_interval
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `16` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_nvmeofgw_skip_failovers_interval
ceph -s
ceph mon stat
```

---

### mon_session_timeout

| | |
|---|---|
| 类型 | Int · default `5_min` · **Advanced** |
| 表格 | [mon.md#SP_mon_session_timeout](../../../config/mon/mon.md#SP_mon_session_timeout) |

**作用：** close inactive mon client connections after this many seconds

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_session_timeout 5_min
ceph config get mon mon_session_timeout
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_session_timeout
ceph -s
ceph mon stat
```

---

### mon_smart_report_timeout

| | |
|---|---|
| 类型 | Uint · default `5` · **Advanced** |
| 表格 | [mon.md#SP_mon_smart_report_timeout](../../../config/mon/mon.md#SP_mon_smart_report_timeout) |

**作用：** Timeout (in seconds) for smartctl to run, default is set to 5

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_smart_report_timeout 5
ceph config get mon mon_smart_report_timeout
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_smart_report_timeout
ceph -s
ceph mon stat
```

---

### mon_subscribe_interval

| | |
|---|---|
| 类型 | Float · default `1_day` · **Dev** |
| 表格 | [mon.md#SP_mon_subscribe_interval](../../../config/mon/mon.md#SP_mon_subscribe_interval) |

**作用：** subscribe interval for pre-jewel clients

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_subscribe_interval 1_day
ceph config get mon mon_subscribe_interval
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`1_day`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_tick_interval

| | |
|---|---|
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [mon.md#SP_mon_tick_interval](../../../config/mon/mon.md#SP_mon_tick_interval) |

**作用：** interval for internal mon background checks

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_tick_interval 5
ceph config get mon mon_tick_interval
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_tick_interval
ceph -s
ceph mon stat
```

---

### mon_timecheck_interval

| | |
|---|---|
| 类型 | Float · default `5_min` · **Advanced** |
| 表格 | [mon.md#SP_mon_timecheck_interval](../../../config/mon/mon.md#SP_mon_timecheck_interval) |

**作用：** frequency of clock synchronization checks between monitors (seconds)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_timecheck_interval 5_min
ceph config get mon mon_timecheck_interval
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_timecheck_interval
ceph -s
ceph mon stat
```

---

### mon_timecheck_skew_interval

| | |
|---|---|
| 类型 | Float · default `30` · **Advanced** |
| 表格 | [mon.md#SP_mon_timecheck_skew_interval](../../../config/mon/mon.md#SP_mon_timecheck_skew_interval) |

**作用：** frequency of clock synchronization (re)checks between monitors while clocks are believed to be skewed (seconds)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_timecheck_skew_interval 30
ceph config get mon mon_timecheck_skew_interval
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_timecheck_skew_interval
ceph -s
ceph mon stat
```

---

### mon_use_min_delay_socket

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [mon.md#SP_mon_use_min_delay_socket](../../../config/mon/mon.md#SP_mon_use_min_delay_socket) |

**作用：** priority packets between mons

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mon mon_use_min_delay_socket true
ceph config get mon mon_use_min_delay_socket
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_use_min_delay_socket
ceph -s
ceph mon stat
```

---

### mon_warn_older_version_delay

| | |
|---|---|
| 类型 | Secs · default `7_day` · **Advanced** |
| 表格 | [mon.md#SP_mon_warn_older_version_delay](../../../config/mon/mon.md#SP_mon_warn_older_version_delay) |

**作用：** issue DAEMON_OLD_VERSION health warning after this amount of time has elapsed

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_warn_older_version_delay 7_day
ceph config get mon mon_warn_older_version_delay
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `7_day` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_warn_older_version_delay
ceph -s
ceph mon stat
```

---

### nvmeof_mon_client_tick_period

| | |
|---|---|
| 类型 | Secs · default `1` · **Advanced** |
| 表格 | [mon.md#SP_nvmeof_mon_client_tick_period](../../../config/mon/mon.md#SP_nvmeof_mon_client_tick_period) |

**作用：** Period in seconds of nvmeof gateway beacon messages to monitor

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon nvmeof_mon_client_tick_period 1
ceph config get mon nvmeof_mon_client_tick_period
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon nvmeof_mon_client_tick_period
ceph -s
ceph mon stat
```

---


[← 概览](../OVERVIEW.md)
