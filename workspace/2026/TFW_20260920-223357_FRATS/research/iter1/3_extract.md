# Extract — "What do we NOT see?"
> **Mindset:** Analyst. Build structure from the gathered evidence; expose combinations without selecting a winner.
> **Test:** "Does the configuration space reveal at least one combination that the Briefing did not propose?"
> Parent: [HL-TFW_20260920-223357_FRATS](../../HL-TFW_20260920-223357_FRATS.md)
> Goal: Refactor TFW from field evidence so its artifacts remain behaviorally complete while routine coordination moves from repeated dialogue to concise durable traces.
> Boundary: iteration 1 only; no live provider/AT trial, architecture selection, framework/receiver mutation or restoration of retired tooling.

## Configuration Space

The table uses the eight Gather dimension names. It lists non-obviously-contradictory configuration
families rather than the full `4^8` cross-product.

| Config | D1: receiver state at observation | D2: receipt-to-current relation | D3: measurement continuity | D4: runtime context charge | D5: rule/delivery relationship | D6: artifact filename state | D7: rule-compliance cause | D8: principal-resolution context |
|---|---|---|---|---|---|---|---|---|
| C1 | clean after committed update | receipt claim corroborated now | exact historical replay | whole file | sole canonical owner | current single-phase `TYPE__{ID}` | checkpoint placement/timing | human owner session |
| C2 | clean after committed update | receipt condition resolved later | historical replay plus explicit current bridge | addressed heading/range | exact installed copy | current phase `TYPE__phase-*` | conflicting/incompletely loaded instructions | non-AT operational session with no named agent principal |
| C3 | clean but installed release is behind | receipt condition still visible | successor measure with no equality claim | deliberate repeated read | managed block projection | current `__revN` sibling/append | raw instruction length/attention pressure | human owner session |
| C4 | dirty only in project/task-owned paths | receipt claim corroborated now | historical replay plus explicit current bridge | dynamic task-local input, visible but not fixed-charged | foreign/customized content preserved | historical non-current grammar retained | conflicting/incompletely loaded instructions | human owner session |
| C5 | concurrent uncommitted framework update | newer/current state lacks a settled committed receipt | comparison unavailable until epoch settles | whole file | exact installed copy | current single-phase `TYPE__{ID}` | checkpoint placement/timing | shared device or several human principals |
| C6 | clean after committed update | receipt claim corroborated now | historical replay plus explicit current bridge | addressed heading/range | sole canonical owner | current `__revN` sibling/append | checkpoint placement/timing | selected-LEAD root session |
| C7 | dirty only in project/task-owned paths | receipt condition resolved later | successor measure with no equality claim | dynamic task-local input, visible but not fixed-charged | managed block projection | current phase `TYPE__phase-*` | native capability/readback limit | non-AT operational session with no named agent principal |
| C8 | clean but installed release is behind | receipt condition still visible | exact historical replay | deliberate repeated read | foreign/customized content preserved | historical non-current grammar retained | raw instruction length/attention pressure | shared device or several human principals |
| C9 | clean after committed update | receipt condition resolved later | historical replay plus explicit current bridge | whole file | managed block projection | historical non-current grammar retained | native capability/readback limit | selected-LEAD root session |
| C10 | concurrent uncommitted framework update | newer/current state lacks a settled committed receipt | successor measure with no equality claim | dynamic task-local input, visible but not fixed-charged | foreign/customized content preserved | current phase `TYPE__phase-*` | conflicting/incompletely loaded instructions | human owner session |
| C11 | dirty only in project/task-owned paths | receipt claim corroborated now | historical replay plus explicit current bridge | addressed heading/range | exact installed copy | current single-phase `TYPE__{ID}` | raw instruction length/attention pressure | selected-LEAD root session |
| C12 | clean after committed update | receipt claim corroborated now | successor measure with no equality claim | deliberate repeated read | sole canonical owner | current `__revN` sibling/append | checkpoint placement/timing | non-AT operational session with no named agent principal |

New combinations not proposed in the Briefing are now visible. For example, C9 combines a clean
receiver and retained historical filename readability with a native title/readback limit in a
selected-LEAD root session; C12 combines an artifact-complete committed receiver with no named
operational principal while preserving deliberate rereads and revision lineage. Neither combination
can be judged from raw corpus size alone.

## Findings

### E1: Receiver chronology separates committed state, working state and receipt epoch

