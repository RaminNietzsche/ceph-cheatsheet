# Debug

deep dive پیکربندی MDS — 9 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mds/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mds_debug_frag](#mds_debug_frag) | `False` | Dev | Dev |
| [mds_debug_scatterstat](#mds_debug_scatterstat) | `False` | Dev | Dev |
| [mds_debug_subtrees](#mds_debug_subtrees) | `False` | Dev | Dev |
| [mds_inject_health_dummy](#mds_inject_health_dummy) | `False` | Dev | Dev |
| [mds_inject_journal_corrupt_dentry_first](#mds_inject_journal_corrupt_dentry_first) | `0.0` | Dev | Dev |
| [mds_inject_migrator_session_race](#mds_inject_migrator_session_race) | `False` | Dev | Dev |
| [mds_inject_rename_corrupt_dentry_first](#mds_inject_rename_corrupt_dentry_first) | `0.0` | Dev | Dev |
| [mds_inject_skip_replaying_inotable](#mds_inject_skip_replaying_inotable) | `False` | Dev | Dev |
| [mds_inject_traceless_reply_probability](#mds_inject_traceless_reply_probability) | `0` | Dev | Dev |

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
ceph config get <daemon> <option>  # e.g. mds
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mds_debug_frag

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_debug_frag](../../../config/mds/mds.md#SP_mds_debug_frag) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mds mds_debug_frag true
ceph config get mds mds_debug_frag
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mds_debug_scatterstat

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_debug_scatterstat](../../../config/mds/mds.md#SP_mds_debug_scatterstat) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mds mds_debug_scatterstat true
ceph config get mds mds_debug_scatterstat
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mds_debug_subtrees

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_debug_subtrees](../../../config/mds/mds.md#SP_mds_debug_subtrees) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mds mds_debug_subtrees true
ceph config get mds mds_debug_subtrees
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mds_inject_health_dummy

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_inject_health_dummy](../../../config/mds/mds.md#SP_mds_inject_health_dummy) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mds mds_inject_health_dummy true
ceph config get mds mds_inject_health_dummy
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mds_inject_journal_corrupt_dentry_first

| | |
|---|---|
| نوع | Float · default `0.0` · **Dev** |
| جدول | [mds.md#SP_mds_inject_journal_corrupt_dentry_first](../../../config/mds/mds.md#SP_mds_inject_journal_corrupt_dentry_first) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mds mds_inject_journal_corrupt_dentry_first 0.0
ceph config get mds mds_inject_journal_corrupt_dentry_first
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0.0`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mds_inject_migrator_session_race

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_inject_migrator_session_race](../../../config/mds/mds.md#SP_mds_inject_migrator_session_race) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mds mds_inject_migrator_session_race true
ceph config get mds mds_inject_migrator_session_race
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mds_inject_rename_corrupt_dentry_first

| | |
|---|---|
| نوع | Float · default `0.0` · **Dev** |
| جدول | [mds.md#SP_mds_inject_rename_corrupt_dentry_first](../../../config/mds/mds.md#SP_mds_inject_rename_corrupt_dentry_first) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mds mds_inject_rename_corrupt_dentry_first 0.0
ceph config get mds mds_inject_rename_corrupt_dentry_first
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0.0`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mds_inject_skip_replaying_inotable

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_inject_skip_replaying_inotable](../../../config/mds/mds.md#SP_mds_inject_skip_replaying_inotable) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mds mds_inject_skip_replaying_inotable true
ceph config get mds mds_inject_skip_replaying_inotable
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mds_inject_traceless_reply_probability

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_inject_traceless_reply_probability](../../../config/mds/mds.md#SP_mds_inject_traceless_reply_probability) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mds mds_inject_traceless_reply_probability 0
ceph config get mds mds_inject_traceless_reply_probability
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
