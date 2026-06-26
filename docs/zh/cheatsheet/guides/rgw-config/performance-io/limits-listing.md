# Listing limits

RGW 配置深度指南 — 12 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_delete_multi_obj_max_num](#rgw_delete_multi_obj_max_num) | `1000` | Advanced | 策略 |
| [rgw_list_buckets_max_chunk](#rgw_list_buckets_max_chunk) | `1000` | Advanced | 策略 |
| [rgw_max_attr_name_len](#rgw_max_attr_name_len) | `0` | Advanced | 策略 |
| [rgw_max_attr_size](#rgw_max_attr_size) | `0` | Advanced | 策略 |
| [rgw_max_attrs_num_in_req](#rgw_max_attrs_num_in_req) | `0` | Advanced | 策略 |
| [rgw_max_chunk_size](#rgw_max_chunk_size) | `4_M` | Advanced | 性能 |
| [rgw_max_control_aio](#rgw_max_control_aio) | `8` | Advanced | 策略 |
| [rgw_max_dynamic_shards](#rgw_max_dynamic_shards) | `1999` | Advanced | 策略 |
| [rgw_max_listing_results](#rgw_max_listing_results) | `5000` | Advanced | 策略 |
| [rgw_max_put_param_size](#rgw_max_put_param_size) | `1_M` | Advanced | 策略 |
| [rgw_max_put_size](#rgw_max_put_size) | `5_G` | Advanced | 策略 |
| [rgw_max_slo_entries](#rgw_max_slo_entries) | `1000` | Advanced | 策略 |

## 寻找最优值

| 模型 | 如何选择 |
|-------|---------------|
| **策略** | 安全、API 兼容性、租户限制 |
| **容量** | 磁盘布局、路径、池容量 |
| **性能** | 基线 → 逐步调整 → 监控 OSD/RGW |
| **连通性** | 最近且稳定的外部端点 |
| **架构** | 后端、多站点拓扑 — 非数值扫描 |
| **开发** | 生产环境保持 upstream 默认值 |

**常用工具：**

```bash
ceph config get client.rgw <option>
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph pg stat
```

---

### rgw_delete_multi_obj_max_num

| | |
|---|---|
| 类型 | Int · default `1000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_delete_multi_obj_max_num](../../../config/rgw/rgw.md#SP_rgw_delete_multi_obj_max_num) |

**作用：** The maximum number of objects in a single multi-object delete request.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_delete_multi_obj_max_num 1000
ceph config get client.rgw rgw_delete_multi_obj_max_num
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_list_buckets_max_chunk

| | |
|---|---|
| 类型 | Int · default `1000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_list_buckets_max_chunk](../../../config/rgw/rgw.md#SP_rgw_list_buckets_max_chunk) |

**作用：** Max number of buckets to retrieve in a single listing operation When RGW fetches lists of user's buckets from the backend, this is the max number of entries it will try to retrieve in a single operation. Note that the backend may choose to return a smaller number of entries.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_list_buckets_max_chunk 1000
ceph config get client.rgw rgw_list_buckets_max_chunk
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_max_attr_name_len

| | |
|---|---|
| 类型 | Size · default `0` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_max_attr_name_len](../../../config/rgw/rgw.md#SP_rgw_max_attr_name_len) |

**作用：** The maximum length of metadata name. 0 skips the check

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_max_attr_name_len 128
ceph config get client.rgw rgw_max_attr_name_len
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `0` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_max_attr_size

| | |
|---|---|
| 类型 | Size · default `0` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_max_attr_size](../../../config/rgw/rgw.md#SP_rgw_max_attr_size) |

**作用：** The maximum length of metadata value. 0 skips the check

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_max_attr_size 128
ceph config get client.rgw rgw_max_attr_size
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `0` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_max_attrs_num_in_req

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_max_attrs_num_in_req](../../../config/rgw/rgw.md#SP_rgw_max_attrs_num_in_req) |

**作用：** The maximum number of metadata items that can be put via single request

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_max_attrs_num_in_req 128
ceph config get client.rgw rgw_max_attrs_num_in_req
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `0` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_max_chunk_size

| | |
|---|---|
| 类型 | Size · default `4_M` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_max_chunk_size](../../../config/rgw/rgw.md#SP_rgw_max_chunk_size) |

**作用：** The maximum RGW chunk size. The chunk size is the size of requests that RGW sends to OSDs when accessing RADOS objects. RGW read and write operations will never request more than this amount in a single request. This also defines the RGW HEAD object size, as head operations need to be atomic, and anything larger than this would require more than a single operation. When RGW objects are written to the default storage class, up to this amount of payload data will be stored alongside metadata in the head object. Note that when writing an RGW object to a non-default storage class the HEAD RADOS object is always stored in the default storage class' pool but no inlining of payload data is performed.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_max_chunk_size 4_M
ceph config get client.rgw rgw_max_chunk_size
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline `4_M` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**观测信号：** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_max_chunk_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_max_control_aio

| | |
|---|---|
| 类型 | Int · default `8` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_max_control_aio](../../../config/rgw/rgw.md#SP_rgw_max_control_aio) |

**作用：** Maximum number of concurrent operations over control objects. When metadata caching is enabled, a watch operation is sent to each control object on startup, with a corresponding unwatch on shutdown. To accelerate startup/shutdown, allow several concurrent operations to be sent at once.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**相关选项：**

- [`rgw_num_control_oids`](../../../config/rgw/rgw.md#SP_rgw_num_control_oids)

**示例：**

```bash
ceph config set client.rgw rgw_max_control_aio 8
ceph config get client.rgw rgw_max_control_aio
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `8` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_max_dynamic_shards

| | |
|---|---|
| 类型 | Uint · default `1999` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_max_dynamic_shards](../../../config/rgw/rgw.md#SP_rgw_max_dynamic_shards) |

**作用：** Max shards that dynamic resharding can create This is the maximum number of bucket index shards that dynamic sharding is able to create on its own. This does not limit user requested resharding. Ideally this value is a prime number.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_max_dynamic_shards 1999
ceph config get client.rgw rgw_max_dynamic_shards
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `1999` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

**边界：** min `1`, max `—`.

---

### rgw_max_listing_results

| | |
|---|---|
| 类型 | Uint · default `5000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_max_listing_results](../../../config/rgw/rgw.md#SP_rgw_max_listing_results) |

**作用：** Upper bound on results in listing operations, ListObjects max-keys This caps the maximum permitted value for listing-like operations in RGW S3. Affects ListObjects(max-keys), ListObjectsVersions(max-keys), ListMultipartUploads(max-uploads), ListParts(max-parts)

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_max_listing_results 5000
ceph config get client.rgw rgw_max_listing_results
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `5000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

**边界：** min `1`, max `100000`.

---

### rgw_max_put_param_size

| | |
|---|---|
| 类型 | Size · default `1_M` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_max_put_param_size](../../../config/rgw/rgw.md#SP_rgw_max_put_param_size) |

**作用：** The maximum size (in bytes) of data input of certain RESTful requests.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_max_put_param_size 1_M
ceph config get client.rgw rgw_max_put_param_size
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `1_M` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_max_put_size

| | |
|---|---|
| 类型 | Size · default `5_G` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_max_put_size](../../../config/rgw/rgw.md#SP_rgw_max_put_size) |

**作用：** The maximum size (in bytes) of regular (non multi-part) object upload. Plain object upload is capped at this amount of data. In order to upload larger objects, a special composite upload mechanism is required multi-part upload (MPU) for S3 and DLO and SLO for Swift. Note that this value also limits the size of individual chunks uploaded for MPU and DLO/SLO objects, thus the largest composite object that can be uploaded is of size ``rgw_max_put_size`` * ``rgw_multipart_part_upload_limit``

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_max_put_size 5_G
ceph config get client.rgw rgw_max_put_size
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `5_G` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_max_slo_entries

| | |
|---|---|
| 类型 | Int · default `1000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_max_slo_entries](../../../config/rgw/rgw.md#SP_rgw_max_slo_entries) |

**作用：** Max number of entries in Swift Static Large Object manifest

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_max_slo_entries 1000
ceph config get client.rgw rgw_max_slo_entries
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---


[← RGW 配置概览](../OVERVIEW.md)
