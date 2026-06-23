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

## Topics

| Topic | Options |
|-------|---------|
| [Access and object logging](logging.md) | 4 |
| [Admin CORS](admin-cors.md) | 4 |
| [BitTorrent](torrent.md) | 8 |
| [Bucket notifications](notifications.md) | 13 |
| [Bucket operations and index](bucket-ops.md) | 12 |
| [Caches and TTL](caches-and-ttl.md) | 3 |
| [Copy progress](copy-progress.md) | 2 |
| [D4N / D3N cache](d4n-cache.md) | 22 |
| [Debug and fault injection](debug-inject.md) | 7 |
| [Dynamic resharding](resharding.md) | 12 |
| [Encryption and KMS](encryption.md) | 42 |
| [Experimental backends](experimental-backends.md) | 6 |
| [Feature toggles](feature-toggles.md) | 10 |
| [Frontends and DNS](frontends-dns.md) | 4 |
| [Garbage collection](garbage-collection.md) | 7 |
| [General RGW options](general.md) | 54 |
| [HTTP / libcurl](http-curl.md) | 5 |
| [Keystone and STS](keystone-sts.md) | 32 |
| [LDAP authentication](ldap.md) | 6 |
| [Lifecycle (LC) workers](lifecycle.md) | 12 |
| [Limits and listing](limits-listing.md) | 10 |
| [Lua scripting](lua.md) | 4 |
| [Motr (experimental backend)](motr-experimental.md) | 7 |
| [Multipart uploads](multipart.md) | 2 |
| [Multisite sync](multisite-sync.md) | 28 |
| [Multisite zones and realm](multisite-zones.md) | 15 |
| [NFS gateway](nfs.md) | 14 |
| [OPA authorization](opa-authz.md) | 3 |
| [Object expiry hints](object-expiry.md) | 1 |
| [Object read/write I/O](object-io.md) | 4 |
| [Ops logging](ops-logging.md) | 4 |
| [POSIX backend (experimental)](posix-experimental.md) | 7 |
| [Performance and concurrency](performance-tuning.md) | 17 |
| [Quota sync and defaults](quotas.md) | 5 |
| [REST connections (multisite)](rest-connections.md) | 3 |
| [RGW LC counters](lifecycle-counters.md) | 2 |
| [RGW metadata cache](metadata-cache.md) | 3 |
| [Request scheduler](scheduler.md) | 1 |
| [S3 API behavior](s3-api.md) | 8 |
| [Swift API](swift.md) | 11 |
| [Timeouts and intervals](timeouts-intervals.md) | 8 |
| [Usage logging](usage-logging.md) | 4 |
| [Users and per-user settings](users-quotas.md) | 3 |
| [dmclock scheduler](dmclock.md) | 12 |

[← Guides overview](../OVERVIEW.md)
