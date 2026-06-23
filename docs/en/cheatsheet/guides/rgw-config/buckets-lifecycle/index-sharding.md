# Bucket index & sharding

RGW config deep dive — 4 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_override_bucket_index_max_shards](#rgw_override_bucket_index_max_shards) | `0` | Dev | Policy |
| [rgw_pending_bucket_index_op_expiration](#rgw_pending_bucket_index_op_expiration) | `120` | Advanced | Performance |
| [rgw_safe_max_objects_per_shard](#rgw_safe_max_objects_per_shard) | `102400` | Advanced | Policy |
| [rgw_shard_warning_threshold](#rgw_shard_warning_threshold) | `90` | Advanced | Performance |

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
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph pg stat
```

---

### rgw_override_bucket_index_max_shards

| | |
|---|---|
| Type | Uint · default `0` · **Dev** |
| Table | [rgw.md#SP_rgw_override_bucket_index_max_shards](../../../config/rgw/rgw.md#SP_rgw_override_bucket_index_max_shards) |

**What it does:** The default number of bucket index shards for newly-created buckets. This value overrides bucket_index_max_shards stored in the zone. Setting this value in the zone is preferred, because it applies globally to all radosgw daemons running in the zone.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_override_bucket_index_max_shards 128
ceph config get client.rgw rgw_override_bucket_index_max_shards
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `0` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_pending_bucket_index_op_expiration

| | |
|---|---|
| Type | Uint · default `120` · **Advanced** |
| Table | [rgw.md#SP_rgw_pending_bucket_index_op_expiration](../../../config/rgw/rgw.md#SP_rgw_pending_bucket_index_op_expiration) |

**What it does:** Number of seconds a pending operation can remain in bucket index shard.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_pending_bucket_index_op_expiration 120
ceph config get client.rgw rgw_pending_bucket_index_op_expiration
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `120`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_pending_bucket_index_op_expiration
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_safe_max_objects_per_shard

| | |
|---|---|
| Type | Int · default `102400` · **Advanced** |
| Table | [rgw.md#SP_rgw_safe_max_objects_per_shard](../../../config/rgw/rgw.md#SP_rgw_safe_max_objects_per_shard) |

**What it does:** Safe number of objects per shard

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_safe_max_objects_per_shard 102400
ceph config get client.rgw rgw_safe_max_objects_per_shard
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `102400` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_shard_warning_threshold

| | |
|---|---|
| Type | Float · default `90` · **Advanced** |
| Table | [rgw.md#SP_rgw_shard_warning_threshold](../../../config/rgw/rgw.md#SP_rgw_shard_warning_threshold) |

**What it does:** Warn about max objects per shard

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_shard_warning_threshold 90
ceph config get client.rgw rgw_shard_warning_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `90`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_shard_warning_threshold
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](../OVERVIEW.md)
