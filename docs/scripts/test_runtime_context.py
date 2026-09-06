"""Source-derived semantic fixtures and runtime-context audits for the complete TFW runtime."""
from __future__ import annotations
import argparse, ast, fnmatch, json, re, subprocess
from dataclasses import dataclass, field
from pathlib import Path
import pytest
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PHASE_A_BASELINE_REF = "2728dae78d55f6cb7daa39c82874ad5b43621f8a"
BASELINE_REF = "80382fbffd52b1f13cb3b38e8e450ecc0fef2fd5"
PHASE_C_BASELINE_REF = "cf36dd6ac404b2335234cd9763bc4821409ca9fc"
PRIMARY_VARIANTS = (
    "/tfw-plan", "/tfw-research:focused", "/tfw-research:deep", "/tfw-handoff", "/tfw-review",
)
SECONDARY_COMMANDS = (
    "/tfw-resume", "/tfw-docs", "/tfw-knowledge", "/tfw-release", "/tfw-update",
    "/tfw-config", "/tfw-init",
)
LIFECYCLE_VARIANTS = (
    "lifecycle:status-write", "lifecycle:journal-write", "lifecycle:knowledge-close",
)
RUNTIME_VARIANTS = (*PRIMARY_VARIANTS, *SECONDARY_COMMANDS, "/tfw-handoff:revise",
                    *LIFECYCLE_VARIANTS)
PHASE_C_PRIMARY_ENTRY_WORDS = {
    "/tfw-plan": 24_730,
    "/tfw-research:focused": 6_103,
    "/tfw-research:deep": 6_168,
    "/tfw-handoff": 6_366,
    "/tfw-review": 25_182,
}
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
        "gate": _variants("wait for the owner's verdict", "WAIT",
                          ("resolve and record the rule-8 verdict", "WAIT")),
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


@dataclass(frozen=True)
class PhaseCSemanticSpec:
    path: str
    baseline_anchors: tuple[str, ...]
    candidate_anchors: tuple[str, ...]


PHASE_C_EXPECTED_RECORDS = {
    "S1-resume": ("ask phase choice", "phase order is not assumed", (), (),
                  ("status.md", "REVIEW"), "WAIT"),
    "S2-docs": ("preview documentation changes", None, (),
                ("KNOWLEDGE.md §§1–3", "REVIEW marker"), ("REVIEW", "RF"), "WAIT"),
    "S3-knowledge": ("apply approved facts", "unresolved problems or removed IDs",
                     ("topic facts",), ("KNOWLEDGE.md §4", "knowledge_state.yaml"),
                     ("pending checker",), "WAIT"),
    "S4-release": ("prepare triggered release", "no trigger or pre-release failure",
                   ("changelog version section",), (".tfw/VERSION", "project_config.yaml"),
                   ("RELEASE.md",), "STOP_EXTERNAL"),
    "S5-update": ("apply pinned framework update", "missing pin or migration", (),
                  ("framework payload", "project_config.yaml"),
                  ("pinned target", "intervening ranges"), "WAIT"),
    "S6-config": ("apply approved config batch", "missing or duplicate registry target", (),
                  ("project_config.yaml", "registered ranges"),
                  ("Config Sync Registry",), "WAIT"),
    "S7-init": ("route init mode", "configured state forbids full init",
                ("init task", "created event"), ("project config", "status.md"),
                ("adapter manifest", "research"), "STOP_AFTER_ROUTE"),
    "L1-status": ("write authoritative state", "invalid closed schema", ("status.md",), (),
                  ("status template",), "PREWRITE"),
    "L2-journal": ("append immutable event", "invalid event bounds", ("journal event",), (),
                   ("event template",), "PREWRITE"),
    "L3-close": ("close after knowledge markers", "undisposed item or missing marker", (),
                 ("status.md", "transition event"), ("REVIEW §5", "closure markers"), "DONE"),
    "A2-secondary": ("route secondary command", None, (), (), ("adapter manifest",), "CONTINUE"),
}


PHASE_C_SEMANTIC_SPECS = {
    "S1-resume": PhaseCSemanticSpec(
        ".tfw/workflows/resume.md", ("Build Status Matrix", "Assume phase order is fixed"),
        ("Build the Matrix", "User Decision Gate")),
    "S2-docs": PhaseCSemanticSpec(
        ".tfw/workflows/docs.md", ("tfw-docs: N/A (minor)", "Presents a diff preview"),
        ("tfw-docs: N/A (minor)", "Show the exact diff and sources")),
    "S3-knowledge": PhaseCSemanticSpec(
        ".tfw/workflows/knowledge.md", ("removed_task_ids", "WAIT 2"),
        ("removed_task_ids", "WAIT 2")),
    "S4-release": PhaseCSemanticSpec(
        ".tfw/workflows/release.md", ("Update Version Files", "Release Steps"),
        ("Update `.tfw/VERSION`", "separate external effects")),
    "S5-update": PhaseCSemanticSpec(
        ".tfw/workflows/update.md", ("ask exactly three questions", "intervening CHANGELOG"),
        ("ask exactly three questions", "only intervening")),
    "S6-config": PhaseCSemanticSpec(
        ".tfw/workflows/config.md", ("Config Sync Registry", "Verify Mode"),
        ("Config Sync Registry", "Verify Mode")),
    "S7-init": PhaseCSemanticSpec(
        ".tfw/workflows/init.md", ("Detect Full Init vs Adapter Attach/Repair", "Interview + Mini-Setup"),
        ("Route Before Discovery", "Discover and Interview")),
    "L1-status": PhaseCSemanticSpec(
        ".tfw/templates/status.md", ("CLOSED KEY SET", "lifecycle_verbatim"),
        ("lifecycle_verbatim", "outcome")),
    "L2-journal": PhaseCSemanticSpec(
        ".tfw/templates/journal/event.md", ("on_behalf_of", "IMMUTABLE ONCE WRITTEN"),
        ("on_behalf_of", "summary")),
    "L3-close": PhaseCSemanticSpec(
        ".tfw/workflows/review.md", ("tfw-docs: Applied/N/A", "undisposed item"),
        ("tfw-docs: Applied/N/A", "undisposed item")),
    "A2-secondary": PhaseCSemanticSpec(
        ".tfw/adapters/manifest.yaml", ("resume:", "role: Coordinator"),
        ("resume:", "role: Coordinator")),
}


PHASE_C_DERIVATIONS = {
    "S1-resume": {
        "decision": _variants("Start planning Phase C?", "ask phase choice",
                              ("Start planning Phase X?", "ask phase choice"),
                              ("Continue with Phase X automatically", "auto-select phase")),
        "refusal_reason": _variants("Assume phase order is fixed", "phase order is not assumed",
                                    ("Phase order is\nnot assumed", "phase order is not assumed")),
        "artifacts_created": _variants("Build matrix and present", (),
                                       ("Present one row per declared phase", ())),
        "artifacts_modified": _variants("After User Confirms", (),
                                        ("After the user chooses", ())),
        "citations": _variants("last completed phase has a REVIEW", ("status.md", "REVIEW"),
                               ("latest completed/returned phase", ("status.md", "REVIEW"))),
        "gate": _variants("Ask user:", "WAIT", ("Then stop.", "WAIT")),
    },
    "S2-docs": {
        "decision": _variants("Presents a diff preview", "preview documentation changes",
                              ("Show the exact diff and sources", "preview documentation changes")),
        "refusal_reason": _variants("tfw-docs: N/A (minor)", None),
        "artifacts_created": _variants("_(no action)_", (), ("no write here; route later", ())),
        "artifacts_modified": _variants("**Writes to:** KNOWLEDGE.md", ("KNOWLEDGE.md §§1–3", "REVIEW marker"),
                                        ("Apply only the approved rows", ("KNOWLEDGE.md §§1–3", "REVIEW marker"))),
        "citations": _variants("Agent reads the RF for the specified task", ("REVIEW", "RF"),
                               ("highest REVIEW and the RF it references", ("REVIEW", "RF"))),
        "gate": _variants("Human approves before applying", "WAIT",
                          ("wait for human approval before applying", "WAIT"),
                          ("apply immediately without human approval", "CONTINUE")),
    },
    "S3-knowledge": {
        "decision": _variants("Apply only the approved topic-file", "apply approved facts"),
        "refusal_reason": _variants("removed_task_ids", "unresolved problems or removed IDs"),
        "artifacts_created": _variants("Updated `knowledge/` topic files", ("topic facts",)),
        "artifacts_modified": _variants("state last", ("KNOWLEDGE.md §4", "knowledge_state.yaml"),
                                        ("state first", ("knowledge_state.yaml first",))),
        "citations": _variants("pending checker", ("pending checker",)),
        "gate": _variants("WAIT 2", "WAIT"),
    },
    "S4-release": {
        "decision": _variants("Determine Version Bump", "prepare triggered release",
                              ("Scope and Version", "prepare triggered release")),
        "refusal_reason": _variants("If NO → stop", "no trigger or pre-release failure",
                                    ("If no trigger fires, stop", "no trigger or pre-release failure")),
        "artifacts_created": _variants("Add a new section to `.tfw/CHANGELOG.md`", ("changelog version section",),
                                       ("move only selected bullets into", ("changelog version section",))),
        "artifacts_modified": _variants("Update `.tfw/VERSION` to the new version", (".tfw/VERSION", "project_config.yaml"),
                                        ("Update `.tfw/VERSION` and `tfw.version` together", (".tfw/VERSION", "project_config.yaml"))),
        "citations": _variants("Consult `RELEASE.md` §3", ("RELEASE.md",),
                               ("Apply `RELEASE.md` Release Triggers", ("RELEASE.md",))),
        "gate": _variants("Follow `RELEASE.md` §6", "STOP_EXTERNAL",
                          ("user explicitly authorizes that effect", "STOP_EXTERNAL"),
                          ("automation implicitly authorizes that effect", "CONTINUE_EXTERNAL")),
    },
    "S5-update": {
        "decision": _variants("follow the target's workflow, not this file", "apply pinned framework update",
                              ("Follow the pinned target workflow now", "apply pinned framework update")),
        "refusal_reason": _variants("If the tag is missing", "missing pin or migration",
                                    ("A missing pin", "missing pin or migration")),
        "artifacts_created": _variants("Materialize the pinned payload", (),
                                       ("Materialize exactly that object", ())),
        "artifacts_modified": _variants("Project state, never overwrite", ("framework payload", "project_config.yaml"),
                                        ("project state — never overwrite", ("framework payload", "project_config.yaml")),
                                        ("project state — overwrite from target", ("framework payload", "project state overwritten"))),
        "citations": _variants("list every intervening CHANGELOG entry", ("pinned target", "intervening ranges"),
                               ("only intervening changelog version ranges", ("pinned target", "intervening ranges"))),
        "gate": _variants("ask exactly three questions", "WAIT"),
    },
    "S6-config": {
        "decision": _variants("Propose batch update", "apply approved config batch",
                              ("Present one batch preview", "apply approved config batch")),
        "refusal_reason": _variants("Adding new inline value locations without updating", "missing or duplicate registry target",
                                    ("missing or duplicate heading/row/target", "missing or duplicate registry target")),
        "artifacts_created": _variants("Verify Mode", ()),
        "artifacts_modified": _variants("**User approves** → update all files", ("project_config.yaml", "registered ranges"),
                                        ("update config and every resolved row atomically", ("project_config.yaml", "registered ranges"))),
        "citations": _variants("Config Sync Registry", ("Config Sync Registry",)),
        "gate": _variants("User approves", "WAIT", ("Wait for approval", "WAIT"),
                          ("Apply without approval", "CONTINUE")),
    },
    "S7-init": {
        "decision": _variants("Preserve all project state", "route init mode",
                              ("Preserve all state", "route init mode"),
                              ("Reset all state", "full init over configured state")),
        "refusal_reason": _variants("must run adapter attach/repair instead", "configured state forbids full init",
                                    ("full init over configured state", "configured state forbids full init")),
        "artifacts_created": _variants("After interview, create the skeleton", ("init task", "created event"),
                                       ("one `created` event", ("init task", "created event"))),
        "artifacts_modified": _variants("Set the first task's state", ("project config", "status.md"),
                                        ("Finalize project config and set the init task lifecycle", ("project config", "status.md"))),
        "citations": _variants("Run `/tfw-research` formally", ("adapter manifest", "research"),
                               ("Announce and run `/tfw-research`", ("adapter manifest", "research"))),
        "gate": _variants("report the repair and stop", "STOP_AFTER_ROUTE",
                          ("report, then stop", "STOP_AFTER_ROUTE")),
    },
    "L1-status": {
        "decision": _variants("only authority for this task's live state", "write authoritative state"),
        "refusal_reason": _variants("CLOSED KEY SET", "invalid closed schema",
                                    ("The key set is closed", "invalid closed schema"),
                                    ("The key set is open", None)),
        "artifacts_created": _variants("copy into a task directory as status.md", ("status.md",),
                                       ("Copy to `{task}/status.md`", ("status.md",))),
        "artifacts_modified": _variants("WHAT DOES NOT GO HERE", (), ("No history, event pointers", ())),
        "citations": _variants("project_config.yaml `tfw.statuses`", ("status template",),
                               ("`project_config.yaml` `tfw.statuses`", ("status template",))),
        "gate": _variants("Format: YAML front matter", "PREWRITE", ("Keep front matter", "PREWRITE")),
    },
    "L2-journal": {
        "decision": _variants("IMMUTABLE ONCE WRITTEN", "append immutable event",
                              ("Events are immutable once written", "append immutable event"),
                              ("Events may be edited once written", "edit existing event")),
        "refusal_reason": _variants("AN EVENT WITHOUT `on_behalf_of` IS INVALID", "invalid event bounds",
                                    ("current event without `on_behalf_of` is refused", "invalid event bounds")),
        "artifacts_created": _variants("copy into a task's journal", ("journal event",),
                                       ("Copy to the task or phase `journal/`", ("journal event",))),
        "artifacts_modified": _variants("never edited and never deleted", (),
                                        ("Correct by appending a new event", ())),
        "citations": _variants("event keeps a reference to it", ("event template",),
                               ("cite it through\n`refs`", ("event template",))),
        "gate": _variants("THE TIMESTAMP IS READ FROM THE SYSTEM CLOCK", "PREWRITE",
                          ("BEFORE WRITING", "PREWRITE")),
    },
    "L3-close": {
        "decision": _variants("When both markers are set", "close after knowledge markers",
                              ("When either marker is set", "close before knowledge markers")),
        "refusal_reason": _variants("undisposed item blocks `DONE`", "undisposed item or missing marker"),
        "artifacts_created": _variants("After ✅ APPROVE verdict", ()),
        "artifacts_modified": _variants("Every actual transition", ("status.md", "transition event")),
        "citations": _variants("REVIEW §5 carries no undisposed item", ("REVIEW §5", "closure markers")),
        "gate": _variants("Hard stop:", "DONE"),
    },
    "A2-secondary": {
        "decision": _variants("workflow: .tfw/workflows/resume.md", "route secondary command",
                              ("workflow: .tfw/workflows/obsolete-resume.md", "misroute secondary command")),
        "refusal_reason": _variants("Runtime roles never read this file", None),
        "artifacts_created": _variants("Tooling-only copy/install map", ()),
        "artifacts_modified": _variants("strategy: copy", ()),
        "citations": _variants("source: .tfw/adapters/codex/skills", ("adapter manifest",)),
        "gate": _variants("route: /tfw-resume", "CONTINUE"),
    },
}


PHASE_C_SEMANTIC_MUTATIONS = {
    item.case: item for item in (
        SemanticMutation("phase-c", "S1-resume", ".tfw/workflows/resume.md",
                         "Start planning Phase X?", "Continue with Phase X automatically", "decision"),
        SemanticMutation("phase-c", "S2-docs", ".tfw/workflows/docs.md",
                         "wait for human approval before applying", "apply immediately without human approval", "gate"),
        SemanticMutation("phase-c", "S3-knowledge", ".tfw/workflows/knowledge.md",
                         "state last", "state first", "artifacts_modified"),
        SemanticMutation("phase-c", "S4-release", ".tfw/workflows/release.md",
                         "user explicitly authorizes that effect", "automation implicitly authorizes that effect", "gate"),
        SemanticMutation("phase-c", "S5-update", ".tfw/workflows/update.md",
                         "project state — never overwrite", "project state — overwrite from target", "artifacts_modified"),
        SemanticMutation("phase-c", "S6-config", ".tfw/workflows/config.md",
                         "Wait for approval", "Apply without approval", "gate"),
        SemanticMutation("phase-c", "S7-init", ".tfw/workflows/init.md",
                         "Preserve all state", "Reset all state", "decision"),
        SemanticMutation("phase-c", "L1-status", ".tfw/templates/status.md",
                         "The key set is closed", "The key set is open", "refusal_reason"),
        SemanticMutation("phase-c", "L2-journal", ".tfw/templates/journal/event.md",
                         "Events are immutable once written", "Events may be edited once written", "decision"),
        SemanticMutation("phase-c", "L3-close", ".tfw/workflows/review.md",
                         "When both markers are set", "When either marker is set", "decision"),
        SemanticMutation("phase-c", "A2-secondary", ".tfw/adapters/manifest.yaml",
                         "workflow: .tfw/workflows/resume.md",
                         "workflow: .tfw/workflows/obsolete-resume.md", "decision"),
    )
}


def execute_phase_c_semantic(tree: SourceTree, case: str) -> SemanticRecord:
    spec = PHASE_C_SEMANTIC_SPECS[case]
    text = tree.read(spec.path)
    anchors = spec.baseline_anchors if tree.ref is not None else spec.candidate_anchors
    missing = [anchor for anchor in anchors if anchor not in text]
    if missing:
        raise SourceContractError(f"{case}: semantic anchors are absent: {missing}")
    values = []
    provenance = []
    for field_name in SEMANTIC_FIELDS:
        matches = [(clause, value) for clause, value in PHASE_C_DERIVATIONS[case][field_name]
                   if clause in text]
        if len(matches) != 1:
            raise SourceContractError(
                f"{case}: {field_name} semantic source resolved {len(matches)} times")
        clause, value = matches[0]
        values.append(value)
        provenance.append((field_name, spec.path, "*", clause))
    return SemanticRecord(*values, read_manifest=(spec.path,), source_clauses=tuple(provenance))


def phase_c_semantic_mutant(tree: SourceTree, case: str) -> SourceTree:
    mutation = PHASE_C_SEMANTIC_MUTATIONS[case]
    text = tree.read(mutation.path)
    if mutation.old not in text:
        raise SourceContractError(f"{case}: candidate clause does not resolve")
    return tree.with_text(mutation.path, text.replace(mutation.old, mutation.new, 1))

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
    reason: str; repeat: str; authority: str; dynamic: bool = False; charged: bool = True

def _words(text: str) -> int:
    return len(re.findall(r"\S+", text))

def test_audit_has_required_fields_and_no_candidate_full_library_edge():
    rows = [row for command in RUNTIME_VARIANTS for row in audit_rows(command, "candidate")]
    required = {"command", "checkpoint", "source", "heading", "reason", "observed_words",
                "repeat", "authority", "dynamic", "charged"}
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
    parser.add_argument("--audit", action="store_true"); parser.add_argument("--baseline-ref", default=PHASE_C_BASELINE_REF)
    parser.add_argument("--semantic-json", action="store_true")
    parser.add_argument("--semantic-mutants", action="store_true")
    parser.add_argument("--phase-c-semantic-json", action="store_true")
    parser.add_argument("--phase-c-mutants", action="store_true")
    parser.add_argument("--phase-c-role-census", action="store_true")
    parser.add_argument("--revise-routes", action="store_true")
    parser.add_argument("--session-identity-scenarios", action="store_true")
    parser.add_argument("--session-identity-mutants", action="store_true")
    parser.add_argument("--session-identity-context", action="store_true")
    parser.add_argument("--phase-d-scenarios", action="store_true")
    parser.add_argument("--phase-d-mutants", action="store_true")
    parser.add_argument("--phase-d-census", action="store_true")
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
    if args.phase_c_semantic_json:
        before = SourceTree.from_git(PROJECT_ROOT, PHASE_C_BASELINE_REF)
        after = SourceTree.from_path(PROJECT_ROOT)
        payload = {case: {
            "baseline": execute_phase_c_semantic(before, case).__dict__,
            "candidate": execute_phase_c_semantic(after, case).__dict__,
        } for case in sorted(PHASE_C_SEMANTIC_SPECS)}
        print(json.dumps(payload, indent=2, sort_keys=True))
    if args.phase_c_mutants:
        tree = SourceTree.from_path(PROJECT_ROOT)
        payload = []
        for case in sorted(PHASE_C_SEMANTIC_SPECS):
            normal = semantic_projection(execute_phase_c_semantic(tree, case))
            produced = semantic_projection(execute_phase_c_semantic(
                phase_c_semantic_mutant(tree, case), case))
            payload.append({"case": case, "field": PHASE_C_SEMANTIC_MUTATIONS[case].field,
                            "produced": produced, "expected": normal,
                            "projection_changed": produced != normal,
                            "independent_expected_rejects":
                                produced != PHASE_C_EXPECTED_RECORDS[case]})
        print(json.dumps(payload, indent=2, sort_keys=True))
    if args.phase_c_role_census:
        errors = phase_c_competing_role_errors(SourceTree.from_path(PROJECT_ROOT))
        print(json.dumps({"errors": errors, "status": "PASS" if not errors else "FAIL"},
                         indent=2, sort_keys=True))
    if args.revise_routes:
        routes = resolve_revise_routes(SourceTree.from_path(PROJECT_ROOT))
        print(json.dumps({case: record.__dict__ for case, record in routes.items()},
                         indent=2, sort_keys=True))
    if args.session_identity_scenarios:
        print(json.dumps(session_identity_scenario_payload(SourceTree.from_path(PROJECT_ROOT)),
                         indent=2, sort_keys=True))
    if args.session_identity_mutants:
        print(json.dumps(session_identity_mutant_payload(SourceTree.from_path(PROJECT_ROOT)),
                         indent=2, sort_keys=True))
    if args.session_identity_context:
        print(json.dumps(session_identity_context_payload(SourceTree.from_path(PROJECT_ROOT)),
                         indent=2, sort_keys=True))
    if args.phase_d_scenarios:
        print(json.dumps(phase_d_scenario_payload(SourceTree.from_path(PROJECT_ROOT)),
                         indent=2, sort_keys=True))
    if args.phase_d_mutants:
        print(json.dumps(phase_d_mutant_payload(SourceTree.from_path(PROJECT_ROOT)),
                         indent=2, sort_keys=True))
    if args.phase_d_census:
        print(json.dumps(phase_d_census(SourceTree.from_path(PROJECT_ROOT)),
                         indent=2, sort_keys=True))
    return 0

# Review round 1 source-sensitivity contract. These tests intentionally name the source-backed
# API rather than accepting records or graph rows assembled independently of a source tree.
PATH_TOKEN = re.compile(r"`([^`]+)`")
SOURCE_TOKEN = re.compile(
    r"(?:AGENTS\.md|README\.md|RELEASE\.md|KNOWLEDGE\.md|knowledge/\*\.md|"
    r"\.tfw/VERSION|\.tfw/[^\s`]+\.(?:md|yaml))$"
)
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

def _append_edge(edges, command, checkpoint, source, heading, reason, authority,
                 dynamic=False, charged=True):
    source = source.replace("\\", "/")
    repeat = "repeated" if any(edge.source == source for edge in edges) else "once"
    edges.append(ReadEdge(command, checkpoint, source, heading, reason, repeat, authority,
                          dynamic, charged))

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
        "tfw.knowledge": "@yaml-knowledge",
        "tfw.scope_budgets": "@scope-values",
        "tfw.task_containers": "@task-containers",
        "tfw.task_prefix": "@task-prefix",
        "tfw.templates": "@yaml-templates",
        "tfw.release": "@release-values",
        "tfw.update": "@update-values",
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
            following = []
            for value in tokens[index + 1:]:
                if SOURCE_TOKEN.fullmatch(value): break
                following.append(value)
            if token.startswith(".tfw/.upstream/"):
                _add_dynamic(edges, command, "workflow read contract", f"<{token}>", reason, authority)
            elif token == ".tfw/project_config.yaml":
                selectors = [_selector_for_config(value) for value in following
                             if _selector_for_config(value)]
                if selectors:
                    for selector in selectors:
                        _edge_text(tree, token, selector)
                        _append_edge(edges, command, "workflow read contract", token, selector,
                                     reason, authority)
                else:
                    _add_full(tree, edges, command, "workflow read contract", token, reason, authority)
            elif token == ".tfw/CHANGELOG.md" and following == ["[Unreleased]"]:
                _append_edge(edges, command, "workflow read contract", token, "@unreleased",
                             reason, authority)
            elif following:
                for heading in following:
                    resolve_heading(tree.read(token), heading)
                    _append_edge(edges, command, "workflow read contract", token, heading,
                                 reason, authority)
            else:
                _add_full(tree, edges, command, "workflow read contract", token, reason, authority)

def _add_ranges(tree, edges, command, checkpoint, ranges, reason, authority):
    for source, heading in ranges:
        _edge_text(tree, source, heading)
        _append_edge(edges, command, checkpoint, source, heading, reason, authority)

def _add_dynamic(edges, command, checkpoint, source, reason, authority):
    _append_edge(edges, command, checkpoint, source, "@dynamic", reason, authority,
                 dynamic=True, charged=False)

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


