from __future__ import annotations

import hashlib
import json
import os
import subprocess
import time
from pathlib import Path


SLOT = os.environ["TFW_FIELD_SLOT"]
PROJECT = Path(os.environ["TFW_FIELD_PROJECT"]).resolve()
PROVIDER = os.environ["TFW_FIELD_PROVIDER"]
PROMPT_PATH = Path(os.environ["TFW_FIELD_PROMPT_PATH"])
RUN_DIR = PROJECT.parent
STDOUT = RUN_DIR / "stdout.raw"
STDERR = RUN_DIR / "stderr.raw"
RESULT = RUN_DIR / "launcher-result.json"
DEBUG = RUN_DIR / "provider-debug.log"
SAFE_REPORT = RUN_DIR / "safe-report.json"
TIMEOUT_SECONDS = 900


def digest(path: Path) -> tuple[int, str]:
    h = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            size += len(chunk)
            h.update(chunk)
    return size, h.hexdigest()


def run_capture(argv: list[str], cwd: Path, env: dict[str, str], timeout: int | None = None) -> tuple[int, bytes]:
    completed = subprocess.run(argv, cwd=str(cwd), env=env, stdin=subprocess.DEVNULL,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               timeout=timeout, check=False)
    return completed.returncode, completed.stdout


def git_snapshot() -> dict[str, object]:
    code, head = run_capture(["git", "rev-parse", "HEAD"], PROJECT, os.environ.copy())
    status_code, status = run_capture(["git", "status", "--porcelain=v1"], PROJECT, os.environ.copy())
    status_size = len(status)
    return {
        "head_exit_code": code,
        "head_sha256": hashlib.sha256(head).hexdigest(),
        "status_exit_code": status_code,
        "status_lines": status.count(b"\n"),
        "status_bytes": status_size,
        "status_sha256": hashlib.sha256(status).hexdigest(),
    }


def safe_json_metadata(stdout: bytes) -> dict[str, object]:
    lines = [line for line in stdout.splitlines() if line.strip()]
    records: list[dict[str, object]] = []
    for line in lines:
        try:
            value = json.loads(line)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if isinstance(value, dict):
            records.append(value)
    metadata: dict[str, object] = {
        "json_records": len(records),
        "record_types": sorted({str(item.get("type")) for item in records if item.get("type") is not None}),
        "item_types": sorted({str(item.get("item", {}).get("type")) for item in records
                               if isinstance(item.get("item"), dict) and item["item"].get("type") is not None}),
    }
    for item in reversed(records):
        if item.get("type") == "thread.started":
            metadata.update({
                "thread_id": item.get("thread_id"),
                "thread_model": item.get("model"),
            })
        if item.get("type") == "result":
            metadata.update({
                "result_subtype": item.get("subtype"),
                "is_error": item.get("is_error"),
                "stop_reason": item.get("stop_reason"),
                "terminal_reason": item.get("terminal_reason"),
                "num_turns": item.get("num_turns"),
                "model": item.get("model"),
                "session_id": item.get("session_id"),
                "uuid": item.get("uuid"),
                "session_id_present": bool(item.get("session_id")),
                "uuid_present": bool(item.get("uuid")),
                "result_text_bytes": len(str(item.get("result", "")).encode("utf-8")),
                "result_text_sha256": hashlib.sha256(str(item.get("result", "")).encode("utf-8")).hexdigest(),
            })
            break
    return metadata


def redact_text(value: object) -> str:
    text = str(value or "")
    import re
    patterns = [
        (r"(?i)(authorization|proxy-authorization|bearer|api[_ -]?key|access[_ -]?token|refresh[_ -]?token|password|secret|credential)\s*[:=]\s*\S+", r"\1=<REDACTED>"),
        (r"(?i)(set-cookie|cookie)\s*:\s*[^\r\n]+", r"\1: <REDACTED>"),
        (r"(?<![A-Za-z0-9])[A-Za-z0-9_+/=-]{96,}(?![A-Za-z0-9])", "<REDACTED_LONG_TOKEN>"),
    ]
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)
    return text


def safe_action_records(stdout: bytes) -> list[dict[str, object]]:
    records = []
    for line in stdout.splitlines():
        try:
            value = json.loads(line)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(value, dict):
            continue
        if value.get("type") == "result":
            records.append({
                "event": "result",
                "subtype": value.get("subtype"),
                "stop_reason": value.get("stop_reason"),
                "terminal_reason": value.get("terminal_reason"),
                "session_id": value.get("session_id"),
                "uuid": value.get("uuid"),
                "assistant_text": redact_text(value.get("result")),
            })
            continue
        if value.get("type") == "thread.started":
            records.append({"event": "thread.started", "thread_id": value.get("thread_id"),
                            "model": value.get("model")})
            continue
        if value.get("type") != "item.completed" or not isinstance(value.get("item"), dict):
            continue
        item = value["item"]
        item_type = item.get("type")
        safe: dict[str, object] = {"event": "item.completed", "item_type": item_type}
        if item_type == "agent_message":
            safe["assistant_text"] = redact_text(item.get("text"))
        elif item_type == "command_execution":
            safe.update({"command": redact_text(item.get("command")),
                         "status": item.get("status"), "exit_code": item.get("exit_code"),
                         "duration_ms": item.get("duration_ms")})
        elif item_type == "file_change":
            diff = item.get("diff")
            safe.update({"path": item.get("path"), "kind": item.get("kind"),
                         "additions": item.get("additions"), "deletions": item.get("deletions"),
                         "diff_sha256": hashlib.sha256(str(diff).encode()).hexdigest() if diff else None})
        else:
            safe["keys"] = sorted(str(key) for key in item.keys())
        records.append(safe)
    return records


