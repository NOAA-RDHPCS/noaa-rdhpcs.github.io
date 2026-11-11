# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line or environment.
SPHINXOPTS    ?=
SOURCEDIR     = source
BUILDDIR      = build
PORT          ?= 8000
VENV          = .venv
PYTHON        ?= python3
MIN_PY_VER    = 3.12

# Verify python3 is available and meets minimum version requirement.
PYTHON3 := $(firstword $(wildcard $(VENV)/bin/python3 $(shell command -v $(PYTHON) 2>/dev/null)))

# Use venv binaries so the user does not need to activate the environment.
SPHINXBUILD   := $(VENV)/bin/sphinx-build
LINTRST       := $(VENV)/bin/doc8
PIP           := $(VENV)/bin/pip

# Put it first so that "make" without argument is like "make help".
help: venv
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo "  lint        to run a linter on the RST files in the source directory"
	@echo "  serve       to start a local web server on port $(PORT) to view the built docs"
	@echo "  venv        to create the Python virtual environment and install dependencies"
	@echo "  distclean   to remove the build directory and the virtual environment"

.PHONY: help Makefile lint serve venv distclean check-python

# Prevent the catch-all pattern rule from trying to "build" requirements.txt.
requirements.txt: ;

check-python:
	@if [ -z "$(PYTHON3)" ];then \
		echo "$(PYTHON) not found.  Please install Python $(MIN_PY_VER) or newer" 2>&1; \
		exit 1; \
	fi
	@PY_VER=$$($(PYTHON3) -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"); \
	if [ "$$($(PYTHON3) -c "import sys; print('ok' if sys.version_info >= tuple(map(int, '$(MIN_PY_VER)'.split('.'))) else 'old')")" != "ok" ]; then \
		echo "Python $(MIN_PY_VER)+ required, found $$PY_VER.  Please upgrade Python." 2>&1; \
		exit 1;\
	fi

# Create the virtual environment and install dependencies.
venv: check-python $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	@echo "Creating Python virtual environment in $(VENV)/ ..."
	@$(PYTHON3) -m venv $(VENV)
	@echo "Installing dependencies from requirements.txt ..."
	@$(PIP) install --quiet --upgrade pip
	@$(PIP) install --quiet -r requirements.txt
	@touch $(VENV)/bin/activate
	@echo "Virtual environment ready."

distclean:
	@echo "Removing build directory $(BUILDDIR)/ ..."
	@rm -rf $(BUILDDIR)
	@if [ -d $(VENV) ]; then \
		echo "Leaving virtual environment $(VENV)/"; \
		echo "Run \`rm -rf $(VENV)\` to remove it."; \
	fi

serve: html
	@if lsof -ti:$(PORT) >/dev/null 2>&1; then \
		echo "Error: Port $(PORT) is already in use. Run 'make serve PORT=<number>' to use a different port."; \
		exit 1; \
	fi
	@echo "Serving documentation at http://localhost:$(PORT) (press Ctrl+C to stop)"
	@$(PYTHON3) -m http.server $(PORT) --directory "$(BUILDDIR)/html"

lint: venv
	@$(LINTRST) $(SOURCEDIR)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: venv Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
