# Admin CORS

راهنمای عمیق پیکربندی RGW — 4 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_gcors_allow_headers](#rgw_gcors_allow_headers) | `(empty)` | Advanced | Performance |
| [rgw_gcors_allow_methods](#rgw_gcors_allow_methods) | `(empty)` | Advanced | Performance |
| [rgw_gcors_allow_origins](#rgw_gcors_allow_origins) | `(empty)` | Advanced | Performance |
| [rgw_gcors_expose_headers](#rgw_gcors_expose_headers) | `(empty)` | Advanced | Performance |

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

### rgw_gcors_allow_headers

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_gcors_allow_headers](../../../config/rgw/rgw.md#SP_rgw_gcors_allow_headers) |

**کارکرد:** When not empty, this value is returned as a response header Access-Control-Allow-Headers to preflight requests.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_gcors_allow_headers <value>
ceph config get client.rgw rgw_gcors_allow_headers
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_gcors_allow_headers
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_gcors_allow_methods

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_gcors_allow_methods](../../../config/rgw/rgw.md#SP_rgw_gcors_allow_methods) |

**کارکرد:** When not empty, this value is returned as a response header Access-Control-Allow-Methods.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_gcors_allow_methods <value>
ceph config get client.rgw rgw_gcors_allow_methods
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_gcors_allow_methods
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_gcors_allow_origins

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_gcors_allow_origins](../../../config/rgw/rgw.md#SP_rgw_gcors_allow_origins) |

**کارکرد:** When not empty, this value is returned as a response header Access-Control-Allow-Origins.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_gcors_allow_origins <value>
ceph config get client.rgw rgw_gcors_allow_origins
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_gcors_allow_origins
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_gcors_expose_headers

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_gcors_expose_headers](../../../config/rgw/rgw.md#SP_rgw_gcors_expose_headers) |

**کارکرد:** When not empty, this value is returned as a response header Access-Control-Expose-Headers.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_gcors_expose_headers <value>
ceph config get client.rgw rgw_gcors_expose_headers
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_gcors_expose_headers
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
