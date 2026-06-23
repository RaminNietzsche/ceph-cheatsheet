# Cephx

Global 配置深度指南 — 7 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [cephx_cluster_require_signatures](#cephx_cluster_require_signatures) | `False` | Advanced | Performance |
| [cephx_cluster_require_version](#cephx_cluster_require_version) | `2` | Advanced | Performance |
| [cephx_require_signatures](#cephx_require_signatures) | `False` | Advanced | Performance |
| [cephx_require_version](#cephx_require_version) | `2` | Advanced | Performance |
| [cephx_service_require_signatures](#cephx_service_require_signatures) | `False` | Advanced | Performance |
| [cephx_service_require_version](#cephx_service_require_version) | `2` | Advanced | Performance |
| [cephx_sign_messages](#cephx_sign_messages) | `True` | Advanced | Performance |

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

### cephx_cluster_require_signatures

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [cephx.md#SP_cephx_cluster_require_signatures](../../../config/global/cephx.md#SP_cephx_cluster_require_signatures) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global cephx_cluster_require_signatures true
ceph config get global cephx_cluster_require_signatures
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global cephx_cluster_require_signatures
ceph -s
```

---

### cephx_cluster_require_version

| | |
|---|---|
| 类型 | Int · default `2` · **Advanced** |
| 表格 | [cephx.md#SP_cephx_cluster_require_version](../../../config/global/cephx.md#SP_cephx_cluster_require_version) |

**作用：** Cephx version required by the cluster from clients (1 = pre-mimic, 2 = mimic+)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global cephx_cluster_require_version 2
ceph config get global cephx_cluster_require_version
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global cephx_cluster_require_version
ceph -s
```

---

### cephx_require_signatures

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [cephx.md#SP_cephx_require_signatures](../../../config/global/cephx.md#SP_cephx_require_signatures) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global cephx_require_signatures true
ceph config get global cephx_require_signatures
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global cephx_require_signatures
ceph -s
```

---

### cephx_require_version

| | |
|---|---|
| 类型 | Int · default `2` · **Advanced** |
| 表格 | [cephx.md#SP_cephx_require_version](../../../config/global/cephx.md#SP_cephx_require_version) |

**作用：** Cephx version required (1 = pre-mimic, 2 = mimic+)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global cephx_require_version 2
ceph config get global cephx_require_version
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global cephx_require_version
ceph -s
```

---

### cephx_service_require_signatures

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [cephx.md#SP_cephx_service_require_signatures](../../../config/global/cephx.md#SP_cephx_service_require_signatures) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global cephx_service_require_signatures true
ceph config get global cephx_service_require_signatures
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global cephx_service_require_signatures
ceph -s
```

---

### cephx_service_require_version

| | |
|---|---|
| 类型 | Int · default `2` · **Advanced** |
| 表格 | [cephx.md#SP_cephx_service_require_version](../../../config/global/cephx.md#SP_cephx_service_require_version) |

**作用：** Cephx version required from ceph services (1 = pre-mimic, 2 = mimic+)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global cephx_service_require_version 2
ceph config get global cephx_service_require_version
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global cephx_service_require_version
ceph -s
```

---

### cephx_sign_messages

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [cephx.md#SP_cephx_sign_messages](../../../config/global/cephx.md#SP_cephx_sign_messages) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global cephx_sign_messages false
ceph config get global cephx_sign_messages
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global cephx_sign_messages
ceph -s
```

---


[← 概览](../OVERVIEW.md)
