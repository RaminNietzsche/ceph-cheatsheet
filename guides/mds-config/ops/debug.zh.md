# Debug

MDS 配置深度指南 — 9 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mds/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mds_debug_frag](#mds_debug_frag) | `False` | Dev | 开发 |
| [mds_debug_scatterstat](#mds_debug_scatterstat) | `False` | Dev | 开发 |
| [mds_debug_subtrees](#mds_debug_subtrees) | `False` | Dev | 开发 |
| [mds_inject_health_dummy](#mds_inject_health_dummy) | `False` | Dev | 开发 |
| [mds_inject_journal_corrupt_dentry_first](#mds_inject_journal_corrupt_dentry_first) | `0.0` | Dev | 开发 |
| [mds_inject_migrator_session_race](#mds_inject_migrator_session_race) | `False` | Dev | 开发 |
| [mds_inject_rename_corrupt_dentry_first](#mds_inject_rename_corrupt_dentry_first) | `0.0` | Dev | 开发 |
| [mds_inject_skip_replaying_inotable](#mds_inject_skip_replaying_inotable) | `False` | Dev | 开发 |
| [mds_inject_traceless_reply_probability](#mds_inject_traceless_reply_probability) | `0` | Dev | 开发 |

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
ceph config get <daemon> <option>  # e.g. mds
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mds_debug_frag

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_debug_frag](../../../config/mds/mds.md#SP_mds_debug_frag) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_debug_frag true
ceph config get mds mds_debug_frag
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_debug_scatterstat

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_debug_scatterstat](../../../config/mds/mds.md#SP_mds_debug_scatterstat) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_debug_scatterstat true
ceph config get mds mds_debug_scatterstat
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_debug_subtrees

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_debug_subtrees](../../../config/mds/mds.md#SP_mds_debug_subtrees) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_debug_subtrees true
ceph config get mds mds_debug_subtrees
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_inject_health_dummy

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_inject_health_dummy](../../../config/mds/mds.md#SP_mds_inject_health_dummy) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_inject_health_dummy true
ceph config get mds mds_inject_health_dummy
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_inject_journal_corrupt_dentry_first

| | |
|---|---|
| 类型 | Float · default `0.0` · **Dev** |
| 表格 | [mds.md#SP_mds_inject_journal_corrupt_dentry_first](../../../config/mds/mds.md#SP_mds_inject_journal_corrupt_dentry_first) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_inject_journal_corrupt_dentry_first 0.0
ceph config get mds mds_inject_journal_corrupt_dentry_first
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0.0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_inject_migrator_session_race

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_inject_migrator_session_race](../../../config/mds/mds.md#SP_mds_inject_migrator_session_race) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_inject_migrator_session_race true
ceph config get mds mds_inject_migrator_session_race
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_inject_rename_corrupt_dentry_first

| | |
|---|---|
| 类型 | Float · default `0.0` · **Dev** |
| 表格 | [mds.md#SP_mds_inject_rename_corrupt_dentry_first](../../../config/mds/mds.md#SP_mds_inject_rename_corrupt_dentry_first) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_inject_rename_corrupt_dentry_first 0.0
ceph config get mds mds_inject_rename_corrupt_dentry_first
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0.0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_inject_skip_replaying_inotable

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_inject_skip_replaying_inotable](../../../config/mds/mds.md#SP_mds_inject_skip_replaying_inotable) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_inject_skip_replaying_inotable true
ceph config get mds mds_inject_skip_replaying_inotable
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_inject_traceless_reply_probability

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_inject_traceless_reply_probability](../../../config/mds/mds.md#SP_mds_inject_traceless_reply_probability) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_inject_traceless_reply_probability 0
ceph config get mds mds_inject_traceless_reply_probability
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
