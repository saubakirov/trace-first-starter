#!/usr/bin/env python3
"""Reject Git blobs larger than 5 MiB in staged or post-release-tag changes."""

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys

LIMIT = 5 * 1024 * 1024
TAG = re.compile(r"v(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\Z")


class Refusal(Exception):
    """The requested range cannot be checked completely."""


class Git:
    def __init__(self, root):
        self.root = root
        self.env = dict(
            os.environ,
            GIT_NO_LAZY_FETCH="1",
            GIT_NO_REPLACE_OBJECTS="1",
            GIT_TERMINAL_PROMPT="0",
        )

    def run(self, *args, data=None, allowed=(0,)):
        result = subprocess.run(
            ["git", "-c", "core.longpaths=true", "-c", "core.autocrlf=false", *args],
            cwd=self.root,
            env=self.env,
            input=data,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if result.returncode not in allowed:
            detail = result.stderr.decode("utf-8", "replace").strip()
            raise Refusal(f"git {args[0]} failed ({result.returncode}): {detail}")
        return result

    def out(self, *args, data=None):
        return self.run(*args, data=data).stdout

    def commit(self, ref):
        return self.out(
            "rev-parse", "--verify", "--end-of-options", ref + "^{commit}"
        ).decode("ascii").strip()


def changed_blobs(raw):
    """Return (path, new object id) pairs from NUL-delimited Git raw output."""
    tokens = raw.split(b"\0")
    result = set()
    index = 0
    while index < len(tokens):
        header = tokens[index].strip(b"\n")
        index += 1
        if not header:
            continue
        if not re.fullmatch(
            rb":[0-7]{6} [0-7]{6} [0-9a-f]{40,64} [0-9a-f]{40,64} [AMDTUXB]",
            header,
        ):
            raise Refusal("unexpected Git raw change record")
        if index >= len(tokens) or not tokens[index]:
            raise Refusal("missing Git raw change path")
        path = tokens[index].decode("utf-8", "surrogateescape")
        index += 1
        _, new_mode, _, new_oid, _ = header[1:].split()
        if new_mode not in (b"000000", b"160000"):
            result.add((path, new_oid.decode("ascii")))
    return result


def object_metadata(git, occurrences):
    oids = sorted({oid for _, oid in occurrences})
    if not oids:
        return {}
    raw = git.out(
        "cat-file",
        "--batch-check=%(objectname) %(objecttype) %(objectsize)",
        data=("\n".join(oids) + "\n").encode("ascii"),
    )
    rows = raw.decode("ascii").splitlines()
    if len(rows) != len(oids):
        raise Refusal("incomplete object metadata")
    metadata = {}
    for expected, line in zip(oids, rows):
        parts = line.split()
        if len(parts) != 3 or parts[0] != expected or not parts[2].isdigit():
            raise Refusal(f"missing or unreadable object: {expected}")
        metadata[expected] = (parts[1], int(parts[2]))
    return metadata


def inspect_occurrences(occurrences, metadata):
    violations = []
    for path, oid in sorted(occurrences):
        if oid not in metadata or metadata[oid][0] != "blob":
            raise Refusal(f"expected readable blob at {path!r}: {oid}")
        size = metadata[oid][1]
        if size > LIMIT:
            violations.append(
                {
                    "reason": f"blob exceeds {LIMIT} bytes",
                    "path": path,
                    "oid": oid,
                    "bytes": size,
                }
            )
    return violations


def base_tag(git, candidate, requested):
    tags = [requested] if requested else git.out("tag", "--list").decode("utf-8").splitlines()
    eligible = []
    for tag in tags:
        match = TAG.fullmatch(tag or "")
        if not match:
            if requested:
                raise Refusal("base must name a stable vX.Y.Z release tag")
            continue
        commit = git.commit("refs/tags/" + tag)
        if commit == candidate:
            if requested:
                raise Refusal("base tag must be a proper ancestor")
            continue
        result = git.run("merge-base", "--is-ancestor", commit, candidate, allowed=(0, 1))
        if result.returncode == 0:
            eligible.append((tuple(map(int, match.groups())), tag, commit))
        elif requested:
            raise Refusal("base tag is not an ancestor of Candidate")
    if not eligible:
        raise Refusal("no stable release tag on a proper ancestor")
    _, tag, commit = max(eligible)
    return tag, commit


def check(root, mode, candidate="HEAD", base=None):
    git = Git(root)
    result = {"mode": mode, "limit_bytes": LIMIT}
    if mode == "staged":
        raw = git.out("diff", "--cached", "--raw", "--no-renames", "--no-abbrev", "-z", "--")
    else:
        if git.out("rev-parse", "--is-shallow-repository").strip() != b"false":
            raise Refusal("shallow repository: the release range is incomplete")
        candidate = git.commit(candidate)
        tag, start = base_tag(git, candidate, base)
        result.update(candidate=candidate, base_tag=tag, base_commit=start)
        raw = git.out(
            "log",
            "--format=",
            "--raw",
            "-m",
            "--full-history",
            "--no-renames",
            "--no-abbrev",
            "-z",
            start + ".." + candidate,
            "--",
        )
    occurrences = changed_blobs(raw)
    violations = inspect_occurrences(occurrences, object_metadata(git, occurrences))
    result.update(
        status="FAIL" if violations else "PASS",
        checked_occurrences=len(occurrences),
        violations=violations,
    )
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    sub = parser.add_subparsers(dest="mode", required=True)
    sub.add_parser("staged", help="check staged additions and modifications")
    release = sub.add_parser("release", help="check changes since the latest reachable stable tag")
    release.add_argument("--candidate", default="HEAD")
    release.add_argument("--base", help="use this stable ancestor tag instead")
    args = parser.parse_args(argv)
    try:
        result = check(
            args.repo,
            args.mode,
            getattr(args, "candidate", "HEAD"),
            getattr(args, "base", None),
        )
    except (Refusal, OSError, ValueError) as error:
        print(json.dumps({"status": "REFUSED", "reason": str(error)}, sort_keys=True))
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
