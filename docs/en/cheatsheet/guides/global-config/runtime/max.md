# Max

Global config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [max_rotating_auth_attempts](#max_rotating_auth_attempts) | `10` | Advanced | Performance |

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

### max_rotating_auth_attempts

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [max.md#SP_max_rotating_auth_attempts](../../../config/global/max.md#SP_max_rotating_auth_attempts) |

**What it does:** Mumber of attempts to initialize rotating keys before giving up

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global max_rotating_auth_attempts 10
ceph config get global max_rotating_auth_attempts
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global max_rotating_auth_attempts
ceph -s
```

---


[← Overview](../OVERVIEW.md)
