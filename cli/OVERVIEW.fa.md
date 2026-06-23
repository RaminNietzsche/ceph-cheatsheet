# مرجع دستورات CLI

<span class="badge badge-cli">CLI</span> دستورات ضروری Ceph برای مدیریت روزانهٔ کلاستر. فرض: کلاستر در حال اجرا، دسترسی به `ceph` و credential مناسب (`ceph.conf` / keyring).

<table class="guide-table">
<thead>
<tr><th>بخش</th><th>موضوعات</th></tr>
</thead>
<tbody>
<tr class="row-cluster"><td><span class="badge badge-cli">cluster</span> <a href="cluster/">→</a></td><td>وضعیت، سلامت، مانیتور، نسخه‌ها</td></tr>
<tr class="row-small"><td><span class="badge badge-cli">config</span> <a href="config/">→</a></td><td>پیکربندی runtime (<code>ceph config …</code>)</td></tr>
<tr class="row-storage"><td><span class="badge badge-cli">osd-pool</span> <a href="osd-pool/">→</a></td><td>OSD، pool، placement group</td></tr>
<tr class="row-lab"><td><span class="badge badge-cli">rados</span> <a href="rados/">→</a></td><td>شیء و pool در سطح پایین RADOS</td></tr>
<tr class="row-large"><td><span class="badge badge-cli">rbd</span> <a href="rbd/">→</a></td><td>تصویر بلوکی، snapshot، map</td></tr>
<tr class="row-rgw"><td><span class="badge badge-cli">rgw</span> <a href="rgw/">→</a></td><td>مدیریت S3/Swift، کاربر، bucket</td></tr>
<tr class="row-cephfs"><td><span class="badge badge-cli">cephfs</span> <a href="cephfs/">→</a></td><td>فایل‌سیستم، MDS، mount</td></tr>
<tr class="row-multi"><td><span class="badge badge-cli">cephadm</span> <a href="cephadm/">→</a></td><td>ارکستراتور، سرویس، میزبان</td></tr>
<tr class="row-dev"><td><span class="badge badge-cli">troubleshooting</span> <a href="troubleshooting/">→</a></td><td>log، عملکرد، recovery، رفع مشکلات رایج</td></tr>
</tbody>
</table>

## پرچم‌های سراسری

بیشتر دستورات این‌ها را می‌پذیرند:

```bash
ceph -s                          # short status
ceph -w                          # watch cluster events
ceph --cluster mycluster …       # non-default cluster name
ceph -c /path/ceph.conf …
ceph -k /path/keyring …
ceph -n client.admin …           # explicit entity name
```

## خانوادهٔ دستورات

| باینری | کاربرد |
|--------|---------|
| `ceph` | مدیریت کلاستر — health، config، orch، tell |
| `rados` | I/O مستقیم pool/شیء |
| `rbd` | مدیریت block device |
| `radosgw-admin` | کاربر، bucket و zoneهای RGW |
| `cephadm` | bootstrap و عملیات cephadm روی نود |
| `cephfs` | shell تعاملی CephFS |

## مثال‌های سریع

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

[← Cheatsheet](../cheatsheet/OVERVIEW.md)
