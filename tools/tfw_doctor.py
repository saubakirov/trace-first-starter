"""Deterministic, read-only diagnostics for the upstream TFW repository.

This maintainer tool is authority over nothing and never repairs a receiver.  Its exact
operations are ``status``, ``check tasks``, ``check project``, and ``knowledge-pending``.
Exit 0 means a complete clean scoped read, 1 means determinate material findings, and 2
means an input or interpretation was indeterminate.  Advice and compatibility notes are
exit-neutral.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

import tfw_state as state


REPORT_KEYS = (
    "operation",
    "inputs",
    "records",
    "material_findings",
    "indeterminate_findings",
    "advice",
    "compatibility_notes",
)


def report(operation: str, root: Path) -> dict:
    return {
        "operation": operation,
        "inputs": {"root": root.as_posix()},
        "records": [],
        "material_findings": [],
        "indeterminate_findings": [],
        "advice": [],
        "compatibility_notes": [],
    }


def _path(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def _carrier_error(target: str, problem: str, result: dict) -> None:
    text = f"{target}: {problem}"
    if problem.startswith(("no YAML front matter", "unparseable", "front matter is not")):
        result["indeterminate_findings"].append(text)
    else:
        result["material_findings"].append(text)


def _task_inventory(root: Path, include_journals: bool) -> dict:
    result = report("check tasks" if include_journals else "status", root)
    try:
        declared = state.declared_lifecycles(root)
        profiles = state.team_profiles(root)
        tasks = state.iter_task_dirs(root)
        unmatched = state.iter_unmatched_task_dirs(root)
    except state.IdentifierCollisionError as exc:
        result["indeterminate_findings"].append(str(exc))
        return result
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
        result["indeterminate_findings"].append(f"task discovery is unreadable: {exc}")
        return result

    for path in unmatched:
        result["indeterminate_findings"].append(
            f"unmatched task directory: {_path(root, path)}"
        )

    for task_dir in tasks:
        kind, identifier = state.parse_identifier(task_dir.name)
        try:
            carrier = state.read_status(task_dir, declared)
        except (OSError, UnicodeError) as exc:
            result["indeterminate_findings"].append(
                f"{_path(root, task_dir / 'status.md')}: unreadable: {exc}"
            )
            carrier = None
        task_record = {
            "kind": "task",
            "id": identifier,
            "path": _path(root, task_dir),
            "lifecycle": None,
        }
        if carrier is None:
            if kind == "legacy":
                result["compatibility_notes"].append(
                    f"{identifier}: legacy task has no status.md; task-local artifacts remain readable"
                )
            else:
                result["material_findings"].append(f"{identifier}: current task has no status.md")
        elif carrier.get("_error"):
            _carrier_error(_path(root, task_dir / "status.md"), carrier["_error"], result)
        else:
            task_record["lifecycle"] = str(carrier.get("lifecycle"))
        result["records"].append(task_record)

        for phase_dir in state.iter_phase_dirs(task_dir):
            try:
                phase = state.read_phase_status(phase_dir, declared)
            except (OSError, UnicodeError) as exc:
                result["indeterminate_findings"].append(
                    f"{_path(root, phase_dir / 'status.md')}: unreadable: {exc}"
                )
                phase = None
            phase_record = {
                "kind": "phase",
                "id": identifier,
                "phase": phase_dir.name,
                "path": _path(root, phase_dir),
                "lifecycle": None,
            }
            if phase is None:
                if kind == "legacy":
                    result["compatibility_notes"].append(
                        f"{identifier}/{phase_dir.name}: legacy phase has no status.md"
                    )
                else:
                    result["material_findings"].append(
                        f"{_path(root, phase_dir)}: current phase has no status.md"
                    )
            elif phase.get("_error"):
                _carrier_error(_path(root, phase_dir / "status.md"), phase["_error"], result)
            else:
                phase_record["lifecycle"] = str(phase.get("lifecycle"))
            result["records"].append(phase_record)

        if include_journals:
            try:
                events, problems = state.read_journal(task_dir, profiles)
            except (OSError, UnicodeError) as exc:
                result["indeterminate_findings"].append(
                    f"{identifier}: journal is unreadable: {exc}"
                )
                continue
            result["inputs"].setdefault("journal_events", 0)
            result["inputs"]["journal_events"] += len(events)
            for problem in problems:
                if "predate the 2.0.0 event grammar" in problem:
                    result["compatibility_notes"].append(f"{identifier}: {problem}")
                elif any(mark in problem for mark in (
                    "no YAML front matter", "unparseable", "front matter is not a mapping",
                )):
                    result["indeterminate_findings"].append(f"{identifier}: {problem}")
                else:
                    result["material_findings"].append(f"{identifier}: {problem}")

    result["inputs"]["task_containers"] = state.task_containers(root)
    result["inputs"]["recognized_tasks"] = sum(
        item["kind"] == "task" for item in result["records"]
    )
    result["inputs"]["recognized_phases"] = sum(
        item["kind"] == "phase" for item in result["records"]
    )
    return result


def status(root: Path) -> dict:
    return _task_inventory(root, include_journals=False)


def check_tasks(root: Path) -> dict:
    return _task_inventory(root, include_journals=True)


def _retired_config_keys(document: object, prefix: str = "") -> list[str]:
    retired = {"max_summary_length", "max_index_lines", "max_index_facts_lines"}
    found: list[str] = []
    if isinstance(document, dict):
        for key, value in document.items():
            address = f"{prefix}.{key}" if prefix else str(key)
            if key in retired:
                found.append(address)
            found.extend(_retired_config_keys(value, address))
    elif isinstance(document, list):
        for index, value in enumerate(document):
            found.extend(_retired_config_keys(value, f"{prefix}[{index}]"))
    return found


def check_project(root: Path) -> dict:
    result = report("check project", root)
    config_path = root / ".tfw" / "project_config.yaml"
    if not config_path.is_file():
        result["indeterminate_findings"].append("missing .tfw/project_config.yaml")
        return result
    try:
        document = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        result["indeterminate_findings"].append(f"project configuration is unreadable: {exc}")
        return result
    if not isinstance(document, dict):
        result["indeterminate_findings"].append("project configuration is not a mapping")
        return result

    tfw = document.get("tfw")
    build = document.get("build")
    if not isinstance(tfw, dict):
        result["material_findings"].append("project configuration has no `tfw` mapping")
        tfw = {}
    if not isinstance(build, dict):
        result["material_findings"].append("project configuration has no `build` mapping")
        build = {}
    if not str(tfw.get("version", "")).strip():
        result["material_findings"].append("tfw.version is absent")
    for address in sorted(_retired_config_keys(document)):
        result["material_findings"].append(f"retired configuration key remains: {address}")
    for name, command in sorted(build.items()):
        if not isinstance(command, str):
            result["material_findings"].append(f"build.{name} is not a command string")
            continue
        if any(token in command for token in (".tfw/scripts", "gen_index.py", "tfw_doctor.py")):
            result["material_findings"].append(
                f"build.{name} depends on retired or optional diagnostics: {command}"
            )
    scripts = root / ".tfw" / "scripts"
    if scripts.exists():
        result["material_findings"].append("retired Full payload directory remains: .tfw/scripts")

    profiles = state.team_profiles(root)
    for handle, profile in sorted(profiles.items()):
        for problem in state.validate_profile(handle, profile, profiles):
            result["material_findings"].append(problem)
    result["records"] = [
        {"kind": "project", "version": tfw.get("version"), "profile_count": len(profiles)}
    ]
    result["inputs"]["task_containers"] = state.task_containers(root)
    return result


def knowledge_pending(root: Path) -> dict:
    result = report("knowledge-pending", root)
    try:
        data = state.knowledge_pending(root)
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
        result["indeterminate_findings"].append(f"knowledge inputs are unreadable: {exc}")
        return result
    result["records"] = [
        {"id": identifier, "digest": digest}
        for identifier, digest in sorted(data["current_task_digests"].items())
    ]
    result["inputs"].update({
        "pending_task_ids": data["pending_task_ids"],
        "removed_task_ids": data["removed_task_ids"],
        "migration_required": data["migration_required"],
    })
    result["indeterminate_findings"].extend(data["problems"])
    return result


def exit_code(result: dict) -> int:
    if result["indeterminate_findings"]:
        return 2
    if result["material_findings"]:
        return 1
    return 0


def render_human(result: dict) -> str:
    lines = [f"operation: {result['operation']}"]
    for key in REPORT_KEYS[1:]:
        value = result[key]
        lines.append(f"{key}: {len(value) if isinstance(value, list) else value}")
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    fields = ", ".join(f"{name}={item[name]}" for name in sorted(item))
                    lines.append(f"  - {fields}")
                else:
                    lines.append(f"  - {item}")
    return "\n".join(lines) + "\n"


def _add_format(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--format", choices=("human", "json"), default="human")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    commands = parser.add_subparsers(dest="command", required=True)
    status_parser = commands.add_parser("status", help="report recognized task and phase state")
    _add_format(status_parser)
    check = commands.add_parser("check", help="run a bounded structural check")
    check_commands = check.add_subparsers(dest="check", required=True)
    for name in ("tasks", "project"):
        leaf = check_commands.add_parser(name)
        _add_format(leaf)
    pending = commands.add_parser("knowledge-pending", help="report exact Knowledge Gate inputs")
    _add_format(pending)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = args.root.resolve()
    operation = args.command if args.command != "check" else f"check {args.check}"
    functions = {
        "status": status,
        "check tasks": check_tasks,
        "check project": check_project,
        "knowledge-pending": knowledge_pending,
    }
    try:
        result = functions[operation](root)
    except Exception as exc:  # CLI boundary: an incomplete read must be explicit and exit 2.
        result = report(operation, root)
        result["indeterminate_findings"].append(f"unresolved diagnostic input: {exc}")
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    else:
        print(render_human(result), end="")
    return exit_code(result)


if __name__ == "__main__":
    raise SystemExit(main())
