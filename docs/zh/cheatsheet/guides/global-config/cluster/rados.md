# Rados

Global 配置深度指南 — 5 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rados_mon_op_timeout](#rados_mon_op_timeout) | `0` | Advanced | 性能 |
| [rados_osd_op_timeout](#rados_osd_op_timeout) | `0` | Advanced | 性能 |
| [rados_replica_read_policy](#rados_replica_read_policy) | `default` | Advanced | 性能 |
| [rados_replica_read_policy_on_objclass](#rados_replica_read_policy_on_objclass) | `False` | Advanced | 性能 |
| [rados_tracing](#rados_tracing) | `False` | Advanced | 性能 |

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
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rados_mon_op_timeout

| | |
|---|---|
| 类型 | Secs · default `0` · **Advanced** |
| 表格 | [rados.md#SP_rados_mon_op_timeout](../../../config/global/rados.md#SP_rados_mon_op_timeout) |

**作用：** Timeout for operations handled by Monitors, for example statfs(). (0 is unlimited)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global rados_mon_op_timeout 0
ceph config get global rados_mon_op_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global rados_mon_op_timeout
ceph -s
```

---

### rados_osd_op_timeout

| | |
|---|---|
| 类型 | Secs · default `0` · **Advanced** |
| 表格 | [rados.md#SP_rados_osd_op_timeout](../../../config/global/rados.md#SP_rados_osd_op_timeout) |

**作用：** Timeout for operations handled by OSDs, for example write(). (0 is unlimited)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global rados_osd_op_timeout 0
ceph config get global rados_osd_op_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global rados_osd_op_timeout
ceph -s
```

---

### rados_replica_read_policy

| | |
|---|---|
| 类型 | Str · enum: ["default", "balance", "localize"] · default `default` · **Advanced** |
| 表格 | [rados.md#SP_rados_replica_read_policy](../../../config/global/rados.md#SP_rados_replica_read_policy) |

**作用：** Read policy for sending read requests to OSD

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global rados_replica_read_policy default
ceph config get global rados_replica_read_policy
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `default` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global rados_replica_read_policy
ceph -s
```

---

### rados_replica_read_policy_on_objclass

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rados.md#SP_rados_replica_read_policy_on_objclass](../../../config/global/rados.md#SP_rados_replica_read_policy_on_objclass) |

**作用：** Enable read policy for sending read requests to OSD on objclass ops

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global rados_replica_read_policy_on_objclass true
ceph config get global rados_replica_read_policy_on_objclass
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global rados_replica_read_policy_on_objclass
ceph -s
```

---

### rados_tracing

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rados.md#SP_rados_tracing](../../../config/global/rados.md#SP_rados_tracing) |

**作用：** Should LTTng-UST tracepoints be enabled?

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global rados_tracing true
ceph config get global rados_tracing
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global rados_tracing
ceph -s
```

---


[← 概览](../OVERVIEW.md)
