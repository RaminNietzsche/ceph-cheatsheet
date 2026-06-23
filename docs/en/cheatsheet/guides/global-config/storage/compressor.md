# Compressor

Global config deep dive — 4 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [compressor_zlib_isal](#compressor_zlib_isal) | `False` | Advanced | Performance |
| [compressor_zlib_level](#compressor_zlib_level) | `5` | Advanced | Performance |
| [compressor_zlib_winsize](#compressor_zlib_winsize) | `-15` | Advanced | Performance |
| [compressor_zstd_level](#compressor_zstd_level) | `1` | Advanced | Performance |

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

### compressor_zlib_isal

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [compressor.md#SP_compressor_zlib_isal](../../../config/global/compressor.md#SP_compressor_zlib_isal) |

**What it does:** Use Intel ISA-L accelerated zlib implementation if available

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global compressor_zlib_isal true
ceph config get global compressor_zlib_isal
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global compressor_zlib_isal
ceph -s
```

---

### compressor_zlib_level

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [compressor.md#SP_compressor_zlib_level](../../../config/global/compressor.md#SP_compressor_zlib_level) |

**What it does:** Zlib compression level to use

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global compressor_zlib_level 5
ceph config get global compressor_zlib_level
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global compressor_zlib_level
ceph -s
```

---

### compressor_zlib_winsize

| | |
|---|---|
| Type | Int · default `-15` · **Advanced** |
| Table | [compressor.md#SP_compressor_zlib_winsize](../../../config/global/compressor.md#SP_compressor_zlib_winsize) |

**What it does:** Zlib compression winsize to use

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global compressor_zlib_winsize -15
ceph config get global compressor_zlib_winsize
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `-15`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `-15`, max `32`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global compressor_zlib_winsize
ceph -s
```

---

### compressor_zstd_level

| | |
|---|---|
| Type | Int · default `1` · **Advanced** |
| Table | [compressor.md#SP_compressor_zstd_level](../../../config/global/compressor.md#SP_compressor_zstd_level) |

**What it does:** Zstd compression level to use

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global compressor_zstd_level 1
ceph config get global compressor_zstd_level
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global compressor_zstd_level
ceph -s
```

---


[← Overview](../OVERVIEW.md)
