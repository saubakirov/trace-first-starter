# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260904-113200_VBSA](../../HL-TFW_20260904-113200_VBSA.md)
> Goal: Reconstruct a completed non-code/binary delivery and expose every choice needed to make trigger disposition, authority, hard bounds, and compatibility enforceable.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1 — non-code metric applicability | Apply logical file count and text LOC everywhere | Apply logical file count universally; LOC only where meaningful | Use only delivery-specific measures | Use no numeric signal outside code |
| D2 — file-count meaning | Absolute configured size trigger | Planned-versus-actual membership trigger | Cardinality disclosure only | Hard file ceiling |
| D3 — classification unit | Whole changed path | Semantic hunk/line | Accepted-output component | Commit/path-set intersection |
| D4 — growth authority | Owner decides every crossing | Coordinator decides inside an unchanged contract | Executor adapts and Reviewer accepts | Mechanical split with no discretion |
| D5 — discovery timing | Planned before TS approval | Discovered before added work | Discovered after work but before RF | Discovered only by Reviewer |
| D6 — cross-phase allocation | Count a shared path in every phase | Assign the whole changed path to one phase | Separate phase candidates/commits | Allocate sub-file hunks |
| D7 — hard-bound basis | Any configured threshold | Named material harm with direct metric | Reviewer capacity or generic smallness | External/frozen constraint with zero tolerance |
| D8 — compatibility epoch | Reinterpret every task on update | New semantics only for TS approved after the release | Preserve hard semantics for each existing project | Add a hard/soft configuration key |
| D9 — trigger carrier | Dedicated new record | TS-only ruling | TS→RF→EV→REVIEW chain | REVIEW reconstructs and rules after execution |
| D10 — mixed-role treatment | Accepted-output precedence for whole path | Exclude trace hunks | Require physical separation | Report INVALID when exact attribution matters |

These dimensions are independent. For example, fixed phase candidates do not decide whether a file-count threshold is hard, and accepted-output precedence does not decide who may authorize a newly discovered path.

## Findings

### G1 — TFW-27 Phase A is an immutable completed non-code/binary replay

The selected historical delivery is `tasks/TFW-27__wiki_polish_and_brand/PhaseA`, a brand-identity/documentation phase whose REVIEW records `✅ APPROVE`. Its accepted results include brand guidelines, a README hero, theme configuration and CSS, plus raster logo and favicon assets. It therefore exercises document, configuration, visual, and binary surfaces rather than treating code as the product.

The immutable replay pair is:

```text
Baseline  e3f67e124c7c05a77003f1ca31260590b6f2569a
Candidate 5108c25135f171be1a8f54ade4884a3219fd6e34
```

`5108c25` is the reviewed Phase A+B delivery commit and has `e3f67e1` as its sole parent. Phase A's TS declared six product paths: four new and two modified. The fixed candidate contains one additional necessary visual constituent that the TS/RF inventory omitted: `docs/brand/logo_header.png`. At the same candidate, `docs/mkdocs.yml` points its active `theme.logo` to that file. Accepted-output/necessary-constituent precedence therefore makes it `VALUE`; treating it as an incidental generated file would hide the actual header asset used by the accepted site.

The Phase A value selector yields:

| VALUE path | Status | Additions | Deletions | LOC treatment | Why VALUE |
|---|---:|---:|---:|---|---|
| `README.md` | M | 34 | 15 | 49 touched | Accepted hero/document surface; it also contained a task-board trace line, so it is a mixed-role path. |
| `docs/brand/identity.md` | A | 156 | 0 | 156 touched | Accepted brand-guidelines document. |
| `docs/overrides/stylesheets/extra.css` | A | 77 | 0 | 77 touched | Necessary constituent of the accepted rendered theme. |
| `docs/mkdocs.yml` | M | 21 | 27 | 48 touched, conservative | Necessary configuration; the same squashed commit also carries Phase B plugin edits. |
| `docs/brand/logo.png` | A | N/A | N/A | **N/A** | Accepted raster logo; blob `40d4a00…`, 97,443 bytes. |
| `docs/brand/logo_header.png` | A | N/A | N/A | **N/A** | Active accepted header logo; blob `463da2d…`, 14,983 bytes; omitted from TS/RF. |
| `docs/brand/favicon.png` | A | N/A | N/A | **N/A** | Accepted favicon; blob `feb30b5…`, 2,607 bytes. |

Result: **7 logical VALUE paths = 5 new + 2 modified; 288 additions + 42 deletions = 330 touched text LOC; three binary VALUE paths with LOC = N/A.** The historical six-path/four-new plan was therefore one path low, while its then-configured 14-file ceiling did not fire.

