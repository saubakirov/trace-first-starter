# Upstream maintainer tools

This directory belongs to the upstream repository. Receiver projects do not inherit its
Python, Git-history, pytest, or MkDocs requirements.

- `tfw_state.py` provides optional, side-effect-free state readers.
- `tfw_doctor.py` provides optional read-only diagnostics and never repairs files.
- `migrations/2.0.0/` is the pinned pre-2.0 board-conversion bundle.
- `check_git_blob_sizes.py` is the CI/release guard for oversized Git objects.

## Retained verification

The permanent pytest surface is deliberately limited to:

- `docs/scripts/test_gen_docs.py`: documentation-generator behavior;
- `docs/scripts/test_integration.py`: one MkDocs build and checks of the rendered site;
- `tools/tests/test_git_blob_sizes.py`: one cheap in-memory check of the 5 MiB boundary.

Install and run it only when those surfaces changed:

```bash
python -m pip install -r tools/requirements.txt -r docs/requirements.txt
python -m pytest docs/scripts/test_gen_docs.py docs/scripts/test_integration.py tools/tests/test_git_blob_sizes.py -q
```

GitHub Actions directly gates deployment with the blob guard and `mkdocs build`; it does not
run the pytest suite.

## Optional inspection

```bash
python tools/tfw_doctor.py --root . status
python tools/tfw_doctor.py --root . check tasks --format json
python tools/tfw_doctor.py --root . check project
python tools/tfw_doctor.py --root . knowledge-pending --format json
```

These reports are disposable projections. Task-local carriers remain authoritative.

## Git-blob size policy

The limit is 5 MiB (5,242,880 bytes). A blob exactly at the limit passes; a larger blob
fails.

```bash
python tools/check_git_blob_sizes.py staged
python tools/check_git_blob_sizes.py release --candidate HEAD
```

`staged` checks only staged additions and modifications. `release` selects the latest
reachable stable `vX.Y.Z` tag that is a proper ancestor and checks only changes in
`tag..Candidate`, including intermediate commits and merged branches. It does not rescan
the whole reachable repository history. Use `--base vX.Y.Z` to select another stable
ancestor explicitly.

Incomplete history, a missing base tag, or unreadable Git objects refuse with exit 2.
Oversized blobs return 1; a complete pass returns 0.
