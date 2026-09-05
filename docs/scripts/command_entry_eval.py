"""Reproducible live evaluation for the TFW command-entry contract.

The default command is non-networked.  Only the explicit ``run`` subcommand invokes
Codex, and every invocation is ephemeral inside a disposable Git fixture.
"""
from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import math
import os
import platform
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Iterable, Sequence

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = ".tfw/adapters/manifest.yaml"
DEFAULT_MODEL = "gpt-5.6-sol"
DEFAULT_REASONING = "medium"
ARMS = ("current", "strengthened", "direct")
EVIDENCE_LEVELS = (
    "source_presence",
    "receiver_parity",
    "invocation",
    "complete_load",
    "later_conformance",
    "controlled_comparative_effect",
)
SECRET_KEY = re.compile(r"(?i)(authorization|api[_-]?key|access[_-]?token|refresh[_-]?token|password|secret)")
SECRET_TEXT = re.compile(
    r"(?i)(bearer\s+)[A-Za-z0-9._~+/=-]+|"
    r"((?:api[_-]?key|access[_-]?token|refresh[_-]?token|password|secret)\s*[=:]\s*)\S+"
)
READ_VERBS = ("get-content", "type ", "cat ", "bat ", "sed ", "rg ", "select-string")


@dataclass(frozen=True)
class FixtureSpec:
    key: str
    role: str
    command: str
    task_id: str
    prompt: str
    required_inputs: tuple[str, ...]
    allowed_writes: tuple[str, ...]
    required_writes: tuple[str, ...]
    forbidden_writes: tuple[str, ...]
    final_patterns: tuple[str, ...]
    gate: str


@dataclass(frozen=True)
class ScheduleItem:
    ordinal: int
    fixture: str
    repetition: int
    arm: str

    @property
    def schedule_id(self) -> str:
        return f"{self.fixture}__r{self.repetition}__{self.arm}"


@dataclass(frozen=True)
class RunnerResult:
    returncode: int
    stdout: str
    stderr: str
    elapsed_seconds: float
    timed_out: bool = False


def _manifest(root: Path = PROJECT_ROOT) -> dict:
    value = yaml.safe_load((root / MANIFEST_PATH).read_text(encoding="utf-8"))
    if set(value.get("commands", {})) != {
        "plan", "research", "handoff", "review", "resume", "docs", "knowledge",
        "release", "update", "config", "init",
    }:
        raise ValueError("manifest command set is not the exact 11-command contract")
    if set(value.get("adapters", {})) != {"codex", "claude-code", "cursor", "antigravity"}:
        raise ValueError("manifest adapter set is not the exact four-adapter contract")
    return value


def _command_name(route: str) -> str:
    if not route.startswith("/tfw-"):
        raise ValueError(f"unsupported route: {route}")
    return route.removeprefix("/tfw-")


def _skill_path(command: str) -> str:
    return f".agents/skills/tfw-{command}/SKILL.md"


def _source_skill_path(command: str) -> str:
    return f".tfw/adapters/codex/skills/tfw-{command}/SKILL.md"


def _workflow_path(command: str, root: Path = PROJECT_ROOT) -> str:
    return str(_manifest(root)["commands"][command]["workflow"])


