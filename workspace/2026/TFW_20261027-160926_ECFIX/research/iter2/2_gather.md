# Gather — Continuity guarantees, execution burden and discoverable entry

> **Mindset:** Explorer. Separate independent choices before comparing procedures.
> Parent: [HL](../../HL-TFW_20261027-160926_ECFIX.md)
> Goal: Make native economics collection discoverable and correct under Daily and Full.
> Producer: `codex:thread:local:01a17d31-497c-7c02-9dfe-33555f8a0314`
> Parent Coordinator: `codex:thread:local:01a17d02-d786-7583-ba4f-abb00d60f5e5`
> Authority: frozen HL at `91eeb269e9db44356cb356187363a1f3689e3c06`; unchanged delegated/native-gates/tfw-gates-only spine and selection.
> Continuation: `journal/20261027-174504__gate_answer__7a3d.md @ 866371354b04d34d13d577778419ca29d8e76e0c` accepts iteration 2 Briefing and authorizes Gather.
> Originating proposer: none. Observation date: 2026-10-27 (+05:00).

## Dimensions

These factors refine iteration 1's C8/C7 comparison; no alternative is selected here.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| D1: Continuity guarantee | Raw selected bytes equal | Same per-event measured values and identities | Same complete aggregate groups and event membership | No current continuity proof; retain last-good |
| D2: Returned fact selection | Disjoint intervals plus checked union | Covering successor plus verified predecessor | Fresh isolated source with explicit task membership | Actual failure/gap plus prior facts |
| D3: Recurring execution work | Agent orchestrates comparison and collection steps | One checked helper operation combines steps | Native runtime supplies a sufficient checked receipt | Observer-only experiment, no self-collection proof |
| D4: Discovery instruction ownership | Existing common recipe | Common route to provider-owned complete procedure | Runtime binding plus thin provider procedure | Precise unsupported-entry diagnosis |
| D5: Native execution context | Permitted file-read headless discovery | Headless collection with already authorized applicable command policy | Interactive confirmation of an exact bounded command | Unavailable dependent execution with explicit limit |

## Findings

### G1 — Automation is independent of disjoint versus covering selection

At source epoch `866371354b04d34d13d577778419ca29d8e76e0c`, `collect` checks the predecessor's namespace/source/unit, hashes the selected source and, for a covering capture, checks its old prefix against the previous manifest. `reconcile` selects disjoint ranges or a verified covering successor and excludes unsupported overlaps. These mechanisms do not provide C8's old numerical comparison automatically.

It would bias the comparison to make C8 a manual multi-step procedure and C7 one helper command without pricing the automation choice separately. Both can potentially put their repeated source inspection and checks in a bounded helper. Conversely, a short C7 instruction can hide substantial required semantics. Extract should compare equal declared guarantees and expose any extra helper behavior as a prototype alteration, keeping collection wall time, native agent consumption and instruction size distinct. No comparative cost has yet been measured.

### G2 — Compact portable rows cannot prove per-event value continuity

`compact_rows` groups by consumption date, model, effort and timezone, with separate duration kind. It preserves category sums, event count and a digest of event IDs. The digest covers IDs, not each event's measured values. Its source manifest still carries the raw-source hash, which iteration 1 showed can change after a legitimate CLI continuation.

A bounded in-memory controlled fixture used the unchanged `usage`, `zero_tokens` and `compact_rows` functions: two same-model undated events `idx:0` and `idx:1`, fresh input 10 and 20, output 2 and 3, generation durations 1 and 2 seconds. A copy changed fresh/input/total by +1 on event 0 and -1 on event 1. Individual values became 11 and 19, while compacted rows remained exactly equal. This is a synthetic counterexample to inferring per-event equality from aggregate equality, not a native source mutation or a miscount in the current task.

There are consequently distinct options: explicitly compare complete aggregate facts when that is the required current-account guarantee, retain a bounded numeric per-event basis, or retain a specified per-event measured digest. The first cannot claim the stronger guarantee; the others introduce state or digest semantics whose cost belongs in the comparison. Aggregate equality can still be useful for aggregate correctness. Research should not require stronger event-history immutability merely because it is possible, nor silently weaken the intended guarantee to make C8 pass. The choice must be explicit before interpreting prototype results.

