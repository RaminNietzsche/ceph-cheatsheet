# 指南

按 **职责** 与 **集群规模** 组织的任务导向文档。

## 按角色 {#by-role}

<table class="guide-table">
<thead>
<tr><th>角色</th><th>您负责…</th><th>从这里开始</th></tr>
</thead>
<tbody>
<tr class="row-cluster">
  <td><span class="badge badge-role-cluster">集群管理员</span> <a href="roles/cluster-admin/">→</a></td>
  <td>Mon、MGR、cephadm、升级、认证</td>
  <td>日常健康、编排器</td>
</tr>
<tr class="row-storage">
  <td><span class="badge badge-role-storage">存储运维</span> <a href="roles/storage-operator/">→</a></td>
  <td>OSD、池、PG、CRUSH、容量</td>
  <td>OSD/池操作、恢复</td>
</tr>
<tr class="row-rgw">
  <td><span class="badge badge-role-rgw">RGW 管理员</span> <a href="roles/rgw-admin/">→</a></td>
  <td>S3 网关、用户、多站点</td>
  <td>radosgw-admin、RGW 配置</td>
</tr>
<tr class="row-cephfs">
  <td><span class="badge badge-role-cephfs">CephFS 管理员</span> <a href="roles/cephfs-admin/">→</a></td>
  <td>文件系统、MDS、挂载</td>
  <td>ceph fs、MDS 配置</td>
</tr>
</tbody>
</table>

## 按规模 {#by-scale}

<table class="guide-table">
<thead>
<tr><th>规模</th><th>典型大小</th><th>从这里开始</th></tr>
</thead>
<tbody>
<tr class="row-lab">
  <td><span class="badge badge-scale-lab">实验室 / 开发</span> <a href="scales/lab/">→</a></td>
  <td>1–3 节点，测试</td>
  <td>最小部署、宽松调优</td>
</tr>
<tr class="row-small">
  <td><span class="badge badge-scale-small">小型生产</span> <a href="scales/small-production/">→</a></td>
  <td>3–12 节点</td>
  <td>三副本、PG 自动扩缩</td>
</tr>
<tr class="row-large">
  <td><span class="badge badge-scale-large">大型生产</span> <a href="scales/large-production/">→</a></td>
  <td>12+ 节点，大量 OSD</td>
  <td>mclock、scrub、容量</td>
</tr>
<tr class="row-multi">
  <td><span class="badge badge-scale-multi">多站点</span> <a href="scales/multisite/">→</a></td>
  <td>多站点 / 区域</td>
  <td>RGW zone、镜像</td>
</tr>
</tbody>
</table>

## 通用

- [快速入门](quickstart.md) — 日常检查清单（任意角色）
- [配置查找](config-lookup.md) — 阅读选项表
- **配置深度指南**（MkDocs：指南 → 配置深度指南）— 各子系统调优与示例：
  RGW · [OSD](osd-config/OVERVIEW.md) · [MON](mon-config/OVERVIEW.md) · [MGR](mgr-config/OVERVIEW.md) · [MDS](mds-config/OVERVIEW.md) · [Global](global-config/OVERVIEW.md)
- [贡献](contributing.md) — 规则、技能、重新生成

[← Cheatsheet](../cheatsheet/OVERVIEW.md)
