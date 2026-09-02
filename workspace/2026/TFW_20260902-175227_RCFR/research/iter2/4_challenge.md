# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260902-175227_RCFR](../../HL-TFW_20260902-175227_RCFR.md)
> Goal: Reduce mandatory runtime context by at least 30% for each primary role without changing methodology meaning, lifecycle guarantees, or supported-adapter behavior.

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| Knowledge cursor | processed source set | Candidate accounting | candidate-bearing tasks | a candidate added later to an old/no-candidate task can remain behind the cursor |
| Knowledge cursor | rebuild every run | Candidate accounting | artifacts only | with no persisted comparison, no-op and interval delta cannot be distinguished from the complete corpus |
| Retry consistency | transaction journal | Historical/addition policy | subtraction-first contract | a new runtime transaction artifact is unnecessary because state-last plus dedup is idempotent |
| Adapter parity | byte equality | Clean-context proof | semantic fixtures | equality proves only present copies; a missing command or wrong vendor directory disappears from the sample |
| Historical retention | keep inline | Glossary/runtime reduction | mandatory whole sections | preserves the human-facing resident material DoD 9 requires removing and weakens H3 |
| Normative addressing | generated packet | Adapter parity | command-resolution contract | a generated role input becomes a second runtime authority unless generation and source equivalence become a new gate |

**Surviving configurations:**

| Config | Normative addressing | Glossary runtime | Knowledge cursor | Retry | Proof | Adapter parity | History | Notes |
|--------|----------------------|------------------|------------------|-------|-------|----------------|---------|-------|
| C9 | exact heading range | query + addressed PV | task-section digest/all tasks | state last | deterministic fixtures | exact commands/roles | source links | minimum architecture; selected |
| C10 | compact rule blocks | compact index + addressed PV | task-section digest/all tasks | state last | fixtures + model eval | exact commands/roles | maintainer appendix | valid later compaction if C9 fixtures stay green |

**Unexpected survivor:** C10. Physically extracting compact rule blocks is not required to meet the target, but it remains compatible with the one-authority model if the original mixed sections cease to be a second normative owner. It is a post-C9 optimization, not a prerequisite and not a separate runtime view.

## Findings

### C1: The digest cursor survives every required replay

A temporary, read-only PowerShell model used SHA-256 over canonical task/section strings and compared prior/current maps. No repository source or state was changed.

| Replay | Expected | Observed | Verdict |
|---|---:|---:|---|
| K0 identical map/no-op | 0 pending | 0 | pass |
| K1 four new tasks below interval 5 | 4 | 4 | pass |
| K2 five new tasks at threshold | 5 | 5 | pass |
| K3 retry after fact write/source marker but before state | 1 | 1 | pass |
| K4 absent map migration over repository task population | 61 | 61 | pass |
| K5 equal timestamp, distinct ABBR | 2 | 2 | pass |
| K6 changed candidate body | 1 | 1 | pass |
| K7 new no-candidate task | 1 | 1 | pass |
| K8 late candidate added after empty digest | 1 | 1 | pass |
| K9 prior task disappears | hard-stop input detected | 1 removed | pass |

Attack 1—self-changing processed markers: if the marker lies inside a selected section, writing it changes the digest. The algorithm remains correct only if the final map is recomputed after all approved markers/fact changes, immediately before the state-last write. R25/R27 must say this explicitly.

Attack 2—retry after partial write: facts may exist while the old map remains. The task is still pending; existing deduplication prevents a duplicate row, derived statistics prevent a duplicate increment, and the recomputed final digest converges. A workflow that increments stats or copies the pre-write digest fails K3.

Attack 3—no-candidate threshold: five ordinary tasks can trigger a hard gate and yield no new facts. That is not a false positive: the configured interval counts tasks, not facts, and the consolidation records that those task candidate surfaces were examined. The final write may update only state/audit totals. Restricting the cursor to candidate-bearing tasks would silently change interval semantics and fail K8.

Attack 4—map growth: one 64-hex digest per resolved task is linear. The current 61-task repository makes the first map bounded, and only the checker/knowledge workflow reads it. The field has one reader family and one job and replaces an uncomputable sequence field, so it passes DoD 13. If growth later becomes operationally significant, state can be partitioned without changing digest semantics; no partition is justified now.

Attack 5—hash meaning: collision resistance/change detection does not verify truth. The existing Human-Only, deduplication, contradiction, source-count, and two human WAIT gates remain unchanged. Git's official content-addressing documentation supports independently detecting content changes, not interpreting them ([Git hash-function transition](https://git-scm.com/docs/hash-function-transition.html)).

Result: C9's cursor is selected. Timestamp, sequence, path-only, candidate-only and rebuild-every-run alternatives are eliminated.

### C2: Exact ranges clear the threshold under adverse counting

