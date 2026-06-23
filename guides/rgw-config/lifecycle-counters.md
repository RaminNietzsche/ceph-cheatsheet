# RGW LC counters

RGW config deep dive — 2 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgwlc_auto_session_clear](#rgwlc_auto_session_clear) | `True` | Advanced | Policy |
| [rgwlc_skip_bucket_step](#rgwlc_skip_bucket_step) | `False` | Advanced | Policy |

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

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

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

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← RGW config overview](OVERVIEW.md)
