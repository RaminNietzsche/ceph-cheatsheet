# گام ۸ — فاز ۷: Multisite

**مدت پیشنهادی:** ۵–۷ روز  
**پیش‌نیاز:** [فاز ۵](06-phase-5-rados-services.md) (حداقل)

## اهداف

- [ ] Realm / Zonegroup / Zone / Period را تعریف می‌کنی
- [ ] تفاوت metadata sync و data sync را می‌دانی
- [ ] `RGWRESTConn` برای چه استفاده می‌شود

## مفاهیم

| مفهوم | فایل |
|--------|------|
| Zone | `rgw_zone.h` |
| Period | `rgw_period.cc` |
| Realm | `rgw_realm.cc` |
| Sync | `rgw_sync.cc`, `driver/rados/rgw_data_sync.*` |
| HTTP بین زون | `rgw_rest_conn.h` |

## تمرین

```bash
radosgw-admin zone list
radosgw-admin sync status
```

نگاشت خروجی به `RGWSI_Zone`.

## مستندات مکمل

- [multisite](../modules/multisite.md)
- [critical-gaps HA](../architecture/critical-gaps-and-ha-limitations.md)

## چک‌لیست

- [ ] diagram دو zone با پیکان sync کشیدم
- [ ] mdlog vs datalog را یک جمله توضیح دادم

## گام بعدی

→ [09-phase-8-subsystems.md](09-phase-8-subsystems.md)
