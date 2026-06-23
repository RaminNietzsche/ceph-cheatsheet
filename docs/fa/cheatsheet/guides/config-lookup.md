# استفاده از مرجع Config

بخش config به‌صورت خودکار از YAML upstream Ceph تولید می‌شود. هر گزینه یک سطر در جدول Markdown است.

## یافتن یک گزینه

**با نام:**

```bash
./scripts/lookup-config.sh rgw_cache_enabled
```

**با کلیدواژه:**

```bash
./scripts/search-config.sh scrub
./scripts/search-config.sh -s osd mclock
```

**مرور:**

1. [config/OVERVIEW.md](../config/OVERVIEW.md) را باز کنید
2. زیرسیستم را انتخاب کنید (مثلاً `rgw`)
3. `INDEX.md` برای فهرست لینک‌دار، یا `rgw.md` برای جدول کامل

## خواندن سطر جدول

مثال: `osd_max_scrubs`

| ستون | معنی |
|--------|---------|
| **Name** | کلیدی که با `ceph config set osd osd_max_scrubs 2` استفاده می‌شود |
| **Desc** | توضیح کوتاه |
| **Level** | `Basic` (معمولاً تنظیم می‌شود) · `Advanced` · `Dev` |
| **Type** | `Int`، `Bool`، `Size`، `Str`، … |
| **non-Daemon / Daemon Default** | مقدار پیش‌فرض (ممکن است برای دیمن‌ها متفاوت باشد) |
| **Min / Max** | محدودهٔ عددی مجاز |
| **Valid Values** | مقادیر enum مجاز به‌صورت آرایهٔ JSON |
| **Flags** | `RUNTIME` = `ceph config set` زنده؛ `STARTUP` = نیاز به restart |
| **Services** | کدام اجزا این گزینه را مصرف می‌کنند |
| **See also** | گزینه‌های مرتبط (لینک‌دار) |
| **Long Desc** | توضیح مفصل |

## اعمال تغییرات

```bash
# Check current effective value
ceph config get osd.0 osd_max_scrubs

# Set for all OSDs (persistent)
ceph config set osd osd_max_scrubs 2

# Set for one daemon
ceph config set osd.0 osd_max_scrubs 1

# Remove override
ceph config rm osd osd_max_scrubs
```

فقط گزینه‌های دارای پرچم `RUNTIME` با `ceph config set` زنده پذیرفته می‌شوند. بقیه restart یا `ceph.conf` می‌خواهند.

## بازتولید از upstream

با release جدید Ceph:

```bash
python3 scripts/generate-config.py --ref reef    # or squid, main, …
```

ref فعلی در [VERSION](../../version.md).

[← Cheatsheet](../index.md)
