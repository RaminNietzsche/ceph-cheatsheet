# راهنمای عیب‌یابی

تشخیص ساخت‌یافته مشکلات رایج. مرجع سریع دستور: [CLI troubleshooting](../cli/troubleshooting.md).

## PG گیر کرده / recovery

```bash
ceph pg stat
ceph pg dump_stuck inactive
ceph osd blocked-by
```

## OSD flapping

بررسی دیسک، شبکه، `osd_heartbeat_grace`.

## RGW

- **503/SlowDown** — rate limit / dmclock
- **sync lag** — `radosgw-admin sync status`

## quorum مانیتور

```bash
ceph mon stat
ceph quorum_status --format json-pretty
```

[← نمای کلی](OVERVIEW.md)
