# CLI 命令参考

<span class="badge badge-cli">CLI</span> 日常集群管理必备 Ceph 命令。前提：集群运行中，可访问 `ceph` CLI 及相应凭据（`ceph.conf` / keyring）。

<table class="guide-table">
<thead>
<tr><th>章节</th><th>主题</th></tr>
</thead>
<tbody>
<tr class="row-cluster"><td><span class="badge badge-cli">cluster</span> <a href="cluster/">→</a></td><td>状态、健康、Monitor、版本</td></tr>
<tr class="row-small"><td><span class="badge badge-cli">config</span> <a href="config/">→</a></td><td>运行时配置（<code>ceph config …</code>）</td></tr>
<tr class="row-storage"><td><span class="badge badge-cli">osd-pool</span> <a href="osd-pool/">→</a></td><td>OSD、池、PG</td></tr>
<tr class="row-lab"><td><span class="badge badge-cli">rados</span> <a href="rados/">→</a></td><td>底层 RADOS 对象与池</td></tr>
<tr class="row-large"><td><span class="badge badge-cli">rbd</span> <a href="rbd/">→</a></td><td>块镜像、快照、映射</td></tr>
<tr class="row-rgw"><td><span class="badge badge-cli">rgw</span> <a href="rgw/">→</a></td><td>S3/Swift 管理、用户、bucket</td></tr>
<tr class="row-cephfs"><td><span class="badge badge-cli">cephfs</span> <a href="cephfs/">→</a></td><td>文件系统、MDS、挂载</td></tr>
<tr class="row-multi"><td><span class="badge badge-cli">cephadm</span> <a href="cephadm/">→</a></td><td>编排器、服务、主机</td></tr>
<tr class="row-dev"><td><span class="badge badge-cli">troubleshooting</span> <a href="troubleshooting/">→</a></td><td>日志、性能、恢复、常见修复</td></tr>
</tbody>
</table>

## 全局选项

多数命令支持：

```bash
ceph -s                          # short status
ceph -w                          # watch cluster events
ceph --cluster mycluster …       # non-default cluster name
ceph -c /path/ceph.conf …
ceph -k /path/keyring …
ceph -n client.admin …           # explicit entity name
```

## 命令族

| 二进制 | 用途 |
|--------|------|
| `ceph` | 集群管理 — 健康、配置、orch、tell |
| `rados` | 直接 pool/对象 I/O |
| `rbd` | 块设备管理 |
| `radosgw-admin` | RGW 用户、bucket、zone |
| `cephadm` | bootstrap 与节点级 cephadm 操作 |
| `cephfs` | CephFS 交互 shell |

## 快速示例

```bash
ceph status
ceph health detail
ceph osd tree
ceph df
ceph pg stat
rbd ls
radosgw-admin user list
ceph orch ps
```

[← Cheatsheet](../index.md)
