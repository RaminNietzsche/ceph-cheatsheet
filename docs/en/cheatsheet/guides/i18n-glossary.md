# Ceph terminology glossary (en / fa / zh)

Use these terms consistently across Persian and Chinese pages. **Do not translate** CLI commands, config keys, daemon names, or API identifiers.

## Core daemons & components

| English | Persian (fa) | Chinese (zh) | Notes |
|---------|--------------|--------------|-------|
| Monitor (MON) | مانیتور | Monitor | Keep acronym MON |
| Object Storage Daemon (OSD) | دیمن ذخیره‌سازی شیء (OSD) | 对象存储守护进程 (OSD) | |
| Manager (MGR) | Manager | Manager | Module names stay English |
| Metadata server (MDS) | سرور متادیتا (MDS) | 元数据服务器 (MDS) | |
| RADOS Gateway (RGW) | دروازه RADOS (RGW) | RADOS 网关 (RGW) | |
| Placement group (PG) | گروه placement (PG) | 放置组 (PG) | |
| Pool | pool | 池 | Lowercase in prose when generic |
| CRUSH | CRUSH | CRUSH | Algorithm name — never translate |

## RGW & object storage

| English | Persian (fa) | Chinese (zh) | Notes |
|---------|--------------|--------------|-------|
| Bucket | bucket | bucket | S3 term — keep English |
| User (RGW) | کاربر | 用户 | |
| Access key / secret key | کلید دسترسی / کلید مخفی | 访问密钥 / 秘密密钥 | |
| Quota | سهمیه (quota) | 配额 | |
| Realm | realm | realm | Multisite hierarchy |
| Zone / zonegroup | zone / zonegroup | zone / zonegroup | |
| Period | period | period | RGW multisite epoch |
| Multisite | چندسایته | 多站点 | |
| Sync | همگام‌سازی (sync) | 同步 | |
| Store Abstraction Layer (SAL) | لایه انتزاع store (SAL) | 存储抽象层 (SAL) | `sal::Driver` stays English |
| Garbage collection (GC) | جمع‌آوری زباله (GC) | 垃圾回收 (GC) | |

## Block & file

| English | Persian (fa) | Chinese (zh) | Notes |
|---------|--------------|--------------|-------|
| RBD image | image RBD | RBD 镜像 | |
| Snapshot | snapshot | 快照 | |
| CephFS | CephFS | CephFS | |
| Subvolume | subvolume | 子卷 | |

## Operations

| English | Persian (fa) | Chinese (zh) | Notes |
|---------|--------------|--------------|-------|
| Recovery | recovery | 恢复 | PG state term |
| Backfill | backfill | backfill | |
| Scrub / deep-scrub | scrub / deep-scrub | scrub / deep-scrub | |
| Quorum | quorum | quorum | Monitor term |
| Orchestrator / cephadm | orchestrator / cephadm | 编排器 / cephadm | |

## Config & docs conventions

| English | Persian (fa) | Chinese (zh) | Notes |
|---------|--------------|--------------|-------|
| Runtime config | پیکربندی runtime | 运行时配置 | `ceph config set` |
| Default value | مقدار پیش‌فرض | 默认值 | |
| Override | override | 覆盖 | |
| Deep dive | راهنمای عمیق | 深度指南 | Config guide sections |

## Translation rules

1. **Prose** — translate headings, table labels, and explanations.
2. **Code** — keep commands, flags, JSON keys, and config option names in English.
3. **Placeholders** — use `<angle_brackets>` (`<user_id>`, `<bucket_name>`); see [CLI style guide](cli-style-guide.md).
4. **Mixed RTL** — wrap inline code with bidi-safe markup; see [readability guide](../../readability-guide.md).

Contributors: add new rows here before introducing alternate translations in `.fa.md` / `.zh.md` files.

[← Guides overview](OVERVIEW.md) · [Getting started](getting-started.md)
