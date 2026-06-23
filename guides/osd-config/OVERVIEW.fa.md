# Deep Dive پیکربندی OSD — همه گزینه‌ها

مرجع گسترده برای **158** گزینه OSD با راهنمای **یافتن مقدار بهینه** (یک بخش برای هر گزینه). تولید شده از [config/osd/INDEX.md](../../config/osd/INDEX.md).

```bash
./scripts/lookup-config.sh <option-name>
python3 scripts/generate-config-guide.py osd
```

- [مرجع سریع تنظیم](TUNING.md)

## موضوعات بر اساس دسته


### Recovery & backfill

| موضوع | گزینه‌ها |
|-------|---------|
| [Recovery & backfill](recovery/recovery.md) | 28 |

### Scrub

| موضوع | گزینه‌ها |
|-------|---------|
| [Scrub](scrub/scrub.md) | 39 |

### mClock scheduler

| موضوع | گزینه‌ها |
|-------|---------|
| [mClock scheduler](mclock/mclock.md) | 18 |

### Limits & intervals

| موضوع | گزینه‌ها |
|-------|---------|
| [Limits & caps](limits-intervals/limits.md) | 15 |
| [Intervals & throttling](limits-intervals/intervals.md) | 12 |

### Runtime & paths

| موضوع | گزینه‌ها |
|-------|---------|
| [Paths & data dirs](runtime/paths.md) | 2 |
| [Cache agent](runtime/agent.md) | 7 |
| [Object classes](runtime/classes.md) | 5 |
| [CRUSH & weight](runtime/crush.md) | 2 |
| [General runtime](runtime/general.md) | 26 |

### Debug

| موضوع | گزینه‌ها |
|-------|---------|
| [Debug & injection](debug/debug.md) | 4 |

[← نمای کلی راهنما](../../guides/OVERVIEW.md)
