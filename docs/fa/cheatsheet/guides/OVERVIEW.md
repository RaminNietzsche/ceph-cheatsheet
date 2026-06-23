# راهنما

مستندات وظیفه‌محور بر اساس **نقش شما** و **اندازهٔ کلاستر**.

## بر اساس نقش {#by-role}

<table class="guide-table">
<thead>
<tr><th>نقش</th><th>مسئولیت شما…</th><th>شروع از اینجا</th></tr>
</thead>
<tbody>
<tr class="row-cluster">
  <td><span class="badge badge-role-cluster">مدیر کلاستر</span> <a href="roles/cluster-admin/">→</a></td>
  <td>Mon، MGR، cephadm، ارتقا، احراز هویت</td>
  <td>سلامت روزانه، orchestrator</td>
</tr>
<tr class="row-storage">
  <td><span class="badge badge-role-storage">مسئول ذخیره‌سازی</span> <a href="roles/storage-operator/">→</a></td>
  <td>OSD، pool، PG، CRUSH، ظرفیت</td>
  <td>عملیات OSD/pool، بازیابی</td>
</tr>
<tr class="row-rgw">
  <td><span class="badge badge-role-rgw">مدیر RGW</span> <a href="roles/rgw-admin/">→</a></td>
  <td>درگاه S3، کاربران، چندسایته</td>
  <td>radosgw-admin، پیکربندی RGW</td>
</tr>
<tr class="row-cephfs">
  <td><span class="badge badge-role-cephfs">مدیر CephFS</span> <a href="roles/cephfs-admin/">→</a></td>
  <td>فایل‌سیستم، MDS، mount</td>
  <td>ceph fs، پیکربندی MDS</td>
</tr>
</tbody>
</table>

## بر اساس مقیاس {#by-scale}

<table class="guide-table">
<thead>
<tr><th>مقیاس</th><th>اندازهٔ معمول</th><th>شروع از اینجا</th></tr>
</thead>
<tbody>
<tr class="row-lab">
  <td><span class="badge badge-scale-lab">آزمایشگاه / توسعه</span> <a href="scales/lab/">→</a></td>
  <td>۱–۳ نود، آزمایش</td>
  <td>راه‌اندازی minimal، تنظیم آزاد</td>
</tr>
<tr class="row-small">
  <td><span class="badge badge-scale-small">محیط عملیاتی کوچک</span> <a href="scales/small-production/">→</a></td>
  <td>۳–۱۲ نود</td>
  <td>Replica 3، autoscale PG</td>
</tr>
<tr class="row-large">
  <td><span class="badge badge-scale-large">محیط عملیاتی بزرگ</span> <a href="scales/large-production/">→</a></td>
  <td>۱۲+ نود، OSD زیاد</td>
  <td>mclock، scrub، ظرفیت</td>
</tr>
<tr class="row-multi">
  <td><span class="badge badge-scale-multi">چندسایته</span> <a href="scales/multisite/">→</a></td>
  <td>چند سایت / منطقه</td>
  <td>zoneهای RGW، mirroring</td>
</tr>
</tbody>
</table>

## عمومی

- [شروع سریع](quickstart.md) — چک‌لیست روزانه (هر نقش)
- [جستجوی پیکربندی](config-lookup.md) — خواندن جداول گزینه‌ها
- **راهنمای عمیق پیکربندی** (MkDocs: راهنما → راهنمای عمیق پیکربندی) — تنظیم و مثال برای هر زیرسیستم:
  RGW · [OSD](osd-config/OVERVIEW.md) · [MON](mon-config/OVERVIEW.md) · [MGR](mgr-config/OVERVIEW.md) · [MDS](mds-config/OVERVIEW.md) · [Global](global-config/OVERVIEW.md)
- [مشارکت](contributing.md) — قوانین، مهارت‌ها، بازتولید

[← Cheatsheet](../index.md)
