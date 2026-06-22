# Ceph Reference

Simple, offline-friendly reference for Ceph administrators — organized by **role**, **scale**, **CLI**, and **config**.

**Source:** [ceph/ceph](https://github.com/ceph/ceph) `main` — see [`VERSION`](VERSION) for generation date.

---

## Start here

| I want to… | Go to |
|------------|-------|
| Find docs for my job | [Guides by role](guides/OVERVIEW.md#by-role) |
| Size-specific advice | [Guides by scale](guides/OVERVIEW.md#by-scale) |
| Run cluster commands | [CLI reference](cli/OVERVIEW.md) |
| Look up a config option | [Config reference](config/OVERVIEW.md) |
| Daily checklist | [Quick start](guides/quickstart.md) |
| Search locally | `./scripts/search-all.sh <term>` |
| One config option | `./scripts/lookup-config.sh <option>` |

---

## By role

| Role | Guide | CLI | Config |
|------|-------|-----|--------|
| Cluster admin | [guide](guides/roles/cluster-admin.md) | [cluster](cli/cluster.md), [cephadm](cli/cephadm.md) | [mon](config/mon/INDEX.md), [mgr](config/mgr/INDEX.md) |
| Storage operator | [guide](guides/roles/storage-operator.md) | [osd-pool](cli/osd-pool.md) | [osd](config/osd/INDEX.md) |
| RGW admin | [guide](guides/roles/rgw-admin.md) | [rgw](cli/rgw.md) | [rgw config](config/rgw/INDEX.md) |
| CephFS admin | [guide](guides/roles/cephfs-admin.md) | [cephfs](cli/cephfs.md) | [mds](config/mds/INDEX.md) |

---

## By scale

| Scale | Guide |
|-------|-------|
| Lab / dev (1–3 nodes) | [lab](guides/scales/lab.md) |
| Small production (3–12 nodes) | [small production](guides/scales/small-production.md) |
| Large production (12+ nodes) | [large production](guides/scales/large-production.md) |
| Multisite | [multisite](guides/scales/multisite.md) |

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

---

## Maintaining this reference

Rules: `.cursor/rules/` · Skill: `.cursor/skills/ceph-cheatsheet/` · [Contributing guide](guides/contributing.md)

---

## Browse online

```bash
pip install -r scripts/requirements.txt
mkdocs serve
```

Open https://blog.raminnietzsche.ir/ceph-cheatsheet/ (or http://127.0.0.1:8000 locally).

---

## Project layout

```
cli/              Command reference
config/           Config tables (auto-generated)
guides/roles/     By operator role
guides/scales/    By cluster size
.cursor/rules/    Documentation conventions
.cursor/skills/   Agent maintenance workflows
scripts/          Search, lookup, regenerate
```

[README](https://github.com/RaminNietzsche/ceph-cheatsheet) · [License](LICENSE)
