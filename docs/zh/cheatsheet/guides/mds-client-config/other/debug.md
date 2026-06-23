# Debug

MDS client 配置深度指南 — 1 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mds-client/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [debug_allow_any_pool_priority](#debug_allow_any_pool_priority) | `False` | Dev | 开发 |

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
ceph config get <daemon> <option>  # e.g. mds-client
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### debug_allow_any_pool_priority

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [debug.md#SP_debug_allow_any_pool_priority](../../../config/mds-client/debug.md#SP_debug_allow_any_pool_priority) |

**作用：** Allow any pool priority to be set to test conversion to new range

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client debug_allow_any_pool_priority true
ceph config get client debug_allow_any_pool_priority
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
