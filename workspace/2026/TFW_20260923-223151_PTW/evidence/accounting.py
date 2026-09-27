"""Replay exact approved TS + prospective SR1 VALUE accounting; never define new authority."""
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
EV = Path(__file__).resolve().parent
BASELINE = "0c32c50e8d7c0dd2b7c509e5cc0605e64c76d669"
PATHS = [
    (".tfw/extensions/daily-task/SKILL.md", "Sole portable semantic source"),
    (".tfw/extensions/daily-task/templates/task.md", "Daily-only selected Trace form"),
    (".tfw/extensions/daily-task/installation.md", "Pinned optional source/receiver and preservation contract"),
    (".tfw/extensions/daily-task/entries/codex/SKILL.md", "Thin Codex entry source"),
    (".tfw/extensions/daily-task/entries/claude-code/SKILL.md", "Thin Claude entry source"),
    (".agents/skills/tfw-daily-task/SKILL.md", "Selected self Codex receiver"),
    (".claude/skills/tfw-daily-task/SKILL.md", "Selected self Claude receiver"),
    (".tfw/conventions.md", "Formal Full / local Daily scope and navigation"),
    (".tfw/glossary.md", "Existing Task/Trace meaning for local Daily"),
    (".tfw/adapters/README.md", "Fixed Full commands versus optional entries"),
    (".tfw/workflows/init.md", "Conditional opt-in installation/preservation"),
    (".tfw/workflows/update.md", "Pinned package update and local receiver preservation"),
    (".tfw/workflows/config.md", "Exact Full and separately selected optional parity"),
    (".claude/commands/tfw-init.md", "SR1 necessary canonical init byte copy"),
    (".claude/commands/tfw-update.md", "SR1 necessary canonical update byte copy"),
    (".claude/commands/tfw-config.md", "SR1 necessary canonical config byte copy"),
]


def main():
    candidate = sys.argv[1]
    assert subprocess.check_output(["git", "rev-parse", candidate + "^{commit}"], cwd=ROOT).decode().strip() == candidate
    command1 = ["git", "diff", "--name-status", "--find-renames=50%", "-z", BASELINE, candidate, "--"] + [p for p, _ in PATHS]
    command2 = ["git", "diff", "--numstat", "--find-renames=50%", "-z", BASELINE, candidate, "--"] + [p for p, _ in PATHS]
    names = subprocess.check_output(command1, cwd=ROOT)
    nums = subprocess.check_output(command2, cwd=ROOT)
    tokens = names.decode().split("\0")[:-1]
    assert len(tokens) % 2 == 0
    actions = dict(zip(tokens[1::2], tokens[::2]))
    assert set(actions) == {p for p, _ in PATHS}
    numstat = {}
    for row in nums.decode().split("\0"):
        if row:
            adds, deletes, path = row.split("\t", 2)
            assert adds.isdigit() and deletes.isdigit(), "Binary/rename handling needs explicit per-file N/A, not guessed numbers"
            numstat[path] = (int(adds), int(deletes))
    members = [{"path": p, "action": {"A": "CREATE", "M": "MODIFY"}[actions[p]], "class": "VALUE",
                "reason": reason, "additions": numstat[p][0], "deletions": numstat[p][1]} for p, reason in PATHS]
    additions = sum(x["additions"] for x in members)
    deletions = sum(x["deletions"] for x in members)
    assert len(members) < 26 and additions + deletions < 3400
    (EV / "value-name-status.z").write_bytes(names)
    (EV / "value-numstat.z").write_bytes(nums)
    report = {"TS_approval": "84e1299afa5479826a9a756bf044dd137ad5f8a9",
        "approved_TS_source": "95da8458b8cbd4d2796b9f2cddab598d4cd4007a",
        "approved_TS_blob": "d0695859ee4d30a60d83bd99286bd3fd4f99df93",
        "prospective_SR1": "b2c9cf63bab878f83e071fccaec1c2de9677544f",
        "Baseline": BASELINE, "Candidate": candidate, "members": members,
        "logical_VALUE_files": len(members), "additions": additions, "deletions": deletions,
        "touched_text_LOC": additions + deletions, "binary_non_text": "N/A — no binary VALUE selector member",
        "immutable_owner_denominator": {"files": 13, "touched_LOC": 1700},
        "approval_timing": "Owner TS/denominator approved before activation; SR1 before all product writes",
        "triggers": {"configured": [50, 5000], "owner_multiplier_thresholds": [26, 3400], "fired": False},
        "deviations": "Only three prospective necessary VALUE copies admitted by SR1; no other selector deviation",
        "shared_provenance": "Whole conventions delta includes inherited Coordinator +21/-4 refinement; no sole-authorship or baseline-shift claim",
        "exact_NUL_safe_commands": [command1, command2],
        "unchanged_PowerShell_method": ["git diff --name-status --find-renames=50% -z $ptwBaseline $ptwCandidate -- $ptwValuePaths",
                                        "git diff --numstat --find-renames=50% -z $ptwBaseline $ptwCandidate -- $ptwValuePaths"]}
    (EV / "accounting.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ["Baseline", "Candidate", "logical_VALUE_files", "additions", "deletions", "touched_text_LOC"]}))


if __name__ == "__main__":
    main()