def main() -> None:
    prompt = PROMPT_PATH.read_text(encoding="utf-8")
    if PROVIDER == "claude":
        proxy = "http://127.0.0.1:3128"
        argv = [
            "/usr/local/bin/claude", "--debug-file", str(DEBUG),
            "--setting-sources", "project,local", "--strict-mcp-config",
            "--mcp-config=/opt/tfw/empty-mcp.json", "--no-chrome",
            "--permission-mode", "bypassPermissions", "--tools",
            "Bash,Read,Edit,Write,Glob,Grep", "--no-session-persistence",
            "--output-format", "json", "--add-dir", str(PROJECT), "-p", prompt,
        ]
    elif PROVIDER == "codex":
        disabled = [
            "plugins", "plugin_sharing", "remote_plugin", "browser_use", "browser_use_external",
            "browser_use_full_cdp_access", "computer_use", "multi_agent", "in_app_browser",
            "in_app_chat", "in_app_local_automation", "tool_call_mcp_elicitation",
            "skill_mcp_dependency_install", "unbounded_connection_retries",
        ]
        proxy = "http://127.0.0.1:3129"
        argv = [
            "/usr/local/bin/codex", "exec", "--model", "gpt-5.6-sol", "--json", "--ephemeral",
            "--sandbox", "workspace-write", "--ignore-user-config",
            "-c", "mcp_servers={}", "-c", 'web_search="disabled"',
            "-C", str(PROJECT),
        ]
        for feature in disabled:
            argv.extend(["--disable", feature])
        argv.append(prompt)
    else:
        raise ValueError(f"unsupported provider: {PROVIDER}")

    env = os.environ.copy()
    env.update({
        "HOME": "/run/tfw/runtime-home",
        "TMPDIR": "/run/tfw/runtime-tmp",
        "HTTP_PROXY": proxy,
        "HTTPS_PROXY": proxy,
        "ALL_PROXY": proxy,
        "http_proxy": proxy,
        "https_proxy": proxy,
        "all_proxy": proxy,
        "NO_PROXY": "127.0.0.1,localhost",
        "no_proxy": "127.0.0.1,localhost",
    })
    if PROVIDER == "claude":
        env["CLAUDE_CONFIG_DIR"] = "/run/tfw/auth/claude"
    else:
        env["CODEX_HOME"] = "/run/tfw/auth/codex"

    for path in (STDOUT, STDERR, RESULT, DEBUG, SAFE_REPORT):
        path.unlink(missing_ok=True)
    before = git_snapshot()
    started = time.time()
    timed_out = False
    with STDOUT.open("wb") as stdout, STDERR.open("wb") as stderr:
        child = subprocess.Popen(argv, cwd=str(PROJECT), env=env, stdin=subprocess.DEVNULL,
                                 stdout=stdout, stderr=stderr)
        try:
            exit_code = child.wait(timeout=TIMEOUT_SECONDS)
        except subprocess.TimeoutExpired:
            timed_out = True
            child.kill()
            exit_code = child.wait()
    after = git_snapshot()
    stdout_bytes, stdout_sha256 = digest(STDOUT)
    stderr_bytes, stderr_sha256 = digest(STDERR)
    raw_stdout = STDOUT.read_bytes()
    safe_report = {
        "slot": SLOT,
        "provider": PROVIDER,
        "native_identity": safe_json_metadata(raw_stdout),
        "actions_and_assistant_text": safe_action_records(raw_stdout),
        "raw_output_retained_privately": True,
        "raw_output_sha256": stdout_sha256,
        "raw_output_bytes": stdout_bytes,
    }
    SAFE_REPORT.write_text(json.dumps(safe_report, sort_keys=True) + "\n", encoding="utf-8")
    safe_report_bytes, safe_report_sha256 = digest(SAFE_REPORT)
    receipt = {
        "slot": SLOT,
        "provider": PROVIDER,
        "project": str(PROJECT),
        "cwd": str(PROJECT),
        "argv_without_prompt": argv[:-1],
        "prompt_utf8_bytes": len(prompt.encode("utf-8")),
        "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        "started_epoch": started,
        "duration_seconds": round(time.time() - started, 3),
        "timeout_seconds": TIMEOUT_SECONDS,
        "timed_out": timed_out,
        "child_exit_code": exit_code,
        "stdout_bytes": stdout_bytes,
        "stdout_sha256": stdout_sha256,
        "stderr_bytes": stderr_bytes,
        "stderr_sha256": stderr_sha256,
        "safe_report_path": str(SAFE_REPORT),
        "safe_report_bytes": safe_report_bytes,
        "safe_report_sha256": safe_report_sha256,
        "safe_provider_metadata": safe_json_metadata(raw_stdout),
        "git_before": before,
        "git_after": after,
    }
    RESULT.write_text(json.dumps(receipt, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
