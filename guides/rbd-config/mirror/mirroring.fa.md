# Mirroring

deep dive پیکربندی RBD — 4 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rbd_mirroring_delete_delay](#rbd_mirroring_delete_delay) | `0` | Advanced | Performance |
| [rbd_mirroring_max_mirroring_snapshots](#rbd_mirroring_max_mirroring_snapshots) | `5` | Advanced | Performance |
| [rbd_mirroring_replay_delay](#rbd_mirroring_replay_delay) | `0` | Advanced | Performance |
| [rbd_mirroring_resync_after_disconnect](#rbd_mirroring_resync_after_disconnect) | `False` | Advanced | Performance |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **Policy** | امنیت، سازگاری، پیش‌فرض‌های عملیاتی |
| **Capacity** | چیدمان دیسک، مسیرها، اندازه‌گیری |
| **Performance** | خط پایه → تغییر تدریجی → پایش کلاستر |
| **Connectivity** | نزدیک‌ترین endpoint پایدار خارجی |
| **Dev** | پیش‌فرض upstream در production |

**ابزارهای مشترک:**

```bash
ceph config get <daemon> <option>  # e.g. rbd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_mirroring_delete_delay

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirroring_delete_delay](../../../config/rbd/rbd.md#SP_rbd_mirroring_delete_delay) |

**کارکرد:** time-delay in seconds for rbd-mirror delete propagation

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client rbd_mirroring_delete_delay 64
ceph config get client rbd_mirroring_delete_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_mirroring_delete_delay
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirroring_max_mirroring_snapshots

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirroring_max_mirroring_snapshots](../../../config/rbd/rbd.md#SP_rbd_mirroring_max_mirroring_snapshots) |

**کارکرد:** mirroring snapshots limit

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client rbd_mirroring_max_mirroring_snapshots 5
ceph config get client rbd_mirroring_max_mirroring_snapshots
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.

**محدوده:** حداقل `3`، حداکثر `—`.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_mirroring_max_mirroring_snapshots
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirroring_replay_delay

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirroring_replay_delay](../../../config/rbd/rbd.md#SP_rbd_mirroring_replay_delay) |

**کارکرد:** time-delay in seconds for rbd-mirror asynchronous replication

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client rbd_mirroring_replay_delay 64
ceph config get client rbd_mirroring_replay_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_mirroring_replay_delay
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirroring_resync_after_disconnect

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirroring_resync_after_disconnect](../../../config/rbd/rbd.md#SP_rbd_mirroring_resync_after_disconnect) |

**کارکرد:** automatically start image resync after mirroring is disconnected due to being laggy

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client rbd_mirroring_resync_after_disconnect true
ceph config get client rbd_mirroring_resync_after_disconnect
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_mirroring_resync_after_disconnect
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---


[← نمای کلی](../OVERVIEW.md)
