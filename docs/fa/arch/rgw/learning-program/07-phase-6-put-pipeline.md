# گام ۷ — فاز ۶: خط لوله نوشتن (PUT)

**مدت پیشنهادی:** ۴–۶ روز  
**پیش‌نیاز:** [فاز ۵](06-phase-5-rados-services.md)

## اهداف

- [ ] زنجیره `DataProcessor` را برای PUT توضیح می‌دهی
- [ ] head object و manifest stripe را می‌شناسی
- [ ] مسیر encryption/compression را در read/write پیدا کرده‌ای

## فایل‌ها

| فایل | نقش |
|------|-----|
| `rgw_putobj.h` | pipeline abstraction |
| `rgw_putobj.cc` | pipes |
| `driver/rados/rgw_putobj_processor.cc` | writer RADOS |
| `rgw_crypt.cc` | SSE |
| `rgw_op.cc` | `RGWPutObj::execute` |

## جریان

```mermaid
flowchart LR
  PUT[RGWPutObj] --> DP[DataProcessor chain]
  DP --> W[RADOS writer]
  W --> IDX[Bucket index]
```

## تمرین

1. PUT ساده بدون encryption — حداقل ۴ مرحله pipeline.
2. PUT با `x-amz-server-side-encryption` — ورود به `rgw_crypt`.
3. مقایسه با GET: فیلترهای symmetric.

## مستندات مکمل

- [object-lifecycle](../architecture/object-lifecycle.md)

## چک‌لیست

- [ ] یک PUT را در لاگ از `executing` تا index دنبال کردم

## گام بعدی

→ [08-phase-7-multisite.md](08-phase-7-multisite.md)
