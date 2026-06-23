# راهنمای پیاده‌سازی استقرار

این سند **گام‌های استقرار** را برای اپراتور و توسعه‌دهنده توضیح می‌دهد. شامل pipeline CI/CD نیست.

## پیش‌نیازها

- خوشه Ceph فعال (MON + OSD)
- poolهای placement برای RGW تعریف‌شده
- realm/zonegroup/zone برای multisite (در صورت نیاز)
- گواهی TLS (تولید) یا پروکسی TLS

## حالت توسعه (تک نود)

1. اجرای خوشه dev (cephadm یا ceph-volume)
2. ایجاد کاربر سیستم RGW و keyring
3. `radosgw` با `rgw frontends = beast` و `rgw enable apis = s3`
4. تست با `aws s3 --endpoint-url http://127.0.0.1:7480 ls`

## حالت تولید

1. حداقل دو نمونه `radosgw` در AZهای جدا
2. Load balancer با health check به `GET /health` (در صورت فعال بودن)
3. `rgw dns name` و certificate مطابق endpoint عمومی
4. محدود کردن `rgw enable apis` به APIهای لازم
5. فعال‌سازی ops log و متریک mgr

## وابستگی‌های سرویس

| سرویس | وابسته به |
|--------|-----------|
| radosgw | MON, OSD, poolهای rgw |
| radosgw-admin | همان + دسترسی admin caps |
| multisite sync | دسترسی HTTP بین زون‌ها |

## مقایسه با میکروسرویس کلاسیک

| میکروسرویس | RGW |
|-------------|-----|
| broker پیام | ندارد — HTTP مستقیم |
| DB جدا برای metadata | RADOS + CLS |
| state در سرویس | stateless در لبه |

## عیب‌یابی رایج

- **503 slow down** — dmclock یا ratelimit
- **No such bucket** — zone/tenant یا endpoint اشتباه
- **sync lag** — بررسی `radosgw-admin sync status`

## معماری

- [معماری استقرار](../architecture/deployment-architecture.md)
- [توپولوژی زمان اجرا](../architecture/runtime-topology.md)