| Receiver | Receipt/update epoch | Later/current observation | Relation that Extract can safely use |
|---|---|---|---|
| Helpdesk | 3.4.1 receipt sealed 2026-09-20 with 32 uncommitted update paths and concurrent, non-overlapping HEAD movement | `f53ed5d`, `beta`, clean; update commit `ba963dc` exists after the receipt | The update-process facts remain evidence; “32 uncommitted paths” is resolved current state, not a live defect. |
| SenseLab / KazNPU AI Lab | 3.1.0 receipt and commit `3d49558` on 2026-09-08 | `443eece`, `master`, 27 project-content paths dirty; config still 3.1.0 | Stale installed release and non-verifying build commands remain current configuration facts; current dirt is not update payload dirt. |
| AFD | 3.3.0 re-entry receipt and commit `c615a907` on 2026-09-14 | same HEAD; three task paths dirty, matching the receipt's AFD-46/AFD-51 boundary | Task dirt remains visible. Receipt-era lint/tests and singular-workflow observations stay historical until rerun. |
| RYC — epoch A | before receipt `UPDATE__20260920-231630__93b9` existed | `c5b49a9`, `master`, one untracked `.tfw/.upstream-source/` | A pre-update working snapshot; no actor or process is inferred from the path. |
| RYC — epoch B | receipt recorded 2026-09-20 23:16:30 +05:00 for 3.4.1 | 23:18:09 +05:00: same HEAD, 52 uncommitted paths (46 `.tfw`, five adapter paths, one `KNOWLEDGE.md`) | A separate, concurrent uncommitted update snapshot. Receipt authorship is recorded in the receipt, but this Researcher does not infer which live process changed the tree. |

The matrix challenges a receiver-wide “dirty equals failed update” rule. Dirty project work,
uncommitted framework application, receipt-era changes later committed, and clean-but-stale release
state are different configurations with different owners and evidence needs.

### E2: RCFR is exactly reproducible at its accepted candidate

The deleted audit was executed without restoring it to the live tree: a temporary detached worktree
at accepted candidate `25d0e89afe48144c79c11324ff09d300b76dd6e9` ran
`python -X utf8 docs/scripts/test_runtime_context.py --audit`, exited `0`, and was removed. It
reproduced:

```text
TRAJECTORY          before=310485  after=112206  reduction=63.9%
ACTIVE_TFW_CORPUS   before=66436   after=32088   reduction=51.7%
```

This establishes the historical selector and numbers. It does not make the deleted audit a current
runtime dependency.

The trace hierarchy now has three distinguishable epochs:

| Value | Source state | Disposition |
|---:|---|---|
| `112,210` / `32,092` | earlier Phase C audit and first review verification before the final four-word role correction | valid earlier candidate, superseded by the recorded return |
| `112,206` / `32,088` | RF return, REVIEW rev2/rev3 verification, final appended audit evidence, and fresh replay at `25d0e89` | terminal measured Phase C result |
| `112,536` / `32,088` | current `KNOWLEDGE.md` D75 only | unresolved publication inconsistency: D75 cites the terminal artifacts but disagrees with them; no successor/correction link exists |

The source hierarchy and successor search have therefore been tested explicitly. The measured
historical result reproduces at `112,206`; D75 remains an uncorrected trace inconsistency that this
Researcher may report but not edit.

### E3: A non-equal ten-command bridge quantifies current growth

The historical selector was loaded in memory, Resume was removed from `SECONDARY_COMMANDS` on both
the accepted and current sides, and the same discovery/count functions were applied to accepted
`25d0e89` and the current tree. This is an explicit ten-command bridge, not equality with the
published eleven-command headline.

| Surface | Accepted ten-command projection | Current ten-command projection | Change |
|---|---:|---:|---:|
| Canonical trajectory | 108,942 | 113,465 | +4,523 (+4.2%) |
| Unique active `.tfw` corpus | 31,529 | 37,045 | +5,516 (+17.5%) |

Per-command exposure under the same bridge:

| Command | Accepted | Current | Delta |
|---|---:|---:|---:|
| Plan | 24,638 | 26,213 | +1,575 |
| Research focused | 6,103 | 6,660 | +557 |
| Research deep | 6,168 | 6,725 | +557 |
| Handoff | 6,274 | 7,955 | +1,681 |
| Review | 25,090 | 27,819 | +2,729 |
| Docs | 14,845 | 18,812 | +3,967 |
| Knowledge | 14,148 | 2,966 | −11,182 |
| Release | 2,265 | 1,801 | −464 |
| Update | 2,350 | 6,477 | +4,127 |
| Config | 2,423 | 3,614 | +1,191 |
| Init | 4,638 | 4,423 | −215 |

The unique-corpus delta is concentrated but not yet classified as removable:

