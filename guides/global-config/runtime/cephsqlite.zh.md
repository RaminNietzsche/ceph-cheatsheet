# Cephsqlite

Global 配置深度指南 — 3 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [cephsqlite_blocklist_dead_locker](#cephsqlite_blocklist_dead_locker) | `True` | Advanced | Performance |
| [cephsqlite_lock_renewal_interval](#cephsqlite_lock_renewal_interval) | `2000` | Advanced | Performance |
| [cephsqlite_lock_renewal_timeout](#cephsqlite_lock_renewal_timeout) | `30000` | Advanced | Performance |

## 寻找最优值

| 模型 | 如何选择 |
|-------|---------------|
| **Policy** | 安全、兼容性、运维默认值 |
| **Capacity** | 磁盘布局、路径、容量规划 |
| **Performance** | 基线 → 逐步调整 → 监控集群 |
| **Connectivity** | 最近且稳定的外部端点 |
| **Dev** | 生产环境保持 upstream 默认值 |

**常用工具：**

```bash
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### cephsqlite_blocklist_dead_locker

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [cephsqlite.md#SP_cephsqlite_blocklist_dead_locker](../../../config/global/cephsqlite.md#SP_cephsqlite_blocklist_dead_locker) |

**作用：** Blocklist the last dead owner of the database lock

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global cephsqlite_blocklist_dead_locker false
ceph config get global cephsqlite_blocklist_dead_locker
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global cephsqlite_blocklist_dead_locker
ceph -s
```

---

### cephsqlite_lock_renewal_interval

| | |
|---|---|
| 类型 | Millisecs · default `2000` · **Advanced** |
| 表格 | [cephsqlite.md#SP_cephsqlite_lock_renewal_interval](../../../config/global/cephsqlite.md#SP_cephsqlite_lock_renewal_interval) |

**作用：** Number of milliseconds before a cephsqlite lock is renewed

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global cephsqlite_lock_renewal_interval 2000
ceph config get global cephsqlite_lock_renewal_interval
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `100`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global cephsqlite_lock_renewal_interval
ceph -s
```

---

### cephsqlite_lock_renewal_timeout

| | |
|---|---|
| 类型 | Millisecs · default `30000` · **Advanced** |
| 表格 | [cephsqlite.md#SP_cephsqlite_lock_renewal_timeout](../../../config/global/cephsqlite.md#SP_cephsqlite_lock_renewal_timeout) |

**作用：** Number of milliseconds before a libcephsqlite transaction lock times out

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global cephsqlite_lock_renewal_timeout 30000
ceph config get global cephsqlite_lock_renewal_timeout
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `30000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `100`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global cephsqlite_lock_renewal_timeout
ceph -s
```

---


[← 概览](../OVERVIEW.md)
