# گام ۲ — فاز ۱: چرخه عمر RGWOp

**مدت پیشنهادی:** ۴–۶ روز  
**پیش‌نیاز:** [فاز ۰](01-phase-0-request-path.md)

## اهداف

- [ ] متدهای مجازی `RGWOp` و ترتیب فراخوانی را حفظ می‌کنی
- [ ] سه op نمونه (GET, PUT, DELETE) را با هم مقایسه می‌کنی
- [ ] می‌دانی `op_mask` و `get_type()` چه نقشی دارند

## چرخه عمر RGWOp

```text
verify_requester
  → init_processing
  → verify_op_mask
  → verify_permission
  → verify_params
  → pre_exec
  → execute
  → complete → send_response
```

تعریف در `rgw_op.h`:


> **Source:** [`rgw_op.h`](https://github.com/ceph/ceph/blob/main/src/rgw/rgw_op.h#L283-L306)


## فایل‌های این فاز

| فایل | بخش |
|------|-----|
| `rgw_op.h` | کلاس `RGWOp`, `RGWHandler` |
| `rgw_op.cc` | `RGWGetObj`, `RGWPutObj`, `RGWDeleteObj` |
| `rgw_op_type.h` | enum `RGWOpType` |

## تمرین ۱ — جدول مقایسه

| Op | `get_type()` | `op_mask` | body stream؟ |
|----|--------------|-----------|--------------|
| RGWGetObj | | | خروجی |
| RGWPutObj | | | ورودی |
| RGWDeleteObj | | | |

(خودت از کد پر کن.)

## تمرین ۲ — Find References

برای `RGWGetObj::execute` ببین چه filterهایی (`RGWGetObj_Filter`) در مسیر read هستند.

## سوالات

1. `init_processing` چه کاری با quota می‌کند؟
2. `pre_exec` در کدام opها override شده؟
3. تفاوت `name()` و `canonical_name()` برای IAM چیست؟

## مستندات مکمل

- [object-lifecycle](../architecture/object-lifecycle.md)

## چک‌لیست تکمیل

- [ ] چرخه عمر را بدون نگاه کردن به یادداشت تکرار کردم
- [ ] جدول مقایسه سه op پر شده
- [ ] یک `dout` در `verify_permission` یک op گذاشتم (اختیاری)

## گام بعدی

→ [03-phase-2-rest-s3.md](03-phase-2-rest-s3.md)