The weakest primary-role reduction is Coordinator at 53.1%, still 23.1 percentage points above the requirement. Adding the 420-word PV router to both Coordinator and Reviewer, retaining both independent PV source scans, retaining the Review Purpose Check reread, using current uncompressed workflows/templates, and counting deep mode all make the target more conservative. Removing §14.1 compatibility history from ordinary Researcher/Executor packets lowers their exact targets without deleting the query route.

| Path | Candidate | Current | Reduction | Adverse condition retained |
|---|---:|---:|---:|---|
| Coordinator | 25,620 | 54,610 | 53.1% | full independent PV + exact router |
| Researcher focused | 6,051 | 34,057 | 82.2% | whole operative anti-pattern range |
| Researcher deep | 6,084 | 34,090 | 82.2% | deep-mode delta |
| Executor | 7,220 | 64,738 | 88.8% | evidence/safety and operative anti-patterns |
| Reviewer | 26,881 | 83,875 | 68.0% | full independent PV + Purpose Check reread |
| Docs | 14,752 | 45,404 | 67.5% | current 13,769-word KNOWLEDGE §§1–3 |
| Knowledge | 11,840 | 65,526 | 81.9% | all 9,594 topic words and state/config/template |
| actual two-iteration trajectory | 98,448 | 382,267 | 74.2% | focused iter1 + deep iter2 + both closures |

Attack—anchor drift: research line numbers cannot become the runtime contract. Unique headings are the address; the audit resolves them and fails on absent/duplicate anchors. After implementation, raw before/after output must be retained in phase evidence. If a section is compacted, its measured target may decrease but may not substitute a different semantic packet.

Attack—dynamic reads hidden from the baseline: task artifacts and relevance-triggered knowledge are excluded on both sides. They must still appear in the manifest when triggered, but are not claimed as savings. A phase that removes a required task read cannot use that removal to pass the metric.

Result: H4's numerical claim is confirmed with exact current ranges. Behavioral confirmation belongs to the paired phase fixtures and cannot be inferred from these counts.

### C3: A clean receiver exposes four different adapter outcomes

A temporary empty directory was populated using the current `init.md` mappings; it was deleted after the check. Expected command set size was 11.

| Adapter | Current clean-receiver result | Why self-hosting hid it | Required candidate result |
|---|---|---|---|
| Claude Code | 10/11; `research` missing | current repository already has 11 manually/successfully copied commands | 11/11 from explicit map including nested `research/base.md`; Researcher role |
| Cursor | 0/11 custom commands | Cursor adapter is not selected/installed in this repository | 11/11 `.cursor/commands`; compact `.cursor/rules/tfw.mdc` |
| Antigravity | 10/11 under obsolete `.agent/workflows`; 0/11 under official `.agents/workflows`; rule source path absent | current repository has 11 equal copies under the obsolete singular directory | 11/11 under `.agents/workflows`, rule under `.agents/rules`, explicit Research source |
| Codex | 11/11 skills | current init has a complete explicit adapter install contract | keep 11/11; remove duplicate preloads; exact role/read manifest |

The root `.tfw/workflows/*.md` glob contains 10 files and necessarily omits nested `research/base.md`. The Antigravity init rule source `.tfw/adapters/antigravity/rules/` does not exist. Current Claude template and README both label `/tfw-research` as Coordinator. Current Cursor adapter has no command sources. Existing installed Claude, singular Antigravity and Codex bodies matching their sources is therefore counter-evidence against generic copy corruption but does not rescue clean installation.

Official discovery contracts decide the destination paths: Cursor custom commands use `.cursor/commands`, Claude's legacy `.claude/commands` remains supported, and Google documents Antigravity workspace rules/workflows under plural `.agents/rules` and `.agents/workflows`. Google also explicitly distinguishes always-on rules from on-demand workflows and warns that loading everything creates context bloat ([Google Antigravity customization and skills](https://codelabs.developers.google.com/getting-started-agy-ide), especially workspace locations and progressive disclosure). These findings make R34–R39 correctness repairs, not optional context optimization.

Attack—vendor UI unavailable: Cursor is not installed on this host. A live UI claim would be fabricated, so the required gate is a deterministic clean-receiver packaging/command-role fixture against the official discovery contract. Optional live smoke tests can supplement but never replace it. This preserves portability and gives all adapters the same test.

### C4: Semantic fixtures are adequate only when their grader ignores prose resemblance

The G3 record schema compares decision, refusal reason, artifact create/modify set, citations and gate. This detects the frozen failure modes: silent amendment, implementation before ONB clearance, unsupported VERIFIED, APPROVE after purpose failure, review round without citation, docs/knowledge ownership crossing, and stale-index resumption. Read manifests are separately compared to prove the intended context reduction.

Counterexample: a candidate can copy the baseline's final sentence while having skipped the evidence file. A text-similarity grader would pass; the structured record fails `citations`, `gate`, and `read_manifest`. Conversely, wording may differ while all behavioral fields match; that is equivalent under the frozen “meaning fixed, representation open” principle.

