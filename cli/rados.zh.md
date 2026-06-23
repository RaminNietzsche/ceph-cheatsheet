# RADOS 命令

底层对象存储接口。通常需通过 `-p` 或 `--pool` 指定池名。

## 池信息

```bash
rados lspools
rados df
rados pool stats <pool>
rados pool get-quota <pool>
rados pool set-quota <pool> [--max-objects N] [--max-size N]
```

## 对象

```bash
rados -p <pool> ls
rados -p <pool> ls <prefix>
rados -p <pool> stat <object>
rados -p <pool> get <object> <local-file>
rados -p <pool> put <object> <local-file>
rados -p <pool> rm <object>
rados -p <pool> create <object>              # empty object
rados -p <pool> cp <src> <dest>
rados -p <pool> mv <src> <dest>
rados -p <pool> truncate <object> <size>
rados -p <pool> touch <object>
```

## 扩展属性与 omap

```bash
rados -p <pool> getxattr <object> <attr>
rados -p <pool> setxattr <object> <attr> <value>
rados -p <pool> rmxattr <object> <attr>
rados -p <pool> listxattr <object>
rados -p <pool> getomapval <object> <key>
rados -p <pool> setomapval <object> <key> <value>
rados -p <pool> rmomapkey <object> <key>
rados -p <pool> listomapkeys <object>
rados -p <pool> listomapvals <object>
```

## 快照与 bench

```bash
rados -p <pool> mksnap <snap-name>
rados -p <pool> rmsnap <snap-name>
rados -p <pool> bench <seconds> write|seq|rand [-b blocksize] [-t threads]
rados cleanup --pool <pool> --prefix <prefix> --dry-run
```

## 通过 rados 管理集群

```bash
rados purge <pool> --yes-i-really-really-mean-it
rados list-inconsistent-pg <pool>
rados list-inconsistent-obj <pgid> --format json-pretty
```

[← CLI 概览](OVERVIEW.md)
