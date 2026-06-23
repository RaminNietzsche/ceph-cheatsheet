# Multisite example

RGW **realm → zonegroup → zones** across datacenters. Each zone has local pools and RGW fleet.

## Concepts

| Object | Role |
|--------|------|
| Realm | Configuration namespace |
| Period | Epoch version of multisite config |
| Zone | Site with local placement pools |
| Zonegroup | Group of zones in one realm |

## Per-zone RGW settings

```ini
[client.rgw.zone-a]
rgw_zone = zone-a
rgw_zonegroup = mygroup
rgw_realm = myrealm
rgw_run_sync_thread = true

[client.rgw.zone-b]
rgw_zone = zone-b
rgw_zonegroup = mygroup
rgw_realm = myrealm
rgw_run_sync_thread = true
```

## Setup workflow (summary)

```bash
# On primary zone
radosgw-admin realm create --rgw-realm=myrealm --default
radosgw-admin zonegroup create --rgw-zonegroup=mygroup --master --default
radosgw-admin zone create --rgw-zonegroup=mygroup --rgw-zone=zone-a --master --default
radosgw-admin period update --commit

# Secondary zone — pull period, create local zone
radosgw-admin realm pull --url=http://primary:8080 --access-key=... --secret=...
radosgw-admin zone create --rgw-zonegroup=mygroup --rgw-zone=zone-b
radosgw-admin period update --commit
```

## Monitoring

```bash
radosgw-admin sync status
radosgw-admin sync error list
```

## CRUSH / pools

- Separate CRUSH rules per site when possible
- Plan erasure coding vs replication per zone policy
- Test failover (`period update`, promote) in maintenance windows

See [Multisite scale guide](../../guides/scales/multisite.md) · [Multisite module](../../../arch/rgw/modules/multisite.md).

[← Examples overview](OVERVIEW.md)
