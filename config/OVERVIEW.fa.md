# مرجع پیکربندی Ceph

بر اساس زیرسیستم مرور کنید. هر بخش یک فهرست گزینه و جدول جزئیات دارد.

> **یادداشت:** توضیحات فنی گزینه‌ها در جدول از مستندات upstream Ceph (انگلیسی) است.

<div class="level-legend">
<span class="badge badge-level-basic">Basic</span>
<span class="badge badge-level-advanced">Advanced</span>
<span class="badge badge-level-dev">Dev</span>
</div>

<table class="guide-table config-overview">
<thead>
<tr><th>زیرسیستم</th><th>توضیح</th><th>فهرست</th></tr>
</thead>
<tbody>
<tr class="row-global"><td><a href="global/INDEX/"><span class="badge badge-cfg-global">global</span></a></td><td>احراز هویت، backend ذخیره‌سازی، log، شبکه، debug</td><td><a href="global/INDEX/">فهرست</a></td></tr>
<tr class="row-osd"><td><a href="osd/INDEX/"><span class="badge badge-cfg-osd">osd</span></a></td><td>Object Storage Daemon — recovery، scrub، mclock</td><td><a href="osd/INDEX/">فهرست</a></td></tr>
<tr class="row-mon"><td><a href="mon/INDEX/"><span class="badge badge-cfg-mon">mon</span></a></td><td>Monitor — نقشه کلاستر، paxos</td><td><a href="mon/INDEX/">فهرست</a></td></tr>
<tr class="row-mgr"><td><a href="mgr/INDEX/"><span class="badge badge-cfg-mgr">mgr</span></a></td><td>Manager — ماژول‌ها، cephadm</td><td><a href="mgr/INDEX/">فهرست</a></td></tr>
<tr class="row-mds"><td><a href="mds/INDEX/"><span class="badge badge-cfg-mds">mds</span></a></td><td>سرور متادیتای CephFS</td><td><a href="mds/INDEX/">فهرست</a></td></tr>
<tr class="row-mds-client"><td><a href="mds-client/INDEX/"><span class="badge badge-cfg-mds-client">mds-client</span></a></td><td>کلاینت CephFS / FUSE</td><td><a href="mds-client/INDEX/">فهرست</a></td></tr>
<tr class="row-rgw"><td><a href="rgw/INDEX/"><span class="badge badge-cfg-rgw">rgw</span></a></td><td>RADOS Gateway — S3، چندسایته، رمزنگاری</td><td><a href="rgw/INDEX/">فهرست</a></td></tr>
<tr class="row-rbd"><td><a href="rbd/INDEX/"><span class="badge badge-cfg-rbd">rbd</span></a></td><td>RADOS Block Device — image، cache، feature</td><td><a href="rbd/INDEX/">فهرست</a></td></tr>
<tr class="row-rbd-mirror"><td><a href="rbd-mirror/INDEX/"><span class="badge badge-cfg-rbd-mirror">rbd-mirror</span></a></td><td>mirroring ناهمزمان RBD</td><td><a href="rbd-mirror/INDEX/">فهرست</a></td></tr>
<tr class="row-cephfs-mirror"><td><a href="cephfs-mirror/INDEX/"><span class="badge badge-cfg-cephfs-mirror">cephfs-mirror</span></a></td><td>mirroring CephFS</td><td><a href="cephfs-mirror/INDEX/">فهرست</a></td></tr>
<tr class="row-crimson"><td><a href="crimson/INDEX/"><span class="badge badge-cfg-crimson">crimson</span></a></td><td>Crimson OSD / Seastore (آزمایشی)</td><td><a href="crimson/INDEX/">فهرست</a></td></tr>
<tr class="row-immutable"><td><a href="immutable-object-cache/INDEX/"><span class="badge badge-cfg-immutable">immutable-object-cache</span></a></td><td>کش شیء immutable</td><td><a href="immutable-object-cache/INDEX/">فهرست</a></td></tr>
<tr class="row-exporter"><td><a href="ceph-exporter/INDEX/"><span class="badge badge-cfg-exporter">ceph-exporter</span></a></td><td>متریک Prometheus ceph-exporter</td><td><a href="ceph-exporter/INDEX/">فهرست</a></td></tr>
</tbody>
</table>

## جستجو

از ریشهٔ مخزن:

```bash
./scripts/search-config.sh <option-or-keyword>
./scripts/search-config.sh -s osd scrub
```

## فهرست master کامل

generator همچنین `config/readme.md` (فهرست بین‌زیرسیستمی برای اسکریپت‌ها) می‌نویسد.
گزینه‌ها را از فهرست‌های بالا مرور کنید، یا پس از ویرایش `readme.md` دستور `python3 scripts/split-index.py` را اجرا کنید.

[← Cheatsheet](../index.md)
