# Jaeger

Global config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [jaeger_agent_port](#jaeger_agent_port) | `6799` | Advanced | Performance |
| [jaeger_tracing_enable](#jaeger_tracing_enable) | `False` | Advanced | Policy |

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

### jaeger_agent_port

| | |
|---|---|
| Type | Int · default `6799` · **Advanced** |
| Table | [jaeger.md#SP_jaeger_agent_port](../../../config/global/jaeger.md#SP_jaeger_agent_port) |

**What it does:** TCP port number of the Jaeger agent

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global jaeger_agent_port 6799
ceph config get global jaeger_agent_port
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `6799`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global jaeger_agent_port
ceph -s
```

---

### jaeger_tracing_enable

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [jaeger.md#SP_jaeger_tracing_enable](../../../config/global/jaeger.md#SP_jaeger_tracing_enable) |

**What it does:** Ceph should use the Jaeger tracing system

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global jaeger_tracing_enable true
ceph config get global jaeger_tracing_enable
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global jaeger_tracing_enable
ceph -s
```

---


[← Overview](../OVERVIEW.md)
