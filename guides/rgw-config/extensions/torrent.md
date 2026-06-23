# BitTorrent

RGW config deep dive — 8 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_torrent_comment](#rgw_torrent_comment) | `(empty)` | Advanced | Performance |
| [rgw_torrent_createby](#rgw_torrent_createby) | `(empty)` | Advanced | Performance |
| [rgw_torrent_encoding](#rgw_torrent_encoding) | `(empty)` | Advanced | Performance |
| [rgw_torrent_flag](#rgw_torrent_flag) | `False` | Advanced | Policy |
| [rgw_torrent_max_size](#rgw_torrent_max_size) | `5_G` | Advanced | Policy |
| [rgw_torrent_origin](#rgw_torrent_origin) | `(empty)` | Advanced | Performance |
| [rgw_torrent_sha_unit](#rgw_torrent_sha_unit) | `512_K` | Advanced | Performance |
| [rgw_torrent_tracker](#rgw_torrent_tracker) | `(empty)` | Advanced | Performance |

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

### rgw_torrent_comment

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_torrent_comment](../../../config/rgw/rgw.md#SP_rgw_torrent_comment) |

**What it does:** Torrent field comment

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_torrent_comment <value>
ceph config get client.rgw rgw_torrent_comment
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_torrent_comment
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_torrent_createby

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_torrent_createby](../../../config/rgw/rgw.md#SP_rgw_torrent_createby) |

**What it does:** torrent field created by

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_torrent_createby <value>
ceph config get client.rgw rgw_torrent_createby
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_torrent_createby
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_torrent_encoding

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_torrent_encoding](../../../config/rgw/rgw.md#SP_rgw_torrent_encoding) |

**What it does:** torrent field encoding

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_torrent_encoding <value>
ceph config get client.rgw rgw_torrent_encoding
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_torrent_encoding
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_torrent_flag

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_torrent_flag](../../../config/rgw/rgw.md#SP_rgw_torrent_flag) |

**What it does:** When true, uploaded objects will calculate and store a SHA256 hash of object data so the object can be retrieved as a torrent file

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_torrent_flag true
ceph config get client.rgw rgw_torrent_flag
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_torrent_max_size

| | |
|---|---|
| Type | Size · default `5_G` · **Advanced** |
| Table | [rgw.md#SP_rgw_torrent_max_size](../../../config/rgw/rgw.md#SP_rgw_torrent_max_size) |

**What it does:** Objects over this size will not store torrent info.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_torrent_max_size 5_G
ceph config get client.rgw rgw_torrent_max_size
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `5_G` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_torrent_origin

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_torrent_origin](../../../config/rgw/rgw.md#SP_rgw_torrent_origin) |

**What it does:** Torrent origin

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_torrent_origin <value>
ceph config get client.rgw rgw_torrent_origin
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_torrent_origin
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_torrent_sha_unit

| | |
|---|---|
| Type | Size · default `512_K` · **Advanced** |
| Table | [rgw.md#SP_rgw_torrent_sha_unit](../../../config/rgw/rgw.md#SP_rgw_torrent_sha_unit) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_torrent_sha_unit 512_K
ceph config get client.rgw rgw_torrent_sha_unit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `512_K`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_torrent_sha_unit
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_torrent_tracker

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_torrent_tracker](../../../config/rgw/rgw.md#SP_rgw_torrent_tracker) |

**What it does:** Torrent field announce and announce list

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_torrent_tracker <value>
ceph config get client.rgw rgw_torrent_tracker
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_torrent_tracker
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](../OVERVIEW.md)
