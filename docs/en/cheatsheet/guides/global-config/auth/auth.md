# Auth

Global config deep dive — 9 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [auth_allow_insecure_global_id_reclaim](#auth_allow_insecure_global_id_reclaim) | `True` | Advanced | Policy |
| [auth_client_required](#auth_client_required) | `cephx, none` | Advanced | Performance |
| [auth_cluster_required](#auth_cluster_required) | `cephx` | Advanced | Performance |
| [auth_debug](#auth_debug) | `False` | Dev | Dev |
| [auth_expose_insecure_global_id_reclaim](#auth_expose_insecure_global_id_reclaim) | `True` | Advanced | Policy |
| [auth_mon_ticket_ttl](#auth_mon_ticket_ttl) | `72_hr` | Advanced | Performance |
| [auth_service_required](#auth_service_required) | `cephx` | Advanced | Performance |
| [auth_service_ticket_ttl](#auth_service_ticket_ttl) | `1_hr` | Advanced | Performance |
| [auth_supported](#auth_supported) | `(empty)` | Advanced | Performance |

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, compatibility, operational defaults |
| **Capacity** | Disk layout, paths, sizing |
| **Performance** | Baseline → incremental change → monitor cluster |
| **Connectivity** | Nearest stable external endpoint |
| **Dev** | Keep upstream default in production |

**Shared tooling:**

```bash
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### auth_allow_insecure_global_id_reclaim

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [auth.md#SP_auth_allow_insecure_global_id_reclaim](../../../config/global/auth.md#SP_auth_allow_insecure_global_id_reclaim) |

**What it does:** Allow reclaiming global_id without presenting a valid ticket proving previous possession of that global_id Allowing unauthorized global_id (re)use poses a security risk. Unfortunately, older clients may omit their ticket on reconnects and therefore rely on this being allowed for preserving their global_id for the lifetime of the client instance. Setting this value to false would immediately prevent new connections from those clients (assuming auth_expose_insecure_global_id_reclaim set to true) and eventually break existing sessions as well (regardless of auth_expose_insecure_global_id_reclaim setting).

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global auth_allow_insecure_global_id_reclaim false
ceph config get global auth_allow_insecure_global_id_reclaim
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global auth_allow_insecure_global_id_reclaim
ceph -s
```

---

### auth_client_required

| | |
|---|---|
| Type | Str · default `cephx, none` · **Advanced** |
| Table | [auth.md#SP_auth_client_required](../../../config/global/auth.md#SP_auth_client_required) |

**What it does:** Authentication methods allowed by clients

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global auth_client_required "cephx, none"
ceph config get global auth_client_required
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `cephx, none`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global auth_client_required
ceph -s
```

---

### auth_cluster_required

| | |
|---|---|
| Type | Str · default `cephx` · **Advanced** |
| Table | [auth.md#SP_auth_cluster_required](../../../config/global/auth.md#SP_auth_cluster_required) |

**What it does:** Authentication methods required by the cluster

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global auth_cluster_required cephx
ceph config get global auth_cluster_required
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `cephx`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global auth_cluster_required
ceph -s
```

---

### auth_debug

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [auth.md#SP_auth_debug](../../../config/global/auth.md#SP_auth_debug) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global auth_debug true
ceph config get global auth_debug
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### auth_expose_insecure_global_id_reclaim

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [auth.md#SP_auth_expose_insecure_global_id_reclaim](../../../config/global/auth.md#SP_auth_expose_insecure_global_id_reclaim) |

**What it does:** Force older clients that may omit their ticket on reconnects to reconnect as part of establishing a session In permissive mode (auth_allow_insecure_global_id_reclaim set to true), this helps with identifying clients that are not patched. In enforcing mode (auth_allow_insecure_global_id_reclaim set to false), this is a fail-fast mechanism: don't establish a session that will almost inevitably be broken later.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global auth_expose_insecure_global_id_reclaim false
ceph config get global auth_expose_insecure_global_id_reclaim
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global auth_expose_insecure_global_id_reclaim
ceph -s
```

---

### auth_mon_ticket_ttl

| | |
|---|---|
| Type | Float · default `72_hr` · **Advanced** |
| Table | [auth.md#SP_auth_mon_ticket_ttl](../../../config/global/auth.md#SP_auth_mon_ticket_ttl) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global auth_mon_ticket_ttl 72_hr
ceph config get global auth_mon_ticket_ttl
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `72_hr`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global auth_mon_ticket_ttl
ceph -s
```

---

### auth_service_required

| | |
|---|---|
| Type | Str · default `cephx` · **Advanced** |
| Table | [auth.md#SP_auth_service_required](../../../config/global/auth.md#SP_auth_service_required) |

**What it does:** Authentication methods required by service daemons

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global auth_service_required cephx
ceph config get global auth_service_required
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `cephx`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global auth_service_required
ceph -s
```

---

### auth_service_ticket_ttl

| | |
|---|---|
| Type | Float · default `1_hr` · **Advanced** |
| Table | [auth.md#SP_auth_service_ticket_ttl](../../../config/global/auth.md#SP_auth_service_ticket_ttl) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global auth_service_ticket_ttl 1_hr
ceph config get global auth_service_ticket_ttl
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_hr`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global auth_service_ticket_ttl
ceph -s
```

---

### auth_supported

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [auth.md#SP_auth_supported](../../../config/global/auth.md#SP_auth_supported) |

**What it does:** Authentication methods required (deprecated)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global auth_supported "example"
ceph config get global auth_supported
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global auth_supported
ceph -s
```

---


[← Overview](../OVERVIEW.md)