This replay establishes both usefulness and limitation. File membership exposed an accepted artifact that the textual trace omitted; raw LOC could not represent three of the seven value paths at all.

### G2 — The combined commit tests all four classes and a phase-allocation gap

The immutable candidate contains 29 changed paths because Phase A and Phase B were squashed with their traces. Relative to the combined accepted Phase A+B delivery:

| Class | Paths | Touched text LOC | Binary handling | Observation |
|---|---:|---:|---|---|
| `VALUE` | 11 | 665 | 3 paths, LOC = N/A | Phase A brand/document value plus Phase B documentation pipeline value. |
| `ASSURANCE` | 2 | 155 | none | Phase B unit/integration tests. They remain in implementation and review scope but do not enlarge delivered value. |
| `TRACE` | 16 | 1,943 | none | Fifteen task research/HL/TS/ONB/RF/REVIEW paths plus the then-live debt record. |
| `DERIVED` | 0 tracked | N/A | build tree absent | `docs/mkdocs.yml` declares `site_dir: ../site`; `.gitignore` excludes `site/`. The build output is reproducible and not independently accepted, so it remains outside the candidate. |

The text arithmetic reconciles: 665 VALUE + 155 ASSURANCE + 1,943 TRACE = **2,763 touched text LOC**; the three binary VALUE paths remain outside that sum rather than appearing as zero.

The replay also yields counterevidence to a path selector being sufficient by itself. `docs/mkdocs.yml` contains Phase A brand settings and Phase B plugin/navigation settings in the same commit. A path-level Phase A selector conservatively charges all 48 touched lines to Phase A; excluding the file would hide accepted value, while counting it fully in both phases would duplicate it. Exact per-phase LOC allocation is unrecoverable from the squashed historical commit without hunk interpretation. Forward reproducibility therefore needs one of three explicit choices already expressible in TS: a phase-specific VALUE candidate, whole-path ownership assigned to one phase, or `INVALID` when exact allocation matters. A fifth semantic class does not solve attribution.

### G3 — Logical VALUE-file count is universal as cardinality, not as magnitude

The official Git diff documentation says its file-based distribution mode counts every changed file equally and does not inspect content; its binary `--numstat` output is `-`/`-`, not `0`/`0`: <https://git-scm.com/docs/diff-options>. This makes logical file count broadly reproducible across text and binary repositories, but also supplies direct counterevidence to interpreting one file as one equal amount of value or work.

TFW-27/A makes the distinction material:

- **Useful signal:** the planned selector had six paths and the accepted surface had seven. The count detected an undisclosed necessary constituent when LOC could not.
- **Weak absolute signal:** three binary assets range from 2,607 to 97,443 bytes, yet each contributes one file; the 14-file hard ceiling said nothing about their visual quality, internal complexity, or review burden.
- **Cross-domain limit:** the Library of Congress evaluates digital formats using multiple sustainability, functionality and quality factors and states that significant characteristics vary by genre or form of expression: <https://www.loc.gov/preservation/digital/formats/sustain/sustain.shtml>. A PNG, a PDF, a presentation and a dataset are not made commensurable by counting each as one.
- **Decision-useful interpretation:** logical VALUE-file count can always disclose cardinality and selector drift for file-backed deliveries. It becomes a soft action signal when actual membership differs from the TS plan or crosses a configured trigger; it is never sufficient proof that the delivery is too large, too risky, or low quality.

This narrows Iteration 1 D5 rather than simply confirming it: a universal *reportable measure* survives, while a universal *meaning for the absolute number* does not.

### G4 — The six-condition Coordinator boundary has five adversarial holes to test

Iteration 1 proposed six conditions around unchanged Goal, Value, accepted deliverables, AC, DoF and phase boundary; necessary path mapping; fixed recalculation; prospective timing; recorded cause/cost/assurance/split; and Reviewer verification. Applying them literally exposes these cases:

| Attack | Disguised request | Condition that appears to allow it | Fact that must decide it |
|---|---|---|---|
| New deliverable disguised as constituent | “The accepted report needs a reusable export CLI, so add it as support.” | It can be described as necessary to the existing result. | A separately usable or independently accepted interface/output changes accepted deliverables or an AC and remains Owner authority. |
| Mixed-role path | “Only the new helper section is VALUE; ignore the implementation half of the same file.” | The path has both accepted and supporting content. | Default metrics operate at logical-path/diff level. Whole-path VALUE is conservative; sub-file exclusion is unenforceable unless an approved selector can reproduce it. |
| Late architecture | “The same AC needs a new persistent service and public authority boundary.” | Goal and user-visible outcome may be textually unchanged. | Durable architecture, public interface, persisted-data, security/trust or authority-boundary changes are not ordinary path growth; if they alter a frozen claim they require amendment, otherwise Coordinator must revise TS prospectively before implementation. |
| Cross-phase reuse | “Phase B uses Phase A's file, so charge it again,” or “both phases changed it in one commit.” | Each phase can claim necessity. | Unchanged reuse costs zero; a changed shared path needs one named phase owner or separate phase candidate. Ambiguous simultaneous allocation is INVALID, not double-counted. |
| Retroactive discovery | “We already built it; now record that the Coordinator approved the crossing.” | The added paths map to an existing result and review can verify them. | Authority must exist before work on the newly discovered surface. After-the-fact recording is a deviation, not prospective authorization. |

