# Troubleshooting Guide

Structured diagnosis for common production issues. For command quick-reference see [CLI troubleshooting](../cli/troubleshooting.md).

## 1. PG stuck / recovery

**Symptoms:** PGs `degraded`, `recovering`, or `stuck` for a long time; `ceph health` warnings.

```bash
ceph -s
ceph pg stat
ceph pg dump_stuck inactive
ceph pg dump_stuck unclean
ceph osd blocked-by
```

**Actions:**

| Situation | Fix |
|-----------|-----|
| Slow recovery | Temporarily raise `osd_recovery_max_active` (maintenance window) |
| Backfill storm | Lower `osd_max_backfills`; check network/disk |
| Stuck inactive | Find down OSDs: `ceph osd tree`; restore or mark out |
| Inconsistent PG | `ceph pg repair <pgid>` after fixing hardware |

Deep dive: [OSD recovery config](../guides/osd-config/recovery/recovery.md)

## 2. OSD flapping

**Symptoms:** OSDs repeatedly go `down`/`up`; slow requests; heartbeat timeouts.

```bash
ceph osd tree
ceph daemon osd.<id> dump_historic_ops
journalctl -u ceph-osd@<id> --since "1 hour ago"
ceph config get osd osd_heartbeat_grace
```

**Check:** disk errors, network latency between OSDs, insufficient RAM (`osd_memory_target`), overloaded CPU.

## 3. RGW errors

### HTTP 503 / SlowDown

Often rate limiting or dmclock throttling.

```bash
ceph config get client.rgw rgw_enable_rate_limit
radosgw-admin user stats --uid=<user>
```

See [Rate limit architecture](../../arch/rgw/architecture/rate-limit-architecture.md).

### NoSuchBucket / wrong endpoint

Verify zone, tenant, and `rgw dns name`:

```bash
radosgw-admin bucket stats --bucket=<name>
ceph config get client.rgw rgw_zone
```

### Multisite sync lag

```bash
radosgw-admin sync status
radosgw-admin sync error list
radosgw-admin period update --commit   # after config change only
```

Guide: [Multisite scale](scales/multisite.md) · [RGW admin role](roles/rgw-admin.md)

## 4. Monitor quorum problems

**Symptoms:** `HEALTH_ERR` mon quorum; clients cannot connect.

```bash
ceph mon stat
ceph quorum_status --format json-pretty
ceph daemon mon.<name> mon_status
```

Ensure odd number of MONs, stable clock sync (chrony), and no firewall blocking mon ports.

## 5. Cephadm deployment issues

```bash
ceph orch ps
ceph orch host ls
cephadm ls
journalctl -u ceph-<cluster>-@*.service --since today
ceph orch upgrade status
```

Common fixes: fix container registry access, re-deploy daemon with `ceph orch redeploy <svc>`.

## 6. Performance bottlenecks

| Layer | Commands |
|-------|----------|
| Cluster | `ceph osd perf`, `ceph osd df tree`, `ceph health detail` |
| OSD | `ceph daemon osd.<id> perf dump` |
| RGW | ops log, `l_rgw_qlen` metrics — [Observability](../../arch/rgw/architecture/observability-overview.md) |
| Network | Compare `public_network` vs `cluster_network` load |

**Throttle recovery during business hours:**

```bash
ceph config set osd osd_max_backfills 1
ceph config set osd osd_recovery_max_active 3
```

## 7. Log analysis workflow

1. `ceph -s` and `ceph health detail` — cluster-wide
2. Daemon logs via `ceph orch logs` or `journalctl`
3. Raise debug temporarily: `ceph config set osd debug_osd 20/5`
4. Revert debug after capture

[← Guides overview](OVERVIEW.md)
