from __future__ import annotations

import hashlib
import json
import os
import subprocess
import time
from pathlib import Path


SLOT = os.environ["TFW_ID_SLOT"]
PROVIDER = os.environ["TFW_ID_PROVIDER"]
PROMPT = os.environ["TFW_ID_PROMPT"]
WORK = Path("/run/tfw/field")
EMPTY_CWD = Path("/run/tfw/runtime-home")
STDOUT = WORK / "identity.stdout"
STDERR = WORK / "identity.stderr"
RESULT = WORK / "identity.result.json"
DEBUG = WORK / "identity.debug.log"
TIMEOUT_SECONDS = 60


def digest(path: Path) -> tuple[int, str]:
    h = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            size += len(chunk)
            h.update(chunk)
    return size, h.hexdigest()


def parse_records(payload: bytes) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for line in payload.splitlines():
        try:
            value = json.loads(line)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if isinstance(value, dict):
            records.append(value)
    return records


def safe_metadata(payload: bytes) -> dict[str, object]:
    records = parse_records(payload)
    metadata: dict[str, object] = {
        "json_records": len(records),
        "record_types": sorted({str(v.get("type")) for v in records if v.get("type") is not None}),
        "item_types": sorted({str(v.get("item", {}).get("type")) for v in records
                               if isinstance(v.get("item"), dict) and v["item"].get("type") is not None}),
    }
    for value in records:
        if value.get("type") == "thread.started":
            metadata["thread_id"] = value.get("thread_id")
            metadata["model"] = value.get("model")
        if value.get("type") == "result":
            metadata.update({
                "result_subtype": value.get("subtype"),
                "is_error": value.get("is_error"),
                "stop_reason": value.get("stop_reason"),
                "terminal_reason": value.get("terminal_reason"),
                "model": value.get("model", metadata.get("model")),
                "session_id": value.get("session_id"),
                "uuid": value.get("uuid"),
            })
    return metadata


def main() -> None:
    proxy = "http://127.0.0.1:3128" if PROVIDER == "claude" else "http://127.0.0.1:3129"
    if PROVIDER == "claude":
        argv = [
            "/usr/local/bin/claude", "--debug-file", str(DEBUG), "--setting-sources", "user",
            "--strict-mcp-config", "--mcp-config=/opt/tfw/empty-mcp.json", "--no-chrome",
            "--disable-slash-commands", "--tools", "", "--no-session-persistence",
            "--output-format", "json", "-p", PROMPT,
        ]
    elif PROVIDER == "codex":
        disabled = [
            "plugins", "plugin_sharing", "remote_plugin", "browser_use", "browser_use_external",
            "browser_use_full_cdp_access", "computer_use", "multi_agent", "in_app_browser",
            "in_app_chat", "in_app_local_automation", "tool_call_mcp_elicitation",
            "skill_mcp_dependency_install", "unbounded_connection_retries",
        ]
        argv = [
            "/usr/local/bin/codex", "exec", "--model", "gpt-5.6-sol", "--json", "--ephemeral",
            "--sandbox", "read-only", "--ignore-user-config", "-c", "mcp_servers={}", "-c",
            'web_search="disabled"', "-C", str(EMPTY_CWD), "--skip-git-repo-check",
        ]
        for feature in disabled:
            argv.extend(["--disable", feature])
        argv.append(PROMPT)
    else:
        raise ValueError(PROVIDER)
    env = os.environ.copy()
    env.update({"HOME": "/run/tfw/runtime-home", "TMPDIR": "/run/tfw/runtime-tmp",
                "HTTP_PROXY": proxy, "HTTPS_PROXY": proxy, "ALL_PROXY": proxy,
                "http_proxy": proxy, "https_proxy": proxy, "all_proxy": proxy,
                "NO_PROXY": "127.0.0.1,localhost", "no_proxy": "127.0.0.1,localhost"})
    if PROVIDER == "claude":
        env["CLAUDE_CONFIG_DIR"] = "/run/tfw/auth/claude"
    else:
        env["CODEX_HOME"] = "/run/tfw/auth/codex"
    for path in (STDOUT, STDERR, RESULT, DEBUG):
        path.unlink(missing_ok=True)
    started = time.time()
    with STDOUT.open("wb") as stdout, STDERR.open("wb") as stderr:
        child = subprocess.Popen(argv, cwd=str(EMPTY_CWD), env=env, stdin=subprocess.DEVNULL,
                                 stdout=stdout, stderr=stderr)
        timed_out = False
        try:
            exit_code = child.wait(timeout=TIMEOUT_SECONDS)
        except subprocess.TimeoutExpired:
            timed_out = True
            child.kill()
            exit_code = child.wait()
    stdout_bytes, stdout_sha256 = digest(STDOUT)
    stderr_bytes, stderr_sha256 = digest(STDERR)
    payload = STDOUT.read_bytes()
    receipt = {"slot": SLOT, "provider": PROVIDER, "cwd": str(EMPTY_CWD),
               "requested_model": "gpt-5.6-sol" if PROVIDER == "codex" else None,
               "argv_without_prompt": argv[:-1],
               "prompt_sha256": hashlib.sha256(PROMPT.encode()).hexdigest(),
               "timeout_seconds": TIMEOUT_SECONDS, "timed_out": timed_out,
               "child_exit_code": exit_code, "duration_seconds": round(time.time() - started, 3),
               "stdout_bytes": stdout_bytes, "stdout_sha256": stdout_sha256,
               "stderr_bytes": stderr_bytes, "stderr_sha256": stderr_sha256,
               "safe_provider_metadata": safe_metadata(payload)}
    RESULT.write_text(json.dumps(receipt, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
