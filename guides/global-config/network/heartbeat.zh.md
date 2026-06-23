# Heartbeat

Global 配置深度指南 — 3 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [heartbeat_file](#heartbeat_file) | `(empty)` | Advanced | Capacity |
| [heartbeat_inject_failure](#heartbeat_inject_failure) | `0` | Dev | Dev |
| [heartbeat_interval](#heartbeat_interval) | `5` | Advanced | Performance |

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

### heartbeat_file

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [heartbeat.md#SP_heartbeat_file](../../../config/global/heartbeat.md#SP_heartbeat_file) |

**作用：** File to touch on successful internal heartbeat

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global heartbeat_file "example"
ceph config get global heartbeat_file
```

**寻找最优值：**

**调优模型：** Capacity

1. 以 `(empty)` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global heartbeat_file
ceph -s
```

---

### heartbeat_inject_failure

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [heartbeat.md#SP_heartbeat_inject_failure](../../../config/global/heartbeat.md#SP_heartbeat_inject_failure) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global heartbeat_inject_failure 64
ceph config get global heartbeat_inject_failure
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### heartbeat_interval

| | |
|---|---|
| 类型 | Int · default `5` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [heartbeat.md#SP_heartbeat_interval](../../../config/global/heartbeat.md#SP_heartbeat_interval) |

**作用：** Frequency of internal heartbeat checks (seconds)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global heartbeat_interval 5
ceph config get global heartbeat_interval
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global heartbeat_interval
ceph -s
```

---


[← 概览](../OVERVIEW.md)
