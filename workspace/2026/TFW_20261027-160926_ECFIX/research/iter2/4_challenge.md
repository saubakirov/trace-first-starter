# Challenge — Preserve sufficient guarantees without hiding execution gaps

> **Mindset:** Critic. A survivor must preserve the intended result and disclose its limits.
> Parent: [HL](../../HL-TFW_20261027-160926_ECFIX.md)
> Goal: Discoverable, correct native economics under Daily and Full.
> Producer: `codex:thread:local:01a17d31-497c-7c02-9dfe-33555f8a0314`
> Parent Coordinator: `codex:thread:local:01a17d02-d786-7583-ba4f-abb00d60f5e5`
> Authority: frozen HL at `91eeb269e9db44356cb356187363a1f3689e3c06`; unchanged delegated/native-gates/tfw-gates-only spine and selection.
> Continuation: `journal/20261027-181215__gate_answer__0225.md @ 9416f22269aa8a15b67d147f3968a64e739e637e`
> Originating proposer: none. Observation date: 2026-10-27 (+05:00).

## Consistency Check

All ten dimension pairs were checked against the actual guarantee and evidence level.

| Pair | Incompatible claim or surviving independence | Consequence |
|---|---|---|
| D1 continuity × D2 selection | A raw-basis old receipt linked to a different-basis covering successor without proof | Preserve old rules; reject the successor and retain last-good facts |
| D1 continuity × D3 execution work | An aggregate comparison claimed to prove every event value unchanged | Name the weaker sufficient guarantee; automation does not strengthen it |
| D1 continuity × D4 discovery | A located path or read guide claimed to establish current numerical continuity | Require actual supported extraction/comparison |
| D1 continuity × D5 execution context | Permission-denied inspection claimed as verified source content | Preserve locator evidence and access failure separately |
| D2 selection × D3 execution work | Observer reconciliation claimed as recurring agent self-execution | Both C8 and C7 remain observational prototypes |
| D2 selection × D4 discovery | An old cumulative report added as a new source because another entry found it | Select exact immutable facts once |
| D2 selection × D5 execution context | Unavailable current execution silently replacing measured old facts with zero | Keep last-good facts and precise current nonmeasurement |
| D3 execution work × D4 discovery | Shorter guide interpreted as measured lower agent cost | Compare actual reads/operations; word count alone supplies neither cost nor reliability |
| D3 execution work × D5 execution context | Broad automatic approval presented as necessary source-discovery support | Keep command policy independent; exact interactive action is a distinct unproved route |
| D4 discovery × D5 execution context | Headless discovery or analytical entry presented as a Full producer's final return | Preserve the separate native proof obligations |

| Survivor | Continuity / selection | Execution / discovery | Evidence and limit |
|---|---|---|---|
| X3 / automated C8 | Complete exported groups and membership checked per prior interval; disjoint selected facts | A bounded helper plus provider-owned procedure | Survives tested all-measured contiguous CLI case and controlled attacks; mixed dispositions require proof or refusal |
| X4 / aggregate C7 | Precisely specified aggregate projection; verified covering successor | Bounded helper plus provider-owned procedure | Survives tested same-basis calculations; requires explicit new digest/compatibility meaning |
| X6 / precise nonmeasurement | Last-good facts plus actual gap/failure | Discoverable diagnosis under unavailable execution | Necessary outcome; valid shape and correct cause both required; not product acceptance |
| X1 / existing raw successor | Unchanged bytes on a supported source | Existing collector | Retained for its actual supported cases; a version-only CLI expansion does not solve observed mutation |

X5's per-event archive/proof is not needed for the Coordinator-selected aggregate estimate. X7's new-source alternative remains a possible bounded recovery but is not demonstrated here and cannot erase attributable prior work. The unexpected survivor is X3 with automated complete aggregate checks: it can retain existing raw receipt meanings without a per-event archive. That is a compatibility advantage, not measured operating superiority over X4.

## Findings

### C1 — Aggregate-current checks survive the deciding controlled changes

Controlled in-memory variants of the retained numerical snapshot were passed through the unchanged compaction functions and the two candidate comparisons. C8 used only its prior validated disjoint receipts, exact source identity, per-range compact groups, contiguous measured membership and event counts. C7 compared the explicitly named aggregate projection. These are projection-level adversarial fixtures, not new provider events or evidence that arbitrary edited fixtures pass every v1 validator.

