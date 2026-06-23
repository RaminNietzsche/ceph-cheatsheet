# Debug & injection

OSD 配置深度指南 — 4 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [osd_debug_feed_pullee](#osd_debug_feed_pullee) | `-1` | Dev | Dev |
| [osd_debug_trim_objects](#osd_debug_trim_objects) | `False` | Advanced | Performance |
| [osd_inject_bad_map_crc_probability](#osd_inject_bad_map_crc_probability) | `0` | Dev | Dev |
| [osd_inject_failure_on_pg_removal](#osd_inject_failure_on_pg_removal) | `False` | Dev | Dev |

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
ceph config get <daemon> <option>  # e.g. osd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_debug_feed_pullee

| | |
|---|---|
| 类型 | Int · default `-1` · **Dev** |
| 表格 | [osd.md#SP_osd_debug_feed_pullee](../../../config/osd/osd.md#SP_osd_debug_feed_pullee) |

**作用：** Feed a pullee, and force primary to pull a currently missing object from it

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_feed_pullee 128
ceph config get osd osd_debug_feed_pullee
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`-1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_debug_trim_objects

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_debug_trim_objects](../../../config/osd/osd.md#SP_osd_debug_trim_objects) |

**作用：** Asserts that no clone-objects were added to a snap after we start trimming it

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_debug_trim_objects true
ceph config get osd osd_debug_trim_objects
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_debug_trim_objects
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_inject_bad_map_crc_probability

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [osd.md#SP_osd_inject_bad_map_crc_probability](../../../config/osd/osd.md#SP_osd_inject_bad_map_crc_probability) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_inject_bad_map_crc_probability 0
ceph config get osd osd_inject_bad_map_crc_probability
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_inject_failure_on_pg_removal

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_inject_failure_on_pg_removal](../../../config/osd/osd.md#SP_osd_inject_failure_on_pg_removal) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_inject_failure_on_pg_removal true
ceph config get osd osd_inject_failure_on_pg_removal
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
