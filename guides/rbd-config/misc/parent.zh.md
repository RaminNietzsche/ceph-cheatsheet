# Parent

RBD 配置深度指南 — 1 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rbd_parent_cache_enabled](#rbd_parent_cache_enabled) | `False` | Advanced | Policy |

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

### rbd_parent_cache_enabled

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_parent_cache_enabled](../../../config/rbd/rbd.md#SP_rbd_parent_cache_enabled) |

**作用：** whether to enable rbd shared ro cache

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client rbd_parent_cache_enabled true
ceph config get client rbd_parent_cache_enabled
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_parent_cache_enabled
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---


[← 概览](../OVERVIEW.md)
