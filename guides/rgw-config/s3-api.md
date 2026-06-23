# S3 API & auth

RGW config deep dive — 8 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_s3_auth_disable_signature_url](#rgw_s3_auth_disable_signature_url) | `False` | Advanced | Connectivity |
| [rgw_s3_auth_order](#rgw_s3_auth_order) | `sts, external, local` | Advanced | Performance |
| [rgw_s3_auth_use_keystone](#rgw_s3_auth_use_keystone) | `False` | Advanced | Policy |
| [rgw_s3_auth_use_ldap](#rgw_s3_auth_use_ldap) | `False` | Advanced | Policy |
| [rgw_s3_auth_use_rados](#rgw_s3_auth_use_rados) | `True` | Advanced | Policy |
| [rgw_s3_auth_use_sts](#rgw_s3_auth_use_sts) | `False` | Advanced | Policy |
| [rgw_s3_client_max_sig_ver](#rgw_s3_client_max_sig_ver) | `-1` | Advanced | Policy |
| [rgw_s3_success_create_obj_status](#rgw_s3_success_create_obj_status) | `0` | Advanced | Performance |

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

### rgw_s3_auth_disable_signature_url

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_s3_auth_disable_signature_url](../../config/rgw/rgw.md#SP_rgw_s3_auth_disable_signature_url) |

**What it does:** Should authentication with presigned URLs be disabled

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_s3_auth_disable_signature_url true
ceph config get client.rgw rgw_s3_auth_disable_signature_url
# curl -k <url>  # from each RGW node
```

**Finding optimal value:**

**Tuning model:** Connectivity

1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).
2. From **each** RGW node: `curl -k <url>` or vendor health check.
3. Pick the lowest-latency endpoint that stays healthy over 24h.
4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).
5. Leave empty (`False`) if the integration is disabled.

```bash
ceph config get client.rgw rgw_s3_auth_disable_signature_url
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_s3_auth_order

| | |
|---|---|
| Type | Str · default `sts, external, local` · **Advanced** |
| Table | [rgw.md#SP_rgw_s3_auth_order](../../config/rgw/rgw.md#SP_rgw_s3_auth_order) |

**What it does:** Authentication strategy order to use for S3

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_s3_auth_order "sts, external, local"
ceph config get client.rgw rgw_s3_auth_order
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `sts, external, local`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_s3_auth_order
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_s3_auth_use_keystone

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_s3_auth_use_keystone](../../config/rgw/rgw.md#SP_rgw_s3_auth_use_keystone) |

**What it does:** Specify whether S3 authentication uses Keystone

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_s3_auth_use_keystone true
ceph config get client.rgw rgw_s3_auth_use_keystone
```

**Finding optimal value:**

**Tuning model:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_s3_auth_use_ldap

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_s3_auth_use_ldap](../../config/rgw/rgw.md#SP_rgw_s3_auth_use_ldap) |

**What it does:** Should S3 authentication use LDAP.

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_s3_auth_use_ldap true
ceph config get client.rgw rgw_s3_auth_use_ldap
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_s3_auth_use_rados

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_s3_auth_use_rados](../../config/rgw/rgw.md#SP_rgw_s3_auth_use_rados) |

**What it does:** Specify whether S3 authentication uses credentials stored in RADOS

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_s3_auth_use_rados false
ceph config get client.rgw rgw_s3_auth_use_rados
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_s3_auth_use_sts

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_s3_auth_use_sts](../../config/rgw/rgw.md#SP_rgw_s3_auth_use_sts) |

**What it does:** Should S3 authentication use STS.

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_s3_auth_use_sts true
ceph config get client.rgw rgw_s3_auth_use_sts
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_s3_client_max_sig_ver

| | |
|---|---|
| Type | Int · default `-1` · **Advanced** |
| Table | [rgw.md#SP_rgw_s3_client_max_sig_ver](../../config/rgw/rgw.md#SP_rgw_s3_client_max_sig_ver) |

**What it does:** Max S3 authentication signature version

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_s3_client_max_sig_ver -1
ceph config get client.rgw rgw_s3_client_max_sig_ver
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `-1` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_s3_success_create_obj_status

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_s3_success_create_obj_status](../../config/rgw/rgw.md#SP_rgw_s3_success_create_obj_status) |

**What it does:** HTTP return code override for object creation

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_s3_success_create_obj_status 0
ceph config get client.rgw rgw_s3_success_create_obj_status
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_s3_success_create_obj_status
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](OVERVIEW.md)
