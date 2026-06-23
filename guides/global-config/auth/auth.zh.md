# Auth

Global 配置深度指南 — 9 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [auth_allow_insecure_global_id_reclaim](#auth_allow_insecure_global_id_reclaim) | `True` | Advanced | Policy |
| [auth_client_required](#auth_client_required) | `cephx, none` | Advanced | Performance |
| [auth_cluster_required](#auth_cluster_required) | `cephx` | Advanced | Performance |
| [auth_debug](#auth_debug) | `False` | Dev | Dev |
| [auth_expose_insecure_global_id_reclaim](#auth_expose_insecure_global_id_reclaim) | `True` | Advanced | Policy |
| [auth_mon_ticket_ttl](#auth_mon_ticket_ttl) | `72_hr` | Advanced | Performance |
| [auth_service_required](#auth_service_required) | `cephx` | Advanced | Performance |
| [auth_service_ticket_ttl](#auth_service_ticket_ttl) | `1_hr` | Advanced | Performance |
| [auth_supported](#auth_supported) | `(empty)` | Advanced | Performance |

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

### auth_allow_insecure_global_id_reclaim

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [auth.md#SP_auth_allow_insecure_global_id_reclaim](../../../config/global/auth.md#SP_auth_allow_insecure_global_id_reclaim) |

**作用：** Allow reclaiming global_id without presenting a valid ticket proving previous possession of that global_id

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global auth_allow_insecure_global_id_reclaim false
ceph config get global auth_allow_insecure_global_id_reclaim
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global auth_allow_insecure_global_id_reclaim
ceph -s
```

---

### auth_client_required

| | |
|---|---|
| 类型 | Str · default `cephx, none` · **Advanced** |
| 表格 | [auth.md#SP_auth_client_required](../../../config/global/auth.md#SP_auth_client_required) |

**作用：** Authentication methods allowed by clients

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global auth_client_required "cephx, none"
ceph config get global auth_client_required
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `cephx, none` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global auth_client_required
ceph -s
```

---

### auth_cluster_required

| | |
|---|---|
| 类型 | Str · default `cephx` · **Advanced** |
| 表格 | [auth.md#SP_auth_cluster_required](../../../config/global/auth.md#SP_auth_cluster_required) |

**作用：** Authentication methods required by the cluster

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global auth_cluster_required cephx
ceph config get global auth_cluster_required
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `cephx` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global auth_cluster_required
ceph -s
```

---

### auth_debug

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [auth.md#SP_auth_debug](../../../config/global/auth.md#SP_auth_debug) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global auth_debug true
ceph config get global auth_debug
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### auth_expose_insecure_global_id_reclaim

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [auth.md#SP_auth_expose_insecure_global_id_reclaim](../../../config/global/auth.md#SP_auth_expose_insecure_global_id_reclaim) |

**作用：** Force older clients that may omit their ticket on reconnects to reconnect as part of establishing a session

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global auth_expose_insecure_global_id_reclaim false
ceph config get global auth_expose_insecure_global_id_reclaim
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global auth_expose_insecure_global_id_reclaim
ceph -s
```

---

### auth_mon_ticket_ttl

| | |
|---|---|
| 类型 | Float · default `72_hr` · **Advanced** |
| 表格 | [auth.md#SP_auth_mon_ticket_ttl](../../../config/global/auth.md#SP_auth_mon_ticket_ttl) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global auth_mon_ticket_ttl 72_hr
ceph config get global auth_mon_ticket_ttl
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `72_hr` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global auth_mon_ticket_ttl
ceph -s
```

---

### auth_service_required

| | |
|---|---|
| 类型 | Str · default `cephx` · **Advanced** |
| 表格 | [auth.md#SP_auth_service_required](../../../config/global/auth.md#SP_auth_service_required) |

**作用：** Authentication methods required by service daemons

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global auth_service_required cephx
ceph config get global auth_service_required
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `cephx` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global auth_service_required
ceph -s
```

---

### auth_service_ticket_ttl

| | |
|---|---|
| 类型 | Float · default `1_hr` · **Advanced** |
| 表格 | [auth.md#SP_auth_service_ticket_ttl](../../../config/global/auth.md#SP_auth_service_ticket_ttl) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global auth_service_ticket_ttl 1_hr
ceph config get global auth_service_ticket_ttl
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1_hr` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global auth_service_ticket_ttl
ceph -s
```

---

### auth_supported

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [auth.md#SP_auth_supported](../../../config/global/auth.md#SP_auth_supported) |

**作用：** Authentication methods required (deprecated)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global auth_supported "example"
ceph config get global auth_supported
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global auth_supported
ceph -s
```

---


[← 概览](../OVERVIEW.md)
