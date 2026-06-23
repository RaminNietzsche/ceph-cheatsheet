#!/usr/bin/env bash
# Interactive fuzzy search across CLI and config docs (requires fzf).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if ! command -v fzf >/dev/null 2>&1; then
  echo "fzf is required. Install: brew install fzf  (or apt install fzf)" >&2
  echo "Fallback: ./scripts/search-all.sh QUERY" >&2
  exit 1
fi

if ! command -v rg >/dev/null 2>&1; then
  echo "ripgrep (rg) is required." >&2
  exit 1
fi

preview_cmd='bat --color=always --line-range :300 {} 2>/dev/null || sed -n "1,200p" {}'

echo "Loading index…" >&2
mapfile -t entries < <(
  rg -l --glob '*.md' --glob '!**/INDEX.md' --glob '!site/**' '' \
    "${ROOT}/cli" "${ROOT}/guides" "${ROOT}/config" 2>/dev/null \
    | sort
)

if ((${#entries[@]} == 0)); then
  echo "No markdown files found." >&2
  exit 1
fi

selected="$(
  printf '%s\n' "${entries[@]}" \
    | fzf --prompt 'Ceph docs> ' \
          --preview "${preview_cmd}" \
          --preview-window 'right:60%:wrap' \
          --header 'Enter: open path · Esc: quit'
)"

if [[ -z "${selected}" ]]; then
  exit 0
fi

echo "${selected}"
rel="${selected#"${ROOT}/"}"
echo ""
echo "File: ${rel}"
echo "Search inside:"
rg -n --ignore-case "${1:-}" "${selected}" 2>/dev/null | head -40 || true
