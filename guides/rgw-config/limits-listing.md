# Listing limits

RGW config deep dive — 12 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_delete_multi_obj_max_num](#rgw_delete_multi_obj_max_num) | `1000` | Advanced | Policy |
| [rgw_list_buckets_max_chunk](#rgw_list_buckets_max_chunk) | `1000` | Advanced | Policy |
| [rgw_max_attr_name_len](#rgw_max_attr_name_len) | `0` | Advanced | Policy |
| [rgw_max_attr_size](#rgw_max_attr_size) | `0` | Advanced | Policy |
| [rgw_max_attrs_num_in_req](#rgw_max_attrs_num_in_req) | `0` | Advanced | Policy |
| [rgw_max_chunk_size](#rgw_max_chunk_size) | `4_M` | Advanced | Performance |
| [rgw_max_control_aio](#rgw_max_control_aio) | `8` | Advanced | Policy |
| [rgw_max_dynamic_shards](#rgw_max_dynamic_shards) | `1999` | Advanced | Policy |
| [rgw_max_listing_results](#rgw_max_listing_results) | `5000` | Advanced | Policy |
| [rgw_max_put_param_size](#rgw_max_put_param_size) | `1_M` | Advanced | Policy |
| [rgw_max_put_size](#rgw_max_put_size) | `5_G` | Advanced | Policy |
| [rgw_max_slo_entries](#rgw_max_slo_entries) | `1000` | Advanced | Policy |

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

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_list_buckets_max_chunk

| | |
|---|---|
| Type | Int · default `1000` · **Advanced** |
| Table | [rgw.md#SP_rgw_list_buckets_max_chunk](../../config/rgw/rgw.md#SP_rgw_list_buckets_max_chunk) |

**What it does:** Max number of buckets to retrieve in a single listing operation

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_list_buckets_max_chunk 1000
ceph config get client.rgw rgw_list_buckets_max_chunk
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

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
ceph config set client.rgw rgw_max_attr_name_len 128
ceph config get client.rgw rgw_max_attr_name_len
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `0` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

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
ceph config set client.rgw rgw_max_attr_size 128
ceph config get client.rgw rgw_max_attr_size
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `0` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

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
ceph config set client.rgw rgw_max_attrs_num_in_req 128
ceph config get client.rgw rgw_max_attrs_num_in_req
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `0` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_max_chunk_size

| | |
|---|---|
| Type | Size · default `4_M` · **Advanced** |
| Table | [rgw.md#SP_rgw_max_chunk_size](../../config/rgw/rgw.md#SP_rgw_max_chunk_size) |

**What it does:** The maximum RGW chunk size.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_max_chunk_size 4_M
ceph config get client.rgw rgw_max_chunk_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline `4_M` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**Signals:** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_max_chunk_size
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

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

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `8` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

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

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `1999` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

**Bounds:** min `1`, max `—`.

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

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `5000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

**Bounds:** min `1`, max `100000`.

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

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `1_M` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

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

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `5_G` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

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

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---


[← RGW config overview](OVERVIEW.md)
