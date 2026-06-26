# CRUSH & weight

OSD 配置深度指南 — 2 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [osd_crush_initial_weight](#osd_crush_initial_weight) | `-1` | Advanced | 性能 |
| [osd_crush_update_on_start](#osd_crush_update_on_start) | `True` | Advanced | 性能 |

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

### osd_crush_initial_weight

| | |
|---|---|
| 类型 | Float · default `-1` · **Advanced** |
| 表格 | [osd.md#SP_osd_crush_initial_weight](../../../config/osd/osd.md#SP_osd_crush_initial_weight) |

**作用：** if >= 0, initial CRUSH weight for newly created OSDs If this value is negative, the size of the OSD in TiB is used.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_crush_initial_weight -1
ceph config get osd osd_crush_initial_weight
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `-1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_crush_initial_weight
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_crush_update_on_start

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [osd.md#SP_osd_crush_update_on_start](../../../config/osd/osd.md#SP_osd_crush_update_on_start) |

**作用：** update OSD CRUSH location on startup

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set osd osd_crush_update_on_start false
ceph config get osd osd_crush_update_on_start
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_crush_update_on_start
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← 概览](../OVERVIEW.md)
