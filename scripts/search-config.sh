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

search_path="${CONFIG_DIR}"
if [[ -n "${subsystem}" ]]; then
  search_path="${CONFIG_DIR}/${subsystem}"
  if [[ ! -d "${search_path}" ]]; then
    echo "Unknown subsystem: ${subsystem}" >&2
    exit 1
  fi
fi

pattern="${query}"
if [[ "${mode}" == "name" ]]; then
  rg --no-heading --line-number --ignore-case \
    --glob '*.md' --glob '!**/INDEX.md' \
    "${pattern}" "${search_path}" \
    | rg -v '^\S+:1:\|' || true
else
  rg --no-heading --line-number --ignore-case \
    --glob '*.md' --glob '!**/INDEX.md' \
    "${pattern}" "${search_path}" || true
fi
