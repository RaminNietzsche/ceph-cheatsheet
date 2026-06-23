# Feature toggles

RGW config deep dive — 10 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_disable_s3select](#rgw_disable_s3select) | `False` | Advanced | Policy |
| [rgw_enable_apis](#rgw_enable_apis) | `s3, s3control, s3website, swift, swift_auth, admin, sts, iam, notifications` | Advanced | Performance |
| [rgw_enable_gc_threads](#rgw_enable_gc_threads) | `True` | Advanced | Policy |
| [rgw_enable_jwks_url_verification](#rgw_enable_jwks_url_verification) | `False` | Advanced | Policy |
| [rgw_enable_lc_threads](#rgw_enable_lc_threads) | `True` | Advanced | Policy |
| [rgw_enable_mdsearch](#rgw_enable_mdsearch) | `True` | Basic | Policy |
| [rgw_enable_ops_log](#rgw_enable_ops_log) | `False` | Advanced | Policy |
| [rgw_enable_restore_threads](#rgw_enable_restore_threads) | `True` | Advanced | Policy |
| [rgw_enable_static_website](#rgw_enable_static_website) | `False` | Basic | Policy |
| [rgw_enable_usage_log](#rgw_enable_usage_log) | `False` | Advanced | Policy |

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

### rgw_disable_s3select

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_disable_s3select](../../../config/rgw/rgw.md#SP_rgw_disable_s3select) |

**What it does:** disable the s3select operation; RGW will report an error and will return ERR_INVALID_REQUEST.

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_disable_s3select true
ceph config get client.rgw rgw_disable_s3select
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_apis

| | |
|---|---|
| Type | Str · default `s3, s3control, s3website, swift, swift_auth, admin, sts, iam, notifications` · **Advanced** |
| Table | [rgw.md#SP_rgw_enable_apis](../../../config/rgw/rgw.md#SP_rgw_enable_apis) |

**What it does:** A list of RESTful APIs for RGW to enable

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_enable_apis "s3, s3control, s3website, swift, swift_auth, admin, sts, iam, notifications"
ceph config get client.rgw rgw_enable_apis
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `s3, s3control, s3website, swift, swift_auth, admin, sts, iam, notifications`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_enable_apis
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_enable_gc_threads

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_enable_gc_threads](../../../config/rgw/rgw.md#SP_rgw_enable_gc_threads) |

**What it does:** Enables the garbage collection maintenance thread.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_enable_gc_threads false
ceph config get client.rgw rgw_enable_gc_threads
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_jwks_url_verification

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_enable_jwks_url_verification](../../../config/rgw/rgw.md#SP_rgw_enable_jwks_url_verification) |

**What it does:** Enable JWKS url verification for AWS compliance

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_enable_jwks_url_verification true
ceph config get client.rgw rgw_enable_jwks_url_verification
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_lc_threads

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_enable_lc_threads](../../../config/rgw/rgw.md#SP_rgw_enable_lc_threads) |

**What it does:** Enables the lifecycle maintenance thread. This is required on at least one RGW daemon for each zone.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_enable_lc_threads false
ceph config get client.rgw rgw_enable_lc_threads
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_mdsearch

| | |
|---|---|
| Type | Bool · default `True` · **Basic** |
| Table | [rgw.md#SP_rgw_enable_mdsearch](../../../config/rgw/rgw.md#SP_rgw_enable_mdsearch) |

**What it does:** Enable elastic metadata search APIs

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_enable_mdsearch false
ceph config get client.rgw rgw_enable_mdsearch
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_ops_log

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_enable_ops_log](../../../config/rgw/rgw.md#SP_rgw_enable_ops_log) |

**What it does:** Enable ops log

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_enable_ops_log true
ceph config get client.rgw rgw_enable_ops_log
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_restore_threads

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_enable_restore_threads](../../../config/rgw/rgw.md#SP_rgw_enable_restore_threads) |

**What it does:** Enables the objects' restore maintenance thread.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_enable_restore_threads false
ceph config get client.rgw rgw_enable_restore_threads
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_static_website

| | |
|---|---|
| Type | Bool · default `False` · **Basic** |
| Table | [rgw.md#SP_rgw_enable_static_website](../../../config/rgw/rgw.md#SP_rgw_enable_static_website) |

**What it does:** Enable static website APIs

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_enable_static_website true
ceph config get client.rgw rgw_enable_static_website
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_usage_log

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_enable_usage_log](../../../config/rgw/rgw.md#SP_rgw_enable_usage_log) |

**What it does:** Enable the usage log

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_enable_usage_log true
ceph config get client.rgw rgw_enable_usage_log
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← RGW config overview](../OVERVIEW.md)
