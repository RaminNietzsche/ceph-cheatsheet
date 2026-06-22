# Lab / Development Scale

1–3 nodes, testing, learning, CI — not for production data.

## Goals

- Minimal footprint, fast iteration
- Accept single points of failure
- Looser durability settings only in isolated lab networks

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
| Replication | `size=2` acceptable on single host with `--single-host-defaults` |
| PGs | Autoscale on; small pools |
| OSD memory | Lower `osd_memory_target` if RAM constrained |
| Scrub | Can increase intervals for less disk churn |

Look up options:

```bash
./scripts/lookup-config.sh osd_memory_target
./scripts/lookup-config.sh osd_pool_default_pg_autoscale_mode
```

## Role guides

- [Cluster admin](../roles/cluster-admin.md) — bootstrap
- [Storage operator](../roles/storage-operator.md) — first pool

## CLI quick ref

[cli/cluster.md](../../cli/cluster.md) · [cli/osd-pool.md](../../cli/osd-pool.md)

[← Guides overview](../OVERVIEW.md)
