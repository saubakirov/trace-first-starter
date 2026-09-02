#!/usr/bin/env python3
"""Run the AC-1 clean replay without disclosing source-manifest rows."""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import runpy
import subprocess
import sys


TASK_ID = "TFW_20260830-202031_FA15ES"
EXPECTED_BRANCH = "codex/tfw-fa15es-executor"
PRODUCT_PARENT = "e5e20f5b1070f48740d7d47bdd264ccc66ee524d"
PRODUCT_COMMIT = "626d77b5c3261dff493d15c7ce5862b9e036d10e"
EXPECTED_SOURCE_FILES = 28
EXPECTED_SOURCE_BYTES = 297_522
ROUTING_PATHS = (
    "editions/README.md",
    "editions/ASSISTED_MAINTENANCE.md",
)

REPO = Path(__file__).resolve().parents[5]
EVIDENCE = REPO / "workspace" / "2026" / TASK_ID / "evidence" / "attachments"
MATERIALIZER = EVIDENCE / "materialize_assisted.py"
SOURCE = Path(os.environ["TFW_FA15ES_SOURCE"]).resolve(strict=True)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_bytes(*args: str) -> bytes:
    result = subprocess.run(
        ["git", "-c", "core.quotepath=false", *args],
        cwd=REPO,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(f"git command failed ({result.returncode}): {' '.join(args)}")
    return result.stdout


def git_text(*args: str) -> str:
    return git_bytes(*args).decode("utf-8").strip()


def persist_once(path: Path, value: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    with path.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())


def source_aggregate(label: str) -> dict[str, object]:
    paths = sorted(
        (path for path in SOURCE.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(SOURCE).as_posix(),
    )
    if any(path.is_symlink() for path in paths):
        raise RuntimeError("source contains a symlink")
    rows: list[str] = []
    total = 0
    for path in paths:
        data = path.read_bytes()
        relative = path.relative_to(SOURCE).as_posix()
        rows.append(f"{relative}|{len(data)}|{sha256(data)}")
        total += len(data)
    payload = ("\n".join(rows) + "\n").encode("utf-8")
    result: dict[str, object] = {
        "label": label,
        "captured_at": dt.datetime.now().astimezone().isoformat(timespec="microseconds"),
        "canonicalization": "ordinal relative-path|size|sha256 rows joined by LF with final LF",
        "files": len(paths),
        "bytes": total,
        "aggregate_sha256": sha256(payload),
        "private_rows_covered": True,
        "per_row_values_persisted": False,
        "source_locator_persisted": False,
    }
    if (len(paths), total) != (EXPECTED_SOURCE_FILES, EXPECTED_SOURCE_BYTES):
        raise RuntimeError("source census differs from the frozen 28-file/297522-byte contract")
    return result


def derive_materializer_targets(module: dict[str, object]) -> list[str]:
    target_root = REPO / "editions" / "02-assisted"
    exact = module["EXACT"]
    adapted = module["ADAPTED_TARGETS"]
    delete_baselines = module["DELETE_BASELINES"]
    if not isinstance(exact, dict) or not isinstance(adapted, dict) or not isinstance(delete_baselines, dict):
        raise RuntimeError("materializer target tables are unavailable")
    targets = {
        (target_root / str(relative)).resolve().relative_to(REPO.resolve()).as_posix()
        for relative in [*exact.values(), *adapted.values()]
    }
    targets.add("editions/02-assisted/people/README.md")
    for relative in delete_baselines:
        targets.add((target_root / str(relative)).resolve().relative_to(REPO.resolve()).as_posix())
    if len(targets) != 28:
        raise RuntimeError(f"materializer target count is {len(targets)}, expected 28")
    return sorted(targets)


def canonical_file_aggregate(rows: dict[str, bytes]) -> dict[str, object]:
    ordered = [f"{path}|{len(rows[path])}|{sha256(rows[path])}" for path in sorted(rows)]
    payload = ("\n".join(ordered) + "\n").encode("utf-8")
    return {
        "files": len(rows),
        "bytes": sum(len(data) for data in rows.values()),
        "aggregate_sha256": sha256(payload),
    }


def committed_editions() -> dict[str, bytes]:
    raw = git_bytes("ls-tree", "-r", "-z", "--name-only", PRODUCT_COMMIT, "--", "editions")
    paths = [item.decode("utf-8") for item in raw.split(b"\0") if item]
    return {path: git_bytes("show", f"{PRODUCT_COMMIT}:{path}") for path in paths}


def working_editions() -> dict[str, bytes]:
    return {
        path.relative_to(REPO).as_posix(): path.read_bytes()
        for path in sorted((REPO / "editions").rglob("*"))
        if path.is_file()
    }


def main() -> None:
    if git_text("rev-parse", "HEAD") != PRODUCT_PARENT:
        raise RuntimeError("replay checkout is not the exact product parent")
    if git_text("branch", "--show-current") != EXPECTED_BRANCH:
        raise RuntimeError("replay branch is not the executor branch name")
    if not MATERIALIZER.is_file():
        raise RuntimeError("committed task-local materializer was not supplied")

    materializer_module = runpy.run_path(str(MATERIALIZER))
    materializer_targets = derive_materializer_targets(materializer_module)
    product_targets = sorted(set(materializer_targets) | set(ROUTING_PATHS))
    if len(product_targets) != 30:
        raise RuntimeError("replay product write ledger is not exactly 30 paths")
    source_root = SOURCE.resolve()
    source_write_targets = [
        path for path in product_targets if source_root == (REPO / path).resolve() or source_root in (REPO / path).resolve().parents
    ]
    if source_write_targets:
        raise RuntimeError("a replay write target enters the source root")

    pre_path = EVIDENCE / "replay-pre-source-aggregate.json"
    post_path = EVIDENCE / "replay-post-source-aggregate.json"
    result_path = EVIDENCE / "replay-result.json"

    pre = source_aggregate("immediately-before-materialization")
    persist_once(pre_path, pre)

    materializer_command = [sys.executable, str(MATERIALIZER)]
    materializer = subprocess.run(
        materializer_command,
        cwd=REPO,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        check=False,
    )
    if materializer.returncode:
        raise RuntimeError(f"materializer failed with exit code {materializer.returncode}")

    post = source_aggregate("immediately-after-materializer")
    persist_once(post_path, post)
    if (pre["files"], pre["bytes"], pre["aggregate_sha256"]) != (
        post["files"],
        post["bytes"],
        post["aggregate_sha256"],
    ):
        raise RuntimeError("source aggregate changed during clean replay")

    routing_rows = []
    for relative in ROUTING_PATHS:
        data = git_bytes("show", f"{PRODUCT_COMMIT}:{relative}")
        target = (REPO / relative).resolve()
        if (REPO / "editions").resolve() not in target.parents:
            raise RuntimeError("routing target escapes editions")
        target.write_bytes(data)
        routing_rows.append(
            {
                "path": relative,
                "source": f"{PRODUCT_COMMIT}:{relative}",
                "bytes": len(data),
                "sha256": sha256(data),
            }
        )

    expected = committed_editions()
    actual = working_editions()
    expected_paths, actual_paths = set(expected), set(actual)
    missing = sorted(expected_paths - actual_paths)
    extra = sorted(actual_paths - expected_paths)
    mismatched = sorted(path for path in expected_paths & actual_paths if expected[path] != actual[path])
    if missing or extra or mismatched:
        raise RuntimeError("replayed editions tree differs from the frozen product commit")

    result: dict[str, object] = {
        "task_id": TASK_ID,
        "proof_kind": "clean replay evidence; not an original historical observation",
        "checkout": {
            "branch": EXPECTED_BRANCH,
            "head": PRODUCT_PARENT,
            "disposable": True,
        },
        "materializer": {
            "path": f"workspace/2026/{TASK_ID}/evidence/attachments/materialize_assisted.py",
            "sha256": sha256(MATERIALIZER.read_bytes()),
            "command": materializer_command,
            "exit_code": materializer.returncode,
            "stdout": materializer.stdout.splitlines(),
            "stderr": materializer.stderr.splitlines(),
        },
        "routing_materialization": {
            "method": "exact git object bytes from the frozen product commit",
            "paths": routing_rows,
            "exit_code": 0,
        },
        "source": {
            "pre": pre,
            "post": post,
            "equal": True,
            "source_write_targets": source_write_targets,
            "source_write_target_count": len(source_write_targets),
        },
        "write_target_ledger": {
            "materializer_paths": materializer_targets,
            "routing_paths": list(ROUTING_PATHS),
            "product_path_count": len(product_targets),
        },
        "product_tree_comparison": {
            "expected_ref": PRODUCT_COMMIT,
            "expected_editions_tree_oid": git_text("rev-parse", f"{PRODUCT_COMMIT}:editions"),
            "expected": canonical_file_aggregate(expected),
            "actual": canonical_file_aggregate(actual),
            "missing_paths": missing,
            "extra_paths": extra,
            "content_mismatches": mismatched,
            "byte_and_tree_equal": True,
        },
        "verdict": "PASS",
    }
    persist_once(result_path, result)
    print(f"SOURCE_PRE={pre['files']} files / {pre['bytes']} bytes / {pre['aggregate_sha256']}")
    print(f"SOURCE_POST={post['files']} files / {post['bytes']} bytes / {post['aggregate_sha256']}")
    print(f"SOURCE_WRITE_TARGETS={len(source_write_targets)}")
    actual_summary = canonical_file_aggregate(actual)
    print(
        "PRODUCT_TREE="
        f"{actual_summary['files']} files / {actual_summary['bytes']} bytes / "
        f"{actual_summary['aggregate_sha256']}"
    )
    print("CLEAN_REPLAY_VERDICT=PASS")


if __name__ == "__main__":
    main()
