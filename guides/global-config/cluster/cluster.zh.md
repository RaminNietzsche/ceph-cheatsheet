# Cluster

Global 配置深度指南 — 3 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [cluster_addr](#cluster_addr) | `(empty)` | Basic | Connectivity |
| [cluster_network](#cluster_network) | `(empty)` | Advanced | Performance |
| [cluster_network_interface](#cluster_network_interface) | `(empty)` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### cluster_addr

| | |
|---|---|
| 类型 | Addr · default `(empty)` · **Basic** · **STARTUP**（需重启） |
| 表格 | [cluster.md#SP_cluster_addr](../../../config/global/cluster.md#SP_cluster_addr) |

**作用：** Cluster-facing address to bind to

**何时使用：** 与外部服务集成时设置；未使用时留空。

**示例：**

```bash
ceph config set global cluster_addr (empty)
ceph config get global cluster_addr
```

**寻找最优值：**

**调优模型：** Connectivity

1. 列出环境中的候选端点。
2. 从运行守护进程的每个节点验证可达性。
3. 选择延迟最低且稳定的端点。
4. 未启用集成时留空（`(empty)`）。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global cluster_addr
ceph -s
```

---

### cluster_network

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [cluster.md#SP_cluster_network](../../../config/global/cluster.md#SP_cluster_network) |

**作用：** Network(s) from which to choose a cluster address to bind to

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global cluster_network "example"
ceph config get global cluster_network
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global cluster_network
ceph -s
```

---

### cluster_network_interface

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [cluster.md#SP_cluster_network_interface](../../../config/global/cluster.md#SP_cluster_network_interface) |

**作用：** Interface name(s) from which to choose an address from a ``cluster_network`` to bind to; ``cluster_network`` must also be specified.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global cluster_network_interface "example"
ceph config get global cluster_network_interface
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global cluster_network_interface
ceph -s
```

---


[← 概览](../OVERVIEW.md)
