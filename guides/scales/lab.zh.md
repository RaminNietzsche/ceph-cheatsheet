# Lab / 开发规模

<span class="badge badge-scale-lab">Lab / dev</span> 1–3 节点，测试与学习 — **不用于生产数据**。

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
| OSD 内存 | 降低 `osd_memory_target` |
| Scrub | 延长间隔 |

```bash
./scripts/lookup-config.sh osd_memory_target
```

## 角色指南

| 角色 | 指南 |
|------|------|
| 集群 | [cluster-admin.md](../roles/cluster-admin.md) |
| 存储 | [storage-operator.md](../roles/storage-operator.md) |

[← 指南概览](../OVERVIEW.md)
