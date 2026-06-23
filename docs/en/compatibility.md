# Ceph version compatibility

This repository tracks **Ceph upstream `main`** by default (see [VERSION](../VERSION) and [version page](version.md)).

## Supported release lines (reference)

| Release | Codename | Status (2026) | Notes |
|---------|----------|---------------|-------|
| 19.x | Squid | Current stable | Recommended for new deployments |
| 18.x | Reef | Stable | Widely deployed |
| 17.x | Quincy | Maintenance | Plan upgrades |
| `main` | — | Development | This docs snapshot |

Always run `ceph versions` on your cluster before applying config from this site.

## How options are versioned here

| Source | Version info |
|--------|----------------|
| **Config tables** | Generated from upstream YAML (`scripts/generate-config.py --ref main`). Upstream `introduced`/`deprecated` fields appear when present in YAML. |
| **CLI docs** | Hand-written; verify against your release man pages. |
| **Architecture** | RGW internals from `src/rgw/docs-extended` (main branch). |

## High-risk options (review before change)

These affect production availability or data path — read deep dives before tuning:

| Option | Subsystem | Risk |
|--------|-----------|------|
| `osd_pool_default_size` | global | **Data loss** if lowered below min_size |
| `mon_osd_full_ratio` | mon | Write freeze when exceeded |
| `osd_mclock_profile` | osd | Latency vs recovery trade-off |
| `osd_max_backfills` | osd | Recovery speed vs client I/O |
| `rgw_enable_apis` | rgw | Security exposure |
| `rgw_enable_rate_limit` | rgw | Client throttling / 503 responses |

Enriched options in config deep dives include **when to use** and **finding notes**.

## Regenerate for a specific release

```bash
python3 scripts/generate-config.py --ref reef
python3 scripts/regenerate-docs.py
```

Update `VERSION` ref after regeneration and note the target release in commit message.

## Future work

- Per-option version badges in generated tables (upstream YAML metadata)
- CLI command version matrix
- MkDocs version selector for multiple release branches

[← Home](index.md)
