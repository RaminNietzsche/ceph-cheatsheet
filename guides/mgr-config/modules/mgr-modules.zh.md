# Manager & cephadm modules

MGR 配置深度指南 — 31 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mgr/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [cephadm_path](#cephadm_path) | `/usr/sbin/cephadm` | Advanced | Capacity |
| [mgr_client_bytes](#mgr_client_bytes) | `128_M` | Dev | Dev |
| [mgr_client_messages](#mgr_client_messages) | `512` | Dev | Dev |
| [mgr_data](#mgr_data) | `/var/lib/ceph/mgr/$cluster-$id` | Advanced | Performance |
| [mgr_debug_aggressive_pg_num_changes](#mgr_debug_aggressive_pg_num_changes) | `False` | Dev | Dev |
| [mgr_disabled_modules](#mgr_disabled_modules) | `0` | Advanced | Performance |
| [mgr_initial_modules](#mgr_initial_modules) | `iostat nfs nvmeof` | Basic | Policy |
| [mgr_max_pg_creating](#mgr_max_pg_creating) | `1024` | Advanced | Performance |
| [mgr_max_pg_num_change](#mgr_max_pg_num_change) | `128` | Advanced | Performance |
| [mgr_mds_bytes](#mgr_mds_bytes) | `128_M` | Dev | Dev |
| [mgr_mds_messages](#mgr_mds_messages) | `128` | Dev | Dev |
| [mgr_module_load_delay](#mgr_module_load_delay) | `0` | Dev | Dev |
| [mgr_module_load_delay_name](#mgr_module_load_delay_name) | `(empty)` | Dev | Dev |
| [mgr_module_load_expiration](#mgr_module_load_expiration) | `20000` | Dev | Dev |
| [mgr_module_monitor_interval](#mgr_module_monitor_interval) | `5` | Advanced | Performance |
| [mgr_module_path](#mgr_module_path) | `0/mgr` | Advanced | Capacity |
| [mgr_mon_bytes](#mgr_mon_bytes) | `128_M` | Dev | Dev |
| [mgr_mon_messages](#mgr_mon_messages) | `128` | Dev | Dev |
| [mgr_osd_bytes](#mgr_osd_bytes) | `512_M` | Dev | Dev |
| [mgr_osd_messages](#mgr_osd_messages) | `8_K` | Dev | Dev |
| [mgr_osd_upgrade_check_convergence_factor](#mgr_osd_upgrade_check_convergence_factor) | `0.8` | Advanced | Performance |
| [mgr_pool](#mgr_pool) | `True` | Dev | Dev |
| [mgr_service_beacon_grace](#mgr_service_beacon_grace) | `1_min` | Advanced | Performance |
| [mgr_standby_modules](#mgr_standby_modules) | `True` | Advanced | Performance |
| [mgr_stats_period](#mgr_stats_period) | `5` | Basic | Policy |
| [mgr_stats_period_autotune](#mgr_stats_period_autotune) | `True` | Basic | Policy |
| [mgr_stats_period_autotune_queue_threshold](#mgr_stats_period_autotune_queue_threshold) | `100` | Advanced | Performance |
| [mgr_stats_threshold](#mgr_stats_threshold) | `5` | Advanced | Performance |
| [mgr_subinterpreter_modules](#mgr_subinterpreter_modules) | `0` | Advanced | Performance |
| [mgr_test_metadata_error](#mgr_test_metadata_error) | `False` | Dev | Dev |
| [mgr_tick_period](#mgr_tick_period) | `2` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. mgr
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### cephadm_path

| | |
|---|---|
| 类型 | Str · default `/usr/sbin/cephadm` · **Advanced** |
| 表格 | [cephadm.md#SP_cephadm_path](../../../config/mgr/cephadm.md#SP_cephadm_path) |

**作用：** Path to the `cephadm` binary used by the cephadm orchestrator module.

**何时使用：** Set when cephadm is not in `$PATH` for the mgr daemon user (common with custom installs).

**示例：**

```bash
ceph config set mgr cephadm_path "/usr/sbin/cephadm"
ceph config get mgr cephadm_path
```

**寻找最优值：**

**调优模型：** Capacity

1. 以 `/usr/sbin/cephadm` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr cephadm_path
ceph -s
ceph mgr stat
```

---

### mgr_client_bytes

| | |
|---|---|
| 类型 | Size · default `128_M` · **Dev** |
| 表格 | [mgr.md#SP_mgr_client_bytes](../../../config/mgr/mgr.md#SP_mgr_client_bytes) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mgr mgr_client_bytes 128_M
ceph config get mgr mgr_client_bytes
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`128_M`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mgr_client_messages

| | |
|---|---|
| 类型 | Uint · default `512` · **Dev** |
| 表格 | [mgr.md#SP_mgr_client_messages](../../../config/mgr/mgr.md#SP_mgr_client_messages) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mgr mgr_client_messages 512
ceph config get mgr mgr_client_messages
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`512`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mgr_data

| | |
|---|---|
| 类型 | Str · default `/var/lib/ceph/mgr/$cluster-$id` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_data](../../../config/mgr/mgr.md#SP_mgr_data) |

**作用：** Filesystem path to the Manager's data directory, which contains keyrings and other data

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mgr mgr_data "/var/lib/ceph/mgr/$cluster-$id"
ceph config get mgr mgr_data
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `/var/lib/ceph/mgr/$cluster-$id` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_data
ceph -s
ceph mgr stat
```

---

### mgr_debug_aggressive_pg_num_changes

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mgr.md#SP_mgr_debug_aggressive_pg_num_changes](../../../config/mgr/mgr.md#SP_mgr_debug_aggressive_pg_num_changes) |

**作用：** Bypass most throttling and safety checks in pg&#91;p&#93;_num controller

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mgr mgr_debug_aggressive_pg_num_changes true
ceph config get mgr mgr_debug_aggressive_pg_num_changes
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mgr_disabled_modules

| | |
|---|---|
| 类型 | Str · default `0` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [mgr.md#SP_mgr_disabled_modules](../../../config/mgr/mgr.md#SP_mgr_disabled_modules) |

**作用：** Comma-separated list of manager modules that must not be loaded.

**何时使用：** Disable unused modules to reduce attack surface and MGR startup time.

**示例：**

```bash
ceph config set mgr mgr_disabled_modules "example"
ceph config get mgr mgr_disabled_modules
ceph orch restart mgr
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_disabled_modules
ceph -s
ceph mgr stat
```

---

### mgr_initial_modules

| | |
|---|---|
| 类型 | Str · default `iostat nfs nvmeof` · **Basic** |
| 表格 | [mgr.md#SP_mgr_initial_modules](../../../config/mgr/mgr.md#SP_mgr_initial_modules) |

**作用：** List of manager modules to enable when the cluster is first started

**何时使用：** 核心 MGR 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set mgr mgr_initial_modules "iostat nfs nvmeof"
ceph config get mgr mgr_initial_modules
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `iostat nfs nvmeof` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_initial_modules
ceph -s
ceph mgr stat
```

---

### mgr_max_pg_creating

| | |
|---|---|
| 类型 | Uint · default `1024` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_max_pg_creating](../../../config/mgr/mgr.md#SP_mgr_max_pg_creating) |

**作用：** bound on max creating pgs when acting to create more pgs

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mgr mgr_max_pg_creating 1024
ceph config get mgr mgr_max_pg_creating
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1024` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_max_pg_creating
ceph -s
ceph mgr stat
```

---

### mgr_max_pg_num_change

| | |
|---|---|
| 类型 | Int · default `128` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_max_pg_num_change](../../../config/mgr/mgr.md#SP_mgr_max_pg_num_change) |

**作用：** Maximum PG count change the MGR balancer/autoscaler applies per iteration.

**何时使用：** Lower on busy clusters to avoid large placement churn; raise for faster PG convergence after expansion.

**示例：**

```bash
ceph config set mgr mgr_max_pg_num_change 128
ceph config get mgr mgr_max_pg_num_change
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `128` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_max_pg_num_change
ceph -s
ceph mgr stat
```

---

### mgr_mds_bytes

| | |
|---|---|
| 类型 | Size · default `128_M` · **Dev** |
| 表格 | [mgr.md#SP_mgr_mds_bytes](../../../config/mgr/mgr.md#SP_mgr_mds_bytes) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mgr mgr_mds_bytes 128_M
ceph config get mgr mgr_mds_bytes
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`128_M`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mgr_mds_messages

| | |
|---|---|
| 类型 | Uint · default `128` · **Dev** |
| 表格 | [mgr.md#SP_mgr_mds_messages](../../../config/mgr/mgr.md#SP_mgr_mds_messages) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mgr mgr_mds_messages 128
ceph config get mgr mgr_mds_messages
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`128`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mgr_module_load_delay

| | |
|---|---|
| 类型 | Millisecs · default `0` · **Dev** |
| 表格 | [mgr.md#SP_mgr_module_load_delay](../../../config/mgr/mgr.md#SP_mgr_module_load_delay) |

**作用：** Number of milliseconds for Manager modules to delay loading. For testing purposes only.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mgr mgr_module_load_delay 0
ceph config get mgr mgr_module_load_delay
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mgr_module_load_delay_name

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Dev** |
| 表格 | [mgr.md#SP_mgr_module_load_delay_name](../../../config/mgr/mgr.md#SP_mgr_module_load_delay_name) |

**作用：** Specify which Manager module is to delay loading by mgr_module_load_delay milliseconds. For testing purposes only.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mgr mgr_module_load_delay_name "example"
ceph config get mgr mgr_module_load_delay_name
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`(empty)`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mgr_module_load_expiration

| | |
|---|---|
| 类型 | Millisecs · default `20000` · **Dev** |
| 表格 | [mgr.md#SP_mgr_module_load_expiration](../../../config/mgr/mgr.md#SP_mgr_module_load_expiration) |

**作用：** Maximum number of milliseconds the active mgr is allowed to load the mgr modules before declaring availability.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mgr mgr_module_load_expiration 20000
ceph config get mgr mgr_module_load_expiration
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`20000`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mgr_module_monitor_interval

| | |
|---|---|
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_module_monitor_interval](../../../config/mgr/mgr.md#SP_mgr_module_monitor_interval) |

**作用：** Period in seconds for collecting Manager modules cpu and memory performance counters.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mgr mgr_module_monitor_interval 5
ceph config get mgr mgr_module_monitor_interval
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_module_monitor_interval
ceph -s
ceph mgr stat
```

---

### mgr_module_path

| | |
|---|---|
| 类型 | Str · default `0/mgr` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_module_path](../../../config/mgr/mgr.md#SP_mgr_module_path) |

**作用：** Directory where Ceph manager modules are loaded from.

**何时使用：** Change only for custom module paths or non-packaged installs.

**示例：**

```bash
ceph config set mgr mgr_module_path "0/mgr"
ceph config get mgr mgr_module_path
```

**寻找最优值：**

**调优模型：** Capacity

1. 以 `0/mgr` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_module_path
ceph -s
ceph mgr stat
```

---

### mgr_mon_bytes

| | |
|---|---|
| 类型 | Size · default `128_M` · **Dev** |
| 表格 | [mgr.md#SP_mgr_mon_bytes](../../../config/mgr/mgr.md#SP_mgr_mon_bytes) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mgr mgr_mon_bytes 128_M
ceph config get mgr mgr_mon_bytes
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`128_M`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mgr_mon_messages

| | |
|---|---|
| 类型 | Uint · default `128` · **Dev** |
| 表格 | [mgr.md#SP_mgr_mon_messages](../../../config/mgr/mgr.md#SP_mgr_mon_messages) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mgr mgr_mon_messages 128
ceph config get mgr mgr_mon_messages
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`128`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mgr_osd_bytes

| | |
|---|---|
| 类型 | Size · default `512_M` · **Dev** |
| 表格 | [mgr.md#SP_mgr_osd_bytes](../../../config/mgr/mgr.md#SP_mgr_osd_bytes) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mgr mgr_osd_bytes 512_M
ceph config get mgr mgr_osd_bytes
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`512_M`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mgr_osd_messages

| | |
|---|---|
| 类型 | Uint · default `8_K` · **Dev** |
| 表格 | [mgr.md#SP_mgr_osd_messages](../../../config/mgr/mgr.md#SP_mgr_osd_messages) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mgr mgr_osd_messages 8_K
ceph config get mgr mgr_osd_messages
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`8_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mgr_osd_upgrade_check_convergence_factor

| | |
|---|---|
| 类型 | Float · default `0.8` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_osd_upgrade_check_convergence_factor](../../../config/mgr/mgr.md#SP_mgr_osd_upgrade_check_convergence_factor) |

**作用：** The factor used to converge to a subset of OSDs within a CRUSH bucket that can be upgraded without affecting immediate data availability.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mgr mgr_osd_upgrade_check_convergence_factor 0.8
ceph config get mgr mgr_osd_upgrade_check_convergence_factor
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.8` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0.1`，最大 `0.9`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_osd_upgrade_check_convergence_factor
ceph -s
ceph mgr stat
```

---

### mgr_pool

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** · **STARTUP**（需重启） |
| 表格 | [mgr.md#SP_mgr_pool](../../../config/mgr/mgr.md#SP_mgr_pool) |

**作用：** Allow use/creation of .mgr pool.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mgr mgr_pool false
ceph config get mgr mgr_pool
ceph orch restart mgr
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mgr_service_beacon_grace

| | |
|---|---|
| 类型 | Float · default `1_min` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_service_beacon_grace](../../../config/mgr/mgr.md#SP_mgr_service_beacon_grace) |

**作用：** Period in seconds from last beacon to manager dropping state about a monitored service (RGW, rbd-mirror etc)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mgr mgr_service_beacon_grace 1_min
ceph config get mgr mgr_service_beacon_grace
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_service_beacon_grace
ceph -s
ceph mgr stat
```

---

### mgr_standby_modules

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_standby_modules](../../../config/mgr/mgr.md#SP_mgr_standby_modules) |

**作用：** When `true`, standby MGR daemons serve the dashboard/API via HTTP redirect to the active manager.

**何时使用：** Disable (`false`) when a load balancer fronts MGR endpoints — redirects often break behind LB private IPs.

**示例：**

```bash
ceph config set mgr mgr_standby_modules false
ceph config get mgr mgr_standby_modules
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_standby_modules
ceph -s
ceph mgr stat
```

---

### mgr_stats_period

| | |
|---|---|
| 类型 | Int · default `5` · **Basic** |
| 表格 | [mgr.md#SP_mgr_stats_period](../../../config/mgr/mgr.md#SP_mgr_stats_period) |

**作用：** Interval (seconds) between MGR cluster stat refreshes.

**何时使用：** Shorten for fresher dashboard metrics; lengthen on very large clusters to reduce MGR CPU load.

**示例：**

```bash
ceph config set mgr mgr_stats_period 5
ceph config get mgr mgr_stats_period
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `5` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_stats_period
ceph -s
ceph mgr stat
```

---

### mgr_stats_period_autotune

| | |
|---|---|
| 类型 | Bool · default `True` · **Basic** |
| 表格 | [mgr.md#SP_mgr_stats_period_autotune](../../../config/mgr/mgr.md#SP_mgr_stats_period_autotune) |

**作用：** Automatically adjust mgr_stats_period based on Manager message queue depth

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mgr mgr_stats_period_autotune false
ceph config get mgr mgr_stats_period_autotune
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_stats_period_autotune
ceph -s
ceph mgr stat
```

---

### mgr_stats_period_autotune_queue_threshold

| | |
|---|---|
| 类型 | Int · default `100` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_stats_period_autotune_queue_threshold](../../../config/mgr/mgr.md#SP_mgr_stats_period_autotune_queue_threshold) |

**作用：** Message queue depth that triggers automatic increase of mgr_stats_period

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mgr mgr_stats_period_autotune_queue_threshold 100
ceph config get mgr mgr_stats_period_autotune_queue_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `100` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_stats_period_autotune_queue_threshold
ceph -s
ceph mgr stat
```

---

### mgr_stats_threshold

| | |
|---|---|
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_stats_threshold](../../../config/mgr/mgr.md#SP_mgr_stats_threshold) |

**作用：** Lowest perfcounter priority collected by mgr

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mgr mgr_stats_threshold 5
ceph config get mgr mgr_stats_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `11`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_stats_threshold
ceph -s
ceph mgr stat
```

---

### mgr_subinterpreter_modules

| | |
|---|---|
| 类型 | Str · default `0` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [mgr.md#SP_mgr_subinterpreter_modules](../../../config/mgr/mgr.md#SP_mgr_subinterpreter_modules) |

**作用：** List of manager modules to load in independent subinterpreters

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mgr mgr_subinterpreter_modules "example"
ceph config get mgr mgr_subinterpreter_modules
ceph orch restart mgr
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_subinterpreter_modules
ceph -s
ceph mgr stat
```

---

### mgr_test_metadata_error

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mgr.md#SP_mgr_test_metadata_error](../../../config/mgr/mgr.md#SP_mgr_test_metadata_error) |

**作用：** Used for simulating errors during operations involving metadata.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mgr mgr_test_metadata_error true
ceph config get mgr mgr_test_metadata_error
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mgr_tick_period

| | |
|---|---|
| 类型 | Secs · default `2` · **Advanced** |
| 表格 | [mgr.md#SP_mgr_tick_period](../../../config/mgr/mgr.md#SP_mgr_tick_period) |

**作用：** Period in seconds of beacon messages to monitor

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mgr mgr_tick_period 2
ceph config get mgr mgr_tick_period
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr mgr_tick_period
ceph -s
ceph mgr stat
```

---


[← 概览](../OVERVIEW.md)
