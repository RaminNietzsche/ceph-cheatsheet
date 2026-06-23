# رصدپذیری (Observability)

## لاگ‌ها

| نوع | محل / مکانیزم |
|-----|----------------|
| daemon log | `dout` با `ceph_subsys_rgw` |
| ops log | `rgw_log` — درخواست‌های S3/Swift |
| bucket logging | `rgw_bucket_logging` — تحویل به bucket هدف |

## متریک‌ها

`rgw_perf_counters` شمارنده‌هایی مانند:

- `l_rgw_req` — تعداد درخواست
- `l_rgw_qlen` / `l_rgw_qactive` — صف پردازش

متریک‌ها در اکوسیستم Ceph (mgr/prometheus) قابل export هستند.

## tracing

`rgw_tracer` spanهایی برای `verify_permission` و `execute` در `process_request` اضافه می‌کند (`TRANS_ID`, `USER_ID`, …).

## سلامت

`RGW_OP_GET_HEALTH_CHECK` برای probe بدون بار سنگین.

## Lua و OPA

- Lua: لاگ warning در شکست اسکریپت pre/post
- OPA: `rgw_use_opa_authz` برای مجوز خارجی

## هشدارهای عملیاتی پیشنهادی

- افزایش پایدار `l_rgw_qlen`
- نرخ بالای `ERR_RATE_LIMITED`
- lag همگام‌سازی multisite
- شکست GC یا resharding در لاگ driver

## مستندات مرتبط

- [تحلیل کیفیت کد](../analysis/code-quality-and-security.md)
- [شکاف‌های HA](critical-gaps-and-ha-limitations.md)
