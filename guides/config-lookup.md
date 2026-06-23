# Using the Config Reference

The config section is auto-generated from Ceph upstream YAML. Each option is a row in a Markdown table.

## Finding an option

**By name:**

```bash
./scripts/lookup-config.sh rgw_cache_enabled
```

**By keyword:**

```bash
./scripts/search-config.sh scrub
./scripts/search-config.sh -s osd mclock
```

**Browse:**

1. Open [config/OVERVIEW.md](../config/OVERVIEW.md)
2. Pick a subsystem (e.g. `rgw`)
3. Open `INDEX.md` for a linked list, or open `rgw.md` for the full table

## Reading a table row

Example: `osd_max_scrubs`

| Column | Meaning |
|--------|---------|
| **Name** | Key used with `ceph config set osd osd_max_scrubs 2` |
| **Desc** | Short description |
| **Level** | `Basic` (commonly tuned) · `Advanced` · `Dev` |
| **Type** | `Int`, `Bool`, `Size`, `Str`, … |
| **non-Daemon / Daemon Default** | Default value (may differ for daemons) |
| **Min / Max** | Valid numeric range |
| **Valid Values** | Allowed enum values as JSON array |
| **Flags** | `RUNTIME` = live `ceph config set`; `STARTUP` = needs restart |
| **Services** | Which components consume the option |
| **See also** | Related options (linked) |
| **Long Desc** | Extended explanation |

## Applying changes

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

Only options with the `RUNTIME` flag accept live `ceph config set`. Others require restart or `ceph.conf`.

## Regenerating from upstream

When Ceph releases a new version:

```bash
python3 scripts/generate-config.py --ref reef    # or squid, main, …
```

See [VERSION](../version.md) for the current source ref.

[← Main reference](../index.md)
