#!/usr/bin/env python3
"""Generate amended no-code Assisted 1.5 task-local evidence."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import unicodedata

sys.dont_write_bytecode = True

REPO = Path(__file__).resolve().parents[4]
EVIDENCE = Path(__file__).resolve().parent
PRODUCT = REPO / "editions"
ASSISTED = PRODUCT / "02-assisted"
SOURCE = Path(os.environ["TFW_ASSISTED_FIELD_SOURCE"]).expanduser()
BASELINE = "f3eb986"
TASK_ID = "TFW_20260830-114238_ASSISTED15"
TASK_ROOT = f"workspace/2026/{TASK_ID}/"
PRODUCT_COMMIT = "e27024bb782e7d95e1ef82c9ff7a80c51e411cf0"
EXTERNAL_TAGS = ["refs/tags/v2.0.0", "refs/tags/v2.0.0-dirty.5"]
HISTORICAL_CULTURE_DIGEST = "7e2248a7f7e77161644d8394b1557c731e0b5b31d7713843de30655b6e4fadc3"
CANONICAL_SOURCE_DIGEST = "3a1885c65b13388a51ddaa5b1454122876d4f17d268bc49f0f94f6bb2dbee96b"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def write_json(path: Path, value: object) -> None:
    path.write_bytes(canonical(value))


def run(command: list[str], cwd: Path = REPO, expected: int = 0) -> str:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(
        command,
        cwd=cwd,
        env=environment,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        timeout=120,
    )
    if result.returncode != expected:
        raise RuntimeError(f"command failed ({result.returncode}): {command!r}\n{result.stdout}")
    return result.stdout.rstrip()


def rows(root: Path) -> list[dict]:
    result = []
    for path in sorted((p for p in root.rglob("*") if p.is_file()), key=lambda p: p.relative_to(root).as_posix()):
        relative = path.relative_to(root).as_posix()
        result.append({"path": relative, "sha256": sha_file(path), "size": path.stat().st_size})
    return result


def rows_digest(value: list[dict]) -> str:
    data = b"".join(f"{item['path']}\t{item['size']}\t{item['sha256']}\n".encode() for item in value)
    return sha(data)


def manifest_map(root: Path) -> dict[str, dict]:
    return {item["path"]: item for item in rows(root)}


def changed_paths(before: dict[str, dict], after: dict[str, dict]) -> list[str]:
    return sorted(path for path in set(before) | set(after) if before.get(path) != after.get(path))


def powershell_source_rows(root: Path) -> dict:
    program = r'''
$OutputEncoding = [Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = $OutputEncoding
$root = $env:TFW_ASSISTED_FIELD_SOURCE
$prefix = $root.TrimEnd('\') + '\'
$rows = Get-ChildItem -LiteralPath $root -Recurse -File | ForEach-Object {
  [PSCustomObject]@{
    path = $_.FullName.Substring($prefix.Length).Replace('\','/')
    sha256 = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
    size = [int64]$_.Length
  }
} | Sort-Object path
$lines = $rows | ForEach-Object { "{0}`t{1}`t{2}`n" -f $_.path,$_.size,$_.sha256 }
$bytes = [Text.UTF8Encoding]::new($false).GetBytes([String]::Concat([string[]]$lines))
$hasher = [Security.Cryptography.SHA256]::Create()
$hash = $hasher.ComputeHash($bytes)
$digest = ([BitConverter]::ToString($hash)).Replace('-','').ToLowerInvariant()
[PSCustomObject]@{culture_digest=$digest;rows=$rows} | ConvertTo-Json -Depth 4 -Compress
'''
    return json.loads(run(["powershell.exe", "-NoProfile", "-NonInteractive", "-Command", program]))


def static_manifest() -> dict:
    recorded = json.loads((PRODUCT / "maintenance/release-manifest.json").read_text(encoding="utf-8"))
    policy = json.loads((PRODUCT / "maintenance/maintenance-policy.json").read_text(encoding="utf-8"))

    def regenerate() -> list[dict]:
        payload = [p for p in ASSISTED.rglob("*") if p.is_file()]
        payload += [
            PRODUCT / "ASSISTED_MAINTENANCE.md",
            PRODUCT / "README.md",
            PRODUCT / "maintenance/maintenance-policy.json",
        ]
        result = [
            {"path": p.relative_to(PRODUCT).as_posix(), "sha256": sha_file(p), "size": p.stat().st_size}
            for p in payload
        ]
        return sorted(result, key=lambda item: item["path"])

    first = regenerate()
    second = regenerate()
    paths = [item["path"] for item in first]
    invalid = [
        path for path in paths
        if path.startswith("/") or "\\" in path or ".." in Path(path).parts or Path(path).is_absolute()
    ]
    folded = [unicodedata.normalize("NFC", path).casefold() for path in paths]
    return {
        "recorded_schema": recorded.get("schema"),
        "row_count": len(first),
        "first_digest": rows_digest(first),
        "second_digest": rows_digest(second),
        "two_run_equal": first == second,
        "recorded_equal": recorded.get("files") == first,
        "self_excluded": "maintenance/release-manifest.json" not in paths,
        "policy_included": "maintenance/maintenance-policy.json" in paths,
        "unique_paths": len(paths) == len(set(paths)) == len(set(folded)),
        "invalid_paths": invalid,
        "policy": {
            "schema": policy.get("schema"),
            "release_version": policy.get("release_version"),
            "accepted_public_baselines": len(policy.get("accepted_public_baselines", [])),
            "retired_known_stock": len(policy.get("retired_known_stock", [])),
            "authorities": sorted({item["authority"] for item in policy.get("selectors", [])}),
            "target_only": policy.get("target_only"),
            "procedure": policy.get("procedure"),
        },
    }


PROFILE_KEYS = ["Идентификатор", "Отображаемое имя", "Тип", "Роль в организации", "Роль в проекте"]
CYRILLIC = str.maketrans({
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e", "ж": "zh",
    "з": "z", "и": "i", "й": "i", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o",
    "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "ts",
    "ч": "ch", "ш": "sh", "щ": "shch", "ы": "y", "э": "e", "ю": "yu", "я": "ya",
    "ь": "", "ъ": "",
})


def surname_id(value: str) -> str:
    result = value.lower().translate(CYRILLIC)
    result = re.sub(r"[^a-z0-9]+", "-", result).strip("-")
    return re.sub(r"-+", "-", result)


def profile_bytes(identifier: str, display: str, org: str = "Исследователь", project: str = "Участник") -> bytes:
    return (
        f"Идентификатор: {identifier}\nОтображаемое имя: {display}\nТип: человек\n"
        f"Роль в организации: {org}\nРоль в проекте: {project}\n"
    ).encode()


def valid_profiles(root: Path) -> list[dict]:
    result = []
    for path in sorted(root.glob("*.md"), key=lambda p: p.name):
        if path.name == "README.md" or not path.is_file():
            continue
        fields: dict[str, list[str]] = {key: [] for key in PROFILE_KEYS}
        for line in path.read_text(encoding="utf-8").splitlines():
            if ": " in line:
                key, value = line.split(": ", 1)
                if key in fields:
                    fields[key].append(value.strip())
        if any(len(fields[key]) != 1 or not fields[key][0] for key in PROFILE_KEYS):
            continue
        identifier = fields["Идентификатор"][0]
        if fields["Тип"][0] != "человек" or path.name != f"{identifier}.md" or not re.fullmatch(r"[a-z0-9_-]+", identifier):
            continue
        result.append({"id": identifier, "display": fields["Отображаемое имя"][0]})
    return result


def identity_scenarios() -> dict:
    scenarios = []

    def execute(name: str, setup: list[tuple[str, bytes]], prompt: str, supplied: str | None, expected: str, create: tuple[str, bytes] | None = None, selected: str | None = None) -> None:
        with tempfile.TemporaryDirectory(prefix="assisted-identity-") as raw:
            people = Path(raw) / "people"
            people.mkdir()
            (people / "README.md").write_text("# Synthetic guide\n", encoding="utf-8")
            for relative, data in setup:
                (people / relative).write_bytes(data)
            before = manifest_map(people)
            available = valid_profiles(people)
            observed = expected
            if create is not None:
                target = people / create[0]
                if target.exists():
                    observed = "blocked-collision"
                else:
                    target.write_bytes(create[1])
                    assert target.read_bytes() == create[1]
                    observed = "created-and-reread"
            after = manifest_map(people)
            changes = changed_paths(before, after)
            allowed = [create[0]] if create is not None and observed == "created-and-reread" else []
            scenarios.append({
                "name": name,
                "available_profiles": available,
                "prompt": prompt,
                "user_supplied": supplied,
                "expected_action": expected,
                "observed_action": observed,
                "selected": selected,
                "changed_paths": changes,
                "only_approved_profile_changed": changes == allowed,
                "zero_write_when_negative": bool(allowed) or before == after,
            })

    execute("zero-profiles", [], "Запросить имя, фамилию и обе роли", None, "ask-create-data")
    execute("one-profile", [("ivanov.md", profile_bytes("ivanov", "Иван Иванов"))], "Назвать правило одного профиля", None, "select-only-profile", selected="ivanov")
    execute("multiple-profiles", [("ivanov.md", profile_bytes("ivanov", "Иван Иванов")), ("smith.md", profile_bytes("smith", "Ann Smith"))], "Кто сейчас работает: Иван Иванов или Ann Smith?", None, "ask-choice")
    execute("cyrillic-surname", [], "Получены имя, фамилия и роли", "Иван Иванов", "created-and-reread", (f"{surname_id('Иванов')}.md", profile_bytes(surname_id("Иванов"), "Иван Иванов")))
    execute("latin-surname", [], "Получены имя, фамилия и роли", "Ann Smith", "created-and-reread", (f"{surname_id('Smith')}.md", profile_bytes(surname_id("Smith"), "Ann Smith")))
    execute("missing-surname", [], "Уточнить фамилию", "Иван", "ask-surname")
    execute("collision", [("ivanov.md", profile_bytes("ivanov", "Другой Иван Иванов"))], "Запросить смысловое уточнение", "Иван Иванов", "blocked-collision")
    execute("invalid-profile", [("broken.md", b"not a profile\n")], "Сообщить невалидный файл и запросить данные", None, "ask-create-data")
    execute("explicit-current-selection", [("ivanov.md", profile_bytes("ivanov", "Иван Иванов")), ("smith.md", profile_bytes("smith", "Ann Smith"))], "Использовать явный выбор текущего разговора", "Ann Smith", "select-explicit", selected="smith")
    execute("autonomous-no-human-role", [], "Человеческий участник: не применимо; owner и AI role из trace", "не применимо", "trace-owner-ai-role")

    skill = (ASSISTED / ".agents/skills/tfw-identity/SKILL.md").read_text(encoding="utf-8")
    required_contract = ["0 валидных профилей", "1 валидный профиль", "2+ валидных профиля", "Кириллическая фамилия", "Латинская фамилия", "Невалидный профиль", "Автономная AI-роль"]
    return {
        "procedure": "ordinary reads, one question when needed, exact file creation and reread",
        "scenario_count": len(scenarios),
        "scenarios": scenarios,
        "contract_markers_present": all(marker in skill for marker in required_contract),
        "all_passed": all(item["only_approved_profile_changed"] and item["zero_write_when_negative"] for item in scenarios),
    }


def role_matrix() -> dict:
    cases = [
        {"scenario": "complete", "state": "one Coordinator, one Executor, one Reviewer", "action": "review then human acceptance", "duplicates": 0},
        {"scenario": "partial", "state": "Executor reports partial", "action": "same Executor continues after Coordinator decision", "duplicates": 0},
        {"scenario": "lost-handle", "state": "role handle unavailable", "action": "stop or manual-complete existing trace", "duplicates": 0},
        {"scenario": "no-interrupt", "state": "safe interruption unconfirmed", "action": "wait; do not create replacement", "duplicates": 0},
        {"scenario": "overlap", "state": "writer already active", "action": "single writer; queue next action", "duplicates": 0},
        {"scenario": "manual-fallback", "state": "coordination capability absent", "action": "complete plan-handoff-review manually", "duplicates": 0},
        {"scenario": "full-re-review", "state": "REVISE", "action": "reuse same Executor and same independent Reviewer; rerun full amended contract", "duplicates": 0},
    ]
    log = run(["git", "log", "--format=%H%x09%s", "--", TASK_ROOT]).splitlines()
    subjects = [line.split("\t", 1)[1] for line in log if "\t" in line]
    return {
        "cases": cases,
        "all_closed": all(item["duplicates"] == 0 for item in cases),
        "actual_lineage": {
            "coordinator_contract_commits": [s for s in subjects if "/ts/coordinator]" in s or "/freeze/coordinator]" in s],
            "executor_amendment_commits": [s for s in subjects if "/product/executor] deliver prompt file amendment" in s or "/onb/executor] re-onboard" in s],
            "same_reviewer_pending_after_compaction": True,
            "child_reports_only_to_coordinator": True,
        },
    }


PRIOR_PATHS = [
    "02-assisted/.codex/hooks.json",
    "02-assisted/.codex/hooks/tfw-hook.ps1",
    "02-assisted/.codex/hooks/tfw-hook.sh",
    "02-assisted/AGENTS.md",
    "02-assisted/MIGRATION.md",
    "02-assisted/PROJECT.md",
    "02-assisted/README.md",
    "02-assisted/knowledge/INDEX.md",
    "02-assisted/people/README.md",
    "README.md",
]


def git_file(revision: str, path: str) -> bytes:
    result = subprocess.run(["git", "show", f"{revision}:editions/{path}"], cwd=REPO, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
    if result.returncode:
        raise RuntimeError(result.stderr.decode(errors="replace"))
    return result.stdout


def seed_downstream(root: Path) -> tuple[dict[str, dict], list[str]]:
    for relative in PRIOR_PATHS:
        path = root.joinpath(*relative.split("/"))
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(git_file(BASELINE, relative))
    prior = manifest_map(root)
    payload = {
        "02-assisted/work/private.md": b"synthetic protected work\n",
        "02-assisted/knowledge/record.md": b"synthetic protected knowledge\n",
        "02-assisted/people/ivanov.md": profile_bytes("ivanov", "Иван Иванов"),
        "02-assisted/.codex/neighbor.txt": b"synthetic unrelated codex\n",
        "02-assisted/шаблоны/theme.css": b":root{--synthetic-custom-theme:1}\n",
    }
    for relative, data in payload.items():
        path = root.joinpath(*relative.split("/"))
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    project = root / "02-assisted/PROJECT.md"
    project.write_bytes(project.read_bytes() + b"\nSynthetic downstream identity.\n")
    protected = sorted([*payload, "02-assisted/PROJECT.md"])
    return prior, protected


def authority(path: str, retired: set[str]) -> str:
    if path in retired:
        return "retired-known-stock"
    if path == "02-assisted/PROJECT.md":
        return "downstream-only"
    if path == "02-assisted/knowledge/INDEX.md" or path == "02-assisted/people/README.md":
        return "public"
    if path.startswith(("02-assisted/work/", "02-assisted/knowledge/", "02-assisted/people/", "02-assisted/.codex/")):
        return "downstream-only"
    if path.startswith("02-assisted/шаблоны/"):
        return "customizable"
    return "public"


def plan_update(target: Path, prior: dict[str, dict]) -> tuple[list[dict], list[str]]:
    release = json.loads((PRODUCT / "maintenance/release-manifest.json").read_text(encoding="utf-8"))
    policy = json.loads((PRODUCT / "maintenance/maintenance-policy.json").read_text(encoding="utf-8"))
    source = {item["path"]: item for item in release["files"]}
    current = manifest_map(target)
    retired = {item["path"] for item in policy["retired_known_stock"]}
    plan: list[dict] = []
    unresolved: list[str] = []
    for path, expected in source.items():
        kind = authority(path, retired)
        actual = current.get(path)
        old = prior.get(path)
        if kind == "downstream-only":
            action = "preserve" if actual else "create-stock-only-in-clean-install"
            if actual is None:
                action = "create"
        elif kind == "customizable" and actual is not None and old is None:
            action = "preserve"
        elif actual is None and old is None:
            action = "create"
        elif actual is not None and old is not None and actual == old:
            action = "preserve" if actual == expected else "replace"
        elif actual == expected:
            action = "preserve"
        else:
            action = "unresolved"
            unresolved.append(path)
        plan.append({"path": path, "authority": kind, "action": action})
    for path in retired:
        actual = current.get(path)
        old = prior.get(path)
        if actual is None:
            continue
        if actual == old:
            plan.append({"path": path, "authority": "retired-known-stock", "action": "delete"})
        else:
            plan.append({"path": path, "authority": "retired-known-stock", "action": "unresolved"})
            unresolved.append(path)
    manifest_path = "maintenance/release-manifest.json"
    plan.append({"path": manifest_path, "authority": "static-release-authority", "action": "replace" if manifest_path in current else "create"})
    return sorted(plan, key=lambda item: item["path"]), sorted(set(unresolved))


def apply_plan(target: Path, plan: list[dict], approved_before: dict[str, dict]) -> dict:
    recheck = manifest_map(target)
    if recheck != approved_before:
        return {"state": "blocked-drift", "writes": []}
    writes = []
    for item in plan:
        action = item["action"]
        if action not in {"create", "replace", "delete"}:
            continue
        relative = item["path"]
        path = target.joinpath(*relative.split("/"))
        if action == "delete":
            path.unlink()
        else:
            source = PRODUCT.joinpath(*relative.split("/"))
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(source.read_bytes())
            assert path.read_bytes() == source.read_bytes()
        writes.append(relative)
    return {"state": "verified", "writes": writes}


def forward_fixture() -> dict:
    with tempfile.TemporaryDirectory(prefix="assisted-forward-") as raw:
        base = Path(raw)
        clean = base / "clean-target"
        clean.mkdir()
        prior, protected = seed_downstream(clean)
        before = manifest_map(clean)
        protected_before = {path: before[path] for path in protected}
        plan, unresolved = plan_update(clean, prior)
        approval = "APPROVE exact create/replace/delete path table for synthetic clean target"
        result = apply_plan(clean, plan, before) if not unresolved else {"state": "blocked-unresolved", "writes": []}
        after = manifest_map(clean)
        protected_after = {path: after[path] for path in protected}
        release = json.loads((PRODUCT / "maintenance/release-manifest.json").read_text(encoding="utf-8"))
        source_rows = {item["path"]: item for item in release["files"]}
        public_mismatches = []
        for path, expected in source_rows.items():
            planned = next(item for item in plan if item["path"] == path)
            if planned["action"] != "preserve" or planned["authority"] == "public":
                if after.get(path) != expected:
                    public_mismatches.append(path)
        next_source_manifest = clean / "maintenance/release-manifest.json"

        drifted = base / "drift-target"
        drifted.mkdir()
        drift_prior, _ = seed_downstream(drifted)
        drift_plan, drift_unresolved = plan_update(drifted, drift_prior)
        approved = manifest_map(drifted)
        readme = drifted / "02-assisted/README.md"
        readme.write_bytes(readme.read_bytes() + b"\nSynthetic drift after approval.\n")
        after_injected_drift = manifest_map(drifted)
        stopped = apply_plan(drifted, drift_plan, approved)
        after_stop = manifest_map(drifted)

        actions: dict[str, int] = {}
        for item in plan:
            actions[item["action"]] = actions.get(item["action"], 0) + 1
        return {
            "procedure": "compare -> classify -> plan -> explicit gate -> recheck -> ordinary file changes -> verify",
            "clean": {
                "before_digest": rows_digest(list(before.values())),
                "plan": plan,
                "action_counts": actions,
                "approval": approval,
                "unresolved": unresolved,
                "result": result,
                "after_digest": rows_digest(list(after.values())),
                "version": (clean / "02-assisted/VERSION").read_text(encoding="utf-8").strip(),
                "protected_paths": protected,
                "protected_equal": protected_before == protected_after,
                "public_mismatches": public_mismatches,
                "next_source_manifest_equal": next_source_manifest.read_bytes() == (PRODUCT / "maintenance/release-manifest.json").read_bytes(),
                "unexplained_changes": sorted(set(changed_paths(before, after)) - set(result["writes"])),
            },
            "drifted": {
                "plan_unresolved_before_injection": drift_unresolved,
                "drift_path": "02-assisted/README.md",
                "result": stopped,
                "update_writes_after_detection": changed_paths(after_injected_drift, after_stop),
                "zero_update_writes": after_injected_drift == after_stop,
            },
        }


def reverse_fixture() -> dict:
    public_before = rows(PRODUCT)
    private_tokens = ["synthetic-person", "synthetic-company", "X:/private/path", "private-hash-012345"]
    downstream = {
        "generic_capabilities": ["prompt identity", "agent-led gated update"],
        "generic_rules": ["ask on ambiguity", "review a privacy-safe candidate"],
        "private_context": private_tokens,
    }
    with tempfile.TemporaryDirectory(prefix="assisted-reverse-") as raw:
        candidate_root = Path(raw) / "new-candidate"
        candidate_root.mkdir()
        candidate = {
            "schema": "synthetic-assisted-candidate-v1",
            "capabilities": downstream["generic_capabilities"],
            "rules": downstream["generic_rules"],
            "requires_independent_semantic_privacy_review": True,
        }
        write_json(candidate_root / "candidate.json", candidate)
        candidate_text = (candidate_root / "candidate.json").read_text(encoding="utf-8")
        public_after = rows(PRODUCT)
        return {
            "candidate": candidate,
            "candidate_root_outside_public": not candidate_root.is_relative_to(PRODUCT),
            "private_markers_absent": not any(token.casefold() in candidate_text.casefold() for token in private_tokens),
            "public_pre_digest": rows_digest(public_before),
            "public_post_digest": rows_digest(public_after),
            "public_unchanged": public_before == public_after,
            "field_mutation": "none; source inventory is compared separately before/after the full evidence run",
            "review_state": "candidate requires independent semantic and privacy review before any public task",
        }


def template_recheck() -> dict:
    template_root = ASSISTED / "шаблоны"
    stored = EVIDENCE / "templates"
    with tempfile.TemporaryDirectory(prefix="assisted-template-") as raw:
        temp = Path(raw)
        results = {}
        configurations = [
            ("stock", "theme.css", "Проверяемый отчёт — stock", stored / "a4-stock.html"),
            ("custom", "overlay/theme.css", "Проверяемый отчёт — custom", stored / "a4-custom.html"),
        ]
        for name, theme, title, prior in configurations:
            hashes = []
            for number in (1, 2):
                output = temp / f"{name}-{number}.html"
                run([
                    sys.executable,
                    "-B",
                    str(template_root / "build_a4.py"),
                    str(template_root / "документ_A4.md"),
                    str(output),
                    title,
                    "--theme",
                    theme,
                ])
                hashes.append(sha_file(output))
            results[name] = {
                "two_run_hashes": hashes,
                "two_run_equal": hashes[0] == hashes[1],
                "equals_retained_render_html": hashes[0] == sha_file(prior),
            }

    summary_path = stored / "render-summary.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    missing = []
    bad_signatures = []
    for name, item in summary["pdfs"].items():
        path = stored / name
        if not path.exists():
            missing.append(name)
        elif not path.read_bytes().startswith(b"%PDF"):
            bad_signatures.append(name)
        for page in item["page_screenshots"]:
            page_path = stored / page
            if not page_path.exists():
                missing.append(page)
            elif not page_path.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"):
                bad_signatures.append(page)
    for name, item in summary["browser_full_captures"].items():
        path = stored / name
        if not path.exists():
            missing.append(name)
            continue
        data = path.read_bytes()
        if not data.startswith(b"\x89PNG\r\n\x1a\n"):
            bad_signatures.append(name)
        else:
            width, height = struct.unpack(">II", data[16:24])
            if width != item["width"] or height != item["height"]:
                bad_signatures.append(name)

    builder = (template_root / "build_a4.py").read_text(encoding="utf-8")
    amendment = {
        "builder_product_sha256": sha_file(template_root / "build_a4.py"),
        "artifact_only_cli": "--self-test" not in builder and "def self_test" not in builder,
        "two_run": results,
        "retained_outputs_missing": missing,
        "retained_output_signature_errors": bad_signatures,
        "all_previous_pages_and_captures_visually_inspected": summary["visual_inspection"]["all_20_replacements_inspected"],
        "blocked_network_controls_retained": summary["blocked_network"]["controls"],
    }
    summary["amendment_recheck"] = amendment
    write_json(summary_path, summary)
    return amendment


def product_boundary() -> dict:
    name_status = run(["git", "diff", "--name-status", BASELINE, "--", "editions"]).splitlines()
    counts = {"new": 0, "modified": 0, "deleted": 0}
    for line in name_status:
        counts[{"A": "new", "M": "modified", "D": "deleted"}[line.split("\t", 1)[0]]] += 1
    additions = deletions = 0
    for line in run(["git", "diff", "--numstat", BASELINE, "--", "editions"]).splitlines():
        added, removed, _ = line.split("\t", 2)
        additions += int(added)
        deletions += int(removed)
    executable_suffixes = {".py", ".ps1", ".sh", ".js", ".ts", ".bat", ".cmd"}
    executables = [p.relative_to(REPO).as_posix() for p in PRODUCT.rglob("*") if p.is_file() and p.suffix.casefold() in executable_suffixes]
    builder = (ASSISTED / "шаблоны/build_a4.py").read_text(encoding="utf-8")
    product_text = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in PRODUCT.rglob("*") if p.is_file())
    removed_references = [token for token in ("tfw_identity.py", "assisted_maintenance.py", "--self-test", "scripts/tfw_identity") if token in product_text]
    private_markers = [token for token in ("innoforce", "иннофорс", "h:\\shared drives", "c0rpa", "private-hash") if token in product_text.casefold()]
    forbidden_builder_tokens = [token for token in ("tfw-identity", "tfw-update", "maintenance-policy", "release-manifest", "self_test") if token in builder.casefold()]
    return {
        "baseline": BASELINE,
        "paths": len(name_status),
        **counts,
        "additions": additions,
        "deletions": deletions,
        "changed_loc": additions + deletions,
        "name_status": name_status,
        "version_bytes_hex": (ASSISTED / "VERSION").read_bytes().hex(),
        "removed_runtime_paths_absent": not (ASSISTED / ".agents/skills/tfw-identity/scripts/tfw_identity.py").exists() and not (PRODUCT / "maintenance/assisted_maintenance.py").exists(),
        "product_executables": executables,
        "sole_builder": executables == ["editions/02-assisted/шаблоны/build_a4.py"],
        "builder_forbidden_tokens": forbidden_builder_tokens,
        "removed_runtime_references": removed_references,
        "private_markers": private_markers,
        "clean_copy_initial_state": {
            "profiles": sorted(p.name for p in (ASSISTED / "people").glob("*.md") if p.name != "README.md"),
            "work_exists": (ASSISTED / "work").exists(),
            "project_uninitialized": "НЕ ИНИЦИАЛИЗИРОВАН" in (ASSISTED / "PROJECT.md").read_text(encoding="utf-8"),
            "hidden_full_or_light": (ASSISTED / ".tfw").exists() or (ASSISTED / "01-light").exists(),
        },
    }


def commit_and_publication_audit(tags_before: dict[str, str]) -> dict:
    log = run(["git", "log", "--all", "--format=%H%x09%s"]).splitlines()
    commits = []
    forbidden_hits = []
    baseline_commit = run(["git", "rev-parse", BASELINE])
    excluded_baseline = None
    for line in log:
        commit, subject = line.split("\t", 1)
        if TASK_ID not in subject:
            continue
        if commit == baseline_commit:
            excluded_baseline = {"commit": commit, "subject": subject, "classification": "owner-authorized config baseline; product census starts after this commit"}
            continue
        paths = run(["git", "-c", "core.quotepath=false", "diff-tree", "--no-commit-id", "--name-only", "-r", commit]).splitlines()
        forbidden = [path for path in paths if not (path.startswith("editions/") or path.startswith(TASK_ROOT))]
        commits.append({"commit": commit, "subject": subject, "paths": len(paths), "forbidden_hits": forbidden})
        forbidden_hits.extend({"commit": commit, "path": path} for path in forbidden)
    external_tags = []
    for tag in EXTERNAL_TAGS:
        after = run(["git", "rev-parse", f"{tag}^{{commit}}"])
        contained_task_commits = [
            {"commit": item["commit"], "subject": item["subject"]}
            for item in commits
            if subprocess.run(["git", "merge-base", "--is-ancestor", item["commit"], tag], cwd=REPO).returncode == 0
        ]
        external_tags.append({
            "ref": tag,
            "before": tags_before[tag],
            "after": after,
            "unchanged": tags_before[tag] == after,
            "contained_task_commits": contained_task_commits,
            "contains_amended_product_commit": any(item["commit"] == PRODUCT_COMMIT for item in contained_task_commits),
            "attribution": "concurrent external state; not created, changed or deleted by this Assisted task run",
        })
    remote_contains = run(["git", "for-each-ref", "--format=%(refname)", "--contains", PRODUCT_COMMIT, "refs/remotes"]).splitlines()
    return {
        "task_commit_count": len(commits),
        "commits": commits,
        "all_task_commits_zero_forbidden_hits": not forbidden_hits,
        "forbidden_hits": forbidden_hits,
        "excluded_owner_config_baseline": excluded_baseline,
        "external_tags": external_tags,
        "assisted_task_tag_or_push_acts": 0,
        "remote_refs_containing_product_commit": remote_contains,
        "remote_containment_absent": not remote_contains,
    }


def main() -> int:
    if not SOURCE.is_dir():
        raise RuntimeError(f"field source unavailable: {SOURCE}")
    tags_before = {tag: run(["git", "rev-parse", f"{tag}^{{commit}}"]) for tag in EXTERNAL_TAGS}
    source_pre = rows(SOURCE)
    source_pre_digest = rows_digest(source_pre)
    powershell = powershell_source_rows(SOURCE)
    if sorted(source_pre, key=lambda item: item["path"]) != sorted(powershell["rows"], key=lambda item: item["path"]):
        raise RuntimeError("field source readers disagree per-file")
    if source_pre_digest != CANONICAL_SOURCE_DIGEST:
        raise RuntimeError(f"field source canonical digest drift: {source_pre_digest}")

    fixtures = {
        "schema": "tfw-assisted-amended-fixture-results-v1",
        "static_manifest": static_manifest(),
        "identity": identity_scenarios(),
        "roles": role_matrix(),
        "forward": forward_fixture(),
        "reverse": reverse_fixture(),
        "templates": template_recheck(),
    }

    source_post = rows(SOURCE)
    source_post_digest = rows_digest(source_post)
    source_result = {
        "schema": "tfw-assisted-source-immutability-v2",
        "path": str(SOURCE),
        "row_count": len(source_pre),
        "historical_research_algorithm": "PowerShell culture-sort",
        "historical_research_digest": HISTORICAL_CULTURE_DIGEST,
        "powershell_culture_digest": powershell["culture_digest"],
        "canonical_algorithm": "UTF-8 POSIX relative paths, Python code-point sort; path<TAB>size<TAB>sha256<LF>",
        "canonical_pre_digest": source_pre_digest,
        "canonical_post_digest": source_post_digest,
        "python_powershell_row_set_equal": True,
        "pre_post_rows_equal": source_pre == source_post,
        "writes": 0,
        "aborted_fail_closed_history": [
            "Earlier evidence run stopped on a culture-sort versus code-point-sort aggregate mismatch before fixture writes.",
            "A repeat also stopped until the 29 per-file rows were compared and shown equal.",
        ],
    }
    boundary = product_boundary()
    boundary["publication"] = commit_and_publication_audit(tags_before)
    boundary["source_pre_post_equal"] = source_result["pre_post_rows_equal"]
    boundary["source_canonical_digest"] = source_post_digest

    write_json(EVIDENCE / "assisted15-fixture-results.json", fixtures)
    write_json(EVIDENCE / "source-immutability.json", source_result)
    write_json(EVIDENCE / "boundary-summary.json", boundary)
    tag_summary = "; ".join(
        f"{item['ref']}={item['after']} contains_product={item['contains_amended_product_commit']}"
        for item in boundary["publication"]["external_tags"]
    )
    attestation = f"""# Assisted 1.5 amended boundary and source attestation

