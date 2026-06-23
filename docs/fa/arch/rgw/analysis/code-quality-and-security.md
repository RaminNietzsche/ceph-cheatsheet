# کیفیت کد و امنیت (مرور استاتیک)

مرور اولیه `src/rgw/` برای راهنمای توسعه — **بدون** خروجی CSV issue tracker.

## روش

- خوانش ساختار لایه‌ها و مسیرهای حساس (auth، HTTP client، sync)
- شناسایی الگوهای پرریسک رایج در gateways
- ارجاع `file:line` برای پیگیری دستی

## یافته‌های با اولویت بالاتر

| اولویت | ناحیه | فایل:خط | توضیح |
|--------|--------|---------|--------|
| P1 | Auth | `rgw_process.cc` ~422 | استثنا `DigestException` → کلید نامعتبر؛ اطمینان از عدم leak اطلاعات در پاسخ |
| P1 | Permission | `rgw_process.cc` ~238-248 | bypass فقط برای `is_admin()` — بررسی هر op جدید |
| P2 | HTTP outbound | `rgw_http_client.cc` | اتصال به endpointهای zone/tier — اعتبارسنجی URL در پیکربندی |
| P2 | Lua | `rgw_lua_request.cc` | اسکریپت کاربر — محدودیت sandbox و timeout |
| P2 | Multisite | `rgw_rest_conn.cc` | TLS verify بین زون‌ها در تولید |
| P3 | Legacy | `rgw_rest.h` ~677 | بلوک `#if 0` — بدهی فنی |

## امنیت

- **امضای S3** — پیاده‌سازی در `rgw_auth_s3.*`؛ clock skew و header canonicalization
- **SSE** — `rgw_crypt.cc`, `rgw_kms.cc` — مدیریت کلید
- **ACL vs IAM** — ترتیب در `verify_permission` باید با AWS semantics هم‌راستا بماند
- **Public access block** — `rgw_public_access.h`

## بدهی فنی

- `RGWObjContext` در SAL marked for removal (`rgw_sal.h` note)
- مسیرهای dual auth (`transform_old_authinfo` در `rgw_process.cc` ~390)
- اندازه `rgw_rest_s3.cc` — نگهداری سخت

## شکاف تست

- driverهای غیر-RADOS (dbstore, posix) پوشش operability محدودتر
- multisite race — تست end-to-end طولانی

## HA / عملیات

جزئیات در [محدودیت‌های HA](../architecture/critical-gaps-and-ha-limitations.md).

## به‌روزرسانی

پس از تغییرات امنیتی در کد، این جدول و سند معماری مرتبط را به‌روز کنید (`guides/development-convention.md`).
