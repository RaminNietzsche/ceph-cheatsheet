# Ops logging

راهنمای عمیق پیکربندی RGW — 4 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_ops_log_data_backlog](#rgw_ops_log_data_backlog) | `5_M` | Advanced | Performance |
| [rgw_ops_log_file_path](#rgw_ops_log_file_path) | `/var/log/ceph/ops-log-$cluster-$name.log` | Advanced | Capacity |
| [rgw_ops_log_rados](#rgw_ops_log_rados) | `False` | Advanced | Policy |
| [rgw_ops_log_socket_path](#rgw_ops_log_socket_path) | `(empty)` | Advanced | Capacity |

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

### rgw_ops_log_data_backlog

| | |
|---|---|
| نوع | Size · default `5_M` · **Advanced** |
| جدول | [rgw.md#SP_rgw_ops_log_data_backlog](../../../config/rgw/rgw.md#SP_rgw_ops_log_data_backlog) |

**کارکرد:** Ops log socket backlog

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_ops_log_data_backlog 5_M
ceph config get client.rgw rgw_ops_log_data_backlog
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `5_M`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_ops_log_data_backlog
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_ops_log_file_path

| | |
|---|---|
| نوع | Str · default `/var/log/ceph/ops-log-$cluster-$name.log` · **Advanced** |
| جدول | [rgw.md#SP_rgw_ops_log_file_path](../../../config/rgw/rgw.md#SP_rgw_ops_log_file_path) |

**کارکرد:** File-system path for ops log.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_ops_log_file_path "/var/log/ceph/ops-log-$cluster-$name.log"
ceph config get client.rgw rgw_ops_log_file_path
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`/var/log/ceph/ops-log-$cluster-$name.log`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw rgw_ops_log_file_path)
iostat -x 5  # disk saturation
```

---

### rgw_ops_log_rados

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_ops_log_rados](../../../config/rgw/rgw.md#SP_rgw_ops_log_rados) |

**کارکرد:** Use RADOS for ops log

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_ops_log_rados true
ceph config get client.rgw rgw_ops_log_rados
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_ops_log_socket_path

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_ops_log_socket_path](../../../config/rgw/rgw.md#SP_rgw_ops_log_socket_path) |

**کارکرد:** Unix domain socket path for ops log.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_ops_log_socket_path "/var/lib/ceph/radosgw"
ceph config get client.rgw rgw_ops_log_socket_path
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`(empty)`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw rgw_ops_log_socket_path)
iostat -x 5  # disk saturation
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
