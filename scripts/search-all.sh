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

search() {
  local dir="$1" label="$2"
  local results
  results="$(rg -n --ignore-case --glob '*.md' --glob '!**/INDEX.md' \
    "${query}" "${dir}" 2>/dev/null || true)"
  if [[ -n "${results}" ]]; then
    echo "=== ${label} ==="
    echo "${results}"
    echo
  fi
}

case "${mode}" in
  all)
    search "${ROOT}/cli" "CLI"
    search "${ROOT}/config" "Config"
    search "${ROOT}/guides" "Guides"
    ;;
  cli) search "${ROOT}/cli" "CLI" ;;
  config) search "${ROOT}/config" "Config" ;;
esac
