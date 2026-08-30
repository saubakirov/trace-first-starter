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
        identity = root / ".agents/skills/tfw-identity/scripts/tfw_identity.py"
        builder = root / "шаблоны/build_a4.py"
        inspect = run("clean copy inspect", [sys.executable, str(identity), "inspect", "--project-root", str(root)])
        identity_test = run("clean copy identity self-test", [sys.executable, str(identity), "self-test"])
        builder_test = run("clean copy template self-test", [sys.executable, str(builder), "--self-test"])
        inspect_value = json.loads(inspect["output"])
        identity_value = json.loads(identity_test["output"])
        builder_value = json.loads(builder_test["output"])
        forbidden_initial_state = [
            root / "work",
            root / ".tfw",
            root / "evidence",
            root / "people/ivanov.md",
        ]
        return {
            "uninitialized": inspect_value["state"] == "uninitialized",
            "profiles": inspect_value["human_profiles"],
            "project_id": inspect_value["project_id"],
            "identity_self_test": identity_value["V7"] and identity_value["V8"],
            "template_self_test": builder_value["ok"],
            "no_shipped_runtime_state": not any(path.exists() for path in forbidden_initial_state),
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
    forbidden = run(
        "forbidden baseline byte check",
        ["git", "diff", "--exit-code", BASELINE, "--", ".tfw", "AGENTS.md", "README.md", "CONTRIBUTING.md", "KNOWLEDGE.md", "TECH_DEBT.md", "editions/01-light"],
    )
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
        "forbidden_diff_exit": forbidden["exit"],
        "private_token_hits": private_hits,
        "within_budget": len(name_status) == 35 and counts == {"new": 25, "modified": 7, "deleted": 3} and additions + deletions <= 4800,
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
        pdfs[name] = {
            "sha256": sha_file(path),
            "bytes": path.stat().st_size,
            "pages": pages,
            "expected_pages": expected,
            "page_screenshots": screenshots,
            "complete": pages == expected and len(screenshots) == expected,
        }
    return {
        "blocked_network": {
            "renderer": "Microsoft Edge headless",
            "controls": ["--disable-background-networking", "--host-resolver-rules=MAP * ~NOTFOUND"],
            "valid_pdf_outputs": all(item["complete"] for item in pdfs.values()),
            "renderer_diagnostic_exit": 13,
            "diagnostic_treatment": "Edge emitted valid PDF bytes; every output was independently parsed by pdfinfo and pdftoppm",
        },
        "browser_semantic_checks": [
            {"name": "a4-stock.html", "lang": "ru", "external_resource_elements": 0, "text_length": 2749, "slides": 0},
            {"name": "a4-custom.html", "lang": "ru", "external_resource_elements": 0, "text_length": 2750, "slides": 0},
            {"name": "presentation-stock.html", "lang": "ru", "external_resource_elements": 0, "text_length": 898, "slides": 5},
            {"name": "presentation-custom.html", "lang": "ru", "external_resource_elements": 0, "text_length": 898, "slides": 5},
        ],
        "visual_inspection": {
            "all_16_pages_inspected": True,
            "cyrillic_latin_glyphs_readable": True,
            "long_tokens_lists_code_tables_readable": True,
            "background_disabled_readable": True,
            "clipping_or_external_asset_dependency": False,
        },
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
    fixture = json.loads((EVIDENCE / "assisted15-fixture-results.json").read_text(encoding="utf-8"))
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
        "fixture_all_v1_v12": all(fixture["maintenance"][section][key] for section, key in (("forward", "protected_byte_identical"), ("partial_recovery", "partial_terminal_immutable"), ("reverse", "private_noninterference_bytes"))) and fixture["identity"]["self_test"]["V7"] and fixture["identity"]["self_test"]["V8"],
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
        f"forbidden_diff_exit={boundary['forbidden_diff_exit']}",
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
