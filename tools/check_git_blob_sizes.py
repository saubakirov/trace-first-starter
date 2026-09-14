#!/usr/bin/env python3
"""Enforce the upstream repository's 10 MiB Git-blob policy (stdlib and Git only).

The index or Candidate supplies policy bytes. Release checks inspect every parent
edge in the selected range, plus forbidden identities throughout reachable history.
Exit 0: complete PASS; 1: policy violation; 2: invalid/incomplete input.
"""

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys

LIMIT = 10485760
POLICY_PATH = "tools/git_blob_size_policy.json"
PREFIX = "workspace/2026/TFW_20260909-231654_TKL/"
SOURCE_CARRIER = "56a872c3377c62aa453d1f221ba745719c5739a1"
# Owner-approved pre-policy identities. Changing the policy cannot broaden these.
GRANDFATHERED = (
    (PREFIX + "evidence/capture-final/06-stopped-build-output.zip", "5f7b427cf8f16a8df20c95d1239217a5a8d26881", 34977746),
    (PREFIX + "evidence/r1-ac7/03-baseline-physical.zip", "ae2e294b0e8e16fda99f76e01853a510c7fc5057", 31225273),
    (PREFIX + "evidence/r1-ac8/03-input/source-before.zip", "6032a97cc4289a61bd9af7a2b0d60457974b83ff", 18722824),
    (PREFIX + "evidence/r1-return/full-diff-check.stdout.raw", "14aa41a84395a47b4071a1440f37d18f35f56404", 57216329),
    (PREFIX + "evidence/r2-native/06-partial-physical.zip", "02a544a9275fabb7524e993bc88a4c0501d35b32", 31840944),
)
EXCLUDED = (
    (PREFIX + "evidence/r3-native/07-candidate.tar", "981e37313353637b594e8a36240ba80317cd2238", 216791040),
    (PREFIX + "evidence/r3-native/18-final-physical.zip", "6cbf1d29369eb3579e8a6543d4858f2e5267a42b", 178325428),
)
DENIED_PATHS = {row[0] for row in EXCLUDED}
DENIED_OIDS = {row[1] for row in EXCLUDED}
TAG = re.compile(r"v(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\Z")


class Refusal(Exception):
    """A complete, authoritative result cannot be produced."""


class Git:
    def __init__(self, root):
        self.root = root
        self.env = dict(os.environ, GIT_NO_LAZY_FETCH="1", GIT_NO_REPLACE_OBJECTS="1",
                        GIT_TERMINAL_PROMPT="0")

    def run(self, *args, data=None, allowed=(0,)):
        result = subprocess.run(
            ["git", "-c", "core.longpaths=true", "-c", "core.autocrlf=false", *args],
            cwd=self.root, env=self.env, input=data, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, check=False)
        if result.returncode not in allowed:
            detail = result.stderr.decode("utf-8", "replace").strip()
            raise Refusal(f"git {args[0]} failed ({result.returncode}): {detail}")
        return result

    def out(self, *args, data=None):
        return self.run(*args, data=data).stdout

    def commit(self, ref):
        return self.out("rev-parse", "--verify", "--end-of-options", ref + "^{commit}").decode("ascii").strip()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise Refusal(f"duplicate policy key: {key}")
        result[key] = value
    return result


def fields(value, expected):
    if not isinstance(value, dict) or set(value) != set(expected):
        raise Refusal("policy fields do not match the fixed schema")


