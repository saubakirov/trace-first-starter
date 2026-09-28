#!/usr/bin/env python3
"""Task-local checks and conversion of the returned UPM/DARYN numeric snapshots."""

import copy
import hashlib
import importlib.util
import json
import pathlib
import shutil
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[4]
TASK = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("econ", ROOT / ".tfw/economics/tfw_economics.py")
e = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e)
RATES = e.load_rates(ROOT / ".tfw/economics/rates.json")
checks = []


def check(name, okay):
    assert okay, name
    checks.append(name)


def fails(name, action, fragment):
    try:
        action()
    except e.EconomicsError as exc:
        check(name, fragment in str(exc))
    else:
        raise AssertionError(name + " unexpectedly accepted")


def manifest(**changes):
    m = dict(kind="manifest", schema_version=1, project="helpdesk", task="HD_SAMPLE",
             phase=None, owner="declared-owner", role="executor", unit="unit-a",
             source_namespace="codex.rollout", source_id="source-a", source_version="0.1",
             source_label="bound source", source_sha256="a" * 64, source_size=12,
             collector="assurance/1", revision=1, predecessor_sha256=None,
             range_start=0, range_end=5, complete=False,
             captured_at="2026-09-29T00:00:00+00:00",
             cutoff="2026-09-29T00:00:00+00:00", timezone="+05:00",
             operation_seconds=0.1, tfw_version=None, coordination_mode=None,
             unavailable={"tfw_version": "not in bound sample",
                          "coordination_mode": "not in bound sample"},
             extensions={"tfw.includes_sources": []})
    m.update(changes)
    return m


def row(index=0, tokens=None, **changes):
    r = e.usage("event:" + str(index), index, None, "+05:00", "gpt-6-sol",
                "high", tokens or e.zero_tokens(5, 7, 0, 3, 1),
                consumption_date="2026-09-28")
    r.update(changes)
    return r


def write(folder, m, rows):
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / (hashlib.sha256(json.dumps(m, sort_keys=True).encode()).hexdigest() + ".jsonl")
    e.write_jsonl(path, [m] + rows)
    return path


def contract(temp):
    m, r = manifest(), row()
    e.validate_manifest(m)
    e.validate_row(r, m)
    check("observed zero", r["tokens"]["cache_write"] == 0)
    fails("null reason", lambda: e.validate_row(row(tokens={**r["tokens"], "reasoning": None},
        unavailable={"observed_at": "date-only", "duration_seconds": "unknown"}), m), "reasoning")
    fails("cache inclusion", lambda: e.validate_row(row(tokens={**r["tokens"], "input": 5}), m),
          "input bucket sum")
    fails("reasoning inclusion", lambda: e.validate_row(row(tokens={**r["tokens"],
          "reasoning": 4}), m), "reasoning exceeds")
    fails("schema version", lambda: e.validate_manifest(manifest(schema_version=2)),
          "unsupported schema")
    fails("identity", lambda: e.validate_manifest(manifest(unit="bad unit")), "unit invalid")
    fails("revision", lambda: e.validate_manifest(manifest(predecessor_sha256="b" * 64)),
          "predecessor SHA-256")
    fails("extension", lambda: e.validate_row(row(extensions={"bare": 1}), m), "namespaced")
    e.validate_row(row(extensions={"tfw.future": 1}), m)
    check("namespaced extension", True)
    first = write(temp, m, [r])
    digest = e.validate_file(first)["sha256"]
    successor = manifest(revision=2, predecessor_sha256=digest, range_end=7,
                         source_sha256="c" * 64, complete=True,
                         extensions={"tfw.includes_sources": [],
                                     "tfw.predecessor_source_prefix_sha256": "a" * 64})
    second = write(temp, successor, [row(0), row(5)])
    result = e.reconcile([first, second], ["unit-a", "unit-b"])
    check("successor", len(result["records"]) == 2 and result["missing"] == {"unit-b"})
    bad = copy.deepcopy(successor)
    bad["extensions"]["tfw.predecessor_source_prefix_sha256"] = "f" * 64
    third = write(temp, bad, [row()])
    check("unproved prefix", len(e.reconcile([first, third])["records"]) == 1)
    disjoint = write(temp, manifest(range_start=5, range_end=10, revision=2), [row(5)])
    check("disjoint", len(e.reconcile([first, disjoint])["records"]) == 2)
    overlap = write(temp, manifest(unit="unit-b", range_start=3, range_end=8), [row(3)])
    check("overlap", len(e.reconcile([first, overlap])["records"]) == 0)
    parent = write(temp, manifest(source_id="parent",
                   extensions={"tfw.includes_sources": ["codex.rollout:source-a"]}), [row()])
    check("inclusive parent", len(e.reconcile([first, parent])["records"]) == 1)
    failure = dict(kind="failure", schema_version=1, code="source-unreadable",
                   detail="sample read failed", extensions={})
    failed = write(temp, manifest(source_id="failed", unit="unit-f"), [failure])
    result = e.reconcile([failed], ["unit-f"])
    check("failure is no measurement", result["failure_only"] == {"unit-f"} and
          not result["records"])
    dated = [(m, row(0), "first"),
             (m, row(1, consumption_date="2026-10-02"), "second"),
             (m, e.usage("undated", 2, None, "+05:00", "unknown-model", None,
                         e.zero_tokens(2, 0, 0, 1, None)), "third")]
    period, _ = e.summarize(dated, RATES, {"date_from": "2026-10-01",
                                           "date_to": "2026-10-31"})
    check("cross-month date filter", period["tokens"] == 15)
    lifetime, _ = e.summarize(dated, RATES)
    check("undated only in lifetime", lifetime["tokens"] == 33 and
          lifetime["undated_tokens"] == 3)
    check("unknown model unpriced", lifetime["unpriced_tokens"] >= 3)


