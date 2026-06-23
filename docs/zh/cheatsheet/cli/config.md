# 配置命令

运行时配置存储在 Monitor 配置库中。选项名、默认值与标志见 [配置参考](../config/OVERVIEW.md)。

## 读取配置

```bash
ceph config show <who>                 # effective config for a daemon
ceph config show-with-defaults <who>
ceph config get <who> <option>
ceph config dump                       # entire config database
ceph config help <option>              # option metadata (if documented)
```

`<who>` 示例：`global`、`mon`、`osd`、`osd.0`、`mgr`、`mds`、`rgw`、`client.rgw.gateway1`

## 设置配置

```bash
ceph config set <who> <option> <value>
ceph config rm <who> <option>          # remove override (revert to default)
ceph config assimilate-conf -i ceph.conf   # import ceph.conf into mon store
```

示例：

```bash
ceph config set global mon_allow_pool_delete true
ceph config set osd.0 osd_max_scrubs 2
ceph config set mgr debug_mgr 20/5
ceph config set client.rgw.mygw rgw frontends "beast ssl_port=443"
```

## 旧式 / injectargs

```bash
ceph tell osd.* injectargs '--debug-osd=10/5'   # temporary (lost on restart)
```

持久变更请优先使用 `ceph config set`。

## 本地 ceph.conf

bootstrap 与仅本地选项仍在 `/etc/ceph/ceph.conf`：

```ini
[global]
    fsid = …
    mon_host = 10.0.0.1,10.0.0.2

[mon]
    mon_allow_pool_delete = false

[osd]
    osd_memory_target = 4294967296
```

是否支持运行时更新：在 [配置表](../config/OVERVIEW.md) 中查看 `RUNTIME` 标志。

## 本地查找配置项

```bash
./scripts/lookup-config.sh osd_max_scrubs
./scripts/search-config.sh -s osd scrub
```

[← CLI 概览](OVERVIEW.md) · [配置参考](../config/OVERVIEW.md)
