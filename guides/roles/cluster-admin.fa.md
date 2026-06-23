# مدیر کلاستر

<span class="badge badge-role-cluster">مدیر کلاستر</span> — مدیریت مانیتور، مدیر (MGR)، orchestration، سلامت کلاستر، احراز هویت و ارتقا.

## دستورات روزانه

```bash
ceph -s
ceph health detail
ceph versions
ceph orch ps                    # cephadm
ceph mon stat
ceph mgr stat
```

[CLI کلاستر](../../cli/cluster.md) · [CLI cephadm](../../cli/cephadm.md)

## پیکربندی

| کار | دستور / config |
|------|----------------|
| پیکربندی runtime | [cli/config.md](../../cli/config.md) — `ceph config set …` |
| گزینه‌های MON | [config/mon/INDEX.md](../../config/mon/INDEX.md) · [راهنمای عمیق MON](../mon-config/OVERVIEW.md) |
| Manager / ماژول‌ها | [config/mgr/INDEX.md](../../config/mgr/INDEX.md) · [راهنمای عمیق MGR](../mgr-config/OVERVIEW.md) |
| Auth و کلیدها | [config/global/auth.md](../../config/global/auth.md) · [راهنمای عمیق Global](../global-config/OVERVIEW.md) |
| مسیر cephadm | `cephadm_path` در [config/mgr/cephadm.md](../../config/mgr/cephadm.md) |

گزینه‌های پرکاربرد: `mon_osd_down_out_interval`، `mgr_standby_modules`، `cephadm_path` — [MON](../mon-config/TUNING.md) و [MGR](../mgr-config/TUNING.md).

## روندهای کاری رایج

**استقرار سرویس (cephadm):**

```bash
ceph orch apply mon --placement="3"
ceph orch apply mgr --placement="2"
ceph orch apply osd --all-available-devices
```

**ارتقای کلاستر:**

```bash
ceph orch upgrade ls
ceph orch upgrade start --image quay.io/ceph/ceph:v19
ceph orch upgrade status
```

**افزودن میزبان / مانیتور:**

```bash
ceph orch host add newhost --labels _admin
ceph orch apply mon --placement="host1 host2 host3"
```

## یادداشت مقیاس

| مقیاس | تمرکز |
|-------|--------|
| [Lab](../scales/lab.md) | یک mon، `--single-host-defaults` |
| [محیط عملیاتی کوچک](../scales/small-production.md) | ۳ mon، ۲ mgr، یک DC |
| [محیط عملیاتی بزرگ](../scales/large-production.md) | stretch، شبکه جدا |
| [Multisite](../scales/multisite.md) | quorum هر سایت یا stretch |

## عیب‌یابی

[cli/troubleshooting.md](../../cli/troubleshooting.md)

[← نمای کلی راهنما](../OVERVIEW.md)
