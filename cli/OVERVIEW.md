# CLI Command Reference

<span class="badge badge-cli">CLI</span> Essential Ceph commands for day-to-day cluster administration. Commands assume a running cluster with `ceph` CLI access and appropriate credentials (`ceph.conf` / keyring).

<table class="guide-table">
<thead>
<tr><th>Section</th><th>Topics</th></tr>
</thead>
<tbody>
<tr class="row-cluster"><td><span class="badge badge-cli">cluster</span> <a href="cluster/">→</a></td><td>Status, health, monitors, versions</td></tr>
<tr class="row-small"><td><span class="badge badge-cli">config</span> <a href="config/">→</a></td><td>Runtime configuration (<code>ceph config …</code>)</td></tr>
<tr class="row-storage"><td><span class="badge badge-cli">osd-pool</span> <a href="osd-pool/">→</a></td><td>OSDs, pools, placement groups</td></tr>
<tr class="row-lab"><td><span class="badge badge-cli">rados</span> <a href="rados/">→</a></td><td>Low-level RADOS objects and pools</td></tr>
<tr class="row-large"><td><span class="badge badge-cli">rbd</span> <a href="rbd/">→</a></td><td>Block images, snapshots, mapping</td></tr>
<tr class="row-rgw"><td><span class="badge badge-cli">rgw</span> <a href="rgw/">→</a></td><td>S3/Swift admin, users, buckets</td></tr>
<tr class="row-cephfs"><td><span class="badge badge-cli">cephfs</span> <a href="cephfs/">→</a></td><td>File systems, MDS, mounts</td></tr>
<tr class="row-multi"><td><span class="badge badge-cli">cephadm</span> <a href="cephadm/">→</a></td><td>Orchestrator, services, hosts</td></tr>
<tr class="row-dev"><td><span class="badge badge-cli">troubleshooting</span> <a href="troubleshooting/">→</a></td><td>Logs, perf, recovery, common fixes</td></tr>
</tbody>
</table>

## Global flags

Most commands accept:

```bash
ceph -s                          # short status
ceph -w                          # watch cluster events
ceph --cluster mycluster …       # non-default cluster name
ceph -c /path/ceph.conf …
ceph -k /path/keyring …
ceph -n client.admin …           # explicit entity name
```

## Command families

| Binary | Purpose |
|--------|---------|
| `ceph` | Cluster admin — health, config, orch, tell |
| `rados` | Direct pool/object I/O |
| `rbd` | Block device management |
| `radosgw-admin` | RGW users, buckets, zones |
| `cephadm` | Bootstrap and node-level cephadm ops |
| `cephfs` | CephFS shell (interactive) |

## Quick examples

```bash
ceph status
ceph health detail
ceph osd tree
ceph df
ceph pg stat
rbd ls
radosgw-admin user list
ceph orch ps
```

[← Back to main reference](../index.md)
