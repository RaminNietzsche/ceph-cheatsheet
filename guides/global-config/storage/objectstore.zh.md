# Objectstore

Global 配置深度指南 — 2 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [objectstore_blackhole](#objectstore_blackhole) | `False` | Advanced | Performance |
| [objectstore_debug_throw_on_failed_txc](#objectstore_debug_throw_on_failed_txc) | `False` | Dev | Dev |

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

### objectstore_blackhole

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [objectstore.md#SP_objectstore_blackhole](../../../config/global/objectstore.md#SP_objectstore_blackhole) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global objectstore_blackhole true
ceph config get global objectstore_blackhole
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global objectstore_blackhole
ceph -s
```

---

### objectstore_debug_throw_on_failed_txc

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [objectstore.md#SP_objectstore_debug_throw_on_failed_txc](../../../config/global/objectstore.md#SP_objectstore_debug_throw_on_failed_txc) |

**作用：** Enables exception throwing instead of process abort on transaction submission error.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global objectstore_debug_throw_on_failed_txc true
ceph config get global objectstore_debug_throw_on_failed_txc
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
