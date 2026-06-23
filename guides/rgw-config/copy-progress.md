# Copy progress

RGW config deep dive — 2 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_copy_obj_progress](#rgw_copy_obj_progress) | `True` | Advanced |
| [rgw_copy_obj_progress_every_bytes](#rgw_copy_obj_progress_every_bytes) | `1_M` | Advanced |

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

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`True`) matches upstream.

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

**Finding optimal value:** Start from upstream default (`1_M`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---


[← RGW config overview](OVERVIEW.md)
