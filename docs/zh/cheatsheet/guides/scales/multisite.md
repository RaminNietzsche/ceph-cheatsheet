# 多站点规模

<span class="badge badge-scale-multi">多站点</span> 多数据中心或区域 — RGW zone、可选 RBD / CephFS 镜像。

## 模式

| 用例 | 组件 |
|------|------|
| S3 地理分布 | realm → zonegroup → zone、`period update` |
| 块存储 DR | RBD mirroring |
| CephFS DR | cephfs-mirror |

## RGW 多站点

```bash
radosgw-admin realm list
radosgw-admin sync status
radosgw-admin period update --commit
ceph config get client.rgw rgw_zone
```

CLI：[cli/rgw.md](../../cli/rgw.md)  
配置：[config/rgw/INDEX.md](../../config/rgw/INDEX.md)  
深度指南：[multisite-zones.md](../rgw-config/multisite/multisite-zones.md) · [multisite-sync.md](../rgw-config/multisite/multisite-sync.md)

```bash
./scripts/search-config.sh -s rgw zone
```

## RBD 镜像

```bash
rbd mirror pool enable rbd image
rbd mirror pool status rbd
rbd mirror image promote rbd/image --force
```

配置：[config/rbd-mirror/INDEX.md](../../config/rbd-mirror/INDEX.md)

## CephFS 镜像

```bash
ceph fs snapshot mirror enable myfs
ceph fs snapshot mirror info myfs
```

配置：[config/cephfs-mirror/INDEX.md](../../config/cephfs-mirror/INDEX.md)

## 角色指南

| 角色 | 指南 |
|------|------|
| RGW 多站点 | [rgw-admin.md](../roles/rgw-admin.md) |
| CephFS 灾备 | [cephfs-admin.md](../roles/cephfs-admin.md) |
| 集群 / Mon | [cluster-admin.md](../roles/cluster-admin.md) |

## 注意

- 站点间延迟影响 RGW 同步与 RBD journal 延迟
- 在维护窗口测试 failover（`promote`）
- 为多站点 erasure 规划各站点的 CRUSH 与池

[← 指南概览](../OVERVIEW.md)

## RGW 多站点模型（docs-extended）

来自 [部署架构](../../../arch/rgw/architecture/deployment-architecture.md) 与 [运行时拓扑](../../../arch/rgw/architecture/runtime-topology.md)：

| 概念 | 作用 |
|------|------|
| **Realm** | 配置命名空间 |
| **Period** | 配置 epoch 版本 |
| **Zone** | 带本地 pool 的地理站点 |
| **Sync** | 区域间 HTTP 上的 metadata log + 数据同步 |

每个 zone 运行独立的 RGW 集群；实例无状态 — 通过 RADOS 与多站点协调。

深度阅读：[Multisite 模块](../../../arch/rgw/modules/multisite.md) · [阶段 7 — 多站点](../../../arch/rgw/learning-program/08-phase-7-multisite.md)
