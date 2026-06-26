# Host

Global config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [host](#host) | `(empty)` | Basic | Policy |

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

### host

| | |
|---|---|
| Type | Str · default `(empty)` · **Basic** |
| Table | [host.md#SP_host](../../../config/global/host.md#SP_host) |

**What it does:** local hostname If blank, Ceph uses the short hostname (hostname -s)

**When to use:** Core Global behavior — review before changing in production.

**Example:**

```bash
ceph config set global host "example"
ceph config get global host
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `(empty)` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global host
ceph -s
```

---


[← Overview](../OVERVIEW.md)
