# Quota sync & defaults

راهنمای عمیق پیکربندی RGW — 5 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

اعمال quota همچنین به `rgw_enable_quota_threads` روی حداقل یک RGW در هر zone نیاز دارد. [rgw_enable_quota_threads](../../../config/rgw/rgw.md#SP_rgw_enable_quota_threads) را ببینید.

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_account_default_quota_max_objects](#rgw_account_default_quota_max_objects) | `-1` | Basic | سیاست |
| [rgw_account_default_quota_max_size](#rgw_account_default_quota_max_size) | `-1` | Basic | سیاست |
| [rgw_enable_quota_threads](#rgw_enable_quota_threads) | `True` | Advanced | سیاست |
| [rgw_user_default_quota_max_objects](#rgw_user_default_quota_max_objects) | `-1` | Basic | سیاست |
| [rgw_user_default_quota_max_size](#rgw_user_default_quota_max_size) | `-1` | Basic | سیاست |

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

### rgw_account_default_quota_max_objects

| | |
|---|---|
| نوع | Int · default `-1` · **Basic** |
| جدول | [rgw.md#SP_rgw_account_default_quota_max_objects](../../../config/rgw/rgw.md#SP_rgw_account_default_quota_max_objects) |

**کارکرد:** Default cap on **total object count** across all buckets owned by a **new** S3 account. `-1` means unlimited.

**زمان استفاده:** Multi-tenant platforms using the account abstraction. Applies only when accounts are created — existing accounts are unchanged.

**گزینه‌های مرتبط:**

- `rgw_account_default_quota_max_size`
- `rgw_enable_quota_threads` (required on at least one RGW per zone)

**مثال:**

```bash
ceph config set client rgw_account_default_quota_max_objects 1000000
radosgw-admin user create --uid=alice --display-name="Alice"
radosgw-admin quota get --quota-scope=user --uid=alice
```

Set in `[client]` or global so `radosgw-admin` picks it up.

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. `ceph df detail` — usable cluster capacity.
2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.
3. Set limit; `-1` means unlimited. Default: `-1`.
4. Create a test user and confirm via `radosgw-admin quota get --quota-scope=user --uid=<uid>`.
5. Existing users/accounts are **not** retroactively changed.

```bash
ceph df detail
radosgw-admin quota get --quota-scope=user --uid=testuser
radosgw-admin bucket stats --bucket=testbucket
```

---

### rgw_account_default_quota_max_size

| | |
|---|---|
| نوع | Int · default `-1` · **Basic** |
| جدول | [rgw.md#SP_rgw_account_default_quota_max_size](../../../config/rgw/rgw.md#SP_rgw_account_default_quota_max_size) |

**کارکرد:** Default cap on **total stored bytes** for a new account.

**زمان استفاده:** محدودیت پیش‌فرض tenant یا پلتفرم برای کاربران، account یا bucket جدید.

**مثال:**

```bash
# 10 TiB
ceph config set client rgw_account_default_quota_max_size $((10*1024*1024*1024*1024))
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. `ceph df detail` — usable cluster capacity.
2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.
3. Set limit; `-1` means unlimited. Default: `-1`.
4. Create a test user and confirm via `radosgw-admin quota get --quota-scope=user --uid=<uid>`.
5. Existing users/accounts are **not** retroactively changed.

```bash
ceph df detail
radosgw-admin quota get --quota-scope=user --uid=testuser
radosgw-admin bucket stats --bucket=testbucket
```

---

### rgw_enable_quota_threads

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_enable_quota_threads](../../../config/rgw/rgw.md#SP_rgw_enable_quota_threads) |

**کارکرد:** Enables the quota maintenance thread.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_enable_quota_threads false
ceph config get client.rgw rgw_enable_quota_threads
radosgw-admin quota get --quota-scope=user --uid=testuser
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_user_default_quota_max_objects

| | |
|---|---|
| نوع | Int · default `-1` · **Basic** |
| جدول | [rgw.md#SP_rgw_user_default_quota_max_objects](../../../config/rgw/rgw.md#SP_rgw_user_default_quota_max_objects) |

**کارکرد:** User quota max objects

**زمان استفاده:** محدودیت پیش‌فرض tenant یا پلتفرم برای کاربران، account یا bucket جدید.

**مثال:**

```bash
ceph config set client rgw_user_default_quota_max_objects 1000000
ceph config get client rgw_user_default_quota_max_objects
radosgw-admin quota get --quota-scope=user --uid=testuser
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. `ceph df detail` — usable cluster capacity.
2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.
3. Set limit; `-1` means unlimited. Default: `-1`.
4. Create a test user and confirm via `radosgw-admin quota get --quota-scope=user --uid=<uid>`.
5. Existing users/accounts are **not** retroactively changed.

```bash
ceph df detail
radosgw-admin quota get --quota-scope=user --uid=testuser
radosgw-admin bucket stats --bucket=testbucket
```

---

### rgw_user_default_quota_max_size

| | |
|---|---|
| نوع | Int · default `-1` · **Basic** |
| جدول | [rgw.md#SP_rgw_user_default_quota_max_size](../../../config/rgw/rgw.md#SP_rgw_user_default_quota_max_size) |

**کارکرد:** User quota max size

**زمان استفاده:** محدودیت پیش‌فرض tenant یا پلتفرم برای کاربران، account یا bucket جدید.

**مثال:**

```bash
ceph config set client rgw_user_default_quota_max_size $((100*1024*1024*1024))
ceph config get client rgw_user_default_quota_max_size
radosgw-admin quota get --quota-scope=user --uid=testuser
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. `ceph df detail` — usable cluster capacity.
2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.
3. Set limit; `-1` means unlimited. Default: `-1`.
4. Create a test user and confirm via `radosgw-admin quota get --quota-scope=user --uid=<uid>`.
5. Existing users/accounts are **not** retroactively changed.

```bash
ceph df detail
radosgw-admin quota get --quota-scope=user --uid=testuser
radosgw-admin bucket stats --bucket=testbucket
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
