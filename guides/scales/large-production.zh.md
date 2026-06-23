# 大型生产规模

<span class="badge badge-scale-large">Large production</span> **12+ 节点**、大量 OSD、严格 SLA、独立网络、性能调优。

## 重点领域

| 领域 | 措施 |
|------|------|
| 调度 | `osd_mclock_profile`、设备类 |
| PG | 自动扩缩 + `mon_target_pg_per_osd` |
| Scrub | `osd_max_scrubs`、深度 scrub 窗口 |
| 网络 | public / cluster — [public.md](../../config/global/public.md) |
| CRUSH | 每机架/数据中心规则 |

## 命令

```bash
ceph osd crush class ls
ceph osd crush tree
ceph osd perf
ceph osd reweight-by-utilization 0.05
ceph osd ok-to-stop osd.0 osd.1 osd.2
```

## 配置审查

```bash
./scripts/lookup-config.sh osd_mclock_profile
./scripts/lookup-config.sh osd_max_scrubs
```

深度指南：[OSD](../osd-config/OVERVIEW.md) · [recovery](../osd-config/recovery/recovery.md)

## 限制恢复（业务时段）

```bash
ceph config set osd osd_max_backfills 1
ceph config set osd osd_recovery_max_active 3
```

[← 指南概览](../OVERVIEW.md)
