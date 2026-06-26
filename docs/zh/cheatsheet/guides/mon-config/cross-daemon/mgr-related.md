# MGR-related settings

MON 配置深度指南 — 6 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mon_mgr_beacon_grace](#mon_mgr_beacon_grace) | `30` | Advanced | 性能 |
| [mon_mgr_blocklist_interval](#mon_mgr_blocklist_interval) | `1_day` | Dev | 开发 |
| [mon_mgr_digest_period](#mon_mgr_digest_period) | `5` | Dev | 开发 |
| [mon_mgr_inactive_grace](#mon_mgr_inactive_grace) | `1_min` | Advanced | 性能 |
| [mon_mgr_mkfs_grace](#mon_mgr_mkfs_grace) | `2_min` | Advanced | 性能 |
| [mon_mgr_proxy_client_bytes_ratio](#mon_mgr_proxy_client_bytes_ratio) | `0.3` | Dev | 开发 |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_mgr_beacon_grace

| | |
|---|---|
| 类型 | Secs · default `30` · **Advanced** |
| 表格 | [mon.md#SP_mon_mgr_beacon_grace](../../../config/mon/mon.md#SP_mon_mgr_beacon_grace) |

**作用：** Period in seconds from last beacon to monitor marking a manager daemon as failed

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_mgr_beacon_grace 30
ceph config get mon mon_mgr_beacon_grace
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_mgr_beacon_grace
ceph -s
ceph mon stat
```

---

### mon_mgr_blocklist_interval

| | |
|---|---|
| 类型 | Float · default `1_day` · **Dev** |
| 表格 | [mon.md#SP_mon_mgr_blocklist_interval](../../../config/mon/mon.md#SP_mon_mgr_blocklist_interval) |

**作用：** Duration in seconds that blocklist entries for mgr daemons remain in the OSD map

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_mgr_blocklist_interval 1_day
ceph config get mon mon_mgr_blocklist_interval
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1_day`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_mgr_digest_period

| | |
|---|---|
| 类型 | Int · default `5` · **Dev** |
| 表格 | [mon.md#SP_mon_mgr_digest_period](../../../config/mon/mon.md#SP_mon_mgr_digest_period) |

**作用：** Period in seconds between monitor-to-manager health/status updates

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_mgr_digest_period 5
ceph config get mon mon_mgr_digest_period
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`5`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_mgr_inactive_grace

| | |
|---|---|
| 类型 | Int · default `1_min` · **Advanced** |
| 表格 | [mon.md#SP_mon_mgr_inactive_grace](../../../config/mon/mon.md#SP_mon_mgr_inactive_grace) |

**作用：** Period in seconds after cluster creation during which cluster may have no active manager This grace period enables the cluster to come up cleanly without raising spurious health check failures about managers that aren't online yet

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_mgr_inactive_grace 1_min
ceph config get mon mon_mgr_inactive_grace
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_mgr_inactive_grace
ceph -s
ceph mon stat
```

---

### mon_mgr_mkfs_grace

| | |
|---|---|
| 类型 | Int · default `2_min` · **Advanced** |
| 表格 | [mon.md#SP_mon_mgr_mkfs_grace](../../../config/mon/mon.md#SP_mon_mgr_mkfs_grace) |

**作用：** Period in seconds that the cluster may have no active manager before this is reported as an ERR rather than a WARN

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_mgr_mkfs_grace 2_min
ceph config get mon mon_mgr_mkfs_grace
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_mgr_mkfs_grace
ceph -s
ceph mon stat
```

---

### mon_mgr_proxy_client_bytes_ratio

| | |
|---|---|
| 类型 | Float · default `0.3` · **Dev** |
| 表格 | [mon.md#SP_mon_mgr_proxy_client_bytes_ratio](../../../config/mon/mon.md#SP_mon_mgr_proxy_client_bytes_ratio) |

**作用：** ratio of mon_client_bytes that can be consumed by proxied mgr commands before we error out to client

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_mgr_proxy_client_bytes_ratio 0.3
ceph config get mon mon_mgr_proxy_client_bytes_ratio
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0.3`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
