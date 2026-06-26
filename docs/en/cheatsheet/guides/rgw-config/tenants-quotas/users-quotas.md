# Users & per-user settings

RGW config deep dive — 5 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_user_counters_cache](#rgw_user_counters_cache) | `False` | Dev | Performance |
| [rgw_user_counters_cache_size](#rgw_user_counters_cache_size) | `10000` | Advanced | Performance |
| [rgw_user_max_buckets](#rgw_user_max_buckets) | `1000` | Basic | Policy |
| [rgw_user_policies_max_num](#rgw_user_policies_max_num) | `100` | Advanced | Policy |
| [rgw_user_unique_email](#rgw_user_unique_email) | `True` | Basic | Policy |

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

### rgw_user_counters_cache

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [rgw.md#SP_rgw_user_counters_cache](../../../config/rgw/rgw.md#SP_rgw_user_counters_cache) |

**What it does:** enable a rgw perf counters cache for counters with user label If set to true, rgw creates perf counters with a label for the user and stores them in a perf counters cache. This perf counters cache contains only perf counters labeled by user.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Related options:**

- [`rgw_user_counters_cache_size`](../../../config/rgw/rgw.md#SP_rgw_user_counters_cache_size)

**Example:**

```bash
ceph config set client.rgw rgw_user_counters_cache true
ceph config get client.rgw rgw_user_counters_cache
ceph config set client.rgw rgw_user_counters_cache_size 20000
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `False` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_user_counters_cache_size

| | |
|---|---|
| Type | Uint · default `10000` · **Advanced** |
| Table | [rgw.md#SP_rgw_user_counters_cache_size](../../../config/rgw/rgw.md#SP_rgw_user_counters_cache_size) |

**What it does:** Number of labeled perf counters the user perf counters cache can store

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Related options:**

- [`rgw_user_counters_cache`](../../../config/rgw/rgw.md#SP_rgw_user_counters_cache)

**Example:**

```bash
ceph config set client.rgw rgw_user_counters_cache_size 10000
ceph config get client.rgw rgw_user_counters_cache_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**Signals:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_user_counters_cache_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_user_max_buckets

| | |
|---|---|
| Type | Int · default `1000` · **Basic** |
| Table | [rgw.md#SP_rgw_user_max_buckets](../../../config/rgw/rgw.md#SP_rgw_user_max_buckets) |

**What it does:** Max number of buckets per user A user can create at most this number of buckets. Zero means no limit; a negative value means users cannot create any new buckets, although users will retain buckets already created.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_user_max_buckets 1000
ceph config get client.rgw rgw_user_max_buckets
radosgw-admin user create --uid=newuser --display-name="New User"
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_user_policies_max_num

| | |
|---|---|
| Type | Int · default `100` · **Advanced** |
| Table | [rgw.md#SP_rgw_user_policies_max_num](../../../config/rgw/rgw.md#SP_rgw_user_policies_max_num) |

**What it does:** The maximum number of IAM user policies for a single user.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_user_policies_max_num 100
ceph config get client.rgw rgw_user_policies_max_num
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `100` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_user_unique_email

| | |
|---|---|
| Type | Bool · default `True` · **Basic** |
| Table | [rgw.md#SP_rgw_user_unique_email](../../../config/rgw/rgw.md#SP_rgw_user_unique_email) |

**What it does:** Require local RGW users to have unique email addresses Enforce builtin user accounts to have unique email addresses. This setting is historical. In future, non-enforcement of email address uniqueness is likely to become the default.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_user_unique_email false
ceph config get client.rgw rgw_user_unique_email
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← RGW config overview](../OVERVIEW.md)
