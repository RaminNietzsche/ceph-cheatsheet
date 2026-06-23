# Getting Started

New to Ceph? Start here before diving into config tables or RGW internals.

## What is Ceph?

Ceph is a unified, software-defined storage platform. One cluster can expose:

| Interface | Use case |
|-----------|----------|
| **RADOS** | Raw object/block storage (internal) |
| **RBD** | Block volumes for VMs / Kubernetes |
| **RGW** | S3/Swift object storage |
| **CephFS** | POSIX file system |

## Core concepts (glossary)

| Term | Meaning |
|------|---------|
| **MON** | Monitor — keeps cluster maps and quorum |
| **OSD** | Object Storage Daemon — stores data on disks |
| **MGR** | Manager — modules, metrics, orchestration UI |
| **MDS** | Metadata server — CephFS directory metadata |
| **PG** | Placement group — shard of a pool for recovery |
| **CRUSH** | Algorithm mapping objects to OSDs |
| **Pool** | Logical partition of storage with replication rules |
| **RGW** | RADOS Gateway — HTTP S3/Swift front-end |
| **SAL** | Store Abstraction Layer in RGW (`sal::Driver`) |
| **Realm / Zone** | RGW multisite configuration hierarchy |

## Choose your path

| You are… | Start with |
|----------|------------|
| New cluster operator | [Quick start](quickstart.md) → [Cluster admin role](roles/cluster-admin.md) |
| OSD / capacity owner | [Storage operator](roles/storage-operator.md) → [OSD config](../guides/osd-config/OVERVIEW.md) |
| S3 / object storage admin | [RGW admin](roles/rgw-admin.md) → [RGW architecture](../../arch/rgw/OVERVIEW.md) |
| File storage admin | [CephFS admin](roles/cephfs-admin.md) |
| Developer / contributor | [Develop section](../../dev/index.md) → [Learning program](../../arch/rgw/learning-program/index.md) |

## By cluster size

| Scale | Guide |
|-------|--------|
| Lab / testing | [Lab scale](scales/lab.md) · [Lab config example](../config/examples/lab.md) |
| Small production | [Small production](scales/small-production.md) · [Example config](../config/examples/small-production.md) |
| Large production | [Large production](scales/large-production.md) · [Example config](../config/examples/large-production.md) |
| Multisite | [Multisite scale](scales/multisite.md) · [Example config](../config/examples/multisite.md) |

## Tools in this repo

```bash
./scripts/lookup-config.sh osd_max_scrubs    # one config option
./scripts/search-config.sh -s rgw cache      # search config tables
./scripts/search-all.sh scrub                # CLI + config
./scripts/search-fuzzy.sh                    # interactive (requires fzf)
```

## Version note

Config and CLI in this repo track **Ceph `main`** (see [compatibility](../../compatibility.md)). Check your cluster with `ceph versions` before applying settings.

[← Guides overview](OVERVIEW.md)
