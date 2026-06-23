# Device

Global config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [device_failure_prediction_mode](#device_failure_prediction_mode) | `none` | Basic | Policy |

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

### device_failure_prediction_mode

| | |
|---|---|
| Type | Str · enum: ["none", "local", "cloud"] · default `none` · **Basic** |
| Table | [device.md#SP_device_failure_prediction_mode](../../../config/global/device.md#SP_device_failure_prediction_mode) |

**What it does:** Method used to predict device failures

**When to use:** Core Global behavior — review before changing in production.

**Example:**

```bash
ceph config set global device_failure_prediction_mode none
ceph config get global device_failure_prediction_mode
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `none` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global device_failure_prediction_mode
ceph -s
```

---


[← Overview](../OVERVIEW.md)
