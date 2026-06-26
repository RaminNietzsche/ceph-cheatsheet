# Public

Global config deep dive — 5 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [public_addr](#public_addr) | `(empty)` | Basic | Connectivity |
| [public_addrv](#public_addrv) | `(empty)` | Basic | Policy |
| [public_bind_addr](#public_bind_addr) | `(empty)` | Advanced | Connectivity |
| [public_network](#public_network) | `(empty)` | Advanced | Performance |
| [public_network_interface](#public_network_interface) | `(empty)` | Advanced | Performance |

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

### public_addr

| | |
|---|---|
| Type | Addr · default `(empty)` · **Basic** · **STARTUP** (restart required) |
| Table | [public.md#SP_public_addr](../../../config/global/public.md#SP_public_addr) |

**What it does:** Public-facing address to which to bind

**When to use:** Set when integrating with an external service; leave empty if unused.

**Example:**

```bash
ceph config set global public_addr (empty)
ceph config get global public_addr
```

**Finding optimal value:**

**Tuning model:** Connectivity

1. List candidate endpoints from your environment.
2. Verify reachability from every node running the daemon.
3. Pick the lowest-latency stable endpoint.
4. Leave empty (`(empty)`) if the integration is disabled.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global public_addr
ceph -s
```

---

### public_addrv

| | |
|---|---|
| Type | Addrvec · default `(empty)` · **Basic** · **STARTUP** (restart required) |
| Table | [public.md#SP_public_addrv](../../../config/global/public.md#SP_public_addrv) |

**What it does:** Public-facing addresses to which services are to bind

**When to use:** Core Global behavior — review before changing in production.

**Example:**

```bash
ceph config set global public_addrv (empty)
ceph config get global public_addrv
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `(empty)` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global public_addrv
ceph -s
```

---

### public_bind_addr

| | |
|---|---|
| Type | Addr · default `(empty)` · **Advanced** · **STARTUP** (restart required) |
| Table | [public.md#SP_public_bind_addr](../../../config/global/public.md#SP_public_bind_addr) |

**When to use:** Set when integrating with an external service; leave empty if unused.

**Example:**

```bash
ceph config set global public_bind_addr (empty)
ceph config get global public_bind_addr
```

**Finding optimal value:**

**Tuning model:** Connectivity

1. List candidate endpoints from your environment.
2. Verify reachability from every node running the daemon.
3. Pick the lowest-latency stable endpoint.
4. Leave empty (`(empty)`) if the integration is disabled.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global public_bind_addr
ceph -s
```

---

### public_network

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** · **STARTUP** (restart required) |
| Table | [public.md#SP_public_network](../../../config/global/public.md#SP_public_network) |

**What it does:** Network(s) from which to choose a public address to bind to

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global public_network "example"
ceph config get global public_network
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global public_network
ceph -s
```

---

### public_network_interface

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** · **STARTUP** (restart required) |
| Table | [public.md#SP_public_network_interface](../../../config/global/public.md#SP_public_network_interface) |

**What it does:** Interface name(s) from which to choose an address from a ``public_network`` to bind to; ``public_network`` must also be specified.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`public_network`](../../../config/global/public.md#SP_public_network)

**Example:**

```bash
ceph config set global public_network_interface "example"
ceph config get global public_network_interface
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global public_network_interface
ceph -s
```

---


[← Overview](../OVERVIEW.md)
