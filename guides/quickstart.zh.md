# 快速入门 — 日常运维流程

操作 Ceph 集群的最小流程。请按环境调整（cephadm 或手动部署、发行版版本）。

## 1. 检查集群健康

```bash
ceph -s
ceph health detail
ceph versions
ceph orch ps          # if using cephadm
```

期望：`health: HEALTH_OK`，所有 OSD 在线，quorum 正常。

## 2. 容量与使用率

```bash
ceph df
ceph df detail
ceph osd df tree
```

关注 `nearfull` / `backfillfull` 警告。

## 3. PG 状态

```bash
ceph pg stat
ceph pg dump_stuck
```

所有 PG 应为 `active+clean`。排查 `degraded`、`recovering`、`backfilling` 或 `stuck`。

## 4. 常见变更

```bash
# Set a runtime config option
ceph config set osd osd_max_scrubs 2

# Create an RBD pool
ceph osd pool create rbd 128 128 replicated
ceph osd pool application enable rbd rbd

# Create an RBD image
rbd create rbd/myimage --size 10G

# Mark OSD out for maintenance
ceph osd out 5
# … wait for backfill …
ceph osd in 5
```

## 5. 升级前

```bash
ceph versions                         # mixed versions?
ceph health detail
ceph osd ok-to-stop osd.0 osd.1 …    # check N OSDs at a time
ceph orch upgrade status              # cephadm path
```

## 6. 出问题时

1. `ceph health detail` — 阅读警告/错误文本
2. `ceph -w` — 观察实时事件
3. [故障排查命令](../cli/troubleshooting.md)
4. 查找相关配置：`./scripts/lookup-config.sh <option>`

## 查找速查

```bash
./scripts/lookup-config.sh osd_max_scrubs
./scripts/search-all.sh "full ratio"
./scripts/search-config.sh -s rgw cache
```

## 下一步

- 按 [角色](OVERVIEW.md#by-role) 或 [规模](OVERVIEW.md#by-scale) 选择更聚焦的流程。

[← Cheatsheet](../index.md)
