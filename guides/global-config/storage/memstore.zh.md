# Memstore

Global 配置深度指南 — 4 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [memstore_debug_omit_block_device_write](#memstore_debug_omit_block_device_write) | `False` | Dev | 开发 |
| [memstore_device_bytes](#memstore_device_bytes) | `1_G` | Advanced | 性能 |
| [memstore_page_set](#memstore_page_set) | `False` | Advanced | 性能 |
| [memstore_page_size](#memstore_page_size) | `64_K` | Advanced | 性能 |

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

### memstore_debug_omit_block_device_write

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [memstore.md#SP_memstore_debug_omit_block_device_write](../../../config/global/memstore.md#SP_memstore_debug_omit_block_device_write) |

**作用：** write metadata only

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global memstore_debug_omit_block_device_write true
ceph config get global memstore_debug_omit_block_device_write
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### memstore_device_bytes

| | |
|---|---|
| 类型 | Size · default `1_G` · **Advanced** |
| 表格 | [memstore.md#SP_memstore_device_bytes](../../../config/global/memstore.md#SP_memstore_device_bytes) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global memstore_device_bytes 1_G
ceph config get global memstore_device_bytes
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_G` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global memstore_device_bytes
ceph -s
```

---

### memstore_page_set

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [memstore.md#SP_memstore_page_set](../../../config/global/memstore.md#SP_memstore_page_set) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global memstore_page_set true
ceph config get global memstore_page_set
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global memstore_page_set
ceph -s
```

---

### memstore_page_size

| | |
|---|---|
| 类型 | Size · default `64_K` · **Advanced** |
| 表格 | [memstore.md#SP_memstore_page_size](../../../config/global/memstore.md#SP_memstore_page_size) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global memstore_page_size 64_K
ceph config get global memstore_page_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global memstore_page_size
ceph -s
```

---


[← 概览](../OVERVIEW.md)
