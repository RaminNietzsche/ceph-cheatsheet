# مدیر CephFS

<span class="badge badge-role-cephfs">CephFS admin</span> مدیریت فایل‌سیستم Ceph، MDS، subvolume و mirroring.

## دستورات روزانه

```bash
ceph fs ls
ceph fs status myfs
ceph mds stat
ceph orch ps --service-type mds
```

[CLI CephFS](../../cli/cephfs.md)

## پیکربندی

| حوزه | INDEX |
|------|-------|
| MDS | [config/mds/INDEX.md](../../config/mds/INDEX.md) · [deep dive](../mds-config/OVERVIEW.md) |
| Client | [mds-client/INDEX.md](../../config/mds-client/INDEX.md) · [deep dive](../mds-client-config/OVERVIEW.md) |
| Mirror | [cephfs-mirror/INDEX.md](../../config/cephfs-mirror/INDEX.md) · [deep dive](../cephfs-mirror-config/OVERVIEW.md) |

گزینه‌های کلیدی: `mds_cache_memory_limit` — [TUNING](../mds-config/TUNING.md)

```bash
./scripts/lookup-config.sh mds_cache_memory_limit
```

## workflowهای رایج

```bash
ceph osd pool create cephfs-metadata 32 32
ceph osd pool create cephfs-data 128 128
ceph fs new myfs cephfs-metadata cephfs-data
ceph orch apply mds myfs --placement="2"
ceph fs subvolume create myfs vol1 --size 10737418240
ceph fs snapshot mirror enable myfs
```

## یادداشت مقیاس

| مقیاس | تمرکز |
|-------|--------|
| [Lab](../scales/lab.md) | ۱ MDS |
| [Small production](../scales/small-production.md) | ۲ MDS برای HA |
| [Multisite](../scales/multisite.md) | cephfs-mirror |

[← نمای کلی راهنما](../OVERVIEW.md)
