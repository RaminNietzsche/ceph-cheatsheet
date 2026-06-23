# Usage logging

RGW config deep dive — 4 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_usage_log_flush_threshold](#rgw_usage_log_flush_threshold) | `1024` | Advanced | Performance |
| [rgw_usage_log_key_transition](#rgw_usage_log_key_transition) | `True` | Advanced | Policy |
| [rgw_usage_max_shards](#rgw_usage_max_shards) | `32` | Advanced | Policy |
| [rgw_usage_max_user_shards](#rgw_usage_max_user_shards) | `1` | Advanced | Policy |

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

### rgw_usage_log_flush_threshold

| | |
|---|---|
| Type | Int · default `1024` · **Advanced** |
| Table | [rgw.md#SP_rgw_usage_log_flush_threshold](../../config/rgw/rgw.md#SP_rgw_usage_log_flush_threshold) |

**What it does:** Number of entries in usage log before flushing

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_usage_log_flush_threshold 1024
ceph config get client.rgw rgw_usage_log_flush_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1024`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_usage_log_flush_threshold
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_usage_log_key_transition

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_usage_log_key_transition](../../config/rgw/rgw.md#SP_rgw_usage_log_key_transition) |

**What it does:** Handle the co-existence of both old and new name-by-user keys

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_usage_log_key_transition false
ceph config get client.rgw rgw_usage_log_key_transition
```

**Finding optimal value:**

**Tuning model:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_usage_max_shards

| | |
|---|---|
| Type | Int · default `32` · **Advanced** |
| Table | [rgw.md#SP_rgw_usage_max_shards](../../config/rgw/rgw.md#SP_rgw_usage_max_shards) |

**What it does:** Number of shards for usage log.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set global rgw_usage_max_shards 32
ceph config get global rgw_usage_max_shards
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `32` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_usage_max_user_shards

| | |
|---|---|
| Type | Int · default `1` · **Advanced** |
| Table | [rgw.md#SP_rgw_usage_max_user_shards](../../config/rgw/rgw.md#SP_rgw_usage_max_user_shards) |

**What it does:** Number of shards for single user in usage log

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_usage_max_user_shards 1
ceph config get client.rgw rgw_usage_max_user_shards
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `1` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

**Bounds:** min `1`, max `—`.

---


[← RGW config overview](OVERVIEW.md)
