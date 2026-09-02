"""Verify the frozen Assisted 1.6 path, hunk, preservation, and source gates."""

from __future__ import annotations

import hashlib
import os
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote


REPO = Path(__file__).resolve().parents[5]
SOURCE = Path(os.environ["TFW_FA15ES_SOURCE"])
TARGET = REPO / "editions" / "02-assisted"
PRODUCT_BASE = "e5e20f5b1070f48740d7d47bdd264ccc66ee524d"


RANGES = {
    ".agents/skills/tfw-plan/SKILL.md": [(21, 1), (29, 1)],
    ".agents/skills/tfw-handoff/SKILL.md": [(12, 1), (30, 2)],
    ".agents/skills/tfw-review/SKILL.md": [(12, 1), (31, 2)],
    ".agents/skills/tfw-update/SKILL.md": [(3, 1), (18, 1), (43, 1), (45, 1), (53, 1), (57, 1), (64, 1), (67, 2), (73, 2), (81, 3)],
    ".agents/skills/tfw-identity/SKILL.md": [(23, 1), (46, 2), (59, 1), (63, 1), (67, 3), (85, 1)],
    "AGENTS.md": [(20, 1), (41, 1), (49, 1), (62, 1), (81, 1), (86, 1), (118, 2), (121, 1), (129, 1), (145, 1), (148, 2), (159, 1), (164, 1)],
    "CHANGELOG.md": [(3, 1), (9, 1), (16, 1), (27, 2), (32, 1), (36, 1), (46, 2), (49, 1), (62, 2), (67, 4), (77, 1), (81, 3), (111, 1), (116, 1), (119, 3), (126, 1), (128, 1), (131, 2), (153, 1), (174, 1), (182, 5), (196, 1), (222, 1), (224, 1), (228, 1), (234, 1), (236, 1), (242, 1)],
    "knowledge/INDEX.md": [(5, 1), (9, 10)],
    "MIGRATION.md": [(7, 1), (13, 1), (18, 1), (20, 3), (30, 1), (34, 1), (40, 1), (46, 1), (51, 2), (54, 1), (63, 2), (77, 1), (79, 1), (85, 1), (87, 1), (89, 1), (118, 2), (135, 2), (138, 1), (151, 1)],
    "people/README.md": [(3, 1), (7, 1), (25, 1), (39, 1)],
    "PROJECT.md": [(12, 1), (18, 1), (20, 1), (28, 8), (45, 1), (49, 1), (56, 1), (58, 1), (64, 7)],
    "README.md": [(5, 1), (16, 3), (31, 1), (37, 1), (45, 1), (56, 1), (83, 1), (93, 1), (96, 1), (102, 1)],
    "шаблоны/build_a4.py": [(2, 1), (12, 2), (30, 1), (135, 1)],
    "шаблоны/документ_A4.md": [(2, 1), (94, 1)],
    "шаблоны/заметка.md": [(1, 1), (25, 1), (43, 1)],
    "шаблоны/план_работы.md": [(3, 1), (78, 1)],
    "шаблоны/презентация.html": [(6, 1), (9, 1), (12, 1), (30, 1), (35, 10), (114, 1), (153, 1), (226, 1), (264, 2), (279, 2), (289, 1), (294, 1), (296, 1), (302, 1), (337, 1), (362, 1), (380, 2)],
}


TARGET_MAP = {name: name for name in RANGES}
TARGET_MAP["people/README.md"] = "team/README.md"

EXACT = {
    ".agents/skills/tfw-handoff/agents/openai.yaml",
    ".agents/skills/tfw-identity/agents/openai.yaml",
    ".agents/skills/tfw-plan/agents/openai.yaml",
    ".agents/skills/tfw-review/agents/openai.yaml",
    ".agents/skills/tfw-update/agents/openai.yaml",
    "VERSION",
}

