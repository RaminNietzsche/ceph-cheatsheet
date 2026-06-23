# REST connections

راهنمای عمیق پیکربندی RGW — 3 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_rest_conn_connect_to_resolved_ips](#rgw_rest_conn_connect_to_resolved_ips) | `False` | Advanced | Policy |
| [rgw_rest_conn_ip_fail_timeout_secs](#rgw_rest_conn_ip_fail_timeout_secs) | `2` | Advanced | Performance |
| [rgw_rest_getusage_op_compat](#rgw_rest_getusage_op_compat) | `False` | Advanced | Policy |

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

### rgw_rest_conn_connect_to_resolved_ips

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_rest_conn_connect_to_resolved_ips](../../../config/rgw/rgw.md#SP_rgw_rest_conn_connect_to_resolved_ips) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

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

**کارکرد:** IP failure tracking timeout (requires rgw_rest_conn_connect_to_resolved_ips=true)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

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
