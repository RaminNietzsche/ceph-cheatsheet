# Cephx

Global config deep dive — 7 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [cephx_cluster_require_signatures](#cephx_cluster_require_signatures) | `False` | Advanced | Performance |
| [cephx_cluster_require_version](#cephx_cluster_require_version) | `2` | Advanced | Performance |
| [cephx_require_signatures](#cephx_require_signatures) | `False` | Advanced | Performance |
| [cephx_require_version](#cephx_require_version) | `2` | Advanced | Performance |
| [cephx_service_require_signatures](#cephx_service_require_signatures) | `False` | Advanced | Performance |
| [cephx_service_require_version](#cephx_service_require_version) | `2` | Advanced | Performance |
| [cephx_sign_messages](#cephx_sign_messages) | `True` | Advanced | Performance |

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

### cephx_cluster_require_signatures

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [cephx.md#SP_cephx_cluster_require_signatures](../../../config/global/cephx.md#SP_cephx_cluster_require_signatures) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global cephx_cluster_require_signatures true
ceph config get global cephx_cluster_require_signatures
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global cephx_cluster_require_signatures
ceph -s
```

---

### cephx_cluster_require_version

| | |
|---|---|
| Type | Int · default `2` · **Advanced** |
| Table | [cephx.md#SP_cephx_cluster_require_version](../../../config/global/cephx.md#SP_cephx_cluster_require_version) |

**What it does:** Cephx version required by the cluster from clients (1 = pre-mimic, 2 = mimic+)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global cephx_cluster_require_version 2
ceph config get global cephx_cluster_require_version
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global cephx_cluster_require_version
ceph -s
```

---

### cephx_require_signatures

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [cephx.md#SP_cephx_require_signatures](../../../config/global/cephx.md#SP_cephx_require_signatures) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global cephx_require_signatures true
ceph config get global cephx_require_signatures
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global cephx_require_signatures
ceph -s
```

---

### cephx_require_version

| | |
|---|---|
| Type | Int · default `2` · **Advanced** |
| Table | [cephx.md#SP_cephx_require_version](../../../config/global/cephx.md#SP_cephx_require_version) |

**What it does:** Cephx version required (1 = pre-mimic, 2 = mimic+)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global cephx_require_version 2
ceph config get global cephx_require_version
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global cephx_require_version
ceph -s
```

---

### cephx_service_require_signatures

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [cephx.md#SP_cephx_service_require_signatures](../../../config/global/cephx.md#SP_cephx_service_require_signatures) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global cephx_service_require_signatures true
ceph config get global cephx_service_require_signatures
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global cephx_service_require_signatures
ceph -s
```

---

### cephx_service_require_version

| | |
|---|---|
| Type | Int · default `2` · **Advanced** |
| Table | [cephx.md#SP_cephx_service_require_version](../../../config/global/cephx.md#SP_cephx_service_require_version) |

**What it does:** Cephx version required from ceph services (1 = pre-mimic, 2 = mimic+)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global cephx_service_require_version 2
ceph config get global cephx_service_require_version
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global cephx_service_require_version
ceph -s
```

---

### cephx_sign_messages

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [cephx.md#SP_cephx_sign_messages](../../../config/global/cephx.md#SP_cephx_sign_messages) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global cephx_sign_messages false
ceph config get global cephx_sign_messages
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global cephx_sign_messages
ceph -s
```

---


[← Overview](../OVERVIEW.md)
