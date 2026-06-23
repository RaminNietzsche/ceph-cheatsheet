# Keystone & STS

RGW config deep dive — 32 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_keystone_accepted_admin_roles](#rgw_keystone_accepted_admin_roles) | `(empty)` | Advanced | Performance |
| [rgw_keystone_accepted_reader_roles](#rgw_keystone_accepted_reader_roles) | `(empty)` | Advanced | Performance |
| [rgw_keystone_accepted_roles](#rgw_keystone_accepted_roles) | `Member, admin` | Advanced | Performance |
| [rgw_keystone_admin_domain](#rgw_keystone_admin_domain) | `(empty)` | Advanced | Performance |
| [rgw_keystone_admin_password](#rgw_keystone_admin_password) | `(empty)` | Advanced | Policy |
| [rgw_keystone_admin_password_path](#rgw_keystone_admin_password_path) | `(empty)` | Advanced | Capacity |
| [rgw_keystone_admin_project](#rgw_keystone_admin_project) | `(empty)` | Advanced | Performance |
| [rgw_keystone_admin_tenant](#rgw_keystone_admin_tenant) | `(empty)` | Advanced | Performance |
| [rgw_keystone_admin_user](#rgw_keystone_admin_user) | `(empty)` | Advanced | Performance |
| [rgw_keystone_barbican_domain](#rgw_keystone_barbican_domain) | `(empty)` | Advanced | Performance |
| [rgw_keystone_barbican_password](#rgw_keystone_barbican_password) | `(empty)` | Advanced | Policy |
| [rgw_keystone_barbican_project](#rgw_keystone_barbican_project) | `(empty)` | Advanced | Performance |
| [rgw_keystone_barbican_tenant](#rgw_keystone_barbican_tenant) | `(empty)` | Advanced | Performance |
| [rgw_keystone_barbican_user](#rgw_keystone_barbican_user) | `(empty)` | Advanced | Performance |
| [rgw_keystone_expired_token_cache_expiration](#rgw_keystone_expired_token_cache_expiration) | `3600` | Advanced | Performance |
| [rgw_keystone_implicit_tenants](#rgw_keystone_implicit_tenants) | `false` | Advanced | Architecture |
| [rgw_keystone_scope_enabled](#rgw_keystone_scope_enabled) | `False` | Advanced | Policy |
| [rgw_keystone_scope_include_roles](#rgw_keystone_scope_include_roles) | `True` | Advanced | Policy |
| [rgw_keystone_scope_include_user](#rgw_keystone_scope_include_user) | `False` | Advanced | Policy |
| [rgw_keystone_service_token_accepted_roles](#rgw_keystone_service_token_accepted_roles) | `admin` | Advanced | Policy |
| [rgw_keystone_service_token_enabled](#rgw_keystone_service_token_enabled) | `False` | Advanced | Policy |
| [rgw_keystone_token_cache_size](#rgw_keystone_token_cache_size) | `10000` | Advanced | Performance |
| [rgw_keystone_token_cache_ttl](#rgw_keystone_token_cache_ttl) | `300` | Advanced | Performance |
| [rgw_keystone_url](#rgw_keystone_url) | `(empty)` | Basic | Connectivity |
| [rgw_keystone_verify_ssl](#rgw_keystone_verify_ssl) | `True` | Advanced | Policy |
| [rgw_sts_client_id](#rgw_sts_client_id) | `(empty)` | Advanced | Policy |
| [rgw_sts_client_secret](#rgw_sts_client_secret) | `(empty)` | Advanced | Policy |
| [rgw_sts_entry](#rgw_sts_entry) | `sts` | Advanced | Policy |
| [rgw_sts_key](#rgw_sts_key) | `(empty)` | Advanced | Performance |
| [rgw_sts_max_session_duration](#rgw_sts_max_session_duration) | `43200` | Advanced | Policy |
| [rgw_sts_min_session_duration](#rgw_sts_min_session_duration) | `900` | Advanced | Performance |
| [rgw_sts_token_introspection_url](#rgw_sts_token_introspection_url) | `(empty)` | Advanced | Connectivity |

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

### rgw_keystone_accepted_admin_roles

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_accepted_admin_roles](../../../config/rgw/rgw.md#SP_rgw_keystone_accepted_admin_roles) |

**What it does:** List of roles allowing user to gain admin privileges (Keystone).

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_accepted_admin_roles <value>
ceph config get client.rgw rgw_keystone_accepted_admin_roles
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_accepted_admin_roles
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_accepted_reader_roles

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_accepted_reader_roles](../../../config/rgw/rgw.md#SP_rgw_keystone_accepted_reader_roles) |

**What it does:** List of roles that can only be used for reads (Keystone).

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_accepted_reader_roles <value>
ceph config get client.rgw rgw_keystone_accepted_reader_roles
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_accepted_reader_roles
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_accepted_roles

| | |
|---|---|
| Type | Str · default `Member, admin` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_accepted_roles](../../../config/rgw/rgw.md#SP_rgw_keystone_accepted_roles) |

**What it does:** Only users with one of these roles will be served when doing Keystone authentication.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_accepted_roles "Member, admin"
ceph config get client.rgw rgw_keystone_accepted_roles
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `Member, admin`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_accepted_roles
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_admin_domain

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_admin_domain](../../../config/rgw/rgw.md#SP_rgw_keystone_admin_domain) |

**What it does:** Keystone admin user domain (for Keystone v3).

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_admin_domain <value>
ceph config get client.rgw rgw_keystone_admin_domain
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_admin_domain
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_admin_password

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_admin_password](../../../config/rgw/rgw.md#SP_rgw_keystone_admin_password) |

**What it does:** DEPRECATED: Keystone admin password.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_admin_password "<from-secrets-manager>"
ceph config get client.rgw rgw_keystone_admin_password
```

**Finding optimal value:**

**Tuning model:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_admin_password_path

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_admin_password_path](../../../config/rgw/rgw.md#SP_rgw_keystone_admin_password_path) |

**What it does:** Path to a file containing the Keystone admin password.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_admin_password_path "/var/lib/ceph/radosgw"
ceph config get client.rgw rgw_keystone_admin_password_path
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`(empty)`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw rgw_keystone_admin_password_path)
iostat -x 5  # disk saturation
```

---

### rgw_keystone_admin_project

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_admin_project](../../../config/rgw/rgw.md#SP_rgw_keystone_admin_project) |

**What it does:** Keystone admin user project (for Keystone v3).

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_admin_project <value>
ceph config get client.rgw rgw_keystone_admin_project
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_admin_project
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_admin_tenant

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_admin_tenant](../../../config/rgw/rgw.md#SP_rgw_keystone_admin_tenant) |

**What it does:** Keystone admin user tenant.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_admin_tenant <value>
ceph config get client.rgw rgw_keystone_admin_tenant
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_admin_tenant
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_admin_user

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_admin_user](../../../config/rgw/rgw.md#SP_rgw_keystone_admin_user) |

**What it does:** Keystone admin user.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_admin_user <value>
ceph config get client.rgw rgw_keystone_admin_user
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_admin_user
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_barbican_domain

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_barbican_domain](../../../config/rgw/rgw.md#SP_rgw_keystone_barbican_domain) |

**What it does:** Keystone barbican user domain.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_barbican_domain <value>
ceph config get client.rgw rgw_keystone_barbican_domain
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_barbican_domain
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_barbican_password

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_barbican_password](../../../config/rgw/rgw.md#SP_rgw_keystone_barbican_password) |

**What it does:** Keystone password for barbican user.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_barbican_password "<from-secrets-manager>"
ceph config get client.rgw rgw_keystone_barbican_password
```

**Finding optimal value:**

**Tuning model:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_barbican_project

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_barbican_project](../../../config/rgw/rgw.md#SP_rgw_keystone_barbican_project) |

**What it does:** Keystone barbican user project (Keystone v3).

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_barbican_project <value>
ceph config get client.rgw rgw_keystone_barbican_project
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_barbican_project
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_barbican_tenant

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_barbican_tenant](../../../config/rgw/rgw.md#SP_rgw_keystone_barbican_tenant) |

**What it does:** Keystone barbican user tenant (Keystone v2.0).

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_barbican_tenant <value>
ceph config get client.rgw rgw_keystone_barbican_tenant
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_barbican_tenant
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_barbican_user

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_barbican_user](../../../config/rgw/rgw.md#SP_rgw_keystone_barbican_user) |

**What it does:** Keystone user to access barbican secrets.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_barbican_user <value>
ceph config get client.rgw rgw_keystone_barbican_user
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_barbican_user
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_expired_token_cache_expiration

| | |
|---|---|
| Type | Int · default `3600` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_expired_token_cache_expiration](../../../config/rgw/rgw.md#SP_rgw_keystone_expired_token_cache_expiration) |

**What it does:** The number of seconds to add to current time for expired token expiration

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_expired_token_cache_expiration 3600
ceph config get client.rgw rgw_keystone_expired_token_cache_expiration
```

**Finding optimal value:**

**Tuning model:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `3600`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**Signals:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_keystone_expired_token_cache_expiration
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_implicit_tenants

| | |
|---|---|
| Type | Str · enum: ["false", "true", "swift", "s3", "both", "0", "1", "none"] · default `false` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_implicit_tenants](../../../config/rgw/rgw.md#SP_rgw_keystone_implicit_tenants) |

**What it does:** RGW Keystone implicit tenants creation

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_implicit_tenants false
ceph config get client.rgw rgw_keystone_implicit_tenants
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Valid values: ["false", "true", "swift", "s3", "both", "0", "1", "none"].
2. Default `false` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_keystone_scope_enabled

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_scope_enabled](../../../config/rgw/rgw.md#SP_rgw_keystone_scope_enabled) |

**What it does:** Enable logging of Keystone scope information in ops log

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_scope_enabled true
ceph config get client.rgw rgw_keystone_scope_enabled
```

**Finding optimal value:**

**Tuning model:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_scope_include_roles

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_scope_include_roles](../../../config/rgw/rgw.md#SP_rgw_keystone_scope_include_roles) |

**What it does:** Include role names in Keystone scope logs

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_scope_include_roles false
ceph config get client.rgw rgw_keystone_scope_include_roles
```

**Finding optimal value:**

**Tuning model:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_scope_include_user

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_scope_include_user](../../../config/rgw/rgw.md#SP_rgw_keystone_scope_include_user) |

**What it does:** Include human-readable identity names in Keystone scope logs

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_scope_include_user true
ceph config get client.rgw rgw_keystone_scope_include_user
```

**Finding optimal value:**

**Tuning model:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_service_token_accepted_roles

| | |
|---|---|
| Type | Str · default `admin` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_service_token_accepted_roles](../../../config/rgw/rgw.md#SP_rgw_keystone_service_token_accepted_roles) |

**What it does:** Only users with one of these roles will be valid for service users.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_service_token_accepted_roles admin
ceph config get client.rgw rgw_keystone_service_token_accepted_roles
```

**Finding optimal value:**

**Tuning model:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_service_token_enabled

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_service_token_enabled](../../../config/rgw/rgw.md#SP_rgw_keystone_service_token_enabled) |

**What it does:** Service tokens allowing the usage of expired Keystone auth tokens

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_service_token_enabled true
ceph config get client.rgw rgw_keystone_service_token_enabled
```

**Finding optimal value:**

**Tuning model:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_token_cache_size

| | |
|---|---|
| Type | Int · default `10000` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_token_cache_size](../../../config/rgw/rgw.md#SP_rgw_keystone_token_cache_size) |

**What it does:** Keystone token cache size

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_token_cache_size 10000
ceph config get client.rgw rgw_keystone_token_cache_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**Signals:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_keystone_token_cache_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_token_cache_ttl

| | |
|---|---|
| Type | Int · default `300` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_token_cache_ttl](../../../config/rgw/rgw.md#SP_rgw_keystone_token_cache_ttl) |

**What it does:** Keystone token secret key cache TTL

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_token_cache_ttl 300
ceph config get client.rgw rgw_keystone_token_cache_ttl
```

**Finding optimal value:**

**Tuning model:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `300`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**Signals:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_keystone_token_cache_ttl
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_url

| | |
|---|---|
| Type | Str · default `(empty)` · **Basic** |
| Table | [rgw.md#SP_rgw_keystone_url](../../../config/rgw/rgw.md#SP_rgw_keystone_url) |

**What it does:** The URL to the Keystone server.

**When to use:** Set when integrating with an external service; leave empty if the feature is unused.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_url "https://keystone.example.com:5000/v3/"
ceph config get client.rgw rgw_keystone_url
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
ceph config get client.rgw rgw_keystone_url
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_verify_ssl

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_keystone_verify_ssl](../../../config/rgw/rgw.md#SP_rgw_keystone_verify_ssl) |

**What it does:** Should RGW verify the Keystone server SSL certificate.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_keystone_verify_ssl false
ceph config get client.rgw rgw_keystone_verify_ssl
```

**Finding optimal value:**

**Tuning model:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_sts_client_id

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_sts_client_id](../../../config/rgw/rgw.md#SP_rgw_sts_client_id) |

**What it does:** Client Id

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_sts_client_id <value>
ceph config get client.rgw rgw_sts_client_id
```

**Finding optimal value:**

**Tuning model:** Policy

1. Upstream default (`(empty)`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---

### rgw_sts_client_secret

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_sts_client_secret](../../../config/rgw/rgw.md#SP_rgw_sts_client_secret) |

**What it does:** Client Secret

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_sts_client_secret "<from-secrets-manager>"
ceph config get client.rgw rgw_sts_client_secret
```

**Finding optimal value:**

**Tuning model:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_sts_entry

| | |
|---|---|
| Type | Str · default `sts` · **Advanced** |
| Table | [rgw.md#SP_rgw_sts_entry](../../../config/rgw/rgw.md#SP_rgw_sts_entry) |

**What it does:** STS URL prefix

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_sts_entry sts
ceph config get client.rgw rgw_sts_entry
```

**Finding optimal value:**

**Tuning model:** Policy

1. Upstream default (`sts`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---

### rgw_sts_key

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_sts_key](../../../config/rgw/rgw.md#SP_rgw_sts_key) |

**What it does:** STS Key

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_sts_key "<from-secrets-manager>"
ceph config get client.rgw rgw_sts_key
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_sts_key
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_sts_max_session_duration

| | |
|---|---|
| Type | Uint · default `43200` · **Advanced** |
| Table | [rgw.md#SP_rgw_sts_max_session_duration](../../../config/rgw/rgw.md#SP_rgw_sts_max_session_duration) |

**What it does:** Session token max duration

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_sts_max_session_duration 43200
ceph config get client.rgw rgw_sts_max_session_duration
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `43200` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_sts_min_session_duration

| | |
|---|---|
| Type | Uint · default `900` · **Advanced** |
| Table | [rgw.md#SP_rgw_sts_min_session_duration](../../../config/rgw/rgw.md#SP_rgw_sts_min_session_duration) |

**What it does:** Minimum allowed duration of a session

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_sts_min_session_duration 900
ceph config get client.rgw rgw_sts_min_session_duration
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `900`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_sts_min_session_duration
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_sts_token_introspection_url

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_sts_token_introspection_url](../../../config/rgw/rgw.md#SP_rgw_sts_token_introspection_url) |

**What it does:** STS Web Token introspection URL

**When to use:** Set when integrating with an external service; leave empty if the feature is unused.

**Example:**

```bash
ceph config set client.rgw rgw_sts_token_introspection_url "https://idp.example.com/oauth2/introspect"
ceph config get client.rgw rgw_sts_token_introspection_url
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
ceph config get client.rgw rgw_sts_token_introspection_url
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](../OVERVIEW.md)
