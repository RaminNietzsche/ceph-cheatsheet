# Localize

RBD 配置深度指南 — 2 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rbd_localize_parent_reads](#rbd_localize_parent_reads) | `False` | Advanced | Performance |
| [rbd_localize_snap_reads](#rbd_localize_snap_reads) | `False` | Advanced | Performance |

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

### rbd_localize_parent_reads

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_localize_parent_reads](../../../config/rbd/rbd.md#SP_rbd_localize_parent_reads) |

**作用：** localize parent requests to closest OSD

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client rbd_localize_parent_reads true
ceph config get client rbd_localize_parent_reads
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_localize_parent_reads
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_localize_snap_reads

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_localize_snap_reads](../../../config/rbd/rbd.md#SP_rbd_localize_snap_reads) |

**作用：** localize snap read requests to closest OSD

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client rbd_localize_snap_reads true
ceph config get client rbd_localize_snap_reads
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_localize_snap_reads
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---


[← 概览](../OVERVIEW.md)
