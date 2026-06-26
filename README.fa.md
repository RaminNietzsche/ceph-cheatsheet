# ceph-cheatsheet

**زبان‌ها:** [English](README.md) · فارسی · [中文](README.zh.md)

**مرجع آفلاین ساده و کامل** برای Ceph — بر اساس **نقش**، **مقیاس**، CLI و پیکربندی.

**انتشار:** [v2026.06.2](https://github.com/RaminNietzsche/ceph-cheatsheet/releases/tag/v2026.06.2) · **سایت:** [blog.ceph-s3.ir](https://blog.ceph-s3.ir/)

→ **[باز کردن مرجع](docs/en/cheatsheet/OVERVIEW.md)** · **[شروع کار](docs/en/cheatsheet/guides/getting-started.md)**

| لایه | محتوا |
|------|--------|
| [شروع کار](docs/en/cheatsheet/guides/getting-started.md) | واژه‌نامه، مسیر یادگیری، ابزارها |
| [نقش‌ها](docs/en/cheatsheet/guides/OVERVIEW.md#by-role) | مدیر کلاستر، اپراتور ذخیره‌سازی، RGW، CephFS |
| [مقیاس‌ها](docs/en/cheatsheet/guides/OVERVIEW.md#by-scale) | آزمایشگاه، تولید کوچک/بزرگ، چندسایتی |
| [نمونه پیکربندی](docs/en/cheatsheet/config/examples/OVERVIEW.md) | قطعات ceph.conf تولیدی |
| [عیب‌یابی](docs/en/cheatsheet/guides/troubleshooting-guide.md) | PG، OSD، RGW، MON، کارایی |
| [CLI](docs/en/cheatsheet/cli/OVERVIEW.md) | `ceph`، `rbd`، `rados`، `radosgw-admin`، `cephadm` |
| [پیکربندی](docs/en/cheatsheet/config/OVERVIEW.md) | **2122** گزینه از YAML upstream Ceph |
| [معماری](docs/en/arch/rgw/OVERVIEW.md) | مستندات عمیق RGW (docs-extended) |

**آنلاین:** [blog.ceph-s3.ir/cheatsheet](http://blog.ceph-s3.ir/cheatsheet/)

## ابزارهای سریع

```bash
./scripts/lookup-config.sh osd_max_scrubs
./scripts/search-all.sh scrub
./scripts/search-fuzzy.sh          # تعاملی (نیاز به fzf)
```

## برای مشارکت‌کنندگان / agentها

- قوانین: `.cursor/rules/` · چیدمان: `scripts/LAYOUT.md`
- Skill: `.cursor/skills/ceph-cheatsheet/SKILL.md` · [reference](.cursor/skills/ceph-cheatsheet/reference.md)
- [راهنمای مشارکت](docs/en/cheatsheet/guides/contributing.md)
- [AGENTS.md](AGENTS.md)

## بازتولید config و مستندات (en + fa + zh)

```bash
pip install -r scripts/requirements.txt
make help          # فهرست targetها
make all           # وابستگی‌ها + config upstream + build کامل
make serve         # سرور dev با mkdocs
```

یا گام‌به‌گام:

```bash
make setup
python3 scripts/generate-config.py --ref main   # یا: make config
make docs                                       # pipeline کامل + build
make serve-site                                 # پیش‌نمایش layout تولید
```

جزئیات اسکریپت‌ها: [`scripts/README.md`](scripts/README.md)

سایت از **mkdocs-static-i18n** استفاده می‌کند: انگلیسی (`.md`)، فارسی (`.fa.md`، RTL)، چینی (`.zh.md`). generatorها و `sync-i18n-*.py` هر سه را همگام نگه می‌دارند.

## مجوز

GPL-3.0 — [LICENSE](LICENSE).
