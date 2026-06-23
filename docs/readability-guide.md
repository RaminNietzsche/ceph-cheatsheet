# Readability guide for technical docs

Authoring reference for Ceph Docs Hub — especially Persian (FA) CLI and config pages.

## Typography

- **Measure:** content column `min(800px, 70ch)` — do not span full monitor width.
- **Line height:** English 1.55; Persian 1.8 (more vertical space for Arabic script ascenders).
- **Fonts:** Vazirmatn (FA prose), JetBrains Mono (code).

## Color & contrast

- Avoid pure `#000` / `#FFF` (halation on long reading sessions).
- Body text `#f1f5f9` on `#0f172a`; links `#5eead4`.
- Target WCAG AA minimum (4.5:1); AAA (~7:1) for body where possible.

## Spacing (Gestalt)

- Tight gap between a paragraph and **its** code block (~0.5rem).
- Large gap between sections (~3rem before `h2`).
- Generous margin around `pre` blocks (1.5–2.5rem vertical).

## RTL / LTR

- Inline `code` in Persian: LTR + `unicode-bidi: embed`.
- Code **blocks:** distinct container (dark background, border, optional accent bar).
- See [CLI style guide](cheatsheet/guides/cli-style-guide.md).

## CLI pages checklist

Before merging FA CLI changes:

- [ ] Placeholders use `<angle_brackets>`; flags not translated
- [ ] Section has action badge where applicable
- [ ] Long commands use `\` continuations
- [ ] JSON/output samples in `??? example` blocks
- [ ] Reference table for flag-heavy sections
- [ ] Bold lead terms for scanability
- [ ] Copy button works; copied text is clean LTR

## Navigation

- Sticky ToC on desktop (1220px+) with active heading highlight.
- Long pages: use tables + collapsible output to reduce scroll fatigue.

## Related GitHub issues

Implemented: #18–#31 (CSS/theme/CLI content). Ongoing: #14 (human translation review).
