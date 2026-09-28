# Task economics — TFW_20260928-181352_TEQM

<!-- tfw-economics-v1 {"calendar_elapsed_seconds":30408.262894,"collector_operation_seconds":0.232565,"cutoff":"2026-09-28T21:40:40.262894+00:00","excluded":[],"failure_only":[],"incomplete":["a5f42644c0cd185bb70c093787d9b1c8741b300894d26ffd3fd2f4896961e6e1","ef80eb0f7221c4f75f0b161e843cc685a115c781aab2ef6fd6a0e963b7907db5"],"keywords":["token-accounting","task-reports","product-costs","distributed-role-returns"],"lifecycle":"RF","measured":["codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793","codex:thread:local:01a0e9c4-e45c-7940-8515-fd083f4a7886"],"missing":["codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243","codex:thread:local:01a0e9f5-538c-7152-b704-b7f4b7e41784"],"owner":"saubakirov","primary_area":"task-economics","project":"steps-framework","rate_version":"2026-09-29","received":["codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793","codex:thread:local:01a0e9c4-e45c-7940-8515-fd083f4a7886"],"report_at":"2026-09-28T21:45:33.395749+00:00","schema_version":1,"status_timezone":"+05:00","task":"TFW_20260928-181352_TEQM","totals":{"cached":89439232,"duration_seconds":{"completed_turn":11408.016},"input":92126406,"output":502920,"priced_usd":"93.7930584","tokens":92629326,"undated_tokens":0,"unpriced_tokens":0},"unknown_collector_operations":0} -->

## Purpose, result and value

- Purpose: Measure tokens, time, quality, and attributable cost for TFW work across roles and product areas.
- Value sought: Enable evidence-based decisions about team practice, TFW releases, and coordination modes.
- Lifecycle at report: RF
- Accepted result: not supplied at this cutoff; see RF/REVIEW before final close

## Resource summary

| Measure | Observed selected contribution |
|---|---:|
| Tokens, input + output | 92,629,326 |
| Input, including cache | 92,126,406 |
| Cached input subset | 89,439,232 |
| Output, including reasoning when source says so | 502,920 |
| API reference estimate on priced rows (USD) | 93.7930584 |
| Unpriced tokens | 0 |
| Undated tokens, excluded from date filters | 0 |
| Collection operation, observed wall seconds | 0.233 (0 files unknown) |
| Task calendar elapsed, status clock | 30408.263 seconds |

Time kinds remain separate; task calendar elapsed is read from task control,
not inferred from summed roles. Parallel role times can overlap.

- completed_turn: 11408.016 observed seconds

Money is a dated Standard API token equivalent, not a subscription bill.
Unknown models, tariff conditions, storage and tools are excluded.

## By role and model

### Role

| Role | Tokens | Priced USD |
|---|---:|---:|
| coordinator | 64,405,038 | 86.349740 |
| executor | 28,224,288 | 7.4433184 |

### Model

| Model | Tokens | Priced USD |
|---|---:|---:|
| gpt-6-astra | 47,914,992 | 81.877080 |
| gpt-6-sol | 44,714,334 | 11.9159784 |

### Consumption date

| Date | Tokens | Priced USD |
|---|---:|---:|
| 2026-09-28 | 38,993,311 | 42.485166 |
| 2026-09-29 | 53,636,015 | 51.3078924 |

## Coverage and provenance

- Expected units: codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793, codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243, codex:thread:local:01a0e9c4-e45c-7940-8515-fd083f4a7886, codex:thread:local:01a0e9f5-538c-7152-b704-b7f4b7e41784
- Received units: codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793, codex:thread:local:01a0e9c4-e45c-7940-8515-fd083f4a7886
- Measured units: codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793, codex:thread:local:01a0e9c4-e45c-7940-8515-fd083f4a7886
- Missing units: codex:thread:local:01a0e903-fa15-7e62-8032-956fdd7b7243, codex:thread:local:01a0e9f5-538c-7152-b704-b7f4b7e41784
- Failure-only units: none
- Incomplete source captures: 2 (a finite snapshot is not full task coverage).
- Excluded conflicting/superseded files: 0
- Capture cutoff: 2026-09-28T21:40:40.262894+00:00
- Finite tail: later report delivery, final message and cleanup are outside this cutoff.
- Rate card: 2026-09-29; USD per million text tokens, first-party Standard API reference; short context for OpenAI, no subscription allocation or tools