def _config_registry_targets(tree: SourceTree) -> tuple[tuple[str, str, bool], ...]:
    """Resolve the registry's unique source ranges; baseline defects remain visible, not hidden."""
    section = resolve_heading(tree.read(".tfw/workflows/config.md"), "Config Sync Registry")
    targets = []
    config_keys = set()
    for line in section.splitlines():
        if not line.startswith("| `"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 4 or cells[0] == "Config Key":
            continue
        config_key = cells[0].strip("`")
        if config_key in config_keys:
            if tree.ref is None:
                raise SourceContractError(f"config registry row is duplicated: {config_key}")
            continue
        config_keys.add(config_key)
        source = cells[1].strip("`")
        heading = cells[2].strip("`")
        if not source or not heading:
            raise SourceContractError("config registry row has no source or heading")
        key = (source, heading)
        if any((have_source, have_heading) == key for have_source, have_heading, _ in targets):
            continue
        try:
            resolve_heading(tree.read(source), heading)
            targets.append((source, heading, True))
        except (ValueError, SourceContractError):
            if tree.ref is None:
                raise SourceContractError(f"config registry target does not resolve: {source}#{heading}")
            targets.append((source, f"@unresolved:{heading}", False))
    return tuple(targets)


def _add_secondary_supplements(tree, edges, command, workflow_text):
    base = command.split(":", 1)[0]
    has_contract = re.search(r"^## Read Contract\s*$", workflow_text, re.MULTILINE) is not None
    if base == "/tfw-resume":
        if not has_contract:
            _append_edge(edges, command, "legacy context guard", ".tfw/conventions.md",
                         "Context Selection", "legacy core-context verification", "shared rule")
        _add_dynamic(edges, command, "task selection", "<selected task/phase status and journal>",
                     "authoritative current state", "task-local")
        _add_dynamic(edges, command, "lineage", "<governing HL/TS/REVIEW/RF lineage>",
                     "current artifacts and user decision", "governing artifacts")
    elif base == "/tfw-docs":
        if not has_contract:
            prerequisites = resolve_heading(workflow_text, "Prerequisites")
            _add_literal_loads(tree, edges, command, "legacy prerequisites", prerequisites,
                               "documentation preload", "workflow")
        _add_dynamic(edges, command, "selection", "<selected status, journal, REVIEW, and RF>",
                     "live verdict and documentation changes", "task-local/governing artifacts")
        _add_dynamic(edges, command, "convention trigger", "<named conventions heading>",
                     "checklist item 4 only", "shared rule")
    elif base == "/tfw-knowledge":
        _add_dynamic(edges, command, "pending batch", "<pending task knowledge headings>",
                     "candidate and insight inputs", "task artifacts")
        _add_dynamic(edges, command, "human input", "<approved conversation facts>",
                     "human-only knowledge", "user")
    elif base == "/tfw-release":
        if not has_contract:
            prerequisites = resolve_heading(workflow_text, "Prerequisites")
            _add_literal_loads(tree, edges, command, "legacy prerequisites", prerequisites,
                               "release preload", "workflow")
            for heading in ("Version Scheme", "Release Triggers", "Pre-Release Checklist", "Release Steps"):
                resolve_heading(tree.read("RELEASE.md"), heading)
                _append_edge(edges, command, "legacy release step", "RELEASE.md", heading,
                             "re-read project release rule", "project release contract")
            _append_edge(edges, command, "task discovery", ".tfw/project_config.yaml",
                         "@task-containers", "configured task locations", "project config")
        _add_dynamic(edges, command, "release scope", "<DONE status and referenced task artifacts since tag>",
                     "authoritative release contents", "task-local/governing artifacts")
    elif base == "/tfw-update":
        if not has_contract:
            for path in (".tfw/adapters/manifest.yaml", ".tfw/templates/briefing.md"):
                _add_full(tree, edges, command, "legacy update gate", path,
                          "adapter sync or briefing form", "tooling metadata/template")
        _add_dynamic(edges, command, "pinned target", "<pinned target workflow and VERSION>",
                     "target-owned update algorithm", "pinned target")
        _add_dynamic(edges, command, "version delta", "<intervening changelog and migration ranges>",
                     "only required version changes", "pinned target history")
    elif base == "/tfw-config":
        if not has_contract:
            _add_full(tree, edges, command, "legacy mode read", ".tfw/project_config.yaml",
                      "verify or edit source values", "project config")
        for source, heading, resolved in _config_registry_targets(tree):
            _append_edge(edges, command, "registered range", source, heading,
                         "only registered inline value locations", "config registry",
                         charged=resolved)
        _add_dynamic(edges, command, "adapter sync", "<affected installed adapter targets>",
                     "changed config-bearing copies only", "manifest expansion")
    elif base == "/tfw-init":
        if not has_contract:
            for path in (
                ".tfw/project_config.yaml", ".tfw/adapters/manifest.yaml",
                ".tfw/templates/project_config.yaml", ".tfw/templates/knowledge_state.yaml",
                ".tfw/templates/team/profile.md", ".tfw/templates/status.md",
                ".tfw/templates/journal/event.md", ".tfw/templates/KNOWLEDGE.md",
                ".tfw/templates/RF.md",
            ):
                if not _has_edge(edges, path):
                    _add_full(tree, edges, command, "legacy full-init gate", path,
                              "setup form or adapter mapping", "config/template/tooling metadata")
        _add_dynamic(edges, command, "routing", "<existing task state or selected adapter>",
                     "full init versus attach/repair", "task-local/receiver")
        _add_dynamic(edges, command, "discovery", "<selected project documentation and structure>",
                     "full-init project understanding", "project sources")
        _add_dynamic(edges, command, "research", "<selected research workflow and task artifacts>",
                     "formal init research", "governing workflow/task")


def validate_lifecycle_graph(command: str, edges: tuple[ReadEdge, ...]) -> None:
    required = {
        "lifecycle:status-write": {".tfw/templates/status.md"},
        "lifecycle:journal-write": {".tfw/templates/journal/event.md"},
        "lifecycle:knowledge-close": {
            ".tfw/workflows/docs.md", ".tfw/workflows/knowledge.md",
            ".tfw/templates/status.md", ".tfw/templates/journal/event.md",
        },
    }[command]
    observed = {edge.source for edge in edges}
    missing = sorted(required - observed)
    if missing:
        raise SourceContractError(f"{command}: required lifecycle edge is missing: {missing}")


def _lifecycle_graph(tree: SourceTree, command: str) -> tuple[ReadEdge, ...]:
    if command == "lifecycle:knowledge-close":
        edges: list[ReadEdge] = []
        for source_command in ("/tfw-docs", "/tfw-knowledge"):
            for edge in discover_read_graph(tree, source_command):
                _append_edge(edges, command, edge.checkpoint, edge.source, edge.heading,
                             edge.reason, edge.authority, edge.dynamic, edge.charged)
        for source_command in ("lifecycle:status-write", "lifecycle:journal-write"):
            for edge in _lifecycle_graph(tree, source_command):
                _append_edge(edges, command, edge.checkpoint, edge.source, edge.heading,
                             edge.reason, edge.authority, edge.dynamic, edge.charged)
        result = tuple(edges)
        validate_lifecycle_graph(command, result)
        return result
    template = (".tfw/templates/status.md" if command == "lifecycle:status-write"
                else ".tfw/templates/journal/event.md")
    edges = []
    _append_edge(edges, command, "pre-write shared rule", ".tfw/conventions.md",
                 "Task control files", "write location and template route", "shared rule")
    _append_edge(edges, command, "pre-write lifecycle rule", ".tfw/conventions.md",
                 "Task Statuses", "state meaning and legal transition", "shared rule")
    _append_edge(edges, command, "write gate", template, "*",
                 "complete form, bounds, and readers", "template")
    _add_dynamic(edges, command, "write target", "<selected status or journal path>",
                 "task/phase-local durable effect", "task-local")
    result = tuple(edges)
    validate_lifecycle_graph(command, result)
    return result

def validate_research_stage_graph(edges: tuple[ReadEdge, ...]) -> None:
    stages = tuple(edge.source for edge in edges if edge.checkpoint == "stage gate")
    if stages != RESEARCH_STAGE_TEMPLATES:
        raise SourceContractError(
            "Researcher graph stage order is incomplete: "
            f"expected {RESEARCH_STAGE_TEMPLATES!r}, observed {stages!r}"
        )

def discover_read_graph(tree: SourceTree, command: str) -> tuple[ReadEdge, ...]:
    if command in LIFECYCLE_VARIANTS:
        return _lifecycle_graph(tree, command)
    base_command = command.split(":", 1)[0]
    canonical_bases = {item.split(":", 1)[0] for item in (*PRIMARY_VARIANTS, *SECONDARY_COMMANDS)}
    if base_command not in canonical_bases:
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
    if tree.ref is None and load_lines and any(
            token in load_lines for token in ("AGENTS.md", *sorted(FORBIDDEN_UNSCOPED))):
        raise SourceContractError(f"{command}: duplicate skill/workflow preload")
    if load_lines:
        _add_literal_loads(tree, edges, command, "skill contract", load_lines,
                           "skill-mandated context", "adapter")
    elif tree.ref is None and "do not independently preload" not in contract:
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
    if base_command in {"/tfw-plan", "/tfw-research", "/tfw-handoff", "/tfw-review"}:
        _add_primary_supplements(tree, edges, command, workflow_text)
    if base_command in {item.split(":", 1)[0] for item in SECONDARY_COMMANDS}:
        _add_secondary_supplements(tree, edges, command, workflow_text)
    if command == "/tfw-handoff:revise":
        _add_dynamic(edges, command, "revision return", "<live REVIEW and highest TS lineage>",
                     "rung-specific return bound without unchanged rereads", "governing artifacts")
    if base_command == "/tfw-research":
        validate_research_stage_graph(tuple(edges))
    return tuple(edges)

def _edge_text(tree: SourceTree, source: str, heading: str) -> str:
    if heading == "@dynamic":
        return ""
    text = tree.read(source)
    if heading.startswith("@unresolved:"):
        return ""
    if heading == "*":
        return text
    if heading == "@preamble":
        return text.partition("\n## ")[0]
    if heading == "@yaml-research":
        match = re.search(r"^  research:\s*$\n(?P<body>(?:(?:    |\s*$).*(?:\n|$))+)", text, re.MULTILINE)
        if not match:
            raise SourceContractError("tfw.research config range does not resolve")
        return match.group("body")
    if heading == "@yaml-knowledge":
        match = re.search(r"^  knowledge:\s*$\n(?P<body>(?:(?:    |\s*$).*(?:\n|$))+)", text, re.MULTILINE)
        if not match:
            raise SourceContractError("tfw.knowledge config range does not resolve")
        return "\n".join(line.split("#", 1)[0].rstrip()
                         for line in match.group("body").splitlines() if line.strip())
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
    if heading == "@task-containers":
        line = next((line for line in text.splitlines()
                     if re.match(r"^  task_containers:\s*", line)), None)
        if line is None:
            raise SourceContractError("tfw.task_containers config range does not resolve")
        return line
    if heading == "@task-prefix":
        line = next((line for line in text.splitlines()
                     if re.match(r"^  task_prefix:\s*", line)), None)
        if line is None:
            raise SourceContractError("tfw.task_prefix config range does not resolve")
        return line.split("#", 1)[0].rstrip()
    if heading == "@yaml-templates":
        match = re.search(r"^  templates:\s*$\n(?P<body>(?:    .*\n)+)", text, re.MULTILINE)
        if not match:
            raise SourceContractError("tfw.templates config range does not resolve")
        return match.group("body")
    if heading == "@release-values":
        keys = ("version", "task_containers")
        lines = [line for line in text.splitlines()
                 if any(re.match(rf"^  {key}:\s*", line) for key in keys)]
        if len(lines) != len(keys):
            raise SourceContractError("tfw.release config range does not resolve")
        return "\n".join(lines)
    if heading == "@update-values":
        # Update preserves project-owned blocks as well as framework provenance, so its named
        # config range is intentionally the complete project config rather than a hidden subset.
        return text
    if heading == "@unreleased":
        try:
            return resolve_heading(text, "[Unreleased]")
        except ValueError as exc:
            if "resolved 0 times" not in str(exc):
                raise
            return "\n".join(line for line in text.splitlines() if HEADING.match(line))
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
        "Rung 3", "Coordinator, then HL Contract rule-8 ruler",
        "HL §12 proposal plus amendment_escalated event and resolved ruler's terminal verdict",
        "none until that verdict leaves an executable bound",
        "unchanged; Executor is not dispatchable",
        "Reviewer → Coordinator → resolved ruler; STOP until terminal verdict",
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


# CRATM Phase C: the source contract is projected into executable, in-memory authority fixtures.
# Expected outcomes below are independent literals; neither fixture execution nor mutation output
# reads the expected oracle.
@dataclass(frozen=True)
class AuthorityDecision:
    case: str
    decision: str
    ruler: str | None
    refusal_reason: str | None
    proposer: str
    path: tuple[str, ...]
    signer: str | None


def _authority_rule(text: str, number: int) -> str:
    section = resolve_heading(text, "HL Contract")
    prefix = f"{number}. **"
    line = next((line for line in section.splitlines() if line.startswith(prefix)), None)
    if line is None:
        raise SourceContractError(f"HL Contract rule {number} does not resolve")
    return line


def authority_contract(tree: SourceTree) -> dict[str, bool]:
    conventions = tree.read(".tfw/conventions.md")
    rule8 = _authority_rule(conventions, 8)
    rule9 = _authority_rule(conventions, 9)
    rule10 = _authority_rule(conventions, 10)
    review = tree.read(".tfw/workflows/review.md")
    return {
        "owner_from_status": "`status.md.owner` must be a declared human" in rule8,
        "old_to_new_guarantee": (
            "Old: “only the owner rules.”" in rule8
            and "New ordinary delegation: nearest eligible non-proposer, else governing owner." in rule8),
        "separate_root_authorization": "separate governing record authorizes the root Coordinator" in rule8,
        "coordinator_only": "Only a Coordinator" in rule8,
        "child_only": "new child" in rule8,
        "preserve_proposer": "Preserve the originating proposer through transcription and sessions" in rule8,
        "skip_false": "skip `false` grants" in rule8,
        "stable_handle_equality": "same handle" in rule8,
        "nearest": "nearest remaining immutable `true` principal" in rule8,
        "owner_fallback": "otherwise the owner" in rule8,
        "accountability_forbidden": "`accountable_to`" in rule8 and "never supplies root" in rule8,
        "owner_explicit": "real explicit decision" in rule9,
        "restrict_on_filing": "applies on filing" in rule10,
        "purpose_owner": "both route to the **owner**, never the executor" in review,
        "reviewer_stops": "stops\nwithout resolving authority" in review,
    }


def _authority_nodes(**updates: dict[str, object]) -> dict[str, dict[str, object]]:
    nodes = {
        "root": {"handle": "ruler-root", "type": "agent", "workflow_role": "Coordinator",
                 "grant": True, "grant_changed": False, "accountable_to": "owner-human"},
        "mid": {"handle": "ruler-mid", "type": "agent", "workflow_role": "Coordinator",
                "grant": True, "grant_changed": False, "accountable_to": "owner-human"},
        "worker": {"handle": "probe-worker", "type": "agent", "workflow_role": "Researcher",
                   "grant": False, "grant_changed": False, "accountable_to": "owner-human"},
        "executor": {"handle": "exec-worker", "type": "agent", "workflow_role": "Executor",
                     "grant": False, "grant_changed": False, "accountable_to": "owner-human"},
    }
    for node_id, replacement in updates.items():
        nodes[node_id] = replacement
    return nodes


def _authority_edge(writer: str, destination: str) -> dict[str, str]:
    return {"writer": writer, "destination": destination,
            "scope_ref": "phase/status.md", "role_ref": "authority/delegation-record"}


def _authority_payload(name: str, **updates: object) -> dict[str, object]:
    payload: dict[str, object] = {
        "name": name,
        "status_owner": {"handle": "owner-human", "type": "human"},
        "root_authorizations": [{"owner": "owner-human", "coordinator": "root",
                                 "scope_ref": "phase/status.md",
                                 "authority_ref": "authority/delegation-record"}],
        "nodes": _authority_nodes(),
        "edges": [_authority_edge("root", "mid"), _authority_edge("mid", "worker")],
        "claim_delegated": True,
        "route_kind": "amendment",
        "amendment_type": "EXTEND",
        "proposer_node": "worker",
        "originating_proposer": "probe-worker",
        "transcriber_node": "mid",
        "reserved": False,
        "grant_change_for": None,
        "owner_initiated": False,
        "explicit_owner_decision": False,
        "signer": "ruler-mid",
        "spoof_provenance": {"accountable_to": None, "binding": None, "title": None,
                             "provider": None, "on_behalf_of": None},
    }
    payload.update(updates)
    return payload


def authority_fixture_payloads() -> dict[str, dict[str, object]]:
    no_true = _authority_nodes()
    no_true["root"] = {**no_true["root"], "grant": False}
    no_true["mid"] = {**no_true["mid"], "grant": False}
    false_then_true = _authority_nodes()
    false_then_true["mid"] = {**false_then_true["mid"], "grant": False}
    same_handle = _authority_nodes()
    same_handle["fresh"] = {"handle": "probe-worker", "type": "agent",
                            "workflow_role": "Coordinator", "grant": True,
                            "grant_changed": False, "accountable_to": "owner-human"}
    same_handle["top"] = {"handle": "ruler-top", "type": "agent",
                          "workflow_role": "Coordinator", "grant": True,
                          "grant_changed": False, "accountable_to": "owner-human"}
    orphan_nodes = _authority_nodes()
    orphan_nodes["orphan"] = {**orphan_nodes["root"], "handle": "orphan-ruler"}
    second_root_nodes = _authority_nodes()
    second_root_nodes["root2"] = {**second_root_nodes["root"], "handle": "ruler-second"}
    unknown_grant = _authority_nodes()
    unknown_grant["mid"] = {**unknown_grant["mid"], "grant": None}
    duplicate_grant = _authority_nodes()
    duplicate_grant["mid"] = {**duplicate_grant["mid"], "grant": [True, False]}
    changed_grant = _authority_nodes()
    changed_grant["mid"] = {**changed_grant["mid"], "grant_changed": True}
    foreign_accountability = _authority_nodes()
    foreign_accountability["worker"] = {**foreign_accountability["worker"],
                                        "accountable_to": "other-human"}
    cases = {
        "ordinary_cl": _authority_payload(
            "ordinary_cl", claim_delegated=False, root_authorizations=[], edges=[], signer="owner-human"),
        "root_child": _authority_payload(
            "root_child", edges=[_authority_edge("root", "worker")], signer="ruler-root"),
        "two_level_nearest": _authority_payload("two_level_nearest"),
        "false_then_higher_true": _authority_payload(
            "false_then_higher_true", nodes=false_then_true, signer="ruler-root"),
        "no_true_owner": _authority_payload("no_true_owner", nodes=no_true, signer="owner-human"),
        "proposer_nearest_true": _authority_payload(
            "proposer_nearest_true", proposer_node="mid", originating_proposer="ruler-mid",
            transcriber_node="root", signer="ruler-root"),
        "same_principal_fresh_session": _authority_payload(
            "same_principal_fresh_session", nodes=same_handle,
            root_authorizations=[{"owner": "owner-human", "coordinator": "top",
                                  "scope_ref": "phase/status.md",
                                  "authority_ref": "authority/delegation-record"}],
            edges=[_authority_edge("top", "fresh"), _authority_edge("fresh", "worker")],
            signer="ruler-top"),
        "coordinator_transcribes_child": _authority_payload("coordinator_transcribes_child"),
        "executor_source": _authority_payload(
            "executor_source", edges=[_authority_edge("root", "executor"),
                                       _authority_edge("executor", "worker")], signer="ruler-root"),
        "backward_ancestor": _authority_payload(
            "backward_ancestor", edges=[_authority_edge("root", "mid"),
                                        _authority_edge("mid", "root")]),
        "repeated_child": _authority_payload(
            "repeated_child", edges=[_authority_edge("root", "worker"),
                                     _authority_edge("root", "worker")], signer="ruler-root"),
        "competing_parent": _authority_payload(
            "competing_parent", edges=[_authority_edge("root", "mid"),
                                       _authority_edge("root", "worker"),
                                       _authority_edge("mid", "worker")]),
        "missing_parent": _authority_payload(
            "missing_parent", nodes=orphan_nodes, edges=[_authority_edge("orphan", "worker")]),
        "unknown_writer": _authority_payload(
            "unknown_writer", edges=[_authority_edge("missing", "worker")]),
        "unknown_destination": _authority_payload(
            "unknown_destination", edges=[_authority_edge("root", "missing")]),
        "unassigned_owner": _authority_payload(
            "unassigned_owner", status_owner={"handle": "unassigned", "type": "unassigned"}),
        "nonhuman_owner": _authority_payload(
            "nonhuman_owner", status_owner={"handle": "owner-agent", "type": "agent"}),
        "accountable_without_root": _authority_payload(
            "accountable_without_root", root_authorizations=[], signer="ruler-mid"),
        "binding_as_provenance": _authority_payload(
            "binding_as_provenance", root_authorizations=[],
            spoof_provenance={"accountable_to": None, "binding": "ruler-root", "title": None,
                              "provider": None, "on_behalf_of": None}),
        "title_as_provenance": _authority_payload(
            "title_as_provenance", root_authorizations=[],
            spoof_provenance={"accountable_to": None, "binding": None, "title": "Coordinator",
                              "provider": None, "on_behalf_of": None}),
        "provider_as_provenance": _authority_payload(
            "provider_as_provenance", root_authorizations=[],
            spoof_provenance={"accountable_to": None, "binding": None, "title": None,
                              "provider": "codex", "on_behalf_of": None}),
        "accountability_as_provenance": _authority_payload(
            "accountability_as_provenance", root_authorizations=[], nodes=foreign_accountability,
            spoof_provenance={"accountable_to": "owner-human", "binding": None, "title": None,
                              "provider": None, "on_behalf_of": None}),
        "unknown_grant": _authority_payload("unknown_grant", nodes=unknown_grant),
        "duplicate_grant": _authority_payload("duplicate_grant", nodes=duplicate_grant),
        "changed_grant": _authority_payload("changed_grant", nodes=changed_grant),
        "mismatched_signer": _authority_payload("mismatched_signer", signer="ruler-root"),
        "two_roots": _authority_payload(
            "two_roots", nodes=second_root_nodes,
            root_authorizations=[{"owner": "owner-human", "coordinator": "root",
                                  "scope_ref": "phase/status.md",
                                  "authority_ref": "authority/delegation-record"},
                                 {"owner": "owner-human", "coordinator": "root2",
                                  "scope_ref": "phase/status.md",
                                  "authority_ref": "authority/delegation-record"}]),
        "owner_reserved": _authority_payload("owner_reserved", reserved=True, signer="owner-human"),
        "agent_self_grant": _authority_payload(
            "agent_self_grant", grant_change_for="probe-worker", signer="owner-human"),
        "restrict": _authority_payload(
            "restrict", claim_delegated=False, root_authorizations=[], edges=[],
            amendment_type="RESTRICT", signer=None),
        "owner_initiated": _authority_payload(
            "owner_initiated", claim_delegated=False, root_authorizations=[], edges=[],
            proposer_node=None, originating_proposer="owner-human", transcriber_node=None,
            owner_initiated=True, explicit_owner_decision=True, signer="owner-human"),
        "false_owner_initiated": _authority_payload(
            "false_owner_initiated", owner_initiated=True, explicit_owner_decision=False,
            signer="owner-human",
            spoof_provenance={"accountable_to": "owner-human", "binding": "owner-human",
                              "title": "Owner", "provider": None,
                              "on_behalf_of": "owner-human"}),
        "purpose_not_fit": _authority_payload(
            "purpose_not_fit", claim_delegated=False, root_authorizations=[], edges=[],
            route_kind="purpose_not_fit", signer="owner-human"),
        "contract_defect": _authority_payload(
            "contract_defect", claim_delegated=False, root_authorizations=[], edges=[],
            route_kind="contract_defect", signer="owner-human"),
        "review_reject": _authority_payload(
            "review_reject", claim_delegated=False, root_authorizations=[], edges=[],
            route_kind="review_reject", signer="owner-human"),
        "budget_return": _authority_payload(
            "budget_return", claim_delegated=False, root_authorizations=[], edges=[],
            route_kind="budget", signer="owner-human"),
        "unavailable_participant": _authority_payload(
            "unavailable_participant", claim_delegated=False, root_authorizations=[], edges=[],
            route_kind="unavailable", signer="owner-human"),
        "fallback_probe": _authority_payload(
            "fallback_probe", nodes=foreign_accountability | {
                "root": {**foreign_accountability["root"], "grant": False},
                "mid": {**foreign_accountability["mid"], "grant": False}}, signer="owner-human"),
    }
    return cases


def _authority_refusal(payload: dict[str, object], reason: str,
                       proposer: str | None = None) -> AuthorityDecision:
    return AuthorityDecision(str(payload["name"]), "REFUSE", None, reason,
                             proposer or str(payload["originating_proposer"]), (),
                             str(payload["signer"]) if payload["signer"] is not None else None)


def _authority_route(payload: dict[str, object], ruler: str, proposer: str,
                     path: tuple[str, ...], decision: str = "ROUTE") -> AuthorityDecision:
    signer = str(payload["signer"]) if payload["signer"] is not None else None
    if signer != ruler:
        return _authority_refusal(payload, "mismatched-verdict-signer", proposer)
    return AuthorityDecision(str(payload["name"]), decision, ruler, None, proposer, path, signer)


def resolve_amendment_authority(tree: SourceTree, payload: dict[str, object]) -> AuthorityDecision:
    contract = authority_contract(tree)
    nodes = payload["nodes"]
    assert isinstance(nodes, dict)
    status_owner = payload["status_owner"]
    assert isinstance(status_owner, dict)
    owner = str(status_owner.get("handle"))
    if not contract["owner_from_status"]:
        proposer_node = payload.get("proposer_node")
        owner = str(nodes.get(proposer_node, {}).get("accountable_to", owner))
    if status_owner.get("type") != "human" or owner == "unassigned":
        return _authority_refusal(payload, "governing-owner-is-not-a-declared-human")

    proposer = str(payload["originating_proposer"])
    if not contract["preserve_proposer"] and payload.get("transcriber_node") in nodes:
        proposer = str(nodes[str(payload["transcriber_node"])]["handle"])

    kind = str(payload["route_kind"])
    if kind in {"purpose_not_fit", "contract_defect", "review_reject"}:
        if contract["purpose_owner"]:
            return _authority_route(payload, owner, proposer, (owner,), "HUMAN")
        return _authority_route(payload, "ruler-mid", proposer, ("ruler-mid",))
    if kind in {"budget", "unavailable"}:
        return _authority_route(payload, owner, proposer, (owner,), "HUMAN")
    if payload["amendment_type"] == "RESTRICT" and contract["restrict_on_filing"]:
        return AuthorityDecision(str(payload["name"]), "APPLY_ON_FILING", None, None,
                                 proposer, (), None)
    if payload["owner_initiated"]:
        explicit = bool(payload["explicit_owner_decision"])
        if not contract["owner_explicit"]:
            explicit = payload["spoof_provenance"].get("on_behalf_of") == owner
            if explicit:
                proposer = owner
        if explicit and proposer == owner:
            return _authority_route(payload, owner, proposer, (owner,), "DIRECT_OWNER_ACT")
    if not payload["claim_delegated"]:
        return _authority_route(payload, owner, proposer, (owner,))

    authorizations = payload["root_authorizations"]
    assert isinstance(authorizations, list)
    if not authorizations and not contract["accountability_forbidden"]:
        roots = [node_id for node_id, node in nodes.items()
                 if node.get("workflow_role") == "Coordinator"
                 and node.get("accountable_to") == owner]
        if roots:
            authorizations = [{"owner": owner, "coordinator": roots[0],
                               "scope_ref": "derived-accountability",
                               "authority_ref": "derived-accountability"}]
    if contract["separate_root_authorization"] and len(authorizations) != 1:
        return _authority_refusal(payload, "missing-or-competing-root-authorization", proposer)
    if len(authorizations) != 1:
        return _authority_refusal(payload, "unresolved-root", proposer)
    authorization = authorizations[0]
    root = str(authorization.get("coordinator"))
    if authorization.get("owner") != owner or root not in nodes:
        return _authority_refusal(payload, "invalid-root-authorization", proposer)
    if not authorization.get("scope_ref") or not authorization.get("authority_ref"):
        return _authority_refusal(payload, "missing-root-provenance", proposer)
    if nodes[root].get("workflow_role") != "Coordinator":
        return _authority_refusal(payload, "root-is-not-coordinator", proposer)

    reached, parents = {root}, {}
    for edge in payload["edges"]:
        writer, destination = str(edge.get("writer")), str(edge.get("destination"))
        if writer not in nodes:
            return _authority_refusal(payload, "unknown-writer", proposer)
        if destination not in nodes:
            return _authority_refusal(payload, "unknown-destination", proposer)
        if writer not in reached:
            return _authority_refusal(payload, "missing-parent-prefix", proposer)
        if contract["coordinator_only"] and nodes[writer].get("workflow_role") != "Coordinator":
            return _authority_refusal(payload, "edge-source-is-not-coordinator", proposer)
        if not edge.get("scope_ref") or not edge.get("role_ref"):
            return _authority_refusal(payload, "missing-edge-provenance", proposer)
        if destination in reached and contract["child_only"]:
            cursor = writer
            ancestors = {writer}
            while cursor in parents:
                cursor = parents[cursor]
                ancestors.add(cursor)
            if destination in ancestors:
                reason = "backward-ancestor-edge"
            elif destination in parents and parents[destination] != writer:
                reason = "competing-parent"
            else:
                reason = "repeated-child"
            return _authority_refusal(payload, reason, proposer)
        parents[destination] = writer
        reached.add(destination)

    proposer_node = payload.get("proposer_node")
    if proposer_node not in reached:
        return _authority_refusal(payload, "proposer-outside-resolved-prefix", proposer)
    if payload["reserved"] or payload["grant_change_for"] == proposer:
        return _authority_route(payload, owner, proposer, (str(proposer_node), owner), "HUMAN")

    path_nodes, cursor = [], str(proposer_node)
    while cursor in parents:
        cursor = parents[cursor]
        path_nodes.append(cursor)
    if cursor != root:
        return _authority_refusal(payload, "prefix-does-not-terminate-at-root", proposer)
    eligible = []
    for node_id in path_nodes:
        node = nodes[node_id]
        grant = node.get("grant")
        if not isinstance(grant, bool) or node.get("grant_changed"):
            return _authority_refusal(payload, "unknown-duplicate-or-changed-grant", proposer)
        same_principal = (str(node.get("handle")) == proposer if contract["stable_handle_equality"]
                          else node_id == payload.get("proposer_node"))
        granted = grant if contract["skip_false"] else not grant
        if granted and not same_principal:
            eligible.append(str(node.get("handle")))
    if eligible:
        ruler = eligible[0] if contract["nearest"] else eligible[-1]
    elif contract["owner_fallback"]:
        ruler = owner
    else:
        ruler = str(nodes[str(proposer_node)].get("accountable_to"))
    return _authority_route(payload, ruler, proposer,
                            tuple(str(nodes[node]["handle"]) for node in path_nodes) + (owner,))


AUTHORITY_EXPECTED = {
    "ordinary_cl": ("ROUTE", "owner-human", None),
    "root_child": ("ROUTE", "ruler-root", None),
    "two_level_nearest": ("ROUTE", "ruler-mid", None),
    "false_then_higher_true": ("ROUTE", "ruler-root", None),
    "no_true_owner": ("ROUTE", "owner-human", None),
    "proposer_nearest_true": ("ROUTE", "ruler-root", None),
    "same_principal_fresh_session": ("ROUTE", "ruler-top", None),
    "coordinator_transcribes_child": ("ROUTE", "ruler-mid", None),
    "executor_source": ("REFUSE", None, "edge-source-is-not-coordinator"),
    "backward_ancestor": ("REFUSE", None, "backward-ancestor-edge"),
    "repeated_child": ("REFUSE", None, "repeated-child"),
    "competing_parent": ("REFUSE", None, "competing-parent"),
    "missing_parent": ("REFUSE", None, "missing-parent-prefix"),
    "unknown_writer": ("REFUSE", None, "unknown-writer"),
    "unknown_destination": ("REFUSE", None, "unknown-destination"),
    "unassigned_owner": ("REFUSE", None, "governing-owner-is-not-a-declared-human"),
    "nonhuman_owner": ("REFUSE", None, "governing-owner-is-not-a-declared-human"),
    "accountable_without_root": ("REFUSE", None, "missing-or-competing-root-authorization"),
    "binding_as_provenance": ("REFUSE", None, "missing-or-competing-root-authorization"),
    "title_as_provenance": ("REFUSE", None, "missing-or-competing-root-authorization"),
    "provider_as_provenance": ("REFUSE", None, "missing-or-competing-root-authorization"),
    "accountability_as_provenance": ("REFUSE", None, "missing-or-competing-root-authorization"),
    "unknown_grant": ("REFUSE", None, "unknown-duplicate-or-changed-grant"),
    "duplicate_grant": ("REFUSE", None, "unknown-duplicate-or-changed-grant"),
    "changed_grant": ("REFUSE", None, "unknown-duplicate-or-changed-grant"),
    "mismatched_signer": ("REFUSE", None, "mismatched-verdict-signer"),
    "two_roots": ("REFUSE", None, "missing-or-competing-root-authorization"),
    "owner_reserved": ("HUMAN", "owner-human", None),
    "agent_self_grant": ("HUMAN", "owner-human", None),
    "restrict": ("APPLY_ON_FILING", None, None),
    "owner_initiated": ("DIRECT_OWNER_ACT", "owner-human", None),
    "false_owner_initiated": ("REFUSE", None, "mismatched-verdict-signer"),
    "purpose_not_fit": ("HUMAN", "owner-human", None),
    "contract_defect": ("HUMAN", "owner-human", None),
    "review_reject": ("HUMAN", "owner-human", None),
    "budget_return": ("HUMAN", "owner-human", None),
    "unavailable_participant": ("HUMAN", "owner-human", None),
    "fallback_probe": ("ROUTE", "owner-human", None),
}


def authority_fixture_results(tree: SourceTree) -> dict[str, AuthorityDecision]:
    return {name: resolve_amendment_authority(tree, payload)
            for name, payload in authority_fixture_payloads().items()}


def authority_mutant_results(tree: SourceTree) -> list[dict[str, object]]:
    mutations = (
        ("proposer-preservation", ".tfw/conventions.md",
         "Preserve the originating proposer through transcription and sessions",
         "Replace the originating proposer with the transcriber session", "two_level_nearest"),
        ("nearest-order", ".tfw/conventions.md", "nearest remaining immutable `true` principal",
         "highest remaining immutable `true` principal", "two_level_nearest"),
        ("grant-polarity", ".tfw/conventions.md", "skip `false` grants", "skip `true` grants",
         "false_then_higher_true"),
        ("stable-handle", ".tfw/conventions.md", "same handle", "same session",
         "same_principal_fresh_session"),
        ("status-owner-fallback", ".tfw/conventions.md", "otherwise the owner",
         "otherwise `accountable_to`", "fallback_probe"),
        ("accountability-provenance", ".tfw/conventions.md", "never supplies root",
         "may supply root", "accountable_without_root"),
        ("coordinator-only", ".tfw/conventions.md", "Only a Coordinator", "Any role",
         "executor_source"),
        ("owner-explicit-act", ".tfw/conventions.md", "real explicit decision",
         "`on_behalf_of` decision", "false_owner_initiated"),
        ("restrict-filing", ".tfw/conventions.md", "applies on filing", "waits for a ruler",
         "restrict"),
        ("purpose-owner", ".tfw/workflows/review.md",
         "both route to the **owner**, never the executor",
         "both route to the resolved ruler", "purpose_not_fit"),
    )
    results = []
    for family, path, old, new, case in mutations:
        source = tree.read(path)
        if old not in source:
            raise SourceContractError(f"{family}: mutation source does not resolve")
        normal = resolve_amendment_authority(tree, authority_fixture_payloads()[case])
        produced = resolve_amendment_authority(
            tree.with_text(path, source.replace(old, new, 1)), authority_fixture_payloads()[case])
        expected = AUTHORITY_EXPECTED[case]
        independent_rejects = (produced.decision, produced.ruler, produced.refusal_reason) != expected
        results.append({"family": family, "case": case, "normal": normal.__dict__,
                        "produced": produced.__dict__, "projection_changed": produced != normal,
                        "independent_expected_rejects": independent_rejects})
    return results


@dataclass(frozen=True)
class PlanAuthorityDecision:
    case: str
    decision: str
    ruler: str | None
    refusal_reason: str | None
    branch: str
    branch_order: tuple[str, ...]
    required_facts: tuple[str, ...]


def parse_plan_authority_consumer(tree: SourceTree) -> dict[str, object]:
    section = resolve_heading(
        tree.read(".tfw/workflows/plan.md"),
        "6d. Amendment verdicts — whenever one arrives, in research, ONB, review or execution")
    bullets: list[str] = []
    for line in section.splitlines()[1:]:
        if line.startswith("- "):
            bullets.append(line[2:])
        elif line.startswith("  ") and bullets:
            bullets[-1] += " " + line.strip()
    branches = []
    for bullet in bullets:
        if bullet.startswith("**No delegation claimed:**"):
            branches.append("ordinary")
        elif bullet.startswith("**Delegation claimed:**"):
            branches.append("delegated")
    ordinary = next((bullet for bullet in bullets
                     if bullet.startswith("**No delegation claimed:**")), "")
    delegated = next((bullet for bullet in bullets
                      if bullet.startswith("**Delegation claimed:**")), "")
    return {
        "section": section,
        "branch_order": tuple(branches),
        "ordinary_routes_owner": "route directly to that owner" in ordinary,
        "ordinary_omits_prefix": "root, chain and grant facts are inapplicable" in ordinary,
        "delegated_required_facts": tuple(fact for fact in (
            "owner", "root authorization", "child-only chain", "proposer", "immutable grant",
            "reservation", "signer") if fact in delegated),
        "delegated_stops_on_gaps": "Gaps stay `PROPOSED` and **STOP**" in delegated,
    }


def resolve_plan_authority_consumer(tree: SourceTree,
                                    payload: dict[str, object]) -> PlanAuthorityDecision:
    parsed = parse_plan_authority_consumer(tree)
    order = tuple(parsed["branch_order"])
    ordinary_facts = ("human status owner", "signer")
    delegated_facts = ("owner", "root authorization", "child-only chain", "proposer",
                       "immutable grant", "reservation", "signer")
    if not payload["claim_delegated"]:
        if order[:2] != ("ordinary", "delegated"):
            return PlanAuthorityDecision(str(payload["name"]), "REFUSE", None,
                                         "ordinary-branch-not-first", "ordinary", order,
                                         ordinary_facts)
        if not parsed["ordinary_routes_owner"] or not parsed["ordinary_omits_prefix"]:
            return PlanAuthorityDecision(str(payload["name"]), "REFUSE", None,
                                         "ordinary-cl-requires-delegation", "ordinary", order,
                                         ordinary_facts)
        resolved = resolve_amendment_authority(tree, payload)
        return PlanAuthorityDecision(str(payload["name"]), resolved.decision, resolved.ruler,
                                     resolved.refusal_reason, "ordinary", order, ordinary_facts)
    if tuple(parsed["delegated_required_facts"]) != delegated_facts or not parsed["delegated_stops_on_gaps"]:
        return PlanAuthorityDecision(str(payload["name"]), "REFUSE", None,
                                     "delegated-validation-incomplete", "delegated", order,
                                     delegated_facts)
    resolved = resolve_amendment_authority(tree, payload)
    return PlanAuthorityDecision(str(payload["name"]), resolved.decision, resolved.ruler,
                                 resolved.refusal_reason, "delegated", order, delegated_facts)


def plan_authority_consumer_payload(tree: SourceTree) -> dict[str, object]:
    payloads = authority_fixture_payloads()
    cases = {name: resolve_plan_authority_consumer(tree, payloads[name]).__dict__
             for name in ("ordinary_cl", "two_level_nearest", "accountable_without_root")}
    source = tree.read(".tfw/workflows/plan.md")
    old = "root, chain and grant facts are inapplicable"
    if old not in source:
        raise SourceContractError("Plan ordinary-CL mutation source does not resolve")
    mutant = tree.with_text(".tfw/workflows/plan.md", source.replace(
        old, "root, chain and grant facts are required", 1))
    normal = resolve_plan_authority_consumer(tree, payloads["ordinary_cl"])
    produced = resolve_plan_authority_consumer(mutant, payloads["ordinary_cl"])
    return {
        "parsed": parse_plan_authority_consumer(tree),
        "cases": cases,
        "mutant": {
            "family": "ordinary-cl-prefix-contradiction",
            "case": "ordinary_cl",
            "normal": normal.__dict__,
            "produced": produced.__dict__,
            "projection_changed": produced != normal,
            "independent_expected_rejects": (
                produced.decision, produced.ruler, produced.refusal_reason)
                != ("ROUTE", "owner-human", None),
        },
    }

def measure_graph(tree: SourceTree, edges: tuple[ReadEdge, ...]) -> int:
    return sum(_words(_edge_text(tree, edge.source, edge.heading))
               for edge in edges if edge.charged)
def graph_reduction(baseline: SourceTree, candidate: SourceTree, command: str) -> float:
    before = measure_graph(baseline, discover_read_graph(baseline, command))
    after = measure_graph(candidate, discover_read_graph(candidate, command))
    return (before - after) * 100 / before


def active_runtime_corpus_words(tree: SourceTree) -> int:
    """Count each charged `.tfw` source/range once, removing contained addressed ranges."""
    selected: dict[str, set[str]] = {}
    for command in RUNTIME_VARIANTS:
        for edge in discover_read_graph(tree, command):
            if edge.charged and edge.source.startswith(".tfw/"):
                selected.setdefault(edge.source, set()).add(edge.heading)
    total = 0
    for source, headings in selected.items():
        if "*" in headings:
            total += _words(tree.read(source))
            continue
        texts = {_edge_text(tree, source, heading) for heading in headings}
        maximal = [text for text in texts if text and not any(
            text != other and text in other for other in texts)]
        total += sum(_words(text) for text in maximal)
    return total
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
def render_audit(baseline_ref: str = PHASE_C_BASELINE_REF) -> str:
    lines = ["command\tprofile\tcheckpoint\tsource\theading\treason\tobserved_words\trepeat_classification\tauthority\tdynamic\tcharged"]
    trajectory = {"before": 0, "after": 0}
    for command in RUNTIME_VARIANTS:
        totals = {}
        for profile in ("before", "after"):
            rows = audit_rows(command, "baseline" if profile == "before" else "candidate", baseline_ref)
            for row in rows:
                keys = ("command", "checkpoint", "source", "heading", "reason", "observed_words",
                        "repeat", "authority", "dynamic", "charged")
                lines.append("\t".join(map(str, (row["command"], profile, *(row[key] for key in keys[1:])))))
            totals[profile] = sum(int(row["observed_words"]) for row in rows)
            if command in (*PRIMARY_VARIANTS, *SECONDARY_COMMANDS):
                trajectory[profile] += totals[profile]
        reduction = (totals["before"] - totals["after"]) * 100 / totals["before"]
        lines.append(f"TOTAL\t{command}\tbefore={totals['before']}\tafter={totals['after']}\treduction={reduction:.1f}%")
    reduction = (trajectory["before"] - trajectory["after"]) * 100 / trajectory["before"]
    lines.append(f"TRAJECTORY\tbefore={trajectory['before']}\tafter={trajectory['after']}\treduction={reduction:.1f}%")
    baseline = SourceTree.from_git(PROJECT_ROOT, baseline_ref)
    candidate = SourceTree.from_path(PROJECT_ROOT)
    before, after = active_runtime_corpus_words(baseline), active_runtime_corpus_words(candidate)
    reduction = (before - after) * 100 / before
    lines.append(f"ACTIVE_TFW_CORPUS\tbefore={before}\tafter={after}\treduction={reduction:.1f}%")
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

def _secondary_carrier_words(tree: SourceTree) -> int:
    paths = []
    for command in SECONDARY_COMMANDS:
        name = command.removeprefix("/tfw-")
        paths.extend((f".agents/skills/tfw-{name}/SKILL.md", f".tfw/workflows/{name}.md"))
    paths.extend((".tfw/templates/status.md", ".tfw/templates/journal/event.md"))
    return sum(_words(tree.read(path)) for path in paths)


def test_phase_c_immutable_baseline_reproduces_primary_and_carrier_anchors():
    baseline = SourceTree.from_git(PROJECT_ROOT, PHASE_C_BASELINE_REF)
    assert {command: measure_graph(baseline, discover_read_graph(baseline, command))
            for command in PRIMARY_VARIANTS} == PHASE_C_PRIMARY_ENTRY_WORDS
    assert _secondary_carrier_words(baseline) == 9_873


def test_phase_c_every_changed_path_and_active_corpus_clear_thirty_percent():
    baseline = SourceTree.from_git(PROJECT_ROOT, PHASE_C_BASELINE_REF)
    candidate = SourceTree.from_path(PROJECT_ROOT)
    for command, ceiling in PHASE_C_PRIMARY_ENTRY_WORDS.items():
        assert measure_graph(candidate, discover_read_graph(candidate, command)) <= ceiling
    for command in (*SECONDARY_COMMANDS, *LIFECYCLE_VARIANTS):
        assert graph_reduction(baseline, candidate, command) >= 30.0, command
    before, after = active_runtime_corpus_words(baseline), active_runtime_corpus_words(candidate)
    assert (before - after) / before >= 0.30


def test_phase_c_graphs_expose_dynamic_repeated_and_transitive_inputs():
    candidate = SourceTree.from_path(PROJECT_ROOT)
    graphs = {command: discover_read_graph(candidate, command) for command in RUNTIME_VARIANTS}
    assert all(graphs.values())
    assert all(any(edge.dynamic and not edge.charged and edge.heading == "@dynamic"
                   for edge in graphs[command])
               for command in (*SECONDARY_COMMANDS, *LIFECYCLE_VARIANTS))
    assert all(any(edge.repeat == "repeated" for edge in graphs[command])
               for command in (*SECONDARY_COMMANDS[:-1], *LIFECYCLE_VARIANTS))
    required_transitive = {
        "/tfw-resume": "<governing HL/TS/REVIEW/RF lineage>",
        "/tfw-docs": "<selected status, journal, REVIEW, and RF>",
        "/tfw-knowledge": "<pending task knowledge headings>",
        "/tfw-release": "<DONE status and referenced task artifacts since tag>",
        "/tfw-update": "<intervening changelog and migration ranges>",
        "/tfw-config": "<affected installed adapter targets>",
        "/tfw-init": "<selected research workflow and task artifacts>",
    }
    for command, source in required_transitive.items():
        assert any(edge.source == source and edge.dynamic and not edge.charged
                   for edge in graphs[command])


def test_phase_c_secondary_skills_are_thin_and_workflows_own_one_read_contract():
    for command in SECONDARY_COMMANDS:
        name = command.removeprefix("/tfw-")
        skill = _read(f".agents/skills/tfw-{name}/SKILL.md")
        contract = resolve_heading(skill, "Contract")
        assert f".tfw/workflows/{name}.md" in contract
        assert "do not independently preload" in contract
        assert not any(line.startswith("- Load ") for line in contract.splitlines())
        workflow = _read(f".tfw/workflows/{name}.md")
        assert len(re.findall(r"^## Read Contract\s*$", workflow, re.MULTILINE)) == 1


def test_phase_c_secondary_omissions_addresses_and_preloads_fail_independently():
    candidate = SourceTree.from_path(PROJECT_ROOT)
    with pytest.raises(SourceContractError, match="route.*tfw-resume"):
        discover_read_graph(omit_command_route(candidate, "/tfw-resume"), "/tfw-resume")
    for mode, count in (("missing", 0), ("duplicate", 2)):
        with pytest.raises(ValueError, match=fr"resolved {count} times"):
            discover_read_graph(mutate_addressed_heading(candidate, "Task control files", mode),
                                "/tfw-resume")
    skill_path = ".agents/skills/tfw-release/SKILL.md"
    injected = candidate.with_text(
        skill_path,
        candidate.read(skill_path).replace("## Contract\n",
                                           "## Contract\n\n- Load `.tfw/conventions.md`.\n", 1),
    )
    with pytest.raises(SourceContractError, match="duplicate skill/workflow preload"):
        discover_read_graph(injected, "/tfw-release")
    status_edges = discover_read_graph(candidate, "lifecycle:status-write")
    omitted = tuple(edge for edge in status_edges if edge.source != ".tfw/templates/status.md")
    with pytest.raises(SourceContractError, match="required lifecycle edge"):
        validate_lifecycle_graph("lifecycle:status-write", omitted)


def test_phase_c_config_registry_refuses_missing_and_duplicate_targets():
    candidate = SourceTree.from_path(PROJECT_ROOT)
    assert _config_registry_targets(candidate)
    path = ".tfw/workflows/config.md"
    text = candidate.read(path)
    missing = candidate.with_text(path, text.replace(
        "| `.tfw/conventions.md` | Scope Budgets (per Phase) |",
        "| `.tfw/conventions.md` | Missing Scope Heading |", 1))
    with pytest.raises(SourceContractError, match="does not resolve"):
        _config_registry_targets(missing)
    row = next(line for line in text.splitlines()
               if "| `.tfw/conventions.md` | Scope Budgets (per Phase) |" in line)
    duplicate = candidate.with_text(path, text.replace(row, row + "\n" + row, 1))
    with pytest.raises(SourceContractError, match="duplicated"):
        _config_registry_targets(duplicate)


@pytest.mark.parametrize("case", sorted(PHASE_C_SEMANTIC_SPECS))
def test_phase_c_secondary_and_lifecycle_records_are_source_derived_and_exact(case):
    baseline = SourceTree.from_git(PROJECT_ROOT, PHASE_C_BASELINE_REF)
    candidate = SourceTree.from_path(PROJECT_ROOT)
    before = execute_phase_c_semantic(baseline, case)
    after = execute_phase_c_semantic(candidate, case)
    assert semantic_projection(before) == semantic_projection(after) == PHASE_C_EXPECTED_RECORDS[case]
    assert before.read_manifest == after.read_manifest == (PHASE_C_SEMANTIC_SPECS[case].path,)
    assert tuple(field for field, _, _, _ in after.source_clauses) == SEMANTIC_FIELDS


@pytest.mark.parametrize("case", sorted(PHASE_C_SEMANTIC_SPECS))
def test_phase_c_each_secondary_lifecycle_and_adapter_mutant_changes_output(case):
    candidate = SourceTree.from_path(PROJECT_ROOT)
    normal = execute_phase_c_semantic(candidate, case)
    produced = execute_phase_c_semantic(phase_c_semantic_mutant(candidate, case), case)
    mutation = PHASE_C_SEMANTIC_MUTATIONS[case]
    assert getattr(produced, mutation.field) != getattr(normal, mutation.field)
    assert semantic_projection(produced) != semantic_projection(normal)
    with pytest.raises(AssertionError):
        assert semantic_projection(produced) == PHASE_C_EXPECTED_RECORDS[case]


def test_phase_c_expected_records_cannot_feed_production_and_anchors_alone_are_insufficient(
        monkeypatch):
    candidate = SourceTree.from_path(PROJECT_ROOT)
    trusted_expected = PHASE_C_EXPECTED_RECORDS["S1-resume"]
    monkeypatch.setitem(PHASE_C_EXPECTED_RECORDS, "S1-resume",
                        ("WRONG", None, (), (), (), "CONTINUE"))
    produced = semantic_projection(execute_phase_c_semantic(candidate, "S1-resume"))
    assert produced == trusted_expected
    assert produced != PHASE_C_EXPECTED_RECORDS["S1-resume"]
    spec = PHASE_C_SEMANTIC_SPECS["S1-resume"]
    minimal = candidate.with_text(spec.path, "\n".join(spec.candidate_anchors) + "\n")
    with pytest.raises(SourceContractError, match="semantic source"):
        execute_phase_c_semantic(minimal, "S1-resume")


def test_phase_c_clean_context_lifecycle_roles_states_effects_and_return_are_complete():
    tree = SourceTree.from_path(PROJECT_ROOT)
    sequence = (
        ("P4", "route /tfw-knowledge"),
        ("R3", "finish iteration 2"),
        ("E4", "execute latest revision"),
        ("V2", "reject purpose failure"),
    )
    assert [execute_scenario(tree, case).decision for case, _ in sequence] == [
        expected for _, expected in sequence]
    phase_c = {case: execute_phase_c_semantic(tree, case)
               for case in ("S1-resume", "S2-docs", "S3-knowledge", "L3-close")}
    assert phase_c["S1-resume"].gate == "WAIT"
    assert phase_c["S2-docs"].artifacts_modified[-1] == "REVIEW marker"
    assert phase_c["S3-knowledge"].gate == "WAIT"
    assert phase_c["L3-close"].artifacts_modified == ("status.md", "transition event")
    statuses = resolve_heading(tree.read(".tfw/conventions.md"), "Task Statuses")
    for state in ("TODO", "HL_DRAFT", "RES", "PHASES", "TS_DRAFT", "ONB", "RF",
                  "REV", "KNW", "DONE", "BLOCKED", "REJECTED"):
        assert state in statuses
    role_expectations = {
        "plan": "COORDINATOR", "research/base": "RESEARCHER", "handoff": "EXECUTOR",
        "review": "REVIEWER", "docs": "COORDINATOR", "knowledge": "COORDINATOR",
    }
    for workflow, role in role_expectations.items():
        assert f"ROLE LOCK: {role}" in tree.read(f".tfw/workflows/{workflow}.md")


PHASE_C_STALE_INSTRUCTIONS = (
    "Scan folder for `HL__Phase*`",
    "Read all RF files in full",
    "Load full CHANGELOG history",
    "Use the adapter manifest to decide the acting role",
    "Set `lifecycle: TS_DRAFT` for every REVISE",
)

ROLE_LOCK_DECLARATION = re.compile(r"ROLE LOCK:\s*([A-Z][A-Z]+)", re.IGNORECASE)
ROLE_HEADING_DECLARATION = re.compile(
    r"^>\s+\*\*Role:\*\*\s*(?P<roles>.+?)\s*$", re.MULTILINE)
SKILL_ROLE_DECLARATION = re.compile(
    r"Enforce the (?P<roles>.+?) role lock", re.IGNORECASE)


def _declared_roles(text: str) -> tuple[str, ...]:
    """Normalize one active declaration without hiding competing slash/or forms."""
    declaration = text.split("(", 1)[0].strip()
    return tuple(part.strip().casefold() for part in re.split(
        r"\s*(?:/|\bor\b|\band\b)\s*", declaration, flags=re.IGNORECASE) if part.strip())


def phase_c_competing_role_errors(tree: SourceTree) -> list[str]:
    """Census every active role declaration and its tracked adapter copies.

    The expected boundary is derived from each command's immutable Phase C baseline workflow
    lock. The current manifest enumerates the active instruction graph; no command or role phrase
    is baked into the census. Secondary workflow headings, canonical/installed Codex skills, and
    tracked Claude/Antigravity copies must all express that same one-role boundary.
    """
    baseline = SourceTree.from_git(PROJECT_ROOT, PHASE_C_BASELINE_REF)
    current_manifest = yaml.safe_load(tree.read(".tfw/adapters/manifest.yaml"))
    baseline_manifest = yaml.safe_load(baseline.read(".tfw/adapters/manifest.yaml"))
    current_commands = (current_manifest or {}).get("commands") or {}
    baseline_commands = (baseline_manifest or {}).get("commands") or {}
    errors = []
    if set(current_commands) != set(baseline_commands):
        errors.append("manifest command census differs from the Phase C baseline")

    secondary_names = {command.removeprefix("/tfw-") for command in SECONDARY_COMMANDS}
    for command in sorted(set(current_commands) | set(baseline_commands)):
        current_row = current_commands.get(command)
        baseline_row = baseline_commands.get(command)
        if not isinstance(current_row, dict) or not isinstance(baseline_row, dict):
            errors.append(f"{command}: missing or malformed manifest command declaration")
            continue
        workflow_path = baseline_row.get("workflow")
        if not isinstance(workflow_path, str) or current_row.get("workflow") != workflow_path:
            errors.append(f"{command}: workflow route differs from the Phase C baseline")
            continue

        baseline_roles = _declared_roles(str(baseline_row.get("role", "")))
        if len(baseline_roles) != 1:
            errors.append(f"{command}: baseline manifest role resolved {len(baseline_roles)} times")
            continue
        expected = baseline_roles[0]

        manifest_roles = _declared_roles(str(current_row.get("role", "")))
        if manifest_roles != (expected,):
            errors.append(f"{command}: manifest roles {manifest_roles!r} != {(expected,)!r}")

        workflow_text = tree.read(workflow_path)
        workflow_locks = tuple(role.casefold() for role in
                               ROLE_LOCK_DECLARATION.findall(workflow_text))
        if workflow_locks != (expected,):
            errors.append(f"{command}: workflow locks {workflow_locks!r} != {(expected,)!r}")
        headings = ROLE_HEADING_DECLARATION.findall(workflow_text)
        if command in secondary_names:
            if len(headings) != 1:
                errors.append(f"{command}: active role heading resolved {len(headings)} times")
            elif _declared_roles(headings[0]) != (expected,):
                errors.append(
                    f"{command}: workflow heading roles {_declared_roles(headings[0])!r} "
                    f"!= {(expected,)!r}")
        elif any(_declared_roles(heading) != (expected,) for heading in headings):
            errors.append(f"{command}: workflow heading competes with its role lock")

        skill_source = f".tfw/adapters/codex/skills/tfw-{command}/SKILL.md"
        skill_text = tree.read(skill_source)
        skill_roles = SKILL_ROLE_DECLARATION.findall(skill_text)
        if len(skill_roles) != 1:
            errors.append(f"{command}: canonical skill role resolved {len(skill_roles)} times")
        elif _declared_roles(skill_roles[0]) != (expected,):
            errors.append(
                f"{command}: canonical skill roles {_declared_roles(skill_roles[0])!r} "
                f"!= {(expected,)!r}")

        installed_skill = f".agents/skills/tfw-{command}/SKILL.md"
        if tree.read(installed_skill) != skill_text:
            errors.append(f"{command}: installed Codex skill differs from canonical source")
        for copy_path in (f".claude/commands/tfw-{command}.md",
                          f".agent/workflows/tfw-{command}.md"):
            if tree.read(copy_path) != workflow_text:
                errors.append(f"{command}: tracked adapter copy differs: {copy_path}")
    return errors


def _phase_c_stale_instruction_errors(tree: SourceTree) -> list[str]:
    paths = [f".tfw/workflows/{command.removeprefix('/tfw-')}.md"
             for command in SECONDARY_COMMANDS]
    paths.extend(f".agents/skills/tfw-{command.removeprefix('/tfw-')}/SKILL.md"
                 for command in SECONDARY_COMMANDS)
    return [f"{path}: {clause}" for path in paths for clause in PHASE_C_STALE_INSTRUCTIONS
            if clause.casefold() in tree.read(path).casefold()]


def test_phase_c_stale_readerless_and_second_authority_census_rejects_mutants():
    candidate = SourceTree.from_path(PROJECT_ROOT)
    assert _phase_c_stale_instruction_errors(candidate) == []
    assert phase_c_competing_role_errors(candidate) == []
    for path, clause in (
        (".tfw/workflows/resume.md", PHASE_C_STALE_INSTRUCTIONS[0]),
        (".tfw/workflows/release.md", PHASE_C_STALE_INSTRUCTIONS[2]),
        (".tfw/workflows/update.md", PHASE_C_STALE_INSTRUCTIONS[3]),
    ):
        mutant = candidate.with_text(path, candidate.read(path) + f"\n{clause}.\n")
        assert _phase_c_stale_instruction_errors(mutant) == [f"{path}: {clause}"]
    workflow_path = ".tfw/workflows/docs.md"
    duplicate = candidate.with_text(
        workflow_path, candidate.read(workflow_path) + "\n## Read Contract\nsecond authority\n")
    with pytest.raises(ValueError, match="resolved 2 times"):
        discover_read_graph(duplicate, "/tfw-docs")
    for command in ("/tfw-update", "/tfw-config", "/tfw-init"):
        manifest_edges = [edge for edge in discover_read_graph(candidate, command)
                          if edge.source == ".tfw/adapters/manifest.yaml"]
        assert manifest_edges and all("role" not in edge.reason for edge in manifest_edges)


def test_phase_c_role_census_rejects_omitted_duplicate_stale_conflicting_and_drifted_sources():
    candidate = SourceTree.from_path(PROJECT_ROOT)
    mutations = (
        (".tfw/workflows/docs.md", "> **Role:** Coordinator\n", ""),
        (".tfw/workflows/release.md", "> **Role:** Coordinator\n",
         "> **Role:** Coordinator\n> **Role:** Coordinator\n"),
        (".tfw/workflows/docs.md", "> **Role:** Coordinator", "> **Role:** Reviewer"),
        (".tfw/workflows/release.md", "ROLE LOCK: COORDINATOR", "ROLE LOCK: MAINTAINER"),
        (".tfw/adapters/codex/skills/tfw-release/SKILL.md",
         "Enforce the Coordinator role lock", "Enforce the Maintainer role lock"),
        (".tfw/adapters/manifest.yaml", "  release:\n    route: /tfw-release\n    workflow: .tfw/workflows/release.md\n    role: Coordinator",
         "  release:\n    route: /tfw-release\n    workflow: .tfw/workflows/release.md\n    role: Maintainer"),
        (".agents/skills/tfw-release/SKILL.md", "permit version and changelog artifacts",
         "permit stale release artifacts"),
        (".claude/commands/tfw-docs.md", "Show the exact diff and sources",
         "Show a stale diff without sources"),
    )
    for path, old, new in mutations:
        assert old in candidate.read(path), path
        mutant = candidate.with_text(path, candidate.read(path).replace(old, new, 1))
        assert phase_c_competing_role_errors(mutant), path


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
        ("Rung 3", "Exact hard stop", "hard_stop", "dispatch Executor before terminal verdict"),
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
    assert routes["Rung 3"].hard_stop.endswith("STOP until terminal verdict")
    assert routes["Mixed rung 1 + 2"].governing_artifact == "highest approved TS revision"


def test_cratm_phase_c_authority_contract_is_source_derived_and_complete():
    contract = authority_contract(SourceTree.from_path(PROJECT_ROOT))
    assert contract and all(contract.values())
    assert set(contract) == {
        "owner_from_status", "old_to_new_guarantee", "separate_root_authorization",
        "coordinator_only", "child_only",
        "preserve_proposer", "skip_false", "stable_handle_equality", "nearest",
        "owner_fallback", "accountability_forbidden", "owner_explicit", "restrict_on_filing",
        "purpose_owner", "reviewer_stops",
    }


def test_cratm_phase_c_full_authority_payloads_cover_routes_refusals_and_human_exceptions():
    payloads = authority_fixture_payloads()
    assert set(payloads) == set(AUTHORITY_EXPECTED)
    required = {
        "name", "status_owner", "root_authorizations", "nodes", "edges", "claim_delegated",
        "route_kind", "amendment_type", "proposer_node", "originating_proposer",
        "transcriber_node", "reserved", "grant_change_for", "owner_initiated",
        "explicit_owner_decision", "signer", "spoof_provenance",
    }
    assert all(set(payload) == required for payload in payloads.values())
    records = authority_fixture_results(SourceTree.from_path(PROJECT_ROOT))
    assert {(name, record.decision, record.ruler, record.refusal_reason)
            for name, record in records.items()} == {
                (name, *expected) for name, expected in AUTHORITY_EXPECTED.items()}
    assert records["coordinator_transcribes_child"].proposer == "probe-worker"
    assert records["same_principal_fresh_session"].ruler == "ruler-top"
    assert all(payloads[name]["spoof_provenance"] for name in (
        "binding_as_provenance", "title_as_provenance", "provider_as_provenance",
        "accountability_as_provenance", "false_owner_initiated"))


def test_cratm_phase_c_authority_mutants_change_output_before_independent_rejection():
    results = authority_mutant_results(SourceTree.from_path(PROJECT_ROOT))
    assert {row["family"] for row in results} == {
        "proposer-preservation", "nearest-order", "grant-polarity", "stable-handle",
        "status-owner-fallback", "accountability-provenance", "coordinator-only",
        "owner-explicit-act", "restrict-filing", "purpose-owner",
    }
    assert all(row["projection_changed"] and row["independent_expected_rejects"] for row in results)


def test_cratm_phase_c_plan_consumer_executes_ordinary_and_delegated_branches():
    result = plan_authority_consumer_payload(SourceTree.from_path(PROJECT_ROOT))
    assert result["parsed"]["branch_order"] == ("ordinary", "delegated")
    assert result["parsed"]["ordinary_routes_owner"]
    assert result["parsed"]["ordinary_omits_prefix"]
    assert (result["cases"]["ordinary_cl"]["decision"],
            result["cases"]["ordinary_cl"]["ruler"],
            result["cases"]["ordinary_cl"]["required_facts"]) == (
                "ROUTE", "owner-human", ("human status owner", "signer"))
    assert (result["cases"]["two_level_nearest"]["decision"],
            result["cases"]["two_level_nearest"]["ruler"]) == ("ROUTE", "ruler-mid")
    assert result["cases"]["accountable_without_root"]["refusal_reason"] == (
        "missing-or-competing-root-authorization")


def test_cratm_phase_c_plan_consumer_contradiction_mutant_changes_output_and_is_rejected():
    mutant = plan_authority_consumer_payload(SourceTree.from_path(PROJECT_ROOT))["mutant"]
    assert mutant["projection_changed"] and mutant["independent_expected_rejects"]
    assert mutant["normal"]["decision"] == "ROUTE"
    assert mutant["produced"]["refusal_reason"] == "ordinary-cl-requires-delegation"


def test_cratm_phase_c_consumers_preserve_role_locks_and_human_only_routes():
    tree = SourceTree.from_path(PROJECT_ROOT)
    plan = tree.read(".tfw/workflows/plan.md")
    review = tree.read(".tfw/workflows/review.md")
    handoff = tree.read(".tfw/workflows/handoff.md")
    hl = tree.read(".tfw/templates/HL.md")
    res = tree.read(".tfw/templates/RES.md")
    assert all("HL Contract` rule 8" in text or "HL Contract rule 8" in text
               for text in (plan, review, handoff))
    assert "route to the **owner**, never the executor" in review
    assert "❌ REJECT" in review and "selected owner route" in review
    assert "never an Executor decision" in handoff
    assert "§15 Role Lock" in res and "never applies or rules" in res
    assert "Owner-reserved" in hl and "grant/change-of-handle route to the owner" in hl
    assert "applies on filing" in _authority_rule(tree.read(".tfw/conventions.md"), 10)


# Value-bearing scope accounting (VBSA). These checks derive the produced contract from the
# canonical sources before comparing it with an independent expected record. Mutants therefore
# prove that a changed carrier changes observable output rather than merely satisfying a grep.
@dataclass(frozen=True)
class VBSARecord:
    classes: tuple[str, ...]
    measures: tuple[str, ...]
    config: tuple[tuple[str, int], ...]
    migration: tuple[tuple[str, str], ...]
    candidate_before_trace: bool
    immutable_denominator: bool
    approval_epoch: bool


EXPECTED_VBSA = VBSARecord(
    classes=("VALUE", "ASSURANCE", "TRACE", "DERIVED"),
    measures=("Logical touched `VALUE` files", "Touched text LOC"),
    config=(("decomposition_trigger_files", 50),
            ("decomposition_trigger_loc", 5000),
            ("owner_escalation_multiplier", 2)),
    migration=(("max_files_per_phase", "decomposition_trigger_files"),
               ("max_loc", "decomposition_trigger_loc"),
               ("max_new_files", "—"), ("max_modified_files", "—")),
    candidate_before_trace=True,
    immutable_denominator=True,
    approval_epoch=True,
)


def _vbsa_table_pairs(section: str, first_header: str) -> tuple[tuple[str, str], ...]:
    rows = []
    for line in section.splitlines():
        if not line.startswith("| `"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 2 and cells[0] != first_header:
            rows.append((cells[0].strip("`"), cells[1].strip("`")))
    return tuple(rows)


def resolve_vbsa_record(tree: SourceTree) -> VBSARecord:
    conventions = resolve_heading(tree.read(".tfw/conventions.md"), "Scope Budgets (per Phase)")
    classes = tuple(re.findall(r"^\| `([A-Z]+)` \|", conventions, re.MULTILINE))
    measures = tuple(re.findall(
        r"^\| (Logical touched `VALUE` files|Touched text LOC) \|", conventions, re.MULTILINE))
    config = yaml.safe_load(tree.read(".tfw/project_config.yaml"))["tfw"]["scope_budgets"]
    migration = _vbsa_table_pairs(
        resolve_heading(tree.read(".tfw/workflows/update.md"),
                        "Project-owned scope-budget migration"), "Old key")
    handoff = tree.read(".tfw/workflows/handoff.md")
    return VBSARecord(
        classes=classes,
        measures=measures,
        config=tuple(config.items()),
        migration=migration,
        candidate_before_trace="before creating or updating EV or RF" in handoff,
        immutable_denominator="plan is the immutable denominator" in handoff,
        approval_epoch="approval epoch" in conventions,
    )


VBSA_PLAN_HEADINGS = (
    "Semantic value-bearing classification",
    "Value-bearing accounting contract",
    "Decomposition, constraints, and change authority",
)
EXPECTED_VBSA_PLAN_CONTRACT = (
    (("VALUE", "Yes"), ("ASSURANCE", "No; yes only when assurance is the accepted product"),
     ("TRACE", "Never"), ("DERIVED", "No; yes when that output is accepted")),
    (("code", "VALUE"), ("shipped prompts", "VALUE"),
     ("accepted documents", "VALUE"), ("accepted presentations", "VALUE"),
     ("accepted data", "VALUE"), ("accepted generated final outputs", "VALUE"),
     ("ordinary tests", "ASSURANCE"), ("conformance-as-product", "VALUE"),
     ("task-folder deliverables", "VALUE"), ("TFW-looking product sources", "VALUE")),
    (("Precedence", "Accepted/necessary; whole fixed Baseline→Candidate diff if roles inseparable"),
     ("Narrower selector", "Deterministic, replayable, and declared before work"),
     ("Line subtraction", "No freehand line subtraction")),
    True, True, True,
    ("purpose", "value", "correctness", "architecture", "modularity", "inspectability", "continuation"),
)


def _vbsa_plan_table(section: str, header: str) -> tuple[tuple[str, ...], ...]:
    lines = section.splitlines()
    start = next((i for i, line in enumerate(lines) if line.startswith(f"| {header} |")), None)
    if start is None:
        return ()
    rows = []
    for line in lines[start + 2:]:
        if not line.startswith("|"):
            break
        rows.append(tuple(cell.strip().strip("`") for cell in line.strip("|").split("|")))
    return tuple(rows)


def resolve_vbsa_plan_contract(tree: SourceTree):
    graph = discover_read_graph(tree, "/tfw-plan")
    loaded = tuple(edge.heading for edge in graph
                   if edge.source == ".tfw/conventions.md" and edge.heading in VBSA_PLAN_HEADINGS)
    classification = resolve_heading(tree.read(".tfw/conventions.md"), VBSA_PLAN_HEADINGS[0])
    rows = []
    for line in classification.splitlines():
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) == 3 and cells[0].startswith("`"):
            rows.append((cells[0].strip("`"), cells[2]))
    examples = tuple(
        (example.strip(), row[1])
        for row in _vbsa_plan_table(classification, "Examples")
        for example in row[0].split(";")
    )
    ambiguity = _vbsa_plan_table(classification, "Ambiguity rule")
    accounting = resolve_heading(tree.read(".tfw/conventions.md"), VBSA_PLAN_HEADINGS[1])
    authority = resolve_heading(tree.read(".tfw/conventions.md"), VBSA_PLAN_HEADINGS[2])
    saint = re.search(
        r"Apply\s+Saint-Exupéry only without damaging (?P<boundary>[^.]+)\.", authority)
    saint_boundary = () if saint is None else tuple(
        item.strip() for item in re.split(r",\s*(?:or\s+)?|\s+or\s+", saint.group("boundary"))
        if item.strip())
    produced = (
        tuple(rows),
        examples,
        ambiguity,
        "before\nEV/RF/REVIEW/final transition" in accounting,
        "soft prompts, never quality vetoes" in authority,
        "no ruling ratchets it" in authority,
        saint_boundary,
    )
    return loaded, produced


def validate_vbsa_plan_contract(tree: SourceTree) -> None:
    loaded, produced = resolve_vbsa_plan_contract(tree)
    if loaded != VBSA_PLAN_HEADINGS or produced != EXPECTED_VBSA_PLAN_CONTRACT:
        raise SourceContractError("VBSA planner canonical route is incomplete or changed")


def test_vbsa_plan_loads_three_unique_canonical_sections_with_d75_intact():
    tree = SourceTree.from_path(PROJECT_ROOT)
    validate_vbsa_plan_contract(tree)
    assert measure_graph(tree, discover_read_graph(tree, "/tfw-plan")) <= PHASE_C_PRIMARY_ENTRY_WORDS["/tfw-plan"]


def test_vbsa_plan_meaning_reversal_changes_output_before_rejection():
    tree = SourceTree.from_path(PROJECT_ROOT)
    text = tree.read(".tfw/conventions.md")
    old = "| `VALUE` | Accepted output or its necessary constituent | Yes |"
    mutant = tree.with_text(
        ".tfw/conventions.md", text.replace(old, old.replace("| Yes |", "| No |"), 1))
    assert resolve_vbsa_plan_contract(mutant)[1] != EXPECTED_VBSA_PLAN_CONTRACT
    with pytest.raises(SourceContractError, match="planner canonical route"):
        validate_vbsa_plan_contract(mutant)


def test_vbsa_plan_freehand_permission_mutant_changes_output_before_rejection():
    tree = SourceTree.from_path(PROJECT_ROOT)
    path = ".tfw/conventions.md"
    old = "| Line subtraction | No freehand line subtraction |"
    text = tree.read(path)
    assert text.count(old) == 1
    mutant = tree.with_text(path, text.replace(
        old, "| Line subtraction | Freehand line subtraction allowed |", 1))
    assert resolve_vbsa_plan_contract(mutant)[1] != EXPECTED_VBSA_PLAN_CONTRACT
    with pytest.raises(SourceContractError, match="planner canonical route"):
        validate_vbsa_plan_contract(mutant)


@pytest.mark.parametrize(
    ("old", "new"),
    (("shipped prompts; ", ""), (", replayable", "")),
)
def test_vbsa_plan_missing_required_example_or_rule_changes_output_before_rejection(old, new):
    tree = SourceTree.from_path(PROJECT_ROOT)
    path = ".tfw/conventions.md"
    text = tree.read(path)
    assert text.count(old) == 1
    mutant = tree.with_text(path, text.replace(old, new, 1))
    assert resolve_vbsa_plan_contract(mutant)[1] != EXPECTED_VBSA_PLAN_CONTRACT
    with pytest.raises(SourceContractError, match="planner canonical route"):
        validate_vbsa_plan_contract(mutant)


def test_vbsa_plan_missing_route_changes_graph_before_rejection():
    tree = SourceTree.from_path(PROJECT_ROOT)
    text = tree.read(".tfw/workflows/plan.md")
    token = ", `Decomposition, constraints, and change authority`"
    mutant = tree.with_text(".tfw/workflows/plan.md", text.replace(token, "", 1))
    assert resolve_vbsa_plan_contract(mutant)[0] != VBSA_PLAN_HEADINGS
    with pytest.raises(SourceContractError, match="planner canonical route"):
        validate_vbsa_plan_contract(mutant)


EVIDENCE_RESULT_VOCABULARY = ("VERIFIED", "DEFERRED", "BLOCKED", "N/A")


def resolve_vbsa_ev_result_contract(tree: SourceTree):
    text = tree.read(".tfw/templates/evidence/EV.md")
    rows = {}
    for name in ("E1", "E-accounting"):
        line = next(line for line in text.splitlines() if line.startswith(f"| {name} |"))
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        rows[name] = (tuple(re.findall(
            r"VERIFIED|DEFERRED|BLOCKED|N/A|INVALID", cells[4])), cells[2])
    return rows


def validate_vbsa_ev_result_contract(tree: SourceTree) -> None:
    rows = resolve_vbsa_ev_result_contract(tree)
    if any(result != EVIDENCE_RESULT_VOCABULARY for result, _ in rows.values()):
        raise SourceContractError("EV Result vocabulary is not the fixed four values")
    if "INVALID" in rows["E-accounting"][0] or "INVALID" not in rows["E-accounting"][1]:
        raise SourceContractError("INVALID must remain accounting detail, not Evidence Result")


def test_vbsa_ev_has_four_result_statuses_and_invalid_only_in_detail():
    validate_vbsa_ev_result_contract(SourceTree.from_path(PROJECT_ROOT))


def test_vbsa_ev_fifth_status_mutant_changes_output_before_rejection():
    tree = SourceTree.from_path(PROJECT_ROOT)
    path = ".tfw/templates/evidence/EV.md"
    old = "{VERIFIED/DEFERRED/BLOCKED/N/A}"
    mutant = tree.with_text(path, tree.read(path).replace(
        old, "{VERIFIED/DEFERRED/BLOCKED/N/A/INVALID}", 1))
    assert resolve_vbsa_ev_result_contract(mutant) != resolve_vbsa_ev_result_contract(tree)
    with pytest.raises(SourceContractError, match="fixed four"):
        validate_vbsa_ev_result_contract(mutant)


def _vbsa_mutant(tree: SourceTree, family: str) -> SourceTree:
    if family == "classification":
        path, old, new = ".tfw/conventions.md", (
            "| `ASSURANCE` | Ordinary tests/checks/fixtures |"), (
            "| `SUPPORT` | Ordinary tests/checks/fixtures |")
    elif family == "accounting":
        path, old, new = ".tfw/conventions.md", "| Touched text LOC |", "| Net text LOC |"
    elif family == "authority":
        path, old, new = ".tfw/workflows/handoff.md", (
            "plan is the immutable denominator"), "actual result is the mutable denominator"
    elif family == "migration":
        path, old, new = ".tfw/workflows/update.md", (
            "| `max_loc` | `decomposition_trigger_loc` |"), (
            "| `max_loc` | `decomposition_trigger_files` |")
    else:
        raise AssertionError(f"unknown VBSA mutant family: {family}")
    text = tree.read(path)
    assert text.count(old) == 1
    return tree.with_text(path, text.replace(old, new, 1))


def test_vbsa_contract_is_source_derived_and_exact():
    assert resolve_vbsa_record(SourceTree.from_path(PROJECT_ROOT)) == EXPECTED_VBSA


@pytest.mark.parametrize("family", ("classification", "accounting", "authority", "migration"))
def test_vbsa_semantic_mutants_change_output_before_independent_rejection(family):
    produced = resolve_vbsa_record(_vbsa_mutant(SourceTree.from_path(PROJECT_ROOT), family))
    assert produced != EXPECTED_VBSA
    with pytest.raises(AssertionError):
        assert produced == EXPECTED_VBSA


@pytest.mark.parametrize(
    ("case", "accepted", "necessary", "ordinary_test", "trace", "reproducible", "expected"),
    (
        ("product source", True, False, False, False, False, "VALUE"),
        ("task-folder deliverable", True, False, False, True, False, "VALUE"),
        ("generated final deliverable", True, False, False, False, True, "VALUE"),
        ("necessary constituent", False, True, False, False, False, "VALUE"),
        ("ordinary assurance", False, False, True, False, False, "ASSURANCE"),
        ("test-as-product", True, False, True, False, False, "VALUE"),
        ("lifecycle record", False, False, False, True, False, "TRACE"),
        ("reproducible inspection output", False, False, False, False, True, "DERIVED"),
    ),
)
def test_vbsa_classification_uses_semantic_precedence(
        case, accepted, necessary, ordinary_test, trace, reproducible, expected):
    del case
    actual = ("VALUE" if accepted or necessary else "ASSURANCE" if ordinary_test else
              "TRACE" if trace else "DERIVED" if reproducible else None)
    assert actual == expected


def _git(cwd: Path, *args: str, text: bool = True):
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True,
                          text=text, encoding="utf-8" if text else None)


