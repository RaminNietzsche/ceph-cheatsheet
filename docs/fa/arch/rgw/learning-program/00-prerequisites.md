# گام ۰ — پیش‌نیازها

**مدت پیشنهادی:** ۲–۳ روز  
**پیش‌نیاز این گام:** ندارد

## اهداف یادگیری

- [ ] می‌دانی RGW در اکوسیستم Ceph کجا قرار دارد
- [ ] ابزار trace و debug را آماده کرده‌ای
- [ ] مفاهیم S3 و HTTP برای خواندن کد کافی است

## دانش پیش‌نیاز

| موضوع | سطح لازم | منبع پیشنهادی |
|--------|----------|----------------|
| C++11/14/17 | متوسط | virtual، `unique_ptr`، RAII |
| HTTP | پایه | method، header، status code |
| S3 API | پایه | PUT/GET، bucket، key، SigV4 (مفهومی) |
| RADOS | آشنایی | pool، object؛ بدون expert بودن OSD |

## آماده‌سازی محیط

### کد

```bash
# کلون مخزن Ceph (در صورت نداشتن)
# مسیر کد RGW:
# src/rgw/
```

### ابزار

- [ ] IDE با C++ index (clangd / VS Code C++)
- [ ] `rg` یا جستجوی IDE روی `src/rgw/`
- [ ] (اختیاری) cluster dev با `radosgw` و `aws cli`

### Debug

در `ceph.conf` برای نمونه under test:

```ini
debug rgw = 20
```

## تمرین کوتاه

1. لیست ۱۰ فایل `rgw_*.cc` در ریشه `src/rgw/` را ببین — حدس بزن هر کدام چه لایه‌ای است.
2. [نمای کلی سیستم](../architecture/system-overview.md) را یک‌بار بخوان.

## سوالات خودارزیابی

- تفاوت **authentication** و **authorization** چیست؟
- **Bucket** و **Object** در S3 چه رابطه‌ای دارند؟

## چک‌لیست تکمیل گام ۰

- [ ] محیط جستجو در کد آماده است
- [ ] سند system-overview خوانده شد
- [ ] آماده ورود به [فاز ۰ — مسیر درخواست](01-phase-0-request-path.md)

## گام بعدی

→ [01-phase-0-request-path.md](01-phase-0-request-path.md)
