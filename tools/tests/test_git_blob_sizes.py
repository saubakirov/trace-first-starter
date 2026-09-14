"""CLI mutation tests using actual Git objects, indexes and commit histories."""

import importlib.util
import json
import os
from pathlib import Path
import stat
import subprocess
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CHECKER = PROJECT_ROOT / "tools/check_git_blob_sizes.py"
POLICY_PATH = "tools/git_blob_size_policy.json"
POLICY = (PROJECT_ROOT / POLICY_PATH).read_bytes()
spec = importlib.util.spec_from_file_location("git_blob_guard", CHECKER)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


def git(root, *args, data=None, ok=True):
    env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_TERMINAL_PROMPT="0",
               GIT_NO_LAZY_FETCH="1", GIT_NO_REPLACE_OBJECTS="1")
    result = subprocess.run(["git", "-c", "core.longpaths=true", "-c", "core.autocrlf=false",
                             *args], cwd=root, env=env, input=data,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if ok:
        assert result.returncode == 0, result.stderr.decode("utf-8", "replace")
    return result.stdout if ok else result


def write(root, path, data):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    return target


def commit(root, message="fixture"):
    git(root, "commit", "--allow-empty", "-m", message)
    return git(root, "rev-parse", "HEAD").decode().strip()


def cli(root, mode="staged", *args):
    result = subprocess.run([sys.executable, str(CHECKER), "--repo", str(root), mode, *args],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert not result.stderr, result.stderr.decode("utf-8", "replace")
    report = json.loads(result.stdout)
    assert report["status"] == {0: "PASS", 1: "FAIL", 2: "REFUSED"}[result.returncode]
    return result.returncode, report


@pytest.fixture
def repo(tmp_path):
    root = tmp_path / "repo"
    root.mkdir()
    git(root, "init", "-b", "main")
    git(root, "config", "user.name", "Blob policy fixture")
    git(root, "config", "user.email", "fixture@example.invalid")
    git(root, "config", "commit.gpgsign", "false")
    write(root, POLICY_PATH, POLICY)
    git(root, "add", "--", POLICY_PATH)
    commit(root, "baseline policy")
    git(root, "tag", "v3.3.0")
    return root


def stage_blob(repo, path, size):
    # Binary content makes the measured object size independent of line endings.
    data = b"\0\xff\n" * (size // 3) + b"\0" * (size % 3)
    write(repo, path, data)
    git(repo, "add", "--", path)
    return git(repo, "rev-parse", ":" + path).decode().strip()


def borrow_objects(repo):
    # Read-only alternate: test real grandfather objects without copying archives.
    common = Path(git(PROJECT_ROOT, "rev-parse", "--path-format=absolute", "--git-common-dir").decode().strip())
    write(repo, ".git/objects/info/alternates", (common.joinpath("objects").as_posix() + "\n").encode())


def stage_existing(repo, path, oid):
    git(repo, "update-index", "--add", "--cacheinfo", "100644", oid, path)


def test_boundary_index_bytes_and_binary_whitespace_path(repo):
    path = " space\tand newline\nfile.bin " if os.name != "nt" else " space file.bin"
    exact = stage_blob(repo, path, 10485760)
    assert cli(repo)[0] == 0
    # Unstaged oversized bytes cannot turn a valid index into a failure.
    write(repo, path, b"z" * 10485761)
    assert cli(repo)[0] == 0
    over = stage_blob(repo, path, 10485761)
    write(repo, path, b"small working copy")
    code, report = cli(repo)
    assert code == 1
    assert report["violations"] == [{"path": path, "oid": over, "bytes": 10485761,
                                      "reason": "blob exceeds 10485760 bytes"}]
    assert exact != over


def test_staged_modified_and_renamed_file(repo):
    write(repo, "small.bin", b"small")
    git(repo, "add", "small.bin")
    commit(repo)
    stage_blob(repo, "small.bin", 10485761)
    assert cli(repo)[0] == 1
    git(repo, "mv", "small.bin", "renamed large.bin")
    code, report = cli(repo)
    assert code == 1 and report["violations"][0]["path"] == "renamed large.bin"


def test_index_and_history_preserve_tab_newline_and_trailing_space(repo):
    # This index-only fixture deliberately represents a non-Windows checkout path.
    git(repo, "config", "core.protectNTFS", "false")
    oid = stage_blob(repo, "source.bin", 10485761)
    git(repo, "update-index", "--force-remove", "source.bin")
    path = " space\ttab\nnewline.bin "
    stage_existing(repo, path, oid)
    code, report = cli(repo)
    assert code == 1 and report["violations"][0]["path"] == path
    commit(repo)
    code, report = cli(repo, "release")
    assert code == 1 and report["violations"][0]["path"] == path


def test_release_detects_add_then_delete_and_uses_committed_policy(repo):
    stage_blob(repo, "transient.bin", 10485761)
    commit(repo, "add large")
    git(repo, "rm", "transient.bin")
    commit(repo, "remove large")
    write(repo, POLICY_PATH, b"invalid working policy")
    code, report = cli(repo, "release")
    assert code == 1 and report["base_tag"] == "v3.3.0"
    assert report["violations"][0]["path"] == "transient.bin"


def test_release_detects_deleted_blob_on_merged_side_branch(repo):
    git(repo, "checkout", "-b", "side")
    stage_blob(repo, "side.bin", 10485761)
    commit(repo)
    git(repo, "rm", "side.bin")
    commit(repo)
    git(repo, "checkout", "main")
    commit(repo, "main diverges")
    git(repo, "merge", "--no-ff", "-m", "merge side", "side")
    code, report = cli(repo, "release")
    assert code == 1 and any(row.get("path") == "side.bin" for row in report["violations"])


def test_tip_tag_cannot_empty_default_or_explicit_range(repo):
    stage_blob(repo, "large.bin", 10485761)
    commit(repo)
    git(repo, "tag", "-a", "v3.4.0", "-m", "tip")
    code, report = cli(repo, "release")
    assert code == 1 and report["base_tag"] == "v3.3.0"
    assert cli(repo, "release", "--base", "v3.4.0")[0] == 2


def test_default_tag_is_semantic_and_ignores_unreachable_tags(repo):
    git(repo, "tag", "v3.9.0")
    git(repo, "tag", "v3.10.0")
    git(repo, "checkout", "-b", "other")
    commit(repo)
    git(repo, "tag", "v99.0.0")
    git(repo, "checkout", "main")
    commit(repo)
    code, report = cli(repo, "release")
    assert code == 0 and report["base_tag"] == "v3.10.0"
    assert cli(repo, "release", "--base", "v99.0.0")[0] == 2


@pytest.mark.parametrize("identity", guard.GRANDFATHERED)
def test_exact_grandfathered_instance_passes_and_alias_fails(repo, identity):
    path, oid, size = identity
    borrow_objects(repo)
    stage_existing(repo, path, oid)
    code, report = cli(repo)
    assert code == 0 and report["grandfathered"] == [{"path": path, "oid": oid, "bytes": size}]
    commit(repo)
    assert cli(repo, "release")[0] == 0
    alias = "renamed/" + Path(path).name
    stage_existing(repo, alias, oid)
    code, report = cli(repo)
    assert code == 1 and any(row.get("path") == alias for row in report["violations"])
    commit(repo, "alias")
    assert cli(repo, "release")[0] == 1


def test_exact_path_with_different_large_oid_is_not_grandfathered(repo):
    path = guard.GRANDFATHERED[0][0]
    stage_blob(repo, path, 10485761)
    assert cli(repo)[0] == 1


@pytest.mark.parametrize("mutation", ["path", "oid", "size", "glob", "forbidden", "extra",
                                     "missing", "duplicate", "limit", "unknown", "provenance"])
def test_policy_identity_and_schema_mutations_refuse(repo, mutation):
    policy = json.loads(POLICY)
    row = policy["grandfathered"][0]
    if mutation == "path":
        row["path"] = "wrong/" + row["path"]
    elif mutation == "oid":
        row["oid"] = "0" * 40
    elif mutation == "size":
        row["bytes"] += 1
    elif mutation == "glob":
        row["path"] = "workspace/**"
    elif mutation == "forbidden":
        row.update(zip(("path", "oid", "bytes"), guard.EXCLUDED[0]))
    elif mutation == "extra":
        policy["grandfathered"].append(dict(row))
    elif mutation == "missing":
        policy["grandfathered"].pop()
    elif mutation == "duplicate":
        policy["grandfathered"][1] = dict(row)
    elif mutation == "limit":
        policy["max_blob_bytes"] += 1
    elif mutation == "unknown":
        policy["allow_globs"] = ["*"]
    elif mutation == "provenance":
        policy["excluded_attachments"][0]["source_carrier"] = "0" * 40
    write(repo, POLICY_PATH, json.dumps(policy).encode())
    # Working policy changes do not affect the valid staged policy.
    assert cli(repo)[0] == 0
    git(repo, "add", POLICY_PATH)
    assert cli(repo)[0] == 2
    commit(repo)
    assert cli(repo, "release")[0] == 2


def test_duplicate_json_key_is_rejected(repo):
    write(repo, POLICY_PATH, POLICY.replace(b'"schema_version": 1,', b'"schema_version": 1, "schema_version": 1,'))
    git(repo, "add", POLICY_PATH)
    assert cli(repo)[0] == 2


@pytest.mark.parametrize("path", [row[0] for row in guard.EXCLUDED])
def test_forbidden_path_fails_even_with_small_bytes_and_before_release_base(repo, path):
    write(repo, path, b"small")
    git(repo, "add", "--", path)
    assert cli(repo)[0] == 1
    commit(repo)
    git(repo, "rm", "--", path)
    commit(repo)
    git(repo, "tag", "v3.4.0")
    commit(repo)
    code, report = cli(repo, "release")
    assert code == 1 and report["base_tag"] == "v3.4.0"
    assert any(row["reason"] == "forbidden historical path" for row in report["violations"])
    assert cli(repo)[0] == 1


@pytest.mark.parametrize("oid", [row[1] for row in guard.EXCLUDED])
def test_forbidden_object_is_rejected_at_any_path_and_any_reachable_epoch(repo, oid):
    # The fixed deny identities are exercised without copying or retrieving archives.
    # Fresh publication clones intentionally lack these objects: synthetic metadata
    # exercises the identity branch there; producer repositories also test real Git.
    if git(PROJECT_ROOT, "cat-file", "-e", oid, ok=False).returncode != 0:
        errors, used = guard.inspect_occurrences({("alias.bin", oid)}, {oid: ("blob", 1)}, set())
        assert errors[0]["reason"] == "forbidden attachment" and not used
        return
    borrow_objects(repo)
    stage_existing(repo, "alias.bin", oid)
    assert cli(repo)[0] == 1
    commit(repo)
    git(repo, "update-index", "--force-remove", "alias.bin")
    commit(repo)
    git(repo, "tag", "v3.4.0")
    commit(repo)
    code, report = cli(repo, "release")
    assert code == 1 and any(row["reason"] == "forbidden reachable object" for row in report["violations"])


def test_missing_tag_unresolvable_candidate_and_policy_refuse(repo):
    commit(repo)
    assert cli(repo, "release", "--base", "v0.0.0")[0] == 2
    assert cli(repo, "release", "--candidate", "missing-ref")[0] == 2
    git(repo, "tag", "-d", "v3.3.0")
    assert cli(repo, "release")[0] == 2
    git(repo, "rm", POLICY_PATH)
    assert cli(repo)[0] == 2


def test_shallow_clone_refuses(repo, tmp_path):
    commit(repo)
    clone = tmp_path / "shallow"
    git(tmp_path, "clone", "--depth=1", "--no-local", repo.as_uri(), str(clone))
    assert cli(clone)[0] == cli(clone, "release")[0] == 2


def test_missing_reachable_object_refuses(repo):
    oid = stage_blob(repo, "lost.bin", 1024)
    commit(repo)
    git(repo, "rm", "lost.bin")
    commit(repo)
    # Delete only the known fixture object inside this temporary repository.
    obj = repo / ".git/objects" / oid[:2] / oid[2:]
    obj.chmod(stat.S_IWRITE | stat.S_IREAD)
    obj.unlink()
    assert cli(repo, "release")[0] == 2


def test_unmerged_index_refuses(repo):
    oid = git(repo, "hash-object", "-w", "--stdin", data=b"conflict").decode().strip()
    git(repo, "update-index", "--index-info", data=f"100644 {oid} 1\tconflict.bin\n".encode())
    assert cli(repo)[0] == 2


def test_first_commit_index_and_forbidden_gitlink_paths(repo, tmp_path):
    unborn = tmp_path / "unborn"
    unborn.mkdir()
    git(unborn, "init", "-b", "main")
    write(unborn, POLICY_PATH, POLICY)
    git(unborn, "add", POLICY_PATH)
    assert cli(unborn)[0] == 0
    path = guard.EXCLUDED[0][0]
    oid = git(repo, "rev-parse", "HEAD").decode().strip()
    git(repo, "update-index", "--add", "--cacheinfo", "160000", oid, path)
    code, report = cli(repo)
    assert code == 1 and any(row["reason"] == "forbidden index path" for row in report["violations"])
    commit(repo)
    git(repo, "update-index", "--force-remove", path)
    commit(repo)
    assert cli(repo, "release")[0] == 1


def test_actual_repository_release_history_obeys_policy():
    code, report = cli(PROJECT_ROOT, "release", "--base", "v3.3.0")
    assert code == 0, report
    assert {row["oid"] for row in report["grandfathered"]} == {row[1] for row in guard.GRANDFATHERED}
