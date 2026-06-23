# RBD 命令

## 镜像

```bash
rbd ls [-p pool]
rbd ls -l [-p pool]                # long format with size/features
rbd info <pool>/<image>
rbd create <pool>/<image> --size <bytes> [--image-feature layering,…]
rbd rm <pool>/<image>
rbd rename <src> <dest>
rbd resize <pool>/<image> --size <bytes> [--allow-shrink]
rbd clone <parent-pool>/<parent>@<snap> <child-pool>/<child>
rbd flatten <pool>/<image>
rbd copy <src-pool>/<src> <dest-pool>/<dest>
rbd import <file> <pool>/<image>
rbd export <pool>/<image> <file>
rbd diff <pool>/<image> [--from-snap snap]
rbd du [-p pool]
```

## 快照

```bash
rbd snap ls <pool>/<image>
rbd snap create <pool>/<image>@<snap>
rbd snap rm <pool>/<image>@<snap>
rbd snap rename <pool>/<image>@<old> <new>
rbd snap protect <pool>/<image>@<snap>
rbd snap unprotect <pool>/<image>@<snap>
rbd snap purge <pool>/<image>
```

## 映射（kernel / nbd）

```bash
rbd map <pool>/<image>             # kernel krbd
rbd showmapped
rbd unmap <pool>/<image>|/dev/rbd*
rbd map <pool>/<image> --device nbd   # nbd
```

## 锁定与镜像

```bash
rbd lock ls <pool>/<image>
rbd lock rm <pool>/<image> <cookie> <entity>
rbd mirror pool enable <pool> <mode>   # image or pool mode
rbd mirror pool disable <pool>
rbd mirror pool status <pool>
rbd mirror image enable <pool>/<image>
rbd mirror image status <pool>/<image>
rbd mirror image resync <pool>/<image>
rbd mirror image promote <pool>/<image> [--force]
rbd mirror image demote <pool>/<image>
```

## 特性与元数据

```bash
rbd feature ls <pool>/<image>
rbd feature enable <pool>/<image> <feature>
rbd feature disable <pool>/<image> <feature>
rbd metadata ls <pool>/<image>
rbd image-meta get/set/rm <pool>/<image> <key> [value]
```

## 常见镜像特性

| Feature | Bit | 说明 |
|---------|-----|------|
| layering | +1 | 克隆/快照 |
| exclusive-lock | +4 | live migration 所需 |
| object-map | +8 | 快速 diff、deep-flatten |
| fast-diff | +16 | 高效 diff |
| deep-flatten | +32 | 扁平化克隆 |
| journaling | +64 | RBD 镜像 |
| data-pool | +128 | 独立数据池 |

默认特性：见 [config/rbd](../config/rbd/INDEX.md) 中的 `rbd_default_features`。

[← CLI 概览](OVERVIEW.md)
