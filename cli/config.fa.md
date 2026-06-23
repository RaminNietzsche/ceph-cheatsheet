> **یادداشت:** متن این صفحه هنوز به فارسی ترجمه نشده است؛ نسخهٔ انگلیسی در ادامه آمده است.

# Configuration Commands

Runtime config is stored in the monitor config database. See the [config reference](../config/OVERVIEW.md) for option names, defaults, and flags.

## Read config

```bash
ceph config show <who>                 # effective config for a daemon
ceph config show-with-defaults <who>
ceph config get <who> <option>
ceph config dump                       # entire config database
ceph config help <option>              # option metadata (if documented)
```

`<who>` examples: `global`, `mon`, `osd`, `osd.0`, `mgr`, `mds`, `rgw`, `client.rgw.gateway1`

## Set config

```bash
ceph config set <who> <option> <value>
ceph config rm <who> <option>          # remove override (revert to default)
ceph config assimilate-conf -i ceph.conf   # import ceph.conf into mon store
```

Examples:

```bash
ceph config set global mon_allow_pool_delete true
ceph config set osd.0 osd_max_scrubs 2
ceph config set mgr debug_mgr 20/5
ceph config set client.rgw.mygw rgw frontends "beast ssl_port=443"
```

## Legacy / injectargs

```bash
ceph tell osd.* injectargs '--debug-osd=10/5'   # temporary (lost on restart)
```

Prefer `ceph config set` for persistent changes.

## Local ceph.conf

Bootstrap and local-only options still live in `/etc/ceph/ceph.conf`:

```ini
[global]
    fsid = …
    mon_host = 10.0.0.1,10.0.0.2

[mon]
    mon_allow_pool_delete = false

[osd]
    osd_memory_target = 4294967296
```

Check whether an option supports runtime update: look for the `RUNTIME` flag in the [config tables](../config/OVERVIEW.md).

## Lookup a config option locally

```bash
./scripts/lookup-config.sh osd_max_scrubs
./scripts/search-config.sh -s osd scrub
```

[← CLI overview](OVERVIEW.md) · [Config reference](../config/OVERVIEW.md)
