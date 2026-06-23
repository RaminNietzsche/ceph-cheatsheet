# Users and per-user settings

RGW config deep dive — 3 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_user_max_buckets](#rgw_user_max_buckets) | `1000` | Basic |
| [rgw_user_policies_max_num](#rgw_user_policies_max_num) | `100` | Advanced |
| [rgw_user_unique_email](#rgw_user_unique_email) | `True` | Basic |

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

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`1000`) matches S3 compatibility for most workloads.

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

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`100`) matches S3 compatibility for most workloads.

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

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`True`) matches upstream.

---


[← RGW config overview](OVERVIEW.md)
