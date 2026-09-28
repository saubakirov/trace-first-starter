# Task economics — TFW_20260928-181352_TEQM

<!-- tfw-economics-v1 {"calendar_elapsed_seconds":30408.262894,"collector_operation_seconds":0.307434,"cutoff":"2026-09-28T21:40:40.262894+00:00","excluded":[],"failure_only":[],"incomplete":["a5f42644c0cd185bb70c093787d9b1c8741b300894d26ffd3fd2f4896961e6e1","eaf560cb0c592b440eb6821e7302aa93717ff378604dd472eb7ea96a618a0eb0","ef80eb0f7221c4f75f0b161e843cc685a115c781aab2ef6fd6a0e963b7907db5"],"keywords":[],"lifecycle":"ONB","measured":["codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793","codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243","codex:thread:local:01a0e9c4-e45c-7940-8515-fd083f4a7886"],"missing":[],"owner":"saubakirov","phase_coverage_gaps":[],"phase_roots":[],"primary_area":null,"project":"steps-framework","rate_version":"2026-09-29","received":["codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793","codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243","codex:thread:local:01a0e9c4-e45c-7940-8515-fd083f4a7886"],"report_at":"2026-09-28T22:17:10.278425+00:00","schema_version":1,"source_diagnostics":[{"notes":["unmatched task_started: 1","compacted 481 verified native rows into 6 daily/run/model records"],"sha256":"a5f42644c0cd185bb70c093787d9b1c8741b300894d26ffd3fd2f4896961e6e1","source_qualification":{"tfw.adaptation_reason":"Delivered reader succeeded but its cumulative token_count view omitted usage visible in the same verified prefix; bounded own-source extraction, shared schema/validator/rates unchanged","tfw.alternate_token_count_total":62902737,"tfw.counter_difference_tokens":1502301,"tfw.native_stream":"token_usage_record.usage deduplicated by response_id; per-response sum equals final thread_token_usage"},"unit":"codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793"},{"notes":[],"sha256":"eaf560cb0c592b440eb6821e7302aa93717ff378604dd472eb7ea96a618a0eb0","source_qualification":{},"unit":"codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243"},{"notes":["unmatched task_started: 1","compacted 203 verified native rows into 1 daily/run/model records"],"sha256":"ef80eb0f7221c4f75f0b161e843cc685a115c781aab2ef6fd6a0e963b7907db5","source_qualification":{},"unit":"codex:thread:local:01a0e9c4-e45c-7940-8515-fd083f4a7886"}],"status_timezone":"+05:00","task":"TFW_20260928-181352_TEQM","totals":{"cached":117745408,"duration_seconds":{"completed_turn":14959.275},"input":120933691,"output":618847,"priced_usd":"101.6157816","tokens":121552538,"undated_tokens":0,"unpriced_tokens":0},"unknown_collector_operations":0} -->

## Purpose, result and value

- Purpose: Measure tokens, time, quality, and attributable cost for TFW work across roles and product areas.
- Value sought: Enable evidence-based decisions about team practice, TFW releases, and coordination modes.
- Lifecycle at report: ONB
- Accepted result: not supplied at this cutoff; see RF/REVIEW before final close

## Resource summary

| Measure | Observed selected contribution |
|---|---:|
| Tokens, input + output | 121,552,538 |
| Input, including cache | 120,933,691 |
| Cached input subset | 117,745,408 |
| Output, including reasoning when source says so | 618,847 |
| API reference estimate on priced rows (USD) | 101.6157816 |
| Unpriced tokens | 0 |
| Undated tokens, excluded from date filters | 0 |
| Collection operation, observed wall seconds | 0.307 (0 files unknown) |
| Task calendar elapsed, status clock | 30408.263 seconds |

Time kinds remain separate; task calendar elapsed is read from task control,
not inferred from summed roles. Parallel role times can overlap.

- completed_turn: 14959.275 observed seconds

Money is a dated Standard API token equivalent, not a subscription bill.
Unknown models, tariff conditions, storage and tools are excluded.

