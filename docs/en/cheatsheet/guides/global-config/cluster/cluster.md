# Cluster

Global config deep dive — 3 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [cluster_addr](#cluster_addr) | `(empty)` | Basic | Connectivity |
| [cluster_network](#cluster_network) | `(empty)` | Advanced | Performance |
| [cluster_network_interface](#cluster_network_interface) | `(empty)` | Advanced | Performance |

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

### cluster_addr

| | |
|---|---|
| Type | Addr · default `(empty)` · **Basic** · **STARTUP** (restart required) |
| Table | [cluster.md#SP_cluster_addr](../../../config/global/cluster.md#SP_cluster_addr) |

**What it does:** Cluster-facing address to bind to

**When to use:** Set when integrating with an external service; leave empty if unused.

**Example:**

```bash
ceph config set global cluster_addr (empty)
ceph config get global cluster_addr
```

**Finding optimal value:**

**Tuning model:** Connectivity

1. List candidate endpoints from your environment.
2. Verify reachability from every node running the daemon.
3. Pick the lowest-latency stable endpoint.
4. Leave empty (`(empty)`) if the integration is disabled.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global cluster_addr
ceph -s
```

---

### cluster_network

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** · **STARTUP** (restart required) |
| Table | [cluster.md#SP_cluster_network](../../../config/global/cluster.md#SP_cluster_network) |

**What it does:** Network(s) from which to choose a cluster address to bind to

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global cluster_network "example"
ceph config get global cluster_network
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global cluster_network
ceph -s
```

---

### cluster_network_interface

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** · **STARTUP** (restart required) |
| Table | [cluster.md#SP_cluster_network_interface](../../../config/global/cluster.md#SP_cluster_network_interface) |

**What it does:** Interface name(s) from which to choose an address from a ``cluster_network`` to bind to; ``cluster_network`` must also be specified.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global cluster_network_interface "example"
ceph config get global cluster_network_interface
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global cluster_network_interface
ceph -s
```

---


[← Overview](../OVERVIEW.md)