def package_copy(temp):
    paths = [ROOT / ".tfw/economics" / name for name in
             ("README.md", "record.schema.json", "tfw_economics.py", "rates.json")]
    paths.append(ROOT / ".tfw/templates/economics.md")
    receiver = temp / "receiver"
    receiver.mkdir()
    for source in paths:
        dest = receiver / source.relative_to(ROOT)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, dest)
        check("receiver copied " + source.name, dest.read_bytes() == source.read_bytes())
    before = {p.relative_to(receiver): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in receiver.rglob("*") if p.is_file()}
    for source in paths:
        dest = receiver / source.relative_to(ROOT)
        if dest.read_bytes() != source.read_bytes():
            raise AssertionError("repeat install would overwrite customization")
    after = {p.relative_to(receiver): hashlib.sha256(p.read_bytes()).hexdigest()
             for p in receiver.rglob("*") if p.is_file()}
    check("repeat package copy stable", before == after)
    changed = receiver / paths[0].relative_to(ROOT)
    changed.write_bytes(changed.read_bytes() + b"\nlocal customization\n")
    check("custom receiver preserved",
          changed.read_bytes() != paths[0].read_bytes() and
          all((receiver / p.relative_to(ROOT)).is_file() for p in paths))


def snapshot(name):
    s = (TASK / "samples/codex" / name / "economics.md").read_text(encoding="utf-8")
    return json.loads(s.split("```json", 1)[1].split("```", 1)[0])


def owner(status):
    return next(line.split(":", 1)[1].strip() for line in
                status.read_text(encoding="utf-8").splitlines() if line.startswith("owner:"))


def convert(name, temp):
    saved = snapshot(name)
    root = temp / saved["task_id"]
    root.mkdir()
    source_status = pathlib.Path(saved["task_status_source"])
    check(name + " status exists", source_status.is_file())
    shutil.copyfile(source_status, root / "status.md")
    paths = []
    for session in saved["sessions"]:
        source = session["source"]
        rows = []
        for index, (label, counters) in enumerate(session["models"].items()):
            model, effort = [x.strip() for x in label.split(" / ", 1)]
            tokens = e.zero_tokens(
                counters["input_tokens"] - counters["cached_input_tokens"] -
                counters["cache_write_input_tokens"], counters["cached_input_tokens"],
                counters["cache_write_input_tokens"], counters["output_tokens"],
                counters["reasoning_output_tokens"])
            check(name + " model arithmetic", tokens["total"] == counters["total_tokens"])
            rows.append(e.usage("saved-model:" + str(index), index, None, "+05:00",
                                model, effort, tokens,
                                unavailable={"observed_at": "saved model total has no event timestamp",
                                             "consumption_date": "model total spans days",
                                             "duration_seconds": "model timer split unavailable"},
                                extensions={"tfw.saved_source_hash": source["sha256"]}))
        duration = session["completed_turn_duration_ms"]
        if duration:
            rows.append(e.usage("saved-duration", len(rows), None, "+05:00",
                                None, None, e.zero_tokens(0, 0, 0, 0, 0),
                                duration=duration / 1000, duration_kind="completed_turn"))
        version = (source.get("session_meta") or [{}])[0].get("cli_version") or "unknown"
        m = manifest(project=saved["project"], task=saved["task_id"],
                     owner=owner(source_status), role="historical",
                     unit=session["session_id"], source_id=session["session_id"],
                     source_version=version,
                     source_label=pathlib.Path(source["path"]).name,
                     source_sha256=source["sha256"], source_size=source["bytes"],
                     range_end=max(source["usage_line"] + 1, len(rows) + 1),
                     captured_at=saved["capture_started_at"],
                     cutoff=saved["capture_started_at"], operation_seconds=None,
                     unavailable={"tfw_version": "not bound in saved report",
                                  "coordination_mode": "not bound in saved report",
                                  "operation_seconds": "historical capture did not measure conversion"},
                     extensions={"tfw.includes_sources": [], "tfw.saved_snapshot": name})
        path = write(root / "economics/roles", m, rows)
        e.validate_file(path)
        paths.append(path)
        check(name + " source session sum",
              sum(r["tokens"]["total"] for r in rows) == session["raw_usage"]["total_tokens"])
    result = e.reconcile(paths, [s["session_id"] for s in saved["sessions"]])
    total, _ = e.summarize(result["records"], RATES)
    expected = {"upm": 1_509_525_191, "daryn": 184_937_058}[name]
    check(name + " known total", total["tokens"] == expected)
    check(name + " undated lifetime", total["undated_tokens"] == expected)
    return saved, root, paths


