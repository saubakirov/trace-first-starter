# Receiver project check set — TFW_20260906-190312_CRUE

This is the project-check contract for the approved field matrix. It is separate from the native
containment preflight (UID, HOME/TMPDIR, auth JSON, source reachability and read-only proof).
Commands are discovered from each sanitized receiver's `.tfw/project_config.yaml` and may be run only
as safe local checks inside that receiver copy. A command that cannot run is recorded as unavailable;
no dependency installation, external fetch, cloud, database, Kubernetes, incident, production or
deployment command is substituted.

## AFD

Observed `.tfw/project_config.yaml` build commands:

```text
./gradlew assemble --console=plain
./gradlew test --console=plain
./gradlew build --console=plain
```

These are local Gradle checks. The updater may run them when its target workflow selects the configured
check subjects and the required local wrapper/dependencies are available. Missing wrapper, runtime or
dependency is an unavailable check, not a PASS and not a reason to fetch or install anything.

## helpdesk

Observed project checks:

```text
make lint
make test-unit
python .tfw/scripts/gen_index.py --check tasks
```

The first two are local Make targets. The third is the documented manual task-state check; the config
records a known immutable historical violation in the copied task history. Its observed result must be
reported as that actual failure/limitation, never as a new migration defect or a passing build gate.

## Atamat

Observed project checks:

```text
python .tfw/scripts/gen_index.py --check tasks
```

The configured `lint` and `test` values are `echo "configure your lint command"` and
`echo "configure your test command"`. They are placeholders and must not be reported as verification
success. The real task-state check may run locally; any existing failure is recorded honestly.

## Common local observations

The updater's field report must distinguish these project checks from the common observations that are
safe and required for evidence: `.tfw/VERSION`, `.tfw/project_config.yaml` provenance/build section,
the pinned `.tfw/.upstream` Git identity, `git status --porcelain=v1`, `git diff --stat`, and the
append-only receipt/preservation paths selected by the workflow. Paths and diff metadata may be
retained; credentials, raw HTTP/TLS/debug bodies, account identifiers and secret file contents may not.

## Unavailable-check policy

Cloud/Yandex, Kubernetes, PostgreSQL, ClickHouse, Redis, production services, deployment scripts,
incident commands, external upstream fetches, and checks requiring credentials beyond the minimum
provider auth are unavailable by policy in this campaign. A missing local executable, missing dependency,
placeholder command, timeout, refusal or pre-existing failure is reported with its exact command and
state. The agent must not convert unavailable or stopped checks into success.