- codex:thread:local:01a0e7f5-7791-7ad0-99ff-30068c11b793: codex.rollout / 01a0e7f5-7791-7ad0-99ff-30068c11b793 revision 1, range [0, 3841), complete False, 5713 bytes, SHA-256 a5f42644c0cd185bb70c093787d9b1c8741b300894d26ffd3fd2f4896961e6e1, source 9c28cb91907a15674fbac6e2f6a0b78d644baa477bc8f275d4e476d6ccb29a7b.
- codex:thread:local:01a0e9c4-e45c-7940-8515-fd083f4a7886: codex.rollout / 01a0e9c4-e45c-7940-8515-fd083f4a7886 revision 1, range [0, 1509), complete False, 1774 bytes, SHA-256 ef80eb0f7221c4f75f0b161e843cc685a115c781aab2ef6fd6a0e963b7907db5, source a9d9edb912aa432ec8046e11fb371db754a2c25f19ed56fe4dde59fbaeb18f39.

## TEQM rollout coverage and numeric reconciliation

This is a pre-close basis, not final acceptance. The current four-unit compact view covers the Coordinator and Executor; the Researcher compact return and independent Reviewer return are still pending. The Researcher has already returned a separate numeric preparation snapshot: 28,923,212 tokens at 2026-09-28T18:41:26.934Z, pending common-format receipt. It is not added again to the table above.

The Coordinator contribution uses unique native token_usage_record response values whose sum equals the final thread_token_usage at the identical verified prefix. The alternative token_count view was 62,902,737; the selected stream is 64,405,038 (difference 1,502,301). Both are preserved in economics/preparation/coordinator-v1-reconciliation.json. A bounded own-source adaptation produced the standard rows without modifying shared field meanings, validator or tariffs. This discrepancy is an independent-review input, not a claim that the Candidate reader already handles it.

Earlier task contributors predate the new mandatory return contract. Their returned observations stay visible:

| Earlier contributor / returned source | Observed coverage | Relation to the compact total |
|---|---|---|
| Claude TEQM sample session local_049b6095-fe44-4cd6-bde1-acf4ce41e238; samples/claude/economics.md | 2,155,816 tokens across Sonnet 5 and Opus 5.5, cutoff 2026-09-28T19:08:11Z; 270.6 seconds inferred from turn boundaries, not native generation time | Separate legacy return, not yet a standard producer JSONL and not included above |
| Claude Research iteration 2, claude-code:session:local_802eab5b-1770-4551-b59a-aefd367bb975; research/iter2/RES.md | Session consumption total unavailable; context-window occupancy is not consumption | Historical gap, not zero |
| Antigravity Research iteration 3, antigravity:thread:local:b022b050-c6ce-450a-a406-257fbf471601; research/iter3/4_challenge.md | 236.92 model-generation seconds over 69 observed turns; no aggregate own token total returned | Historical partial observation, separate time kind, not included above |
| Codex Researcher's four separately recorded CLI probes; economics/preparation/researcher_codex_own_numeric_20260928.jsonl | Probe-specific returned numeric observations; some identities/initial attempts incomplete | Not folded into its rollout or other products |

UPM, DARYN, ROBBIE and KMCP are accounting examples from other tasks. Their totals are never TEQM costs. Captured API equivalents are not actual subscription charges. Remaining report preparation, verdict/return, owner acceptance and cleanup occur after one or more producer cutoffs; no claim of fully measured task lifetime is made.
