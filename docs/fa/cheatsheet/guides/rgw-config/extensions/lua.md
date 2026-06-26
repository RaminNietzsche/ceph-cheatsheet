# Lua scripting

راهنمای عمیق پیکربندی RGW — 4 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_lua_enable](#rgw_lua_enable) | `True` | Advanced | سیاست |
| [rgw_lua_max_memory_per_state](#rgw_lua_max_memory_per_state) | `128000` | Advanced | سیاست |
| [rgw_lua_max_runtime_per_state](#rgw_lua_max_runtime_per_state) | `1000` | Advanced | سیاست |
| [rgw_luarocks_location](#rgw_luarocks_location) | `/tmp/rgw_luarocks/$name` | Advanced | عملکرد |

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

### rgw_lua_enable

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [rgw.md#SP_rgw_lua_enable](../../../config/rgw/rgw.md#SP_rgw_lua_enable) |

**کارکرد:** Enable lua scripting.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_lua_enable false
ceph config get client.rgw rgw_lua_enable
ceph orch restart rgw
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_lua_max_memory_per_state

| | |
|---|---|
| نوع | Uint · default `128000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_lua_max_memory_per_state](../../../config/rgw/rgw.md#SP_rgw_lua_max_memory_per_state) |

**کارکرد:** Max size of memory used by a single lua state This is the maximum size in bytes that a lua state can allocate for its own use. Note that this does not include any memory that can be accessed from lua, but managed by the RGW. If not set, it would use a default of 128K. If set to zero, the amount of memory would only be limited by the system.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_lua_max_memory_per_state 128000
ceph config get client.rgw rgw_lua_max_memory_per_state
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `128000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_lua_max_runtime_per_state

| | |
|---|---|
| نوع | Uint · default `1000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_lua_max_runtime_per_state](../../../config/rgw/rgw.md#SP_rgw_lua_max_runtime_per_state) |

**کارکرد:** Maximum runtime for each Lua state in milliseconds Sets the maximum runtime for each Lua state in milliseconds. If exceeded, the script will be terminated. Defaults to 1000 milliseconds (1 second). If set to zero, there is no limit.

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه یا هم‌زمانی (concurrency) می‌رسند، یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_lua_max_runtime_per_state 1000
ceph config get client.rgw rgw_lua_max_runtime_per_state
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_luarocks_location

| | |
|---|---|
| نوع | Str · default `/tmp/rgw_luarocks/$name` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [rgw.md#SP_rgw_luarocks_location](../../../config/rgw/rgw.md#SP_rgw_luarocks_location) |

**کارکرد:** Directory where luarocks install packages from allowlist

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_luarocks_location "/tmp/rgw_luarocks/$name"
ceph config get client.rgw rgw_luarocks_location
ceph orch restart rgw
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `/tmp/rgw_luarocks/$name`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_luarocks_location
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
