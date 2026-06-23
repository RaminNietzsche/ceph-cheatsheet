# RGW (S3) 命令

**管理工具：** `radosgw-admin` · 网关守护进程：cephadm（`ceph orch …`）或 unit 文件。

占位符使用 `<尖括号>` — 不要翻译 flag 名称。见 [CLI 风格指南](../guides/cli-style-guide.md) · [术语表](../guides/i18n-glossary.md)

## 用户与密钥 <span class="badge badge-action-create">创建</span> <span class="badge badge-action-read">读取</span> <span class="badge badge-action-delete">删除</span>

| 命令 / flag | 用途 | 示例 |
| --- | --- | --- |
| `user list` | 列出 RGW 用户 | `radosgw-admin user list` |
| `user info --uid=<user_id>` | 查看单个用户 | `--uid=john_doe` |
| `user create` | 创建 S3 用户 | `--uid=<user_id> --display-name="<display_name>"` |
| `user rm --uid=<user_id>` | 删除用户 | `--uid=john_doe` |
| `user suspend` | 暂停访问 | `--uid=<user_id>` |
| `user enable` | 重新启用 | `--uid=<user_id>` |
| `key create` | 添加 S3 密钥 | `--uid=<user_id> --key-type=s3` |

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

??? example "示例 `user info` JSON 输出"
    ```json
    {
      "user_id": "john_doe",
      "display_name": "John Doe",
      "email": "john@example.com",
      "suspended": 0,
      "max_buckets": 1000
    }
    ```

## Bucket 与配额 <span class="badge badge-action-quota">Quota</span> <span class="badge badge-action-delete">删除</span>

| 命令 / flag | 用途 | 示例 |
| --- | --- | --- |
| `bucket list` | 列出 bucket | `radosgw-admin bucket list` |
| `bucket stats --bucket=<bucket_name>` | 用量统计 | `--bucket=my-data` |
| `bucket rm --bucket=<bucket_name>` | 删除 bucket | `--bucket=my-data` |
| `bucket link --bucket=<bucket_name> --uid=<user_id>` | 指定所有者 | 孤儿 bucket |
| `quota set --quota-scope=user\|bucket` | 设置限额 | `--max-size=<bytes>` |

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

??? example "示例 `bucket stats` JSON 输出"
    ```json
    {
      "bucket": "my-data",
      "num_shards": 11,
      "usage": {
        "rgw.main": { "size": 1073741824, "num_objects": 42 }
      }
    }
    ```

## 多站点（realm / zone / zonegroup） <span class="badge badge-action-sync">Sync</span>

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

??? example "示例 `sync status` 输出（截断）"
    ```json
    {
      "summary": "sync status",
      "meta_sync": { "sync_status": "complete" },
      "data_sync": { "sync_status": "complete" }
    }
    ```

## 网关操作 <span class="badge badge-action-read">读取</span>

```bash
radosgw-admin gc list
radosgw-admin gc process
radosgw-admin bi list --bucket=<bucket_name>
radosgw-admin log list
radosgw-admin log show --object=<object_id>
radosgw-admin datalog list
radosgw-admin mdlog list
```

## S3 CLI 示例（awscli / s3cmd）

```bash
aws s3 ls --endpoint-url http://<rgw_host>
aws s3 mb s3://<bucket_name> --endpoint-url http://<rgw_host>
aws s3 cp <local_file> s3://<bucket_name>/<object_key> \
  --endpoint-url http://<rgw_host>
```

## 常用配置选项

见 [config/rgw](../config/rgw/INDEX.md)：`rgw_frontends`、`rgw_dns_name`、`rgw_zone`、`rgw_cache_enabled`、`rgw_crypt_s3_kms_backend`。

[← CLI 概览](OVERVIEW.md)
