# شروع کار

تازه با Ceph آشنا شده‌اید؟ قبل از جدول config یا درون‌ریزی RGW از اینجا شروع کنید.

## Ceph چیست؟

پلتفرم ذخیره‌سازی یکپارچه — RBD (بلوک)، RGW (S3)، CephFS (فایل).

## واژه‌نامه

| اصطلاح | معنی |
|--------|------|
| **MON** | مانیتور — نقشه کلاستر و quorum |
| **OSD** | دیمن ذخیره‌سازی شیء — داده روی دیسک |
| **PG** | گروه placement — واحد recovery |
| **RGW** | دروازه S3/Swift |
| **SAL** | لایه انتزاع store در RGW |

## مسیر یادگیری

| نقش | شروع |
|-----|------|
| اپراتور کلاستر | [شروع سریع](quickstart.md) → [مدیر کلاستر](roles/cluster-admin.md) |
| مدیر RGW | [مدیر RGW](roles/rgw-admin.md) → [معماری RGW](../../arch/rgw/OVERVIEW.md) |
| توسعه‌دهنده | [بخش توسعه](../../dev/index.md) |

## ابزارها

```bash
./scripts/search-all.sh scrub
./scripts/search-fuzzy.sh    # نیاز به fzf
```

[سازگاری نسخه](../../compatibility.md) · [← نمای کلی](OVERVIEW.md)
