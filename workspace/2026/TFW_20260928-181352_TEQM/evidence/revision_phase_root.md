# Task economics — TFW_SAMPLE

<!-- tfw-economics-v1 {"calendar_elapsed_seconds":38768.0,"collector_operation_seconds":0.2,"cutoff":"2026-09-29T00:00:00+00:00","excluded":[],"failure_only":[],"incomplete":["2a6c656565290d446b946449f2f585a2c5447d1253a272d90cd2c74809e04d43","8ec62b034ddc860c6e85f1a59a4cf651fca7262b6a81ea39975f20a31ec121b3"],"keywords":["phase","root","cost"],"lifecycle":"ONB","measured":["phase-unit","root-unit"],"missing":[],"owner":"declared-owner","phase_coverage_gaps":["phase-b: no returned role bytes"],"phase_roots":["phase-a","phase-b"],"primary_area":"fixture","project":"steps-framework","rate_version":"2026-09-29","received":["phase-unit","root-unit"],"report_at":"2026-09-28T22:10:45.894790+00:00","schema_version":1,"source_diagnostics":[{"notes":[],"sha256":"2a6c656565290d446b946449f2f585a2c5447d1253a272d90cd2c74809e04d43","unit":"root-unit"},{"notes":[],"sha256":"8ec62b034ddc860c6e85f1a59a4cf651fca7262b6a81ea39975f20a31ec121b3","unit":"phase-unit"}],"status_timezone":"+05:00","task":"TFW_SAMPLE","totals":{"cached":0,"duration_seconds":{},"input":8,"output":4,"priced_usd":"0.000056","tokens":12,"undated_tokens":0,"unpriced_tokens":0},"unknown_collector_operations":0} -->

## Purpose, result and value

- Purpose: Measure this fixture
- Value sought: Verify phase selection
- Lifecycle at report: ONB
- Accepted result: not supplied at this cutoff; see RF/REVIEW before final close

## Resource summary

| Measure | Observed selected contribution |
|---|---:|
| Tokens, input + output | 12 |
| Input, including cache | 8 |
| Cached input subset | 0 |
| Output, including reasoning when source says so | 4 |
| API reference estimate on priced rows (USD) | 0.000056 |
| Unpriced tokens | 0 |
| Undated tokens, excluded from date filters | 0 |
| Collection operation, observed wall seconds | 0.200 (0 files unknown) |
| Task calendar elapsed, status clock | 38768.000 seconds |

Time kinds remain separate; task calendar elapsed is read from task control,
not inferred from summed roles. Parallel role times can overlap.


Money is a dated Standard API token equivalent, not a subscription bill.
Unknown models, tariff conditions, storage and tools are excluded.

## By role and model

### Role

| Role | Tokens | Priced USD |
|---|---:|---:|
| executor | 12 | 0.000056 |

### Model

| Model | Tokens | Priced USD |
|---|---:|---:|
| gpt-6-sol | 12 | 0.000056 |

### Consumption date

| Date | Tokens | Priced USD |
|---|---:|---:|
| 2026-09-28 | 7 | 0.00003 |
| 2026-10-02 | 5 | 0.000026 |

## Coverage and provenance

- Expected units: root-unit, phase-unit
- Received units: phase-unit, root-unit
- Measured units: phase-unit, root-unit
- Missing units: none among declared expected
- Failure-only units: none
- Selected phase leaves: phase-a, phase-b
- Phase coverage gaps: phase-b: no returned role bytes
- Incomplete source captures: 2 (a finite snapshot is not full task coverage).
- Excluded conflicting/superseded files: 0
- Capture cutoff: 2026-09-29T00:00:00+00:00
- Finite tail: later report delivery, final message and cleanup are outside this cutoff.
- Rate card: 2026-09-29; USD per million text tokens, first-party Standard API reference; short context for OpenAI, no subscription allocation or tools

- root-unit: codex.rollout / root-source revision 1, range [0, 5), complete False, 1286 bytes, SHA-256 2a6c656565290d446b946449f2f585a2c5447d1253a272d90cd2c74809e04d43, source aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.
- phase-unit: codex.rollout / phase-source revision 1, range [0, 5), complete False, 1293 bytes, SHA-256 8ec62b034ddc860c6e85f1a59a4cf651fca7262b6a81ea39975f20a31ec121b3, source aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.
