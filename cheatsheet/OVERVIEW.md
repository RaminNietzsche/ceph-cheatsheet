[← Home](../index.md)

# Ceph Reference

Simple, offline-friendly reference for Ceph administrators — organized by **role**, **scale**, **CLI**, and **config**.

**Source:** [ceph/ceph](https://github.com/ceph/ceph) `main` — see [VERSION](../version.md) for generation date.

---

## Start here

| I want to… | Go to |
|------------|-------|
| Find docs for my job | [Guides by role](../guides/OVERVIEW.md#by-role) |
| Size-specific advice | [Guides by scale](../guides/OVERVIEW.md#by-scale) |
| Run cluster commands | [CLI reference](../cli/OVERVIEW.md) |
| Look up a config option | [Config reference](../config/OVERVIEW.md) |
| Daily checklist | [Quick start](../guides/quickstart.md) |
| Search locally | `./scripts/search-all.sh <term>` |
| One config option | `./scripts/lookup-config.sh <option>` |

---

## By role

<table class="guide-table">
<thead>
<tr><th>Role</th><th>Guide</th><th>CLI</th><th>Config</th></tr>
</thead>
<tbody>
<tr class="row-cluster">
  <td><span class="badge badge-role-cluster">Cluster admin</span></td>
  <td><a href="guides/roles/cluster-admin/">guide</a></td>
  <td><a href="cli/cluster/">cluster</a>, <a href="cli/cephadm/">cephadm</a></td>
  <td><a href="config/mon/INDEX/">mon</a>, <a href="config/mgr/INDEX/">mgr</a></td>
</tr>
<tr class="row-storage">
  <td><span class="badge badge-role-storage">Storage operator</span></td>
  <td><a href="guides/roles/storage-operator/">guide</a></td>
  <td><a href="cli/osd-pool/">osd-pool</a></td>
  <td><a href="config/osd/INDEX/">osd</a></td>
</tr>
<tr class="row-rgw">
  <td><span class="badge badge-role-rgw">RGW admin</span></td>
  <td><a href="guides/roles/rgw-admin/">guide</a></td>
  <td><a href="cli/rgw/">rgw</a></td>
  <td><a href="config/rgw/INDEX/">rgw config</a></td>
</tr>
<tr class="row-cephfs">
  <td><span class="badge badge-role-cephfs">CephFS admin</span></td>
  <td><a href="guides/roles/cephfs-admin/">guide</a></td>
  <td><a href="cli/cephfs/">cephfs</a></td>
  <td><a href="config/mds/INDEX/">mds</a></td>
</tr>
</tbody>
</table>

---

## By scale

<table class="guide-table">
<thead>
<tr><th>Scale</th><th>Guide</th></tr>
</thead>
<tbody>
<tr class="row-lab">
  <td><span class="badge badge-scale-lab">Lab / dev</span> (1–3 nodes)</td>
  <td><a href="guides/scales/lab/">lab</a></td>
</tr>
<tr class="row-small">
  <td><span class="badge badge-scale-small">Small production</span> (3–12 nodes)</td>
  <td><a href="guides/scales/small-production/">small production</a></td>
</tr>
<tr class="row-large">
  <td><span class="badge badge-scale-large">Large production</span> (12+ nodes)</td>
  <td><a href="guides/scales/large-production/">large production</a></td>
</tr>
<tr class="row-multi">
  <td><span class="badge badge-scale-multi">Multisite</span></td>
  <td><a href="guides/scales/multisite/">multisite</a></td>
</tr>
</tbody>
</table>

---

## CLI commands

| Section | Description |
|---------|-------------|
| [Overview](../cli/OVERVIEW.md) | Command families and quick examples |
| [Cluster](../cli/cluster.md) | Status, health, auth, CRUSH |
| [Config](../cli/config.md) | `ceph config get/set/dump` |
| [OSD & pools](../cli/osd-pool.md) | OSDs, pools, PGs, erasure coding |
| [RADOS](../cli/rados.md) | Objects, omap, bench |
| [RBD](../cli/rbd.md) | Images, snapshots, map, mirror |
| [RGW](../cli/rgw.md) | Users, buckets, multisite |
| [CephFS](../cli/cephfs.md) | File systems, MDS, mounts |
| [Cephadm](../cli/cephadm.md) | Orchestrator, deploy, upgrade |
| [Troubleshooting](../cli/troubleshooting.md) | Logs, recovery, diagnostics |

---

## Configuration options

**2122 options** across 13 subsystems — generated from upstream YAML.

| Subsystem | Index |
|-----------|-------|
| [global](../config/global/INDEX.md) | Auth, bluestore, debug, network |
| [osd](../config/osd/INDEX.md) | Recovery, scrub, mclock |
| [mon](../config/mon/INDEX.md) | Quorum, paxos |
| [mgr](../config/mgr/INDEX.md) | Modules, cephadm |
| [mds](../config/mds/INDEX.md) | CephFS metadata |
| [rgw](../config/rgw/INDEX.md) | S3 gateway |
| [rbd](../config/rbd/INDEX.md) | Block device client |
| … | [Full list →](../config/OVERVIEW.md) |

---

## Maintaining this reference

Rules: `.cursor/rules/` · Skill: `.cursor/skills/ceph-cheatsheet/` · [Contributing guide](../guides/contributing.md)

---

## Browse online

```bash
pip install -r scripts/requirements.txt
mkdocs serve
```

Open http://blog.ceph-s3.ir/cheatsheet/ (or http://127.0.0.1:8000 locally).

---

## Project layout

```
cli/                    Command reference
config/                 Config tables (auto-generated)
guides/roles/           By operator role
guides/scales/          By cluster size
guides/rgw-config/      Generated — RGW options (441)
guides/osd-config/      Generated — OSD options (158)
guides/mon-config/      Generated — MON options (156)
guides/mgr-config/      Generated — MGR options (52)
guides/mds-config/      Generated — MDS options (194)
guides/global-config/   Generated — Global options (852)
guides/*-config/        Other subsystems — see generate-config-guide.py
docs/                   MkDocs shell (index, CSS; symlinks to content)
scripts/                Search, lookup, regenerate
.cursor/rules/          Documentation conventions
.cursor/skills/         Agent maintenance workflows
```

[README](https://github.com/RaminNietzsche/ceph-cheatsheet) · [License](../license.md)
