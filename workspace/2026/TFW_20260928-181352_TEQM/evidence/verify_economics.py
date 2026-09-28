#!/usr/bin/env python3
"""Task-local checks and conversion of the returned UPM/DARYN numeric snapshots."""

import copy
import hashlib
import importlib.util
import json
import pathlib
import shutil
import subprocess
import tempfile
from decimal import Decimal

ROOT = pathlib.Path(__file__).resolve().parents[4]
TASK = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("econ", ROOT / ".tfw/economics/tfw_economics.py")
e = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e)
RATES = e.load_rates(ROOT / ".tfw/economics/rates.json")
checks = []
RETURN_REF = "94ebaf4908fb167db42cfb81582752b70e256e4f"


def check(name, okay):
    assert okay, name
    checks.append(name)


def preserve_attachment(source, name):
    target = TASK / "evidence" / name
    if not target.exists():
        shutil.copyfile(source, target)
    check("reviewable attachment " + name, target.is_file())
    return target


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


def revision_stream(temp):
    fields = ("input_tokens", "cached_input_tokens", "cache_write_input_tokens",
              "output_tokens", "reasoning_output_tokens", "total_tokens")

    def counters(fresh, cached, output):
        values = (fresh + cached, cached, 0, output, 0, fresh + cached + output)
        return dict(zip(fields, values))

    first, second = counters(7, 3, 2), counters(15, 5, 3)
    thread_one, thread_two = first, counters(22, 8, 5)
    count_one, count_two = counters(6, 3, 1), counters(19, 8, 3)

    def event(kind, payload):
        return {"type": kind, "payload": payload,
                "timestamp": "2026-09-29T00:00:00Z"}

    def response(identifier, usage_value, thread_value):
        return event("token_usage_record",
                     {"session_id": "source-a", "response_id": identifier,
                      "usage": usage_value, "thread_token_usage": thread_value})

    raw_events = [
        event("session_meta", {"id": "source-a"}),
        event("turn_context", {"model": "gpt-6-sol", "effort": "high", "turn_id": "turn-a"}),
        event("event_msg", {"type": "task_started", "turn_id": "turn-a"}),
        response("response-a", first, thread_one),
        event("event_msg", {"type": "token_count",
                            "info": {"total_token_usage": count_one,
                                     "last_token_usage": count_one}}),
        response("response-b", second, thread_two),
        response("response-b", second, thread_two),
        event("event_msg", {"type": "token_count",
                            "info": {"total_token_usage": count_two,
                                     "last_token_usage": counters(13, 5, 2)}}),
        event("event_msg", {"type": "task_complete", "turn_id": "turn-a",
                            "duration_ms": 1200}),
    ]
    raw = "".join(json.dumps(x) + "\n" for x in raw_events).encode()
    args = type("Args", (), dict(source_id="source-a", timezone="+05:00",
                                 start=0, end=None))
    rows, diagnostics = e.codex_rows(raw, args)
    check("F1 response sum selected without duplicate",
          sum(r["tokens"]["total"] for r in rows) == 35)
    check("F1 native conflict is visible",
          any("token_count total 30 differs" in note and "thread total 35" in note
              for note in diagnostics))
    check("F1 completed-turn timer remains distinct",
          sum(r["duration_seconds"] or 0 for r in rows) == 1.2)
    damaged = copy.deepcopy(raw_events)
    damaged[6]["payload"]["thread_token_usage"] = counters(21, 8, 5)
    bad_raw = "".join(json.dumps(x) + "\n" for x in damaged).encode()
    fails("F1 inconsistent native thread total refused",
          lambda: e.codex_rows(bad_raw, args), "response sum disagrees")
    leading_count = copy.deepcopy(raw_events)
    leading_count[7]["payload"]["info"]["total_token_usage"] = counters(30, 8, 2)
    leading_count[7]["payload"]["info"]["last_token_usage"] = counters(24, 5, 1)
    leading_raw = "".join(json.dumps(x) + "\n" for x in leading_count).encode()
    fails("F1 later larger count tail refused",
          lambda: e.codex_rows(leading_raw, args), "token_count exceeds")
    no_responses = [x for x in raw_events if x["type"] != "token_usage_record"]
    count_only = "".join(json.dumps(x) + "\n" for x in no_responses).encode()
    rows, notes = e.codex_rows(count_only, args)
    check("F1 count-only source is explicit",
          sum(r["tokens"]["total"] for r in rows) == 30 and
          any("only observed native usage stream" in note for note in notes))
    reconciliation = json.loads(subprocess.check_output(
        ["git", "show", RETURN_REF + ":workspace/2026/TFW_20260928-181352_TEQM/"
         "economics/preparation/coordinator-v1-reconciliation.json"], cwd=ROOT))
    check("F1 returned same-prefix native discrepancy",
          reconciliation["helper_token_count_total"] == 62_902_737 and
          reconciliation["token_usage_record_sum"]["total_tokens"] == 64_405_038 and
          reconciliation["native_thread_token_usage"]["total_tokens"] == 64_405_038 and
          reconciliation["difference_total_tokens"] == 1_502_301)


