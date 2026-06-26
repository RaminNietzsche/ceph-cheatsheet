# Object expiry hints

RGW config deep dive — 2 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_objexp_chunk_size](#rgw_objexp_chunk_size) | `100` | Dev | Performance |
| [rgw_objexp_hints_num_shards](#rgw_objexp_hints_num_shards) | `127` | Advanced | Policy |

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

### rgw_objexp_chunk_size

| | |
|---|---|
| Type | Uint · default `100` · **Dev** |
| Table | [rgw.md#SP_rgw_objexp_chunk_size](../../../config/rgw/rgw.md#SP_rgw_objexp_chunk_size) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_objexp_chunk_size 100
ceph config get client.rgw rgw_objexp_chunk_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline `100` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**Signals:** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_objexp_chunk_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_objexp_hints_num_shards

| | |
|---|---|
| Type | Uint · default `127` · **Advanced** |
| Table | [rgw.md#SP_rgw_objexp_hints_num_shards](../../../config/rgw/rgw.md#SP_rgw_objexp_hints_num_shards) |

**What it does:** Number of object expirer data shards The number of shards the (Swift) object expirer will store its data on.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_objexp_hints_num_shards 127
ceph config get client.rgw rgw_objexp_hints_num_shards
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `127` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---


[← RGW config overview](../OVERVIEW.md)