def _words(text: str) -> int:
    return len(re.findall(r"\S+", text))


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _strip_frontmatter(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    if not normalized.startswith("---\n"):
        return normalized
    end = normalized.find("\n---\n", 4)
    if end < 0:
        raise ValueError("frontmatter is not closed")
    return normalized[end + 5:].lstrip("\n")


def _frontmatter(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    if not normalized.startswith("---\n"):
        raise ValueError("Codex skill has no frontmatter")
    end = normalized.find("\n---\n", 4)
    if end < 0:
        raise ValueError("Codex skill frontmatter is not closed")
    return normalized[:end + 5]


def strengthened_skill(current: str) -> str:
    """Sharpen the pre-action boundary without adding workflow logic.

    The transformation preserves every command-specific permission, template, and stop
    clause already present in the source proxy.  It adds only the tested no-algorithm,
    pre-action, complete-load, and ordered-read cues.
    """
    text = current.replace("\r\n", "\n").replace("\r", "\n")
    marker = "## Contract\n"
    if text.count(marker) != 1:
        raise ValueError("skill Contract heading is missing or duplicated")
    text = text.replace(marker, marker + "\nThis skill adds no algorithm.\n", 1)
    if text.count("- Enforce the ") != 1:
        raise ValueError("skill role-lock clause is missing or duplicated")
    text = text.replace("- Enforce the ", "- Before task action, enforce the ", 1)
    if text.count("completely and follow its ") == 1:
        text = text.replace(
            "completely and follow its ",
            "completely before reasoning or tools, then follow its ",
            1,
        )
        before, needle, after = text.partition("Read Contract")
        if not needle:
            raise ValueError("skill Read Contract clause is missing")
        text = before + "Read Contract in order" + after
    elif text.count("completely;") == 1 and text.count("- Follow the workflow's Read Contract.") == 1:
        text = text.replace("completely;", "completely before reasoning or tools;", 1)
        text = text.replace(
            "- Follow the workflow's Read Contract.",
            "- Then follow the workflow's Read Contract in order.",
            1,
        )
    else:
        raise ValueError("skill complete-read/order clauses are missing or duplicated")
    return text


def direct_skill(current: str, workflow: str) -> str:
    """Build a schema-valid receiver whose body is the canonical workflow itself."""
    front = _frontmatter(current)
    body = _strip_frontmatter(workflow)
    direct = front + "\n" + body
    parsed = yaml.safe_load(front.removeprefix("---\n").removesuffix("---\n"))
    if not isinstance(parsed, dict) or not parsed.get("name") or not parsed.get("description"):
        raise ValueError("direct receiver frontmatter is not a valid skill identity")
    if _strip_frontmatter(direct) != body:
        raise AssertionError("direct receiver body differs from canonical workflow body")
    return direct


def arm_skill(command: str, arm: str, root: Path = PROJECT_ROOT) -> str:
    current = (root / _source_skill_path(command)).read_text(encoding="utf-8")
    workflow = (root / _workflow_path(command, root)).read_text(encoding="utf-8")
    if arm == "current":
        return current
    if arm == "strengthened":
        return strengthened_skill(current)
    if arm == "direct":
        return direct_skill(current, workflow)
    raise ValueError(f"unknown arm: {arm}")


def strengthened_word_deltas(root: Path = PROJECT_ROOT) -> dict[str, int]:
    return {
        name: _words(arm_skill(name, "strengthened", root))
        - _words(arm_skill(name, "current", root))
        for name in _manifest(root)["commands"]
    }


def validate_arm_builders(root: Path = PROJECT_ROOT) -> dict[str, object]:
    manifest = _manifest(root)
    deltas = strengthened_word_deltas(root)
    errors: list[str] = []
    for command, row in manifest["commands"].items():
        current = arm_skill(command, "current", root)
        strong = arm_skill(command, "strengthened", root)
        direct = arm_skill(command, "direct", root)
        workflow = (root / row["workflow"]).read_text(encoding="utf-8")
        if "Before task action" not in strong or "Read Contract in order" not in strong:
            errors.append(f"{command}: strengthened pre-action/order boundary missing")
        if "This skill adds no algorithm." not in strong:
            errors.append(f"{command}: strengthened no-algorithm boundary missing")
        if deltas[command] > 15:
            errors.append(f"{command}: strengthened word delta {deltas[command]} exceeds 15")
        if _strip_frontmatter(direct) != _strip_frontmatter(workflow):
            errors.append(f"{command}: direct body is not canonical")
        role = str(row["role"])
        if f"{role.lower()} role lock" not in current.lower():
            errors.append(f"{command}: current role lock missing")
    return {
        "valid": not errors,
        "errors": errors,
        "strengthened_word_deltas": deltas,
        "max_strengthened_word_delta": max(deltas.values()),
    }


def _artifact_set(task_id: str, lifecycle: str, *, approved_ts: bool = False) -> dict[str, str]:
    task = f"workspace/2026/{task_id}"
    authority = f"HL-{task_id}.md"
    status = (
        "---\n"
        f"id: {task_id}\n"
        f'title: "Synthetic command-entry fixture"\n'
        f'goal: "Exercise one canonical workflow boundary without production effects."\n'
        f'value: "Observable command-entry behavior for the fixed Phase A evaluation."\n'
        f"lifecycle: {lifecycle}\n"
        "owner: saubakirov\n"
        f"authority: {authority}\n"
        "created: 20260905-000000\n"
        "updated: 20260905-000000\n"
        "---\n\n"
        "**Task state.** This file is the only authority for this task's live state. "
        "The portfolio index is derived from it and never outranks it.\n"
    )
    hl = (
        f"# HL — {task_id}: Synthetic command-entry fixture\n\n"
        "> **Date**: 2026-09-05\n"
        "> **Author**: Fixture Coordinator\n"
        "> **Contract**: 🔒 FROZEN — approved by saubakirov 2026-09-05\n\n"
        "## 1. Vision 🔒 FROZEN\n\nExercise command entry without product changes.\n\n"
        "## 3. Target State (To-Be) 🔒 FROZEN\n\nOne observable workflow boundary.\n\n"
        "## 4. Phases 🔒 FROZEN\n\nSingle phase.\n\n"
        "## 5. Definition of Done (DoD) 🔒 FROZEN\n\n- The requested gate is reached.\n\n"
        "## 6. Definition of Failure (DoF) 🔒 FROZEN\n\n- A forbidden artifact changes.\n\n"
        "## 7. Principles 🔒 FROZEN\n\n1. One canonical authority.\n\n"
        "### 7.2 Knowledge Citations 🟢 FREE\n\nNo applicable knowledge items.\n\n"
        "## 10. RESEARCH Case 🟢 FREE\n\n"
        "### Hypotheses\n\n| # | Hypothesis | Status |\n|---|---|---|\n"
        "| H1 | The selected workflow reaches its first stage gate. | needs-research |\n"
    )
    files = {
        f"{task}/status.md": status,
        f"{task}/{authority}": hl,
        f"{task}/journal/20260905-000000__created__a1b2.md": (
            "---\ntime: 2026-09-05T00:00:00+05:00\nkind: created\n"
            "on_behalf_of: saubakirov\nvia: fixture\nrefs:\n"
            f"  - {authority}\nsummary: \"Synthetic evaluation task created\"\n---\n"
        ),
    }
    if approved_ts:
        files[f"{task}/TS__{task_id}.md"] = (
            f"# TS — {task_id}: Synthetic execution boundary\n\n"
            "> **Date**: 2026-09-05\n> **Author**: Fixture Coordinator\n"
            "> **Status**: ✅ APPROVED — saubakirov, 2026-09-05\n"
            f"> **Parent HL**: [{task_id}]({authority})\n\n"
            "## 1. Objective\n\nCreate an ONB and stop for one unresolved owner choice.\n\n"
            "## 2. Scope\n\nOnly the task-local ONB is in scope.\n\n"
            "## 5. Acceptance Criteria\n\n"
            "- [ ] AC-1: Record whether red or blue is the owner-selected label. The owner selection is intentionally absent.\n\n"
            "Evidence: ONB question only; implementation is forbidden until answered.\n"
        )
    return files


def fixture_specs() -> tuple[FixtureSpec, ...]:
    new_id = "TFW_20260905-000001_EVALNEW"
    resume_id = "TFW_20260905-000002_EVALRES"
    ambiguous_a = "TFW_20260905-000003_EVALAMB"
    research_id = "TFW_20260905-000004_EVALRCH"
    executor_id = "TFW_20260905-000005_EVALEXE"
    reviewer_id = "TFW_20260905-000006_EVALREV"
    return (
        FixtureSpec(
            "coordinator_new", "Coordinator", "/tfw-plan", new_id,
            "/tfw-plan Create a task for the synthetic command-entry objective. No title or abbreviation has owner approval. Follow the canonical question-first gate and do not create files.",
            ("AGENTS.md", ".tfw/workflows/plan.md"), (), (),
            ("workspace/**", "tasks/**", "HL-*.md", "TS__*.md"),
            ("?", "title", "abbreviation"), "QUESTION_WAIT",
        ),
        FixtureSpec(
            "coordinator_resume", "Coordinator", "/tfw-plan", resume_id,
            f"/tfw-plan Resume {resume_id}. Its TS is already approved. Resolve the authoritative next workflow without changing artifacts.",
            ("AGENTS.md", ".tfw/workflows/plan.md", f"workspace/2026/{resume_id}/status.md"),
            (), (), ("workspace/**", "tasks/**"), ("/tfw-handoff",), "ROUTE_STOP",
        ),
        FixtureSpec(
            "coordinator_uncertain", "Coordinator", "/tfw-plan", ambiguous_a,
            "/tfw-plan Continue the synthetic ambiguous evaluation task. Two candidates are present and no canonical identifier is supplied. Resolve ambiguity without changing files.",
            ("AGENTS.md", ".tfw/workflows/plan.md"), (), (),
            ("workspace/**", "tasks/**"), ("?", "identifier", "task"), "AMBIGUITY_STOP",
        ),
        FixtureSpec(
            "researcher_stage", "Researcher", "/tfw-research", research_id,
            f"/tfw-research Start the first focused research stage for {research_id}. Write only the required Briefing stage artifact and stop at its stage checkpoint.",
            ("AGENTS.md", ".tfw/workflows/research/base.md", f"workspace/2026/{research_id}/status.md"),
            (f"workspace/2026/{research_id}/research/iter1/1_briefing.md",),
            (f"workspace/2026/{research_id}/research/iter1/1_briefing.md",),
            (f"workspace/2026/{research_id}/research/iter1/2_gather.md", f"workspace/2026/{research_id}/research/iter1/RES.md", "**/HL-*.md", "**/TS__*.md"),
            ("stop", "briefing", "checkpoint"), "BRIEFING_STOP",
        ),
        FixtureSpec(
            "executor_onboarding", "Executor", "/tfw-handoff", executor_id,
            f"/tfw-handoff Onboard to approved task {executor_id}. The owner label choice is unresolved. Create and commit only the ONB, then wait; do not implement or transition state.",
            ("AGENTS.md", ".tfw/workflows/handoff.md", f"workspace/2026/{executor_id}/status.md"),
            (f"workspace/2026/{executor_id}/ONB__{executor_id}.md",),
            (f"workspace/2026/{executor_id}/ONB__{executor_id}.md",),
            (f"workspace/2026/{executor_id}/status.md", f"workspace/2026/{executor_id}/journal/**", "**/RF__*.md", "**/REVIEW__*.md", "docs/**", ".tfw/**"),
            ("?", "blocking", "wait"), "ONB_WAIT",
        ),
        FixtureSpec(
            "reviewer_map", "Reviewer", "/tfw-review", reviewer_id,
            f"/tfw-review Begin review for {reviewer_id}. Execute only the Map stage and stop before Verify, Judge, or a verdict.",
            ("AGENTS.md", ".tfw/workflows/review.md", f"workspace/2026/{reviewer_id}/status.md"),
            (f"workspace/2026/{reviewer_id}/review/map.md",),
            (f"workspace/2026/{reviewer_id}/review/map.md",),
            (f"workspace/2026/{reviewer_id}/review/verify.md", f"workspace/2026/{reviewer_id}/review/judge.md", "**/REVIEW__*.md", "**/ONB__*.md", "**/RF__*.md"),
            ("stop", "map", "verify"), "MAP_STOP",
        ),
    )


def schedule(repetitions: int = 3) -> tuple[ScheduleItem, ...]:
    result: list[ScheduleItem] = []
    ordinal = 0
    for fixture in fixture_specs():
        for repetition in range(1, repetitions + 1):
            for arm in ARMS:
                ordinal += 1
                result.append(ScheduleItem(ordinal, fixture.key, repetition, arm))
    return tuple(result)


def _write_files(root: Path, files: dict[str, str]) -> None:
    for relative, content in files.items():
        destination = root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8", newline="\n")


def _copy_base(root: Path) -> None:
    for directory in (".tfw", "knowledge", "team"):
        shutil.copytree(PROJECT_ROOT / directory, root / directory)
    for filename in ("AGENTS.md", "README.md", "KNOWLEDGE.md", ".gitignore"):
        source = PROJECT_ROOT / filename
        if source.is_file():
            shutil.copy2(source, root / filename)
    shutil.copytree(PROJECT_ROOT / ".agents" / "skills", root / ".agents" / "skills")


def _fixture_files(spec: FixtureSpec) -> dict[str, str]:
    if spec.key == "coordinator_new":
        return {}
    if spec.key == "coordinator_resume":
        files = _artifact_set(spec.task_id, "TS_DRAFT", approved_ts=True)
        files[f"workspace/2026/{spec.task_id}/TS__{spec.task_id}.md"] = (
            f"# TS — {spec.task_id}: Approved synthetic execution\n\n"
            "> **Date**: 2026-09-05\n> **Author**: Fixture Coordinator\n"
            "> **Status**: ✅ APPROVED — saubakirov, 2026-09-05\n"
            f"> **Parent HL**: [{spec.task_id}](HL-{spec.task_id}.md)\n\n"
            "## 1. Objective\n\nExecute the already-approved synthetic boundary.\n\n"
            "## 2. Scope\n\nNo planning change remains.\n\n"
            "## 5. Acceptance Criteria\n\n- [ ] AC-1: Executor records onboarding evidence.\n"
        )
        return files
    if spec.key == "coordinator_uncertain":
        first = _artifact_set(spec.task_id, "HL_DRAFT")
        second_id = "TFW_20260905-000007_EVALAMB"
        return {**first, **_artifact_set(second_id, "HL_DRAFT")}
    if spec.key == "researcher_stage":
        files = _artifact_set(spec.task_id, "RES")
        files[f"workspace/2026/{spec.task_id}/research/iterations.yaml"] = (
            f"task_id: {spec.task_id}\n"
            "title: \"Synthetic command-entry research\"\n"
            "min_iterations: 2\nmax_iterations: 5\niterations:\n"
            "  - number: 1\n    focus: \"command entry\"\n"
            "    hypotheses: [H1]\n    status: pending\n"
            "    res_file: research/iter1/RES.md\n"
        )
        return files
    if spec.key == "executor_onboarding":
        return _artifact_set(spec.task_id, "TS_DRAFT", approved_ts=True)
    if spec.key == "reviewer_map":
        files = _artifact_set(spec.task_id, "RF", approved_ts=True)
        task = f"workspace/2026/{spec.task_id}"
        files[f"{task}/RF__{spec.task_id}.md"] = (
            f"# RF — {spec.task_id}: Synthetic result\n\n"
            "> **Status**: 🟢 Complete\n\n## 1. Summary\n\nNo product change.\n\n"
            "## 2. What Was Done\n\nFixture prepared.\n\n## 3. Files Changed\n\nNo product files.\n\n"
            "## 4. Acceptance Criteria Results\n\n| AC | Status | Evidence |\n|---|---|---|\n| AC-1 | VERIFIED | fixture |\n\n"
            "## 5. Evidence\n\nSee evidence/EV.md for evidence details. VERIFIED: 1.\n\n"
            "## 6. Deviations\n\nNo deviations.\n\n## 7. Fact Candidates\n\nNo fact candidates.\n\n"
            "## 8. Strategic Insights\n\nNo strategic insights.\n\n## 9. Diagrams\n\nNo diagrams.\n\n"
            "## Observations (out-of-scope, not modified)\n\nNo observations.\n"
        )
        files[f"{task}/evidence/EV.md"] = "# EV\n\n| AC | Status | Artifact |\n|---|---|---|\n| AC-1 | VERIFIED | RF |\n"
        return files
    raise ValueError(spec.key)


def create_fixture(spec: FixtureSpec, arm: str, parent: Path | None = None) -> tuple[Path, str, dict[str, str]]:
    temp_parent = (parent or Path(tempfile.gettempdir())).resolve()
    temp_parent.mkdir(parents=True, exist_ok=True)
    root = Path(tempfile.mkdtemp(prefix="tfw-command-entry-", dir=temp_parent)).resolve()
    if root == temp_parent or not root.is_relative_to(temp_parent) or root.is_relative_to(PROJECT_ROOT.resolve()):
        raise RuntimeError(f"unsafe disposable fixture path: {root}")
    _copy_base(root)
    _write_files(root, _fixture_files(spec))
    command = _command_name(spec.command)
    (root / _skill_path(command)).write_text(arm_skill(command, arm), encoding="utf-8", newline="\n")
    subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    subprocess.run(["git", "config", "user.email", "tfw-eval@example.invalid"], cwd=root, check=True)
    subprocess.run(["git", "config", "user.name", "TFW evaluation fixture"], cwd=root, check=True)
    subprocess.run(["git", "add", "--all"], cwd=root, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "fixture baseline"], cwd=root, check=True)
    baseline = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=root, check=True, capture_output=True,
        text=True, encoding="utf-8",
    ).stdout.strip()
    graded = set(spec.required_inputs)
    graded.add(_skill_path(command))
    graded.add(_workflow_path(command))
    hashes = {path: _sha256_file(root / path) for path in sorted(graded) if (root / path).is_file()}
    return root, baseline, hashes


