# گام ۹ — فاز ۸: زیرسیستم‌های موازی (اختیاری)

**مدت:** بر اساس نیاز  
**پیش‌نیاز:** فاز ۱–۵ تکمیل شده باشد

## اهداف

- [ ] می‌دانی هر زیرسیستم در چه فایل‌هایی زندگی می‌کند
- [ ] یک زیرسیستم را عمیق انتخاب و مطالعه کرده‌ای

## نقشه انتخاب موضوع

| اگر علاقه داری به… | شروع کن از |
|---------------------|------------|
| انقضا و tiering | `rgw_lc.h`, `rgw_lc.cc` |
| پاک‌سازی | `driver/rados/rgw_gc.*` |
| event | `rgw_pubsub.*`, `rgw_notify` |
| scripting | `rgw_lua_request.cc` |
| سهمیه | `rgw_quota.cc` |
| Swift | `rgw_rest_swift.cc` |
| Admin CLI | `radosgw-admin/radosgw-admin.cc` |
| resharding | `driver/rados/rgw_reshard.*` |

## روش

1. یک زیرسیستم انتخاب کن.
2. یک عملیات end-to-end (مثلاً یک rule LC) trace کن.
3. مستند [analysis/code-quality](../analysis/code-quality-and-security.md) را برای همان ناحیه بخوان.

## چک‌لیست

- [ ] حداقل یک زیرسیستم را به عمق فاز ۰–۵ مطالعه کردم
- [ ] فایل‌های اصلی آن را در یادداشت لیست کردم

## گام بعدی

→ [10-development-checklist.md](10-development-checklist.md)
