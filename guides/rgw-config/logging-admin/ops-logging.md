# Ops logging

RGW config deep dive — 4 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_ops_log_data_backlog](#rgw_ops_log_data_backlog) | `5_M` | Advanced | Performance |
| [rgw_ops_log_file_path](#rgw_ops_log_file_path) | `/var/log/ceph/ops-log-$cluster-$name.log` | Advanced | Capacity |
| [rgw_ops_log_rados](#rgw_ops_log_rados) | `False` | Advanced | Policy |
| [rgw_ops_log_socket_path](#rgw_ops_log_socket_path) | `(empty)` | Advanced | Capacity |

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, API compatibility, tenant limits |
| **Capacity** | Disk layout, paths, pool sizing |
| **Performance** | Baseline → incremental change → monitor OSD/RGW |
| **Connectivity** | Nearest stable external endpoint |
| **Architecture** | Backend, multisite topology — not numeric sweeps |
| **Dev** | Keep upstream default in production |

**Shared tooling:**

```bash
ceph config get client.rgw <option>
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph pg stat
```

---

### rgw_ops_log_data_backlog

| | |
|---|---|
| Type | Size · default `5_M` · **Advanced** |
| Table | [rgw.md#SP_rgw_ops_log_data_backlog](../../../config/rgw/rgw.md#SP_rgw_ops_log_data_backlog) |

**What it does:** Ops log socket backlog

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_ops_log_data_backlog 5_M
ceph config get client.rgw rgw_ops_log_data_backlog
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5_M`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_ops_log_data_backlog
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_ops_log_file_path

| | |
|---|---|
| Type | Str · default `/var/log/ceph/ops-log-$cluster-$name.log` · **Advanced** |
| Table | [rgw.md#SP_rgw_ops_log_file_path](../../../config/rgw/rgw.md#SP_rgw_ops_log_file_path) |

**What it does:** File-system path for ops log.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_ops_log_file_path "/var/log/ceph/ops-log-$cluster-$name.log"
ceph config get client.rgw rgw_ops_log_file_path
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`/var/log/ceph/ops-log-$cluster-$name.log`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw rgw_ops_log_file_path)
iostat -x 5  # disk saturation
```

---

### rgw_ops_log_rados

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_ops_log_rados](../../../config/rgw/rgw.md#SP_rgw_ops_log_rados) |

**What it does:** Use RADOS for ops log

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_ops_log_rados true
ceph config get client.rgw rgw_ops_log_rados
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_ops_log_socket_path

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_ops_log_socket_path](../../../config/rgw/rgw.md#SP_rgw_ops_log_socket_path) |

**What it does:** Unix domain socket path for ops log.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_ops_log_socket_path "/var/lib/ceph/radosgw"
ceph config get client.rgw rgw_ops_log_socket_path
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`(empty)`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw rgw_ops_log_socket_path)
iostat -x 5  # disk saturation
```

---


[← RGW config overview](../OVERVIEW.md)
