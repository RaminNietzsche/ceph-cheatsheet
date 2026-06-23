# LDAP

راهنمای عمیق پیکربندی RGW — 6 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_ldap_binddn](#rgw_ldap_binddn) | `uid=admin,cn=users,dc=example,dc=com` | Advanced | Policy |
| [rgw_ldap_dnattr](#rgw_ldap_dnattr) | `uid` | Advanced | Performance |
| [rgw_ldap_searchdn](#rgw_ldap_searchdn) | `cn=users,cn=accounts,dc=example,dc=com` | Advanced | Performance |
| [rgw_ldap_searchfilter](#rgw_ldap_searchfilter) | `(empty)` | Advanced | Performance |
| [rgw_ldap_secret](#rgw_ldap_secret) | `/etc/openldap/secret` | Advanced | Policy |
| [rgw_ldap_uri](#rgw_ldap_uri) | `(empty)` | Advanced | Connectivity |

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

### rgw_ldap_binddn

| | |
|---|---|
| نوع | Str · default `uid=admin,cn=users,dc=example,dc=com` · **Advanced** |
| جدول | [rgw.md#SP_rgw_ldap_binddn](../../../config/rgw/rgw.md#SP_rgw_ldap_binddn) |

**کارکرد:** LDAP entry RGW will bind with (user match).

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_ldap_binddn "uid=admin,cn=users,dc=example,dc=com"
ceph config get client.rgw rgw_ldap_binddn
ceph config set client.rgw rgw_s3_auth_use_ldap true
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Upstream default (`uid=admin,cn=users,dc=example,dc=com`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---

### rgw_ldap_dnattr

| | |
|---|---|
| نوع | Str · default `uid` · **Advanced** |
| جدول | [rgw.md#SP_rgw_ldap_dnattr](../../../config/rgw/rgw.md#SP_rgw_ldap_dnattr) |

**کارکرد:** LDAP attribute containing RGW user names (to form binddns).

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_ldap_dnattr uid
ceph config get client.rgw rgw_ldap_dnattr
ceph config set client.rgw rgw_s3_auth_use_ldap true
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `uid`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_ldap_dnattr
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_ldap_searchdn

| | |
|---|---|
| نوع | Str · default `cn=users,cn=accounts,dc=example,dc=com` · **Advanced** |
| جدول | [rgw.md#SP_rgw_ldap_searchdn](../../../config/rgw/rgw.md#SP_rgw_ldap_searchdn) |

**کارکرد:** LDAP search base (basedn).

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_ldap_searchdn "cn=users,cn=accounts,dc=example,dc=com"
ceph config get client.rgw rgw_ldap_searchdn
ceph config set client.rgw rgw_s3_auth_use_ldap true
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `cn=users,cn=accounts,dc=example,dc=com`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_ldap_searchdn
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_ldap_searchfilter

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_ldap_searchfilter](../../../config/rgw/rgw.md#SP_rgw_ldap_searchfilter) |

**کارکرد:** LDAP search filter.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_ldap_searchfilter <value>
ceph config get client.rgw rgw_ldap_searchfilter
ceph config set client.rgw rgw_s3_auth_use_ldap true
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_ldap_searchfilter
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_ldap_secret

| | |
|---|---|
| نوع | Str · default `/etc/openldap/secret` · **Advanced** |
| جدول | [rgw.md#SP_rgw_ldap_secret](../../../config/rgw/rgw.md#SP_rgw_ldap_secret) |

**کارکرد:** Path to file containing credentials for rgw_ldap_binddn.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_ldap_secret "/etc/openldap/secret"
ceph config get client.rgw rgw_ldap_secret
ceph config set client.rgw rgw_s3_auth_use_ldap true
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_ldap_uri

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_ldap_uri](../../../config/rgw/rgw.md#SP_rgw_ldap_uri) |

**کارکرد:** Space-separated list of LDAP servers in URI format, e.g., "ldaps://<ldap.your.domain>".

**زمان استفاده:** هنگام یکپارچه‌سازی با سرویس خارجی تنظیم کنید؛ اگر قابلیت استفاده نمی‌شود خالی بگذارید.

**مثال:**

```bash
ceph config set client.rgw rgw_ldap_uri "ldaps://ldap.example.com/"
ceph config get client.rgw rgw_ldap_uri
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
ceph config get client.rgw rgw_ldap_uri
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
