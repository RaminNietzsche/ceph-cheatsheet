# Auth & caps

MON 配置深度指南 — 1 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mon_auth_validate_all_caps](#mon_auth_validate_all_caps) | `True` | Advanced | 策略 |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_auth_validate_all_caps

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_auth_validate_all_caps](../../../config/mon/mon.md#SP_mon_auth_validate_all_caps) |

**作用：** Whether to parse non-monitor capabilities set by the 'ceph auth ...' commands. Disabling this saves CPU on the monitor, but allows invalid capabilities to be set, and only be rejected later, when they are used.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_auth_validate_all_caps false
ceph config get mon mon_auth_validate_all_caps
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_auth_validate_all_caps
ceph -s
ceph mon stat
```

---


[← 概览](../OVERVIEW.md)
