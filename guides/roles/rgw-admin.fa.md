# مدیر RGW

<span class="badge badge-role-rgw">RGW admin</span> مدیریت RADOS Gateway — S3/Swift، کاربران، bucket، quota و multisite.

## دستورات روزانه

```bash
radosgw-admin user list
radosgw-admin bucket stats --bucket=mybucket
radosgw-admin quota get --quota-scope=user --uid=user1
radosgw-admin sync status
ceph orch ps --service-type rgw
ceph config show client.rgw.<instance>
```

[CLI RGW](../../cli/rgw.md) · [عیب‌یابی RGW](../../cli/troubleshooting.md)

## پیکربندی

INDEX: [config/rgw/INDEX.md](../../config/rgw/INDEX.md)

| موضوع | deep dive |
|-------|-----------|
| Frontends | [frontends.md](../rgw-config/core-gateway/frontends.md) |
| Multisite | [multisite-zones.md](../rgw-config/multisite/multisite-zones.md) |
| رمزنگاری | [encryption.md](../rgw-config/security-auth/encryption.md) |
| Quota | [quotas.md](../rgw-config/tenants-quotas/quotas.md) |
| همه گزینه‌ها | [OVERVIEW](../rgw-config/OVERVIEW.md) · [TUNING](../rgw-config/TUNING.md) |

```bash
./scripts/lookup-config.sh rgw_cache_enabled
./scripts/search-config.sh -s rgw multisite
```

## workflowهای رایج

```bash
radosgw-admin user create --uid=alice --display-name="Alice"
radosgw-admin key create --uid=alice --key-type=s3 --gen-access-key --gen-secret
radosgw-admin period update --commit
radosgw-admin sync status
ceph orch apply rgw myrgw --placement="2 host1 host2" --port=8080
```

## یادداشت مقیاس

| مقیاس | تمرکز |
|-------|--------|
| [Small production](../scales/small-production.md) | یک zone |
| [Multisite](../scales/multisite.md) | realm/zone، lag |
| [Large production](../scales/large-production.md) | چند RGW، cache |

[← نمای کلی راهنما](../OVERVIEW.md)
