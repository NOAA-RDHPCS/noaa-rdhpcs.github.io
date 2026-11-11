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

# Run the preview in its own session.  GitHub Codespaces stops the
# processes in the postStartCommand session when the command finishes.
# PYTHONUNBUFFERED writes the log as the preview runs.
PYTHONUNBUFFERED=1 setsid nohup .venv/bin/sphinx-autobuild source build/html \
    --host 0.0.0.0 --port "${PORT}" >"${LOG}" 2>&1 </dev/null &
pid=$!

# Do not exit until the preview has moved to its own session.  Otherwise
# it can be stopped along with this script.
for _ in $(seq 1 50); do
    if [ "$(ps -o sid= -p "${pid}" | tr -d ' ')" = "${pid}" ]; then
        break
    fi
    sleep 0.1
done

if ! kill -0 "${pid}" 2>/dev/null; then
    echo "The live preview did not start.  See ${LOG}." >&2
    exit 1
fi

echo "Started the live preview on port ${PORT}.  Log: ${LOG}"