### G3 — A semantic fingerprint needs a named, narrow meaning

The [Protocol Buffers guidance](https://protobuf.dev/programming-guides/serialization-not-canonical/), checked 2026-10-27, advises a deliberately named field selection rather than a generic protobuf fingerprint. Applied to this experiment, the relevant candidate projection would specify row index/identity, model, exclusive token buckets and reasoning subset, measured/unmeasured disposition, timing presence and seconds/nanoseconds, and omitted-zero rules. It would not silently normalize every unknown protobuf field. The observed source mutation was a real change to nonnumeric contents, not an assumption about field ordering.

The current receiver compares predecessor source hashes without an independent digest-basis field. Changing a reader's hash meaning therefore needs explicit source/collector compatibility rules, even if JSONL remains schema v1. Existing raw-basis receipts must not be rewritten or casually linked to semantic-basis successors. A distinct experimental CLI path can investigate this without changing the existing IDE recipe; whether that is the sufficient product choice remains open. No provider-wide stable projection is established here.

### G4 — Installed headless controls limit what a successful discovery probe proves

Actual `agy --help` for installed CLI 1.2.16 exposes `--mode`, `--sandbox`, `--conversation`, `--print-timeout`, `--input-format`, `--output-format` and `--disable-slash-commands`; it exposes no scoped per-command permission flag. The current [headless reference](https://antigravity.google/docs/cli/headless/) describes command soft-denial, settings-based grants and rejection of stream `control_request`/`control_response`. The [CLI reference](https://antigravity.google/docs/cli/reference/) documents interactive confirmation and labels auto mode with newer Windows version requirements. Documentation does not establish availability of those newer behaviors on installed 1.2.16.

No permission setting, global grant, model or installation was changed. A fresh headless file-reading probe can test whether the normal entry reaches the provider procedure and obtains a grounded locator. It cannot by itself prove command execution, a validated self-capture or the Daily before-return cadence. A one-time interactive confirmation of an inspected command is a separate possible native route, still untested; no automatic stream approval bridge is assumed. Existing denied-command evidence already suffices to reject an unchanged attempt at headless execution under the same policy.

Keep slash/skill expansion enabled for the entry experiment. `--conversation` is suitable for an exact known continuation; `--continue` would select the most recent conversation and is unsuitable for this attribution test. No new native model invocation was performed in Gather.

### G5 — Baseline instruction size is measurable; relocated text is not automatic savings

Method: decode each selected file as UTF-8, count maximal non-whitespace spans with Python `re.findall(r'\S+', text)`; headings, front matter and code count. This is a reproducible text-size measure, not model-token consumption. Baseline is the unmodified source at the epoch above.

| Selected text | Words | SHA-256 or exact section |
|---|---:|---|
| `.tfw/economics/README.md` | 3,900 | `8bea60bfe64a20111f877191e5cec3146b871e550e57a8d2152f2bd943a066df` |
| Common Antigravity recipe | 203 | Heading `Antigravity IDE numeric database recipe` through the next level-two heading, including its heading |
| `.tfw/adapters/antigravity/README.md` | 263 | `84034554a9144a7b5d3fb5203180c03caf4853ede90233fa5127443d6bd35493` |
| `.agents/skills/tfw-daily-task/SKILL.md` | 71 | `2d5608deca56a6ef017206a2a53f8cd18c20b888511661edf2aa9c7f089d7c64` |
| `.agents/skills/tfw-economics/SKILL.md` | 76 | `4e1b45b3e166bcd153d863dfb8763dbcc8ef48bf96f9c993c39eb87223033b08` |
| `.tfw/extensions/daily-task/SKILL.md` | 1,355 | `61e17248a3d4966f5ddbe7ae98a109901c153bcb9eec3feb706d7c8470aa70d2` |
| `.tfw/workflows/economics.md` | 1,398 | `657b3835ab87e4849d2fd03f662f144c81e344d2f0f48e66565f152c3543b4d6` |

The 203-word recipe is already part of the 3,900-word README, not additive text. Existing Daily and economics entries explicitly route to canonical sources which require that common README. Moving the AG recipe to a separately reached provider file may improve ownership while leaving the total read size similar or larger. Extract must report moved, replaced, removed and added text and the actually reached read path. A guide filename or a smaller patch is not proof of reduced input tokens. This stage measures no completed candidate guide and claims no savings.

### G6 — Full analysis entry and Full producer return are distinct tests

The inspected economics workflow analyzes authorized returned bytes and retains an active role's authority. The Daily workflow additionally requires own-source binding and a cumulative capture before each orderly return. Thus an experimental `/tfw-economics` success on a copied Full record proves that analytical entry only; it does not establish a real Full producer's final own-source obligation. Fresh experimental subjects remain subjects, not substitute formal TFW role units. Prototype evidence must name exactly which boundary it tested, leaving actual product proof to the authorized implementation and independent review.

An isolated receiver should contain the selected thin entry, its canonical dependencies and a minimal explicitly experimental work object, with only the declared provider-procedure alterations. It must not inherit unrelated project history or receive the exact source answer in its prompt. Record actual discovered identity, location, loaded files and supported failure independently from the observer's own ability to extract numbers. A completed read-only discovery can be useful even when capture execution remains unavailable, provided it is labelled narrowly.

## OODA and material handover

**Observe:** installed help, selected reader/compaction/reconciliation functions, adapter and normal entry routes, first-party CLI/protobuf documentation, baseline word counts and one in-memory controlled counterexample. **Orient:** distinguish proof granularity, fact selection, automation, discovery and executable permissions. **Decide:** keep five independent dimensions and require equal explicit guarantees in the next comparison; neither C8 nor C7 wins this stage. **Act:** return the deciding refinements and proposed bounded Extract to the same Coordinator.

Current status and prepared iteration were rechecked after fast-forward to the gate. Same producer, parent, selection and `RESEARCH · ECFIX` identity continue. Current knowledge-use and handover ranges were reread; iteration 1 retains the exact native evidence and historical supported-surface limits. No new qualified knowledge publication is asserted. This stage created no on-disk prototype, raw export or fixture file; the controlled fixture existed in memory only. No native model invocation, unrelated-source read, authentication retry, UI retry, permission change or product implementation occurred.

Own source remains the bound Researcher rollout `01a17d31-497c-7c02-9dfe-33555f8a0314`, version `0.164.0-alpha.11.1`, start 0, timezone `+05:00`; the received revision-1 prefix `[0,622)` was rechecked unchanged. A final verified successor/disjoint contribution remains owed at RES. This intermediate checkpoint does not add the old cumulative total again.

## Checkpoint

| Found | Remaining |
|---|---|
| Automation choice is independent of C8/C7 selection | Comparable complete procedures and actual recurring effort |
| Compacted rows cannot prove per-event numerical equality | Choose and explicitly test the required continuity guarantee |
| Headless discovery and executable capture are different | Fresh native entry observation; available exact-command execution route |
| Baseline text and counting method established | Candidate additions/removals and actual read path |
| Full analytical entry does not replace a Full producer return | Precise prototype scope and later required product proof |

**Sufficiency:**
- [x] External source used.
- [x] Briefing gap closed at Gather level: fair comparison factors and observable limits established.
- [x] Five independent dimensions with at least three alternatives each.

**Questions for the Coordinator:**
1. Accept the distinction between aggregate-current correctness and per-event continuity, and permit Extract to expose both guarantees explicitly rather than treating aggregate equality as full event proof?
2. Proceed to bounded temporary procedure/receiver prototypes and fresh-entry discovery, retaining any unavailable capture execution and genuine Full-producer proof as separate open conditions?

Stage complete: YES
Recommendation: close Gather; await the Coordinator's Extract decision under research Step 5.
