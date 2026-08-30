#!/usr/bin/env python3
"""Bounded independent Reviewer probes for D1–D8 paths not requiring live locks."""

from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


REPO = Path(__file__).resolve().parents[5]
MAINT_PATH = REPO / "editions/maintenance/assisted_maintenance.py"
IDENTITY_PATH = REPO / "editions/02-assisted/.agents/skills/tfw-identity/scripts/tfw_identity.py"


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    maint = load("reviewer_v_maintenance", MAINT_PATH)
    results: dict[str, object] = {}
    with tempfile.TemporaryDirectory(prefix="tfw-review-v-") as raw:
        base = Path(raw)

        omitted = base / "omitted"
        shutil.copytree(REPO / "editions", omitted)
        (omitted / "02-assisted/README.md").unlink()
        try:
            maint.verify_release_root(omitted)
            results["D1_omitted_payload_rejected"] = False
        except maint.MaintenanceError as exc:
            results["D1_omitted_payload_rejected"] = "paths differ" in str(exc)

        source = base / "source"
        source.mkdir()
        _, _, prior, prior_raw = maint.fixture_release(source)
        target = base / "target"
        (target / "02-assisted").mkdir(parents=True)
        (target / "02-assisted/README.md").write_bytes(b"old\n")
        (target / "02-assisted/PROJECT.md").write_bytes(b"private\n")
        target_before = maint.tree_state(target)
        junction = base / "operation-parent-junction"
        if os.name == "nt":
            linked = subprocess.run(
                ["cmd", "/c", "mklink", "/J", str(junction), str(target)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            ).returncode == 0
        else:
            os.symlink(target, junction, target_is_directory=True)
            linked = True
        try:
            maint.execute_forward(source, target, prior, prior_raw, junction / "operation")
            link_rejected = False
        except maint.MaintenanceError as exc:
            link_rejected = linked and "link or reparse" in str(exc)
        results["D3_operation_link_rejected"] = link_rejected
        results["D3_target_unchanged"] = target_before == maint.tree_state(target)
        results["D3_operation_absent"] = not (target / "operation").exists()
        if linked:
            if junction.is_symlink():
                junction.unlink()
            else:
                os.rmdir(junction)

        fake = base / "fake-operation"
        fake.mkdir()
        (fake / "terminal.json").write_bytes(
            maint.canonical(
                {
                    "schema": maint.REPORT_SCHEMA,
                    "operation_id": "f" * 32,
                    "status": "verified",
                    "changes": 0,
                    "recover_from": None,
                }
            )
        )
        (fake / "journal.ndjson").write_bytes(b"{}\n")
        fake_candidate = base / "fake-candidate"
        try:
            maint.reverse_candidate(fake / "terminal.json", fake_candidate, fake_candidate, [source, target], False)
            results["D5_fake_provenance_rejected_zero_write"] = False
        except maint.MaintenanceError:
            results["D5_fake_provenance_rejected_zero_write"] = not fake_candidate.exists()

        private_a = maint.write_private_operation_fixture(base / "private-a", "a" * 32, 1)
        private_b = maint.write_private_operation_fixture(base / "private-b", "b" * 32, 2)
        under_public = source / "candidate"
        try:
            maint.reverse_candidate(private_a, under_public, under_public, [source, target], False)
            results["D5_public_root_rejected_zero_write"] = False
        except maint.MaintenanceError:
            results["D5_public_root_rejected_zero_write"] = not under_public.exists()
        candidate_a = base / "candidate-a"
        candidate_b = base / "candidate-b"
        projection_a = maint.reverse_candidate(private_a, candidate_a, candidate_a, [source, target], False)
        projection_b = maint.reverse_candidate(private_b, candidate_b, candidate_b, [source, target], False)
        results["D5_private_noninterference"] = (
            projection_a == projection_b
            and (candidate_a / "public-candidate.json").read_bytes()
            == (candidate_b / "public-candidate.json").read_bytes()
        )

        tabletop = maint.role_scenario_matrix()
        results["D6_seven_deterministic_roles"] = (
            tabletop["ok"]
            and len(tabletop["records"]) == 7
            and all(record["observed"]["duplicates"] == 0 for record in tabletop["records"])
        )

        clean = base / "clean-assisted"
        shutil.copytree(REPO / "editions/02-assisted", clean)
        environment = dict(os.environ)
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        manifest_run = subprocess.run(
            [sys.executable, "-B", str(IDENTITY_PATH), "profile-manifest", "--project-root", str(clean)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            env=environment,
            timeout=20,
        )
        manifest = json.loads(manifest_run.stdout)
        create_run = subprocess.run(
            [
                sys.executable,
                "-B",
                str(IDENTITY_PATH),
                "create-profile",
                "--project-root",
                str(clean),
                "--expected-manifest",
                manifest["people_manifest"],
                "--display-name",
                "Иван Иванов",
                "--surname",
                "Иванов",
                "--organization-role",
                "Эксперт",
                "--project-role",
                "Участник",
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            env=environment,
            timeout=20,
        )
        created = json.loads(create_run.stdout)
        results["D7_documented_identity_flag"] = (
            created.get("participant") == "ivanov" and (clean / "people/ivanov.md").is_file()
        )

    results["ok"] = all(bool(value) for value in results.values())
    print(json.dumps(results, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    return 0 if results["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
