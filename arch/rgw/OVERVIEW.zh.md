# Ceph RADOS Gateway — 技术文档

面向开发者的文档 for the Ceph **RADOS Gateway (RGW)**. It explains architecture, request flow, storage layers, and code landmarks **without browsing the entire upstream tree**.

## 范围

| 包含 | 不包含 |
|----------|--------------|
| Runtime architecture and topology | Git workflow and branching |
| `src/rgw/` modules | CI/CD pipelines |
| Live code references (GitHub links) | Changing service behavior from this repo |

## 结构

- **Learning program** — step-by-step path into the code ([start here](learning-program/index.md))
- **Architecture** — system overview, pipelines, HA limits
- **Modules** — core packages (request path, SAL, RADOS driver, auth, …)
- **Guides** — deployment and doc conventions (upstream `docs-extended`)

## Source tree

Code: [`src/rgw/`](https://github.com/ceph/ceph/tree/main/src/rgw) in [Ceph](https://github.com/ceph/ceph).

Local upstream docs site: `src/rgw/docs-extended/` (MkDocs Material, Persian originals).

## 相关

- [System overview](architecture/system-overview.md)
- [HTTP request pipeline](architecture/request-pipeline.md)
- [Core request path module](modules/core-request-path.md)
