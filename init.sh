#!/usr/bin/env bash
# init.sh — everything needed to work on bayesian-stats: Python check, venv/, pinned dependencies.
# Idempotent: a second run reuses venv/ (pass --clean to rebuild it). The pins (numpy 1.26.4, scipy 1.12.0) ship wheels for Python 3.9 to 3.12.
#   ./init.sh            set up or refresh
#   ./init.sh --clean    remove venv/ first
#   ./init.sh --help     this text
set -euo pipefail
cd "$(dirname "$0")"

VENV=venv
CLEAN=0
case "${1:-}" in
  -h|--help|help) sed -n '2,6p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
  --clean) CLEAN=1 ;;
  '') ;;
  *) echo "init.sh: unknown option: $1 (see ./init.sh --help)" >&2; exit 2 ;;
esac

pick_python() {
  local c
  for c in python3.12 python3.11 python3; do
    if command -v "$c" >/dev/null 2>&1; then echo "$c"; return 0; fi
  done
  echo "init.sh: no suitable python3 found on PATH (tried: python3.12 python3.11 python3)" >&2
  return 1
}

if [ "$CLEAN" -eq 1 ] && [ -d "$VENV" ]; then echo "Removing $VENV (--clean)"; rm -rf "$VENV"; fi
if [ -x "$VENV/bin/python" ]; then
  echo "Reusing $VENV ($("$VENV/bin/python" --version))"
else
  PY="$(pick_python)"
  echo "Creating $VENV with $("$PY" --version) ($PY)"
  "$PY" -m venv "$VENV"
fi
echo "Installing pinned dependencies"
"$VENV/bin/python" -m pip install --quiet --disable-pip-version-check -r requirements.txt

echo "Ready. Next: ./test.sh, then ./run.sh"
