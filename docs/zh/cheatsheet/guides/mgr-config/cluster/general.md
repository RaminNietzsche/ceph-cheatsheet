# General manager

MGR 配置深度指南 — 8 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mgr/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mon_cache_target_full_warn_ratio](#mon_cache_target_full_warn_ratio) | `0.66` | Advanced | 性能 |
| [mon_osd_err_op_age_ratio](#mon_osd_err_op_age_ratio) | `128` | Advanced | 性能 |
| [mon_reweight_max_change](#mon_reweight_max_change) | `0.05` | Advanced | 性能 |
| [mon_reweight_max_osds](#mon_reweight_max_osds) | `4` | Advanced | 性能 |
| [mon_reweight_min_bytes_per_osd](#mon_reweight_min_bytes_per_osd) | `100_M` | Advanced | 性能 |
| [mon_reweight_min_pgs_per_osd](#mon_reweight_min_pgs_per_osd) | `10` | Advanced | 性能 |
| [mon_warn_on_misplaced](#mon_warn_on_misplaced) | `False` | Advanced | 性能 |
| [mon_warn_on_too_few_osds](#mon_warn_on_too_few_osds) | `True` | Advanced | 性能 |

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
ceph config get <daemon> <option>  # e.g. mgr
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_cache_target_full_warn_ratio

| | |
|---|---|
| 类型 | Float · default `0.66` · **Advanced** |
| 表格 | [mon.md#SP_mon_cache_target_full_warn_ratio](../../../config/mgr/mon.md#SP_mon_cache_target_full_warn_ratio) |

**作用：** issue CACHE_POOL_NEAR_FULL health warning when cache pool utilization exceeds this ratio of usable space

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_cache_target_full_warn_ratio 0.66
ceph config get mon mon_cache_target_full_warn_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.66` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_cache_target_full_warn_ratio
ceph -s
ceph mon stat
```

---

### mon_osd_err_op_age_ratio

| | |
|---|---|
| 类型 | Float · default `128` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_err_op_age_ratio](../../../config/mgr/mon.md#SP_mon_osd_err_op_age_ratio) |

**作用：** issue REQUEST_STUCK health error if OSD ops are slower than is age (seconds)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_osd_err_op_age_ratio 128
ceph config get mon mon_osd_err_op_age_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `128` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_err_op_age_ratio
ceph -s
ceph mon stat
```

---

### mon_reweight_max_change

| | |
|---|---|
| 类型 | Float · default `0.05` · **Advanced** |
| 表格 | [mon.md#SP_mon_reweight_max_change](../../../config/mgr/mon.md#SP_mon_reweight_max_change) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_reweight_max_change 0.05
ceph config get mon mon_reweight_max_change
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.05` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_reweight_max_change
ceph -s
ceph mon stat
```

---

### mon_reweight_max_osds

| | |
|---|---|
| 类型 | Int · default `4` · **Advanced** |
| 表格 | [mon.md#SP_mon_reweight_max_osds](../../../config/mgr/mon.md#SP_mon_reweight_max_osds) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_reweight_max_osds 4
ceph config get mon mon_reweight_max_osds
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `4` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_reweight_max_osds
ceph -s
ceph mon stat
```

---

### mon_reweight_min_bytes_per_osd

| | |
|---|---|
| 类型 | Size · default `100_M` · **Advanced** |
| 表格 | [mon.md#SP_mon_reweight_min_bytes_per_osd](../../../config/mgr/mon.md#SP_mon_reweight_min_bytes_per_osd) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_reweight_min_bytes_per_osd 100_M
ceph config get mon mon_reweight_min_bytes_per_osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `100_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_reweight_min_bytes_per_osd
ceph -s
ceph mon stat
```

---

### mon_reweight_min_pgs_per_osd

| | |
|---|---|
| 类型 | Uint · default `10` · **Advanced** |
| 表格 | [mon.md#SP_mon_reweight_min_pgs_per_osd](../../../config/mgr/mon.md#SP_mon_reweight_min_pgs_per_osd) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_reweight_min_pgs_per_osd 10
ceph config get mon mon_reweight_min_pgs_per_osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_reweight_min_pgs_per_osd
ceph -s
ceph mon stat
```

---

### mon_warn_on_misplaced

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [mon.md#SP_mon_warn_on_misplaced](../../../config/mgr/mon.md#SP_mon_warn_on_misplaced) |

**作用：** Issue a health warning if there are misplaced objects

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mon mon_warn_on_misplaced true
ceph config get mon mon_warn_on_misplaced
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_warn_on_misplaced
ceph -s
ceph mon stat
```

---

### mon_warn_on_too_few_osds

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_warn_on_too_few_osds](../../../config/mgr/mon.md#SP_mon_warn_on_too_few_osds) |

**作用：** Issue a health warning if there are fewer OSDs than osd_pool_default_size

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_warn_on_too_few_osds false
ceph config get mon mon_warn_on_too_few_osds
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_warn_on_too_few_osds
ceph -s
ceph mon stat
```

---


[← 概览](../OVERVIEW.md)
