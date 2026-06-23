# Restapi

Global config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [restapi_base_url](#restapi_base_url) | `(empty)` | Advanced | Connectivity |
| [restapi_log_level](#restapi_log_level) | `(empty)` | Advanced | Performance |

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

### restapi_base_url

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [restapi.md#SP_restapi_base_url](../../../config/global/restapi.md#SP_restapi_base_url) |

**What it does:** default set by python code

**When to use:** Set when integrating with an external service; leave empty if unused.

**Example:**

```bash
ceph config set global restapi_base_url "https://example.com/"
ceph config get global restapi_base_url
```

**Finding optimal value:**

**Tuning model:** Connectivity

1. List candidate endpoints from your environment.
2. Verify reachability from every node running the daemon.
3. Pick the lowest-latency stable endpoint.
4. Leave empty (`(empty)`) if the integration is disabled.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global restapi_base_url
ceph -s
```

---

### restapi_log_level

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [restapi.md#SP_restapi_log_level](../../../config/global/restapi.md#SP_restapi_log_level) |

**What it does:** default set by python code

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global restapi_log_level "example"
ceph config get global restapi_log_level
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global restapi_log_level
ceph -s
```

---


[← Overview](../OVERVIEW.md)
