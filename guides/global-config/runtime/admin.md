# Admin

Global config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [admin_socket](#admin_socket) | `$run_dir/$cluster-$name.asok` | Advanced | Performance |
| [admin_socket_mode](#admin_socket_mode) | `(empty)` | Advanced | Performance |

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

### admin_socket

| | |
|---|---|
| Type | Str · default `$run_dir/$cluster-$name.asok` · **Advanced** · **STARTUP** (restart required) |
| Table | [admin.md#SP_admin_socket](../../../config/global/admin.md#SP_admin_socket) |

**What it does:** Path for the runtime control socket file, used by the 'ceph daemon' command

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global admin_socket "$run_dir/$cluster-$name.asok"
ceph config get global admin_socket
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `$run_dir/$cluster-$name.asok`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global admin_socket
ceph -s
```

---

### admin_socket_mode

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** · **STARTUP** (restart required) |
| Table | [admin.md#SP_admin_socket_mode](../../../config/global/admin.md#SP_admin_socket_mode) |

**What it does:** File mode to set for the admin socket, e.g, '0755'

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global admin_socket_mode "example"
ceph config get global admin_socket_mode
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global admin_socket_mode
ceph -s
```

---


[← Overview](../OVERVIEW.md)
