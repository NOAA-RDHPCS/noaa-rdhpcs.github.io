#!/usr/bin/env bash
# Start the sphinx-autobuild live preview in the background.
#
# The dev container runs this each time the container starts.  Run it again
# to restart the preview, for example after recreating .venv.

set -euo pipefail

cd "$(dirname "$0")/.."

PORT=8000
LOG=/tmp/sphinx-autobuild.log

if pgrep -f "sphinx-autobuild source" >/dev/null; then
    echo "The live preview is already running on port ${PORT}."
    exit 0
fi

# sphinx-autobuild is only used for the live preview, so it is not part of
# requirements.txt.  Install it if .venv was created without it.
if ! .venv/bin/python -m pip show --quiet sphinx-autobuild 2>/dev/null; then
    echo "Installing sphinx-autobuild ..."
    .venv/bin/python -m pip install --quiet sphinx-autobuild
fi

nohup .venv/bin/sphinx-autobuild source build/html \
    --host 0.0.0.0 --port "${PORT}" >"${LOG}" 2>&1 &

echo "Started the live preview on port ${PORT}.  Log: ${LOG}"
