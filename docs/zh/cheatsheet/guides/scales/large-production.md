# 大型生产规模

<span class="badge badge-scale-large">大型生产</span> **12+ 节点**、大量 OSD、严格 SLA、独立网络、性能调优。

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
./scripts/search-config.sh -s osd mclock
./scripts/lookup-config.sh osd_mclock_profile
./scripts/lookup-config.sh osd_max_scrubs
./scripts/lookup-config.sh mon_osd_full_ratio
```

深度指南：[OSD](../osd-config/OVERVIEW.md) · [recovery](../osd-config/recovery/recovery.md) · [scrub](../osd-config/scrub/scrub.md)

## 限制恢复（业务时段）

```bash
ceph config set osd osd_max_backfills 1
ceph config set osd osd_recovery_max_active 3
```

## 角色指南

[storage-operator.md](../roles/storage-operator.md) · [cluster-admin.md](../roles/cluster-admin.md)

[← 指南概览](../OVERVIEW.md)

## 大型生产中的 RGW

多个无状态网关、共享 RADOS，尽量分离 public 与 cluster 网络。

| 关注点 | 措施 |
|--------|------|
| 调度 / 公平性 | [dmclock 架构](../../../arch/rgw/architecture/dmclock-architecture.md) |
| 客户端限速 | [速率限制](../../../arch/rgw/architecture/rate-limit-architecture.md) |
| 可观测性 | ops log、`rgw_perf_counters`、健康检查 — [可观测性](../../../arch/rgw/architecture/observability-overview.md) |
| HA 缺口 | [HA 限制](../../../arch/rgw/architecture/critical-gaps-and-ha-limitations.md) |

关注：持续偏高的 `l_rgw_qlen`、`ERR_RATE_LIMITED`、多站点同步滞后、GC/reshard 失败。
