# Paths & storage

MON 配置深度指南 — 4 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mon_data](#mon_data) | `/var/lib/ceph/mon/$cluster-$id` | Advanced | Performance |
| [mon_data_avail_crit](#mon_data_avail_crit) | `5` | Advanced | Performance |
| [mon_data_avail_warn](#mon_data_avail_warn) | `30` | Advanced | Performance |
| [mon_data_size_warn](#mon_data_size_warn) | `15_G` | Advanced | Performance |

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

### mon_data

| | |
|---|---|
| 类型 | Str · default `/var/lib/ceph/mon/$cluster-$id` · **Advanced** |
| 表格 | [mon.md#SP_mon_data](../../../config/mon/mon.md#SP_mon_data) |

**作用：** path to mon database

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_data "/var/lib/ceph/mon/$cluster-$id"
ceph config get mon mon_data
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `/var/lib/ceph/mon/$cluster-$id` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_data
ceph -s
ceph mon stat
```

---

### mon_data_avail_crit

| | |
|---|---|
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [mon.md#SP_mon_data_avail_crit](../../../config/mon/mon.md#SP_mon_data_avail_crit) |

**作用：** issue MON_DISK_CRIT health error when mon available space below this percentage

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_data_avail_crit 5
ceph config get mon mon_data_avail_crit
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_data_avail_crit
ceph -s
ceph mon stat
```

---

### mon_data_avail_warn

| | |
|---|---|
| 类型 | Int · default `30` · **Advanced** |
| 表格 | [mon.md#SP_mon_data_avail_warn](../../../config/mon/mon.md#SP_mon_data_avail_warn) |

**作用：** issue MON_DISK_LOW health warning when mon available space below this percentage

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_data_avail_warn 30
ceph config get mon mon_data_avail_warn
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_data_avail_warn
ceph -s
ceph mon stat
```

---

### mon_data_size_warn

| | |
|---|---|
| 类型 | Size · default `15_G` · **Advanced** |
| 表格 | [mon.md#SP_mon_data_size_warn](../../../config/mon/mon.md#SP_mon_data_size_warn) |

**作用：** issue MON_DISK_BIG health warning when mon database is above this size

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_data_size_warn 15_G
ceph config get mon mon_data_size_warn
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `15_G` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_data_size_warn
ceph -s
ceph mon stat
```

---


[← 概览](../OVERVIEW.md)
