# Guides

Task-oriented documentation organized by **who you are** (role) and **how big the cluster is** (scale).

## By role

<table class="guide-table">
<thead>
<tr><th>Role</th><th>You manage…</th><th>Start here</th></tr>
</thead>
<tbody>
<tr class="row-cluster">
  <td><span class="badge badge-role-cluster">Cluster admin</span> <a href="roles/cluster-admin/">→</a></td>
  <td>Mon, MGR, cephadm, upgrades, auth</td>
  <td>Daily health, orchestrator</td>
</tr>
<tr class="row-storage">
  <td><span class="badge badge-role-storage">Storage operator</span> <a href="roles/storage-operator/">→</a></td>
  <td>OSDs, pools, PGs, CRUSH, capacity</td>
  <td>OSD/pool ops, recovery</td>
</tr>
<tr class="row-rgw">
  <td><span class="badge badge-role-rgw">RGW admin</span> <a href="roles/rgw-admin/">→</a></td>
  <td>S3 gateway, users, multisite</td>
  <td>radosgw-admin, RGW config</td>
</tr>
<tr class="row-cephfs">
  <td><span class="badge badge-role-cephfs">CephFS admin</span> <a href="roles/cephfs-admin/">→</a></td>
  <td>File systems, MDS, mounts</td>
  <td>ceph fs, MDS config</td>
</tr>
</tbody>
</table>

## By scale

<table class="guide-table">
<thead>
<tr><th>Scale</th><th>Typical size</th><th>Start here</th></tr>
</thead>
<tbody>
<tr class="row-lab">
  <td><span class="badge badge-scale-lab">Lab / dev</span> <a href="scales/lab/">→</a></td>
  <td>1–3 nodes, testing</td>
  <td>Minimal setup, loose tuning</td>
</tr>
<tr class="row-small">
  <td><span class="badge badge-scale-small">Small production</span> <a href="scales/small-production/">→</a></td>
  <td>3–12 nodes</td>
  <td>Replica 3, PG autoscale</td>
</tr>
<tr class="row-large">
  <td><span class="badge badge-scale-large">Large production</span> <a href="scales/large-production/">→</a></td>
  <td>12+ nodes, many OSDs</td>
  <td>mclock, scrub, capacity</td>
</tr>
<tr class="row-multi">
  <td><span class="badge badge-scale-multi">Multisite</span> <a href="scales/multisite/">→</a></td>
  <td>Multiple sites / regions</td>
  <td>RGW zones, mirroring</td>
</tr>
</tbody>
</table>

## General

- [Quick start](quickstart.md) — daily checklist (any role)
- [Config lookup](config-lookup.md) — read option tables
- **Config deep dives** (MkDocs: Guides → Config deep dives) — tuning + examples per subsystem:
  RGW · [OSD](osd-config/OVERVIEW.md) · [MON](mon-config/OVERVIEW.md) · [MGR](mgr-config/OVERVIEW.md) · [MDS](mds-config/OVERVIEW.md) · [Global](global-config/OVERVIEW.md)
- [Contributing](contributing.md) — rules, skills, regeneration

[← Main reference](../index.md)