| Selected source | Accepted | Current | Delta | Structural topic visible from history/headings |
|---|---:|---:|---:|---|
| `.tfw/conventions.md` | 6,068 | 8,481 | +2,413 | value accounting, session/AT identity, task state/closure, knowledge lifecycle, authority and scope |
| `.tfw/workflows/update.md` | 756 | 2,495 | +1,739 | update provenance, exact-path ownership, migration, receipt and cleanup behavior |
| `.tfw/README.md` | 640 | 1,984 | +1,344 | North Star and methodology/value material |
| `.tfw/workflows/handoff.md` | 1,751 | 2,327 | +576 | execution/return/identity behavior |
| `.tfw/templates/update_receipt.md` | 0 | 554 | +554 | new durable update-result form |
| `.tfw/templates/HL.md` | 1,994 | 2,530 | +536 | contract/architecture fields |
| `.tfw/workflows/review.md` | 1,894 | 2,385 | +491 | independent review/accounting/return behavior |

Within selected convention ranges, the largest increases are `Task Statuses` +680, `Scope Budgets`
+522, `HL (High Level)` +278, the three knowledge use/handover/qualification ranges +680 combined,
value-bearing classification/accounting/decomposition +588 combined, and `Session identity` +166.
This pattern weakens any claim that all growth is mere repeated wording: it includes newly introduced
behavior. It simultaneously supports H4's narrower concern that identity, authority, closure and
exception rules are concentrated in a few high-exposure owners. Challenge must distinguish
irreducible additions from duplicated expression.

### E4: Actual rule, reader and copy relationships are bounded and currently coherent

| Surface | Normative owner / producer | Actual readers or delivery sites | Observed relationship |
|---|---|---|---|
| Command algorithms | ten `.tfw/workflows/*` entries, with Research at `research/base.md` | Claude Code and Antigravity command targets copy workflows; Codex skills dispatch to workflows; Cursor targets are not installed in this repository | Codex 10/10 skill pairs byte-equal; Claude Code 10/10 and Antigravity 10/10 workflow pairs byte-equal. Missing Cursor targets are absence of that installed adapter, not demonstrated drift. |
| Persistent entry rules | provider templates named by `manifest.yaml` | root `AGENTS.md`, root `CLAUDE.md`, `.agents/rules/tfw.md`; Cursor persistent target absent | Codex and Claude managed blocks equal their template blocks; Antigravity rule equals its template. |
| Adapter topology | `.tfw/adapters/manifest.yaml` (tooling-only) | Update, Init and Config read it at adapter gates | One map owns source/target/strategy; runtime roles do not treat the manifest as substantive authority. |
| Session title rendering | `.tfw/conventions.md` → `Session identity` | Plan, Research, Handoff, Review, Docs and Init read the named range | One shared rendering owner; checkpoints are workflow-local. |
| Acting-principal selection | `.tfw/conventions.md` → `Which handle a machine acts as`; inline `Who Is Acting` tables in Research, Handoff and Review | Those three operational workflows execute the binding/question branch | The rule is expressed in a shared range and repeated inline in three workflow algorithms; whether that duplication is required or compressible remains for Challenge. |
| Artifact naming | `.tfw/conventions.md` → `Artifact file naming` | Plan produces HL/TS; Handoff consumes TS and produces ONB/RF; Review consumes TS/RF/EV and produces REVIEW | The naming owner is single, but producer templates do not emit their output path themselves. |

No byte-drift defect was found in the currently installed Codex, Claude Code or Antigravity delivery
sets. The Extract finding is therefore about reader topology and repeated semantics, not a present
copy mismatch.

### E5: Filename production is one normative grammar with an incomplete last mile

| Artifact | Producing workflow | Current normative filename | Producer instruction | Consuming workflow behavior | Historical compatibility |
|---|---|---|---|---|---|
| Master HL | Plan | `HL-{ID}.md` | Plan reads naming range and opens HL template | Plan/task state resolves authority by exact task | existing historical whole-ID/legacy forms remain readable |
| Iteration RES | Research | `research/iterN/RES.md` | Research workflow states exact path | Plan reads iterations/RES lineage | separate from single-phase root `RES__{ID}.md` rule |
| Single-phase TS | Plan | `TS__{ID}.md` | “Write TS” opens generic template; no literal output filename in template/step | Handoff reads highest approved TS lineage | CRUE's `TS-TFW_...md` is observed history, not a current producer rule |
| Phase TS | Plan | `TS__phase-{x}__{title}.md` | topology chosen before template write | Handoff selects governing phase lineage | current examples match double-underscore form |
| TS revision | Plan after REVIEW ruling | `TS__{ID}__rev{N}.md` or phase equivalent | Plan says one approved TS revision; Handoff names the single-phase form explicitly | Handoff requires highest approved sibling | unsuffixed revision 1 remains immutable |
| ONB / RF | Handoff | `ONB__{ID}.md` / `RF__{ID}.md` or phase equivalents | opens templates; steps say create/write file without literal complete name | Review reads RF/EV by selected task/phase state | RF/ONB append on returns rather than create revision siblings |
| REVIEW | Review | `REVIEW__{ID}.md` or phase equivalent | workflow says `REVIEW__*.md`; template has no literal path | Plan/Handoff read live verdict and revision lineage | REVIEW revisions use `__revN` siblings |

