# Ceph RADOS Gateway — technical documentation

Developer documentation for the Ceph **RADOS Gateway (RGW)**. It explains architecture, request flow, storage layers, and code landmarks **without browsing the entire upstream tree**.

## Scope

| In scope | Out of scope |
|----------|--------------|
| Runtime architecture and topology | Git workflow and branching |
| `src/rgw/` modules | CI/CD pipelines |
| Live code references (GitHub links) | Changing service behavior from this repo |

## Structure

- **Learning program** — step-by-step path into the code ([start here](learning-program/index.md))
- **Architecture** — system overview, pipelines, HA limits
- **Modules** — core packages (request path, SAL, RADOS driver, auth, …)
- **Guides** — deployment and doc conventions (upstream `docs-extended`)

## Source tree

Code: [`src/rgw/`](https://github.com/ceph/ceph/tree/main/src/rgw) in [Ceph](https://github.com/ceph/ceph).

Local upstream docs site: `src/rgw/docs-extended/` (MkDocs Material, Persian originals).

## Related

- [System overview](architecture/system-overview.md)
- [HTTP request pipeline](architecture/request-pipeline.md)
- [Core request path module](modules/core-request-path.md)
