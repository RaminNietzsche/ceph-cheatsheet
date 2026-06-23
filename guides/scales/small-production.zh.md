# 小型生产规模

<span class="badge badge-scale-small">Small production</span> 通常 **3–12 节点**、单数据中心、**三副本**、cephadm 管理。

## 架构检查清单

- [ ] 3 个 Monitor 分布在不同主机
- [ ] 2 个 Manager（active + standby）
- [ ] 每盘一个 OSD
- [ ] 所有池开启 PG 自动扩缩
- [ ] 池设置 `application` 标签

## 日常运维

[quickstart.md](../quickstart.md) 与角色指南：

| 角色 | 指南 |
|------|------|
| 集群 | [cluster-admin.md](../roles/cluster-admin.md) |
| 存储 | [storage-operator.md](../roles/storage-operator.md) |
| RGW | [rgw-admin.md](../roles/rgw-admin.md) |
| CephFS | [cephfs-admin.md](../roles/cephfs-admin.md) |

## 关键配置

```bash
ceph config get mon osd_pool_default_pg_autoscale_mode
ceph config get mgr mon_target_pg_per_osd
ceph osd pool autoscale-status
```

深度指南：[OSD](../osd-config/OVERVIEW.md) · [MON](../mon-config/OVERVIEW.md)

## 容量规划

```bash
ceph df detail
ceph osd df tree
```

`nearfull` 前约 **70%** 可用容量。

[← 指南概览](../OVERVIEW.md)
