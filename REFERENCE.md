# Ceph Reference

Simple, offline-friendly reference for Ceph administrators.

**Source:** [ceph/ceph](https://github.com/ceph/ceph) `main` — see [`VERSION`](VERSION) for generation date.

---

## Start here

| I want to… | Go to |
|------------|-------|
| Run cluster commands | [CLI reference](cli/OVERVIEW.md) |
| Look up a config option | [Config reference](config/OVERVIEW.md) |
| Do common daily tasks | [Quick start guide](guides/quickstart.md) |
| Search everything locally | `./scripts/search-all.sh <term>` |
| Look up one config option | `./scripts/lookup-config.sh <option>` |

---

## CLI commands

| Section | Description |
|---------|-------------|
| [Overview](cli/OVERVIEW.md) | Command families and quick examples |
| [Cluster](cli/cluster.md) | Status, health, auth, CRUSH |
| [Config](cli/config.md) | `ceph config get/set/dump` |
| [OSD & pools](cli/osd-pool.md) | OSDs, pools, PGs, erasure coding |
| [RADOS](cli/rados.md) | Objects, omap, bench |
| [RBD](cli/rbd.md) | Images, snapshots, map, mirror |
| [RGW](cli/rgw.md) | Users, buckets, multisite |
| [CephFS](cli/cephfs.md) | File systems, MDS, mounts |
| [Cephadm](cli/cephadm.md) | Orchestrator, deploy, upgrade |
| [Troubleshooting](cli/troubleshooting.md) | Logs, recovery, diagnostics |

---

## Configuration options

**2122 options** across 13 subsystems — generated from upstream YAML.

| Subsystem | Index |
|-----------|-------|
| [global](config/global/INDEX.md) | Auth, bluestore, debug, network |
| [osd](config/osd/INDEX.md) | Recovery, scrub, mclock |
| [mon](config/mon/INDEX.md) | Quorum, paxos |
| [mgr](config/mgr/INDEX.md) | Modules, cephadm |
| [mds](config/mds/INDEX.md) | CephFS metadata |
| [rgw](config/rgw/INDEX.md) | S3 gateway |
| [rbd](config/rbd/INDEX.md) | Block device client |
| … | [Full list →](config/OVERVIEW.md) |

Each option includes type, default, valid values, flags (`RUNTIME`, `STARTUP`), and cross-links.

---

## Guides

- [Quick start](guides/quickstart.md) — daily admin workflow
- [Using the config reference](guides/config-lookup.md) — how to read option tables

---

## Browse online

Build the static site locally:

```bash
pip install -r scripts/requirements.txt
mkdocs serve
```

Open http://127.0.0.1:8000

---

## Project layout

```
cli/          Command reference
config/       Config option tables (auto-generated)
guides/       How-to guides
scripts/      Search, lookup, regenerate tools
```

[README](README.md) · [License](LICENSE)
