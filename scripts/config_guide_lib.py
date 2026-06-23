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

# MkDocs serves guides under /cheatsheet/guides/ (see docs/cheatsheet/guides symlink).
GUIDES_NAV_PREFIX = "cheatsheet/guides"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from i18n import (  # noqa: E402
    LOCALES,
    apply_inline_labels,
    cleanup_stale_markdown,
    get_locale,
    locale_path,
    model_label,
    render_all_locales,
    set_locale,
    t,
    write_localized,
)

ROW_RE = re.compile(
    r'^\| <span id="SP_([^"]+)">([^<]+)</span> \|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|'
)
SEE_ALSO_RE = re.compile(r"\[\[([^\]]+)\]\(#SP_([^)]+)\)\]")
INDEX_LINK_RE = re.compile(r"^ - \[([^\]]+)\]\(([^)]+)\)")


def is_source_config_md(path: Path) -> bool:
    """English config tables only — skip INDEX/README and i18n suffix files."""
    name = path.name
    if name in ("INDEX.md", "README.md"):
        return False
    if name.endswith(".fa.md") or name.endswith(".zh.md"):
        return False
    return name.endswith(".md")


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
        return t("when_use_dev")
    if typ == "Bool":
        default = opt.effective_default.lower()
        if default == "true":
            return t("when_use_bool_true")
        return t("when_use_bool_false")
    if name.endswith(("_url", "_uri", "_addr")):
        return t("when_use_external_url")
    if any(x in name for x in ("max_", "min_", "limit", "cap")):
        return t("when_use_limits")
    if any(x in name for x in ("interval", "sleep", "timeout", "period")):
        return t("when_use_intervals")
    if level == "Basic":
        return t("when_use_basic", title=profile.title)
    return t("when_use_advanced")


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
        return t("tune_quick_dev")
    if model == "Capacity":
        return t("tune_quick_capacity")
    if model == "Connectivity":
        return t("tune_quick_connectivity")
    if model == "Policy":
        return t("tune_quick_policy")
    if opt.typ == "Bool":
        return t("tune_quick_bool")
    if opt.min_val or opt.max_val:
        return t("tune_quick_bounds")
    return t("tune_quick_default")


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
        t("signals_default"),
        "",
        "```bash",
        f"ceph config get {target} {opt.name}",
        "ceph -s",
    ]
    if target == "osd":
        lines.append("ceph daemon osd.<id> perf dump | head")
        lines.append("ceph pg stat")
    elif target == "mon":
        lines.append("ceph mon stat")
    elif target == "mgr":
        lines.append("ceph mgr stat")
    elif target == "mds":
        lines.append("ceph fs status")
        lines.append("ceph mds stat")
    elif target == "client":
        lines.append(t("client_monitor_comment"))
    lines.append("```")
    return "\n".join(lines)


def render_finding_optimal_value(profile: SubsystemProfile, opt: Option) -> str:
    model = tuning_model(opt)
    default = opt.effective_default
    lines = [f"{t('label_tuning_model')} {model_label(model)}", ""]

    if model == "Dev":
        lines.extend(
            [
                t("find_dev_1", default=default),
                t("find_dev_2"),
                t("find_dev_3"),
            ]
        )
        return "\n".join(lines)

    if model == "Capacity":
        lines.extend(
            [
                t("find_cap_1", default=default),
                t("find_cap_2"),
                t("find_cap_3"),
            ]
        )
        return "\n".join(lines) + monitor_block(profile, opt)

    if model == "Connectivity":
        lines.extend(
            [
                t("find_conn_1"),
                t("find_conn_2"),
                t("find_conn_3"),
                t("find_conn_4", default=default),
            ]
        )
        return "\n".join(lines) + monitor_block(profile, opt)

    if model == "Policy":
        lines.extend(
            [
                t("find_policy_1", default=default),
                t("find_policy_2"),
                t("find_policy_3"),
            ]
        )
        return "\n".join(lines) + monitor_block(profile, opt)

    lines.extend(
        [
            t("find_perf_1", default=default),
            t("find_perf_2"),
            t("find_perf_3"),
            t("find_perf_4"),
        ]
    )
    if opt.min_val or opt.max_val:
        lines.append(
            "\n"
            + t(
                "label_bounds_line",
                min_val=opt.min_val or "—",
                max_val=opt.max_val or "—",
            )
        )
    return "\n".join(lines) + monitor_block(profile, opt)


