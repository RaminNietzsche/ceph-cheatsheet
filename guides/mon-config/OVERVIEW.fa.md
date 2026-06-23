# Deep Dive پیکربندی MON — همه گزینه‌ها

مرجع گسترده برای **156** گزینه MON با راهنمای **یافتن مقدار بهینه** (یک بخش برای هر گزینه). تولید شده از [config/mon/INDEX.md](../../config/mon/INDEX.md).

```bash
./scripts/lookup-config.sh <option-name>
python3 scripts/generate-config-guide.py mon
```

- [مرجع سریع تنظیم](TUNING.md)

## موضوعات بر اساس دسته


### Quorum & Paxos

| موضوع | گزینه‌ها |
|-------|---------|
| [Quorum & Paxos](quorum/quorum-paxos.md) | 14 |

### PG & pool health

| موضوع | گزینه‌ها |
|-------|---------|
| [PG & pool health](pg-pool/pg-pool.md) | 14 |

### Logging & backup

| موضوع | گزینه‌ها |
|-------|---------|
| [Cluster logging](logging/logging.md) | 20 |
| [Monitor backup](logging/backup.md) | 7 |

### Cross-daemon

| موضوع | گزینه‌ها |
|-------|---------|
| [OSD-related settings](cross-daemon/osd-related.md) | 28 |
| [MGR-related settings](cross-daemon/mgr-related.md) | 6 |
| [MDS-related settings](cross-daemon/mds-related.md) | 1 |

### Auth & runtime

| موضوع | گزینه‌ها |
|-------|---------|
| [Auth & caps](runtime/auth.md) | 1 |
| [Intervals & timeouts](runtime/intervals.md) | 17 |
| [Paths & storage](runtime/paths.md) | 4 |
| [General monitor](runtime/general.md) | 44 |

[← نمای کلی راهنما](../../guides/OVERVIEW.md)
