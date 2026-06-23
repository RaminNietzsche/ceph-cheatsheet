# Deep Dive پیکربندی RGW — همه گزینه‌ها

مرجع گسترده برای **441** گزینه RGW با راهنمای **یافتن مقدار بهینه**. تولید شده از [config/rgw/INDEX.md](../../config/rgw/INDEX.md).

```bash
./scripts/lookup-config.sh <option-name>
python3 scripts/generate-rgw-guide.py  # regenerate after config sync
```

## تنظیم

- [مرجع سریع تنظیم](TUNING.md) — all options, model, one-line answer

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **Policy** | امنیت، سازگاری API، محدودیت tenant |
| **Capacity** | چیدمان دیسک، مسیرها، اندازه pool |
| **Performance** | خط پایه → تغییر تدریجی → پایش OSD/RGW |
| **Connectivity** | نزدیک‌ترین endpoint پایدار خارجی |
| **Architecture** | backend، توپولوژی multisite — نه sweep عددی |
| **Dev** | پیش‌فرض upstream در production |

## موضوعات بر اساس دسته


### Core gateway

| موضوع | گزینه‌ها |
|-------|---------|
| [Frontends & HTTP stack](core-gateway/frontends.md) | 6 |
| [Feature toggles](core-gateway/feature-toggles.md) | 10 |
| [Scheduler & dmclock](core-gateway/scheduler-dmclock.md) | 13 |
| [HTTP compatibility](core-gateway/http-compat.md) | 17 |
| [Core runtime](core-gateway/core-runtime.md) | 16 |

### Performance & I/O

| موضوع | گزینه‌ها |
|-------|---------|
| [Concurrency & RADOS I/O](performance-io/performance-tuning.md) | 14 |
| [Object read/write windows](performance-io/object-io.md) | 4 |
| [Multipart & copy](performance-io/multipart-copy.md) | 4 |
| [Metadata & object caches](performance-io/caching.md) | 4 |
| [Timeouts & intervals](performance-io/timeouts-intervals.md) | 8 |
| [Listing limits](performance-io/limits-listing.md) | 12 |

### Buckets & data lifecycle

| موضوع | گزینه‌ها |
|-------|---------|
| [Bucket operations](buckets-lifecycle/bucket-ops.md) | 12 |
| [Bucket index & sharding](buckets-lifecycle/index-sharding.md) | 4 |
| [Dynamic resharding](buckets-lifecycle/resharding.md) | 12 |
| [Object expiry hints](buckets-lifecycle/object-expiry.md) | 2 |
| [Garbage collection](buckets-lifecycle/garbage-collection.md) | 7 |
| [Lifecycle (LC)](buckets-lifecycle/lifecycle.md) | 17 |

### Tenants & quotas

| موضوع | گزینه‌ها |
|-------|---------|
| [Quota sync & defaults](tenants-quotas/quotas.md) | 5 |
| [Users & per-user settings](tenants-quotas/users-quotas.md) | 5 |

### Multisite

| موضوع | گزینه‌ها |
|-------|---------|
| [Zones, realm & region](multisite/multisite-zones.md) | 19 |
| [Replication & sync](multisite/multisite-sync.md) | 28 |
| [REST connections](multisite/rest-connections.md) | 3 |

### Security & authentication

| موضوع | گزینه‌ها |
|-------|---------|
| [Encryption & KMS](security-auth/encryption.md) | 43 |
| [Keystone & STS](security-auth/keystone-sts.md) | 32 |
| [LDAP](security-auth/ldap.md) | 6 |
| [OPA authorization](security-auth/opa-authz.md) | 4 |
| [Swift API](security-auth/swift.md) | 11 |
| [S3 API & auth](security-auth/s3-api.md) | 8 |

### Notifications

| موضوع | گزینه‌ها |
|-------|---------|
| [Bucket notifications](notifications/notifications.md) | 13 |

### Logging & admin

| موضوع | گزینه‌ها |
|-------|---------|
| [Access & object logging](logging-admin/logging.md) | 4 |
| [Ops logging](logging-admin/ops-logging.md) | 4 |
| [Usage logging](logging-admin/usage-logging.md) | 4 |
| [Admin CORS](logging-admin/admin-cors.md) | 4 |
| [API limits & policies](logging-admin/api-limits.md) | 6 |

### Extensions

| موضوع | گزینه‌ها |
|-------|---------|
| [NFS gateway](extensions/nfs.md) | 14 |
| [Lua scripting](extensions/lua.md) | 4 |
| [BitTorrent](extensions/torrent.md) | 8 |
| [HTTP / libcurl](extensions/http-curl.md) | 5 |

### Experimental & debug

| موضوع | گزینه‌ها |
|-------|---------|
| [Experimental backends](experimental-debug/experimental-backends.md) | 6 |
| [Motr backend](experimental-debug/motr-experimental.md) | 7 |
| [POSIX backend](experimental-debug/posix-experimental.md) | 7 |
| [D4N / D3N cache](experimental-debug/d4n-cache.md) | 22 |
| [Debug & fault injection](experimental-debug/debug-inject.md) | 7 |

[← نمای کلی راهنما](../../guides/OVERVIEW.md)
