# Paths & data dirs

OSD 配置深度指南 — 2 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [osd_data](#osd_data) | `/var/lib/ceph/osd/$cluster-$id` | Advanced | Performance |
| [osd_skip_data_digest](#osd_skip_data_digest) | `False` | Dev | Dev |

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

### osd_data

| | |
|---|---|
| 类型 | Str · default `/var/lib/ceph/osd/$cluster-$id` · **Advanced** |
| 表格 | [osd.md#SP_osd_data](../../../config/osd/osd.md#SP_osd_data) |

**作用：** path to OSD data

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_data "/var/lib/ceph/osd/$cluster-$id"
ceph config get osd osd_data
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `/var/lib/ceph/osd/$cluster-$id` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_data
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_skip_data_digest

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [osd.md#SP_osd_skip_data_digest](../../../config/osd/osd.md#SP_osd_skip_data_digest) |

**作用：** Do not store full-object checksums if the backend (bluestore) does its own checksums. Only usable with all BlueStore OSDs.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set osd osd_skip_data_digest true
ceph config get osd osd_skip_data_digest
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
