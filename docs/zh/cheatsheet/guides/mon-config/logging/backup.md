# Monitor backup

MON 配置深度指南 — 7 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mon_backup_cleanup_interval](#mon_backup_cleanup_interval) | `0` | Advanced | 性能 |
| [mon_backup_interval](#mon_backup_interval) | `0` | Advanced | 性能 |
| [mon_backup_keep_daily](#mon_backup_keep_daily) | `7` | Advanced | 性能 |
| [mon_backup_keep_hourly](#mon_backup_keep_hourly) | `5` | Advanced | 性能 |
| [mon_backup_keep_last](#mon_backup_keep_last) | `6` | Advanced | 性能 |
| [mon_backup_min_avail](#mon_backup_min_avail) | `10` | Advanced | 性能 |
| [mon_backup_path](#mon_backup_path) | `/var/backups/ceph/mon/$cluster-$id` | Advanced | 容量 |

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

### mon_backup_cleanup_interval

| | |
|---|---|
| 类型 | Secs · default `0` · **Advanced** |
| 表格 | [mon.md#SP_mon_backup_cleanup_interval](../../../config/mon/mon.md#SP_mon_backup_cleanup_interval) |

**作用：** Trigger backup cleanup every N seconds (0 disables)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_backup_cleanup_interval 0
ceph config get mon mon_backup_cleanup_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_backup_cleanup_interval
ceph -s
ceph mon stat
```

---

### mon_backup_interval

| | |
|---|---|
| 类型 | Secs · default `0` · **Advanced** |
| 表格 | [mon.md#SP_mon_backup_interval](../../../config/mon/mon.md#SP_mon_backup_interval) |

**作用：** Automatic backups every N seconds (0 disables)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_backup_interval 0
ceph config get mon mon_backup_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_backup_interval
ceph -s
ceph mon stat
```

---

### mon_backup_keep_daily

| | |
|---|---|
| 类型 | Uint · default `7` · **Advanced** |
| 表格 | [mon.md#SP_mon_backup_keep_daily](../../../config/mon/mon.md#SP_mon_backup_keep_daily) |

**作用：** Number of daily backups

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_backup_keep_daily 7
ceph config get mon mon_backup_keep_daily
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `7` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_backup_keep_daily
ceph -s
ceph mon stat
```

---

### mon_backup_keep_hourly

| | |
|---|---|
| 类型 | Uint · default `5` · **Advanced** |
| 表格 | [mon.md#SP_mon_backup_keep_hourly](../../../config/mon/mon.md#SP_mon_backup_keep_hourly) |

**作用：** Number of hourly backups

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_backup_keep_hourly 5
ceph config get mon mon_backup_keep_hourly
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_backup_keep_hourly
ceph -s
ceph mon stat
```

---

### mon_backup_keep_last

| | |
|---|---|
| 类型 | Uint · default `6` · **Advanced** |
| 表格 | [mon.md#SP_mon_backup_keep_last](../../../config/mon/mon.md#SP_mon_backup_keep_last) |

**作用：** Keep the last N backups

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_backup_keep_last 6
ceph config get mon mon_backup_keep_last
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `6` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_backup_keep_last
ceph -s
ceph mon stat
```

---

### mon_backup_min_avail

| | |
|---|---|
| 类型 | Int · default `10` · **Advanced** |
| 表格 | [mon.md#SP_mon_backup_min_avail](../../../config/mon/mon.md#SP_mon_backup_min_avail) |

**作用：** Only capture backups if at least this percentage of the target filesystem is free

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_backup_min_avail 10
ceph config get mon mon_backup_min_avail
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `100`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_backup_min_avail
ceph -s
ceph mon stat
```

---

### mon_backup_path

| | |
|---|---|
| 类型 | Str · default `/var/backups/ceph/mon/$cluster-$id` · **Advanced** |
| 表格 | [mon.md#SP_mon_backup_path](../../../config/mon/mon.md#SP_mon_backup_path) |

**作用：** Path to Monitor database backups

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_backup_path "/var/backups/ceph/mon/$cluster-$id"
ceph config get mon mon_backup_path
```

**寻找最优值：**

**调优模型：** 容量

1. 以 `/var/backups/ceph/mon/$cluster-$id` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_backup_path
ceph -s
ceph mon stat
```

---


[← 概览](../OVERVIEW.md)
