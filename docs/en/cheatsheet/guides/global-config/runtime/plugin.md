# Plugin

Global config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [plugin_crypto_accelerator](#plugin_crypto_accelerator) | `crypto_isal` | Advanced | Performance |
| [plugin_dir](#plugin_dir) | `0` | Advanced | Capacity |

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

### plugin_crypto_accelerator

| | |
|---|---|
| Type | Str · default `crypto_isal` · **Advanced** |
| Table | [plugin.md#SP_plugin_crypto_accelerator](../../../config/global/plugin.md#SP_plugin_crypto_accelerator) |

**What it does:** Crypto accelerator library to use

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global plugin_crypto_accelerator crypto_isal
ceph config get global plugin_crypto_accelerator
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `crypto_isal`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global plugin_crypto_accelerator
ceph -s
```

---

### plugin_dir

| | |
|---|---|
| Type | Str · default `0` · **Advanced** · **STARTUP** (restart required) |
| Table | [plugin.md#SP_plugin_dir](../../../config/global/plugin.md#SP_plugin_dir) |

**What it does:** Base directory for dynamically loaded plugins

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global plugin_dir "/var/lib/ceph/example"
ceph config get global plugin_dir
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `0`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global plugin_dir
ceph -s
```

---


[← Overview](../OVERVIEW.md)
