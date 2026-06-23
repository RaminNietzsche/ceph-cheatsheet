# گام ۳ — فاز ۲: REST و پروتکل S3

**مدت پیشنهادی:** ۵–۷ روز  
**پیش‌نیاز:** [فاز ۱](02-phase-1-rgwop-lifecycle.md)

## اهداف

- [ ] ساختار `RGWRESTMgr` و درخت URI را می‌فهمی
- [ ] `RGWHandler_REST::op_get/put/...` را به `RGWOp` وصل می‌کنی
- [ ] `ListBuckets` را end-to-end trace کرده‌ای

## الگوی کد

```text
RGWREST
  └─ RGWRESTMgr (prefix /bucket/...)
       └─ RGWHandler_REST_Obj_S3
            └─ op_get() → RGWGetObj_ObjStore_S3
```

Handler و متدهای HTTP:


> **Source:** [`rgw_rest.h`](https://github.com/ceph/ceph/blob/main/src/rgw/rgw_rest.h#L557-L565)


## فایل‌ها

| فایل | نحوه خواندن |
|------|-------------|
| `rgw_rest.cc` | ثبت managerها |
| `rgw_rest_s3.cc` | **فقط** با search: handler مورد نظر |
| `rgw_rest_s3.h` | اعلان handlerها |
| `rgw_formats.h` | XML/JSON formatter |

## تمرین اصلی — ListBuckets

1. URI: `GET /`
2. جستجو: `RGWListBuckets` یا handler مربوط
3. تا `send_response` و XML

## تمرین — Multipart (شناسایی)

فقط **نام** opها را پیدا کن (اجرا نه):

- `InitMultipart`
- `UploadPart`
- `CompleteMultipart`

## قانون طلایی

!!! warning "فایل بزرگ"
    `rgw_rest_s3.cc` هزاران خط است. **هرگز از خط ۱ شروع نکن.**

## مستندات مکمل

- [protocol-apis](../modules/protocol-apis.md)

## چک‌لیست

- [ ] `RGWREST::get_handler` را خواندم
- [ ] ListBuckets trace شد
- [ ] سه op multipart را نام بردم

## گام بعدی

→ [04-phase-3-auth.md](04-phase-3-auth.md)
