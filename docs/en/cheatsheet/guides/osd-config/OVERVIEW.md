# OSD Config Deep Dive — All Options

Extended reference for all **158** OSD options with **Finding optimal value** guidance (one section per option). Generated from [config/osd/INDEX.md](../../config/osd/INDEX.md).

```bash
./scripts/lookup-config.sh <option-name>
python3 scripts/generate-config-guide.py osd
```

- [Tuning quick reference](TUNING.md)

## Topics by category


### Recovery & backfill

| Topic | Options |
|-------|---------|
| [Recovery & backfill](recovery/recovery.md) | 28 |

### Scrub

| Topic | Options |
|-------|---------|
| [Scrub](scrub/scrub.md) | 39 |

### mClock scheduler

| Topic | Options |
|-------|---------|
| [mClock scheduler](mclock/mclock.md) | 18 |

### Limits & intervals

| Topic | Options |
|-------|---------|
| [Limits & caps](limits-intervals/limits.md) | 15 |
| [Intervals & throttling](limits-intervals/intervals.md) | 12 |

### Runtime & paths

| Topic | Options |
|-------|---------|
| [Paths & data dirs](runtime/paths.md) | 2 |
| [Cache agent](runtime/agent.md) | 7 |
| [Object classes](runtime/classes.md) | 5 |
| [CRUSH & weight](runtime/crush.md) | 2 |
| [General runtime](runtime/general.md) | 26 |

### Debug

| Topic | Options |
|-------|---------|
| [Debug & injection](debug/debug.md) | 4 |

[← Guides overview](../OVERVIEW.md)
