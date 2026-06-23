> **یادداشت:** توضیحات گزینه‌ها در جدول از upstream Ceph (انگلیسی) است.

# Troubleshooting Commands

## Logs

```bash
# Cluster log (recent events)
ceph log last [n]
ceph log dump

# Daemon logs (cephadm)
ceph orch logs mon.<host>.<id> --follow
ceph orch logs osd.<host>.<id> --follow
journalctl -u ceph-osd@<id> -f          # systemd (non-cephadm)

# Debug levels (runtime)
ceph config set global debug_ms 1/5
ceph config set osd debug_osd 20/5
ceph config set mon debug_mon 10/5
ceph tell osd.* config set debug_osd 20/5
```

## Performance & slow requests

```bash
ceph daemon osd.<id> perf dump
ceph daemon osd.<id> dump_historic_ops
ceph daemon osd.<id> dump_ops_in_flight
ceph tell osd.<id> dump_ops_in_flight
ceph health detail                     # SLOW_OPS warnings
```

## Recovery & backfill

```bash
ceph -s                                # recovery progress
ceph pg stat
ceph pg dump | grep -E 'degraded|recovering|backfill'
ceph osd blocked-by
ceph tell osd.* injectargs '--osd_max_backfills=1'   # throttle (temporary)
```

## Inconsistent PGs / objects

```bash
ceph pg dump | grep inconsistent
rados list-inconsistent-pg <pool>
rados list-inconsistent-obj <pgid> --format json-pretty
ceph pg repair <pgid>
```

## Full / nearfull cluster

```bash
ceph df detail
ceph osd df tree
ceph osd pool set <pool> size <n>      # reduce if oversized (careful!)
ceph osd reweight-by-utilization
```

## Monitor issues

```bash
ceph mon stat
ceph quorum_status --format json-pretty
ceph daemon mon.<name> mon_status
ceph mon dump
```

## RGW issues

```bash
radosgw-admin sync status
radosgw-admin gc process --include-all
ceph orch ps --service-type rgw
ceph config show client.rgw.<instance>
ceph daemon rgw.<id> perf dump          # local admin socket on RGW node
```

## RBD issues

```bash
rbd status <pool>/<image>
rbd showmapped
rbd mirror pool status <pool>
```

## Config reference lookup

When tuning, look up option defaults and flags:

```bash
./scripts/lookup-config.sh <option-name>
./scripts/search-config.sh <keyword>
```

[← CLI overview](OVERVIEW.md)
