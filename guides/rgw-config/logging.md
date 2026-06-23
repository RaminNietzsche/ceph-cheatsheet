# Access and object logging

RGW config deep dive — 4 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_log_http_headers](#rgw_log_http_headers) | `(empty)` | Basic |
| [rgw_log_nonexistent_bucket](#rgw_log_nonexistent_bucket) | `False` | Advanced |
| [rgw_log_object_name](#rgw_log_object_name) | `%Y-%m-%d-%H-%i-%n` | Advanced |
| [rgw_log_object_name_utc](#rgw_log_object_name_utc) | `False` | Advanced |

---

### rgw_log_http_headers

| | |
|---|---|
| Type | Str · default `(empty)` · **Basic** |
| Table | [rgw.md#SP_rgw_log_http_headers](../../config/rgw/rgw.md#SP_rgw_log_http_headers) |

**What it does:** List of HTTP headers to log

**When to use:** Core RGW behavior — review before changing in production.

**Example:**

```bash
ceph config set client.rgw rgw_log_http_headers <value>
ceph config get client.rgw rgw_log_http_headers
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_log_nonexistent_bucket

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_log_nonexistent_bucket](../../config/rgw/rgw.md#SP_rgw_log_nonexistent_bucket) |

**What it does:** Should RGW log operations on bucket that does not exist

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_log_nonexistent_bucket False
ceph config get client.rgw rgw_log_nonexistent_bucket
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

---

### rgw_log_object_name

| | |
|---|---|
| Type | Str · default `%Y-%m-%d-%H-%i-%n` · **Advanced** |
| Table | [rgw.md#SP_rgw_log_object_name](../../config/rgw/rgw.md#SP_rgw_log_object_name) |

**What it does:** Ops log object name format

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_log_object_name %Y-%m-%d-%H-%i-%n
ceph config get client.rgw rgw_log_object_name
```

**Finding optimal value:** Start from upstream default (`%Y-%m-%d-%H-%i-%n`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_log_object_name_utc

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_log_object_name_utc](../../config/rgw/rgw.md#SP_rgw_log_object_name_utc) |

**What it does:** Should ops log object name based on UTC

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_log_object_name_utc False
ceph config get client.rgw rgw_log_object_name_utc
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

---


[← RGW config overview](OVERVIEW.md)
