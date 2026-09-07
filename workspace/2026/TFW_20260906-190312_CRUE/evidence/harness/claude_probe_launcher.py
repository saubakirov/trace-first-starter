from __future__ import annotations

import hashlib
import json
import os
import subprocess
from pathlib import Path


RUN_DIR = Path("/run/tfw/neutral-empty")
DEBUG = RUN_DIR / "debug-corrected-20260908.log"
STDOUT = RUN_DIR / "claude-corrected.stdout"
STDERR = RUN_DIR / "claude-corrected.stderr"
RESULT = RUN_DIR / "claude-corrected.result.json"
TIMEOUT_SECONDS = 45


def _digest(path: Path) -> tuple[int, str]:
    payload = path.read_bytes()
    return len(payload), hashlib.sha256(payload).hexdigest()


def main() -> None:
    argv = [
        "/usr/local/bin/claude",
        "--debug-file",
        str(DEBUG),
        "--setting-sources",
        "user",
        "--strict-mcp-config",
        "--mcp-config=/opt/tfw/empty-mcp.json",
        "--no-chrome",
        "--disable-slash-commands",
        "--tools",
        "",
        "--no-session-persistence",
        "--output-format",
        "json",
        "-p",
        "PREFLIGHT",
    ]
    for path in (DEBUG, STDOUT, STDERR, RESULT):
        path.unlink(missing_ok=True)
    with STDOUT.open("wb") as stdout, STDERR.open("wb") as stderr:
        child = subprocess.Popen(
            argv,
            cwd=str(RUN_DIR),
            env=os.environ.copy(),
            stdin=subprocess.DEVNULL,
            stdout=stdout,
            stderr=stderr,
        )
        timed_out = False
        try:
            exit_code = child.wait(timeout=TIMEOUT_SECONDS)
        except subprocess.TimeoutExpired:
            timed_out = True
            child.kill()
            exit_code = child.wait()
    stdout_bytes, stdout_sha256 = _digest(STDOUT)
    stderr_bytes, stderr_sha256 = _digest(STDERR)
    receipt = {
        "argv": argv,
        "cwd": str(RUN_DIR),
        "debug_path": str(DEBUG),
        "stdout_path": str(STDOUT),
        "stderr_path": str(STDERR),
        "timeout_seconds": TIMEOUT_SECONDS,
        "timed_out": timed_out,
        "child_exit_code": exit_code,
        "stdout_bytes": stdout_bytes,
        "stdout_sha256": stdout_sha256,
        "stderr_bytes": stderr_bytes,
        "stderr_sha256": stderr_sha256,
    }
    RESULT.write_text(json.dumps(receipt, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
