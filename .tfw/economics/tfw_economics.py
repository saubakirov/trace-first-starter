#!/usr/bin/env python3
"""Portable, task-local TFW economics. Python standard library only.

The collectors inspect exact bound numeric sources. They do not discover sessions
by title, read message bodies for reporting, or alter a provider source.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import math
import re
import sqlite3
import statistics
import sys
import time
from collections import defaultdict
from decimal import Decimal
from pathlib import Path

VERSION = 1
COLLECTOR = "tfw-economics/1.0"
TOKEN_KEYS = ("fresh", "cached", "cache_write", "cache_write_5m",
              "cache_write_1h", "input", "output", "reasoning", "total")
KINDS = {"manifest", "usage", "failure"}
DURATIONS = {"completed_turn", "model_generation", "provider_run"}
ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:/-]*$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
HASH = re.compile(r"^[0-9a-f]{64}$")
TZ = re.compile(r"^(Z|[+-](?:0\d|1[0-4]):[0-5]\d)$")


class EconomicsError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise EconomicsError(message)


def exact_keys(value, required, optional=(), where="object"):
    require(isinstance(value, dict), where + " must be an object")
    missing = set(required) - value.keys()
    extra = value.keys() - set(required) - set(optional)
    require(not missing, where + " missing " + ", ".join(sorted(missing)))
    require(not extra, where + " has unknown " + ", ".join(sorted(extra)))


def identity(value, where):
    require(isinstance(value, str) and bool(ID.fullmatch(value)), where + " invalid")


def nonempty(value, where):
    require(isinstance(value, str) and bool(value.strip()), where + " required")


def nonnegative(value, where):
    require(type(value) in (int, float) and math.isfinite(value) and value >= 0,
            where + " must be finite and nonnegative")


def integer(value, where):
    require(type(value) is int and value >= 0, where + " must be a nonnegative integer")


def timestamp(value, where):
    nonempty(value, where)
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise EconomicsError(where + " invalid ISO timestamp") from exc
    require(parsed.tzinfo is not None, where + " needs an offset")
    return parsed


def day(value, where):
    require(isinstance(value, str) and bool(DATE.fullmatch(value)), where + " invalid date")
    try:
        dt.date.fromisoformat(value)
    except ValueError as exc:
        raise EconomicsError(where + " invalid calendar date") from exc


def timezone(value):
    require(isinstance(value, str) and bool(TZ.fullmatch(value)),
            "timezone must be Z or an explicit offset")
    if value == "Z":
        return dt.timezone.utc
    sign = 1 if value[0] == "+" else -1
    hours, minutes = map(int, value[1:].split(":"))
    return dt.timezone(sign * dt.timedelta(hours=hours, minutes=minutes))


def date_at(value, tz):
    if value is None:
        return None
    return timestamp(value, "source timestamp").astimezone(timezone(tz)).date().isoformat()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_jsonl(path):
    raw = Path(path).read_bytes()
    require(raw.endswith(b"\n"), str(path) + " lacks final newline")
    try:
        lines = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise EconomicsError(str(path) + ": malformed UTF-8 JSONL") from exc
    return raw, lines


def write_jsonl(path, rows):
    data = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True,
                              separators=(",", ":")) + "\n" for row in rows).encode("utf-8")
    dest = Path(path)
    require(not dest.exists(), "refuse to overwrite " + str(dest))
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    return sha(data)


def validate_extensions(value):
    require(isinstance(value, dict), "extensions must be an object")
    for key in value:
        require(isinstance(key, str) and "." in key and not key.startswith(".")
                and not key.endswith("."), "extension key must be namespaced")


def validate_tokens(tokens, unavailable):
    exact_keys(tokens, TOKEN_KEYS, where="tokens")
    for key in ("input", "output", "total"):
        require(tokens[key] is not None, "tokens." + key + " is required for measured usage")
    for key, value in tokens.items():
        if value is None:
            require(key in unavailable, "null token " + key + " needs a reason")
        else:
            integer(value, "tokens." + key)
    a = tokens
    if all(a[k] is not None for k in ("fresh", "cached", "cache_write", "input")):
        require(a["input"] == a["fresh"] + a["cached"] + a["cache_write"],
                "input bucket sum mismatch")
    if all(a[k] is not None for k in ("input", "output", "total")):
        require(a["total"] == a["input"] + a["output"], "total token sum mismatch")
    if a["reasoning"] is not None and a["output"] is not None:
        require(a["reasoning"] <= a["output"], "reasoning exceeds output")
    if a["cache_write_5m"] is not None and a["cache_write_1h"] is not None:
        require(a["cache_write"] is not None and
                a["cache_write"] == a["cache_write_5m"] + a["cache_write_1h"],
                "cache write split mismatch")
    require(a["cached"] is None or a["input"] is None or a["cached"] <= a["input"],
            "cached input exceeds input")


def validate_manifest(m):
    keys = ("kind", "schema_version", "project", "task", "phase", "owner",
            "role", "unit", "source_namespace", "source_id", "source_version",
            "source_label", "source_sha256", "source_size", "collector",
            "revision", "predecessor_sha256", "range_start", "range_end",
            "complete", "captured_at", "cutoff", "timezone", "operation_seconds",
            "tfw_version", "coordination_mode", "unavailable", "extensions")
    exact_keys(m, keys, where="manifest")
    require(m["kind"] == "manifest" and m["schema_version"] == VERSION,
            "unsupported schema version or first row")
    nonempty(m["project"], "manifest.project")
    for k in ("task", "owner", "role", "unit", "source_namespace",
              "source_id", "source_version", "collector"):
        identity(m[k], "manifest." + k)
    if m["phase"] is not None:
        identity(m["phase"], "manifest.phase")
    nonempty(m["source_label"], "manifest.source_label")
    require(isinstance(m["source_sha256"], str) and HASH.fullmatch(m["source_sha256"]),
            "source SHA-256 invalid")
    integer(m["source_size"], "source_size")
    require(type(m["revision"]) is int and m["revision"] >= 1, "revision must start at 1")
    if m["predecessor_sha256"] is not None:
        require(m["revision"] > 1 and isinstance(m["predecessor_sha256"], str) and
                HASH.fullmatch(m["predecessor_sha256"]),
                "predecessor SHA-256 invalid")
    integer(m["range_start"], "range_start")
    integer(m["range_end"], "range_end")
    require(m["range_end"] > m["range_start"], "empty or reversed source range")
    require(type(m["complete"]) is bool, "complete must be boolean")
    captured = timestamp(m["captured_at"], "captured_at")
    cutoff = timestamp(m["cutoff"], "cutoff")
    require(cutoff <= captured, "cutoff after capture")
    timezone(m["timezone"])
    exact_keys(m["unavailable"], (), ("tfw_version", "coordination_mode", "operation_seconds"),
               "manifest.unavailable")
    if m["operation_seconds"] is None:
        nonempty(m["unavailable"].get("operation_seconds"), "unavailable.operation_seconds")
    else:
        nonnegative(m["operation_seconds"], "operation_seconds")
    for key in ("tfw_version", "coordination_mode"):
        if m[key] is None:
            nonempty(m["unavailable"].get(key), "unavailable." + key)
        else:
            nonempty(m[key], key)
    validate_extensions(m["extensions"])
    included = m["extensions"].get("tfw.includes_sources", [])
    require(isinstance(included, list) and all(isinstance(x, str) and ID.fullmatch(x)
            for x in included), "includes_sources must list exact native source identities")


def validate_row(row, m):
    require(isinstance(row, dict), "row must be object")
    require(row.get("schema_version") == VERSION, "unsupported row version")
    kind = row.get("kind")
    require(kind in {"usage", "failure"}, "unknown row kind")
    if kind == "failure":
        exact_keys(row, ("kind", "schema_version", "code", "detail", "extensions"),
                   where="failure")
        identity(row["code"], "failure.code")
        nonempty(row["detail"], "failure.detail")
        validate_extensions(row["extensions"])
        return
    keys = ("kind", "schema_version", "event_id", "source_index", "observed_at",
            "consumption_date", "timezone", "model", "effort", "tokens",
            "duration_seconds", "duration_kind", "unavailable", "extensions")
    exact_keys(row, keys, where="usage")
    identity(row["event_id"], "event_id")
    integer(row["source_index"], "source_index")
    require(m["range_start"] <= row["source_index"] < m["range_end"],
            "event outside declared range")
    if row["observed_at"] is not None:
        observed = timestamp(row["observed_at"], "observed_at")
        require(observed <= timestamp(m["cutoff"], "cutoff"),
                "observed event after declared cutoff")
    if row["consumption_date"] is not None:
        day(row["consumption_date"], "consumption_date")
        if row["observed_at"] is not None:
            require(date_at(row["observed_at"], row["timezone"]) == row["consumption_date"],
                    "date does not match source timestamp and timezone")
    timezone(row["timezone"])
    require(row["timezone"] == m["timezone"], "row timezone differs from bound manifest")
    exact_keys(row["unavailable"], (), ("observed_at", "consumption_date",
               "model", "effort", "duration_seconds", "fresh", "cached", "cache_write",
               "reasoning", "cache_write_5m", "cache_write_1h"), "usage.unavailable")
    for key in ("observed_at", "consumption_date", "model", "effort"):
        if row[key] is None:
            nonempty(row["unavailable"].get(key), "unavailable." + key)
    if row["model"] is not None:
        identity(row["model"], "model")
    if row["effort"] is not None:
        identity(row["effort"], "effort")
    if row["duration_seconds"] is None:
        require(row["duration_kind"] is None, "null duration needs null kind")
        nonempty(row["unavailable"].get("duration_seconds"),
                 "unavailable.duration_seconds")
    else:
        nonnegative(row["duration_seconds"], "duration_seconds")
        require(row["duration_kind"] in DURATIONS, "invalid duration kind")
    validate_tokens(row["tokens"], row["unavailable"])
    validate_extensions(row["extensions"])


def validate_file(path):
    raw, rows = read_jsonl(path)
    require(rows, str(path) + " is empty")
    m = rows[0]
    validate_manifest(m)
    ids = set()
    failure = False
    for row in rows[1:]:
        validate_row(row, m)
        if row["kind"] == "failure":
            failure = True
        else:
            require(row["event_id"] not in ids, "duplicate event_id in one file")
            ids.add(row["event_id"])
    require(not (failure and ids), "failure receipt must not claim measured rows")
    require(not failure or len(rows) == 2, "failure receipt needs exactly one failure row")
    require(ids or failure, "contribution has no measurement or failure receipt")
    return {"path": str(path), "sha256": sha(raw), "manifest": m,
            "rows": rows[1:], "bytes": len(raw)}


def zero_tokens(fresh, cached, cache_write, output, reasoning,
                write_5m=0, write_1h=0):
    return dict(fresh=fresh, cached=cached, cache_write=cache_write,
                cache_write_5m=write_5m, cache_write_1h=write_1h,
                input=fresh + cached + cache_write, output=output,
                reasoning=reasoning, total=fresh + cached + cache_write + output)


def usage(event_id, index, observed_at, tz, model, effort, tokens,
          duration=None, duration_kind=None, unavailable=None, extensions=None,
          consumption_date=None):
    gaps = dict(unavailable or {})
    date = consumption_date if consumption_date is not None else date_at(observed_at, tz)
    for key, value, reason in (
        ("observed_at", observed_at, "source has no proved event timestamp"),
        ("consumption_date", date, "source date join is unproved"),
        ("model", model, "model unavailable at this event"),
        ("effort", effort, "effort not reported by numeric source"),
        ("duration_seconds", duration, "no matched native duration event"),
    ):
        if value is None:
            gaps.setdefault(key, reason)
    for key in ("fresh", "cached", "cache_write", "reasoning",
                "cache_write_5m", "cache_write_1h"):
        if tokens[key] is None:
            gaps.setdefault(key, "source does not expose this token subcategory")
    return dict(kind="usage", schema_version=VERSION, event_id=str(event_id),
                source_index=index, observed_at=observed_at, consumption_date=date,
                timezone=tz, model=model, effort=effort, tokens=tokens,
                duration_seconds=duration, duration_kind=duration_kind,
                unavailable=gaps, extensions=extensions or {})


def source_lines(path):
    raw = Path(path).read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw = raw[:raw.rfind(b"\n") + 1]
    require(raw, "source has no complete JSONL line")
    return raw, raw.splitlines()


def codex_rows(raw, args):
    result = []
    active = None
    model = effort = None
    total = None
    turns = {}
    seen_session = None
    diagnostics = []
    completed = set()
    for line_no, line in enumerate(raw.splitlines()):
        if args.end is not None and line_no >= args.end:
            break
        in_range = line_no >= args.start
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise EconomicsError("Codex malformed JSON at bound line " + str(line_no)) from exc
        kind = event.get("type")
        payload = event.get("payload") or {}
        if kind == "session_meta":
            seen_session = payload.get("id") or payload.get("session_id")
        if kind == "turn_context":
            model = payload.get("model")
            effort = payload.get("effort") or payload.get("reasoning_effort")
            active = payload.get("turn_id") or active
        if kind != "event_msg":
            continue
        sub = payload.get("type")
        if sub == "task_started":
            active = payload.get("turn_id") or active
            if active:
                turns.setdefault(active, {"start": line_no, "last": None})
        elif sub == "token_count":
            info = payload.get("info")
            if not isinstance(info, dict) or not isinstance(info.get("total_token_usage"), dict):
                continue
            cur = info["total_token_usage"]
            fields = ("input_tokens", "cached_input_tokens", "cache_write_input_tokens",
                      "output_tokens", "reasoning_output_tokens", "total_tokens")
            require(all(type(cur.get(k)) is int and cur[k] >= 0 for k in fields),
                    "Codex counters malformed")
            prior = {k: 0 for k in fields} if total is None else total
            delta = {k: cur[k] - prior[k] for k in fields}
            require(all(v >= 0 for v in delta.values()), "Codex counter reset needs explicit reconciliation")
            total = cur
            if all(v == 0 for v in delta.values()):
                continue
            last = info.get("last_token_usage")
            require(isinstance(last, dict) and all(last.get(k) == delta[k] for k in fields),
                    "Codex last usage disagrees with cumulative delta")
            require(delta["input_tokens"] + delta["output_tokens"] == delta["total_tokens"],
                    "Codex total counter mismatch")
            fresh = delta["input_tokens"] - delta["cached_input_tokens"] - delta["cache_write_input_tokens"]
            require(fresh >= 0, "Codex cache exceeds input")
            if not in_range:
                continue
            tok = zero_tokens(fresh, delta["cached_input_tokens"],
                              delta["cache_write_input_tokens"], delta["output_tokens"],
                              delta["reasoning_output_tokens"])
            if tok["cache_write"]:
                tok["cache_write_5m"] = tok["cache_write_1h"] = None
            row = usage("line:" + str(line_no), line_no, event.get("timestamp"),
                        args.timezone, model, effort, tok)
            result.append(row)
            if active:
                turns.setdefault(active, {"start": line_no, "last": None})["last"] = len(result) - 1
        elif sub == "task_complete":
            turn = payload.get("turn_id") or active
            milliseconds = payload.get("duration_ms")
            if in_range and type(milliseconds) in (int, float) and milliseconds >= 0 and turn:
                item = turns.get(turn)
                if item and item["start"] >= args.start and item["last"] is not None and turn not in completed:
                    prior_row = result[item["last"]]
                    result.append(usage("complete:" + turn, line_no, event.get("timestamp"),
                                        args.timezone, prior_row["model"], prior_row["effort"],
                                        zero_tokens(0, 0, 0, 0, 0),
                                        duration=milliseconds / 1000,
                                        duration_kind="completed_turn"))
                    completed.add(turn)
                else:
                    diagnostics.append("completed turn without a measured usage row")
            active = None
        elif sub == "turn_aborted":
            diagnostics.append("aborted turn has no completed-turn duration")
            active = None
    require(seen_session == args.source_id, "Codex session_meta does not match exact source ID")
    diagnostics.append("unmatched task_started: " + str(sum(1 for turn, v in turns.items()
                       if v["last"] is not None and turn not in completed)))
    return result, diagnostics


def claude_rows(raw, args):
    best = {}
    seen_sessions = set()
    earlier_ids = set()
    for line_no, line in enumerate(raw.splitlines()):
        if args.end is not None and line_no >= args.end:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise EconomicsError("Claude malformed JSON at bound line " + str(line_no)) from exc
        if event.get("sessionId"):
            seen_sessions.add(event["sessionId"])
        message = event.get("message")
        if event.get("type") != "assistant" or not isinstance(message, dict):
            continue
        u = message.get("usage")
        if not isinstance(u, dict):
            continue
        mid = message.get("id")
        identity(mid, "Claude message id")
        if line_no < args.start:
            earlier_ids.add(mid)
            continue
        require(mid not in earlier_ids,
                "Claude message spans selected range boundary; include its earlier blocks")
        fresh = u.get("input_tokens", 0)
        cached = u.get("cache_read_input_tokens", 0)
        writes = u.get("cache_creation_input_tokens", 0)
        creation = u.get("cache_creation") or {}
        w5 = creation.get("ephemeral_5m_input_tokens", 0)
        w1 = creation.get("ephemeral_1h_input_tokens", 0)
        output = u.get("output_tokens", 0)
        for key, value in (("input", fresh), ("cached", cached), ("write", writes),
                           ("5m", w5), ("1h", w1), ("output", output)):
            integer(value, "Claude " + key)
        require(writes == w5 + w1, "Claude cache write categories disagree")
        details = u.get("output_tokens_details") or {}
        reasoning = details.get("thinking_tokens")
        if reasoning is not None:
            integer(reasoning, "Claude thinking")
        tok = zero_tokens(fresh, cached, writes, output, reasoning, w5, w1)
        prior = best.get(mid)
        if prior:
            stable = ("fresh", "cached", "cache_write", "cache_write_5m", "cache_write_1h", "input")
            require(all(prior["tokens"][k] == tok[k] for k in stable),
                    "Claude repeated message changed input categories")
            if prior["tokens"]["output"] > output:
                continue
            if prior["tokens"]["output"] == output and prior["tokens"]["reasoning"] is not None:
                reasoning = prior["tokens"]["reasoning"]
                tok["reasoning"] = reasoning
        best[mid] = dict(index=line_no, at=event.get("timestamp"),
                         model=message.get("model"), tokens=tok)
    require(seen_sessions == {args.source_id},
            "Claude session IDs disagree with exact source ID")
    result = []
    for mid, rec in best.items():
        result.append(usage("message:" + mid, rec["index"], rec["at"],
                            args.timezone, rec["model"], None, rec["tokens"],
                            unavailable={"duration_seconds": "Claude Code JSONL has no native agent interval"}))
    return sorted(result, key=lambda r: r["source_index"]), [
        "repeated assistant blocks reconciled by message id and maximum output",
        "gap-based active time excluded from native duration"]


def varint(data, at):
    value = shift = 0
    while at < len(data):
        byte = data[at]
        at += 1
        value |= (byte & 127) << shift
        if byte < 128:
            return value, at
        shift += 7
        require(shift < 70, "protobuf varint too long")
    raise EconomicsError("truncated protobuf varint")


def proto_fields(data):
    at, result = 0, defaultdict(list)
    while at < len(data):
        tag, at = varint(data, at)
        number, wire = tag >> 3, tag & 7
        require(number > 0, "invalid protobuf field")
        if wire == 0:
            value, at = varint(data, at)
        elif wire == 1:
            require(at + 8 <= len(data), "truncated fixed64")
            value, at = data[at:at + 8], at + 8
        elif wire == 2:
            size, at = varint(data, at)
            require(at + size <= len(data), "truncated protobuf bytes")
            value, at = data[at:at + size], at + size
        elif wire == 5:
            require(at + 4 <= len(data), "truncated fixed32")
            value, at = data[at:at + 4], at + 4
        else:
            raise EconomicsError("unsupported protobuf wire type")
        result[number].append(value)
    return result


def one(fields, key, typ, default=None):
    values = fields.get(key, [])
    require(len(values) <= 1, "repeated private numeric field " + str(key))
    value = values[0] if values else default
    require(value is None or isinstance(value, typ), "private field type changed " + str(key))
    return value


def antigravity_rows(source, args):
    require(args.source_version == "Antigravity-IDE-2.17.0",
            "unsupported Antigravity private source version")
    require(Path(source).stem == args.source_id, "conversation DB filename differs from exact ID")
    uri = Path(source).resolve().as_uri() + "?mode=ro"
    con = sqlite3.connect(uri, uri=True)
    copy = sqlite3.connect(":memory:")
    try:
        con.backup(copy)
    finally:
        con.close()
    columns = [r[1] for r in copy.execute("pragma table_info(gen_metadata)")]
    require(columns == ["idx", "data", "size"], "unsupported gen_metadata layout")
    raw_digest = hashlib.sha256()
    total_size = 0
    result = []
    query = "select idx, data from gen_metadata where idx >= ?"
    params = [args.start]
    if args.end is not None:
        query += " and idx < ?"
        params.append(args.end)
    query += " order by idx"
    for idx, blob in copy.execute(query, params):
        require(type(idx) is int and isinstance(blob, bytes), "invalid numeric DB row")
        raw_digest.update(idx.to_bytes(8, "big", signed=False))
        raw_digest.update(len(blob).to_bytes(8, "big"))
        raw_digest.update(blob)
        total_size += len(blob) + 16
        top = proto_fields(blob)
        outer_blob = one(top, 1, bytes)
        require(outer_blob is not None, "Antigravity outer numeric field missing")
        outer = proto_fields(outer_blob)
        usage_blob = one(outer, 4, bytes)
        require(usage_blob is not None, "Antigravity usage field missing")
        u = proto_fields(usage_blob)
        model_blob = one(outer, 19, bytes)
        try:
            model = model_blob.decode("utf-8") if model_blob is not None else None
        except UnicodeError as exc:
            raise EconomicsError("Antigravity model encoding changed") from exc
        fresh = one(u, 2, int)
        cached = one(u, 5, int, 0)
        output = one(u, 3, int)
        reasoning = one(u, 9, int)
        content = one(u, 10, int)
        require(all(type(x) is int and x >= 0 for x in (fresh, cached, output, reasoning, content)),
                "Antigravity numeric mapping changed")
        require(output == reasoning + content, "Antigravity candidate inclusion changed")
        timing_blob = one(outer, 11, bytes)
        timing = proto_fields(timing_blob) if timing_blob is not None else None
        seconds = one(timing, 1, int, 0) if timing is not None else None
        nanos = one(timing, 2, int, 0) if timing is not None else None
        if timing is not None:
            require(0 <= nanos < 1_000_000_000, "invalid generation nanoseconds")
        row = usage("idx:" + str(idx), idx, None, args.timezone, model, None,
                    zero_tokens(fresh, cached, 0, output, reasoning),
                    duration=(seconds + nanos / 1_000_000_000 if timing is not None else None),
                    duration_kind="model_generation" if timing is not None else None,
                    extensions={"antigravity.content_tokens": content})
        result.append(row)
    copy.close()
    require(result, "selected Antigravity range has no numeric rows")
    return result, raw_digest.hexdigest(), total_size, [
        "Antigravity DB copied through SQLite read-only backup",
        "daily date omitted: no proved gen_metadata to timestamp join",
        "model generation duration is not agent session time"]


def compact_rows(rows):
    """Aggregate verified native events at date × bound run × model × effort.

    The manifest preserves native source identity/range/hash. Individual call
    identifiers are digested for proof, not shipped as a routine event archive.
    Duration is a separate row, so a partially matched timer never appears to
    describe all tokens in its day/model bucket.
    """
    groups = defaultdict(list)
    for row in rows:
        base = (row["consumption_date"], row["model"], row["effort"], row["timezone"])
        if row["tokens"]["total"] != 0 or row["duration_seconds"] is None:
            groups[("tokens",) + base].append(row)
        if row["duration_seconds"] is not None:
            groups[("duration", row["duration_kind"]) + base].append(row)
    compact = []
    for key, members in sorted(groups.items(), key=lambda item: str(item[0])):
        is_duration = key[0] == "duration"
        at = max((r["observed_at"] for r in members if r["observed_at"] is not None),
                 default=None)
        first = min(r["source_index"] for r in members)
        ids = sorted(r["event_id"] for r in members)
        digest = sha("\n".join(ids).encode("utf-8"))
        model = members[0]["model"]
        effort = members[0]["effort"]
        tz = members[0]["timezone"]
        if is_duration:
            tok = zero_tokens(0, 0, 0, 0, 0)
            duration = sum(r["duration_seconds"] for r in members)
            duration_kind = key[1]
        else:
            tok = {}
            for field in TOKEN_KEYS:
                values = [r["tokens"][field] for r in members]
                tok[field] = sum(values) if all(v is not None for v in values) else None
            duration = duration_kind = None
        gaps = {}
        if not is_duration:
            gaps["duration_seconds"] = "duration reported separately at proved native granularity"
        aggregate = usage("aggregate:" + digest[:24] + (":time" if is_duration else ":tokens"),
                          first, at, tz, model, effort, tok, duration, duration_kind,
                          unavailable=gaps,
                          extensions={"tfw.native_event_count": len(members),
                                      "tfw.native_ids_sha256": digest,
                                      "tfw.aggregate_kind": key[0]},
                          consumption_date=members[0]["consumption_date"])
        compact.append(aggregate)
    return compact


def manifest(args, source_hash, source_size, end, operation_seconds, diagnostics,
             source_prefix_sha256=None):
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    predecessor = None
    if args.predecessor:
        predecessor = validate_file(args.predecessor)["sha256"]
    return dict(kind="manifest", schema_version=VERSION, project=args.project,
                task=args.task, phase=args.phase, owner=args.owner, role=args.role,
                unit=args.unit, source_namespace=args.provider, source_id=args.source_id,
                source_version=args.source_version, source_label=args.source_label or Path(args.source).name,
                source_sha256=source_hash, source_size=source_size, collector=COLLECTOR,
                revision=args.revision, predecessor_sha256=predecessor,
                range_start=args.start, range_end=end, complete=args.complete,
                captured_at=now, cutoff=now, timezone=args.timezone,
                operation_seconds=round(operation_seconds, 6),
                tfw_version=args.tfw_version, coordination_mode=args.coordination_mode,
                unavailable={k: "not present in a bound task source" for k in
                             ("tfw_version", "coordination_mode") if getattr(args, k) is None},
                extensions={"tfw.diagnostics": diagnostics,
                            "tfw.includes_sources": args.includes_source,
                            "tfw.predecessor_source_prefix_sha256": source_prefix_sha256})


def collect(args):
    timezone(args.timezone)
    nonempty(args.project, "project")
    for key in ("task", "owner", "role", "unit", "source_id", "source_version"):
        identity(getattr(args, key), key)
    started = time.monotonic()
    source = Path(args.source)
    require(source.is_file(), "exact source file missing")
    prefix_hash = None
    predecessor = validate_file(args.predecessor) if args.predecessor else None
    if predecessor:
        p = predecessor["manifest"]
        require(p["source_namespace"] == args.provider and p["source_id"] == args.source_id
                and p["unit"] == args.unit, "predecessor source/unit mismatch")
    if args.provider == "antigravity.ide":
        rows, source_hash, source_size, diagnostics = antigravity_rows(source, args)
        end = max(r["source_index"] for r in rows) + 1 if args.end is None else args.end
        if predecessor and args.start <= predecessor["manifest"]["range_start"]:
            prior_end = predecessor["manifest"]["range_end"]
            prior_args = argparse.Namespace(**vars(args))
            prior_args.start, prior_args.end = predecessor["manifest"]["range_start"], prior_end
            _, prefix_hash, _, _ = antigravity_rows(source, prior_args)
    else:
        raw, lines = source_lines(source)
        end = len(lines) if args.end is None else args.end
        require(0 <= args.start < end <= len(lines), "source line range invalid")
        bound_raw = b"\n".join(lines[:end]) + b"\n"
        source_hash, source_size = sha(bound_raw), len(bound_raw)
        if args.provider == "codex.rollout":
            rows, diagnostics = codex_rows(raw, args)
        else:
            rows, diagnostics = claude_rows(raw, args)
        if predecessor and args.start <= predecessor["manifest"]["range_start"]:
            prior_end = predecessor["manifest"]["range_end"]
            require(prior_end <= len(lines), "predecessor source range no longer exists")
            prefix_hash = sha(b"\n".join(lines[:prior_end]) + b"\n")
    require(rows, "selected range has no measured usage; use failure receipt if capture failed")
    native_count = len(rows)
    rows = compact_rows(rows)
    diagnostics.append("compacted {} verified native rows into {} daily/run/model records".format(
        native_count, len(rows)))
    if predecessor and prefix_hash is not None:
        require(prefix_hash == predecessor["manifest"]["source_sha256"],
                "source bytes changed in predecessor range")
    m = manifest(args, source_hash, source_size, end, time.monotonic() - started,
                 diagnostics, prefix_hash)
    digest = write_jsonl(args.out, [m] + rows)
    validate_file(args.out)
    print(json.dumps({"file": str(args.out), "sha256": digest, "rows": len(rows),
                      "cutoff": m["cutoff"]}, sort_keys=True))


def failure_receipt(args):
    timezone(args.timezone)
    nonempty(args.project, "project")
    for key in ("task", "owner", "role", "unit", "source_id", "source_version"):
        identity(getattr(args, key), key)
    require(args.end is not None and args.end > args.start, "failure receipt needs attempted range")
    source_hash = sha(Path(args.source).read_bytes()) if Path(args.source).is_file() else sha(b"")
    source_size = Path(args.source).stat().st_size if Path(args.source).is_file() else 0
    m = manifest(args, source_hash, source_size, args.end, 0, ["capture failed"])
    row = dict(kind="failure", schema_version=VERSION, code=args.code,
               detail=args.detail, extensions={})
    digest = write_jsonl(args.out, [m, row])
    validate_file(args.out)
    print(json.dumps({"file": str(args.out), "sha256": digest, "measured": False}))


def receive(args):
    item = validate_file(args.source)
    m = item["manifest"]
    require(m["project"] == args.project and m["task"] == args.task
            and m["unit"] == args.expected_unit, "received contributor identity mismatch")
    task = Path(args.task_root).resolve()
    status = task / "status.md"
    require(status.is_file(), "task root has no status.md")
    require(re.search(r"(?m)^id: " + re.escape(args.task) + r"$",
                      status.read_text(encoding="utf-8")), "task-root ID mismatch")
    dest_dir = task / "economics" / "roles"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / (item["sha256"] + ".jsonl")
    if dest.exists():
        require(sha(dest.read_bytes()) == item["sha256"], "received hash path corrupted")
        action = "no-op"
    else:
        verified_bytes = Path(args.source).read_bytes()
        require(sha(verified_bytes) == item["sha256"], "source changed during receipt")
        dest.write_bytes(verified_bytes)
        action = "copied"
    print(json.dumps({"action": action, "path": str(dest), "sha256": item["sha256"],
                      "unit": m["unit"], "revision": m["revision"]}, sort_keys=True))


def selected_files(task_root):
    folder = Path(task_root) / "economics" / "roles"
    return sorted(folder.glob("*.jsonl")) if folder.is_dir() else []


def reconcile(paths, expected_units=()):
    files = [validate_file(p) for p in paths]
    by_hash = {f["sha256"]: f for f in files}
    require(len(by_hash) == len(files), "duplicate content under multiple paths")
    excluded, active, diagnostics = set(), set(), []
    groups = defaultdict(list)
    for f in files:
        m = f["manifest"]
        groups[(m["source_namespace"], m["source_id"])].append(f)
    for source, group in groups.items():
        group.sort(key=lambda f: (f["manifest"]["revision"], f["manifest"]["range_start"]))
        for f in group:
            m = f["manifest"]
            prior = by_hash.get(m["predecessor_sha256"])
            if m["predecessor_sha256"] is not None:
                if prior is None:
                    excluded.add(f["sha256"])
                    diagnostics.append("missing predecessor for " + f["sha256"])
                    continue
                p = prior["manifest"]
                same = (p["source_namespace"], p["source_id"], p["unit"], p["project"], p["task"])
                cur = (m["source_namespace"], m["source_id"], m["unit"], m["project"], m["task"])
                if same != cur or m["revision"] <= p["revision"]:
                    excluded.add(f["sha256"])
                    diagnostics.append("invalid successor identity/revision " + f["sha256"])
                    continue
                if m["range_start"] <= p["range_start"] and m["range_end"] >= p["range_end"] and m["complete"]:
                    if m["extensions"].get("tfw.predecessor_source_prefix_sha256") != p["source_sha256"]:
                        excluded.add(f["sha256"])
                        diagnostics.append("unproved successor source prefix " + f["sha256"])
                        continue
                    excluded.add(prior["sha256"])
                elif not (m["range_end"] <= p["range_start"] or p["range_end"] <= m["range_start"]):
                    excluded.add(f["sha256"])
                    diagnostics.append("unproved successor overlap " + f["sha256"])
                    continue
            active.add(f["sha256"])
        chosen = [f for f in group if f["sha256"] in active - excluded]
        for i, left in enumerate(chosen):
            a = left["manifest"]
            for right in chosen[i + 1:]:
                b = right["manifest"]
                if max(a["range_start"], b["range_start"]) < min(a["range_end"], b["range_end"]):
                    excluded.update((left["sha256"], right["sha256"]))
                    diagnostics.append("conflicting overlapping source range " + str(source))
                    if a["unit"] != b["unit"]:
                        diagnostics.append("one overlapping native range claimed by multiple units " + str(source))
    active -= excluded
    for f in files:
        if f["sha256"] not in active:
            continue
        for included in f["manifest"]["extensions"].get("tfw.includes_sources", []):
            if any(g["sha256"] in active and
                   included == g["manifest"]["source_namespace"] + ":" + g["manifest"]["source_id"]
                   for g in files):
                active.remove(f["sha256"])
                excluded.add(f["sha256"])
                diagnostics.append("inclusive parent excluded while named child is present: " +
                                   f["sha256"])
                break
    records = []
    event_ids = set()
    for f in files:
        if f["sha256"] not in active:
            continue
        m = f["manifest"]
        for row in f["rows"]:
            if row["kind"] == "failure":
                diagnostics.append("capture failure " + m["unit"] + ": " + row["code"])
                continue
            key = (m["source_namespace"], m["source_id"], row["event_id"])
            if key in event_ids:
                diagnostics.append("duplicate native event " + str(key))
                continue
            event_ids.add(key)
            records.append((m, row, f["sha256"]))
    received = {f["manifest"]["unit"] for f in files}
    measured = {m["unit"] for m, _, _ in records}
    expected = set(expected_units)
    return dict(records=records, received=received, measured=measured,
                missing=expected - received, failure_only=received - measured,
                excluded=excluded, diagnostics=diagnostics, files=files)


def price(tokens, model, rates):
    card = rates["models"].get(model)
    if card is None:
        return None, "unknown exact model or rate"
    if tokens["fresh"] is None or tokens["cached"] is None or tokens["output"] is None:
        return None, "required token category unavailable"
    writes = tokens["cache_write"]
    if writes is None:
        return None, "cache write category unavailable"
    if writes and (tokens["cache_write_5m"] is None or tokens["cache_write_1h"] is None):
        return None, "cache write tariff split unavailable"
    value = (Decimal(tokens["fresh"]) * Decimal(str(card["fresh"]))
             + Decimal(tokens["cached"]) * Decimal(str(card["cached"]))
             + Decimal(tokens["cache_write_5m"]) * Decimal(str(card["cache_write_5m"]))
             + Decimal(tokens["cache_write_1h"]) * Decimal(str(card["cache_write_1h"]))
             + Decimal(tokens["output"]) * Decimal(str(card["output"]))) / 1_000_000
    return value, None


def load_rates(path):
    rates = json.loads(Path(path).read_text(encoding="utf-8"))
    require(rates.get("version") == 1 and isinstance(rates.get("models"), dict),
            "unsupported rate card")
    return rates


def summarize(records, rates, filters=None):
    filters = filters or {}
    selected = []
    for m, row, digest in records:
        if filters.get("date_from") and (row["consumption_date"] is None or
                                         row["consumption_date"] < filters["date_from"]):
            continue
        if filters.get("date_to") and (row["consumption_date"] is None or
                                       row["consumption_date"] > filters["date_to"]):
            continue
        if any(filters.get(k) and value != filters[k] for k, value in
               (("project", m["project"]), ("task", m["task"]), ("role", m["role"]),
                ("model", row["model"]))):
            continue
        selected.append((m, row, digest))
    total = dict(tokens=0, input=0, output=0, cached=0, priced_usd=Decimal(0),
                 unpriced_tokens=0, undated_tokens=0, duration=defaultdict(float),
                 by_role=defaultdict(lambda: dict(tokens=0, usd=Decimal(0))),
                 by_model=defaultdict(lambda: dict(tokens=0, usd=Decimal(0))),
                 by_date=defaultdict(lambda: dict(tokens=0, usd=Decimal(0))))
    flat = []
    for m, row, digest in selected:
        tok = row["tokens"]
        cost, reason = price(tok, row["model"], rates)
        total["tokens"] += tok["total"]
        total["input"] += tok["input"]
        total["output"] += tok["output"]
        if tok["cached"] is None:
            total["cached"] = None
        elif total["cached"] is not None:
            total["cached"] += tok["cached"]
        if row["consumption_date"] is None:
            total["undated_tokens"] += tok["total"]
        if cost is None:
            total["unpriced_tokens"] += tok["total"]
        else:
            total["priced_usd"] += cost
        if row["duration_seconds"] is not None:
            total["duration"][row["duration_kind"]] += row["duration_seconds"]
        for bucket, key in (("by_role", m["role"]), ("by_model", row["model"] or "unknown")):
            total[bucket][key]["tokens"] += tok["total"]
            if cost is not None:
                total[bucket][key]["usd"] += cost
        date_key = row["consumption_date"] or "undated"
        total["by_date"][date_key]["tokens"] += tok["total"]
        if cost is not None:
            total["by_date"][date_key]["usd"] += cost
        flat.append(dict(project=m["project"], task=m["task"], phase=m["phase"],
                         owner=m["owner"], role=m["role"], unit=m["unit"],
                         source=m["source_namespace"], source_id=m["source_id"],
                         source_revision=m["revision"], file_sha256=digest,
                         event_id=row["event_id"], date=row["consumption_date"],
                         model=row["model"], tokens=tok["total"], input=tok["input"],
                         cached=tok["cached"], output=tok["output"],
                         duration_seconds=row["duration_seconds"],
                         duration_kind=row["duration_kind"],
                         api_reference_usd=str(cost) if cost is not None else None,
                         price_gap=reason))
    return total, flat


def status_fields(task_root):
    path = Path(task_root) / "status.md"
    require(path.is_file(), "missing task status")
    fields = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip('"')
    for key in ("id", "goal", "value", "lifecycle", "owner", "created"):
        require(fields.get(key), "status missing " + key)
    return fields


def metadata_block(path):
    if not Path(path).is_file():
        return None
    content = Path(path).read_text(encoding="utf-8")
    match = re.search(r"<!-- tfw-economics-v1 (\{[^\n]*\}) -->", content)
    return json.loads(match.group(1)) if match else None


def render_report(args):
    task = Path(args.task_root)
    state = status_fields(task)
    require(args.task_root and state["id"] == task.name, "task root/name mismatch")
    rates = load_rates(args.rates)
    data = reconcile(selected_files(task), args.expected_unit)
    require(all(f["manifest"]["project"] == args.project and
                f["manifest"]["task"] == state["id"] for f in data["files"]),
            "received project/task differs from selected report root")
    total, flat = summarize(data["records"], rates)
    keywords = args.keyword or []
    if args.primary_area is not None:
        nonempty(args.primary_area, "primary area")
        require(3 <= len(keywords) <= 5 and len(set(keywords)) == len(keywords),
                "close classification needs 3–5 distinct keywords")
        for item in keywords:
            nonempty(item, "keyword")
    elif keywords:
        raise EconomicsError("keywords need primary area")
    cutoff = max((f["manifest"]["cutoff"] for f in data["files"]), default=None)
    calendar_seconds = None
    if args.status_timezone and cutoff:
        tz = timezone(args.status_timezone)
        try:
            created = dt.datetime.strptime(state["created"], "%Y%m%d-%H%M%S").replace(tzinfo=tz)
            end = (dt.datetime.strptime(state["updated"], "%Y%m%d-%H%M%S").replace(tzinfo=tz)
                   if state["lifecycle"] == "DONE" else
                   timestamp(cutoff, "cutoff").astimezone(tz))
            require(end >= created, "status calendar interval reversed")
            calendar_seconds = (end - created).total_seconds()
        except ValueError as exc:
            raise EconomicsError("invalid status calendar clock") from exc
    operation_seconds = sum(f["manifest"]["operation_seconds"] or 0 for f in data["files"])
    unknown_operations = sum(f["manifest"]["operation_seconds"] is None for f in data["files"])
    incomplete = sorted(f["sha256"] for f in data["files"] if not f["manifest"]["complete"])
    block = dict(schema_version=1, project=args.project, task=state["id"],
                 lifecycle=state["lifecycle"], owner=state["owner"],
                 primary_area=args.primary_area, keywords=keywords,
                 report_at=dt.datetime.now(dt.timezone.utc).isoformat(),
                 cutoff=cutoff, rate_version=rates["rate_epoch"],
                 calendar_elapsed_seconds=calendar_seconds,
                 status_timezone=args.status_timezone,
                 totals=dict(tokens=total["tokens"], input=total["input"],
                             cached=total["cached"], output=total["output"],
                             priced_usd=str(total["priced_usd"]),
                             unpriced_tokens=total["unpriced_tokens"],
                             undated_tokens=total["undated_tokens"],
                             duration_seconds=dict(total["duration"])),
                 collector_operation_seconds=round(operation_seconds, 6),
                 unknown_collector_operations=unknown_operations,
                 received=sorted(data["received"]), measured=sorted(data["measured"]),
                 missing=sorted(data["missing"]),
                 failure_only=sorted(data["failure_only"]),
                 excluded=sorted(data["excluded"]), incomplete=incomplete)
    lines = ["# Task economics — " + state["id"], "",
             "<!-- tfw-economics-v1 " + json.dumps(block, ensure_ascii=False,
                                                  sort_keys=True, separators=(",", ":")) + " -->",
             "", "## Purpose, result and value", "",
             "- Purpose: " + state["goal"],
             "- Value sought: " + state["value"],
             "- Lifecycle at report: " + state["lifecycle"],
             "- Accepted result: " + (args.accepted_result or
                                     "not supplied at this cutoff; see RF/REVIEW before final close"),
             "", "## Resource summary", "",
             "| Measure | Observed selected contribution |", "|---|---:|",
             "| Tokens, input + output | {:,} |".format(total["tokens"]),
             "| Input, including cache | {:,} |".format(total["input"]),
             "| Cached input subset | {} |".format(
                 "{:,}".format(total["cached"]) if total["cached"] is not None else "unavailable"),
             "| Output, including reasoning when source says so | {:,} |".format(total["output"]),
             "| API reference estimate on priced rows (USD) | {} |".format(total["priced_usd"]),
             "| Unpriced tokens | {:,} |".format(total["unpriced_tokens"]),
             "| Undated tokens, excluded from date filters | {:,} |".format(total["undated_tokens"]),
             "| Collection operation, observed wall seconds | {:.3f} ({} files unknown) |".format(
                 operation_seconds, unknown_operations),
             "| Task calendar elapsed, status clock | {} |".format(
                 "{:.3f} seconds".format(calendar_seconds) if calendar_seconds is not None
                 else "unavailable (status timezone/cutoff not supplied)"),
             "", "Time kinds remain separate; task calendar elapsed is read from task control,",
             "not inferred from summed roles. Parallel role times can overlap.",
             ""]
    for kind, seconds in sorted(total["duration"].items()):
        lines.append("- {}: {:.3f} observed seconds".format(kind, seconds))
    lines += ["", "Money is a dated Standard API token equivalent, not a subscription bill.",
              "Unknown models, tariff conditions, storage and tools are excluded.",
              "", "## By role and model", ""]
    for group, title in (("by_role", "Role"), ("by_model", "Model")):
        lines += ["### " + title, "", "| " + title + " | Tokens | Priced USD |",
                  "|---|---:|---:|"]
        for key, item in sorted(total[group].items(), key=lambda x: -x[1]["tokens"]):
            lines.append("| {} | {:,} | {} |".format(key, item["tokens"], item["usd"]))
        lines.append("")
    lines += ["### Consumption date", "", "| Date | Tokens | Priced USD |",
              "|---|---:|---:|"]
    for key, item in sorted(total["by_date"].items()):
        lines.append("| {} | {:,} | {} |".format(key, item["tokens"], item["usd"]))
    lines.append("")
    lines += ["## Coverage and provenance", "",
              "- Expected units: " + (", ".join(args.expected_unit) or "not supplied"),
              "- Received units: " + (", ".join(sorted(data["received"])) or "none"),
              "- Measured units: " + (", ".join(sorted(data["measured"])) or "none"),
              "- Missing units: " + (", ".join(sorted(data["missing"])) or "none among declared expected"),
              "- Failure-only units: " + (", ".join(sorted(data["failure_only"])) or "none"),
              "- Incomplete source captures: " + str(len(incomplete)) +
              " (a finite snapshot is not full task coverage).",
              "- Excluded conflicting/superseded files: " + str(len(data["excluded"])),
              "- Capture cutoff: " + (cutoff or "no received contribution"),
              "- Finite tail: later report delivery, final message and cleanup are outside this cutoff.",
              "- Rate card: " + rates["rate_epoch"] + "; " + rates["basis"], ""]
    for f in data["files"]:
        m = f["manifest"]
        lines.append("- {}: {} / {} revision {}, range [{}, {}), complete {}, {} bytes, SHA-256 {}, source {}.".format(
            m["unit"], m["source_namespace"], m["source_id"], m["revision"],
            m["range_start"], m["range_end"], m["complete"],
            f["bytes"], f["sha256"], m["source_sha256"]))
    for item in data["diagnostics"]:
        lines.append("- Diagnostic: " + item)
    output = "\n".join(lines) + "\n"
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(output, encoding="utf-8")
        print(json.dumps({"report": str(args.out), "records": len(flat),
                          "tokens": total["tokens"], "missing": sorted(data["missing"])}))
    else:
        print(output)


def render_summary(args):
    rates = load_rates(args.rates)
    for value in (args.date_from, args.date_to):
        if value:
            day(value, "summary filter date")
    require(not (args.date_from and args.date_to and args.date_from > args.date_to),
            "summary date range reversed")
    roots = [Path(x) for x in args.task_root]
    selected = []
    task_meta = {}
    included_roots = []
    for root in roots:
        state = status_fields(root)
        report = metadata_block(root / "economics.md")
        task_meta[state["id"]] = (state, report)
        if args.tag and (report is None or args.tag not in report.get("keywords", [])
                         and args.tag != report.get("primary_area")):
            continue
        included_roots.append(root)
        data = reconcile(selected_files(root))
        selected.extend(data["records"])
    filters = {k: getattr(args, k) for k in ("date_from", "date_to", "project", "task", "role", "model")}
    total, flat = summarize(selected, rates, filters)
    for row in flat:
        meta = task_meta[row["task"]][1] or {}
        row["primary_area"] = meta.get("primary_area")
        row["keywords"] = ",".join(meta.get("keywords", []))
    if args.csv:
        dest = Path(args.csv)
        dest.parent.mkdir(parents=True, exist_ok=True)
        with dest.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(flat[0]) if flat else
                                    ["project", "task", "role", "model", "tokens", "api_reference_usd"])
            writer.writeheader()
            writer.writerows(flat)
    by_project = defaultdict(lambda: dict(tokens=0, priced=Decimal(0), duration=defaultdict(float)))
    by_task = defaultdict(lambda: dict(tokens=0, priced=Decimal(0)))
    for row in flat:
        for box in (by_project[row["project"]], by_task[row["task"]]):
            box["tokens"] += row["tokens"]
            if row["api_reference_usd"] is not None:
                box["priced"] += Decimal(row["api_reference_usd"])
        if row["duration_seconds"] is not None:
            by_project[row["project"]]["duration"][row["duration_kind"]] += row["duration_seconds"]
    lines = ["# Selected task economics", "",
             "Filters: " + json.dumps({k: v for k, v in filters.items() if v}, sort_keys=True),
             "Selected roots: " + ", ".join(str(x) for x in roots),
             "Rate basis: " + rates["basis"] + " (" + rates["rate_epoch"] + ")",
             "", "| Project | Tokens | Priced USD | Time by kind (seconds) |",
             "|---|---:|---:|---|"]
    for name in sorted(set(by_project) | ({"helpdesk", "afd"} if args.show_helpdesk_afd else set())):
        box = by_project.get(name)
        if box is None:
            lines.append("| {} | no captured data | no captured data | no captured data |".format(name))
        else:
            kinds = ", ".join("{}: {:.3f}".format(k, v) for k, v in sorted(box["duration"].items()))
            lines.append("| {} | {:,} | {} | {} |".format(name, box["tokens"], box["priced"],
                                                        kinds or "unavailable"))
    lines += ["", "Token ranking, time kinds and priced money are distinct; unknown time and",
              "unpriced tokens are not zeros. Dates without a proved source join are excluded",
              "from date-filtered totals.", "", "## Task lifetime and completed-task comparison", ""]
    for label, key in (("Token", lambda x: x[1]["tokens"]),
                       ("Priced USD", lambda x: x[1]["priced"])):
        order = sorted(by_project.items(), key=key, reverse=True)
        lines.append("- {} ranking: {}.".format(label, ", ".join(x[0] for x in order) or "none"))
    for kind in sorted({k for box in by_project.values() for k in box["duration"]}):
        order = sorted(by_project.items(), key=lambda x: x[1]["duration"][kind], reverse=True)
        lines.append("- {} time ranking: {}.".format(kind, ", ".join(x[0] for x in order)))
    for task, box in sorted(by_task.items(), key=lambda x: -x[1]["tokens"]):
        lines.append("- {}: {:,} selected tokens; {} USD priced.".format(task, box["tokens"], box["priced"]))
    completed = []
    for root in included_roots:
        task = root.name
        state = task_meta[task][0]
        if state["lifecycle"] == "DONE" and task in by_task and (not args.task or task == args.task) and (not args.project or args.project in
            {f["manifest"]["project"] for f in reconcile(selected_files(root))["files"]}):
            lifetime_data = reconcile(selected_files(root))
            lifetime, _ = summarize(lifetime_data["records"], rates)
            completed.append((task, lifetime["tokens"], lifetime["priced_usd"]))
    if completed:
        token_values = [v[1] for v in completed]
        lines += ["", "Completed tasks: {} selected roots; lifetime token mean {:.1f}, median {:.1f}, range {}–{}.".format(
            len(completed), statistics.mean(token_values), statistics.median(token_values),
            min(token_values), max(token_values))]
        usd_values = [v[2] for v in completed]
        lines.append("Priced USD among these tasks: mean {}, median {}, range {}–{}; unknown-rate portions remain excluded.".format(
            sum(usd_values) / len(usd_values),
            statistics.median(usd_values), min(usd_values), max(usd_values)))
    else:
        lines += ["", "Completed tasks: none among selected roots; no mean or median."]
    lines += ["", "Period spending includes ongoing and unsuccessful tasks with dated",
              "observations. Lifetime figures use all received dates; both retain partial coverage.", ""]
    output = "\n".join(lines)
    if args.out:
        Path(args.out).write_text(output, encoding="utf-8")
        print(json.dumps({"summary": str(args.out), "records": len(flat),
                          "tokens": total["tokens"], "priced_usd": str(total["priced_usd"])}))
    else:
        print(output)


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    common = argparse.ArgumentParser(add_help=False)
    for name in ("project", "task", "owner", "role", "unit", "source-id", "source-version"):
        common.add_argument("--" + name, required=True)
    common.add_argument("--phase")
    common.add_argument("--source", required=True)
    common.add_argument("--source-label")
    common.add_argument("--out", required=True)
    common.add_argument("--timezone", default="Z")
    common.add_argument("--start", type=int, default=0)
    common.add_argument("--end", type=int)
    common.add_argument("--revision", type=int, default=1)
    common.add_argument("--predecessor")
    common.add_argument("--complete", action="store_true")
    common.add_argument("--tfw-version")
    common.add_argument("--coordination-mode")
    common.add_argument("--includes-source", action="append", default=[],
                        help="exact namespace:source-id already included by parent counters")
    c = sub.add_parser("collect", parents=[common], help="collect one exact bound native source")
    c.add_argument("--provider", required=True,
                   choices=("codex.rollout", "claude.code-jsonl", "antigravity.ide"))
    f = sub.add_parser("failure", parents=[common], help="write typed unsuccessful capture receipt")
    f.add_argument("--provider", required=True,
                   choices=("codex.rollout", "claude.code-jsonl", "antigravity.ide"))
    f.add_argument("--code", required=True)
    f.add_argument("--detail", required=True)
    v = sub.add_parser("validate", help="validate portable contribution files")
    v.add_argument("files", nargs="+")
    r = sub.add_parser("receive", help="copy verified actual bytes to task-local roles")
    r.add_argument("--source", required=True)
    r.add_argument("--task-root", required=True)
    r.add_argument("--project", required=True)
    r.add_argument("--task", required=True)
    r.add_argument("--expected-unit", required=True)
    for command in ("report", "summary"):
        q = sub.add_parser(command)
        q.add_argument("--task-root", action="append", required=True)
        q.add_argument("--rates", default=str(Path(__file__).with_name("rates.json")))
        q.add_argument("--out")
        if command == "report":
            q.add_argument("--project", required=True)
            q.add_argument("--primary-area")
            q.add_argument("--keyword", action="append")
            q.add_argument("--expected-unit", action="append", default=[])
            q.add_argument("--accepted-result")
            q.add_argument("--status-timezone",
                           help="explicit offset of task status created/updated clock, e.g. +05:00")
        else:
            q.add_argument("--csv")
            q.add_argument("--date-from")
            q.add_argument("--date-to")
            q.add_argument("--project")
            q.add_argument("--task")
            q.add_argument("--role")
            q.add_argument("--model")
            q.add_argument("--tag")
            q.add_argument("--show-helpdesk-afd", action="store_true")
    return p


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        if args.command == "collect":
            collect(args)
        elif args.command == "failure":
            failure_receipt(args)
        elif args.command == "validate":
            print(json.dumps([{"path": f["path"], "sha256": f["sha256"],
                               "rows": len(f["rows"])} for f in
                              (validate_file(p) for p in args.files)], sort_keys=True))
        elif args.command == "receive":
            receive(args)
        elif args.command == "report":
            require(len(args.task_root) == 1, "report takes one task root")
            args.task_root = args.task_root[0]
            render_report(args)
        else:
            render_summary(args)
    except (EconomicsError, OSError, sqlite3.Error) as exc:
        print("tfw-economics: " + str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
