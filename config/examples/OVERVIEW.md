# Production configuration examples

Commented **ceph.conf** fragments and rationale for common deployment scales. Apply via `ceph config set` (cephadm) or merge into `[global]` / daemon sections.

| Example | Scale | Link |
|---------|-------|------|
| Lab / dev | 1–3 nodes, testing | [lab.md](lab.md) |
| Small production | 3–12 nodes, single DC | [small-production.md](small-production.md) |
| Large production | 12+ nodes, tuned I/O | [large-production.md](large-production.md) |
| Multisite RGW | Multiple zones | [multisite.md](multisite.md) |
| RGW optimized | Object gateway focus | [rgw-optimized.md](rgw-optimized.md) |

Also see role/scale guides: [Guides overview](../../guides/OVERVIEW.md).

[← Config index](../OVERVIEW.md)