def main():
    with tempfile.TemporaryDirectory(prefix="teqm-economics-assurance-") as td:
        temp = pathlib.Path(td)
        contract(temp / "contract")
        package_copy(temp)
        sources = [convert(name, temp) for name in ("upm", "daryn")]
        for saved, root, paths in sources:
            received = temp / ("receive-" + root.name) / root.name
            received.mkdir(parents=True)
            shutil.copyfile(root / "status.md", received / "status.md")
            args = type("Args", (), dict(source=str(paths[0]), task_root=str(received),
                         project=saved["project"], task=root.name,
                         expected_unit=saved["sessions"][0]["session_id"]))
            e.receive(args)
            e.receive(args)
            check("idempotent receive " + root.name, len(e.selected_files(received)) == 1)
            pilot_name = "pilot_" + ("upm" if "UPM" in root.name else "daryn") + ".md"
            report_args = type("Args", (), dict(task_root=str(root), project=saved["project"],
                rates=str(ROOT / ".tfw/economics/rates.json"),
                expected_unit=[s["session_id"] for s in saved["sessions"]],
                primary_area=saved["primary_area"], keyword=saved["keywords"][:5],
                accepted_result="saved sample only", status_timezone="+05:00",
                out=str(temp / pilot_name)))
            e.render_report(report_args)
            check("pilot report total " + root.name,
                  e.metadata_block(report_args.out)["totals"]["tokens"] ==
                  saved["tokens"]["total_tokens"])
            shutil.copyfile(report_args.out, root / "economics.md")
            pilot = TASK / "evidence" / pilot_name
            if not pilot.exists():
                shutil.copyfile(report_args.out, pilot)
            check("saved pilot total " + root.name,
                  e.metadata_block(pilot)["totals"]["tokens"] ==
                  saved["tokens"]["total_tokens"])
        args = type("Args", (), dict(task_root=[str(x[1]) for x in sources],
             rates=str(ROOT / ".tfw/economics/rates.json"), date_from=None,
             date_to=None, project=None, task=None, role=None, model=None, tag=None,
             show_helpdesk_afd=True, csv=str(TASK / "evidence/pilot_selected.csv"),
             out=str(TASK / "evidence/pilot_selected.md")))
        e.render_summary(args)
        summary = pathlib.Path(args.out).read_text(encoding="utf-8")
        check("afd gap", "| afd | no captured data |" in summary)
        check("two real sample totals", "1,509,525,191" in summary and
              "184,937,058" in summary)
        for tag, saved, root, _ in (("upm", *sources[0]), ("daryn", *sources[1])):
            args.tag = saved["primary_area"]
            args.out = str(temp / (tag + "-tag.md"))
            args.csv = str(temp / (tag + "-tag.csv"))
            e.render_summary(args)
            tagged = pathlib.Path(args.out).read_text(encoding="utf-8")
            check(tag + " overlapping area/tag does not multiply",
                  "{:,}".format(saved["tokens"]["total_tokens"]) in tagged)
        names = ("plan", "research", "handoff", "review", "docs", "knowledge",
                 "release", "update", "config", "init")
        for name in names:
            canonical = ROOT / ".tfw/workflows" / (
                "research/base.md" if name == "research" else name + ".md")
            installed = ROOT / ".claude/commands" / ("tfw-" + name + ".md")
            check("installed copy " + name, canonical.read_bytes() == installed.read_bytes())
    print(json.dumps({"result": "PASS", "checks": len(checks)}, sort_keys=True))


if __name__ == "__main__":
    main()
