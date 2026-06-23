# Limits and listing

RGW config deep dive — 10 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_delete_multi_obj_max_num](#rgw_delete_multi_obj_max_num) | `1000` | Advanced |
| [rgw_max_attr_name_len](#rgw_max_attr_name_len) | `0` | Advanced |
| [rgw_max_attr_size](#rgw_max_attr_size) | `0` | Advanced |
| [rgw_max_attrs_num_in_req](#rgw_max_attrs_num_in_req) | `0` | Advanced |
| [rgw_max_control_aio](#rgw_max_control_aio) | `8` | Advanced |
| [rgw_max_dynamic_shards](#rgw_max_dynamic_shards) | `1999` | Advanced |
| [rgw_max_listing_results](#rgw_max_listing_results) | `5000` | Advanced |
| [rgw_max_put_param_size](#rgw_max_put_param_size) | `1_M` | Advanced |
| [rgw_max_put_size](#rgw_max_put_size) | `5_G` | Advanced |
| [rgw_max_slo_entries](#rgw_max_slo_entries) | `1000` | Advanced |

---

### rgw_delete_multi_obj_max_num

| | |
|---|---|
| Type | Int · default `1000` · **Advanced** |
| Table | [rgw.md#SP_rgw_delete_multi_obj_max_num](../../config/rgw/rgw.md#SP_rgw_delete_multi_obj_max_num) |

**What it does:** The maximum number of objects in a single multi-object delete request.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_delete_multi_obj_max_num 1000
ceph config get client.rgw rgw_delete_multi_obj_max_num
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`1000`) matches S3 compatibility for most workloads.

---

### rgw_max_attr_name_len

| | |
|---|---|
| Type | Size · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_max_attr_name_len](../../config/rgw/rgw.md#SP_rgw_max_attr_name_len) |

**What it does:** The maximum length of metadata name. 0 skips the check

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_max_attr_name_len 0
ceph config get client.rgw rgw_max_attr_name_len
```

**Finding optimal value:** Start from upstream default (`0`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_max_attr_size

| | |
|---|---|
| Type | Size · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_max_attr_size](../../config/rgw/rgw.md#SP_rgw_max_attr_size) |

**What it does:** The maximum length of metadata value. 0 skips the check

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_max_attr_size 0
ceph config get client.rgw rgw_max_attr_size
```

**Finding optimal value:** Start from upstream default (`0`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_max_attrs_num_in_req

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_max_attrs_num_in_req](../../config/rgw/rgw.md#SP_rgw_max_attrs_num_in_req) |

**What it does:** The maximum number of metadata items that can be put via single request

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_max_attrs_num_in_req 0
ceph config get client.rgw rgw_max_attrs_num_in_req
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`0`) matches S3 compatibility for most workloads.

---

### rgw_max_control_aio

| | |
|---|---|
| Type | Int · default `8` · **Advanced** |
| Table | [rgw.md#SP_rgw_max_control_aio](../../config/rgw/rgw.md#SP_rgw_max_control_aio) |

**What it does:** Maximum number of concurrent operations over control objects.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_max_control_aio 8
ceph config get client.rgw rgw_max_control_aio
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`8`) matches S3 compatibility for most workloads.

---

### rgw_max_dynamic_shards

| | |
|---|---|
| Type | Uint · default `1999` · **Advanced** |
| Table | [rgw.md#SP_rgw_max_dynamic_shards](../../config/rgw/rgw.md#SP_rgw_max_dynamic_shards) |

**What it does:** Max shards that dynamic resharding can create

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_max_dynamic_shards 1999
ceph config get client.rgw rgw_max_dynamic_shards
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`1999`) matches S3 compatibility for most workloads. Valid range: min=1, max=—.

---

### rgw_max_listing_results

| | |
|---|---|
| Type | Uint · default `5000` · **Advanced** |
| Table | [rgw.md#SP_rgw_max_listing_results](../../config/rgw/rgw.md#SP_rgw_max_listing_results) |

**What it does:** Upper bound on results in listing operations, ListObjects max-keys

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_max_listing_results 5000
ceph config get client.rgw rgw_max_listing_results
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`5000`) matches S3 compatibility for most workloads. Valid range: min=1, max=100000.

---

### rgw_max_put_param_size

| | |
|---|---|
| Type | Size · default `1_M` · **Advanced** |
| Table | [rgw.md#SP_rgw_max_put_param_size](../../config/rgw/rgw.md#SP_rgw_max_put_param_size) |

**What it does:** The maximum size (in bytes) of data input of certain RESTful requests.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_max_put_param_size 1_M
ceph config get client.rgw rgw_max_put_param_size
```

**Finding optimal value:** Start from upstream default (`1_M`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_max_put_size

| | |
|---|---|
| Type | Size · default `5_G` · **Advanced** |
| Table | [rgw.md#SP_rgw_max_put_size](../../config/rgw/rgw.md#SP_rgw_max_put_size) |

**What it does:** The maximum size (in bytes) of regular (non multi-part) object upload.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_max_put_size 5_G
ceph config get client.rgw rgw_max_put_size
```

**Finding optimal value:** Start from upstream default (`5_G`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_max_slo_entries

| | |
|---|---|
| Type | Int · default `1000` · **Advanced** |
| Table | [rgw.md#SP_rgw_max_slo_entries](../../config/rgw/rgw.md#SP_rgw_max_slo_entries) |

**What it does:** Max number of entries in Swift Static Large Object manifest

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_max_slo_entries 1000
ceph config get client.rgw rgw_max_slo_entries
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`1000`) matches S3 compatibility for most workloads.

---


[← RGW config overview](OVERVIEW.md)
