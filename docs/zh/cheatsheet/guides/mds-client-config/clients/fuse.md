# FUSE client

MDS client 配置深度指南 — 15 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mds-client/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [fuse_allow_other](#fuse_allow_other) | `True` | Advanced | 策略 |
| [fuse_atomic_o_trunc](#fuse_atomic_o_trunc) | `True` | Advanced | 性能 |
| [fuse_big_writes](#fuse_big_writes) | `True` | Advanced | 性能 |
| [fuse_debug](#fuse_debug) | `False` | Advanced | 性能 |
| [fuse_default_permissions](#fuse_default_permissions) | `False` | Advanced | 性能 |
| [fuse_disable_pagecache](#fuse_disable_pagecache) | `False` | Advanced | 策略 |
| [fuse_max_write](#fuse_max_write) | `0` | Advanced | 性能 |
| [fuse_multithreaded](#fuse_multithreaded) | `True` | Advanced | 性能 |
| [fuse_require_active_mds](#fuse_require_active_mds) | `True` | Advanced | 性能 |
| [fuse_set_user_groups](#fuse_set_user_groups) | `True` | Advanced | 性能 |
| [fuse_splice_move](#fuse_splice_move) | `True` | Advanced | 性能 |
| [fuse_splice_read](#fuse_splice_read) | `True` | Advanced | 性能 |
| [fuse_splice_write](#fuse_splice_write) | `True` | Advanced | 性能 |
| [fuse_syncfs_on_mksnap](#fuse_syncfs_on_mksnap) | `True` | Advanced | 性能 |
| [fuse_use_invalidate_cb](#fuse_use_invalidate_cb) | `True` | Advanced | 性能 |

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

### fuse_allow_other

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [fuse.md#SP_fuse_allow_other](../../../config/mds-client/fuse.md#SP_fuse_allow_other) |

**作用：** pass allow_other to FUSE on mount

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client fuse_allow_other false
ceph config get client fuse_allow_other
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client fuse_allow_other
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### fuse_atomic_o_trunc

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [fuse.md#SP_fuse_atomic_o_trunc](../../../config/mds-client/fuse.md#SP_fuse_atomic_o_trunc) |

**作用：** pass atomic_o_trunc flag to FUSE on mount

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client fuse_atomic_o_trunc false
ceph config get client fuse_atomic_o_trunc
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client fuse_atomic_o_trunc
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### fuse_big_writes

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [fuse.md#SP_fuse_big_writes](../../../config/mds-client/fuse.md#SP_fuse_big_writes) |

**作用：** big_writes is deprecated in libfuse 3.0.0

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client fuse_big_writes false
ceph config get client fuse_big_writes
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client fuse_big_writes
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### fuse_debug

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [fuse.md#SP_fuse_debug](../../../config/mds-client/fuse.md#SP_fuse_debug) |

**作用：** enable debugging for the libfuse

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client fuse_debug true
ceph config get client fuse_debug
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client fuse_debug
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### fuse_default_permissions

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [fuse.md#SP_fuse_default_permissions](../../../config/mds-client/fuse.md#SP_fuse_default_permissions) |

**作用：** pass default_permisions to FUSE on mount

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client fuse_default_permissions true
ceph config get client fuse_default_permissions
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client fuse_default_permissions
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### fuse_disable_pagecache

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [fuse.md#SP_fuse_disable_pagecache](../../../config/mds-client/fuse.md#SP_fuse_disable_pagecache) |

**作用：** disable page caching in the kernel for this FUSE mount

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client fuse_disable_pagecache true
ceph config get client fuse_disable_pagecache
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client fuse_disable_pagecache
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### fuse_max_write

| | |
|---|---|
| 类型 | Size · default `0` · **Advanced** |
| 表格 | [fuse.md#SP_fuse_max_write](../../../config/mds-client/fuse.md#SP_fuse_max_write) |

**作用：** set the maximum number of bytes in a single write operation Set the maximum number of bytes in a single write operation that may pass atomically through FUSE. The FUSE default is 128kB and may be indicated by setting this option to 0.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client fuse_max_write 64
ceph config get client fuse_max_write
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client fuse_max_write
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### fuse_multithreaded

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [fuse.md#SP_fuse_multithreaded](../../../config/mds-client/fuse.md#SP_fuse_multithreaded) |

**作用：** allow parallel processing through FUSE library

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client fuse_multithreaded false
ceph config get client fuse_multithreaded
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client fuse_multithreaded
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### fuse_require_active_mds

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [fuse.md#SP_fuse_require_active_mds](../../../config/mds-client/fuse.md#SP_fuse_require_active_mds) |

**作用：** require active MDSs in the file system when mounting

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client fuse_require_active_mds false
ceph config get client fuse_require_active_mds
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client fuse_require_active_mds
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### fuse_set_user_groups

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [fuse.md#SP_fuse_set_user_groups](../../../config/mds-client/fuse.md#SP_fuse_set_user_groups) |

**作用：** check for ceph-fuse to consider supplementary groups for permissions

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client fuse_set_user_groups false
ceph config get client fuse_set_user_groups
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client fuse_set_user_groups
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### fuse_splice_move

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [fuse.md#SP_fuse_splice_move](../../../config/mds-client/fuse.md#SP_fuse_splice_move) |

**作用：** enable splice move to reduce the memory copies

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client fuse_splice_move false
ceph config get client fuse_splice_move
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client fuse_splice_move
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### fuse_splice_read

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [fuse.md#SP_fuse_splice_read](../../../config/mds-client/fuse.md#SP_fuse_splice_read) |

**作用：** enable splice read to reduce the memory copies

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client fuse_splice_read false
ceph config get client fuse_splice_read
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client fuse_splice_read
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### fuse_splice_write

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [fuse.md#SP_fuse_splice_write](../../../config/mds-client/fuse.md#SP_fuse_splice_write) |

**作用：** enable splice write to reduce the memory copies

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client fuse_splice_write false
ceph config get client fuse_splice_write
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client fuse_splice_write
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### fuse_syncfs_on_mksnap

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [fuse.md#SP_fuse_syncfs_on_mksnap](../../../config/mds-client/fuse.md#SP_fuse_syncfs_on_mksnap) |

**作用：** synchronize all local metadata/file changes after snapshot

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client fuse_syncfs_on_mksnap false
ceph config get client fuse_syncfs_on_mksnap
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client fuse_syncfs_on_mksnap
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### fuse_use_invalidate_cb

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [fuse.md#SP_fuse_use_invalidate_cb](../../../config/mds-client/fuse.md#SP_fuse_use_invalidate_cb) |

**作用：** use fuse 2.8+ invalidate callback to keep page cache consistent

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client fuse_use_invalidate_cb false
ceph config get client fuse_use_invalidate_cb
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client fuse_use_invalidate_cb
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---


[← 概览](../OVERVIEW.md)
