# Global Config Deep Dive — All Options

Extended reference for all **852** Global options with **Finding optimal value** guidance (one section per option). Generated from [config/global/INDEX.md](../../config/global/INDEX.md).

```bash
./scripts/lookup-config.sh <option-name>
python3 scripts/generate-config-guide.py global
```

- [Tuning quick reference](TUNING.md)

## Topics by category


### Storage backends

| Topic | Options |
|-------|---------|
| [Bdev](storage/bdev.md) | 31 |
| [Bluefs](storage/bluefs.md) | 24 |
| [Bluestore](storage/bluestore.md) | 174 |
| [Compressor](storage/compressor.md) | 4 |
| [Ec](storage/ec.md) | 2 |
| [Erasure](storage/erasure.md) | 1 |
| [Filestore](storage/filestore.md) | 84 |
| [Journal](storage/journal.md) | 17 |
| [Journaler](storage/journaler.md) | 3 |
| [Memstore](storage/memstore.md) | 4 |
| [Objectstore](storage/objectstore.md) | 2 |
| [Qat](storage/qat.md) | 3 |
| [Rocksdb](storage/rocksdb.md) | 21 |
| [Uadk](storage/uadk.md) | 2 |

### Auth & keys

| Topic | Options |
|-------|---------|
| [Auth](auth/auth.md) | 9 |
| [Cephx](auth/cephx.md) | 7 |
| [Gss](auth/gss.md) | 2 |
| [Key](auth/key.md) | 1 |
| [Keyfile](auth/keyfile.md) | 1 |
| [Keyring](auth/keyring.md) | 1 |
| [Rotating](auth/rotating.md) | 2 |

### Network & I/O

| Topic | Options |
|-------|---------|
| [Heartbeat](network/heartbeat.md) | 3 |
| [Ms](network/ms.md) | 91 |
| [Objecter](network/objecter.md) | 8 |
| [Osdc](network/osdc.md) | 1 |
| [Public](network/public.md) | 5 |

### Cluster maps

| Topic | Options |
|-------|---------|
| [Ceph](cluster/ceph.md) | 1 |
| [Cluster](cluster/cluster.md) | 3 |
| [Crush](cluster/crush.md) | 3 |
| [Fsid](cluster/fsid.md) | 1 |
| [Mgr](cluster/mgr.md) | 11 |
| [Mon](cluster/mon.md) | 74 |
| [Monmap](cluster/monmap.md) | 1 |
| [Osd](cluster/osd.md) | 174 |
| [Rados](cluster/rados.md) | 5 |

### Logging & debug

| Topic | Options |
|-------|---------|
| [Clog](debug/clog.md) | 7 |
| [Debug](debug/debug.md) | 5 |
| [Err](debug/err.md) | 4 |
| [Event](debug/event.md) | 1 |
| [Inject](debug/inject.md) | 1 |
| [Lockdep](debug/lockdep.md) | 2 |
| [Log](debug/log.md) | 14 |
| [Perf](debug/perf.md) | 1 |

### Runtime & host

| Topic | Options |
|-------|---------|
| [Admin](runtime/admin.md) | 2 |
| [Breakpad](runtime/breakpad.md) | 1 |
| [Cephsqlite](runtime/cephsqlite.md) | 3 |
| [Chdir](runtime/chdir.md) | 1 |
| [Container](runtime/container.md) | 1 |
| [Crash](runtime/crash.md) | 1 |
| [Daemonize](runtime/daemonize.md) | 1 |
| [Device](runtime/device.md) | 1 |
| [Enable](runtime/enable.md) | 1 |
| [Fatal](runtime/fatal.md) | 1 |
| [Filer](runtime/filer.md) | 2 |
| [Fio](runtime/fio.md) | 1 |
| [Host](runtime/host.md) | 1 |
| [Jaeger](runtime/jaeger.md) | 2 |
| [Librados](runtime/librados.md) | 1 |
| [Max](runtime/max.md) | 1 |
| [Mempool](runtime/mempool.md) | 1 |
| [No](runtime/no.md) | 1 |
| [Openssl](runtime/openssl.md) | 1 |
| [Pid](runtime/pid.md) | 1 |
| [Plugin](runtime/plugin.md) | 2 |
| [Restapi](runtime/restapi.md) | 2 |
| [Run](runtime/run.md) | 1 |
| [Service](runtime/service.md) | 1 |
| [Setgroup](runtime/setgroup.md) | 1 |
| [Setuser](runtime/setuser.md) | 2 |
| [Target](runtime/target.md) | 1 |
| [Thp](runtime/thp.md) | 1 |
| [Threadpool](runtime/threadpool.md) | 2 |
| [Throttler](runtime/throttler.md) | 1 |
| [Tmp](runtime/tmp.md) | 2 |

[← Guides overview](../../guides/OVERVIEW.md)
