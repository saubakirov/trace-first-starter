"""Retain observed fixture checks and a pre-action revision checkpoint; not independent review."""
from pathlib import Path
from datetime import datetime
import hashlib
import json
import subprocess
import sys
import xml.etree.ElementTree as ET

EV = Path(__file__).resolve().parent


def sha(data):
    return hashlib.sha256(data).hexdigest()


def append(path, text):
    with path.open("a", encoding="utf-8") as stream:
        stream.write(text)


def main():
    checkpoints = json.loads((EV / "pre-action-checkpoints.json").read_text())
    before = json.loads((EV / "case-before.json").read_text())
    report = {"origin": "Actual Executor observation of source-labelled isolated cases, not native discovery or independent Review",
              "pre_action_commit": "b4a5c67736f109e637c453c64f60e11d0d7f18b0", "cases": [], "comparison": {}}
    for receiver in ("new-project", "local-split"):
        root = EV / "cases" / receiver
        run = subprocess.run([sys.executable, "run_login.py"], cwd=root / "app", capture_output=True, text=True, check=True)
        expected = "trimmed login: True\nunknown rejected: True\nregistration: {'email': 'New@Example.org', 'verified': False}\n"
        assert run.stdout == expected
        for protected in ("app/register.py", "design/pack1.svg"):
            key = f"cases/{receiver}/{protected}"
            assert before[key] == sha((root / protected).read_bytes())
        doc = (root / "docs/invitation-v1.md").read_text(encoding="utf-8")
        assert "15 October 2026 at 14:00" in doc and "Please confirm" in doc
        assert "venue" not in doc and "has not been sent" in doc
        tree = ET.parse(root / "design/pack2.svg").getroot()
        assert tree.attrib["viewBox"] == "0 0 240 240"
        fills = {x.attrib["fill"] for x in tree.iter() if "fill" in x.attrib}
        strokes = {x.attrib["stroke"] for x in tree.iter() if "stroke" in x.attrib}
        assert fills | strokes == {"#008080", "#263238"}
        assert len(list(tree.iter("{http://www.w3.org/2000/svg}path"))) == 4
        for cp in [x for x in checkpoints if x["receiver"] == receiver]:
            folder = EV / cp["folder"]
            slug = cp["slug"]
            product = {"login": "app/login.py", "letter": "docs/invitation-v1.md", "pack2": "design/pack2.svg"}[slug]
            check = {"login": run.stdout.strip(), "letter": "Complete Markdown document opened/read: correct initial date/time, confirmation request, no invented venue or sending claim.",
                     "pack2": "Actual SVG parsed and CairoSVG-rendered image visually inspected: teal cloud/rain silhouette, charcoal outline, no crop. Same source bytes in both contexts."}[slug]
            normalized = sha((root / product).read_bytes().replace(b"\r\n", b"\n"))
            append(folder / "task.md", "\n## Round 1 — completed local preparation\n"
                   f"Current result: [product](../../../{product}); LF-normalized SHA-256 `{normalized}`.\n"
                   f"Observed check: {check}\n"
                   "Protected registration and pack1 hashes match case-before.json. Prepared and checked only; "
                   "human acceptance/release/sending remain unobserved and reserved to saubakirov.\n"
                   "Next authority: PTW independent Reviewer reconstructs these records; actual human decides acceptance.\n")
            report["cases"].append({"receiver": receiver, "task_id": cp["task_id"], "product": product,
                                    "check": check, "product_lf_sha256": normalized,
                                    "protected_unchanged": True, "accepted": False,
                                    "released_or_sent": False})

        letter_cp = next(x for x in checkpoints if x["receiver"] == receiver and x["slug"] == "letter")
        folder = EV / letter_cp["folder"]
        now = datetime.now().astimezone().isoformat(timespec="seconds")
        exact = (root / "requests.md").read_text(encoding="utf-8").split("## Letter v2 — same deliverable\n", 1)[1].split("\n\n", 1)[0]
        revision = (f"\n## Round 2 — pre-action meaning revision, {now}\n"
                    f"Exact fixture source requests.md §Letter v2: {exact}\n"
                    "Same invitation/deliverable, same accepting authority and preparation-only boundary. "
                    "New Goal: invitation for 16 October 2026 at 10:00. Value: accurate rescheduling. "
                    "Read current meeting.md, existing invitation-v1.md and earlier task record; original request/meaning/result retained. "
                    "Oracle: new invitation date/time and unchanged v1 hash, no sending.\n")
        if receiver == "local-split":
            append(folder / "brief.md", "\n## v2 — same invitation rescheduled\n" + revision)
            append(folder / "messages.md", "\n## Fixture input 2, source requests.md §Letter v2\n> " + exact + "\n")
        else:
            append(folder / "task.md", revision)
        # The durable revision checkpoint is written before the next product is created.
        checkpoint = {"time": now, "receiver": receiver, "record": folder.relative_to(EV).as_posix(),
                      "request_source": "requests.md §Letter v2", "old_result_sha256": sha((root / "docs/invitation-v1.md").read_bytes()),
                      "next_result_exists": (root / "docs/invitation-v2.md").exists()}
        assert not checkpoint["next_result_exists"]
        (EV / f"revision-before-{receiver}.json").write_text(json.dumps(checkpoint, indent=2) + "\n", encoding="utf-8")
        report["comparison"][receiver] = {"initial_trace_files_per_task": 1 if receiver == "new-project" else 3,
            "initial_trace_writes_per_task": 1 if receiver == "new-project" else 3,
            "meaning_revision_trace_files_written": 1 if receiver == "new-project" else 2,
            "recovery_inputs": ["source", "Goal/Value", "Boundaries", "current product", "check", "next authority"],
            "independent_recovery": "owed to separate Reviewer", "time_or_token_advantage": "not measured"}
    report["field_split_source"] = {"repository_epoch": "13729f4ac3faa7fdae928295f1d81164cde08cc5",
        "inspected": "Inspected field local skill and daily/README.md, read-only; task/brief/messages contract only adapted neutrally",
        "scope": "No identity/content copied; no field-project write; current field rules take precedence in real adoption"}
    (EV / "case-results-round1.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"checks": len(report["cases"]), "same_deliverable_revisions": 2,
                      "revision_product_written": False, "protected_outputs": "unchanged"}))


if __name__ == "__main__":
    main()