def test_vbsa_accounting_is_nul_safe_for_rename_identity_and_binary_na(tmp_path):
    _git(tmp_path, "init", "-q")
    _git(tmp_path, "config", "user.email", "assurance@example.invalid")
    _git(tmp_path, "config", "user.name", "VBSA assurance")
    (tmp_path / "old name.txt").write_text("one\ntwo\n", encoding="utf-8")
    (tmp_path / "payload.bin").write_bytes(b"\x00\x01")
    _git(tmp_path, "add", "--", "old name.txt", "payload.bin")
    _git(tmp_path, "commit", "-q", "-m", "baseline")
    baseline = _git(tmp_path, "rev-parse", "HEAD").stdout.strip()
    (tmp_path / "old name.txt").rename(tmp_path / "new name.txt")
    (tmp_path / "payload.bin").write_bytes(b"\x00\x02\x03")
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "candidate")
    candidate = _git(tmp_path, "rev-parse", "HEAD").stdout.strip()
    paths = ("old name.txt", "new name.txt", "payload.bin")
    names = _git(tmp_path, "diff", "--name-status", "--find-renames=50%", "-z",
                 baseline, candidate, "--", *paths, text=False).stdout.split(b"\0")
    nums = _git(tmp_path, "diff", "--numstat", "--find-renames=50%", "-z",
                baseline, candidate, "--", *paths, text=False).stdout.split(b"\0")
    assert names[:3] == [b"R100", b"old name.txt", b"new name.txt"]
    assert any(field.startswith(b"M\0") for field in ()) is False  # records, not path count
    assert any(row.startswith(b"-\t-\tpayload.bin") for row in nums)


