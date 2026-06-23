# شروع سریع — روند کاری روزانهٔ مدیر

حداقل گام‌ها برای بهره‌برداری از کلاستر Ceph. با محیط خود (cephadm یا دستی، نسخهٔ release) تطبیق دهید.

## ۱. بررسی سلامت کلاستر

```bash
ceph -s
ceph health detail
ceph versions
ceph orch ps          # if using cephadm
```

انتظار: `health: HEALTH_OK`، همه OSDها up، quorum سالم.

## ۲. ظرفیت و مصرف

```bash
ceph df
ceph df detail
ceph osd df tree
```

به هشدارهای `nearfull` / `backfillfull` توجه کنید.

## ۳. وضعیت PG

```bash
ceph pg stat
ceph pg dump_stuck
```

همه PGها باید `active+clean` باشند. `degraded`، `recovering`، `backfilling` یا `stuck` را بررسی کنید.

## ۴. تغییرات رایج

```bash
# Set a runtime config option
ceph config set osd osd_max_scrubs 2

# Create an RBD pool
ceph osd pool create rbd 128 128 replicated
ceph osd pool application enable rbd rbd

# Create an RBD image
rbd create rbd/myimage --size 10G

# Mark OSD out for maintenance
ceph osd out 5
# … wait for backfill …
ceph osd in 5
```

## ۵. پیش از ارتقا

```bash
ceph versions                         # mixed versions?
ceph health detail
ceph osd ok-to-stop osd.0 osd.1 …    # check N OSDs at a time
ceph orch upgrade status              # cephadm path
```

## ۶. وقتی مشکلی پیش آمد

1. `ceph health detail` — متن هشدار/خطا را بخوانید
2. `ceph -w` — رویدادهای زنده را ببینید
3. [دستورات عیب‌یابی](../cli/troubleshooting.md)
4. پیکربندی مرتبط: `./scripts/lookup-config.sh <option>`

## برگهٔ تقلب جستجو

```bash
./scripts/lookup-config.sh osd_max_scrubs
./scripts/search-all.sh "full ratio"
./scripts/search-config.sh -s rgw cache
```

## گام بعدی

- [نقش](OVERVIEW.md#by-role) یا [مقیاس](OVERVIEW.md#by-scale) خود را برای روندهای تخصصی‌تر انتخاب کنید.

[← Cheatsheet](../index.md)
