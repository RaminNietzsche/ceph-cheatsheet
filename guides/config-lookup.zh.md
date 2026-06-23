# 使用配置参考

config 部分由 Ceph upstream YAML 自动生成。每个选项对应 Markdown 表格中的一行。

## 查找选项

**按名称：**

```bash
./scripts/lookup-config.sh rgw_cache_enabled
```

**按关键词：**

```bash
./scripts/search-config.sh scrub
./scripts/search-config.sh -s osd mclock
```

**浏览：**

1. 打开 [config/OVERVIEW.md](../config/OVERVIEW.md)
2. 选择子系统（如 `rgw`）
3. 打开 `INDEX.md` 查看链接列表，或 `rgw.md` 查看完整表格

## 阅读表格行

示例：`osd_max_scrubs`

| 列 | 含义 |
|--------|---------|
| **Name** | 与 `ceph config set osd osd_max_scrubs 2` 配合使用的键 |
| **Desc** | 简短说明 |
| **Level** | `Basic`（常调）· `Advanced` · `Dev` |
| **Type** | `Int`、`Bool`、`Size`、`Str` 等 |
| **non-Daemon / Daemon Default** | 默认值（守护进程可能不同） |
| **Min / Max** | 有效数值范围 |
| **Valid Values** | 允许的枚举值（JSON 数组） |
| **Flags** | `RUNTIME` = 可 `ceph config set` 热更新；`STARTUP` = 需重启 |
| **Services** | 使用该选项的组件 |
| **See also** | 相关选项（链接） |
| **Long Desc** | 详细说明 |

## 应用变更

```bash
# Check current effective value
ceph config get osd.0 osd_max_scrubs

# Set for all OSDs (persistent)
ceph config set osd osd_max_scrubs 2

# Set for one daemon
ceph config set osd.0 osd_max_scrubs 1

# Remove override
ceph config rm osd osd_max_scrubs
```

仅带 `RUNTIME` 标志的选项支持 `ceph config set` 热更新；其余需重启或修改 `ceph.conf`。

## 从 upstream 重新生成

Ceph 新版本发布后：

```bash
python3 scripts/generate-config.py --ref reef    # or squid, main, …
```

当前 ref 见 [VERSION](../version.md)。

[← Cheatsheet](../cheatsheet/OVERVIEW.md)
