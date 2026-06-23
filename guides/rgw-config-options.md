# RGW Config Options — Deep Dive

Extended reference for selected RADOS Gateway options. Generated tables live in [config/rgw/INDEX.md](../config/rgw/INDEX.md); this guide adds behavior, use cases, related options, and examples from upstream Ceph `main`.

**Full coverage:** [421 additional options](rgw-config/OVERVIEW.md) are documented by topic (with tuning guidance). Regenerate after config sync: `python3 scripts/generate-rgw-guide.py`.

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

## Finding optimal values

Most RGW options fall into one of three tuning models:

| Model | Meaning | How to choose |
|-------|---------|---------------|
| **Policy** | Security or API compatibility | Upstream default or compliance requirement |
| **Capacity** | Disk, tenant, or SLA limits | Arithmetic from cluster size and product plans |
| **Performance** | Latency, throughput, OSD load | Baseline → incremental change → monitor → validate |

**Shared tooling:**

```bash
ceph config get client.rgw <option>
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph osd pool stats
```

| Option | Tuning model | Quick answer |
|--------|--------------|--------------|
| `d4n_writecache_enabled` | Performance | Benchmark writes with/without cache; watch cache disk |
| `daos_pool` | Capacity | Match a DAOS pool sized for your redundancy and S3 capacity |
| `dbstore_*` | Capacity | Dedicated fast disk with enough free space for metadata growth |
| Account/bucket default quotas | Policy | Cluster capacity ÷ tenant plan; verify with test users |
| `rgw_acl_grants_max_num` | Policy | Default `100`; raise only if clients hit grant limits |
| `rgw_admin_entry` | Policy | Keep `admin` (required for multisite) |
| `rgw_allow_notification_secrets_in_cleartext` | Policy | `false` unless broker has no TLS on a trusted network |
| `rgw_asio_assert_yielding` | Dev | `false` in production |
| `rgw_backend_store` | Architecture | `rados` in production |
| `rgw_barbican_url` | Connectivity | Nearest stable Barbican endpoint; enable KMS cache |
| `rgw_beast_enable_async` | Performance | `true` in production |
| `rgw_bucket_counters_cache*` | Performance | Enable only if per-bucket monitoring; size ≈ active buckets |
| `rgw_bucket_eexist_override` | Policy | Match client API contract (AWS idempotent vs 409) |
| `rgw_bucket_index_max_aio` | Performance | Sweep upward until OSD slow ops increase |

Each option below includes a **Finding optimal value** subsection with step-by-step guidance.

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

**Finding optimal value:** Take a write-heavy baseline with `false` (p50/p99 latency, throughput). Enable D4N on a dedicated NVMe path, set `rgw_d4n_l1_datacache_disk_reserve` so the cache disk cannot fill, then repeat the same workload with `true`. The optimal setting is where write p99 drops without unacceptable cache eviction, flush errors, or consistency risk after restart. On standard RADOS-only clusters, `false` is usually optimal.

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

**Finding optimal value:** There is no numeric sweep — pick a pool that meets redundancy and capacity targets. Query with `dmg pool list` and `dmg pool query <name>`; align engine/tier (NVMe vs HDD) with expected S3 throughput. The value must match an existing DAOS pool name exactly.

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

**Finding optimal value:** Point the URI at a filesystem with low latency and enough space for config and metadata growth. Prefer a dedicated volume over the OS disk. Verify with `df` and startup time after RGW restart.

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

**Finding optimal value:** Choose a path on fast local storage with headroom for SQLite growth (metadata + object index). Watch `iowait` and free space; if the OS disk is busy, move to a dedicated mount. All RGW instances sharing dbstore data must use the same path.

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

**Finding optimal value:** Use the default `dbstore` unless multiple dbstore instances on one host need separate SQLite files. The prefix must be unique per co-located instance to avoid filename collisions.

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

**Finding optimal value:** This is an architecture choice, not a performance knob. For production Ceph clusters, `rados` is optimal. Other values are for PoC or specialized builds only.

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

**Finding optimal value:** Derive from business plans: total cluster usable capacity ÷ expected accounts, with 20–30% headroom for bursts and GC. Verify with `ceph df detail`, create a test account, and confirm limits via `radosgw-admin quota get`. Existing accounts are not affected — use per-account overrides for them.

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

**Finding optimal value:** Same as object quota — align with product tiers (e.g. 10 TiB per account). Size in bytes; `-1` is unlimited. Cross-check against `rgw_account_default_quota_max_objects` so neither cap binds unexpectedly under real object sizes.

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

