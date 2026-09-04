"""Source-derived Phase-A semantic fixtures and runtime-context audit."""
from __future__ import annotations
import argparse, fnmatch, json, re, subprocess
from dataclasses import dataclass, field
from pathlib import Path
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
BASELINE_REF = "2728dae78d55f6cb7daa39c82874ad5b43621f8a"
SEMANTIC_FIELDS = ("decision", "refusal_reason", "artifacts_created", "artifacts_modified", "citations", "gate")
FORBIDDEN_UNSCOPED = {".tfw/conventions.md", ".tfw/glossary.md", "KNOWLEDGE.md"}

@dataclass(frozen=True)
class SemanticRecord:
    decision: str; refusal_reason: str | None; artifacts_created: tuple[str, ...]
    artifacts_modified: tuple[str, ...]; citations: tuple[str, ...]; gate: str
    read_manifest: tuple[str, ...]; source_clauses: tuple[tuple[str, str, str, str], ...]

class SourceContractError(RuntimeError):
    pass
@dataclass(frozen=True)
class SourceTree:
    root: Path; ref: str | None = None; overlays: dict[str, str] = field(default_factory=dict)
    @classmethod
    def from_path(cls, root: Path) -> "SourceTree":
        root = Path(root).resolve()
        if not root.is_dir(): raise FileNotFoundError(f"source root does not exist: {root}")
        return cls(root)
    @classmethod
    def from_git(cls, root: Path, ref: str) -> "SourceTree":
        tree = cls.from_path(root)
        result = subprocess.run(["git", "cat-file", "-e", f"{ref}^{{commit}}"],
                                cwd=tree.root, capture_output=True)
        if result.returncode: raise SourceContractError(f"source ref does not resolve: {ref}")
        return cls(tree.root, ref=ref)
    def read(self, path: str) -> str:
        path = path.replace("\\", "/")
        if path in self.overlays: return self.overlays[path]
        if self.ref is None:
            target = self.root / path
            if not target.is_file(): raise SourceContractError(f"source file does not resolve: {path}")
            return target.read_text(encoding="utf-8")
        result = subprocess.run(["git", "show", f"{self.ref}:{path}"], cwd=self.root,
                                text=True, encoding="utf-8", capture_output=True)
        if result.returncode: raise SourceContractError(f"source file does not resolve at {self.ref}: {path}")
        return result.stdout
    def with_text(self, path: str, text: str) -> "SourceTree":
        return SourceTree(self.root, self.ref,
                          {**self.overlays, path.replace("\\", "/"): text})
    def files(self, pattern: str) -> tuple[str, ...]:
        if self.ref is None:
            return tuple(sorted(p.relative_to(self.root).as_posix()
                                for p in self.root.glob(pattern) if p.is_file()))
        output = subprocess.run(["git", "ls-tree", "-r", "--name-only", self.ref], cwd=self.root,
                                text=True, encoding="utf-8", capture_output=True, check=True).stdout
        return tuple(sorted(p for p in output.splitlines() if fnmatch.fnmatch(p, pattern)))
@dataclass(frozen=True)
class Probe:
    path: str; needle: str; heading: str = "*"
@dataclass(frozen=True)
class Scenario:
    baseline: tuple[Probe, ...]; candidate: tuple[Probe, ...]

