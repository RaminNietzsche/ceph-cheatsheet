# BitTorrent

راهنمای عمیق پیکربندی RGW — 8 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_torrent_comment](#rgw_torrent_comment) | `(empty)` | Advanced | عملکرد |
| [rgw_torrent_createby](#rgw_torrent_createby) | `(empty)` | Advanced | عملکرد |
| [rgw_torrent_encoding](#rgw_torrent_encoding) | `(empty)` | Advanced | عملکرد |
| [rgw_torrent_flag](#rgw_torrent_flag) | `False` | Advanced | سیاست |
| [rgw_torrent_max_size](#rgw_torrent_max_size) | `5_G` | Advanced | سیاست |
| [rgw_torrent_origin](#rgw_torrent_origin) | `(empty)` | Advanced | عملکرد |
| [rgw_torrent_sha_unit](#rgw_torrent_sha_unit) | `512_K` | Advanced | عملکرد |
| [rgw_torrent_tracker](#rgw_torrent_tracker) | `(empty)` | Advanced | عملکرد |

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

### rgw_torrent_comment

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_torrent_comment](../../../config/rgw/rgw.md#SP_rgw_torrent_comment) |

**کارکرد:** Torrent field comment

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_torrent_comment <value>
ceph config get client.rgw rgw_torrent_comment
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_torrent_comment
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_torrent_createby

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_torrent_createby](../../../config/rgw/rgw.md#SP_rgw_torrent_createby) |

**کارکرد:** torrent field created by

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_torrent_createby <value>
ceph config get client.rgw rgw_torrent_createby
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_torrent_createby
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_torrent_encoding

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_torrent_encoding](../../../config/rgw/rgw.md#SP_rgw_torrent_encoding) |

**کارکرد:** torrent field encoding

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_torrent_encoding <value>
ceph config get client.rgw rgw_torrent_encoding
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_torrent_encoding
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_torrent_flag

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_torrent_flag](../../../config/rgw/rgw.md#SP_rgw_torrent_flag) |

**کارکرد:** When true, uploaded objects will calculate and store a SHA256 hash of object data so the object can be retrieved as a torrent file

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_torrent_flag true
ceph config get client.rgw rgw_torrent_flag
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_torrent_max_size

| | |
|---|---|
| نوع | Size · default `5_G` · **Advanced** |
| جدول | [rgw.md#SP_rgw_torrent_max_size](../../../config/rgw/rgw.md#SP_rgw_torrent_max_size) |

**کارکرد:** Objects over this size will not store torrent info.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_torrent_max_size 5_G
ceph config get client.rgw rgw_torrent_max_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `5_G` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_torrent_origin

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_torrent_origin](../../../config/rgw/rgw.md#SP_rgw_torrent_origin) |

**کارکرد:** Torrent origin

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_torrent_origin <value>
ceph config get client.rgw rgw_torrent_origin
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_torrent_origin
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_torrent_sha_unit

| | |
|---|---|
| نوع | Size · default `512_K` · **Advanced** |
| جدول | [rgw.md#SP_rgw_torrent_sha_unit](../../../config/rgw/rgw.md#SP_rgw_torrent_sha_unit) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_torrent_sha_unit 512_K
ceph config get client.rgw rgw_torrent_sha_unit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `512_K`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_torrent_sha_unit
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_torrent_tracker

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_torrent_tracker](../../../config/rgw/rgw.md#SP_rgw_torrent_tracker) |

**کارکرد:** Torrent field announce and announce list

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_torrent_tracker <value>
ceph config get client.rgw rgw_torrent_tracker
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_torrent_tracker
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
