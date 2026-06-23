# RGW 管理员

<span class="badge badge-role-rgw">RGW 管理员</span> 管理 RADOS Gateway — S3/Swift、用户、bucket、配额与多站点。

## 日常命令

```bash
radosgw-admin user list
radosgw-admin bucket stats --bucket=mybucket
radosgw-admin quota get --quota-scope=user --uid=user1
radosgw-admin sync status
ceph orch ps --service-type rgw
ceph config show client.rgw.<instance>
```

[RGW CLI](../../cli/rgw.md) · [RGW 故障排查](../../cli/troubleshooting.md)

## 配置

完整索引：[config/rgw/INDEX.md](../../config/rgw/INDEX.md)

| 主题 | 深度指南 |
|------|----------|
| 前端与 HTTP | [frontends.md](../rgw-config/core-gateway/frontends.md) |
| 多站点 | [multisite-zones.md](../rgw-config/multisite/multisite-zones.md) |
| 安全与加密 | [encryption.md](../rgw-config/security-auth/encryption.md) |
| 配额 | [quotas.md](../rgw-config/tenants-quotas/quotas.md) |
| 全部选项 | [OVERVIEW](../rgw-config/OVERVIEW.md) · [TUNING](../rgw-config/TUNING.md) |

```bash
./scripts/lookup-config.sh rgw_cache_enabled
./scripts/search-config.sh -s rgw multisite
```

## 常见工作流

**创建用户：**

```bash
radosgw-admin user create --uid=alice --display-name="Alice"
radosgw-admin key create --uid=alice --key-type=s3 --gen-access-key --gen-secret
```

**多站点 period 更新：**

```bash
radosgw-admin period update --commit
radosgw-admin sync status
```

**部署 RGW（cephadm）：**

```bash
ceph orch apply rgw myrgw --placement="2 host1 host2" --port=8080
```

## 规模说明

| 规模 | 重点 |
|------|------|
| [小型生产](../scales/small-production.md) | 单 zone、本地缓存 |
| [多站点](../scales/multisite.md) | realm/zone、同步延迟 |
| [大型生产](../scales/large-production.md) | 多 RGW、缓存调优 |

[← 指南概览](../OVERVIEW.md)
