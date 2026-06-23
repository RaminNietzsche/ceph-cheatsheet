# API limits & policies

deep dive پیکربندی RGW — 6 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_acl_grants_max_num](#rgw_acl_grants_max_num) | `100` | Advanced | Policy |
| [rgw_admin_entry](#rgw_admin_entry) | `admin` | Advanced | Policy |
| [rgw_cors_rules_max_num](#rgw_cors_rules_max_num) | `100` | Advanced | Policy |
| [rgw_policy_reject_invalid_principals](#rgw_policy_reject_invalid_principals) | `True` | Basic | Policy |
| [rgw_topic_require_publish_policy](#rgw_topic_require_publish_policy) | `False` | Basic | Policy |
| [rgw_website_routing_rules_max_num](#rgw_website_routing_rules_max_num) | `50` | Advanced | Policy |

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

### rgw_acl_grants_max_num

| | |
|---|---|
| نوع | Int · default `100` · **Advanced** |
| جدول | [rgw.md#SP_rgw_acl_grants_max_num](../../../config/rgw/rgw.md#SP_rgw_acl_grants_max_num) |

**کارکرد:** Maximum number of ACL grants in a single PutBucketAcl / PutObjectAcl request (aligned with S3 limits).

**زمان استفاده:** Raise only if clients legitimately need more grants; lowering hardens against oversized ACL payloads.

**گزینه‌های مرتبط:**

- `rgw_cors_rules_max_num`, `rgw_user_policies_max_num`

**مثال:**

```bash
ceph config set client.rgw rgw_acl_grants_max_num 100
ceph config get client.rgw rgw_acl_grants_max_num
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `100` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_admin_entry

| | |
|---|---|
| نوع | Str · default `admin` · **Advanced** |
| جدول | [rgw.md#SP_rgw_admin_entry](../../../config/rgw/rgw.md#SP_rgw_admin_entry) |

**کارکرد:** URL path prefix for the **RGW Admin Ops REST API** (bucket/user introspection, usage, etc.). **Not runtime-updatable.**

**Important:** Multisite replication **requires** the value `admin`. Do not change it on multisite clusters.

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
# GET https://rgw.example.com/admin/bucket?bucket=mybucket&format=json
curl -s -H "Authorization: AWS ..." \
  "https://rgw.example.com/admin/bucket?bucket=mybucket&format=json"
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Upstream default (`admin`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---

### rgw_cors_rules_max_num

| | |
|---|---|
| نوع | Int · default `100` · **Advanced** |
| جدول | [rgw.md#SP_rgw_cors_rules_max_num](../../../config/rgw/rgw.md#SP_rgw_cors_rules_max_num) |

**کارکرد:** The maximum number of CORS rules in a single request.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه/concurrency می‌رسند یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_cors_rules_max_num 100
ceph config get client.rgw rgw_cors_rules_max_num
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `100` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_policy_reject_invalid_principals

| | |
|---|---|
| نوع | Bool · default `True` · **Basic** |
| جدول | [rgw.md#SP_rgw_policy_reject_invalid_principals](../../../config/rgw/rgw.md#SP_rgw_policy_reject_invalid_principals) |

**کارکرد:** Whether to reject policies with invalid principals

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_policy_reject_invalid_principals false
ceph config get client.rgw rgw_policy_reject_invalid_principals
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_topic_require_publish_policy

| | |
|---|---|
| نوع | Bool · default `False` · **Basic** |
| جدول | [rgw.md#SP_rgw_topic_require_publish_policy](../../../config/rgw/rgw.md#SP_rgw_topic_require_publish_policy) |

**کارکرد:** Whether to validate user permissions to publish notifications to topics.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_topic_require_publish_policy true
ceph config get client.rgw rgw_topic_require_publish_policy
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Production: prefer secure default (`False` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---

### rgw_website_routing_rules_max_num

| | |
|---|---|
| نوع | Int · default `50` · **Advanced** |
| جدول | [rgw.md#SP_rgw_website_routing_rules_max_num](../../../config/rgw/rgw.md#SP_rgw_website_routing_rules_max_num) |

**کارکرد:** The maximum number of website routing rules in a single request.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه/concurrency می‌رسند یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_website_routing_rules_max_num 50
ceph config get client.rgw rgw_website_routing_rules_max_num
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `50` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
