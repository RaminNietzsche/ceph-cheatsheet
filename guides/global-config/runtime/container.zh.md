# Container

Global 配置深度指南 — 1 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [container_image](#container_image) | `docker.io/ceph/daemon-base:latest-master-devel` | Basic | Policy |

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

### container_image

| | |
|---|---|
| 类型 | Str · default `docker.io/ceph/daemon-base:latest-master-devel` · **Basic** · **STARTUP**（需重启） |
| 表格 | [container.md#SP_container_image](../../../config/global/container.md#SP_container_image) |

**作用：** Container image for core daemons, used by the cephadm orchestrator

**何时使用：** 核心 Global 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set global container_image "docker.io/ceph/daemon-base:latest-master-devel"
ceph config get global container_image
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `docker.io/ceph/daemon-base:latest-master-devel` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global container_image
ceph -s
```

---


[← 概览](../OVERVIEW.md)
