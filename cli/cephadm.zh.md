> **说明：** 下表中的选项说明来自 upstream Ceph（英文）。

# Cephadm & Orchestrator Commands

Requires active `ceph mgr` module: `ceph mgr module enable cephadm`.

## Cluster bootstrap

```bash
cephadm bootstrap --mon-ip <ip> [--cluster-network …] [--single-host-defaults]
cephadm install                        # install cephadm on local host
```

## Host management

```bash
ceph orch host ls
ceph orch host add <hostname> [--addr ip] [--labels label1,label2]
ceph orch host rm <hostname> [--offline] [--force]
ceph orch host label add|rm <hostname> <label>
ceph orch host maintenance enter|exit <hostname>
```

## Service deployment

```bash
ceph orch ls
ceph orch ps
ceph orch apply mon --unmanaged | 3
ceph orch apply mgr --unmanaged | 2
ceph orch apply osd --all-available-devices
ceph orch apply rgw <svc-id> --placement="3 host1 host2" --port=8080
ceph orch apply mds <fs-name> --placement="2"
ceph orch apply node-exporter
ceph orch apply ceph-exporter

ceph orch daemon ls
ceph orch daemon restart <daemon-type>.<hostname>.<id>
ceph orch daemon redeploy <daemon>
ceph orch daemon rm <daemon> [--force]
```

## Upgrades

```bash
ceph orch upgrade ls
ceph orch upgrade start --image quay.io/ceph/ceph:v19
ceph orch upgrade status
ceph orch upgrade pause|resume|stop
```

## Device / OSD

```bash
ceph orch device ls
ceph orch device zap <hostname> <path> [--force]
ceph orch daemon add osd <hostname>:<device-path>
```

## Logs & shell

```bash
ceph orch logs <svc-type>.<hostname>.<id> [--follow]
cephadm shell                              # run ceph commands in container
cephadm enter --name <daemon-name>
```

See [config/mgr/cephadm](../config/mgr/INDEX.md) for cephadm-related config options.

[← CLI overview](OVERVIEW.md)
