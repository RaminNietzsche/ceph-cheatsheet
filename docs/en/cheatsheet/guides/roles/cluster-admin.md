# Cluster Admin

<span class="badge badge-role-cluster">Cluster admin</span> Manage monitors, managers, orchestration, cluster health, auth, and upgrades.

## Daily commands

```bash
ceph -s
ceph health detail
ceph versions
ceph orch ps                    # cephadm
ceph mon stat
ceph mgr stat
```

See [cluster CLI](../../cli/cluster.md) and [cephadm CLI](../../cli/cephadm.md).

## Configuration

| Task | Command / config |
|------|------------------|
| Runtime config | [cli/config.md](../../cli/config.md) — `ceph config set …` |
| Monitor options | [config/mon/INDEX.md](../../config/mon/INDEX.md) · [MON deep dive](../mon-config/OVERVIEW.md) |
| Manager / modules | [config/mgr/INDEX.md](../../config/mgr/INDEX.md) · [MGR deep dive](../mgr-config/OVERVIEW.md) |
| Auth & keys | [config/global/auth.md](../../config/global/auth.md) · [Global deep dive](../global-config/OVERVIEW.md) |
| cephadm path | `cephadm_path` in [config/mgr/cephadm.md](../../config/mgr/cephadm.md) |

Hot options: `mon_osd_down_out_interval`, `mgr_standby_modules`, `cephadm_path` — see [MON](../mon-config/TUNING.md) and [MGR](../mgr-config/TUNING.md) tuning indexes.

## Common workflows

**Deploy services (cephadm):**

```bash
ceph orch apply mon --placement="3"
ceph orch apply mgr --placement="2"
ceph orch apply osd --all-available-devices
```

**Upgrade cluster:**

```bash
ceph orch upgrade ls
ceph orch upgrade start --image quay.io/ceph/ceph:v19
ceph orch upgrade status
```

**Add host / monitor:**

```bash
ceph orch host add newhost --labels _admin
ceph orch apply mon --placement="host1 host2 host3"
```

## Scale notes

| Scale | Focus |
|-------|--------|
| [Lab](../scales/lab.md) | Single mon, `--single-host-defaults` |
| [Small production](../scales/small-production.md) | 3 mon, 2 mgr, one DC |
| [Large production](../scales/large-production.md) | Stretch rules, separate networks |
| [Multisite](../scales/multisite.md) | Mon quorum per site or stretch |

## Troubleshooting

[cli/troubleshooting.md](../../cli/troubleshooting.md) — logs, mon quorum, upgrade stalls

[← Guides overview](../OVERVIEW.md)
