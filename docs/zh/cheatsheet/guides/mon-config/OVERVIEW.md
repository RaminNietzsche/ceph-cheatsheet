# MON 配置深度指南 — 全部选项

全部 **156** 个 MON 选项的扩展参考，含 **寻找最优值** 指南（每个选项一节）。由 [config/mon/INDEX.md](../../config/mon/INDEX.md) 生成。

```bash
./scripts/lookup-config.sh <option-name>
python3 scripts/generate-config-guide.py mon
```

- [调优快速参考](TUNING.md)

## 按类别浏览


### Quorum & Paxos

| 主题 | 选项数 |
|-------|---------|
| [Quorum & Paxos](quorum/quorum-paxos.md) | 14 |

### PG & pool health

| 主题 | 选项数 |
|-------|---------|
| [PG & pool health](pg-pool/pg-pool.md) | 14 |

### Logging & backup

| 主题 | 选项数 |
|-------|---------|
| [Cluster logging](logging/logging.md) | 20 |
| [Monitor backup](logging/backup.md) | 7 |

### Cross-daemon

| 主题 | 选项数 |
|-------|---------|
| [OSD-related settings](cross-daemon/osd-related.md) | 28 |
| [MGR-related settings](cross-daemon/mgr-related.md) | 6 |
| [MDS-related settings](cross-daemon/mds-related.md) | 1 |

### Auth & runtime

| 主题 | 选项数 |
|-------|---------|
| [Auth & caps](runtime/auth.md) | 1 |
| [Intervals & timeouts](runtime/intervals.md) | 17 |
| [Paths & storage](runtime/paths.md) | 4 |
| [General monitor](runtime/general.md) | 44 |

[← 指南概览](../OVERVIEW.md)
