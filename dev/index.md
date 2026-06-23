# Develop

Structured path to **understand and change RGW** — synced from upstream `src/rgw/docs-extended/`.

## Start here

| Topic | Guide |
|-------|--------|
| Learning program | [RGW learning program](../arch/rgw/learning-program/index.md) — phased path through `src/rgw/` |
| Docs-as-code conventions | [Development convention](../arch/rgw/guides/development-convention.md) |
| Deployment (ops) | [Deployment implementation](../arch/rgw/guides/deployment-implementation-guide.md) |
| Code references in docs | [Source code in docs](../arch/rgw/guides/source-code-in-docs.md) |

## Learning program phases
Follow the steps in order (prerequisites → request path → SAL → RADOS → multisite):

- [Prerequisites](../arch/rgw/learning-program/00-prerequisites.md)
- [Phase 0 — Request path](../arch/rgw/learning-program/01-phase-0-request-path.md)
- [Development checklist](../arch/rgw/learning-program/10-development-checklist.md)

Full index: [learning program overview](../arch/rgw/learning-program/index.md)

## Meanwhile

- [Cheatsheet](../cheatsheet/index.md) — operations reference
- [RGW architecture](../arch/rgw/OVERVIEW.md) — subsystem deep dives
- [Contributing](../cheatsheet/guides/contributing.md) — maintaining this repository

## Upstream source

Persian originals live in `dev-code/rgw/docs-extended/` (local clone of `src/rgw/docs-extended` in ceph/ceph). Regenerate with:

```bash
python3 scripts/sync-rgw-from-docs-extended.py
python3 scripts/generate-role-scale-guides.py
```
