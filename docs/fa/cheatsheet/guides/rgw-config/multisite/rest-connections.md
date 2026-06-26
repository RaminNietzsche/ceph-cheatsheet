# REST connections

راهنمای عمیق پیکربندی RGW — 3 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_rest_conn_connect_to_resolved_ips](#rgw_rest_conn_connect_to_resolved_ips) | `False` | Advanced | سیاست |
| [rgw_rest_conn_ip_fail_timeout_secs](#rgw_rest_conn_ip_fail_timeout_secs) | `2` | Advanced | عملکرد |
| [rgw_rest_getusage_op_compat](#rgw_rest_getusage_op_compat) | `False` | Advanced | سیاست |

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

### rgw_rest_conn_connect_to_resolved_ips

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_rest_conn_connect_to_resolved_ips](../../../config/rgw/rgw.md#SP_rgw_rest_conn_connect_to_resolved_ips) |

**کارکرد:** When an RGW endpoint hostname resolves to multiple A or AAAA records, libcurl normally connects to only the first address returned by DNS. Enabling this option causes RGW to resolve each configured endpoint into all of its addresses and distribute outgoing requests across them using round-robin, with per-IP health tracking. This applies to multisite replication traffic between zones (via RGWRESTConn). For example, in a multisite deployment where zone endpoints such as "https://zone-a.example.com" map to several backend RGW nodes, this allows inter-zone traffic to be spread across all peers without requiring an external load balancer.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**گزینه‌های مرتبط:**

- [`rgw_rest_conn_ip_fail_timeout_secs`](../../../config/rgw/rgw.md#SP_rgw_rest_conn_ip_fail_timeout_secs)

**مثال:**

```bash
ceph config set client.rgw rgw_rest_conn_connect_to_resolved_ips true
ceph config get client.rgw rgw_rest_conn_connect_to_resolved_ips
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_rest_conn_ip_fail_timeout_secs

| | |
|---|---|
| نوع | Uint · default `2` · **Advanced** |
| جدول | [rgw.md#SP_rgw_rest_conn_ip_fail_timeout_secs](../../../config/rgw/rgw.md#SP_rgw_rest_conn_ip_fail_timeout_secs) |

**کارکرد:** IP failure tracking timeout (requires rgw_rest_conn_connect_to_resolved_ips=true) When rgw_rest_conn_connect_to_resolved_ips is enabled, RGW tracks per-IP connection failures by remembering the timestamp of the most recent failure. This option controls how long (in seconds) an IP address remains marked as "failed" before RGW considers it eligible for retry. After this timeout expires, the IP will be tried again in the normal round-robin rotation.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`rgw_rest_conn_connect_to_resolved_ips`](../../../config/rgw/rgw.md#SP_rgw_rest_conn_connect_to_resolved_ips)

**مثال:**

```bash
ceph config set client.rgw rgw_rest_conn_ip_fail_timeout_secs 2
ceph config get client.rgw rgw_rest_conn_ip_fail_timeout_secs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `2` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**سیگنال‌ها:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_rest_conn_ip_fail_timeout_secs
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_rest_getusage_op_compat

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_rest_getusage_op_compat](../../../config/rgw/rgw.md#SP_rgw_rest_getusage_op_compat) |

**کارکرد:** REST GetUsage request backward compatibility

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_rest_getusage_op_compat true
ceph config get client.rgw rgw_rest_getusage_op_compat
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
