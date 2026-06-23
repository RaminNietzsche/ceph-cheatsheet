#!/usr/bin/env python3
"""Shared engine for per-subsystem config deep-dive guides."""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ROW_RE = re.compile(
    r'^\| <span id="SP_([^"]+)">([^<]+)</span> \|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|'
)
SEE_ALSO_RE = re.compile(r"\[\[([^\]]+)\]\(#SP_([^)]+)\)\]")
INDEX_LINK_RE = re.compile(r"^ - \[([^\]]+)\]\(([^)]+)\)")


@dataclass
class Option:
    name: str
    desc: str
    level: str
    typ: str
    default: str
    daemon_default: str
    min_val: str
    max_val: str
    valid_values: str
    flags: str
    long_desc: str
    see_also_raw: str
    source_file: str

    @property
    def effective_default(self) -> str:
        return self.daemon_default.strip() or self.default.strip() or "(empty)"

    @property
    def full_desc(self) -> str:
        parts = [self.desc.strip(), self.long_desc.strip()]
        return " ".join(p for p in parts if p)


@dataclass
class SubsystemProfile:
    id: str
    title: str
    config_subdir: str
    guides_subdir: str
    group_for: Callable[[str], str]
    group_titles: dict[str, str] = field(default_factory=dict)
    nav_sections: list[tuple[str, str, list[str]]] = field(default_factory=list)
    """(section title, section dir slug, topic slugs)"""
    section_slugs: dict[str, str] = field(default_factory=dict)
    nav_marker: str = ""
    restart_service: str | None = None
    enrichments: dict[str, dict[str, str]] = field(default_factory=dict)

    @property
    def config_dir(self) -> Path:
        return ROOT / "config" / self.config_subdir

    @property
    def guides_dir(self) -> Path:
        return ROOT / "guides" / self.guides_subdir

    @property
    def config_href_from_topic(self) -> str:
        return f"../../../config/{self.config_subdir}"

    @property
    def config_href_from_root(self) -> str:
        return f"../../config/{self.config_subdir}"


def strip_badge(cell: str) -> str:
    m = re.search(r"badge-level-(\w+)", cell)
    if m:
        return m.group(1).capitalize()
    return cell.strip()


def parse_table(path: Path) -> list[Option]:
    opts: list[Option] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        name = m.group(2).strip()
        opts.append(
            Option(
                name=name,
                desc=m.group(3).strip(),
                level=strip_badge(m.group(4)),
                typ=m.group(5).strip(),
                default=m.group(6).strip(),
                daemon_default=m.group(7).strip(),
                min_val=m.group(8).strip(),
                max_val=m.group(9).strip(),
                valid_values=m.group(10).strip(),
                flags=m.group(13).strip(),
                long_desc=m.group(15).strip(),
                see_also_raw=m.group(11).strip(),
                source_file=path.name,
            )
        )
    return opts


def parse_index_order(config_dir: Path) -> list[tuple[str, str]]:
    order: list[tuple[str, str]] = []
    for line in (config_dir / "INDEX.md").read_text(encoding="utf-8").splitlines():
        m = INDEX_LINK_RE.match(line)
        if m:
            order.append((m.group(1), m.group(2)))
    return order


def slug_title(slug: str) -> str:
    return slug.replace("-", " ").title()


def infer_config_target(profile: SubsystemProfile, opt: Option) -> str:
    flags = opt.flags.lower()
    for daemon in ("rgw", "mds", "mgr", "mon", "osd"):
        if re.search(rf"\b{daemon}\b", flags):
            return daemon
    if "client" in flags:
        return "client"
    prefixes = (
        ("osd_", "osd"),
        ("mon_", "mon"),
        ("mgr_", "mgr"),
        ("mds_", "mds"),
        ("rbd_", "client"),
        ("client_", "client"),
        ("fuse_", "client"),
        ("crimson_", "osd"),
        ("seastore_", "osd"),
        ("ceph_exporter_", "mgr"),
    )
    for prefix, target in prefixes:
        if opt.name.startswith(prefix):
            return target
    if profile.id == "global":
        return "global"
    if profile.id in ("mds-client", "rbd", "rbd-mirror"):
        return "client"
    if profile.id == "ceph-exporter":
        return "mgr"
    return profile.id.replace("-", "_")


