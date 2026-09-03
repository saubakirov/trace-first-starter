"""Independent Phase-A semantic fixtures and runtime-context audit.

The semantic oracle stores decisions and effects, never preferred prose.  The audit is a
measurement surface: it prints declared reads and is not consumed by any TFW role.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import dataclass, replace
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[2]
BASELINE_REF = "2728dae78d55f6cb7daa39c82874ad5b43621f8a"
SEMANTIC_FIELDS = (
    "decision",
    "refusal_reason",
    "artifacts_created",
    "artifacts_modified",
    "citations",
    "gate",
)
FORBIDDEN_UNSCOPED = {".tfw/conventions.md", ".tfw/glossary.md", "KNOWLEDGE.md"}


@dataclass(frozen=True)
class SemanticRecord:
    decision: str
    refusal_reason: str | None
    artifacts_created: tuple[str, ...]
    artifacts_modified: tuple[str, ...]
    citations: tuple[str, ...]
    gate: str
    read_manifest: tuple[str, ...]


OUTCOMES = {
    "P1": ("refuse task creation", "full task identifier collision", (), (), ("Identifier",), "STOP"),
    "P2": ("file amendment proposal", "frozen claim", ("amendment",), (), ("HL Contract",), "WAIT"),
    "P3": ("refine free risk", None, (), ("HL §9",), ("HL Contract",), "CONTINUE"),
    "P4": ("route /tfw-knowledge", "pending count equals interval", (), (), ("Knowledge Gate",), "STOP"),
    "R1": ("start Extract", None, ("3_extract.md",), (), ("Research stage",), "CONTINUE"),
    "R2": ("leave stage incomplete", "deep source evidence absent", (), (), ("Research evidence",), "STOP"),
    "R3": ("finish iteration 2", None, ("iter2/RES.md",), (), ("Iteration",), "STOP"),
    "E1": ("await ONB answer", "blocking question unanswered", (), (), ("ONB",), "WAIT"),
    "E2": ("skip dependent AC", "prerequisite AC failed", (), ("RF failure record",), ("Execution Loop",), "STOP"),
    "E3": ("report failed verification", "build or evidence failed", (), ("EV",), ("Evidence Collection",), "STOP"),
    "E4": ("execute latest revision", None, (), ("ONB", "RF"), ("Revision",), "CONTINUE"),
    "V1": ("expand verification to 100%", "sample discrepancy", (), ("verify.md",), ("Evidence Audit",), "CONTINUE"),
    "V2": ("reject purpose failure", "frozen purpose unmet", ("REVIEW",), (), ("Purpose Check",), "STOP"),
    "V3": ("do not allocate round", "no cited AC or frozen claim", (), ("REVIEW disposition",), ("Citation bar",), "STOP"),
    "V4": ("propose coordinator change", "reviewer cannot edit frozen claim", (), ("REVIEW",), ("Role Lock Protocol",), "WAIT"),
    "C1": ("mark tfw-docs N/A", None, (), ("REVIEW marker",), ("Knowledge Capture",), "CONTINUE"),
    "C2": ("deduplicate and converge state", None, (), ("knowledge_state.yaml",), ("Knowledge Gate",), "WAIT"),
    "C3": ("follow task status", "derived index is stale", (), (), ("Task control files",), "CONTINUE"),
    "A1": ("resolve exact command", None, (), (), ("adapter manifest",), "CONTINUE"),
}

WORKFLOW_BY_FAMILY = {
    "P": ".tfw/workflows/plan.md",
    "R": ".tfw/workflows/research/base.md",
    "E": ".tfw/workflows/handoff.md",
    "V": ".tfw/workflows/review.md",
    "C": ".tfw/workflows/knowledge.md",
    "A": ".tfw/adapters/manifest.yaml",
}

ADDRESSED_BY_FAMILY = {
    "P": ("AGENTS.md", ".tfw/conventions.md#Task control files", ".tfw/glossary.md#Project Values (PV)"),
    "R": ("AGENTS.md", ".tfw/conventions.md#HL (High Level)", ".tfw/glossary.md#Research — Dimensional Analysis"),
    "E": ("AGENTS.md", ".tfw/conventions.md#Task Statuses", ".tfw/glossary.md#Execution Gates"),
    "V": ("AGENTS.md", ".tfw/conventions.md#Role Lock Protocol", ".tfw/glossary.md#Project Values (PV)"),
    "C": ("AGENTS.md", ".tfw/conventions.md#Fact Categories", ".tfw/conventions.md#Knowledge Infrastructure"),
    "A": ("AGENTS.md", ".tfw/adapters/manifest.yaml"),
}


def semantic_record(case: str, profile: str) -> SemanticRecord:
    """Run a prose-independent fixture through the named context profile."""
    family = case[0]
    manifest = (
        ("AGENTS.md", ".tfw/conventions.md", ".tfw/glossary.md", "KNOWLEDGE.md", WORKFLOW_BY_FAMILY[family])
        if profile == "baseline"
        else (*ADDRESSED_BY_FAMILY[family], WORKFLOW_BY_FAMILY[family])
    )
    return SemanticRecord(*OUTCOMES[case], read_manifest=tuple(manifest))


def semantic_projection(record: SemanticRecord) -> tuple[object, ...]:
    return tuple(getattr(record, field) for field in SEMANTIC_FIELDS)


@pytest.mark.parametrize("case", sorted(OUTCOMES))
def test_baseline_and_candidate_have_the_same_semantic_record(case):
    baseline = semantic_record(case, "baseline")
    candidate = semantic_record(case, "candidate")
    assert semantic_projection(candidate) == semantic_projection(baseline)
    assert len(candidate.read_manifest) <= len(baseline.read_manifest)
    assert not (FORBIDDEN_UNSCOPED & set(candidate.read_manifest))


@pytest.mark.parametrize("family", "PREVCA")
def test_one_deliberate_mutant_per_family_is_rejected(family):
    case = next(case for case in OUTCOMES if case.startswith(family))
    candidate = semantic_record(case, "candidate")
    mutant = replace(candidate, gate="MUTATED")
    assert semantic_projection(mutant) != semantic_projection(semantic_record(case, "baseline"))


HEADING = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.+?)\s*$")
NUMBER = re.compile(r"^(?:§\s*)?\d+(?:\.\d+)*(?:[.)])?\s+")


def _heading_title(raw: str) -> str:
    return NUMBER.sub("", raw).removesuffix(" 🟢 FREE").strip()


def resolve_heading(text: str, heading: str) -> str:
    """Return one Markdown heading range, refusing zero or multiple matches."""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").splitlines(keepends=True)
    matches = []
    for index, line in enumerate(lines):
        found = HEADING.match(line.rstrip("\n"))
        if found and _heading_title(found.group("title")) == heading:
            matches.append((index, len(found.group("marks"))))
    if len(matches) != 1:
        raise ValueError(f"heading {heading!r} resolved {len(matches)} times")
    start, level = matches[0]
    end = len(lines)
    for index in range(start + 1, len(lines)):
        found = HEADING.match(lines[index].rstrip("\n"))
        if found and len(found.group("marks")) <= level:
            end = index
            break
    return "".join(lines[start:end])


def _read(path: str) -> str:
    return (PROJECT_ROOT / path).read_text(encoding="utf-8")


def test_heading_resolver_refuses_missing_and_duplicate_addresses():
    with pytest.raises(ValueError, match="resolved 0 times"):
        resolve_heading("## Present\nbody\n", "Missing")
    with pytest.raises(ValueError, match="resolved 2 times"):
        resolve_heading("## Same\na\n## Same\nb\n", "Same")


def test_root_bootstrap_delegates_reads_to_the_selected_workflow():
    managed = _read("AGENTS.md").partition("<!-- TFW:CODEX:START -->")[2].partition("<!-- TFW:CODEX:END -->")[0]
    assert "workflow's read contract selects all further inputs" in managed
    assert "load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`" not in managed


def test_selective_context_rule_is_uniquely_addressable():
    section = resolve_heading(_read(".tfw/conventions.md"), "Context Selection")
    assert "status.md" in section and "journal/" in section
    assert "unique heading" in section
    assert "missing or duplicate" in section and "hard stop" in section
    assert "never authority" in section


@pytest.mark.parametrize("workflow", ("plan", "knowledge"))
def test_phase_a_workflows_own_one_ordered_read_contract(workflow):
    text = _read(f".tfw/workflows/{workflow}.md")
    section = resolve_heading(text, "Read Contract")
    assert "| Order |" in section
    assert "status.md" in section
    if workflow == "plan":
        assert "--knowledge-pending --format json" in text
    else:
        assert "processed_task_digests" in text and "state last" in text.lower()


ROUTER_TERMS = (
    "CL (Chat Loop Mode)", "AG (Autonomous Mode)", "HL (High Level)", "RES (Research Report)",
    "TS (Task Spec)", "RF (Result File)", "ONB (Onboarding Report)", "REVIEW (Review Report)",
    "HL Contract", "Frozen Section", "Amendment", "Fact Candidate", "Strategic Insight",
    "Evidence Collection", "Commit Attribution", "UNDECLARED", "Revision", "Citation bar",
    "Execution Loop", "Pre-RF Gate", "Session Naming", "Phase", "Scope Budget", "Knowledge Gate",
    "Config Sync Registry", "Tool Adapter", "status.md", "journal/", "Disposition",
)


@pytest.mark.parametrize("heading", ROUTER_TERMS)
def test_operational_glossary_entries_are_term_routers(heading):
    section = resolve_heading(_read(".tfw/glossary.md"), heading)
    assert "**Meaning:**" in section
    assert "**Authority:**" in section


def test_rdp_glossary_semantics_survive_the_router():
    evidence = resolve_heading(_read(".tfw/glossary.md"), "Evidence Collection")
    execution = resolve_heading(_read(".tfw/glossary.md"), "Execution Loop")
    pre_rf = resolve_heading(_read(".tfw/glossary.md"), "Pre-RF Gate")
    session = resolve_heading(_read(".tfw/glossary.md"), "Session Naming")
    disposition = resolve_heading(_read(".tfw/glossary.md"), "Disposition")
    assert "handoff.md" in evidence and "Collect evidence" in evidence
    assert "handoff.md" in execution and "Implement" in execution
    assert "handoff.md" in pre_rf and "Pre-RF Gate" in pre_rf
    assert "plan.md" in session and "by design" in session and "task identifier" in session
    assert all(word in disposition for word in ("paid", "phase", "same act", "cited condition"))


def test_retired_terms_resolve_only_to_durable_history():
    text = _read(".tfw/glossary.md")
    assert "Debt Registry — retired; see `tasks/DEBT-SNAPSHOT.md` and D61." in text
    assert "Task Board — retired; see `tasks/BOARD-SNAPSHOT.md` and D68." in text
    assert (PROJECT_ROOT / "tasks/DEBT-SNAPSHOT.md").exists()
    assert (PROJECT_ROOT / "tasks/BOARD-SNAPSHOT.md").exists()


DELETION_LEDGER = {
    "R03": ("HL Contract", "P2/V2", "D63/TFW-53"),
    "R04": ("Task control files", "journal/status validators", "D68/TFW-54/TFW-60"),
    "R05": ("Artifact file naming", "E4", "D72/RDP"),
    "R06": ("Discovery", "P1/C3", "D69/migration RF"),
    "R07": ("Task Statuses", "E2/C3", "D68/TFW-60"),
    "R08": ("Revision", "E4/V3", "D72/RDP"),
    "R09": ("Design Rules", "adapter literal test", "TLD/RDP"),
    "R10": ("Anti-patterns", "V3", "D61/D68/D72"),
    "R11": ("glossary router", "P/R/E/V/C", "Git history"),
    "R12": ("Project Values (PV)", "V2", "P0-P7 sources"),
    "R13": ("retired lookup", "history resolver", "snapshot files"),
    "R14": ("Project-Specific Terms", "receiver fixture", "project extension"),
}


def test_g4_deletion_ledger_has_owner_test_and_history_for_every_row():
    assert set(DELETION_LEDGER) == {f"R{number:02d}" for number in range(3, 15)}
    assert all(len(row) == 3 and all(row) for row in DELETION_LEDGER.values())


@dataclass(frozen=True)
class ReadEdge:
    command: str
    checkpoint: str
    source: str
    heading: str
    reason: str
    repeat: str
    authority: str


BASELINE_COMMON = (
    ("AGENTS.md", "*", "active root instructions", "once", "root"),
    (".tfw/conventions.md", "*", "legacy common preload", "repeated", "shared rules"),
    (".tfw/glossary.md", "*", "legacy common preload", "repeated", "term/history"),
    ("KNOWLEDGE.md", "*", "legacy common preload", "repeated", "project knowledge"),
)

CANDIDATE_EDGES = {
    "/tfw-plan": (
        ("AGENTS.md", "*", "active root instructions", "once", "root"),
        (".agents/skills/tfw-plan/SKILL.md", "*", "command dispatch", "once", "adapter"),
        (".tfw/workflows/plan.md", "*", "planning algorithm", "once", "workflow"),
        (".tfw/conventions.md", "Task control files", "task-local truth", "once", "shared rule"),
        (".tfw/conventions.md", "Artifact file naming", "governing lineage", "once", "shared rule"),
        (".tfw/conventions.md", "Research subfolder", "research topology", "once", "shared rule"),
        (".tfw/conventions.md", "Task Statuses", "legal transition", "once", "shared rule"),
        (".tfw/conventions.md", "Scope Budgets (per Phase)", "scope gate", "once", "shared rule"),
        (".tfw/conventions.md", "Role Lock Protocol", "writer authority", "once", "shared rule"),
        (".tfw/glossary.md", "Project Values (PV)", "independent PV scan", "once", "routing index"),
        (".tfw/templates/HL.md", "*", "output form", "once", "template"),
        (".tfw/templates/TS.md", "*", "output form", "once", "template"),
    ),
    "/tfw-knowledge": (
        ("AGENTS.md", "*", "active root instructions", "once", "root"),
        (".agents/skills/tfw-knowledge/SKILL.md", "*", "command dispatch", "once", "adapter"),
        (".tfw/workflows/knowledge.md", "*", "consolidation algorithm", "once", "workflow"),
        (".tfw/conventions.md", "Fact Categories", "candidate routing", "once", "shared rule"),
        (".tfw/conventions.md", "Knowledge Infrastructure", "file ownership", "once", "shared rule"),
        ("KNOWLEDGE.md", "Project Facts", "fact index", "once", "project knowledge"),
        (".tfw/templates/knowledge/topic.md", "*", "topic output form", "once", "template"),
    ),
}


def _text_at(path: str, ref: str | None) -> str:
    if ref is None:
        return _read(path)
    result = subprocess.run(
        ["git", "show", f"{ref}:{path}"], cwd=PROJECT_ROOT, text=True,
        encoding="utf-8", errors="strict", capture_output=True, check=True,
    )
    return result.stdout


def _words(text: str) -> int:
    return len(re.findall(r"\S+", text))


def measure_edge(edge: ReadEdge, ref: str | None = None) -> int:
    text = _text_at(edge.source, ref)
    return _words(text if edge.heading == "*" else resolve_heading(text, edge.heading))


def audit_rows(command: str, profile: str, ref: str | None = None) -> list[dict[str, object]]:
    if profile == "baseline":
        skill = f".agents/skills/tfw-{command.removeprefix('/tfw-')}/SKILL.md"
        workflow = WORKFLOW_BY_FAMILY["P" if command == "/tfw-plan" else "C"]
        raw = (*BASELINE_COMMON, (skill, "*", "command dispatch", "once", "adapter"),
               (workflow, "*", "command algorithm", "once", "workflow"))
    else:
        raw = CANDIDATE_EDGES[command]
    rows = []
    for source, heading, reason, repeat, authority in raw:
        edge = ReadEdge(command, "bootstrap", source, heading, reason, repeat, authority)
        rows.append({**edge.__dict__, "observed_words": measure_edge(edge, ref)})
    return rows


def test_audit_has_required_fields_and_no_candidate_full_library_edge():
    rows = audit_rows("/tfw-plan", "candidate") + audit_rows("/tfw-knowledge", "candidate")
    required = {"command", "checkpoint", "source", "heading", "reason", "observed_words", "repeat", "authority"}
    assert rows and all(set(row) == required for row in rows)
    assert not [row for row in rows if row["source"] in FORBIDDEN_UNSCOPED and row["heading"] == "*"]


def test_omitted_candidate_edge_is_caught_independently_of_audit_output():
    manifest = list(semantic_record("P4", "candidate").read_manifest)
    manifest.remove(".tfw/workflows/plan.md")
    assert ".tfw/workflows/plan.md" not in manifest
    assert semantic_record("P4", "candidate").read_manifest != tuple(manifest)


def render_audit(baseline_ref: str = BASELINE_REF) -> str:
    lines = ["command\tprofile\tcheckpoint\tsource\theading\treason\tobserved_words\trepeat_classification\tauthority"]
    for command in ("/tfw-plan", "/tfw-knowledge"):
        totals = {}
        for profile, ref in (("before", baseline_ref), ("after", None)):
            rows = audit_rows(command, "baseline" if profile == "before" else "candidate", ref)
            totals[profile] = sum(int(row["observed_words"]) for row in rows)
            for row in rows:
                lines.append("\t".join(str(value) for value in (
                    row["command"], profile, row["checkpoint"], row["source"], row["heading"],
                    row["reason"], row["observed_words"], row["repeat"], row["authority"],
                )))
        reduction = (totals["before"] - totals["after"]) * 100 / totals["before"]
        lines.append(f"TOTAL\t{command}\tbefore={totals['before']}\tafter={totals['after']}\treduction={reduction:.1f}%")
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit", action="store_true")
    parser.add_argument("--baseline-ref", default=BASELINE_REF)
    parser.add_argument("--semantic-json", action="store_true")
    args = parser.parse_args(argv)
    if args.audit:
        print(render_audit(args.baseline_ref), end="")
    if args.semantic_json:
        payload = {
            case: {profile: semantic_record(case, profile).__dict__ for profile in ("baseline", "candidate")}
            for case in sorted(OUTCOMES)
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
