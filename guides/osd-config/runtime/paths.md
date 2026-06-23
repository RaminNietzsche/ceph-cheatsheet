# Paths & data dirs

OSD config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [osd_data](#osd_data) | `/var/lib/ceph/osd/$cluster-$id` | Advanced | Performance |
| [osd_skip_data_digest](#osd_skip_data_digest) | `False` | Dev | Dev |

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

### osd_data

| | |
|---|---|
| Type | Str · default `/var/lib/ceph/osd/$cluster-$id` · **Advanced** |
| Table | [osd.md#SP_osd_data](../../../config/osd/osd.md#SP_osd_data) |

**What it does:** path to OSD data

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_data "/var/lib/ceph/osd/$cluster-$id"
ceph config get osd osd_data
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `/var/lib/ceph/osd/$cluster-$id`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_data
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_skip_data_digest

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_skip_data_digest](../../../config/osd/osd.md#SP_osd_skip_data_digest) |

**What it does:** Do not store full-object checksums if the backend (bluestore) does its own checksums. Only usable with all BlueStore OSDs.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_skip_data_digest true
ceph config get osd osd_skip_data_digest
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
