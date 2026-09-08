from __future__ import annotations

import hashlib
import json
import os
import pathlib
import subprocess


auth_path = pathlib.Path(os.environ["TFW_CHECK_AUTH_PATH"])
payload = auth_path.read_bytes()
parsed = json.loads(payload)
for path in (pathlib.Path("/run/tfw/runtime-home/check-write"),
             pathlib.Path("/run/tfw/runtime-tmp/check-write")):
    path.write_text("ok", encoding="utf-8")
try:
    pathlib.Path("/run/tfw/source/.write-check").write_text("blocked", encoding="utf-8")
    source_write_exit = 0
except OSError:
    source_write_exit = 1
head = subprocess.check_output(
    ["git", "-c", "safe.directory=/run/tfw/source", "-C", "/run/tfw/source", "rev-parse", "HEAD"],
    text=True,
).strip()
remote = subprocess.check_output(
    ["git", "-c", "safe.directory=/run/tfw/source", "-C", "/run/tfw/source", "remote", "-v"],
    text=True,
)
print(json.dumps({
    "uid": os.getuid(),
    "cwd": os.getcwd(),
    "home": os.environ.get("HOME"),
    "tmpdir": os.environ.get("TMPDIR"),
    "auth_bytes": len(payload),
    "auth_sha256": hashlib.sha256(payload).hexdigest(),
    "auth_json_object": isinstance(parsed, dict),
    "source_head": head,
    "source_remote_chars": len(remote),
    "source_write_exit": source_write_exit,
}, sort_keys=True))
