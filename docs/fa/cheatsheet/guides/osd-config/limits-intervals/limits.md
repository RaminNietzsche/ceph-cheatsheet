# Limits & caps

راهنمای عمیق پیکربندی OSD — 15 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [osd_check_max_object_name_len_on_startup](#osd_check_max_object_name_len_on_startup) | `True` | Dev | توسعه |
| [osd_client_message_cap](#osd_client_message_cap) | `256` | Advanced | عملکرد |
| [osd_client_message_size_cap](#osd_client_message_size_cap) | `500_M` | Advanced | عملکرد |
| [osd_copyfrom_max_chunk](#osd_copyfrom_max_chunk) | `8_M` | Advanced | عملکرد |
| [osd_heartbeat_min_peers](#osd_heartbeat_min_peers) | `10` | Advanced | عملکرد |
| [osd_map_share_max_epochs](#osd_map_share_max_epochs) | `40` | Advanced | عملکرد |
| [osd_max_markdown_count](#osd_max_markdown_count) | `5` | Advanced | عملکرد |
| [osd_max_pgls](#osd_max_pgls) | `1_K` | Advanced | عملکرد |
| [osd_max_push_cost](#osd_max_push_cost) | `8_M` | Advanced | عملکرد |
| [osd_max_push_objects](#osd_max_push_objects) | `10` | Advanced | عملکرد |
| [osd_max_write_size](#osd_max_write_size) | `90` | Advanced | عملکرد |
| [osd_op_pq_max_tokens_per_priority](#osd_op_pq_max_tokens_per_priority) | `4_M` | Advanced | عملکرد |
| [osd_op_pq_min_cost](#osd_op_pq_min_cost) | `64_K` | Advanced | عملکرد |
| [osd_pg_epoch_max_lag_factor](#osd_pg_epoch_max_lag_factor) | `2` | Advanced | عملکرد |
| [set_keepcaps](#set_keepcaps) | `False` | Advanced | عملکرد |

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
ceph config get <daemon> <option>  # e.g. osd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_check_max_object_name_len_on_startup

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [osd.md#SP_osd_check_max_object_name_len_on_startup](../../../config/osd/osd.md#SP_osd_check_max_object_name_len_on_startup) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_check_max_object_name_len_on_startup false
ceph config get osd osd_check_max_object_name_len_on_startup
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_client_message_cap

| | |
|---|---|
| نوع | Uint · default `256` · **Advanced** |
| جدول | [osd.md#SP_osd_client_message_cap](../../../config/osd/osd.md#SP_osd_client_message_cap) |

**کارکرد:** maximum number of in-flight client requests

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_client_message_cap 256
ceph config get osd osd_client_message_cap
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `256`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_client_message_cap
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_client_message_size_cap

| | |
|---|---|
| نوع | Size · default `500_M` · **Advanced** |
| جدول | [osd.md#SP_osd_client_message_size_cap](../../../config/osd/osd.md#SP_osd_client_message_size_cap) |

**کارکرد:** maximum memory to devote to in-flight client requests If this value is exceeded, the OSD will not read any new client data off of the network until memory is freed.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_client_message_size_cap 500_M
ceph config get osd osd_client_message_size_cap
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `500_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_client_message_size_cap
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_copyfrom_max_chunk

| | |
|---|---|
| نوع | Size · default `8_M` · **Advanced** |
| جدول | [osd.md#SP_osd_copyfrom_max_chunk](../../../config/osd/osd.md#SP_osd_copyfrom_max_chunk) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_copyfrom_max_chunk 8_M
ceph config get osd osd_copyfrom_max_chunk
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `8_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_copyfrom_max_chunk
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_heartbeat_min_peers

| | |
|---|---|
| نوع | Int · default `10` · **Advanced** |
| جدول | [osd.md#SP_osd_heartbeat_min_peers](../../../config/osd/osd.md#SP_osd_heartbeat_min_peers) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_heartbeat_min_peers 10
ceph config get osd osd_heartbeat_min_peers
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_heartbeat_min_peers
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_map_share_max_epochs

| | |
|---|---|
| نوع | Int · default `40` · **Advanced** |
| جدول | [osd.md#SP_osd_map_share_max_epochs](../../../config/osd/osd.md#SP_osd_map_share_max_epochs) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_map_share_max_epochs 40
ceph config get osd osd_map_share_max_epochs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `40`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_map_share_max_epochs
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_markdown_count

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [osd.md#SP_osd_max_markdown_count](../../../config/osd/osd.md#SP_osd_max_markdown_count) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_max_markdown_count 5
ceph config get osd osd_max_markdown_count
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_max_markdown_count
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_pgls

| | |
|---|---|
| نوع | Uint · default `1_K` · **Advanced** |
| جدول | [osd.md#SP_osd_max_pgls](../../../config/osd/osd.md#SP_osd_max_pgls) |

**کارکرد:** maximum number of results when listing objects in a pool

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_max_pgls 1_K
ceph config get osd osd_max_pgls
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_max_pgls
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_push_cost

| | |
|---|---|
| نوع | Size · default `8_M` · **Advanced** |
| جدول | [osd.md#SP_osd_max_push_cost](../../../config/osd/osd.md#SP_osd_max_push_cost) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_max_push_cost 8_M
ceph config get osd osd_max_push_cost
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `8_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_max_push_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_push_objects

| | |
|---|---|
| نوع | Uint · default `10` · **Advanced** |
| جدول | [osd.md#SP_osd_max_push_objects](../../../config/osd/osd.md#SP_osd_max_push_objects) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_max_push_objects 10
ceph config get osd osd_max_push_objects
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_max_push_objects
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_write_size

| | |
|---|---|
| نوع | Size · default `90` · **Advanced** |
| جدول | [osd.md#SP_osd_max_write_size](../../../config/osd/osd.md#SP_osd_max_write_size) |

**کارکرد:** Maximum size of a RADOS write operation in megabytes This setting prevents clients from doing very large writes to RADOS. If you set this to a value below what clients expect, they will receive an error when attempting to write to the cluster.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_max_write_size 90
ceph config get osd osd_max_write_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `90`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `4`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_max_write_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_pq_max_tokens_per_priority

| | |
|---|---|
| نوع | Uint · default `4_M` · **Advanced** |
| جدول | [osd.md#SP_osd_op_pq_max_tokens_per_priority](../../../config/osd/osd.md#SP_osd_op_pq_max_tokens_per_priority) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_op_pq_max_tokens_per_priority 4_M
ceph config get osd osd_op_pq_max_tokens_per_priority
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `4_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_op_pq_max_tokens_per_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_pq_min_cost

| | |
|---|---|
| نوع | Size · default `64_K` · **Advanced** |
| جدول | [osd.md#SP_osd_op_pq_min_cost](../../../config/osd/osd.md#SP_osd_op_pq_min_cost) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_op_pq_min_cost 64_K
ceph config get osd osd_op_pq_min_cost
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_op_pq_min_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pg_epoch_max_lag_factor

| | |
|---|---|
| نوع | Float · default `2` · **Advanced** |
| جدول | [osd.md#SP_osd_pg_epoch_max_lag_factor](../../../config/osd/osd.md#SP_osd_pg_epoch_max_lag_factor) |

**کارکرد:** Max multiple of the map cache that PGs can lag before we throttle map injest

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**گزینه‌های مرتبط:**

- [`osd_map_cache_size`](../../../config/osd/osd.md#SP_osd_map_cache_size)

**مثال:**

```bash
ceph config set osd osd_pg_epoch_max_lag_factor 2
ceph config get osd osd_pg_epoch_max_lag_factor
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_pg_epoch_max_lag_factor
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### set_keepcaps

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [osd.md#SP_set_keepcaps](../../../config/osd/osd.md#SP_set_keepcaps) |

**کارکرد:** set the keepcaps flag before changing UID, preserving the permitted capability set When ceph switches from root to the ceph uid, all capabilities in all sets are eraseed. If a component that is capability aware needs a specific capability, the keepcaps flag maintains the permitted capability set, allowing the capabilities in the effective set to be activated as needed.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd set_keepcaps true
ceph config get osd set_keepcaps
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd set_keepcaps
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← نمای کلی](../OVERVIEW.md)
