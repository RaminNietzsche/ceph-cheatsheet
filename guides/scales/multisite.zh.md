# 多站点规模

<span class="badge badge-scale-multi">Multisite</span> 多数据中心或区域 — RGW zone、可选 RBD / CephFS 镜像。

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

[cli/rgw.md](../../cli/rgw.md) · [multisite-zones.md](../rgw-config/multisite/multisite-zones.md)

```bash
./scripts/search-config.sh -s rgw zone
```

## RBD 镜像

```bash
rbd mirror pool enable rbd image
rbd mirror pool status rbd
rbd mirror image promote rbd/image --force
```

## CephFS 镜像

```bash
ceph fs snapshot mirror enable myfs
ceph fs snapshot mirror info myfs
```

## 角色指南

[rgw-admin.md](../roles/rgw-admin.md) · [cephfs-admin.md](../roles/cephfs-admin.md)

## 注意

- 站点间延迟影响 RGW 同步与 RBD journal
- 在维护窗口测试 failover（`promote`）

[← 指南概览](../OVERVIEW.md)
