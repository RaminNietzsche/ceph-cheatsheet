# Journal

RBD 配置深度指南 — 11 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rbd_journal_commit_age](#rbd_journal_commit_age) | `5` | Advanced | 性能 |
| [rbd_journal_max_concurrent_object_sets](#rbd_journal_max_concurrent_object_sets) | `0` | Advanced | 性能 |
| [rbd_journal_max_payload_bytes](#rbd_journal_max_payload_bytes) | `16_K` | Advanced | 性能 |
| [rbd_journal_object_flush_age](#rbd_journal_object_flush_age) | `0` | Advanced | 性能 |
| [rbd_journal_object_flush_bytes](#rbd_journal_object_flush_bytes) | `1_M` | Advanced | 性能 |
| [rbd_journal_object_flush_interval](#rbd_journal_object_flush_interval) | `0` | Advanced | 性能 |
| [rbd_journal_object_max_in_flight_appends](#rbd_journal_object_max_in_flight_appends) | `0` | Advanced | 性能 |
| [rbd_journal_object_writethrough_until_flush](#rbd_journal_object_writethrough_until_flush) | `True` | Advanced | 性能 |
| [rbd_journal_order](#rbd_journal_order) | `24` | Advanced | 性能 |
| [rbd_journal_pool](#rbd_journal_pool) | `(empty)` | Advanced | 性能 |
| [rbd_journal_splay_width](#rbd_journal_splay_width) | `4` | Advanced | 性能 |

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

### rbd_journal_commit_age

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_journal_commit_age](../../../config/rbd/rbd.md#SP_rbd_journal_commit_age) |

**作用：** commit time interval, seconds

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_journal_commit_age 5
ceph config get client rbd_journal_commit_age
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_journal_commit_age
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_journal_max_concurrent_object_sets

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_journal_max_concurrent_object_sets](../../../config/rbd/rbd.md#SP_rbd_journal_max_concurrent_object_sets) |

**作用：** maximum number of object sets a journal client can be behind before it is automatically unregistered

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client rbd_journal_max_concurrent_object_sets 64
ceph config get client rbd_journal_max_concurrent_object_sets
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_journal_max_concurrent_object_sets
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_journal_max_payload_bytes

| | |
|---|---|
| 类型 | Size · default `16_K` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_journal_max_payload_bytes](../../../config/rbd/rbd.md#SP_rbd_journal_max_payload_bytes) |

**作用：** maximum journal payload size before splitting

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client rbd_journal_max_payload_bytes 16_K
ceph config get client rbd_journal_max_payload_bytes
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `16_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_journal_max_payload_bytes
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_journal_object_flush_age

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_journal_object_flush_age](../../../config/rbd/rbd.md#SP_rbd_journal_object_flush_age) |

**作用：** maximum age (in seconds) for pending commits

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_journal_object_flush_age 0
ceph config get client rbd_journal_object_flush_age
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_journal_object_flush_age
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_journal_object_flush_bytes

| | |
|---|---|
| 类型 | Size · default `1_M` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_journal_object_flush_bytes](../../../config/rbd/rbd.md#SP_rbd_journal_object_flush_bytes) |

**作用：** maximum number of pending bytes per journal object

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_journal_object_flush_bytes 1_M
ceph config get client rbd_journal_object_flush_bytes
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_journal_object_flush_bytes
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_journal_object_flush_interval

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_journal_object_flush_interval](../../../config/rbd/rbd.md#SP_rbd_journal_object_flush_interval) |

**作用：** maximum number of pending commits per journal object

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set client rbd_journal_object_flush_interval 64
ceph config get client rbd_journal_object_flush_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_journal_object_flush_interval
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_journal_object_max_in_flight_appends

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_journal_object_max_in_flight_appends](../../../config/rbd/rbd.md#SP_rbd_journal_object_max_in_flight_appends) |

**作用：** maximum number of in-flight appends per journal object

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client rbd_journal_object_max_in_flight_appends 64
ceph config get client rbd_journal_object_max_in_flight_appends
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_journal_object_max_in_flight_appends
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_journal_object_writethrough_until_flush

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_journal_object_writethrough_until_flush](../../../config/rbd/rbd.md#SP_rbd_journal_object_writethrough_until_flush) |

**作用：** when enabled, the rbd_journal_object_flush* configuration options are ignored until the first flush so that batched journal IO is known to be safe for consistency

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client rbd_journal_object_writethrough_until_flush false
ceph config get client rbd_journal_object_writethrough_until_flush
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_journal_object_writethrough_until_flush
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_journal_order

| | |
|---|---|
| 类型 | Uint · default `24` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_journal_order](../../../config/rbd/rbd.md#SP_rbd_journal_order) |

**作用：** default order (object size) for journal data objects

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_journal_order 24
ceph config get client rbd_journal_order
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `24` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `12`，最大 `26`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_journal_order
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_journal_pool

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_journal_pool](../../../config/rbd/rbd.md#SP_rbd_journal_pool) |

**作用：** pool for journal objects

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_journal_pool "example"
ceph config get client rbd_journal_pool
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_journal_pool
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_journal_splay_width

| | |
|---|---|
| 类型 | Uint · default `4` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_journal_splay_width](../../../config/rbd/rbd.md#SP_rbd_journal_splay_width) |

**作用：** number of active journal objects

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_journal_splay_width 4
ceph config get client rbd_journal_splay_width
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `4` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_journal_splay_width
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---


[← 概览](../OVERVIEW.md)
