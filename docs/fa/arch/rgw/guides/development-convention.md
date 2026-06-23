# قرارداد توسعه و Docs-as-Code

## اصل Docs-as-Code

هر تغییر **رفتاری** در `src/rgw/` باید همراه با به‌روزرسانی مستندات در `docs-extended/` در همان تغییر کد باشد:

| نوع تغییر | سند لازم |
|-----------|----------|
| مسیر درخواست جدید | `architecture/request-pipeline.md` یا `sequence-diagrams.md` |
| API S3 جدید | `modules/protocol-apis.md` |
| SAL / driver | `modules/sal-layer.md` یا `rados-driver.md` |
| multisite | `modules/multisite.md` |

## کار محلی (بدون CI اجباری)

```bash
cd src/rgw/docs-extended
make install
make generate   # appendix
make check      # build --strict
```

## Definition of Done (مستندات)

- [ ] سند معماری/ماژول به‌روز
- [ ] snippet با شماره خط صحیح (`--8<--`)
- [ ] صفحه جدید در `mkdocs.yml` → `nav`
- [ ] `make check` سبز
- [ ] appendix بازتولید شده

## نام‌گذاری

- متن راهنما: **فارسی**
- شناسه‌های کد، API، config key: **انگلیسی** (`process_request`, `rgw_enable_apis`)

## آنچه عمداً خارج است

- قالب GitLab MR
- pipeline CI
- pre-commit سازمانی

تیم می‌تواند این ابزارها را جداگانه اضافه کند؛ این مخزن مستندات مستقل است.

## ارجاع کد

[source-code-in-docs.md](source-code-in-docs.md)
