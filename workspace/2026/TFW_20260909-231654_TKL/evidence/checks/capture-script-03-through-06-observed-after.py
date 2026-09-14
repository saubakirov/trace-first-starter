"""Capture upstream checks as raw evidence; never installed in a receiver."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import time
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
label, executable, *arguments = sys.argv[1:]
destination = HERE / "checks" / label
destination.mkdir(parents=True, exist_ok=False)
paths = json.loads((HERE / "checks/01-02-source-before-corrections.json").read_text(encoding="utf-8"))["paths"]

def source_state():
    return {name: ({"bytes": (ROOT / name).stat().st_size,
                   "sha256": hashlib.sha256((ROOT / name).read_bytes()).hexdigest()}
                  if (ROOT / name).is_file() else {"absent": True}) for name in paths}

before = source_state()
with zipfile.ZipFile(destination / "source-before.zip", "w", zipfile.ZIP_DEFLATED) as archive:
    for name in paths:
        if (ROOT / name).is_file(): archive.write(ROOT / name, name)
(destination / "source-before.json").write_text(json.dumps(before, indent=2) + "\n", encoding="utf-8")
command = [executable, *arguments]
started = datetime.now(timezone.utc).isoformat()
clock = time.perf_counter()
environment = os.environ.copy()
environment["PYTHONIOENCODING"] = "utf-8"
with (destination / "stdout.txt").open("wb") as out, (destination / "stderr.txt").open("wb") as err:
    result = subprocess.run(command, cwd=ROOT, env=environment, stdout=out, stderr=err)
receipt = {
    "argv": command, "cwd": ROOT.as_posix(), "started": started,
    "finished": datetime.now(timezone.utc).isoformat(),
    "seconds": time.perf_counter() - clock, "exit_code": result.returncode,
    "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
    "source_unchanged": before == source_state(),
    "source_archive_sha256": hashlib.sha256((destination / "source-before.zip").read_bytes()).hexdigest(),
    "streams": {p.name: {"bytes": p.stat().st_size,
                           "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
                for p in destination.glob("*.txt")},
}
(destination / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2), flush=True)
print((destination / "stdout.txt").read_text(encoding="utf-8", errors="replace")[-18000:], flush=True)
print((destination / "stderr.txt").read_text(encoding="utf-8", errors="replace")[-3000:], flush=True)
raise SystemExit(result.returncode)
