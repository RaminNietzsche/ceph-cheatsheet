# S3 API & auth

deep dive پیکربندی RGW — 8 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_s3_auth_disable_signature_url](#rgw_s3_auth_disable_signature_url) | `False` | Advanced | Connectivity |
| [rgw_s3_auth_order](#rgw_s3_auth_order) | `sts, external, local` | Advanced | Performance |
| [rgw_s3_auth_use_keystone](#rgw_s3_auth_use_keystone) | `False` | Advanced | Policy |
| [rgw_s3_auth_use_ldap](#rgw_s3_auth_use_ldap) | `False` | Advanced | Policy |
| [rgw_s3_auth_use_rados](#rgw_s3_auth_use_rados) | `True` | Advanced | Policy |
| [rgw_s3_auth_use_sts](#rgw_s3_auth_use_sts) | `False` | Advanced | Policy |
| [rgw_s3_client_max_sig_ver](#rgw_s3_client_max_sig_ver) | `-1` | Advanced | Policy |
| [rgw_s3_success_create_obj_status](#rgw_s3_success_create_obj_status) | `0` | Advanced | Performance |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **Policy** | امنیت، سازگاری API، محدودیت tenant |
| **Capacity** | چیدمان دیسک، مسیرها، اندازه pool |
| **Performance** | خط پایه → تغییر تدریجی → پایش OSD/RGW |
| **Connectivity** | نزدیک‌ترین endpoint پایدار خارجی |
| **Architecture** | backend، توپولوژی multisite — نه sweep عددی |
| **Dev** | پیش‌فرض upstream در production |

**ابزارهای مشترک:**

```bash
ceph config get client.rgw <option>
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph pg stat
```

---

### rgw_s3_auth_disable_signature_url

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_s3_auth_disable_signature_url](../../../config/rgw/rgw.md#SP_rgw_s3_auth_disable_signature_url) |

**کارکرد:** Should authentication with presigned URLs be disabled

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_s3_auth_disable_signature_url true
ceph config get client.rgw rgw_s3_auth_disable_signature_url
# curl -k <url>  # from each RGW node
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Connectivity

1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).
2. From **each** RGW node: `curl -k <url>` or vendor health check.
3. Pick the lowest-latency endpoint that stays healthy over 24h.
4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).
5. Leave empty (`False`) if the integration is disabled.

```bash
ceph config get client.rgw rgw_s3_auth_disable_signature_url
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_s3_auth_order

| | |
|---|---|
| نوع | Str · default `sts, external, local` · **Advanced** |
| جدول | [rgw.md#SP_rgw_s3_auth_order](../../../config/rgw/rgw.md#SP_rgw_s3_auth_order) |

**کارکرد:** Authentication strategy order to use for S3

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_s3_auth_order "sts, external, local"
ceph config get client.rgw rgw_s3_auth_order
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `sts, external, local`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_s3_auth_order
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_s3_auth_use_keystone

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_s3_auth_use_keystone](../../../config/rgw/rgw.md#SP_rgw_s3_auth_use_keystone) |

**کارکرد:** Specify whether S3 authentication uses Keystone

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_s3_auth_use_keystone true
ceph config get client.rgw rgw_s3_auth_use_keystone
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_s3_auth_use_ldap

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_s3_auth_use_ldap](../../../config/rgw/rgw.md#SP_rgw_s3_auth_use_ldap) |

**کارکرد:** Should S3 authentication use LDAP.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_s3_auth_use_ldap true
ceph config get client.rgw rgw_s3_auth_use_ldap
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_s3_auth_use_rados

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_s3_auth_use_rados](../../../config/rgw/rgw.md#SP_rgw_s3_auth_use_rados) |

**کارکرد:** Specify whether S3 authentication uses credentials stored in RADOS

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_s3_auth_use_rados false
ceph config get client.rgw rgw_s3_auth_use_rados
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_s3_auth_use_sts

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_s3_auth_use_sts](../../../config/rgw/rgw.md#SP_rgw_s3_auth_use_sts) |

**کارکرد:** Should S3 authentication use STS.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_s3_auth_use_sts true
ceph config get client.rgw rgw_s3_auth_use_sts
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_s3_client_max_sig_ver

| | |
|---|---|
| نوع | Int · default `-1` · **Advanced** |
| جدول | [rgw.md#SP_rgw_s3_client_max_sig_ver](../../../config/rgw/rgw.md#SP_rgw_s3_client_max_sig_ver) |

**کارکرد:** Max S3 authentication signature version

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه/concurrency می‌رسند یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_s3_client_max_sig_ver -1
ceph config get client.rgw rgw_s3_client_max_sig_ver
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `-1` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_s3_success_create_obj_status

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [rgw.md#SP_rgw_s3_success_create_obj_status](../../../config/rgw/rgw.md#SP_rgw_s3_success_create_obj_status) |

**کارکرد:** HTTP return code override for object creation

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_s3_success_create_obj_status 0
ceph config get client.rgw rgw_s3_success_create_obj_status
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_s3_success_create_obj_status
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
