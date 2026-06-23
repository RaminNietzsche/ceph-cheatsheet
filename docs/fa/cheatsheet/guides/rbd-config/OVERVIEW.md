# راهنمای عمیق پیکربندی RBD — همهٔ گزینه‌ها

مرجع کامل **97** گزینهٔ RBD با راهنمای **یافتن مقدار بهینه** (یک بخش برای هر گزینه). تولیدشده از [config/rbd/INDEX.md](../../config/rbd/INDEX.md).

```bash
./scripts/lookup-config.sh <option-name>
python3 scripts/generate-config-guide.py rbd
```

- [مرجع سریع تنظیم](TUNING.md)

## موضوعات بر اساس دسته


### Performance

| موضوع | گزینه‌ها |
|-------|---------|
| [Cache](performance/cache.md) | 8 |
| [Io](performance/io.md) | 2 |
| [QoS & throttling](performance/qos.md) | 20 |
| [Readahead](performance/readahead.md) | 3 |

### Mirroring & journal

| موضوع | گزینه‌ها |
|-------|---------|
| [Journal](mirror/journal.md) | 11 |
| [Mirroring](mirror/mirroring.md) | 4 |

### Defaults & misc

| موضوع | گزینه‌ها |
|-------|---------|
| [Atime](misc/atime.md) | 1 |
| [Auto](misc/auto.md) | 1 |
| [Balance](misc/balance.md) | 2 |
| [Blkin](misc/blkin.md) | 1 |
| [Blocklist](misc/blocklist.md) | 2 |
| [Clone](misc/clone.md) | 1 |
| [Compression](misc/compression.md) | 1 |
| [Concurrent](misc/concurrent.md) | 1 |
| [Config](misc/config.md) | 1 |
| [Defaults](misc/default.md) | 10 |
| [Disable](misc/disable.md) | 1 |
| [Discard](misc/discard.md) | 2 |
| [Enable](misc/enable.md) | 1 |
| [General](misc/general.md) | 3 |
| [Invalidate](misc/invalidate.md) | 1 |
| [Localize](misc/localize.md) | 2 |
| [Move](misc/move.md) | 3 |
| [Mtime](misc/mtime.md) | 1 |
| [Non](misc/non.md) | 1 |
| [Op](misc/op.md) | 2 |
| [Parent](misc/parent.md) | 1 |
| [Persistent](misc/persistent.md) | 3 |
| [Quiesce](misc/quiesce.md) | 1 |
| [Read](misc/read.md) | 1 |
| [Request](misc/request.md) | 1 |
| [Skip](misc/skip.md) | 1 |
| [Sparse](misc/sparse.md) | 1 |
| [Validate](misc/validate.md) | 2 |

[← نمای کلی راهنما](../OVERVIEW.md)