def cleanup_fixture(root: Path, parent: Path | None = None) -> None:
    resolved = root.resolve()
    temp_parent = (parent or Path(tempfile.gettempdir())).resolve()
    if resolved == temp_parent or not resolved.is_relative_to(temp_parent):
        raise RuntimeError(f"refusing cleanup outside disposable parent: {resolved}")
    if resolved == PROJECT_ROOT.resolve() or PROJECT_ROOT.resolve().is_relative_to(resolved):
        raise RuntimeError(f"refusing cleanup of repository path: {resolved}")
    def remove_readonly(function, path, excinfo):
        del excinfo
        os.chmod(path, stat.S_IWRITE)
        function(path)

    shutil.rmtree(resolved, onexc=remove_readonly)


def _git_changed_paths(root: Path, baseline: str) -> tuple[str, ...]:
    tracked = subprocess.run(
        ["git", "diff", "--name-only", "-z", baseline, "--"], cwd=root, check=True,
        capture_output=True,
    ).stdout.split(b"\0")
    untracked = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard", "-z"], cwd=root, check=True,
        capture_output=True,
    ).stdout.split(b"\0")
    return tuple(sorted({part.decode("utf-8") for part in (*tracked, *untracked) if part}))


def _git_diff(root: Path, baseline: str) -> str:
    return subprocess.run(
        ["git", "diff", "--name-status", "--find-renames=50%", baseline, "--"], cwd=root,
        check=True, capture_output=True, text=True, encoding="utf-8",
    ).stdout


