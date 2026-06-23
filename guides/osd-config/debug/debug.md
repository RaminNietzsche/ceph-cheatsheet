# Debug & injection

OSD config deep dive — 4 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [osd_debug_feed_pullee](#osd_debug_feed_pullee) | `-1` | Dev | Dev |
| [osd_debug_trim_objects](#osd_debug_trim_objects) | `False` | Advanced | Performance |
| [osd_inject_bad_map_crc_probability](#osd_inject_bad_map_crc_probability) | `0` | Dev | Dev |
| [osd_inject_failure_on_pg_removal](#osd_inject_failure_on_pg_removal) | `False` | Dev | Dev |

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

### osd_debug_feed_pullee

| | |
|---|---|
| Type | Int · default `-1` · **Dev** |
| Table | [osd.md#SP_osd_debug_feed_pullee](../../../config/osd/osd.md#SP_osd_debug_feed_pullee) |

**What it does:** Feed a pullee, and force primary to pull a currently missing object from it

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_feed_pullee 128
ceph config get osd osd_debug_feed_pullee
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`-1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_debug_trim_objects

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_debug_trim_objects](../../../config/osd/osd.md#SP_osd_debug_trim_objects) |

**What it does:** Asserts that no clone-objects were added to a snap after we start trimming it

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_debug_trim_objects true
ceph config get osd osd_debug_trim_objects
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_debug_trim_objects
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_inject_bad_map_crc_probability

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [osd.md#SP_osd_inject_bad_map_crc_probability](../../../config/osd/osd.md#SP_osd_inject_bad_map_crc_probability) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_inject_bad_map_crc_probability 0
ceph config get osd osd_inject_bad_map_crc_probability
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_inject_failure_on_pg_removal

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_inject_failure_on_pg_removal](../../../config/osd/osd.md#SP_osd_inject_failure_on_pg_removal) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_inject_failure_on_pg_removal true
ceph config get osd osd_inject_failure_on_pg_removal
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
