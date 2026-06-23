# شکاف‌های بحرانی و محدودیت‌های HA

تحلیل صادقانه برای برنامه‌ریزی ظرفیت و دسترس‌پذیری — **بدون** وابستگی به ابزار issue tracker.

## نقاط تک‌خرابی احتمالی

| مؤلفه | ریسک | توضیح |
|--------|------|-------|
| Ceph MON quorum | بالا | از دست رفتن quorum → کل خوشه |
| Pool پر | بالا | نوشتن متوقف می‌شود |
| Period قدیمی | متوسط | پیکربندی multisite ناسازگار |
| یک zone master | متوسط | برخی عملیات admin به master وابسته‌اند |

## HA در لبه RGW

**ممکن:**

- چند `radosgw` پشت LB
- rolling restart نمونه‌ها

**ممکن نیست / محدود بدون طراحی:**

- state session در حافظه محلی (RGW stateless است؛ خوب)
- تضمین read-your-writes بین زون‌ها بدون sync lag
- HA بدون replication RADOS روی poolها

## گلوگاه‌ها

| گلوگاه | علامت |
|--------|--------|
| Bucket index hotspot | سطل با ترافیک شدید |
| Reshard | تأخیر listing در حین resharding |
| Sync lag | داده قدیمی در zone ثانویه |
| dmclock/ratelimit | 503 SlowDown — [dmclock](dmclock-architecture.md) / [rate limit](rate-limit-architecture.md#_7) |

## FS مشترک

RGW production روی **RADOS** است، نه NFS مشترک برای داده شیء. backend **POSIX** (`driver/posix`) برای استقرار خاص است و محدودیت‌های consistency فایل‌سیستم محلی را دارد.

## شرایط «HA غیرممکن»

1. تک MON یا تک OSD بدون replica کافی
2. تمام RGW در یک zone بدون sync به zone پشتیبان
3. period نامعتبر و reloader شکست‌خورده
4. pool placement اشتباه — داده در یک failure domain

## توصیه‌های طراحی

- حداقل **۳ MON**، replica ≥ ۳ برای poolهای RGW
- ≥ ۲ نمونه `radosgw` در هر site پرترافیک
- مانیتور lag multisite و `l_rgw_qlen`
- تست failover LB قبل از تولید

## مستندات مرتبط

- [استقرار](deployment-architecture.md)
- [Multisite](../modules/multisite.md)
- [تحلیل امنیت](../analysis/code-quality-and-security.md)
