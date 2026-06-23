# OSD 配置深度指南 — 全部选项

全部 **158** 个 OSD 选项的扩展参考，含 **寻找最优值** 指南（每个选项一节）。由 [config/osd/INDEX.md](../../config/osd/INDEX.md) 生成。

```bash
./scripts/lookup-config.sh <option-name>
python3 scripts/generate-config-guide.py osd
```

- [调优快速参考](TUNING.md)

## 按类别浏览


### Recovery & backfill

| 主题 | 选项数 |
|-------|---------|
| [Recovery & backfill](recovery/recovery.md) | 28 |

### Scrub

| 主题 | 选项数 |
|-------|---------|
| [Scrub](scrub/scrub.md) | 39 |

### mClock scheduler

| 主题 | 选项数 |
|-------|---------|
| [mClock scheduler](mclock/mclock.md) | 18 |

### Limits & intervals

| 主题 | 选项数 |
|-------|---------|
| [Limits & caps](limits-intervals/limits.md) | 15 |
| [Intervals & throttling](limits-intervals/intervals.md) | 12 |

### Runtime & paths

| 主题 | 选项数 |
|-------|---------|
| [Paths & data dirs](runtime/paths.md) | 2 |
| [Cache agent](runtime/agent.md) | 7 |
| [Object classes](runtime/classes.md) | 5 |
| [CRUSH & weight](runtime/crush.md) | 2 |
| [General runtime](runtime/general.md) | 26 |

### Debug

| 主题 | 选项数 |
|-------|---------|
| [Debug & injection](debug/debug.md) | 4 |

[← 指南概览](../../guides/OVERVIEW.md)