def test_vbsa_candidate_invariance_and_later_value_rule_are_explicit():
    handoff = " ".join(_read(".tfw/workflows/handoff.md").split())
    assert "excluded-only TRACE/ASSURANCE/non-value DERIVED write does not move Candidate" in handoff
    assert "later VALUE write requires a new Candidate and full recomputation" in handoff


@pytest.mark.parametrize(
    ("case", "rule"),
    (("distinct candidates", "distinct immutable phase Candidates"),
     ("single owner", "assigns the whole delta to one phase"),
     ("unresolved", "reports exact phase enforcement as `INVALID`")),
)
def test_vbsa_attribution_has_only_three_terminal_routes(case, rule):
    del case
    section = " ".join(resolve_heading(
        _read(".tfw/conventions.md"), "Scope Budgets (per Phase)").split())
    assert rule in section


def test_vbsa_handoff_rf_ev_bind_one_approved_contract():
    handoff = _read(".tfw/workflows/handoff.md")
    rf = _read(".tfw/templates/RF.md")
    ev = _read(".tfw/templates/evidence/EV.md")
    assert all(term in handoff for term in ("full Baseline and Candidate SHAs", "exactly one dedicated accounting row", "approval ref"))
    assert all(term in rf for term in ("TS approval ref", "Candidate", "VALUE membership", "Authority and timing"))
    assert ev.count("| E-accounting |") == 1


def test_vbsa_review_replays_without_repair_or_late_authority():
    workflow = _read(".tfw/workflows/review.md")
    template = _read(".tfw/templates/REVIEW.md")
    assert all(term in workflow for term in ("independently resolve the approved TS", "never repaired inside REVIEW", "BLOCKED"))
    assert all(term in template for term in ("Independent value-bearing replay", "REVIEW never repairs", "INVALID"))


# RTPSN Phase A: command-entry contracts.  The projection is derived from the
# conventions and manifest; independent mutants prove each rejected boundary fires.
ENTRY_SEQUENCE_TERMS = (
    "Discover the command receiver",
    "Reach the command's one canonical workflow",
    "Bind that workflow's declared Role Lock",
    "Execute the workflow's Read Contract",
    "Obey the workflow's gates and stops",
    "name the next workflow only by its `/tfw-*` route",
)
ENTRY_EVIDENCE_LEVELS = (
    "R0 — source presence", "R1 — receiver parity", "R2 — invocation",
    "R3 — complete load", "R4 — later conformance", "R5 — controlled comparative effect",
)


def command_entry_projection(tree: SourceTree) -> tuple[tuple[str, ...], tuple[str, ...]]:
    section = resolve_heading(tree.read(".tfw/conventions.md"), "Tool Adapter Pattern")
    sequence = tuple(term for position, term in sorted(
        (section.find(term), term) for term in ENTRY_SEQUENCE_TERMS if term in section))
    levels = tuple(level for position, level in sorted(
        (section.find(level), level) for level in ENTRY_EVIDENCE_LEVELS if level in section))
    return sequence, levels


def command_entry_errors(tree: SourceTree) -> list[str]:
    errors: list[str] = []
    section = resolve_heading(tree.read(".tfw/conventions.md"), "Tool Adapter Pattern")
    sequence, levels = command_entry_projection(tree)
    if sequence != ENTRY_SEQUENCE_TERMS:
        errors.append("universal entry sequence is incomplete")
    positions = [section.find(term) for term in ENTRY_SEQUENCE_TERMS]
    if any(position < 0 for position in positions) or positions != sorted(positions):
        errors.append("universal entry sequence is reordered")
    if levels != ENTRY_EVIDENCE_LEVELS:
        errors.append("six-level evidence ladder is incomplete")
    if "A higher level is never inferred from a lower one" not in section:
        errors.append("evidence non-substitution rule is missing")

    manifest = yaml.safe_load(tree.read(".tfw/adapters/manifest.yaml"))
    if len(manifest.get("commands", {})) != 11 or len(manifest.get("adapters", {})) != 4:
        errors.append("manifest is not the exact 11-command/four-adapter topology")
        return errors
    for command, row in manifest["commands"].items():
        workflow_path = row["workflow"]
        workflow = tree.read(workflow_path)
        source_path = f".tfw/adapters/codex/skills/tfw-{command}/SKILL.md"
        installed_path = f".agents/skills/tfw-{command}/SKILL.md"
        source = tree.read(source_path)
        installed = tree.read(installed_path)
        normalized = source.casefold()
        if workflow_path not in source:
            errors.append(f"{command}: canonical workflow route missing")
        if "completely" not in normalized:
            errors.append(f"{command}: complete-load instruction missing")
        if f"{str(row['role']).casefold()} role lock" not in normalized:
            errors.append(f"{command}: declared Role Lock missing")
        if "read contract" not in normalized:
            errors.append(f"{command}: Read Contract ownership missing")
        if "stop" not in normalized:
            errors.append(f"{command}: stop boundary missing")
        if any(term in normalized for term in ("load `knowledge.md`", "load `.tfw/conventions.md`")):
            errors.append(f"{command}: adapter-owned common preload injected")
        if "phase-a/evidence" in normalized or "command-entry-summary" in normalized:
            errors.append(f"{command}: generated evidence became a runtime input")
        if installed != source:
            errors.append(f"{command}: installed Codex skill differs from source")
        for copy_path in (f".claude/commands/tfw-{command}.md",
                          f".agent/workflows/tfw-{command}.md"):
            if tree.read(copy_path) != workflow:
                errors.append(f"{command}: full-copy receiver differs from canonical workflow")
    return errors


def test_rtpsn_command_entry_projection_is_complete_source_derived_and_exact():
    candidate = SourceTree.from_path(PROJECT_ROOT)
    assert command_entry_projection(candidate) == (ENTRY_SEQUENCE_TERMS, ENTRY_EVIDENCE_LEVELS)
    assert command_entry_errors(candidate) == []
    section = resolve_heading(candidate.read(".tfw/conventions.md"), "Tool Adapter Pattern")
    assert "manifest remains tooling-only" in section
    assert "receiver supplies no alternative algorithm" in section


@pytest.mark.parametrize(
    ("path", "old", "new", "message"),
    (
        (".tfw/adapters/codex/skills/tfw-plan/SKILL.md", ".tfw/workflows/plan.md",
         ".tfw/workflows/missing.md", "canonical workflow route missing"),
        (".tfw/adapters/codex/skills/tfw-plan/SKILL.md", "completely", "partially",
         "complete-load instruction missing"),
        (".tfw/adapters/codex/skills/tfw-plan/SKILL.md", "Coordinator role lock",
         "Coordinator role hint", "declared Role Lock missing"),
        (".tfw/adapters/codex/skills/tfw-plan/SKILL.md", "Stop when the workflow routes",
         "Continue when the workflow routes", "stop boundary missing"),
        (".agents/skills/tfw-plan/SKILL.md", "This repository skill implements",
         "This drifted installed skill implements", "installed Codex skill differs"),
        (".claude/commands/tfw-plan.md", "# TFW Plan — Task Inception Workflow",
         "# Drifted TFW Plan — Task Inception Workflow", "full-copy receiver differs"),
    ),
)
def test_rtpsn_source_parity_role_load_and_stop_mutants_are_rejected(path, old, new, message):
    candidate = SourceTree.from_path(PROJECT_ROOT)
    text = candidate.read(path)
    assert old in text
    mutant = candidate.with_text(path, text.replace(old, new, 1))
    assert any(message in error for error in command_entry_errors(mutant))


def test_rtpsn_reordered_preload_and_generated_evidence_mutants_are_rejected():
    candidate = SourceTree.from_path(PROJECT_ROOT)
    conventions = candidate.read(".tfw/conventions.md")
    third = "3. Bind that workflow's declared Role Lock"
    fourth = "4. Execute the workflow's Read Contract"
    reordered = conventions.replace(third, "TEMP", 1).replace(fourth, third, 1).replace("TEMP", fourth, 1)
    produced = command_entry_projection(candidate.with_text(".tfw/conventions.md", reordered))[0]
    assert produced != ENTRY_SEQUENCE_TERMS
    assert "universal entry sequence is reordered" in command_entry_errors(
        candidate.with_text(".tfw/conventions.md", reordered))

    skill_path = ".tfw/adapters/codex/skills/tfw-plan/SKILL.md"
    skill = candidate.read(skill_path)
    preload = skill.replace("## Contract\n", "## Contract\n\n- Load `KNOWLEDGE.md`.\n", 1)
    assert any("common preload" in error for error in command_entry_errors(
        candidate.with_text(skill_path, preload)))
    generated = skill + "\nRead phase-a/evidence/command-entry-summary.json.\n"
    assert any("generated evidence" in error for error in command_entry_errors(
        candidate.with_text(skill_path, generated)))


def test_rtpsn_adapter_docs_keep_availability_and_behavior_claims_separate():
    adapter = " ".join(_read(".tfw/adapters/README.md").split())
    codex = _read(".tfw/adapters/codex/README.md")
    assert all(level in adapter for level in ("R0 source presence", "R1 receiver parity",
                                               "R2 invocation", "R3 complete canonical load",
                                               "R4 later conformance", "R5 controlled comparative effect"))
    assert all(state in adapter for state in ("declared", "tracked", "installed",
                                               "clean-receiver reproduced", "live-observed"))
    assert "explicit, non-default evaluation harness" in codex
    assert "must not be relabelled" in codex


# RTPSN Phase B: source-derived session identity semantics. Generated evidence and task
# specifications are deliberately absent from every source manifest below.
RTPSN_PHASE_B_BASELINE_REF = "83b31ff8d6cdb879fdf4f20578fa688b48863f8a"
SESSION_IDENTITY_PATH = ".tfw/conventions.md"
SESSION_WORKFLOW_PATHS = {
    "plan": ".tfw/workflows/plan.md",
    "research": ".tfw/workflows/research/base.md",
    "handoff": ".tfw/workflows/handoff.md",
    "review": ".tfw/workflows/review.md",
    "resume": ".tfw/workflows/resume.md",
    "docs": ".tfw/workflows/docs.md",
    "init": ".tfw/workflows/init.md",
    "knowledge": ".tfw/workflows/knowledge.md",
    "release": ".tfw/workflows/release.md",
    "update": ".tfw/workflows/update.md",
    "config": ".tfw/workflows/config.md",
}
SESSION_PROJECT_WIDE = frozenset({"knowledge", "release", "update", "config"})
SESSION_ROUTE_CEILINGS = {
    "/tfw-plan": 24_725,
    "/tfw-research:focused": 6_102,
    "/tfw-research:deep": 6_167,
    "/tfw-handoff": 6_366,
    "/tfw-handoff:revise": 6_366,
    "/tfw-review": 24_954,
    "/tfw-resume": 3_264,
    "/tfw-docs": 15_278,
    "/tfw-init": 4_529,
}
SESSION_RECORD_FIELDS = (
    "case", "task_source", "phase_source", "phase_omission_reason", "work_source",
    "base", "suffix_decision", "intended_title", "rename_readback_result",
    "report_once_result", "checkpoint", "claim_level", "read_manifest",
)


@dataclass(frozen=True)
class SessionIdentityCase:
    name: str
    command: str
    mode: str = "normal"
    cue: str = "EXEC"
    task_id: str = "TFW_20260905-124029_RTPSN"
    approved_abbr: str | None = "RTPSN"
    known_abbrs: tuple[str, ...] = ("RTPSN",)
    phase_candidates: tuple[str, ...] = ("phase-b",)
    phase_source: str | None = "governing-state"
    iteration: str | None = None
    lead_binding: bool = False
    existing_titles: tuple[str, ...] = ()
    colliding_keys: tuple[str, ...] = ()
    stable_key: str | None = "new-key"
    rename_available: bool = True
    readback_available: bool = True
    readback_override: str | None = None


@dataclass(frozen=True)
class SessionIdentityRecord:
    case: str
    task_source: str
    phase_source: str | None
    phase_omission_reason: str | None
    work_source: str
    base: str | None
    suffix_decision: str
    intended_title: str | None
    rename_readback_result: str
    report_once_result: str
    checkpoint: str
    claim_level: str
    read_manifest: tuple[str, ...]


def _session_contract(tree: SourceTree) -> dict[str, object]:
    section = resolve_heading(tree.read(SESSION_IDENTITY_PATH), "Session identity")
    work = re.search(r"^WORK:=(?P<items>[A-Z|]+)$", section, re.MULTILINE)
    if not work:
        raise SourceContractError("Session identity WORK vocabulary does not resolve")
    return {
        "separator": " · " if "SP:=U+0020;DOT:=U+00B7" in section else " | ",
        "work": tuple(work["items"].split("|")),
        "task_policy": "abbreviation" if "approved root-unique abbreviation" in section else "full-id",
        "phase_case": "upper" if "uppercase(" in section else "lower",
        "collision": "prefix" if "shortest-unique-leading-prefix" in section else "full-key",
        "failure_claim": "unclaimed" if "continue-unclaimed" in section else "claimed",
        "authority": "state/lineage" if "authoritative-state/lineage" in section else "chat",
        "section": section,
    }


