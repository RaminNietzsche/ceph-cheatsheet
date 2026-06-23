# Quorum & Paxos

راهنمای عمیق پیکربندی MON — 14 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mon_accept_timeout_factor](#mon_accept_timeout_factor) | `2` | Advanced | عملکرد |
| [mon_election_default_strategy](#mon_election_default_strategy) | `1` | Advanced | عملکرد |
| [mon_election_timeout](#mon_election_timeout) | `5` | Advanced | عملکرد |
| [paxos_kill_at](#paxos_kill_at) | `0` | Dev | توسعه |
| [paxos_max_join_drift](#paxos_max_join_drift) | `10` | Advanced | عملکرد |
| [paxos_min](#paxos_min) | `500` | Advanced | عملکرد |
| [paxos_min_wait](#paxos_min_wait) | `0.05` | Advanced | عملکرد |
| [paxos_propose_interval](#paxos_propose_interval) | `1` | Advanced | عملکرد |
| [paxos_service_trim_max](#paxos_service_trim_max) | `500` | Advanced | عملکرد |
| [paxos_service_trim_max_multiplier](#paxos_service_trim_max_multiplier) | `20` | Advanced | عملکرد |
| [paxos_service_trim_min](#paxos_service_trim_min) | `250` | Advanced | عملکرد |
| [paxos_stash_full_interval](#paxos_stash_full_interval) | `25` | Advanced | عملکرد |
| [paxos_trim_max](#paxos_trim_max) | `500` | Advanced | عملکرد |
| [paxos_trim_min](#paxos_trim_min) | `250` | Advanced | عملکرد |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **سیاست** | امنیت، سازگاری، پیش‌فرض‌های عملیاتی |
| **ظرفیت** | چیدمان دیسک، مسیرها، اندازه‌گیری |
| **عملکرد** | خط پایه → تغییر تدریجی → پایش کلاستر |
| **اتصال** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **توسعه** | در محیط عملیاتی همان پیش‌فرض upstream |

**ابزارهای مشترک:**

```bash
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_accept_timeout_factor

| | |
|---|---|
| نوع | Float · default `2` · **Advanced** |
| جدول | [mon.md#SP_mon_accept_timeout_factor](../../../config/mon/mon.md#SP_mon_accept_timeout_factor) |

**کارکرد:** multiple of mon_lease for follower mons to accept proposed state changes before calling a new election

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_accept_timeout_factor 2
ceph config get mon mon_accept_timeout_factor
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_accept_timeout_factor
ceph -s
ceph mon stat
```

---

### mon_election_default_strategy

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [mon.md#SP_mon_election_default_strategy](../../../config/mon/mon.md#SP_mon_election_default_strategy) |

**کارکرد:** The election strategy to set when constructing the first monmap.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_election_default_strategy 1
ceph config get mon mon_election_default_strategy
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `3`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_election_default_strategy
ceph -s
ceph mon stat
```

---

### mon_election_timeout

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [mon.md#SP_mon_election_timeout](../../../config/mon/mon.md#SP_mon_election_timeout) |

**کارکرد:** maximum time for a mon election (seconds)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_election_timeout 5
ceph config get mon mon_election_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_election_timeout
ceph -s
ceph mon stat
```

---

### paxos_kill_at

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [paxos.md#SP_paxos_kill_at](../../../config/mon/paxos.md#SP_paxos_kill_at) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mon paxos_kill_at 64
ceph config get mon paxos_kill_at
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### paxos_max_join_drift

| | |
|---|---|
| نوع | Int · default `10` · **Advanced** |
| جدول | [paxos.md#SP_paxos_max_join_drift](../../../config/mon/paxos.md#SP_paxos_max_join_drift) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon paxos_max_join_drift 10
ceph config get mon paxos_max_join_drift
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon paxos_max_join_drift
ceph -s
ceph mon stat
```

---

### paxos_min

| | |
|---|---|
| نوع | Int · default `500` · **Advanced** |
| جدول | [paxos.md#SP_paxos_min](../../../config/mon/paxos.md#SP_paxos_min) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon paxos_min 500
ceph config get mon paxos_min
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `500`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon paxos_min
ceph -s
ceph mon stat
```

---

### paxos_min_wait

| | |
|---|---|
| نوع | Float · default `0.05` · **Advanced** |
| جدول | [paxos.md#SP_paxos_min_wait](../../../config/mon/paxos.md#SP_paxos_min_wait) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon paxos_min_wait 0.05
ceph config get mon paxos_min_wait
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.05`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon paxos_min_wait
ceph -s
ceph mon stat
```

---

### paxos_propose_interval

| | |
|---|---|
| نوع | Float · default `1` · **Advanced** |
| جدول | [paxos.md#SP_paxos_propose_interval](../../../config/mon/paxos.md#SP_paxos_propose_interval) |

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon paxos_propose_interval 1
ceph config get mon paxos_propose_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon paxos_propose_interval
ceph -s
ceph mon stat
```

---

### paxos_service_trim_max

| | |
|---|---|
| نوع | Uint · default `500` · **Advanced** |
| جدول | [paxos.md#SP_paxos_service_trim_max](../../../config/mon/paxos.md#SP_paxos_service_trim_max) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon paxos_service_trim_max 500
ceph config get mon paxos_service_trim_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `500`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon paxos_service_trim_max
ceph -s
ceph mon stat
```

---

### paxos_service_trim_max_multiplier

| | |
|---|---|
| نوع | Uint · default `20` · **Advanced** |
| جدول | [paxos.md#SP_paxos_service_trim_max_multiplier](../../../config/mon/paxos.md#SP_paxos_service_trim_max_multiplier) |

**کارکرد:** factor by which paxos_service_trim_max will be multiplied to get a new upper bound when trim sizes are high (0 disables it)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon paxos_service_trim_max_multiplier 20
ceph config get mon paxos_service_trim_max_multiplier
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `20`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon paxos_service_trim_max_multiplier
ceph -s
ceph mon stat
```

---

### paxos_service_trim_min

| | |
|---|---|
| نوع | Uint · default `250` · **Advanced** |
| جدول | [paxos.md#SP_paxos_service_trim_min](../../../config/mon/paxos.md#SP_paxos_service_trim_min) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon paxos_service_trim_min 250
ceph config get mon paxos_service_trim_min
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `250`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon paxos_service_trim_min
ceph -s
ceph mon stat
```

---

### paxos_stash_full_interval

| | |
|---|---|
| نوع | Int · default `25` · **Advanced** |
| جدول | [paxos.md#SP_paxos_stash_full_interval](../../../config/mon/paxos.md#SP_paxos_stash_full_interval) |

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon paxos_stash_full_interval 25
ceph config get mon paxos_stash_full_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `25`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon paxos_stash_full_interval
ceph -s
ceph mon stat
```

---

### paxos_trim_max

| | |
|---|---|
| نوع | Int · default `500` · **Advanced** |
| جدول | [paxos.md#SP_paxos_trim_max](../../../config/mon/paxos.md#SP_paxos_trim_max) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon paxos_trim_max 500
ceph config get mon paxos_trim_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `500`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon paxos_trim_max
ceph -s
ceph mon stat
```

---

### paxos_trim_min

| | |
|---|---|
| نوع | Int · default `250` · **Advanced** |
| جدول | [paxos.md#SP_paxos_trim_min](../../../config/mon/paxos.md#SP_paxos_trim_min) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon paxos_trim_min 250
ceph config get mon paxos_trim_min
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `250`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon paxos_trim_min
ceph -s
ceph mon stat
```

---


[← نمای کلی](../OVERVIEW.md)
