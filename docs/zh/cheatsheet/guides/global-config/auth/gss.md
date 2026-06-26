# Gss

Global 配置深度指南 — 2 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [gss_ktab_client_file](#gss_ktab_client_file) | `/var/lib/ceph/$name/gss_client_$name.ktab` | Advanced | 容量 |
| [gss_target_name](#gss_target_name) | `ceph` | Advanced | 性能 |

## 寻找最优值

| 模型 | 如何选择 |
|-------|---------------|
| **策略** | 安全、兼容性、运维默认值 |
| **容量** | 磁盘布局、路径、容量规划 |
| **性能** | 基线 → 逐步调整 → 监控集群 |
| **连通性** | 最近且稳定的外部端点 |
| **开发** | 生产环境保持 upstream 默认值 |

**常用工具：**

```bash
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### gss_ktab_client_file

| | |
|---|---|
| 类型 | Str · default `/var/lib/ceph/$name/gss_client_$name.ktab` · **Advanced** |
| 表格 | [gss.md#SP_gss_ktab_client_file](../../../config/global/gss.md#SP_gss_ktab_client_file) |

**作用：** GSS/KRB5 Keytab file for client authentication This sets the full path for the GSS/Kerberos client keytab file location.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global gss_ktab_client_file "/var/lib/ceph/$name/gss_client_$name.ktab"
ceph config get global gss_ktab_client_file
```

**寻找最优值：**

**调优模型：** 容量

1. 以 `/var/lib/ceph/$name/gss_client_$name.ktab` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global gss_ktab_client_file
ceph -s
```

---

### gss_target_name

| | |
|---|---|
| 类型 | Str · default `ceph` · **Advanced** |
| 表格 | [gss.md#SP_gss_target_name](../../../config/global/gss.md#SP_gss_target_name) |

**作用：** This sets the GSS target service name.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global gss_target_name ceph
ceph config get global gss_target_name
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `ceph` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global gss_target_name
ceph -s
```

---


[← 概览](../OVERVIEW.md)