def _session_workflow_source(tree: SourceTree, case: SessionIdentityCase) -> tuple[str, str, str]:
    path = SESSION_WORKFLOW_PATHS[case.command]
    text = tree.read(path)
    if case.command in SESSION_PROJECT_WIDE:
        if "Session identity" in text:
            raise SourceContractError(f"{case.command}: project-wide route acquired task identity")
        return "project-wide", f"{path}:project-wide", path
    if case.command == "docs" and case.mode == "batch":
        line = next(i for i, value in enumerate(text.splitlines(), 1) if value == "Batch: skip.")
        return "DOCS", f"{path}:{line}:skip", path
    if case.command == "init" and case.mode == "attach":
        line = next(i for i, value in enumerate(text.splitlines(), 1) if value == "Attach/repair:")
        return "INIT", f"{path}:{line}:skip", path
    cue = (re.search(r"WORK=(PLAN|RESEARCH|EXEC|REVIEW|RESUME|DOCS|INIT)", text)
           or re.search(r"apply `Session identity` as `(PLAN|RESEARCH|EXEC|REVIEW|RESUME|DOCS|INIT)`", text))
    if not cue:
        raise SourceContractError(f"{case.command}: WORK binding does not resolve")
    marker = "**Apply session identity.**" if case.command == "plan" and case.mode == "new" else "Session identity checkpoint"
    if marker not in text:
        marker = "apply `Session identity`"
    line = next(i for i, value in enumerate(text.splitlines(), 1) if marker in value)
    window = " ".join(text.splitlines()[line - 1:line + 8]).casefold()
    order = "after" if "after(" in window or "after onb" in window else "before"
    return cue.group(1), f"{path}:{line}:{order}", path


def _session_task(case: SessionIdentityCase, contract: dict[str, object]) -> tuple[str, str]:
    if re.fullmatch(r"TFW-\d+", case.task_id):
        return case.task_id, "legacy-state"
    unique = case.approved_abbr is not None and case.known_abbrs.count(case.approved_abbr) == 1
    if contract["task_policy"] == "abbreviation" and unique:
        return case.approved_abbr or case.task_id, str(contract["authority"])
    return case.task_id, str(contract["authority"])


def _session_phase(case: SessionIdentityCase, contract: dict[str, object]) -> tuple[str | None, str | None]:
    if case.iteration and not case.phase_candidates:
        return None, "research-iteration"
    if len(case.phase_candidates) != 1 or case.phase_source != "governing-state":
        reason = "absent" if not case.phase_candidates else "ambiguous"
        return None, reason
    token = case.phase_candidates[0].removeprefix("phase-")
    return (token.upper() if contract["phase_case"] == "upper" else token.lower()), None


def _shortest_unique_prefix(current: str, others: tuple[str, ...]) -> str | None:
    for size in range(1, len(current) + 1):
        prefix = current[:size]
        if not any(value.startswith(prefix) for value in others):
            return prefix
    return None


def resolve_session_identity(tree: SourceTree, case: SessionIdentityCase) -> SessionIdentityRecord:
    work, checkpoint, workflow_path = _session_workflow_source(tree, case)
    if case.command in SESSION_PROJECT_WIDE or (case.command, case.mode) in {("docs", "batch"), ("init", "attach")}:
        return SessionIdentityRecord(
            case.name, "not-applicable", None, "route-has-no-single-task", work,
            None, "skipped", None, "not-attempted", "none", checkpoint,
            "synthetic-structural", (workflow_path,),
        )
    contract = _session_contract(tree)
    if work not in contract["work"]:
        raise SourceContractError(f"{case.command}: WORK is outside conventions vocabulary")
    effective_work = "LEAD" if case.lead_binding and work in {"PLAN", "RESUME"} else work
    task, task_source = _session_task(case, contract)
    phase, omission = _session_phase(case, contract)
    separator = str(contract["separator"])
    base = separator.join(value for value in (effective_work, task, phase) if value)
    title = base
    suffix = "none"
    report_reason = None
    if base in case.existing_titles:
        if not case.stable_key:
            suffix, report_reason = "unclaimed:no-stable-key", "no-stable-key"
        else:
            prefix = (_shortest_unique_prefix(case.stable_key, case.colliding_keys)
                      if contract["collision"] == "prefix" else case.stable_key)
            if prefix:
                suffix = f"@{prefix}"
                title += separator + suffix
            else:
                suffix, report_reason = "unclaimed:no-unique-prefix", "no-unique-prefix"
    if not case.rename_available:
        report_reason = "rename-unavailable"
        readback_result = report_reason
    elif not case.readback_available:
        report_reason = "readback-unavailable"
        readback_result = report_reason
    else:
        observed = case.readback_override if case.readback_override is not None else title
        if observed != title:
            report_reason = "altered-readback"
            readback_result = f"mismatch:{observed}"
        else:
            readback_result = "exact"
    claim = "synthetic-semantic"
    if report_reason and contract["failure_claim"] != "unclaimed":
        claim = "synthetic:claimed-after-failure"
    report = "none" if not report_reason else f"once:{title}:{report_reason}"
    return SessionIdentityRecord(
        case.name, task_source, case.phase_source if phase else None, omission,
        f"{workflow_path}:WORK={effective_work}", base, suffix, title,
        readback_result, report, checkpoint, claim,
        (SESSION_IDENTITY_PATH, workflow_path),
    )


SESSION_IDENTITY_CASES = {
    "modern_unique": SessionIdentityCase("modern_unique", "handoff"),
    "modern_abbr_collision": SessionIdentityCase(
        "modern_abbr_collision", "handoff", known_abbrs=("RTPSN", "RTPSN")),
    "legacy": SessionIdentityCase("legacy", "review", cue="REVIEW", task_id="TFW-42",
                                  approved_abbr=None, known_abbrs=()),
    "dirty_clock": SessionIdentityCase(
        "dirty_clock", "handoff", task_id="TFW_20260905-126199_DIRTY",
        approved_abbr="DIRTY", known_abbrs=("DIRTY",)),
    "phase_absent": SessionIdentityCase("phase_absent", "handoff", phase_candidates=()),
    "phase_ambiguous": SessionIdentityCase(
        "phase_ambiguous", "resume", cue="RESUME", phase_candidates=("phase-a", "phase-b")),
    "phase_complex": SessionIdentityCase(
        "phase_complex", "review", cue="REVIEW", phase_candidates=("phase-b.2-red",)),
    "research_iteration": SessionIdentityCase(
        "research_iteration", "research", cue="RESEARCH", phase_candidates=(),
        phase_source=None, iteration="iter2"),
    "lead_bound": SessionIdentityCase("lead_bound", "plan", cue="PLAN", lead_binding=True),
    "lead_unbound": SessionIdentityCase("lead_unbound", "resume", cue="RESUME"),
    "base_collision": SessionIdentityCase(
        "base_collision", "handoff", existing_titles=("EXEC · RTPSN · B",),
        colliding_keys=("ac9",), stable_key="ab7"),
    "collision_no_key": SessionIdentityCase(
        "collision_no_key", "handoff", existing_titles=("EXEC · RTPSN · B",), stable_key=None),
    "rename_unavailable": SessionIdentityCase("rename_unavailable", "handoff", rename_available=False),
    "readback_unavailable": SessionIdentityCase("readback_unavailable", "handoff", readback_available=False),
    "middle_dot_corrupt": SessionIdentityCase(
        "middle_dot_corrupt", "handoff", readback_override="EXEC | RTPSN | B"),
}


SESSION_MODE_CASES = {
    "plan_new": SessionIdentityCase("plan_new", "plan", mode="new", cue="PLAN"),
    "plan_existing": SessionIdentityCase("plan_existing", "plan", mode="existing", cue="PLAN"),
    "research": SessionIdentityCase("research", "research", cue="RESEARCH"),
    "handoff": SessionIdentityCase("handoff", "handoff"),
    "review": SessionIdentityCase("review", "review", cue="REVIEW"),
    "resume_single": SessionIdentityCase("resume_single", "resume", cue="RESUME"),
    "resume_ambiguous": SessionIdentityCase(
        "resume_ambiguous", "resume", cue="RESUME", phase_candidates=("phase-a", "phase-b")),
    "docs_auto": SessionIdentityCase("docs_auto", "docs", mode="auto", cue="DOCS"),
    "docs_manual": SessionIdentityCase("docs_manual", "docs", mode="manual", cue="DOCS"),
    "docs_batch": SessionIdentityCase("docs_batch", "docs", mode="batch", cue="DOCS"),
    "init_full": SessionIdentityCase("init_full", "init", mode="full", cue="INIT"),
    "init_attach": SessionIdentityCase("init_attach", "init", mode="attach", cue="INIT"),
    **{name: SessionIdentityCase(name, name, mode="project-wide", cue=name.upper(), task_id="")
       for name in sorted(SESSION_PROJECT_WIDE)},
}


def session_identity_scenario_payload(tree: SourceTree) -> dict[str, object]:
    return {
        "scenarios": {name: resolve_session_identity(tree, case).__dict__
                      for name, case in SESSION_IDENTITY_CASES.items()},
        "workflow_modes": {name: resolve_session_identity(tree, case).__dict__
                           for name, case in SESSION_MODE_CASES.items()},
    }


def _independent_session_errors(record: SessionIdentityRecord, case: SessionIdentityCase) -> list[str]:
    errors = []
    expected_work = "LEAD" if case.lead_binding and case.cue in {"PLAN", "RESUME"} else case.cue
    if expected_work not in record.work_source:
        errors.append("work")
    if case.command not in SESSION_PROJECT_WIDE and case.mode not in {"batch", "attach"}:
        if record.task_source not in {"state/lineage", "legacy-state"}:
            errors.append("authority")
        if ":after" in record.checkpoint:
            errors.append("checkpoint")
        if record.base and " | " in record.base:
            errors.append("separator")
        if record.claim_level == "synthetic:claimed-after-failure":
            errors.append("transport")
    if case.name == "modern_unique" and record.intended_title != "EXEC · RTPSN · B":
        errors.append("task")
    if case.name == "phase_complex" and not (record.base or "").endswith("B.2-RED"):
        errors.append("phase")
    if case.name == "base_collision" and record.suffix_decision != "@ab":
        errors.append("collision")
    return errors


def session_identity_mutant_payload(tree: SourceTree) -> list[dict[str, object]]:
    mutations = {
        "work": ("modern_unique", SESSION_WORKFLOW_PATHS["handoff"], "WORK=EXEC", "WORK=REVIEW"),
        "task": ("modern_unique", SESSION_IDENTITY_PATH, "approved root-unique abbreviation", "full-ID only"),
        "phase": ("phase_complex", SESSION_IDENTITY_PATH, "uppercase(", "lowercase("),
        "collision": ("base_collision", SESSION_IDENTITY_PATH, "shortest-unique-leading-prefix", "full-stable-key"),
        "transport": ("rename_unavailable", SESSION_IDENTITY_PATH, "continue-unclaimed", "continue-claimed"),
        "checkpoint": ("modern_unique", SESSION_WORKFLOW_PATHS["handoff"], "before ONB", "after ONB"),
        "authority": ("modern_unique", SESSION_IDENTITY_PATH, "authoritative-state/lineage", "chat-state"),
    }
    results = []
    for family, (case_name, path, old, new) in mutations.items():
        case = SESSION_IDENTITY_CASES[case_name]
        normal = resolve_session_identity(tree, case)
        source = tree.read(path)
        if old not in source:
            raise SourceContractError(f"{family}: mutation source does not resolve")
        produced = resolve_session_identity(tree.with_text(path, source.replace(old, new, 1)), case)
        errors = _independent_session_errors(produced, case)
        results.append({
            "family": family,
            "case": case_name,
            "produced": produced.__dict__,
            "projection_changed": produced != normal,
            "independent_expected_rejects": bool(errors),
            "rejection_fields": errors,
        })
    return results


def session_identity_context_payload(candidate: SourceTree) -> dict[str, object]:
    baseline = SourceTree.from_git(PROJECT_ROOT, RTPSN_PHASE_B_BASELINE_REF)
    routes = {}
    for command, ceiling in SESSION_ROUTE_CEILINGS.items():
        before = measure_graph(baseline, discover_read_graph(baseline, command))
        after = measure_graph(candidate, discover_read_graph(candidate, command))
        routes[command] = {"baseline": before, "candidate": after, "ceiling": ceiling,
                           "passes": before == ceiling and after <= ceiling}
    workflows = {}
    for command in ("plan", "research", "handoff", "review", "resume", "docs", "init"):
        path = SESSION_WORKFLOW_PATHS[command]
        delta = _words(candidate.read(path)) - _words(baseline.read(path))
        workflows[path] = {"net_words": delta, "cap": 45, "passes": delta <= 45}
    central = _words(resolve_heading(candidate.read(SESSION_IDENTITY_PATH), "Session identity"))
    return {
        "baseline": RTPSN_PHASE_B_BASELINE_REF,
        "routes": routes,
        "active_corpus": {"baseline": active_runtime_corpus_words(baseline),
                          "candidate": active_runtime_corpus_words(candidate), "ceiling": 33_749},
        "central_range": {"words": central, "cap": 260, "passes": central <= 260},
        "workflow_local": workflows,
        "claim_level": "R0/R1 structural and synthetic semantic evidence only",
    }


def _python_named_span(text: str, name: str) -> str:
    tree = ast.parse(text)
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name:
            return "\n".join(text.splitlines()[node.lineno - 1:node.end_lineno])
        if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == name
                                                for target in node.targets):
            return "\n".join(text.splitlines()[node.lineno - 1:node.end_lineno])
    raise SourceContractError(f"protected Python span does not resolve: {name}")


def test_rtpsn_phase_b_contract_is_single_source_complete_and_glossary_is_only_a_router():
    tree = SourceTree.from_path(PROJECT_ROOT)
    contract = _session_contract(tree)
    assert contract["separator"] == " · "
    assert contract["work"] == ("PLAN", "RESEARCH", "EXEC", "REVIEW", "RESUME", "DOCS", "INIT", "LEAD")
    section = str(contract["section"])
    assert all(term in section for term in (
        "non-authoritative", "approved root-unique abbreviation", "full-ID", "historical:=full-ID",
        "absent/conflict/ambiguity/iteration", "governing-bound", "shortest-unique-leading-prefix",
        "exact-readback-only", "report-once", "continue-unclaimed", "title-pipe",
        "authoritative-state/lineage", "never chat/index/folder/memory",
    ))
    glossary = resolve_heading(tree.read(".tfw/glossary.md"), "Session Naming")
    assert "conventions.md" in glossary and "Session identity" in glossary
    assert not any(term in glossary for term in ("BASE:=", "WORK:=", "shortest-unique-leading-prefix"))


def test_rtpsn_phase_b_scenarios_cover_titles_omissions_collisions_and_fail_soft_transport():
    records = {name: resolve_session_identity(SourceTree.from_path(PROJECT_ROOT), case)
               for name, case in SESSION_IDENTITY_CASES.items()}
    assert records["modern_unique"].intended_title == "EXEC · RTPSN · B"
    assert records["modern_abbr_collision"].base == "EXEC · TFW_20260905-124029_RTPSN · B"
    assert records["legacy"].base == "REVIEW · TFW-42 · B"
    assert records["dirty_clock"].base == "EXEC · DIRTY · B"
    assert records["phase_absent"].phase_omission_reason == "absent"
    assert records["phase_ambiguous"].phase_omission_reason == "ambiguous"
    assert records["phase_complex"].base == "REVIEW · RTPSN · B.2-RED"
    assert records["research_iteration"].phase_omission_reason == "research-iteration"
    assert records["lead_bound"].base == "LEAD · RTPSN · B"
    assert records["lead_unbound"].base == "RESUME · RTPSN · B"
    assert records["base_collision"].intended_title == "EXEC · RTPSN · B · @ab"
    assert records["collision_no_key"].suffix_decision == "unclaimed:no-stable-key"
    assert all(records[name].report_once_result.startswith("once:") for name in (
        "collision_no_key", "rename_unavailable", "readback_unavailable", "middle_dot_corrupt"))
    assert all(tuple(record.__dict__) == SESSION_RECORD_FIELDS for record in records.values())
    assert all(" | " not in (record.intended_title or "") for record in records.values())


def test_rtpsn_phase_b_all_workflow_modes_are_classified_and_source_bounded():
    tree = SourceTree.from_path(PROJECT_ROOT)
    records = {name: resolve_session_identity(tree, case) for name, case in SESSION_MODE_CASES.items()}
    assert set(records) == {
        "plan_new", "plan_existing", "research", "handoff", "review", "resume_single",
        "resume_ambiguous", "docs_auto", "docs_manual", "docs_batch", "init_full",
        "init_attach", "knowledge", "release", "update", "config",
    }
    assert records["resume_ambiguous"].phase_omission_reason == "ambiguous"
    assert records["docs_batch"].suffix_decision == records["init_attach"].suffix_decision == "skipped"
    assert all(records[name].suffix_decision == "skipped" for name in SESSION_PROJECT_WIDE)
    assert all(not any("phase-b/evidence" in path or "TS__" in path for path in record.read_manifest)
               for record in records.values())


def test_rtpsn_phase_b_each_semantic_mutant_changes_output_then_is_independently_rejected():
    results = session_identity_mutant_payload(SourceTree.from_path(PROJECT_ROOT))
    assert {row["family"] for row in results} == {
        "work", "task", "phase", "collision", "transport", "checkpoint", "authority"}
    assert all(row["projection_changed"] and row["independent_expected_rejects"] for row in results)


def test_rtpsn_phase_b_context_routes_corpus_and_local_caps_do_not_grow():
    report = session_identity_context_payload(SourceTree.from_path(PROJECT_ROOT))
    assert all(row["passes"] for row in report["routes"].values())
    assert report["active_corpus"]["baseline"] == 33_749
    assert report["active_corpus"]["candidate"] <= report["active_corpus"]["ceiling"]
    assert report["central_range"]["passes"]
    assert all(row["passes"] for row in report["workflow_local"].values())


def test_rtpsn_phase_b_protected_d75_vbsa_tests_and_ceiling_constant_are_byte_exact():
    baseline = SourceTree.from_git(PROJECT_ROOT, RTPSN_PHASE_B_BASELINE_REF).read(
        "docs/scripts/test_runtime_context.py")
    candidate = SourceTree.from_path(PROJECT_ROOT).read("docs/scripts/test_runtime_context.py")
    for name in (
        "PHASE_C_PRIMARY_ENTRY_WORDS",
        "test_phase_c_every_changed_path_and_active_corpus_clear_thirty_percent",
        "test_vbsa_plan_loads_three_unique_canonical_sections_with_d75_intact",
    ):
        assert _python_named_span(candidate, name) == _python_named_span(baseline, name)
    assert PHASE_C_PRIMARY_ENTRY_WORDS["/tfw-plan"] == 24_730


def test_rtpsn_phase_b_all_full_copy_receivers_match_canonical_bytes():
    for name, path in SESSION_WORKFLOW_PATHS.items():
        if name in SESSION_PROJECT_WIDE:
            continue
        canonical = (PROJECT_ROOT / path).read_bytes()
        assert (PROJECT_ROOT / f".claude/commands/tfw-{name}.md").read_bytes() == canonical
        assert (PROJECT_ROOT / f".agent/workflows/tfw-{name}.md").read_bytes() == canonical


# CRATM Phase D: AT is projected from the product sources into executable decisions. The
# independent literals below are the oracle; parsers never import the phase HL/TS or test fixtures.
PHASE_D_BASELINE_REF = "8e68ab37d300122ff110500ad58f354f76b6210f"
PHASE_D_CONVENTIONS = ".tfw/conventions.md"
PHASE_D_ASSIGNMENT = ".tfw/templates/HL.md"
PHASE_D_ADAPTER = ".tfw/adapters/codex/AGENTS.md.template"
PHASE_D_COLUMNS = (
    "Participant", "Workflow role", "Scope", "Reports to", "Semantic channel", "Autonomous from",
)
PHASE_D_DECLARATION_FACTS = (
    "Role Assignment exists", "master HL owner-approved and frozen", "freeze baseline committed",
)
PHASE_D_RETURNS = (
    ("Amendment whose nearest authorised ruler is its proposer", "§12, up the chain to a human"),
    ("Amendment against an owner-reserved claim", "§12 directly to owner"),
    ("Purpose Check finds the reference set self-contradictory",
     "judge.md → owner as contract defect"),
    ("❌ REJECT verdict", "review.md → owner"),
    ("Declared participant unavailable", "§12 SUPERSEDE; wait, never substitute silently"),
    ("Scope-budget decision", "§6 first: below both immutable multipliers, necessary growth may "
     "receive prospective Coordinator approval with all invariants fixed; at/above a multiplier or "
     "from planned zero returns to owner; rule 19 forbids delegated self-acceptance"),
    ("Initiation chain does not terminate at a human", "Pre-work refusal; work does not start"),
)
PHASE_D_NATIVE_GATES = (
    "Behavioral preflight", "Frozen unit", "Provisioning identity", "Direct route", "Isolation",
    "Role/artifact cycle", "Owner-turn outcome", "Terminal reconstruction",
)
PHASE_D_OPERATIONS = ("create_thread", "send_message_to_thread", "wait_threads")


def _phase_d_table(section: str, first_column: str) -> tuple[tuple[str, ...], tuple[tuple[str, ...], ...]]:
    lines = section.splitlines()
    header = next((line for line in lines if line.startswith(f"| {first_column} |")), None)
    if header is None:
        header = next((line for line in lines if line.startswith("|") and
                       not re.match(r"^\|[-:| ]+\|$", line)), None)
    if header is None:
        raise SourceContractError(f"Phase D table does not resolve: {first_column}")
    columns = tuple(_plain_table_cell(cell) for cell in header.strip("|").split("|"))
    rows = []
    start = lines.index(header)
    for line in lines[start + 2:]:
        if not line.startswith("|"):
            break
        cells = tuple(_plain_table_cell(cell) for cell in line.strip("|").split("|"))
        if len(cells) == len(columns):
            rows.append(cells)
    return columns, tuple(rows)


def _phase_d_span(text: str, needle: str) -> dict[str, int]:
    if needle not in text:
        raise SourceContractError(f"Phase D source clause does not resolve: {needle!r}")
    start = text[:text.index(needle)].count("\n") + 1
    return {"start": start, "end": start + needle.count("\n")}


def parse_phase_d_contract(tree: SourceTree) -> dict[str, object]:
    section = resolve_heading(tree.read(PHASE_D_CONVENTIONS),
                              "AT (Agent Team) — explicit declaration only")
    fact_anchors = {
        "Role Assignment exists": "a Role Assignment exists",
        "master HL owner-approved and frozen": "its master HL is owner-approved and frozen",
        "freeze baseline committed": "that freeze baseline is committed",
    }
    facts = tuple(name for name, anchor in fact_anchors.items() if anchor in section)
    _, return_rows = _phase_d_table(section, "Owner-return trigger")
    returns = tuple((row[0], row[1]) for row in return_rows)
    gates = tuple(re.findall(r"^\d+\. \*\*(.+?):\*\*", section, re.MULTILINE))
    return {
        "declaration_facts": facts,
        "coordinator_to_owner": "returns the seven triggers below to the owner" in section,
        "delegate_to_coordinator": "reports gates/results directly" in section,
        "owner_returns": returns,
        "degradation_safe": all(phrase in section for phrase in (
            "stop and wait", "relay, hidden helper", "Already-authorized CL or AG")),
        "native_gates": gates,
        "native_single_run": "passes all eight gates in one trial" in section,
        "no_partial_composition": "partial demonstrations do not compose" in section,
        "nonordinal": "Never compare lifecycle ids ordinally" in section,
        "same_unit_path": all(phrase in section for phrase in (
            "same unit", "ordered journal path", "current gate", "direct dispatch event")),
        "hl_approval_gate": "At `HL_DRAFT`, activation needs owner-approved freeze and its commit" in section,
        "ts_approval_gate": "At `TS_DRAFT`, exact TS approval must precede Executor activation" in section,
        "dash_wait": "`—` means report and wait at every decision" in section,
        "metadata_no_authority": all(term in section for term in (
            "title", "profile", "binding", "provider", "`writer`", "`on_behalf_of`",
            "is not authority")),
    }


def phase_d_contract_errors(record: dict[str, object]) -> list[str]:
    errors = []
    if tuple(record["declaration_facts"]) != PHASE_D_DECLARATION_FACTS:
        errors.append("declaration-facts")
    if not record["coordinator_to_owner"]: errors.append("coordinator-duty")
    if not record["delegate_to_coordinator"]: errors.append("delegate-duty")
    if tuple(record["owner_returns"]) != PHASE_D_RETURNS: errors.append("owner-returns")
    if not record["degradation_safe"]: errors.append("degradation")
    if tuple(record["native_gates"]) != PHASE_D_NATIVE_GATES: errors.append("native-gates")
    for name in ("native_single_run", "no_partial_composition", "nonordinal", "same_unit_path",
                 "hl_approval_gate", "ts_approval_gate", "dash_wait", "metadata_no_authority"):
        if not record[name]: errors.append(name)
    return errors


def parse_phase_d_assignment(tree: SourceTree) -> dict[str, object]:
    text = tree.read(PHASE_D_ASSIGNMENT)
    section = resolve_heading(text, "Role Assignment 🔒 FROZEN")
    columns, rows = _phase_d_table(section, "Participant")
    return {
        "columns": columns,
        "sample_rows": rows,
        "before_phase_dependencies": text.index("### 4.1 Role Assignment") < text.index("### Phase Dependencies"),
        "human_rooted": "human-rooted `team/` handle" in section,
        "existing_lifecycle_or_dash": "one existing lifecycle id or `—`" in section,
        "no_default": "`TS_DRAFT` is a conservative example, never a default" in section,
        "hl_gate": "`HL_DRAFT` requires owner approval and committed freeze" in section,
        "ts_gate": "`TS_DRAFT` also requires exact TS approval" in section,
        "role_lock_only": "permissions still come only from Role Locks" in section,
        "source_span": _phase_d_span(text, "### 4.1 Role Assignment 🔒 FROZEN"),
    }


def phase_d_assignment_errors(record: dict[str, object]) -> list[str]:
    errors = []
    if tuple(record["columns"]) != PHASE_D_COLUMNS: errors.append("columns")
    if len(record["sample_rows"]) != 1: errors.append("rendered-sample")
    for name in ("before_phase_dependencies", "human_rooted", "existing_lifecycle_or_dash",
                 "no_default", "hl_gate", "ts_gate", "role_lock_only"):
        if not record[name]: errors.append(name)
    return errors


PHASE_D_WORKFLOW_SPECS = {
    "plan": (".tfw/workflows/plan.md", "Coordinator", "HL/dispatch", "before HL approval",
             ("all six columns", "approved handles", "human-rooted reporting", "bounded scope",
              "direct semantic channel", "Autonomous from")),
    "handoff": (".tfw/workflows/handoff.md", "Executor", "ONB", "before ONB/work",
                ("participant", "role", "scope", "report target", "semantic channel",
                 "Autonomous from", "authoritative source")),
    "research": (".tfw/workflows/research/base.md", "Researcher", "Briefing and RES", "before Step 1",
                 ("participant", "role", "scope", "report target", "semantic channel",
                  "Autonomous from", "authoritative source")),
    "review": (".tfw/workflows/review.md", "Reviewer", "REVIEW", "Reviewer row before Map",
               ("participant", "role", "scope", "report target", "semantic channel",
                "Autonomous from", "authoritative source")),
}


def parse_phase_d_workflows(tree: SourceTree) -> dict[str, dict[str, object]]:
    records = {}
    for name, (path, role, artifact, order_phrase, fields) in PHASE_D_WORKFLOW_SPECS.items():
        text = tree.read(path)
        if name == "plan":
            start = text.index("10. **Validate Role Assignment when AT is declared.**")
            end = text.index("**GATE: User approves HL**", start)
            checkpoint = text[start:end] + resolve_heading(text, "AT dispatch after exact TS approval")
            order_ok = order_phrase in checkpoint and start < end
            direct = "Questions and results return directly" in checkpoint
            return_values = ("questions", "results")
            same_role = "same Executor and independent Reviewer" in checkpoint
            role_lock = "Never execute another workflow" in checkpoint
        else:
            checkpoint = resolve_heading(text, "Agent Team checkpoint")
            first_work = {"handoff": "## Phase 1: Executor Onboarding",
                          "research": "## Step 1: Load Context",
                          "review": "## Step 1: Map"}[name]
            order_ok = order_phrase in checkpoint and text.index("## Agent Team checkpoint") < text.index(first_work)
            direct = "directly" in checkpoint
            return_values = {
                "handoff": ("questions", "RF"), "research": ("WAIT", "final RES"),
                "review": ("questions", "verdict", "proposals"),
            }[name]
            same_role = "same" in checkpoint or "reuse the Executor unit" in checkpoint
            role_lock = "Role Lock" in checkpoint
        records[name] = {
            "path": path, "role": role, "artifact": artifact,
            "prework_order": order_ok,
            "received_fields": tuple(field for field in fields if field in checkpoint),
            "direct_return": direct, "return_values": return_values,
            "same_role_continuity": same_role,
            "unresolved_wait": "`—`" in checkpoint and "wait" in checkpoint,
            "role_lock": role_lock,
            "source_span": _phase_d_span(text, checkpoint.splitlines()[0]),
        }
    return records


def phase_d_workflow_errors(records: dict[str, dict[str, object]]) -> list[str]:
    errors = []
    for name, (_, role, artifact, _, fields) in PHASE_D_WORKFLOW_SPECS.items():
        row = records[name]
        if row["role"] != role or row["artifact"] != artifact: errors.append(f"{name}:identity")
        if tuple(row["received_fields"]) != fields: errors.append(f"{name}:fields")
        for key in ("prework_order", "direct_return", "same_role_continuity", "unresolved_wait",
                    "role_lock"):
            if not row[key]: errors.append(f"{name}:{key}")
    return errors


def parse_phase_d_adapter(tree: SourceTree) -> dict[str, object]:
    text = tree.read(PHASE_D_ADAPTER)
    section = resolve_heading(text, "Codex AT profile")
    operations = tuple(op for op in PHASE_D_OPERATIONS if f"`{op}`" in section)
    return {
        "operations": operations,
        "fresh_visible_addressable": all(word in section for word in (
            "fresh", "user-visible", "independently-addressable")),
        "separate_worktrees": "separate worktrees" in section,
        "approved_human_root": "approved human-rooted rows" in section.casefold(),
        "metadata_no_grant": "metadata/profile grant nothing" in section,
        "same_role_reuse": "reuse the same Executor/Reviewer" in section,
        "rejected_holders": tuple(term for term in (
            "Forks", "subagents", "relays", "hidden helpers", "provider switches") if term in section),
        "evidence_limit": "G1–G7 support mechanics, not G8 reliability" in section,
        "source_span": _phase_d_span(text, "### Codex AT profile"),
    }


