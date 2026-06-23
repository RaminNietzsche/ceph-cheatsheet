# Object classes

OSD 配置深度指南 — 5 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [osd_class_default_list](#osd_class_default_list) | `cephfs hello journal lock log numops otp rbd refcount rgw rgw_gc timeindex user version cas cmpomap queue 2pc_queue fifo sem_set` | Advanced | Performance |
| [osd_class_dir](#osd_class_dir) | `0/rados-classes` | Advanced | Capacity |
| [osd_class_load_list](#osd_class_load_list) | `cephfs hello journal lock log numops otp rbd refcount rgw rgw_gc timeindex user version cas cmpomap queue 2pc_queue fifo sem_set` | Advanced | Performance |
| [osd_class_update_on_start](#osd_class_update_on_start) | `True` | Advanced | Performance |
| [osd_open_classes_on_start](#osd_open_classes_on_start) | `True` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. osd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_class_default_list

| | |
|---|---|
| 类型 | Str · default `cephfs hello journal lock log numops otp rbd refcount rgw rgw_gc timeindex user version cas cmpomap queue 2pc_queue fifo sem_set` · **Advanced** |
| 表格 | [osd.md#SP_osd_class_default_list](../../../config/osd/osd.md#SP_osd_class_default_list) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_class_default_list "cephfs hello journal lock log numops otp rbd refcount rgw rgw_gc timeindex user version cas cmpomap queue 2pc_queue fifo sem_set"
ceph config get osd osd_class_default_list
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `cephfs hello journal lock log numops otp rbd refcount rgw rgw_gc timeindex user version cas cmpomap queue 2pc_queue fifo sem_set` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_class_default_list
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_class_dir

| | |
|---|---|
| 类型 | Str · default `0/rados-classes` · **Advanced** |
| 表格 | [osd.md#SP_osd_class_dir](../../../config/osd/osd.md#SP_osd_class_dir) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_class_dir "0/rados-classes"
ceph config get osd osd_class_dir
```

**寻找最优值：**

**调优模型：** Capacity

1. 以 `0/rados-classes` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_class_dir
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_class_load_list

| | |
|---|---|
| 类型 | Str · default `cephfs hello journal lock log numops otp rbd refcount rgw rgw_gc timeindex user version cas cmpomap queue 2pc_queue fifo sem_set` · **Advanced** |
| 表格 | [osd.md#SP_osd_class_load_list](../../../config/osd/osd.md#SP_osd_class_load_list) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_class_load_list "cephfs hello journal lock log numops otp rbd refcount rgw rgw_gc timeindex user version cas cmpomap queue 2pc_queue fifo sem_set"
ceph config get osd osd_class_load_list
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `cephfs hello journal lock log numops otp rbd refcount rgw rgw_gc timeindex user version cas cmpomap queue 2pc_queue fifo sem_set` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_class_load_list
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_class_update_on_start

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_class_update_on_start](../../../config/osd/osd.md#SP_osd_class_update_on_start) |

**作用：** set OSD device class on startup

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_class_update_on_start false
ceph config get osd osd_class_update_on_start
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_class_update_on_start
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_open_classes_on_start

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_open_classes_on_start](../../../config/osd/osd.md#SP_osd_open_classes_on_start) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_open_classes_on_start false
ceph config get osd osd_open_classes_on_start
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_open_classes_on_start
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← 概览](../OVERVIEW.md)
