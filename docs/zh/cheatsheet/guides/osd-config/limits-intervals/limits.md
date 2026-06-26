# Limits & caps

OSD 配置深度指南 — 15 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [osd_check_max_object_name_len_on_startup](#osd_check_max_object_name_len_on_startup) | `True` | Dev | 开发 |
| [osd_client_message_cap](#osd_client_message_cap) | `256` | Advanced | 性能 |
| [osd_client_message_size_cap](#osd_client_message_size_cap) | `500_M` | Advanced | 性能 |
| [osd_copyfrom_max_chunk](#osd_copyfrom_max_chunk) | `8_M` | Advanced | 性能 |
| [osd_heartbeat_min_peers](#osd_heartbeat_min_peers) | `10` | Advanced | 性能 |
| [osd_map_share_max_epochs](#osd_map_share_max_epochs) | `40` | Advanced | 性能 |
| [osd_max_markdown_count](#osd_max_markdown_count) | `5` | Advanced | 性能 |
| [osd_max_pgls](#osd_max_pgls) | `1_K` | Advanced | 性能 |
| [osd_max_push_cost](#osd_max_push_cost) | `8_M` | Advanced | 性能 |
| [osd_max_push_objects](#osd_max_push_objects) | `10` | Advanced | 性能 |
| [osd_max_write_size](#osd_max_write_size) | `90` | Advanced | 性能 |
| [osd_op_pq_max_tokens_per_priority](#osd_op_pq_max_tokens_per_priority) | `4_M` | Advanced | 性能 |
| [osd_op_pq_min_cost](#osd_op_pq_min_cost) | `64_K` | Advanced | 性能 |
| [osd_pg_epoch_max_lag_factor](#osd_pg_epoch_max_lag_factor) | `2` | Advanced | 性能 |
| [set_keepcaps](#set_keepcaps) | `False` | Advanced | 性能 |

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
ceph config get <daemon> <option>  # e.g. osd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_check_max_object_name_len_on_startup

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [osd.md#SP_osd_check_max_object_name_len_on_startup](../../../config/osd/osd.md#SP_osd_check_max_object_name_len_on_startup) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_check_max_object_name_len_on_startup false
ceph config get osd osd_check_max_object_name_len_on_startup
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### osd_client_message_cap

| | |
|---|---|
| 类型 | Uint · default `256` · **Advanced** |
| 表格 | [osd.md#SP_osd_client_message_cap](../../../config/osd/osd.md#SP_osd_client_message_cap) |

**作用：** maximum number of in-flight client requests

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_client_message_cap 256
ceph config get osd osd_client_message_cap
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `256` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_client_message_cap
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_client_message_size_cap

| | |
|---|---|
| 类型 | Size · default `500_M` · **Advanced** |
| 表格 | [osd.md#SP_osd_client_message_size_cap](../../../config/osd/osd.md#SP_osd_client_message_size_cap) |

**作用：** maximum memory to devote to in-flight client requests If this value is exceeded, the OSD will not read any new client data off of the network until memory is freed.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_client_message_size_cap 500_M
ceph config get osd osd_client_message_size_cap
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `500_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_client_message_size_cap
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_copyfrom_max_chunk

| | |
|---|---|
| 类型 | Size · default `8_M` · **Advanced** |
| 表格 | [osd.md#SP_osd_copyfrom_max_chunk](../../../config/osd/osd.md#SP_osd_copyfrom_max_chunk) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_copyfrom_max_chunk 8_M
ceph config get osd osd_copyfrom_max_chunk
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `8_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_copyfrom_max_chunk
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_heartbeat_min_peers

| | |
|---|---|
| 类型 | Int · default `10` · **Advanced** |
| 表格 | [osd.md#SP_osd_heartbeat_min_peers](../../../config/osd/osd.md#SP_osd_heartbeat_min_peers) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_heartbeat_min_peers 10
ceph config get osd osd_heartbeat_min_peers
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_heartbeat_min_peers
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_map_share_max_epochs

| | |
|---|---|
| 类型 | Int · default `40` · **Advanced** |
| 表格 | [osd.md#SP_osd_map_share_max_epochs](../../../config/osd/osd.md#SP_osd_map_share_max_epochs) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_map_share_max_epochs 40
ceph config get osd osd_map_share_max_epochs
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `40` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_map_share_max_epochs
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_markdown_count

| | |
|---|---|
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_markdown_count](../../../config/osd/osd.md#SP_osd_max_markdown_count) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_max_markdown_count 5
ceph config get osd osd_max_markdown_count
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_max_markdown_count
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_pgls

| | |
|---|---|
| 类型 | Uint · default `1_K` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_pgls](../../../config/osd/osd.md#SP_osd_max_pgls) |

**作用：** maximum number of results when listing objects in a pool

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_max_pgls 1_K
ceph config get osd osd_max_pgls
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_max_pgls
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_push_cost

| | |
|---|---|
| 类型 | Size · default `8_M` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_push_cost](../../../config/osd/osd.md#SP_osd_max_push_cost) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_max_push_cost 8_M
ceph config get osd osd_max_push_cost
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `8_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_max_push_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_push_objects

| | |
|---|---|
| 类型 | Uint · default `10` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_push_objects](../../../config/osd/osd.md#SP_osd_max_push_objects) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_max_push_objects 10
ceph config get osd osd_max_push_objects
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_max_push_objects
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_write_size

| | |
|---|---|
| 类型 | Size · default `90` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_write_size](../../../config/osd/osd.md#SP_osd_max_write_size) |

**作用：** Maximum size of a RADOS write operation in megabytes This setting prevents clients from doing very large writes to RADOS. If you set this to a value below what clients expect, they will receive an error when attempting to write to the cluster.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_max_write_size 90
ceph config get osd osd_max_write_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `90` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `4`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_max_write_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_pq_max_tokens_per_priority

| | |
|---|---|
| 类型 | Uint · default `4_M` · **Advanced** |
| 表格 | [osd.md#SP_osd_op_pq_max_tokens_per_priority](../../../config/osd/osd.md#SP_osd_op_pq_max_tokens_per_priority) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_op_pq_max_tokens_per_priority 4_M
ceph config get osd osd_op_pq_max_tokens_per_priority
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `4_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_op_pq_max_tokens_per_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_pq_min_cost

| | |
|---|---|
| 类型 | Size · default `64_K` · **Advanced** |
| 表格 | [osd.md#SP_osd_op_pq_min_cost](../../../config/osd/osd.md#SP_osd_op_pq_min_cost) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_op_pq_min_cost 64_K
ceph config get osd osd_op_pq_min_cost
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_op_pq_min_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pg_epoch_max_lag_factor

| | |
|---|---|
| 类型 | Float · default `2` · **Advanced** |
| 表格 | [osd.md#SP_osd_pg_epoch_max_lag_factor](../../../config/osd/osd.md#SP_osd_pg_epoch_max_lag_factor) |

**作用：** Max multiple of the map cache that PGs can lag before we throttle map injest

**何时使用：** 触及资源限制或保护集群容量时调整。

**相关选项：**

- [`osd_map_cache_size`](../../../config/osd/osd.md#SP_osd_map_cache_size)

**示例：**

```bash
ceph config set osd osd_pg_epoch_max_lag_factor 2
ceph config get osd osd_pg_epoch_max_lag_factor
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_pg_epoch_max_lag_factor
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### set_keepcaps

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [osd.md#SP_set_keepcaps](../../../config/osd/osd.md#SP_set_keepcaps) |

**作用：** set the keepcaps flag before changing UID, preserving the permitted capability set When ceph switches from root to the ceph uid, all capabilities in all sets are eraseed. If a component that is capability aware needs a specific capability, the keepcaps flag maintains the permitted capability set, allowing the capabilities in the effective set to be activated as needed.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd set_keepcaps true
ceph config get osd set_keepcaps
ceph orch restart osd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd set_keepcaps
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← 概览](../OVERVIEW.md)