def format_see_also(profile: SubsystemProfile, opt: Option) -> str:
    refs = related_options(opt)
    if not refs:
        return ""
    lines = [t("label_related_options"), ""]
    for ref in refs:
        lines.append(
            f"- [`{ref}`]({profile.config_href_from_topic}/{opt.source_file}#SP_{ref})"
        )
    lines.append("")
    return "\n".join(lines)


def render_option(profile: SubsystemProfile, opt: Option) -> str:
    enrich = profile.enrichments.get(opt.name, {})
    table_link = f"{profile.config_href_from_topic}/{opt.source_file}#SP_{opt.name}"
    startup = t("label_startup") if opt.flags and "STARTUP" in opt.flags else ""
    type_bits = [opt.typ, f"default `{opt.effective_default}`", f"**{opt.level}**"]
    if opt.valid_values:
        type_bits.insert(1, f"enum: {opt.valid_values}")
    parts = [
        f"### {opt.name}",
        "",
        "| | |",
        "|---|---|",
        f"{t('label_type')} {' · '.join(type_bits)}{startup} |",
        f"{t('label_table')} [{opt.source_file}#SP_{opt.name}]({table_link}) |",
        "",
    ]
    what = enrich.get("what") or opt.full_desc
    if what:
        parts.extend([f"{t('label_what_it_does')} {what}", ""])
    if enrich.get("when_to_use"):
        parts.extend([f"{t('label_when_to_use')} {enrich['when_to_use']}", ""])
    else:
        parts.extend([f"{t('label_when_to_use')} {when_to_use(opt, profile)}", ""])
    see = format_see_also(profile, opt)
    if see:
        parts.append(see)
    parts.extend(
        [
            t("label_example"),
            "",
            render_example(profile, opt),
            "",
            t("label_finding_optimal"),
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
            t("finding_intro_title"),
            "",
            t("finding_intro_table"),
            "|-------|---------------|",
            t("finding_policy_row"),
            t("finding_capacity_row"),
            t("finding_performance_row"),
            t("finding_connectivity_row"),
            t("finding_dev_row"),
            "",
            t("label_shared_tooling"),
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
        t(
            "group_intro",
            title=profile.title,
            count=len(options),
            overview=t("back_overview"),
            tuning=t("tuning_index_link"),
            index=f"[INDEX]({profile.config_href_from_topic}/INDEX.md)",
        ),
        "",
        t("option_summary_header"),
        "|--------|---------|-------|--------|",
    ]
    for opt in options:
        lines.append(
            f"| [{opt.name}](#{opt.name}) | `{opt.effective_default}` | {opt.level} | "
            f"{model_label(tuning_model(opt))} |"
        )
    lines.extend(["", tuning_intro(profile)])
    for opt in options:
        lines.append(render_option(profile, opt))
    lines.extend(["", t("back_overview"), ""])
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
        t("overview_title", title=profile.title),
        "",
        t(
            "overview_blurb",
            count=total,
            title=profile.title,
            subdir=profile.config_subdir,
            href=f"{profile.config_href_from_root}/INDEX.md",
        ),
        "",
        "```bash",
        "./scripts/lookup-config.sh <option-name>",
        f"python3 scripts/generate-config-guide.py {profile.id}",
        "```",
        "",
        t("tuning_quick_link"),
        "",
        t("topics_by_category"),
        "",
    ]
    current_section = ""
    for slug in nav_slugs_in_order(profile, groups):
        section = section_title_for_slug(profile, slug)
        if section != current_section:
            current_section = section
            lines.extend(["", f"### {section}", "", t("topic_summary_header"), "|-------|---------|"])
        lines.append(f"| [{group_title(profile, slug)}]({topic_href(profile, slug)}) | {len(groups[slug])} |")
    lines.extend(["", t("back_guides_overview"), ""])
    return "\n".join(lines)


