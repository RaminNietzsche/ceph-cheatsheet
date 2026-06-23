# ماژول APIهای پروتکل

## REST managers

| API | فایل اصلی | فعال‌سازی |
|-----|-----------|-----------|
| S3 | `rgw_rest_s3.cc` | `rgw_enable_apis` s3 |
| Swift | `rgw_rest_swift.cc` | swift |
| STS | `rgw_rest_sts.cc` | sts |
| IAM | `rgw_rest_iam.cc` | iam |
| Admin | `rgw_rest_admin.h` + driver REST | admin |
| PubSub | `rgw_rest_pubsub.cc` | — |

ثبت در `rgw::AppMain::cond_init_apis()` (`rgw_appmain.cc`).

## الگوی Handler

`RGWHandler_REST` برای هر متد HTTP یک `RGWOp` برمی‌گرداند:


> **Source:** [`rgw_rest.h`](https://github.com/ceph/ceph/blob/main/src/rgw/rgw_rest.h#L557-L565)


[GitHub](https://github.com/ceph/ceph/blob/main/src/rgw/rgw_rest.h#L557-L565)

## `RGWRESTOp`

پاسخ XML/JSON و `send_response()` مشترک:


> **Source:** [`rgw_rest.h`](https://github.com/ceph/ceph/blob/main/src/rgw/rgw_rest.h#L540-L555)


## S3 Website

`rgw_rest_s3website.h` — retarget در `handler->retarget()` برای hosting استاتیک.

## مستندات

- [نمودارهای توالی](../architecture/sequence-diagrams.md)
- [مسیر درخواست](core-request-path.md)