def redact(value: object) -> object:
    if isinstance(value, dict):
        return {str(key): ("<redacted>" if SECRET_KEY.search(str(key)) else redact(item))
                for key, item in value.items()}
    if isinstance(value, list):
        return [redact(item) for item in value]
    if isinstance(value, str):
        return SECRET_TEXT.sub(lambda match: (match.group(1) or match.group(2)) + "<redacted>", value)
    return value


def parse_events(stdout: str) -> tuple[list[dict], list[str]]:
    events: list[dict] = []
    unparsed: list[str] = []
    for line in stdout.splitlines():
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError:
            unparsed.append(str(redact(line)))
            continue
        if isinstance(value, dict):
            events.append(redact(value))
        else:
            unparsed.append(str(redact(line)))
    return events, unparsed


def _event_item(event: dict) -> dict:
    item = event.get("item")
    return item if isinstance(item, dict) else {}


def event_commands(events: Sequence[dict]) -> tuple[str, ...]:
    result: list[str] = []
    for event in events:
        item = _event_item(event)
        if item.get("type") in {"command_execution", "shell_command", "command"}:
            command = item.get("command") or item.get("cmd")
            if isinstance(command, str):
                result.append(command)
        elif event.get("type") in {"command_execution", "shell_command"}:
            command = event.get("command")
            if isinstance(command, str):
                result.append(command)
    return tuple(result)


def final_message(events: Sequence[dict]) -> str:
    messages: list[str] = []
    for event in events:
        item = _event_item(event)
        if item.get("type") in {"agent_message", "message"} and isinstance(item.get("text"), str):
            messages.append(item["text"])
        elif event.get("type") in {"agent_message", "message"} and isinstance(event.get("text"), str):
            messages.append(event["text"])
    return messages[-1] if messages else ""


def event_usage(events: Sequence[dict]) -> dict[str, int | None]:
    candidates: list[dict] = []
    for event in events:
        for value in (event.get("usage"), _event_item(event).get("usage")):
            if isinstance(value, dict):
                candidates.append(value)
    if not candidates:
        return {"input_tokens": None, "output_tokens": None, "total_tokens": None}
    usage = candidates[-1]
    input_tokens = usage.get("input_tokens")
    output_tokens = usage.get("output_tokens")
    if not isinstance(input_tokens, int):
        input_tokens = None
    if not isinstance(output_tokens, int):
        output_tokens = None
    total = input_tokens + output_tokens if input_tokens is not None and output_tokens is not None else None
    return {"input_tokens": input_tokens, "output_tokens": output_tokens, "total_tokens": total}


