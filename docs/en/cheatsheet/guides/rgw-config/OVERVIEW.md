# RGW Config Deep Dive — All Options

Extended reference for all **441** RGW options with **Finding optimal value** guidance. Generated from [config/rgw/INDEX.md](../../config/rgw/INDEX.md).

```bash
./scripts/lookup-config.sh <option-name>
python3 scripts/generate-rgw-guide.py  # regenerate after config sync
```

## Tuning

- [Tuning quick reference](TUNING.md) — all options, model, one-line answer

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, API compatibility, tenant limits |
| **Capacity** | Disk layout, paths, pool sizing |
| **Performance** | Baseline → incremental change → monitor OSD/RGW |
| **Connectivity** | Nearest stable external endpoint |
| **Architecture** | Backend, multisite topology — not numeric sweeps |
| **Dev** | Keep upstream default in production |

## Topics by category


### Core gateway

| Topic | Options |
|-------|---------|
| [Frontends & HTTP stack](core-gateway/frontends.md) | 6 |
| [Feature toggles](core-gateway/feature-toggles.md) | 10 |
| [Scheduler & dmclock](core-gateway/scheduler-dmclock.md) | 13 |
| [HTTP compatibility](core-gateway/http-compat.md) | 17 |
| [Core runtime](core-gateway/core-runtime.md) | 16 |

### Performance & I/O

| Topic | Options |
|-------|---------|
| [Concurrency & RADOS I/O](performance-io/performance-tuning.md) | 14 |
| [Object read/write windows](performance-io/object-io.md) | 4 |
| [Multipart & copy](performance-io/multipart-copy.md) | 4 |
| [Metadata & object caches](performance-io/caching.md) | 4 |
| [Timeouts & intervals](performance-io/timeouts-intervals.md) | 8 |
| [Listing limits](performance-io/limits-listing.md) | 12 |

### Buckets & data lifecycle

| Topic | Options |
|-------|---------|
| [Bucket operations](buckets-lifecycle/bucket-ops.md) | 12 |
| [Bucket index & sharding](buckets-lifecycle/index-sharding.md) | 4 |
| [Dynamic resharding](buckets-lifecycle/resharding.md) | 12 |
| [Object expiry hints](buckets-lifecycle/object-expiry.md) | 2 |
| [Garbage collection](buckets-lifecycle/garbage-collection.md) | 7 |
| [Lifecycle (LC)](buckets-lifecycle/lifecycle.md) | 17 |

### Tenants & quotas

| Topic | Options |
|-------|---------|
| [Quota sync & defaults](tenants-quotas/quotas.md) | 5 |
| [Users & per-user settings](tenants-quotas/users-quotas.md) | 5 |

### Multisite

| Topic | Options |
|-------|---------|
| [Zones, realm & region](multisite/multisite-zones.md) | 19 |
| [Replication & sync](multisite/multisite-sync.md) | 28 |
| [REST connections](multisite/rest-connections.md) | 3 |

### Security & authentication

| Topic | Options |
|-------|---------|
| [Encryption & KMS](security-auth/encryption.md) | 43 |
| [Keystone & STS](security-auth/keystone-sts.md) | 32 |
| [LDAP](security-auth/ldap.md) | 6 |
| [OPA authorization](security-auth/opa-authz.md) | 4 |
| [Swift API](security-auth/swift.md) | 11 |
| [S3 API & auth](security-auth/s3-api.md) | 8 |

### Notifications

| Topic | Options |
|-------|---------|
| [Bucket notifications](notifications/notifications.md) | 13 |

### Logging & admin

| Topic | Options |
|-------|---------|
| [Access & object logging](logging-admin/logging.md) | 4 |
| [Ops logging](logging-admin/ops-logging.md) | 4 |
| [Usage logging](logging-admin/usage-logging.md) | 4 |
| [Admin CORS](logging-admin/admin-cors.md) | 4 |
| [API limits & policies](logging-admin/api-limits.md) | 6 |

### Extensions

| Topic | Options |
|-------|---------|
| [NFS gateway](extensions/nfs.md) | 14 |
| [Lua scripting](extensions/lua.md) | 4 |
| [BitTorrent](extensions/torrent.md) | 8 |
| [HTTP / libcurl](extensions/http-curl.md) | 5 |

### Experimental & debug

| Topic | Options |
|-------|---------|
| [Experimental backends](experimental-debug/experimental-backends.md) | 6 |
| [Motr backend](experimental-debug/motr-experimental.md) | 7 |
| [POSIX backend](experimental-debug/posix-experimental.md) | 7 |
| [D4N / D3N cache](experimental-debug/d4n-cache.md) | 22 |
| [Debug & fault injection](experimental-debug/debug-inject.md) | 7 |

[← Guides overview](../OVERVIEW.md)
