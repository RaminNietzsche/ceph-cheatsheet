# Debug

Global 配置深度指南 — 5 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [debug_asok_assert_abort](#debug_asok_assert_abort) | `False` | Dev | Dev |
| [debug_asserts_on_shutdown](#debug_asserts_on_shutdown) | `False` | Dev | Dev |
| [debug_deliberately_leak_memory](#debug_deliberately_leak_memory) | `False` | Dev | Dev |
| [debug_disable_randomized_ping](#debug_disable_randomized_ping) | `False` | Dev | Dev |
| [debug_heartbeat_testing_span](#debug_heartbeat_testing_span) | `0` | Dev | Dev |

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

### debug_asok_assert_abort

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [debug.md#SP_debug_asok_assert_abort](../../../config/global/debug.md#SP_debug_asok_assert_abort) |

**作用：** Enable the admin socket commands 'assert' and 'abort' testing crash dumps etc.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global debug_asok_assert_abort true
ceph config get global debug_asok_assert_abort
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### debug_asserts_on_shutdown

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [debug.md#SP_debug_asserts_on_shutdown](../../../config/global/debug.md#SP_debug_asserts_on_shutdown) |

**作用：** Enable certain assertions to check for refcounting bugs on shutdown; see http://tracker.ceph.com/issues/21738

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global debug_asserts_on_shutdown true
ceph config get global debug_asserts_on_shutdown
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### debug_deliberately_leak_memory

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [debug.md#SP_debug_deliberately_leak_memory](../../../config/global/debug.md#SP_debug_deliberately_leak_memory) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global debug_deliberately_leak_memory true
ceph config get global debug_deliberately_leak_memory
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### debug_disable_randomized_ping

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [debug.md#SP_debug_disable_randomized_ping](../../../config/global/debug.md#SP_debug_disable_randomized_ping) |

**作用：** Disable heartbeat ping randomization for testing purposes

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global debug_disable_randomized_ping true
ceph config get global debug_disable_randomized_ping
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### debug_heartbeat_testing_span

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [debug.md#SP_debug_heartbeat_testing_span](../../../config/global/debug.md#SP_debug_heartbeat_testing_span) |

**作用：** Override 60 second periods for testing only

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global debug_heartbeat_testing_span 64
ceph config get global debug_heartbeat_testing_span
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
