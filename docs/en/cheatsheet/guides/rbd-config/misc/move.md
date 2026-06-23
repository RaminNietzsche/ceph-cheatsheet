# Move

RBD config deep dive — 3 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_move_parent_to_trash_on_remove](#rbd_move_parent_to_trash_on_remove) | `False` | Basic | Policy |
| [rbd_move_to_trash_on_remove](#rbd_move_to_trash_on_remove) | `False` | Basic | Policy |
| [rbd_move_to_trash_on_remove_expire_seconds](#rbd_move_to_trash_on_remove_expire_seconds) | `0` | Basic | Policy |

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

### rbd_move_parent_to_trash_on_remove

| | |
|---|---|
| Type | Bool · default `False` · **Basic** |
| Table | [rbd.md#SP_rbd_move_parent_to_trash_on_remove](../../../config/rbd/rbd.md#SP_rbd_move_parent_to_trash_on_remove) |

**What it does:** move parent with clone format v2 children to the trash when deleted

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client rbd_move_parent_to_trash_on_remove true
ceph config get client rbd_move_parent_to_trash_on_remove
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_move_parent_to_trash_on_remove
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_move_to_trash_on_remove

| | |
|---|---|
| Type | Bool · default `False` · **Basic** |
| Table | [rbd.md#SP_rbd_move_to_trash_on_remove](../../../config/rbd/rbd.md#SP_rbd_move_to_trash_on_remove) |

**What it does:** automatically move images to the trash when deleted

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client rbd_move_to_trash_on_remove true
ceph config get client rbd_move_to_trash_on_remove
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_move_to_trash_on_remove
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_move_to_trash_on_remove_expire_seconds

| | |
|---|---|
| Type | Uint · default `0` · **Basic** |
| Table | [rbd.md#SP_rbd_move_to_trash_on_remove_expire_seconds](../../../config/rbd/rbd.md#SP_rbd_move_to_trash_on_remove_expire_seconds) |

**What it does:** default number of seconds to protect deleted images in the trash

**When to use:** Core RBD behavior — review before changing in production.

**Example:**

```bash
ceph config set client rbd_move_to_trash_on_remove_expire_seconds 64
ceph config get client rbd_move_to_trash_on_remove_expire_seconds
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `0` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_move_to_trash_on_remove_expire_seconds
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
