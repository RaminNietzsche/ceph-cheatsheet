# Rotating

Global config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rotating_keys_bootstrap_timeout](#rotating_keys_bootstrap_timeout) | `30` | Advanced | Performance |
| [rotating_keys_renewal_timeout](#rotating_keys_renewal_timeout) | `10` | Advanced | Performance |

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

### rotating_keys_bootstrap_timeout

| | |
|---|---|
| Type | Int · default `30` · **Advanced** |
| Table | [rotating.md#SP_rotating_keys_bootstrap_timeout](../../../config/global/rotating.md#SP_rotating_keys_bootstrap_timeout) |

**What it does:** Timeout for obtaining rotating keys during bootstrap phase (seconds)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global rotating_keys_bootstrap_timeout 30
ceph config get global rotating_keys_bootstrap_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rotating_keys_bootstrap_timeout
ceph -s
```

---

### rotating_keys_renewal_timeout

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [rotating.md#SP_rotating_keys_renewal_timeout](../../../config/global/rotating.md#SP_rotating_keys_renewal_timeout) |

**What it does:** Timeout for updating rotating keys (seconds)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global rotating_keys_renewal_timeout 10
ceph config get global rotating_keys_renewal_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rotating_keys_renewal_timeout
ceph -s
```

---


[← Overview](../OVERVIEW.md)
