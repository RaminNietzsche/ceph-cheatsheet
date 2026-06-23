# General

RBD 配置深度指南 — 3 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rbd_cache](#rbd_cache) | `True` | Advanced | Performance |
| [rbd_plugins](#rbd_plugins) | `(empty)` | Advanced | Performance |
| [rbd_tracing](#rbd_tracing) | `False` | Advanced | Performance |

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

### rbd_cache

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_cache](../../../config/rbd/rbd.md#SP_rbd_cache) |

**作用：** whether to enable caching (writeback unless rbd_cache_max_dirty is 0)

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client rbd_cache false
ceph config get client rbd_cache
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_cache
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_plugins

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_plugins](../../../config/rbd/rbd.md#SP_rbd_plugins) |

**作用：** comma-delimited list of librbd plugins to enable

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_plugins "example"
ceph config get client rbd_plugins
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_plugins
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_tracing

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_tracing](../../../config/rbd/rbd.md#SP_rbd_tracing) |

**作用：** true if LTTng-UST tracepoints should be enabled

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client rbd_tracing true
ceph config get client rbd_tracing
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_tracing
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---


[← 概览](../OVERVIEW.md)
