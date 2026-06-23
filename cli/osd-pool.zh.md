# OSD、池与 PG 命令

## OSD 生命周期

```bash
ceph osd tree
ceph osd ls
ceph osd ls-tree <bucket>          # e.g. host, rack, root
ceph osd find <id>
ceph osd metadata <id>
ceph osd perf

# Mark OSD in/out/down
ceph osd down <id>                 # mark down (admin)
ceph osd in <id>                   # allow data (default)
ceph osd out <id>                  # drain — triggers backfill
ceph osd rm <id>                   # remove from cluster (must be out + down)
ceph osd destroy <id> --yes-i-really-mean-it

# Weights and rebalancing
ceph osd crush reweight <id> <weight>
ceph osd reweight-by-utilization [max_change] [max_osds]
ceph osd reweight-by-pg [threshold]
```

## OSD 维护

```bash
ceph osd safe-to-destroy <id>      # check before destroy
ceph osd ok-to-stop osd.<id> …     # check before stopping multiple OSDs
ceph osd blocked-by                # what's blocking PGs
ceph osd require-min-compat-client <release>
```

## Scrub 与 deep-scrub

```bash
ceph pg scrub <pgid>
ceph pg deep-scrub <pgid>
ceph osd scrub <osd-id>            # all PGs on OSD
ceph osd deep-scrub <osd-id>
```

## 池管理

```bash
ceph osd lspools
ceph osd pool ls detail
ceph osd pool create <name> <pg> [<pgp>] [replicated|erasure] [<crush-rule>] [<expected-num-objects>]
ceph osd pool delete <name> [<name> --yes-i-really-really-mean-it]
ceph osd pool rename <old> <new>
ceph osd pool get <name> all
ceph osd pool set <name> size <n>
ceph osd pool set <name> min_size <n>
ceph osd pool set <name> pg_num <n>
ceph osd pool set <name> pgp_num <n>
ceph osd pool set <name> crush_rule <rule>
ceph osd pool set <name> application rbd|rgw|cephfs
ceph osd pool autoscale-status
ceph osd pool set <name> pg_autoscale_mode on|off|warn
```

## 纠删码池

```bash
ceph osd erasure-code-profile ls
ceph osd erasure-code-profile set <profile> k=4 m=2 crush-failure-domain=host
ceph osd erasure-code-profile rm <profile>
ceph osd pool create <ec-pool> 12 12 erasure <profile>
```

## 放置组

```bash
ceph pg dump [filtered]
ceph pg dump_stuck [inactive|unclean|stale|undersized|degraded]
ceph pg map <pgid>
ceph pg <pgid> query
ceph pg repair <pgid>
ceph pg force-recovery <pgid>
ceph pg force-backfill <pgid>
ceph pg cancel-force-recovery <pgid>
```

## CRUSH / 设备类

```bash
ceph osd crush class ls
ceph osd crush set-device-class <class> <osd> …
ceph osd crush rule create-replicated <name> default host hdd
```

[← CLI 概览](OVERVIEW.md)
