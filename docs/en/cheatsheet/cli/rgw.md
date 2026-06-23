# RGW (S3) Commands

**Admin tool:** `radosgw-admin` · Gateway daemons: cephadm (`ceph orch …`) or unit files.

Placeholders use `<angle_brackets>` — never translate flag names. See [CLI style guide](../guides/cli-style-guide.md).

## Users & keys <span class="badge badge-action-create">Create</span> <span class="badge badge-action-read">Read</span>

| Command / flag | Purpose | Example |
| --- | --- | --- |
| `user list` | List all RGW users | `radosgw-admin user list` |
| `user info --uid=<user_id>` | Show one user | `--uid=john_doe` |
| `user create` | Create S3 user | `--uid=<user_id> --display-name="<display_name>"` |
| `user rm --uid=<user_id>` | Delete user | `--uid=john_doe` |
| `user suspend` | Disable user access | `--uid=<user_id>` |
| `user enable` | Re-enable suspended user | `--uid=<user_id>` |
| `key create` | Add S3 access key | `--uid=<user_id> --key-type=s3` |

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

??? example "Sample `user info` JSON output"
    ```json
    {
      "user_id": "john_doe",
      "display_name": "John Doe",
      "email": "john@example.com",
      "suspended": 0,
      "max_buckets": 1000
    }
    ```

## Buckets & quotas <span class="badge badge-action-quota">Quota</span> <span class="badge badge-action-delete">Delete</span>

| Command / flag | Purpose | Example |
| --- | --- | --- |
| `bucket list` | List buckets | `radosgw-admin bucket list` |
| `bucket stats --bucket=<bucket_name>` | Bucket usage stats | `--bucket=my-data` |
| `bucket rm --bucket=<bucket_name>` | Remove bucket | `--bucket=my-data` |
| `bucket link --bucket=<bucket_name> --uid=<user_id>` | Assign bucket owner | link orphan bucket |
| `quota set --quota-scope=user\|bucket` | Set size/object limits | `--max-size=<bytes>` |

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

??? example "Sample `bucket stats` JSON output"
    ```json
    {
      "bucket": "my-data",
      "num_shards": 11,
      "usage": {
        "rgw.main": { "size": 1073741824, "num_objects": 42 }
      }
    }
    ```

## Multisite (realm / zone / zonegroup) <span class="badge badge-action-sync">Sync</span>

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

??? example "Sample `sync status` output (truncated)"
    ```json
    {
      "summary": "sync status",
      "meta_sync": { "sync_status": "complete" },
      "data_sync": { "sync_status": "complete" }
    }
    ```

## Gateway ops <span class="badge badge-action-read">Read</span>

```bash
radosgw-admin gc list
radosgw-admin gc process
radosgw-admin bi list --bucket=<bucket_name>
radosgw-admin log list
radosgw-admin log show --object=<object_id>
radosgw-admin datalog list
radosgw-admin mdlog list
```

## S3 CLI examples (awscli / s3cmd)

```bash
aws s3 ls --endpoint-url http://<rgw_host>
aws s3 mb s3://<bucket_name> --endpoint-url http://<rgw_host>
aws s3 cp <local_file> s3://<bucket_name>/<object_key> \
  --endpoint-url http://<rgw_host>
```

## Useful config options

See [config/rgw](../config/rgw/INDEX.md): `rgw_frontends`, `rgw_dns_name`, `rgw_zone`, `rgw_cache_enabled`, `rgw_crypt_s3_kms_backend`.

[← CLI overview](OVERVIEW.md)