EXPECTED_RECORDS = {
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
def _scenario(path: str, baseline: str, candidate: str | None = None, heading: str = "*") -> Scenario:
    return Scenario((Probe(path, baseline, heading),), (Probe(path, candidate or baseline, heading),))
SCENARIOS = {
    "P1": _scenario(".tfw/conventions.md", "If the full identifier already exists at creation, creation refuses", heading="Identifier"),
    "P2": _scenario(".tfw/conventions.md", "The only channel is §12 Amendment Log", heading="HL Contract"),
    "P3": _scenario(".tfw/conventions.md", "Free sections stay free", heading="HL Contract"),
    "P4": _scenario(".tfw/workflows/plan.md", "current_seq - last_consolidation_seq", "pending_task_ids", "Step 2: Knowledge Gate"),
    "R1": _scenario(".tfw/workflows/research/base.md", "Stage Checkpoint"),
    "R2": _scenario(".tfw/workflows/research/base.md", "MUST: external research every stage"),
    "R3": _scenario(".tfw/workflows/research/base.md", "STOP after writing final RES"),
    "E1": _scenario(".tfw/workflows/handoff.md", "all blocking questions resolved"),
    "E2": _scenario(".tfw/workflows/handoff.md", "verify the prerequisite AC gate passes"),
    "E3": _scenario(".tfw/workflows/handoff.md", "If build fails"),
    "E4": _scenario(".tfw/workflows/handoff.md", "highest-numbered revision"),
    "V1": _scenario(".tfw/workflows/review.md", "On any discrepancy"),
    "V2": _scenario(".tfw/workflows/review.md", "Purpose Check"),
    "V3": _scenario(".tfw/workflows/review.md", "The citation bar."),
    "V4": _scenario(".tfw/workflows/review.md", "ROLE LOCK: REVIEWER"),
    "C1": _scenario(".tfw/workflows/review.md", "Mark both in REVIEW §6"),
    "C2": _scenario(".tfw/workflows/knowledge.md", "Deduplicate"),
    "C3": _scenario(".tfw/conventions.md", "re-reads that task", heading="Discovery"),
    "A1": _scenario("AGENTS.md", "| `/tfw-plan` | `.tfw/workflows/plan.md` |", heading="Trace-First Workflow Commands"),
}

def _variants(clause: str, value: object, *alternatives: tuple[str, object]):
    return ((clause, value), *alternatives)

DERIVATIONS = {
    "P1": {
        "decision": _variants("creation refuses", "refuse task creation"),
        "refusal_reason": _variants("full identifier already exists at creation", "full task identifier collision"),
        "artifacts_created": _variants("asks for a different", ()),
        "artifacts_modified": _variants("never recomputes the timestamp", ()),
        "citations": _variants("owner-approved abbreviation", ("Identifier",)),
        "gate": _variants("creation refuses", "STOP"),
    },
    "P2": {
        "decision": _variants("only channel is §12 Amendment Log", "file amendment proposal"),
        "refusal_reason": _variants("A frozen section may not be edited", "frozen claim"),
        "artifacts_created": _variants("§12 Amendment Log", ("amendment",)),
        "artifacts_modified": _variants("may not be edited", ()),
        "citations": _variants("contract state is artifact state", ("HL Contract",)),
        "gate": _variants("wait for the owner's verdict", "WAIT"),
    },
    "P3": {
        "decision": _variants("Free sections stay free", "refine free risk"),
        "refusal_reason": _variants("with no proposal and no verdict", None),
        "artifacts_created": _variants("with no proposal and no verdict", ()),
        "artifacts_modified": _variants("Risk registers", ("HL §9",)),
        "citations": _variants("Free sections stay free", ("HL Contract",)),
        "gate": _variants("update §2, §7.2, §8, §9, §10 and §11 directly", "CONTINUE"),
    },
    "P4": {
        "decision": _variants("Run `/tfw-knowledge` before proceeding", "route /tfw-knowledge",
                              ("route to `/tfw-knowledge`", "route /tfw-knowledge")),
        "refusal_reason": _variants("IF `>= interval` AND gate_mode = `hard`", "pending count equals interval",
                                    ("when `delta >= interval`", "pending count equals interval")),
        "artifacts_created": _variants("Knowledge consolidation overdue", ()),
        "artifacts_modified": _variants("Knowledge consolidation overdue", ()),
        "citations": _variants("Knowledge consolidation overdue", ("Knowledge Gate",)),
        "gate": _variants("→ **HARD STOP**", "STOP",
                          ("when `delta >= interval`, **STOP**", "STOP")),
    },
    "R1": {
        "decision": _variants("Gather → Extract → Challenge", "start Extract"),
        "refusal_reason": _variants("ALL met → STAGE CHECKPOINT", None),
        "artifacts_created": _variants("`3_extract.md`", ("3_extract.md",)),
        "artifacts_modified": _variants("before next stage", ()),
        "citations": _variants("Run Stages", ("Research stage",)),
        "gate": _variants("checkpoint before advancing", "CONTINUE"),
    },
    "R2": {
        "decision": _variants("NOT met + no loops → report, exit", "leave stage incomplete"),
        "refusal_reason": _variants("NOT met + no loops → report, exit", "deep source evidence absent"),
        "artifacts_created": _variants("NEVER: skip to conclusions without data", ()),
        "artifacts_modified": _variants("no loops → report, exit", ()),
        "citations": _variants("External source used?", ("Research evidence",)),
        "gate": _variants("no loops → report, exit", "STOP"),
    },
    "R3": {
        "decision": _variants("STOP after writing final RES", "finish iteration 2"),
        "refusal_reason": _variants("never proceed to HL/TS", None),
        "artifacts_created": _variants("research/iterN/RES.md", ("iter2/RES.md",)),
        "artifacts_modified": _variants("never proceed to HL/TS", ()),
        "citations": _variants("Research iteration {N} complete", ("Iteration",)),
        "gate": _variants("STOP after writing final RES", "STOP"),
    },
    "E1": {
        "decision": _variants("Wait for user approval", "await ONB answer"),
        "refusal_reason": _variants("blocking questions resolved", "blocking question unanswered"),
        "artifacts_created": _variants("do NOT proceed until all blocking questions resolved", ()),
        "artifacts_modified": _variants("do NOT proceed until all blocking questions resolved", ()),
        "citations": _variants("Commit ONB", ("ONB",)),
        "gate": _variants("Wait for user approval", "WAIT"),
    },
    "E2": {
        "decision": _variants("before starting the dependent AC", "skip dependent AC"),
        "refusal_reason": _variants("prerequisite AC gate passes", "prerequisite AC failed"),
        "artifacts_created": _variants("Independent ACs", ()),
        "artifacts_modified": _variants("prerequisite AC gate passes", ("RF failure record",)),
        "citations": _variants("Execution Loops", ("Execution Loop",)),
        "gate": _variants("before starting the dependent AC", "STOP"),
    },
    "E3": {
        "decision": _variants("Never write RF with failing build", "report failed verification",
                              ("Write RF even with failing build", "publish failed verification")),
        "refusal_reason": _variants("Never write RF with failing build", "build or evidence failed",
                                    ("Write RF even with failing build", "build failure ignored")),
        "artifacts_created": _variants("fix BEFORE writing RF", ()),
        "artifacts_modified": _variants("populate the EV file", ("EV",)),
        "citations": _variants("Collect evidence", ("Evidence Collection",)),
        "gate": _variants("Never write RF with failing build", "STOP",
                          ("Write RF even with failing build", "CONTINUE")),
    },
    "E4": {
        "decision": _variants("highest-numbered revision", "execute latest revision"),
        "refusal_reason": _variants("What is not re-done", None),
        "artifacts_created": _variants("TS and the REVIEW take **siblings**", ()),
        "artifacts_modified": _variants("RF and the ONB are **appended to**", ("ONB", "RF")),
        "citations": _variants("Returning after a 🔄 REVISE", ("Revision",)),
        "gate": _variants("which governs and which carries the round's order", "CONTINUE"),
    },
    "V1": {
        "decision": _variants("On any discrepancy → escalate to 100%", "expand verification to 100%"),
        "refusal_reason": _variants("On any discrepancy", "sample discrepancy"),
        "artifacts_created": _variants("Min verify ratio", ()),
        "artifacts_modified": _variants("verify.md findings", ("verify.md",)),
        "citations": _variants("On any discrepancy", ("Evidence Audit",)),
        "gate": _variants("go back and do it", "CONTINUE"),
    },
    "V2": {
        "decision": _variants("not fit for purpose", "reject purpose failure"),
        "refusal_reason": _variants("Purpose Check's reference set", "frozen purpose unmet"),
        "artifacts_created": _variants("Write `REVIEW__*.md`", ("REVIEW",)),
        "artifacts_modified": _variants("never the TS", ()),
        "citations": _variants("Purpose Check (row 2a)", ("Purpose Check",)),
        "gate": _variants("route to the **owner**, never the executor", "STOP"),
    },
    "V3": {
        "decision": _variants("Cite nothing and the verdict is", "do not allocate round"),
        "refusal_reason": _variants("frozen HL claim", "no cited AC or frozen claim"),
        "artifacts_created": _variants("the remainder disposed", ()),
        "artifacts_modified": _variants("disposed of in §5", ("REVIEW disposition",)),
        "citations": _variants("The citation bar", ("Citation bar",)),
        "gate": _variants("Neither cite nor approve", "STOP"),
    },
    "V4": {
        "decision": _variants("reviewer marks and proposes", "propose coordinator change"),
        "refusal_reason": _variants("Forbidden actions: writing code, writing ONB, writing RF, modifying HL/TS", "reviewer cannot edit frozen claim"),
        "artifacts_created": _variants("Permitted artifacts: review stage files", ()),
        "artifacts_modified": _variants("REVIEW file", ("REVIEW",)),
        "citations": _variants("ROLE LOCK: REVIEWER", ("Role Lock Protocol",)),
        "gate": _variants("returns to the task's `owner`", "WAIT"),
    },
    "C1": {
        "decision": _variants("Mark both in REVIEW §6", "mark tfw-docs N/A"),
        "refusal_reason": _variants("For trivial tasks: reviewer pre-marks both as N/A", None),
        "artifacts_created": _variants("After ✅ APPROVE verdict", ()),
        "artifacts_modified": _variants("tfw-docs: Applied/N/A", ("REVIEW marker",)),
        "citations": _variants("Knowledge Capture (KNW)", ("Knowledge Capture",)),
        "gate": _variants("When both markers are set", "CONTINUE"),
    },
    "C2": {
        "decision": _variants("**Deduplicate**", "deduplicate and converge state"),
        "refusal_reason": _variants("DO NOT auto-resolve contradictions", None),
        "artifacts_created": _variants("already exists in topic files → skip", ()),
        "artifacts_modified": _variants("Update `.tfw/knowledge_state.yaml`", ("knowledge_state.yaml",),
                                        ("processed_task_digests", ("knowledge_state.yaml",))),
        "citations": _variants("gate in plan.md Step 2", ("Knowledge Gate",)),
        "gate": _variants("user approves changes before writing", "WAIT",
                          ("WAIT 2", "WAIT")),
    },
    "C3": {
        "decision": _variants("re-reads that task's", "follow task status"),
        "refusal_reason": _variants("It is never authoritative", "derived index is stale"),
        "artifacts_created": _variants("index degrades discovery", ()),
        "artifacts_modified": _variants("index degrades discovery", ()),
        "citations": _variants("task state", ("Task control files",)),
        "gate": _variants("project stays workable", "CONTINUE"),
    },
    "A1": {
        "decision": _variants("| `/tfw-plan` | `.tfw/workflows/plan.md` |", "resolve exact command"),
        "refusal_reason": _variants("command must", None),
        "artifacts_created": _variants("canonical workflow", ()),
        "artifacts_modified": _variants("command must", ()),
        "citations": _variants("Trace-First Workflow Commands", ("adapter manifest",)),
        "gate": _variants("canonical workflow", "CONTINUE"),
    },
}

def execute_scenario(tree: SourceTree, case: str) -> SemanticRecord:
    if case not in SCENARIOS:
        raise SourceContractError(f"unknown scenario: {case}")
    scenario = SCENARIOS[case]
    probes = scenario.baseline if tree.ref is not None else scenario.candidate
    sources = []
    for probe in probes:
        text = tree.read(probe.path)
        addressed = text if probe.heading == "*" else resolve_heading(text, probe.heading)
        if probe.needle not in addressed:
            raise SourceContractError(f"{case}: absent anchor in {probe.path}#{probe.heading}")
        sources.append((probe, addressed))
    values = []
    provenance = []
    for field_name in SEMANTIC_FIELDS:
        matches = [(probe, clause, value) for clause, value in DERIVATIONS[case][field_name]
                   for probe, text in sources if clause in text]
        if len(matches) != 1:
            raise SourceContractError(f"{case}: {field_name} semantic source resolved {len(matches)} times")
        probe, clause, value = matches[0]
        values.append(value)
        provenance.append((field_name, probe.path, probe.heading, clause))
    manifest = tuple(probe.path if probe.heading == "*" else f"{probe.path}#{probe.heading}"
                     for probe, _ in sources)
    return SemanticRecord(*values, read_manifest=manifest, source_clauses=tuple(provenance))
def semantic_record(case: str, profile: str) -> SemanticRecord:
    tree = (SourceTree.from_git(PROJECT_ROOT, BASELINE_REF) if profile == "baseline"
            else SourceTree.from_path(PROJECT_ROOT))
    return execute_scenario(tree, case)
def source_mutant(tree: SourceTree, case: str) -> SourceTree:
    scenario = SCENARIOS[case]; probe = (scenario.baseline if tree.ref else scenario.candidate)[0]
    text = tree.read(probe.path)
    if probe.needle not in text: raise SourceContractError(f"{case}: cannot construct source mutant")
    return tree.with_text(probe.path, text.replace(probe.needle, f"MUTATED-{case}", 1))
def semantic_projection(record: SemanticRecord) -> tuple[object, ...]:
    return tuple(getattr(record, field) for field in SEMANTIC_FIELDS)

def test_round2_expected_outcome_cannot_feed_source_execution(monkeypatch):
    candidate = SourceTree.from_path(PROJECT_ROOT)
    produced = semantic_projection(execute_scenario(candidate, "P1"))
    wrong = ("WRONG", None, (), (), (), "CONTINUE")
    monkeypatch.setitem(EXPECTED_RECORDS, "P1", wrong)
    assert semantic_projection(execute_scenario(candidate, "P1")) == produced
    with pytest.raises(AssertionError):
        assert produced == EXPECTED_RECORDS["P1"]

def test_round2_minimal_anchor_only_source_cannot_manufacture_a_record():
    candidate = SourceTree.from_path(PROJECT_ROOT)
    probe = SCENARIOS["P1"].candidate[0]
    minimal = candidate.with_text(probe.path, f"## {probe.heading}\n{probe.needle}\n")
    with pytest.raises(SourceContractError, match="P1.*semantic"):
        execute_scenario(minimal, "P1")

def test_round2_semantic_substitution_changes_produced_output_before_comparison_rejects():
    candidate = SourceTree.from_path(PROJECT_ROOT)
    path = SCENARIOS["E3"].candidate[0].path
    original = candidate.read(path)
    assert "If build fails" in original and "Never write RF with failing build" in original
    substituted = candidate.with_text(
        path,
        original.replace("Never write RF with failing build", "Write RF even with failing build", 1),
    )
    actual = semantic_projection(execute_scenario(substituted, "E3"))
    assert actual != semantic_projection(execute_scenario(candidate, "E3"))
    with pytest.raises(AssertionError):
        assert actual == EXPECTED_RECORDS["E3"]

@pytest.mark.parametrize("case", sorted(SCENARIOS))
def test_baseline_and_candidate_have_the_same_semantic_record(case):
    baseline = semantic_record(case, "baseline"); candidate = semantic_record(case, "candidate")
    assert semantic_projection(candidate) == semantic_projection(baseline) == EXPECTED_RECORDS[case]
    assert candidate.read_manifest and baseline.read_manifest
    assert tuple(field for field, _, _, _ in candidate.source_clauses) == SEMANTIC_FIELDS

@pytest.mark.parametrize("family", "PREVCA")
def test_one_deliberate_mutant_per_family_is_rejected(family):
    case = next(case for case in SCENARIOS if case.startswith(family)); candidate = SourceTree.from_path(PROJECT_ROOT)
    with pytest.raises(SourceContractError, match=case):
        execute_scenario(source_mutant(candidate, case), case)

HEADING = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.+?)\s*$")
NUMBER = re.compile(r"^(?:§\s*)?\d+(?:\.\d+)*(?:[.)])?\s+")

