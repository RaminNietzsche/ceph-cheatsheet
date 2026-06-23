# 存储运维

<span class="badge badge-role-storage">Storage operator</span> 管理 OSD、池、PG、CRUSH、恢复与 scrub。

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
| [Lab](../scales/lab.md) | 较低 `osd_memory_target` |
| [Small production](../scales/small-production.md) | 自动扩缩、三副本 |
| [Large production](../scales/large-production.md) | mClock、设备类 |
| [Multisite](../scales/multisite.md) | 各站点 CRUSH |

## 故障排查

[cli/troubleshooting.md](../../cli/troubleshooting.md)

[← 指南概览](../OVERVIEW.md)
