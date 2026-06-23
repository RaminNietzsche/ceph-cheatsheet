# Quiesce

RBD 配置深度指南 — 1 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rbd_quiesce_notification_attempts](#rbd_quiesce_notification_attempts) | `10` | Dev | 开发 |

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
ceph config get <daemon> <option>  # e.g. rbd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_quiesce_notification_attempts

| | |
|---|---|
| 类型 | Uint · default `10` · **Dev** |
| 表格 | [rbd.md#SP_rbd_quiesce_notification_attempts](../../../config/rbd/rbd.md#SP_rbd_quiesce_notification_attempts) |

**作用：** the number of quiesce notification attempts

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client rbd_quiesce_notification_attempts 10
ceph config get client rbd_quiesce_notification_attempts
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`10`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
