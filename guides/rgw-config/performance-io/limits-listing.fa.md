# Listing limits

راهنمای عمیق پیکربندی RGW — 12 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
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

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **Policy** | امنیت، سازگاری API، محدودیت tenant |
| **Capacity** | چیدمان دیسک، مسیرها، اندازه pool |
| **Performance** | خط پایه → تغییر تدریجی → پایش OSD/RGW |
| **Connectivity** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **Architecture** | backend، توپولوژی چندسایته — نه جستجوی عددی |
| **Dev** | در محیط عملیاتی همان پیش‌فرض upstream |

**ابزارهای مشترک:**

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
| نوع | Int · default `1000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_delete_multi_obj_max_num](../../../config/rgw/rgw.md#SP_rgw_delete_multi_obj_max_num) |

**کارکرد:** The maximum number of objects in a single multi-object delete request.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_delete_multi_obj_max_num 1000
ceph config get client.rgw rgw_delete_multi_obj_max_num
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_list_buckets_max_chunk

| | |
|---|---|
| نوع | Int · default `1000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_list_buckets_max_chunk](../../../config/rgw/rgw.md#SP_rgw_list_buckets_max_chunk) |

**کارکرد:** Max number of buckets to retrieve in a single listing operation

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_list_buckets_max_chunk 1000
ceph config get client.rgw rgw_list_buckets_max_chunk
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_max_attr_name_len

| | |
|---|---|
| نوع | Size · default `0` · **Advanced** |
| جدول | [rgw.md#SP_rgw_max_attr_name_len](../../../config/rgw/rgw.md#SP_rgw_max_attr_name_len) |

**کارکرد:** The maximum length of metadata name. 0 skips the check

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_max_attr_name_len 128
ceph config get client.rgw rgw_max_attr_name_len
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `0` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_max_attr_size

| | |
|---|---|
| نوع | Size · default `0` · **Advanced** |
| جدول | [rgw.md#SP_rgw_max_attr_size](../../../config/rgw/rgw.md#SP_rgw_max_attr_size) |

**کارکرد:** The maximum length of metadata value. 0 skips the check

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_max_attr_size 128
ceph config get client.rgw rgw_max_attr_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `0` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_max_attrs_num_in_req

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rgw.md#SP_rgw_max_attrs_num_in_req](../../../config/rgw/rgw.md#SP_rgw_max_attrs_num_in_req) |

**کارکرد:** The maximum number of metadata items that can be put via single request

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_max_attrs_num_in_req 128
ceph config get client.rgw rgw_max_attrs_num_in_req
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `0` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_max_chunk_size

| | |
|---|---|
| نوع | Size · default `4_M` · **Advanced** |
| جدول | [rgw.md#SP_rgw_max_chunk_size](../../../config/rgw/rgw.md#SP_rgw_max_chunk_size) |

**کارکرد:** The maximum RGW chunk size.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_max_chunk_size 4_M
ceph config get client.rgw rgw_max_chunk_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline `4_M` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**سیگنال‌ها:** PUT/GET p99 by object size, RADOS op count per MB transferred.

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
| نوع | Int · default `8` · **Advanced** |
| جدول | [rgw.md#SP_rgw_max_control_aio](../../../config/rgw/rgw.md#SP_rgw_max_control_aio) |

**کارکرد:** Maximum number of concurrent operations over control objects.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_max_control_aio 8
ceph config get client.rgw rgw_max_control_aio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `8` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_max_dynamic_shards

| | |
|---|---|
| نوع | Uint · default `1999` · **Advanced** |
| جدول | [rgw.md#SP_rgw_max_dynamic_shards](../../../config/rgw/rgw.md#SP_rgw_max_dynamic_shards) |

**کارکرد:** Max shards that dynamic resharding can create

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_max_dynamic_shards 1999
ceph config get client.rgw rgw_max_dynamic_shards
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `1999` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

**محدوده:** min `1`, max `—`.

---

### rgw_max_listing_results

| | |
|---|---|
| نوع | Uint · default `5000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_max_listing_results](../../../config/rgw/rgw.md#SP_rgw_max_listing_results) |

**کارکرد:** Upper bound on results in listing operations, ListObjects max-keys

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_max_listing_results 5000
ceph config get client.rgw rgw_max_listing_results
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `5000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

**محدوده:** min `1`, max `100000`.

---

### rgw_max_put_param_size

| | |
|---|---|
| نوع | Size · default `1_M` · **Advanced** |
| جدول | [rgw.md#SP_rgw_max_put_param_size](../../../config/rgw/rgw.md#SP_rgw_max_put_param_size) |

**کارکرد:** The maximum size (in bytes) of data input of certain RESTful requests.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_max_put_param_size 1_M
ceph config get client.rgw rgw_max_put_param_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `1_M` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_max_put_size

| | |
|---|---|
| نوع | Size · default `5_G` · **Advanced** |
| جدول | [rgw.md#SP_rgw_max_put_size](../../../config/rgw/rgw.md#SP_rgw_max_put_size) |

**کارکرد:** The maximum size (in bytes) of regular (non multi-part) object upload.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_max_put_size 5_G
ceph config get client.rgw rgw_max_put_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `5_G` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_max_slo_entries

| | |
|---|---|
| نوع | Int · default `1000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_max_slo_entries](../../../config/rgw/rgw.md#SP_rgw_max_slo_entries) |

**کارکرد:** Max number of entries in Swift Static Large Object manifest

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_max_slo_entries 1000
ceph config get client.rgw rgw_max_slo_entries
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
