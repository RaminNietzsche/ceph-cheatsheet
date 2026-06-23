# RGW LC counters

RGW config deep dive — 2 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgwlc_auto_session_clear](#rgwlc_auto_session_clear) | `True` | Advanced |
| [rgwlc_skip_bucket_step](#rgwlc_skip_bucket_step) | `False` | Advanced |

---

### rgwlc_auto_session_clear

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgwlc.md#SP_rgwlc_auto_session_clear](../../config/rgw/rgwlc.md#SP_rgwlc_auto_session_clear) |

**What it does:** Automatically clear stale lifecycle sessions (i.e., after 2 idle processing cycles)

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgwlc_auto_session_clear True
ceph config get client.rgw rgwlc_auto_session_clear
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`True`) matches upstream.

---

### rgwlc_skip_bucket_step

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgwlc.md#SP_rgwlc_skip_bucket_step](../../config/rgw/rgwlc.md#SP_rgwlc_skip_bucket_step) |

**What it does:** Conditionally skip the processing (but not the scheduling) of bucket lifecycle

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgwlc_skip_bucket_step False
ceph config get client.rgw rgwlc_skip_bucket_step
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

---


[← RGW config overview](OVERVIEW.md)
