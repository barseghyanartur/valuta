.PHONY: help install sync update-lock create-venv \
        test quick-test ipython \
        doc8 ruff ruff-fix format mypy \
        build-docs rebuild-docs build-docs-epub build-docs-pdf auto-build-docs serve-docs \
        compile-requirements compile-requirements-upgrade \
        pre-commit-install pre-commit \
        clean-dev clean-test clean clean-venv \
        update-version package-build check-package-build release test-release

SHELL := /bin/bash

PROJECT_NAME ?= valuta
PACKAGE_IMPORT_NAME ?= valuta
PACKAGE_SRC ?= src/valuta
PACKAGE_EGG_INFO ?= src/valuta.egg-info
VERSION ?= 0.3.2

UV ?= uv
PYTHON ?= $(UV) run python
PYTEST ?= $(UV) run pytest
RUFF ?= $(UV) run ruff
MYPY ?= $(UV) run mypy
DOC8 ?= $(UV) run doc8
PRE_COMMIT ?= $(UV) run pre-commit
TWINE ?= $(UV) run twine

PYTEST_ARGS ?= --ignore=.tox --ignore=examples/requirements
TEST_PATHS ?=
RUFF_PATHS ?= src/valuta
MYPY_PATHS ?= src/valuta

DOCS_DIR ?= docs
BUILD_DOCS_DIR ?= builddocs
DOCS_REQUIREMENTS ?= $(DOCS_DIR)/requirements.txt
DOCS_PORT ?= 5001
SPHINX_BUILD ?= $(UV) run sphinx-build
SPHINX_APIDOC ?= $(UV) run sphinx-apidoc
SPHINX_AUTOBUILD ?= $(UV) run sphinx-autobuild

VERSION_DOC ?= docs/index.rst

help:
	@echo "Common targets:"
	@echo "  make install          Sync uv environment with all groups and extras"
	@echo "  make test             Run pytest through uv"
	@echo "  make ruff             Run ruff check"
	@echo "  make mypy             Run mypy"
	@echo "  make build-docs       Build Sphinx documentation"
	@echo "  make package-build    Build distribution packages"
	@echo "  make release          Upload packages to PyPI"

# ----------------------------------------------------------------------------
# Installation
# ----------------------------------------------------------------------------

create-venv:
	$(UV) venv

sync install:
	$(UV) sync --all-groups --all-extras

update-lock:
	$(UV) lock --upgrade

# ----------------------------------------------------------------------------
# Testing
# ----------------------------------------------------------------------------

test: quick-test

quick-test:
	$(PYTEST) $(PYTEST_ARGS) $(TEST_PATHS)

ipython:
	$(UV) run ipython

# ----------------------------------------------------------------------------
# Code quality
# ----------------------------------------------------------------------------

doc8:
	$(DOC8)

ruff:
	$(RUFF) check $(RUFF_PATHS)

ruff-fix:
	$(RUFF) check $(RUFF_PATHS) --fix

format:
	$(RUFF) format $(RUFF_PATHS)

mypy:
	$(MYPY) $(MYPY_PATHS)

# ----------------------------------------------------------------------------
# Documentation
# ----------------------------------------------------------------------------

build-docs:
	$(SPHINX_BUILD) -n -a -b html $(DOCS_DIR) $(BUILD_DOCS_DIR)
	cd $(BUILD_DOCS_DIR) && zip -r ../$(BUILD_DOCS_DIR).zip . -x ".*"

rebuild-docs:
	$(SPHINX_APIDOC) . --full -o $(DOCS_DIR) -H '$(PROJECT_NAME)' -f -d 20
	@if [ -f "$(DOCS_DIR)/conf.py.distrib" ]; then cp "$(DOCS_DIR)/conf.py.distrib" "$(DOCS_DIR)/conf.py"; fi
	@if [ -f "$(DOCS_DIR)/index.rst.distrib" ]; then cp "$(DOCS_DIR)/index.rst.distrib" "$(DOCS_DIR)/index.rst"; fi

build-docs-epub:
	$(MAKE) -C $(DOCS_DIR) epub

build-docs-pdf:
	$(MAKE) -C $(DOCS_DIR) latexpdf

auto-build-docs:
	$(SPHINX_AUTOBUILD) $(DOCS_DIR) $(DOCS_DIR)/_build/html --port $(DOCS_PORT)

serve-docs:
	cd $(BUILD_DOCS_DIR) && $(PYTHON) -m http.server $(DOCS_PORT)

compile-requirements:
	$(UV) pip compile pyproject.toml --all-extras --group docs -o $(DOCS_REQUIREMENTS)

compile-requirements-upgrade:
	$(UV) pip compile pyproject.toml --all-extras --group docs -o $(DOCS_REQUIREMENTS) --upgrade

# ----------------------------------------------------------------------------
# Pre-commit
# ----------------------------------------------------------------------------

pre-commit-install:
	$(PRE_COMMIT) install

pre-commit: pre-commit-install
	$(PRE_COMMIT) run --all-files

# ----------------------------------------------------------------------------
# Housekeeping
# ----------------------------------------------------------------------------

clean-dev:
	find . -name "*.orig" -exec rm -rf {} +
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	rm -rf dist/ build/ $(PACKAGE_EGG_INFO) src/*.egg-info *.egg-info
	rm -rf .cache/ .mypy_cache/ .ruff_cache/

clean-test:
	find . -name "*.pyc" -exec rm -rf {} +
	rm -rf .coverage .coverage.* .pytest_cache/ htmlcov/

clean-venv:
	rm -rf .venv/

clean: clean-dev clean-test

# ----------------------------------------------------------------------------
# Versioning
# ----------------------------------------------------------------------------

update-version:
	@echo "Updating version to $(VERSION)"
	$(PYTHON) -c "from pathlib import Path; import re; p=Path('pyproject.toml'); s=p.read_text(); s=re.sub(r'^version = \"[^\"]+\"', 'version = \"$(VERSION)\"', s, count=1, flags=re.M); p.write_text(s)"
	@if [ -f "$(PACKAGE_SRC)/__init__.py" ]; then \
		$(PYTHON) -c "from pathlib import Path; import re; p=Path('$(PACKAGE_SRC)/__init__.py'); s=p.read_text(); s=re.sub(r'__version__ = \"[^\"]+\"', '__version__ = \"$(VERSION)\"', s, count=1); p.write_text(s)"; \
	fi
	@if [ -n "$(VERSION_DOC)" ] && [ -f "$(VERSION_DOC)" ]; then \
		$(PYTHON) -c "from pathlib import Path; import re; p=Path('$(VERSION_DOC)'); s=p.read_text(); s=re.sub(r'^:Version: .+', ':Version: $(VERSION)', s, count=1, flags=re.M); p.write_text(s)"; \
	fi

# ----------------------------------------------------------------------------
# Release
# ----------------------------------------------------------------------------

package-build:
	$(PYTHON) -m build .

check-package-build:
	$(TWINE) check dist/*

release:
	$(TWINE) upload dist/* --verbose

test-release:
	$(TWINE) upload --repository testpypi dist/* --verbose