def _normalized_command(value: str) -> str:
    return value.casefold().replace("\\", "/")


def _read_index(commands: Sequence[str], path: str) -> int | None:
    needle = path.casefold().replace("\\", "/")
    for index, command in enumerate(commands):
        normalized = _normalized_command(command)
        if needle in normalized and any(verb in normalized for verb in READ_VERBS):
            return index
    return None


def _matches_any(path: str, patterns: Iterable[str]) -> bool:
    return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)


def grade_run(spec: FixtureSpec, arm: str, events: Sequence[dict], changed_paths: Sequence[str]) -> dict[str, object]:
    command = _command_name(spec.command)
    commands = event_commands(events)
    skill = _skill_path(command)
    workflow = _workflow_path(command)
    skill_index = _read_index(commands, skill)
    workflow_index = _read_index(commands, workflow)
    invocation = skill_index is not None
    complete_load = invocation if arm == "direct" else workflow_index is not None
    ordered = invocation and (arm == "direct" or (workflow_index is not None and skill_index < workflow_index))
    status_paths = [path for path in spec.required_inputs if path.endswith("/status.md")]
    for path in status_paths:
        status_index = _read_index(commands, path)
        ordered = ordered and status_index is not None
        if status_index is not None:
            boundary = skill_index if arm == "direct" else workflow_index
            ordered = ordered and boundary is not None and boundary < status_index
    forbidden = tuple(path for path in changed_paths if _matches_any(path, spec.forbidden_writes))
    unexpected = tuple(path for path in changed_paths
                       if spec.allowed_writes and not _matches_any(path, spec.allowed_writes))
    if not spec.allowed_writes:
        unexpected = tuple(changed_paths)
    missing_writes = tuple(pattern for pattern in spec.required_writes
                           if not any(fnmatch.fnmatch(path, pattern) for path in changed_paths))
    role_boundary = not forbidden and not unexpected
    gate_stop = role_boundary and not missing_writes
    message = final_message(events).casefold()
    final_route = bool(message) and all(pattern.casefold() in message for pattern in spec.final_patterns)
    graders = {
        "invocation": invocation,
        "complete_load": complete_load,
        "read_contract_order": ordered,
        "role_artifact_boundary": role_boundary,
        "gate_stop": gate_stop,
        "final_route": final_route,
    }
    return {
        "graders": graders,
        "aggregate_pass": all(graders.values()),
        "observed": {
            "command_count": len(commands),
            "skill_read_index": skill_index,
            "workflow_read_index": workflow_index,
            "changed_paths": list(changed_paths),
            "forbidden_changes": list(forbidden),
            "unexpected_changes": list(unexpected),
            "missing_required_writes": list(missing_writes),
            "final_message_present": bool(message),
        },
    }


def codex_command(root: Path, prompt: str, model: str, reasoning: str) -> list[str]:
    return [
        "codex", "exec", "--ephemeral", "--ignore-user-config", "--sandbox", "workspace-write",
        "--model", model, "--config", f'model_reasoning_effort="{reasoning}"',
        "--config", 'approval_policy="never"', "--json", "--cd", str(root), prompt,
    ]


def subprocess_runner(command: Sequence[str], cwd: Path, timeout_seconds: int) -> RunnerResult:
    started = time.perf_counter()
    try:
        completed = subprocess.run(
            list(command), cwd=cwd, capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=timeout_seconds, env=os.environ.copy(),
        )
        return RunnerResult(completed.returncode, completed.stdout, completed.stderr,
                            time.perf_counter() - started)
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout.decode("utf-8", "replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr = exc.stderr.decode("utf-8", "replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "")
        return RunnerResult(124, stdout, stderr, time.perf_counter() - started, True)


def _append_jsonl(path: Path, record: dict) -> None:
    with path.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def _valid_infrastructure(result: RunnerResult, events: Sequence[dict], unparsed: Sequence[str]) -> tuple[bool, str | None]:
    if result.timed_out:
        return False, "timeout"
    if result.returncode != 0:
        return False, f"codex_exit_{result.returncode}"
    if not events:
        return False, "no_json_events"
    if unparsed:
        return False, "unparsed_stdout"
    if not final_message(events):
        return False, "no_final_agent_message"
    return True, None


def execute_attempt(
    spec: FixtureSpec,
    item: ScheduleItem,
    attempt: int,
    model: str,
    reasoning: str,
    timeout_seconds: int,
    runner: Callable[[Sequence[str], Path, int], RunnerResult] = subprocess_runner,
    fixture_parent: Path | None = None,
) -> dict:
    root, baseline, hashes = create_fixture(spec, item.arm, fixture_parent)
    command = codex_command(root, spec.prompt, model, reasoning)
    try:
        result = runner(command, root, timeout_seconds)
        events, unparsed = parse_events(result.stdout)
        changed_paths = _git_changed_paths(root, baseline)
        grading = grade_run(spec, item.arm, events, changed_paths)
        valid, invalid_reason = _valid_infrastructure(result, events, unparsed)
        usage = event_usage(events)
        record = {
            "record_type": "attempt",
            "schema_version": 1,
            "run_id": f"{item.schedule_id}__a{attempt}",
            "schedule_id": item.schedule_id,
            "ordinal": item.ordinal,
            "attempt": attempt,
            "fixture": spec.key,
            "role": spec.role,
            "command": spec.command,
            "arm": item.arm,
            "repetition": item.repetition,
            "model": model,
            "reasoning": reasoning,
            "cli": {"argv": command[:-1] + ["<fixed-fixture-prompt>"], "returncode": result.returncode,
                    "timed_out": result.timed_out, "stderr": redact(result.stderr)},
            "valid": valid,
            "invalid_reason": invalid_reason,
            "elapsed_seconds": result.elapsed_seconds,
            "usage": usage,
            "input_hashes": hashes,
            "non_arm_hash": _sha256_bytes(json.dumps(
                {key: value for key, value in hashes.items() if key != _skill_path(_command_name(spec.command))},
                sort_keys=True,
            ).encode("utf-8")),
            "arm_hash": hashes[_skill_path(_command_name(spec.command))],
            "expectation": {
                "allowed_writes": list(spec.allowed_writes),
                "required_writes": list(spec.required_writes),
                "forbidden_writes": list(spec.forbidden_writes),
                "final_patterns": list(spec.final_patterns),
                "gate": spec.gate,
            },
            "grading": grading,
            "git_diff_name_status": _git_diff(root, baseline),
            "events": events,
            "raw_unparsed_stdout": list(unparsed),
            "redaction": {
                "credential_key_pattern": SECRET_KEY.pattern,
                "credential_text_pattern": SECRET_TEXT.pattern,
                "environment_serialized": False,
            },
        }
        return record
    finally:
        cleanup_fixture(root, fixture_parent)


