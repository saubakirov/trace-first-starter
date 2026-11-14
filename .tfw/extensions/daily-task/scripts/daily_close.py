#!/usr/bin/env python3
"""Capture the worker's own economics snapshot for a Daily record in one command.

Finds the worker's own Claude Code journal by exact session ID (never the newest file), runs the
economics helper's collect (with --predecessor after the first revision of the same source) and
receive, and prints the revision line for the record. A failed collect is written as a received
failure receipt; an unknown owner or an unfound own source is written as a binding gap in the
record. Run at close, at interruption and at handover only. The work is never blocked by it.

Inside a subagent CLAUDE_CODE_SESSION_ID names the parent: pass --agent-id, or capture by hand.

Exit codes: 0 captured; 3 failure or binding gap written; 2 nothing could be written.
"""

import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
EXTENSION = SCRIPTS.parent
HELPER = EXTENSION.parent.parent / "economics" / "tfw_economics.py"
BINDING = re.compile(r"<!-- tfw-economics-record-v1 (\{[^\n]*\}) -->")
STATES = ("prepared", "checked", "accepted")
SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")
CLAUDE_PROVIDER = "claude.code-jsonl"


class DailyError(Exception):
    pass


def utf8_stdout():
    for stream in (sys.stdout, sys.stderr):
        encoding = (getattr(stream, "encoding", "") or "").lower().replace("-", "")
        if encoding != "utf8" and hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def load_helper():
    if not HELPER.is_file():
        raise DailyError("economics helper missing: " + str(HELPER))
    spec = importlib.util.spec_from_file_location("tfw_economics", HELPER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def now():
    return dt.datetime.now().astimezone().replace(microsecond=0)


def read_text(path):
    """Read without newline translation, so writes keep the file's own line endings."""
    with open(path, encoding="utf-8", newline="") as handle:
        return handle.read()


def write_text(path, text):
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def read_binding(record):
    text = read_text(record)
    blocks = BINDING.findall(text)
    if len(blocks) != 1:
        raise DailyError("record needs exactly one economics binding block, found {}".format(len(blocks)))
    return json.loads(blocks[0])


def binding_line(fields):
    return "<!-- tfw-economics-record-v1 " + json.dumps(fields, ensure_ascii=False, separators=(",", ":")) + " -->"


def write_binding(record, fields):
    text = read_text(record)
    new, count = BINDING.subn(lambda _m: binding_line(fields), text)
    if count != 1:
        raise DailyError("record needs exactly one economics binding block")
    write_text(record, new)


def insert_before_binding(record, line):
    text = read_text(record)
    match = BINDING.search(text)
    if not match:
        raise DailyError("record has no economics binding block")
    if line in text:
        return
    newline = "\r\n" if "\r\n" in text else "\n"
    write_text(record, text[:match.start()] + line + newline * 2 + text[match.start():])


def binding_gap(producer, observed_at, code, detail, known, unavailable, last_good=None):
    return {"kind": "binding_unavailable", "producer": producer, "observed_at": observed_at,
            "code": code, "detail": detail, "known": known, "unavailable": unavailable,
            "attempted_extraction": False, "last_good": last_good}


def claude_root(config_root=None):
    if config_root:
        return Path(config_root)
    env = os.environ.get("CLAUDE_CONFIG_DIR")
    return Path(env) if env else Path.home() / ".claude"


def find_claude_journals(session_id, agent_id=None, config_root=None):
    """Exact-filename matches only; never the newest journal."""
    projects = claude_root(config_root) / "projects"
    if not projects.is_dir():
        return []
    if agent_id:
        pattern = "*/{}/subagents/agent-{}.jsonl".format(session_id, agent_id)
    else:
        pattern = "*/{}.jsonl".format(session_id)
    return sorted(projects.glob(pattern))


def resolve_claude_source(session_id, agent_id=None, config_root=None):
    """Return (path, source_id) or raise DailyError with a gap code."""
    if not session_id:
        raise DailyError("session_unknown: no --session-id and no CLAUDE_CODE_SESSION_ID")
    for value in (session_id, agent_id):
        if value is not None and not SAFE_ID.match(value):
            raise DailyError("session_invalid: {!r} is not a session or agent ID".format(value))
    matches = find_claude_journals(session_id, agent_id, config_root)
    if not matches:
        raise DailyError("source_not_found: no {} journal under {}".format(
            session_id + ("/" + agent_id if agent_id else ""), claude_root(config_root) / "projects"))
    if len(matches) > 1:
        raise DailyError("source_ambiguous: " + ", ".join(str(m) for m in matches))
    source_id = session_id + ("/" + agent_id if agent_id else "")
    return matches[0], source_id


def complete_lines(path):
    """Complete JSONL lines, counted as the economics helper counts them."""
    raw = Path(path).read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw = raw[:raw.rfind(b"\n") + 1]
    return raw.splitlines()


def journal_version(path, session_id):
    """The Claude Code version the journal itself records for this session."""
    version = None
    with open(path, "rb") as handle:
        for raw in handle:
            try:
                row = json.loads(raw)
            except ValueError:
                continue
            if isinstance(row, dict) and row.get("sessionId") == session_id and row.get("version"):
                version = row["version"]
    return version


def received_files(helper, task_root):
    """Validated received contributions under economics/roles (helper.validate_file items)."""
    folder = Path(task_root) / "economics" / "roles"
    if not folder.is_dir():
        return []
    return [helper.validate_file(path) for path in sorted(folder.glob("*.jsonl"))]


def is_failure(item):
    return any(row["kind"] == "failure" for row in item["rows"])


def run_helper(*argv):
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
    proc = subprocess.run([sys.executable, str(HELPER)] + list(argv), env=env,
                          capture_output=True, text=True, encoding="utf-8", errors="replace")
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def number(value):
    return "{:,}".format(value)


def token_text(tokens):
    parts = ["cache read " + number(tokens["cached"])]
    if tokens.get("cache_write_1h"):
        parts.append("cache write 1 h " + number(tokens["cache_write_1h"]))
    if tokens.get("cache_write_5m"):
        parts.append("cache write 5 min " + number(tokens["cache_write_5m"]))
    parts.append("fresh " + number(tokens["fresh"]))
    output = "output " + number(tokens["output"])
    if tokens.get("reasoning"):
        output += " (reasoning {})".format(number(tokens["reasoning"]))
    parts.append(output)
    return "{} tokens — {}".format(number(tokens["total"]), ", ".join(parts))


def covers(revision):
    if revision == 1:
        return "Revision 1"
    if revision == 2:
        return "Revision 2 (covers revision 1, do not add)"
    return "Revision {} (covers revisions 1–{}, do not add)".format(revision, revision - 1)


def revision_line(item, label=None):
    m = item["manifest"]
    cutoff = m["cutoff"][:19] + "Z" if m["cutoff"].endswith("+00:00") else m["cutoff"]
    head = "{}{}: lines `[{}, {})`, `--complete`, cutoff {}, sha256 `{}`".format(
        covers(m["revision"]), ", " + label if label else "", m["range_start"], m["range_end"],
        cutoff, item["sha256"])
    per_model = {}
    for row in item["rows"]:
        model = per_model.setdefault(row["model"], {"responses": 0, "tokens": {}})
        model["responses"] += row["extensions"].get("tfw.native_event_count", 1)
        for key, value in row["tokens"].items():
            model["tokens"][key] = model["tokens"].get(key, 0) + (value or 0)
    models = ["model `{}`, {} responses: {}".format(name, data["responses"], token_text(data["tokens"]))
              for name, data in sorted(per_model.items())]
    return head + "; " + "; ".join(models) + "."


def failure_line(item, last_good):
    m = item["manifest"]
    row = item["rows"][0]
    good = "last good revision {} `{}`".format(last_good["manifest"]["revision"], last_good["sha256"]) \
        if last_good else "no earlier good revision"
    return ("Revision {} failed, unmeasured: attempted lines `[{}, {})`, code `{}`: {}; receipt sha256 `{}`; "
            "{}.").format(m["revision"], m["range_start"], m["range_end"], row["code"], row["detail"],
                         item["sha256"], good)


def record_gap(record, fields, unit, code, detail, known, unavailable, last_good):
    """Add a binding gap unless the same producer already recorded the same code and last good."""
    last = last_good["sha256"] if last_good else None
    outcomes = fields.setdefault("binding_outcomes", [])
    if not any(g["producer"] == unit and g["code"] == code and g["last_good"] == last for g in outcomes):
        outcomes.append(binding_gap(unit, now().isoformat(), code, detail, known, unavailable, last))
        write_binding(record, fields)
    return "Binding gap `{}`: {}; nothing collected.".format(code, detail)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--record", required=True, help="the record file with the binding block")
    p.add_argument("--session-id", default=os.environ.get("CLAUDE_CODE_SESSION_ID"),
                   help="own Claude Code session (default: CLAUDE_CODE_SESSION_ID)")
    p.add_argument("--agent-id", help="capture this session's subagent journal instead")
    p.add_argument("--source", help="explicit source file (other providers); needs --source-id")
    p.add_argument("--source-id")
    p.add_argument("--provider", default=CLAUDE_PROVIDER)
    p.add_argument("--source-version", help="default: the version the journal records")
    p.add_argument("--unit", help="default: claude-code:<source ID>")
    p.add_argument("--start", type=int, default=0,
                   help="first line of this record's work in the source: 0 when the session began with it")
    p.add_argument("--write", action="store_true", help="insert the line into the record before the binding block")
    p.add_argument("--state", choices=STATES, help="set result_state to what the record already holds")
    p.add_argument("--report", action="store_true", help="also print the helper's report for the summary")
    p.add_argument("--config-root", help=argparse.SUPPRESS)
    args = p.parse_args(argv)
    utf8_stdout()
    record = Path(args.record).resolve()
    root = record.parent
    try:
        helper = load_helper()
        helper.status_fields(root, record)
        fields = read_binding(record)
        received = received_files(helper, root)
    except (DailyError, ValueError, OSError) as exc:
        print("daily_close: " + str(exc), file=sys.stderr)
        return 2
    if args.source and not args.source_id:
        print("daily_close: --source needs --source-id", file=sys.stderr)
        return 2
    start = args.start
    if args.source:
        source, source_id = Path(args.source), args.source_id
    else:
        source_id = (args.session_id or "") + ("/" + args.agent_id if args.agent_id else "")
        try:
            source, source_id = resolve_claude_source(args.session_id, args.agent_id, args.config_root)
        except DailyError as exc:
            source = None
            code, _, detail = str(exc).partition(": ")
    unit = args.unit or "claude-code:" + (source_id or "unknown")
    mine = [i for i in received if i["manifest"]["source_id"] == source_id and i["manifest"]["unit"] == unit]
    good = [i for i in received if not is_failure(i)]
    last_good = max([i for i in good if i in mine] or good,
                    key=lambda i: i["manifest"]["captured_at"], default=None)
    status = 3
    if source is None:
        line = record_gap(record, fields, unit, code, detail,
                          {"provider": args.provider, "session_id": args.session_id},
                          {"source": detail}, last_good)
    elif fields.get("owner") is None:
        line = record_gap(record, fields, unit, "owner_unknown", "owner ID not in the binding block",
                          {"provider": args.provider, "source_id": source_id}, {"owner": "not supplied"},
                          last_good)
    else:
        version = args.source_version or (journal_version(source, args.session_id)
                                          if args.provider == CLAUDE_PROVIDER else None)
        if not version:
            print("daily_close: source version unknown; pass --source-version", file=sys.stderr)
            return 2
        try:
            lines = len(complete_lines(source))
        except OSError:
            lines = None
        if lines is None or lines <= start:
            reason = "source unreadable" if lines is None else \
                "source has {} complete lines, not more than start line {}".format(lines, start)
            line = record_gap(record, fields, unit, "range_unknown", reason,
                              {"provider": args.provider, "source_id": source_id, "range_start": start},
                              {"range_end": reason}, last_good)
        else:
            result = capture(args, record, fields, source, source_id, unit, version, start, lines, mine)
            if result is None:
                return 2
            item, failed = result
            item = helper.validate_file(item)
            if failed:
                line = failure_line(item, last_good)
            else:
                status = 0
                label = None if source_id == args.session_id or args.source else "source `{}`".format(source_id)
                line = revision_line(item, label)
    if args.state:
        fields["result_state"] = args.state
        write_binding(record, fields)
    if args.write:
        insert_before_binding(record, line)
    print(line)
    if args.report:
        code_, stdout, stderr = run_helper("report", "--task-root", str(root), "--record", str(record),
                                           "--project", fields["project"])
        print(stdout if code_ == 0 else "report failed: " + stderr)
    return status


def capture(args, record, fields, source, source_id, unit, version, start, lines, mine):
    """Collect (or write a failure receipt) and receive. Returns (received path, failed) or None."""
    revision = max((i["manifest"]["revision"] for i in mine), default=0) + 1
    predecessor = max((i for i in mine if not is_failure(i)),
                      key=lambda i: i["manifest"]["revision"], default=None)
    work = Path(tempfile.gettempdir()) / "tfw" / fields["id"]
    work.mkdir(parents=True, exist_ok=True)
    out = work / "{}-r{}.jsonl".format(hashlib.sha256(unit.encode()).hexdigest()[:12], revision)
    try:
        common = ["--provider", args.provider, "--source", str(source), "--source-id", source_id,
                  "--source-version", version, "--project", fields["project"], "--task", fields["id"],
                  "--owner", fields["owner"], "--role", "daily", "--unit", unit,
                  "--timezone", fields["created"][-6:] if fields["created"][-6] in "+-" else "Z",
                  "--start", str(start), "--revision", str(revision), "--out", str(out)]
        code_, _, stderr = run_helper("collect", *common, "--complete",
                                      *(["--predecessor", predecessor["path"]] if predecessor else []))
        failed = code_ != 0
        if failed:
            code_, _, stderr2 = run_helper("failure", *common, "--end", str(lines), "--code", "collect_failed",
                                           "--detail", (stderr.splitlines() or ["collect failed"])[-1])
            if code_ != 0:
                print("daily_close: collect failed ({}); failure receipt failed ({})".format(stderr, stderr2),
                      file=sys.stderr)
                return None
        code_, stdout, stderr = run_helper("receive", "--source", str(out), "--task-root", str(record.parent),
                                           "--project", fields["project"], "--task", fields["id"],
                                           "--expected-unit", unit, "--record", str(record))
        if code_ != 0:
            print("daily_close: receive failed: " + stderr, file=sys.stderr)
            return None
        return json.loads(stdout)["path"], failed
    finally:
        if out.exists():
            out.unlink()
        for folder in (work, work.parent):
            try:
                folder.rmdir()
            except OSError:
                break

if __name__ == "__main__":
    sys.exit(main())
