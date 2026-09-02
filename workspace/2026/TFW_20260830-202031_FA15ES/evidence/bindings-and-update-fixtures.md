# Bindings and update fixtures — TFW_20260830-202031_FA15ES

> Date: 2026-09-02
> Fixture root: `E:\TEMP\tfw-fa15es-final-626d77b-qa`
> Runner: `evidence/attachments/run_fixtures.py`
> Structured result: `evidence/attachments/fixture-results.json`

All scenarios use synthetic identifiers and sentinels under the fixture root. The executor did not read or write the machine's actual Full, Assisted, or legacy binding stores.

## Namespace contract

| Store | Contract | Observed fixture behavior |
|---|---|---|
| Assisted Windows | `%LOCALAPPDATA%\tfw\assisted\bindings.yml` | isolated child namespace; only a gated current-project entry may change |
| Assisted POSIX | `~/.tfw/assisted/bindings.yml` | same schema and gates; documented alternative only |
| Full | its independent `bindings.yaml` | sentinel hash unchanged in every scenario; never imported or rewritten |
| legacy Assisted | `tfw-assisted/bindings.yml` | sentinel hash unchanged; preserved and ignored, never a fallback |

## Binding-state matrix

| Scenario | Expected gate/write boundary | Observed result |
|---|---|---|
| missing | ask once; after human choice create only the current-project canonical entry | one human gate; canonical entry created |
| valid fixed | select existing participant without a write | existing selection returned; file hash unchanged |
| ask mode | ask one human question each human session | one question; file hash unchanged |
| disagreement | stop at human gate; reserve and change only the current project | only current-project entry changed under reservation |
| malformed | do not repair or guess | session-only attribution; no file write |
| foreign lock | do not break another writer's reservation | session-only attribution; foreign lock preserved |
| shared device | never infer the next human from the previous session | one question in each new human session |
| autonomous role | skip local participant selection | task owner inherited from trace; local bindings untouched |

Every scenario rehashed the Full and legacy sentinels after the Assisted operation. Unexpected Full/legacy changes: **0**.

## Provider-neutral acquisition matrix

| Capability shape | Observation | Result |
|---|---|---|
| local exact directory | safe closed tree, 24-file manifest, immediate recheck | PASS |
| Drive-like immutable object | same closed-tree contract independent of transport | PASS |
| GitHub-like exact commit/object | same closed-tree contract independent of transport | PASS |
| safe archive | 24 safe members; archive SHA-256 `0333dff31a741e18e9da0b90c7ee441b1edd41d4eecde4a7258613307cc8aa2d` | PASS |
| same-version drift | changed source byte detected before target write | STOP / new Gate |
| unsafe archive path | parent-escape member rejected before extraction | STOP |
| occupied target | collision detected before write | STOP |
| reverse promotion | one generic candidate emitted | public core byte-identical |

No provider API, credential, URL token, or vendor-specific runtime is part of the product contract. A provider may supply stronger origin/immutability evidence, but a local same-package hash is described only as observed integrity.

## Protected-state fixture

The installed-project fixture protected `workspace/`, `team/`, and `knowledge/` with pre/post manifests. After the simulated service-set update, all three protected manifests were byte-identical. The package itself carried no `workspace/`, participant profile, project UUID, local binding, lock, or task evidence.

## Reproduction

```powershell
$env:TFW_FA15ES_FIXTURE_ROOT = '<new empty temporary directory>'
python workspace/2026/TFW_20260830-202031_FA15ES/evidence/attachments/run_fixtures.py
```

The target must not already exist. Expected terminal line: `FIXTURE_VERDICT=PASS`.

Fixture cleanup policy: the final fixture root is intentionally retained through independent review so the Reviewer can inspect or rerun it; it may be deleted after review acceptance. Earlier executor-only fixture roots are disposable and are not evidence authorities.
