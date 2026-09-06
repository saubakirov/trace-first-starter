# Upstream maintainer tools

This directory belongs to the upstream repository, not to the copied `.tfw/` Full payload
or `editions/02-assisted/`. Its Python and PyYAML requirement is therefore not a receiver
prerequisite and none of these commands is an ordinary lifecycle or build gate.

- `tfw_state.py` provides side-effect-free semantic readers used by upstream tests and
  diagnostics. Task-local carriers remain authoritative.
- `tfw_doctor.py` is a bounded, read-only diagnostic with exactly `status`, `check tasks`,
  `check project`, and `knowledge-pending`. It never repairs files. Exit `0` is a complete
  clean scoped read, `1` reports determinate structural findings, and `2` reports incomplete
  or indeterminate input. Advice and compatibility notes are exit-neutral.
- `migrations/2.0.0/` is the self-contained recovery bundle for the pre-2.0 board conversion.

Prepare an isolated maintainer environment, then run the suite:

```bash
python -m venv .venv
python -m pip install -r tools/requirements.txt
python -m pytest tools/tests/ docs/scripts/ -q
```

Examples of optional read-only inspection:

```bash
python tools/tfw_doctor.py --root . status
python tools/tfw_doctor.py --root . check tasks --format json
python tools/tfw_doctor.py --root . check project
python tools/tfw_doctor.py --root . knowledge-pending --format json
```

These reports are disposable projections. They do not replace `status.md`, journals, task
artifacts, or the tool-independent Knowledge Gate in `.tfw/workflows/knowledge.md`.
