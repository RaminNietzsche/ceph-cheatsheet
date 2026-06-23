# RGW (S3) 命令

RGW 管理使用 `radosgw-admin`。网关守护进程通过 cephadm（`ceph orch …`）或 unit 文件管理。

## 用户与密钥

```bash
radosgw-admin user list
radosgw-admin user info --uid=<uid>
radosgw-admin user create --uid=<uid> --display-name="Name"
radosgw-admin user rm --uid=<uid>
radosgw-admin user modify --uid=<uid> --email=… --max-buckets=…
radosgw-admin user suspend --uid=<uid>
radosgw-admin user enable --uid=<uid>

radosgw-admin key create --uid=<uid> --key-type=s3 --access-key=… --secret-key=…
radosgw-admin key rm --uid=<uid> --access-key=…
```

## Bucket 与配额

```bash
radosgw-admin bucket list
radosgw-admin bucket stats --bucket=<name>
radosgw-admin bucket rm --bucket=<name>
radosgw-admin bucket link --bucket=<name> --uid=<uid>
radosgw-admin bucket unlink --bucket=<name> --uid=<uid>

radosgw-admin quota set --quota-scope=user|bucket --uid=<uid> [--max-size=…] [--max-objects=…]
radosgw-admin quota get --quota-scope=user|bucket --uid=<uid>
radosgw-admin quota enable --quota-scope=user|bucket --uid=<uid>
```

## 多站点（realm / zone / zonegroup）

```bash
radosgw-admin realm list
radosgw-admin realm create --rgw-realm=<name> --default
radosgw-admin zonegroup create --rgw-zonegroup=<name> --master --default
radosgw-admin zone create --rgw-zonegroup=<zg> --rgw-zone=<zone> --master --default
radosgw-admin period update --commit
radosgw-admin period pull --url=http://<master>:80 --access-key=… --secret-key=…
radosgw-admin sync status
radosgw-admin metadata sync status
radosgw-admin data sync status
```

## 网关操作

```bash
radosgw-admin gc list|process
radosgw-admin bi list --bucket=<name>
radosgw-admin log list|show|rm
radosgw-admin datalog list|trim
radosgw-admin mdlog list|status
```

## S3 CLI 示例（awscli / s3cmd）

```bash
aws s3 ls --endpoint-url http://rgw.example.com
aws s3 mb s3://mybucket --endpoint-url http://rgw.example.com
aws s3 cp file s3://mybucket/key --endpoint-url http://rgw.example.com
```

## 常用配置选项

见 [config/rgw](../config/rgw/INDEX.md)：`rgw_frontends`、`rgw_dns_name`、`rgw_zone`、`rgw_cache_enabled`、`rgw_crypt_s3_kms_backend`。

[← CLI 概览](OVERVIEW.md)
