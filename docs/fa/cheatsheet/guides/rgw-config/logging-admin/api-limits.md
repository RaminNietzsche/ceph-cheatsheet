# API limits & policies

راهنمای عمیق پیکربندی RGW — 6 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_acl_grants_max_num](#rgw_acl_grants_max_num) | `100` | Advanced | سیاست |
| [rgw_admin_entry](#rgw_admin_entry) | `admin` | Advanced | سیاست |
| [rgw_cors_rules_max_num](#rgw_cors_rules_max_num) | `100` | Advanced | سیاست |
| [rgw_policy_reject_invalid_principals](#rgw_policy_reject_invalid_principals) | `True` | Basic | سیاست |
| [rgw_topic_require_publish_policy](#rgw_topic_require_publish_policy) | `False` | Basic | سیاست |
| [rgw_website_routing_rules_max_num](#rgw_website_routing_rules_max_num) | `50` | Advanced | سیاست |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **سیاست** | امنیت، سازگاری API، محدودیت tenant |
| **ظرفیت** | چیدمان دیسک، مسیرها، اندازه pool |
| **عملکرد** | خط پایه → تغییر تدریجی → پایش OSD/RGW |
| **اتصال** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **معماری** | backend، توپولوژی چندسایته — نه جستجوی عددی |
| **توسعه** | در محیط عملیاتی همان پیش‌فرض upstream |

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

**زمان استفاده:** تنظیم replication و sync در محیط چندسایته — وقتی تأخیر (lag) یا بار sync مشکل‌ساز است.

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

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

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

**کارکرد:** Whether to reject policies with invalid principals If true, policies with invalid principals will be rejected. We don't support Canonical User identifiers or some other form of policies that Amazon does, so if you are mirroring policies between RGW and AWS, you may wish to set this to false.

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

**کارکرد:** Whether to validate user permissions to publish notifications to topics. If true, all users (other then the owner of the topic) will need to have a policy to publish notifications to topics. The topic policy can be set by owner via CreateTopic() or SetTopicAttribute(). Following permissions can be granted "sns:Publish", "sns:GetTopicAttributes", "sns:SetTopicAttributes", "sns:DeleteTopic" and "sns:CreateTopic" via Policy. NOTE that even if set to "false" topics will still follow the policies if set on them.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

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

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

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
