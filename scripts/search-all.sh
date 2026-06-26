#!/usr/bin/env bash
# Search CLI docs and config reference.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

usage() {
  cat <<'EOF'
Usage: search-all.sh [OPTIONS] QUERY

Search CLI commands and config options.

Options:
  -c, --cli-only     Search cli/ only
  -g, --config-only  Search config/ only
  -h, --help         Show help

Examples:
  search-all.sh scrub
  search-all.sh --cli-only "ceph orch"
  search-all.sh --config-only rgw_cache
EOF
}

mode="all"
query=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    -c|--cli-only) mode="cli"; shift ;;
    -g|--config-only) mode="config"; shift ;;
    -h|--help) usage; exit 0 ;;
    -*) echo "Unknown option: $1" >&2; usage; exit 1 ;;
    *) query="$*"; break ;;
  esac
done

if [[ -z "${query}" ]]; then
  usage
  exit 1
fi

search_dir_with_rg() {
  local dir="$1"
  rg -n --ignore-case --glob '*.md' --glob '!**/INDEX.md' \
    "${query}" "${dir}" 2>/dev/null || true
}

search_dir_with_grep() {
  local dir="$1"
  if [[ ! -d "${dir}" ]]; then
    return 0
  fi
  while IFS= read -r file; do
    grep -in -e "${query}" "${file}" 2>/dev/null || true
  done < <(find "${dir}" -name '*.md' ! -name 'INDEX.md' -print)
}

search_dir() {
  local dir="$1"
  if command -v rg >/dev/null 2>&1; then
    search_dir_with_rg "${dir}"
  elif command -v grep >/dev/null 2>&1; then
    search_dir_with_grep "${dir}"
  else
    echo "Need ripgrep (rg) or grep to search documentation." >&2
    echo "Install ripgrep: brew install ripgrep" >&2
    exit 1
  fi
}

search() {
  local dir="$1" label="$2"
  local results
  results="$(search_dir "${dir}")"
  if [[ -n "${results}" ]]; then
    echo "=== ${label} ==="
    echo "${results}"
    echo
  fi
}

case "${mode}" in
  all)
    search "${ROOT}/docs/en/cheatsheet/cli" "CLI"
    search "${ROOT}/docs/en/cheatsheet/config" "Config"
    search "${ROOT}/docs/en/cheatsheet/guides" "Guides"
    ;;
  cli) search "${ROOT}/docs/en/cheatsheet/cli" "CLI" ;;
  config) search "${ROOT}/docs/en/cheatsheet/config" "Config" ;;
esac
