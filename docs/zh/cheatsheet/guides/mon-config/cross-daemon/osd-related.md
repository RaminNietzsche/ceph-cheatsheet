# OSD-related settings

MON 配置深度指南 — 28 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mon_osd_adjust_down_out_interval](#mon_osd_adjust_down_out_interval) | `True` | Advanced | 性能 |
| [mon_osd_adjust_heartbeat_grace](#mon_osd_adjust_heartbeat_grace) | `True` | Advanced | 性能 |
| [mon_osd_auto_mark_auto_out_in](#mon_osd_auto_mark_auto_out_in) | `True` | Advanced | 性能 |
| [mon_osd_auto_mark_in](#mon_osd_auto_mark_in) | `False` | Advanced | 性能 |
| [mon_osd_auto_mark_new_in](#mon_osd_auto_mark_new_in) | `True` | Advanced | 性能 |
| [mon_osd_blocklist_default_expire](#mon_osd_blocklist_default_expire) | `1_hr` | Advanced | 性能 |
| [mon_osd_cache_size](#mon_osd_cache_size) | `500` | Advanced | 性能 |
| [mon_osd_cache_size_min](#mon_osd_cache_size_min) | `128_M` | Advanced | 性能 |
| [mon_osd_crush_smoke_test](#mon_osd_crush_smoke_test) | `True` | Advanced | 性能 |
| [mon_osd_destroyed_out_interval](#mon_osd_destroyed_out_interval) | `10_min` | Advanced | 性能 |
| [mon_osd_down_out_interval](#mon_osd_down_out_interval) | `10_min` | Advanced | 性能 |
| [mon_osd_down_out_subtree_limit](#mon_osd_down_out_subtree_limit) | `rack` | Advanced | 性能 |
| [mon_osd_laggy_halflife](#mon_osd_laggy_halflife) | `1_hr` | Advanced | 性能 |
| [mon_osd_laggy_max_interval](#mon_osd_laggy_max_interval) | `5_min` | Advanced | 性能 |
| [mon_osd_laggy_weight](#mon_osd_laggy_weight) | `0.3` | Advanced | 性能 |
| [mon_osd_mapping_pgs_per_chunk](#mon_osd_mapping_pgs_per_chunk) | `4096` | Dev | 开发 |
| [mon_osd_max_initial_pgs](#mon_osd_max_initial_pgs) | `1024` | Advanced | 性能 |
| [mon_osd_min_in_ratio](#mon_osd_min_in_ratio) | `0.75` | Advanced | 性能 |
| [mon_osd_min_up_ratio](#mon_osd_min_up_ratio) | `0.3` | Advanced | 性能 |
| [mon_osd_warn_num_repaired](#mon_osd_warn_num_repaired) | `10` | Advanced | 性能 |
| [mon_osd_warn_op_age](#mon_osd_warn_op_age) | `32` | Advanced | 性能 |
| [mon_osdmap_full_prune_enabled](#mon_osdmap_full_prune_enabled) | `True` | Advanced | 策略 |
| [mon_osdmap_full_prune_interval](#mon_osdmap_full_prune_interval) | `10` | Advanced | 性能 |
| [mon_osdmap_full_prune_min](#mon_osdmap_full_prune_min) | `10000` | Advanced | 性能 |
| [mon_osdmap_full_prune_txsize](#mon_osdmap_full_prune_txsize) | `100` | Advanced | 性能 |
| [mon_warn_on_filestore_osds](#mon_warn_on_filestore_osds) | `True` | Dev | 开发 |
| [mon_warn_on_osd_down_out_interval_zero](#mon_warn_on_osd_down_out_interval_zero) | `True` | Advanced | 性能 |
| [osd_crush_update_weight_set](#osd_crush_update_weight_set) | `True` | Advanced | 性能 |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_osd_adjust_down_out_interval

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_adjust_down_out_interval](../../../config/mon/mon.md#SP_mon_osd_adjust_down_out_interval) |

**作用：** increase the mon_osd_down_out_interval if an OSD appears to be laggy

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**相关选项：**

- [`mon_osd_adjust_heartbeat_grace`](../../../config/mon/mon.md#SP_mon_osd_adjust_heartbeat_grace)

**示例：**

```bash
ceph config set mon mon_osd_adjust_down_out_interval false
ceph config get mon mon_osd_adjust_down_out_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_adjust_down_out_interval
ceph -s
ceph mon stat
```

---

### mon_osd_adjust_heartbeat_grace

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_adjust_heartbeat_grace](../../../config/mon/mon.md#SP_mon_osd_adjust_heartbeat_grace) |

**作用：** increase OSD heartbeat grace if peers appear to be laggy If an OSD is marked down but then marks itself back up, it implies it wasn't actually down but was unable to respond to heartbeats. If this option is true, we can use the laggy_probability and laggy_interval values calculated to model this situation to increase the heartbeat grace period for this OSD so that it isn't marked down again. laggy_probability is an estimated probability that the given OSD is down because it is laggy (not actually down), and laggy_interval is an estiate on how long it stays down when it is laggy.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_osd_adjust_heartbeat_grace false
ceph config get mon mon_osd_adjust_heartbeat_grace
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_adjust_heartbeat_grace
ceph -s
ceph mon stat
```

---

### mon_osd_auto_mark_auto_out_in

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_auto_mark_auto_out_in](../../../config/mon/mon.md#SP_mon_osd_auto_mark_auto_out_in) |

**作用：** mark any OSD that comes up that was automatically marked 'out' back 'in'

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**相关选项：**

- [`mon_osd_down_out_interval`](../../../config/mon/mon.md#SP_mon_osd_down_out_interval)

**示例：**

```bash
ceph config set mon mon_osd_auto_mark_auto_out_in false
ceph config get mon mon_osd_auto_mark_auto_out_in
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_auto_mark_auto_out_in
ceph -s
ceph mon stat
```

---

### mon_osd_auto_mark_in

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_auto_mark_in](../../../config/mon/mon.md#SP_mon_osd_auto_mark_in) |

**作用：** mark any OSD that comes up 'in'

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mon mon_osd_auto_mark_in true
ceph config get mon mon_osd_auto_mark_in
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_auto_mark_in
ceph -s
ceph mon stat
```

---

### mon_osd_auto_mark_new_in

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_auto_mark_new_in](../../../config/mon/mon.md#SP_mon_osd_auto_mark_new_in) |

**作用：** mark any new OSD that comes up 'in'

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_osd_auto_mark_new_in false
ceph config get mon mon_osd_auto_mark_new_in
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_auto_mark_new_in
ceph -s
ceph mon stat
```

---

### mon_osd_blocklist_default_expire

| | |
|---|---|
| 类型 | Float · default `1_hr` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_blocklist_default_expire](../../../config/mon/mon.md#SP_mon_osd_blocklist_default_expire) |

**作用：** Duration in seconds that blocklist entries for clients remain in the OSD map

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_osd_blocklist_default_expire 1_hr
ceph config get mon mon_osd_blocklist_default_expire
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_hr` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_blocklist_default_expire
ceph -s
ceph mon stat
```

---

### mon_osd_cache_size

| | |
|---|---|
| 类型 | Int · default `500` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_cache_size](../../../config/mon/mon.md#SP_mon_osd_cache_size) |

**作用：** maximum number of OSDMaps to cache in memory

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_osd_cache_size 500
ceph config get mon mon_osd_cache_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `500` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_cache_size
ceph -s
ceph mon stat
```

---

### mon_osd_cache_size_min

| | |
|---|---|
| 类型 | Size · default `128_M` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_cache_size_min](../../../config/mon/mon.md#SP_mon_osd_cache_size_min) |

**作用：** The minimum amount of bytes to be kept mapped in memory for osd monitor caches.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_osd_cache_size_min 128_M
ceph config get mon mon_osd_cache_size_min
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `128_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_cache_size_min
ceph -s
ceph mon stat
```

---

### mon_osd_crush_smoke_test

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_crush_smoke_test](../../../config/mon/mon.md#SP_mon_osd_crush_smoke_test) |

**作用：** perform a smoke test on any new CRUSH map before accepting changes

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_osd_crush_smoke_test false
ceph config get mon mon_osd_crush_smoke_test
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_crush_smoke_test
ceph -s
ceph mon stat
```

---

### mon_osd_destroyed_out_interval

| | |
|---|---|
| 类型 | Int · default `10_min` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_destroyed_out_interval](../../../config/mon/mon.md#SP_mon_osd_destroyed_out_interval) |

**作用：** mark any OSD 'out' that has been 'destroy'ed for this long (seconds)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_osd_destroyed_out_interval 10_min
ceph config get mon mon_osd_destroyed_out_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_destroyed_out_interval
ceph -s
ceph mon stat
```

---

### mon_osd_down_out_interval

| | |
|---|---|
| 类型 | Int · default `10_min` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_down_out_interval](../../../config/mon/mon.md#SP_mon_osd_down_out_interval) |

**作用：** Seconds an OSD can stay `down` before the monitor marks it `out` and CRUSH begins rebalancing.

**何时使用：** Increase for flaky networks or long maintenance (avoid premature rebalance). Decrease when you want faster failover — at the cost of more data movement.

**示例：**

```bash
ceph config set mon mon_osd_down_out_interval 10_min
ceph config get mon mon_osd_down_out_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_down_out_interval
ceph -s
ceph mon stat
```

Common production range: 600–3600 s. Coordinate with `mon_osd_min_down_reporters`.

---

### mon_osd_down_out_subtree_limit

| | |
|---|---|
| 类型 | Str · default `rack` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_down_out_subtree_limit](../../../config/mon/mon.md#SP_mon_osd_down_out_subtree_limit) |

**作用：** do not automatically mark OSDs 'out' if an entire subtree of this size is down

**何时使用：** 触及资源限制或保护集群容量时调整。

**相关选项：**

- [`mon_osd_down_out_interval`](../../../config/mon/mon.md#SP_mon_osd_down_out_interval)

**示例：**

```bash
ceph config set mon mon_osd_down_out_subtree_limit rack
ceph config get mon mon_osd_down_out_subtree_limit
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `rack` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_down_out_subtree_limit
ceph -s
ceph mon stat
```

---

### mon_osd_laggy_halflife

| | |
|---|---|
| 类型 | Int · default `1_hr` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_laggy_halflife](../../../config/mon/mon.md#SP_mon_osd_laggy_halflife) |

**作用：** halflife of OSD 'lagginess' factor

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_osd_laggy_halflife 1_hr
ceph config get mon mon_osd_laggy_halflife
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_hr` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_laggy_halflife
ceph -s
ceph mon stat
```

---

### mon_osd_laggy_max_interval

| | |
|---|---|
| 类型 | Int · default `5_min` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_laggy_max_interval](../../../config/mon/mon.md#SP_mon_osd_laggy_max_interval) |

**作用：** cap value for period for OSD to be marked for laggy_interval calculation

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_osd_laggy_max_interval 5_min
ceph config get mon mon_osd_laggy_max_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_laggy_max_interval
ceph -s
ceph mon stat
```

---

### mon_osd_laggy_weight

| | |
|---|---|
| 类型 | Float · default `0.3` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_laggy_weight](../../../config/mon/mon.md#SP_mon_osd_laggy_weight) |

**作用：** how heavily to weight OSD marking itself back up in overall laggy_probability 1.0 means that an OSD marking itself back up (because it was marked down but not actually dead) means a 100% laggy_probability; 0.0 effectively disables tracking of laggy_probability.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_osd_laggy_weight 0.3
ceph config get mon mon_osd_laggy_weight
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `1`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_laggy_weight
ceph -s
ceph mon stat
```

---

### mon_osd_mapping_pgs_per_chunk

| | |
|---|---|
| 类型 | Int · default `4096` · **Dev** |
| 表格 | [mon.md#SP_mon_osd_mapping_pgs_per_chunk](../../../config/mon/mon.md#SP_mon_osd_mapping_pgs_per_chunk) |

**作用：** granularity of PG placement calculation background work

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_osd_mapping_pgs_per_chunk 4096
ceph config get mon mon_osd_mapping_pgs_per_chunk
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`4096`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_osd_max_initial_pgs

| | |
|---|---|
| 类型 | Int · default `1024` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_max_initial_pgs](../../../config/mon/mon.md#SP_mon_osd_max_initial_pgs) |

**作用：** maximum number of PGs a pool will created with If the user specifies more PGs than this, the cluster will subsequently split PGs after the pool is created in order to reach the target.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_osd_max_initial_pgs 1024
ceph config get mon mon_osd_max_initial_pgs
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1024` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_max_initial_pgs
ceph -s
ceph mon stat
```

---

### mon_osd_min_in_ratio

| | |
|---|---|
| 类型 | Float · default `0.75` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_min_in_ratio](../../../config/mon/mon.md#SP_mon_osd_min_in_ratio) |

**作用：** do not automatically mark OSDs 'out' if fewer than this many OSDs are 'in'

**何时使用：** 触及资源限制或保护集群容量时调整。

**相关选项：**

- [`mon_osd_down_out_interval`](../../../config/mon/mon.md#SP_mon_osd_down_out_interval)

**示例：**

```bash
ceph config set mon mon_osd_min_in_ratio 0.75
ceph config get mon mon_osd_min_in_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.75` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_min_in_ratio
ceph -s
ceph mon stat
```

---

### mon_osd_min_up_ratio

| | |
|---|---|
| 类型 | Float · default `0.3` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_min_up_ratio](../../../config/mon/mon.md#SP_mon_osd_min_up_ratio) |

**作用：** do not automatically mark OSDs 'out' if fewer than this many OSDs are 'up'

**何时使用：** 触及资源限制或保护集群容量时调整。

**相关选项：**

- [`mon_osd_down_out_interval`](../../../config/mon/mon.md#SP_mon_osd_down_out_interval)

**示例：**

```bash
ceph config set mon mon_osd_min_up_ratio 0.3
ceph config get mon mon_osd_min_up_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_min_up_ratio
ceph -s
ceph mon stat
```

---

### mon_osd_warn_num_repaired

| | |
|---|---|
| 类型 | Uint · default `10` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_warn_num_repaired](../../../config/mon/mon.md#SP_mon_osd_warn_num_repaired) |

**作用：** issue OSD_TOO_MANY_REPAIRS health warning if an OSD has more than this many read repairs

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_osd_warn_num_repaired 10
ceph config get mon mon_osd_warn_num_repaired
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_warn_num_repaired
ceph -s
ceph mon stat
```

---

### mon_osd_warn_op_age

| | |
|---|---|
| 类型 | Float · default `32` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_warn_op_age](../../../config/mon/mon.md#SP_mon_osd_warn_op_age) |

**作用：** issue REQUEST_SLOW health warning if OSD ops are slower than this age (seconds)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_osd_warn_op_age 32
ceph config get mon mon_osd_warn_op_age
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `32` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_warn_op_age
ceph -s
ceph mon stat
```

---

### mon_osdmap_full_prune_enabled

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_osdmap_full_prune_enabled](../../../config/mon/mon.md#SP_mon_osdmap_full_prune_enabled) |

**作用：** enables pruning full osdmap versions when we go over a given number of maps

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_osdmap_full_prune_enabled false
ceph config get mon mon_osdmap_full_prune_enabled
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osdmap_full_prune_enabled
ceph -s
ceph mon stat
```

---

### mon_osdmap_full_prune_interval

| | |
|---|---|
| 类型 | Uint · default `10` · **Advanced** |
| 表格 | [mon.md#SP_mon_osdmap_full_prune_interval](../../../config/mon/mon.md#SP_mon_osdmap_full_prune_interval) |

**作用：** interval between maps that will not be pruned; maps in the middle will be pruned.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_osdmap_full_prune_interval 10
ceph config get mon mon_osdmap_full_prune_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osdmap_full_prune_interval
ceph -s
ceph mon stat
```

---

### mon_osdmap_full_prune_min

| | |
|---|---|
| 类型 | Uint · default `10000` · **Advanced** |
| 表格 | [mon.md#SP_mon_osdmap_full_prune_min](../../../config/mon/mon.md#SP_mon_osdmap_full_prune_min) |

**作用：** minimum number of versions in the store to trigger full map pruning

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_osdmap_full_prune_min 10000
ceph config get mon mon_osdmap_full_prune_min
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osdmap_full_prune_min
ceph -s
ceph mon stat
```

---

### mon_osdmap_full_prune_txsize

| | |
|---|---|
| 类型 | Uint · default `100` · **Advanced** |
| 表格 | [mon.md#SP_mon_osdmap_full_prune_txsize](../../../config/mon/mon.md#SP_mon_osdmap_full_prune_txsize) |

**作用：** number of maps we will prune per iteration

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_osdmap_full_prune_txsize 100
ceph config get mon mon_osdmap_full_prune_txsize
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `100` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osdmap_full_prune_txsize
ceph -s
ceph mon stat
```

---

### mon_warn_on_filestore_osds

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [mon.md#SP_mon_warn_on_filestore_osds](../../../config/mon/mon.md#SP_mon_warn_on_filestore_osds) |

**作用：** log health warn for filestore OSDs

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_warn_on_filestore_osds false
ceph config get mon mon_warn_on_filestore_osds
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_warn_on_osd_down_out_interval_zero

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_warn_on_osd_down_out_interval_zero](../../../config/mon/mon.md#SP_mon_warn_on_osd_down_out_interval_zero) |

**作用：** issue OSD_NO_DOWN_OUT_INTERVAL health warning if mon_osd_down_out_interval is zero Having mon_osd_down_out_interval set to 0 means that down OSDs are not marked out automatically and the cluster does not heal itself without administrator intervention.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**相关选项：**

- [`mon_osd_down_out_interval`](../../../config/mon/mon.md#SP_mon_osd_down_out_interval)

**示例：**

```bash
ceph config set mon mon_warn_on_osd_down_out_interval_zero false
ceph config get mon mon_warn_on_osd_down_out_interval_zero
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_warn_on_osd_down_out_interval_zero
ceph -s
ceph mon stat
```

---

### osd_crush_update_weight_set

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_crush_update_weight_set](../../../config/mon/osd.md#SP_osd_crush_update_weight_set) |

**作用：** update CRUSH weight-set weights when updating weights If this setting is true, we will update the weight-set weights when adjusting an item's weight, effectively making changes take effect immediately, and discarding any previous optimization in the weight-set value. Setting this value to false will leave it to the balancer to (slowly, presumably) adjust weights to approach the new target value.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_crush_update_weight_set false
ceph config get osd osd_crush_update_weight_set
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_crush_update_weight_set
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← 概览](../OVERVIEW.md)
