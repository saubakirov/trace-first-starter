"""Retain actual inspected-input checkpoints before any material product write."""
from pathlib import Path
from datetime import datetime
import hashlib
import json

EV = Path(__file__).resolve().parent
WORKER = "codex:thread:local:01a0e449-55b7-7621-8f62-25a202c2b4a0"
SPECS = {
    "login": ("Repair", "Restore trimmed case-insensitive login", "Predictable access without registration change",
              "app/login.py only; preserve app/register.py; release belongs to owner",
              ["docs/login.md", "app/login.py", "app/register.py", "daily/2026/20260101-120000_login/task.md"],
              "Prior no-trim premise is stale; current docs/login.md governs.",
              "Actual run_login.py must print trimmed login True, unknown rejected True, exact registration input preserved."),
    "letter": ("Letter v1", "Prepare a factual meeting invitation", "Recipient can confirm scheduling",
              "docs/invitation*.md only; no invented venue/attendance; sending belongs to owner",
              ["docs/meeting.md"], "Bounded invitation lookup in daily/ returned no match.",
              "Read complete document: initial 15 October 2026 14:00, request confirmation, no unprovided facts."),
    "pack2": ("Design pack 2 — independent outcome", "Add the rain motif as pack 2", "Continue the recognisable series",
              "design/pack2.svg only; preserve pack1.svg; publication belongs to owner",
              ["docs/brand.md", "design/pack1.svg", "daily/2026/20260102-120000_pack1/task.md"],
              "Prior blue suggestion is stale; current teal/charcoal rules govern; useful exact predecessor link.",
              "Open real SVG; 240×240 teal/charcoal rain motif; pack1 hash unchanged."),
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    events = []
    for name in ("new-project", "local-split"):
        root = EV / "cases" / name
        assert not (root / "docs/invitation.md").exists()
        assert not (root / "design/pack2.svg").exists()
        assert (root / "app/login.py").read_text() == 'def login(email):\n    return email.lower() == "reader@example.org"\n'
        requests = (root / "requests.md").read_text(encoding="utf-8")
        for slug, (heading, goal, value, boundary, selected, lookup, oracle) in SPECS.items():
            now = datetime.now().astimezone()
            task_id = now.strftime("%Y%m%d-%H%M%S") + "_" + slug
            folder = root / "daily" / now.strftime("%Y") / task_id
            assert not folder.exists(), "A current ID collision must preserve the occupied record"
            folder.mkdir(parents=True)
            excerpt = requests.split("## " + heading + "\n", 1)[1].split("\n\n", 1)[0]
            inputs = ["AGENTS.md", "README.md", "requests.md", ".agents/skills/tfw-daily-task/SKILL.md",
                      ".tfw/extensions/daily-task/SKILL.md", ".tfw/extensions/daily-task/templates/task.md"] + selected
            hashes = {p: sha((root / p).read_bytes()) for p in inputs}
            protected = {p: sha((root / p).read_bytes()) for p in ["app/register.py", "design/pack1.svg"]}
            pre = (f"## Context before action — {now.isoformat(timespec='seconds')}\n"
                   "Actual Executor inspected the listed receiving rules, purpose, current objects and bounded prior-work matches "
                   "in the preceding tool read, then retained this checkpoint before product edits.\n"
                   f"North Star fit: {value}; factual accuracy, preservation and human acceptance remain governing.\n"
                   f"Prior-work disposition: {lookup}\nCompletion oracle: {oracle}\n"
                   "No formal ownership in these three product paths. Missing profile disclosed; actual fixture authorization "
                   "is approved PTW TS, not a fictional human message. No second approval requested.\n"
                   "Title control for these filesystem-only receiving records is unavailable; parent Executor title remains EXEC · PTW.\n"
                   + "\n".join(f"- Read `{p}` SHA-256 `{h}`" for p, h in hashes.items()) + "\n")
            source = ("## Source and attribution\n"
                      "Actual accepting/accountable human: saubakirov under approved PTW TS; acceptance not observed. "
                      f"Worker: {WORKER}. Scenario input is Executor-authored fixture requests.md, not a quoted field message.\n"
                      f"Selected exact fixture excerpt (requests.md §{heading}):\n> {excerpt}\n")
            brief = f"## Goal, Value and Boundaries\nGoal: {goal}.\nValue: {value}.\nBoundaries: {boundary}.\n"
            pending = "## Result, decisions and check\nProduct execution not yet started.\n\n## Next or close\nExecutor performs the bounded preparation/check; human acceptance remains open.\n"
            if name == "new-project":
                (folder / "task.md").write_text(f"# Daily Task — {task_id}\n\n" + source + brief + pre + pending, encoding="utf-8")
                record_paths = ["task.md"]
            else:
                (folder / "messages.md").write_text(source, encoding="utf-8")
                (folder / "brief.md").write_text("# Brief history\n## v1 — initial fixture request\n" + brief + pre, encoding="utf-8")
                (folder / "task.md").write_text(f"# Daily Task — {task_id}\nSource: [messages](messages.md). "
                    "Goal/Value/Boundaries/pre-action: [brief v1](brief.md).\n" + pending, encoding="utf-8")
                record_paths = ["task.md", "brief.md", "messages.md"]
            if slug in ("login", "pack2"):
                related = ("20260101-120000_login" if slug == "login" else "20260102-120000_pack1")
                with (folder / "task.md").open("a", encoding="utf-8") as stream:
                    stream.write(f"\nRelated inspected fixture history: [prior task](../{related}/task.md), scope/currentness disposition above.\n")
            events.append({"receiver": name, "task_id": task_id, "slug": slug,
                           "time": now.isoformat(timespec="seconds"), "phase": "pre-action",
                           "folder": folder.relative_to(EV).as_posix(), "input_hashes": hashes,
                           "protected_hashes": protected, "oracle": oracle,
                           "record_writes": record_paths,
                           "checkpoint_hashes": {p: sha((folder / p).read_bytes()) for p in record_paths}})
    output = EV / "pre-action-checkpoints.json"
    assert not output.exists()
    output.write_text(json.dumps(events, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"checkpoints": len(events), "product_execution": "not started", "tasks":
                     [{"receiver": x["receiver"], "id": x["task_id"]} for x in events]}))


if __name__ == "__main__":
    main()