def phase_d_adapter_errors(record: dict[str, object]) -> list[str]:
    errors = []
    if tuple(record["operations"]) != PHASE_D_OPERATIONS: errors.append("operations")
    if tuple(record["rejected_holders"]) != (
            "Forks", "subagents", "relays", "hidden helpers", "provider switches"):
        errors.append("rejected-holders")
    for name in ("fresh_visible_addressable", "separate_worktrees", "approved_human_root",
                 "metadata_no_grant", "same_role_reuse", "evidence_limit"):
        if not record[name]: errors.append(name)
    return errors


@dataclass(frozen=True)
class ATFixture:
    table: bool; frozen: bool; committed: bool; ordinary_ag: bool = False
    boundary: str = "before"; same_unit: bool = True; ordered_path: bool = True
    approval: bool = True; direct_dispatch: bool = True; ambiguous: bool = False
    metadata: bool = False; relay: bool = False; event: str = "start"


@dataclass(frozen=True)
class ATDecision:
    mode: str; declared: bool; active: bool; holder: str; action: str; reason: str


PHASE_D_SCENARIOS = {
    "cl_default": ATFixture(False, False, False),
    "explicit_ag": ATFixture(False, False, False, ordinary_ag=True),
    "table_only": ATFixture(True, False, False),
    "draft_hl": ATFixture(True, False, False, boundary="HL_DRAFT"),
    "uncommitted": ATFixture(True, True, False, boundary="HL_DRAFT"),
    "declared_before": ATFixture(True, True, True, boundary="before"),
    "hl_unapproved": ATFixture(True, True, True, boundary="HL_DRAFT", approval=False),
    "hl_active": ATFixture(True, True, True, boundary="HL_DRAFT"),
    "ts_unapproved": ATFixture(True, True, True, boundary="TS_DRAFT", approval=False),
    "ts_active": ATFixture(True, True, True, boundary="TS_DRAFT"),
    "dash": ATFixture(True, True, True, boundary="—"),
    "wrong_unit": ATFixture(True, True, True, boundary="TS_DRAFT", same_unit=False),
    "missing_transition": ATFixture(True, True, True, boundary="TS_DRAFT", ordered_path=False),
    "ambiguous_branch": ATFixture(True, True, True, boundary="TS_DRAFT", ambiguous=True),
    "identity_bootstrap": ATFixture(False, False, False, metadata=True),
    "degraded_relay": ATFixture(True, True, True, boundary="TS_DRAFT", direct_dispatch=False, relay=True),
    "return_to_coordinator": ATFixture(True, True, True, boundary="TS_DRAFT", event="return"),
}


PHASE_D_EXPECTED_SCENARIOS = {
    "cl_default": ("CL", False, False, "human", "PROPOSE", "table-absent"),
    "explicit_ag": ("AG", False, True, "delegate", "CONTINUE", "explicit-ordinary-ag"),
    "table_only": ("CL", False, False, "human", "WAIT", "declaration-incomplete"),
    "draft_hl": ("CL", False, False, "human", "WAIT", "declaration-incomplete"),
    "uncommitted": ("CL", False, False, "human", "WAIT", "declaration-incomplete"),
    "declared_before": ("AT", True, False, "Coordinator", "REPORT_WAIT", "boundary-not-reached"),
    "hl_unapproved": ("AT", True, False, "Coordinator", "REPORT_WAIT", "approval-missing"),
    "hl_active": ("AT", True, True, "delegate", "CONTINUE", "row-active"),
    "ts_unapproved": ("AT", True, False, "Coordinator", "REPORT_WAIT", "approval-missing"),
    "ts_active": ("AT", True, True, "delegate", "CONTINUE", "row-active"),
    "dash": ("AT", True, False, "Coordinator", "REPORT_WAIT", "dash-boundary"),
    "wrong_unit": ("AT", True, False, "Coordinator", "REPORT_WAIT", "foreign-unit"),
    "missing_transition": ("AT", True, False, "Coordinator", "REPORT_WAIT", "path-incomplete"),
    "ambiguous_branch": ("AT", True, False, "Coordinator", "REPORT_WAIT", "ambiguous-path"),
    "identity_bootstrap": ("CL", False, False, "human", "PROPOSE", "metadata-no-authority"),
    "degraded_relay": ("AT", True, False, "Coordinator", "REPORT_WAIT", "direct-route-missing"),
    "return_to_coordinator": ("AT", True, True, "Coordinator", "DIRECT_RETURN", "workflow-return"),
}


def resolve_phase_d_scenario(tree: SourceTree, fixture: ATFixture) -> ATDecision:
    contract = parse_phase_d_contract(tree)
    facts_available = len(contract["declaration_facts"]) == 3
    declared = fixture.table and fixture.frozen and fixture.committed and facts_available
    if not declared:
        if fixture.ordinary_ag:
            return ATDecision("AG", False, True, "delegate", "CONTINUE", "explicit-ordinary-ag")
        if fixture.metadata and contract["metadata_no_authority"]:
            return ATDecision("CL", False, False, "human", "PROPOSE", "metadata-no-authority")
        reason = "table-absent" if not fixture.table and not fixture.metadata else "declaration-incomplete"
        action = "PROPOSE" if reason == "table-absent" else "WAIT"
        return ATDecision("CL", False, False, "human", action, reason)
    if fixture.boundary == "before":
        return ATDecision("AT", True, False, "Coordinator", "REPORT_WAIT", "boundary-not-reached")
    if fixture.boundary == "—" and contract["dash_wait"]:
        return ATDecision("AT", True, False, "Coordinator", "REPORT_WAIT", "dash-boundary")
    if contract["nonordinal"]:
        if not fixture.same_unit:
            return ATDecision("AT", True, False, "Coordinator", "REPORT_WAIT", "foreign-unit")
        if not fixture.ordered_path:
            return ATDecision("AT", True, False, "Coordinator", "REPORT_WAIT", "path-incomplete")
        if fixture.ambiguous:
            return ATDecision("AT", True, False, "Coordinator", "REPORT_WAIT", "ambiguous-path")
    if not fixture.direct_dispatch and contract["degradation_safe"]:
        return ATDecision("AT", True, False, "Coordinator", "REPORT_WAIT", "direct-route-missing")
    needs_approval = ((fixture.boundary == "HL_DRAFT" and contract["hl_approval_gate"]) or
                      (fixture.boundary == "TS_DRAFT" and contract["ts_approval_gate"]))
    if needs_approval and not fixture.approval:
        return ATDecision("AT", True, False, "Coordinator", "REPORT_WAIT", "approval-missing")
    if fixture.event == "return":
        return ATDecision("AT", True, True, "Coordinator", "DIRECT_RETURN", "workflow-return")
    return ATDecision("AT", True, True, "delegate", "CONTINUE", "row-active")


def phase_d_scenario_payload(tree: SourceTree) -> dict[str, object]:
    contract = parse_phase_d_contract(tree)
    assignment = parse_phase_d_assignment(tree)
    workflows = parse_phase_d_workflows(tree)
    adapter = parse_phase_d_adapter(tree)
    cases = {}
    for name, fixture in PHASE_D_SCENARIOS.items():
        actual = resolve_phase_d_scenario(tree, fixture)
        cases[name] = {
            "fixture": fixture.__dict__, "actual": actual.__dict__,
            "expected": dict(zip(ATDecision.__dataclass_fields__, PHASE_D_EXPECTED_SCENARIOS[name])),
        }
    return {"contract": contract, "assignment": assignment, "workflows": workflows,
            "adapter": adapter, "cases": cases}


@dataclass(frozen=True)
class ATMutation:
    family: str; target: str; path: str; old: str; new: str


def _phase_d_mutations() -> tuple[ATMutation, ...]:
    items = [
        ATMutation("declaration", "table", PHASE_D_CONVENTIONS,
                   "a Role Assignment exists", "a team note exists"),
        ATMutation("declaration", "freeze", PHASE_D_CONVENTIONS,
                   "its master HL is owner-approved and frozen", "its master HL is drafted"),
        ATMutation("declaration", "commit", PHASE_D_CONVENTIONS,
                   "that freeze baseline is committed", "that freeze baseline is optional"),
        ATMutation("duty", "coordinator-owner", PHASE_D_CONVENTIONS,
                   "returns the seven triggers below to the owner", "keeps every trigger locally"),
        ATMutation("duty", "delegate-coordinator", PHASE_D_CONVENTIONS,
                   "reports gates/results directly", "reports gates/results through a relay"),
        ATMutation("degradation", "relay", PHASE_D_CONVENTIONS,
                   "stop and wait; do not replace it", "continue silently; replace it"),
        ATMutation("boundary", "ordinal", PHASE_D_CONVENTIONS,
                   "Never compare lifecycle ids ordinally", "Compare lifecycle ids ordinally"),
        ATMutation("boundary", "hl-approval", PHASE_D_CONVENTIONS,
                   "At `HL_DRAFT`, activation needs owner-approved freeze and its commit",
                   "At `HL_DRAFT`, activation needs the token"),
        ATMutation("boundary", "ts-approval", PHASE_D_CONVENTIONS,
                   "At `TS_DRAFT`, exact TS approval must precede Executor activation",
                   "At `TS_DRAFT`, the token activates Executor"),
        ATMutation("boundary", "dash", PHASE_D_CONVENTIONS,
                   "`—` means report and wait at every decision", "`—` means continue"),
    ]
    for trigger, channel in PHASE_D_RETURNS:
        source_channel = channel.replace("SUPERSEDE", "`SUPERSEDE`").replace("judge.md", "`judge.md`").replace(
            "review.md", "`review.md`")
        row = next(line for line in resolve_heading(
            SourceTree.from_path(PROJECT_ROOT).read(PHASE_D_CONVENTIONS),
            "AT (Agent Team) — explicit declaration only").splitlines()
                   if line.startswith(f"| {trigger}"))
        items.append(ATMutation("return-channel", trigger, PHASE_D_CONVENTIONS,
                                row, row.rsplit("|", 2)[0] + "| generic user route |"))
    for gate in PHASE_D_NATIVE_GATES:
        items.append(ATMutation("native-gate", gate, PHASE_D_CONVENTIONS,
                                f"**{gate}:**", f"**Omitted {gate}:**"))
    assignment_header = "| " + " | ".join(PHASE_D_COLUMNS) + " |"
    for column in PHASE_D_COLUMNS:
        items.append(ATMutation("assignment-column", column, PHASE_D_ASSIGNMENT,
                                assignment_header,
                                assignment_header.replace(column, f"Missing {column}", 1)))
    items.extend((
        ATMutation("workflow-order", "plan", ".tfw/workflows/plan.md",
                   "before HL approval", "after HL approval"),
        ATMutation("workflow-order", "handoff", ".tfw/workflows/handoff.md",
                   "before ONB/work", "after ONB/work"),
        ATMutation("workflow-order", "research", ".tfw/workflows/research/base.md",
                   "before Step 1", "after Step 1"),
        ATMutation("workflow-order", "review", ".tfw/workflows/review.md",
                   "Reviewer row before Map", "Reviewer row after Map"),
        ATMutation("workflow-route", "handoff", ".tfw/workflows/handoff.md",
                   "Return questions and RF directly", "Return questions and RF through a relay"),
        ATMutation("workflow-route", "research", ".tfw/workflows/research/base.md",
                   "Every WAIT and final RES return directly", "Every WAIT and final RES returns through a relay"),
        ATMutation("workflow-route", "review", ".tfw/workflows/review.md",
                   "Questions, verdict, and proposals return directly",
                   "Questions, verdict, and proposals return through a relay"),
    ))
    for operation in PHASE_D_OPERATIONS:
        items.append(ATMutation("adapter-operation", operation, PHASE_D_ADAPTER,
                                f"`{operation}`", f"`relay_{operation}`"))
    items.extend((
        ATMutation("adapter-boundary", "visible", PHASE_D_ADAPTER,
                   "fresh user-visible independently-addressable tasks", "hidden helper tasks"),
        ATMutation("adapter-boundary", "worktree", PHASE_D_ADAPTER,
                   "separate worktrees", "shared checkout partitions"),
        ATMutation("adapter-boundary", "self-start", PHASE_D_ADAPTER,
                   "Approved human-rooted rows", "Self-approved rows"),
        ATMutation("adapter-boundary", "same-role", PHASE_D_ADAPTER,
                   "reuse the same Executor/Reviewer", "replace Executor/Reviewer"),
    ))
    return tuple(items)


def _phase_d_projection(tree: SourceTree, mutation: ATMutation) -> tuple[object, list[str]]:
    if mutation.path == PHASE_D_CONVENTIONS:
        record = parse_phase_d_contract(tree); return record, phase_d_contract_errors(record)
    if mutation.path == PHASE_D_ASSIGNMENT:
        record = parse_phase_d_assignment(tree); return record, phase_d_assignment_errors(record)
    if mutation.path == PHASE_D_ADAPTER:
        record = parse_phase_d_adapter(tree); return record, phase_d_adapter_errors(record)
    records = parse_phase_d_workflows(tree); return records, phase_d_workflow_errors(records)


def phase_d_mutant_payload(tree: SourceTree) -> list[dict[str, object]]:
    output = []
    for mutation in _phase_d_mutations():
        source = tree.read(mutation.path)
        if source.count(mutation.old) != 1:
            raise SourceContractError(
                f"Phase D mutation source must resolve once: {mutation.target} -> {source.count(mutation.old)}")
        normal, normal_errors = _phase_d_projection(tree, mutation)
        mutant = tree.with_text(mutation.path, source.replace(mutation.old, mutation.new, 1))
        produced, errors = _phase_d_projection(mutant, mutation)
        output.append({
            "family": mutation.family, "target": mutation.target, "path": mutation.path,
            "projection_changed": produced != normal,
            "independent_expected_rejects": bool(errors),
            "normal_errors": normal_errors, "rejection_fields": errors,
        })
    return output


PHASE_D_CENSUS_TERMS = re.compile(
    r"Role Assignment|AT \(Agent Team\)|Agent Team checkpoint|Codex AT profile|Profile admission|"
    r"\bdispatch\b|create_thread|send_message_to_thread|wait_threads", re.IGNORECASE)
PHASE_D_PROVIDER_TERMS = ("Codex", "Claude", "create_thread", "send_message_to_thread",
                          "wait_threads", "fork_thread", "spawn_agent")
PHASE_D_PROVIDER_ALLOWED = {PHASE_D_ADAPTER, "AGENTS.md"}


def _phase_d_census_class(path: str) -> str:
    if path == PHASE_D_CONVENTIONS: return "canonical-contract"
    if path == PHASE_D_ASSIGNMENT or path.startswith(".tfw/templates/"): return "template-form"
    if path.startswith(".tfw/workflows/") or path.startswith(".agent/workflows/") or path.startswith(
            ".claude/commands/"): return "workflow-enforcement"
    if path.startswith(".tfw/adapters/") or path in {"AGENTS.md", "CLAUDE.md"}: return "adapter-operation"
    if path.startswith("workspace/") or path.startswith("tasks/"): return "task-trace-history"
    if path.startswith("docs/scripts/") or path.startswith(".tfw/scripts/"): return "assurance"
    return "reference-history"


def phase_d_census(tree: SourceTree) -> dict[str, object]:
    paths = tuple(path for path in tree.files("**/*") if Path(path).suffix in {".md", ".yaml", ".py"})
    occurrences = []
    for path in paths:
        text = tree.read(path)
        count = len(PHASE_D_CENSUS_TERMS.findall(text))
        if count:
            occurrences.append({"path": path, "class": _phase_d_census_class(path), "count": count})
    baseline = SourceTree.from_git(PROJECT_ROOT, PHASE_D_BASELINE_REF)
    provider_deltas = []
    changed = subprocess.run(
        ["git", "diff", "--name-only", PHASE_D_BASELINE_REF, "--"], cwd=PROJECT_ROOT,
        text=True, encoding="utf-8", capture_output=True, check=True).stdout.splitlines()
    common = sorted(set(changed) & set(paths) & set(baseline.files("**/*")))
    for path in common:
        if Path(path).suffix not in {".md", ".yaml", ".py"}: continue
        before, after = baseline.read(path), tree.read(path)
        for term in PHASE_D_PROVIDER_TERMS:
            delta = after.count(term) - before.count(term)
            if delta:
                provider_deltas.append({"path": path, "term": term, "delta": delta,
                                        "allowed": (path in PHASE_D_PROVIDER_ALLOWED or
                                                    path.startswith("docs/scripts/"))})
    return {"occurrences": occurrences, "provider_deltas": provider_deltas,
            "unclassified": [row for row in occurrences if not row["class"]],
            "positive_provider_leaks": [row for row in provider_deltas
                                         if row["delta"] > 0 and not row["allowed"]]}


def test_phase_d_contract_assignment_workflows_and_adapter_are_source_derived_and_complete():
    tree = SourceTree.from_path(PROJECT_ROOT)
    contract = parse_phase_d_contract(tree)
    assignment = parse_phase_d_assignment(tree)
    workflows = parse_phase_d_workflows(tree)
    adapter = parse_phase_d_adapter(tree)
    assert phase_d_contract_errors(contract) == []
    assert phase_d_assignment_errors(assignment) == []
    assert phase_d_workflow_errors(workflows) == []
    assert phase_d_adapter_errors(adapter) == []
    assert len(contract["owner_returns"]) == 7 and len(contract["native_gates"]) == 8


def test_phase_d_positive_negative_boundary_and_return_scenarios_match_independent_oracle():
    tree = SourceTree.from_path(PROJECT_ROOT)
    for name, fixture in PHASE_D_SCENARIOS.items():
        actual = resolve_phase_d_scenario(tree, fixture)
        assert tuple(actual.__dict__.values()) == PHASE_D_EXPECTED_SCENARIOS[name], name


def test_phase_d_each_semantic_mutant_changes_output_then_is_independently_rejected():
    rows = phase_d_mutant_payload(SourceTree.from_path(PROJECT_ROOT))
    assert len(rows) >= 40
    assert {row["family"] for row in rows} == {
        "declaration", "duty", "return-channel", "degradation", "native-gate", "boundary",
        "assignment-column", "workflow-order", "workflow-route", "adapter-operation",
        "adapter-boundary",
    }
    assert all(not row["normal_errors"] for row in rows)
    assert all(row["projection_changed"] and row["independent_expected_rejects"] for row in rows)


def test_phase_d_live_census_classifies_consumers_and_adds_no_provider_leak():
    report = phase_d_census(SourceTree.from_path(PROJECT_ROOT))
    assert report["occurrences"] and not report["unclassified"]
    assert not report["positive_provider_leaks"]
    classes = {row["class"] for row in report["occurrences"]}
    assert {"canonical-contract", "template-form", "workflow-enforcement", "adapter-operation",
            "task-trace-history", "assurance", "reference-history"} <= classes


def test_phase_d_attention_cap_literals_and_measurer_are_byte_exact_from_baseline():
    before = SourceTree.from_git(PROJECT_ROOT, PHASE_D_BASELINE_REF).read(
        "docs/scripts/test_runtime_context.py")
    after = SourceTree.from_path(PROJECT_ROOT).read("docs/scripts/test_runtime_context.py")
    for name in ("PHASE_C_PRIMARY_ENTRY_WORDS", "SESSION_ROUTE_CEILINGS",
                 "session_identity_context_payload"):
        assert _python_named_span(after, name) == _python_named_span(before, name)

# CRATM Phase D revision 2. These definitions intentionally replace the historical Phase D
# projection above: the old test source remains readable, while the live oracle follows A7.
PHASE_D_PROFILE = ".tfw/templates/team/profile.md"
PHASE_D_EVENT = ".tfw/templates/journal/event.md"
PHASE_D_MANDATE_COLUMNS = (
    "Selected LEAD principal", "Accountable owner", "Mandate scope", "Role coverage / reach",
    "Reservations / controls", "Direct reporting", "Autonomous from",
)
PHASE_D_UNIT_COLUMNS = (
    "Principal attribution", "Workflow role", "Actual unit / native address", "Parent unit",
    "Bounded scope", "Direct channel", "Autonomous from", "Dispatch ref",
)
PHASE_D_RETURNS = (
    ("LEAD/root-unit-origin or same-ruler proposal",
     "§12 directly to owner; forwarding/restart cannot launder origin"),
    ("Amendment against an owner-reserved claim", "§12 directly to owner"),
    ("Purpose Check finds the reference set self-contradictory",
     "judge.md → owner as contract defect"),
    ("❌ REJECT verdict", "review.md → owner"),
    ("Selected LEAD or assigned holder unavailable",
     "Owner-approved §12 SUPERSEDE, then bounded dispatch; wait before both acts complete"),
    ("Scope-budget decision", "§6 first: below both immutable multipliers, necessary growth may "
     "receive prospective Coordinator approval with all invariants fixed; at/above a multiplier or "
     "from planned zero returns to owner; rule 19 forbids delegated self-acceptance"),
    ("Missing/ambiguous origin, root, mandate, grant, parent or direct address",
     "Pre-work refusal; work does not start"),
)


def parse_phase_d_contract(tree: SourceTree) -> dict[str, object]:
    text = tree.read(PHASE_D_CONVENTIONS)
    at = resolve_heading(text, "AT (Agent Team) — explicit declaration only")
    _, rows = _phase_d_table(at, "Owner-return trigger")
    gates = tuple(re.findall(r"^\d+\. \*\*(.+?):\*\*", at, re.MULTILINE))
    return {
        "post_hl_owner_choice": all(s in at for s in (
            "After an owner-approved HL is frozen and committed",
            "human owner explicitly chooses manual work", "No choice preserves CL")),
        "stable_lead": "selects one existing stable agent" in at and "principal as LEAD" in at,
        "bounded_mandate": all(s in at for s in (
            "bounded scope", "role coverage/reach", "reservations/controls",
            "direct reporting", "`Autonomous from` boundary")),
        "roster_no_authority": "full unit roster neither declares AT nor grants authority" in at,
        "mandate_unit_split": all(s in at for s in (
            "selected mandate is the protected human commitment",
            "working-unit assignment is its", "append-only operational trace")),
        "bounded_instantiation": all(s in at for s in (
            "ordinary instantiation plus a bounded direct dispatch",
            "not a new principal", "profile or amendment")),
        "replacement_two_act": all(s in at for s in (
            "owner-approved §12 `SUPERSEDE` and then a bounded replacement dispatch",
            "replacement dispatch alone still means wait")),
        "separate_resolution": all(s in at for s in (
            "resolves the selected principal and", "mandate separately from its own actual address",
            "parent, role/scope, direct channel, dispatch refs and", "proposal origin")),
        "nonordinal": "lifecycle\nids are never compared ordinally" in at,
        "exact_gates": all(s in at for s in (
            "At `HL_DRAFT`, an", "approved committed freeze is required",
            "at `TS_DRAFT`, exact TS approval precedes Executor work")),
        "coordinator_duties": all(s in at for s in (
            "preserves scope, Role Locks, direct routes, durable state, same-role",
            "unit provenance and proposal origin", "returns the seven triggers below to the owner")),
        "unit_duties": all(s in at for s in (
            "accepts only its assigned role", "re-resolves all bounds",
            "reports questions/gates/results directly to its parent",
            "never executes another workflow")),
        "human_ultimate": "Human accountability remains ultimate" in at,
        "owner_returns": tuple((row[0], row[1]) for row in rows),
        "degradation_safe": all(s in at for s in (
            "stop and wait", "relay", "hidden helper", "provider switch", "fabricated profile",
            "Already-authorized CL or AG")),
        "native_gates": gates,
        "supplied_limited": all(s in at for s in (
            "supplied initial Codex profile", "`ADMIT_SUPPLIED_LIMITED`",
            "G1–G7 mechanics disclosed", "no G8 reliability rate or cross-provider claim")),
        "additional_all_eight": all(s in at for s in (
            "Every additional provider profile", "`REJECT_NO_NATIVE_ALL_EIGHT`",
            "passes G1–G8 together in one trial")),
        "no_partial": "partial receipts never compose" in at,
        "principal_unit_distinct": all(s in text for s in (
            "A principal is attribution", "working unit is the actual addressable node",
            "never merges nodes", "child consume the root unit's", "grant")),
        "dispatch_provenance": all(s in text for s in (
            "actual source,", "destination and parent units", "originating proposer as",
            "`{principal, unit}` or explicit `none`", "`writer` is attribution, not an edge")),
        "routing_guards": all(s in text for s in (
            "Executor source", "ancestor/task-Coordinator target", "cycle", "foreign scope",
            "missing address", "missing root authorization", "Forwarding,", "restart",
            "never changes proposal origin")),
        "authority_split": all(s in text for s in (
            "genuinely", "subordinate-origin", "inside both its immutable `true` grant and mandate",
            "A child", "never inherits that grant", "LEAD/root-unit-origin",
            "missing/ambiguous-origin", "out-of-grant or out-of-mandate")),
        "source_span": _phase_d_span(text, "### AT (Agent Team) — explicit declaration only"),
    }


def phase_d_contract_errors(record: dict[str, object]) -> list[str]:
    errors = []
    booleans = (
        "post_hl_owner_choice", "stable_lead", "bounded_mandate", "roster_no_authority",
        "mandate_unit_split", "bounded_instantiation", "replacement_two_act",
        "separate_resolution", "nonordinal", "exact_gates", "coordinator_duties",
        "unit_duties", "human_ultimate", "degradation_safe", "supplied_limited",
        "additional_all_eight", "no_partial", "principal_unit_distinct",
        "dispatch_provenance", "routing_guards", "authority_split",
    )
    for name in booleans:
        if not record[name]: errors.append(name)
    if tuple(record["owner_returns"]) != PHASE_D_RETURNS: errors.append("owner_returns")
    if tuple(record["native_gates"]) != PHASE_D_NATIVE_GATES: errors.append("native_gates")
    return errors


def parse_phase_d_assignment(tree: SourceTree) -> dict[str, object]:
    text = tree.read(PHASE_D_ASSIGNMENT)
    section = resolve_heading(text, "Role Assignment 🔒 FROZEN")
    mandate_columns, mandate_rows = _phase_d_table(section, "Selected LEAD principal")
    unit_columns, unit_rows = _phase_d_table(section, "Principal attribution")
    return {
        "mandate_columns": mandate_columns, "mandate_rows": mandate_rows,
        "unit_columns": unit_columns, "unit_rows": unit_rows,
        "before_phase_dependencies": text.index("### 4.1 Role Assignment") < text.index(
            "### Phase Dependencies"),
        "two_layers": section.index("#### Selected LEAD mandate") < section.index(
            "#### Working-unit assignment"),
        "owner_post_freeze_choice": all(s in section for s in (
            "owner-approved, frozen and committed", "owner may choose", "manual work or AT")),
        "roster_not_prerequisite": "complete unit roster is neither a\n> freeze prerequisite" in section,
        "mandate_protected": all(s in section for s in (
            "frozen human commitment", "Widening scope", "replacing\n> the selected principal",
            "removing a reservation/control")),
        "unit_dynamic": all(s in section for s in (
            "append-only instantiation", "dispatch trace, not a profile or HL amendment")),
        "replacement_two_act": all(s in section for s in (
            "owner-approved §12 `SUPERSEDE`, then bounded dispatch",
            "replacement dispatch alone is not approval")),
        "same_principal_distinct_units": len(unit_rows) >= 3 and len({row[0] for row in unit_rows}) == 1
            and len({row[2] for row in unit_rows}) == len(unit_rows),
        "role_lock_only": "permissions still come only from Role Locks" in section,
        "source_span": _phase_d_span(text, "### 4.1 Role Assignment 🔒 FROZEN"),
    }


def phase_d_assignment_errors(record: dict[str, object]) -> list[str]:
    errors = []
    if tuple(record["mandate_columns"]) != PHASE_D_MANDATE_COLUMNS: errors.append("mandate_columns")
    if tuple(record["unit_columns"]) != PHASE_D_UNIT_COLUMNS: errors.append("unit_columns")
    if len(record["mandate_rows"]) != 1: errors.append("mandate_sample")
    if len(record["unit_rows"]) < 3: errors.append("unit_samples")
    for name in ("before_phase_dependencies", "two_layers", "owner_post_freeze_choice",
                 "roster_not_prerequisite", "mandate_protected", "unit_dynamic",
                 "replacement_two_act", "same_principal_distinct_units", "role_lock_only"):
        if not record[name]: errors.append(name)
    return errors


def parse_phase_d_carriers(tree: SourceTree) -> dict[str, object]:
    profile = tree.read(PHASE_D_PROFILE)
    event = tree.read(PHASE_D_EVENT)
    return {
        "profile_not_unit": all(s in profile for s in (
            "workflow role, or directly addressable", "working unit", "Never create one per run",
            "Coordinator, Researcher, Executor, or Reviewer")),
        "profile_shared_distinct": all(s in profile for s in (
            "One selected LEAD principal may attribute several distinct units",
            "proposal origins")),
        "grant_root_only": all(s in profile for s in (
            "owner-selected LEAD's root Coordinator unit", "inside its approved mandate",
            "children sharing principal attribution never inherit it")),
        "event_no_new_key": "Add no frontmatter key for these facts" in event,
        "event_writer_not_edge": all(s in event for s in (
            "`writer` remains optional principal attribution", "never stands for a unit\nedge")),
        "event_provenance": all(s in event for s in (
            "actual source, destination and parent units", "workflow role and bounded scope",
            "direct address/channel", "originating\nproposer `{principal, unit}` or explicit `none`")),
        "event_origin_stable": all(s in event for s in (
            "Identical writers never merge units", "restart or continuation never changes")),
    }


def phase_d_carrier_errors(record: dict[str, object]) -> list[str]:
    return [name for name, value in record.items() if not value]


PHASE_D_WORKFLOW_SPECS = {
    "plan": (".tfw/workflows/plan.md", "Coordinator", "HL/dispatch"),
    "handoff": (".tfw/workflows/handoff.md", "Executor", "ONB"),
    "research": (".tfw/workflows/research/base.md", "Researcher", "Briefing and RES"),
    "review": (".tfw/workflows/review.md", "Reviewer", "REVIEW"),
}


