"""One cheap contract test for the repository's useful Git-blob guard."""

import importlib.util
from pathlib import Path

CHECKER = Path(__file__).resolve().parents[1] / "check_git_blob_sizes.py"
SPEC = importlib.util.spec_from_file_location("git_blob_guard", CHECKER)
GUARD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GUARD)


def test_five_mib_boundary_accepts_exact_and_rejects_larger():
    exact_oid = "a" * 40
    over_oid = "b" * 40
    occurrences = {("exact.bin", exact_oid), ("oversized.log", over_oid)}
    metadata = {
        exact_oid: ("blob", GUARD.LIMIT),
        over_oid: ("blob", GUARD.LIMIT + 1),
    }

    assert GUARD.LIMIT == 5 * 1024 * 1024
    assert GUARD.inspect_occurrences(occurrences, metadata) == [
        {
            "reason": "blob exceeds 5242880 bytes",
            "path": "oversized.log",
            "oid": over_oid,
            "bytes": 5242881,
        }
    ]
