# Bucket operations and index

RGW config deep dive — 6 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_bucket_index_transaction_instrumentation](#rgw_bucket_index_transaction_instrumentation) | `False` | Dev |
| [rgw_bucket_logging_obj_roll_time](#rgw_bucket_logging_obj_roll_time) | `300` | Advanced |
| [rgw_bucket_persistent_notif_num_shards](#rgw_bucket_persistent_notif_num_shards) | `11` | Advanced |
| [rgw_bucket_quota_cache_size](#rgw_bucket_quota_cache_size) | `10000` | Advanced |
| [rgw_bucket_quota_ttl](#rgw_bucket_quota_ttl) | `10_min` | Advanced |
| [rgw_bucket_sync_spawn_window](#rgw_bucket_sync_spawn_window) | `20` | Dev |

---

### rgw_bucket_index_transaction_instrumentation

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [rgw.md#SP_rgw_bucket_index_transaction_instrumentation](../../config/rgw/rgw.md#SP_rgw_bucket_index_transaction_instrumentation) |

**What it does:** Turns on extra instrumentation surrounding bucket index transactions.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_bucket_index_transaction_instrumentation False
ceph config get client.rgw rgw_bucket_index_transaction_instrumentation
```

**Finding optimal value:** Keep the upstream default (`False`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_bucket_logging_obj_roll_time

| | |
|---|---|
| Type | Uint · default `300` · **Advanced** |
| Table | [rgw.md#SP_rgw_bucket_logging_obj_roll_time](../../config/rgw/rgw.md#SP_rgw_bucket_logging_obj_roll_time) |

**What it does:** Default time in seconds for the bucket logging object to roll

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_bucket_logging_obj_roll_time 300
ceph config get client.rgw rgw_bucket_logging_obj_roll_time
```

**Finding optimal value:** Lower for fresher behavior / faster reaction; higher to reduce background load. Adjust from default (`300`) only when logs show sync, cache, or timeout issues.

---

### rgw_bucket_persistent_notif_num_shards

| | |
|---|---|
| Type | Uint · default `11` · **Advanced** |
| Table | [rgw.md#SP_rgw_bucket_persistent_notif_num_shards](../../config/rgw/rgw.md#SP_rgw_bucket_persistent_notif_num_shards) |

**What it does:** Number of shards for a persistent topic.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_bucket_persistent_notif_num_shards 11
ceph config get client.rgw rgw_bucket_persistent_notif_num_shards
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`11`) matches S3 compatibility for most workloads.

---

### rgw_bucket_quota_cache_size

| | |
|---|---|
| Type | Int · default `10000` · **Advanced** |
| Table | [rgw.md#SP_rgw_bucket_quota_cache_size](../../config/rgw/rgw.md#SP_rgw_bucket_quota_cache_size) |

**What it does:** RGW quota stats cache size

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_bucket_quota_cache_size 10000
ceph config get client.rgw rgw_bucket_quota_cache_size
```

**Finding optimal value:** Balance quota enforcement freshness vs RGW/CLS load. Start at default (`10000`); shorten if users exceed limits before stats catch up, lengthen if quota sync dominates CPU.

---

### rgw_bucket_quota_ttl

| | |
|---|---|
| Type | Int · default `10_min` · **Advanced** |
| Table | [rgw.md#SP_rgw_bucket_quota_ttl](../../config/rgw/rgw.md#SP_rgw_bucket_quota_ttl) |

**What it does:** Bucket quota stats cache TTL

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_bucket_quota_ttl 10_min
ceph config get client.rgw rgw_bucket_quota_ttl
```

**Finding optimal value:** Balance quota enforcement freshness vs RGW/CLS load. Start at default (`10_min`); shorten if users exceed limits before stats catch up, lengthen if quota sync dominates CPU.

---

### rgw_bucket_sync_spawn_window

| | |
|---|---|
| Type | Int · default `20` · **Dev** |
| Table | [rgw.md#SP_rgw_bucket_sync_spawn_window](../../config/rgw/rgw.md#SP_rgw_bucket_sync_spawn_window) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_bucket_sync_spawn_window 20
ceph config get client.rgw rgw_bucket_sync_spawn_window
```

**Finding optimal value:** Keep the upstream default (`20`) in production. Enable or change only during targeted debugging sessions.

---


[← RGW config overview](OVERVIEW.md)