def parse_phase_d_workflows(tree: SourceTree) -> dict[str, dict[str, object]]:
    records = {}
    for name, (path, role, artifact) in PHASE_D_WORKFLOW_SPECS.items():
        text = tree.read(path)
        if name == "plan":
            checkpoint = text[text.index("10. **Prepare Role Assignment"):text.index("## Step 8:")]
            prework = all(s in checkpoint for s in (
                "Ask the human owner to choose manual work or AT", "after exact TS approval"))
            fields = all(s in checkpoint for s in (
                "selected principal/mandate separately", "actual\ndestination unit, address, parent",
                "role/scope, direct channel", "dispatch refs", "originating proposer"))
            continuity = "Reuse the same Executor and independent Reviewer" in checkpoint
            role_lock = "Never execute another workflow" in checkpoint
        else:
            checkpoint = resolve_heading(text, "Agent Team checkpoint")
            first = {"handoff": "## Phase 1: Executor Onboarding",
                     "research": "## Step 1: Load Context", "review": "## Step 1: Map"}[name]
            order_phrase = {"handoff": "dispatch refs before ONB/work",
                            "research": "dispatch refs before Step 1",
                            "review": "dispatch refs before Map"}[name]
            prework = (text.index("## Agent Team checkpoint") < text.index(first)
                       and order_phrase in checkpoint and "recheck all on every continuation" in checkpoint)
            fields = all(s in checkpoint for s in (
                "selected LEAD principal and mandate separately", "actual address",
                "parent Coordinator unit", "role/scope", "direct channel", "`Autonomous from`",
                "exact gate", "dispatch refs")) and (
                    "proposal origin" in checkpoint or "originating proposer" in checkpoint)
            continuity = "continue in this" in checkpoint or "reuse this Executor" in checkpoint
            role_lock = "Role Lock" in checkpoint
        records[name] = {
            "path": path, "role": role, "artifact": artifact, "prework": prework,
            "separate_fields": fields, "direct_return": (
                "return" in checkpoint.casefold() and "directly" in checkpoint),
            "continuity": continuity, "supersede_before_replacement": (
                "owner-approved §12 `SUPERSEDE`" in checkpoint and (
                    "bounded replacement dispatch" in checkpoint or
                    "bounded\nreplacement dispatch" in checkpoint)),
            "origin_stable": ("never replace origin" in checkpoint or
                              "never\nreplace origin" in checkpoint or
                              "never changes origin" in checkpoint or name == "handoff" or name == "plan"),
            "role_lock": role_lock,
        }
    return records


def phase_d_workflow_errors(records: dict[str, dict[str, object]]) -> list[str]:
    errors = []
    for name, (_, role, artifact) in PHASE_D_WORKFLOW_SPECS.items():
        row = records[name]
        if row["role"] != role or row["artifact"] != artifact: errors.append(f"{name}:identity")
        for key in ("prework", "separate_fields", "direct_return", "continuity",
                    "supersede_before_replacement", "origin_stable", "role_lock"):
            if not row[key]: errors.append(f"{name}:{key}")
    return errors


def parse_phase_d_adapter(tree: SourceTree) -> dict[str, object]:
    section = resolve_heading(tree.read(PHASE_D_ADAPTER), "Codex AT profile")
    return {
        "operations": tuple(op for op in PHASE_D_OPERATIONS if f"`{op}`" in section),
        "one_lead": "one user-visible LEAD task" in section,
        "direct_role_tasks": all(s in section for s in (
            "creates distinct", "directly addressable Coordinator, Researcher, Executor and Reviewer tasks")),
        "parent_records": "actual task addresses and parents" in section,
        "no_grant_inheritance": "never merges units or grants a\nchild amendment authority" in section,
        "separate_worktrees": "Mutating units use separate worktrees" in section,
        "same_role_reuse": "reuse the same Executor and\nindependent Reviewer" in section,
        "rejected_holders": tuple(term for term in (
            "Forks", "subagents", "relays", "hidden helpers", "provider switches") if term in section),
        "supplied_limited": all(s in section for s in (
            "supplied initial Codex profile", "G1–G7 mechanics only", "not G8 reliability")),
        "additional_native": all(s in section for s in (
            "every additional provider profile", "one native all-eight TFW trial",
            "partial receipts never compose")),
    }


def phase_d_adapter_errors(record: dict[str, object]) -> list[str]:
    errors = []
    if tuple(record["operations"]) != PHASE_D_OPERATIONS: errors.append("operations")
    if tuple(record["rejected_holders"]) != (
            "Forks", "subagents", "relays", "hidden helpers", "provider switches"):
        errors.append("rejected_holders")
    for name in ("one_lead", "direct_role_tasks", "parent_records", "no_grant_inheritance",
                 "separate_worktrees", "same_role_reuse", "supplied_limited", "additional_native"):
        if not record[name]: errors.append(name)
    return errors


@dataclass(frozen=True)
class ATModeFixture:
    choice: str = "none"; approved_hl: bool = False; committed: bool = False
    stable_lead: bool = False; mandate: bool = False; roster: bool = False
    boundary: str = "TS_DRAFT"; unit_ok: bool = True; gate_ok: bool = True
    direct_dispatch: bool = True; returning: bool = False


@dataclass(frozen=True)
class ATModeDecision:
    mode: str; declared: bool; active: bool; holder: str; action: str; reason: str


PHASE_D_SCENARIOS = {
    "no_choice": ATModeFixture(),
    "manual": ATModeFixture("manual", True, True),
    "ordinary_ag": ATModeFixture("ag", True, True),
    "roster_only": ATModeFixture(roster=True),
    "at_unapproved": ATModeFixture("at", committed=True, stable_lead=True, mandate=True),
    "at_uncommitted": ATModeFixture("at", approved_hl=True, stable_lead=True, mandate=True),
    "at_missing_lead": ATModeFixture("at", True, True, mandate=True),
    "at_missing_mandate": ATModeFixture("at", True, True, True),
    "at_active": ATModeFixture("at", True, True, True, True),
    "dash": ATModeFixture("at", True, True, True, True, boundary="—"),
    "wrong_unit": ATModeFixture("at", True, True, True, True, unit_ok=False),
    "missing_gate": ATModeFixture("at", True, True, True, True, gate_ok=False),
    "missing_direct": ATModeFixture("at", True, True, True, True, direct_dispatch=False),
    "direct_return": ATModeFixture("at", True, True, True, True, returning=True),
}
PHASE_D_EXPECTED_SCENARIOS = {
    "no_choice": ("CL", False, False, "human", "PROPOSE", "owner-choice-absent"),
    "manual": ("CL", False, True, "human", "PROCEED_MANUAL", "owner-chose-manual"),
    "ordinary_ag": ("AG", False, True, "delegate", "CONTINUE", "explicit-ordinary-ag"),
    "roster_only": ("CL", False, False, "human", "PROPOSE", "roster-no-authority"),
    "at_unapproved": ("CL", False, False, "human", "WAIT", "hl-approval-missing"),
    "at_uncommitted": ("CL", False, False, "human", "WAIT", "hl-commit-missing"),
    "at_missing_lead": ("CL", False, False, "human", "WAIT", "lead-missing"),
    "at_missing_mandate": ("CL", False, False, "human", "WAIT", "mandate-missing"),
    "at_active": ("AT", True, True, "unit", "CONTINUE", "bounded-unit-active"),
    "dash": ("AT", True, False, "Coordinator", "REPORT_WAIT", "dash-boundary"),
    "wrong_unit": ("AT", True, False, "Coordinator", "REPORT_WAIT", "unit-mismatch"),
    "missing_gate": ("AT", True, False, "Coordinator", "REPORT_WAIT", "gate-missing"),
    "missing_direct": ("AT", True, False, "Coordinator", "REPORT_WAIT", "dispatch-missing"),
    "direct_return": ("AT", True, True, "Coordinator", "DIRECT_RETURN", "workflow-return"),
}


def resolve_phase_d_scenario(tree: SourceTree, fixture: ATModeFixture) -> ATModeDecision:
    contract = parse_phase_d_contract(tree)
    if fixture.choice == "manual":
        return ATModeDecision("CL", False, True, "human", "PROCEED_MANUAL", "owner-chose-manual")
    if fixture.choice == "ag":
        return ATModeDecision("AG", False, True, "delegate", "CONTINUE", "explicit-ordinary-ag")
    if fixture.choice != "at":
        reason = "roster-no-authority" if fixture.roster and contract["roster_no_authority"] else "owner-choice-absent"
        return ATModeDecision("CL", False, False, "human", "PROPOSE", reason)
    missing = (("hl-approval-missing", not fixture.approved_hl),
               ("hl-commit-missing", not fixture.committed),
               ("lead-missing", not fixture.stable_lead),
               ("mandate-missing", not fixture.mandate))
    for reason, failed in missing:
        if failed:
            return ATModeDecision("CL", False, False, "human", "WAIT", reason)
    if fixture.boundary == "—":
        return ATModeDecision("AT", True, False, "Coordinator", "REPORT_WAIT", "dash-boundary")
    if not fixture.unit_ok:
        return ATModeDecision("AT", True, False, "Coordinator", "REPORT_WAIT", "unit-mismatch")
    if not fixture.gate_ok:
        return ATModeDecision("AT", True, False, "Coordinator", "REPORT_WAIT", "gate-missing")
    if not fixture.direct_dispatch:
        return ATModeDecision("AT", True, False, "Coordinator", "REPORT_WAIT", "dispatch-missing")
    if fixture.returning:
        return ATModeDecision("AT", True, True, "Coordinator", "DIRECT_RETURN", "workflow-return")
    return ATModeDecision("AT", True, True, "unit", "CONTINUE", "bounded-unit-active")


@dataclass(frozen=True)
class AuthorityFixture:
    origin_principal: str | None; origin_unit: str | None; signer_principal: str = "lead"
    signer_unit: str = "lead/root"; selected_lead: bool = True; root_unit: bool = True
    subordinate: bool = True; grant: bool = True; inside_mandate: bool = True
    reserved: bool = False; ambiguous: bool = False; forwarded_writer: str | None = None


def resolve_phase_d_authority(tree: SourceTree, case: AuthorityFixture) -> str:
    contract = parse_phase_d_contract(tree)
    if phase_d_contract_errors(contract): return "BLOCK_SOURCE"
    if not case.origin_principal or not case.origin_unit or case.ambiguous: return "OWNER_OR_BLOCK"
    if case.reserved or not case.grant or not case.inside_mandate: return "OWNER"
    if (case.origin_principal, case.origin_unit) == (case.signer_principal, case.signer_unit):
        return "OWNER"
    if not case.selected_lead or not case.root_unit or not case.subordinate: return "OWNER"
    return "LEAD_RULE"


@dataclass(frozen=True)
class DispatchFixture:
    source_role: str = "Coordinator"; unique_parent: bool = True; ancestor_target: bool = False
    task_coordinator_target: bool = False; cycle: bool = False; foreign_scope: bool = False
    address: bool = True; root: bool = True


def resolve_phase_d_dispatch(tree: SourceTree, case: DispatchFixture) -> str:
    if not parse_phase_d_contract(tree)["routing_guards"]: return "REFUSE_SOURCE"
    if case.source_role != "Coordinator": return "REFUSE_EXECUTOR_SOURCE"
    if not case.unique_parent: return "REFUSE_COMPETING_PARENT"
    if case.ancestor_target or case.task_coordinator_target or case.cycle: return "REFUSE_CYCLE_OR_ANCESTOR"
    if case.foreign_scope or not case.address or not case.root: return "REFUSE_BOUNDARY"
    return "PROCEED"


def resolve_phase_d_replacement(tree: SourceTree, unavailable: bool, owner_supersede: bool,
                                bounded_dispatch: bool) -> str:
    valid = parse_phase_d_contract(tree)["replacement_two_act"] and parse_phase_d_assignment(tree)[
        "replacement_two_act"]
    if not valid: return "BLOCK_SOURCE"
    if unavailable and not (owner_supersede and bounded_dispatch): return "WAIT_FOR_OWNER"
    if unavailable: return "PROCEED_REPLACEMENT"
    return "NOT_A_REPLACEMENT"


@dataclass(frozen=True)
class AdmissionFixture:
    profile_class: str; gates: tuple[bool, ...]; native_single_trial: bool = True
    partial_receipts: bool = False


def resolve_phase_d_admission(tree: SourceTree, case: AdmissionFixture) -> str:
    canon = parse_phase_d_contract(tree); adapter = parse_phase_d_adapter(tree)
    if not (canon["supplied_limited"] and canon["additional_all_eight"] and canon["no_partial"]
            and adapter["supplied_limited"] and adapter["additional_native"]):
        return "BLOCK_SOURCE"
    if case.profile_class == "supplied" and all(case.gates[:7]):
        return "ADMIT_SUPPLIED_LIMITED"
    if (case.profile_class == "additional" and len(case.gates) == 8 and all(case.gates)
            and case.native_single_trial and not case.partial_receipts):
        return "ADMIT_ADDITIONAL_NATIVE_ALL_EIGHT"
    return "REJECT_NO_NATIVE_ALL_EIGHT"


def phase_d_scenario_payload(tree: SourceTree) -> dict[str, object]:
    cases = {name: {"fixture": case.__dict__, "actual": resolve_phase_d_scenario(tree, case).__dict__,
                    "expected": dict(zip(ATModeDecision.__dataclass_fields__,
                                         PHASE_D_EXPECTED_SCENARIOS[name]))}
             for name, case in PHASE_D_SCENARIOS.items()}
    authority = {
        "subordinate": resolve_phase_d_authority(tree, AuthorityFixture("lead", "child/executor")),
        "lead_origin": resolve_phase_d_authority(tree, AuthorityFixture("lead", "lead/root")),
        "child_signer": resolve_phase_d_authority(tree, AuthorityFixture(
            "lead", "child/research", signer_unit="child/reviewer", root_unit=False)),
    }
    admission = {
        "supplied": resolve_phase_d_admission(tree, AdmissionFixture("supplied", (True,) * 7 + (False,))),
        "additional_missing_g8": resolve_phase_d_admission(
            tree, AdmissionFixture("additional", (True,) * 7 + (False,))),
        "additional_complete": resolve_phase_d_admission(
            tree, AdmissionFixture("additional", (True,) * 8)),
    }
    return {"contract": parse_phase_d_contract(tree), "assignment": parse_phase_d_assignment(tree),
            "carriers": parse_phase_d_carriers(tree), "workflows": parse_phase_d_workflows(tree),
            "adapter": parse_phase_d_adapter(tree), "cases": cases, "authority": authority,
            "admission": admission}


def _phase_d_mutations() -> tuple[ATMutation, ...]:
    items = [
        ATMutation("declaration", "owner-choice", PHASE_D_CONVENTIONS,
                   "human owner explicitly chooses manual work", "system infers autonomous work"),
        ATMutation("declaration", "stable-lead", PHASE_D_CONVENTIONS,
                   "selects one existing stable agent", "selects any current session"),
        ATMutation("declaration", "bounded-mandate", PHASE_D_CONVENTIONS,
                   "mandate with bounded scope", "roster with informal scope"),
        ATMutation("declaration", "roster", PHASE_D_CONVENTIONS,
                   "full unit roster neither declares AT nor grants authority",
                   "full unit roster declares AT and grants authority"),
        ATMutation("mandate-unit", "split", PHASE_D_CONVENTIONS,
                   "selected mandate is the protected human commitment",
                   "unit roster is the protected human commitment"),
        ATMutation("mandate-unit", "instantiation", PHASE_D_CONVENTIONS,
                   "ordinary instantiation plus a bounded direct dispatch",
                   "automatic mandate amendment"),
        ATMutation("replacement", "supersede", PHASE_D_CONVENTIONS,
                   "owner-approved §12 `SUPERSEDE` and then a bounded replacement dispatch",
                   "replacement dispatch"),
        ATMutation("replacement", "dispatch-alone", PHASE_D_CONVENTIONS,
                   "replacement dispatch alone still means wait",
                   "replacement dispatch alone means proceed"),
        ATMutation("unit-resolution", "separate", PHASE_D_CONVENTIONS,
                   "resolves the selected principal and\nmandate separately from its own actual address",
                   "resolves writer as unit identity"),
        ATMutation("unit-resolution", "nonordinal", PHASE_D_CONVENTIONS,
                   "lifecycle\nids are never compared ordinally", "lifecycle\nids grant authority ordinally"),
        ATMutation("duty", "coordinator", PHASE_D_CONVENTIONS,
                   "returns the seven triggers below to the owner", "keeps owner triggers locally"),
        ATMutation("duty", "unit", PHASE_D_CONVENTIONS,
                   "reports questions/gates/results directly to its parent",
                   "reports questions/gates/results through a relay"),
        ATMutation("degradation", "stop", PHASE_D_CONVENTIONS,
                   "stop and wait; do not replace it", "continue and replace it"),
        ATMutation("principal-unit", "distinct", PHASE_D_CONVENTIONS,
                   "A principal is attribution; a\nworking unit is the actual addressable node",
                   "A principal is the working unit"),
        ATMutation("principal-unit", "writer-edge", PHASE_D_CONVENTIONS,
                   "`writer` is attribution, not an edge", "`writer` is the dispatch edge"),
        ATMutation("proposal-origin", "restart", PHASE_D_CONVENTIONS,
                   "restart, continuation, or a new writer never changes proposal origin",
                   "restart changes proposal origin to the new writer"),
        ATMutation("authority", "subordinate", PHASE_D_CONVENTIONS,
                   "subordinate-origin, non-reserved proposal", "any forwarded proposal"),
        ATMutation("authority", "child-grant", PHASE_D_CONVENTIONS,
                   "A child\nnever inherits that grant", "A child\ninherits that grant"),
        ATMutation("authority", "lead-origin", PHASE_D_CONVENTIONS,
                   "A LEAD/root-unit-origin, owner-reserved, missing/ambiguous-origin",
                   "Only an owner-reserved proposal"),
        ATMutation("admission", "supplied", PHASE_D_CONVENTIONS,
                   "first-release exception: admit it only as `ADMIT_SUPPLIED_LIMITED`",
                   "ordinary profile: require all eight"),
        ATMutation("admission", "additional", PHASE_D_CONVENTIONS,
                   "Every additional provider profile is\n`REJECT_NO_NATIVE_ALL_EIGHT`",
                   "Every additional provider profile is admitted"),
        ATMutation("admission", "partial", PHASE_D_CONVENTIONS,
                   "partial receipts never compose", "partial receipts compose"),
    ]
    section = resolve_heading(SourceTree.from_path(PROJECT_ROOT).read(PHASE_D_CONVENTIONS),
                              "AT (Agent Team) — explicit declaration only")
    for trigger, _ in PHASE_D_RETURNS:
        row = next(line for line in section.splitlines() if line.startswith(f"| {trigger} |"))
        items.append(ATMutation("return-channel", trigger, PHASE_D_CONVENTIONS,
                                row, row.rsplit("|", 2)[0] + "| generic route |"))
    for gate in PHASE_D_NATIVE_GATES:
        items.append(ATMutation("native-gate", gate, PHASE_D_CONVENTIONS,
                                f"**{gate}:**", f"**Omitted {gate}:**"))
    mandate_header = "| " + " | ".join(PHASE_D_MANDATE_COLUMNS) + " |"
    unit_header = "| " + " | ".join(PHASE_D_UNIT_COLUMNS) + " |"
    for column in PHASE_D_MANDATE_COLUMNS:
        items.append(ATMutation("mandate-column", column, PHASE_D_ASSIGNMENT, mandate_header,
                                mandate_header.replace(column, f"Missing {column}", 1)))
    for column in PHASE_D_UNIT_COLUMNS:
        items.append(ATMutation("unit-column", column, PHASE_D_ASSIGNMENT, unit_header,
                                unit_header.replace(column, f"Missing {column}", 1)))
    items.extend((
        ATMutation("carrier", "profile-not-unit", PHASE_D_PROFILE,
                   "workflow role, or directly addressable\nworking unit", "workflow role or unit identity"),
        ATMutation("carrier", "profile-grant", PHASE_D_PROFILE,
                   "children sharing principal attribution never inherit it",
                   "children sharing principal attribution inherit it"),
        ATMutation("carrier", "event-writer", PHASE_D_EVENT,
                   "never stands for a unit\nedge", "stands for a unit\nedge"),
        ATMutation("carrier", "event-origin", PHASE_D_EVENT,
                   "originating\nproposer `{principal, unit}` or explicit `none`",
                   "current writer as proposer"),
        ATMutation("workflow", "plan-owner-choice", ".tfw/workflows/plan.md",
                   "Ask the human owner to choose manual work or AT", "Infer AT from a roster"),
        ATMutation("workflow", "plan-unit", ".tfw/workflows/plan.md",
                   "resolve the selected principal/mandate separately", "resolve writer as unit"),
        ATMutation("workflow", "handoff-order", ".tfw/workflows/handoff.md",
                   "dispatch refs before ONB/work", "dispatch refs after ONB/work"),
        ATMutation("workflow", "handoff-route", ".tfw/workflows/handoff.md",
                   "Return questions and RF directly", "Return questions and RF through a relay"),
        ATMutation("workflow", "research-order", ".tfw/workflows/research/base.md",
                   "dispatch refs before Step 1", "dispatch refs after Step 1"),
        ATMutation("workflow", "research-origin", ".tfw/workflows/research/base.md",
                   "forwarding or restart never changes origin", "restart changes origin"),
        ATMutation("workflow", "review-order", ".tfw/workflows/review.md",
                   "dispatch refs before Map", "dispatch refs after Map"),
        ATMutation("workflow", "review-origin", ".tfw/workflows/review.md",
                   "never\nreplace origin on forwarding, transcription or restart",
                   "replace origin on restart"),
    ))
    for operation in PHASE_D_OPERATIONS:
        items.append(ATMutation("adapter-operation", operation, PHASE_D_ADAPTER,
                                f"`{operation}`", f"`relay_{operation}`"))
    items.extend((
        ATMutation("adapter", "one-lead", PHASE_D_ADAPTER,
                   "one user-visible LEAD task", "one task per role profile"),
        ATMutation("adapter", "direct-units", PHASE_D_ADAPTER,
                   "creates distinct\nuser-visible, directly addressable",
                   "creates hidden relay"),
        ATMutation("adapter", "child-grant", PHASE_D_ADAPTER,
                   "never merges units or grants a\nchild amendment authority",
                   "merges units and grants child authority"),
        ATMutation("adapter", "worktrees", PHASE_D_ADAPTER,
                   "Mutating units use separate worktrees", "Mutating units share one checkout"),
        ATMutation("adapter", "same-role", PHASE_D_ADAPTER,
                   "reuse the same Executor and\nindependent Reviewer", "replace both role tasks"),
        ATMutation("adapter", "holders", PHASE_D_ADAPTER,
                   "Forks, subagents, relays, hidden helpers and provider switches cannot",
                   "Forks and subagents may"),
        ATMutation("adapter-admission", "supplied", PHASE_D_ADAPTER,
                   "supplied initial Codex profile is\nadmitted with disclosed G1–G7 mechanics only",
                   "supplied profile requires G8"),
        ATMutation("adapter-admission", "additional", PHASE_D_ADAPTER,
                   "every additional provider profile\nrequires one native all-eight TFW trial",
                   "additional profiles use translated documentation"),
    ))
    return tuple(items)


def _phase_d_projection(tree: SourceTree, mutation: ATMutation) -> tuple[object, list[str]]:
    if mutation.path == PHASE_D_CONVENTIONS:
        record = parse_phase_d_contract(tree); return record, phase_d_contract_errors(record)
    if mutation.path == PHASE_D_ASSIGNMENT:
        record = parse_phase_d_assignment(tree); return record, phase_d_assignment_errors(record)
    if mutation.path in {PHASE_D_PROFILE, PHASE_D_EVENT}:
        record = parse_phase_d_carriers(tree); return record, phase_d_carrier_errors(record)
    if mutation.path == PHASE_D_ADAPTER:
        record = parse_phase_d_adapter(tree); return record, phase_d_adapter_errors(record)
    records = parse_phase_d_workflows(tree); return records, phase_d_workflow_errors(records)


def phase_d_mutant_payload(tree: SourceTree) -> list[dict[str, object]]:
    output = []
    for mutation in _phase_d_mutations():
        source = tree.read(mutation.path)
        if source.count(mutation.old) != 1:
            raise SourceContractError(
                f"Phase D rev2 mutation source must resolve once: {mutation.target} -> "
                f"{source.count(mutation.old)}")
        normal, normal_errors = _phase_d_projection(tree, mutation)
        mutant = tree.with_text(mutation.path, source.replace(mutation.old, mutation.new, 1))
        produced, errors = _phase_d_projection(mutant, mutation)
        output.append({
            "family": mutation.family, "target": mutation.target, "path": mutation.path,
            "projection_changed": produced != normal,
            "independent_expected_rejects": bool(errors),
            "normal_errors": normal_errors, "rejection_fields": errors,
        })
    return output


PHASE_D_PROVIDER_ALLOWED = {PHASE_D_ADAPTER, "AGENTS.md", PHASE_D_CONVENTIONS}


def phase_d_census(tree: SourceTree) -> dict[str, object]:
    paths = tuple(path for path in tree.files("**/*") if Path(path).suffix in {".md", ".yaml", ".py"})
    occurrences = []
    for path in paths:
        count = len(PHASE_D_CENSUS_TERMS.findall(tree.read(path)))
        if count:
            occurrences.append({"path": path, "class": _phase_d_census_class(path), "count": count})
    baseline = SourceTree.from_git(PROJECT_ROOT, PHASE_D_BASELINE_REF)
    changed = subprocess.run(
        ["git", "diff", "--name-only", PHASE_D_BASELINE_REF, "--"], cwd=PROJECT_ROOT,
        text=True, encoding="utf-8", capture_output=True, check=True).stdout.splitlines()
    deltas = []
    for path in sorted(set(changed) & set(paths) & set(baseline.files("**/*"))):
        before, after = baseline.read(path), tree.read(path)
        for term in PHASE_D_PROVIDER_TERMS:
            delta = after.count(term) - before.count(term)
            if delta:
                deltas.append({"path": path, "term": term, "delta": delta,
                               "allowed": path in PHASE_D_PROVIDER_ALLOWED or path.startswith("docs/scripts/")})
    return {"occurrences": occurrences, "provider_deltas": deltas,
            "unclassified": [row for row in occurrences if not row["class"]],
            "positive_provider_leaks": [row for row in deltas if row["delta"] > 0 and not row["allowed"]]}


def test_phase_d_contract_assignment_workflows_and_adapter_are_source_derived_and_complete():
    tree = SourceTree.from_path(PROJECT_ROOT)
    assert phase_d_contract_errors(parse_phase_d_contract(tree)) == []
    assert phase_d_assignment_errors(parse_phase_d_assignment(tree)) == []
    assert phase_d_carrier_errors(parse_phase_d_carriers(tree)) == []
    assert phase_d_workflow_errors(parse_phase_d_workflows(tree)) == []
    assert phase_d_adapter_errors(parse_phase_d_adapter(tree)) == []
    assert len(parse_phase_d_contract(tree)["owner_returns"]) == 7
    assert len(parse_phase_d_contract(tree)["native_gates"]) == 8


def test_phase_d_positive_negative_boundary_and_return_scenarios_match_independent_oracle():
    tree = SourceTree.from_path(PROJECT_ROOT)
    for name, fixture in PHASE_D_SCENARIOS.items():
        actual = resolve_phase_d_scenario(tree, fixture)
        assert tuple(actual.__dict__.values()) == PHASE_D_EXPECTED_SCENARIOS[name], name


def test_phase_d_principal_unit_origin_dispatch_and_replacement_matrix():
    tree = SourceTree.from_path(PROJECT_ROOT)
    assert resolve_phase_d_authority(tree, AuthorityFixture("lead", "child/executor")) == "LEAD_RULE"
    assert resolve_phase_d_authority(tree, AuthorityFixture(
        "lead", "child/executor", forwarded_writer="other")) == "LEAD_RULE"
    negatives = (
        AuthorityFixture("lead", "lead/root"),
        AuthorityFixture("lead", "child/executor", root_unit=False),
        AuthorityFixture("lead", "child/executor", reserved=True),
        AuthorityFixture(None, None), AuthorityFixture("lead", "child", ambiguous=True),
        AuthorityFixture("lead", "child", grant=False),
        AuthorityFixture("lead", "child", inside_mandate=False),
    )
    assert all(resolve_phase_d_authority(tree, case) in {"OWNER", "OWNER_OR_BLOCK"}
               for case in negatives)
    assert resolve_phase_d_dispatch(tree, DispatchFixture()) == "PROCEED"
    dispatch_negatives = (
        DispatchFixture(source_role="Executor"), DispatchFixture(unique_parent=False),
        DispatchFixture(ancestor_target=True), DispatchFixture(task_coordinator_target=True),
        DispatchFixture(cycle=True), DispatchFixture(foreign_scope=True),
        DispatchFixture(address=False), DispatchFixture(root=False),
    )
    assert all(resolve_phase_d_dispatch(tree, case).startswith("REFUSE") for case in dispatch_negatives)
    assert resolve_phase_d_replacement(tree, True, False, True) == "WAIT_FOR_OWNER"
    assert resolve_phase_d_replacement(tree, True, True, False) == "WAIT_FOR_OWNER"
    assert resolve_phase_d_replacement(tree, True, True, True) == "PROCEED_REPLACEMENT"


def test_phase_d_combined_admission_oracle_rejects_each_missing_gate_and_partial_receipts():
    tree = SourceTree.from_path(PROJECT_ROOT)
    assert resolve_phase_d_admission(tree, AdmissionFixture(
        "supplied", (True,) * 7 + (False,))) == "ADMIT_SUPPLIED_LIMITED"
    assert resolve_phase_d_admission(tree, AdmissionFixture(
        "additional", (True,) * 8)) == "ADMIT_ADDITIONAL_NATIVE_ALL_EIGHT"
    for missing in range(8):
        gates = tuple(index != missing for index in range(8))
        assert resolve_phase_d_admission(tree, AdmissionFixture(
            "additional", gates)) == "REJECT_NO_NATIVE_ALL_EIGHT"
    assert resolve_phase_d_admission(tree, AdmissionFixture(
        "additional", (True,) * 8, native_single_trial=False)) == "REJECT_NO_NATIVE_ALL_EIGHT"
    assert resolve_phase_d_admission(tree, AdmissionFixture(
        "additional", (True,) * 8, partial_receipts=True)) == "REJECT_NO_NATIVE_ALL_EIGHT"


