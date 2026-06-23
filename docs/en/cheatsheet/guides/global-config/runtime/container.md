# Container

Global config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [container_image](#container_image) | `docker.io/ceph/daemon-base:latest-master-devel` | Basic | Policy |

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, compatibility, operational defaults |
| **Capacity** | Disk layout, paths, sizing |
| **Performance** | Baseline → incremental change → monitor cluster |
| **Connectivity** | Nearest stable external endpoint |
| **Dev** | Keep upstream default in production |

**Shared tooling:**

```bash
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### container_image

| | |
|---|---|
| Type | Str · default `docker.io/ceph/daemon-base:latest-master-devel` · **Basic** · **STARTUP** (restart required) |
| Table | [container.md#SP_container_image](../../../config/global/container.md#SP_container_image) |

**What it does:** Container image for core daemons, used by the cephadm orchestrator

**When to use:** Core Global behavior — review before changing in production.

**Example:**

```bash
ceph config set global container_image "docker.io/ceph/daemon-base:latest-master-devel"
ceph config get global container_image
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `docker.io/ceph/daemon-base:latest-master-devel` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global container_image
ceph -s
```

---


[← Overview](../OVERVIEW.md)
