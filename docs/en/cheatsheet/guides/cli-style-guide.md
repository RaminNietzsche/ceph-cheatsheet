# CLI documentation style guide

Conventions for writing and translating CLI pages (especially RGW / `radosgw-admin`).

## Placeholders (#19)

| Rule | Good | Bad |
| --- | --- | --- |
| Use `<snake_case>` for variables | `--uid=<user_id>` | `--uid=user_id` mixed with Persian |
| Quote display names | `--display-name="<display_name>"` | translated placeholder inside command |
| Keep flags in English | `--bucket=<bucket_name>` | Persian flag names |
| Use `…` for omitted secrets | `--secret-key=…` | fake secrets in docs |

**Never translate** command names, subcommands, or flag names inside code blocks.

## F-pattern scanning (#27)

- Start prose with **action + object**: **Create user:** then the command.
- **Bold** the first keyword in table cells and list items.
- Put the command block directly under its description (Gestalt proximity).

## Tables (#20)

For sections with many flags, add a reference table before the copy-paste block:

| Command / flag | Purpose | Example |

Keep examples LTR inside RTL pages.

## Long output (#21)

Use collapsible admonitions:

```markdown
??? example "Sample JSON output"
    ```json
    { "user_id": "..." }
    ```
```

## Action badges (#23)

Tag section headings:

```html
## Users & keys <span class="badge badge-action-create">Create</span>
```

Classes: `badge-action-create`, `badge-action-delete`, `badge-action-suspend`, `badge-action-read`, `badge-action-quota`, `badge-action-sync`.

## Multi-line commands (#24)

Break at ~80 columns or one flag per line:

```bash
radosgw-admin user create \
  --uid="<user_id>" \
  --display-name="<display_name>"
```

## RTL / FA pages

- Prose: RTL (Persian)
- Commands: LTR blocks with `direction: ltr` (handled by theme CSS)
- Inline `--flags` in sentences: keep LTR; do not embed Persian inside commands

See also: [Readability guide](../../readability-guide.md).
