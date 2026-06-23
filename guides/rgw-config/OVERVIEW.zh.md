# RGW 配置深度指南 — 全部选项

全部 **441** 个 RGW 选项的扩展参考，含 **寻找最优值** 指南。由 [config/rgw/INDEX.md](../../config/rgw/INDEX.md) 生成。

```bash
./scripts/lookup-config.sh <option-name>
python3 scripts/generate-rgw-guide.py  # regenerate after config sync
```

## 调优

- [调优快速参考](TUNING.md) — all options, model, one-line answer

## 寻找最优值

| 模型 | 如何选择 |
|-------|---------------|
| **Policy** | 安全、API 兼容性、租户限制 |
| **Capacity** | 磁盘布局、路径、池容量 |
| **Performance** | 基线 → 逐步调整 → 监控 OSD/RGW |
| **Connectivity** | 最近且稳定的外部端点 |
| **Architecture** | 后端、多站点拓扑 — 非数值扫描 |
| **Dev** | 生产环境保持 upstream 默认值 |

## 按类别浏览


### Core gateway

| 主题 | 选项数 |
|-------|---------|
| [Frontends & HTTP stack](core-gateway/frontends.md) | 6 |
| [Feature toggles](core-gateway/feature-toggles.md) | 10 |
| [Scheduler & dmclock](core-gateway/scheduler-dmclock.md) | 13 |
| [HTTP compatibility](core-gateway/http-compat.md) | 17 |
| [Core runtime](core-gateway/core-runtime.md) | 16 |

### Performance & I/O

| 主题 | 选项数 |
|-------|---------|
| [Concurrency & RADOS I/O](performance-io/performance-tuning.md) | 14 |
| [Object read/write windows](performance-io/object-io.md) | 4 |
| [Multipart & copy](performance-io/multipart-copy.md) | 4 |
| [Metadata & object caches](performance-io/caching.md) | 4 |
| [Timeouts & intervals](performance-io/timeouts-intervals.md) | 8 |
| [Listing limits](performance-io/limits-listing.md) | 12 |

### Buckets & data lifecycle

| 主题 | 选项数 |
|-------|---------|
| [Bucket operations](buckets-lifecycle/bucket-ops.md) | 12 |
| [Bucket index & sharding](buckets-lifecycle/index-sharding.md) | 4 |
| [Dynamic resharding](buckets-lifecycle/resharding.md) | 12 |
| [Object expiry hints](buckets-lifecycle/object-expiry.md) | 2 |
| [Garbage collection](buckets-lifecycle/garbage-collection.md) | 7 |
| [Lifecycle (LC)](buckets-lifecycle/lifecycle.md) | 17 |

### Tenants & quotas

| 主题 | 选项数 |
|-------|---------|
| [Quota sync & defaults](tenants-quotas/quotas.md) | 5 |
| [Users & per-user settings](tenants-quotas/users-quotas.md) | 5 |

### Multisite

| 主题 | 选项数 |
|-------|---------|
| [Zones, realm & region](multisite/multisite-zones.md) | 19 |
| [Replication & sync](multisite/multisite-sync.md) | 28 |
| [REST connections](multisite/rest-connections.md) | 3 |

### Security & authentication

| 主题 | 选项数 |
|-------|---------|
| [Encryption & KMS](security-auth/encryption.md) | 43 |
| [Keystone & STS](security-auth/keystone-sts.md) | 32 |
| [LDAP](security-auth/ldap.md) | 6 |
| [OPA authorization](security-auth/opa-authz.md) | 4 |
| [Swift API](security-auth/swift.md) | 11 |
| [S3 API & auth](security-auth/s3-api.md) | 8 |

### Notifications

| 主题 | 选项数 |
|-------|---------|
| [Bucket notifications](notifications/notifications.md) | 13 |

### Logging & admin

| 主题 | 选项数 |
|-------|---------|
| [Access & object logging](logging-admin/logging.md) | 4 |
| [Ops logging](logging-admin/ops-logging.md) | 4 |
| [Usage logging](logging-admin/usage-logging.md) | 4 |
| [Admin CORS](logging-admin/admin-cors.md) | 4 |
| [API limits & policies](logging-admin/api-limits.md) | 6 |

### Extensions

| 主题 | 选项数 |
|-------|---------|
| [NFS gateway](extensions/nfs.md) | 14 |
| [Lua scripting](extensions/lua.md) | 4 |
| [BitTorrent](extensions/torrent.md) | 8 |
| [HTTP / libcurl](extensions/http-curl.md) | 5 |

### Experimental & debug

| 主题 | 选项数 |
|-------|---------|
| [Experimental backends](experimental-debug/experimental-backends.md) | 6 |
| [Motr backend](experimental-debug/motr-experimental.md) | 7 |
| [POSIX backend](experimental-debug/posix-experimental.md) | 7 |
| [D4N / D3N cache](experimental-debug/d4n-cache.md) | 22 |
| [Debug & fault injection](experimental-debug/debug-inject.md) | 7 |

[← 指南概览](../../guides/OVERVIEW.md)
