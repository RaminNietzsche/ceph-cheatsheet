# PG & pool settings

MGR 配置深度指南 — 11 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mgr/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mon_pg_check_down_all_threshold](#mon_pg_check_down_all_threshold) | `0.5` | Advanced | 性能 |
| [mon_pg_stuck_threshold](#mon_pg_stuck_threshold) | `1_min` | Advanced | 性能 |
| [mon_pg_warn_max_object_skew](#mon_pg_warn_max_object_skew) | `10` | Advanced | 性能 |
| [mon_pg_warn_min_objects](#mon_pg_warn_min_objects) | `10000` | Advanced | 性能 |
| [mon_pg_warn_min_per_osd](#mon_pg_warn_min_per_osd) | `0` | Advanced | 性能 |
| [mon_pg_warn_min_pool_objects](#mon_pg_warn_min_pool_objects) | `1000` | Advanced | 性能 |
| [mon_pool_quota_crit_threshold](#mon_pool_quota_crit_threshold) | `0` | Advanced | 性能 |
| [mon_pool_quota_warn_threshold](#mon_pool_quota_warn_threshold) | `0` | Advanced | 性能 |
| [mon_target_pg_per_osd](#mon_target_pg_per_osd) | `200` | Advanced | 性能 |
| [mon_warn_on_pool_no_app](#mon_warn_on_pool_no_app) | `True` | Dev | 开发 |
| [mon_warn_on_pool_no_app_grace](#mon_warn_on_pool_no_app_grace) | `5_min` | Dev | 开发 |

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

### mon_pg_check_down_all_threshold

| | |
|---|---|
| 类型 | Float · default `0.5` · **Advanced** |
| 表格 | [mon.md#SP_mon_pg_check_down_all_threshold](../../../config/mgr/mon.md#SP_mon_pg_check_down_all_threshold) |

**作用：** threshold of down osds after which we check all pgs

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_pg_check_down_all_threshold 0.5
ceph config get mon mon_pg_check_down_all_threshold
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_pg_check_down_all_threshold
ceph -s
ceph mon stat
```

---

### mon_pg_stuck_threshold

| | |
|---|---|
| 类型 | Int · default `1_min` · **Advanced** |
| 表格 | [mon.md#SP_mon_pg_stuck_threshold](../../../config/mgr/mon.md#SP_mon_pg_stuck_threshold) |

**作用：** number of seconds after which pgs can be considered stuck inactive, unclean, etc

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_pg_stuck_threshold 1_min
ceph config get mon mon_pg_stuck_threshold
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_pg_stuck_threshold
ceph -s
ceph mon stat
```

---

### mon_pg_warn_max_object_skew

| | |
|---|---|
| 类型 | Float · default `10` · **Advanced** |
| 表格 | [mon.md#SP_mon_pg_warn_max_object_skew](../../../config/mgr/mon.md#SP_mon_pg_warn_max_object_skew) |

**作用：** max skew few average in objects per pg

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_pg_warn_max_object_skew 10
ceph config get mon mon_pg_warn_max_object_skew
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_pg_warn_max_object_skew
ceph -s
ceph mon stat
```

---

### mon_pg_warn_min_objects

| | |
|---|---|
| 类型 | Int · default `10000` · **Advanced** |
| 表格 | [mon.md#SP_mon_pg_warn_min_objects](../../../config/mgr/mon.md#SP_mon_pg_warn_min_objects) |

**作用：** do not warn below this object #

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_pg_warn_min_objects 10000
ceph config get mon mon_pg_warn_min_objects
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_pg_warn_min_objects
ceph -s
ceph mon stat
```

---

### mon_pg_warn_min_per_osd

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [mon.md#SP_mon_pg_warn_min_per_osd](../../../config/mgr/mon.md#SP_mon_pg_warn_min_per_osd) |

**作用：** minimal number PGs per (in) osd before we warn the admin

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_pg_warn_min_per_osd 64
ceph config get mon mon_pg_warn_min_per_osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_pg_warn_min_per_osd
ceph -s
ceph mon stat
```

---

### mon_pg_warn_min_pool_objects

| | |
|---|---|
| 类型 | Int · default `1000` · **Advanced** |
| 表格 | [mon.md#SP_mon_pg_warn_min_pool_objects](../../../config/mgr/mon.md#SP_mon_pg_warn_min_pool_objects) |

**作用：** do not warn on pools below this object #

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_pg_warn_min_pool_objects 1000
ceph config get mon mon_pg_warn_min_pool_objects
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_pg_warn_min_pool_objects
ceph -s
ceph mon stat
```

---

### mon_pool_quota_crit_threshold

| | |
|---|---|
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [mon.md#SP_mon_pool_quota_crit_threshold](../../../config/mgr/mon.md#SP_mon_pool_quota_crit_threshold) |

**作用：** percent of quota at which to issue errors

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_pool_quota_crit_threshold 64
ceph config get mon mon_pool_quota_crit_threshold
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_pool_quota_crit_threshold
ceph -s
ceph mon stat
```

---

### mon_pool_quota_warn_threshold

| | |
|---|---|
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [mon.md#SP_mon_pool_quota_warn_threshold](../../../config/mgr/mon.md#SP_mon_pool_quota_warn_threshold) |

**作用：** percent of quota at which to issue warnings

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_pool_quota_warn_threshold 64
ceph config get mon mon_pool_quota_warn_threshold
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_pool_quota_warn_threshold
ceph -s
ceph mon stat
```

---

### mon_target_pg_per_osd

| | |
|---|---|
| 类型 | Uint · default `200` · **Advanced** |
| 表格 | [mon.md#SP_mon_target_pg_per_osd](../../../config/mgr/mon.md#SP_mon_target_pg_per_osd) |

**作用：** Target PGs per OSD for autoscaler and PG health warnings (also listed under MON cross-daemon settings in mgr config tables).

**何时使用：** Adjust when autoscaler consistently over/under-shards pools for your OSD count.

**示例：**

```bash
ceph config set mon mon_target_pg_per_osd 200
ceph config get mon mon_target_pg_per_osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `200` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_target_pg_per_osd
ceph -s
ceph mon stat
```

---

### mon_warn_on_pool_no_app

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [mon.md#SP_mon_warn_on_pool_no_app](../../../config/mgr/mon.md#SP_mon_warn_on_pool_no_app) |

**作用：** issue POOL_APP_NOT_ENABLED health warning if pool has not application enabled

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_warn_on_pool_no_app false
ceph config get mon mon_warn_on_pool_no_app
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_warn_on_pool_no_app_grace

| | |
|---|---|
| 类型 | Secs · default `5_min` · **Dev** |
| 表格 | [mon.md#SP_mon_warn_on_pool_no_app_grace](../../../config/mgr/mon.md#SP_mon_warn_on_pool_no_app_grace) |

**作用：** time after which POOL_APP_NOT_ENABLED health warning is issued

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_warn_on_pool_no_app_grace 5_min
ceph config get mon mon_warn_on_pool_no_app_grace
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`5_min`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
