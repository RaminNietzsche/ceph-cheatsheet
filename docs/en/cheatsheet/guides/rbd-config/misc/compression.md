# Compression

RBD config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_compression_hint](#rbd_compression_hint) | `none` | Basic | Policy |

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
ceph config get <daemon> <option>  # e.g. rbd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_compression_hint

| | |
|---|---|
| Type | Str · enum: ["none", "compressible", "incompressible"] · default `none` · **Basic** |
| Table | [rbd.md#SP_rbd_compression_hint](../../../config/rbd/rbd.md#SP_rbd_compression_hint) |

**What it does:** Compression hint to send to the OSDs during writes

**When to use:** Core RBD behavior — review before changing in production.

**Example:**

```bash
ceph config set client rbd_compression_hint none
ceph config get client rbd_compression_hint
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `none` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_compression_hint
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
