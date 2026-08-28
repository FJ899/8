from __future__ import annotations

import sys

# This entrypoint is the supported G1 evidence launcher.  The isolation check
# deliberately occurs before importing any path-sensitive Python module.
if not sys.flags.isolated:
    raise SystemExit("G1 evidence requires isolated Python: invoke with python -I")

import runpy
from pathlib import Path

SCRIPT = Path(__file__).resolve().with_name("capture_g1_evidence.py")
runpy.run_path(str(SCRIPT), run_name="__main__")
