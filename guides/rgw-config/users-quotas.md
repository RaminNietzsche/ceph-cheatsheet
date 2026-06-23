# Users and per-user settings

RGW config deep dive — 3 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
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
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph osd pool stats
```

---

### rgw_user_max_buckets

| | |
|---|---|
| Type | Int · default `1000` · **Basic** |
| Table | [rgw.md#SP_rgw_user_max_buckets](../../config/rgw/rgw.md#SP_rgw_user_max_buckets) |

**What it does:** Max number of buckets per user

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_user_max_buckets 1000
ceph config get client.rgw rgw_user_max_buckets
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
| Table | [rgw.md#SP_rgw_user_policies_max_num](../../config/rgw/rgw.md#SP_rgw_user_policies_max_num) |

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
| Table | [rgw.md#SP_rgw_user_unique_email](../../config/rgw/rgw.md#SP_rgw_user_unique_email) |

**What it does:** Require local RGW users to have unique email addresses

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_user_unique_email True
ceph config get client.rgw rgw_user_unique_email
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← RGW config overview](OVERVIEW.md)
