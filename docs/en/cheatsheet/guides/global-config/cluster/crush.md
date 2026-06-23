# Crush

Global config deep dive — 3 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [crush_location](#crush_location) | `(empty)` | Advanced | Performance |
| [crush_location_hook](#crush_location_hook) | `(empty)` | Advanced | Performance |
| [crush_location_hook_timeout](#crush_location_hook_timeout) | `10` | Advanced | Performance |

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

### crush_location

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [crush.md#SP_crush_location](../../../config/global/crush.md#SP_crush_location) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global crush_location "example"
ceph config get global crush_location
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global crush_location
ceph -s
```

---

### crush_location_hook

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [crush.md#SP_crush_location_hook](../../../config/global/crush.md#SP_crush_location_hook) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global crush_location_hook "example"
ceph config get global crush_location_hook
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global crush_location_hook
ceph -s
```

---

### crush_location_hook_timeout

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [crush.md#SP_crush_location_hook_timeout](../../../config/global/crush.md#SP_crush_location_hook_timeout) |

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global crush_location_hook_timeout 10
ceph config get global crush_location_hook_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global crush_location_hook_timeout
ceph -s
```

---


[← Overview](../OVERVIEW.md)