| Controlled change | C8 | C7 | Meaning |
|---|---|---|---|
| No change | Accept | Accept | Baseline continuity |
| Fresh/input/total +1 | Reject | Reject | A changed total is visible |
| Fresh -1, cached +1, same input/total | Reject | Reject | Exclusive categories matter independently of total |
| Reasoning subset +1 | Reject | Reject | Diagnostic measured subset is preserved |
| Model, effort or date group changed | Reject each | Reject each | Group identity is part of the guarantee |
| Duration changed or becomes unavailable | Reject each | Reject each | Time value and availability remain distinct |
| Event identity changed or event removed | Reject each | Reject each | Membership cannot silently change |
| Source identity changed | Reject | Reject | Same values do not establish same source |
| Measured disposition becomes unmeasured | Reject | Reject | Missing measurement cannot be normalized to zero |
| +1/-1 fresh changes inside the same prior aggregate group | Accept | Accept | Intended aggregate guarantee; no per-event immutability claim |
| Only nonnumeric raw fingerprint changes | Accept | Accept | Intended independence from irrelevant old bytes |

Neither survivor permits merely comparing the grand total. C8's demonstrated shortcut for membership works because all prior intervals contain contiguous, positive measured events with matching token-event counts. A historical interval with unmeasured/zero-only/noncontiguous events must have a sufficient retained disposition/membership basis or return an explicit unproved-continuity outcome. Do not manufacture that basis retrospectively. C8 also compares each retained interval, which can be stricter than comparing only an entire combined prefix; this may produce safe refusals rather than false current totals.

### C2 — One numerical snapshot must supply values, membership and hashes

A controlled SQLite in-memory database began with `(idx=0, amount=10)`. Backup A retained 10; after a committed source update to 11, backup B retained 11 while A still retained 10. Combining measurements from A with a fingerprint from B does not describe one source state. This is a concurrency counterexample, not a native AG mutation invented by the observer.

