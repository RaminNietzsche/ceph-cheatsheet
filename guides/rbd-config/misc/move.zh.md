# Move

RBD 配置深度指南 — 3 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rbd_move_parent_to_trash_on_remove](#rbd_move_parent_to_trash_on_remove) | `False` | Basic | Policy |
| [rbd_move_to_trash_on_remove](#rbd_move_to_trash_on_remove) | `False` | Basic | Policy |
| [rbd_move_to_trash_on_remove_expire_seconds](#rbd_move_to_trash_on_remove_expire_seconds) | `0` | Basic | Policy |

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

### rbd_move_parent_to_trash_on_remove

| | |
|---|---|
| 类型 | Bool · default `False` · **Basic** |
| 表格 | [rbd.md#SP_rbd_move_parent_to_trash_on_remove](../../../config/rbd/rbd.md#SP_rbd_move_parent_to_trash_on_remove) |

**作用：** move parent with clone format v2 children to the trash when deleted

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client rbd_move_parent_to_trash_on_remove true
ceph config get client rbd_move_parent_to_trash_on_remove
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_move_parent_to_trash_on_remove
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_move_to_trash_on_remove

| | |
|---|---|
| 类型 | Bool · default `False` · **Basic** |
| 表格 | [rbd.md#SP_rbd_move_to_trash_on_remove](../../../config/rbd/rbd.md#SP_rbd_move_to_trash_on_remove) |

**作用：** automatically move images to the trash when deleted

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client rbd_move_to_trash_on_remove true
ceph config get client rbd_move_to_trash_on_remove
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_move_to_trash_on_remove
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_move_to_trash_on_remove_expire_seconds

| | |
|---|---|
| 类型 | Uint · default `0` · **Basic** |
| 表格 | [rbd.md#SP_rbd_move_to_trash_on_remove_expire_seconds](../../../config/rbd/rbd.md#SP_rbd_move_to_trash_on_remove_expire_seconds) |

**作用：** default number of seconds to protect deleted images in the trash

**何时使用：** 核心 RBD 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set client rbd_move_to_trash_on_remove_expire_seconds 64
ceph config get client rbd_move_to_trash_on_remove_expire_seconds
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `0` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_move_to_trash_on_remove_expire_seconds
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---


[← 概览](../OVERVIEW.md)
