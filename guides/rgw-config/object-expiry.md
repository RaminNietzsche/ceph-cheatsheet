# Object expiry hints

RGW config deep dive — 1 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
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
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph osd pool stats
```

---

### rgw_objexp_hints_num_shards

| | |
|---|---|
| Type | Uint · default `127` · **Advanced** |
| Table | [rgw.md#SP_rgw_objexp_hints_num_shards](../../config/rgw/rgw.md#SP_rgw_objexp_hints_num_shards) |

**What it does:** Number of object expirer data shards

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


[← RGW config overview](OVERVIEW.md)
