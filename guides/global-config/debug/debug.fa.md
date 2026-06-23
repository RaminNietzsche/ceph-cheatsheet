# Debug

راهنمای عمیق پیکربندی Global — 5 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [debug_asok_assert_abort](#debug_asok_assert_abort) | `False` | Dev | Dev |
| [debug_asserts_on_shutdown](#debug_asserts_on_shutdown) | `False` | Dev | Dev |
| [debug_deliberately_leak_memory](#debug_deliberately_leak_memory) | `False` | Dev | Dev |
| [debug_disable_randomized_ping](#debug_disable_randomized_ping) | `False` | Dev | Dev |
| [debug_heartbeat_testing_span](#debug_heartbeat_testing_span) | `0` | Dev | Dev |

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
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### debug_asok_assert_abort

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [debug.md#SP_debug_asok_assert_abort](../../../config/global/debug.md#SP_debug_asok_assert_abort) |

**کارکرد:** Enable the admin socket commands 'assert' and 'abort' testing crash dumps etc.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global debug_asok_assert_abort true
ceph config get global debug_asok_assert_abort
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### debug_asserts_on_shutdown

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [debug.md#SP_debug_asserts_on_shutdown](../../../config/global/debug.md#SP_debug_asserts_on_shutdown) |

**کارکرد:** Enable certain assertions to check for refcounting bugs on shutdown; see http://tracker.ceph.com/issues/21738

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global debug_asserts_on_shutdown true
ceph config get global debug_asserts_on_shutdown
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### debug_deliberately_leak_memory

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [debug.md#SP_debug_deliberately_leak_memory](../../../config/global/debug.md#SP_debug_deliberately_leak_memory) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global debug_deliberately_leak_memory true
ceph config get global debug_deliberately_leak_memory
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### debug_disable_randomized_ping

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [debug.md#SP_debug_disable_randomized_ping](../../../config/global/debug.md#SP_debug_disable_randomized_ping) |

**کارکرد:** Disable heartbeat ping randomization for testing purposes

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global debug_disable_randomized_ping true
ceph config get global debug_disable_randomized_ping
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### debug_heartbeat_testing_span

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [debug.md#SP_debug_heartbeat_testing_span](../../../config/global/debug.md#SP_debug_heartbeat_testing_span) |

**کارکرد:** Override 60 second periods for testing only

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global debug_heartbeat_testing_span 64
ceph config get global debug_heartbeat_testing_span
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
