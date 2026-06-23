# Lab / Development Scale

<span class="badge badge-scale-lab">Lab / dev</span> 1–3 nodes, testing, learning, CI — **not for production data**.

## Goals

- Minimal footprint, fast iteration
- Accept single points of failure
- Looser durability only on isolated lab networks

## Suggested layout

```bash
cephadm bootstrap --mon-ip <ip> --single-host-defaults
ceph orch apply mon --placement="1"
ceph orch apply mgr --placement="1"
ceph orch apply osd --all-available-devices
```

## Tuning hints

| Area | Lab approach |
|------|--------------|
| Replication | `size=2` with `--single-host-defaults` on one host |
| PGs | Autoscale on; small pools |
| OSD memory | Lower `osd_memory_target` if RAM constrained |
| Scrub | Longer intervals to reduce disk churn |

```bash
./scripts/lookup-config.sh osd_memory_target
./scripts/lookup-config.sh osd_pool_default_pg_autoscale_mode
```

## Role guides

| Role | Guide |
|------|-------|
| Cluster | [cluster-admin.md](../roles/cluster-admin.md) |
| Storage | [storage-operator.md](../roles/storage-operator.md) |
| RGW (optional) | [rgw-admin.md](../roles/rgw-admin.md) |
| CephFS (optional) | [cephfs-admin.md](../roles/cephfs-admin.md) |

## CLI quick ref

[cli/cluster.md](../../cli/cluster.md) · [cli/osd-pool.md](../../cli/osd-pool.md)

[← Guides overview](../OVERVIEW.md)
