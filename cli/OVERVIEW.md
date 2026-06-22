# CLI Command Reference

Essential Ceph commands for day-to-day cluster administration. Commands assume a running cluster with `ceph` CLI access and appropriate credentials (`ceph.conf` / keyring).

| Section | Topics |
|---------|--------|
| [cluster](cluster.md) | Status, health, monitors, versions |
| [config](config.md) | Runtime configuration (`ceph config …`) |
| [osd-pool](osd-pool.md) | OSDs, pools, placement groups |
| [rados](rados.md) | Low-level RADOS objects and pools |
| [rbd](rbd.md) | Block images, snapshots, mapping |
| [rgw](rgw.md) | S3/Swift admin, users, buckets |
| [cephfs](cephfs.md) | File systems, MDS, mounts |
| [cephadm](cephadm.md) | Orchestrator, services, hosts |
| [troubleshooting](troubleshooting.md) | Logs, perf, recovery, common fixes |

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

[← Back to main reference](../REFERENCE.md)
