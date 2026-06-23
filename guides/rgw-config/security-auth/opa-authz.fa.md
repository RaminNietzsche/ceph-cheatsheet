# OPA authorization

deep dive پیکربندی RGW — 4 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_opa_token](#rgw_opa_token) | `(empty)` | Advanced | Policy |
| [rgw_opa_url](#rgw_opa_url) | `(empty)` | Advanced | Connectivity |
| [rgw_opa_verify_ssl](#rgw_opa_verify_ssl) | `True` | Advanced | Policy |
| [rgw_use_opa_authz](#rgw_use_opa_authz) | `False` | Advanced | Policy |

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

### rgw_opa_token

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_opa_token](../../../config/rgw/rgw.md#SP_rgw_opa_token) |

**کارکرد:** The Bearer token OPA uses to authenticate client requests.

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_opa_token <value>
ceph config get client.rgw rgw_opa_token
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_opa_url

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_opa_url](../../../config/rgw/rgw.md#SP_rgw_opa_url) |

**کارکرد:** URL to OPA server.

**زمان استفاده:** هنگام یکپارچه‌سازی با سرویس خارجی تنظیم کنید؛ اگر قابلیت استفاده نمی‌شود خالی بگذارید.

**مثال:**

```bash
ceph config set client.rgw rgw_opa_url "https://opa.example.com:8181/v1/data/ceph/authz"
ceph config get client.rgw rgw_opa_url
# curl -k <url>  # from each RGW node
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Connectivity

1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).
2. From **each** RGW node: `curl -k <url>` or vendor health check.
3. Pick the lowest-latency endpoint that stays healthy over 24h.
4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).
5. Leave empty (`(empty)`) if the integration is disabled.

```bash
ceph config get client.rgw rgw_opa_url
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_opa_verify_ssl

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_opa_verify_ssl](../../../config/rgw/rgw.md#SP_rgw_opa_verify_ssl) |

**کارکرد:** Should RGW verify the OPA server SSL certificate.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_opa_verify_ssl false
ceph config get client.rgw rgw_opa_verify_ssl
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Production: prefer secure default (`True` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---

### rgw_use_opa_authz

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_use_opa_authz](../../../config/rgw/rgw.md#SP_rgw_use_opa_authz) |

**کارکرد:** Should OPA be used to authorize client requests.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_use_opa_authz true
ceph config get client.rgw rgw_use_opa_authz
ceph config set client.rgw rgw_opa_url "https://opa.example.com:8181/v1/data/ceph/authz"
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