def when_to_use(opt: Option, profile: SubsystemProfile) -> str:
    name, level, typ = opt.name, opt.level, opt.typ
    if level == "Dev" or "inject" in name or "debug" in name:
        return "Development, testing, or upstream debugging only — not for production tuning."
    if typ == "Bool":
        default = opt.effective_default.lower()
        if default == "true":
            return "Enabled by default; disable only when troubleshooting the related feature."
        return "Disabled by default; enable when you need the feature and accept its trade-offs."
    if name.endswith(("_url", "_uri", "_addr")):
        return "Set when integrating with an external service; leave empty if unused."
    if any(x in name for x in ("max_", "min_", "limit", "cap")):
        return "Adjust when hitting resource limits or protecting cluster capacity."
    if any(x in name for x in ("interval", "sleep", "timeout", "period")):
        return "Tune background work timing — balance freshness vs cluster load."
    if level == "Basic":
        return f"Core {profile.title} behavior — review before changing in production."
    return "Advanced tuning — change from upstream default only with a measured workload and rollback plan."


def tuning_model(opt: Option) -> str:
    name, typ, level = opt.name, opt.typ, opt.level
    if level == "Dev" or "inject" in name:
        return "Dev"
    if name.endswith(("_path", "_dir", "_file", "_base_path")):
        return "Capacity"
    if name.endswith(("_url", "_uri", "_addr")):
        return "Connectivity"
    if typ == "Bool" and any(x in name for x in ("enforce", "allow", "auth", "enable", "disable")):
        return "Policy"
    if any(
        x in name
        for x in (
            "mclock",
            "scrub",
            "recovery",
            "backfill",
            "thread",
            "max_",
            "min_",
            "interval",
            "sleep",
            "cache",
            "queue",
            "throughput",
            "concurrent",
        )
    ):
        return "Performance"
    if level == "Basic":
        return "Policy"
    return "Performance"


def tuning_quick_answer(opt: Option) -> str:
    model = tuning_model(opt)
    if model == "Dev":
        return "Keep upstream default in production"
    if model == "Capacity":
        return "Match filesystem layout and capacity plan"
    if model == "Connectivity":
        return "Use nearest stable endpoint"
    if model == "Policy":
        return "Align with security and compatibility policy"
    if opt.typ == "Bool":
        return "Enable/disable based on measured need"
    if opt.min_val or opt.max_val:
        return "Stay within documented bounds"
    return "Baseline → adjust → validate under load"


def related_options(opt: Option) -> list[str]:
    return [m.group(2) for m in SEE_ALSO_RE.finditer(opt.see_also_raw)]


def quote_config_value(opt: Option, value: str) -> str:
    if opt.typ != "Str":
        return value
    if value.startswith('"') and value.endswith('"'):
        return value
    if any(c in value for c in (' ', '/', '@', ':', '.', '-', '<', '>', '=')):
        return f'"{value}"'
    return value


def example_value(opt: Option) -> str:
    default = opt.effective_default
    if default in ("(empty)", "-1", "0") or not default:
        if opt.typ == "Str":
            if "_path" in opt.name or "_dir" in opt.name:
                return '"/var/lib/ceph/example"'
            if "_url" in opt.name or "_uri" in opt.name:
                return '"https://example.com/"'
            return '"example"'
        if opt.typ in ("Int", "Uint", "Size") and default == "-1":
            return "1024"
    return quote_config_value(opt, default)


def bool_example_value(opt: Option) -> str:
    default = opt.effective_default.lower()
    return "false" if default == "true" else "true"


def numeric_example_value(opt: Option) -> str:
    default = opt.effective_default
    if default == "-1":
        return "128"
    if default == "0":
        return "64"
    return quote_config_value(opt, default)


def render_example(profile: SubsystemProfile, opt: Option) -> str:
    enrich = profile.enrichments.get(opt.name, {})
    if enrich.get("example"):
        return enrich["example"]

    target = infer_config_target(profile, opt)
    restart = ""
    if profile.restart_service and opt.flags and "STARTUP" in opt.flags:
        restart = f"\nceph orch restart {profile.restart_service}"
    if opt.typ == "Bool":
        val = bool_example_value(opt)
    elif opt.typ in ("Int", "Uint", "Size"):
        val = numeric_example_value(opt)
    else:
        val = example_value(opt)
    lines = [
        f"ceph config set {target} {opt.name} {val}",
        f"ceph config get {target} {opt.name}",
    ]
    return "```bash\n" + "\n".join(lines) + restart + "\n```"


def monitor_block(profile: SubsystemProfile, opt: Option) -> str:
    target = infer_config_target(profile, opt)
    lines = [
        "",
        "**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.",
        "",
        "```bash",
        f"ceph config get {target} {opt.name}",
        "ceph -s",
    ]
    if target == "osd":
        lines.append("ceph daemon osd.<id> perf dump | head")
        lines.append("ceph osd pool stats")
    elif target == "mon":
        lines.append("ceph mon stat")
    elif target == "mgr":
        lines.append("ceph mgr dump")
    elif target == "mds":
        lines.append("ceph fs status")
    elif target == "client":
        lines.append("# client options: set on client section or ceph.conf")
    lines.append("```")
    return "\n".join(lines)


