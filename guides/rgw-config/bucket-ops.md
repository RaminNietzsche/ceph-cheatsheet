# Bucket operations

RGW config deep dive — 12 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_bucket_counters_cache](#rgw_bucket_counters_cache) | `False` | Dev | Performance |
| [rgw_bucket_counters_cache_size](#rgw_bucket_counters_cache_size) | `10000` | Advanced | Performance |
| [rgw_bucket_default_quota_max_objects](#rgw_bucket_default_quota_max_objects) | `-1` | Basic | Policy |
| [rgw_bucket_default_quota_max_size](#rgw_bucket_default_quota_max_size) | `-1` | Advanced | Policy |
| [rgw_bucket_eexist_override](#rgw_bucket_eexist_override) | `False` | Advanced | Policy |
| [rgw_bucket_index_max_aio](#rgw_bucket_index_max_aio) | `128` | Advanced | Performance |
| [rgw_bucket_index_transaction_instrumentation](#rgw_bucket_index_transaction_instrumentation) | `False` | Dev | Dev |
| [rgw_bucket_logging_obj_roll_time](#rgw_bucket_logging_obj_roll_time) | `300` | Advanced | Performance |
| [rgw_bucket_persistent_notif_num_shards](#rgw_bucket_persistent_notif_num_shards) | `11` | Advanced | Policy |
| [rgw_bucket_quota_cache_size](#rgw_bucket_quota_cache_size) | `10000` | Advanced | Performance |
| [rgw_bucket_quota_ttl](#rgw_bucket_quota_ttl) | `10_min` | Advanced | Performance |
| [rgw_bucket_sync_spawn_window](#rgw_bucket_sync_spawn_window) | `20` | Dev | Performance |

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, API compatibility, tenant limits |
| **Capacity** | Disk layout, paths, pool sizing |
| **Performance** | Baseline → incremental change → monitor OSD/RGW |
| **Connectivity** | Nearest stable external endpoint |
| **Architecture** | Backend, multisite topology — not numeric sweeps |
| **Dev** | Keep upstream default in production |

**Shared tooling:**

```bash
ceph config get client.rgw <option>
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph osd pool stats
```

---

### rgw_bucket_counters_cache

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [rgw.md#SP_rgw_bucket_counters_cache](../../config/rgw/rgw.md#SP_rgw_bucket_counters_cache) |

**What it does:** Enables an in-memory cache for **perf counters** with a bucket label, so per-bucket metrics avoid repeated counter lookups.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Related options:**

- `rgw_bucket_counters_cache_size`

**Example:**

```bash
ceph config set client.rgw rgw_bucket_counters_cache true
ceph config set client.rgw rgw_bucket_counters_cache_size 20000
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `False` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_bucket_counters_cache_size

| | |
|---|---|
| Type | Uint · default `10000` · **Advanced** |
| Table | [rgw.md#SP_rgw_bucket_counters_cache_size](../../config/rgw/rgw.md#SP_rgw_bucket_counters_cache_size) |

**What it does:** Maximum number of labeled per-bucket perf counter entries kept in the cache.

**When to use:** Increase on clusters with many active buckets and bucket-level monitoring enabled.

**Example:**

```bash
ceph config set client.rgw rgw_bucket_counters_cache_size 10000
ceph config get client.rgw rgw_bucket_counters_cache_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**Signals:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_bucket_counters_cache_size
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_bucket_default_quota_max_objects

| | |
|---|---|
| Type | Int · default `-1` · **Basic** |
| Table | [rgw.md#SP_rgw_bucket_default_quota_max_objects](../../config/rgw/rgw.md#SP_rgw_bucket_default_quota_max_objects) |

**What it does:** Default maximum **objects per bucket** for **newly created users**. Does not retroactively change existing users.

**When to use:** Enforce per-bucket object limits for every new tenant without per-user `radosgw-admin quota` calls.

**Related options:**

- `rgw_bucket_default_quota_max_size`, `rgw_user_default_quota_*`

**Example:**

```bash
ceph config set client rgw_bucket_default_quota_max_objects 500000
radosgw-admin user create --uid=newuser --display-name="New User"
```

**Finding optimal value:**

**Tuning model:** Policy

1. `ceph df detail` — usable cluster capacity.
2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.
3. Set limit; `-1` means unlimited. Default: `-1`.
4. Create a test user/account and confirm via `radosgw-admin quota get`.
5. Existing users/accounts are **not** retroactively changed.

```bash
ceph df detail
radosgw-admin quota get --uid=testuser
radosgw-admin bucket stats --bucket=testbucket
```

---

### rgw_bucket_default_quota_max_size

| | |
|---|---|
| Type | Int · default `-1` · **Advanced** |
| Table | [rgw.md#SP_rgw_bucket_default_quota_max_size](../../config/rgw/rgw.md#SP_rgw_bucket_default_quota_max_size) |

**What it does:** Default maximum **bytes per bucket** for new users.

**When to use:** Set tenant or platform default limits for new users, accounts, or buckets.

**Example:**

```bash
ceph config set client rgw_bucket_default_quota_max_size $((100*1024*1024*1024))

radosgw-admin quota set --uid=alice --max-size=50G --max-objects=10000
radosgw-admin quota enable --uid=alice
```

**Finding optimal value:**

**Tuning model:** Policy

1. `ceph df detail` — usable cluster capacity.
2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.
3. Set limit; `-1` means unlimited. Default: `-1`.
4. Create a test user/account and confirm via `radosgw-admin quota get`.
5. Existing users/accounts are **not** retroactively changed.

```bash
ceph df detail
radosgw-admin quota get --uid=testuser
radosgw-admin bucket stats --bucket=testbucket
```

---

### rgw_bucket_eexist_override

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_bucket_eexist_override](../../config/rgw/rgw.md#SP_rgw_bucket_eexist_override) |

**What it does:** When `true`, `CreateBucket` on an existing bucket (same owner) returns **HTTP 409 / EEXIST** instead of succeeding idempotently.

**Default (`false`):** Matches AWS S3 — repeated CreateBucket by the same owner typically returns 200 OK.

**When to use:** Clients or automation that expect an error on duplicate bucket creation.

**Example:**

```bash
ceph config set client.rgw rgw_bucket_eexist_override true
# aws s3 mb s3://existing-bucket  →  409 BucketAlreadyExists
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_bucket_index_max_aio

| | |
|---|---|
| Type | Uint · default `128` · **Advanced** |
| Table | [rgw.md#SP_rgw_bucket_index_max_aio](../../config/rgw/rgw.md#SP_rgw_bucket_index_max_aio) |

**What it does:** Limits **concurrent RADOS requests** across **bucket index shards** (list operations, index maintenance, multi-shard updates). Used in `svc_bi_rados.cc`.

**When to use:**

- **Increase** when listings/deletes on sharded buckets are slow and OSDs have headroom.
- **Decrease** when bucket-index pools show sustained load spikes or slow ops.

**Related options:**

- [`rgw_multi_obj_del_max_aio`](../../config/rgw/rgw.md#SP_rgw_multi_obj_del_max_aio) (default 16)
- [`rgw_override_bucket_index_max_shards`](../../config/rgw/rgw.md#SP_rgw_override_bucket_index_max_shards)

**Example:**

```bash
ceph config set client.rgw rgw_bucket_index_max_aio 256
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at `128` with large bucket LIST, bulk DELETE, multipart completion.
2. Watch list/delete p99, RGW CPU, and OSD slow ops.
3. Increase in steps (~25%: e.g. 128 → 160 → 192 → 256) until latency stops improving.
4. **Decrease** under recovery pressure, `nearfull`, or sustained bucket-index pool load.

**Signals:** OSD `slow requests`, rising `rgw` throttle counters, flat client throughput.

```bash
ceph config get client.rgw rgw_bucket_index_max_aio
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
radosgw-admin bucket stats --bucket=BIG_BUCKET | jq '.num_shards'
```

More shards and faster OSDs tolerate higher values; during `nearfull` or heavy recovery, lower is safer.

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
ceph config set client.rgw rgw_bucket_index_transaction_instrumentation true
ceph config get client.rgw rgw_bucket_index_transaction_instrumentation
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**Signals:** assertion failures, injected errors, or trace noise in logs.

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

**Finding optimal value:**

**Tuning model:** Performance

1. Default `300` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_bucket_logging_obj_roll_time
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

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

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `11` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_bucket_quota_cache_size

| | |
|---|---|
| Type | Int · default `10000` · **Advanced** |
| Table | [rgw.md#SP_rgw_bucket_quota_cache_size](../../config/rgw/rgw.md#SP_rgw_bucket_quota_cache_size) |

**What it does:** RGW quota stats cache size

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Example:**

```bash
ceph config set client.rgw rgw_bucket_quota_cache_size 10000
ceph config get client.rgw rgw_bucket_quota_cache_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**Signals:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_bucket_quota_cache_size
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_bucket_quota_ttl

| | |
|---|---|
| Type | Int · default `10_min` · **Advanced** |
| Table | [rgw.md#SP_rgw_bucket_quota_ttl](../../config/rgw/rgw.md#SP_rgw_bucket_quota_ttl) |

**What it does:** Bucket quota stats cache TTL

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_bucket_quota_ttl 10_min
ceph config get client.rgw rgw_bucket_quota_ttl
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `10_min` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_bucket_quota_ttl
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_bucket_sync_spawn_window

| | |
|---|---|
| Type | Int · default `20` · **Dev** |
| Table | [rgw.md#SP_rgw_bucket_sync_spawn_window](../../config/rgw/rgw.md#SP_rgw_bucket_sync_spawn_window) |

**When to use:**

- **Increase** when multisite replication lag grows.
- **Decrease** when sync load competes with client I/O.

**Example:**

```bash
ceph config set client.rgw rgw_bucket_sync_spawn_window 20
ceph config get client.rgw rgw_bucket_sync_spawn_window
radosgw-admin sync status
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `20` limits parallel sync coroutines per bucket/zone.
2. **Increase** when multisite lag grows and RGW CPU headroom exists.
3. **Decrease** if sync threads starve client-facing requests or OSDs spike.

**Signals:** `radosgw-admin sync status`, data/meta sync lag, RGW load average.

```bash
ceph config get client.rgw rgw_bucket_sync_spawn_window
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
radosgw-admin sync status
```

---


[← RGW config overview](OVERVIEW.md)
