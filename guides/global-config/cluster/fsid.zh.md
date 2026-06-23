# Fsid

Global 配置深度指南 — 1 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [fsid](#fsid) | `(empty)` | Basic | Policy |

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

### fsid

| | |
|---|---|
| 类型 | Uuid · default `(empty)` · **Basic** · **STARTUP**（需重启） |
| 表格 | [fsid.md#SP_fsid](../../../config/global/fsid.md#SP_fsid) |

**作用：** cluster fsid (uuid)

**何时使用：** 核心 Global 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set global fsid (empty)
ceph config get global fsid
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `(empty)` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global fsid
ceph -s
```

---


[← 概览](../OVERVIEW.md)
