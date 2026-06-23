# گام ۱۰ — چک‌لیست توسعه و نگهداری

**نوع:** مرجع دائمی  
**پیش‌نیاز:** حداقل فاز ۰–۴

## قبل از نوشتن کد

- [ ] feature در کدام لایه است؟ (REST / Op / SAL / RADOS / service)
- [ ] آیا API S3 جدید است یا رفتار داخلی؟
- [ ] IAM action و `op_mask` تعریف شده؟
- [ ] مستندات `docs-extended` کدام صفحه نیاز به به‌روزرسانی دارد؟

## الگوی افزودن API S3

```text
1. کلاس RGWOp (+ RGWRESTOp برای پاسخ)
2. RGWHandler_REST_*::op_*()
3. ثبت در RGWRESTMgr
4. verify_permission + IAM
5. متدهای sal:: در صورت نیاز
6. RadosStore + svc_* در صورت نیاز
```

## الگوی تغییر ذخیره‌سازی

```text
1. API در rgw_sal.h
2. پیاده‌سازی RadosStore
3. استفاده از RGWSI_* موجود یا سرویس جدید
4. بدون include مستقیم rgw_rados.h از rgw_rest_s3
```

## Debug

| مشکل | کجا نگاه کنی |
|------|----------------|
| 403 | auth → IAM → ACL |
| 404 | bucket/instance load در SAL |
| 500 بعد از execute | driver / CLS return code |
| کندی | dmclock, ratelimit, index hotspot |

## تست

- [ ] یک درخواست HTTP دستی
- [ ] (در صورت وجود) تست qa در `qa/` مربوط به RGW
- [ ] `make check` در docs-extended اگر doc عوض شد

## بازگشت به برنامه

[فهرست گام‌ها](index.md) · [ردیاب پیشرفت](progress-tracker.md)
