# 故障排查命令

## 日志

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

## 性能与慢请求

```bash
ceph daemon osd.<id> perf dump
ceph daemon osd.<id> dump_historic_ops
ceph daemon osd.<id> dump_ops_in_flight
ceph tell osd.<id> dump_ops_in_flight
ceph health detail                     # SLOW_OPS warnings
```

## 恢复与 backfill

```bash
ceph -s                                # recovery progress
ceph pg stat
ceph pg dump | grep -E 'degraded|recovering|backfill'
ceph osd blocked-by
ceph tell osd.* injectargs '--osd_max_backfills=1'   # throttle (temporary)
```

## 不一致 PG / 对象

```bash
ceph pg dump | grep inconsistent
rados list-inconsistent-pg <pool>
rados list-inconsistent-obj <pgid> --format json-pretty
ceph pg repair <pgid>
```

## 集群 full / nearfull

```bash
ceph df detail
ceph osd df tree
ceph osd pool set <pool> size <n>      # reduce if oversized (careful!)
ceph osd reweight-by-utilization
```

## Monitor 问题

```bash
ceph mon stat
ceph quorum_status --format json-pretty
ceph daemon mon.<name> mon_status
ceph mon dump
```

## RGW 问题

```bash
radosgw-admin sync status
radosgw-admin gc process --include-all
ceph orch ps --service-type rgw
ceph config show client.rgw.<instance>
ceph daemon rgw.<id> perf dump          # local admin socket on RGW node
```

## RBD 问题

```bash
rbd status <pool>/<image>
rbd showmapped
rbd mirror pool status <pool>
```

## 配置参考查找

调优时查看选项默认值与标志：

```bash
./scripts/lookup-config.sh <option-name>
./scripts/search-config.sh <keyword>
```

[← CLI 概览](OVERVIEW.md)
