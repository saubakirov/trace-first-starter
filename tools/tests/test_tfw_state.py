"""Conformance tests for the upstream read-only semantic state library."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import tfw_state as state  # noqa: E402


PROJECT_ROOT = state.find_project_root(Path(__file__))


def project(tmp_path: Path, containers=("workspace", "tasks")) -> Path:
    (tmp_path / ".tfw").mkdir()
    (tmp_path / ".tfw" / "project_config.yaml").write_text(
        "tfw:\n"
        f"  task_containers: [{', '.join(containers)}]\n"
        "  statuses:\n"
        + "".join(f"    - id: {item}\n" for item in state.DECLARED_LIFECYCLES),
        encoding="utf-8",
    )
    (tmp_path / "team").mkdir()
    (tmp_path / "team" / "human.md").write_text(
        "---\nhandle: human\nname: A Human\ntype: human\nsince: 2026-01-01\n---\n",
        encoding="utf-8",
    )
    return tmp_path


def status_text(identifier: str, **updates) -> str:
    fields = {
        "id": identifier,
        "title": "A concise title",
        "goal": "A complete goal whose length is never a validity condition",
        "value": "A complete value",
        "lifecycle": "TODO",
        "owner": "human",
        "authority": "HL.md",
        "created": "20260906-120000",
        "updated": "20260906-120000",
    }
    fields.update(updates)
    return "---\n" + yaml.safe_dump(fields, sort_keys=False) + "---\n"


def task(root: Path, rel: str, **updates) -> Path:
    path = root / rel
    path.mkdir(parents=True)
    identifier = state.parse_identifier(path.name)[1]
    (path / "status.md").write_text(status_text(identifier, **updates), encoding="utf-8")
    return path


@pytest.mark.parametrize(
    "value,expected",
    [
        ("TFW_20260906-120000_EX", ("current", "TFW_20260906-120000_EX")),
        ("20260906-120000__dirty", ("clock", "20260906-120000__dirty")),
        ("TFW-12__legacy", ("legacy", "TFW-12")),
        ("20260906-120000", None),
        ("tfw_20260906-120000_EX", None),
        ("TFW_20260906-120000_EX_more", None),
    ],
)
def test_identifier_grammars_are_whole(value, expected):
    assert state.parse_identifier(value) == expected


def test_discovery_is_ordered_and_reports_unmatched(tmp_path):
    root = project(tmp_path)
    task(root, "workspace/2026/TFW_20260906-120000_Z")
    task(root, "tasks/TFW-2__legacy")
    (root / "tasks" / "not-an-id").mkdir(parents=True)
    assert [path.name for path in state.iter_task_dirs(root)] == [
        "TFW-2__legacy",
        "TFW_20260906-120000_Z",
    ]
    assert [path.name for path in state.iter_unmatched_task_dirs(root)] == ["not-an-id"]


def test_duplicate_identifier_is_indeterminate_not_chosen(tmp_path):
    root = project(tmp_path)
    task(root, "workspace/TFW-2__one")
    task(root, "tasks/TFW-2__two")
    with pytest.raises(state.IdentifierCollisionError, match="TFW-2"):
        state.iter_task_dirs(root)


def test_workspace_default_and_reference_scope_preserve_active_choices(tmp_path):
    assert state.task_containers(tmp_path) == ['workspace']
    root = project(tmp_path, containers=('current',))
    active = task(root, 'current/2026/TFW_20260906-120000_NOW')
    old = task(root, 'history/TFW-1__old')
    path = root / '.tfw/project_config.yaml'
    path.write_text(path.read_text() + '  historical_containers: [history, history/]\n')
    assert state.reference_containers(root) == ['current', 'history']
    assert state.iter_task_dirs(root) == [active]
    assert state.iter_task_dirs(root, state.reference_containers(root)) == [old, active]
    (root / '.tfw/knowledge_state.yaml').write_text('knowledge:\n  processed_task_digests: {}\n')
    assert set(state.knowledge_pending(root)['current_task_digests']) == {'TFW_20260906-120000_NOW'}
    path.write_text('tfw:\n  task_containers: tasks\n  historical_containers: [history]\n')
    assert state.task_containers(root) == ['tasks']  # existing scalar compatibility
    assert state.reference_containers(root) == ['tasks', 'history']


@pytest.mark.parametrize('history', ['tasks', None, [None], [''], ['../escape'], ['/absolute'], ['C:/outside']])
def test_malformed_historical_input_refuses_without_changing_active_choice(tmp_path, history):
    root = project(tmp_path, containers=('custom',))
    path = root / '.tfw/project_config.yaml'
    path.write_text(yaml.safe_dump({'tfw': {'task_containers': ['custom'], 'historical_containers': history}}))
    before = path.read_bytes()
    with pytest.raises(ValueError, match='historical'):
        state.reference_containers(root)
    assert path.read_bytes() == before
    assert state.task_containers(root) == ['custom']


def test_reference_collision_names_both_paths_while_current_discovery_is_unchanged(tmp_path):
    root = project(tmp_path, containers=('workspace',))
    active = task(root, 'workspace/TFW-1__current')
    task(root, 'tasks/TFW-1__history')
    config = root / '.tfw/project_config.yaml'
    config.write_text(config.read_text() + '  historical_containers: [tasks]\n')
    with pytest.raises(state.IdentifierCollisionError, match='tasks/TFW-1__history.*workspace/TFW-1__current'):
        state.iter_task_dirs(root, state.reference_containers(root))
    assert state.iter_task_dirs(root) == [active]


def test_status_semantics_keep_structural_rules_but_have_no_prose_ceiling(tmp_path):
    root = project(tmp_path)
    item = task(root, "tasks/TFW-1__legacy", goal="x" * 1000, value="y" * 1000)
    assert "_error" not in state.read_status(item)
    bad = task(root, "tasks/TFW-2__bad", lifecycle="DONE")
    assert "outcome is absent" in state.read_status(bad)["_error"]
    unknown = task(root, "tasks/TFW-3__unknown", lifecycle="UNDECLARED")
    assert "lifecycle_verbatim is absent" in state.read_status(unknown)["_error"]


def test_status_identity_and_closed_shape_are_enforced(tmp_path):
    root = project(tmp_path)
    item = task(root, "tasks/TFW-4__identity")
    data = yaml.safe_load((item / "status.md").read_text(encoding="utf-8").split("---")[1])
    data["id"] = "TFW-99"
    data["invented"] = True
    (item / "status.md").write_text(
        "---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n", encoding="utf-8"
    )
    error = state.read_status(item)["_error"]
    assert "unknown keys: invented" in error
    assert "disagrees with its directory" in error


def event(**updates) -> dict:
    value = {
        "time": "2026-09-06T12:00:00+05:00",
        "kind": "handoff",
        "writer": "human",
        "on_behalf_of": "human",
        "via": "test",
        "refs": ["status.md"],
        "summary": "complete",
    }
    value.update(updates)
    return value


def profiles() -> dict:
    return {
        "human": {"handle": "human", "name": "A Human", "type": "human", "since": "2026-01-01"}
    }


def test_current_event_accepts_writer_and_arbitrarily_long_one_line_summary():
    data = event(summary="z" * 1230)
    assert state.validate_event(data, "20260906-120000__handoff__abcd.md", profiles()) == []
    assert state.validate_new_event(data, "20260906-120000__handoff__abcd.md", profiles()) == []


def test_event_structural_counterexamples_remain_findings():
    data = event(on_behalf_of=None, refs=[], via="", writer="missing")
    problems = state.validate_new_event(
        data, "20260906-120000__handoff__nothex.md", profiles()
    )
    assert any("missing on_behalf_of" in item for item in problems)
    assert any("refs must be a non-empty list" in item for item in problems)
    assert any("via must be non-empty" in item for item in problems)
    assert any("writer 'missing'" in item for item in problems)
    assert any("four lowercase hex" in item for item in problems)


def test_legacy_actor_shape_is_readable_without_current_identity_rules():
    data = {
        "time": "2026-09-06T12:00:00+05:00",
        "kind": "handoff",
        "actor": "deleted-session",
        "refs": ["status.md"],
        "summary": "historical",
    }
    assert state.validate_event(data, "20260906-120000__handoff.md", {}) == []


def test_new_transition_requires_legal_pair_and_same_observed_second():
    data = event(kind="transition", **{"from": "ONB", "to": "RF"})
    assert state.validate_new_event(
        data, "20260906-120000__transition__abcd.md", profiles()
    ) == []
    data["to"] = "TODO"
    assert any(
        "illegal transition pair" in problem
        for problem in state.validate_new_event(
            data, "20260906-120000__transition__abcd.md", profiles()
        )
    )


def test_journal_reads_task_and_phase_and_reports_malformed_input(tmp_path):
    root = project(tmp_path)
    item = task(root, "workspace/TFW_20260906-120000_EX")
    phase = item / "phase-a"
    (phase / "journal").mkdir(parents=True)
    (phase / "status.md").write_text(status_text(item.name), encoding="utf-8")
    (phase / "journal" / "20260906-120000__handoff__abcd.md").write_text(
        "---\n" + yaml.safe_dump(event(), sort_keys=False) + "---\n", encoding="utf-8"
    )
    (item / "journal").mkdir()
    (item / "journal" / "bad.md").write_text("not yaml front matter\n", encoding="utf-8")
    events, problems = state.read_journal(item, profiles())
    assert events[0]["_file"].startswith("phase-a/journal/")
    assert any("bad.md: no YAML front matter" in problem for problem in problems)


def reference_sections(path: Path) -> list[tuple[str, str]]:
    """Independent small reference extractor for conformance fixtures."""
    lines = path.read_text(encoding="utf-8").replace("\r\n", "\n").splitlines(keepends=True)
    found: list[tuple[str, str]] = []
    selected = set(state.KNOWLEDGE_HEADINGS)
    index = 0
    fence = None
    while index < len(lines):
        stripped = lines[index].lstrip()
        marker = "```" if stripped.startswith("```") else "~~~" if stripped.startswith("~~~") else None
        if marker:
            fence = None if fence == marker else marker if fence is None else fence
            index += 1
            continue
        heading = state.MARKDOWN_HEADING.match(lines[index].rstrip("\n")) if fence is None else None
        canonical = state._knowledge_heading(heading.group("title")) if heading else None
        if canonical and any(canonical == name or canonical.startswith(name + " (") for name in selected):
            level = len(heading.group("marks"))
            end = index + 1
            inner_fence = None
            while end < len(lines):
                part = lines[end].lstrip()
                inner = "```" if part.startswith("```") else "~~~" if part.startswith("~~~") else None
                if inner:
                    inner_fence = None if inner_fence == inner else inner if inner_fence is None else inner_fence
                elif inner_fence is None:
                    next_heading = state.MARKDOWN_HEADING.match(lines[end].rstrip("\n"))
                    if next_heading and len(next_heading.group("marks")) <= level:
                        break
                end += 1
            found.append((canonical, "".join(lines[index + 1:end])))
            index = end
            continue
        index += 1
    return found


def independent_digest(rel: str, sections: list[tuple[str, str]]) -> str:
    digest = hashlib.sha256()
    if not sections:
        digest.update(b"\0\0")
    for heading, body in sections:
        digest.update(rel.encode())
        digest.update(b"\0")
        digest.update(heading.encode())
        digest.update(b"\0")
        digest.update(body.encode())
    return digest.hexdigest()


def test_knowledge_digest_matches_independent_reference_and_defeats_regex_mutant(tmp_path):
    root = project(tmp_path)
    item = task(root, "tasks/TFW-1__knowledge")
    artifact = item / "RF__TFW-1.md"
    artifact.write_text(
        "# RF\n\n```md\n## Fact Candidates\nmutant-only\n```\n\n"
        "## 7. Fact Candidates\nreal fact\n\n### Detail\nkept\n\n## Other\nstop\n",
        encoding="utf-8",
    )
    rel = artifact.relative_to(root).as_posix()
    expected = independent_digest(rel, reference_sections(artifact))
    actual = state.knowledge_task_digest(root, item)
    mutant_body = "mutant-only\n"
    mutant = independent_digest(rel, [("Fact Candidates", mutant_body)])
    assert actual == expected
    assert mutant != actual


def write_knowledge_state(root: Path, digests: dict[str, str]) -> None:
    (root / ".tfw" / "knowledge_state.yaml").write_text(
        yaml.safe_dump({"knowledge": {"processed_task_digests": digests}}, sort_keys=False),
        encoding="utf-8",
    )


def test_knowledge_pending_reports_changed_removed_and_migration(tmp_path):
    root = project(tmp_path)
    item = task(root, "tasks/TFW-1__knowledge")
    write_knowledge_state(root, {"TFW-1": "0" * 64, "TFW-99": "f" * 64})
    unresolved = state.knowledge_pending(root)
    assert unresolved["removed_task_ids"] == ["TFW-99"]
    assert unresolved["pending_task_ids"] == []
    assert unresolved["problems"]
    write_knowledge_state(root, {"TFW-1": state.knowledge_task_digest(root, item)})
    assert state.knowledge_pending(root)["pending_task_ids"] == []


@pytest.mark.parametrize(
    "mode,interval,pending,action",
    [
        ("off", 1, ["A"], "skip"),
        ("soft", 2, ["A"], "report"),
        ("hard", 2, ["A"], "continue"),
        ("hard", 2, ["A", "B"], "route:/tfw-knowledge"),
    ],
)
def test_knowledge_threshold_outcomes(mode, interval, pending, action):
    assert state.knowledge_gate_result(mode, interval, pending)["action"] == action


def test_library_has_no_cli_render_or_shared_write_surface():
    source = Path(state.__file__).read_text(encoding="utf-8")
    for forbidden in ("def main(", "def build(", "write_text(", "00-INDEX.md"):
        assert forbidden not in source


def test_repository_known_123_character_event_is_clean_and_unchanged_by_read():
    path = PROJECT_ROOT / "workspace/2026/TFW_20260902-112841_RDP/journal/20260902-181437__amendment_escalated__531a.md"
    before = path.read_bytes()
    data = yaml.safe_load(path.read_text(encoding="utf-8").split("---")[1])
    assert len(data["summary"]) == 123
    assert state.validate_event(data, path.name, state.team_profiles(PROJECT_ROOT)) == []
    assert path.read_bytes() == before