def _heading_title(raw: str) -> str:
    return NUMBER.sub("", raw).removesuffix(" 🟢 FREE").strip()

def resolve_heading(text: str, heading: str) -> str:
    """Return one Markdown heading range, refusing zero or multiple matches."""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").splitlines(keepends=True)
    matches = [(i, len(m.group("marks"))) for i, line in enumerate(lines)
               if (m := HEADING.match(line.rstrip("\n"))) and _heading_title(m.group("title")) == heading]
    if len(matches) != 1: raise ValueError(f"heading {heading!r} resolved {len(matches)} times")
    start, level = matches[0]
    end = next((i for i in range(start + 1, len(lines))
                if (m := HEADING.match(lines[i].rstrip("\n"))) and len(m.group("marks")) <= level), len(lines))
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
    assert all((PROJECT_ROOT / path).exists() for path in ("tasks/DEBT-SNAPSHOT.md", "tasks/BOARD-SNAPSHOT.md"))

@dataclass(frozen=True)
class ReadEdge:
    command: str; checkpoint: str; source: str; heading: str
    reason: str; repeat: str; authority: str

def _words(text: str) -> int:
    return len(re.findall(r"\S+", text))

def test_audit_has_required_fields_and_no_candidate_full_library_edge():
    rows = audit_rows("/tfw-plan", "candidate") + audit_rows("/tfw-knowledge", "candidate")
    required = {"command", "checkpoint", "source", "heading", "reason", "observed_words", "repeat", "authority"}
    assert rows and all(set(row) == required for row in rows)
    assert not [r for r in rows if r["source"] in FORBIDDEN_UNSCOPED and
                r["heading"] == "*" and r["checkpoint"] == "root context"]

