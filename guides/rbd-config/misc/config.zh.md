# Config

RBD 配置深度指南 — 1 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rbd_config_pool_override_update_timestamp](#rbd_config_pool_override_update_timestamp) | `0` | Dev | Dev |

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
ceph config get <daemon> <option>  # e.g. rbd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_config_pool_override_update_timestamp

| | |
|---|---|
| 类型 | Uint · default `0` · **Dev** |
| 表格 | [rbd.md#SP_rbd_config_pool_override_update_timestamp](../../../config/rbd/rbd.md#SP_rbd_config_pool_override_update_timestamp) |

**作用：** timestamp of last update to pool-level config overrides

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client rbd_config_pool_override_update_timestamp 64
ceph config get client rbd_config_pool_override_update_timestamp
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
