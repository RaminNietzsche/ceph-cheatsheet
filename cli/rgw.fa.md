# دستورات RGW (S3)

**ابزار:** `radosgw-admin` · دیمن gateway: cephadm (`ceph orch …`) یا unit file.

Placeholderها با `<>` — نام flagها را ترجمه نکنید. [راهنمای سبک CLI](../guides/cli-style-guide.md)

## کاربر و کلید <span class="badge badge-action-create">ایجاد</span> <span class="badge badge-action-read">خواندن</span>

| دستور / flag | کاربرد | مثال |
| --- | --- | --- |
| `user list` | فهرست کاربران | `radosgw-admin user list` |
| `user info --uid=<user_id>` | اطلاعات یک کاربر | `--uid=john_doe` |
| `user create` | ایجاد کاربر S3 | `--uid=<user_id> --display-name="<display_name>"` |
| `user suspend` | تعلیق دسترسی | `--uid=<user_id>` |

```bash
radosgw-admin user list
radosgw-admin user info --uid=<user_id>
radosgw-admin user create \
  --uid="<user_id>" \
  --display-name="<display_name>"
radosgw-admin user suspend --uid=<user_id>
radosgw-admin user enable --uid=<user_id>
```

??? example "نمونه خروجی JSON — user info"
    ```json
    {
      "user_id": "john_doe",
      "display_name": "John Doe",
      "suspended": 0
    }
    ```

## Bucket و quota <span class="badge badge-action-quota">Quota</span>

| دستور / flag | کاربرد | مثال |
| --- | --- | --- |
| `bucket stats --bucket=<bucket_name>` | آمار bucket | `--bucket=my-data` |
| `quota set --quota-scope=user` | تنظیم سقف | `--max-size=<bytes>` |

```bash
radosgw-admin bucket list
radosgw-admin bucket stats --bucket=<bucket_name>
radosgw-admin quota set \
  --quota-scope=user \
  --uid=<user_id> \
  --max-size=<bytes>
```

## چندسایته <span class="badge badge-action-sync">Sync</span>

```bash
radosgw-admin realm list
radosgw-admin period update --commit
radosgw-admin sync status
```

## عملیات gateway

```bash
radosgw-admin gc list|process
radosgw-admin bi list --bucket=<bucket_name>
```

## مثال S3 CLI

```bash
aws s3 ls --endpoint-url http://<rgw_host>
aws s3 cp <local_file> s3://<bucket_name>/<key> \
  --endpoint-url http://<rgw_host>
```

## گزینه‌های config

[config/rgw](../config/rgw/INDEX.md): `rgw_frontends`, `rgw_dns_name`, `rgw_zone`.

[← نمای کلی CLI](OVERVIEW.md)