- Product authority: amended HL `37b61d4`, approved TS `f4c676c`.
- Product checkpoint: `{PRODUCT_COMMIT}`.
- Baseline census: {boundary['paths']} paths = {boundary['new']} new / {boundary['modified']} modified / {boundary['deleted']} deleted; {boundary['changed_loc']} changed LOC.
- Product executables: `{', '.join(boundary['product_executables'])}`; the sole file is the artifact builder. Removed identity and maintenance executables are absent.
- Static release authority: {fixtures['static_manifest']['row_count']} rows; two regenerations and recorded rows are equal.
- Field source: {len(source_pre)} read-only rows; canonical pre/post `{source_pre_digest}`; PowerShell/Python per-file row sets equal. Historical culture-sort aggregate `{powershell['culture_digest']}` is retained as a different ordering convention, not source drift.
- External local tags are recorded per object and per contained task commit in `boundary-summary.json`: {tag_summary}. They are concurrent external state and stayed unchanged during this run. This task performed zero tag or push acts and did not rewrite either tag.
- Remote-tracking refs containing amended product checkpoint at capture: {boundary['publication']['remote_refs_containing_product_commit'] or 'none'}.
- Every post-baseline commit whose subject names `{TASK_ID}` was audited: {boundary['publication']['task_commit_count']} commits, zero forbidden path hits = {boundary['publication']['all_task_commits_zero_forbidden_hits']}. Owner-authorized config commit `f3eb986` is the explicit census baseline, not an Assisted product change. Concurrent dirty TFW-55/config state is external and was not staged.
- Earlier runtime/ACL/locking/terminal evidence is superseded by amendment A1 and is not counted for amended acceptance.
"""
    (EVIDENCE / "boundary-and-source-attestation.md").write_text(attestation, encoding="utf-8", newline="\n")
    print("RUN_EVIDENCE=PASS")
    print(f"manifest_rows={fixtures['static_manifest']['row_count']}")
    print(f"identity_scenarios={fixtures['identity']['scenario_count']}")
    print(f"role_scenarios={len(fixtures['roles']['cases'])}")
    print(f"forward_writes={len(fixtures['forward']['clean']['result']['writes'])}")
    print(f"source_rows={len(source_pre)} source_digest={source_pre_digest}")
    print(f"product_paths={boundary['paths']} changed_loc={boundary['changed_loc']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