def fixture_status(path, task, title):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n"
                    "id: " + task + "\n"
                    "title: \"" + title + "\"\n"
                    "goal: \"Measure this fixture\"\n"
                    "value: \"Verify phase selection\"\n"
                    "lifecycle: ONB\n"
                    "owner: declared-owner\n"
                    "created: 20260928-181352\n"
                    "updated: 20260929-000000\n"
                    "---\n", encoding="utf-8")


def revision_phases(temp):
    root = temp / "TFW_SAMPLE"
    phase = root / "phase-a"
    fixture_status(root / "status.md", root.name, "Root fixture")
    fixture_status(phase / "status.md", root.name, "Phase A: fixture")
    root_manifest = manifest(project="steps-framework", task=root.name,
                             source_id="root-source", unit="root-unit")
    phase_manifest = manifest(project="steps-framework", task=root.name,
                              phase="phase-a", source_id="phase-source",
                              unit="phase-unit")
    root_file = write(root / "economics/roles", root_manifest,
                      [row(tokens=e.zero_tokens(5, 0, 0, 2, 0))])
    phase_file = write(phase / "economics/roles", phase_manifest,
                       [row(tokens=e.zero_tokens(3, 0, 0, 2, 0),
                            consumption_date="2026-10-02")])
    paths, phases, gaps = e.task_sources(root)
    data = e.reconcile(paths, ["root-unit", "phase-unit"])
    e.check_task_sources(root, data["files"])
    total, _ = e.summarize(data["records"], RATES)
    check("F2 root plus phase once", total["tokens"] == 12 and
          phases == ["phase-a"] and not gaps)
    period, _ = e.summarize(data["records"], RATES,
                            {"date_from": "2026-10-01", "date_to": "2026-10-31"})
    check("F2 dated phase selected", period["tokens"] == 5)
    duplicate = phase_file.with_name("same-bytes.jsonl")
    shutil.copyfile(phase_file, duplicate)
    data = e.reconcile(e.selected_files(root))
    check("F2 identical phase bytes counted once",
          e.summarize(data["records"], RATES)[0]["tokens"] == 12 and
          any("counted once" in note for note in data["diagnostics"]))
    duplicate.unlink()
    report_args = type("Args", (), dict(task_root=str(root), project="steps-framework",
          rates=str(ROOT / ".tfw/economics/rates.json"), expected_unit=["root-unit", "phase-unit"],
          primary_area="fixture", keyword=["phase", "root", "cost"],
          accepted_result=None, status_timezone="+05:00",
          out=str(root / "economics.md")))
    e.render_report(report_args)
    block = e.metadata_block(report_args.out)
    check("F2 root report includes phase",
          block["totals"]["tokens"] == 12 and block["phase_roots"] == ["phase-a"])
    report_args.task_root, report_args.out = str(phase), str(phase / "economics.md")
    report_args.expected_unit = ["phase-unit"]
    e.render_report(report_args)
    check("F2 phase report is leaf only",
          e.metadata_block(report_args.out)["totals"]["tokens"] == 5)
    fixture_status(root / "phase-b/status.md", root.name, "Phase B: no return")
    _, _, gaps = e.task_sources(root)
    check("F2 missing phase bytes explicit",
          gaps == ["phase-b: no returned role bytes"])
    report_args.task_root, report_args.out = str(root), str(temp / "root-with-gap.md")
    report_args.expected_unit = ["root-unit", "phase-unit"]
    e.render_report(report_args)
    check("F2 root report names missing phase",
          e.metadata_block(report_args.out)["phase_coverage_gaps"] == gaps)
    attached = preserve_attachment(report_args.out, "revision_phase_root.md")
    check("F2 saved phase report", e.metadata_block(attached)["totals"]["tokens"] == 12)
    summary_args = type("Args", (), dict(task_root=[str(root)], rates=report_args.rates,
          date_from="2026-10-01", date_to="2026-10-31", project=None, task=None,
          role=None, model=None, tag=None, show_helpdesk_afd=False,
          csv=str(temp / "phase-period.csv"), out=str(temp / "phase-period.md")))
    e.render_summary(summary_args)
    text = pathlib.Path(summary_args.out).read_text(encoding="utf-8")
    check("F2 selected period and coverage",
          "| steps-framework | 5 |" in text and "phase-b: no returned role bytes" in text)
    attached = preserve_attachment(summary_args.out, "revision_phase_period.md")
    check("F2 saved period view",
          "| steps-framework | 5 |" in attached.read_text(encoding="utf-8"))
    summary_args.task_root = [str(root), str(phase), str(root)]
    summary_args.out = str(temp / "overlap-selection.md")
    e.render_summary(summary_args)
    check("F2 root and explicit phase selection counted once",
          "| steps-framework | 5 |" in pathlib.Path(summary_args.out).read_text(encoding="utf-8"))


