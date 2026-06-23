> **说明：** 下表中的选项说明来自 upstream Ceph（英文）。

# Quick Start — Daily Admin Workflow

A minimal workflow for operating a Ceph cluster. Adjust for your environment (cephadm vs manual, release version).

## 1. Check cluster health

```bash
ceph -s
ceph health detail
ceph versions
ceph orch ps          # if using cephadm
```

Expected: `health: HEALTH_OK`, all OSDs up, quorum intact.

## 2. Capacity and usage

```bash
ceph df
ceph df detail
ceph osd df tree
```

Watch for `nearfull` / `backfillfull` warnings.

## 3. PG state

```bash
ceph pg stat
ceph pg dump_stuck
```

All PGs should be `active+clean`. Investigate `degraded`, `recovering`, `backfilling`, or `stuck`.

## 4. Common changes

```bash
# Set a runtime config option
ceph config set osd osd_max_scrubs 2

# Create an RBD pool
ceph osd pool create rbd 128 128 replicated
ceph osd pool application enable rbd rbd

# Create an RBD image
rbd create rbd/myimage --size 10G

# Mark OSD out for maintenance
ceph osd out 5
# … wait for backfill …
ceph osd in 5
```

## 5. Before upgrades

```bash
ceph versions                         # mixed versions?
ceph health detail
ceph osd ok-to-stop osd.0 osd.1 …    # check N OSDs at a time
ceph orch upgrade status              # cephadm path
```

## 6. When something breaks

1. `ceph health detail` — read the warning/error text
2. `ceph -w` — watch live events
3. [Troubleshooting commands](../cli/troubleshooting.md)
4. Look up related config: `./scripts/lookup-config.sh <option>`

## Lookup cheat sheet

```bash
./scripts/lookup-config.sh osd_max_scrubs
./scripts/search-all.sh "full ratio"
./scripts/search-config.sh -s rgw cache
```

## Next steps

- Pick your [role](OVERVIEW.md#by-role) or [scale](OVERVIEW.md#by-scale) for focused workflows.

[← Main reference](../index.md)
