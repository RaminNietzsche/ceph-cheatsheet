# Keystone & STS

راهنمای عمیق پیکربندی RGW — 32 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_keystone_accepted_admin_roles](#rgw_keystone_accepted_admin_roles) | `(empty)` | Advanced | عملکرد |
| [rgw_keystone_accepted_reader_roles](#rgw_keystone_accepted_reader_roles) | `(empty)` | Advanced | عملکرد |
| [rgw_keystone_accepted_roles](#rgw_keystone_accepted_roles) | `Member, admin` | Advanced | عملکرد |
| [rgw_keystone_admin_domain](#rgw_keystone_admin_domain) | `(empty)` | Advanced | عملکرد |
| [rgw_keystone_admin_password](#rgw_keystone_admin_password) | `(empty)` | Advanced | سیاست |
| [rgw_keystone_admin_password_path](#rgw_keystone_admin_password_path) | `(empty)` | Advanced | ظرفیت |
| [rgw_keystone_admin_project](#rgw_keystone_admin_project) | `(empty)` | Advanced | عملکرد |
| [rgw_keystone_admin_tenant](#rgw_keystone_admin_tenant) | `(empty)` | Advanced | عملکرد |
| [rgw_keystone_admin_user](#rgw_keystone_admin_user) | `(empty)` | Advanced | عملکرد |
| [rgw_keystone_barbican_domain](#rgw_keystone_barbican_domain) | `(empty)` | Advanced | عملکرد |
| [rgw_keystone_barbican_password](#rgw_keystone_barbican_password) | `(empty)` | Advanced | سیاست |
| [rgw_keystone_barbican_project](#rgw_keystone_barbican_project) | `(empty)` | Advanced | عملکرد |
| [rgw_keystone_barbican_tenant](#rgw_keystone_barbican_tenant) | `(empty)` | Advanced | عملکرد |
| [rgw_keystone_barbican_user](#rgw_keystone_barbican_user) | `(empty)` | Advanced | عملکرد |
| [rgw_keystone_expired_token_cache_expiration](#rgw_keystone_expired_token_cache_expiration) | `3600` | Advanced | عملکرد |
| [rgw_keystone_implicit_tenants](#rgw_keystone_implicit_tenants) | `false` | Advanced | معماری |
| [rgw_keystone_scope_enabled](#rgw_keystone_scope_enabled) | `False` | Advanced | سیاست |
| [rgw_keystone_scope_include_roles](#rgw_keystone_scope_include_roles) | `True` | Advanced | سیاست |
| [rgw_keystone_scope_include_user](#rgw_keystone_scope_include_user) | `False` | Advanced | سیاست |
| [rgw_keystone_service_token_accepted_roles](#rgw_keystone_service_token_accepted_roles) | `admin` | Advanced | سیاست |
| [rgw_keystone_service_token_enabled](#rgw_keystone_service_token_enabled) | `False` | Advanced | سیاست |
| [rgw_keystone_token_cache_size](#rgw_keystone_token_cache_size) | `10000` | Advanced | عملکرد |
| [rgw_keystone_token_cache_ttl](#rgw_keystone_token_cache_ttl) | `300` | Advanced | عملکرد |
| [rgw_keystone_url](#rgw_keystone_url) | `(empty)` | Basic | اتصال |
| [rgw_keystone_verify_ssl](#rgw_keystone_verify_ssl) | `True` | Advanced | سیاست |
| [rgw_sts_client_id](#rgw_sts_client_id) | `(empty)` | Advanced | سیاست |
| [rgw_sts_client_secret](#rgw_sts_client_secret) | `(empty)` | Advanced | سیاست |
| [rgw_sts_entry](#rgw_sts_entry) | `sts` | Advanced | سیاست |
| [rgw_sts_key](#rgw_sts_key) | `(empty)` | Advanced | عملکرد |
| [rgw_sts_max_session_duration](#rgw_sts_max_session_duration) | `43200` | Advanced | سیاست |
| [rgw_sts_min_session_duration](#rgw_sts_min_session_duration) | `900` | Advanced | عملکرد |
| [rgw_sts_token_introspection_url](#rgw_sts_token_introspection_url) | `(empty)` | Advanced | اتصال |

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

### rgw_keystone_accepted_admin_roles

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_accepted_admin_roles](../../../config/rgw/rgw.md#SP_rgw_keystone_accepted_admin_roles) |

**کارکرد:** List of roles allowing user to gain admin privileges (Keystone).

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_accepted_admin_roles <value>
ceph config get client.rgw rgw_keystone_accepted_admin_roles
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_accepted_admin_roles
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_accepted_reader_roles

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_accepted_reader_roles](../../../config/rgw/rgw.md#SP_rgw_keystone_accepted_reader_roles) |

**کارکرد:** List of roles that can only be used for reads (Keystone).

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_accepted_reader_roles <value>
ceph config get client.rgw rgw_keystone_accepted_reader_roles
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_accepted_reader_roles
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_accepted_roles

| | |
|---|---|
| نوع | Str · default `Member, admin` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_accepted_roles](../../../config/rgw/rgw.md#SP_rgw_keystone_accepted_roles) |

**کارکرد:** Only users with one of these roles will be served when doing Keystone authentication.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_accepted_roles "Member, admin"
ceph config get client.rgw rgw_keystone_accepted_roles
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `Member, admin`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_accepted_roles
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_admin_domain

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_admin_domain](../../../config/rgw/rgw.md#SP_rgw_keystone_admin_domain) |

**کارکرد:** Keystone admin user domain (for Keystone v3).

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_admin_domain <value>
ceph config get client.rgw rgw_keystone_admin_domain
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_admin_domain
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_admin_password

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_admin_password](../../../config/rgw/rgw.md#SP_rgw_keystone_admin_password) |

**کارکرد:** DEPRECATED: Keystone admin password.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_admin_password "<from-secrets-manager>"
ceph config get client.rgw rgw_keystone_admin_password
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_admin_password_path

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_admin_password_path](../../../config/rgw/rgw.md#SP_rgw_keystone_admin_password_path) |

**کارکرد:** Path to a file containing the Keystone admin password.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_admin_password_path "/var/lib/ceph/radosgw"
ceph config get client.rgw rgw_keystone_admin_password_path
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`(empty)`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw rgw_keystone_admin_password_path)
iostat -x 5  # disk saturation
```

---

### rgw_keystone_admin_project

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_admin_project](../../../config/rgw/rgw.md#SP_rgw_keystone_admin_project) |

**کارکرد:** Keystone admin user project (for Keystone v3).

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_admin_project <value>
ceph config get client.rgw rgw_keystone_admin_project
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_admin_project
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_admin_tenant

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_admin_tenant](../../../config/rgw/rgw.md#SP_rgw_keystone_admin_tenant) |

**کارکرد:** Keystone admin user tenant.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_admin_tenant <value>
ceph config get client.rgw rgw_keystone_admin_tenant
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_admin_tenant
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_admin_user

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_admin_user](../../../config/rgw/rgw.md#SP_rgw_keystone_admin_user) |

**کارکرد:** Keystone admin user.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_admin_user <value>
ceph config get client.rgw rgw_keystone_admin_user
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_admin_user
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_barbican_domain

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_barbican_domain](../../../config/rgw/rgw.md#SP_rgw_keystone_barbican_domain) |

**کارکرد:** Keystone barbican user domain.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_barbican_domain <value>
ceph config get client.rgw rgw_keystone_barbican_domain
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_barbican_domain
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_barbican_password

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_barbican_password](../../../config/rgw/rgw.md#SP_rgw_keystone_barbican_password) |

**کارکرد:** Keystone password for barbican user.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_barbican_password "<from-secrets-manager>"
ceph config get client.rgw rgw_keystone_barbican_password
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_barbican_project

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_barbican_project](../../../config/rgw/rgw.md#SP_rgw_keystone_barbican_project) |

**کارکرد:** Keystone barbican user project (Keystone v3).

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_barbican_project <value>
ceph config get client.rgw rgw_keystone_barbican_project
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_barbican_project
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_barbican_tenant

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_barbican_tenant](../../../config/rgw/rgw.md#SP_rgw_keystone_barbican_tenant) |

**کارکرد:** Keystone barbican user tenant (Keystone v2.0).

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_barbican_tenant <value>
ceph config get client.rgw rgw_keystone_barbican_tenant
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_barbican_tenant
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_barbican_user

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_barbican_user](../../../config/rgw/rgw.md#SP_rgw_keystone_barbican_user) |

**کارکرد:** Keystone user to access barbican secrets.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_barbican_user <value>
ceph config get client.rgw rgw_keystone_barbican_user
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_barbican_user
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_expired_token_cache_expiration

| | |
|---|---|
| نوع | Int · default `3600` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_expired_token_cache_expiration](../../../config/rgw/rgw.md#SP_rgw_keystone_expired_token_cache_expiration) |

**کارکرد:** The number of seconds to add to current time for expired token expiration

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_expired_token_cache_expiration 3600
ceph config get client.rgw rgw_keystone_expired_token_cache_expiration
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `3600`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**سیگنال‌ها:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_keystone_expired_token_cache_expiration
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_implicit_tenants

| | |
|---|---|
| نوع | Str · enum: ["false", "true", "swift", "s3", "both", "0", "1", "none"] · default `false` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_implicit_tenants](../../../config/rgw/rgw.md#SP_rgw_keystone_implicit_tenants) |

**کارکرد:** RGW Keystone implicit tenants creation

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_implicit_tenants false
ceph config get client.rgw rgw_keystone_implicit_tenants
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Valid values: ["false", "true", "swift", "s3", "both", "0", "1", "none"].
2. Default `false` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_keystone_scope_enabled

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_scope_enabled](../../../config/rgw/rgw.md#SP_rgw_keystone_scope_enabled) |

**کارکرد:** Enable logging of Keystone scope information in ops log

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_scope_enabled true
ceph config get client.rgw rgw_keystone_scope_enabled
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_scope_include_roles

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_scope_include_roles](../../../config/rgw/rgw.md#SP_rgw_keystone_scope_include_roles) |

**کارکرد:** Include role names in Keystone scope logs

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_scope_include_roles false
ceph config get client.rgw rgw_keystone_scope_include_roles
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_scope_include_user

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_scope_include_user](../../../config/rgw/rgw.md#SP_rgw_keystone_scope_include_user) |

**کارکرد:** Include human-readable identity names in Keystone scope logs

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_scope_include_user true
ceph config get client.rgw rgw_keystone_scope_include_user
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_service_token_accepted_roles

| | |
|---|---|
| نوع | Str · default `admin` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_service_token_accepted_roles](../../../config/rgw/rgw.md#SP_rgw_keystone_service_token_accepted_roles) |

**کارکرد:** Only users with one of these roles will be valid for service users.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_service_token_accepted_roles admin
ceph config get client.rgw rgw_keystone_service_token_accepted_roles
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_service_token_enabled

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_service_token_enabled](../../../config/rgw/rgw.md#SP_rgw_keystone_service_token_enabled) |

**کارکرد:** Service tokens allowing the usage of expired Keystone auth tokens

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_service_token_enabled true
ceph config get client.rgw rgw_keystone_service_token_enabled
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_token_cache_size

| | |
|---|---|
| نوع | Int · default `10000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_token_cache_size](../../../config/rgw/rgw.md#SP_rgw_keystone_token_cache_size) |

**کارکرد:** Keystone token cache size

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_token_cache_size 10000
ceph config get client.rgw rgw_keystone_token_cache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**سیگنال‌ها:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_keystone_token_cache_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_token_cache_ttl

| | |
|---|---|
| نوع | Int · default `300` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_token_cache_ttl](../../../config/rgw/rgw.md#SP_rgw_keystone_token_cache_ttl) |

**کارکرد:** Keystone token secret key cache TTL

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_token_cache_ttl 300
ceph config get client.rgw rgw_keystone_token_cache_ttl
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `300`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**سیگنال‌ها:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_keystone_token_cache_ttl
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_url

| | |
|---|---|
| نوع | Str · default `(empty)` · **Basic** |
| جدول | [rgw.md#SP_rgw_keystone_url](../../../config/rgw/rgw.md#SP_rgw_keystone_url) |

**کارکرد:** The URL to the Keystone server.

**زمان استفاده:** هنگام یکپارچه‌سازی با سرویس خارجی تنظیم کنید؛ اگر قابلیت استفاده نمی‌شود خالی بگذارید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_url "https://keystone.example.com:5000/v3/"
ceph config get client.rgw rgw_keystone_url
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
ceph config get client.rgw rgw_keystone_url
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_verify_ssl

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_keystone_verify_ssl](../../../config/rgw/rgw.md#SP_rgw_keystone_verify_ssl) |

**کارکرد:** Should RGW verify the Keystone server SSL certificate.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_keystone_verify_ssl false
ceph config get client.rgw rgw_keystone_verify_ssl
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_sts_client_id

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_sts_client_id](../../../config/rgw/rgw.md#SP_rgw_sts_client_id) |

**کارکرد:** Client Id

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_sts_client_id <value>
ceph config get client.rgw rgw_sts_client_id
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Upstream default (`(empty)`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---

### rgw_sts_client_secret

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_sts_client_secret](../../../config/rgw/rgw.md#SP_rgw_sts_client_secret) |

**کارکرد:** Client Secret

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_sts_client_secret "<from-secrets-manager>"
ceph config get client.rgw rgw_sts_client_secret
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_sts_entry

| | |
|---|---|
| نوع | Str · default `sts` · **Advanced** |
| جدول | [rgw.md#SP_rgw_sts_entry](../../../config/rgw/rgw.md#SP_rgw_sts_entry) |

**کارکرد:** STS URL prefix

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_sts_entry sts
ceph config get client.rgw rgw_sts_entry
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Upstream default (`sts`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---

### rgw_sts_key

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_sts_key](../../../config/rgw/rgw.md#SP_rgw_sts_key) |

**کارکرد:** STS Key

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_sts_key "<from-secrets-manager>"
ceph config get client.rgw rgw_sts_key
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_sts_key
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_sts_max_session_duration

| | |
|---|---|
| نوع | Uint · default `43200` · **Advanced** |
| جدول | [rgw.md#SP_rgw_sts_max_session_duration](../../../config/rgw/rgw.md#SP_rgw_sts_max_session_duration) |

**کارکرد:** Session token max duration

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_sts_max_session_duration 43200
ceph config get client.rgw rgw_sts_max_session_duration
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `43200` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_sts_min_session_duration

| | |
|---|---|
| نوع | Uint · default `900` · **Advanced** |
| جدول | [rgw.md#SP_rgw_sts_min_session_duration](../../../config/rgw/rgw.md#SP_rgw_sts_min_session_duration) |

**کارکرد:** Minimum allowed duration of a session

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_sts_min_session_duration 900
ceph config get client.rgw rgw_sts_min_session_duration
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `900`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_sts_min_session_duration
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_sts_token_introspection_url

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_sts_token_introspection_url](../../../config/rgw/rgw.md#SP_rgw_sts_token_introspection_url) |

**کارکرد:** STS Web Token introspection URL

**زمان استفاده:** هنگام یکپارچه‌سازی با سرویس خارجی تنظیم کنید؛ اگر قابلیت استفاده نمی‌شود خالی بگذارید.

**مثال:**

```bash
ceph config set client.rgw rgw_sts_token_introspection_url "https://idp.example.com/oauth2/introspect"
ceph config get client.rgw rgw_sts_token_introspection_url
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
ceph config get client.rgw rgw_sts_token_introspection_url
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
