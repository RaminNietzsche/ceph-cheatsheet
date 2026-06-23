# مدیر RGW

<span class="badge badge-role-rgw">مدیر RGW</span> مدیریت RADOS Gateway — S3/Swift، کاربران، bucket، quota و چندسایته.

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

**فهرست:** [config/rgw/INDEX.md](../../config/rgw/INDEX.md)

| موضوع | راهنمای عمیق |
|-------|-----------|
| Frontend و HTTP | [frontends.md](../rgw-config/core-gateway/frontends.md) |
| چندسایته | [multisite-zones.md](../rgw-config/multisite/multisite-zones.md) |
| امنیت و رمزنگاری | [encryption.md](../rgw-config/security-auth/encryption.md) |
| سهمیه (quota) | [quotas.md](../rgw-config/tenants-quotas/quotas.md) |
| همه گزینه‌ها | [OVERVIEW](../rgw-config/OVERVIEW.md) · [TUNING](../rgw-config/TUNING.md) |

```bash
./scripts/lookup-config.sh rgw_cache_enabled
./scripts/search-config.sh -s rgw multisite
```

## روندهای کاری رایج

**ایجاد کاربر:**

```bash
radosgw-admin user create --uid=alice --display-name="Alice"
radosgw-admin key create --uid=alice --key-type=s3 --gen-access-key --gen-secret
```

**به‌روزرسانی period چندسایته:**

```bash
radosgw-admin period update --commit
radosgw-admin sync status
```

**استقرار RGW (cephadm):**

```bash
ceph orch apply rgw myrgw --placement="2 host1 host2" --port=8080
```

## یادداشت مقیاس

| مقیاس | تمرکز |
|-------|--------|
| [محیط عملیاتی کوچک](../scales/small-production.md) | یک zone، cache محلی |
| [چندسایته](../scales/multisite.md) | realm/zone، تأخیر sync |
| [محیط عملیاتی بزرگ](../scales/large-production.md) | چند RGW، تنظیم cache |

[← نمای کلی راهنما](../OVERVIEW.md)