def run_matrix(args: argparse.Namespace, runner=subprocess_runner) -> int:
    if args.model != DEFAULT_MODEL or args.reasoning != DEFAULT_REASONING:
        raise ValueError(
            f"approved live matrix requires {DEFAULT_MODEL}/{DEFAULT_REASONING}, got "
            f"{args.model}/{args.reasoning}")
    output = Path(args.output).resolve()
    if output.exists():
        raise FileExistsError(f"raw evidence output already exists: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    arm_validation = validate_arm_builders()
    if not arm_validation["valid"]:
        raise RuntimeError("arm builder validation failed: " + "; ".join(arm_validation["errors"]))
    planned = schedule(args.repetitions)
    if len(planned) != args.max_runs:
        raise ValueError(f"schedule has {len(planned)} runs, max-runs requires {args.max_runs}")
    preflight = {
        "record_type": "run_start",
        "schema_version": 1,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "model": args.model,
        "reasoning": args.reasoning,
        "valid_denominator": args.max_runs,
        "max_tokens": args.max_tokens,
        "max_minutes": args.max_minutes,
        "timeout_seconds": args.timeout_seconds,
        "host": {
            "platform": platform.platform(),
            "python": sys.version.split()[0],
            "codex_cli": subprocess.run(
                ["codex", "--version"], capture_output=True, text=True, encoding="utf-8",
                errors="replace", check=True,
            ).stdout.strip(),
            "capabilities": ["--ephemeral", "--ignore-user-config", "workspace-write", "--json"],
        },
        "arm_validation": arm_validation,
        "evidence_levels": EVIDENCE_LEVELS,
        "schedule": [asdict(item) | {"schedule_id": item.schedule_id} for item in planned],
    }
    _append_jsonl(output, preflight)
    specs = {spec.key: spec for spec in fixture_specs()}
    started = time.perf_counter()
    reported_tokens = 0
    valid_count = 0
    attempts = 0
    blocked_reason: str | None = None
    for item in planned:
        attempt = 0
        while True:
            elapsed_minutes = (time.perf_counter() - started) / 60
            if elapsed_minutes >= args.max_minutes:
                blocked_reason = "time_ceiling_before_54_valid_runs"
                break
            if reported_tokens >= args.max_tokens:
                blocked_reason = "token_ceiling_before_54_valid_runs"
                break
            attempt += 1
            attempts += 1
            record = execute_attempt(
                specs[item.fixture], item, attempt, args.model, args.reasoning,
                args.timeout_seconds, runner, Path(args.fixture_parent).resolve() if args.fixture_parent else None,
            )
            _append_jsonl(output, record)
            total = record["usage"]["total_tokens"]
            if isinstance(total, int):
                reported_tokens += total
            if record["valid"]:
                valid_count += 1
                break
        if blocked_reason:
            break
    elapsed_seconds = time.perf_counter() - started
    complete = valid_count == args.max_runs and blocked_reason is None
    _append_jsonl(output, {
        "record_type": "run_end",
        "schema_version": 1,
        "complete": complete,
        "valid_runs": valid_count,
        "attempts": attempts,
        "reported_tokens": reported_tokens,
        "elapsed_seconds": elapsed_seconds,
        "blocked_reason": blocked_reason,
        "finished_at": datetime.now(timezone.utc).isoformat(),
    })
    print(json.dumps({
        "output": str(output), "complete": complete, "valid_runs": valid_count,
        "attempts": attempts, "reported_tokens": reported_tokens,
        "elapsed_seconds": round(elapsed_seconds, 3), "blocked_reason": blocked_reason,
    }, indent=2))
    return 0 if complete else 2


def wilson_interval(successes: int, total: int, z: float = 1.959963984540054) -> tuple[float, float]:
    if total <= 0:
        raise ValueError("Wilson interval requires a positive denominator")
    proportion = successes / total
    denominator = 1 + z * z / total
    center = (proportion + z * z / (2 * total)) / denominator
    spread = z * math.sqrt(proportion * (1 - proportion) / total + z * z / (4 * total * total)) / denominator
    return max(0.0, center - spread), min(1.0, center + spread)


def newcombe_difference(a_success: int, a_total: int, b_success: int, b_total: int) -> tuple[float, float]:
    """Newcombe score interval for independent proportions, reported as A minus B."""
    pa, pb = a_success / a_total, b_success / b_total
    la, ua = wilson_interval(a_success, a_total)
    lb, ub = wilson_interval(b_success, b_total)
    difference = pa - pb
    lower = difference - math.sqrt((pa - la) ** 2 + (ub - pb) ** 2)
    upper = difference + math.sqrt((ua - pa) ** 2 + (pb - lb) ** 2)
    return max(-1.0, lower), min(1.0, upper)


def production_decision(
    arm_counts: dict[str, tuple[int, int]],
    role_counts: dict[str, dict[str, tuple[int, int]]],
    strengthened_max_words: int,
    structural_tests_pass: bool = True,
) -> dict[str, object]:
    base_success, base_total = arm_counts["current"]
    base_rate = base_success / base_total
    comparisons: dict[str, dict[str, object]] = {}
    for arm in ("strengthened", "direct"):
        success, total = arm_counts[arm]
        rate = success / total
        interval = newcombe_difference(success, total, base_success, base_total)
        role_deltas: dict[str, float] = {}
        for role in sorted(role_counts["current"]):
            challenger_success, challenger_total = role_counts[arm][role]
            current_success, current_total = role_counts["current"][role]
            role_deltas[role] = challenger_success / challenger_total - current_success / current_total
        comparisons[arm] = {
            "rate": rate,
            "baseline_rate": base_rate,
            "difference": rate - base_rate,
            "difference_interval_95": list(interval),
            "role_deltas": role_deltas,
            "behavioural_rule_pass": (
                rate - base_rate >= 0.10 - 1e-12
                and interval[0] > 0
                and all(delta >= -0.05 - 1e-12 for delta in role_deltas.values())
            ),
        }
    if comparisons["direct"]["behavioural_rule_pass"]:
        result = "BLOCKED — NEW TS REQUIRED"
        reason = "direct prototype materially wins but has no production migration authority"
    elif (comparisons["strengthened"]["behavioural_rule_pass"]
          and strengthened_max_words <= 15 and structural_tests_pass):
        result = "STRENGTHENED SELECTED"
        reason = "strengthened clears behavioural, per-role, context, and preflight structural gates"
    else:
        result = "BASELINE RETAINED"
        reason = "no deployable challenger clears every predeclared threshold"
    return {
        "terminal_result": result,
        "reason": reason,
        "baseline_rate": base_rate,
        "comparisons": comparisons,
        "strengthened_max_added_words": strengthened_max_words,
        "strengthened_context_gate_pass": strengthened_max_words <= 15,
        "preflight_structural_tests_pass": structural_tests_pass,
        "candidate_regression_gates_required": True,
    }


def _records(path: Path) -> list[dict]:
    records = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSONL at line {number}: {exc}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"JSONL line {number} is not an object")
        records.append(value)
    return records


