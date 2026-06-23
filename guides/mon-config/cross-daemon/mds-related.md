# MDS-related settings

MON config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mds_beacon_mon_down_grace](#mds_beacon_mon_down_grace) | `1_min` | Advanced | Performance |

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, compatibility, operational defaults |
| **Capacity** | Disk layout, paths, sizing |
| **Performance** | Baseline → incremental change → monitor cluster |
| **Connectivity** | Nearest stable external endpoint |
| **Dev** | Keep upstream default in production |

**Shared tooling:**

```bash
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mds_beacon_mon_down_grace

| | |
|---|---|
| Type | Secs · default `1_min` · **Advanced** |
| Table | [mds.md#SP_mds_beacon_mon_down_grace](../../../config/mon/mds.md#SP_mds_beacon_mon_down_grace) |

**What it does:** tolerance in seconds for missed MDS beacons to monitors

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_beacon_mon_down_grace 1_min
ceph config get mds mds_beacon_mon_down_grace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_beacon_mon_down_grace
ceph -s
ceph fs status
ceph mds stat
```

---


[← Overview](../OVERVIEW.md)
