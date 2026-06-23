# Mirroring

RBD 配置深度指南 — 4 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rbd_mirroring_delete_delay](#rbd_mirroring_delete_delay) | `0` | Advanced | 性能 |
| [rbd_mirroring_max_mirroring_snapshots](#rbd_mirroring_max_mirroring_snapshots) | `5` | Advanced | 性能 |
| [rbd_mirroring_replay_delay](#rbd_mirroring_replay_delay) | `0` | Advanced | 性能 |
| [rbd_mirroring_resync_after_disconnect](#rbd_mirroring_resync_after_disconnect) | `False` | Advanced | 性能 |

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

### rbd_mirroring_delete_delay

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirroring_delete_delay](../../../config/rbd/rbd.md#SP_rbd_mirroring_delete_delay) |

**作用：** time-delay in seconds for rbd-mirror delete propagation

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_mirroring_delete_delay 64
ceph config get client rbd_mirroring_delete_delay
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirroring_delete_delay
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirroring_max_mirroring_snapshots

| | |
|---|---|
| 类型 | Uint · default `5` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirroring_max_mirroring_snapshots](../../../config/rbd/rbd.md#SP_rbd_mirroring_max_mirroring_snapshots) |

**作用：** mirroring snapshots limit

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client rbd_mirroring_max_mirroring_snapshots 5
ceph config get client rbd_mirroring_max_mirroring_snapshots
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `3`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirroring_max_mirroring_snapshots
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirroring_replay_delay

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirroring_replay_delay](../../../config/rbd/rbd.md#SP_rbd_mirroring_replay_delay) |

**作用：** time-delay in seconds for rbd-mirror asynchronous replication

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_mirroring_replay_delay 64
ceph config get client rbd_mirroring_replay_delay
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirroring_replay_delay
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_mirroring_resync_after_disconnect

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mirroring_resync_after_disconnect](../../../config/rbd/rbd.md#SP_rbd_mirroring_resync_after_disconnect) |

**作用：** automatically start image resync after mirroring is disconnected due to being laggy

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client rbd_mirroring_resync_after_disconnect true
ceph config get client rbd_mirroring_resync_after_disconnect
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mirroring_resync_after_disconnect
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---


[← 概览](../OVERVIEW.md)
