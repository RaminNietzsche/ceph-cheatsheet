#!/usr/bin/env bash
# Search Ceph configuration options across all markdown tables.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONFIG_DIR="${ROOT}/docs/en/cheatsheet/config"

usage() {
  cat <<'EOF'
Usage: search-config.sh [OPTIONS] QUERY

Search ceph-cheatsheet configuration documentation.

Options:
  -n, --name-only    Match option names only (default)
  -a, --all          Search all table columns
  -s, --subsystem S  Limit to subsystem (osd, rgw, global, ...)
  -h, --help         Show this help

Examples:
  search-config.sh osd_max_scrubs
  search-config.sh -s rgw cache
  search-config.sh -a "writeback"
EOF
}

subsystem=""
mode="name"
query=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    -n|--name-only) mode="name"; shift ;;
    -a|--all) mode="all"; shift ;;
    -s|--subsystem) subsystem="$2"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    -*) echo "Unknown option: $1" >&2; usage; exit 1 ;;
    *)
      query="$*"
      break
      ;;
  esac
done

if [[ -z "${query}" ]]; then
  usage
  exit 1
fi

if [[ ! -d "${CONFIG_DIR}" ]]; then
  echo "Config reference missing at ${CONFIG_DIR#"${ROOT}/"}" >&2
  echo "Run: make build   (or: python3 scripts/generate-config-guide.py all)" >&2
  exit 1
fi

search_path="${CONFIG_DIR}"
if [[ -n "${subsystem}" ]]; then
  search_path="${CONFIG_DIR}/${subsystem}"
  if [[ ! -d "${search_path}" ]]; then
    echo "Unknown subsystem: ${subsystem}" >&2
    exit 1
  fi
fi

pattern="${query}"

search_with_rg() {
  if [[ "${mode}" == "name" ]]; then
    local name_pattern="SP_${pattern}\""
    rg --no-heading --line-number --ignore-case --fixed-strings \
      --glob '*.md' --glob '!**/INDEX.md' --glob '!**/readme.md' \
      "${name_pattern}" "${search_path}" || true
  else
    rg --no-heading --line-number --ignore-case \
      --glob '*.md' --glob '!**/INDEX.md' \
      "${pattern}" "${search_path}" || true
  fi
}

search_with_grep() {
  local output=""
  while IFS= read -r file; do
    local hits
    if [[ "${mode}" == "name" ]]; then
      hits="$(grep -inF "SP_${pattern}\"" "${file}" 2>/dev/null || true)"
    else
      hits="$(grep -in -e "${pattern}" "${file}" 2>/dev/null || true)"
    fi
    if [[ -n "${hits}" ]]; then
      if [[ -n "${output}" ]]; then
        output+=$'\n'
      fi
      output+="${hits}"
    fi
  done < <(find "${search_path}" -name '*.md' ! -name 'INDEX.md' ! -name 'readme.md' -print)

  if [[ -n "${output}" ]]; then
    printf '%s\n' "${output}"
  fi
}

if command -v rg >/dev/null 2>&1; then
  search_with_rg
elif command -v grep >/dev/null 2>&1; then
  search_with_grep
else
  echo "Need ripgrep (rg) or grep to search config tables." >&2
  echo "Install ripgrep: brew install ripgrep" >&2
  exit 1
fi
