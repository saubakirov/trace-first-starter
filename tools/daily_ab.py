#!/usr/bin/env python3
"""Reproducible A/B test of the Daily Task skill in a receiving project.

Each run: a detached git worktree of the receiving project at --base; the Daily package of the
variant's TFW source (a commit of this repository, WORKTREE for the current files, or a directory
holding the package paths) laid over it;
headless `claude -p` with a pre-generated session ID and Bash/PowerShell permission; then a second
turn on the same session (default «ок, принято»). The summary reports, per run and per variant
median: time, turns and context per call for the work turn and the close turn, permission
denials, the economics capture found in the record, and record size.

    python tools/daily_ab.py --project ../transcard-migration --base main \\
        --variant before=8923f7d9 --variant after=WORKTREE --runs 3 --out <temp>/tfw/ab.json
    python tools/daily_ab.py ... --runs 1 --variant after=WORKTREE --check   # permissions first
"""

import argparse
import json
import os
import shutil
import statistics
import subprocess
import sys
import time
import uuid
from pathlib import Path

TFW = Path(__file__).resolve().parents[1]
PACKAGE = [".tfw/extensions/daily-task", ".claude/skills/tfw-daily-task", ".tfw/economics"]
DEFAULT_TASK = ("/tfw-daily-task Добавь в README.md раздел «Что блокирует Ф1»: коротко перечисли, "
                "что сейчас мешает начать фазу 1, со ссылками на источники.")
TOOLS = ["Bash", "PowerShell", "Read", "Edit", "Write", "Glob", "Grep"]


def git(*args, cwd, check=True):
    return subprocess.run(["git", "-c", "core.longpaths=true"] + list(args), cwd=cwd, check=check, capture_output=True,
                          text=True, encoding="utf-8")


def overlay(target, source):
    """Replace the Daily package paths in target with the variant's bytes."""
    for rel in PACKAGE:
        path = target / rel
        if path.is_dir():
            shutil.rmtree(path)
    if source == "WORKTREE" or Path(source).is_dir():
        origin = TFW if source == "WORKTREE" else Path(source)
        for rel in PACKAGE:
            src = origin / rel
            if src.is_dir():
                shutil.copytree(src, target / rel, ignore=shutil.ignore_patterns("__pycache__"))
        return
    # git archive would honour export-ignore and drop .claude/, so read blobs directly.
    names = git("ls-tree", "-r", "--name-only", source, "--", *PACKAGE, cwd=TFW).stdout.splitlines()
    for name in names:
        blob = subprocess.run(["git", "cat-file", "blob", "{}:{}".format(source, name)], cwd=TFW,
                              check=True, capture_output=True).stdout
        path = target / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(blob)


PARENT_ONLY = {"CLAUDECODE", "CLAUDE_PID", "AI_AGENT", "CLAUDE_EFFORT", "CLAUDE_AGENT_SDK_VERSION",
               "CLAUDE_CODE_SESSION_ID", "CLAUDE_CODE_CHILD_SESSION", "CLAUDE_CODE_ENTRYPOINT",
               "CLAUDE_CODE_EXECPATH", "CLAUDE_CODE_SESSION_ATTENDED", "CLAUDE_CODE_MESSAGING_SOCKET",
               "CLAUDE_CODE_MESSAGING_TOKEN", "CLAUDE_CODE_ENABLE_SDK_FILE_CHECKPOINTING",
               "CLAUDE_CODE_QUESTION_PREVIEW_FORMAT", "CLAUDE_CODE_EMIT_STARTUP_TIMING",
               "CLAUDE_CODE_STARTUP_FAILURE_RESULTS", "CLAUDE_CODE_ENABLE_TASKS"}


def child_env():
    """A fresh launch: drop the parent session's identity, IPC and host flags; keep auth and paths."""
    return {k: v for k, v in os.environ.items() if k not in PARENT_ONLY}


