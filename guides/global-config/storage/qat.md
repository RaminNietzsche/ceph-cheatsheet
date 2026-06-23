# Qat

Global config deep dive — 3 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [qat_compressor_busy_polling](#qat_compressor_busy_polling) | `False` | Advanced | Performance |
| [qat_compressor_enabled](#qat_compressor_enabled) | `False` | Advanced | Policy |
| [qat_compressor_session_max_number](#qat_compressor_session_max_number) | `256` | Advanced | Performance |

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

### qat_compressor_busy_polling

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [qat.md#SP_qat_compressor_busy_polling](../../../config/global/qat.md#SP_qat_compressor_busy_polling) |

**What it does:** Set QAT busy bolling to reduce latency at the cost of potentially increasing CPU usage

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global qat_compressor_busy_polling true
ceph config get global qat_compressor_busy_polling
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global qat_compressor_busy_polling
ceph -s
```

---

### qat_compressor_enabled

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [qat.md#SP_qat_compressor_enabled](../../../config/global/qat.md#SP_qat_compressor_enabled) |

**What it does:** Enable Intel QAT acceleration support for compression if available

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global qat_compressor_enabled true
ceph config get global qat_compressor_enabled
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global qat_compressor_enabled
ceph -s
```

---

### qat_compressor_session_max_number

| | |
|---|---|
| Type | Uint · default `256` · **Advanced** |
| Table | [qat.md#SP_qat_compressor_session_max_number](../../../config/global/qat.md#SP_qat_compressor_session_max_number) |

**What it does:** Set the maximum number of session within Qatzip when using QAT compressor

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global qat_compressor_session_max_number 256
ceph config get global qat_compressor_session_max_number
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `256`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global qat_compressor_session_max_number
ceph -s
```

---


[← Overview](../OVERVIEW.md)
