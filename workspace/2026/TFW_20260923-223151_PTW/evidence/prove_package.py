"""Finite PTW installation proof; not a shipped installer or permanent test."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import yaml
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[4]
EV = Path(__file__).resolve().parent
PREFIX = ".tfw/extensions/daily-task/"
COMMON = [PREFIX + x for x in ["SKILL.md", "templates/task.md", "installation.md",
          "entries/codex/SKILL.md", "entries/claude-code/SKILL.md"]]
ENTRIES = {"codex": ".agents/skills/tfw-daily-task/SKILL.md",
           "claude-code": ".claude/skills/tfw-daily-task/SKILL.md"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def inventory(receiver):
    return {p.relative_to(receiver).as_posix(): sha(p.read_bytes())
            for p in sorted(receiver.rglob("*")) if p.is_file()}


def write(receiver, path, data):
    target = receiver / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)


def install(receiver, payload, selected, previous=None, preserve_form=False):
    """Replay the authored instruction map, checking the whole group before writes."""
    desired = {p: payload[p] for p in COMMON}
    desired.update({ENTRIES[k]: payload[PREFIX + f"entries/{k}/SKILL.md"] for k in selected})
    actions = {}
    for path, data in desired.items():
        target = receiver / path
        old = target.read_bytes() if target.exists() else None
        if old is None:
            actions[path] = "APPLIED"
        elif old == data:
            actions[path] = "UNCHANGED"
        elif path == PREFIX + "templates/task.md" and preserve_form:
            assert b"project-selected local form" in (receiver / "AGENTS.md").read_bytes()
            actions[path] = "PRESERVED"
        elif previous is not None and old == previous.get(path):
            actions[path] = "APPLIED"
        else:
            return {"result": "REFUSED", "path": path, "writes": 0}
    for path, action in actions.items():
        if action == "APPLIED":
            write(receiver, path, desired[path])
    for key in selected:
        assert (receiver / ENTRIES[key]).read_bytes() == payload[PREFIX + f"entries/{key}/SKILL.md"]
        assert (receiver / PREFIX / "SKILL.md").exists()
    return {"result": "VERIFIED", "actions": actions}


def full(receiver):
    manifest = yaml.safe_load((ROOT / ".tfw/adapters/manifest.yaml").read_text(encoding="utf-8"))
    assert len(manifest["commands"]) == 10
    write(receiver, ".tfw/adapters/manifest.yaml", (ROOT / ".tfw/adapters/manifest.yaml").read_bytes())
    for command, row in manifest["commands"].items():
        data = (ROOT / row["workflow"]).read_bytes()
        write(receiver, row["workflow"], data)
        write(receiver, f".claude/commands/tfw-{command}.md", data)
        write(receiver, f".agents/skills/tfw-{command}/SKILL.md",
              (ROOT / f".tfw/adapters/codex/skills/tfw-{command}/SKILL.md").read_bytes())
    for path in COMMON:
        write(receiver, path, (ROOT / path).read_bytes())
    write(receiver, "foreign.txt", b"unrelated receiver bytes\n")
    write(receiver, "daily/2025/20250101-120000_previous/task.md", b"sealed historical record\n")


def main():
    payload = {p: (ROOT / p).read_bytes() for p in COMMON}
    hashes = {p: sha(data) for p, data in payload.items()}
    snapshot_id = sha(json.dumps(hashes, sort_keys=True).encode())
    source_root = EV / "package-snapshots" / snapshot_id
    for path, data in payload.items():
        target = source_root / path
        if target.exists():
            assert target.read_bytes() == data
        else:
            write(source_root, path, data)
    # Read the exact saved snapshot, never a moving source during installation.
    payload = {p: (source_root / p).read_bytes() for p in COMMON}
    report = {"origin": "Executor-authored finite fixture; no live provider invocation",
              "source": {"kind": "content-addressed local snapshot, not release",
                         "snapshot_sha256": snapshot_id, "files": hashes,
                         "authority": "TS approval + SR1 @ b2c9cf63bab878f83e071fccaec1c2de9677544f"},
              "cases": {}}
    fixture_root = EV / "receivers" / (snapshot_id[:12] + "-" + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S"))
    assert not fixture_root.exists(), "Fresh receiver proof refuses an existing root"
    for name, selected in [("no-opt-in", []), ("codex", ["codex"]),
                           ("claude", ["claude-code"]), ("both", list(ENTRIES))]:
        receiver = fixture_root / name
        full(receiver)
        before = inventory(receiver)
        result = install(receiver, payload, selected)
        assert result["result"] == "VERIFIED"
        after = inventory(receiver)
        repeat = install(receiver, payload, selected)
        assert repeat["result"] == "VERIFIED"
        assert inventory(receiver) == after
        for key, path in ENTRIES.items():
            assert (receiver / path).exists() == (key in selected)
        assert before["foreign.txt"] == after["foreign.txt"]
        old_record = "daily/2025/20250101-120000_previous/task.md"
        assert before[old_record] == after[old_record]
        assert len(list((receiver / ".claude/commands").glob("tfw-*.md"))) == 10
        report["cases"][name] = {"root": receiver.relative_to(EV).as_posix(),
                                  "install": result, "repeat": repeat, "before": before, "after": after,
                                  "repeat_diff": [], "Full_commands": 10}

    updated = dict(payload)
    updated[PREFIX + "templates/task.md"] += b"\nFinite future-source proof instruction: retain exact check outputs.\n"
    updated[PREFIX + "installation.md"] += b"\nFinite future-source proof epoch, not distribution.\n"
    future_hashes = {p: sha(data) for p, data in updated.items()}
    future_id = sha(json.dumps(future_hashes, sort_keys=True).encode())
    for path, data in updated.items():
        write(EV / "package-snapshots" / future_id, path, data)
    report["future_source"] = {"snapshot_sha256": future_id, "files": future_hashes}
    receiver = fixture_root / "both"
    before = inventory(receiver)
    result = install(receiver, updated, list(ENTRIES), previous=payload)
    after = inventory(receiver)
    install(receiver, updated, list(ENTRIES), previous=updated)
    assert inventory(receiver) == after
    report["cases"]["changed-source-update"] = {"result": result,
        "changed": [p for p in after if before.get(p) != after[p]], "before": before, "after": after,
        "repeat_diff": []}

    custom = fixture_root / "custom-template"
    full(custom)
    install(custom, payload, ["codex"])
    write(custom, "AGENTS.md", b"Daily uses project-selected local form; preserve task/brief/messages split.\n")
    local_form = b"# Project-selected Daily form\nSource / Goal / Value / Boundaries / Context / Result / Check / Next\n"
    write(custom, PREFIX + "templates/task.md", local_form)
    for path, data in [("task.md", b"previous task meaning\n"), ("brief.md", b"previous brief\n"),
                       ("messages.md", b"material source words\n")]:
        write(custom, "daily/2026/20260101-120000_split/" + path, data)
    before = inventory(custom)
    result = install(custom, updated, ["codex"], previous=payload, preserve_form=True)
    after = inventory(custom)
    assert (custom / PREFIX / "templates/task.md").read_bytes() == local_form
    for path in before:
        if path.startswith("daily/"):
            assert before[path] == after[path]
    report["cases"]["selected-custom-template"] = {"root": custom.relative_to(EV).as_posix(),
        "result": result, "before": before, "after": after, "local_split_preserved": True}

    conflict = fixture_root / "foreign-skill"
    full(conflict)
    write(conflict, ENTRIES["codex"], b"# unrelated local Daily skill\n")
    before = inventory(conflict)
    result = install(conflict, updated, ["codex"], previous=payload)
    assert result["result"] == "REFUSED" and inventory(conflict) == before
    # Existence of the custom skill never opts in during ordinary Full update.
    report["cases"]["foreign-skill-refusal"] = {"root": conflict.relative_to(EV).as_posix(),
        "result": result, "before": before, "after": inventory(conflict), "implicit_opt_in": False}
    template_conflict = fixture_root / "ambiguous-template"
    full(template_conflict)
    write(template_conflict, PREFIX + "templates/task.md", b"unclassified private local form\n")
    before = inventory(template_conflict)
    result = install(template_conflict, updated, ["codex"], previous=payload)
    assert result["result"] == "REFUSED" and inventory(template_conflict) == before
    report["cases"]["ambiguous-template-refusal"] = {"result": result, "unchanged": True}
    report["self_receivers"] = {key: (ROOT / path).read_bytes() == payload[PREFIX + f"entries/{key}/SKILL.md"]
                                for key, path in ENTRIES.items()}
    assert all(report["self_receivers"].values())
    (EV / "package-proof.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"snapshot": snapshot_id, "cases": {k: v.get("result", v.get("install"))
                     for k, v in report["cases"].items()}, "self_receivers": report["self_receivers"]}))


if __name__ == "__main__":
    main()
