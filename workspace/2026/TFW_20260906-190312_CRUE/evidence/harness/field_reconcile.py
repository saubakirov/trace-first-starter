from __future__ import annotations

import hashlib
import json
import os
import pathlib
import re
import subprocess


project = pathlib.Path(os.environ["TFW_RECONCILE_PROJECT"])


def captured(argv: list[str]) -> bytes:
    return subprocess.run(argv, cwd=str(project), stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, check=False).stdout


status = captured(["git", "status", "--porcelain=v1"])
head = captured(["git", "rev-parse", "HEAD"]).decode("utf-8", "replace").strip()
source = captured(["git", "-c", "safe.directory=.tfw/.upstream", "-C", ".tfw/.upstream", "rev-parse", "HEAD"]).decode("utf-8", "replace").strip()
version = (project / ".tfw/VERSION").read_text(encoding="utf-8").strip()
config = (project / ".tfw/project_config.yaml").read_text(encoding="utf-8")
version_match = re.search(r"(?m)^\s*version:\s*[\"']?([^\"'\s]+)", config)
installed_match = re.search(r"(?m)^\s*installed_from:\s*[\"']?([^\"'\n]+)", config)
receipt_count = len(list((project / ".tfw/update_receipts").glob("*"))) if (project / ".tfw/update_receipts").exists() else 0
commands = len(list((project / ".claude/commands").glob("tfw-*.md")))
legacy_commands = len(list((project / ".agent/workflows").glob("tfw-*.md")))
print(json.dumps({
    "receiver_head": head,
    "source_head": source,
    "version_file": version,
    "config_tfw_version": version_match.group(1) if version_match else None,
    "installed_from_present": bool(installed_match),
    "installed_from_sha_present": bool(installed_match and re.search(r"[0-9a-f]{40}", installed_match.group(1))),
    "status_lines": status.count(b"\n"),
    "status_bytes": len(status),
    "status_sha256": hashlib.sha256(status).hexdigest(),
    "receipt_count": receipt_count,
    "claude_tfw_command_count": commands,
    "legacy_tfw_command_count": legacy_commands,
}, sort_keys=True))