The late-architecture attack identifies a missing discriminator in A2's current wording. Goal/outcome sameness does not prove architecture sameness. NASA's Systems Engineering Handbook treats baseline identification, change-control authority, proposal, justification, evaluation, approval, implementation and verification as distinct acts, and says changes affecting external interfaces require coordination and approval by affected stakeholders: <https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf>. The TFW boundary must likewise name architectural/interface/authority changes and preserve decision-before-implementation ordering.

### G5 — Material hard constraints need consequence, directness and pre-act enforceability

Historical and current evidence supplies candidate examples without treating all of them as valid:

| Candidate hard constraint | Named consequence | Direct metric/selector | Pre-write? | Materiality observation |
|---|---|---|---|---|
| AFD-38 A1.2.2 exact nine product/test paths and 900 touched LOC | An incident corrective spreads outside the authorized MQTT/security slice. | Exact path set; fixed baseline/candidate. | Yes. | Material blast-radius/containment example; the exact path set is stronger than generic LOC. |
| VBSA read-only AFD/Helpdesk/history boundary | Evidence history is mutated and the research ceases to be reproducible. | Zero writes to named repository/path sets. | Yes. | Material authority/trace-integrity constraint; not a configured size limit. |
| A schema or external-interface migration limited to a named compatibility surface | Irreversible data or downstream compatibility harm occurs before review. | Exact migration/interface selector plus domain gate. | Potentially. | Material only when the protected interface/state and rollback authority are named. |
| Exact submission attachment/file cap imposed by a recipient | External rejection of the accepted deliverable. | Logical accepted-output count. | Yes. | Material external constraint; Owner or external authority controls relaxation. |
| Current configured 50-file/5,000-LOC defaults | “The phase is large.” | Reproducible after classification. | Only if evaluated prospectively. | No named consequence by itself; a soft decomposition signal, not sufficient hard-bound basis. |
| Reviewer prefers fewer files | More work to inspect. | File count loosely correlates. | Yes. | Counterexample: review capacity is handled by decomposition, reviewer assignment and proportional assurance; generic preference is not a delivery veto. |
| Cap tests, evidence or trace files | Process volume grows. | Easy to count. | Yes. | Counterexample prohibited by the frozen no-shadow-budget boundary; relevance/sufficiency decides instead. |
| Binary presentation under 5,000 LOC | None; LOC is N/A. | No. | No. | Counterexample: metric does not represent the subject. |
| Bound discovered only in RF/REVIEW | Any stated harm. | Possibly. | No. | Counterexample to “hard”: it can detect a breach but cannot prevent the act. |

The candidate materiality test has six independent parts to challenge later: named consequence; protected contract/risk; direct applicable metric; fixed selector; pre-act enforcement; and named authority. A soft trigger remains the alternative unless post-act review would be too late or incapable of repairing the harm.

### G6 — Current carriers can hold a prospective trigger chain, but none does today

The current carrier inventory has no unique missing file:

| Existing carrier | Present capacity | Missing statement for VBSA | Downstream reader |
|---|---|---|---|
| TS §4 Affected Files + Budget line | Planned paths/actions and aggregate estimate | Class/selector, baseline, candidate rule, applicable measure/trigger, task-local hard constraint, and any prospective crossing disposition | Executor; Reviewer |
| TS §5 AC + Evidence | Observable criterion with gate/evidence | One accounting AC that makes undispositioned crossings and mismatched refs non-compliant | Executor; EV; Reviewer |
| RF §1 What Was Done | New/modified path facts | Immutable candidate, actual VALUE result, discovered membership/class changes, and citation to the pre-work TS disposition | EV; Reviewer |
| EV generic evidence row | Per-AC observed result and artifact | Re-run the exact TS method and state whether every crossing had a prospective ruling | Reviewer |
| review/verify.md | Commands, claim/source checks, discrepancy escalation | Re-run same refs/selector/method; compare decision time to first added work; never reconstruct a selector | REVIEW |
| REVIEW §2/§4 | Verified findings and binding verdict | Approve a valid chain; otherwise cite the accounting AC and route by whether repair changes TS or frozen contract | Coordinator/Owner |

