# Public

Global 配置深度指南 — 5 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [public_addr](#public_addr) | `(empty)` | Basic | 连通性 |
| [public_addrv](#public_addrv) | `(empty)` | Basic | 策略 |
| [public_bind_addr](#public_bind_addr) | `(empty)` | Advanced | 连通性 |
| [public_network](#public_network) | `(empty)` | Advanced | 性能 |
| [public_network_interface](#public_network_interface) | `(empty)` | Advanced | 性能 |

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

### public_addr

| | |
|---|---|
| 类型 | Addr · default `(empty)` · **Basic** · **STARTUP**（需重启） |
| 表格 | [public.md#SP_public_addr](../../../config/global/public.md#SP_public_addr) |

**作用：** Public-facing address to which to bind

**何时使用：** 与外部服务集成时设置；未使用时留空。

**示例：**

```bash
ceph config set global public_addr (empty)
ceph config get global public_addr
```

**寻找最优值：**

**调优模型：** 连通性

1. 列出环境中的候选端点。
2. 从运行守护进程的每个节点验证可达性。
3. 选择延迟最低且稳定的端点。
4. 未启用集成时留空（`(empty)`）。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global public_addr
ceph -s
```

---

### public_addrv

| | |
|---|---|
| 类型 | Addrvec · default `(empty)` · **Basic** · **STARTUP**（需重启） |
| 表格 | [public.md#SP_public_addrv](../../../config/global/public.md#SP_public_addrv) |

**作用：** Public-facing addresses to which services are to bind

**何时使用：** 核心 Global 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set global public_addrv (empty)
ceph config get global public_addrv
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `(empty)` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global public_addrv
ceph -s
```

---

### public_bind_addr

| | |
|---|---|
| 类型 | Addr · default `(empty)` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [public.md#SP_public_bind_addr](../../../config/global/public.md#SP_public_bind_addr) |

**何时使用：** 与外部服务集成时设置；未使用时留空。

**示例：**

```bash
ceph config set global public_bind_addr (empty)
ceph config get global public_bind_addr
```

**寻找最优值：**

**调优模型：** 连通性

1. 列出环境中的候选端点。
2. 从运行守护进程的每个节点验证可达性。
3. 选择延迟最低且稳定的端点。
4. 未启用集成时留空（`(empty)`）。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global public_bind_addr
ceph -s
```

---

### public_network

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [public.md#SP_public_network](../../../config/global/public.md#SP_public_network) |

**作用：** Network(s) from which to choose a public address to bind to

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global public_network "example"
ceph config get global public_network
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global public_network
ceph -s
```

---

### public_network_interface

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [public.md#SP_public_network_interface](../../../config/global/public.md#SP_public_network_interface) |

**作用：** Interface name(s) from which to choose an address from a ``public_network`` to bind to; ``public_network`` must also be specified.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**相关选项：**

- [`public_network`](../../../config/global/public.md#SP_public_network)

**示例：**

```bash
ceph config set global public_network_interface "example"
ceph config get global public_network_interface
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global public_network_interface
ceph -s
```

---


[← 概览](../OVERVIEW.md)