def test_omitted_candidate_edge_is_caught_independently_of_audit_output():
    candidate = SourceTree.from_path(PROJECT_ROOT)
    with pytest.raises(SourceContractError, match="route.*tfw-plan"):
        discover_read_graph(omit_command_route(candidate, "/tfw-plan"), "/tfw-plan")

@dataclass(frozen=True)
class TextTarget:
    path: str; needle: str; heading: str = "*"

@dataclass(frozen=True)
class LedgerSpec:
    test: TextTarget; history: TextTarget

@dataclass(frozen=True)
class DeletionLedgerRow:
    condition: str; action: str; authority: TextTarget; test: TextTarget; history: TextTarget

RECOMMENDATION_PATH = "workspace/2026/TFW_20260902-175227_RCFR/research/iter2/3_extract.md"
GATHER_PATH = "workspace/2026/TFW_20260902-175227_RCFR/research/iter2/2_gather.md"

LEDGER_SPECS = {
    "R03": LedgerSpec(TextTarget("docs/scripts/test_runtime_context.py", "def test_round1_semantic_records_come_from_both_source_trees"), TextTarget("KNOWLEDGE.md", "| D63 |", "Architecture Decisions")),
    "R04": LedgerSpec(TextTarget(".tfw/scripts/test_gen_index.py", "def test_an_event_without_on_behalf_of_is_refused"), TextTarget("KNOWLEDGE.md", "| D68 |", "Architecture Decisions")),
    "R05": LedgerSpec(TextTarget("docs/scripts/test_runtime_context.py", "def test_one_deliberate_mutant_per_family_is_rejected"), TextTarget("KNOWLEDGE.md", "| D72 |", "Architecture Decisions")),
    "R06": LedgerSpec(TextTarget(".tfw/scripts/test_gen_index.py", "def test_a_directory_that_is_not_a_task_is_reported_never_dropped"), TextTarget("KNOWLEDGE.md", "| D69 |", "Architecture Decisions")),
    "R07": LedgerSpec(TextTarget(".tfw/scripts/test_gen_index.py", "def test_a_task_transition_does_not_touch_anything_shared"), TextTarget("KNOWLEDGE.md", "| D68 |", "Architecture Decisions")),
    "R08": LedgerSpec(TextTarget("docs/scripts/test_runtime_context.py", "def test_round1_real_omission_and_heading_failures"), TextTarget("KNOWLEDGE.md", "| D72 |", "Architecture Decisions")),
    "R09": LedgerSpec(TextTarget("docs/scripts/test_runtime_context.py", "def test_workflow_commands_do_not_use_adapter_positional_placeholders"), TextTarget("KNOWLEDGE.md", "TFW_20260830-194027_TLD", "Architecture Decisions")),
    "R10": LedgerSpec(TextTarget("docs/scripts/test_integration.py", "def test_no_normative_file_states_a_retired_rule"), TextTarget("KNOWLEDGE.md", "| D61 |", "Architecture Decisions")),
    "R11": LedgerSpec(TextTarget("docs/scripts/test_runtime_context.py", "def test_operational_glossary_entries_are_term_routers"), TextTarget(GATHER_PATH, "Execution Modes", "G4: Deletion ledger has a surviving owner for every glossary/history block")),
    "R12": LedgerSpec(TextTarget("docs/scripts/test_runtime_context.py", "def test_rdp_glossary_semantics_survive_the_router"), TextTarget(GATHER_PATH, "PV and PV Index", "G4: Deletion ledger has a surviving owner for every glossary/history block")),
    "R13": LedgerSpec(TextTarget("docs/scripts/test_runtime_context.py", "def test_retired_terms_resolve_only_to_durable_history"), TextTarget(GATHER_PATH, "retired Debt Registry", "G4: Deletion ledger has a surviving owner for every glossary/history block")),
    "R14": LedgerSpec(TextTarget("docs/scripts/test_integration.py", "def test_empty_receiver_gets_exact_vendor_root_and_eleven_commands"), TextTarget(GATHER_PATH, "project-specific placeholder", "G4: Deletion ledger has a surviving owner for every glossary/history block")),
}

