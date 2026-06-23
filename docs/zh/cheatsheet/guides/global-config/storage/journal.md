# Journal

Global 配置深度指南 — 17 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [journal_aio](#journal_aio) | `True` | Dev | 开发 |
| [journal_align_min_size](#journal_align_min_size) | `64_K` | Dev | 开发 |
| [journal_block_align](#journal_block_align) | `True` | Dev | 开发 |
| [journal_block_size](#journal_block_size) | `4_K` | Dev | 开发 |
| [journal_dio](#journal_dio) | `True` | Dev | 开发 |
| [journal_discard](#journal_discard) | `False` | Dev | 开发 |
| [journal_force_aio](#journal_force_aio) | `False` | Dev | 开发 |
| [journal_ignore_corruption](#journal_ignore_corruption) | `False` | Dev | 开发 |
| [journal_max_write_bytes](#journal_max_write_bytes) | `10_M` | Advanced | 性能 |
| [journal_max_write_entries](#journal_max_write_entries) | `100` | Advanced | 性能 |
| [journal_replay_from](#journal_replay_from) | `0` | Dev | 开发 |
| [journal_throttle_high_multiple](#journal_throttle_high_multiple) | `0` | Dev | 开发 |
| [journal_throttle_high_threshhold](#journal_throttle_high_threshhold) | `0.9` | Dev | 开发 |
| [journal_throttle_low_threshhold](#journal_throttle_low_threshhold) | `0.6` | Dev | 开发 |
| [journal_throttle_max_multiple](#journal_throttle_max_multiple) | `0` | Dev | 开发 |
| [journal_write_header_frequency](#journal_write_header_frequency) | `0` | Dev | 开发 |
| [journal_zero_on_create](#journal_zero_on_create) | `False` | Dev | 开发 |

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

### journal_aio

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [journal.md#SP_journal_aio](../../../config/global/journal.md#SP_journal_aio) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global journal_aio false
ceph config get global journal_aio
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### journal_align_min_size

| | |
|---|---|
| 类型 | Size · default `64_K` · **Dev** |
| 表格 | [journal.md#SP_journal_align_min_size](../../../config/global/journal.md#SP_journal_align_min_size) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global journal_align_min_size 64_K
ceph config get global journal_align_min_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`64_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### journal_block_align

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [journal.md#SP_journal_block_align](../../../config/global/journal.md#SP_journal_block_align) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global journal_block_align false
ceph config get global journal_block_align
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### journal_block_size

| | |
|---|---|
| 类型 | Size · default `4_K` · **Dev** |
| 表格 | [journal.md#SP_journal_block_size](../../../config/global/journal.md#SP_journal_block_size) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global journal_block_size 4_K
ceph config get global journal_block_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`4_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### journal_dio

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [journal.md#SP_journal_dio](../../../config/global/journal.md#SP_journal_dio) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global journal_dio false
ceph config get global journal_dio
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### journal_discard

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [journal.md#SP_journal_discard](../../../config/global/journal.md#SP_journal_discard) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global journal_discard true
ceph config get global journal_discard
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### journal_force_aio

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [journal.md#SP_journal_force_aio](../../../config/global/journal.md#SP_journal_force_aio) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global journal_force_aio true
ceph config get global journal_force_aio
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### journal_ignore_corruption

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [journal.md#SP_journal_ignore_corruption](../../../config/global/journal.md#SP_journal_ignore_corruption) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global journal_ignore_corruption true
ceph config get global journal_ignore_corruption
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### journal_max_write_bytes

| | |
|---|---|
| 类型 | Size · default `10_M` · **Advanced** |
| 表格 | [journal.md#SP_journal_max_write_bytes](../../../config/global/journal.md#SP_journal_max_write_bytes) |

**作用：** Max bytes in flight to journal

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global journal_max_write_bytes 10_M
ceph config get global journal_max_write_bytes
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global journal_max_write_bytes
ceph -s
```

---

### journal_max_write_entries

| | |
|---|---|
| 类型 | Int · default `100` · **Advanced** |
| 表格 | [journal.md#SP_journal_max_write_entries](../../../config/global/journal.md#SP_journal_max_write_entries) |

**作用：** Max IOs in flight to journal (deprecated)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global journal_max_write_entries 100
ceph config get global journal_max_write_entries
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `100` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global journal_max_write_entries
ceph -s
```

---

### journal_replay_from

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [journal.md#SP_journal_replay_from](../../../config/global/journal.md#SP_journal_replay_from) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global journal_replay_from 64
ceph config get global journal_replay_from
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### journal_throttle_high_multiple

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [journal.md#SP_journal_throttle_high_multiple](../../../config/global/journal.md#SP_journal_throttle_high_multiple) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global journal_throttle_high_multiple 0
ceph config get global journal_throttle_high_multiple
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### journal_throttle_high_threshhold

| | |
|---|---|
| 类型 | Float · default `0.9` · **Dev** |
| 表格 | [journal.md#SP_journal_throttle_high_threshhold](../../../config/global/journal.md#SP_journal_throttle_high_threshhold) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global journal_throttle_high_threshhold 0.9
ceph config get global journal_throttle_high_threshhold
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0.9`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### journal_throttle_low_threshhold

| | |
|---|---|
| 类型 | Float · default `0.6` · **Dev** |
| 表格 | [journal.md#SP_journal_throttle_low_threshhold](../../../config/global/journal.md#SP_journal_throttle_low_threshhold) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global journal_throttle_low_threshhold 0.6
ceph config get global journal_throttle_low_threshhold
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0.6`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### journal_throttle_max_multiple

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [journal.md#SP_journal_throttle_max_multiple](../../../config/global/journal.md#SP_journal_throttle_max_multiple) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global journal_throttle_max_multiple 0
ceph config get global journal_throttle_max_multiple
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### journal_write_header_frequency

| | |
|---|---|
| 类型 | Uint · default `0` · **Dev** |
| 表格 | [journal.md#SP_journal_write_header_frequency](../../../config/global/journal.md#SP_journal_write_header_frequency) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global journal_write_header_frequency 64
ceph config get global journal_write_header_frequency
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### journal_zero_on_create

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [journal.md#SP_journal_zero_on_create](../../../config/global/journal.md#SP_journal_zero_on_create) |

**作用：** Deprecated

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global journal_zero_on_create true
ceph config get global journal_zero_on_create
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
