# Gss

Global config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [gss_ktab_client_file](#gss_ktab_client_file) | `/var/lib/ceph/$name/gss_client_$name.ktab` | Advanced | Capacity |
| [gss_target_name](#gss_target_name) | `ceph` | Advanced | Performance |

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

### gss_ktab_client_file

| | |
|---|---|
| Type | Str · default `/var/lib/ceph/$name/gss_client_$name.ktab` · **Advanced** |
| Table | [gss.md#SP_gss_ktab_client_file](../../../config/global/gss.md#SP_gss_ktab_client_file) |

**What it does:** GSS/KRB5 Keytab file for client authentication

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global gss_ktab_client_file "/var/lib/ceph/$name/gss_client_$name.ktab"
ceph config get global gss_ktab_client_file
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `/var/lib/ceph/$name/gss_client_$name.ktab`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global gss_ktab_client_file
ceph -s
```

---

### gss_target_name

| | |
|---|---|
| Type | Str · default `ceph` · **Advanced** |
| Table | [gss.md#SP_gss_target_name](../../../config/global/gss.md#SP_gss_target_name) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global gss_target_name ceph
ceph config get global gss_target_name
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `ceph`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global gss_target_name
ceph -s
```

---


[← Overview](../OVERVIEW.md)