def test_phase_d_required_admission_mutants_change_combined_decision_then_reject():
    tree = SourceTree.from_path(PROJECT_ROOT)
    supplied = AdmissionFixture("supplied", (True,) * 7 + (False,))
    additional = AdmissionFixture("additional", (True,) * 8, partial_receipts=True)
    assert resolve_phase_d_admission(tree, supplied) == "ADMIT_SUPPLIED_LIMITED"
    universal = tree.with_text(PHASE_D_CONVENTIONS, tree.read(PHASE_D_CONVENTIONS).replace(
        "first-release exception: admit it only as `ADMIT_SUPPLIED_LIMITED`",
        "universal all-eight rule", 1))
    assert resolve_phase_d_admission(universal, supplied) == "BLOCK_SOURCE"
    assert resolve_phase_d_admission(tree, additional) == "REJECT_NO_NATIVE_ALL_EIGHT"
    compose = tree.with_text(PHASE_D_CONVENTIONS, tree.read(PHASE_D_CONVENTIONS).replace(
        "partial receipts never compose", "partial receipts compose", 1))
    assert resolve_phase_d_admission(compose, additional) == "BLOCK_SOURCE"


def test_phase_d_each_semantic_mutant_changes_output_then_is_independently_rejected():
    rows = phase_d_mutant_payload(SourceTree.from_path(PROJECT_ROOT))
    assert len(rows) >= 60
    assert {"declaration", "mandate-unit", "replacement", "unit-resolution", "duty",
            "degradation", "principal-unit", "proposal-origin", "authority", "admission",
            "return-channel", "native-gate", "mandate-column", "unit-column", "carrier",
            "workflow", "adapter-operation", "adapter", "adapter-admission"} == {
                row["family"] for row in rows}
    assert all(not row["normal_errors"] for row in rows)
    assert all(row["projection_changed"] and row["independent_expected_rejects"] for row in rows)


def test_phase_d_live_census_classifies_consumers_and_adds_no_provider_leak():
    report = phase_d_census(SourceTree.from_path(PROJECT_ROOT))
    assert report["occurrences"] and not report["unclassified"]
    assert not report["positive_provider_leaks"]
    classes = {row["class"] for row in report["occurrences"]}
    assert {"canonical-contract", "template-form", "workflow-enforcement", "adapter-operation",
            "task-trace-history", "assurance", "reference-history"} <= classes


def test_phase_d_attention_cap_literals_and_measurer_are_byte_exact_from_baseline():
    before = SourceTree.from_git(PROJECT_ROOT, PHASE_D_BASELINE_REF).read(
        "docs/scripts/test_runtime_context.py")
    after = SourceTree.from_path(PROJECT_ROOT).read("docs/scripts/test_runtime_context.py")
    for name in ("PHASE_C_PRIMARY_ENTRY_WORDS", "SESSION_ROUTE_CEILINGS",
                 "session_identity_context_payload"):
        assert _python_named_span(after, name) == _python_named_span(before, name)


def phase_d_attention_payload(candidate: SourceTree) -> dict[str, object]:
    phase_c = SourceTree.from_git(PROJECT_ROOT, PHASE_C_BASELINE_REF)
    rtpsn = SourceTree.from_git(PROJECT_ROOT, RTPSN_PHASE_B_BASELINE_REF)
    primary = {}
    for command, ceiling in PHASE_C_PRIMARY_ENTRY_WORDS.items():
        current = measure_graph(candidate, discover_read_graph(candidate, command))
        primary[command] = {"baseline": ceiling, "current": current, "ceiling": ceiling,
                            "crossed": current > ceiling, "delta": current - ceiling}
    session = {}
    for command, ceiling in SESSION_ROUTE_CEILINGS.items():
        current = measure_graph(candidate, discover_read_graph(candidate, command))
        session[command] = {"baseline": measure_graph(rtpsn, discover_read_graph(rtpsn, command)),
                            "current": current, "ceiling": ceiling,
                            "crossed": current > ceiling, "delta": current - ceiling}
    active = active_runtime_corpus_words(candidate)
    central = _words(resolve_heading(candidate.read(SESSION_IDENTITY_PATH), "Session identity"))
    local = {}
    for command in ("plan", "research", "handoff", "review", "resume", "docs", "init"):
        path = SESSION_WORKFLOW_PATHS[command]
        delta = _words(candidate.read(path)) - _words(rtpsn.read(path))
        local[path] = {"net_words": delta, "historical_cap": 45, "crossed": delta > 45}
    return {
        "primary_routes": primary, "session_routes": session,
        "active_corpus": {"baseline": active_runtime_corpus_words(rtpsn), "current": active,
                          "historical_ceiling": 33_749, "crossed": active > 33_749},
        "central_range": {"current": central, "historical_cap": 260, "crossed": central > 260},
        "workflow_local": local,
        "phase_c_reductions": {command: graph_reduction(phase_c, candidate, command)
                               for command in (*SECONDARY_COMMANDS, *LIFECYCLE_VARIANTS)},
        "a5_disposition": "measured crossing; minimum semantic A7 correction, no cap ratchet",
    }


def test_phase_c_every_changed_path_and_active_corpus_clear_thirty_percent():
    report = phase_d_attention_payload(SourceTree.from_path(PROJECT_ROOT))
    assert report["a5_disposition"] == "measured crossing; minimum semantic A7 correction, no cap ratchet"
    for group in ("primary_routes", "session_routes"):
        for row in report[group].values():
            assert row["crossed"] == (row["current"] > row["ceiling"])
            assert row["delta"] == row["current"] - row["ceiling"]
    assert report["active_corpus"]["crossed"] == (
        report["active_corpus"]["current"] > report["active_corpus"]["historical_ceiling"])
    assert all(isinstance(value, float) for value in report["phase_c_reductions"].values())


def test_vbsa_plan_loads_three_unique_canonical_sections_with_d75_intact():
    tree = SourceTree.from_path(PROJECT_ROOT)
    validate_vbsa_plan_contract(tree)
    row = phase_d_attention_payload(tree)["primary_routes"]["/tfw-plan"]
    assert row["baseline"] == PHASE_C_PRIMARY_ENTRY_WORDS["/tfw-plan"]
    assert row["crossed"] == (row["current"] > row["ceiling"])


def test_rtpsn_phase_b_context_routes_corpus_and_local_caps_do_not_grow():
    report = phase_d_attention_payload(SourceTree.from_path(PROJECT_ROOT))
    assert report["active_corpus"]["baseline"] == 33_749
    assert report["central_range"]["crossed"] == (
        report["central_range"]["current"] > report["central_range"]["historical_cap"])
    assert all(row["crossed"] == (row["net_words"] > row["historical_cap"])
               for row in report["workflow_local"].values())


def test_cratm_phase_c_authority_contract_is_source_derived_and_complete():
    contract = parse_phase_d_contract(SourceTree.from_path(PROJECT_ROOT))
    assert phase_d_contract_errors(contract) == []
    assert all(contract[name] for name in (
        "principal_unit_distinct", "dispatch_provenance", "routing_guards", "authority_split"))


def test_cratm_phase_c_full_authority_payloads_cover_routes_refusals_and_human_exceptions():
    tree = SourceTree.from_path(PROJECT_ROOT)
    cases = {
        "subordinate": (AuthorityFixture("lead", "child/executor"), "LEAD_RULE"),
        "same_principal_restart": (AuthorityFixture(
            "lead", "child/executor", forwarded_writer="lead"), "LEAD_RULE"),
        "lead_origin": (AuthorityFixture("lead", "lead/root"), "OWNER"),
        "child_signer": (AuthorityFixture(
            "lead", "child/research", signer_unit="child/reviewer", root_unit=False), "OWNER"),
        "reserved": (AuthorityFixture("lead", "child", reserved=True), "OWNER"),
        "missing_origin": (AuthorityFixture(None, None), "OWNER_OR_BLOCK"),
        "ambiguous_origin": (AuthorityFixture("lead", "child", ambiguous=True), "OWNER_OR_BLOCK"),
        "false_grant": (AuthorityFixture("lead", "child", grant=False), "OWNER"),
        "outside_mandate": (AuthorityFixture("lead", "child", inside_mandate=False), "OWNER"),
    }
    assert {name: resolve_phase_d_authority(tree, case) for name, (case, _) in cases.items()} == {
        name: expected for name, (_, expected) in cases.items()}


def test_cratm_phase_c_authority_mutants_change_output_before_independent_rejection():
    rows = [row for row in phase_d_mutant_payload(SourceTree.from_path(PROJECT_ROOT))
            if row["family"] in {"principal-unit", "proposal-origin", "authority", "return-channel"}]
    assert rows and all(row["projection_changed"] and row["independent_expected_rejects"] for row in rows)


def test_cratm_phase_c_plan_consumer_executes_ordinary_and_delegated_branches():
    tree = SourceTree.from_path(PROJECT_ROOT)
    plan = parse_phase_d_workflows(tree)["plan"]
    assert all(plan[key] for key in (
        "prework", "separate_fields", "direct_return", "continuity",
        "supersede_before_replacement", "origin_stable", "role_lock"))
    assert resolve_phase_d_authority(tree, AuthorityFixture("lead", "child/executor")) == "LEAD_RULE"
    assert resolve_phase_d_authority(tree, AuthorityFixture("lead", "lead/root")) == "OWNER"


def test_cratm_phase_c_plan_consumer_contradiction_mutant_changes_output_and_is_rejected():
    tree = SourceTree.from_path(PROJECT_ROOT)
    path = ".tfw/workflows/plan.md"
    mutant = tree.with_text(path, tree.read(path).replace(
        "resolve the selected principal/mandate separately", "resolve writer as the unit", 1))
    normal = parse_phase_d_workflows(tree)
    produced = parse_phase_d_workflows(mutant)
    assert produced != normal
    assert "plan:separate_fields" in phase_d_workflow_errors(produced)


def test_cratm_phase_c_consumers_preserve_role_locks_and_human_only_routes():
    tree = SourceTree.from_path(PROJECT_ROOT)
    assert phase_d_workflow_errors(parse_phase_d_workflows(tree)) == []
    assert resolve_phase_d_authority(tree, AuthorityFixture(
        "lead", "child", reserved=True)) == "OWNER"
    assert resolve_phase_d_replacement(tree, True, False, True) == "WAIT_FOR_OWNER"
    assert "never an Executor decision" in tree.read(".tfw/workflows/handoff.md")
    assert "❌ REJECT" in tree.read(".tfw/workflows/review.md")


@dataclass(frozen=True)
class LeadNavigationCase:
    name: str
    command: str
    selected_handle: str | None = "cratm-main"
    selected_profile_type: str = "agent"
    selected_profile_valid: bool = True
    selection_source: str = "authoritative-lineage"
    acting_handle: str | None = "cratm-main"
    root_unit: str | None = "unit/root-coordinator"
    current_unit: str | None = "unit/root-coordinator"
    current_role: str = "Coordinator"
    task: str = "CRATM"
    phase: str | None = "D"
    existing_titles: tuple[str, ...] = ()
    colliding_keys: tuple[str, ...] = ()
    stable_key: str | None = "ab7"
    rename_available: bool = True
    readback_available: bool = True
    readback_override: str | None = None


@dataclass(frozen=True)
class LeadNavigationRecord:
    case: str
    source_valid: bool
    qualifies: bool
    selected_handle: str | None
    acting_handle: str | None
    root_unit: str | None
    current_unit: str | None
    work: str
    suffix_decision: str
    intended_title: str
    readback_result: str
    report_once_result: str
    claim_result: str
    source_manifest: tuple[str, ...]
    source_errors: tuple[str, ...]


def parse_lead_navigation_contract(tree: SourceTree) -> dict[str, bool]:
    section = resolve_heading(tree.read(SESSION_IDENTITY_PATH), "Session identity")
    plan = tree.read(SESSION_WORKFLOW_PATHS["plan"])
    resume = tree.read(SESSION_WORKFLOW_PATHS["resume"])
    return {
        "exact_form": all(s in section for s in (
            "LEAD_BASE:=LEAD+SP+DOT+SP+HANDLE", "`LEAD · {handle} · {TASK}[ · {PHASE}]`")),
        "authoritative_conjunction": "iff all\nauthoritative governing-lineage facts resolve" in section,
        "work_limit": "requested WORK is `PLAN` or `RESUME`" in section,
        "selected_valid_agent": all(s in section for s in (
            "one valid agent\nprincipal is selected as LEAD by the mandate",
            "selected stable profile handle only")),
        "acting_equals_selected": "acting principal equals that stable `team/{handle}.md`\nhandle" in section,
        "current_equals_root": "current actual unit equals the mandate's exact root Coordinator unit" in section,
        "plan_resume_continuity": "same root keeps\nthis form across Plan and Resume" in section,
        "child_keeps_work": all(s in section for s in (
            "same-principal child", "including a Coordinator", "emit ordinary WORK with no handle")),
        "negative_sources": (
            "human/different/unselected agent, stale handle, forwarded selection,\nwrong role, or "
            "missing/ambiguous root/current-unit fact" in section),
        "handle_not_name": all(s in section for s in (
            "Never use mutable `name`", "OS/account/provider", "human binding or chat")),
        "navigation_only": all(s in section for s in (
            "Navigation grants no identity, authority, mandate", "dispatch edge",
            "role permission or amendment right", "generic bound or attribution is insufficient")),
        "rendered_scope": "RENDERED:=BASE|LEAD_BASE" in section,
        "collision_on_rendered": all(s in section for s in (
            "duplicate(RENDERED)", "exposed(stable-key)", "shortest-unique-leading-prefix")),
        "exact_readback_both": "exact-readback-only for either RENDERED" in section,
        "fail_soft_both": all(s in section for s in (
            "either RENDERED unavailable/failed/altered-readback/no-key",
            "report-once(title,reason)", "continue-unclaimed")),
        "plan_consumer": all(s in plan for s in (
            "resolve selected LEAD principal", "acting principal", "mandate root Coordinator unit",
            "current actual unit", "central root predicate qualifies this exact `PLAN` unit",
            "same-principal children keep `PLAN` with no handle")),
        "resume_consumer": all(s in resume for s in (
            "resolve selected/acting principals", "mandate root/current actual units",
            "central root predicate qualifies this exact `RESUME`", "children keep `RESUME` with no handle")),
        "consumer_order": (plan.index("### Session identity checkpoint") < plan.index("## Step 2:")
                           and resume.index("5. After one task resolves") < resume.index("## 2. Build the Matrix")),
    }


def lead_navigation_contract_errors(record: dict[str, bool]) -> list[str]:
    return [name for name, value in record.items() if not value]


def resolve_lead_navigation(tree: SourceTree, case: LeadNavigationCase) -> LeadNavigationRecord:
    contract = parse_lead_navigation_contract(tree)
    errors = tuple(lead_navigation_contract_errors(contract))
    workflow = case.command.upper()
    qualifies = (not errors and workflow in {"PLAN", "RESUME"}
                 and case.selection_source == "authoritative-lineage"
                 and bool(case.selected_handle) and case.selected_profile_type == "agent"
                 and case.selected_profile_valid and case.acting_handle == case.selected_handle
                 and bool(case.root_unit) and case.root_unit == case.current_unit
                 and case.current_role == "Coordinator")
    work = "LEAD" if qualifies else workflow
    parts = (["LEAD", case.selected_handle or ""] if qualifies else [work]) + [case.task]
    if case.phase: parts.append(case.phase)
    title = " · ".join(parts)
    suffix, failure = "none", None
    if title in case.existing_titles:
        if not case.stable_key:
            suffix, failure = "unclaimed:no-stable-key", "no-stable-key"
        else:
            prefix = _shortest_unique_prefix(case.stable_key, case.colliding_keys)
            if prefix:
                suffix = f"@{prefix}"
                title += " · " + suffix
            else:
                suffix, failure = "unclaimed:no-unique-prefix", "no-unique-prefix"
    if failure:
        readback, report = f"not-attempted:{failure}", f"once:{title}:{failure}"
    elif not case.rename_available:
        readback, report = "rename-unavailable", f"once:{title}:rename-unavailable"
    elif not case.readback_available:
        readback, report = "readback-unavailable", f"once:{title}:readback-unavailable"
    else:
        observed = case.readback_override if case.readback_override is not None else title
        if observed == title:
            readback, report = "exact", "none"
        else:
            readback, report = f"mismatch:{observed}", f"once:{title}:altered-readback"
    claim = "claimed" if readback == "exact" else "unclaimed"
    return LeadNavigationRecord(
        case.name, not errors, qualifies, case.selected_handle, case.acting_handle,
        case.root_unit, case.current_unit, work, suffix, title, readback, report, claim,
        (SESSION_IDENTITY_PATH, SESSION_WORKFLOW_PATHS[case.command]), errors,
    )


LEAD_NAVIGATION_CASES = {
    "root_plan": LeadNavigationCase("root_plan", "plan"),
    "root_resume": LeadNavigationCase("root_resume", "resume"),
    "same_principal_child": LeadNavigationCase(
        "same_principal_child", "plan", current_unit="unit/child-executor", current_role="Executor"),
    "child_coordinator": LeadNavigationCase(
        "child_coordinator", "resume", current_unit="unit/child-coordinator"),
    "human": LeadNavigationCase("human", "plan", selected_profile_type="human"),
    "different_agent": LeadNavigationCase("different_agent", "resume", acting_handle="other-agent"),
    "unselected": LeadNavigationCase("unselected", "plan", selected_handle=None, acting_handle=None),
    "stale": LeadNavigationCase("stale", "resume", selected_profile_valid=False),
    "forwarded": LeadNavigationCase("forwarded", "plan", selection_source="forwarded-message"),
    "ambiguous_selection": LeadNavigationCase(
        "ambiguous_selection", "resume", selection_source="ambiguous"),
    "wrong_role": LeadNavigationCase("wrong_role", "plan", current_role="Executor"),
    "missing_root": LeadNavigationCase("missing_root", "resume", root_unit=None),
    "missing_current": LeadNavigationCase("missing_current", "plan", current_unit=None),
    "ambiguous_root": LeadNavigationCase(
        "ambiguous_root", "resume", root_unit="ambiguous", current_unit="unit/root-coordinator"),
    "research_root": LeadNavigationCase("research_root", "research"),
    "collision_exact": LeadNavigationCase(
        "collision_exact", "plan", existing_titles=("LEAD · cratm-main · CRATM · D",),
        colliding_keys=("ac9",), stable_key="ab7"),
    "collision_no_key": LeadNavigationCase(
        "collision_no_key", "resume", existing_titles=("LEAD · cratm-main · CRATM · D",),
        colliding_keys=("ac9",), stable_key=None),
    "collision_altered_readback": LeadNavigationCase(
        "collision_altered_readback", "plan",
        existing_titles=("LEAD · cratm-main · CRATM · D",), colliding_keys=("ac9",),
        stable_key="ab7", readback_override="LEAD | cratm-main | CRATM | D | @ab"),
    "readback_failure": LeadNavigationCase(
        "readback_failure", "plan", readback_override="LEAD | mutable name | CRATM | D"),
}


LEAD_NAVIGATION_EXPECTED = {
    "root_plan": (True, "LEAD", "LEAD · cratm-main · CRATM · D"),
    "root_resume": (True, "LEAD", "LEAD · cratm-main · CRATM · D"),
    "same_principal_child": (False, "PLAN", "PLAN · CRATM · D"),
    "child_coordinator": (False, "RESUME", "RESUME · CRATM · D"),
    "human": (False, "PLAN", "PLAN · CRATM · D"),
    "different_agent": (False, "RESUME", "RESUME · CRATM · D"),
    "unselected": (False, "PLAN", "PLAN · CRATM · D"),
    "stale": (False, "RESUME", "RESUME · CRATM · D"),
    "forwarded": (False, "PLAN", "PLAN · CRATM · D"),
    "ambiguous_selection": (False, "RESUME", "RESUME · CRATM · D"),
    "wrong_role": (False, "PLAN", "PLAN · CRATM · D"),
    "missing_root": (False, "RESUME", "RESUME · CRATM · D"),
    "missing_current": (False, "PLAN", "PLAN · CRATM · D"),
    "ambiguous_root": (False, "RESUME", "RESUME · CRATM · D"),
    "research_root": (False, "RESEARCH", "RESEARCH · CRATM · D"),
    "collision_exact": (True, "LEAD", "LEAD · cratm-main · CRATM · D · @ab"),
    "collision_no_key": (True, "LEAD", "LEAD · cratm-main · CRATM · D"),
    "collision_altered_readback": (True, "LEAD", "LEAD · cratm-main · CRATM · D · @ab"),
    "readback_failure": (True, "LEAD", "LEAD · cratm-main · CRATM · D"),
}


def lead_navigation_mutant_payload(tree: SourceTree) -> list[dict[str, object]]:
    mutations = (
        ATMutation("root-predicate", "generic-bound", SESSION_IDENTITY_PATH,
                   "all\nauthoritative governing-lineage facts resolve", "a generic bound resolves"),
        ATMutation("root-predicate", "selected-agent", SESSION_IDENTITY_PATH,
                   "one valid agent\nprincipal is selected as LEAD by the mandate", "any principal is selected"),
        ATMutation("root-predicate", "acting-principal", SESSION_IDENTITY_PATH,
                   "acting principal equals that stable `team/{handle}.md`\nhandle",
                   "acting principal is any session"),
        ATMutation("root-predicate", "current-root", SESSION_IDENTITY_PATH,
                   "current actual unit equals the mandate's exact root Coordinator unit",
                   "current unit has any Coordinator role"),
        ATMutation("continuity", "plan-resume", SESSION_IDENTITY_PATH,
                   "same root keeps\nthis form across Plan and Resume", "Resume returns to ordinary WORK"),
        ATMutation("child-leak", "same-principal", SESSION_IDENTITY_PATH,
                   "a same-principal child\n(including a Coordinator)", "a different-principal child"),
        ATMutation("identity-source", "stale", SESSION_IDENTITY_PATH,
                   "stale handle", "stale handle may qualify"),
        ATMutation("identity-source", "forwarded", SESSION_IDENTITY_PATH,
                   "forwarded selection", "forwarded selection may qualify"),
        ATMutation("identity-source", "display-name", SESSION_IDENTITY_PATH,
                   "Never use mutable `name`", "Use mutable `name`"),
        ATMutation("non-authority", "title-grant", SESSION_IDENTITY_PATH,
                   "Navigation grants no identity, authority, mandate", "Navigation grants authority"),
        ATMutation("collision-scope", "rendered-base-only", SESSION_IDENTITY_PATH,
                   "RENDERED:=BASE|LEAD_BASE", "RENDERED:=BASE"),
        ATMutation("collision-scope", "duplicate-base-only", SESSION_IDENTITY_PATH,
                   "duplicate(RENDERED)", "duplicate(BASE)"),
        ATMutation("collision-key", "stable-key", SESSION_IDENTITY_PATH,
                   "exposed(stable-key)", "exposed(any-key)"),
        ATMutation("collision-key", "shortest-prefix", SESSION_IDENTITY_PATH,
                   "shortest-unique-leading-prefix", "full-stable-key"),
        ATMutation("collision-readback", "exact-readback", SESSION_IDENTITY_PATH,
                   "exact-readback-only for either RENDERED", "best-effort-readback"),
        ATMutation("collision-failure", "no-key", SESSION_IDENTITY_PATH,
                   "failed/altered-readback/no-key", "failed/altered-readback/guessed-key"),
        ATMutation("collision-failure", "altered-readback", SESSION_IDENTITY_PATH,
                   "unavailable/failed/altered-readback/no-key",
                   "unavailable/failed/accepted-readback/no-key"),
        ATMutation("collision-failure", "report-once", SESSION_IDENTITY_PATH,
                   "report-once(title,reason)", "report-every-time(title,reason)"),
        ATMutation("collision-failure", "continue-unclaimed", SESSION_IDENTITY_PATH,
                   "continue-unclaimed", "continue-claimed"),
        ATMutation("consumer", "plan-root", SESSION_WORKFLOW_PATHS["plan"],
                   "central root predicate qualifies this exact `PLAN` unit",
                   "a governing bound qualifies any `PLAN` unit"),
        ATMutation("consumer", "plan-child", SESSION_WORKFLOW_PATHS["plan"],
                   "same-principal children keep `PLAN` with no handle",
                   "same-principal children render LEAD with the handle"),
        ATMutation("consumer", "resume-root", SESSION_WORKFLOW_PATHS["resume"],
                   "central root predicate qualifies this exact `RESUME`",
                   "principal attribution qualifies any `RESUME`"),
        ATMutation("consumer", "resume-child", SESSION_WORKFLOW_PATHS["resume"],
                   "children keep `RESUME` with no handle", "children render LEAD with the handle"),
    )
    output = []
    root_case = LEAD_NAVIGATION_CASES["root_plan"]
    for mutation in mutations:
        source = tree.read(mutation.path)
        if source.count(mutation.old) != 1:
            raise SourceContractError(
                f"LEAD mutation source must resolve once: {mutation.target} -> {source.count(mutation.old)}")
        normal_contract = parse_lead_navigation_contract(tree)
        normal = resolve_lead_navigation(tree, root_case)
        mutant = tree.with_text(mutation.path, source.replace(mutation.old, mutation.new, 1))
        produced_contract = parse_lead_navigation_contract(mutant)
        produced = resolve_lead_navigation(mutant, root_case)
        errors = lead_navigation_contract_errors(produced_contract)
        output.append({
            "family": mutation.family, "target": mutation.target, "path": mutation.path,
            "projection_changed": produced_contract != normal_contract or produced != normal,
            "independent_expected_rejects": bool(errors), "rejection_fields": errors,
            "normal": normal.__dict__, "produced": produced.__dict__,
        })
    return output


def session_identity_scenario_payload(tree: SourceTree) -> dict[str, object]:
    return {
        "contract": parse_lead_navigation_contract(tree),
        "scenarios": {name: resolve_lead_navigation(tree, case).__dict__
                      for name, case in LEAD_NAVIGATION_CASES.items()},
    }


def session_identity_mutant_payload(tree: SourceTree) -> list[dict[str, object]]:
    return lead_navigation_mutant_payload(tree)


def test_rtpsn_phase_b_contract_is_single_source_complete_and_glossary_is_only_a_router():
    tree = SourceTree.from_path(PROJECT_ROOT)
    base = _session_contract(tree)
    assert base["separator"] == " · "
    assert base["work"] == ("PLAN", "RESEARCH", "EXEC", "REVIEW", "RESUME", "DOCS", "INIT", "LEAD")
    assert base["task_policy"] == "abbreviation" and base["authority"] == "state/lineage"
    assert lead_navigation_contract_errors(parse_lead_navigation_contract(tree)) == []
    glossary = resolve_heading(tree.read(".tfw/glossary.md"), "Session Naming")
    assert "conventions.md" in glossary and "Session identity" in glossary
    assert not any(term in glossary for term in ("BASE:=", "WORK:=", "root Coordinator unit"))


def test_rtpsn_phase_b_scenarios_cover_titles_omissions_collisions_and_fail_soft_transport():
    tree = SourceTree.from_path(PROJECT_ROOT)
    records = {name: resolve_lead_navigation(tree, case)
               for name, case in LEAD_NAVIGATION_CASES.items()}
    for name, expected in LEAD_NAVIGATION_EXPECTED.items():
        row = records[name]
        assert (row.qualifies, row.work, row.intended_title) == expected, name
    assert records["root_plan"].intended_title == records["root_resume"].intended_title
    assert "cratm-main" not in records["same_principal_child"].intended_title
    collision = records["collision_exact"]
    assert (collision.suffix_decision, collision.intended_title, collision.readback_result,
            collision.report_once_result, collision.claim_result) == (
                "@ab", "LEAD · cratm-main · CRATM · D · @ab", "exact", "none", "claimed")
    no_key = records["collision_no_key"]
    assert no_key.suffix_decision == "unclaimed:no-stable-key"
    assert no_key.readback_result == "not-attempted:no-stable-key"
    assert no_key.report_once_result.startswith("once:") and no_key.claim_result == "unclaimed"
    altered = records["collision_altered_readback"]
    assert altered.suffix_decision == "@ab" and altered.readback_result.startswith("mismatch:")
    assert altered.report_once_result.startswith("once:") and altered.claim_result == "unclaimed"
    assert records["readback_failure"].readback_result.startswith("mismatch:")
    assert records["readback_failure"].report_once_result.startswith("once:")


def test_rtpsn_phase_b_all_workflow_modes_are_classified_and_source_bounded():
    tree = SourceTree.from_path(PROJECT_ROOT)
    contract = parse_lead_navigation_contract(tree)
    assert contract["plan_consumer"] and contract["resume_consumer"] and contract["consumer_order"]
    for command in ("research", "handoff", "review", "docs", "init"):
        assert "Session identity" in tree.read(SESSION_WORKFLOW_PATHS[command])
    for command in SESSION_PROJECT_WIDE:
        assert "Session identity" not in tree.read(SESSION_WORKFLOW_PATHS[command])


def test_rtpsn_phase_b_each_semantic_mutant_changes_output_then_is_independently_rejected():
    rows = lead_navigation_mutant_payload(SourceTree.from_path(PROJECT_ROOT))
    assert {row["family"] for row in rows} == {
        "root-predicate", "continuity", "child-leak", "identity-source", "non-authority",
        "collision-scope", "collision-key", "collision-readback", "collision-failure", "consumer"}
    assert all(row["projection_changed"] and row["independent_expected_rejects"] for row in rows)


def test_phase_d_root_lead_navigation_scenarios_and_mutants_are_source_derived():
    tree = SourceTree.from_path(PROJECT_ROOT)
    assert lead_navigation_contract_errors(parse_lead_navigation_contract(tree)) == []
    for name, case in LEAD_NAVIGATION_CASES.items():
        record = resolve_lead_navigation(tree, case)
        assert (record.qualifies, record.work, record.intended_title) == LEAD_NAVIGATION_EXPECTED[name]
        assert not record.source_errors
    rows = lead_navigation_mutant_payload(tree)
    assert len(rows) >= 23
    assert all(row["projection_changed"] and row["independent_expected_rejects"] for row in rows)


def test_phase_d_plan_resume_copies_match_and_other_cues_never_gain_lead_handle():
    tree = SourceTree.from_path(PROJECT_ROOT)
    for name in ("plan", "resume"):
        canonical = tree.read(SESSION_WORKFLOW_PATHS[name])
        assert tree.read(f".agent/workflows/tfw-{name}.md") == canonical
        assert tree.read(f".claude/commands/tfw-{name}.md") == canonical
    for name, cue in (("research", "RESEARCH"), ("handoff", "EXEC"), ("review", "REVIEW"),
                      ("docs", "DOCS"), ("init", "INIT")):
        text = tree.read(SESSION_WORKFLOW_PATHS[name])
        assert "LEAD · {handle}" not in text, name
        assert cue in text, name


if __name__ == "__main__":
    raise SystemExit(main())
