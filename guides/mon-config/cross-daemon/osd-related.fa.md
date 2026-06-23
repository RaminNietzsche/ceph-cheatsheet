# OSD-related settings

راهنمای عمیق پیکربندی MON — 28 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mon_osd_adjust_down_out_interval](#mon_osd_adjust_down_out_interval) | `True` | Advanced | Performance |
| [mon_osd_adjust_heartbeat_grace](#mon_osd_adjust_heartbeat_grace) | `True` | Advanced | Performance |
| [mon_osd_auto_mark_auto_out_in](#mon_osd_auto_mark_auto_out_in) | `True` | Advanced | Performance |
| [mon_osd_auto_mark_in](#mon_osd_auto_mark_in) | `False` | Advanced | Performance |
| [mon_osd_auto_mark_new_in](#mon_osd_auto_mark_new_in) | `True` | Advanced | Performance |
| [mon_osd_blocklist_default_expire](#mon_osd_blocklist_default_expire) | `1_hr` | Advanced | Performance |
| [mon_osd_cache_size](#mon_osd_cache_size) | `500` | Advanced | Performance |
| [mon_osd_cache_size_min](#mon_osd_cache_size_min) | `128_M` | Advanced | Performance |
| [mon_osd_crush_smoke_test](#mon_osd_crush_smoke_test) | `True` | Advanced | Performance |
| [mon_osd_destroyed_out_interval](#mon_osd_destroyed_out_interval) | `10_min` | Advanced | Performance |
| [mon_osd_down_out_interval](#mon_osd_down_out_interval) | `10_min` | Advanced | Performance |
| [mon_osd_down_out_subtree_limit](#mon_osd_down_out_subtree_limit) | `rack` | Advanced | Performance |
| [mon_osd_laggy_halflife](#mon_osd_laggy_halflife) | `1_hr` | Advanced | Performance |
| [mon_osd_laggy_max_interval](#mon_osd_laggy_max_interval) | `5_min` | Advanced | Performance |
| [mon_osd_laggy_weight](#mon_osd_laggy_weight) | `0.3` | Advanced | Performance |
| [mon_osd_mapping_pgs_per_chunk](#mon_osd_mapping_pgs_per_chunk) | `4096` | Dev | Dev |
| [mon_osd_max_initial_pgs](#mon_osd_max_initial_pgs) | `1024` | Advanced | Performance |
| [mon_osd_min_in_ratio](#mon_osd_min_in_ratio) | `0.75` | Advanced | Performance |
| [mon_osd_min_up_ratio](#mon_osd_min_up_ratio) | `0.3` | Advanced | Performance |
| [mon_osd_warn_num_repaired](#mon_osd_warn_num_repaired) | `10` | Advanced | Performance |
| [mon_osd_warn_op_age](#mon_osd_warn_op_age) | `32` | Advanced | Performance |
| [mon_osdmap_full_prune_enabled](#mon_osdmap_full_prune_enabled) | `True` | Advanced | Policy |
| [mon_osdmap_full_prune_interval](#mon_osdmap_full_prune_interval) | `10` | Advanced | Performance |
| [mon_osdmap_full_prune_min](#mon_osdmap_full_prune_min) | `10000` | Advanced | Performance |
| [mon_osdmap_full_prune_txsize](#mon_osdmap_full_prune_txsize) | `100` | Advanced | Performance |
| [mon_warn_on_filestore_osds](#mon_warn_on_filestore_osds) | `True` | Dev | Dev |
| [mon_warn_on_osd_down_out_interval_zero](#mon_warn_on_osd_down_out_interval_zero) | `True` | Advanced | Performance |
| [osd_crush_update_weight_set](#osd_crush_update_weight_set) | `True` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_osd_adjust_down_out_interval

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_adjust_down_out_interval](../../../config/mon/mon.md#SP_mon_osd_adjust_down_out_interval) |

**کارکرد:** increase the mon_osd_down_out_interval if an OSD appears to be laggy

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_osd_adjust_down_out_interval false
ceph config get mon mon_osd_adjust_down_out_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_adjust_down_out_interval
ceph -s
ceph mon stat
```

---

### mon_osd_adjust_heartbeat_grace

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_adjust_heartbeat_grace](../../../config/mon/mon.md#SP_mon_osd_adjust_heartbeat_grace) |

**کارکرد:** increase OSD heartbeat grace if peers appear to be laggy

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_osd_adjust_heartbeat_grace false
ceph config get mon mon_osd_adjust_heartbeat_grace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_adjust_heartbeat_grace
ceph -s
ceph mon stat
```

---

### mon_osd_auto_mark_auto_out_in

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_auto_mark_auto_out_in](../../../config/mon/mon.md#SP_mon_osd_auto_mark_auto_out_in) |

**کارکرد:** mark any OSD that comes up that was automatically marked 'out' back 'in'

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_osd_auto_mark_auto_out_in false
ceph config get mon mon_osd_auto_mark_auto_out_in
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_auto_mark_auto_out_in
ceph -s
ceph mon stat
```

---

### mon_osd_auto_mark_in

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_auto_mark_in](../../../config/mon/mon.md#SP_mon_osd_auto_mark_in) |

**کارکرد:** mark any OSD that comes up 'in'

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set mon mon_osd_auto_mark_in true
ceph config get mon mon_osd_auto_mark_in
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_auto_mark_in
ceph -s
ceph mon stat
```

---

### mon_osd_auto_mark_new_in

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_auto_mark_new_in](../../../config/mon/mon.md#SP_mon_osd_auto_mark_new_in) |

**کارکرد:** mark any new OSD that comes up 'in'

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_osd_auto_mark_new_in false
ceph config get mon mon_osd_auto_mark_new_in
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_auto_mark_new_in
ceph -s
ceph mon stat
```

---

### mon_osd_blocklist_default_expire

| | |
|---|---|
| نوع | Float · default `1_hr` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_blocklist_default_expire](../../../config/mon/mon.md#SP_mon_osd_blocklist_default_expire) |

**کارکرد:** Duration in seconds that blocklist entries for clients remain in the OSD map

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_osd_blocklist_default_expire 1_hr
ceph config get mon mon_osd_blocklist_default_expire
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1_hr`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_blocklist_default_expire
ceph -s
ceph mon stat
```

---

### mon_osd_cache_size

| | |
|---|---|
| نوع | Int · default `500` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_cache_size](../../../config/mon/mon.md#SP_mon_osd_cache_size) |

**کارکرد:** maximum number of OSDMaps to cache in memory

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_osd_cache_size 500
ceph config get mon mon_osd_cache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `500`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_cache_size
ceph -s
ceph mon stat
```

---

### mon_osd_cache_size_min

| | |
|---|---|
| نوع | Size · default `128_M` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_cache_size_min](../../../config/mon/mon.md#SP_mon_osd_cache_size_min) |

**کارکرد:** The minimum amount of bytes to be kept mapped in memory for osd monitor caches.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_osd_cache_size_min 128_M
ceph config get mon mon_osd_cache_size_min
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `128_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_cache_size_min
ceph -s
ceph mon stat
```

---

### mon_osd_crush_smoke_test

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_crush_smoke_test](../../../config/mon/mon.md#SP_mon_osd_crush_smoke_test) |

**کارکرد:** perform a smoke test on any new CRUSH map before accepting changes

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_osd_crush_smoke_test false
ceph config get mon mon_osd_crush_smoke_test
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_crush_smoke_test
ceph -s
ceph mon stat
```

---

### mon_osd_destroyed_out_interval

| | |
|---|---|
| نوع | Int · default `10_min` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_destroyed_out_interval](../../../config/mon/mon.md#SP_mon_osd_destroyed_out_interval) |

**کارکرد:** mark any OSD 'out' that has been 'destroy'ed for this long (seconds)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_osd_destroyed_out_interval 10_min
ceph config get mon mon_osd_destroyed_out_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_destroyed_out_interval
ceph -s
ceph mon stat
```

---

### mon_osd_down_out_interval

| | |
|---|---|
| نوع | Int · default `10_min` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_down_out_interval](../../../config/mon/mon.md#SP_mon_osd_down_out_interval) |

**کارکرد:** Seconds an OSD can stay `down` before the monitor marks it `out` and CRUSH begins rebalancing.

**زمان استفاده:** Increase for flaky networks or long maintenance (avoid premature rebalance). Decrease when you want faster failover — at the cost of more data movement.

**مثال:**

```bash
ceph config set mon mon_osd_down_out_interval 10_min
ceph config get mon mon_osd_down_out_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_down_out_interval
ceph -s
ceph mon stat
```

Common production range: 600–3600 s. Coordinate with `mon_osd_min_down_reporters`.

---

### mon_osd_down_out_subtree_limit

| | |
|---|---|
| نوع | Str · default `rack` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_down_out_subtree_limit](../../../config/mon/mon.md#SP_mon_osd_down_out_subtree_limit) |

**کارکرد:** do not automatically mark OSDs 'out' if an entire subtree of this size is down

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_osd_down_out_subtree_limit rack
ceph config get mon mon_osd_down_out_subtree_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `rack`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_down_out_subtree_limit
ceph -s
ceph mon stat
```

---

### mon_osd_laggy_halflife

| | |
|---|---|
| نوع | Int · default `1_hr` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_laggy_halflife](../../../config/mon/mon.md#SP_mon_osd_laggy_halflife) |

**کارکرد:** halflife of OSD 'lagginess' factor

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_osd_laggy_halflife 1_hr
ceph config get mon mon_osd_laggy_halflife
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1_hr`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_laggy_halflife
ceph -s
ceph mon stat
```

---

### mon_osd_laggy_max_interval

| | |
|---|---|
| نوع | Int · default `5_min` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_laggy_max_interval](../../../config/mon/mon.md#SP_mon_osd_laggy_max_interval) |

**کارکرد:** cap value for period for OSD to be marked for laggy_interval calculation

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_osd_laggy_max_interval 5_min
ceph config get mon mon_osd_laggy_max_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_laggy_max_interval
ceph -s
ceph mon stat
```

---

### mon_osd_laggy_weight

| | |
|---|---|
| نوع | Float · default `0.3` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_laggy_weight](../../../config/mon/mon.md#SP_mon_osd_laggy_weight) |

**کارکرد:** how heavily to weight OSD marking itself back up in overall laggy_probability

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_osd_laggy_weight 0.3
ceph config get mon mon_osd_laggy_weight
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `1`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_laggy_weight
ceph -s
ceph mon stat
```

---

### mon_osd_mapping_pgs_per_chunk

| | |
|---|---|
| نوع | Int · default `4096` · **Dev** |
| جدول | [mon.md#SP_mon_osd_mapping_pgs_per_chunk](../../../config/mon/mon.md#SP_mon_osd_mapping_pgs_per_chunk) |

**کارکرد:** granularity of PG placement calculation background work

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mon mon_osd_mapping_pgs_per_chunk 4096
ceph config get mon mon_osd_mapping_pgs_per_chunk
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`4096`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mon_osd_max_initial_pgs

| | |
|---|---|
| نوع | Int · default `1024` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_max_initial_pgs](../../../config/mon/mon.md#SP_mon_osd_max_initial_pgs) |

**کارکرد:** maximum number of PGs a pool will created with

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_osd_max_initial_pgs 1024
ceph config get mon mon_osd_max_initial_pgs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1024`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_max_initial_pgs
ceph -s
ceph mon stat
```

---

### mon_osd_min_in_ratio

| | |
|---|---|
| نوع | Float · default `0.75` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_min_in_ratio](../../../config/mon/mon.md#SP_mon_osd_min_in_ratio) |

**کارکرد:** do not automatically mark OSDs 'out' if fewer than this many OSDs are 'in'

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_osd_min_in_ratio 0.75
ceph config get mon mon_osd_min_in_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.75`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_min_in_ratio
ceph -s
ceph mon stat
```

---

### mon_osd_min_up_ratio

| | |
|---|---|
| نوع | Float · default `0.3` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_min_up_ratio](../../../config/mon/mon.md#SP_mon_osd_min_up_ratio) |

**کارکرد:** do not automatically mark OSDs 'out' if fewer than this many OSDs are 'up'

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_osd_min_up_ratio 0.3
ceph config get mon mon_osd_min_up_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_min_up_ratio
ceph -s
ceph mon stat
```

---

### mon_osd_warn_num_repaired

| | |
|---|---|
| نوع | Uint · default `10` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_warn_num_repaired](../../../config/mon/mon.md#SP_mon_osd_warn_num_repaired) |

**کارکرد:** issue OSD_TOO_MANY_REPAIRS health warning if an OSD has more than this many read repairs

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_osd_warn_num_repaired 10
ceph config get mon mon_osd_warn_num_repaired
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_warn_num_repaired
ceph -s
ceph mon stat
```

---

### mon_osd_warn_op_age

| | |
|---|---|
| نوع | Float · default `32` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_warn_op_age](../../../config/mon/mon.md#SP_mon_osd_warn_op_age) |

**کارکرد:** issue REQUEST_SLOW health warning if OSD ops are slower than this age (seconds)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_osd_warn_op_age 32
ceph config get mon mon_osd_warn_op_age
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `32`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_warn_op_age
ceph -s
ceph mon stat
```

---

### mon_osdmap_full_prune_enabled

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_osdmap_full_prune_enabled](../../../config/mon/mon.md#SP_mon_osdmap_full_prune_enabled) |

**کارکرد:** enables pruning full osdmap versions when we go over a given number of maps

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_osdmap_full_prune_enabled false
ceph config get mon mon_osdmap_full_prune_enabled
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osdmap_full_prune_enabled
ceph -s
ceph mon stat
```

---

### mon_osdmap_full_prune_interval

| | |
|---|---|
| نوع | Uint · default `10` · **Advanced** |
| جدول | [mon.md#SP_mon_osdmap_full_prune_interval](../../../config/mon/mon.md#SP_mon_osdmap_full_prune_interval) |

**کارکرد:** interval between maps that will not be pruned; maps in the middle will be pruned.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_osdmap_full_prune_interval 10
ceph config get mon mon_osdmap_full_prune_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osdmap_full_prune_interval
ceph -s
ceph mon stat
```

---

### mon_osdmap_full_prune_min

| | |
|---|---|
| نوع | Uint · default `10000` · **Advanced** |
| جدول | [mon.md#SP_mon_osdmap_full_prune_min](../../../config/mon/mon.md#SP_mon_osdmap_full_prune_min) |

**کارکرد:** minimum number of versions in the store to trigger full map pruning

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_osdmap_full_prune_min 10000
ceph config get mon mon_osdmap_full_prune_min
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osdmap_full_prune_min
ceph -s
ceph mon stat
```

---

### mon_osdmap_full_prune_txsize

| | |
|---|---|
| نوع | Uint · default `100` · **Advanced** |
| جدول | [mon.md#SP_mon_osdmap_full_prune_txsize](../../../config/mon/mon.md#SP_mon_osdmap_full_prune_txsize) |

**کارکرد:** number of maps we will prune per iteration

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_osdmap_full_prune_txsize 100
ceph config get mon mon_osdmap_full_prune_txsize
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `100`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osdmap_full_prune_txsize
ceph -s
ceph mon stat
```

---

### mon_warn_on_filestore_osds

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [mon.md#SP_mon_warn_on_filestore_osds](../../../config/mon/mon.md#SP_mon_warn_on_filestore_osds) |

**کارکرد:** log health warn for filestore OSDs

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mon mon_warn_on_filestore_osds false
ceph config get mon mon_warn_on_filestore_osds
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mon_warn_on_osd_down_out_interval_zero

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_warn_on_osd_down_out_interval_zero](../../../config/mon/mon.md#SP_mon_warn_on_osd_down_out_interval_zero) |

**کارکرد:** issue OSD_NO_DOWN_OUT_INTERVAL health warning if mon_osd_down_out_interval is zero

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_warn_on_osd_down_out_interval_zero false
ceph config get mon mon_warn_on_osd_down_out_interval_zero
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_warn_on_osd_down_out_interval_zero
ceph -s
ceph mon stat
```

---

### osd_crush_update_weight_set

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [osd.md#SP_osd_crush_update_weight_set](../../../config/mon/osd.md#SP_osd_crush_update_weight_set) |

**کارکرد:** update CRUSH weight-set weights when updating weights

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_crush_update_weight_set false
ceph config get osd osd_crush_update_weight_set
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_crush_update_weight_set
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← نمای کلی](../OVERVIEW.md)
