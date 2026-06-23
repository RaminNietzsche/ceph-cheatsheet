# مقیاس Multisite

<span class="badge badge-scale-multi">Multisite</span> چند datacenter یا region — zoneهای RGW، mirroring اختیاری RBD / CephFS.

## الگوها

| کاربرد | اجزا |
|--------|------|
| S3 چندسایته | realm → zonegroup → zone، `period update` |
| DR بلوک | RBD mirroring |
| DR CephFS | cephfs-mirror |

## RGW multisite

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

## RBD mirror

```bash
rbd mirror pool enable rbd image
rbd mirror pool status rbd
rbd mirror image promote rbd/image --force
```

## CephFS mirror

```bash
ceph fs snapshot mirror enable myfs
ceph fs snapshot mirror info myfs
```

## راهنمای نقش

[rgw-admin.md](../roles/rgw-admin.md) · [cephfs-admin.md](../roles/cephfs-admin.md)

## هشدار

- latency بین سایت‌ها روی sync RGW اثر دارد
- failover را در پنجره نگهداری تست کنید

[← نمای کلی راهنما](../OVERVIEW.md)
