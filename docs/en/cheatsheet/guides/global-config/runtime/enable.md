# Enable

Global config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [enable_experimental_unrecoverable_data_corrupting_features](#enable_experimental_unrecoverable_data_corrupting_features) | `(empty)` | Advanced | Performance |

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

### enable_experimental_unrecoverable_data_corrupting_features

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [enable.md#SP_enable_experimental_unrecoverable_data_corrupting_features](../../../config/global/enable.md#SP_enable_experimental_unrecoverable_data_corrupting_features) |

**What it does:** Enable named (or all with '*') experimental features that may be untested, dangerous, and/or cause permanent data loss

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global enable_experimental_unrecoverable_data_corrupting_features "example"
ceph config get global enable_experimental_unrecoverable_data_corrupting_features
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global enable_experimental_unrecoverable_data_corrupting_features
ceph -s
```

---


[← Overview](../OVERVIEW.md)
