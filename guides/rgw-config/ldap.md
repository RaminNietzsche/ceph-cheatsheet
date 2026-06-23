# LDAP

RGW config deep dive — 6 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_ldap_binddn](#rgw_ldap_binddn) | `uid=admin,cn=users,dc=example,dc=com` | Advanced | Policy |
| [rgw_ldap_dnattr](#rgw_ldap_dnattr) | `uid` | Advanced | Performance |
| [rgw_ldap_searchdn](#rgw_ldap_searchdn) | `cn=users,cn=accounts,dc=example,dc=com` | Advanced | Performance |
| [rgw_ldap_searchfilter](#rgw_ldap_searchfilter) | `(empty)` | Advanced | Performance |
| [rgw_ldap_secret](#rgw_ldap_secret) | `/etc/openldap/secret` | Advanced | Policy |
| [rgw_ldap_uri](#rgw_ldap_uri) | `(empty)` | Advanced | Connectivity |

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

### rgw_ldap_binddn

| | |
|---|---|
| Type | Str · default `uid=admin,cn=users,dc=example,dc=com` · **Advanced** |
| Table | [rgw.md#SP_rgw_ldap_binddn](../../config/rgw/rgw.md#SP_rgw_ldap_binddn) |

**What it does:** LDAP entry RGW will bind with (user match).

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_ldap_binddn "uid=admin,cn=users,dc=example,dc=com"
ceph config get client.rgw rgw_ldap_binddn
ceph config set client.rgw rgw_s3_auth_use_ldap true
```

**Finding optimal value:**

**Tuning model:** Policy

1. Upstream default (`uid=admin,cn=users,dc=example,dc=com`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---

### rgw_ldap_dnattr

| | |
|---|---|
| Type | Str · default `uid` · **Advanced** |
| Table | [rgw.md#SP_rgw_ldap_dnattr](../../config/rgw/rgw.md#SP_rgw_ldap_dnattr) |

**What it does:** LDAP attribute containing RGW user names (to form binddns).

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_ldap_dnattr uid
ceph config get client.rgw rgw_ldap_dnattr
ceph config set client.rgw rgw_s3_auth_use_ldap true
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `uid`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_ldap_dnattr
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_ldap_searchdn

| | |
|---|---|
| Type | Str · default `cn=users,cn=accounts,dc=example,dc=com` · **Advanced** |
| Table | [rgw.md#SP_rgw_ldap_searchdn](../../config/rgw/rgw.md#SP_rgw_ldap_searchdn) |

**What it does:** LDAP search base (basedn).

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_ldap_searchdn "cn=users,cn=accounts,dc=example,dc=com"
ceph config get client.rgw rgw_ldap_searchdn
ceph config set client.rgw rgw_s3_auth_use_ldap true
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `cn=users,cn=accounts,dc=example,dc=com`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_ldap_searchdn
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_ldap_searchfilter

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_ldap_searchfilter](../../config/rgw/rgw.md#SP_rgw_ldap_searchfilter) |

**What it does:** LDAP search filter.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_ldap_searchfilter <value>
ceph config get client.rgw rgw_ldap_searchfilter
ceph config set client.rgw rgw_s3_auth_use_ldap true
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_ldap_searchfilter
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_ldap_secret

| | |
|---|---|
| Type | Str · default `/etc/openldap/secret` · **Advanced** |
| Table | [rgw.md#SP_rgw_ldap_secret](../../config/rgw/rgw.md#SP_rgw_ldap_secret) |

**What it does:** Path to file containing credentials for rgw_ldap_binddn.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_ldap_secret "/etc/openldap/secret"
ceph config get client.rgw rgw_ldap_secret
ceph config set client.rgw rgw_s3_auth_use_ldap true
```

**Finding optimal value:**

**Tuning model:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_ldap_uri

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_ldap_uri](../../config/rgw/rgw.md#SP_rgw_ldap_uri) |

**What it does:** Space-separated list of LDAP servers in URI format, e.g., "ldaps://<ldap.your.domain>".

**When to use:** Set when integrating with an external service; leave empty if the feature is unused.

**Example:**

```bash
ceph config set client.rgw rgw_ldap_uri "ldaps://ldap.example.com/"
ceph config get client.rgw rgw_ldap_uri
# curl -k <url>  # from each RGW node
```

**Finding optimal value:**

**Tuning model:** Connectivity

1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).
2. From **each** RGW node: `curl -k <url>` or vendor health check.
3. Pick the lowest-latency endpoint that stays healthy over 24h.
4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).
5. Leave empty (`(empty)`) if the integration is disabled.

```bash
ceph config get client.rgw rgw_ldap_uri
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](OVERVIEW.md)
