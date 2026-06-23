# Ceph Configuration Reference

Browse by subsystem. Each section has an option index and detailed tables.

<div class="level-legend">
<span class="badge badge-level-basic">Basic</span>
<span class="badge badge-level-advanced">Advanced</span>
<span class="badge badge-level-dev">Dev</span>
</div>

<table class="guide-table config-overview">
<thead>
<tr><th>Subsystem</th><th>Description</th><th>Index</th></tr>
</thead>
<tbody>
<tr class="row-global"><td><a href="global/INDEX/"><span class="badge badge-cfg-global">global</span></a></td><td>Auth, storage backends, logging, networking, debug</td><td><a href="global/INDEX/">index</a></td></tr>
<tr class="row-osd"><td><a href="osd/INDEX/"><span class="badge badge-cfg-osd">osd</span></a></td><td>Object Storage Daemon — recovery, scrub, mclock</td><td><a href="osd/INDEX/">index</a></td></tr>
<tr class="row-mon"><td><a href="mon/INDEX/"><span class="badge badge-cfg-mon">mon</span></a></td><td>Monitor — cluster map, paxos</td><td><a href="mon/INDEX/">index</a></td></tr>
<tr class="row-mgr"><td><a href="mgr/INDEX/"><span class="badge badge-cfg-mgr">mgr</span></a></td><td>Manager — modules, cephadm</td><td><a href="mgr/INDEX/">index</a></td></tr>
<tr class="row-mds"><td><a href="mds/INDEX/"><span class="badge badge-cfg-mds">mds</span></a></td><td>CephFS metadata server</td><td><a href="mds/INDEX/">index</a></td></tr>
<tr class="row-mds-client"><td><a href="mds-client/INDEX/"><span class="badge badge-cfg-mds-client">mds-client</span></a></td><td>CephFS client / FUSE</td><td><a href="mds-client/INDEX/">index</a></td></tr>
<tr class="row-rgw"><td><a href="rgw/INDEX/"><span class="badge badge-cfg-rgw">rgw</span></a></td><td>RADOS Gateway — S3, multisite, encryption</td><td><a href="rgw/INDEX/">index</a></td></tr>
<tr class="row-rbd"><td><a href="rbd/INDEX/"><span class="badge badge-cfg-rbd">rbd</span></a></td><td>RADOS Block Device — images, cache, features</td><td><a href="rbd/INDEX/">index</a></td></tr>
<tr class="row-rbd-mirror"><td><a href="rbd-mirror/INDEX/"><span class="badge badge-cfg-rbd-mirror">rbd-mirror</span></a></td><td>RBD asynchronous mirroring</td><td><a href="rbd-mirror/INDEX/">index</a></td></tr>
<tr class="row-cephfs-mirror"><td><a href="cephfs-mirror/INDEX/"><span class="badge badge-cfg-cephfs-mirror">cephfs-mirror</span></a></td><td>CephFS mirroring</td><td><a href="cephfs-mirror/INDEX/">index</a></td></tr>
<tr class="row-crimson"><td><a href="crimson/INDEX/"><span class="badge badge-cfg-crimson">crimson</span></a></td><td>Crimson OSD / Seastore (experimental)</td><td><a href="crimson/INDEX/">index</a></td></tr>
<tr class="row-immutable"><td><a href="immutable-object-cache/INDEX/"><span class="badge badge-cfg-immutable">immutable-object-cache</span></a></td><td>Immutable object cache</td><td><a href="immutable-object-cache/INDEX/">index</a></td></tr>
<tr class="row-exporter"><td><a href="ceph-exporter/INDEX/"><span class="badge badge-cfg-exporter">ceph-exporter</span></a></td><td>Prometheus ceph-exporter metrics</td><td><a href="ceph-exporter/INDEX/">index</a></td></tr>
</tbody>
</table>

## Search

From the repo root:

```bash
./scripts/search-config.sh <option-or-keyword>
./scripts/search-config.sh -s osd scrub
```

## Full master index

The generator also writes `config/readme.md` (cross-subsystem TOC for scripts).  
Browse options on the site via the subsystem indexes above, or run `python3 scripts/split-index.py` after editing `readme.md`.

[← Cheatsheet](../cheatsheet/OVERVIEW.md)
