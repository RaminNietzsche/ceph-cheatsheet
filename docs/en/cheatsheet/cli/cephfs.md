# CephFS Commands

## File system management

```bash
ceph fs ls
ceph fs volume ls
ceph fs new <fs-name> <metadata-pool> <data-pool> [--force]
ceph fs rm <fs-name> [--yes-i-really-mean-it]
ceph fs get <fs-name>
ceph fs set <fs-name> max_mds <n>
ceph fs set <fs-name> allow_standby_replay true|false
ceph fs status [<fs-name>]
ceph fs dump
```

## MDS (metadata server)

```bash
ceph mds stat
ceph mds fail <gid|name>           # mark failed
ceph mds rm <gid> <name>           # remove from map
ceph mds repaired <rank>           # after damage repair
ceph tell mds.<name> command …
```

## Subvolumes & quotas (volumes)

```bash
ceph fs subvolume create <vol> <subvol> [--size bytes] [--group=<group>]
ceph fs subvolume rm <vol> <subvol>
ceph fs subvolume ls <vol>
ceph fs subvolume info <vol> <subvol>
ceph fs subvolumegroup create <vol> <group>
```

## Snapshots

```bash
ceph fs snap-schedule status [<path>]
ceph fs snap-schedule list [<path>]
ceph fs snap-schedule add <path> <interval> [--start-time …]
```

## Mount

```bash
# Kernel mount
mount -t ceph mon1,mon2:/ /mnt/cephfs -o name=admin,secret=<key>

# FUSE
ceph-fuse /mnt/cephfs -n client.admin

# With cephadm / fs volume
ceph fs volume info <vol>
```

## CephFS mirroring

```bash
ceph fs snapshot mirror enable <fs>
ceph fs snapshot mirror disable <fs>
ceph fs snapshot mirror add <fs> <peer_fsid>/<remote_fs>
ceph fs snapshot mirror info <fs>
```

See [config/mds](../config/mds/INDEX.md) and [config/cephfs-mirror](../config/cephfs-mirror/INDEX.md).

[← CLI overview](OVERVIEW.md)
