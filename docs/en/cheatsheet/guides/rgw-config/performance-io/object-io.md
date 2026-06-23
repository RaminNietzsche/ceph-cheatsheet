# Object read/write windows

RGW config deep dive — 4 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_get_obj_max_req_size](#rgw_get_obj_max_req_size) | `4_M` | Advanced | Policy |
| [rgw_get_obj_window_size](#rgw_get_obj_window_size) | `16_M` | Advanced | Performance |
| [rgw_put_obj_max_window_size](#rgw_put_obj_max_window_size) | `64_M` | Advanced | Performance |
| [rgw_put_obj_min_window_size](#rgw_put_obj_min_window_size) | `16_M` | Advanced | Performance |

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

### rgw_get_obj_max_req_size

| | |
|---|---|
| Type | Size · default `4_M` · **Advanced** |
| Table | [rgw.md#SP_rgw_get_obj_max_req_size](../../../config/rgw/rgw.md#SP_rgw_get_obj_max_req_size) |

**What it does:** RGW object read chunk size

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_get_obj_max_req_size 4_M
ceph config get client.rgw rgw_get_obj_max_req_size
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `4_M` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_get_obj_window_size

| | |
|---|---|
| Type | Size · default `16_M` · **Advanced** |
| Table | [rgw.md#SP_rgw_get_obj_window_size](../../../config/rgw/rgw.md#SP_rgw_get_obj_window_size) |

**What it does:** RGW object read window size

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_get_obj_window_size 16_M
ceph config get client.rgw rgw_get_obj_window_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline `16_M` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**Signals:** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_get_obj_window_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_put_obj_max_window_size

| | |
|---|---|
| Type | Size · default `64_M` · **Advanced** |
| Table | [rgw.md#SP_rgw_put_obj_max_window_size](../../../config/rgw/rgw.md#SP_rgw_put_obj_max_window_size) |

**What it does:** The maximum RADOS write window size (in bytes).

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_put_obj_max_window_size 64_M
ceph config get client.rgw rgw_put_obj_max_window_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline `64_M` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**Signals:** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_put_obj_max_window_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_put_obj_min_window_size

| | |
|---|---|
| Type | Size · default `16_M` · **Advanced** |
| Table | [rgw.md#SP_rgw_put_obj_min_window_size](../../../config/rgw/rgw.md#SP_rgw_put_obj_min_window_size) |

**What it does:** The minimum RADOS write window size (in bytes).

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_put_obj_min_window_size 16_M
ceph config get client.rgw rgw_put_obj_min_window_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline `16_M` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**Signals:** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_put_obj_min_window_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](../OVERVIEW.md)
