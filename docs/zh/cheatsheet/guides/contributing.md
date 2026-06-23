# 贡献指南

本仓库的结构、维护与扩展方式。

## Cursor 规则

项目规则位于 `.cursor/rules/`：

| 规则 | 适用范围 |
|------|------------|
| `documentation.mdc` | `cli/`、`guides/`、REFERENCE.md |
| `config-generation.mdc` | `config/`、generate 脚本 |
| `no-cursor-coauthor.mdc` | 所有 commit |

所有规则位于仓库根目录 `.cursor/rules/`。

## Cursor 技能

`.cursor/skills/ceph-cheatsheet/SKILL.md` — agent 工作流：重新生成、搜索、mkdocs 与添加内容。

## 内容类型

```
cli/                    手动 — 命令速查
guides/roles/           手动 — 按运维角色
guides/scales/          手动 — 按集群规模
guides/rgw-config/      生成 — 按 nav 分类的 RGW 选项
config/                 生成 — 请勿手改表格
docs/                   MkDocs 外壳 — 从 REFERENCE.md 同步 index
REFERENCE.md            枢纽 — 同步到 docs/index.md
```

## 工作流

**从 upstream Ceph 更新 config：**

```bash
python3 scripts/generate-config.py --ref main
python3 scripts/generate-role-scale-guides.py   # roles + scales (en/fa/zh)
python3 scripts/generate-rgw-guide.py
python3 scripts/generate-config-guide.py all   # OSD, MON, MGR, MDS, global, …
python3 scripts/sync-i18n-config.py            # fa/zh config tables
python3 scripts/sync-i18n-pages.py             # fa/zh hand-written pages
python3 scripts/sync-docs-index.py
```

所有生成器输出 **英文**（`.md`）以及 **波斯语**（`.fa.md`）和 **中文**（`.zh.md`）。模板字符串在 `scripts/locales/strings.yaml`；手写页面翻译在 `scripts/locales/pages/`。

RGW 指南生成器读取 `config/rgw/*.md`，在 `guides/rgw-config/<category>/` 下写入主题文件，并在 `# rgw-nav:start` / `# rgw-nav:end` 之间更新 `mkdocs.yml`。

`generate-config-guide.py` 对其他子系统做同样的事（配置见该脚本；nav 标记 `# osd-nav:start` / … 位于 `mkdocs.yml` 的 `# config-guides-nav:start` 内）。OSD/MON 热点选项的手写说明在 `scripts/subsystem_enrichments.py`。RGW 与 global 扁平指南 URL 通过 `mkdocs-redirects`（由生成器维护）重定向。config 重新生成后请再次运行两个生成器。

**编辑正文（CLI、guides、REFERENCE）：**

1. 编辑文件
2. `python3 scripts/sync-docs-index.py`
3. `mkdocs serve` 预览

**CI：** push 到 `main` → `.github/workflows/docs.yml` 构建并部署 Pages。

## 添加新 CLI 页面

1. 按 documentation 规则创建 `cli/mytopic.md`
2. 从 `cli/OVERVIEW.md`、`REFERENCE.md`、`mkdocs.yml` 链接
3. 从相关角色/规模指南交叉链接

## 添加角色或规模指南

1. 在 `guides/roles/` 或 `guides/scales/` 下创建
2. 更新 `guides/OVERVIEW.md` 与 `REFERENCE.md`
3. 同步 docs index 与 mkdocs nav

[← 指南概览](OVERVIEW.md)
