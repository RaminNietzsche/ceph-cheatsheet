# 存储运维

<span class="badge badge-role-storage">存储运维</span> 管理 OSD、池、PG、CRUSH、恢复与 scrub。

## 日常命令

```bash
ceph osd stat
ceph osd tree
ceph osd df tree
ceph pg stat
ceph pg dump_stuck
ceph df detail
```

[OSD 与池 CLI](../../cli/osd-pool.md) · [RADOS CLI](../../cli/rados.md)

## 配置

| 领域 | 配置索引 |
|------|----------|
| OSD 守护进程 | [config/osd/INDEX.md](../../config/osd/INDEX.md) · [OSD 深度指南](../osd-config/OVERVIEW.md) |
| Global / bluestore | [osd.md](../../config/global/osd.md)、[bluestore.md](../../config/global/bluestore.md) |
| 恢复与 scrub | [recovery](../osd-config/recovery/recovery.md)、[scrub](../osd-config/scrub/scrub.md) |
| mClock | [mclock](../osd-config/mclock/mclock.md) — `osd_mclock_profile` |

```bash
./scripts/lookup-config.sh osd_max_scrubs
./scripts/search-config.sh -s osd recovery
```

## 常见工作流

**OSD 维护：**

```bash
ceph osd safe-to-destroy 5
ceph osd out 5
ceph osd in 5
```

**创建副本池：**

```bash
ceph osd pool create mypool 128 128 replicated
ceph osd pool application enable mypool rbd
ceph osd pool autoscale-status
```

**重平衡：**

```bash
ceph osd reweight-by-utilization
ceph osd crush reweight osd.5 0.95
```

## 规模说明

| 规模 | 重点 |
|------|------|
| [实验室](../scales/lab.md) | 较低 `osd_memory_target`、更少 PG |
| [小型生产](../scales/small-production.md) | 自动扩缩、三副本 |
| [大型生产](../scales/large-production.md) | mClock、设备类、scrub 窗口 |
| [多站点](../scales/multisite.md) | 各站点 CRUSH；DR 池布局 |

## 故障排查

降级 PG、backfill 限流、nearfull — [cli/troubleshooting.md](../../cli/troubleshooting.md)

[← 指南概览](../OVERVIEW.md)
