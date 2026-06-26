# Usage logging

RGW config deep dive — 4 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

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
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph pg stat
```

---

### rgw_usage_log_flush_threshold

| | |
|---|---|
| Type | Int · default `1024` · **Advanced** |
| Table | [rgw.md#SP_rgw_usage_log_flush_threshold](../../../config/rgw/rgw.md#SP_rgw_usage_log_flush_threshold) |

**What it does:** Number of entries in usage log before flushing This is the max number of entries that will be held in the usage log, before it will be flushed to the backend. Note that the usage log is periodically flushed, even if number of entries does not reach this threshold. A usage log entry corresponds to one or more operations on a single bucket.i

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
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_usage_log_key_transition

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_usage_log_key_transition](../../../config/rgw/rgw.md#SP_rgw_usage_log_key_transition) |

**What it does:** Handle the co-existence of both old and new name-by-user keys The new usage log keyed by owner/payer ID has the prefix of "~" for IDs starting with '0'. This prefix is absent from the old scheme. This option instructs RGW to handle the old keys if they still exist. It should be set false when the old keys no longer exist to avoid performance penalty.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Related options:**

- [`rgw_enable_usage_log`](../../../config/rgw/rgw.md#SP_rgw_enable_usage_log)

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
| Table | [rgw.md#SP_rgw_usage_max_shards](../../../config/rgw/rgw.md#SP_rgw_usage_max_shards) |

**What it does:** Number of shards for usage log. The number of RADOS objects that RGW will use in order to store the usage log data. All RGW daemons and radosgw-admin commands must use the same value for this option. If values differ, writes and reads/clears will target different objects, causing usage data to appear empty or not be cleared. Use ``ceph config set global rgw_usage_max_shards <N>`` to ensure consistency across the cluster. Alternatively, ``radosgw-admin`` supports the ``--rgw-usage-max-shards`` command-line parameter.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Related options:**

- [`rgw_enable_usage_log`](../../../config/rgw/rgw.md#SP_rgw_enable_usage_log)

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
| Table | [rgw.md#SP_rgw_usage_max_user_shards](../../../config/rgw/rgw.md#SP_rgw_usage_max_user_shards) |

**What it does:** Number of shards for single user in usage log The number of shards that a single user will span over in the usage log.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Related options:**

- [`rgw_enable_usage_log`](../../../config/rgw/rgw.md#SP_rgw_enable_usage_log)

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


[← RGW config overview](../OVERVIEW.md)
