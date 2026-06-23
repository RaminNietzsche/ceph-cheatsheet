# General

MDS client config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mds-client/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [fake_statfs_for_testing](#fake_statfs_for_testing) | `0` | Dev | Dev |

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
ceph config get <daemon> <option>  # e.g. mds-client
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### fake_statfs_for_testing

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [fake.md#SP_fake_statfs_for_testing](../../../config/mds-client/fake.md#SP_fake_statfs_for_testing) |

**What it does:** Set a value for kb and compute kb_used from total of num_bytes

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client fake_statfs_for_testing 64
ceph config get client fake_statfs_for_testing
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
