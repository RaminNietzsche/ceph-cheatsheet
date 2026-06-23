# Object read/write I/O

RGW config deep dive — 4 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_get_obj_max_req_size](#rgw_get_obj_max_req_size) | `4_M` | Advanced |
| [rgw_get_obj_window_size](#rgw_get_obj_window_size) | `16_M` | Advanced |
| [rgw_put_obj_max_window_size](#rgw_put_obj_max_window_size) | `64_M` | Advanced |
| [rgw_put_obj_min_window_size](#rgw_put_obj_min_window_size) | `16_M` | Advanced |

---

### rgw_get_obj_max_req_size

| | |
|---|---|
| Type | Size · default `4_M` · **Advanced** |
| Table | [rgw.md#SP_rgw_get_obj_max_req_size](../../config/rgw/rgw.md#SP_rgw_get_obj_max_req_size) |

**What it does:** RGW object read chunk size

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_get_obj_max_req_size 4_M
ceph config get client.rgw rgw_get_obj_max_req_size
```

**Finding optimal value:** Start from upstream default (`4_M`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_get_obj_window_size

| | |
|---|---|
| Type | Size · default `16_M` · **Advanced** |
| Table | [rgw.md#SP_rgw_get_obj_window_size](../../config/rgw/rgw.md#SP_rgw_get_obj_window_size) |

**What it does:** RGW object read window size

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_get_obj_window_size 16_M
ceph config get client.rgw rgw_get_obj_window_size
```

**Finding optimal value:** Start from upstream default (`16_M`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_put_obj_max_window_size

| | |
|---|---|
| Type | Size · default `64_M` · **Advanced** |
| Table | [rgw.md#SP_rgw_put_obj_max_window_size](../../config/rgw/rgw.md#SP_rgw_put_obj_max_window_size) |

**What it does:** The maximum RADOS write window size (in bytes).

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_put_obj_max_window_size 64_M
ceph config get client.rgw rgw_put_obj_max_window_size
```

**Finding optimal value:** Start from upstream default (`64_M`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_put_obj_min_window_size

| | |
|---|---|
| Type | Size · default `16_M` · **Advanced** |
| Table | [rgw.md#SP_rgw_put_obj_min_window_size](../../config/rgw/rgw.md#SP_rgw_put_obj_min_window_size) |

**What it does:** The minimum RADOS write window size (in bytes).

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_put_obj_min_window_size 16_M
ceph config get client.rgw rgw_put_obj_min_window_size
```

**Finding optimal value:** Start from upstream default (`16_M`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---


[← RGW config overview](OVERVIEW.md)
