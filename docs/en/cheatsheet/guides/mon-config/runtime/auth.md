# Auth & caps

MON config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mon_auth_validate_all_caps](#mon_auth_validate_all_caps) | `True` | Advanced | Policy |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_auth_validate_all_caps

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_auth_validate_all_caps](../../../config/mon/mon.md#SP_mon_auth_validate_all_caps) |

**What it does:** Whether to parse non-monitor capabilities set by the 'ceph auth ...' commands. Disabling this saves CPU on the monitor, but allows invalid capabilities to be set, and only be rejected later, when they are used.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_auth_validate_all_caps false
ceph config get mon mon_auth_validate_all_caps
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_auth_validate_all_caps
ceph -s
ceph mon stat
```

---


[← Overview](../OVERVIEW.md)
