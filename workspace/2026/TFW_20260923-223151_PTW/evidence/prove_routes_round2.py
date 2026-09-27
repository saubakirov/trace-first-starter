"""Finite interpretation of shipped prose routes; no installer, host run or permanent test.

The read-only route guards bind the interpretation to exact clauses/ordering. Concrete filesystem
effects then follow those clauses, including excluded generic copies and the terminal repair branch.
This is stronger than direct map-helper replay, but remains an Executor interpretation for Review.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import yaml
from prove_package import COMMON, ENTRIES, PREFIX, inventory, write

ROOT = Path(__file__).resolve().parents[4]
EV = Path(__file__).resolve().parent
PRIOR = "5d57157f8b07b0dc5be3e51756af61b57d5411dd"


def source(path):
    return (ROOT / path).read_text(encoding="utf-8")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def bind_routes(update, init):
    u2 = update.index("## Step 2")
    gate = update.index("### Daily prewrite gate", u2)
    u3 = update.index("## Step 3")
    generic = update.index("Copy approved pinned payload", u3)
    u4 = update.index("## Step 4")
    assert u2 < gate < u3 < generic < u4
    clauses = ["Exclude `extensions/daily-task/` and both Daily discovery targets",
               "before Step 3", "Keep refused paths excluded", "Never remove these exclusions",
               "Apply accepted Daily rows", "Verify Step 2/3 Daily actions"]
    assert all(x in update for x in clauses)
    i0 = init.index("## Step 0")
    attach = init.index("**Attach/repair:**", i0)
    invocation = init.index("run the Daily prewrite gate below", attach)
    apply_full = init.index("apply its persistent row and all ten command rows", invocation)
    optional = init.index("apply/check", apply_full)
    stop = init.index("then stop.", optional)
    i1 = init.index("## Step 1")
    igate = init.index("### Daily prewrite gate", i0)
    assert i0 < attach < invocation < apply_full < optional < stop < igate < i1
    assert "before any setup/repair write" in init and "repair runs it" in init
    assert "inside Step 0 before its terminal stop" in init
    assert "skip discovery, research" in init and "Without explicit Daily opt-in" in init
    def line(text, offset):
        return text[:offset].count("\n") + 1
    return {"update": {"gate": line(update, gate), "generic": line(update, generic),
                       "apply": line(update, update.index("Apply accepted Daily rows")),
                       "verify": line(update, update.index("Verify Step 2/3"))},
            "repair": {"gate_call": line(init, invocation), "full_apply": line(init, apply_full),
                       "daily_apply_verify": line(init, optional), "stop": line(init, stop),
                       "gate_definition": line(init, igate)}}


def classify(receiver, payload, previous, selected, preserve_form):
    desired = {p: payload[p] for p in COMMON}
    desired.update({ENTRIES[k]: payload[PREFIX + f"entries/{k}/SKILL.md"] for k in selected})
    actions = {}
    for path, data in desired.items():
        f = receiver / path
        old = f.read_bytes() if f.exists() else None
        if old is None:
            actions[path] = "APPLIED"
        elif old == data:
            actions[path] = "UNCHANGED"
        elif path == PREFIX + "templates/task.md" and preserve_form:
            authority = (receiver / "AGENTS.md").read_bytes()
            assert b"project-selected local form" in authority
            assert all(term in old for term in [b"Source", b"Goal", b"Value", b"Boundaries", b"Check"])
            actions[path] = "PRESERVED"
        elif old == previous.get(path):
            actions[path] = "APPLIED"
        else:
            return {"result": "REFUSED", "path": path, "actions": {}, "writes": 0}, desired
    return {"result": "ACCEPTED", "actions": actions}, desired


def execute(receiver, kind, payload, previous, selected, form, full_rows, routes):
    log = []
    before = inventory(receiver)
    daily_before = {p: h for p, h in before.items() if p.startswith(PREFIX) or p in ENTRIES.values()}
    excluded = set(COMMON) | set(ENTRIES.values())
    group_writes = []; generic_writes = []
    # Update's target includes Daily even without opt-in. Repair with no opt-in excludes it entirely.
    if kind == "repair" and not selected:
        decision, desired = {"result": "EXCLUDED", "actions": {}}, {}
    else:
        decision, desired = classify(receiver, payload, previous, selected, form)
    log.append({"operation": "classify_or_exclude", "line": routes[kind]["gate" if kind == "update" else "gate_call"],
                "result": decision["result"], "inventory_after": inventory(receiver)})
    assert inventory(receiver) == before, "Classification must be read-only"
    # Actual generic-copy counterfactual includes Daily rows. All must remain excluded here.
    generic = dict(full_rows)
    if kind == "update":
        generic.update(payload)
    for path, data in generic.items():
        if path in excluded:
            continue
        if not (receiver / path).exists() or (receiver / path).read_bytes() != data:
            write(receiver, path, data); generic_writes.append(path)
    log.append({"operation": "generic_with_exclusions", "line": routes[kind]["generic" if kind == "update" else "full_apply"],
                "excluded": sorted(excluded), "writes": generic_writes})
    if decision["result"] == "ACCEPTED":
        for path, action in decision["actions"].items():
            if action == "APPLIED":
                write(receiver, path, desired[path]); group_writes.append(path)
    log.append({"operation": "accepted_daily_apply", "line": routes[kind]["apply" if kind == "update" else "daily_apply_verify"],
                "writes": group_writes})
    after = inventory(receiver)
    if decision["result"] in ["REFUSED", "EXCLUDED"]:
        assert not group_writes
        assert daily_before == {p: h for p, h in after.items() if p.startswith(PREFIX) or p in ENTRIES.values()}
    else:
        for path, action in decision["actions"].items():
            if action != "PRESERVED":
                assert (receiver / path).read_bytes() == desired[path]
            else:
                assert after[path] == before[path], "Chosen compatible form retains exact bytes"
        for key in selected:
            assert (receiver / ENTRIES[key]).read_bytes() == payload[PREFIX + f"entries/{key}/SKILL.md"]
            assert b".tfw/extensions/daily-task/SKILL.md" in (receiver / ENTRIES[key]).read_bytes()
            assert (receiver / PREFIX / "SKILL.md").read_bytes() == payload[PREFIX + "SKILL.md"]
    for path, h in before.items():
        if path.startswith("daily/") or path in [".tfw/project_config.yaml", "workspace/old/status.md", "foreign.txt", "AGENTS.md"]:
            assert after[path] == h, path
    for key, path in ENTRIES.items():
        if key not in selected:
            assert after.get(path) == before.get(path), "Unselected entry must retain absence/bytes"
    assert len(list((receiver / ".claude/commands").glob("tfw-*.md"))) == 10
    log.append({"operation": "verify_then_terminal_stop" if kind == "repair" else "verify_receipt_inputs",
                "line": routes[kind]["stop" if kind == "repair" else "verify"],
                "discovery": False, "interview": False, "research": False})
    return {"decision": decision, "log": log, "before": before, "after": after,
            "Daily_writes": group_writes, "generic_writes": generic_writes,
            "configured_state_history_foreign_preserved": True, "Full_commands": 10}


def main():
    texts = {p: source(p) for p in [".tfw/workflows/init.md", ".tfw/workflows/update.md", *COMMON]}
    routes = bind_routes(texts[".tfw/workflows/update.md"], texts[".tfw/workflows/init.md"])
    old_update = subprocess.check_output(["git", "show", PRIOR + ":.tfw/workflows/update.md"]).decode()
    old_init = subprocess.check_output(["git", "show", PRIOR + ":.tfw/workflows/init.md"]).decode()
    try:
        bind_routes(old_update, old_init)
    except (ValueError, AssertionError):
        original_rejected = True
    else:
        raise AssertionError("Original defective ordered route must not pass")
    payload = {p: texts[p].encode() for p in COMMON}
    previous = {p: subprocess.check_output(["git", "show", PRIOR + ":" + p]) for p in COMMON}
    manifest = yaml.safe_load(source(".tfw/adapters/manifest.yaml"))
    assert len(manifest["commands"]) == 10
    full_rows = {}
    for command, row in manifest["commands"].items():
        data = source(row["workflow"]).encode()
        full_rows[row["workflow"]] = data
        full_rows[f".claude/commands/tfw-{command}.md"] = data
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    root = EV / "receivers" / ("round2-" + stamp)
    assert not root.exists()
    report = {"authority": "REVIEW closed F1/F2 @ 2465774b4fd53e6e3f7b28fbc273e0d7ae90c659",
              "kind": "finite filesystem interpretation of actual shipped ordered prose; not native invocation",
              "routes": routes, "original_route_rejected": original_rejected,
              "source": {p: {"utf8_text": t, "sha256_LF": sha(t.encode())} for p, t in texts.items()},
              "prior_source": PRIOR, "cases": {}}
    specs = [("no-opt-in", [], None, False), ("selected-codex", ["codex"], None, False),
             ("selected-claude", ["claude-code"], None, False), ("selected-both", list(ENTRIES), None, False),
             ("compatible-form", ["codex"], "compatible", True),
             ("dormant-custom-source", [], "canonical", False),
             ("dormant-ambiguous-form", [], "ambiguous", False),
             ("foreign-entry", ["codex"], "entry", False),
             ("selected-ambiguous-form", ["codex"], "ambiguous", False)]
    for kind in ["update", "repair"]:
        for name, selected, customization, preserve in specs:
            r = root / (kind + "-" + name)
            for path, data in full_rows.items():
                write(r, path, data)
            if kind == "update":
                write(r, ".tfw/workflows/init.md", b"old verified generic framework payload\n")
            for path, data in previous.items():
                write(r, path, data)
            write(r, ".tfw/project_config.yaml", b"build: {test: owner-selected-check}\ntfw: {task_containers: [workspace]}\n")
            write(r, "workspace/old/status.md", b"owner-preserved historical state\n")
            write(r, "foreign.txt", b"foreign neighbor\n")
            write(r, "AGENTS.md", b"Daily uses project-selected local form; preserve task/brief/messages.\n")
            for filename in ["task.md", "brief.md", "messages.md"]:
                write(r, "daily/2025/old/" + filename, ("sealed meaning: " + filename).encode())
            # Existing foreign unselected entry must never be discovered/overwritten.
            if "claude-code" not in selected:
                write(r, ENTRIES["claude-code"], b"unrelated field skill, no opt-in\n")
            if customization == "compatible":
                write(r, PREFIX + "templates/task.md", b"# Local form\nSource / Goal / Value / Boundaries / Context / Result / Check / Next\n")
            elif customization == "canonical":
                write(r, PREFIX + "SKILL.md", b"private customized canonical source\n")
            elif customization == "ambiguous":
                write(r, PREFIX + "templates/task.md", b"private ambiguous local form\n")
            elif customization == "entry":
                write(r, ENTRIES["codex"], b"foreign selected entry\n")
            first = execute(r, kind, payload, previous, selected, preserve, full_rows, routes)
            repeat = execute(r, kind, payload, payload, selected, preserve, full_rows, routes)
            assert first["after"] == repeat["after"] and not repeat["Daily_writes"] and not repeat["generic_writes"]
            expected = "EXCLUDED" if kind == "repair" and not selected else "REFUSED" if customization in ["canonical", "ambiguous", "entry"] else "ACCEPTED"
            assert first["decision"]["result"] == expected, (kind, name, first)
            if expected == "REFUSED":
                assert not first["Daily_writes"]
            if kind == "repair" and expected in ["REFUSED", "EXCLUDED"]:
                assert first["before"] == first["after"]
            report["cases"][kind + "-" + name] = {"root": r.relative_to(EV).as_posix(),
                                                      "first": first, "repeat": repeat, "repeat_diff": []}
    # The Reviewer's precise failure mechanism remains observable, not just a string guard.
    r = root / "counterfactual-copy-before-gate"
    form = PREFIX + "templates/task.md"
    write(r, form, b"private ambiguous local form\n")
    before = inventory(r)
    early, _ = classify(r, payload, previous, [], False)
    assert early["result"] == "REFUSED" and inventory(r) == before
    for path, data in payload.items():
        write(r, path, data)
    late, _ = classify(r, payload, previous, [], False)
    assert late["result"] == "ACCEPTED" and inventory(r)[form] != before[form]
    report["counterfactual"] = {"early_refusal_zero_writes": True, "generic_before_gate_loses_form": True,
                                "late_gate_false_accept": True, "not_the_shipped_fixed_route": True}
    (EV / "route-proof-round2.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"cases": len(report["cases"]), "routes": routes, "all_repeat_no_diff": True,
                      "original_route_rejected": original_rejected, "receiver_root": root.relative_to(EV).as_posix()}))


if __name__ == "__main__":
    main()