Search of current workflow/template/skill sources found no rule authorizing new `TS-{ID}` or
`RF-{ID}` issuance. H10 therefore has two distinct parts: the competing current grammar is not
supported; the producer last mile is incomplete because generic templates assume `/ Phase {X}` and
do not state an output filename. Historical precedent can fill that gap incorrectly when a producer
does not follow the named convention range.

### E6: Principal resolution is a conditional trace problem, not a title or authority shortcut

| Scenario | Facts already carried elsewhere | What a stable principal could add | Failure mode if principal resolution is skipped or unconditional |
|---|---|---|---|
| one declared human profile | owner/accountable human, workflow role, task/gate | attribution without a question | little ambiguity; current rule already selects silently |
| owner-launched non-AT operational role with human+agent profiles | task address/state, human owner, role, gate recipient, actual `via`; optional `writer` may be omitted | optional durable agent authorship only | unconditional question interrupts even when no stable agent attribution or mandate is needed |
| selected-LEAD root session on the same repository | mandate, root unit address, role, parent, human-rooted chain | stable cross-session delegation/provenance and LEAD title qualification | one project-root binding cannot distinguish this from the owner-launched operational session |
| shared device or several human principals | role/task alone does not say which accountable human is acting | accountability attribution | skipping the question can misattribute a human act; conditional resolution must preserve this safety case |
| AT child operational unit | actual unit address, parent, scope, channel, dispatch and origin carry authority | shared principal attribution may aid provenance | treating a shared principal as authority merges units and creates an invalid mandate shortcut |

This structure refines H11 without deciding it. The present question was correct under current rules;
the candidate change is to make the need for principal attribution conditional while retaining the
multiple-human/shared-device branch. H12 and later owner inputs about a persistent human-facing LEAD,
single mutating lane and sibling collisions are preserved for iteration 2; no additional scan or
architecture selection was added here.

### E7: Iteration-1 hypothesis map before Challenge

| Hypothesis | Extract state | Evidence boundary |
|---|---|---|
| H1 / H9 | open, narrowed | One Codex title mutation/readback succeeded; the identity question occurred after title resolution. This separates title capability from principal attribution but proves no provider-wide cause. |
| H4 | mixed evidence | Ten-command active corpus is +17.5%; growth is concentrated, but the largest ranges include new accounting, knowledge and update behavior as well as identity/closure/authority prose. |
| H5 | plausible but not universal | The four receivers expose concurrency, ownership and weak verification, yet Helpdesk is now clean and dirt types differ. |
| H8 | open | Historical guarantees reproduce; current growth is measurable. Smaller-current feasibility still requires identifying which additions are duplicate versus necessary controls. |
| H10 | partially supported | One current grammar exists; producer/template instructions leave room for historical precedent to be copied incorrectly. |
| H11 | requires conditional test | Current prompt has a real safety case; same-root owner/LEAD and no-principal operational sessions are not represented by one project-root binding. |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| RCFR exact replay succeeds at the accepted candidate without restoring deleted tooling. | Challenge the ten-command bridge, denominator choices and whether the current increase reflects necessary behavior or duplication. |
| The ten-command bridge shows +4.2% trajectory and +17.5% unique active-corpus growth. | Attack the bridge with alternate selectors and identify any hidden omitted/repeated/current-only edge. |
| Receiver chronology distinguishes resolved, stale, project-dirty and concurrently updating states. | Seek counterexamples to H5 and avoid converting four cases into a universal update theory. |
| Installed Codex/Claude/Antigravity copies and persistent projections are coherent. | Challenge semantic duplication and reader necessity even where bytes are intentionally equal. |
| Current filename grammar is singular; producer/template last-mile wording is incomplete. | Test whether actual consumers need an additional form or whether explicit emission alone closes H10. |
| H11's safety and conditional-attribution cases are explicit. | Challenge against multiple-human, shared-device, same-root owner/LEAD and AT-child counterexamples without entering iteration-2 architecture selection. |

**Sufficiency:**
- [x] External source used? — immutable Git candidate, historical audit source, live workflows/templates/manifest, receiver Git states and receipts.
- [x] Briefing gap closed? — chronology, reproducible measurement bridge, actual reader/copy map, filename producer/consumer map and conditional identity cases are explicit.
- [x] Configuration Space built from Gather dimensions? — twelve non-contradictory families use all eight dimensions.

Stage complete: YES
→ User decision: pending Coordinator gate
