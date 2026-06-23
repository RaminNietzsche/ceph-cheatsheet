# Filer

Global 配置深度指南 — 2 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [filer_max_purge_ops](#filer_max_purge_ops) | `10` | Advanced | 性能 |
| [filer_max_truncate_ops](#filer_max_truncate_ops) | `128` | Advanced | 性能 |

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

### filer_max_purge_ops

| | |
|---|---|
| 类型 | Uint · default `10` · **Advanced** |
| 表格 | [filer.md#SP_filer_max_purge_ops](../../../config/global/filer.md#SP_filer_max_purge_ops) |

**作用：** Max in-flight operations for purging a striped range (e.g., MDS journal)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global filer_max_purge_ops 10
ceph config get global filer_max_purge_ops
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filer_max_purge_ops
ceph -s
```

---

### filer_max_truncate_ops

| | |
|---|---|
| 类型 | Uint · default `128` · **Advanced** |
| 表格 | [filer.md#SP_filer_max_truncate_ops](../../../config/global/filer.md#SP_filer_max_truncate_ops) |

**作用：** Max in-flight operations for truncating/deleting a striped sequence (e.g., MDS journal)

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global filer_max_truncate_ops 128
ceph config get global filer_max_truncate_ops
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `128` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global filer_max_truncate_ops
ceph -s
```

---


[← 概览](../OVERVIEW.md)
