# Cache

RBD 配置深度指南 — 8 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rbd_cache_block_writes_upfront](#rbd_cache_block_writes_upfront) | `False` | Advanced | Performance |
| [rbd_cache_max_dirty](#rbd_cache_max_dirty) | `24_M` | Advanced | Performance |
| [rbd_cache_max_dirty_age](#rbd_cache_max_dirty_age) | `1` | Advanced | Performance |
| [rbd_cache_max_dirty_object](#rbd_cache_max_dirty_object) | `0` | Advanced | Performance |
| [rbd_cache_policy](#rbd_cache_policy) | `writearound` | Advanced | Performance |
| [rbd_cache_size](#rbd_cache_size) | `32_M` | Advanced | Performance |
| [rbd_cache_target_dirty](#rbd_cache_target_dirty) | `16_M` | Advanced | Performance |
| [rbd_cache_writethrough_until_flush](#rbd_cache_writethrough_until_flush) | `True` | Advanced | Performance |

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

### rbd_cache_block_writes_upfront

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_cache_block_writes_upfront](../../../config/rbd/rbd.md#SP_rbd_cache_block_writes_upfront) |

**作用：** whether to block writes to the cache before the aio_write call completes

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client rbd_cache_block_writes_upfront true
ceph config get client rbd_cache_block_writes_upfront
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_cache_block_writes_upfront
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_cache_max_dirty

| | |
|---|---|
| 类型 | Size · default `24_M` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_cache_max_dirty](../../../config/rbd/rbd.md#SP_rbd_cache_max_dirty) |

**作用：** dirty limit in bytes - set to 0 for write-through caching

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client rbd_cache_max_dirty 24_M
ceph config get client rbd_cache_max_dirty
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `24_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_cache_max_dirty
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_cache_max_dirty_age

| | |
|---|---|
| 类型 | Float · default `1` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_cache_max_dirty_age](../../../config/rbd/rbd.md#SP_rbd_cache_max_dirty_age) |

**作用：** seconds in cache before writeback starts

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client rbd_cache_max_dirty_age 1
ceph config get client rbd_cache_max_dirty_age
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_cache_max_dirty_age
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_cache_max_dirty_object

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_cache_max_dirty_object](../../../config/rbd/rbd.md#SP_rbd_cache_max_dirty_object) |

**作用：** dirty limit for objects - set to 0 for auto calculate from rbd_cache_size

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client rbd_cache_max_dirty_object 64
ceph config get client rbd_cache_max_dirty_object
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_cache_max_dirty_object
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_cache_policy

| | |
|---|---|
| 类型 | Str · enum: ["writethrough", "writeback", "writearound"] · default `writearound` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_cache_policy](../../../config/rbd/rbd.md#SP_rbd_cache_policy) |

**作用：** cache policy for handling writes.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_cache_policy writearound
ceph config get client rbd_cache_policy
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `writearound` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_cache_policy
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_cache_size

| | |
|---|---|
| 类型 | Size · default `32_M` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_cache_size](../../../config/rbd/rbd.md#SP_rbd_cache_size) |

**作用：** cache size in bytes

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_cache_size 32_M
ceph config get client rbd_cache_size
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `32_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_cache_size
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_cache_target_dirty

| | |
|---|---|
| 类型 | Size · default `16_M` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_cache_target_dirty](../../../config/rbd/rbd.md#SP_rbd_cache_target_dirty) |

**作用：** target dirty limit in bytes

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_cache_target_dirty 16_M
ceph config get client rbd_cache_target_dirty
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `16_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_cache_target_dirty
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_cache_writethrough_until_flush

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_cache_writethrough_until_flush](../../../config/rbd/rbd.md#SP_rbd_cache_writethrough_until_flush) |

**作用：** whether to make writeback caching writethrough until flush is called, to be sure the user of librbd will send flushes so that writeback is safe

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client rbd_cache_writethrough_until_flush false
ceph config get client rbd_cache_writethrough_until_flush
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_cache_writethrough_until_flush
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---


[← 概览](../OVERVIEW.md)
