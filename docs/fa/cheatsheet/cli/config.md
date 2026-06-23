# دستورات پیکربندی

پیکربندی runtime در پایگاه config مانیتور ذخیره می‌شود. نام گزینه‌ها، پیش‌فرض و پرچم‌ها در [مرجع config](../config/OVERVIEW.md).

## خواندن config

```bash
ceph config show <who>                 # effective config for a daemon
ceph config show-with-defaults <who>
ceph config get <who> <option>
ceph config dump                       # entire config database
ceph config help <option>              # option metadata (if documented)
```

نمونه `<who>`: `global`، `mon`، `osd`، `osd.0`، `mgr`، `mds`، `rgw`، `client.rgw.gateway1`

## تنظیم config

```bash
ceph config set <who> <option> <value>
ceph config rm <who> <option>          # remove override (revert to default)
ceph config assimilate-conf -i ceph.conf   # import ceph.conf into mon store
```

مثال‌ها:

```bash
ceph config set global mon_allow_pool_delete true
ceph config set osd.0 osd_max_scrubs 2
ceph config set mgr debug_mgr 20/5
ceph config set client.rgw.mygw rgw frontends "beast ssl_port=443"
```

## Legacy / injectargs

```bash
ceph tell osd.* injectargs '--debug-osd=10/5'   # temporary (lost on restart)
```

برای تغییرات پایدار `ceph config set` را ترجیح دهید.

## ceph.conf محلی

گزینه‌های bootstrap و محلی فقط در `/etc/ceph/ceph.conf`:

```ini
[global]
    fsid = …
    mon_host = 10.0.0.1,10.0.0.2

[mon]
    mon_allow_pool_delete = false

[osd]
    osd_memory_target = 4294967296
```

برای به‌روزرسانی runtime، پرچم `RUNTIME` را در [جداول config](../config/OVERVIEW.md) ببینید.

## جستجوی محلی گزینه

```bash
./scripts/lookup-config.sh osd_max_scrubs
./scripts/search-config.sh -s osd scrub
```

[← نمای کلی CLI](OVERVIEW.md) · [مرجع Config](../config/OVERVIEW.md)
