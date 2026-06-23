# LDAP authentication

RGW config deep dive — 6 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_ldap_binddn](#rgw_ldap_binddn) | `uid=admin,cn=users,dc=example,dc=com` | Advanced |
| [rgw_ldap_dnattr](#rgw_ldap_dnattr) | `uid` | Advanced |
| [rgw_ldap_searchdn](#rgw_ldap_searchdn) | `cn=users,cn=accounts,dc=example,dc=com` | Advanced |
| [rgw_ldap_searchfilter](#rgw_ldap_searchfilter) | `(empty)` | Advanced |
| [rgw_ldap_secret](#rgw_ldap_secret) | `/etc/openldap/secret` | Advanced |
| [rgw_ldap_uri](#rgw_ldap_uri) | `(empty)` | Advanced |

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
ceph config set client.rgw rgw_ldap_binddn uid=admin,cn=users,dc=example,dc=com
ceph config get client.rgw rgw_ldap_binddn
```

**Finding optimal value:** Start from upstream default (`uid=admin,cn=users,dc=example,dc=com`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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
```

**Finding optimal value:** Start from upstream default (`uid`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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
ceph config set client.rgw rgw_ldap_searchdn cn=users,cn=accounts,dc=example,dc=com
ceph config get client.rgw rgw_ldap_searchdn
```

**Finding optimal value:** Start from upstream default (`cn=users,cn=accounts,dc=example,dc=com`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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
```

**Finding optimal value:** Not a performance knob — use credentials from your identity/KMS provider. Rotate via secrets management; never commit values to config repos.

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
ceph config set client.rgw rgw_ldap_uri <value>
ceph config get client.rgw rgw_ldap_uri
```

**Finding optimal value:** Use the nearest stable endpoint reachable from every RGW node. Verify with curl from each host; measure p99 latency of dependent operations and keep the default (`(empty)`) if the integration is unused.

---


[← RGW config overview](OVERVIEW.md)
