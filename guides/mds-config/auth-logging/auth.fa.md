# Auth & capabilities

راهنمای عمیق پیکربندی MDS — 12 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mds/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mds_cache_quiesce_splitauth](#mds_cache_quiesce_splitauth) | `True` | Advanced | Policy |
| [mds_cap_acquisition_throttle_retry_request_timeout](#mds_cap_acquisition_throttle_retry_request_timeout) | `0.5` | Advanced | Performance |
| [mds_cap_revoke_eviction_timeout](#mds_cap_revoke_eviction_timeout) | `0` | Advanced | Performance |
| [mds_debug_auth_pins](#mds_debug_auth_pins) | `False` | Dev | Dev |
| [mds_forward_all_requests_to_auth](#mds_forward_all_requests_to_auth) | `False` | Advanced | Policy |
| [mds_max_caps_per_client](#mds_max_caps_per_client) | `1_M` | Advanced | Performance |
| [mds_min_caps_per_client](#mds_min_caps_per_client) | `100` | Advanced | Performance |
| [mds_min_caps_working_set](#mds_min_caps_working_set) | `10000` | Advanced | Performance |
| [mds_recall_max_caps](#mds_recall_max_caps) | `30000` | Advanced | Performance |
| [mds_session_cap_acquisition_decay_rate](#mds_session_cap_acquisition_decay_rate) | `30` | Advanced | Performance |
| [mds_session_cap_acquisition_throttle](#mds_session_cap_acquisition_throttle) | `100000` | Advanced | Performance |
| [mds_session_max_caps_throttle_ratio](#mds_session_max_caps_throttle_ratio) | `1.1` | Advanced | Performance |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **Policy** | امنیت، سازگاری، پیش‌فرض‌های عملیاتی |
| **Capacity** | چیدمان دیسک، مسیرها، اندازه‌گیری |
| **Performance** | خط پایه → تغییر تدریجی → پایش کلاستر |
| **Connectivity** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **Dev** | در محیط عملیاتی همان پیش‌فرض upstream |

**ابزارهای مشترک:**

```bash
ceph config get <daemon> <option>  # e.g. mds
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mds_cache_quiesce_splitauth

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mds.md#SP_mds_cache_quiesce_splitauth](../../../config/mds/mds.md#SP_mds_cache_quiesce_splitauth) |

**کارکرد:** Allow recursive quiesce across auth boundaries

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mds mds_cache_quiesce_splitauth false
ceph config get mds mds_cache_quiesce_splitauth
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_cache_quiesce_splitauth
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_cap_acquisition_throttle_retry_request_timeout

| | |
|---|---|
| نوع | Float · default `0.5` · **Advanced** |
| جدول | [mds.md#SP_mds_cap_acquisition_throttle_retry_request_timeout](../../../config/mds/mds.md#SP_mds_cap_acquisition_throttle_retry_request_timeout) |

**کارکرد:** Timeout in seconds after which a client request is retried due to cap acquisition throttling

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_cap_acquisition_throttle_retry_request_timeout 0.5
ceph config get mds mds_cap_acquisition_throttle_retry_request_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_cap_acquisition_throttle_retry_request_timeout
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_cap_revoke_eviction_timeout

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [mds.md#SP_mds_cap_revoke_eviction_timeout](../../../config/mds/mds.md#SP_mds_cap_revoke_eviction_timeout) |

**کارکرد:** Seconds to wait before evicting a client that holds caps after revoke.

**زمان استفاده:** Increase for legacy clients that respond slowly to cap revokes; decrease to reclaim metadata cache faster.

**مثال:**

```bash
ceph config set mds mds_cap_revoke_eviction_timeout 0
ceph config get mds mds_cap_revoke_eviction_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_cap_revoke_eviction_timeout
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_debug_auth_pins

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_debug_auth_pins](../../../config/mds/mds.md#SP_mds_debug_auth_pins) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_debug_auth_pins true
ceph config get mds mds_debug_auth_pins
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_forward_all_requests_to_auth

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [mds.md#SP_mds_forward_all_requests_to_auth](../../../config/mds/mds.md#SP_mds_forward_all_requests_to_auth) |

**کارکرد:** always process op on auth mds

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set mds mds_forward_all_requests_to_auth true
ceph config get mds mds_forward_all_requests_to_auth
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_forward_all_requests_to_auth
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_max_caps_per_client

| | |
|---|---|
| نوع | Uint · default `1_M` · **Advanced** |
| جدول | [mds.md#SP_mds_max_caps_per_client](../../../config/mds/mds.md#SP_mds_max_caps_per_client) |

**کارکرد:** maximum number of capabilities a client may hold

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_max_caps_per_client 1_M
ceph config get mds mds_max_caps_per_client
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_max_caps_per_client
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_min_caps_per_client

| | |
|---|---|
| نوع | Uint · default `100` · **Advanced** |
| جدول | [mds.md#SP_mds_min_caps_per_client](../../../config/mds/mds.md#SP_mds_min_caps_per_client) |

**کارکرد:** minimum number of capabilities a client may hold

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_min_caps_per_client 100
ceph config get mds mds_min_caps_per_client
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `100`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_min_caps_per_client
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_min_caps_working_set

| | |
|---|---|
| نوع | Uint · default `10000` · **Advanced** |
| جدول | [mds.md#SP_mds_min_caps_working_set](../../../config/mds/mds.md#SP_mds_min_caps_working_set) |

**کارکرد:** number of capabilities a client may hold without cache pressure warnings generated

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_min_caps_working_set 10000
ceph config get mds mds_min_caps_working_set
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_min_caps_working_set
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_recall_max_caps

| | |
|---|---|
| نوع | Size · default `30000` · **Advanced** |
| جدول | [mds.md#SP_mds_recall_max_caps](../../../config/mds/mds.md#SP_mds_recall_max_caps) |

**کارکرد:** Maximum number of caps to recall from a client session in single recall. Note that this is an integer, though the default value may be displayed with a B suffix.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_recall_max_caps 30000
ceph config get mds mds_recall_max_caps
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `30000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_recall_max_caps
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_session_cap_acquisition_decay_rate

| | |
|---|---|
| نوع | Float · default `30` · **Advanced** |
| جدول | [mds.md#SP_mds_session_cap_acquisition_decay_rate](../../../config/mds/mds.md#SP_mds_session_cap_acquisition_decay_rate) |

**کارکرد:** Decay rate for session readdir caps leading to readdir throttle

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_session_cap_acquisition_decay_rate 30
ceph config get mds mds_session_cap_acquisition_decay_rate
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_session_cap_acquisition_decay_rate
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_session_cap_acquisition_throttle

| | |
|---|---|
| نوع | Uint · default `100000` · **Advanced** |
| جدول | [mds.md#SP_mds_session_cap_acquisition_throttle](../../../config/mds/mds.md#SP_mds_session_cap_acquisition_throttle) |

**کارکرد:** Throttle cap acquisition rate per client session to protect the MDS.

**زمان استفاده:** Tune when clients stampede caps after MDS restart or when many small files are opened concurrently.

**مثال:**

```bash
ceph config set mds mds_session_cap_acquisition_throttle 100000
ceph config get mds mds_session_cap_acquisition_throttle
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `100000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_session_cap_acquisition_throttle
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_session_max_caps_throttle_ratio

| | |
|---|---|
| نوع | Float · default `1.1` · **Advanced** |
| جدول | [mds.md#SP_mds_session_max_caps_throttle_ratio](../../../config/mds/mds.md#SP_mds_session_max_caps_throttle_ratio) |

**کارکرد:** Ratio of mds_max_caps_per_client that client must exceed before readdir may be throttled by cap acquisition throttle

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_session_max_caps_throttle_ratio 1.1
ceph config get mds mds_session_max_caps_throttle_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1.1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_session_max_caps_throttle_ratio
ceph -s
ceph fs status
ceph mds stat
```

---


[← نمای کلی](../OVERVIEW.md)
