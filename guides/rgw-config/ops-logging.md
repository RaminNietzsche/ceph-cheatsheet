# Ops logging

RGW config deep dive — 4 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_ops_log_data_backlog](#rgw_ops_log_data_backlog) | `5_M` | Advanced |
| [rgw_ops_log_file_path](#rgw_ops_log_file_path) | `/var/log/ceph/ops-log-$cluster-$name.log` | Advanced |
| [rgw_ops_log_rados](#rgw_ops_log_rados) | `False` | Advanced |
| [rgw_ops_log_socket_path](#rgw_ops_log_socket_path) | `(empty)` | Advanced |

---

### rgw_ops_log_data_backlog

| | |
|---|---|
| Type | Size · default `5_M` · **Advanced** |
| Table | [rgw.md#SP_rgw_ops_log_data_backlog](../../config/rgw/rgw.md#SP_rgw_ops_log_data_backlog) |

**What it does:** Ops log socket backlog

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_ops_log_data_backlog 5_M
ceph config get client.rgw rgw_ops_log_data_backlog
```

**Finding optimal value:** Start from upstream default (`5_M`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_ops_log_file_path

| | |
|---|---|
| Type | Str · default `/var/log/ceph/ops-log-$cluster-$name.log` · **Advanced** |
| Table | [rgw.md#SP_rgw_ops_log_file_path](../../config/rgw/rgw.md#SP_rgw_ops_log_file_path) |

**What it does:** File-system path for ops log.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_ops_log_file_path "/var/log/ceph/ops-log-$cluster-$name.log"
ceph config get client.rgw rgw_ops_log_file_path
```

**Finding optimal value:** Place on fast, dedicated storage with sufficient free space. Default (`/var/log/ceph/ops-log-$cluster-$name.log`) is fine when that path is on a separate volume.

---

### rgw_ops_log_rados

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_ops_log_rados](../../config/rgw/rgw.md#SP_rgw_ops_log_rados) |

**What it does:** Use RADOS for ops log

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_ops_log_rados False
ceph config get client.rgw rgw_ops_log_rados
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

---

### rgw_ops_log_socket_path

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_ops_log_socket_path](../../config/rgw/rgw.md#SP_rgw_ops_log_socket_path) |

**What it does:** Unix domain socket path for ops log.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_ops_log_socket_path <value>
ceph config get client.rgw rgw_ops_log_socket_path
```

**Finding optimal value:** Place on fast, dedicated storage with sufficient free space. Default (`(empty)`) is fine when that path is on a separate volume.

---


[← RGW config overview](OVERVIEW.md)
