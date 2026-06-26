# Lockdep

Global 配置深度指南 — 2 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [lockdep](#lockdep) | `False` | Dev | 开发 |
| [lockdep_force_backtrace](#lockdep_force_backtrace) | `False` | Dev | 开发 |

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

### lockdep

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** · **STARTUP**（需重启） |
| 表格 | [lockdep.md#SP_lockdep](../../../config/global/lockdep.md#SP_lockdep) |

**作用：** Enable the lockdep lock dependency analyzer

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global lockdep true
ceph config get global lockdep
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### lockdep_force_backtrace

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** · **STARTUP**（需重启） |
| 表格 | [lockdep.md#SP_lockdep_force_backtrace](../../../config/global/lockdep.md#SP_lockdep_force_backtrace) |

**作用：** Gather a current backtrace at every lock

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**相关选项：**

- [`lockdep`](../../../config/global/lockdep.md#SP_lockdep)

**示例：**

```bash
ceph config set global lockdep_force_backtrace true
ceph config get global lockdep_force_backtrace
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