FINAL_PATHS = set(TARGET_MAP.values()) | EXACT | {"шаблоны/assets/tfw-mark.svg"}
DELETE_PATHS = {
    "editions/02-assisted/people/README.md",
    "editions/02-assisted/шаблоны/overlay/theme.css",
    "editions/02-assisted/шаблоны/theme.css",
    "editions/maintenance/maintenance-policy.json",
    "editions/maintenance/release-manifest.json",
}
CHANGED_PATHS = (
    {f"editions/02-assisted/{path}" for path in FINAL_PATHS if path != "шаблоны/assets/tfw-mark.svg"}
    | DELETE_PATHS
    | {"editions/README.md", "editions/ASSISTED_MAINTENANCE.md"}
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def run_git(*args: str, allow_diff: bool = False) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(
        ["git", *args],
        cwd=REPO,
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    allowed = {0, 1} if allow_diff else {0}
    if proc.returncode not in allowed:
        raise RuntimeError(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc


def source_manifest_digest() -> tuple[int, int, str]:
    rows = []
    total = 0
    for path in sorted((p for p in SOURCE.rglob("*") if p.is_file()), key=lambda p: p.relative_to(SOURCE).as_posix()):
        data = path.read_bytes()
        relative = path.relative_to(SOURCE).as_posix()
        rows.append(f"{relative}|{len(data)}|{sha256(data)}")
        total += len(data)
    payload = ("\n".join(rows) + "\n").encode("utf-8")
    return len(rows), total, sha256(payload)


def actual_product_paths() -> set[str]:
    proc = run_git("-c", "core.quotepath=false", "status", "--porcelain=v1", "--untracked-files=all", "--", "editions")
    paths = {line[3:].replace("\\", "/") for line in proc.stdout.splitlines() if line}
    if paths:
        return paths
    committed = run_git(
        "-c",
        "core.quotepath=false",
        "diff",
        "--name-only",
        PRODUCT_BASE,
        "HEAD",
        "--",
        "editions",
    )
    return {line.replace("\\", "/") for line in committed.stdout.splitlines() if line}


def source_hunks(source_relative: str, target_relative: str) -> list[tuple[int, int]]:
    proc = run_git(
        "diff",
        "--no-index",
        "--text",
        "--unified=0",
        "--inter-hunk-context=0",
        "--minimal",
        "--no-indent-heuristic",
        "--",
        str(SOURCE / Path(source_relative)),
        str(TARGET / Path(target_relative)),
        allow_diff=True,
    )
    headers = []
    for line in proc.stdout.splitlines():
        match = re.match(r"^@@ -(\d+)(?:,(\d+))? \+\d+(?:,\d+)? @@", line)
        if match:
            headers.append((int(match.group(1)), int(match.group(2) or "1")))
    return headers


def count_product_loc() -> tuple[int, int]:
    proc = run_git("diff", "--numstat", PRODUCT_BASE, "--", "editions")
    added = deleted = 0
    for line in proc.stdout.splitlines():
        left, right, _ = line.split("\t", 2)
        if left == "-" or right == "-":
            raise RuntimeError("unexpected binary product diff")
        added += int(left)
        deleted += int(right)
    team_path = TARGET / "team" / "README.md"
    if "editions/02-assisted/team/README.md" not in proc.stdout:
        added += len(team_path.read_bytes().splitlines())
    return added, deleted


def check_relative_links() -> int:
    checked = 0
    broken: list[str] = []
    markdown_files = list(TARGET.rglob("*.md")) + [
        REPO / "editions" / "README.md",
        REPO / "editions" / "ASSISTED_MAINTENANCE.md",
    ]
    for document in markdown_files:
        text = document.read_text(encoding="utf-8")
        for raw in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
            target = raw.strip().strip("<>").split("#", 1)[0]
            if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or "<" in target:
                continue
            checked += 1
            resolved = (document.parent / unquote(target)).resolve(strict=False)
            if not resolved.exists():
                broken.append(f"{document.relative_to(REPO).as_posix()} -> {target}")
    presentation = TARGET / "шаблоны" / "презентация.html"
    html = presentation.read_text(encoding="utf-8")
    for raw in re.findall(r'(?:src|href)="([^"]+)"', html):
        if re.match(r"^[a-z][a-z0-9+.-]*:", raw, re.I) or raw.startswith("#"):
            continue
        checked += 1
        if not (presentation.parent / unquote(raw)).resolve(strict=False).exists():
            broken.append(f"{presentation.relative_to(REPO).as_posix()} -> {raw}")
    if broken:
        raise RuntimeError(f"broken relative links: {broken}")
    return checked


def main() -> None:
    if run_git("branch", "--show-current").stdout.strip() != "codex/tfw-fa15es-executor":
        raise RuntimeError("wrong branch")
    if actual_product_paths() != CHANGED_PATHS:
        extra = sorted(actual_product_paths() - CHANGED_PATHS)
        missing = sorted(CHANGED_PATHS - actual_product_paths())
        raise RuntimeError(f"product path ledger mismatch; extra={extra}; missing={missing}")

    final_paths = {p.relative_to(TARGET).as_posix() for p in TARGET.rglob("*") if p.is_file()}
    if final_paths != FINAL_PATHS:
        raise RuntimeError(f"final package path mismatch: extra={sorted(final_paths-FINAL_PATHS)} missing={sorted(FINAL_PATHS-final_paths)}")

    hunk_total = source_line_total = unchanged_total = 0
    for source_relative, expected in RANGES.items():
        target_relative = TARGET_MAP[source_relative]
        actual = source_hunks(source_relative, target_relative)
        if actual != expected:
            raise RuntimeError(f"hunk mismatch for {source_relative}: expected={expected}; actual={actual}")
        source_lines = (SOURCE / Path(source_relative)).read_bytes().splitlines(keepends=True)
        target_lines = (TARGET / Path(target_relative)).read_bytes().splitlines(keepends=True)
        if len(source_lines) != len(target_lines):
            raise RuntimeError(f"line count drift for {source_relative}")
        changed = {number for start, count in expected for number in range(start, start + count)}
        for number, (left, right) in enumerate(zip(source_lines, target_lines), 1):
            if number not in changed and left != right:
                raise RuntimeError(f"unlisted changed line {source_relative}:{number}")
        hunk_total += len(actual)
        source_line_total += sum(count for _, count in actual)
        unchanged_total += len(source_lines) - len(changed)

    if (hunk_total, source_line_total, unchanged_total) != (136, 205, 1900):
        raise RuntimeError(f"aggregate hunk mismatch: {(hunk_total, source_line_total, unchanged_total)}")

    for relative in EXACT:
        if (SOURCE / Path(relative)).read_bytes() != (TARGET / Path(relative)).read_bytes():
            raise RuntimeError(f"exact-copy mismatch: {relative}")

    mark = TARGET / "шаблоны" / "assets" / "tfw-mark.svg"
    if sha256(mark.read_bytes()) != "1ed6d908154678edddf9c1b3ca4c58b9bf813b46b3864d1db0d1be34c9893e11":
        raise RuntimeError("retained mark mismatch")
    if any(path.suffix.lower() in {".exe", ".sh", ".ps1", ".js", ".ts"} for path in TARGET.rglob("*") if path.is_file()):
        raise RuntimeError("unexpected executable product file")
    py_files = [p for p in TARGET.rglob("*.py") if p.is_file()]
    if [p.relative_to(TARGET).as_posix() for p in py_files] != ["шаблоны/build_a4.py"]:
        raise RuntimeError("artifact builder is not the only Python product file")
    if any(path.suffix.lower() == ".png" for path in TARGET.rglob("*") if path.is_file()):
        raise RuntimeError("excluded raster asset found")

    added, deleted = count_product_loc()
    if added + deleted > 5000:
        raise RuntimeError(f"changed LOC budget exceeded: {added + deleted}")
    source_count, source_bytes, manifest_digest = source_manifest_digest()
    if (source_count, source_bytes) != (28, 297522):
        raise RuntimeError("source aggregate drift")
    checked_links = check_relative_links()

    print("PRODUCT_PATHS=30")
    print(f"FINAL_PACKAGE={len(final_paths)} files / {sum(p.stat().st_size for p in TARGET.rglob('*') if p.is_file())} bytes")
    print("SOURCE_DIFF=17 files / 136 hunks / 205 changed source lines / 1900 unchanged lines")
    print("EXACT_SOURCE_FILES=6")
    print("RETAINED_MARK=PASS")
    print(f"PRODUCT_LOC=+{added}/-{deleted}/total={added+deleted}")
    print(f"SOURCE_MANIFEST={source_count} files / {source_bytes} bytes / aggregate-sha256={manifest_digest}")
    print(f"RELATIVE_LINKS={checked_links} checked / 0 broken")
    print("VERDICT=PASS")


if __name__ == "__main__":
    main()
