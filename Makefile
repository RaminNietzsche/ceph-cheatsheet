# ceph-cheatsheet — common tasks
# Run `make` or `make help` for targets. See scripts/README.md for details.

PYTHON    ?= python3
PIP       ?= pip
CEPH_REF  ?= main
PORT      ?= 8000
SITE_PORT ?= 8765

.PHONY: help install setup validate sync-index config generate build docs all \
        inventory trust i18n i18n-pages i18n-config readme fix-hrefs check clean \
        serve serve-site lookup search search-config search-fuzzy

help: ## Show this help
	@grep -E '^[a-zA-Z0-9_.-]+:.*##' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

install: ## Install Python deps (scripts/requirements.txt)
	$(PIP) install -r scripts/requirements.txt

setup: ## Verify docs/{en,fa,zh}/ layout exists
	$(PYTHON) scripts/setup-docs-layout.py

validate: setup ## Validate mkdocs nav, symlinks, hub locale links
	$(PYTHON) scripts/validate-docs-paths.py

sync-index: ## Sync REFERENCE → OVERVIEW; VERSION/LICENSE → docs/en/
	$(PYTHON) scripts/sync-docs-index.py

config: setup ## Regenerate config tables from upstream Ceph (CEPH_REF=main)
	$(PYTHON) scripts/generate-config.py --ref $(CEPH_REF)

generate: setup ## Run generators + i18n + reports (no mkdocs build)
	$(PYTHON) scripts/setup-docs-layout.py
	-$(PYTHON) scripts/sync-rgw-from-docs-extended.py
	$(PYTHON) scripts/generate-role-scale-guides.py
	$(PYTHON) scripts/generate-rgw-guide.py
	$(PYTHON) scripts/generate-config-guide.py all
	$(PYTHON) scripts/sync-i18n-config.py
	$(PYTHON) scripts/sync-docs-index.py
	$(PYTHON) scripts/sync-i18n-pages.py
	$(PYTHON) scripts/sync-readme-i18n.py
	$(PYTHON) scripts/generate-content-inventory.py
	$(PYTHON) scripts/generate-page-trust-manifest.py
	$(PYTHON) scripts/fix-html-hrefs.py

build: fix-hrefs validate ## mkdocs build + restructure site locales
	$(PYTHON) -m mkdocs build
	$(PYTHON) scripts/restructure-site-locales.py

docs: ## Full doc pipeline (generate + build) — same as regenerate-docs.py
	$(PYTHON) scripts/regenerate-docs.py

all: install setup config docs ## Fresh setup: deps + config from upstream + full build

inventory: setup ## Regenerate reports/content-inventory.{csv,md}
	$(PYTHON) scripts/generate-content-inventory.py

inventory-sync: setup ## Inventory + append new nav pages to content-review.yaml
	$(PYTHON) scripts/generate-content-inventory.py --sync-review

trust: setup ## Regenerate page-trust badges (docs/javascripts/page-trust-data.js)
	$(PYTHON) scripts/generate-page-trust-manifest.py

i18n: i18n-config i18n-pages ## Sync fa/zh for config OVERVIEW + hand-written pages

i18n-config: setup ## Sync fa/zh for cheatsheet/config/OVERVIEW
	$(PYTHON) scripts/sync-i18n-config.py

i18n-pages: setup ## Sync fa/zh for cli/, guides/, docs/ hand pages
	$(PYTHON) scripts/sync-i18n-pages.py

readme: setup ## Sync README.md + README.fa.md + README.zh.md from readme.yaml
	$(PYTHON) scripts/sync-readme-i18n.py

fix-hrefs: ## Strip .md from hub HTML hrefs (before mkdocs build)
	$(PYTHON) scripts/fix-html-hrefs.py

check: inventory readme ## CI-style checks: validate + inventory + README committed
	$(PYTHON) scripts/validate-docs-paths.py
	@git diff --exit-code reports/content-inventory.csv reports/content-inventory.md || \
		(echo "Inventory out of date — run: make inventory" && exit 1)
	@git diff --exit-code README.md README.fa.md README.zh.md || \
		(echo "README locales out of date — run: make readme" && exit 1)

serve: setup ## Dev server (English at / — no locale restructure)
	$(PYTHON) -m mkdocs serve -a 127.0.0.1:$(PORT)

serve-site: ## Serve built site/ (production layout: / → en/)
	@test -d site/en || (echo "Run make docs first" && exit 1)
	$(PYTHON) -m http.server $(SITE_PORT) --directory site

clean: ## Remove site/ and Python cache
	rm -rf site
	find . -type d -name __pycache__ -prune -exec rm -rf {} + 2>/dev/null || true

# --- Search (require rg; fuzzy requires fzf) ---

lookup: ## Look up one config option: make lookup OPT=osd_max_scrubs
	@test -n "$(OPT)" || (echo "Usage: make lookup OPT=<option>" && exit 1)
	./scripts/lookup-config.sh $(OPT)

search: ## Search cli + config + guides: make search Q=scrub
	@test -n "$(Q)" || (echo "Usage: make search Q=<term>" && exit 1)
	./scripts/search-all.sh $(Q)

search-config: ## Search config tables only: make search-config Q=rgw_cache
	@test -n "$(Q)" || (echo "Usage: make search-config Q=<term>" && exit 1)
	./scripts/search-config.sh $(Q)

search-fuzzy: ## Interactive fuzzy search (requires fzf)
	./scripts/search-fuzzy.sh
