"""Source-derived semantic fixtures and runtime-context audits for Phases A and B."""
from __future__ import annotations
import argparse, fnmatch, json, re, subprocess
from dataclasses import dataclass, field
from pathlib import Path
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PHASE_A_BASELINE_REF = "2728dae78d55f6cb7daa39c82874ad5b43621f8a"
BASELINE_REF = "80382fbffd52b1f13cb3b38e8e450ecc0fef2fd5"
PRIMARY_VARIANTS = (
    "/tfw-plan", "/tfw-research:focused", "/tfw-research:deep", "/tfw-handoff", "/tfw-review",
)
PHASE_B_BASELINE_WORDS = {
    "/tfw-plan": 50_851,
    "/tfw-research:focused": 29_992,
    "/tfw-research:deep": 30_057,
    "/tfw-handoff": 55_885,
    "/tfw-review": 74_537,
}
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
    "P4": _scenario(".tfw/workflows/plan.md", "pending_task_ids", heading="Step 2: Knowledge Gate"),
    "R1": _scenario(".tfw/workflows/research/base.md", "Stage Checkpoint"),
    "R2": _scenario(".tfw/workflows/research/base.md", "MUST: external research every stage"),
    "R3": _scenario(".tfw/workflows/research/base.md", "STOP after writing final RES"),
    "E1": _scenario(".tfw/workflows/handoff.md", "all blocking questions resolved"),
    "E2": _scenario(".tfw/workflows/handoff.md", "verify the prerequisite AC gate passes"),
    "E3": _scenario(".tfw/workflows/handoff.md", "If build fails"),
    "E4": _scenario(".tfw/workflows/handoff.md", "highest-numbered revision", "highest approved TS lineage"),
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
        "artifacts_created": _variants("asks for a different", (),
                                        ("silently reuses the identifier", ("duplicate task",))),
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
        "decision": _variants("Gather → Extract → Challenge", "start Extract",
                              ("Gather → Omit Extract → Challenge", "skip Extract")),
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
        "decision": _variants("Wait for user approval", "await ONB answer",
                              ("Bypass user approval", "bypass ONB approval")),
        "refusal_reason": _variants("blocking questions resolved", "blocking question unanswered"),
        "artifacts_created": _variants("do NOT proceed until all blocking questions resolved", ()),
        "artifacts_modified": _variants("do NOT proceed until all blocking questions resolved", ()),
        "citations": _variants("Commit ONB", ("ONB",)),
        "gate": _variants("Wait for user approval", "WAIT",
                          ("Bypass user approval", "WAIT")),
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
        "artifacts_modified": _variants("populate the EV file", ("EV",),
                                          ("record the actual environment and one result per TS AC", ("EV",))),
        "citations": _variants("Collect evidence", ("Evidence Collection",)),
        "gate": _variants("Never write RF with failing build", "STOP",
                          ("Write RF even with failing build", "CONTINUE")),
    },
    "E4": {
        "decision": _variants("highest-numbered revision", "execute latest revision",
                                ("highest approved TS lineage", "execute latest revision")),
        "refusal_reason": _variants("What is not re-done", None),
        "artifacts_created": _variants("TS and the REVIEW take **siblings**", ()),
        "artifacts_modified": _variants("RF and the ONB are **appended to**", ("ONB", "RF")),
        "citations": _variants("Returning after a 🔄 REVISE", ("Revision",)),
        "gate": _variants("which governs and which carries the round's order", "CONTINUE",
                          ("one governing order", "CONTINUE")),
    },
    "V1": {
        "decision": _variants("On any discrepancy → escalate to 100%", "expand verification to 100%"),
        "refusal_reason": _variants("On any discrepancy", "sample discrepancy"),
        "artifacts_created": _variants("Min verify ratio", ()),
        "artifacts_modified": _variants("verify.md findings", ("verify.md",),
                                         ("ignore verification findings", ())),
        "citations": _variants("On any discrepancy", ("Evidence Audit",)),
        "gate": _variants("go back and do it", "CONTINUE"),
    },
    "V2": {
        "decision": _variants("not fit for purpose", "reject purpose failure"),
        "refusal_reason": _variants("Purpose Check's reference set", "frozen purpose unmet",
                                    ("master HL at its contract baseline and Project North Star reread", "frozen purpose unmet")),
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
        "refusal_reason": _variants("For trivial tasks: reviewer pre-marks both as N/A", None,
                                    ("For trivial tasks: both tools are mandatory", "knowledge capture required")),
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
        "refusal_reason": _variants("command must", None,
                                    ("command may", "optional command route")),
        "artifacts_created": _variants("canonical workflow", ()),
        "artifacts_modified": _variants("command must", (), ("command may", ())),
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

@dataclass(frozen=True)
class SemanticMutation:
    family: str; case: str; path: str; old: str; new: str; field: str

SEMANTIC_MUTATIONS = (
    SemanticMutation("P", "P1", ".tfw/conventions.md", "asks for a different",
                     "silently reuses the identifier", "artifacts_created"),
    SemanticMutation("R", "R1", ".tfw/workflows/research/base.md", "Gather → Extract → Challenge",
                     "Gather → Omit Extract → Challenge", "decision"),
    SemanticMutation("E", "E1", ".tfw/workflows/handoff.md", "Wait for user approval",
                     "Bypass user approval", "decision"),
    SemanticMutation("V", "V1", ".tfw/workflows/review.md", "verify.md findings",
                     "ignore verification findings", "artifacts_modified"),
    SemanticMutation("C", "C1", ".tfw/workflows/review.md",
                     "For trivial tasks: reviewer pre-marks both as N/A",
                     "For trivial tasks: both tools are mandatory", "refusal_reason"),
    SemanticMutation("A", "A1", "AGENTS.md", "command must", "command may", "refusal_reason"),
)

def semantic_mutant(tree: SourceTree, family: str) -> tuple[SemanticMutation, SourceTree]:
    mutation = next((item for item in SEMANTIC_MUTATIONS if item.family == family), None)
    if mutation is None:
        raise SourceContractError(f"unknown semantic mutant family: {family}")
    text = tree.read(mutation.path)
    if mutation.old not in text:
        raise SourceContractError(f"{mutation.case}: semantic substitution source does not resolve")
    return mutation, tree.with_text(mutation.path, text.replace(mutation.old, mutation.new))

def semantic_mutant_result(tree: SourceTree, family: str) -> dict[str, object]:
    mutation, mutated_tree = semantic_mutant(tree, family)
    produced = execute_scenario(mutated_tree, mutation.case)
    expected = execute_scenario(tree, mutation.case)
    return {
        "family": family,
        "scenario": mutation.case,
        "field": mutation.field,
        "produced": getattr(produced, mutation.field),
        "expected": getattr(expected, mutation.field),
        "projection_changed": semantic_projection(produced) != semantic_projection(expected),
        "independent_expected_rejects": semantic_projection(produced) != EXPECTED_RECORDS[mutation.case],
    }

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
    candidate = SourceTree.from_path(PROJECT_ROOT)
    mutation, mutated_tree = semantic_mutant(candidate, family)
    produced = execute_scenario(mutated_tree, mutation.case)
    normal = execute_scenario(candidate, mutation.case)
    assert getattr(produced, mutation.field) != getattr(normal, mutation.field)
    assert semantic_projection(produced) != semantic_projection(normal)
    with pytest.raises(AssertionError):
        assert semantic_projection(produced) == EXPECTED_RECORDS[mutation.case]

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
    reason: str; repeat: str; authority: str; charged: bool = True

def _words(text: str) -> int:
    return len(re.findall(r"\S+", text))

def test_audit_has_required_fields_and_no_candidate_full_library_edge():
    rows = [row for command in PRIMARY_VARIANTS for row in audit_rows(command, "candidate")]
    required = {"command", "checkpoint", "source", "heading", "reason", "observed_words",
                "repeat", "authority", "charged"}
    assert rows and all(set(row) == required for row in rows)
    assert not [r for r in rows if r["source"] in FORBIDDEN_UNSCOPED and
                r["heading"] == "*" and r["charged"]]

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
    parser.add_argument("--semantic-mutants", action="store_true")
    parser.add_argument("--revise-routes", action="store_true")
    args = parser.parse_args(argv)
    if args.audit: print(render_audit(args.baseline_ref), end="")
    if args.semantic_json:
        payload = {case: {p: semantic_record(case, p).__dict__ for p in ("baseline", "candidate")}
                   for case in sorted(SCENARIOS)}
        print(json.dumps(payload, indent=2, sort_keys=True))
    if args.semantic_mutants:
        tree = SourceTree.from_path(PROJECT_ROOT)
        print(json.dumps([semantic_mutant_result(tree, family) for family in "PREVCA"],
                         indent=2, sort_keys=True))
    if args.revise_routes:
        routes = resolve_revise_routes(SourceTree.from_path(PROJECT_ROOT))
        print(json.dumps({case: record.__dict__ for case, record in routes.items()},
                         indent=2, sort_keys=True))
    return 0

# Review round 1 source-sensitivity contract. These tests intentionally name the source-backed
# API rather than accepting records or graph rows assembled independently of a source tree.
PATH_TOKEN = re.compile(r"`([^`]+)`")
SOURCE_TOKEN = re.compile(r"(?:\.tfw/[^\s`]+\.(?:md|yaml)|KNOWLEDGE\.md|knowledge/\*\.md)$")
P0_P4_RANGES = (
    ("README.md", "@preamble"),
    ("README.md", "How It Works"),
    (".tfw/README.md", "NS1 — Purpose"),
    (".tfw/README.md", "NS2 — Principles"),
    (".tfw/README.md", "Methodology values"),
    (".tfw/README.md", "NS3 — Non-goals"),
    (".tfw/README.md", "Success Criteria"),
    ("knowledge/philosophy.md", "*"),
    ("KNOWLEDGE.md", "Architecture Map"),
    (".tfw/conventions.md", "HL (High Level)"),
    (".tfw/conventions.md", "Design Rules"),
    (".tfw/conventions.md", "Anti-patterns (prohibited)"),
)
PURPOSE_REREAD_RANGES = (
    ("README.md", "@preamble"),
    ("README.md", "How It Works"),
    (".tfw/README.md", "NS1 — Purpose"),
    (".tfw/README.md", "NS2 — Principles"),
    (".tfw/README.md", "NS3 — Non-goals"),
)
RESEARCH_STAGE_TEMPLATES = (
    ".tfw/templates/research/1_briefing.md", ".tfw/templates/research/2_gather.md",
    ".tfw/templates/research/3_extract.md", ".tfw/templates/research/4_challenge.md",
)
REVIEW_STAGE_TEMPLATES = (
    ".tfw/templates/review/map.md", ".tfw/templates/review/verify.md",
    ".tfw/templates/review/judge.md",
)

def _append_edge(edges, command, checkpoint, source, heading, reason, authority, charged=True):
    source = source.replace("\\", "/")
    repeat = "repeated" if any(edge.source == source for edge in edges) else "once"
    edges.append(ReadEdge(command, checkpoint, source, heading, reason, repeat, authority, charged))

def _has_edge(edges, source, heading=None):
    return any(edge.source == source and (heading is None or edge.heading == heading) for edge in edges)

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

def _selector_for_config(token):
    return {
        "tfw.research": "@yaml-research",
        "tfw.scope_budgets": "@scope-values",
        "tfw.review.min_verify_ratio": "@review-value-comment",
    }.get(token)

def _add_read_contract(tree, edges, command, workflow_text):
    contract = resolve_heading(workflow_text, "Read Contract")
    lines = contract.splitlines()
    header = next((line for line in lines if line.startswith("| Order |")), None)
    if header is None:
        raise SourceContractError(f"{command}: Read Contract table header does not resolve")
    headings = [cell.strip() for cell in header.strip("|").split("|")]
    required = {"Input", "Checkpoint purpose", "Authority"}
    if not required.issubset(headings):
        raise SourceContractError(f"{command}: Read Contract columns are incomplete")
    input_index, reason_index, authority_index = (headings.index(name) for name in
                                                    ("Input", "Checkpoint purpose", "Authority"))
    for line in lines:
        if not line.startswith("|") or re.match(r"^\|[-:| ]+\|$", line):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if not cells or not cells[0].isdigit() or len(cells) != len(headings):
            continue
        tokens = PATH_TOKEN.findall(cells[input_index])
        reason, authority = cells[reason_index], cells[authority_index]
        for index, token in enumerate(tokens):
            if not SOURCE_TOKEN.fullmatch(token): continue
            if "{" in token:
                continue
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
            elif token == ".tfw/project_config.yaml":
                following = next((_selector_for_config(value) for value in tokens[index + 1:]
                                  if _selector_for_config(value)), None)
                if following:
                    _append_edge(edges, command, "workflow read contract", token, following,
                                 reason, authority)
                else:
                    _add_full(tree, edges, command, "workflow read contract", token, reason, authority)
            else:
                _add_full(tree, edges, command, "workflow read contract", token, reason, authority)

def _add_ranges(tree, edges, command, checkpoint, ranges, reason, authority):
    for source, heading in ranges:
        _edge_text(tree, source, heading)
        _append_edge(edges, command, checkpoint, source, heading, reason, authority)

def _add_dynamic(edges, command, checkpoint, source, reason, authority):
    _append_edge(edges, command, checkpoint, source, "@dynamic", reason, authority, charged=False)

def _add_primary_supplements(tree, edges, command, workflow_text):
    base = command.split(":", 1)[0]
    has_contract = re.search(r"^## Read Contract\s*$", workflow_text, re.MULTILINE) is not None
    if base == "/tfw-plan":
        _add_ranges(tree, edges, command, "P0-P4 scan", P0_P4_RANGES,
                    "independent Project North Star and architecture scan", "project authority")
        _add_dynamic(edges, command, "task selection", "<selected task artifacts>",
                     "task-specific context selected by planning steps", "named source")
    elif base == "/tfw-research":
        mode = command.partition(":")[2]
        if mode not in {"focused", "deep"}:
            raise SourceContractError(f"unsupported research mode: {command}")
        if not _has_edge(edges, ".tfw/project_config.yaml", "@yaml-research"):
            _append_edge(edges, command, "mode selection", ".tfw/project_config.yaml",
                         "@yaml-research", "research mode and limits", "project config")
        if not _has_edge(edges, ".tfw/conventions.md", "Context Selection"):
            _append_edge(edges, command, "context validation", ".tfw/conventions.md",
                         "Context Selection", "address resolution and hard stop", "shared rule")
        mode_path = f".tfw/workflows/research/{mode}.md"
        if not _has_edge(edges, mode_path):
            _add_full(tree, edges, command, "mode selection", mode_path, "selected research mode", "workflow")
        stage_paths = RESEARCH_STAGE_TEMPLATES
        for path in stage_paths:
            if not _has_edge(edges, path):
                _add_full(tree, edges, command, "stage gate", path, "stage output form", "template")
        if not _has_edge(edges, ".tfw/templates/RES.md"):
            _add_full(tree, edges, command, "synthesis gate", ".tfw/templates/RES.md",
                      "research report form", "template")
        _add_dynamic(edges, command, "iteration state", "<selected status, journal, and iteration artifacts>",
                     "resume and lineage state", "task-local")
    elif base == "/tfw-handoff":
        if not has_contract:
            section = resolve_heading(workflow_text, "Context Loading (Executor)")
            _add_literal_loads(tree, edges, command, "legacy workflow context", section,
                               "executor preload", "workflow")
        if not _has_edge(edges, ".tfw/project_config.yaml", "@scope-values"):
            _append_edge(edges, command, "scope gate", ".tfw/project_config.yaml", "@scope-values",
                         "implementation-surface ceiling", "project config")
        for path in (".tfw/templates/ONB.md", ".tfw/templates/evidence/EV.md", ".tfw/templates/RF.md"):
            if not _has_edge(edges, path):
                _add_full(tree, edges, command, "artifact gate", path, "executor output form", "template")
        _add_dynamic(edges, command, "execution input", "<selected status, journal, HL, TS, RF, and REVIEW lineage>",
                     "governing order and revision state", "task-local/governing artifacts")
    elif base == "/tfw-review":
        if not has_contract:
            section = resolve_heading(workflow_text, "Context Loading (Reviewer)")
            _add_literal_loads(tree, edges, command, "legacy workflow context", section,
                               "reviewer preload", "workflow")
        for path in (*REVIEW_STAGE_TEMPLATES, ".tfw/templates/REVIEW.md"):
            if not _has_edge(edges, path):
                _add_full(tree, edges, command, "review stage gate", path, "review output form", "template")
        _add_ranges(tree, edges, command, "independent P0-P4 scan", P0_P4_RANGES,
                    "verify implementation against project values", "project authority")
        _add_ranges(tree, edges, command, "Purpose Check reread", PURPOSE_REREAD_RANGES,
                    "independent frozen-purpose judgment", "project authority")
        if not _has_edge(edges, ".tfw/project_config.yaml", "@review-value-comment"):
            _append_edge(edges, command, "verification ratio", ".tfw/project_config.yaml",
                         "@review-value-comment", "minimum sample and escalation rule", "project config")
        _add_dynamic(edges, command, "verification inputs", "<selected status, journal, task artifacts, and P5-P7 sources>",
                     "claim map, evidence, and relevant values", "task-local/named sources")

def validate_research_stage_graph(edges: tuple[ReadEdge, ...]) -> None:
    stages = tuple(edge.source for edge in edges if edge.checkpoint == "stage gate")
    if stages != RESEARCH_STAGE_TEMPLATES:
        raise SourceContractError(
            "Researcher graph stage order is incomplete: "
            f"expected {RESEARCH_STAGE_TEMPLATES!r}, observed {stages!r}"
        )

def discover_read_graph(tree: SourceTree, command: str) -> tuple[ReadEdge, ...]:
    base_command = command.split(":", 1)[0]
    if command not in (*PRIMARY_VARIANTS, "/tfw-knowledge"):
        raise SourceContractError(f"unsupported audit command: {command}")
    root = tree.read("AGENTS.md")
    route = re.search(rf"^\| `{re.escape(base_command)}` \| `(?P<workflow>[^`]+)` \|$", root, re.MULTILINE)
    if not route: raise SourceContractError(f"route {command} does not resolve in AGENTS.md")
    workflow = route.group("workflow")
    edges: list[ReadEdge] = []
    _append_edge(edges, command, "root bootstrap", "AGENTS.md", "*", "active root instructions and command route", "root")
    context_match = re.search(r"^## Context (?:Loading|Selection) \(new session\)\s*$\n(?P<body>.*?)(?=^## )", root, re.MULTILINE | re.DOTALL)
    if not context_match: raise SourceContractError("active root context-selection section does not resolve")
    _add_literal_loads(tree, edges, command, "root context", context_match.group("body"), "active root preload", "root")
    name = base_command.removeprefix("/tfw-")
    skill = f".agents/skills/tfw-{name}/SKILL.md"
    skill_text = tree.read(skill)
    _append_edge(edges, command, "command dispatch", skill, "*", "selected command contract", "adapter")
    contract = resolve_heading(skill_text, "Contract")
    load_lines = "\n".join(line for line in contract.splitlines() if line.startswith("- Load "))
    if command in PRIMARY_VARIANTS and tree.ref is None and load_lines and any(
            token in load_lines for token in ("AGENTS.md", *sorted(FORBIDDEN_UNSCOPED))):
        raise SourceContractError(f"{command}: duplicate skill/workflow preload")
    if load_lines:
        _add_literal_loads(tree, edges, command, "skill contract", load_lines,
                           "skill-mandated context", "adapter")
    elif command in PRIMARY_VARIANTS and tree.ref is None and "do not independently preload" not in contract:
        raise SourceContractError(f"{command}: minimal skill delegation contract does not resolve")
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
    if command in PRIMARY_VARIANTS:
        _add_primary_supplements(tree, edges, command, workflow_text)
    if base_command == "/tfw-research":
        validate_research_stage_graph(tuple(edges))
    return tuple(edges)

def _edge_text(tree: SourceTree, source: str, heading: str) -> str:
    if heading == "@dynamic":
        return ""
    text = tree.read(source)
    if heading == "*":
        return text
    if heading == "@preamble":
        return text.partition("\n## ")[0]
    if heading == "@yaml-research":
        match = re.search(r"^  research:\s*$\n(?P<body>(?:(?:    |\s*$).*(?:\n|$))+)", text, re.MULTILINE)
        if not match:
            raise SourceContractError("tfw.research config range does not resolve")
        return match.group("body")
    if heading == "@scope-values":
        match = re.search(r"^  scope_budgets:\s*$\n(?P<body>(?:    .*\n)+)", text, re.MULTILINE)
        if not match:
            raise SourceContractError("tfw.scope_budgets config range does not resolve")
        values = [line.split(":", 1)[1].split("#", 1)[0].strip()
                  for line in match.group("body").splitlines() if ":" in line]
        return "scope_budgets " + " ".join(values)
    if heading == "@review-value-comment":
        line = next((line for line in text.splitlines() if re.match(r"^    min_verify_ratio:", line)), None)
        if line is None:
            raise SourceContractError("tfw.review.min_verify_ratio config range does not resolve")
        value, _, comment = line.split(":", 1)[1].partition("#")
        return f"{value.strip()} {comment.strip()}"
    return resolve_heading(text, heading)

@dataclass(frozen=True)
class ReviseRouteRecord:
    case: str; recipient: str; ruling_site: str; governing_artifact: str
    lifecycle: str; hard_stop: str

EXPECTED_REVISE_ROUTES = {
    "Rung 1 only": ReviseRouteRecord(
        "Rung 1 only",
        "Coordinator for one ruling act, then the same Executor",
        "ruled bound appended to the live REVIEW; no TS sibling",
        "existing approved TS is the implementation order; ruled live REVIEW bounds the return",
        "RF → ONB only when the Executor accepts",
        "Reviewer → Coordinator; Coordinator → /tfw-handoff; Executor → /tfw-review",
    ),
    "Any rung 2": ReviseRouteRecord(
        "Any rung 2", "Coordinator, then the same Executor",
        "one TS revision for the whole round", "highest approved TS revision",
        "TS_DRAFT → ONB when the Executor accepts",
        "Reviewer → Coordinator; Coordinator → /tfw-handoff; Executor → /tfw-review",
    ),
    "Rung 3": ReviseRouteRecord(
        "Rung 3", "Coordinator, then owner through the amendment channel",
        "HL §12 proposal plus amendment_escalated event and owner verdict",
        "none until the owner verdict leaves an executable bound",
        "unchanged; Executor is not dispatchable",
        "Reviewer → Coordinator → owner; STOP until owner verdict",
    ),
    "Mixed rung 1 + 2": ReviseRouteRecord(
        "Mixed rung 1 + 2", "Coordinator, then the same Executor",
        "one TS revision containing the complete ruled round", "highest approved TS revision",
        "TS_DRAFT → ONB when the Executor accepts",
        "Reviewer → Coordinator; Coordinator → /tfw-handoff; Executor → /tfw-review",
    ),
}

def _plain_table_cell(value: str) -> str:
    return value.replace("`", "").replace("**", "").strip()

def resolve_revise_routes(tree: SourceTree) -> dict[str, ReviseRouteRecord]:
    section = resolve_heading(tree.read(".tfw/conventions.md"), "The 🔄 REVISE route")
    lines = section.splitlines()
    header = next((line for line in lines if line.startswith("| Case |")), None)
    if header is None:
        raise SourceContractError("REVISE route table header does not resolve")
    columns = [cell.strip() for cell in header.strip("|").split("|")]
    expected_columns = [
        "Case", "Fix boundary", "Recipient after Reviewer", "Coordinator ruling site",
        "Governing execution artifact", "Lifecycle after REVIEW → after Executor acceptance",
        "Exact hard stop",
    ]
    if columns != expected_columns:
        raise SourceContractError(f"REVISE route columns differ: {columns!r}")
    records = {}
    for line in lines:
        if not line.startswith("|") or re.match(r"^\|[-:| ]+\|$", line):
            continue
        cells = [_plain_table_cell(cell) for cell in line.strip("|").split("|")]
        if len(cells) != len(columns) or cells[0] in {"Case", ""}:
            continue
        record = ReviseRouteRecord(cells[0], cells[2], cells[3], cells[4], cells[5], cells[6])
        if record.case in records:
            raise SourceContractError(f"duplicate REVISE route case: {record.case}")
        records[record.case] = record
    return records

def mutate_revise_route_cell(tree: SourceTree, case: str, column: str, replacement: str) -> SourceTree:
    path = ".tfw/conventions.md"
    text = tree.read(path)
    section = resolve_heading(text, "The 🔄 REVISE route")
    lines = section.splitlines()
    header = next(line for line in lines if line.startswith("| Case |"))
    columns = [cell.strip() for cell in header.strip("|").split("|")]
    index = columns.index(column)
    row = next((line for line in lines if line.startswith(f"| {case} |")), None)
    if row is None:
        raise SourceContractError(f"REVISE route case does not resolve: {case}")
    cells = [cell.strip() for cell in row.strip("|").split("|")]
    cells[index] = replacement
    mutated_row = "| " + " | ".join(cells) + " |"
    return tree.with_text(path, text.replace(row, mutated_row, 1))

def measure_graph(tree: SourceTree, edges: tuple[ReadEdge, ...]) -> int:
    return sum(_words(_edge_text(tree, edge.source, edge.heading))
               for edge in edges if edge.charged)
def graph_reduction(baseline: SourceTree, candidate: SourceTree, command: str) -> float:
    before = measure_graph(baseline, discover_read_graph(baseline, command))
    after = measure_graph(candidate, discover_read_graph(candidate, command))
    return (before - after) * 100 / before
def omit_command_route(tree: SourceTree, command: str) -> SourceTree:
    root = tree.read("AGENTS.md")
    pattern = re.compile(rf"^\| `{re.escape(command.split(':', 1)[0])}` \| `[^`]+` \|\r?\n?", re.MULTILINE)
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
        observed = _words(_edge_text(tree, edge.source, edge.heading)) if edge.charged else 0
        rows.append({**edge.__dict__, "observed_words": observed})
    return rows
def render_audit(baseline_ref: str = BASELINE_REF) -> str:
    lines = ["command\tprofile\tcheckpoint\tsource\theading\treason\tobserved_words\trepeat_classification\tauthority\tcharged"]
    for command in PRIMARY_VARIANTS:
        totals = {}
        for profile in ("before", "after"):
            rows = audit_rows(command, "baseline" if profile == "before" else "candidate", baseline_ref)
            for row in rows:
                keys = ("command", "checkpoint", "source", "heading", "reason", "observed_words", "repeat", "authority", "charged")
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
    baseline = SourceTree.from_git(PROJECT_ROOT, PHASE_A_BASELINE_REF); candidate = SourceTree.from_path(PROJECT_ROOT)
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
        mutation, mutated_tree = semantic_mutant(candidate, family)
        produced = execute_scenario(mutated_tree, mutation.case)
        assert semantic_projection(produced) != semantic_projection(
            execute_scenario(candidate, mutation.case))
        with pytest.raises(AssertionError):
            assert semantic_projection(produced) == EXPECTED_RECORDS[mutation.case]

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

def test_phase_b_baseline_oracle_and_every_primary_reduction_are_exact():
    baseline = SourceTree.from_git(PROJECT_ROOT, BASELINE_REF)
    candidate = SourceTree.from_path(PROJECT_ROOT)
    before = {command: measure_graph(baseline, discover_read_graph(baseline, command))
              for command in PRIMARY_VARIANTS}
    after = {command: measure_graph(candidate, discover_read_graph(candidate, command))
             for command in PRIMARY_VARIANTS}
    assert before == PHASE_B_BASELINE_WORDS
    assert sum(before.values()) == 241_322
    assert all((before[command] - after[command]) / before[command] >= 0.30
               for command in PRIMARY_VARIANTS)
    assert (sum(before.values()) - sum(after.values())) / sum(before.values()) >= 0.30

def test_phase_b_audit_reports_dynamic_selection_and_deliberate_reloads():
    candidate = SourceTree.from_path(PROJECT_ROOT)
    graphs = {command: discover_read_graph(candidate, command) for command in PRIMARY_VARIANTS}
    assert all(any(not edge.charged and edge.heading == "@dynamic" for edge in edges)
               for edges in graphs.values())
    review = graphs["/tfw-review"]
    purpose_sources = {source for source, _ in PURPOSE_REREAD_RANGES}
    purpose_edges = [edge for edge in review if edge.checkpoint == "Purpose Check reread"]
    assert purpose_edges and all(edge.repeat == "repeated" for edge in purpose_edges)
    assert purpose_sources.issubset({edge.source for edge in purpose_edges})
    handoff = graphs["/tfw-handoff"]
    assert any("REVIEW lineage" in edge.source and not edge.charged for edge in handoff)

@pytest.mark.parametrize("command", ("/tfw-research:focused", "/tfw-research:deep"))
def test_phase_b_research_graph_has_all_stages_and_omission_fails_independently(command):
    graph = discover_read_graph(SourceTree.from_path(PROJECT_ROOT), command)
    validate_research_stage_graph(graph)
    stages = tuple(edge.source for edge in graph if edge.checkpoint == "stage gate")
    assert stages == RESEARCH_STAGE_TEMPLATES
    omitted = tuple(edge for edge in graph if edge.source != ".tfw/templates/research/3_extract.md")
    with pytest.raises(SourceContractError, match="stage order is incomplete"):
        validate_research_stage_graph(omitted)

def test_phase_b_primary_skills_are_thin_delegating_routers():
    for name in ("plan", "research", "handoff", "review"):
        text = _read(f".agents/skills/tfw-{name}/SKILL.md")
        contract = resolve_heading(text, "Contract")
        assert f".tfw/workflows/{'research/base' if name == 'research' else name}.md" in contract
        assert "ROLE" not in contract or "role lock" in contract.lower()
        assert "do not independently preload" in contract
        assert not any(line.startswith("- Load ") for line in contract.splitlines())
        assert "stop" in contract.lower()

def test_phase_b_injected_skill_preload_and_address_failures_are_rejected():
    candidate = SourceTree.from_path(PROJECT_ROOT)
    path = ".agents/skills/tfw-review/SKILL.md"
    injected = candidate.with_text(
        path,
        candidate.read(path).replace("## Contract\n", "## Contract\n\n- Load `KNOWLEDGE.md`.\n", 1),
    )
    with pytest.raises(SourceContractError, match="duplicate skill/workflow preload"):
        discover_read_graph(injected, "/tfw-review")
    with pytest.raises(ValueError, match="resolved 0 times"):
        discover_read_graph(mutate_addressed_heading(candidate, "Role Lock Protocol", "missing"),
                            "/tfw-review")
    with pytest.raises(ValueError, match="resolved 2 times"):
        discover_read_graph(mutate_addressed_heading(candidate, "Role Lock Protocol", "duplicate"),
                            "/tfw-review")

@pytest.mark.parametrize("case", ("P4", "R2", "E3", "V2", "V3", "V4"))
def test_phase_b_high_risk_semantic_mutants_are_rejected(case):
    candidate = SourceTree.from_path(PROJECT_ROOT)
    if case == "V2":
        path = ".tfw/workflows/review.md"
        candidate = candidate.with_text(path, candidate.read(path).replace(
            "not fit for purpose", "acceptable despite purpose failure", 1))
        with pytest.raises(SourceContractError, match=case):
            execute_scenario(candidate, case)
        return
    with pytest.raises(SourceContractError, match=case):
        execute_scenario(source_mutant(candidate, case), case)

def _validate_executor_evidence_contract(tree: SourceTree) -> None:
    text = tree.read(".tfw/workflows/handoff.md")
    required = (
        "Use only VERIFIED / DEFERRED / BLOCKED / N/A",
        "give every VERIFIED row a resolving artifact",
        "explain every non-VERIFIED row",
    )
    missing = [clause for clause in required if clause not in text]
    if missing:
        raise SourceContractError("executor evidence contract is incomplete: " + ", ".join(missing))

def test_phase_b_executor_rejects_unsupported_verified_evidence_mutant():
    candidate = SourceTree.from_path(PROJECT_ROOT)
    _validate_executor_evidence_contract(candidate)
    text = candidate.read(".tfw/workflows/handoff.md")
    mutant = candidate.with_text(
        ".tfw/workflows/handoff.md",
        text.replace("give every VERIFIED row a resolving artifact",
                     "allow VERIFIED rows without a resolving artifact", 1),
    )
    with pytest.raises(SourceContractError, match="evidence contract"):
        _validate_executor_evidence_contract(mutant)

def test_phase_b_handoff_preserves_role_gates_artifacts_and_state_transitions():
    text = _read(".tfw/workflows/handoff.md")
    assert "ROLE LOCK: EXECUTOR" in text
    assert all(path in text for path in (".tfw/templates/ONB.md", ".tfw/templates/evidence/EV.md",
                                         ".tfw/templates/RF.md"))
    assert "lifecycle: ONB" in text and "lifecycle: RF" in text
    assert "Wait for user approval" in text and "approved AG execution grant" in text
    assert "If build fails" in text and "Never write RF with failing build" in text
    assert "Scope gate" in text and "tfw.scope_budgets" in text
    assert "Executor STOP" in text

def test_phase_b_reviewer_keeps_42_percent_sampling_and_100_percent_escalation():
    config = _edge_text(SourceTree.from_path(PROJECT_ROOT), ".tfw/project_config.yaml",
                        "@review-value-comment")
    review = _read(".tfw/workflows/review.md")
    assert config.startswith("0.42 ")
    assert "On any discrepancy → escalate to 100%" in review
    assert "independent Purpose Check" in review
    assert "The citation bar." in review
    assert "returns to the task's `owner`" in review

@pytest.mark.parametrize("case", tuple(EXPECTED_REVISE_ROUTES))
def test_revision_2_route_cases_are_source_derived_and_exact(case):
    routes = resolve_revise_routes(SourceTree.from_path(PROJECT_ROOT))
    assert set(routes) == set(EXPECTED_REVISE_ROUTES)
    assert routes[case] == EXPECTED_REVISE_ROUTES[case]

@pytest.mark.parametrize(
    ("case", "column", "field", "replacement"),
    (
        ("Rung 1 only", "Lifecycle after REVIEW → after Executor acceptance", "lifecycle",
         "`TS_DRAFT → ONB` on every REVISE"),
        ("Rung 1 only", "Recipient after Reviewer", "recipient", "Executor directly"),
        ("Any rung 2", "Governing execution artifact", "governing_artifact",
         "existing approved TS without a revision"),
        ("Rung 3", "Exact hard stop", "hard_stop", "dispatch Executor before owner verdict"),
    ),
)
def test_revision_2_route_contradiction_mutants_change_output_before_rejection(
        case, column, field, replacement):
    candidate = SourceTree.from_path(PROJECT_ROOT)
    mutant = mutate_revise_route_cell(candidate, case, column, replacement)
    produced = resolve_revise_routes(mutant)[case]
    expected = EXPECTED_REVISE_ROUTES[case]
    assert getattr(produced, field) != getattr(expected, field)
    with pytest.raises(AssertionError):
        assert produced == expected

def test_revision_2_rung_preconditions_prevent_unauthorized_executor_dispatch():
    routes = resolve_revise_routes(SourceTree.from_path(PROJECT_ROOT))
    assert "no TS sibling" in routes["Rung 1 only"].ruling_site
    assert routes["Rung 1 only"].lifecycle.startswith("RF → ONB")
    assert routes["Any rung 2"].governing_artifact == "highest approved TS revision"
    assert routes["Any rung 2"].lifecycle.startswith("TS_DRAFT → ONB")
    assert "not dispatchable" in routes["Rung 3"].lifecycle
    assert routes["Rung 3"].hard_stop.endswith("STOP until owner verdict")
    assert routes["Mixed rung 1 + 2"].governing_artifact == "highest approved TS revision"

if __name__ == "__main__":
    raise SystemExit(main())
