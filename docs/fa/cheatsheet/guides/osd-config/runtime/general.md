# General runtime

راهنمای عمیق پیکربندی OSD — 26 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [osd_aggregated_slow_ops_logging](#osd_aggregated_slow_ops_logging) | `True` | Advanced | عملکرد |
| [osd_compact_on_start](#osd_compact_on_start) | `False` | Advanced | عملکرد |
| [osd_ec_partial_reads](#osd_ec_partial_reads) | `True` | Advanced | عملکرد |
| [osd_extblkdev_plugins](#osd_extblkdev_plugins) | `vdo fcm` | Advanced | عملکرد |
| [osd_find_best_info_ignore_history_les](#osd_find_best_info_ignore_history_les) | `False` | Dev | توسعه |
| [osd_journal](#osd_journal) | `/var/lib/ceph/osd/$cluster-$id/journal` | Advanced | عملکرد |
| [osd_journal_flush_on_shutdown](#osd_journal_flush_on_shutdown) | `True` | Advanced | عملکرد |
| [osd_journal_size](#osd_journal_size) | `5_K` | Advanced | عملکرد |
| [osd_map_cache_size](#osd_map_cache_size) | `50` | Advanced | عملکرد |
| [osd_num_cache_shards](#osd_num_cache_shards) | `32` | Advanced | عملکرد |
| [osd_numa_auto_affinity](#osd_numa_auto_affinity) | `True` | Advanced | عملکرد |
| [osd_numa_node](#osd_numa_node) | `-1` | Advanced | عملکرد |
| [osd_numa_prefer_iface](#osd_numa_prefer_iface) | `True` | Advanced | عملکرد |
| [osd_op_num_shards](#osd_op_num_shards) | `0` | Advanced | عملکرد |
| [osd_op_num_shards_hdd](#osd_op_num_shards_hdd) | `1` | Advanced | عملکرد |
| [osd_op_num_shards_ssd](#osd_op_num_shards_ssd) | `8` | Advanced | عملکرد |
| [osd_op_num_threads_per_shard](#osd_op_num_threads_per_shard) | `0` | Advanced | عملکرد |
| [osd_op_num_threads_per_shard_hdd](#osd_op_num_threads_per_shard_hdd) | `5` | Advanced | عملکرد |
| [osd_op_num_threads_per_shard_ssd](#osd_op_num_threads_per_shard_ssd) | `2` | Advanced | عملکرد |
| [osd_op_queue](#osd_op_queue) | `mclock_scheduler` | Advanced | عملکرد |
| [osd_op_queue_cut_off](#osd_op_queue_cut_off) | `high` | Advanced | عملکرد |
| [osd_os_flags](#osd_os_flags) | `0` | Dev | توسعه |
| [osd_push_per_object_cost](#osd_push_per_object_cost) | `1000` | Advanced | عملکرد |
| [osd_read_ec_check_for_errors](#osd_read_ec_check_for_errors) | `False` | Advanced | عملکرد |
| [osd_rocksdb_iterator_bounds_enabled](#osd_rocksdb_iterator_bounds_enabled) | `True` | Dev | توسعه |
| [osd_uuid](#osd_uuid) | `(empty)` | Advanced | عملکرد |

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

### osd_aggregated_slow_ops_logging

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [osd.md#SP_osd_aggregated_slow_ops_logging](../../../config/osd/osd.md#SP_osd_aggregated_slow_ops_logging) |

**کارکرد:** Allow OSD daemon to send an aggregated slow ops to the cluster log

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_aggregated_slow_ops_logging false
ceph config get osd osd_aggregated_slow_ops_logging
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_aggregated_slow_ops_logging
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_compact_on_start

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_compact_on_start](../../../config/osd/osd.md#SP_osd_compact_on_start) |

**کارکرد:** compact OSD's object store's OMAP on start

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_compact_on_start true
ceph config get osd osd_compact_on_start
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_compact_on_start
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_ec_partial_reads

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [osd.md#SP_osd_ec_partial_reads](../../../config/osd/osd.md#SP_osd_ec_partial_reads) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_ec_partial_reads false
ceph config get osd osd_ec_partial_reads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_ec_partial_reads
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_extblkdev_plugins

| | |
|---|---|
| نوع | Str · default `vdo fcm` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [osd.md#SP_osd_extblkdev_plugins](../../../config/osd/osd.md#SP_osd_extblkdev_plugins) |

**کارکرد:** extended block device plugins to load, provide compression feedback at runtime

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_extblkdev_plugins "vdo fcm"
ceph config get osd osd_extblkdev_plugins
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `vdo fcm`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_extblkdev_plugins
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_find_best_info_ignore_history_les

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_find_best_info_ignore_history_les](../../../config/osd/osd.md#SP_osd_find_best_info_ignore_history_les) |

**کارکرد:** ignore last_epoch_started value when peering AND PROBABLY LOSE DATA THIS IS AN EXTREMELY DANGEROUS OPTION THAT SHOULD ONLY BE USED AT THE DIRECTION OF A DEVELOPER. It makes peering ignore the last_epoch_started value when peering, which can allow the OSD to believe an OSD has an authoritative view of a PG's contents even when it is in fact old and stale, typically leading to data loss (by believing a stale PG is up to date).

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_find_best_info_ignore_history_les true
ceph config get osd osd_find_best_info_ignore_history_les
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_journal

| | |
|---|---|
| نوع | Str · default `/var/lib/ceph/osd/$cluster-$id/journal` · **Advanced** |
| جدول | [osd.md#SP_osd_journal](../../../config/osd/osd.md#SP_osd_journal) |

**کارکرد:** path to OSD journal (when FileStore backend is in use)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_journal "/var/lib/ceph/osd/$cluster-$id/journal"
ceph config get osd osd_journal
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `/var/lib/ceph/osd/$cluster-$id/journal`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_journal
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_journal_flush_on_shutdown

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [osd.md#SP_osd_journal_flush_on_shutdown](../../../config/osd/osd.md#SP_osd_journal_flush_on_shutdown) |

**کارکرد:** flush FileStore journal contents during clean OSD shutdown

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_journal_flush_on_shutdown false
ceph config get osd osd_journal_flush_on_shutdown
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_journal_flush_on_shutdown
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_journal_size

| | |
|---|---|
| نوع | Size · default `5_K` · **Advanced** |
| جدول | [osd.md#SP_osd_journal_size](../../../config/osd/osd.md#SP_osd_journal_size) |

**کارکرد:** size of FileStore journal (in MiB)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_journal_size 5_K
ceph config get osd osd_journal_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_journal_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_map_cache_size

| | |
|---|---|
| نوع | Int · default `50` · **Advanced** |
| جدول | [osd.md#SP_osd_map_cache_size](../../../config/osd/osd.md#SP_osd_map_cache_size) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_map_cache_size 50
ceph config get osd osd_map_cache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `50`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_map_cache_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_num_cache_shards

| | |
|---|---|
| نوع | Size · default `32` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [osd.md#SP_osd_num_cache_shards](../../../config/osd/osd.md#SP_osd_num_cache_shards) |

**کارکرد:** The number of cache shards to use in the object store.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_num_cache_shards 32
ceph config get osd osd_num_cache_shards
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `32`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_num_cache_shards
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_numa_auto_affinity

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [osd.md#SP_osd_numa_auto_affinity](../../../config/osd/osd.md#SP_osd_numa_auto_affinity) |

**کارکرد:** automatically set affinity to numa node when storage and network match

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_numa_auto_affinity false
ceph config get osd osd_numa_auto_affinity
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_numa_auto_affinity
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_numa_node

| | |
|---|---|
| نوع | Int · default `-1` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [osd.md#SP_osd_numa_node](../../../config/osd/osd.md#SP_osd_numa_node) |

**کارکرد:** set affinity to a numa node (-1 for none)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`osd_numa_auto_affinity`](../../../config/osd/osd.md#SP_osd_numa_auto_affinity)

**مثال:**

```bash
ceph config set osd osd_numa_node 128
ceph config get osd osd_numa_node
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `-1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_numa_node
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_numa_prefer_iface

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [osd.md#SP_osd_numa_prefer_iface](../../../config/osd/osd.md#SP_osd_numa_prefer_iface) |

**کارکرد:** prefer IP on network interface on same numa node as storage

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**گزینه‌های مرتبط:**

- [`osd_numa_auto_affinity`](../../../config/osd/osd.md#SP_osd_numa_auto_affinity)

**مثال:**

```bash
ceph config set osd osd_numa_prefer_iface false
ceph config get osd osd_numa_prefer_iface
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_numa_prefer_iface
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_num_shards

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [osd.md#SP_osd_op_num_shards](../../../config/osd/osd.md#SP_osd_op_num_shards) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_op_num_shards 64
ceph config get osd osd_op_num_shards
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_op_num_shards
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_num_shards_hdd

| | |
|---|---|
| نوع | Int · default `1` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [osd.md#SP_osd_op_num_shards_hdd](../../../config/osd/osd.md#SP_osd_op_num_shards_hdd) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`osd_op_num_shards`](../../../config/osd/osd.md#SP_osd_op_num_shards)

**مثال:**

```bash
ceph config set osd osd_op_num_shards_hdd 1
ceph config get osd osd_op_num_shards_hdd
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_op_num_shards_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_num_shards_ssd

| | |
|---|---|
| نوع | Int · default `8` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [osd.md#SP_osd_op_num_shards_ssd](../../../config/osd/osd.md#SP_osd_op_num_shards_ssd) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`osd_op_num_shards`](../../../config/osd/osd.md#SP_osd_op_num_shards)

**مثال:**

```bash
ceph config set osd osd_op_num_shards_ssd 8
ceph config get osd osd_op_num_shards_ssd
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `8`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_op_num_shards_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_num_threads_per_shard

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [osd.md#SP_osd_op_num_threads_per_shard](../../../config/osd/osd.md#SP_osd_op_num_threads_per_shard) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_op_num_threads_per_shard 64
ceph config get osd osd_op_num_threads_per_shard
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_op_num_threads_per_shard
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_num_threads_per_shard_hdd

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [osd.md#SP_osd_op_num_threads_per_shard_hdd](../../../config/osd/osd.md#SP_osd_op_num_threads_per_shard_hdd) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`osd_op_num_threads_per_shard`](../../../config/osd/osd.md#SP_osd_op_num_threads_per_shard)

**مثال:**

```bash
ceph config set osd osd_op_num_threads_per_shard_hdd 5
ceph config get osd osd_op_num_threads_per_shard_hdd
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_op_num_threads_per_shard_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_num_threads_per_shard_ssd

| | |
|---|---|
| نوع | Int · default `2` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [osd.md#SP_osd_op_num_threads_per_shard_ssd](../../../config/osd/osd.md#SP_osd_op_num_threads_per_shard_ssd) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`osd_op_num_threads_per_shard`](../../../config/osd/osd.md#SP_osd_op_num_threads_per_shard)

**مثال:**

```bash
ceph config set osd osd_op_num_threads_per_shard_ssd 2
ceph config get osd osd_op_num_threads_per_shard_ssd
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_op_num_threads_per_shard_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_queue

| | |
|---|---|
| نوع | Str · enum: ["wpq", "mclock_scheduler", "debug_random"] · default `mclock_scheduler` · **Advanced** |
| جدول | [osd.md#SP_osd_op_queue](../../../config/osd/osd.md#SP_osd_op_queue) |

**کارکرد:** OSD operation queue scheduler (`mclock_scheduler`, `wpq`, or `debug_random`). Production clusters should use mClock.

**زمان استفاده:** Keep `mclock_scheduler` unless upstream support directs otherwise.

**گزینه‌های مرتبط:**

- [`osd_op_queue_cut_off`](../../../config/osd/osd.md#SP_osd_op_queue_cut_off)

**مثال:**

```bash
ceph config set osd osd_op_queue mclock_scheduler
ceph config get osd osd_op_queue
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `mclock_scheduler`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_op_queue
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_queue_cut_off

| | |
|---|---|
| نوع | Str · enum: ["low", "high", "debug_random"] · default `high` · **Advanced** |
| جدول | [osd.md#SP_osd_op_queue_cut_off](../../../config/osd/osd.md#SP_osd_op_queue_cut_off) |

**کارکرد:** the threshold between high priority ops and low priority ops the threshold between high priority ops that use strict priority ordering and low priority ops that use a fairness algorithm that may or may not incorporate priority

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`osd_op_queue`](../../../config/osd/osd.md#SP_osd_op_queue)

**مثال:**

```bash
ceph config set osd osd_op_queue_cut_off high
ceph config get osd osd_op_queue_cut_off
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `high`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_op_queue_cut_off
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_os_flags

| | |
|---|---|
| نوع | Uint · default `0` · **Dev** |
| جدول | [osd.md#SP_osd_os_flags](../../../config/osd/osd.md#SP_osd_os_flags) |

**کارکرد:** flags to skip filestore omap or journal initialization

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_os_flags 64
ceph config get osd osd_os_flags
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_push_per_object_cost

| | |
|---|---|
| نوع | Size · default `1000` · **Advanced** |
| جدول | [osd.md#SP_osd_push_per_object_cost](../../../config/osd/osd.md#SP_osd_push_per_object_cost) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_push_per_object_cost 1000
ceph config get osd osd_push_per_object_cost
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_push_per_object_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_read_ec_check_for_errors

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_read_ec_check_for_errors](../../../config/osd/osd.md#SP_osd_read_ec_check_for_errors) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_read_ec_check_for_errors true
ceph config get osd osd_read_ec_check_for_errors
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_read_ec_check_for_errors
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_rocksdb_iterator_bounds_enabled

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [osd.md#SP_osd_rocksdb_iterator_bounds_enabled](../../../config/osd/osd.md#SP_osd_rocksdb_iterator_bounds_enabled) |

**کارکرد:** Whether omap iterator bounds are applied to rocksdb iterator ReadOptions

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_rocksdb_iterator_bounds_enabled false
ceph config get osd osd_rocksdb_iterator_bounds_enabled
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_uuid

| | |
|---|---|
| نوع | Uuid · default `(empty)` · **Advanced** |
| جدول | [osd.md#SP_osd_uuid](../../../config/osd/osd.md#SP_osd_uuid) |

**کارکرد:** uuid label for a new OSD

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_uuid (empty)
ceph config get osd osd_uuid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_uuid
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← نمای کلی](../OVERVIEW.md)
