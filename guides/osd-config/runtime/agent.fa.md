# Cache agent

راهنمای عمیق پیکربندی OSD — 7 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [osd_agent_delay_time](#osd_agent_delay_time) | `5` | Advanced | Performance |
| [osd_agent_hist_halflife](#osd_agent_hist_halflife) | `1000` | Advanced | Performance |
| [osd_agent_max_low_ops](#osd_agent_max_low_ops) | `2` | Advanced | Performance |
| [osd_agent_max_ops](#osd_agent_max_ops) | `4` | Advanced | Performance |
| [osd_agent_min_evict_effort](#osd_agent_min_evict_effort) | `0.1` | Advanced | Performance |
| [osd_agent_quantize_effort](#osd_agent_quantize_effort) | `0.1` | Advanced | Performance |
| [osd_agent_slop](#osd_agent_slop) | `0.02` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. osd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_agent_delay_time

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [osd.md#SP_osd_agent_delay_time](../../../config/osd/osd.md#SP_osd_agent_delay_time) |

**کارکرد:** how long agent should sleep if it has no work to do

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_agent_delay_time 5
ceph config get osd osd_agent_delay_time
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_agent_delay_time
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_agent_hist_halflife

| | |
|---|---|
| نوع | Int · default `1000` · **Advanced** |
| جدول | [osd.md#SP_osd_agent_hist_halflife](../../../config/osd/osd.md#SP_osd_agent_hist_halflife) |

**کارکرد:** halflife of agent atime and temp histograms

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_agent_hist_halflife 1000
ceph config get osd osd_agent_hist_halflife
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_agent_hist_halflife
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_agent_max_low_ops

| | |
|---|---|
| نوع | Int · default `2` · **Advanced** |
| جدول | [osd.md#SP_osd_agent_max_low_ops](../../../config/osd/osd.md#SP_osd_agent_max_low_ops) |

**کارکرد:** maximum concurrent low-priority tiering operations for tiering agent

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_agent_max_low_ops 2
ceph config get osd osd_agent_max_low_ops
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_agent_max_low_ops
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_agent_max_ops

| | |
|---|---|
| نوع | Int · default `4` · **Advanced** |
| جدول | [osd.md#SP_osd_agent_max_ops](../../../config/osd/osd.md#SP_osd_agent_max_ops) |

**کارکرد:** maximum concurrent tiering operations for tiering agent

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_agent_max_ops 4
ceph config get osd osd_agent_max_ops
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `4`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_agent_max_ops
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_agent_min_evict_effort

| | |
|---|---|
| نوع | Float · default `0.1` · **Advanced** |
| جدول | [osd.md#SP_osd_agent_min_evict_effort](../../../config/osd/osd.md#SP_osd_agent_min_evict_effort) |

**کارکرد:** minimum effort to expend evicting clean objects

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_agent_min_evict_effort 0.1
ceph config get osd osd_agent_min_evict_effort
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `0.99`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_agent_min_evict_effort
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_agent_quantize_effort

| | |
|---|---|
| نوع | Float · default `0.1` · **Advanced** |
| جدول | [osd.md#SP_osd_agent_quantize_effort](../../../config/osd/osd.md#SP_osd_agent_quantize_effort) |

**کارکرد:** size of quantize unit for eviction effort

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_agent_quantize_effort 0.1
ceph config get osd osd_agent_quantize_effort
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_agent_quantize_effort
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_agent_slop

| | |
|---|---|
| نوع | Float · default `0.02` · **Advanced** |
| جدول | [osd.md#SP_osd_agent_slop](../../../config/osd/osd.md#SP_osd_agent_slop) |

**کارکرد:** slop factor to avoid switching tiering flush and eviction mode

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_agent_slop 0.02
ceph config get osd osd_agent_slop
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.02`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_agent_slop
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← نمای کلی](../OVERVIEW.md)
