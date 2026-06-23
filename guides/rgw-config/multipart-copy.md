# Multipart & copy

RGW config deep dive — 4 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_copy_obj_progress](#rgw_copy_obj_progress) | `True` | Advanced | Policy |
| [rgw_copy_obj_progress_every_bytes](#rgw_copy_obj_progress_every_bytes) | `1_M` | Advanced | Performance |
| [rgw_multipart_min_part_size](#rgw_multipart_min_part_size) | `5_M` | Advanced | Performance |
| [rgw_multipart_part_upload_limit](#rgw_multipart_part_upload_limit) | `10000` | Advanced | Policy |

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
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph osd pool stats
```

---

### rgw_copy_obj_progress

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_copy_obj_progress](../../config/rgw/rgw.md#SP_rgw_copy_obj_progress) |

**What it does:** Send progress report through copy operation

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_copy_obj_progress True
ceph config get client.rgw rgw_copy_obj_progress
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_copy_obj_progress_every_bytes

| | |
|---|---|
| Type | Size · default `1_M` · **Advanced** |
| Table | [rgw.md#SP_rgw_copy_obj_progress_every_bytes](../../config/rgw/rgw.md#SP_rgw_copy_obj_progress_every_bytes) |

**What it does:** Send copy-object progress info after these many bytes

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_copy_obj_progress_every_bytes 1_M
ceph config get client.rgw rgw_copy_obj_progress_every_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_M`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_copy_obj_progress_every_bytes
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_multipart_min_part_size

| | |
|---|---|
| Type | Size · default `5_M` · **Advanced** |
| Table | [rgw.md#SP_rgw_multipart_min_part_size](../../config/rgw/rgw.md#SP_rgw_multipart_min_part_size) |

**What it does:** Minimum S3 multipart-upload part size

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_multipart_min_part_size 5_M
ceph config get client.rgw rgw_multipart_min_part_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5_M`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_multipart_min_part_size
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_multipart_part_upload_limit

| | |
|---|---|
| Type | Int · default `10000` · **Advanced** |
| Table | [rgw.md#SP_rgw_multipart_part_upload_limit](../../config/rgw/rgw.md#SP_rgw_multipart_part_upload_limit) |

**What it does:** Max number of parts in multipart upload

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_multipart_part_upload_limit 10000
ceph config get client.rgw rgw_multipart_part_upload_limit
```

**Finding optimal value:**

**Tuning model:** Policy

1. Upstream default (`10000`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---


[← RGW config overview](OVERVIEW.md)