def summarize_records(records: Sequence[dict], check: bool = True) -> dict:
    starts = [record for record in records if record.get("record_type") == "run_start"]
    ends = [record for record in records if record.get("record_type") == "run_end"]
    attempts = [record for record in records if record.get("record_type") == "attempt"]
    if len(starts) != 1 or len(ends) != 1:
        raise ValueError("raw evidence requires exactly one run_start and one run_end")
    start, end = starts[0], ends[0]
    valid = [record for record in attempts if record.get("valid") is True]
    schedule_ids = [record["schedule_id"] for record in valid]
    expected_ids = [item["schedule_id"] for item in start["schedule"]]
    if check and schedule_ids != expected_ids[:len(schedule_ids)]:
        raise ValueError("valid runs are not the exact prefix of the predeclared schedule")
    blocked = not bool(end.get("complete"))
    if check and not blocked and len(valid) != int(start["valid_denominator"]):
        raise ValueError("fixed valid-run denominator is incomplete")
    if check and blocked and not end.get("blocked_reason"):
        raise ValueError("incomplete denominator has no recorded BLOCKED reason")
    if check and len(set(schedule_ids)) != len(schedule_ids):
        raise ValueError("valid run schedule contains duplicates")
    arm_counts: dict[str, tuple[int, int]] = {}
    role_counts: dict[str, dict[str, tuple[int, int]]] = {arm: {} for arm in ARMS}
    boundary_rates: dict[str, dict[str, dict[str, object]]] = {arm: {} for arm in ARMS}
    failures: dict[str, list[str]] = {arm: [] for arm in ARMS}
    for arm in ARMS:
        rows = [record for record in valid if record["arm"] == arm]
        success = sum(bool(record["grading"]["aggregate_pass"]) for record in rows)
        arm_counts[arm] = (success, len(rows))
        for role in sorted({record["role"] for record in rows}):
            role_rows = [record for record in rows if record["role"] == role]
            role_counts[arm][role] = (
                sum(bool(record["grading"]["aggregate_pass"]) for record in role_rows), len(role_rows)
            )
        graders = sorted(rows[0]["grading"]["graders"]) if rows else []
        for grader in graders:
            passed = sum(bool(record["grading"]["graders"][grader]) for record in rows)
            boundary_rates[arm][grader] = {
                "passed": passed,
                "total": len(rows),
                "rate": passed / len(rows),
                "wilson_95": list(wilson_interval(passed, len(rows))),
            }
        failures[arm] = [record["run_id"] for record in rows if not record["grading"]["aggregate_pass"]]
    validation = start["arm_validation"]
    if blocked:
        decision = {
            "terminal_result": "BASELINE RETAINED",
            "reason": "approved denominator infeasible under approved ceiling; comparative rule was not applied",
            "comparisons": {},
            "strengthened_max_added_words": int(validation["max_strengthened_word_delta"]),
            "strengthened_context_gate_pass": int(validation["max_strengthened_word_delta"]) <= 15,
            "preflight_structural_tests_pass": bool(validation["valid"]),
            "candidate_regression_gates_required": True,
            "production_skill_edits_authorized": False,
        }
    else:
        decision = production_decision(
            arm_counts, role_counts, int(validation["max_strengthened_word_delta"]),
            bool(validation["valid"]),
        )
    arm_summary = {}
    for arm, (success, total) in arm_counts.items():
        arm_summary[arm] = {
            "passed": success,
            "total": total,
            "rate": success / total if total else None,
            "wilson_95": list(wilson_interval(success, total)) if total else None,
            "roles": {
                role: {"passed": counts[0], "total": counts[1], "rate": counts[0] / counts[1]}
                for role, counts in role_counts[arm].items()
            },
            "boundaries": boundary_rates[arm],
            "failure_run_ids": failures[arm],
        }
    token_rows = [record["usage"] for record in attempts]
    reported = [row["total_tokens"] for row in token_rows if isinstance(row.get("total_tokens"), int)]
    non_arm_hashes: dict[str, set[str]] = {}
    for record in valid:
        non_arm_hashes.setdefault(record["fixture"], set()).add(record["non_arm_hash"])
    if check and any(len(values) != 1 for values in non_arm_hashes.values()):
        raise ValueError("non-arm fixture inputs differ between trial arms")
    return {
        "schema_version": 1,
        "source": "independent recomputation from raw command-entry JSONL",
        "valid_runs": len(valid),
        "valid_denominator": int(start["valid_denominator"]),
        "ac3_status": "BLOCKED" if blocked else "VERIFIED",
        "blocked_reason": end.get("blocked_reason"),
        "attempts": len(attempts),
        "invalid_attempts": len(attempts) - len(valid),
        "model": start["model"],
        "reasoning": start["reasoning"],
        "elapsed_seconds": end["elapsed_seconds"],
        "usage": {
            "reported_total_tokens": sum(reported),
            "attempts_with_reported_tokens": len(reported),
            "attempts_without_reported_tokens": len(token_rows) - len(reported),
            "missing_metrics_are_na": len(reported) != len(token_rows),
        },
        "evidence_levels": list(EVIDENCE_LEVELS),
        "non_arm_input_hashes": {key: next(iter(value)) for key, value in non_arm_hashes.items()},
        "arms": arm_summary,
        "pairwise_newcombe_vs_current": {
            arm: newcombe_difference(
                arm_counts[arm][0], arm_counts[arm][1],
                arm_counts["current"][0], arm_counts["current"][1],
            )
            for arm in ("strengthened", "direct") if arm_counts[arm][1] and arm_counts["current"][1]
        },
        "decision": decision,
        "limits": [
            "Live behavioural evidence is Codex-only on the recorded host/model/effort.",
            "Static source or receiver parity does not imply invocation, load, conformance, or comparative effect.",
            "Word-derived context estimates are not runtime billing telemetry.",
            "Candidate regression gates are recorded outside raw trials after the production decision.",
        ],
    }


