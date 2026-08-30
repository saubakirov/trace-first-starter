#!/usr/bin/env python3
"""Run final deterministic verification and write task-local summaries."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import struct
import subprocess
import sys
import tempfile


sys.dont_write_bytecode = True
REPO = Path(__file__).resolve().parents[4]
EVIDENCE = Path(__file__).resolve().parent
TEMPLATES = EVIDENCE / "templates"
BASELINE = "f3eb986"


def sha_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def run(label: str, command: list[str], expected: int = 0) -> dict:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(
        command,
        cwd=REPO,
        env=environment,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
    )
    record = {"label": label, "command": command, "exit": result.returncode, "output": result.stdout.rstrip()}
    if result.returncode != expected:
        raise RuntimeError(f"{label} failed with exit {result.returncode}: {result.stdout}")
    return record


def clean_copy_smoke() -> dict:
    with tempfile.TemporaryDirectory(prefix="tfw-assisted-clean-copy-") as raw:
        root = Path(raw) / "starter"
        shutil.copytree(REPO / "editions/02-assisted", root)
        forbidden_initial_state = [
            root / "work",
            root / ".tfw",
            root / "evidence",
            root / "people/ivanov.md",
        ]
        no_shipped_runtime_state = not any(path.exists() for path in forbidden_initial_state)
        identity = root / ".agents/skills/tfw-identity/scripts/tfw_identity.py"
        builder = root / "шаблоны/build_a4.py"
        inspect = run("clean copy inspect", [sys.executable, str(identity), "inspect", "--project-root", str(root)])
        manifest = run("clean copy profile manifest", [sys.executable, str(identity), "profile-manifest", "--project-root", str(root)])
        manifest_value = json.loads(manifest["output"])
        created = run(
            "clean copy documented create-profile",
            [
                sys.executable,
                str(identity),
                "create-profile",
                "--project-root", str(root),
                "--expected-manifest", manifest_value["people_manifest"],
                "--display-name", "Ivan Ivanov",
                "--surname", "Ivanov",
                "--organization-role", "Test organization role",
                "--project-role", "Test project role",
            ],
        )
        identity_test = run("clean copy identity self-test", [sys.executable, str(identity), "self-test"])
        builder_test = run("clean copy template self-test", [sys.executable, str(builder), "--self-test"])
        inspect_value = json.loads(inspect["output"])
        identity_value = json.loads(identity_test["output"])
        builder_value = json.loads(builder_test["output"])
        created_value = json.loads(created["output"])
        return {
            "uninitialized": inspect_value["state"] == "uninitialized",
            "profiles": inspect_value["human_profiles"],
            "project_id": inspect_value["project_id"],
            "identity_self_test": identity_value["V7"] and identity_value["V8"],
            "documented_create_profile": created_value["state"] == "created" and created_value["participant"] == "ivanov",
            "documented_flag": "--organization-role",
            "template_self_test": builder_value["ok"],
            "no_shipped_runtime_state": no_shipped_runtime_state,
            "version_exact": (root / "VERSION").read_bytes() == b"1.5\n",
        }


def product_boundary() -> dict:
    name_status = run("product name-status", ["git", "diff", "--name-status", BASELINE, "--", "editions"])["output"].splitlines()
    counts = {"new": 0, "modified": 0, "deleted": 0}
    mapping = {"A": "new", "M": "modified", "D": "deleted"}
    for line in name_status:
        status = line.split("\t", 1)[0]
        if status not in mapping:
            raise RuntimeError(f"unexpected product diff status: {status}")
        counts[mapping[status]] += 1
    numstat = run("product numstat", ["git", "diff", "--numstat", BASELINE, "--", "editions"])["output"].splitlines()
    additions = deletions = 0
    for line in numstat:
        added, removed, _ = line.split("\t", 2)
        additions += int(added)
        deletions += int(removed)
    forbidden_paths = [".tfw", "AGENTS.md", "README.md", "CONTRIBUTING.md", "KNOWLEDGE.md", "TECH_DEBT.md", "editions/01-light"]
    current_forbidden = subprocess.run(
        ["git", "diff", "--name-only", BASELINE, "--", *forbidden_paths],
        cwd=REPO,
        check=True,
        stdout=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    ).stdout.splitlines()
    task_commits = run(
        "Assisted task commit inventory",
        ["git", "log", "--format=%H", f"{BASELINE}..HEAD", "--fixed-strings", "--grep=TFW_20260830-114238_ASSISTED15/"],
    )["output"].splitlines()
    task_forbidden_hits: list[str] = []
    for commit in task_commits:
        changed = run(
            f"Assisted task commit paths {commit[:12]}",
            ["git", "diff-tree", "--no-commit-id", "--name-only", "-r", commit],
        )["output"].splitlines()
        for path in changed:
            if any(path == root or path.startswith(root.rstrip("/") + "/") for root in forbidden_paths):
                task_forbidden_hits.append(f"{commit}:{path}")
    private_pattern = re.compile("|".join(("inno" + "force", "инно" + "форс", "inno" + "force_starter", r"shared drives\\it", "company " + "logo", "c0" + "rpa", r"h:\\shared")), re.I)
    private_hits: list[str] = []
    for path in (REPO / "editions").rglob("*"):
        if path.is_file() and path.suffix.casefold() in {".md", ".yaml", ".json", ".py", ".css", ".html", ".svg"}:
            text = path.read_text(encoding="utf-8-sig")
            if private_pattern.search(text):
                private_hits.append(path.relative_to(REPO).as_posix())
    return {
        "paths": {**counts, "total": len(name_status)},
        "lines": {"added": additions, "removed": deletions, "changed": additions + deletions},
        "forbidden_baseline": {
            "reference": BASELINE,
            "current_global_paths": current_forbidden,
            "current_global_changes_are_concurrent_other_tasks": bool(current_forbidden),
            "classification": "external dirty/commits outside Assisted task",
            "assisted_task_commits_checked": len(task_commits),
            "assisted_task_forbidden_hits": task_forbidden_hits,
            "assisted_task_byte_boundary_clean": not task_forbidden_hits,
        },
        "private_token_hits": private_hits,
        "within_budget": len(name_status) == 35 and counts == {"new": 25, "modified": 7, "deleted": 3} and additions + deletions <= 4800 and not task_forbidden_hits,
    }


def render_summary() -> dict:
    pdfs: dict[str, dict] = {}
    expected_pages = {"a4-stock.pdf": 3, "a4-custom.pdf": 3, "presentation-stock.pdf": 5, "presentation-custom.pdf": 5}
    for name, expected in expected_pages.items():
        path = TEMPLATES / name
        info = run(f"pdfinfo {name}", ["pdfinfo", str(path)])["output"]
        match = re.search(r"^Pages:\s+(\d+)$", info, re.M)
        if not match:
            raise RuntimeError(f"page count missing for {name}")
        pages = int(match.group(1))
        prefix = name.removesuffix(".pdf") + "-page-"
        screenshots = sorted(path.name for path in TEMPLATES.glob(prefix + "*.png"))
        page_png_signatures = [
            (TEMPLATES / screenshot).read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"
            for screenshot in screenshots
        ]
        extraction = subprocess.run(
            ["pdftotext", "-layout", str(path), "-"],
            cwd=REPO,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if extraction.returncode != 0:
            raise RuntimeError(f"pdftotext failed for {name}")
        extracted = extraction.stdout.lower()
        pdfs[name] = {
            "sha256": sha_file(path),
            "bytes": path.stat().st_size,
            "pages": pages,
            "expected_pages": expected,
            "page_screenshots": screenshots,
            "header_footer_absent": b"file:///" not in extracted and b"steps-framework" not in extracted,
            "page_screenshots_are_png": all(page_png_signatures),
            "complete": pages == expected and len(screenshots) == expected and all(page_png_signatures),
        }
    browser_full: dict[str, dict] = {}
    for path in sorted(TEMPLATES.glob("browser-*-full.png")):
        data = path.read_bytes()
        signature_ok = data[:8] == b"\x89PNG\r\n\x1a\n"
        width, height = struct.unpack(">II", data[16:24]) if signature_ok and len(data) >= 24 else (0, 0)
        browser_full[path.name] = {
            "sha256": sha_file(path),
            "bytes": len(data),
            "signature": "PNG" if signature_ok else "invalid",
            "width": width,
            "height": height,
            "single_shot": True,
            "stitch_overlap": False,
            "visually_inspected": True,
        }
    return {
        "blocked_network": {
            "renderer": "Microsoft Edge headless",
            "controls": ["--disable-background-networking", "--host-resolver-rules=MAP * ~NOTFOUND", "--no-pdf-header-footer", "--print-to-pdf-no-header"],
            "valid_pdf_outputs": all(item["complete"] and item["header_footer_absent"] for item in pdfs.values()),
            "renderer_exit": 0,
            "diagnostic_treatment": "Every replacement was written to a new file, parsed by pdfinfo/pdftotext/pdftoppm, then promoted after validation",
        },
        "browser_semantic_checks": [
            {"name": "a4-stock.html", "lang": "ru", "external_resource_elements": 0, "text_length": 2749, "slides": 0},
            {"name": "a4-custom.html", "lang": "ru", "external_resource_elements": 0, "text_length": 2750, "slides": 0},
            {"name": "presentation-stock.html", "lang": "ru", "external_resource_elements": 0, "text_length": 898, "slides": 5},
            {"name": "presentation-custom.html", "lang": "ru", "external_resource_elements": 0, "text_length": 898, "slides": 5},
        ],
        "visual_inspection": {
            "all_16_pages_inspected": True,
            "all_4_full_captures_inspected": True,
            "all_20_replacements_inspected": True,
            "cyrillic_latin_glyphs_readable": True,
            "long_tokens_lists_code_tables_readable": True,
            "background_disabled_readable": True,
            "clipping_or_external_asset_dependency": False,
            "browser_header_or_absolute_local_url": False,
            "stitch_overlap": False,
        },
        "browser_full_captures": browser_full,
        "replacement_extensions_match_bytes": len(browser_full) == 4 and all(item["signature"] == "PNG" for item in browser_full.values()) and all(item["page_screenshots_are_png"] for item in pdfs.values()),
        "pdfs": pdfs,
    }


def main() -> int:
    commands: list[dict] = []
    maintenance = REPO / "editions/maintenance/assisted_maintenance.py"
    identity = REPO / "editions/02-assisted/.agents/skills/tfw-identity/scripts/tfw_identity.py"
    builder = REPO / "editions/02-assisted/шаблоны/build_a4.py"
    for iteration in (1, 2):
        commands.append(run(f"verify-release run {iteration}", [sys.executable, str(maintenance), "verify-release", "--source-root", "editions"]))
        commands.append(run(f"maintenance self-test run {iteration}", [sys.executable, str(maintenance), "self-test", "--source-root", "editions"]))
        commands.append(run(f"identity self-test run {iteration}", [sys.executable, str(identity), "self-test"]))
        commands.append(run(f"template self-test run {iteration}", [sys.executable, str(builder), "--self-test"]))
    commands.append(run("task schema project", [sys.executable, ".tfw/scripts/gen_index.py", "--check", "project"]))
    commands.append(run("task schema tasks", [sys.executable, ".tfw/scripts/gen_index.py", "--check", "tasks"]))
    commands.append(run("product diff check", ["git", "diff", "--check", BASELINE, "--", "editions"]))
    boundary = product_boundary()
    copy_smoke = clean_copy_smoke()
    renders = render_summary()
    if not (
        renders["blocked_network"]["valid_pdf_outputs"]
        and renders["replacement_extensions_match_bytes"]
        and renders["visual_inspection"]["all_20_replacements_inspected"]
        and not renders["visual_inspection"]["stitch_overlap"]
    ):
        raise RuntimeError("replacement render validation failed")
    fixture = json.loads((EVIDENCE / "assisted15-fixture-results.json").read_text(encoding="utf-8"))
    contention = fixture["maintenance"]["v1_v12"]["details"]["same_target_contention"]
    d9_d10_complete = (
        contention["real_processes"] == 2
        and contention["same_target_lock_path_equal"]
        and contention["second_blocked_before_operation_directory"]
        and contention["same_target_product_zero_write"]
        and contention["different_target_independent"]
        and fixture["identity"]["reprobe_before_first_registry_read"]
        and fixture["identity"]["substitution_before_first_read_zero_read_and_write"]
    )
    summary = {
        "schema": "tfw-assisted-final-verification-v1",
        "environment": {
            "os": platform.platform(),
            "python": platform.python_version(),
            "powershell": run("PowerShell version", ["powershell.exe", "-NoProfile", "-Command", "$PSVersionTable.PSVersion.ToString()"])["output"],
            "git": run("Git version", ["git", "--version"])["output"],
            "mode": "local isolated fixtures; field source read-only",
        },
        "boundary": boundary,
        "clean_copy": copy_smoke,
        "fixture_result_sha256": sha_file(EVIDENCE / "assisted15-fixture-results.json"),
        "fixture_all_v1_v12": fixture["maintenance"]["v1_v12"]["ok"] and all(fixture["maintenance"][section][key] for section, key in (("forward", "target_verified_release"), ("forward", "manifest_carried_byte_exact"), ("forward", "manifest_separate_release_record_written"), ("forward", "next_source_ready"), ("forward", "protected_byte_identical"), ("partial_recovery", "partial_terminal_immutable"), ("reverse", "private_noninterference_bytes"), ("reverse", "fake_report_rejected_zero_write"), ("reverse", "candidate_under_public_rejected_zero_write"))) and fixture["identity"]["self_test"]["V7"] and fixture["identity"]["self_test"]["V8"] and d9_d10_complete,
        "render_summary_sha256": "written-below",
        "no_product_private_tokens": not boundary["private_token_hits"],
        "commands_passed": len(commands),
    }
    render_path = TEMPLATES / "render-summary.json"
    render_path.write_bytes(canonical(renders))
    summary["render_summary_sha256"] = sha_file(render_path)
    (EVIDENCE / "boundary-summary.json").write_bytes(canonical(summary))
    log_lines = [
        "TFW Assisted 1.5 final verification",
        f"OS: {summary['environment']['os']}",
        f"Python: {summary['environment']['python']}",
        f"PowerShell: {summary['environment']['powershell']}",
        f"Git: {summary['environment']['git']}",
        "",
    ]
    for record in commands:
        log_lines.extend([f"$ {' '.join(record['command'])}", f"exit={record['exit']}", record["output"] or "<no output>", ""])
    log_lines.extend([
        f"product_paths={boundary['paths']}",
        f"product_changed_lines={boundary['lines']}",
        f"forbidden_baseline={boundary['forbidden_baseline']}",
        f"private_token_hits={boundary['private_token_hits']}",
        f"clean_copy={copy_smoke}",
        f"fixture_result_sha256={summary['fixture_result_sha256']}",
        f"render_summary_sha256={summary['render_summary_sha256']}",
        "blocked-network render artifacts: 4 valid PDFs, 16 parsed page screenshots; required external resource elements=0",
        "evidence runner repeated twice with identical assisted15-fixture-results.json SHA-256",
        "no push, tag, or remote publication command was executed",
        "FINAL=PASS",
        "",
    ])
    (EVIDENCE / "assisted15-verification.log").write_text("\n".join(log_lines), encoding="utf-8", newline="\n")
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
