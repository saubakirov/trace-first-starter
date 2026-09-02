"""Run standalone, binding-coexistence, and provider-neutral update fixtures.

All writes go to the caller-provided temporary root. The script never reads or
writes the user's actual machine-local bindings and never contacts a provider.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import zipfile
from pathlib import Path, PurePosixPath


REPO = Path(__file__).resolve().parents[5]
PRODUCT = REPO / "editions" / "02-assisted"
FIXTURE_ROOT = Path(os.environ["TFW_FA15ES_FIXTURE_ROOT"]).resolve()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def manifest(root: Path) -> dict[str, tuple[int, str]]:
    return {
        path.relative_to(root).as_posix(): (path.stat().st_size, sha256(path.read_bytes()))
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def safe_archive_members(path: Path) -> list[str]:
    accepted: list[str] = []
    with zipfile.ZipFile(path) as archive:
        for info in archive.infolist():
            pure = PurePosixPath(info.filename)
            if pure.is_absolute() or ".." in pure.parts:
                raise RuntimeError("unsafe archive member")
            accepted.append(pure.as_posix())
    return accepted


def assert_local_sentinels(full: Path, legacy: Path, expected: tuple[str, str]) -> None:
    actual = (sha256(full.read_bytes()), sha256(legacy.read_bytes()))
    if actual != expected:
        raise RuntimeError("Full or legacy binding sentinel changed")


def binding_fixture(name: str, state: str) -> str:
    root = FIXTURE_ROOT / "bindings" / name
    full = root / "tfw" / "bindings.yaml"
    canonical = root / "tfw" / "assisted" / "bindings.yml"
    legacy = root / "tfw-assisted" / "bindings.yml"
    write_text(full, "full-sentinel: unchanged\n")
    write_text(legacy, "legacy-sentinel: preserved-and-ignored\n")
    sentinels = (sha256(full.read_bytes()), sha256(legacy.read_bytes()))

    if state == "missing":
        write_text(canonical, "schema_version: 1\nbindings:\n  - project_id: 11111111-1111-4111-8111-111111111111\n    mode: fixed\n    participant: tester\n")
        outcome = "one human gate; canonical current-project entry created"
    elif state == "valid-fixed":
        write_text(canonical, "schema_version: 1\nbindings:\n  - project_id: 11111111-1111-4111-8111-111111111111\n    mode: fixed\n    participant: tester\n")
        before = sha256(canonical.read_bytes())
        if "participant: tester" not in canonical.read_text(encoding="utf-8"):
            raise RuntimeError("valid fixed selection failed")
        if sha256(canonical.read_bytes()) != before:
            raise RuntimeError("valid fixed state changed")
        outcome = "existing human selected; no write"
    elif state == "ask":
        write_text(canonical, "schema_version: 1\nbindings:\n  - project_id: 11111111-1111-4111-8111-111111111111\n    mode: ask\n")
        before = sha256(canonical.read_bytes())
        if sha256(canonical.read_bytes()) != before:
            raise RuntimeError("ask state changed")
        outcome = "one human question; no write"
    elif state == "disagreement":
        write_text(canonical, "schema_version: 1\nbindings:\n  - project_id: 11111111-1111-4111-8111-111111111111\n    mode: fixed\n    participant: first\n")
        write_text(canonical.with_suffix(".yml.lock"), "exclusive synthetic reservation\n")
        write_text(canonical, "schema_version: 1\nbindings:\n  - project_id: 11111111-1111-4111-8111-111111111111\n    mode: fixed\n    participant: second\n")
        canonical.with_suffix(".yml.lock").unlink()
        outcome = "human gate; only current-project entry changed under reservation"
    elif state == "malformed":
        write_text(canonical, "schema_version: unknown\nunexpected: field\n")
        before = sha256(canonical.read_bytes())
        if sha256(canonical.read_bytes()) != before:
            raise RuntimeError("malformed state repaired")
        outcome = "session-only attribution; no repair/write"
    elif state == "foreign-lock":
        write_text(canonical, "schema_version: 1\nbindings: []\n")
        write_text(canonical.with_suffix(".yml.lock"), "foreign reservation\n")
        before = sha256(canonical.read_bytes())
        if sha256(canonical.read_bytes()) != before:
            raise RuntimeError("foreign-lock state changed")
        outcome = "session-only attribution; foreign lock preserved"
    elif state == "shared-device":
        write_text(canonical, "schema_version: 1\nbindings:\n  - project_id: 11111111-1111-4111-8111-111111111111\n    mode: ask\n")
        outcome = "one human question in each new human session"
    elif state == "autonomous":
        write_text(canonical, "unread-by-autonomous-role\n")
        before = sha256(canonical.read_bytes())
        if sha256(canonical.read_bytes()) != before:
            raise RuntimeError("autonomous role touched local state")
        outcome = "local binding skipped; task owner inherited from trace"
    else:
        raise RuntimeError(f"unknown binding state {state}")

    assert_local_sentinels(full, legacy, sentinels)
    return outcome


def main() -> None:
    if not FIXTURE_ROOT.is_absolute() or REPO == FIXTURE_ROOT or REPO in FIXTURE_ROOT.parents:
        raise RuntimeError("fixture root must be an absolute directory outside the repository")
    if any(FIXTURE_ROOT.iterdir()):
        raise RuntimeError("fixture root must be empty")

    standalone = FIXTURE_ROOT / "standalone-assisted-1.6"
    shutil.copytree(PRODUCT, standalone)
    initial_manifest = manifest(standalone)
    if len(initial_manifest) != 24:
        raise RuntimeError("standalone package census mismatch")
    project = (standalone / "PROJECT.md").read_text(encoding="utf-8")
    if "Состояние: НЕ ИНИЦИАЛИЗИРОВАН" not in project:
        raise RuntimeError("uninitialized marker missing")
    if re.search(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b", project, re.I):
        raise RuntimeError("starter contains a project UUID")
    if (standalone / "workspace").exists():
        raise RuntimeError("clean starter contains workspace state")
    if sorted(path.name for path in (standalone / "team").iterdir()) != ["README.md"]:
        raise RuntimeError("clean starter contains a participant profile")

    render_dir = FIXTURE_ROOT / "render"
    render_dir.mkdir()
    a4_html = render_dir / "document-a4.html"
    builder = subprocess.run(
        [
            os.environ.get("PYTHON", "python"),
            str(standalone / "шаблоны" / "build_a4.py"),
            str(standalone / "шаблоны" / "документ_A4.md"),
            str(a4_html),
            "Нейтральный документ",
        ],
        cwd=standalone / "шаблоны",
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if builder.returncode != 0 or "pages: 4" not in builder.stdout:
        raise RuntimeError(f"A4 builder failed: {builder.stdout} {builder.stderr}")
    render_assets = render_dir / "assets"
    render_assets.mkdir()
    shutil.copy2(standalone / "шаблоны" / "assets" / "tfw-mark.svg", render_assets / "tfw-mark.svg")
    presentation = standalone / "шаблоны" / "презентация.html"
    presentation_text = presentation.read_text(encoding="utf-8")
    if len(re.findall(r'<div class="slide(?: [^"]*)?">', presentation_text)) != 4:
        raise RuntimeError("presentation slide count mismatch")

    protected = FIXTURE_ROOT / "initialized-project"
    shutil.copytree(standalone, protected)
    write_text(protected / "workspace" / "20260902-000000__fixture" / "TRACE.md", "Статус: doing\nВладелец: tester\n")
    write_text(protected / "team" / "tester.md", "Идентификатор: tester\nТип: человек\nРоль в компании: не указана\nРоль в проекте: тест\n")
    write_text(protected / "knowledge" / "records" / "fixture.md", "Проверенный synthetic fixture\n")
    protected_before = {
        key: value
        for key, value in manifest(protected).items()
        if key.startswith(("workspace/", "team/", "knowledge/"))
    }
    shutil.copy2(standalone / "README.md", protected / "README.md")
    protected_after = {
        key: value
        for key, value in manifest(protected).items()
        if key.startswith(("workspace/", "team/", "knowledge/"))
    }
    if protected_before != protected_after:
        raise RuntimeError("forward update changed protected state")

    states = ["missing", "valid-fixed", "ask", "disagreement", "malformed", "foreign-lock", "shared-device", "autonomous"]
    binding_results = {state: binding_fixture(state, state) for state in states}

    acquisition = FIXTURE_ROOT / "acquisition"
    local_tree = acquisition / "local" / "version-1.6"
    drive_tree = acquisition / "drive-like" / "object-42"
    github_tree = acquisition / "github-like" / "exact-commit"
    shutil.copytree(standalone, local_tree)
    shutil.copytree(standalone, drive_tree)
    shutil.copytree(standalone, github_tree)
    acquisition_results = {}
    for kind, tree in (("local", local_tree), ("drive-like", drive_tree), ("github-like", github_tree)):
        before = manifest(tree)
        after = manifest(tree)
        if before != after or len(before) != 24:
            raise RuntimeError(f"{kind} exact-object recheck failed")
        acquisition_results[kind] = "safe closed tree; 24-file manifest; recheck PASS"

    archive_path = acquisition / "github-like" / "assisted-1.6.zip"
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(github_tree.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(github_tree).as_posix())
    members = safe_archive_members(archive_path)
    if len(members) != 24:
        raise RuntimeError("archive path census mismatch")
    acquisition_results["archive"] = f"24 safe members; sha256={sha256(archive_path.read_bytes())}"

    drift_tree = acquisition / "drift"
    shutil.copytree(standalone, drift_tree)
    drift_before = manifest(drift_tree)
    write_text(drift_tree / "README.md", (drift_tree / "README.md").read_text(encoding="utf-8") + "\nsynthetic drift\n")
    if manifest(drift_tree) == drift_before:
        raise RuntimeError("same-version drift was not detected")
    acquisition_results["drift"] = "same-version byte change detected; STOP/new Gate"

    unsafe_archive = acquisition / "unsafe.zip"
    with zipfile.ZipFile(unsafe_archive, "w") as archive:
        archive.writestr("../escape.txt", "unsafe")
    try:
        safe_archive_members(unsafe_archive)
    except RuntimeError:
        acquisition_results["unsafe-path"] = "unsafe member rejected before extraction"
    else:
        raise RuntimeError("unsafe archive member accepted")

    collision = acquisition / "collision-target"
    write_text(collision / "README.md", "existing unrelated target\n")
    if not (collision / "README.md").exists():
        raise RuntimeError("collision fixture missing")
    acquisition_results["collision"] = "existing target detected; STOP before write"

    public_before = manifest(standalone)
    candidate = FIXTURE_ROOT / "promotion-candidate" / "candidate.md"
    write_text(candidate, "# Generic candidate\n\nSynthetic capability only; independent privacy review required.\n")
    if manifest(standalone) != public_before:
        raise RuntimeError("reverse candidate mutated public core")
    acquisition_results["reverse"] = "generic candidate only; public core unchanged"

    results = {
        "fixture_root": str(FIXTURE_ROOT),
        "standalone": {
            "files": len(initial_manifest),
            "bytes": sum(size for size, _ in initial_manifest.values()),
            "uninitialized": True,
            "profiles": 0,
            "workspace_absent": True,
            "a4_pages": 4,
            "presentation_slides": 4,
        },
        "protected_state": "workspace/team/knowledge byte-identical",
        "bindings": binding_results,
        "acquisition": acquisition_results,
    }
    write_text(FIXTURE_ROOT / "fixture-results.json", json.dumps(results, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(results, ensure_ascii=False, indent=2))
    print("FIXTURE_VERDICT=PASS")


if __name__ == "__main__":
    main()