def render_finding_optimal_value(profile: SubsystemProfile, opt: Option) -> str:
    model = tuning_model(opt)
    default = opt.effective_default
    lines = [f"**Tuning model:** {model}", ""]

    if model == "Dev":
        lines.extend(
            [
                f"1. Keep the upstream default (`{default}`) in production.",
                "2. Change only in a lab while reproducing a specific issue.",
                "3. Revert before returning the node to the production pool.",
            ]
        )
        return "\n".join(lines)

    if model == "Capacity":
        lines.extend(
            [
                f"1. Baseline at `{default}`.",
                "2. Plan capacity and filesystem layout before changing paths.",
                "3. Ensure all daemons that must share the path see the same mount.",
            ]
        )
        return "\n".join(lines) + monitor_block(profile, opt)

    if model == "Connectivity":
        lines.extend(
            [
                "1. List candidate endpoints from your environment.",
                "2. Verify reachability from every node running the daemon.",
                "3. Pick the lowest-latency stable endpoint.",
                f"4. Leave empty (`{default}`) if the integration is disabled.",
            ]
        )
        return "\n".join(lines) + monitor_block(profile, opt)

    if model == "Policy":
        lines.extend(
            [
                f"1. Document why `{default}` is correct for your policy.",
                "2. Change only for compatibility or security requirements.",
                "3. Test client and admin workflows after changes.",
            ]
        )
        return "\n".join(lines) + monitor_block(profile, opt)

    lines.extend(
        [
            f"1. Baseline at upstream default `{default}`.",
            "2. Change **one** option per test window under representative load.",
            "3. Compare latency, throughput, and background work before/after.",
            "4. Roll back if health degrades or slow ops increase.",
        ]
    )
    if opt.min_val or opt.max_val:
        lines.append(
            f"\n**Bounds:** min `{opt.min_val or '—'}`, max `{opt.max_val or '—'}`."
        )
    return "\n".join(lines) + monitor_block(profile, opt)


def format_see_also(profile: SubsystemProfile, opt: Option) -> str:
    refs = related_options(opt)
    if not refs:
        return ""
    lines = ["**Related options:**", ""]
    for ref in refs:
        lines.append(
            f"- [`{ref}`]({profile.config_href_from_topic}/{opt.source_file}#SP_{ref})"
        )
    lines.append("")
    return "\n".join(lines)


def render_option(profile: SubsystemProfile, opt: Option) -> str:
    enrich = profile.enrichments.get(opt.name, {})
    table_link = f"{profile.config_href_from_topic}/{opt.source_file}#SP_{opt.name}"
    startup = " · **STARTUP** (restart required)" if opt.flags and "STARTUP" in opt.flags else ""
    type_bits = [opt.typ, f"default `{opt.effective_default}`", f"**{opt.level}**"]
    if opt.valid_values:
        type_bits.insert(1, f"enum: {opt.valid_values}")
    parts = [
        f"### {opt.name}",
        "",
        "| | |",
        "|---|---|",
        f"| Type | {' · '.join(type_bits)}{startup} |",
        f"| Table | [{opt.source_file}#SP_{opt.name}]({table_link}) |",
        "",
    ]
    what = enrich.get("what") or opt.full_desc
    if what:
        parts.extend([f"**What it does:** {what}", ""])
    if enrich.get("when_to_use"):
        parts.extend([f"**When to use:** {enrich['when_to_use']}", ""])
    else:
        parts.extend([f"**When to use:** {when_to_use(opt, profile)}", ""])
    see = format_see_also(profile, opt)
    if see:
        parts.append(see)
    parts.extend(
        [
            "**Example:**",
            "",
            render_example(profile, opt),
            "",
            "**Finding optimal value:**",
            "",
            render_finding_optimal_value(profile, opt),
            "",
        ]
    )
    if enrich.get("finding_note"):
        parts.extend([enrich["finding_note"], ""])
    parts.extend(["---", ""])
    return "\n".join(parts)


