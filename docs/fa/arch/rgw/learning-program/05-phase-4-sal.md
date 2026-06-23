# گام ۵ — فاز ۴: Store Abstraction Layer (SAL)

**مدت پیشنهادی:** ۵–۷ روز  
**پیش‌نیاز:** [فاز ۳](04-phase-3-auth.md)

## اهداف

- [ ] نقش `Driver`, `User`, `Bucket`, `Object` را توضیح می‌دهی
- [ ] می‌دانی چرا نباید از `RGWOp` مستقیم `RGWRados` صدا زد
- [ ] `DriverManager` چگونه backend را انتخاب می‌کند

## مستند درون‌کدی SAL


> **Source:** [`rgw_sal.h`](https://github.com/ceph/ceph/blob/main/src/rgw/rgw_sal.h#L98-L126)


## فایل‌ها

| فایل | محتوا |
|------|--------|
| `rgw_sal.h` | API اصلی |
| `rgw_sal.cc` | `DriverManager`, factories |
| `rgw_sal_filter.h` | stack فیلتر (D4N و …) |
| `driver/rados/rgw_sal_rados.h` | `RadosStore` |

## تمرین

1. از `RGWGetObj::execute` تا اولین call روی `s->object` trace کن.
2. امضای `read` روی `sal::Object` را پیدا کن.
3. لیست driverهای compile-time در `rgw_sal.cc` (`newRadosStore`, …).

## قانون توسعه

> feature جدید = متد SAL + پیاده در `RadosStore` + استفاده در `RGWOp`

## مستندات مکمل

- [sal-layer](../modules/sal-layer.md)

## چک‌لیست

- [ ] diagram سه لایه (Op → SAL → RADOS) کشیدم
- [ ] یک call chain read را کامل نوشتم

## گام بعدی

→ [06-phase-5-rados-services.md](06-phase-5-rados-services.md)