def _resolve_target(tree: SourceTree, target: TextTarget) -> None:
    text = tree.read(target.path)
    addressed = text if target.heading == "*" else resolve_heading(text, target.heading)
    if target.needle not in addressed:
        raise SourceContractError(f"unresolved: {target.path}#{target.heading} -> {target.needle!r}")

def resolve_deletion_ledger(tree: SourceTree) -> dict[str, DeletionLedgerRow]:
    """Resolve each research recommendation to source authority, a test, and history."""
    heading = "E2: Exact implementation recommendation catalogue"
    recommendation = resolve_heading(tree.read(RECOMMENDATION_PATH), heading)
    rows = {}
    for row_id, spec in LEDGER_SPECS.items():
        line = next((line for line in recommendation.splitlines()
                     if line.startswith(f"| {row_id} |")), None)
        if line is None:
            raise SourceContractError(f"{row_id}: recommendation authority row does not resolve")
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 7 or not cells[2] or not cells[3]:
            raise SourceContractError(f"{row_id}: recommendation condition/action is incomplete")
        authority = TextTarget(RECOMMENDATION_PATH, f"| {row_id} |", heading)
        for target in (authority, spec.test, spec.history):
            _resolve_target(tree, target)
        rows[row_id] = DeletionLedgerRow(cells[2], cells[3], authority, spec.test, spec.history)
    return rows

