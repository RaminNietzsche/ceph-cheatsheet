# Usage logging

RGW config deep dive — 4 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_usage_log_flush_threshold](#rgw_usage_log_flush_threshold) | `1024` | Advanced |
| [rgw_usage_log_key_transition](#rgw_usage_log_key_transition) | `True` | Advanced |
| [rgw_usage_max_shards](#rgw_usage_max_shards) | `32` | Advanced |
| [rgw_usage_max_user_shards](#rgw_usage_max_user_shards) | `1` | Advanced |

---

### rgw_usage_log_flush_threshold

| | |
|---|---|
| Type | Int · default `1024` · **Advanced** |
| Table | [rgw.md#SP_rgw_usage_log_flush_threshold](../../config/rgw/rgw.md#SP_rgw_usage_log_flush_threshold) |

**What it does:** Number of entries in usage log before flushing

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_usage_log_flush_threshold 1024
ceph config get client.rgw rgw_usage_log_flush_threshold
```

**Finding optimal value:** Start from upstream default (`1024`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_usage_log_key_transition

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_usage_log_key_transition](../../config/rgw/rgw.md#SP_rgw_usage_log_key_transition) |

**What it does:** Handle the co-existence of both old and new name-by-user keys

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_usage_log_key_transition True
ceph config get client.rgw rgw_usage_log_key_transition
```

**Finding optimal value:** Not a performance knob — use credentials from your identity/KMS provider. Rotate via secrets management; never commit values to config repos.

---

### rgw_usage_max_shards

| | |
|---|---|
| Type | Int · default `32` · **Advanced** |
| Table | [rgw.md#SP_rgw_usage_max_shards](../../config/rgw/rgw.md#SP_rgw_usage_max_shards) |

**What it does:** Number of shards for usage log.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_usage_max_shards 32
ceph config get client.rgw rgw_usage_max_shards
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`32`) matches S3 compatibility for most workloads.

---

### rgw_usage_max_user_shards

| | |
|---|---|
| Type | Int · default `1` · **Advanced** |
| Table | [rgw.md#SP_rgw_usage_max_user_shards](../../config/rgw/rgw.md#SP_rgw_usage_max_user_shards) |

**What it does:** Number of shards for single user in usage log

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_usage_max_user_shards 1
ceph config get client.rgw rgw_usage_max_user_shards
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`1`) matches S3 compatibility for most workloads. Valid range: min=1, max=—.

---


[← RGW config overview](OVERVIEW.md)