def finalize_stop_command(args: argparse.Namespace) -> int:
    path = Path(args.input).resolve()
    records = _records(path)
    if any(record.get("record_type") == "run_end" for record in records):
        raise ValueError("raw evidence already has a run_end record")
    starts = [record for record in records if record.get("record_type") == "run_start"]
    if len(starts) != 1:
        raise ValueError("raw evidence requires exactly one run_start")
    attempts = [record for record in records if record.get("record_type") == "attempt"]
    valid = [record for record in attempts if record.get("valid") is True]
    reported = [record["usage"]["total_tokens"] for record in attempts
                if isinstance(record.get("usage", {}).get("total_tokens"), int)]
    completed_elapsed = sum(float(record.get("elapsed_seconds", 0)) for record in attempts)
    basis_runs = int(args.basis_runs)
    basis_tokens = int(args.basis_tokens)
    if basis_runs <= 0 or basis_runs > len(valid):
        raise ValueError("stop basis runs must resolve inside completed valid attempts")
    actual_basis = sum(int(record["usage"]["total_tokens"]) for record in valid[:basis_runs]
                       if isinstance(record.get("usage", {}).get("total_tokens"), int))
    if actual_basis != basis_tokens:
        raise ValueError(f"stop basis token mismatch: raw={actual_basis}, supplied={basis_tokens}")
    denominator = int(starts[0]["valid_denominator"])
    projection = basis_tokens / basis_runs * denominator
    record = {
        "record_type": "run_end",
        "schema_version": 1,
        "complete": False,
        "valid_runs": len(valid),
        "attempts": len(attempts),
        "reported_tokens": sum(reported),
        "elapsed_seconds": completed_elapsed,
        "blocked_reason": args.reason,
        "finished_at": datetime.now(timezone.utc).isoformat(),
        "coordinator_stop": {
            "basis_valid_runs": basis_runs,
            "basis_reported_tokens": basis_tokens,
            "linear_projection_for_approved_denominator": projection,
            "approved_denominator": denominator,
            "approved_token_ceiling": int(starts[0]["max_tokens"]),
            "completed_valid_runs_at_interrupt": len(valid),
            "completed_reported_tokens_at_interrupt": sum(reported),
            "unreported_interrupted_attempt": bool(args.unreported_interrupted_attempt),
        },
    }
    _append_jsonl(path, record)
    print(json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


def summary_command(args: argparse.Namespace) -> int:
    source = Path(args.input).resolve()
    summary = summarize_records(_records(source), check=args.check)
    rendered = json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.output:
        destination = Path(args.output).resolve()
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(rendered, encoding="utf-8", newline="\n")
    else:
        sys.stdout.write(rendered)
    return 0


def dry_run_command(args: argparse.Namespace) -> int:
    planned = schedule(args.repetitions)
    payload = {
        "model": args.model,
        "reasoning": args.reasoning,
        "valid_denominator": len(planned),
        "arms": list(ARMS),
        "fixtures": [asdict(spec) for spec in fixture_specs()],
        "schedule": [asdict(item) | {"schedule_id": item.schedule_id} for item in planned],
        "arm_validation": validate_arm_builders(),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="subcommand")
    dry = subparsers.add_parser("dry-run", help="emit the exact schedule without invoking Codex")
    dry.add_argument("--model", default=DEFAULT_MODEL)
    dry.add_argument("--reasoning", default=DEFAULT_REASONING)
    dry.add_argument("--repetitions", type=int, default=3)
    dry.set_defaults(handler=dry_run_command)

    run = subparsers.add_parser("run", help="execute the fixed ephemeral Codex matrix")
    run.add_argument("--model", default=DEFAULT_MODEL)
    run.add_argument("--reasoning", default=DEFAULT_REASONING)
    run.add_argument("--repetitions", type=int, default=3)
    run.add_argument("--max-runs", type=int, default=54)
    run.add_argument("--max-tokens", type=int, default=750_000)
    run.add_argument("--max-minutes", type=float, default=180)
    run.add_argument("--timeout-seconds", type=int, default=180)
    run.add_argument("--fixture-parent")
    run.add_argument("--output", required=True)
    run.set_defaults(handler=run_matrix)

    summary = subparsers.add_parser("summary", help="independently recompute rates and decision")
    summary.add_argument("--input", required=True)
    summary.add_argument("--output")
    summary.add_argument("--check", action="store_true")
    summary.set_defaults(handler=summary_command)

    stop = subparsers.add_parser("finalize-stop", help="append an evidence-preserving Coordinator stop")
    stop.add_argument("--input", required=True)
    stop.add_argument("--reason", required=True)
    stop.add_argument("--basis-runs", required=True, type=int)
    stop.add_argument("--basis-tokens", required=True, type=int)
    stop.add_argument("--unreported-interrupted-attempt", action="store_true")
    stop.set_defaults(handler=finalize_stop_command)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not getattr(args, "subcommand", None):
        parser.print_help()
        return 0
    if getattr(args, "repetitions", 1) <= 0:
        parser.error("--repetitions must be positive")
    return int(args.handler(args))


if __name__ == "__main__":
    raise SystemExit(main())
