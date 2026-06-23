# RGW Admin

<span class="badge badge-role-rgw">RGW admin</span> Manage RADOS Gateway — S3/Swift, users, buckets, quotas, and multisite.

## Daily commands

```bash
radosgw-admin user list
radosgw-admin bucket stats --bucket=mybucket
radosgw-admin quota get --quota-scope=user --uid=user1
radosgw-admin sync status
ceph orch ps --service-type rgw
ceph config show client.rgw.<instance>
```

See [RGW CLI](../../cli/rgw.md) and [troubleshooting RGW](../../cli/troubleshooting.md).

## Configuration

Full index: [config/rgw/INDEX.md](../../config/rgw/INDEX.md)

| Topic | Deep dive |
|-------|-----------|
| Frontends & HTTP | [core-gateway/frontends.md](../rgw-config/core-gateway/frontends.md) |
| Multisite | [multisite/multisite-zones.md](../rgw-config/multisite/multisite-zones.md) |
| Security & encryption | [security-auth/encryption.md](../rgw-config/security-auth/encryption.md) |
| Quotas | [tenants-quotas/quotas.md](../rgw-config/tenants-quotas/quotas.md) |
| All options | [rgw-config/OVERVIEW.md](../rgw-config/OVERVIEW.md) · [TUNING](../rgw-config/TUNING.md) |

```bash
./scripts/lookup-config.sh rgw_cache_enabled
./scripts/search-config.sh -s rgw multisite
```

## Common workflows

**Create user:**

```bash
radosgw-admin user create --uid=alice --display-name="Alice"
radosgw-admin key create --uid=alice --key-type=s3 --gen-access-key --gen-secret
```

**Multisite period update:**

```bash
radosgw-admin period update --commit
radosgw-admin sync status
```

**Deploy RGW (cephadm):**

```bash
ceph orch apply rgw myrgw --placement="2 host1 host2" --port=8080
```

## Scale notes

| Scale | Focus |
|-------|--------|
| [Small production](../scales/small-production.md) | Single zone, local cache |
| [Multisite](../scales/multisite.md) | Realms, zones, sync lag |
| [Large production](../scales/large-production.md) | Many RGW instances, cache tuning |

[← Guides overview](../OVERVIEW.md)

## Architecture & deployment (from docs-extended)

Prerequisites: active MON+OSD cluster, RGW placement pools, realm/zonegroup/zone for multisite, TLS or proxy.

| Mode | Steps |
|------|--------|
| **Dev (single node)** | cephadm/volume cluster → RGW system user → `radosgw` with `rgw frontends = beast`, `rgw enable apis = s3` → test with `aws s3 --endpoint-url http://127.0.0.1:7480 ls` |
| **Production** | ≥2 `radosgw` in separate AZs → LB health check (`GET /health`) → `rgw dns name` + cert → restrict `rgw enable apis` → ops log + mgr metrics |

| Service | Depends on |
|---------|------------|
| radosgw | MON, OSD, RGW pools |
| radosgw-admin | + admin caps |
| multisite sync | HTTP between zones |

**Common errors:** 503 slow down (dmclock/ratelimit) · No such bucket (zone/tenant/endpoint) · sync lag (`radosgw-admin sync status`).

Deep dives: [Deployment architecture](../../../arch/rgw/architecture/deployment-architecture.md) · [Runtime topology](../../../arch/rgw/architecture/runtime-topology.md) · [Deployment guide](../../../arch/rgw/guides/deployment-implementation-guide.md)