The [SQLite isolation documentation](https://sqlite.org/isolation.html), checked 2026-10-27, distinguishes transactions/snapshots and later committed states. Both proposed collector routes therefore need one consistent backup to supply the selected current rows, all prior-range checks, raw or semantic hash input and actual source end. Extract's extra C8 raw-hash backup did not establish that property. Reuse a single snapshot and its decoded rows; do not fix the race by guessing that the live agent is idle. This requirement applies independently of C8 versus C7 and can reduce repeated reads without a new persistent service.

### C3 — Historical raw receipts remain protected

A controlled copy of the valid temporary C7 successor was changed to name the existing raw-basis C8 predecessor, retaining the actual aggregate-prefix digest. Unchanged v1 validation accepted the file's structure; reconciliation rejected its successor proof with `unproved successor source prefix`, retaining the old **335,280** tokens and excluding the successor. Fixture SHA-256: `9725d8ec56dfb3acdfd82aa215ded25eb2122207ce62325170c54177341eeb2e`.

This is desired behavior. No implementation may insert the old raw digest into a new semantic-prefix field just to pass reconciliation. [Protocol Buffers guidance](https://protobuf.dev/programming-guides/serialization-not-canonical/), checked this stage, supports defining a narrow field projection; it does not make a changed hash basis backward-compatible. X4 requires a declared scope/basis and transition that preserves originals. X3 avoids changing that existing source-hash meaning but still owes complete current aggregate/membership comparison. A schema-version number alone proves neither option's compatibility.

### C4 — Correct failure representation is a small concrete repair target

The original Daily record remains invalid. A controlled in-memory copy renamed only `known_facts` to `known` and `unavailable_reasons` to `unavailable`; the unchanged `status_fields` then accepted its structure. The original file hash stayed `c7e6ba4da7b22dae9496094c72395e085e3a83111b1906d3c5c5c9b0d0eac946`. The experiment did not weaken the validator or silently repair the native subject's historical output.

Shape validation does not validate the cause. The subject's initial assertion that the experimental mandate prohibited its own-source inspection was false; the later native read-policy denial is an actual different fact. Likewise, known identity plus an unsupported decoder is not automatically missing identity. Recommended instruction correction: state the exact existing gap keys and a checkable example at their single common owner, and explicitly distinguish binding facts, permission failure, unsupported extraction and actual collection attempts. Reuse validation before a return. Avoid adding synonymous key names, a second failure schema or a permissive parser to accommodate one erroneous generated record.

### C5 — Recommend a bounded implementation direction, not an unproved operating winner

The smallest justified direction is a discoverable provider procedure plus a truthful supported-surface reader and a complete automated continuity operation using existing portable facts/reconciliation. Prefer X3/C8 as the initial compatibility-preserving implementation candidate **if** its one-snapshot helper can validate all selected prior aggregate groups and membership/dispositions and return a checked cumulative union with one normal agent operation. Reserve X4/C7 if an actual implementation demonstrates a materially simpler or more dependable recurring path sufficient to justify its explicit digest contract. Neither is claimed cheaper or operationally superior from these prototypes.

Required behavior is more precise than "add a guide": discover and verify the actual own source; preserve the observed CLI fresh/cache/output semantics; retain child membership; give the current all-input union once; represent real failures correctly; preserve historical receipts and last-good facts. Keep platform discovery/format instructions with the provider and common meaning/shape with the common owner. Remove replaced duplication. A new broad wrapper, raw event archive, registry or daemon is unsupported by the evidence.

Fresh Daily proved the link was read. It did not prove unaided binding or successful capture; Full analysis and Desktop did not complete their dependent actions. No further native call in Challenge would by itself prove a not-yet-delivered helper's usability. The permitted interactive exact-command route remains available for later authorized native verification if the CLI actually presents that bounded action; it was not replaced by broad settings changes or a retry of denied actions here.

Implementation and independent review still owe: fresh Daily and actual Full-producer self-collection; repeated returns and failure retention through the supported helper; installed/isolated receiver parity; authenticated Claude ordinary/child/fork attribution; native Desktop identity/source behavior once accessible. Access restoration and a documented supported scope are explicit prerequisites, not acceptance waivers. A third research iteration solely to repeat inaccessible actions is not justified; return the decision and precise remaining proof to the Coordinator.

## OODA, economics and cleanup handover

**Observe:** retained bounded numerical snapshots/receipts, unchanged validator/reconciler, controlled projections and SQLite snapshots, first-party sources, and current gate. **Orient:** separate sufficient aggregate truth, historical compatibility, same-snapshot correctness, valid representation and native execution. **Decide:** X3/X4 survive with explicit conditions; propose X3 first on compatibility grounds without claiming a measured operating winner. **Act:** return the bounded recommendation and unresolved proof for synthesis authorization.

No native model invocation occurred in Challenge. The observed AG union remains **686,810** tokens across the four exact sources in Extract, not a new additive contribution. Own Codex binding remains the same source/unit and received revision 1; a final verified successor or disjoint capture remains owed at RES. Current status/iteration, base/focused workflows and knowledge-use/handover ranges were rechecked; same `RESEARCH · ECFIX`, authority and parent continue. No product code, permanent tests or qualified knowledge publication was added.

Cleanup remains owed. Under the new gate, a narrower attempt first verified the task temporary target and every ancestor through system temp had no reparse points, then verified 15 explicitly named native-output files were regular files. Removal of only those named files, without recursion, was also rejected by automatic approval with `blocked by policy` and no further reason. The owned `tfw/TFW_20261027-160926_ECFIX/iter2-extract` subtree remains under system temporary storage, including the new clearly labelled mixed-basis fixture. No alternate deletion mechanism or bypass was attempted. Preserve this dependency for the Coordinator/owner; do not claim cleanup complete.

## Checkpoint

| Found | Remaining |
|---|---|
| Both complete comparisons reject changed categories/groups/membership/disposition | Delivered one-snapshot implementation and full supported disposition cases |
| Same-basis successors work; mixed bases correctly refuse | Explicit compatibility contract if C7 is chosen |
| Existing gap validator is sufficient for exact keys | Correct guidance, truthful cause and native validated return |
| Compatibility grounds support trying automated C8 first | No demonstrated native operational winner; required product proof remains open |
| Narrower verified cleanup also denied | Owner/Coordinator cleanup dependency; no bypass |

**Sufficiency:**
- [x] External source used.
- [x] Available Briefing uncertainty challenged; inaccessible and future product proof remains explicit.
- [x] All dimension pairs checked and survivors stated.

**Question for the Coordinator:** Accept Challenge and authorize iteration 2 synthesis with the conditional X3-first recommendation, X4 reserve, and unchanged native-proof/cleanup dependencies?

Stage complete: YES
Recommendation: close Challenge; wait for the required Step 5 decision before RES synthesis.
