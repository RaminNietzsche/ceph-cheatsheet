# 集群管理员

<span class="badge badge-role-cluster">集群管理员</span> 管理 Monitor、Manager、编排、集群健康、认证与升级。

## 日常命令

```bash
ceph -s
ceph health detail
ceph versions
ceph orch ps                    # cephadm
ceph mon stat
ceph mgr stat
```

[集群 CLI](../../cli/cluster.md) · [cephadm CLI](../../cli/cephadm.md)

## 配置

| 任务 | 命令 / 配置 |
|------|------------|
| 运行时配置 | [cli/config.md](../../cli/config.md) — `ceph config set …` |
| Monitor 选项 | [config/mon/INDEX.md](../../config/mon/INDEX.md) · [MON 深度指南](../mon-config/OVERVIEW.md) |
| Manager / 模块 | [config/mgr/INDEX.md](../../config/mgr/INDEX.md) · [MGR 深度指南](../mgr-config/OVERVIEW.md) |
| 认证与密钥 | [config/global/auth.md](../../config/global/auth.md) · [Global 深度指南](../global-config/OVERVIEW.md) |
| cephadm 路径 | [config/mgr/cephadm.md](../../config/mgr/cephadm.md) 中的 `cephadm_path` |

常用选项：`mon_osd_down_out_interval`、`mgr_standby_modules`、`cephadm_path` — 见 [MON](../mon-config/TUNING.md) 与 [MGR](../mgr-config/TUNING.md) 调优索引。

## 常见工作流

**部署服务（cephadm）：**

```bash
ceph orch apply mon --placement="3"
ceph orch apply mgr --placement="2"
ceph orch apply osd --all-available-devices
```

**升级集群：**

```bash
ceph orch upgrade ls
ceph orch upgrade start --image quay.io/ceph/ceph:v19
ceph orch upgrade status
```

**添加主机 / Monitor：**

```bash
ceph orch host add newhost --labels _admin
ceph orch apply mon --placement="host1 host2 host3"
```

## 规模说明

| 规模 | 重点 |
|------|------|
| [实验室](../scales/lab.md) | 单 Mon、`--single-host-defaults` |
| [小型生产](../scales/small-production.md) | 3 Mon、2 MGR、单数据中心 |
| [大型生产](../scales/large-production.md) | Stretch、独立网络 |
| [多站点](../scales/multisite.md) | 每站点 quorum 或 stretch |

## 故障排查

[cli/troubleshooting.md](../../cli/troubleshooting.md) — 日志、Monitor quorum、升级停滞

[← 指南概览](../OVERVIEW.md)
