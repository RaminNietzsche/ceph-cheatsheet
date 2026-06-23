# مقیاس چندسایته

<span class="badge badge-scale-multi">چندسایته</span> چند datacenter یا region — zoneهای RGW، mirroring اختیاری RBD / CephFS.

## الگوها

| کاربرد | اجزا |
|--------|------|
| S3 چندسایته | realm → zonegroup → zone، `period update` |
| DR بلوک | RBD mirroring |
| DR CephFS | cephfs-mirror |

## RGW چندسایته

```bash
radosgw-admin realm list
radosgw-admin sync status
radosgw-admin period update --commit
ceph config get client.rgw rgw_zone
```

CLI: [cli/rgw.md](../../cli/rgw.md)  
Config: [config/rgw/INDEX.md](../../config/rgw/INDEX.md)  
راهنمای عمیق: [multisite-zones.md](../rgw-config/multisite/multisite-zones.md) · [multisite-sync.md](../rgw-config/multisite/multisite-sync.md)

```bash
./scripts/search-config.sh -s rgw zone
```

## RBD mirror

```bash
rbd mirror pool enable rbd image
rbd mirror pool status rbd
rbd mirror image promote rbd/image --force
```

Config: [config/rbd-mirror/INDEX.md](../../config/rbd-mirror/INDEX.md)

## CephFS mirror

```bash
ceph fs snapshot mirror enable myfs
ceph fs snapshot mirror info myfs
```

Config: [config/cephfs-mirror/INDEX.md](../../config/cephfs-mirror/INDEX.md)

## راهنمای نقش

| نقش | راهنما |
|------|--------|
| RGW چندسایته | [rgw-admin.md](../roles/rgw-admin.md) |
| DR CephFS | [cephfs-admin.md](../roles/cephfs-admin.md) |
| Cluster / mon | [cluster-admin.md](../roles/cluster-admin.md) |

## هشدارها

- latency بین سایت‌ها روی sync RGW و lag journal RBD اثر دارد
- failover (`promote`) را در پنجره نگهداری تست کنید
- CRUSH و pool را برای erasure + چندسایته برنامه‌ریزی کنید

[← نمای کلی راهنما](../OVERVIEW.md)

## مدل multisite RGW (docs-extended)

از [معماری استقرار](../../../arch/rgw/architecture/deployment-architecture.md) و [توپولوژی زمان اجرا](../../../arch/rgw/architecture/runtime-topology.md):

| مفهوم | نقش |
|-------|------|
| **Realm** | فضای نام پیکربندی |
| **Period** | نسخه epoch پیکربندی |
| **Zone** | سایت با poolهای محلی |
| **Sync** | metadata log + data sync روی HTTP بین زون‌ها |

هر zone fleet RGW خود را دارد؛ نمونه‌ها stateless — هماهنگی از RADOS و multisite.

راهنمای عمیق: [ماژول multisite](../../../arch/rgw/modules/multisite.md) · [فاز ۷ — Multisite](../../../arch/rgw/learning-program/08-phase-7-multisite.md)
