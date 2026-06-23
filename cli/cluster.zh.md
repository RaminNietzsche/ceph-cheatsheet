# 集群与 Monitor 命令

## 状态与健康

```bash
ceph status                      # full cluster status (-s)
ceph -w                          # watch live cluster changes
ceph health                      # HEALTH_OK / WARN / ERR
ceph health detail               # expanded health checks
ceph versions                    # daemon versions across cluster
ceph mon stat                    # monitor quorum info
ceph mon dump                    # full mon map
ceph mgr stat                    # active/standby mgr
ceph fs ls                       # list CephFS volumes
ceph osd stat                    # osd summary counts
ceph osd df                      # per-OSD usage
ceph osd df tree                 # usage by CRUSH hierarchy
ceph df                          # cluster capacity summary
ceph df detail                   # per-pool breakdown
ceph pg stat                     # placement group summary
ceph pg dump                     # all PG states (verbose)
ceph pg dump_stuck               # stuck PGs only
ceph report                    # recent cluster report
```

## 守护进程管理

```bash
ceph tell osd.<id> version
ceph tell mon.<id> mon_status
ceph tell mgr.<id> config show
ceph daemon osd.<id> config show   # via admin socket (local)
ceph daemon osd.<id> perf dump
ceph daemon osd.<id> help
```

## Monitor 操作

```bash
ceph mon add <name> <ip:port>
ceph mon remove <name>
ceph mon getmap -o monmap
ceph quorum_status --format json-pretty
```

## 认证

```bash
ceph auth ls
ceph auth get client.admin
ceph auth get-or-create client.<name> mon 'allow r' osd 'allow rwx pool=<pool>'
ceph auth del client.<name>
ceph auth caps client.<name> mon 'profile rbd' osd 'profile rbd pool=rbd'
```

## CRUSH 映射

```bash
ceph osd crush tree
ceph osd crush rule ls
ceph osd crush rule dump
ceph osd crush weight-set ls
```

## 监视 / 进度

```bash
ceph -w
ceph progress
ceph progress json
```

[← CLI 概览](OVERVIEW.md)
