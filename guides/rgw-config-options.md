# RGW Config Options — Deep Dive

Extended reference for selected RADOS Gateway options. Generated tables live in [config/rgw/INDEX.md](../config/rgw/INDEX.md); this guide adds behavior, use cases, related options, and examples from upstream Ceph `main`.

**Lookup any option:**

```bash
./scripts/lookup-config.sh <option-name>
```

---

## Quick reference

| Option | Default | Level | Summary |
|--------|---------|-------|---------|
| [d4n_writecache_enabled](#d4n_writecache_enabled) | `false` | Advanced | D4N write-back cache (experimental) |
| [daos_pool](#daos_pool) | `tank` | Advanced | DAOS pool name when backend is `daos` |
| [dbstore_config_uri](#dbstore_config_uri) | `file:…/dbstore-config.db` | Advanced | SQLite URI for dbstore config |
| [dbstore_db_dir](#dbstore_db_dir) | `/var/lib/ceph/radosgw` | Advanced | dbstore data directory |
| [dbstore_db_name_prefix](#dbstore_db_name_prefix) | `dbstore` | Advanced | dbstore SQLite file prefix |
| [rgw_account_default_quota_max_objects](#rgw_account_default_quota_max_objects) | `-1` | Basic | Default object quota per new account |
| [rgw_account_default_quota_max_size](#rgw_account_default_quota_max_size) | `-1` | Basic | Default size quota per new account |
| [rgw_acl_grants_max_num](#rgw_acl_grants_max_num) | `100` | Advanced | Max ACL grants per request |
| [rgw_admin_entry](#rgw_admin_entry) | `admin` | Advanced | Admin Ops API URL prefix |
| [rgw_allow_notification_secrets_in_cleartext](#rgw_allow_notification_secrets_in_cleartext) | `false` | Advanced | Allow notification secrets over HTTP |
| [rgw_asio_assert_yielding](#rgw_asio_assert_yielding) | `false` | Dev | Assert if asio thread would block |
| [rgw_backend_store](#rgw_backend_store) | `rados` | Advanced | Object/metadata backend (SAL) |
| [rgw_barbican_url](#rgw_barbican_url) | (empty) | Advanced | OpenStack Barbican URL for SSE-KMS |
| [rgw_beast_enable_async](#rgw_beast_enable_async) | `true` | Dev | Beast frontend async coroutines |
| [rgw_bucket_counters_cache](#rgw_bucket_counters_cache) | `false` | Dev | Cache per-bucket perf counters |
| [rgw_bucket_counters_cache_size](#rgw_bucket_counters_cache_size) | `10000` | Advanced | Size of bucket counters cache |
| [rgw_bucket_default_quota_max_objects](#rgw_bucket_default_quota_max_objects) | `-1` | Basic | Default max objects per bucket (new users) |
| [rgw_bucket_default_quota_max_size](#rgw_bucket_default_quota_max_size) | `-1` | Advanced | Default max bytes per bucket (new users) |
| [rgw_bucket_eexist_override](#rgw_bucket_eexist_override) | `false` | Advanced | CreateBucket on existing bucket → 409 |
| [rgw_bucket_index_max_aio](#rgw_bucket_index_max_aio) | `128` | Advanced | Concurrent RADOS ops for bucket index shards |

---

## Backend, cache, and experimental stores

### d4n_writecache_enabled

| | |
|---|---|
| Type | Bool · default `false` · **STARTUP** (restart required) |
| Table | [rgw.md#SP_d4n_writecache_enabled](../config/rgw/rgw.md#SP_d4n_writecache_enabled) |

**What it does:** Enables the D4N (Data Delivery Network) **write-back cache**. When `true`, writes are staged in the local D4N cache layer (SSD path or Redis, depending on D4N setup) before reaching the backend store. When `false`, writes pass through directly to the backend.

**When to use:** Experimental edge/cache scenarios to reduce write latency. Requires the D4N filter stack — not for standard production RGW on RADOS alone.

**Related options:**

- `rgw_filter` = `d4n` (required)
- `rgw_d4n_l1_datacache_persistent_path`, `rgw_d4n_address`, `rgw_d4n_l1_datacache_disk_reserve`
- `rgw_d4n_cache_cleaning_interval`

**Example:**

```bash
ceph config set client.rgw rgw_filter d4n
ceph config set client.rgw d4n_writecache_enabled true
ceph config set client.rgw rgw_d4n_l1_datacache_persistent_path /var/cache/rgw_d4n/
ceph orch restart rgw
```

---

### daos_pool

| | |
|---|---|
| Type | Str · default `tank` |
| Table | [rgw.md#SP_daos_pool](../config/rgw/rgw.md#SP_daos_pool) |

**What it does:** Name of the [DAOS](https://docs.daos.io/) pool RGW connects to when `rgw_backend_store = daos`.

**When to use:** Experimental DAOS-backed RGW (build with `-DWITH_RADOSGW_DAOS=ON`). Not used in standard Ceph clusters on RADOS.

**Related options:** `rgw_backend_store` = `daos`

**Example:**

```ini
[client.rgw]
rgw backend store = daos
daos pool = mypool
```

Create the pool with `dmg pool create --size=<size> mypool`.

---

### dbstore_config_uri

| | |
|---|---|
| Type | Str · default `file:/var/lib/ceph/radosgw/dbstore-config.db` |
| Table | [rgw.md#SP_dbstore_config_uri](../config/rgw/rgw.md#SP_dbstore_config_uri) |

**What it does:** URI for the **configuration database** when using the experimental **dbstore** backend. URIs starting with `file:` point at a local SQLite file.

**When to use:** Standalone RGW without MON/OSD — zone, zonegroup, and users stored locally. See [dbstore README](https://github.com/ceph/ceph/blob/main/src/rgw/driver/dbstore/README.md).

**Related options:**

- `rgw_backend_store` = `dbstore`
- `rgw_config_store` = `dbstore`
- `dbstore_db_dir`, `dbstore_db_name_prefix`

**Example:**

```bash
ceph config set client.rgw rgw_backend_store dbstore
ceph config set client.rgw rgw_config_store dbstore
ceph config set client.rgw dbstore_config_uri file:/var/lib/ceph/radosgw/dbstore-config.db
```

---

### dbstore_db_dir

| | |
|---|---|
| Type | Str · default `/var/lib/ceph/radosgw` |
| Table | [rgw.md#SP_dbstore_db_dir](../config/rgw/rgw.md#SP_dbstore_db_dir) |

**What it does:** Directory where dbstore writes SQLite files for object and metadata storage.

**When to use:** Isolate dbstore data on a dedicated filesystem. Unlike the `rados` backend, dbstore is **stateful** — each RGW instance must see the same files; cephadm cannot freely move daemons without the data.

**Related options:** `dbstore_db_name_prefix`, `dbstore_config_uri`

**Example:**

```bash
ceph config set client.rgw dbstore_db_dir /data/rgw/dbstore
```

---

### dbstore_db_name_prefix

| | |
|---|---|
| Type | Str · default `dbstore` |
| Table | [rgw.md#SP_dbstore_db_name_prefix](../config/rgw/rgw.md#SP_dbstore_db_name_prefix) |

**What it does:** Filename prefix for SQLite databases created by dbstore.

**When to use:** Multiple dbstore instances or tenants on one host without filename collisions.

**Example:**

```bash
ceph config set client.rgw dbstore_db_name_prefix prod_rgw
```

---

### rgw_backend_store

| | |
|---|---|
| Type | Str · default `rados` · enum: `rados`, `dbstore`, `motr`, `daos`, `posix` |
| Table | [rgw.md#SP_rgw_backend_store](../config/rgw/rgw.md#SP_rgw_backend_store) |

**What it does:** Selects the **Storage Abstraction Layer (SAL)** — where RGW stores objects and metadata.

| Value | Role |
|-------|------|
| `rados` | Production default — objects in RADOS pools |
| `dbstore` | Experimental standalone SQLite backend |
| `daos` | Experimental DAOS backend |
| `motr` | Experimental Motr backend |
| `posix` | Experimental POSIX filesystem backend |

**When to use:** Leave `rados` in production. Other values are for development, testing, or specialized deployments.

**Related options:** Backend-specific (`daos_pool`, `dbstore_*`, `rgw_config_store`, `rgw_filter`)

**Example:**

```bash
ceph config get client.rgw rgw_backend_store
```

---

## Quotas (account and bucket defaults)

Quota enforcement also requires `rgw_enable_quota_threads` on at least one RGW per zone. See [rgw_enable_quota_threads](../config/rgw/rgw.md#SP_rgw_enable_quota_threads).

### rgw_account_default_quota_max_objects

| | |
|---|---|
| Type | Int · default `-1` (unlimited) · **Basic** |
| Table | [rgw.md#SP_rgw_account_default_quota_max_objects](../config/rgw/rgw.md#SP_rgw_account_default_quota_max_objects) |

**What it does:** Default cap on **total object count** across all buckets owned by a **new** S3 account. `-1` means unlimited.

**When to use:** Multi-tenant platforms using the account abstraction. Applies only when accounts are created — existing accounts are unchanged.

**Related options:** `rgw_account_default_quota_max_size`, `rgw_enable_quota_threads`

**Example:**

```bash
ceph config set client rgw_account_default_quota_max_objects 1000000
radosgw-admin account create --account-id=acme --account-name="ACME Corp"
```

Set in `[client]` or global so `radosgw-admin` picks it up.

---

### rgw_account_default_quota_max_size

| | |
|---|---|
| Type | Int (bytes) · default `-1` |
| Table | [rgw.md#SP_rgw_account_default_quota_max_size](../config/rgw/rgw.md#SP_rgw_account_default_quota_max_size) |

**What it does:** Default cap on **total stored bytes** for a new account.

**Example:**

```bash
# 10 TiB
ceph config set client rgw_account_default_quota_max_size $((10*1024*1024*1024*1024))
```

---

### rgw_bucket_default_quota_max_objects

| | |
|---|---|
| Type | Int · default `-1` · **Basic** |
| Table | [rgw.md#SP_rgw_bucket_default_quota_max_objects](../config/rgw/rgw.md#SP_rgw_bucket_default_quota_max_objects) |

**What it does:** Default maximum **objects per bucket** for **newly created users**. Does not retroactively change existing users.

**When to use:** Enforce per-bucket object limits for every new tenant without per-user `radosgw-admin quota` calls.

**Related options:** `rgw_bucket_default_quota_max_size`, `rgw_user_default_quota_*`

**Example:**

```bash
ceph config set client rgw_bucket_default_quota_max_objects 500000
radosgw-admin user create --uid=newuser --display-name="New User"
```

---

### rgw_bucket_default_quota_max_size

| | |
|---|---|
| Type | Int (bytes) · default `-1` |
| Table | [rgw.md#SP_rgw_bucket_default_quota_max_size](../config/rgw/rgw.md#SP_rgw_bucket_default_quota_max_size) |

**What it does:** Default maximum **bytes per bucket** for new users.

**Example:**

```bash
ceph config set client rgw_bucket_default_quota_max_size $((100*1024*1024*1024))

# Per-user override for existing users
radosgw-admin quota set --uid=alice --max-size=50G --max-objects=10000
radosgw-admin quota enable --uid=alice
```

---

## Security, admin API, and notifications

### rgw_acl_grants_max_num

| | |
|---|---|
| Type | Int · default `100` |
| Table | [rgw.md#SP_rgw_acl_grants_max_num](../config/rgw/rgw.md#SP_rgw_acl_grants_max_num) |

**What it does:** Maximum number of ACL grants allowed in a single PutBucketAcl / PutObjectAcl request (aligned with S3 limits).

**When to use:** Raise only if clients legitimately need more grants; lowering can harden against oversized ACL payloads.

**Related options:** `rgw_cors_rules_max_num`, `rgw_user_policies_max_num`

---

### rgw_admin_entry

| | |
|---|---|
| Type | Str · default `admin` · not runtime-updatable |
| Table | [rgw.md#SP_rgw_admin_entry](../config/rgw/rgw.md#SP_rgw_admin_entry) |

**What it does:** URL path prefix for the **RGW Admin Ops REST API** (bucket/user introspection, usage, etc.).

**Important:** Multisite replication **requires** the value `admin`. Do not change it on multisite clusters.

**Example:**

```bash
# Default admin URL pattern:
# GET https://rgw.example.com/admin/bucket?bucket=mybucket&format=json
curl -s -H "Authorization: AWS ..." \
  "https://rgw.example.com/admin/bucket?bucket=mybucket&format=json"
```

---

### rgw_allow_notification_secrets_in_cleartext

| | |
|---|---|
| Type | Bool · default `false` |
| Table | [rgw.md#SP_rgw_allow_notification_secrets_in_cleartext](../config/rgw/rgw.md#SP_rgw_allow_notification_secrets_in_cleartext) |

**What it does:** When `true`, allows creating bucket notification topics that include broker passwords/secrets over plain HTTP. Default requires HTTPS for topics with secrets.

**When to use:** Trusted private lab only — broker has no TLS and cannot use alternative auth. **Never** enable on internet-facing or untrusted networks.

**Related options:** `rgw_trust_forwarded_https` (if TLS terminates at a proxy)

---

### rgw_barbican_url

| | |
|---|---|
| Type | Str · default empty |
| Table | [rgw.md#SP_rgw_barbican_url](../config/rgw/rgw.md#SP_rgw_barbican_url) |

**What it does:** Base URL of the **OpenStack Barbican** key manager for **SSE-KMS** server-side encryption.

**When to use:** Store encryption keys in Barbican instead of on-cluster secrets. Requires Keystone credentials for Barbican access.

**Related options:**

- `rgw_crypt_s3_kms_backend` = `barbican`
- `rgw_keystone_barbican_user`, `rgw_keystone_barbican_password`, `rgw_keystone_barbican_project`
- `rgw_crypt_s3_kms_cache_*`

**Example:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_backend barbican
ceph config set client.rgw rgw_barbican_url https://barbican.example.com:9311/
```

See [Ceph RGW config ref — Barbican](https://docs.ceph.com/en/latest/radosgw/config-ref/#barbican-settings).

---

## Performance and frontend behavior

### rgw_asio_assert_yielding

| | |
|---|---|
| Type | Bool · default `false` · **Dev** |
| Table | [rgw.md#SP_rgw_asio_assert_yielding](../config/rgw/rgw.md#SP_rgw_asio_assert_yielding) |

**What it does:** Triggers an assertion if code running on an asio/beast thread would block instead of yielding to coroutines. Development aid for finding blocking calls.

**When to use:** RGW development/debugging only — keep `false` in production.

**Related options:** `rgw_beast_enable_async`

---

### rgw_beast_enable_async

| | |
|---|---|
| Type | Bool · default `true` · **Dev** |
| Table | [rgw.md#SP_rgw_beast_enable_async](../config/rgw/rgw.md#SP_rgw_beast_enable_async) |

**What it does:** When `true`, the Beast HTTP frontend processes requests with **coroutines**, allowing multiple concurrent requests per thread. When `false`, concurrency is limited by thread count but synchronous call stacks are easier to trace.

**When to use:** Leave `true` for production throughput. Set `false` only when debugging request flow.

**Example:**

```bash
ceph config set client.rgw rgw_beast_enable_async false
ceph orch restart rgw
```

---

### rgw_bucket_counters_cache

| | |
|---|---|
| Type | Bool · default `false` · **Dev** |
| Table | [rgw.md#SP_rgw_bucket_counters_cache](../config/rgw/rgw.md#SP_rgw_bucket_counters_cache) |

**What it does:** Enables an in-memory cache for **perf counters** that carry a bucket label, so per-bucket metrics can be served without repeated counter lookups.

**Related options:** `rgw_bucket_counters_cache_size`

**Example:**

```bash
ceph config set client.rgw rgw_bucket_counters_cache true
ceph config set client.rgw rgw_bucket_counters_cache_size 20000
```

---

### rgw_bucket_counters_cache_size

| | |
|---|---|
| Type | Uint · default `10000` |
| Table | [rgw.md#SP_rgw_bucket_counters_cache_size](../config/rgw/rgw.md#SP_rgw_bucket_counters_cache_size) |

**What it does:** Maximum number of labeled per-bucket perf counter entries kept in the cache.

**When to use:** Increase on clusters with many active buckets and bucket-level monitoring enabled.

---

### rgw_bucket_index_max_aio

| | |
|---|---|
| Type | Uint · default `128` |
| Table | [rgw.md#SP_rgw_bucket_index_max_aio](../config/rgw/rgw.md#SP_rgw_bucket_index_max_aio) |

**What it does:** Limits **concurrent RADOS requests** when operating across **bucket index shards** (list operations, index maintenance, multi-shard updates). Used in `svc_bi_rados.cc` to batch aio operations.

**When to use:**

- **Increase** (e.g. 256) if large sharded buckets have slow listings and OSD capacity allows it.
- **Decrease** (e.g. 64) if bucket index operations cause OSD load spikes.

**Related options:** `rgw_multi_obj_del_max_aio` (default 16), `rgw_override_bucket_index_max_shards`

**Example:**

```bash
ceph config set client.rgw rgw_bucket_index_max_aio 256
```

---

## Bucket API behavior

### rgw_bucket_eexist_override

| | |
|---|---|
| Type | Bool · default `false` |
| Table | [rgw.md#SP_rgw_bucket_eexist_override](../config/rgw/rgw.md#SP_rgw_bucket_eexist_override) |

**What it does:** When `true`, `CreateBucket` on a bucket that already exists (same owner) returns **HTTP 409 / EEXIST** instead of succeeding idempotently.

**Default behavior (`false`):** Matches AWS S3 — repeated CreateBucket by the same owner typically returns 200 OK.

**When to use:** Clients or automation that expect an error on duplicate bucket creation; stricter bucket naming workflows.

**Example:**

```bash
ceph config set client.rgw rgw_bucket_eexist_override true
# aws s3 mb s3://existing-bucket  →  409 BucketAlreadyExists
```

---

## See also

- [RGW admin guide](roles/rgw-admin.md) — daily operations
- [RGW CLI](../cli/rgw.md) — `radosgw-admin`, S3 API
- [Config lookup](config-lookup.md) — reading generated tables
- [RGW INDEX](../config/rgw/INDEX.md) — all 441 RGW options

[← Guides overview](OVERVIEW.md)
