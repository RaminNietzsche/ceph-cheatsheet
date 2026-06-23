# CephFS 管理员

<span class="badge badge-role-cephfs">CephFS 管理员</span> 管理 Ceph 文件系统、元数据服务器 (MDS)、子卷与镜像。

## 日常命令

```bash
ceph fs ls
ceph fs status myfs
ceph mds stat
ceph orch ps --service-type mds
```

[CephFS CLI](../../cli/cephfs.md)

## 配置

| 领域 | 配置索引 |
|------|----------|
| MDS | [config/mds/INDEX.md](../../config/mds/INDEX.md) · [深度指南](../mds-config/OVERVIEW.md) |
| Client | [mds-client/INDEX.md](../../config/mds-client/INDEX.md) · [深度指南](../mds-client-config/OVERVIEW.md) |
| Mirror | [cephfs-mirror/INDEX.md](../../config/cephfs-mirror/INDEX.md) · [深度指南](../cephfs-mirror-config/OVERVIEW.md) |

关键选项：`mds_cache_memory_limit` — [TUNING](../mds-config/TUNING.md)

```bash
./scripts/lookup-config.sh mds_cache_memory_limit
```

## 常见工作流

**创建文件系统：**

```bash
ceph osd pool create cephfs-metadata 32 32
ceph osd pool create cephfs-data 128 128
ceph fs new myfs cephfs-metadata cephfs-data
ceph orch apply mds myfs --placement="2"
```

**子卷：**

```bash
ceph fs subvolume create myfs vol1 --size 10737418240
ceph fs subvolume info myfs vol1
```

**快照镜像：**

```bash
ceph fs snapshot mirror enable myfs
```

## 规模说明

| 规模 | 重点 |
|------|------|
| [实验室](../scales/lab.md) | 1 个 MDS、小缓存 |
| [小型生产](../scales/small-production.md) | 2 个 MDS 高可用 |
| [多站点](../scales/multisite.md) | cephfs-mirror 灾备 |

[← 指南概览](../OVERVIEW.md)