def read_policy(raw):
    try:
        policy = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_object)
    except (ValueError, UnicodeError) as error:
        raise Refusal(f"invalid policy JSON: {error}") from error
    fields(policy, ("schema_version", "max_blob_bytes", "grandfathered", "excluded_attachments"))
    if type(policy["schema_version"]) is not int or policy["schema_version"] != 1:
        raise Refusal("unsupported policy schema")
    if type(policy["max_blob_bytes"]) is not int or policy["max_blob_bytes"] != LIMIT:
        raise Refusal("the blob limit must be exactly 10485760 bytes")
    for key, identities, extra in (
        ("grandfathered", GRANDFATHERED, ("rationale", "follow_up")),
        ("excluded_attachments", EXCLUDED, ("source_carrier", "owner_disposition")),
    ):
        records = policy[key]
        if not isinstance(records, list) or len(records) != len(identities):
            raise Refusal(f"{key} must contain exactly {len(identities)} records")
        actual = []
        for row in records:
            fields(row, ("path", "oid", "bytes", *extra))
            if (not isinstance(row["path"], str) or not isinstance(row["oid"], str)
                    or type(row["bytes"]) is not int
                    or any(not isinstance(row[k], str) or not row[k].strip() for k in extra)):
                raise Refusal(f"invalid {key} record")
            if key == "excluded_attachments" and row["source_carrier"] != SOURCE_CARRIER:
                raise Refusal("excluded attachment provenance changed")
            actual.append((row["path"], row["oid"], row["bytes"]))
        if len(set(actual)) != len(actual) or set(actual) != set(identities):
            raise Refusal(f"{key} identities differ from the owner-approved exact set")
    return set(GRANDFATHERED)


def object_metadata(git, oids):
    ordered = sorted(set(oids))
    if not ordered:
        return {}
    raw = git.out("cat-file", "--batch-check=%(objectname) %(objecttype) %(objectsize)",
                  data=("\n".join(ordered) + "\n").encode("ascii"))
    rows = raw.decode("ascii").splitlines()
    if len(rows) != len(ordered):
        raise Refusal("incomplete object metadata")
    result = {}
    for expected, line in zip(ordered, rows):
        parts = line.split()
        if len(parts) != 3 or parts[0] != expected or not parts[2].isdigit():
            raise Refusal(f"missing or unreadable object: {expected}")
        result[expected] = (parts[1], int(parts[2]))
    return result


def history_occurrences(git, revision, include_old=False, keep_gitlinks=False):
    # -m exposes every merge parent; --no-renames preserves the actual target path.
    # Only raw headers are stripped. Paths may contain whitespace or newlines.
    raw = git.out("log", "--format=", "--raw", "--root", "-m", "--full-history",
                  "--no-renames", "--no-abbrev", "-z", revision, "--")
    tokens = raw.split(b"\0")
    result = set()
    index = 0
    while index < len(tokens):
        header = tokens[index].strip(b"\n")
        index += 1
        if not header:
            continue
        if not re.fullmatch(rb":[0-7]{6} [0-7]{6} [0-9a-f]{40,64} [0-9a-f]{40,64} [AMDTUXB]", header):
            raise Refusal("unexpected Git raw history record")
        if index >= len(tokens) or not tokens[index]:
            raise Refusal("missing Git raw history path")
        path = tokens[index].decode("utf-8", "surrogateescape")
        index += 1
        old_mode, new_mode, old_oid, new_oid, status = header[1:].split()
        pairs = ((old_mode, old_oid), (new_mode, new_oid)) if include_old else ((new_mode, new_oid),)
        for mode, oid in pairs:
            if mode != b"000000" and (keep_gitlinks or mode != b"160000"):
                result.add((path, oid.decode("ascii")))
    return result


def reachable(git, candidate):
    oids = git.out("rev-list", "--objects", "--no-object-names", candidate, "--").decode("ascii").splitlines()
    metadata = object_metadata(git, oids)
    occurrences = history_occurrences(git, candidate, include_old=True, keep_gitlinks=True)
    violations = []
    for oid in sorted(DENIED_OIDS & metadata.keys()):
        violations.append({"reason": "forbidden reachable object", "oid": oid, "bytes": metadata[oid][1]})
    for path, oid in sorted(occurrences):
        if path in DENIED_PATHS:
            violations.append({"reason": "forbidden historical path", "path": path, "oid": oid})
    return metadata, violations


def inspect_occurrences(occurrences, metadata, exceptions):
    violations = []
    used = set()
    for path, oid in sorted(occurrences):
        if oid not in metadata or metadata[oid][0] != "blob":
            raise Refusal(f"expected readable blob at {path!r}: {oid}")
        size = metadata[oid][1]
        identity = (path, oid, size)
        reason = None
        if path in DENIED_PATHS or oid in DENIED_OIDS:
            reason = "forbidden attachment"
        elif size > LIMIT:
            if identity in exceptions:
                used.add(identity)
            else:
                reason = "blob exceeds 10485760 bytes"
        if reason:
            violations.append({"reason": reason, "path": path, "oid": oid, "bytes": size})
    return violations, used


