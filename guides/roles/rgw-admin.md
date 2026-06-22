# RGW Admin

Manage RADOS Gateway — S3/Swift, users, buckets, quotas, and multisite.

## Daily commands

```bash
radosgw-admin user list
radosgw-admin bucket stats --bucket=mybucket
radosgw-admin quota get --quota-scope=bucket --uid=user1
ceph orch ps --service-type rgw
```

See [RGW CLI](../../cli/rgw.md).

## Configuration

Full index: [config/rgw/INDEX.md](../../config/rgw/INDEX.md)

| Topic | Options (lookup) |
|-------|------------------|
| Frontends | `rgw_frontends`, `rgw_dns_name` |
| Cache | `rgw_cache_enabled`, `rgw_cache_lru_size` |
| Multisite | `rgw_zone`, `rgw_zonegroup`, realm/period OIDs |
| Encryption | `rgw_crypt_*`, `rgw_crypt_s3_kms_backend` |
| Quota | `rgw_bucket_default_quota_*` |

```bash
./scripts/lookup-config.sh rgw_cache_enabled
./scripts/search-config.sh -s rgw multisite
```

## Common workflows

**Create user and bucket (admin):**

```bash
radosgw-admin user create --uid=alice --display-name="Alice"
radosgw-admin key create --uid=alice --key-type=s3 --gen-access-key --gen-secret
```

**Multisite period update:**

```bash
radosgw-admin period update --commit
radosgw-admin sync status
```

**Deploy RGW (cephadm):**

```bash
ceph orch apply rgw myrgw --placement="2 host1 host2" --port=8080
```

## Scale notes

- [Small production](../scales/small-production.md) — single zone, local cache
- [Multisite](../scales/multisite.md) — realms, zones, data sync
- [Large production](../scales/large-production.md) — many RGW instances, cache tuning

[← Guides overview](../OVERVIEW.md)
