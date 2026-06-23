# مشارکت در مرجع

ساختار، نگهداری و گسترش این مخزن.

## قوانین Cursor

قوانین پروژه در `.cursor/rules/`:

| قانون | محدوده |
|------|------------|
| `documentation.mdc` | `cli/`، `guides/`، REFERENCE.md |
| `config-generation.mdc` | `config/`، اسکریپت‌های generate |
| `no-cursor-coauthor.mdc` | همه commitها |

همه قوانین در `.cursor/rules/` در ریشهٔ مخزن هستند.

## مهارت Cursor

`.cursor/skills/ceph-cheatsheet/SKILL.md` — روند agent برای بازتولید، جستجو، mkdocs و افزودن محتوا.

## انواع محتوا

```
cli/                    دستی — برگهٔ دستورات
guides/roles/           دستی — بر اساس نقش اپراتور
guides/scales/          دستی — بر اساس اندازهٔ کلاستر
guides/rgw-config/      تولیدشده — گزینه‌های RGW بر اساس nav
config/                 تولیدشده — جداول را دستی ویرایش نکنید
docs/                   پوسته MkDocs — sync index از REFERENCE.md
REFERENCE.md            هاب — sync به docs/index.md
```

## روندهای کاری

**به‌روزرسانی config از upstream Ceph:**

```bash
python3 scripts/generate-config.py --ref main
python3 scripts/generate-role-scale-guides.py   # roles + scales (en/fa/zh)
python3 scripts/generate-rgw-guide.py
python3 scripts/generate-config-guide.py all   # OSD, MON, MGR, MDS, global, …
python3 scripts/sync-i18n-config.py            # fa/zh config tables
python3 scripts/sync-i18n-pages.py             # fa/zh hand-written pages
python3 scripts/sync-docs-index.py
```

همه generatorها **انگلیسی** (`.md`) به‌علاوه **فارسی** (`.fa.md`) و **چینی** (`.zh.md`) می‌نویسند. رشته‌های قالب در `scripts/locales/strings.yaml`؛ ترجمهٔ صفحات دستی در `scripts/locales/pages/`.

generator راهنمای RGW از `config/rgw/*.md` می‌خواند، فایل‌های موضوعی زیر `guides/rgw-config/<category>/` می‌نویسد و `mkdocs.yml` را بین `# rgw-nav:start` / `# rgw-nav:end` به‌روز می‌کند.

`generate-config-guide.py` همین کار را برای زیرسیستم‌های دیگر انجام می‌دهد (پروفایل‌ها در همان اسکریپت؛ نشانگرهای nav `# osd-nav:start` / … داخل `# config-guides-nav:start` در `mkdocs.yml`). متن دست‌نویس گزینه‌های پرکاربرد OSD/MON در `scripts/subsystem_enrichments.py` است. URLهای flat راهنمای RGW و global از طریق `mkdocs-redirects` (توسط generatorها) redirect می‌شوند. پس از بازتولید config هر دو generator را دوباره اجرا کنید.

**ویرایش متن (CLI، guides، REFERENCE):**

1. فایل‌ها را ویرایش کنید
2. `python3 scripts/sync-docs-index.py`
3. `mkdocs serve` برای پیش‌نمایش

**CI:** push به `main` → `.github/workflows/docs.yml` build و deploy Pages.

## افزودن صفحه CLI جدید

1. `cli/mytopic.md` طبق قانون documentation بسازید
2. از `cli/OVERVIEW.md`، `REFERENCE.md`، `mkdocs.yml` لینک دهید
3. از راهنمای نقش/مقیاس مرتبط cross-link کنید

## افزودن راهنمای نقش یا مقیاس

1. زیر `guides/roles/` یا `guides/scales/` بسازید
2. `guides/OVERVIEW.md` و `REFERENCE.md` را به‌روز کنید
3. docs index و nav mkdocs را sync کنید

[← نمای کلی راهنما](OVERVIEW.md)
