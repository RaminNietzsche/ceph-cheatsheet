# Ceph 术语表

中文页面请统一使用下列译法。**不要翻译** CLI 命令、config 键名与守护进程标识。

## 核心组件

| English | 中文 |
|---------|------|
| Monitor (MON) | Monitor |
| OSD | 对象存储守护进程 (OSD) |
| MGR | Manager |
| MDS | 元数据服务器 (MDS) |
| RGW | RADOS 网关 (RGW) |
| PG | 放置组 (PG) |
| CRUSH | CRUSH |

## RGW

| English | 中文 |
|---------|------|
| Bucket | bucket |
| Quota | 配额 |
| Realm / zone | realm / zone |
| Multisite | 多站点 |
| SAL | 存储抽象层 (SAL) |

## 翻译规则

1. **正文** — 翻译标题、表头与说明。
2. **代码** — 命令、flag、config 键保持英文。
3. **占位符** — 使用 `<user_id>`、`<bucket_name>`；见 [CLI 风格指南](cli-style-guide.md)。

[← 概览](OVERVIEW.md) · [入门](getting-started.md)