**Finding optimal value:** Set from expected objects per bucket in your tenant model (e.g. 500k for a standard tier). Use `-1` only if user- or account-level quotas are sufficient. Confirm with a new test user and `radosgw-admin quota get --uid=...`.

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

**Finding optimal value:** Match your bucket size SLA (e.g. 100 GiB per bucket). Pair with `rgw_bucket_default_quota_max_objects` so average object size × max objects does not exceed max size unintentionally. Override existing users with `radosgw-admin quota set`.

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

**Finding optimal value:** Default `100` matches S3/AWS limits and is optimal for most workloads. Raise only if clients return grant-limit errors in RGW logs; lowering hardens against oversized ACL payloads. Avoid raising without a documented client need.

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

**Finding optimal value:** Keep `admin` — optimal for multisite compatibility and existing automation. Changing this is a policy decision with replication risk, not a performance tune.

---

### rgw_allow_notification_secrets_in_cleartext

| | |
|---|---|
| Type | Bool · default `false` |
| Table | [rgw.md#SP_rgw_allow_notification_secrets_in_cleartext](../config/rgw/rgw.md#SP_rgw_allow_notification_secrets_in_cleartext) |

**What it does:** When `true`, allows creating bucket notification topics that include broker passwords/secrets over plain HTTP. Default requires HTTPS for topics with secrets.

**When to use:** Trusted private lab only — broker has no TLS and cannot use alternative auth. **Never** enable on internet-facing or untrusted networks.

**Related options:** `rgw_trust_forwarded_https` (if TLS terminates at a proxy)

**Finding optimal value:** Optimal production value is `false`. Enable `true` only when the notification broker has no TLS on a trusted private network and the security trade-off is accepted — this is not benchmarked.

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

**Finding optimal value:** Use the Barbican endpoint closest to RGW nodes with stable connectivity (`curl -k https://barbican:9311/` from each RGW host). Tune `rgw_crypt_s3_kms_cache_*` so KMS latency does not dominate PUT latency — the URL itself is not swept numerically.

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

**Finding optimal value:** Keep `false` in production. Set `true` only while developing RGW to catch blocking calls on asio threads — it is a debug aid, not a throughput knob.

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

**Finding optimal value:** `true` is optimal for production throughput. Compare requests/sec only if debugging — async coroutines should outperform sync mode. Set `false` only when tracing call stacks during development.

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

**Finding optimal value:** Leave `false` unless you consume per-bucket perf counters in monitoring. If enabled, start with default and watch RGW memory; enable only when dashboards need labeled bucket metrics.

---

### rgw_bucket_counters_cache_size

| | |
|---|---|
| Type | Uint · default `10000` |
| Table | [rgw.md#SP_rgw_bucket_counters_cache_size](../config/rgw/rgw.md#SP_rgw_bucket_counters_cache_size) |

**What it does:** Maximum number of labeled per-bucket perf counter entries kept in the cache.

**When to use:** Increase on clusters with many active buckets and bucket-level monitoring enabled.

**Finding optimal value:** Size the cache to the number of **actively monitored** buckets, not total buckets in the cluster. Sweep 5000 → 10000 → 20000 while watching RGW RSS and counter lookup behavior (`ceph daemon rgw.<id> perf dump`). Use the smallest size that avoids repeated per-bucket counter misses.

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

**Finding optimal value:**

1. Baseline at default `128` with real workloads (large bucket list, bulk delete, multipart).
2. Watch list latency (`aws s3 ls` on sharded buckets), RGW CPU, and OSD slow ops.
3. Increase gradually (192 → 256) until p99 list latency stops improving or OSD slow ops rise.
4. Decrease (e.g. 64) if the cluster is under recovery pressure or bucket-index pools show sustained load spikes.

```bash
radosgw-admin bucket stats --bucket=BIG_BUCKET | jq '.num_shards'
ceph config get client.rgw rgw_multi_obj_del_max_aio
```

More shards and faster OSDs tolerate higher values; during `nearfull` or heavy recovery, lower is safer.

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

**Finding optimal value:** Test with your S3 clients. AWS-compatible idempotent create → `false` (default). Automation that expects HTTP 409 on duplicate create → `true`. This is an API contract choice, not a performance measurement.

---

## See also

- [RGW config — all options by topic](rgw-config/OVERVIEW.md)
- [RGW admin guide](roles/rgw-admin.md) — daily operations
- [RGW CLI](../cli/rgw.md) — `radosgw-admin`, S3 API
- [Config lookup](config-lookup.md) — reading generated tables
- [RGW INDEX](../config/rgw/INDEX.md) — all 441 RGW options

[← Guides overview](OVERVIEW.md)
