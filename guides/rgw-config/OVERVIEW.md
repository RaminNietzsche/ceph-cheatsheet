# RGW Config Deep Dive — All Options

Extended reference for all **441** RADOS Gateway options with **Finding optimal value** tuning guidance (same format as [curated batch 1](../rgw-config-options.md)). Generated from [config/rgw/INDEX.md](../../config/rgw/INDEX.md).

```bash
./scripts/lookup-config.sh <option-name>
python3 scripts/generate-rgw-guide.py  # regenerate after config sync
```

## Tuning

- [Tuning quick reference](TUNING.md) — all options, model, one-line answer
- [Curated batch 1](../rgw-config-options.md) — first 19 options with extra narrative

## Tuning models

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, API compatibility, tenant limits |
| **Capacity** | Disk layout, paths, pool sizing |
| **Performance** | Baseline → incremental change → monitor OSD/RGW |
| **Connectivity** | Nearest stable external endpoint |
| **Architecture** | Backend, multisite topology |
| **Dev** | Upstream default only in production |

## Topics by category


### Core gateway

| Topic | Options |
|-------|---------|
| [Frontends & HTTP stack](frontends.md) | 6 |
| [Feature toggles](feature-toggles.md) | 10 |
| [Scheduler & dmclock](scheduler-dmclock.md) | 13 |
| [HTTP compatibility](http-compat.md) | 17 |
| [Core runtime](core-runtime.md) | 16 |

### Performance & I/O

| Topic | Options |
|-------|---------|
| [Concurrency & RADOS I/O](performance-tuning.md) | 14 |
| [Object read/write windows](object-io.md) | 4 |
| [Multipart & copy](multipart-copy.md) | 4 |
| [Metadata & object caches](caching.md) | 4 |
| [Timeouts & intervals](timeouts-intervals.md) | 8 |
| [Listing limits](limits-listing.md) | 12 |

### Buckets & data lifecycle

| Topic | Options |
|-------|---------|
| [Bucket operations](bucket-ops.md) | 12 |
| [Bucket index & sharding](index-sharding.md) | 4 |
| [Dynamic resharding](resharding.md) | 12 |
| [Object expiry hints](object-expiry.md) | 2 |
| [Garbage collection](garbage-collection.md) | 7 |
| [Lifecycle (LC)](lifecycle.md) | 17 |

### Tenants & quotas

| Topic | Options |
|-------|---------|
| [Quota sync & defaults](quotas.md) | 5 |
| [Users & per-user settings](users-quotas.md) | 5 |

### Multisite

| Topic | Options |
|-------|---------|
| [Zones, realm & region](multisite-zones.md) | 19 |
| [Replication & sync](multisite-sync.md) | 28 |
| [REST connections](rest-connections.md) | 3 |

### Security & authentication

| Topic | Options |
|-------|---------|
| [Encryption & KMS](encryption.md) | 43 |
| [Keystone & STS](keystone-sts.md) | 32 |
| [LDAP](ldap.md) | 6 |
| [OPA authorization](opa-authz.md) | 4 |
| [Swift API](swift.md) | 11 |
| [S3 API & auth](s3-api.md) | 8 |

### Notifications

| Topic | Options |
|-------|---------|
| [Bucket notifications](notifications.md) | 13 |

### Logging & admin

| Topic | Options |
|-------|---------|
| [Access & object logging](logging.md) | 4 |
| [Ops logging](ops-logging.md) | 4 |
| [Usage logging](usage-logging.md) | 4 |
| [Admin CORS](admin-cors.md) | 4 |
| [API limits & policies](api-limits.md) | 6 |

### Extensions

| Topic | Options |
|-------|---------|
| [NFS gateway](nfs.md) | 14 |
| [Lua scripting](lua.md) | 4 |
| [BitTorrent](torrent.md) | 8 |
| [HTTP / libcurl](http-curl.md) | 5 |

### Experimental & debug

| Topic | Options |
|-------|---------|
| [Experimental backends](experimental-backends.md) | 6 |
| [Motr backend](motr-experimental.md) | 7 |
| [POSIX backend](posix-experimental.md) | 7 |
| [D4N / D3N cache](d4n-cache.md) | 22 |
| [Debug & fault injection](debug-inject.md) | 7 |

[← Guides overview](../OVERVIEW.md)