## By role and model

### Role

| Role | Tokens | Priced USD |
|---|---:|---:|
| coordinator | 64,405,038 | 86.349740 |
| Researcher | 28,923,212 | 7.8227232 |
| executor | 28,224,288 | 7.4433184 |

### Model

| Model | Tokens | Priced USD |
|---|---:|---:|
| gpt-6-sol | 73,637,546 | 19.7387016 |
| gpt-6-astra | 47,914,992 | 81.877080 |

### Consumption date

| Date | Tokens | Priced USD |
|---|---:|---:|
| 2026-09-28 | 67,916,523 | 50.3078892 |
| 2026-09-29 | 53,636,015 | 51.3078924 |

## Coverage and provenance

- Expected units: codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793, codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243, codex:thread:local:01a0e9c4-e45c-7940-8515-fd083f4a7886
- Received units: codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793, codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243, codex:thread:local:01a0e9c4-e45c-7940-8515-fd083f4a7886
- Measured units: codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793, codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243, codex:thread:local:01a0e9c4-e45c-7940-8515-fd083f4a7886
- Missing units: none among declared expected
- Failure-only units: none
- Selected phase leaves: none
- Phase coverage gaps: none
- Incomplete source captures: 3 (a finite snapshot is not full task coverage).
- Excluded conflicting/superseded files: 0
- Capture cutoff: 2026-09-28T21:40:40.262894+00:00
- Finite tail: later report delivery, final message and cleanup are outside this cutoff.
- Rate card: 2026-09-29; USD per million text tokens, first-party Standard API reference; short context for OpenAI, no subscription allocation or tools

- codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793: codex.rollout / 01a0e7f5-7791-7ad0-99ff-30068c11b793 revision 1, range [0, 3841), complete False, 5713 bytes, SHA-256 a5f42644c0cd185bb70c093787d9b1c8741b300894d26ffd3fd2f4896961e6e1, source 9c28cb91907a15674fbac6e2f6a0b78d644baa477bc8f275d4e476d6ccb29a7b.
- Source diagnostic codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793: unmatched task_started: 1
- Source diagnostic codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793: compacted 481 verified native rows into 6 daily/run/model records
- Source qualification codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793 / tfw.native_stream: token_usage_record.usage deduplicated by response_id; per-response sum equals final thread_token_usage.
- Source qualification codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793 / tfw.adaptation_reason: Delivered reader succeeded but its cumulative token_count view omitted usage visible in the same verified prefix; bounded own-source extraction, shared schema/validator/rates unchanged.
- Source qualification codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793 / tfw.alternate_token_count_total: 62902737.
- Source qualification codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793 / tfw.counter_difference_tokens: 1502301.
- codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243: codex.rollout / 01a0e903-fa15-7e62-8032-956fdd7b7243 revision 1, range [0, 1858), complete False, 4208 bytes, SHA-256 eaf560cb0c592b440eb6821e7302aa93717ff378604dd472eb7ea96a618a0eb0, source 2c0169a5743948ca29fc623aa0487b77b6d7e98d3e0de17981dfa4f8283d45e5.
- codex:thread:local:01a0e9c4-e45c-7940-8515-fd083f4a7886: codex.rollout / 01a0e9c4-e45c-7940-8515-fd083f4a7886 revision 1, range [0, 1509), complete False, 1774 bytes, SHA-256 ef80eb0f7221c4f75f0b161e843cc685a115c781aab2ef6fd6a0e963b7907db5, source a9d9edb912aa432ec8046e11fb371db754a2c25f19ed56fe4dde59fbaeb18f39.
- Source diagnostic codex:thread:local:01a0e9c4-e45c-7940-8515-fd083f4a7886: unmatched task_started: 1
- Source diagnostic codex:thread:local:01a0e9c4-e45c-7940-8515-fd083f4a7886: compacted 203 verified native rows into 1 daily/run/model records
