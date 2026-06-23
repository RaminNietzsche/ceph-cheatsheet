# 实验室 / 开发规模

<span class="badge badge-scale-lab">实验室 / 开发</span> 1–3 节点，测试、学习与 CI — **不用于生产数据**。

## 目标

- 最小 footprint、快速迭代
- 可接受单点故障
- 仅在隔离 lab 网络放宽 durability

## 建议布局

```bash
cephadm bootstrap --mon-ip <ip> --single-host-defaults
ceph orch apply mon --placement="1"
ceph orch apply mgr --placement="1"
ceph orch apply osd --all-available-devices
```

## 调优提示

| 领域 | Lab 做法 |
|------|----------|
| 副本 | 单主机 `--single-host-defaults` 下 `size=2` |
| PG | 自动扩缩；小池 |
| OSD 内存 | RAM 受限时降低 `osd_memory_target` |
| Scrub | 延长间隔以减少磁盘压力 |

```bash
./scripts/lookup-config.sh osd_memory_target
./scripts/lookup-config.sh osd_pool_default_pg_autoscale_mode
```

## 角色指南

| 角色 | 指南 |
|------|------|
| 集群 | [cluster-admin.md](../roles/cluster-admin.md) |
| 存储 | [storage-operator.md](../roles/storage-operator.md) |
| RGW（可选） | [rgw-admin.md](../roles/rgw-admin.md) |
| CephFS（可选） | [cephfs-admin.md](../roles/cephfs-admin.md) |

## CLI 速查

[cli/cluster.md](../../cli/cluster.md) · [cli/osd-pool.md](../../cli/osd-pool.md)

[← 指南概览](../OVERVIEW.md)