def tuning_intro(profile: SubsystemProfile) -> str:
    return "\n".join(
        [
            "## Finding optimal values",
            "",
            "| Model | How to choose |",
            "|-------|---------------|",
            "| **Policy** | Security, compatibility, operational defaults |",
            "| **Capacity** | Disk layout, paths, sizing |",
            "| **Performance** | Baseline → incremental change → monitor cluster |",
            "| **Connectivity** | Nearest stable external endpoint |",
            "| **Dev** | Keep upstream default in production |",
            "",
            "**Shared tooling:**",
            "",
            "```bash",
            f"ceph config get <daemon> <option>  # e.g. {profile.id}",
            "ceph -s",
            "./scripts/lookup-config.sh <option-name>",
            "```",
            "",
            "---",
            "",
        ]
    )


def section_dir_for_slug(profile: SubsystemProfile, slug: str) -> str:
    for title, section_dir, slugs in profile.nav_sections:
        if slug in slugs:
            return profile.section_slugs.get(title, section_dir)
    return profile.section_slugs.get("Other", "other")


def topic_path(profile: SubsystemProfile, slug: str) -> Path:
    return profile.guides_dir / section_dir_for_slug(profile, slug) / f"{slug}.md"


def topic_href(profile: SubsystemProfile, slug: str) -> str:
    return f"{section_dir_for_slug(profile, slug)}/{slug}.md"


def group_title(profile: SubsystemProfile, slug: str) -> str:
    return profile.group_titles.get(slug, slug_title(slug))


def render_group(profile: SubsystemProfile, slug: str, options: list[Option]) -> str:
    title = group_title(profile, slug)
    lines = [
        f"# {title}",
        "",
        f"{profile.title} config deep dive — {len(options)} options. "
        f"[← Overview](../OVERVIEW.md) · "
        f"[Tuning index](../TUNING.md) · "
        f"[INDEX]({profile.config_href_from_topic}/INDEX.md)",
        "",
        "| Option | Default | Level | Tuning |",
        "|--------|---------|-------|--------|",
    ]
    for opt in options:
        lines.append(
            f"| [{opt.name}](#{opt.name}) | `{opt.effective_default}` | {opt.level} | "
            f"{tuning_model(opt)} |"
        )
    lines.extend(["", tuning_intro(profile)])
    for opt in options:
        lines.append(render_option(profile, opt))
    lines.extend(["", "[← Overview](../OVERVIEW.md)", ""])
    return "\n".join(lines)


def nav_slugs_in_order(profile: SubsystemProfile, groups: dict[str, list[Option]]) -> list[str]:
    ordered: list[str] = []
    seen: set[str] = set()
    for _title, _dir, slugs in profile.nav_sections:
        for slug in slugs:
            if slug in groups and slug not in seen:
                ordered.append(slug)
                seen.add(slug)
    for slug in sorted(groups):
        if slug not in seen:
            ordered.append(slug)
    return ordered


def section_title_for_slug(profile: SubsystemProfile, slug: str) -> str:
    for title, _dir, slugs in profile.nav_sections:
        if slug in slugs:
            return title
    return "Other"


def render_overview(profile: SubsystemProfile, groups: dict[str, list[Option]], total: int) -> str:
    lines = [
        f"# {profile.title} Config Deep Dive — All Options",
        "",
        f"Extended reference for all **{total}** {profile.title} options with "
        "**Finding optimal value** guidance (one section per option). "
        f"Generated from [config/{profile.config_subdir}/INDEX.md]"
        f"({profile.config_href_from_root}/INDEX.md).",
        "",
        "```bash",
        "./scripts/lookup-config.sh <option-name>",
        f"python3 scripts/generate-config-guide.py {profile.id}",
        "```",
        "",
        "- [Tuning quick reference](TUNING.md)",
        "",
        "## Topics by category",
        "",
    ]
    current_section = ""
    for slug in nav_slugs_in_order(profile, groups):
        section = section_title_for_slug(profile, slug)
        if section != current_section:
            current_section = section
            lines.extend(["", f"### {section}", "", "| Topic | Options |", "|-------|---------|"])
        lines.append(f"| [{group_title(profile, slug)}]({topic_href(profile, slug)}) | {len(groups[slug])} |")
    lines.extend(["", "[← Guides overview](../../guides/OVERVIEW.md)", ""])
    return "\n".join(lines)


def render_tuning_index(profile: SubsystemProfile, all_options: list[Option]) -> str:
    lines = [
        f"# {profile.title} Config — Tuning Quick Reference",
        "",
        f"All **{len(all_options)}** options with tuning model and one-line guidance.",
        "",
        "[← Overview](OVERVIEW.md)",
        "",
        "| Option | Default | Model | Quick answer | Topic |",
        "|--------|---------|-------|--------------|-------|",
    ]
    for opt in all_options:
        slug = profile.group_for(opt.name)
        title = group_title(profile, slug)
        lines.append(
            f"| [`{opt.name}`]({topic_href(profile, slug)}#{opt.name}) | "
            f"`{opt.effective_default}` | {tuning_model(opt)} | "
            f"{tuning_quick_answer(opt)} | [{title}]({topic_href(profile, slug)}) |"
        )
    lines.extend(["", "[← Overview](OVERVIEW.md)", ""])
    return "\n".join(lines)


