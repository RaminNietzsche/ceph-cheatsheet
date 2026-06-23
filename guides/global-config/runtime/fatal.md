# Fatal

Global config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [fatal_signal_handlers](#fatal_signal_handlers) | `True` | Advanced | Performance |

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

### fatal_signal_handlers

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** · **STARTUP** (restart required) |
| Table | [fatal.md#SP_fatal_signal_handlers](../../../config/global/fatal.md#SP_fatal_signal_handlers) |

**What it does:** Whether to register signal handlers for SIGABRT etc that dump a stack trace

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global fatal_signal_handlers false
ceph config get global fatal_signal_handlers
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global fatal_signal_handlers
ceph -s
```

---


[← Overview](../OVERVIEW.md)