def test_workflow_commands_do_not_use_adapter_positional_placeholders():
    files = sorted((PROJECT_ROOT / ".tfw/workflows").rglob("*.md")); offenders = []
    for path in files:
        if re.search(r"\$(?:ARGUMENTS|[0-9])", path.read_text(encoding="utf-8")):
            offenders.append(path.relative_to(PROJECT_ROOT).as_posix())
    assert not offenders, f"adapter positional placeholders survive in: {offenders}"

def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit", action="store_true"); parser.add_argument("--baseline-ref", default=BASELINE_REF)
    parser.add_argument("--semantic-json", action="store_true")
    args = parser.parse_args(argv)
    if args.audit: print(render_audit(args.baseline_ref), end="")
    if args.semantic_json:
        payload = {case: {p: semantic_record(case, p).__dict__ for p in ("baseline", "candidate")}
                   for case in sorted(SCENARIOS)}
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0

# Review round 1 source-sensitivity contract. These tests intentionally name the source-backed
# API rather than accepting records or graph rows assembled independently of a source tree.
PATH_TOKEN = re.compile(r"`([^`]+)`")
SOURCE_TOKEN = re.compile(r"(?:\.tfw/[^\s`]+\.(?:md|yaml)|KNOWLEDGE\.md|knowledge/\*\.md)$")
def _append_edge(edges, command, checkpoint, source, heading, reason, authority):
    source = source.replace("\\", "/")
    repeat = "repeated" if any(edge.source == source for edge in edges) else "once"
    edges.append(ReadEdge(command, checkpoint, source, heading, reason, repeat, authority))
def _add_full(tree, edges, command, checkpoint, token, reason, authority):
    if token == "knowledge/*.md":
        for path in tree.files(token):
            _append_edge(edges, command, checkpoint, path, "*", reason, authority)
    else:
        tree.read(token)
        _append_edge(edges, command, checkpoint, token, "*", reason, authority)
def _add_literal_loads(tree, edges, command, checkpoint, text, reason, authority):
    for token in PATH_TOKEN.findall(text):
        if (token == "AGENTS.md" or SOURCE_TOKEN.fullmatch(token)) and "{" not in token:
            _add_full(tree, edges, command, checkpoint, token, reason, authority)
