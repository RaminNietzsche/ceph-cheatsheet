> **说明：** 下表中的选项说明来自 upstream Ceph（英文）。

# RBD Commands

## Images

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

## Snapshots

```bash
rbd snap ls <pool>/<image>
rbd snap create <pool>/<image>@<snap>
rbd snap rm <pool>/<image>@<snap>
rbd snap rename <pool>/<image>@<old> <new>
rbd snap protect <pool>/<image>@<snap>
rbd snap unprotect <pool>/<image>@<snap>
rbd snap purge <pool>/<image>
```

## Mapping (kernel / nbd)

```bash
rbd map <pool>/<image>             # kernel krbd
rbd showmapped
rbd unmap <pool>/<image>|/dev/rbd*
rbd map <pool>/<image> --device nbd   # nbd
```

## Locking & mirroring

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

## Features & metadata

```bash
rbd feature ls <pool>/<image>
rbd feature enable <pool>/<image> <feature>
rbd feature disable <pool>/<image> <feature>
rbd metadata ls <pool>/<image>
rbd image-meta get/set/rm <pool>/<image> <key> [value]
```

## Common image features

| Feature | Bit | Notes |
|---------|-----|-------|
| layering | +1 | clones/snapshots |
| exclusive-lock | +4 | required for live migration |
| object-map | +8 | fast diff, deep-flatten |
| fast-diff | +16 | efficient diff |
| deep-flatten | +32 | flatten clones |
| journaling | +64 | RBD mirroring |
| data-pool | +128 | separate data pool |

Default features: see `rbd_default_features` in [config/rbd](../config/rbd/INDEX.md).

[← CLI overview](OVERVIEW.md)
