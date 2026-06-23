# دستورات RGW (S3)

**ابزار:** `radosgw-admin` · دیمن gateway: cephadm (`ceph orch …`) یا unit file.

Placeholderها با `<>` — نام flagها را ترجمه نکنید. [راهنمای سبک CLI](../guides/cli-style-guide.md) · [واژه‌نامه](../guides/i18n-glossary.md)

## کاربر و کلید <span class="badge badge-action-create">ایجاد</span> <span class="badge badge-action-read">خواندن</span> <span class="badge badge-action-delete">حذف</span>

| دستور / flag | کاربرد | مثال |
| --- | --- | --- |
| `user list` | فهرست کاربران RGW | `radosgw-admin user list` |
| `user info --uid=<user_id>` | اطلاعات یک کاربر | `--uid=john_doe` |
| `user create` | ایجاد کاربر S3 | `--uid=<user_id> --display-name="<display_name>"` |
| `user rm --uid=<user_id>` | حذف کاربر | `--uid=john_doe` |
| `user suspend` | تعلیق دسترسی | `--uid=<user_id>` |
| `user enable` | فعال‌سازی مجدد | `--uid=<user_id>` |
| `key create` | افزودن کلید S3 | `--uid=<user_id> --key-type=s3` |

```bash
radosgw-admin user list
radosgw-admin user info --uid=<user_id>
radosgw-admin user create \
  --uid="<user_id>" \
  --display-name="<display_name>" \
  --email="<email>"
radosgw-admin user rm --uid=<user_id>
radosgw-admin user suspend --uid=<user_id>
radosgw-admin user enable --uid=<user_id>

radosgw-admin key create \
  --uid=<user_id> \
  --key-type=s3 \
  --access-key=<access_key> \
  --secret-key=<secret_key>
radosgw-admin key rm --uid=<user_id> --access-key=<access_key>
```

??? example "نمونه خروجی JSON — user info"
    ```json
    {
      "user_id": "john_doe",
      "display_name": "John Doe",
      "email": "john@example.com",
      "suspended": 0,
      "max_buckets": 1000
    }
    ```

## Bucket و quota <span class="badge badge-action-quota">Quota</span> <span class="badge badge-action-delete">حذف</span>

| دستور / flag | کاربرد | مثال |
| --- | --- | --- |
| `bucket list` | فهرست bucketها | `radosgw-admin bucket list` |
| `bucket stats --bucket=<bucket_name>` | آمار مصرف | `--bucket=my-data` |
| `bucket rm --bucket=<bucket_name>` | حذف bucket | `--bucket=my-data` |
| `bucket link --bucket=<bucket_name> --uid=<user_id>` | انتساب مالک | bucket یتیم |
| `quota set --quota-scope=user\|bucket` | تنظیم سقف | `--max-size=<bytes>` |

```bash
radosgw-admin bucket list
radosgw-admin bucket stats --bucket=<bucket_name>
radosgw-admin bucket rm --bucket=<bucket_name>
radosgw-admin bucket link --bucket=<bucket_name> --uid=<user_id>
radosgw-admin bucket unlink --bucket=<bucket_name> --uid=<user_id>

radosgw-admin quota set \
  --quota-scope=user \
  --uid=<user_id> \
  --max-size=<bytes> \
  --max-objects=<count>
radosgw-admin quota get --quota-scope=user --uid=<user_id>
radosgw-admin quota enable --quota-scope=user --uid=<user_id>
```

??? example "نمونه خروجی JSON — bucket stats"
    ```json
    {
      "bucket": "my-data",
      "num_shards": 11,
      "usage": {
        "rgw.main": { "size": 1073741824, "num_objects": 42 }
      }
    }
    ```

## چندسایته (realm / zone / zonegroup) <span class="badge badge-action-sync">Sync</span>

```bash
radosgw-admin realm list
radosgw-admin realm create --rgw-realm=<realm_name> --default
radosgw-admin zonegroup create --rgw-zonegroup=<zonegroup_name> --master --default
radosgw-admin zone create \
  --rgw-zonegroup=<zonegroup_name> \
  --rgw-zone=<zone_name> \
  --master --default
radosgw-admin period update --commit
radosgw-admin period pull \
  --url=http://<master_host>:80 \
  --access-key=<access_key> \
  --secret-key=<secret_key>
radosgw-admin sync status
radosgw-admin metadata sync status
radosgw-admin data sync status
```

??? example "نمونه خروجی sync status (خلاصه)"
    ```json
    {
      "summary": "sync status",
      "meta_sync": { "sync_status": "complete" },
      "data_sync": { "sync_status": "complete" }
    }
    ```

## عملیات gateway <span class="badge badge-action-read">خواندن</span>

```bash
radosgw-admin gc list
radosgw-admin gc process
radosgw-admin bi list --bucket=<bucket_name>
radosgw-admin log list
radosgw-admin log show --object=<object_id>
radosgw-admin datalog list
radosgw-admin mdlog list
```

## مثال S3 CLI (awscli / s3cmd)

```bash
aws s3 ls --endpoint-url http://<rgw_host>
aws s3 mb s3://<bucket_name> --endpoint-url http://<rgw_host>
aws s3 cp <local_file> s3://<bucket_name>/<object_key> \
  --endpoint-url http://<rgw_host>
```

## گزینه‌های config پرکاربرد

[config/rgw](../config/rgw/INDEX.md): `rgw_frontends`، `rgw_dns_name`، `rgw_zone`، `rgw_cache_enabled`، `rgw_crypt_s3_kms_backend`.

[← نمای کلی CLI](OVERVIEW.md)
