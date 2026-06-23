# Multipart uploads

RGW config deep dive — 2 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_multipart_min_part_size](#rgw_multipart_min_part_size) | `5_M` | Advanced |
| [rgw_multipart_part_upload_limit](#rgw_multipart_part_upload_limit) | `10000` | Advanced |

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

**Finding optimal value:** Start from upstream default (`5_M`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Start from upstream default (`10000`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---


[← RGW config overview](OVERVIEW.md)
