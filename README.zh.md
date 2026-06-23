# ceph-cheatsheet

**语言：** [English](README.md) · [فارسی](README.fa.md) · 中文

**简洁、完整的离线参考** — 按 **角色**、**规模**、CLI 与配置组织。

**发布：** [v2026.06](https://github.com/RaminNietzsche/ceph-cheatsheet/releases/tag/v2026.06) · **站点：** [blog.ceph-s3.ir](http://blog.ceph-s3.ir/)

→ **[打开参考](docs/en/cheatsheet/OVERVIEW.md)** · **[入门](docs/en/cheatsheet/guides/getting-started.md)**

| 层级 | 内容 |
|------|------|
| [入门](docs/en/cheatsheet/guides/getting-started.md) | 术语表、学习路径、工具 |
| [角色](docs/en/cheatsheet/guides/OVERVIEW.md#by-role) | 集群管理员、存储运维、RGW、CephFS |
| [规模](docs/en/cheatsheet/guides/OVERVIEW.md#by-scale) | 实验环境、小型/大型生产、多站点 |
| [配置示例](docs/en/cheatsheet/config/examples/OVERVIEW.md) | 生产 ceph.conf 片段 |
| [故障排查](docs/en/cheatsheet/guides/troubleshooting-guide.md) | PG、OSD、RGW、MON、性能 |
| [CLI](docs/en/cheatsheet/cli/OVERVIEW.md) | `ceph`、`rbd`、`rados`、`radosgw-admin`、`cephadm` |
| [配置](docs/en/cheatsheet/config/OVERVIEW.md) | 来自 upstream Ceph YAML 的 **2122** 个选项 |
| [架构](docs/en/arch/rgw/OVERVIEW.md) | RGW 深度文档（docs-extended） |

**在线：** [blog.ceph-s3.ir/cheatsheet](http://blog.ceph-s3.ir/cheatsheet/)

## 快捷工具

```bash
./scripts/lookup-config.sh osd_max_scrubs
./scripts/search-all.sh scrub
./scripts/search-fuzzy.sh          # 交互式（需要 fzf）
```

## 贡献者 / Agent

- 规则：`.cursor/rules/` · 布局：`scripts/LAYOUT.md`
- Skill：`.cursor/skills/ceph-cheatsheet/SKILL.md` · [reference](.cursor/skills/ceph-cheatsheet/reference.md)
- [贡献指南](docs/en/cheatsheet/guides/contributing.md)
- [AGENTS.md](AGENTS.md)

## 重新生成配置与文档（en + fa + zh）

```bash
pip install -r scripts/requirements.txt
make help          # 列出所有 target
make all           # 依赖 + upstream config + 完整构建
make serve         # mkdocs 开发服务器
```

或分步执行：

```bash
make setup
python3 scripts/generate-config.py --ref main   # 或：make config
make docs                                       # 完整流水线 + 构建
make serve-site                                 # 预览生产 URL 布局
```

脚本详情：[`scripts/README.md`](scripts/README.md)

站点使用 **mkdocs-static-i18n**：英文（`.md`）、波斯语（`.fa.md`，RTL）、中文（`.zh.md`）。生成器与 `sync-i18n-*.py` 在每次运行时保持三者同步。

## 许可证

GPL-3.0 — 见 [LICENSE](LICENSE).
