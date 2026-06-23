# Cephadm 与编排器命令

需要启用 `ceph mgr` 模块：`ceph mgr module enable cephadm`。

## 集群 bootstrap

```bash
cephadm bootstrap --mon-ip <ip> [--cluster-network …] [--single-host-defaults]
cephadm install                        # install cephadm on local host
```

## 主机管理

```bash
ceph orch host ls
ceph orch host add <hostname> [--addr ip] [--labels label1,label2]
ceph orch host rm <hostname> [--offline] [--force]
ceph orch host label add|rm <hostname> <label>
ceph orch host maintenance enter|exit <hostname>
```

## 服务部署

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

## 升级

```bash
ceph orch upgrade ls
ceph orch upgrade start --image quay.io/ceph/ceph:v19
ceph orch upgrade status
ceph orch upgrade pause|resume|stop
```

## 设备 / OSD

```bash
ceph orch device ls
ceph orch device zap <hostname> <path> [--force]
ceph orch daemon add osd <hostname>:<device-path>
```

## 日志与 shell

```bash
ceph orch logs <svc-type>.<hostname>.<id> [--follow]
cephadm shell                              # run ceph commands in container
cephadm enter --name <daemon-name>
```

cephadm 相关配置见 [config/mgr/cephadm](../config/mgr/cephadm.md)。

[← CLI 概览](OVERVIEW.md)
