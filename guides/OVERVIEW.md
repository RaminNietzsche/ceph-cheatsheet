# Guides

Task-oriented documentation organized by **who you are** (role) and **how big the cluster is** (scale).

## By role

| Role | You manage… | Start here |
|------|-------------|------------|
| [Cluster admin](roles/cluster-admin.md) | Mon, MGR, cephadm, upgrades, auth | Daily health, orchestrator |
| [Storage operator](roles/storage-operator.md) | OSDs, pools, PGs, CRUSH, capacity | OSD/pool ops, recovery |
| [RGW admin](roles/rgw-admin.md) | S3 gateway, users, multisite | radosgw-admin, RGW config |
| [CephFS admin](roles/cephfs-admin.md) | File systems, MDS, mounts | ceph fs, MDS config |

## By scale

| Scale | Typical size | Start here |
|-------|--------------|------------|
| [Lab / dev](scales/lab.md) | 1–3 nodes, testing | Minimal setup, loose tuning |
| [Small production](scales/small-production.md) | 3–12 nodes | Replica 3, PG autoscale |
| [Large production](scales/large-production.md) | 12+ nodes, many OSDs | mclock, scrub, capacity |
| [Multisite](scales/multisite.md) | Multiple sites / regions | RGW zones, mirroring |

## General

- [Quick start](quickstart.md) — daily checklist (any role)
- [Config lookup](config-lookup.md) — read option tables
- [Contributing](contributing.md) — rules, skills, regeneration

[← Main reference](../REFERENCE.md)
