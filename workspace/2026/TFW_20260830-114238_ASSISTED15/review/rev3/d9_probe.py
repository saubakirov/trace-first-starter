#!/usr/bin/env python3
"""Independent Reviewer probe for stable target-keyed maintenance locking."""

from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import queue
import subprocess
import sys
import tempfile
import threading


REPO = Path(__file__).resolve().parents[5]
MODULE_PATH = REPO / "editions/maintenance/assisted_maintenance.py"


def load_module():
    spec = importlib.util.spec_from_file_location("reviewer_d9_maintenance", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    holder_program = r'''
import importlib.util
import faulthandler
from pathlib import Path
import sys
faulthandler.dump_traceback_later(10, repeat=False)
spec = importlib.util.spec_from_file_location("reviewer_d9_holder", sys.argv[1])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
target, target_pin = module.pin_existing(Path(sys.argv[2]), "target root")
lock_path, namespace_pin, root_pin = module.project_lock_path(target, target_pin, [target], Path(sys.argv[3]))
with module.ProjectLock(lock_path, namespace_pin, root_pin):
    print(lock_path.name, flush=True)
    sys.stdin.readline()
'''
    with tempfile.TemporaryDirectory(prefix="tfw-review-d9-") as raw:
        base = Path(raw)
        source = base / "source"
        source.mkdir()
        _, _, prior, prior_raw = module.fixture_release(source)
        target = base / "target"
        (target / "02-assisted").mkdir(parents=True)
        (target / "02-assisted/README.md").write_bytes(b"old\n")
        (target / "02-assisted/PROJECT.md").write_bytes(b"private\n")
        state_home = base / "state"
        target_root, target_pin = module.pin_existing(target, "target root")
        expected_lock, _, _ = module.project_lock_path(target_root, target_pin, [source, target], state_home)
        environment = dict(os.environ)
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        holder = subprocess.Popen(
            [sys.executable, "-B", "-c", holder_program, str(MODULE_PATH), str(target), str(state_home)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            env=environment,
        )
        try:
            lines: queue.Queue[str] = queue.Queue()
            reader = threading.Thread(target=lambda: lines.put(holder.stdout.readline().strip()), daemon=True)
            reader.start()
            try:
                held_name = lines.get(timeout=15)
            except queue.Empty:
                holder.terminate()
                try:
                    holder.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    holder.kill()
                    holder.wait(timeout=5)
                result = {
                    "different_target_independent": False,
                    "expected_lock": expected_lock.name,
                    "held_lock": None,
                    "holder_completed_lock_entry": False,
                    "holder_stderr": holder.stderr.read().strip(),
                    "loser_blocked_by_live_lock": False,
                    "loser_operation_directory_absent": True,
                    "same_stable_lock_key": False,
                    "same_target_tree_unchanged": True,
                    "source_tree_unchanged": True,
                    "ok": False,
                }
                print(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
                return 2
            if holder.poll() is not None or not held_name.startswith("target-"):
                raise RuntimeError(holder.stderr.read().strip() or "holder failed before acquiring lock")
            before = module.tree_state(target)
            losing_operation = base / "losing-operation"
            try:
                module.execute_forward(source, target, prior, prior_raw, losing_operation, state_home=state_home)
                loser = "unexpected-success"
            except module.MaintenanceError as exc:
                loser = str(exc)
            same_target_after = module.tree_state(target)

            other = base / "other-target"
            (other / "02-assisted").mkdir(parents=True)
            (other / "02-assisted/README.md").write_bytes(b"old\n")
            (other / "02-assisted/PROJECT.md").write_bytes(b"other-private\n")
            other_operation = base / "other-operation"
            other_result = module.execute_forward(source, other, prior, prior_raw, other_operation, state_home=state_home)

            result = {
                "different_target_independent": other_result.get("status") == "verified",
                "expected_lock": expected_lock.name,
                "held_lock": held_name,
                "loser_blocked_by_live_lock": "holds the project lock" in loser,
                "loser_operation_directory_absent": not losing_operation.exists(),
                "same_stable_lock_key": held_name == expected_lock.name,
                "same_target_tree_unchanged": before == same_target_after,
                "source_tree_unchanged": module.verify_release_root(source)[0]["version"] == "1.5",
            }
            result["ok"] = all(value for key, value in result.items() if key not in {"expected_lock", "held_lock", "ok"})
            print(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
            return 0 if result["ok"] else 2
        finally:
            if holder.poll() is None:
                holder.stdin.write("release\n")
                holder.stdin.flush()
                holder.wait(timeout=10)


if __name__ == "__main__":
    raise SystemExit(main())
