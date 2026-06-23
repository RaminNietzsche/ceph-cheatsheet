# Debug & fault injection

راهنمای عمیق پیکربندی RGW — 7 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_debug_inject_latency_bi_unlink](#rgw_debug_inject_latency_bi_unlink) | `0` | Dev | Dev |
| [rgw_debug_inject_olh_cancel_modification_err](#rgw_debug_inject_olh_cancel_modification_err) | `False` | Dev | Dev |
| [rgw_debug_inject_set_olh_err](#rgw_debug_inject_set_olh_err) | `0` | Dev | Dev |
| [rgw_inject_delay_pattern](#rgw_inject_delay_pattern) | `(empty)` | Dev | Dev |
| [rgw_inject_delay_sec](#rgw_inject_delay_sec) | `0` | Dev | Dev |
| [rgw_mp_lock_inject_delay](#rgw_mp_lock_inject_delay) | `0` | Dev | Dev |
| [rgw_mp_lock_inject_renewal_error](#rgw_mp_lock_inject_renewal_error) | `0` | Dev | Dev |

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

### rgw_debug_inject_latency_bi_unlink

| | |
|---|---|
| نوع | Uint · default `0` · **Dev** |
| جدول | [rgw.md#SP_rgw_debug_inject_latency_bi_unlink](../../../config/rgw/rgw.md#SP_rgw_debug_inject_latency_bi_unlink) |

**کارکرد:** Latency (in seconds) injected before rgw bucket index unlink op calls to simulate queueing latency and validate behavior of simultaneous delete requests which target the same object.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_debug_inject_latency_bi_unlink 0
ceph config get client.rgw rgw_debug_inject_latency_bi_unlink
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_debug_inject_olh_cancel_modification_err

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [rgw.md#SP_rgw_debug_inject_olh_cancel_modification_err](../../../config/rgw/rgw.md#SP_rgw_debug_inject_olh_cancel_modification_err) |

**کارکرد:** Whether to inject an error to simulate a failure to cancel olh modification. This exists for development and testing purposes.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_debug_inject_olh_cancel_modification_err true
ceph config get client.rgw rgw_debug_inject_olh_cancel_modification_err
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`False`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_debug_inject_set_olh_err

| | |
|---|---|
| نوع | Uint · default `0` · **Dev** |
| جدول | [rgw.md#SP_rgw_debug_inject_set_olh_err](../../../config/rgw/rgw.md#SP_rgw_debug_inject_set_olh_err) |

**کارکرد:** Whether to inject errors between rados olh modification initialization and bucket index instance linking. The value determines the error code. This exists for development and testing purposes to help simulate cases where bucket index entries aren't cleaned up by the request thread after an error scenario.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_debug_inject_set_olh_err 0
ceph config get client.rgw rgw_debug_inject_set_olh_err
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_inject_delay_pattern

| | |
|---|---|
| نوع | Str · default `(empty)` · **Dev** |
| جدول | [rgw.md#SP_rgw_inject_delay_pattern](../../../config/rgw/rgw.md#SP_rgw_inject_delay_pattern) |

**کارکرد:** select which delay injection points are activated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_inject_delay_pattern <value>
ceph config get client.rgw rgw_inject_delay_pattern
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`(empty)`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_inject_delay_sec

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [rgw.md#SP_rgw_inject_delay_sec](../../../config/rgw/rgw.md#SP_rgw_inject_delay_sec) |

**کارکرد:** delay duration in seconds for test injection points

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_inject_delay_sec 0
ceph config get client.rgw rgw_inject_delay_sec
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_mp_lock_inject_delay

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [rgw.md#SP_rgw_mp_lock_inject_delay](../../../config/rgw/rgw.md#SP_rgw_mp_lock_inject_delay) |

**کارکرد:** Injected delay after acquiring the multipart lock for renewal testing

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_mp_lock_inject_delay 0
ceph config get client.rgw rgw_mp_lock_inject_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_mp_lock_inject_renewal_error

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [rgw.md#SP_rgw_mp_lock_inject_renewal_error](../../../config/rgw/rgw.md#SP_rgw_mp_lock_inject_renewal_error) |

**کارکرد:** Injected error code for multipart lock renewal testing

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_mp_lock_inject_renewal_error 0
ceph config get client.rgw rgw_mp_lock_inject_renewal_error
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
