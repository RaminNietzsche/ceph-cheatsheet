# Object expiry hints

RGW config deep dive — 1 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_objexp_hints_num_shards](#rgw_objexp_hints_num_shards) | `127` | Advanced |

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

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`127`) matches S3 compatibility for most workloads.

---


[← RGW config overview](OVERVIEW.md)
