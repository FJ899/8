from pathlib import Path
import os

marker = os.environ.get("AK_G1_HOSTILE_MARKER")
if marker:
    Path(marker).write_text("HOSTILE_JSON_EXECUTED\n", encoding="utf-8")
raise RuntimeError("hostile json.py executed")
