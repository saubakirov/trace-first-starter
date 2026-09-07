"""Contract tests for the bounded read-only upstream doctor."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml

TOOLS = Path(__file__).resolve().parents[1]
SCRIPT = TOOLS / "tfw_doctor.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"
sys.path.insert(0, str(TOOLS))

import tfw_doctor as doctor  # noqa: E402
import tfw_state as state  # noqa: E402


def make_project(tmp_path: Path) -> Path:
    (tmp_path / ".tfw").mkdir()
    config = {
        "project": {"name": "fixture"},
        "tfw": {
            "version": "test",
            "task_containers": ["tasks"],
            "statuses": [{"id": item} for item in state.DECLARED_LIFECYCLES],
        },
        "build": {"test": "python -m pytest tests/ -q"},
    }
    (tmp_path / ".tfw" / "project_config.yaml").write_text(
        yaml.safe_dump(config, sort_keys=False), encoding="utf-8"
    )
    (tmp_path / ".tfw" / "knowledge_state.yaml").write_text(
        "knowledge:\n  processed_task_digests: {}\n", encoding="utf-8"
    )
    (tmp_path / "team").mkdir()
    (tmp_path / "team" / "human.md").write_text(
        "---\nhandle: human\nname: Human\ntype: human\nsince: 2026-01-01\n---\n",
        encoding="utf-8",
    )
    item = tmp_path / "tasks" / "TFW_20260906-120000_EX"
    item.mkdir(parents=True)
    carrier = {
        "id": item.name,
        "title": "Example",
        "goal": "Goal",
        "value": "Value",
        "lifecycle": "TODO",
        "owner": "human",
        "authority": "HL.md",
        "created": "20260906-120000",
        "updated": "20260906-120000",
    }
    (item / "status.md").write_text(
        "---\n" + yaml.safe_dump(carrier, sort_keys=False) + "---\n", encoding="utf-8"
    )
    return tmp_path


def snapshot(root: Path) -> dict[str, bytes]:
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file()
    }


def run(root: Path, *operation: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(root), *operation, "--format", "json"],
        capture_output=True,
        text=True,
    )


def test_exact_operation_surface_and_stable_schema(tmp_path):
    root = make_project(tmp_path)
    contract = json.loads((FIXTURES / "doctor_schema.json").read_text(encoding="utf-8"))
    commands = {
        "status": ("status",),
        "check tasks": ("check", "tasks"),
        "check project": ("check", "project"),
        "knowledge-pending": ("knowledge-pending",),
    }
    assert list(commands) == contract["operations"]
    for name, command in commands.items():
        result = run(root, *command)
        assert result.returncode == 0, (name, result.stdout, result.stderr)
        payload = json.loads(result.stdout)
        assert sorted(payload) == contract["keys"]
        assert payload["operation"] == name


def test_json_and_human_output_are_deterministic_and_reads_write_nothing(tmp_path):
    root = make_project(tmp_path)
    before = snapshot(root)
    first = run(root, "check", "tasks")
    second = run(root, "check", "tasks")
    human_a = subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(root), "status"],
        capture_output=True,
        text=True,
    )
    human_b = subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(root), "status"],
        capture_output=True,
        text=True,
    )
    assert first.stdout == second.stdout
    assert human_a.stdout == human_b.stdout
    assert snapshot(root) == before


def test_material_and_indeterminate_findings_have_distinct_exit_codes(tmp_path):
    root = make_project(tmp_path)
    carrier = root / "tasks" / "TFW_20260906-120000_EX" / "status.md"
    text = carrier.read_text(encoding="utf-8").replace("lifecycle: TODO", "lifecycle: DONE")
    carrier.write_text(text, encoding="utf-8")
    material = run(root, "check", "tasks")
    assert material.returncode == 1
    assert json.loads(material.stdout)["material_findings"]

    carrier.write_text("not front matter\n", encoding="utf-8")
    indeterminate = run(root, "check", "tasks")
    assert indeterminate.returncode == 2
    assert json.loads(indeterminate.stdout)["indeterminate_findings"]


def test_unmatched_and_collision_inputs_are_indeterminate(tmp_path):
    root = make_project(tmp_path)
    (root / "tasks" / "notes").mkdir()
    assert run(root, "status").returncode == 2
    (root / "tasks" / "notes").rmdir()
    other = root / "archive"
    other.mkdir()
    document = yaml.safe_load((root / ".tfw" / "project_config.yaml").read_text(encoding="utf-8"))
    document["tfw"]["task_containers"] = ["tasks", "archive"]
    (root / ".tfw" / "project_config.yaml").write_text(
        yaml.safe_dump(document, sort_keys=False), encoding="utf-8"
    )
    duplicate = other / "TFW_20260906-120000_EX"
    duplicate.mkdir()
    assert run(root, "status").returncode == 2


def test_long_prose_is_exit_neutral_but_structural_errors_are_not(tmp_path):
    root = make_project(tmp_path)
    carrier = root / "tasks" / "TFW_20260906-120000_EX" / "status.md"
    text = carrier.read_text(encoding="utf-8").replace("goal: Goal", "goal: " + "x" * 1000)
    carrier.write_text(text, encoding="utf-8")
    clean = run(root, "check", "tasks")
    assert clean.returncode == 0
    assert not json.loads(clean.stdout)["material_findings"]


def test_live_repository_check_tasks_is_clean_and_known_123_event_is_exit_neutral():
    root = state.find_project_root(Path(__file__))
    result = run(root, "check", "tasks")
    assert result.returncode == 0, result.stdout
    payload = json.loads(result.stdout)
    assert not payload["material_findings"]
    assert not payload["indeterminate_findings"]


def test_capability_is_bounded_and_absent_from_full_build():
    root = state.find_project_root(Path(__file__))
    source = SCRIPT.read_text(encoding="utf-8")
    for forbidden in ("repair", "remediate", "behavior analysis", "daemon"):
        if forbidden == "repair":
            assert "never repairs" in source
        else:
            assert forbidden not in source
    config = (root / ".tfw" / "project_config.yaml").read_text(encoding="utf-8")
    build = yaml.safe_load(config)["build"]
    assert all("tfw_doctor.py" not in command for command in build.values())