def _add_read_contract(tree, edges, command, workflow_text):
    contract = resolve_heading(workflow_text, "Read Contract")
    for line in contract.splitlines():
        if not line.startswith("|") or re.match(r"^\|[-:| ]+\|$", line): continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if not cells or not cells[0].isdigit() or len(cells) < 4: continue
        tokens = PATH_TOKEN.findall(cells[1]); reason, authority = cells[2], cells[3]
        for index, token in enumerate(tokens):
            if not SOURCE_TOKEN.fullmatch(token): continue
            if token in (".tfw/conventions.md", ".tfw/glossary.md", "KNOWLEDGE.md"):
                following = []
                for value in tokens[index + 1:]:
                    if SOURCE_TOKEN.fullmatch(value): break
                    following.append(value)
                for heading in following:
                    resolve_heading(tree.read(token), heading)
                    _append_edge(edges, command, "workflow read contract", token, heading, reason, authority)
                if not following:
                    _add_full(tree, edges, command, "workflow read contract", token, reason, authority)
            else:
                _add_full(tree, edges, command, "workflow read contract", token, reason, authority)
def discover_read_graph(tree: SourceTree, command: str) -> tuple[ReadEdge, ...]:
    if command not in ("/tfw-plan", "/tfw-knowledge"):
        raise SourceContractError(f"unsupported audit command: {command}")
    root = tree.read("AGENTS.md")
    route = re.search(rf"^\| `{re.escape(command)}` \| `(?P<workflow>[^`]+)` \|$", root, re.MULTILINE)
    if not route: raise SourceContractError(f"route {command} does not resolve in AGENTS.md")
    workflow = route.group("workflow")
    edges: list[ReadEdge] = []
    _append_edge(edges, command, "root bootstrap", "AGENTS.md", "*", "active root instructions and command route", "root")
    context_match = re.search(r"^## Context (?:Loading|Selection) \(new session\)\s*$\n(?P<body>.*?)(?=^## )", root, re.MULTILINE | re.DOTALL)
    if not context_match: raise SourceContractError("active root context-selection section does not resolve")
    _add_literal_loads(tree, edges, command, "root context", context_match.group("body"), "active root preload", "root")
    name = command.removeprefix("/tfw-")
    skill = f".agents/skills/tfw-{name}/SKILL.md"
    skill_text = tree.read(skill)
    _append_edge(edges, command, "command dispatch", skill, "*", "selected command contract", "adapter")
    contract = resolve_heading(skill_text, "Contract")
    load_lines = "\n".join(line for line in contract.splitlines() if line.startswith("- Load "))
    if not load_lines: raise SourceContractError(f"{command}: skill Load contract does not resolve")
    _add_literal_loads(tree, edges, command, "skill contract", load_lines, "skill-mandated context", "adapter")
    if workflow not in skill_text: raise SourceContractError(f"{command}: workflow absent from skill")
    workflow_text = tree.read(workflow)
    _append_edge(edges, command, "canonical dispatch", workflow, "*", "canonical command algorithm", "workflow")
    if re.search(r"^## Read Contract\s*$", workflow_text, re.MULTILINE):
        _add_read_contract(tree, edges, command, workflow_text)
    elif command == "/tfw-knowledge":
        prerequisites = resolve_heading(workflow_text, "Prerequisites")
        _add_literal_loads(tree, edges, command, "workflow prerequisites", prerequisites, "legacy prerequisites", "workflow")
        conventions = tree.read(".tfw/conventions.md")
        resolve_heading(conventions, "Fact Categories")
        _append_edge(edges, command, "workflow prerequisites", ".tfw/conventions.md", "Fact Categories", "legacy category lookup", "shared rule")
    return tuple(edges)
def measure_graph(tree: SourceTree, edges: tuple[ReadEdge, ...]) -> int:
    return sum(_words(tree.read(e.source) if e.heading == "*" else
                      resolve_heading(tree.read(e.source), e.heading)) for e in edges)
def graph_reduction(baseline: SourceTree, candidate: SourceTree, command: str) -> float:
    before = measure_graph(baseline, discover_read_graph(baseline, command))
    after = measure_graph(candidate, discover_read_graph(candidate, command))
    return (before - after) * 100 / before
def omit_command_route(tree: SourceTree, command: str) -> SourceTree:
    root = tree.read("AGENTS.md")
    pattern = re.compile(rf"^\| `{re.escape(command)}` \| `[^`]+` \|\r?\n?", re.MULTILINE)
    mutated, count = pattern.subn("", root, count=1)
    if count != 1:
        raise SourceContractError(f"route {command} cannot be omitted")
    return tree.with_text("AGENTS.md", mutated)
def mutate_addressed_heading(tree: SourceTree, heading: str, mode: str) -> SourceTree:
    path = ".tfw/conventions.md"; text = tree.read(path); resolve_heading(text, heading)
    if mode == "duplicate":
        return tree.with_text(path, text + f"\n## {heading}\nround-one duplicate mutant\n")
    if mode != "missing": raise ValueError(f"unknown heading mutation: {mode}")
    pattern = re.compile(rf"^(#+\s+(?:§\s*)?(?:\d+(?:\.\d+)*(?:[.)])?\s+)?){re.escape(heading)}\s*$", re.MULTILINE)
    mutated, count = pattern.subn(r"\1MUTATED", text, count=1)
    if count != 1: raise SourceContractError(f"heading {heading!r} cannot be mutated")
    return tree.with_text(path, mutated)
