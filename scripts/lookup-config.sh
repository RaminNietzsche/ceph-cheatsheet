#!/usr/bin/env bash
# Pretty-print a single Ceph config option from the reference tables.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONFIG_DIR="${ROOT}/docs/en/cheatsheet/config"

usage() {
  cat <<'EOF'
Usage: lookup-config.sh <option-name>

Look up a Ceph config option and print a readable summary.

Example:
  lookup-config.sh osd_max_scrubs
  lookup-config.sh rgw_cache_enabled
EOF
}

if [[ $# -lt 1 ]]; then
  usage
  exit 1
fi

if [[ ! -d "${CONFIG_DIR}" ]]; then
  echo "Config reference missing at ${CONFIG_DIR#"${ROOT}/"}" >&2
  echo "Run: make build   (or: python3 scripts/generate-config-guide.py all)" >&2
  exit 1
fi

name="$1"
pattern="SP_${name}\""

find_config_file() {
  if command -v rg >/dev/null 2>&1; then
    rg -l --glob '*.md' --glob '!**/INDEX.md' --glob '!**/readme.md' \
      "${pattern}" "${CONFIG_DIR}" 2>/dev/null | head -1 || true
    return
  fi

  if ! command -v grep >/dev/null 2>&1; then
    echo "Need ripgrep (rg) or grep to search config tables." >&2
    echo "Install ripgrep: brew install ripgrep" >&2
    exit 1
  fi

  while IFS= read -r candidate; do
    if grep -qF "${pattern}" "${candidate}" 2>/dev/null; then
      echo "${candidate}"
      return
    fi
  done < <(find "${CONFIG_DIR}" -name '*.md' ! -name 'INDEX.md' ! -name 'readme.md' -print)
}

find_config_line() {
  local file="$1"
  if command -v rg >/dev/null 2>&1; then
    rg -F "${pattern}" "${file}" 2>/dev/null | head -1 || true
    return
  fi
  grep -F "${pattern}" "${file}" 2>/dev/null | head -1 || true
}

file="$(find_config_file)"

if [[ -z "${file}" ]]; then
  echo "Option not found: ${name}" >&2
  echo "Search: ./scripts/search-config.sh ${name}" >&2
  exit 1
fi

line_content="$(find_config_line "${file}")"
if [[ -z "${line_content}" ]]; then
  echo "Option not found: ${name}" >&2
  exit 1
fi

trim() { echo "$1" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//'; }
strip_html() { echo "$1" | sed -E 's/<[^>]+>//g'; }

IFS='|' read -r -a cells <<< "${line_content}"

raw_name="$(trim "${cells[1]:-}")"
desc="$(trim "${cells[2]:-}")"
level="$(strip_html "$(trim "${cells[3]:-}")")"
typ="$(trim "${cells[4]:-}")"
default="$(trim "${cells[5]:-}")"
daemon_default="$(trim "${cells[6]:-}")"
min_val="$(trim "${cells[7]:-}")"
max_val="$(trim "${cells[8]:-}")"
valid="$(trim "${cells[9]:-}")"
flags="$(trim "${cells[12]:-}")"
services="$(trim "${cells[13]:-}")"
long_desc="$(trim "${cells[15]:-}")"
tags="$(trim "${cells[16]:-}")"

clean_name="$(strip_html "${raw_name}")"

rel_file="${file#"${ROOT}/"}"

echo "Option:    ${clean_name}"
echo "File:      ${rel_file}"
echo "Level:     ${level}"
echo "Type:      ${typ}"
[[ -n "${desc}" ]] && echo "Desc:      ${desc}"
[[ -n "${long_desc}" && "${long_desc}" != "${desc}" ]] && echo "Long:      ${long_desc}"
echo "Default:   ${default:-—}${daemon_default:+ (daemon: ${daemon_default})}"
[[ -n "${min_val}" || -n "${max_val}" ]] && echo "Range:     min=${min_val:-—} max=${max_val:-—}"
[[ -n "${valid}" ]] && echo "Values:    ${valid}"
[[ -n "${flags}" ]] && echo "Flags:     ${flags}"
[[ -n "${services}" ]] && echo "Services:  ${services}"
[[ -n "${tags}" ]] && echo "Tags:      ${tags}"
echo
echo "Set:       ceph config set <who> ${clean_name} <value>"
