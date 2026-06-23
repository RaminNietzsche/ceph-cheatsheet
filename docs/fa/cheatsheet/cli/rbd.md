# دستورات RBD

## تصاویر

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

## Snapshot

```bash
rbd snap ls <pool>/<image>
rbd snap create <pool>/<image>@<snap>
rbd snap rm <pool>/<image>@<snap>
rbd snap rename <pool>/<image>@<old> <new>
rbd snap protect <pool>/<image>@<snap>
rbd snap unprotect <pool>/<image>@<snap>
rbd snap purge <pool>/<image>
```

## Map (kernel / nbd)

```bash
rbd map <pool>/<image>             # kernel krbd
rbd showmapped
rbd unmap <pool>/<image>|/dev/rbd*
rbd map <pool>/<image> --device nbd   # nbd
```

## قفل و mirroring

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

## Feature و متادیتا

```bash
rbd feature ls <pool>/<image>
rbd feature enable <pool>/<image> <feature>
rbd feature disable <pool>/<image> <feature>
rbd metadata ls <pool>/<image>
rbd image-meta get/set/rm <pool>/<image> <key> [value]
```

## featureهای رایج تصویر

| Feature | Bit | توضیح |
|---------|-----|-------|
| layering | +1 | clone/snapshot |
| exclusive-lock | +4 | برای live migration لازم |
| object-map | +8 | diff سریع، deep-flatten |
| fast-diff | +16 | diff کارآمد |
| deep-flatten | +32 | flatten cloneها |
| journaling | +64 | RBD mirroring |
| data-pool | +128 | pool داده جدا |

پیش‌فرض featureها: `rbd_default_features` در [config/rbd](../config/rbd/INDEX.md).

[← نمای کلی CLI](OVERVIEW.md)
