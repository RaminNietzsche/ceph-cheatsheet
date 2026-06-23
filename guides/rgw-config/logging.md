# Access and object logging

RGW config deep dive — 4 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_log_http_headers](#rgw_log_http_headers) | `(empty)` | Basic | Performance |
| [rgw_log_nonexistent_bucket](#rgw_log_nonexistent_bucket) | `False` | Advanced | Policy |
| [rgw_log_object_name](#rgw_log_object_name) | `%Y-%m-%d-%H-%i-%n` | Advanced | Performance |
| [rgw_log_object_name_utc](#rgw_log_object_name_utc) | `False` | Advanced | Policy |

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

### rgw_log_http_headers

| | |
|---|---|
| Type | Str · default `(empty)` · **Basic** |
| Table | [rgw.md#SP_rgw_log_http_headers](../../config/rgw/rgw.md#SP_rgw_log_http_headers) |

**What it does:** List of HTTP headers to log

**When to use:** Core RGW behavior — review before changing in production.

**Example:**

```bash
ceph config set client.rgw rgw_log_http_headers <value>
ceph config get client.rgw rgw_log_http_headers
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_log_http_headers
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_log_nonexistent_bucket

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_log_nonexistent_bucket](../../config/rgw/rgw.md#SP_rgw_log_nonexistent_bucket) |

**What it does:** Should RGW log operations on bucket that does not exist

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_log_nonexistent_bucket False
ceph config get client.rgw rgw_log_nonexistent_bucket
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_log_object_name

| | |
|---|---|
| Type | Str · default `%Y-%m-%d-%H-%i-%n` · **Advanced** |
| Table | [rgw.md#SP_rgw_log_object_name](../../config/rgw/rgw.md#SP_rgw_log_object_name) |

**What it does:** Ops log object name format

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_log_object_name %Y-%m-%d-%H-%i-%n
ceph config get client.rgw rgw_log_object_name
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `%Y-%m-%d-%H-%i-%n`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_log_object_name
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_log_object_name_utc

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_log_object_name_utc](../../config/rgw/rgw.md#SP_rgw_log_object_name_utc) |

**What it does:** Should ops log object name based on UTC

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_log_object_name_utc False
ceph config get client.rgw rgw_log_object_name_utc
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← RGW config overview](OVERVIEW.md)