def base_tag(git, candidate, requested):
    tags = [requested] if requested else git.out("tag", "--list").decode("utf-8").splitlines()
    eligible = []
    for tag in tags:
        match = TAG.fullmatch(tag)
        if not match:
            if requested:
                raise Refusal("base must name an existing stable vX.Y.Z release tag")
            continue
        commit = git.commit("refs/tags/" + tag)
        if commit == candidate:
            if requested:
                raise Refusal("base tag must be a proper ancestor; a tag on Candidate cannot bypass the range")
            continue
        result = git.run("merge-base", "--is-ancestor", commit, candidate, allowed=(0, 1))
        if result.returncode == 0:
            eligible.append((tuple(map(int, match.groups())), tag, commit))
        elif requested:
            raise Refusal("base tag is not an ancestor of Candidate")
    if not eligible:
        raise Refusal("no reachable release tag on a proper ancestor; complete tagged history is required")
    _, tag, commit = max(eligible)
    return tag, commit


def check(root, mode, candidate="HEAD", base=None):
    git = Git(root)
    if git.out("rev-parse", "--is-shallow-repository").strip() != b"false":
        raise Refusal("shallow repository: full history is required")
    result = {"mode": mode, "limit_bytes": LIMIT}
    if mode == "staged":
        exceptions = read_policy(git.out("show", ":" + POLICY_PATH))
        occurrences = set()
        path_violations = []
        for row in git.out("ls-files", "--stage", "-z").split(b"\0"):
            if not row:
                continue
            header, path = row.split(b"\t", 1)
            file_mode, oid, stage = header.split()
            if stage != b"0":
                raise Refusal("unmerged index: resolve all stages before checking")
            decoded_path = path.decode("utf-8", "surrogateescape")
            if decoded_path in DENIED_PATHS:
                path_violations.append({"reason": "forbidden index path", "path": decoded_path,
                                        "oid": oid.decode("ascii")})
            if file_mode != b"160000":
                occurrences.add((decoded_path, oid.decode("ascii")))
        metadata = object_metadata(git, (oid for _, oid in occurrences))
        # An unborn repository has no reachable history; malformed HEAD still refuses.
        head = git.run("rev-parse", "--verify", "HEAD", allowed=(0, 128))
        if head.returncode == 0:
            _, violations = reachable(git, git.commit("HEAD"))
        elif git.out("symbolic-ref", "HEAD").strip() and git.run("show-ref", "--head", allowed=(0, 1)).returncode == 1:
            violations = []
        else:
            raise Refusal("unresolvable HEAD")
        violations.extend(path_violations)
    else:
        candidate = git.commit(candidate)
        exceptions = read_policy(git.out("show", candidate + ":" + POLICY_PATH))
        tag, start = base_tag(git, candidate, base)
        result.update(candidate=candidate, base_tag=tag, base_commit=start)
        metadata, violations = reachable(git, candidate)
        occurrences = history_occurrences(git, start + ".." + candidate)
    new_violations, used = inspect_occurrences(occurrences, metadata, exceptions)
    violations.extend(new_violations)
    # Deterministic JSON, including path aliases and paths containing whitespace.
    violations = sorted({json.dumps(row, sort_keys=True) for row in violations})
    result.update(status="FAIL" if violations else "PASS", checked_occurrences=len(occurrences),
                  grandfathered=[{"path": p, "oid": o, "bytes": s} for p, o, s in sorted(used)],
                  violations=[json.loads(row) for row in violations])
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    sub = parser.add_subparsers(dest="mode", required=True)
    sub.add_parser("staged", help="check actual index blobs and existing reachable history")
    release = sub.add_parser("release", help="check the entire release ancestry range")
    release.add_argument("--candidate", default="HEAD")
    release.add_argument("--base", help="stable release tag; default: highest reachable version before Candidate")
    args = parser.parse_args(argv)
    try:
        result = check(args.repo, args.mode, getattr(args, "candidate", "HEAD"), getattr(args, "base", None))
    except (Refusal, OSError, ValueError) as error:
        print(json.dumps({"status": "REFUSED", "reason": str(error)}, sort_keys=True))
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