def indent_nav_block(block: str) -> str:
    """Indent subsystem nav by 2 spaces (under Config deep dives parent)."""
    return "\n".join(f"  {line}" if line.strip() else line for line in block.splitlines())


def build_mkdocs_nav_yaml(profile: SubsystemProfile, groups: dict[str, list[Option]]) -> str:
    assigned: set[str] = set()
    for _title, _section_dir, slugs in profile.nav_sections:
        assigned.update(slugs)

    lines = [
        f"    - {profile.title} config deep dive:",
        "      - Start here:",
        f"        - Overview: guides/{profile.guides_subdir}/OVERVIEW.md",
        f"        - Tuning quick reference: guides/{profile.guides_subdir}/TUNING.md",
    ]
    for section_title, section_dir, slugs in profile.nav_sections:
        present = [s for s in slugs if s in groups]
        if not present:
            continue
        lines.append(f"      - {section_title}:")
        for slug in present:
            title = group_title(profile, slug)
            lines.append(
                f"        - {title}: guides/{profile.guides_subdir}/"
                f"{section_dir_for_slug(profile, slug)}/{slug}.md"
            )
    extra = [s for s in sorted(groups) if s not in assigned]
    if extra:
        lines.append("      - Other:")
        for slug in extra:
            title = group_title(profile, slug)
            lines.append(
                f"        - {title}: guides/{profile.guides_subdir}/"
                f"{section_dir_for_slug(profile, slug)}/{slug}.md"
            )
    return indent_nav_block("\n".join(lines))


def patch_mkdocs_nav(profile: SubsystemProfile, groups: dict[str, list[Option]], mkdocs: Path) -> None:
    if not profile.nav_marker:
        return
    begin = f"# {profile.nav_marker}:start"
    end = f"# {profile.nav_marker}:end"
    text = mkdocs.read_text(encoding="utf-8")
    if begin not in text or end not in text:
        print(f"warning: {mkdocs} missing {begin}/{end}", file=sys.stderr)
        return
    before, rest = text.split(begin, 1)
    _old, after = rest.split(end, 1)
    block = build_mkdocs_nav_yaml(profile, groups)
    mkdocs.write_text(f"{before}{begin}\n{block}\n{end}{after}", encoding="utf-8")
    print(f"Patched {profile.id} nav in {mkdocs.relative_to(ROOT)}")


def generate_subsystem(profile: SubsystemProfile, *, patch_nav: bool = True) -> int:
    by_name: dict[str, Option] = {}
    for md in sorted(profile.config_dir.glob("*.md")):
        if md.name in ("INDEX.md", "README.md"):
            continue
        for opt in parse_table(md):
            by_name[opt.name] = opt

    index_order = parse_index_order(profile.config_dir)
    all_options: list[Option] = []
    for name, _href in index_order:
        if name not in by_name:
            print(f"warning: {name} in INDEX but not parsed", file=sys.stderr)
            continue
        all_options.append(by_name[name])

    groups: dict[str, list[Option]] = defaultdict(list)
    for opt in all_options:
        groups[profile.group_for(opt.name)].append(opt)

    profile.guides_dir.mkdir(parents=True, exist_ok=True)
    (profile.guides_dir / "OVERVIEW.md").write_text(
        render_overview(profile, groups, len(all_options)), encoding="utf-8"
    )
    (profile.guides_dir / "TUNING.md").write_text(
        render_tuning_index(profile, all_options), encoding="utf-8"
    )
    for slug, options in sorted(groups.items()):
        path = topic_path(profile, slug)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_group(profile, slug, options), encoding="utf-8")

    keep = {topic_path(profile, slug) for slug in groups} | {
        profile.guides_dir / "OVERVIEW.md",
        profile.guides_dir / "TUNING.md",
    }
    for path in profile.guides_dir.rglob("*.md"):
        if path not in keep:
            path.unlink()
            print(f"Removed stale {path.relative_to(ROOT)}")
    for path in sorted(profile.guides_dir.iterdir(), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()

    if patch_nav and profile.nav_marker:
        patch_mkdocs_nav(profile, groups, ROOT / "mkdocs.yml")

    print(
        f"{profile.id}: {len(groups)} topics, {len(all_options)} options → "
        f"guides/{profile.guides_subdir}/"
    )
    return len(all_options)