The chain is smallest only if the initial disposition lives in the Coordinator-owned TS. RF is observation, EV is independent execution evidence, and REVIEW is adjudication; none has authority to create retroactive permission. ONB may surface a question, but it is not required as a fifth budget carrier because the Coordinator's resulting decision must be written into TS before work proceeds.

### G7 — Same-key hard-to-soft compatibility can only be forward by TS approval epoch

The existing `tfw.scope_budgets` keys and values cannot encode both hard and soft semantics. With no new key, three facts follow:

1. Historical measurements and completed artifacts remain facts in their own traces; no update may relabel them.
2. An already approved TS remains the task-local authority for its explicit hard limit, override, or scope boundary. A later framework update cannot silently relax it.
3. A TS approved after the release adopts the new canonical default: configured numbers are soft triggers unless that TS explicitly promotes a task-local bound to hard.

This is forward compatibility, not identical future behavior for every project. Semantic Versioning requires a released version's contents to remain unchanged and ties compatibility communication to the declared public contract: <https://semver.org/>. Changing the default enforcement meaning is therefore a public behavioral change that must be explicit in the release's `Changed` entry and in the update briefing; exact version classification remains a Coordinator/release decision.

Candidate canonical wording to test in Extract/Challenge:

> **Forward applicability.** Beginning with the TFW release that introduces value-bearing scope accounting, `tfw.scope_budgets` values are default soft decomposition and disclosure triggers for a TS approved under that release. They do not amend or reinterpret a previously approved TS, a task-local hard constraint, or any historical measurement. Existing projects keep their configured numbers. To make one of those numbers hard for new work, the governing TS must explicitly name the protected harm, subject and selector, applicable metric and threshold, pre-write enforcement point, and authority allowed to change it.

Candidate release/update wording:

> **Changed:** `tfw.scope_budgets` keeps the same keys and configured values, but newly approved TSs interpret those values as soft VALUE-surface triggers rather than automatic failure limits. Existing approved TSs and historical results keep the semantics they recorded. A new TS that needs a hard constraint states it explicitly with its protected harm and authority. No migration rewrites task history and no replacement key is introduced.

The current update workflow already converts `CHANGELOG` `Changed` bullets into the owner's “What you now do differently” briefing block. That is the existing notification carrier; inventing a second migration note is not yet justified.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| TFW-27/A replay: 7 VALUE paths, 330 touched text LOC, three binary VALUE files with LOC = N/A; the extra active header logo was absent from TS/RF. | Build the final configuration and decide whether A4's whole-artifact fallback is adequate for mixed-role paths. |
| Combined immutable commit: 11 VALUE / 2 ASSURANCE / 16 TRACE / 0 tracked DERIVED; ignored site output demonstrates reproducible derivative exclusion. | Test whether zero tracked DERIVED is enough or whether the rule needs a positive accepted-generated counterexample. |
| Logical VALUE-file count exposes membership/cardinality across binary work but cannot express internal magnitude or quality. | Decide the exact universal claim: reportable measure, configured trigger, planned-delta trigger, or disclosure only. |
| Five attacks expose prospective-timing, architecture/interface, and cross-phase-allocation requirements beyond A2's headline. | Run pairwise authority cases and determine which require Owner, Coordinator, or fail-closed handling. |
| Existing TS→RF→EV→REVIEW carriers can enforce one decision sequence. | Specify mandatory fields/statuses and remove any nonessential statement. |
| Forward-only semantics can preserve approved TSs/history with the same keys. | Attack upgrade ambiguity and determine whether release notes plus canonical clause are sufficient. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?
- [x] At least one hypothesis tested? H1, H3, H4 and H5 received counterevidence.
- [x] Counterevidence sought? TFW-27's mixed commit, hidden required asset, binary size spread, and public change-control sources all challenge Iteration 1's simplest form.

**Metacognitive check:** New findings were produced, not merely confirmed: the approved Phase A result contains a seventh necessary VALUE path omitted by both TS and RF; a shared mixed-phase path makes exact per-phase LOC unrecoverable from the historical squashed commit; and A2 omits an explicit architecture/interface discriminator.

**Decisions recorded at Gather:** retain the replay pair as the immutable non-code corpus; carry logical file count forward only as a cardinality/membership candidate, not a magnitude verdict; require Challenge to test prospective authority and shared-path allocation.

Stage complete: YES
→ User decision: Advance under the owner's fixed Iteration 2 assignment; no new deliverable or authority was accepted at Gather.
