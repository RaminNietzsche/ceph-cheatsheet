# MDS-related settings

MON 配置深度指南 — 1 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mds_beacon_mon_down_grace](#mds_beacon_mon_down_grace) | `1_min` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mds_beacon_mon_down_grace

| | |
|---|---|
| 类型 | Secs · default `1_min` · **Advanced** |
| 表格 | [mds.md#SP_mds_beacon_mon_down_grace](../../../config/mon/mds.md#SP_mds_beacon_mon_down_grace) |

**作用：** tolerance in seconds for missed MDS beacons to monitors

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_beacon_mon_down_grace 1_min
ceph config get mds mds_beacon_mon_down_grace
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_beacon_mon_down_grace
ceph -s
ceph fs status
ceph mds stat
```

---


[← 概览](../OVERVIEW.md)
