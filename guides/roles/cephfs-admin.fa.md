# مدیر CephFS

<span class="badge badge-role-cephfs">مدیر CephFS</span> مدیریت فایل‌سیستم Ceph، سرورهای متاداده (MDS)، subvolume و mirroring.

## دستورات روزانه

```bash
ceph fs ls
ceph fs status myfs
ceph mds stat
ceph orch ps --service-type mds
```

[CLI CephFS](../../cli/cephfs.md)

## پیکربندی

| حوزه | فهرست پیکربندی |
|------|-------|
| دیمن MDS | [config/mds/INDEX.md](../../config/mds/INDEX.md) · [راهنمای عمیق MDS](../mds-config/OVERVIEW.md) |
| Client / FUSE | [mds-client/INDEX.md](../../config/mds-client/INDEX.md) · [راهنمای عمیق client](../mds-client-config/OVERVIEW.md) |
| CephFS mirror | [cephfs-mirror/INDEX.md](../../config/cephfs-mirror/INDEX.md) · [راهنمای عمیق mirror](../cephfs-mirror-config/OVERVIEW.md) |

گزینه‌های کلیدی: `mds_cache_memory_limit`، `mds_max_file_size` — [TUNING MDS](../mds-config/TUNING.md)

```bash
./scripts/lookup-config.sh mds_cache_memory_limit
```

## روندهای کاری رایج

**ایجاد فایل‌سیستم:**

```bash
ceph osd pool create cephfs-metadata 32 32
ceph osd pool create cephfs-data 128 128
ceph fs new myfs cephfs-metadata cephfs-data
ceph orch apply mds myfs --placement="2"
```

**Subvolume:**

```bash
ceph fs subvolume create myfs vol1 --size 10737418240
ceph fs subvolume info myfs vol1
```

**Mirroring snapshot:**

```bash
ceph fs snapshot mirror enable myfs
```

## یادداشت مقیاس

| مقیاس | تمرکز |
|-------|--------|
| [آزمایشگاه](../scales/lab.md) | ۱ MDS، cache کوچک |
| [محیط عملیاتی کوچک](../scales/small-production.md) | ۲ MDS برای HA |
| [چندسایته](../scales/multisite.md) | cephfs-mirror برای DR |

[← نمای کلی راهنما](../OVERVIEW.md)
