# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line or environment.
SPHINXOPTS    ?=
SOURCEDIR     = source
BUILDDIR      = build
PORT          ?= 8000
VENV          = .venv
PYTHON        = $(VENV)/bin/python
PIP           = $(VENV)/bin/pip
MIN_PY_VER    = 3.10

# Verify python3 is available and meets minimum version requirement.
PYTHON3 := $(shell command -v python3 2>/dev/null)
ifeq ($(PYTHON3),)
  $(error python3 not found. Please install Python $(MIN_PY_VER) or newer.)
endif
PYTHON3_VER := $(shell python3 -c \
  "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
PYTHON3_OK := $(shell python3 -c \
  "import sys; print('ok' if sys.version_info >= (3,10) else 'old')")
ifneq ($(PYTHON3_OK),ok)
  $(error Python $(MIN_PY_VER)+ required, found $(PYTHON3_VER). Please upgrade Python.)
endif

# Use venv binaries so the user does not need to activate the environment.
SPHINXBUILD   := $(VENV)/bin/sphinx-build
LINTRST       := $(VENV)/bin/doc8

# Put it first so that "make" without argument is like "make help".
help: venv
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo "  lint        to run a linter on the RST files in the source directory"
	@echo "  serve       to start a local web server on port $(PORT) to view the built docs"
	@echo "  venv        to create the Python virtual environment and install dependencies"
	@echo "  distclean   to remove the build directory and the virtual environment"

.PHONY: help Makefile lint serve venv distclean

# Prevent the catch-all pattern rule from trying to "build" requirements.txt.
requirements.txt: ;

# Create the virtual environment and install dependencies.
venv: $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	@echo "Creating Python virtual environment in $(VENV)/ ..."
	@python3 -m venv $(VENV)
	@echo "Installing dependencies from requirements.txt ..."
	@$(PIP) install --quiet --upgrade pip
	@$(PIP) install --quiet -r requirements.txt
	@touch $(VENV)/bin/activate
	@echo "Virtual environment ready."

distclean:
	@echo "Removing build directory $(BUILDDIR)/ ..."
	@rm -rf $(BUILDDIR)
	@echo "Removing virtual environment $(VENV)/ ..."
	@rm -rf $(VENV)

serve: html
	@if lsof -ti:$(PORT) >/dev/null 2>&1; then \
		echo "Error: Port $(PORT) is already in use. Run 'make serve PORT=<number>' to use a different port."; \
		exit 1; \
	fi
	@echo "Serving documentation at http://localhost:$(PORT) (press Ctrl+C to stop)"
	@$(PYTHON) -m http.server $(PORT) --directory "$(BUILDDIR)/html"

lint: venv
	@$(LINTRST) $(SOURCEDIR)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: venv Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
