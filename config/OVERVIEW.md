# Ceph Configuration Reference

Browse by subsystem. Each section has an option index and detailed tables.

<div class="level-legend">
<span class="badge badge-level-basic">Basic</span>
<span class="badge badge-level-advanced">Advanced</span>
<span class="badge badge-level-dev">Dev</span>
</div>

<table class="guide-table">
<thead>
<tr><th>Subsystem</th><th>Description</th><th>Index</th></tr>
</thead>
<tbody>
<tr class="row-cluster"><td><span class="badge badge-config">global</span></td><td>Auth, storage backends, logging, networking, debug</td><td><a href="global/INDEX.md">index</a></td></tr>
<tr class="row-storage"><td><span class="badge badge-config">osd</span></td><td>Object Storage Daemon — recovery, scrub, mclock</td><td><a href="osd/INDEX.md">index</a></td></tr>
<tr class="row-small"><td><span class="badge badge-config">mon</span></td><td>Monitor — cluster map, paxos</td><td><a href="mon/INDEX.md">index</a></td></tr>
<tr class="row-rgw"><td><span class="badge badge-config">mgr</span></td><td>Manager — modules, cephadm</td><td><a href="mgr/INDEX.md">index</a></td></tr>
<tr class="row-cephfs"><td><span class="badge badge-config">mds</span></td><td>CephFS metadata server</td><td><a href="mds/INDEX.md">index</a></td></tr>
<tr class="row-lab"><td><span class="badge badge-config">mds-client</span></td><td>CephFS client / FUSE</td><td><a href="mds-client/INDEX.md">index</a></td></tr>
<tr class="row-multi"><td><span class="badge badge-config">rgw</span></td><td>RADOS Gateway — S3, multisite, encryption</td><td><a href="rgw/INDEX.md">index</a></td></tr>
<tr class="row-large"><td><span class="badge badge-config">rbd</span></td><td>RADOS Block Device — images, cache, features</td><td><a href="rbd/INDEX.md">index</a></td></tr>
<tr class="row-small"><td><span class="badge badge-config">rbd-mirror</span></td><td>RBD asynchronous mirroring</td><td><a href="rbd-mirror/INDEX.md">index</a></td></tr>
<tr class="row-cephfs"><td><span class="badge badge-config">cephfs-mirror</span></td><td>CephFS mirroring</td><td><a href="cephfs-mirror/INDEX.md">index</a></td></tr>
<tr class="row-multi"><td><span class="badge badge-config">crimson</span></td><td>Crimson OSD / Seastore (experimental)</td><td><a href="crimson/INDEX.md">index</a></td></tr>
<tr class="row-lab"><td><span class="badge badge-config">immutable-object-cache</span></td><td>Immutable object cache</td><td><a href="immutable-object-cache/INDEX.md">index</a></td></tr>
<tr class="row-storage"><td><span class="badge badge-config">ceph-exporter</span></td><td>Prometheus ceph-exporter metrics</td><td><a href="ceph-exporter/INDEX.md">index</a></td></tr>
</tbody>
</table>

## Search

From the repo root:

```bash
./scripts/search-config.sh <option-or-keyword>
./scripts/search-config.sh -s osd scrub
```

## Full master index

The complete cross-subsystem index lives in [`readme.md`](readme.md).  
Run `python3 scripts/split-index.py` to regenerate per-subsystem `INDEX.md` files after editing it.

[← Back to main reference](../index.md)