def returned_bytes(relative_path, expected_sha):
    content = subprocess.check_output(
        ["git", "show", RETURN_REF + ":" + relative_path], cwd=ROOT)
    check("returned exact bytes " + expected_sha[:8],
          hashlib.sha256(content).hexdigest() == expected_sha)
    return content


def revision_real_return(temp):
    task = "TFW_20260928-181352_TEQM"
    root = temp / task
    root.mkdir(parents=True)
    shutil.copyfile(TASK / "status.md", root / "status.md")
    roles = root / "economics/roles"
    roles.mkdir(parents=True)
    coordinator = "a5f42644c0cd185bb70c093787d9b1c8741b300894d26ffd3fd2f4896961e6e1"
    researcher = "eaf560cb0c592b440eb6821e7302aa93717ff378604dd472eb7ea96a618a0eb0"
    for digest in (coordinator, researcher):
        relative = "workspace/2026/" + task + "/economics/roles/" + digest + ".jsonl"
        (roles / (digest + ".jsonl")).write_bytes(returned_bytes(relative, digest))
    executor = "ef80eb0f7221c4f75f0b161e843cc685a115c781aab2ef6fd6a0e963b7907db5"
    shutil.copyfile(TASK / "economics/roles" / (executor + ".jsonl"),
                    roles / (executor + ".jsonl"))
    data = e.reconcile(e.selected_files(root))
    check("F3 three actual units received",
          len(data["received"]) == 3 and len(data["measured"]) == 3)
    total, _ = e.summarize(data["records"], RATES)
    check("F3 three-role token total", total["tokens"] == 121_552_538)
    item = e.validate_file(roles / (researcher + ".jsonl"))
    zero_write = next(r["tokens"] for r in item["rows"] if r["kind"] == "usage" and
                      r["tokens"]["total"] > 0)
    researcher_model = next(r["model"] for r in item["rows"] if r["kind"] == "usage"
                            and r["tokens"]["total"] > 0)
    observed_cost, _ = e.price(zero_write, researcher_model, RATES)
    card = RATES["models"][researcher_model]
    expected_cost = (Decimal(zero_write["fresh"]) * Decimal(str(card["fresh"])) +
                     Decimal(zero_write["cached"]) * Decimal(str(card["cached"])) +
                     Decimal(zero_write["output"]) * Decimal(str(card["output"]))) / 1_000_000
    check("F3 real nullable zero writes price",
          zero_write["cache_write"] == 0 and
          zero_write["cache_write_5m"] is None and
          observed_cost == expected_cost)
    unsplit = copy.deepcopy(zero_write)
    unsplit["cache_write"] = 1
    unsplit["fresh"] -= 1
    e.validate_tokens(unsplit, {"cache_write_5m": "positive split unknown",
                                "cache_write_1h": "positive split unknown",
                                "reasoning": "source optional subset unknown"})
    cost, gap = e.price(unsplit, "gpt-6-sol", RATES)
    check("F3 positive unsplit writes unpriced",
          cost is None and "split unavailable" in gap)
    args = type("Args", (), dict(task_root=str(root), project="steps-framework",
          rates=str(ROOT / ".tfw/economics/rates.json"),
          expected_unit=sorted(data["received"]),
          primary_area=None, keyword=None, accepted_result=None,
          status_timezone="+05:00", out=str(temp / "three-role-report.md")))
    e.render_report(args)
    block = e.metadata_block(args.out)
    check("F3 actual three-role report rendered",
          block["totals"]["tokens"] == 121_552_538 and
          Decimal(block["totals"]["priced_usd"]) == total["priced_usd"] and
          not block["missing"])
    check("F1 adapted source conflict visible in actual report",
          any(x["source_qualification"].get("tfw.counter_difference_tokens") == 1_502_301
              for x in block["source_diagnostics"]) and
          "Source qualification" in pathlib.Path(args.out).read_text(encoding="utf-8"))
    attached = preserve_attachment(args.out, "revision_three_role.md")
    check("F3 saved three-role report",
          e.metadata_block(attached)["totals"]["tokens"] == 121_552_538)


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
        revision_stream(temp)
        revision_phases(temp / "phases")
        revision_real_return(temp / "actual-return")
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
