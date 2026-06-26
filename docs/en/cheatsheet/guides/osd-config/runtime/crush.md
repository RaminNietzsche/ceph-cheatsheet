# CRUSH & weight

OSD config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [osd_crush_initial_weight](#osd_crush_initial_weight) | `-1` | Advanced | Performance |
| [osd_crush_update_on_start](#osd_crush_update_on_start) | `True` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. osd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_crush_initial_weight

| | |
|---|---|
| Type | Float · default `-1` · **Advanced** |
| Table | [osd.md#SP_osd_crush_initial_weight](../../../config/osd/osd.md#SP_osd_crush_initial_weight) |

**What it does:** if >= 0, initial CRUSH weight for newly created OSDs If this value is negative, the size of the OSD in TiB is used.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_crush_initial_weight -1
ceph config get osd osd_crush_initial_weight
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `-1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_crush_initial_weight
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_crush_update_on_start

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_crush_update_on_start](../../../config/osd/osd.md#SP_osd_crush_update_on_start) |

**What it does:** update OSD CRUSH location on startup

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_crush_update_on_start false
ceph config get osd osd_crush_update_on_start
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_crush_update_on_start
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← Overview](../OVERVIEW.md)
