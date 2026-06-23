# ارجاع زنده به کد منبع

## pymdownx.snippets

`base_path` در `mkdocs.yml`:

- `pages` → `docs-extended/pages/`
- `.` → `docs-extended/`
- `..` → `src/rgw/` (ریشه snippet)

## قالب snippet

```markdown
```cpp linenums="278" title="rgw_process.cc"
[`rgw_process.cc`](https://github.com/ceph/ceph/blob/main/src/rgw/rgw_process.cc#L278-L325)
```
```

پس از تغییر کد، **خطوط را به‌روز کنید** یا از `make generate` برای appendix استفاده کنید.

## لینک GitHub

[process_request](https://github.com/ceph/ceph/blob/main/src/rgw/rgw_process.cc#L278-L325)

## classDiagram امن

از fence معمولی Mermaid استفاده کنید — hook آن را به `<div data-mermaid-source="...">` تبدیل می‌کند.

**قوانین:**

- بدون `<<interface>>` در body HTML
- بدون کاما در امضای متد داخل کلاس (`+run()` نه `+run(a, b)`)
- همه کلاس‌های رابطه باید `class Name` داشته باشند

## appendix خودکار

`scripts/generate_code_appendix.py` تولید:

- `appendix/generated/symbol-index.md`
- `appendix/generated/import-graph.md`
- `appendix/generated/modules/<file>.md`

پوشه `appendix/generated/` در gitignore است — هر `make build` بازتولید می‌کند.

## پیوست نمادها

[symbol-index](https://github.com/ceph/ceph/tree/main/src/rgw/docs-extended/pages/appendix/generated/symbol-index.md)