OpenAI's official Eval API defines an evaluation as testing criteria plus a data-source schema, which supports fixture rows with explicit semantic fields rather than unstructured prose comparison ([OpenAI Evals API](https://platform.openai.com/docs/api-reference/evals/deleteRun?lang=python)). Official model guidance says to remove one instruction group at a time and rerun the same representative evals; it treats token reductions as improvements only when the final result still passes existing evaluations ([OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model)).

The candidate implementation does not yet exist, and the Researcher is forbidden to edit test/code surfaces in this iteration. Therefore this stage can specify and structurally review the paired fixtures but cannot honestly report a candidate model run. This is an implementation acceptance condition, not a third-research-iteration question: inputs, output schema, expected behavior, deliberate mutants and phase ownership are all fixed by G3/R28–R30.

### C5: The deletion ledger survives sole-carrier and trace-loss attacks

The named durable history anchors were resolved in the repository: D61, D63, D68, D69 and D72 exist in `KNOWLEDGE.md`; TFW-53, TFW-54, TFW-60, TLD and RDP research/RF/REVIEW traces exist; both `tasks/DEBT-SNAPSHOT.md` and `tasks/BOARD-SNAPSHOT.md` exist. G4 gives every candidate block an operative owner and a fixture/test; historical blocks additionally have a durable source.

Attack—history link is itself broad context: history references are lookup routes, not mandatory reads. Ordinary workflows do not traverse them. Research triggered by a compatibility or regression question may read the exact decision/trace. This preserves discoverability without residency.

Attack—glossary loses comprehension: every term heading survives as a one-sentence discriminating definition and authority link, and PV remains an addressed operational exception. A fresh agent can answer “what is it?” from the glossary and “what do I do?” from the one owner. G3 fixtures fail if an authority link is insufficient to reproduce a refusal or artifact boundary.

Attack—§14.1 is the only old-term decoder: it is retained as maintainer-only query history and omitted only from fixed role packets. Thus compatibility is not deleted, but no ordinary execution pays for it.

Result: H2 and H3 are confirmed at the architecture/specification level. Their implementation gate is deletion-by-deletion link resolution plus paired fixtures; no mapped paragraph may be removed earlier.

### C6: Remaining gaps are implementation evidence, not unresolved research choices

| Gap | Classification | Required owner/stage |
|---|---|---|
| candidate paired runs have not occurred | expected: candidate is unimplemented and Researcher cannot edit code/tests | Phase A establishes baseline/fixture harness; each phase runs affected pairs |
| Cursor live UI was unavailable | non-blocking: deterministic official-path fixture covers framework contract | optional adapter smoke evidence in affected phase |
| final compact prose word counts are unknown | non-blocking: exact current-range upper bounds already pass all thresholds | each implementation RF records actual after count |
| current task validator reports two unrelated repository-state problems | pre-existing, out of research scope; must be reported by migration, not repaired here | Coordinator disposition / owning tasks |
| exact vendor behavior may evolve | normal compatibility risk | pin official contract date in evidence and keep receiver fixture current |

No additional alternative, cursor rule, fixture dimension, history carrier, or adapter mapping remains undecided for a TS. A third research iteration would rerun an implementation test before there is an implementation, not reduce design uncertainty.

## Deep-mode Decisions and Metacognitive Check

1. **Selection:** C9 is the recommended implementation architecture; C10 is permitted only as a later, fixture-preserving compaction of the same authorities. C11–C14 are eliminated.
2. **Sufficiency:** recommend `SUFFICIENT` for Coordinator classification and TS authoring. The recommendation is not approval to edit frozen HL or start implementation.
3. **Behavioral bar:** H2/H3 are confirmed as mapped designs and H4 is numerically confirmed; their observable implementation status remains gated by the paired fixtures rather than upgraded by prose confidence.

Metacognitive check: this research could overstate “clean-context proof” because only the baseline packaging and abstract cursor exist today. It therefore distinguishes fixture specification from future candidate execution and refuses to call the latter complete. It could also overfit to this self-repository; the empty-receiver check exposed precisely that risk. Finally, content hashing can look more rigorous than it is: the digest only says the selected source changed, while humans and current knowledge gates still determine whether a fact is valid.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C9 survives pairwise attacks; K0–K9 replay passes; exact role/closure counts pass; current clean install fails Claude/Cursor/Antigravity in distinct measurable ways and passes Codex command completeness; every deletion has owner/test/history routing; all five iteration-2 directions have implementable closure. | Candidate execution evidence, final after-counts and optional live Cursor smoke test belong to implementation phases, not more research. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked? Surviving configurations listed?

Stage complete: YES
→ User decision: pre-authorized synthesis into iteration-2 RES; do not start iteration 3.
