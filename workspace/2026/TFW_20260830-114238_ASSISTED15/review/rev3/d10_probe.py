#!/usr/bin/env python3
"""Independent Reviewer probes for identity first-access ordering and substitution."""

from __future__ import annotations

from contextlib import contextmanager
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


REPO = Path(__file__).resolve().parents[5]
MODULE_PATH = REPO / "editions/02-assisted/.agents/skills/tfw-identity/scripts/tfw_identity.py"


def load_module():
    spec = importlib.util.spec_from_file_location("reviewer_d10_identity", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def remove_link(path: Path) -> None:
    if path.is_symlink():
        path.unlink()
    else:
        os.rmdir(path)


def main() -> int:
    module = load_module()
    for key in ("OneDrive", "OneDriveCommercial", "OneDriveConsumer", "GOOGLE_DRIVE", "DROPBOX"):
        os.environ.pop(key, None)
    with tempfile.TemporaryDirectory(prefix="tfw-review-d10-") as raw:
        base = Path(raw)
        project = base / "project"
        (project / "people").mkdir(parents=True)
        (project / "PROJECT.md").write_text(
            "Состояние: ИНИЦИАЛИЗИРОВАН\nproject_id: 00000000-0000-4000-8000-000000000001\n",
            encoding="utf-8",
        )
        parent = base / "local"
        namespace = parent / module.PRODUCT
        namespace.mkdir(parents=True)
        module.secure_namespace(namespace)
        store = namespace / "bindings.json"
        original_registry = module.registry_bytes(
            [{"project_id": "00000000-0000-4000-8000-000000000001", "mode": "ask"}]
        )
        store.write_bytes(original_registry)
        if os.name != "nt":
            os.chmod(store, 0o600)
        module.private_permissions(store)
        decision = module.locality(store, project, [], True)
        if decision.get("state") != "proven":
            raise RuntimeError(f"initial locality fixture failed: {decision}")

        # Probe the actual validated read call graph without invoking the Windows
        # icacls-under-live-lock defect: only replace the lock primitive, not the
        # production ordering function under test.
        call_order: list[str] = []
        original_reprobe = module.reprobe
        original_live_lock = module.live_lock
        original_read_registry = module.read_registry

        def tracked_reprobe(value):
            call_order.append("reprobe")
            return original_reprobe(value)

        @contextmanager
        def tracked_live_lock(path):
            call_order.append("lock_exists_type_open")
            path.write_bytes(b"0")
            if os.name != "nt":
                os.chmod(path, 0o600)
            module.private_permissions(path)
            try:
                yield
            finally:
                path.unlink(missing_ok=True)

        def tracked_read_registry(path):
            call_order.append("registry_exists_type_read")
            return original_read_registry(path)

        module.reprobe = tracked_reprobe
        module.live_lock = tracked_live_lock
        module.read_registry = tracked_read_registry
        try:
            with module.validated_registry_lock(store, decision):
                bindings, existed = module.read_registry(store)
        finally:
            module.reprobe = original_reprobe
            module.live_lock = original_live_lock
            module.read_registry = original_read_registry

        # Substitute the namespace after locality() and before update_registry().
        held = parent / "held"
        replacement = parent / "replacement"
        replacement.mkdir()
        module.secure_namespace(replacement)
        replacement_store = replacement / "bindings.json"
        replacement_bytes = module.registry_bytes(
            [{"project_id": "00000000-0000-4000-8000-000000000001", "mode": "fixed", "participant": "ivanov"}]
        )
        replacement_store.write_bytes(replacement_bytes)
        if os.name != "nt":
            os.chmod(replacement_store, 0o600)
        module.private_permissions(replacement_store)
        os.replace(namespace, held)
        if os.name == "nt":
            linked = subprocess.run(
                ["cmd", "/c", "mklink", "/J", str(namespace), str(replacement)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            ).returncode == 0
        else:
            os.symlink(replacement, namespace, target_is_directory=True)
            linked = True
        if not linked:
            raise RuntimeError("namespace substitution fixture could not be created")

        substituted_reads: list[str] = []
        substituted_metadata: list[str] = []
        original_lstat = module.os.lstat
        original_read_registry = module.read_registry
        store_norm = os.path.normcase(str(store))
        lock_norm = os.path.normcase(str(store.with_suffix(".lock")))

        def tracked_lstat(value):
            normalized = os.path.normcase(str(value))
            if normalized in {store_norm, lock_norm}:
                substituted_metadata.append(normalized)
            return original_lstat(value)

        def rejected_read_registry(path):
            substituted_reads.append(os.path.normcase(str(path)))
            return original_read_registry(path)

        module.os.lstat = tracked_lstat
        module.read_registry = rejected_read_registry
        try:
            try:
                module.update_registry(
                    store,
                    decision,
                    {"project_id": "00000000-0000-4000-8000-000000000001", "mode": "ask"},
                )
                rejected = False
            except module.IdentityError:
                rejected = True
        finally:
            module.os.lstat = original_lstat
            module.read_registry = original_read_registry

        replacement_unchanged = replacement_store.read_bytes() == replacement_bytes
        runtime_files_absent = not (replacement / "bindings.lock").exists() and not any(
            path.name.startswith("bindings-") for path in replacement.iterdir()
        )
        remove_link(namespace)
        shutil.rmtree(held, ignore_errors=True)
        result = {
            "first_access_order": call_order,
            "locked_read_saw_existing_registry": existed and bindings[0]["mode"] == "ask",
            "reprobe_precedes_lock_access": call_order.index("reprobe") < call_order.index("lock_exists_type_open"),
            "reprobe_precedes_registry_access": call_order.index("reprobe") < call_order.index("registry_exists_type_read"),
            "substitution_rejected": rejected,
            "substituted_registry_metadata_accesses": len(substituted_metadata),
            "substituted_registry_reads": len(substituted_reads),
            "substituted_registry_unchanged": replacement_unchanged,
            "substituted_runtime_files_absent": runtime_files_absent,
        }
        result["ok"] = (
            result["locked_read_saw_existing_registry"]
            and result["reprobe_precedes_lock_access"]
            and result["reprobe_precedes_registry_access"]
            and result["substitution_rejected"]
            and result["substituted_registry_metadata_accesses"] == 0
            and result["substituted_registry_reads"] == 0
            and result["substituted_registry_unchanged"]
            and result["substituted_runtime_files_absent"]
        )
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
        return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