def audit_rows(command: str, profile: str, ref: str | None = None) -> list[dict[str, object]]:
    tree = (SourceTree.from_git(PROJECT_ROOT, ref or BASELINE_REF) if profile == "baseline"
            else SourceTree.from_path(PROJECT_ROOT))
    rows = []
    for edge in discover_read_graph(tree, command):
        text = tree.read(edge.source)
        observed = _words(text if edge.heading == "*" else resolve_heading(text, edge.heading))
        rows.append({**edge.__dict__, "observed_words": observed})
    return rows
def render_audit(baseline_ref: str = BASELINE_REF) -> str:
    lines = ["command\tprofile\tcheckpoint\tsource\theading\treason\tobserved_words\trepeat_classification\tauthority"]
    for command in ("/tfw-plan", "/tfw-knowledge"):
        totals = {}
        for profile in ("before", "after"):
            rows = audit_rows(command, "baseline" if profile == "before" else "candidate", baseline_ref)
            for row in rows:
                keys = ("command", "checkpoint", "source", "heading", "reason", "observed_words", "repeat", "authority")
                lines.append("\t".join(map(str, (row["command"], profile, *(row[key] for key in keys[1:])))))
            totals[profile] = sum(int(row["observed_words"]) for row in rows)
        reduction = (totals["before"] - totals["after"]) * 100 / totals["before"]
        lines.append(f"TOTAL\t{command}\tbefore={totals['before']}\tafter={totals['after']}\treduction={reduction:.1f}%")
    return "\n".join(lines) + "\n"
def test_round1_active_roots_do_not_preload_the_full_common_library():
    for path in ("AGENTS.md", ".agent/rules/agents.md"):
        text = _read(path)
        match = re.search(
            r"^## Context (?:Loading|Selection) \(new session\)\s*$\n(?P<body>.*?)(?=^## )",
            text,
            re.MULTILINE | re.DOTALL,
        )
        assert match, f"{path}: active context-selection section is missing"
        body = match.group("body")
        for forbidden in (".tfw/conventions.md", ".tfw/glossary.md", "KNOWLEDGE.md"):
            assert forbidden not in body, f"{path}: active root still preloads {forbidden}"

def test_round1_audit_discovers_the_actual_root_skill_workflow_heading_graph():
    baseline = SourceTree.from_git(PROJECT_ROOT, BASELINE_REF); candidate = SourceTree.from_path(PROJECT_ROOT)
    for command in ("/tfw-plan", "/tfw-knowledge"):
        before = discover_read_graph(baseline, command)
        after = discover_read_graph(candidate, command)
        assert before and after and any(edge.source == "AGENTS.md" for edge in after)
        assert any(edge.source.startswith(".agents/skills/") for edge in after)
        assert any(edge.source.startswith(".tfw/workflows/") for edge in after) and any(edge.heading != "*" for edge in after)
        assert graph_reduction(baseline, candidate, command) >= 30.0

def test_round1_nonexistent_source_root_is_a_hard_failure(tmp_path):
    with pytest.raises(FileNotFoundError, match="source root"):
        SourceTree.from_path(tmp_path / "absent")

def test_round1_semantic_records_come_from_both_source_trees_and_reject_source_mutants():
    baseline = SourceTree.from_git(PROJECT_ROOT, BASELINE_REF); candidate = SourceTree.from_path(PROJECT_ROOT)
    for case in sorted(SCENARIOS):
        assert semantic_projection(execute_scenario(baseline, case)) == semantic_projection(
            execute_scenario(candidate, case)
        )
    for family in "PREVCA":
        case = next(name for name in SCENARIOS if name.startswith(family))
        with pytest.raises(SourceContractError, match=case):
            execute_scenario(source_mutant(candidate, case), case)

def test_round1_real_omission_and_heading_failures_are_independent_of_audit_output():
    candidate = SourceTree.from_path(PROJECT_ROOT)
    with pytest.raises(SourceContractError, match="route.*tfw-plan"):
        discover_read_graph(omit_command_route(candidate, "/tfw-plan"), "/tfw-plan")
    with pytest.raises(ValueError, match="resolved 0 times"):
        discover_read_graph(mutate_addressed_heading(candidate, "Task control files", "missing"), "/tfw-plan")
    with pytest.raises(ValueError, match="resolved 2 times"):
        discover_read_graph(mutate_addressed_heading(candidate, "Task control files", "duplicate"), "/tfw-plan")

def test_round1_r03_r14_ledger_resolves_real_targets():
    candidate = SourceTree.from_path(PROJECT_ROOT)
    resolved = resolve_deletion_ledger(candidate)
    assert set(resolved) == {f"R{number:02d}" for number in range(3, 15)}
    assert all(row.condition and row.action and row.authority and row.test and row.history for row in resolved.values())

if __name__ == "__main__":
    raise SystemExit(main())
