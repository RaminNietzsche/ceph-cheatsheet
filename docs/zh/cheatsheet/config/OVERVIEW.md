# Ceph 配置参考

按子系统浏览。每个分区都有选项索引与详细表格。

> **说明：** 下表中的选项说明来自 upstream Ceph（英文）。

<div class="level-legend">
<span class="badge badge-level-basic">Basic</span>
<span class="badge badge-level-advanced">Advanced</span>
<span class="badge badge-level-dev">Dev</span>
</div>

<table class="guide-table config-overview">
<thead>
<tr><th>子系统</th><th>说明</th><th>索引</th></tr>
</thead>
<tbody>
<tr class="row-global"><td><a href="global/INDEX/"><span class="badge badge-cfg-global">global</span></a></td><td>认证、存储后端、日志、网络、调试</td><td><a href="global/INDEX/">索引</a></td></tr>
<tr class="row-osd"><td><a href="osd/INDEX/"><span class="badge badge-cfg-osd">osd</span></a></td><td>Object Storage Daemon — 恢复、scrub、mclock</td><td><a href="osd/INDEX/">索引</a></td></tr>
<tr class="row-mon"><td><a href="mon/INDEX/"><span class="badge badge-cfg-mon">mon</span></a></td><td>Monitor — 集群地图、paxos</td><td><a href="mon/INDEX/">索引</a></td></tr>
<tr class="row-mgr"><td><a href="mgr/INDEX/"><span class="badge badge-cfg-mgr">mgr</span></a></td><td>Manager — 模块、cephadm</td><td><a href="mgr/INDEX/">索引</a></td></tr>
<tr class="row-mds"><td><a href="mds/INDEX/"><span class="badge badge-cfg-mds">mds</span></a></td><td>CephFS 元数据服务器</td><td><a href="mds/INDEX/">索引</a></td></tr>
<tr class="row-mds-client"><td><a href="mds-client/INDEX/"><span class="badge badge-cfg-mds-client">mds-client</span></a></td><td>CephFS 客户端 / FUSE</td><td><a href="mds-client/INDEX/">索引</a></td></tr>
<tr class="row-rgw"><td><a href="rgw/INDEX/"><span class="badge badge-cfg-rgw">rgw</span></a></td><td>RADOS Gateway — S3、多站点、加密</td><td><a href="rgw/INDEX/">索引</a></td></tr>
<tr class="row-rbd"><td><a href="rbd/INDEX/"><span class="badge badge-cfg-rbd">rbd</span></a></td><td>RADOS Block Device — 镜像、缓存、特性</td><td><a href="rbd/INDEX/">索引</a></td></tr>
<tr class="row-rbd-mirror"><td><a href="rbd-mirror/INDEX/"><span class="badge badge-cfg-rbd-mirror">rbd-mirror</span></a></td><td>RBD 异步镜像</td><td><a href="rbd-mirror/INDEX/">索引</a></td></tr>
<tr class="row-cephfs-mirror"><td><a href="cephfs-mirror/INDEX/"><span class="badge badge-cfg-cephfs-mirror">cephfs-mirror</span></a></td><td>CephFS 镜像</td><td><a href="cephfs-mirror/INDEX/">索引</a></td></tr>
<tr class="row-crimson"><td><a href="crimson/INDEX/"><span class="badge badge-cfg-crimson">crimson</span></a></td><td>Crimson OSD / Seastore（实验性）</td><td><a href="crimson/INDEX/">索引</a></td></tr>
<tr class="row-immutable"><td><a href="immutable-object-cache/INDEX/"><span class="badge badge-cfg-immutable">immutable-object-cache</span></a></td><td>不可变对象缓存</td><td><a href="immutable-object-cache/INDEX/">索引</a></td></tr>
<tr class="row-exporter"><td><a href="ceph-exporter/INDEX/"><span class="badge badge-cfg-exporter">ceph-exporter</span></a></td><td>Prometheus ceph-exporter 指标</td><td><a href="ceph-exporter/INDEX/">索引</a></td></tr>
</tbody>
</table>

## 搜索

在仓库根目录：

```bash
./scripts/search-config.sh <option-or-keyword>
./scripts/search-config.sh -s osd scrub
```

## 完整 master 索引

生成器还会写入 `config/readme.md`（跨子系统 TOC，供脚本使用）。
通过上方子系统索引浏览选项，或在编辑 `readme.md` 后运行 `python3 scripts/split-index.py`。

[← Cheatsheet](../index.md)
