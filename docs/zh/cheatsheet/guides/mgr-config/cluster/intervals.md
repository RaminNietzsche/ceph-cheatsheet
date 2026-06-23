# Intervals

MGR 配置深度指南 — 2 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mgr/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mon_delta_reset_interval](#mon_delta_reset_interval) | `10` | Advanced | 性能 |
| [mon_stat_smooth_intervals](#mon_stat_smooth_intervals) | `6` | Advanced | 性能 |

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
ceph config get <daemon> <option>  # e.g. mgr
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_delta_reset_interval

| | |
|---|---|
| 类型 | Float · default `10` · **Advanced** |
| 表格 | [mon.md#SP_mon_delta_reset_interval](../../../config/mgr/mon.md#SP_mon_delta_reset_interval) |

**作用：** window duration for rate calculations in 'ceph status'

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_delta_reset_interval 10
ceph config get mon mon_delta_reset_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_delta_reset_interval
ceph -s
ceph mon stat
```

---

### mon_stat_smooth_intervals

| | |
|---|---|
| 类型 | Uint · default `6` · **Advanced** |
| 表格 | [mon.md#SP_mon_stat_smooth_intervals](../../../config/mgr/mon.md#SP_mon_stat_smooth_intervals) |

**作用：** number of PGMaps stats over which we calc the average read/write throughput of the whole cluster

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_stat_smooth_intervals 6
ceph config get mon mon_stat_smooth_intervals
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `6` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_stat_smooth_intervals
ceph -s
ceph mon stat
```

---


[← 概览](../OVERVIEW.md)