def render_tuning_index(profile: SubsystemProfile, all_options: list[Option]) -> str:
    lines = [
        t("tuning_title", title=profile.title),
        "",
        t("tuning_blurb", count=len(all_options)),
        "",
        t("back_overview"),
        "",
        t("tuning_summary_header"),
        "|--------|---------|-------|--------------|-------|",
    ]
    for opt in all_options:
        slug = profile.group_for(opt.name)
        title = group_title(profile, slug)
        lines.append(
            f"| [`{opt.name}`]({topic_href(profile, slug)}#{opt.name}) | "
            f"`{opt.effective_default}` | {model_label(tuning_model(opt))} | "
            f"{tuning_quick_answer(opt)} | [{title}]({topic_href(profile, slug)}) |"
        )
    lines.extend(["", t("back_overview"), ""])
    return "\n".join(lines)


def indent_nav_block(block: str) -> str:
    """Indent under Cheatsheet → Guides → Config deep dives (4 spaces)."""
    return "\n".join(f"    {line}" if line.strip() else line for line in block.splitlines())


def build_mkdocs_nav_yaml(profile: SubsystemProfile, groups: dict[str, list[Option]]) -> str:
    assigned: set[str] = set()
    for _title, _section_dir, slugs in profile.nav_sections:
        assigned.update(slugs)

    lines = [
        f"    - {profile.title} config deep dive:",
        "      - Start here:",
        f"        - Overview: {GUIDES_NAV_PREFIX}/{profile.guides_subdir}/OVERVIEW.md",
        f"        - Tuning quick reference: {GUIDES_NAV_PREFIX}/{profile.guides_subdir}/TUNING.md",
    ]
    for section_title, section_dir, slugs in profile.nav_sections:
        present = [s for s in slugs if s in groups]
        if not present:
            continue
        lines.append(f"      - {section_title}:")
        for slug in present:
            title = group_title(profile, slug)
            lines.append(
                f"        - {title}: {GUIDES_NAV_PREFIX}/{profile.guides_subdir}/"
                f"{section_dir_for_slug(profile, slug)}/{slug}.md"
            )
    extra = [s for s in sorted(groups) if s not in assigned]
    if extra:
        lines.append("      - Other:")
        for slug in extra:
            title = group_title(profile, slug)
            lines.append(
                f"        - {title}: {GUIDES_NAV_PREFIX}/{profile.guides_subdir}/"
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
        if not is_source_config_md(md):
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

    overview_base = profile.guides_dir / "OVERVIEW.md"
    tuning_base = profile.guides_dir / "TUNING.md"
    write_localized(overview_base, render_all_locales(render_overview, profile, groups, len(all_options)))
    write_localized(tuning_base, render_all_locales(render_tuning_index, profile, all_options))

    topic_bases: set[Path] = {overview_base, tuning_base}
    for slug, options in sorted(groups.items()):
        base = topic_path(profile, slug)
        base.parent.mkdir(parents=True, exist_ok=True)
        write_localized(base, render_all_locales(render_group, profile, slug, options))
        topic_bases.add(base)

    cleanup_stale_markdown(profile.guides_dir, topic_bases)

    if patch_nav and profile.nav_marker:
        patch_mkdocs_nav(profile, groups, ROOT / "mkdocs.yml")

    print(
        f"{profile.id}: {len(groups)} topics, {len(all_options)} options → "
        f"guides/{profile.guides_subdir}/"
    )
    return len(all_options)