def claude(binary, cwd, prompt, session, resume, timeout):
    argv = [binary, "-p", prompt, "--output-format", "json", "--allowedTools"] + TOOLS
    argv += ["--resume", session] if resume else ["--session-id", session]
    started = time.monotonic()
    try:
        proc = subprocess.run(argv, cwd=cwd, env=child_env(), capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=timeout)
    except subprocess.TimeoutExpired:
        return {"is_error": True, "result": "timeout after {} s".format(timeout),
                "wall_seconds": round(time.monotonic() - started, 1)}
    wall = time.monotonic() - started
    try:
        result = json.loads(proc.stdout)
    except ValueError:
        result = {"is_error": True, "result": (proc.stdout + proc.stderr)[-2000:]}
    result["wall_seconds"] = round(wall, 1)
    return result


def journal(session, config_root=None):
    root = Path(config_root or os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude") / "projects"
    matches = list(root.glob("*/{}.jsonl".format(session)))
    return matches[0] if len(matches) == 1 else None


def context_per_call(path, start, end=None):
    """Mean input context (fresh + cache read + cache write) per distinct assistant message."""
    per_message = {}
    with open(path, encoding="utf-8") as handle:
        for number, line in enumerate(handle):
            if number < start or (end is not None and number >= end):
                continue
            try:
                event = json.loads(line)
            except ValueError:
                continue
            if not isinstance(event, dict):
                continue
            message = event.get("message")
            if event.get("type") != "assistant" or not isinstance(message, dict) or event.get("agentId"):
                continue
            usage = message.get("usage") or {}
            per_message[message.get("id")] = (usage.get("input_tokens", 0) + usage.get("cache_read_input_tokens", 0)
                                              + usage.get("cache_creation_input_tokens", 0))
    return round(statistics.mean(per_message.values())) if per_message else None


def line_count(path):
    with open(path, "rb") as handle:
        return sum(1 for _ in handle)


def branches(project):
    return set(git("for-each-ref", "--format=%(refname:short)", "refs/heads", cwd=project).stdout.split())


def new_records(worktree, base):
    """Records the run added: committed since base (agents may commit on acceptance) or uncommitted."""
    committed = git("-c", "core.quotepath=false", "diff", "--name-only", base, "HEAD", cwd=worktree).stdout.splitlines()
    status = git("-c", "core.quotepath=false", "status", "--porcelain", "--untracked-files=all",
                 cwd=worktree).stdout.splitlines()
    paths = committed + [line[3:].strip() for line in status]
    return sorted({worktree / p for p in paths if p.startswith("daily/") and p.endswith("task.md")})


def capture(record):
    roles = record.parent / "economics" / "roles"
    files = sorted(roles.glob("*.jsonl")) if roles.is_dir() else []
    failures = 0
    for path in files:
        rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        failures += any(row.get("kind") == "failure" for row in rows)
    text = record.read_text(encoding="utf-8")
    gaps = text.count('"kind":"binding_unavailable"')
    unwritten = sum(path.stem not in text for path in files)
    return {"received": len(files), "failures": failures, "binding_gaps": gaps, "unwritten": unwritten}


def one_run(args, label, source, number, stamp):
    worktree = Path(args.work_dir) / stamp / "{}-{}".format(label, number)
    worktree.parent.mkdir(parents=True, exist_ok=True)
    run = {"variant": label, "source": source, "run": number, "worktree": str(worktree)}
    before = branches(args.project)
    try:
        git("worktree", "add", "--detach", str(worktree), args.base, cwd=args.project)
    except subprocess.CalledProcessError as exc:
        run["work"] = {"error": True, "message": exc.stderr[-500:], "denials": []}
        return run
    try:
        overlay(worktree, source)
        session = str(uuid.uuid4())
        run["session"] = session
        first = claude(args.claude, worktree, args.task, session, False, args.timeout)
        path = journal(session)
        boundary = line_count(path) if path else None
        second = None if args.check else claude(args.claude, worktree, args.close, session, True, args.timeout)
        for name, result, start, end in (("work", first, 0, boundary), ("close", second, boundary, None)):
            if result is None:
                continue
            run[name] = {"seconds": round(result.get("duration_ms", 0) / 1000, 1) or result["wall_seconds"],
                         "turns": result.get("num_turns"), "error": bool(result.get("is_error")),
                         "denials": [d.get("tool_name") for d in result.get("permission_denials", [])],
                         "context_per_call": context_per_call(path, start, end) if path and start is not None else None,
                         "cost_usd_reference": result.get("total_cost_usd")}
            if result.get("is_error"):
                run[name]["message"] = str(result.get("result"))[-500:]
        records = new_records(worktree, args.base)
        run["records"] = [str(r.relative_to(worktree)) for r in records]
        if records:
            run["record_bytes"] = records[-1].stat().st_size
            run["capture"] = capture(records[-1])
    finally:
        run["branches"] = sorted(branches(args.project) - before)
        if not args.keep:
            git("worktree", "remove", "--force", str(worktree), cwd=args.project, check=False)
            for name in run["branches"]:
                git("branch", "-D", name, cwd=args.project, check=False)
    return run


def median(values):
    values = [v for v in values if isinstance(v, (int, float))]
    return round(statistics.median(values), 1) if values else None


def summary(runs):
    lines = ["| variant | run | work s | work turns | work ctx/call | close s | close turns | capture | denials | record B |",
             "|---|---|---|---|---|---|---|---|---|---|"]

    def row(label, number, run):
        work, close = run.get("work", {}), run.get("close", {})
        cap = run.get("capture")
        cap_text = ("{received} received, {failures} failed, {binding_gaps} gaps, {unwritten} not written"
                    .format(**cap) if cap else "no record")
        denials = sorted(set(work.get("denials", []) + close.get("denials", [])))
        lines.append("| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(
            label, number, work.get("seconds"), work.get("turns"), work.get("context_per_call"),
            close.get("seconds"), close.get("turns"), cap_text, ", ".join(denials) or "none",
            run.get("record_bytes")))

    for run in runs:
        row(run["variant"], run["run"], run)
    for label in dict.fromkeys(r["variant"] for r in runs):
        group = [r for r in runs if r["variant"] == label]
        lines.append("| {} | median | {} | {} | {} | {} | {} | | | {} |".format(
            label, *(median([r.get(k, {}).get(m) for r in group]) for k, m in
                     (("work", "seconds"), ("work", "turns"), ("work", "context_per_call"),
                      ("close", "seconds"), ("close", "turns"))),
            median([r.get("record_bytes") for r in group])))
    return "\n".join(lines)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--project", required=True, help="receiving project repository")
    p.add_argument("--base", required=True, help="commit or ref of the receiving project")
    p.add_argument("--variant", action="append", required=True,
                   help="label=<commit of this repository>, label=WORKTREE, or label=<directory with the package>")
    p.add_argument("--runs", type=int, default=3)
    p.add_argument("--task", default=DEFAULT_TASK, help="first turn prompt")
    p.add_argument("--close", default="ок, принято", help="second turn prompt")
    p.add_argument("--check", action="store_true", help="first turn only; report permission denials")
    p.add_argument("--claude", default="claude")
    p.add_argument("--timeout", type=int, default=1800)
    p.add_argument("--work-dir", help="short path for worktrees (default: <project>/../worktree/daily-ab)")
    p.add_argument("--keep", action="store_true", help="keep worktrees and branches the runs created")
    p.add_argument("--out", help="write all run data as JSON")
    args = p.parse_args(argv)
    args.work_dir = args.work_dir or str(Path(args.project).resolve().parent / "worktree" / "daily-ab")
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    variants = []
    for item in args.variant:
        label, _, source = item.partition("=")
        if not (label and source):
            p.error("--variant needs label=source")
        if Path(source).is_dir():
            source = str(Path(source).resolve())
        elif source != "WORKTREE":
            source = git("rev-parse", "--verify", source + "^{commit}", cwd=TFW).stdout.strip()
        variants.append((label, source))
    stamp = time.strftime("%Y%m%d-%H%M%S")
    runs = []
    for number in range(1, args.runs + 1):
        for label, source in variants:
            print("run {} {} ...".format(label, number), file=sys.stderr, flush=True)
            runs.append(one_run(args, label, source, number, stamp))
            if args.out:
                Path(args.out).write_text(json.dumps(runs, ensure_ascii=False, indent=1), encoding="utf-8")
    print(summary(runs))
    if not args.keep:
        shutil.rmtree(Path(args.work_dir) / stamp, ignore_errors=True)
    return 0 if all(not r.get("work", {}).get("error") for r in runs) else 1


if __name__ == "__main__":
    sys.exit(main())
