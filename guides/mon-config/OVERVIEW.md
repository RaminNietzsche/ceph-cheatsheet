# MON Config Deep Dive — All Options

Extended reference for all **156** MON options with **Finding optimal value** guidance (one section per option). Generated from [config/mon/INDEX.md](../../config/mon/INDEX.md).

```bash
./scripts/lookup-config.sh <option-name>
python3 scripts/generate-config-guide.py mon
```

- [Tuning quick reference](TUNING.md)

## Topics by category


### Quorum & Paxos

| Topic | Options |
|-------|---------|
| [Quorum & Paxos](quorum/quorum-paxos.md) | 14 |

### PG & pool health

| Topic | Options |
|-------|---------|
| [PG & pool health](pg-pool/pg-pool.md) | 14 |

### Logging & backup

| Topic | Options |
|-------|---------|
| [Cluster logging](logging/logging.md) | 20 |
| [Monitor backup](logging/backup.md) | 7 |

### Cross-daemon

| Topic | Options |
|-------|---------|
| [OSD-related settings](cross-daemon/osd-related.md) | 28 |
| [MGR-related settings](cross-daemon/mgr-related.md) | 6 |
| [MDS-related settings](cross-daemon/mds-related.md) | 1 |

### Auth & runtime

| Topic | Options |
|-------|---------|
| [Auth & caps](runtime/auth.md) | 1 |
| [Intervals & timeouts](runtime/intervals.md) | 17 |
| [Paths & storage](runtime/paths.md) | 4 |
| [General monitor](runtime/general.md) | 44 |

[← Guides overview](../OVERVIEW.md)
