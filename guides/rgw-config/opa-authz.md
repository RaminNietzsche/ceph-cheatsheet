# OPA authorization

RGW config deep dive — 3 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_opa_token](#rgw_opa_token) | `(empty)` | Advanced |
| [rgw_opa_url](#rgw_opa_url) | `(empty)` | Advanced |
| [rgw_opa_verify_ssl](#rgw_opa_verify_ssl) | `True` | Advanced |

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

**Finding optimal value:** Not a performance knob — use credentials from your identity/KMS provider. Rotate via secrets management; never commit values to config repos.

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

**Finding optimal value:** Use the nearest stable endpoint reachable from every RGW node. Verify with curl from each host; measure p99 latency of dependent operations and keep the default (`(empty)`) if the integration is unused.

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

**Finding optimal value:** Security/compliance setting — prefer `true` in production unless a trusted lab requires `True`.

---


[← RGW config overview](OVERVIEW.md)
