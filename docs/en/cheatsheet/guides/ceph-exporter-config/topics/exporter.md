# ceph-exporter

Ceph exporter config deep dive — 8 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/ceph-exporter/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [exporter_addr](#exporter_addr) | `0.0.0.0` | Advanced | Connectivity |
| [exporter_cert_file](#exporter_cert_file) | `(empty)` | Advanced | Capacity |
| [exporter_http_port](#exporter_http_port) | `9926` | Advanced | Performance |
| [exporter_key_file](#exporter_key_file) | `(empty)` | Advanced | Capacity |
| [exporter_prio_limit](#exporter_prio_limit) | `5` | Advanced | Performance |
| [exporter_sock_dir](#exporter_sock_dir) | `/var/run/ceph/` | Advanced | Capacity |
| [exporter_sort_metrics](#exporter_sort_metrics) | `True` | Advanced | Performance |
| [exporter_stats_period](#exporter_stats_period) | `5` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. ceph-exporter
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### exporter_addr

| | |
|---|---|
| Type | Str · default `0.0.0.0` · **Advanced** |
| Table | [ceph-exporter.md#SP_exporter_addr](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_addr) |

**What it does:** Host ip address where exporter is deployed

**When to use:** Set when integrating with an external service; leave empty if unused.

**Example:**

```bash
ceph config set mgr exporter_addr "0.0.0.0"
ceph config get mgr exporter_addr
```

**Finding optimal value:**

**Tuning model:** Connectivity

1. List candidate endpoints from your environment.
2. Verify reachability from every node running the daemon.
3. Pick the lowest-latency stable endpoint.
4. Leave empty (`0.0.0.0`) if the integration is disabled.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr exporter_addr
ceph -s
ceph mgr stat
```

---

### exporter_cert_file

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [ceph-exporter.md#SP_exporter_cert_file](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_cert_file) |

**What it does:** Certificate file for TLS.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr exporter_cert_file "example"
ceph config get mgr exporter_cert_file
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `(empty)`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr exporter_cert_file
ceph -s
ceph mgr stat
```

---

### exporter_http_port

| | |
|---|---|
| Type | Int · default `9926` · **Advanced** |
| Table | [ceph-exporter.md#SP_exporter_http_port](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_http_port) |

**What it does:** Port to deploy exporter on. Default is 9926

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr exporter_http_port 9926
ceph config get mgr exporter_http_port
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `9926`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr exporter_http_port
ceph -s
ceph mgr stat
```

---

### exporter_key_file

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [ceph-exporter.md#SP_exporter_key_file](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_key_file) |

**What it does:** Key certificate file for TLS.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr exporter_key_file "example"
ceph config get mgr exporter_key_file
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `(empty)`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr exporter_key_file
ceph -s
ceph mgr stat
```

---

### exporter_prio_limit

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [ceph-exporter.md#SP_exporter_prio_limit](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_prio_limit) |

**What it does:** Only perf counters greater than or equal to exporter_prio_limit are fetched

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mgr exporter_prio_limit 5
ceph config get mgr exporter_prio_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr exporter_prio_limit
ceph -s
ceph mgr stat
```

---

### exporter_sock_dir

| | |
|---|---|
| Type | Str · default `/var/run/ceph/` · **Advanced** |
| Table | [ceph-exporter.md#SP_exporter_sock_dir](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_sock_dir) |

**What it does:** The path to ceph daemons socket files dir

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr exporter_sock_dir "/var/run/ceph/"
ceph config get mgr exporter_sock_dir
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `/var/run/ceph/`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr exporter_sock_dir
ceph -s
ceph mgr stat
```

---

### exporter_sort_metrics

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [ceph-exporter.md#SP_exporter_sort_metrics](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_sort_metrics) |

**What it does:** If true it will sort the metrics and group them.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mgr exporter_sort_metrics false
ceph config get mgr exporter_sort_metrics
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr exporter_sort_metrics
ceph -s
ceph mgr stat
```

---

### exporter_stats_period

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [ceph-exporter.md#SP_exporter_stats_period](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_stats_period) |

**What it does:** Time to wait before sending requests again to exporter server (seconds)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mgr exporter_stats_period 5
ceph config get mgr exporter_stats_period
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr exporter_stats_period
ceph -s
ceph mgr stat
```

---


[← Overview](../OVERVIEW.md)
