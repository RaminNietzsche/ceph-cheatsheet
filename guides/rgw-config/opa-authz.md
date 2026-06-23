# OPA authorization

RGW config deep dive — 3 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_opa_token](#rgw_opa_token) | `(empty)` | Advanced | Policy |
| [rgw_opa_url](#rgw_opa_url) | `(empty)` | Advanced | Connectivity |
| [rgw_opa_verify_ssl](#rgw_opa_verify_ssl) | `True` | Advanced | Policy |

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

### rgw_opa_token

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_opa_token](../../config/rgw/rgw.md#SP_rgw_opa_token) |

**What it does:** The Bearer token OPA uses to authenticate client requests.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_opa_token <value>
ceph config get client.rgw rgw_opa_token
```

**Finding optimal value:**

**Tuning model:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_opa_url

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_opa_url](../../config/rgw/rgw.md#SP_rgw_opa_url) |

**What it does:** URL to OPA server.

**When to use:** Set when integrating with an external service; leave empty if the feature is unused.

**Example:**

```bash
ceph config set client.rgw rgw_opa_url <value>
ceph config get client.rgw rgw_opa_url
```

**Finding optimal value:**

**Tuning model:** Connectivity

1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).
2. From **each** RGW node: `curl -k <url>` or vendor health check.
3. Pick the lowest-latency endpoint that stays healthy over 24h.
4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).
5. Leave empty (`(empty)`) if the integration is disabled.

```bash
ceph config get client.rgw rgw_opa_url
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_opa_verify_ssl

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_opa_verify_ssl](../../config/rgw/rgw.md#SP_rgw_opa_verify_ssl) |

**What it does:** Should RGW verify the OPA server SSL certificate.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_opa_verify_ssl True
ceph config get client.rgw rgw_opa_verify_ssl
```

**Finding optimal value:**

**Tuning model:** Policy

1. Production: prefer secure default (`True` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---


[← RGW config overview](OVERVIEW.md)
