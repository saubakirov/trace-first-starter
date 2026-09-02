# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260902-175227_RCFR](../../HL-TFW_20260902-175227_RCFR.md)
> Goal: Reduce mandatory role context by at least 30% without changing TFW meaning, algorithms, authority boundaries, gates, or guarantees.

## Configuration Space

Representative configurations are shown because the seven-dimension cross-product is larger than 30. Each row changes at least one Gather dimension from the current configuration.

| Config | D1 common bootstrap | D2 normative ownership | D3 terminology | D4 knowledge | D5 history | D6 stale/compatibility | D7 validation |
|--------|---------------------|------------------------|----------------|--------------|------------|------------------------|---------------|
| C1 current | full four-file foundation | monolithic conventions plus workflow copies | full glossary | full KNOWLEDGE for core roles | inline | active and historical mixed | carrier word totals |
| C2 compact monolith | compact common kernel | shortened monolithic conventions | query-only glossary | addressed PV sections | same-file appendix | compatibility appendix | graph totals + scenarios |
| C3 addressed hybrid | `AGENTS.md` router only | workflows own role algorithms; addressed convention sections own shared invariants | query-only term router | Coordinator/Reviewer PV scan; Researcher/Executor citations | task traces/CHANGELOG/human essay | delete active stale rules; keep addressed compatibility only | static graph + word totals + clean-context scenarios |
| C4 split by role | compact kernel | four role normative sources | inline definitions | addressed PV sections | appendices | compatibility appendix | per-role replay |
| C5 persistent generated views | generated role bootstrap | fragments compiled to checked-in role views | generated term subset | generated relevance index | generated links | generated compatibility subset | compare generated outputs |
| C6 ephemeral compilation | `AGENTS.md` router | authoritative workflow + addressed fragments compiled only in memory | query-only glossary | live query over authorities | source links | executable compatibility tests | generated replay, no stored view |
| C7 workflow-only | `AGENTS.md` router only | every rule needed by a role lives in that workflow | inline definitions | citations only, including Reviewer | history absent | stale removed | scenario tests only |
| C8 addressed hybrid + audit-only manifest | same as C3 | same as C3 | same as C3 | same as C3 | same as C3 | same as C3 | generated read manifest is evidence only, never a runtime input |

The non-obvious configuration is C8: generation is useful without generating a role's instructions. A generated manifest can measure and fail drift while the role still reads authoritative source sections. This keeps the benefit of generated views—mechanical coverage—without creating the second operational authority prohibited by HL DoF 7.

## Findings

### E1: Selection architecture dominates sentence compression

The primary reduction does not require shrinking current workflows or templates. It comes from removing broad preloads and duplicate edges:

- Researcher can stop reading 30,432 words (`conventions + glossary + KNOWLEDGE`) before its 1,090-word algorithm.
- Executor and Reviewer each lose one duplicate 30,828-word foundation immediately when only one layer owns context selection.
- Coordinator and Reviewer keep their independent PV algorithms; the sources can be addressed without becoming optional.
- Secondary commands stop inheriting glossary/knowledge/history that their decision does not use.

Official Codex documentation confirms that `AGENTS.md` is discovered and concatenated into the instruction chain once at session start; it is already active before command work begins ([OpenAI: Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)). A skill instruction to read the same root `AGENTS.md` again is therefore an observable duplicate in Codex. Official Skills documentation describes skills as modular instruction bundles for processes and conventions ([OpenAI: Skills](https://developers.openai.com/api/docs/guides/tools-skills)); this supports using the skill as a command router while the canonical workflow owns its algorithm and exact step inputs.

### E2: Conservative after-model clears 30% without PV weakening

The following is a feasibility model, not an implemented after-measurement. It leaves every current skill, role workflow, template, and PV priority 0–4 source at its current word count. It removes full-file `conventions/glossary/KNOWLEDGE` preloads, removes duplicate context edges, and allocates up to 3,200 words per primary role for addressed shared rules. The 3,200 allowance exceeds the present combined size of the main cross-role guard surfaces once incident rationale is not reread: contract rules, role-lock routing, safety/trace rules, and checkpoint-specific status grammar. No PV item is dropped.

| Path | Known fixed current exposure | Conservative addressed target | Reduction | 30% passes? |
|---|---:|---:|---:|---|
| Coordinator | 54,610 | 24,193 | 55.7% | yes |
| Researcher | 34,057 | 6,801 | 80.0% | yes |
| Executor | 64,738 | 6,678 | 89.7% | yes |
| Reviewer | 83,875 | 25,815 | 69.2% | yes |
| `/tfw-docs` closure | 45,404 | 15,754 | 65.3% | yes |
| `/tfw-knowledge` closure | 65,526 | 12,203 | 81.4% | yes |

The task requires at least two research iterations. A complete fixed path of Plan + Research ×2 + Handoff + Review + Docs + Knowledge is currently at least 382,267 words before variable task artifacts. The conservative addressed target is 98,245 words, a 74.3% reduction. Dynamic task artifacts remain on both sides of the comparison and are not claimed as savings.

This model also clears the frozen HL carrier ceilings. The carrier-only target does not include the PV and closure reads that its carrier baseline excluded; removing the three broad files from the common carrier alone leaves every primary role far below its 30% ceiling.

### E3: Secondary Coordinator checkpoints have the same defect

| Command | Current fixed or directly computable exposure | Duplicate/stale edge | Addressed form |
|---|---:|---|---|
| `/tfw-docs` | 31,415 carrier; 45,404 after workflow rereads KNOWLEDGE | skill loads full KNOWLEDGE, workflow reads it again | workflow reads only KNOWLEDGE §§1–3 once plus selected RF/REVIEW |
| `/tfw-knowledge` | 41,780 carrier; 65,526 after workflow rereads state, KNOWLEDGE and all 9,513 topic-file words | skill and workflow independently own prerequisites; sequence cursor is obsolete | workflow owns one read of state, KNOWLEDGE §4, all topics, and unprocessed candidate sources |
| `/tfw-resume` | 31,759 before task artifacts | full foundation plus obsolete `HL__Phase*` discovery | status-first, then current phase directories and governing artifact revisions |
| `/tfw-config` | 18,503 | full conventions/glossary despite one registry task; registry points to inline sections absent from `plan.md` and `knowledge.md` | config + registry + only named target sections; repair registry subjects |
| `/tfw-release` | at least 42,437 before task state; workflow rereads release/version/changelog | the 24,360-word CHANGELOG is loaded whole and then used by release range | `RELEASE.md`, VERSION, and only `[Unreleased]` plus entries since last tag |
| `/tfw-update` | at least 43,321 before target workflow | full installed CHANGELOG before target is pinned, then target workflow becomes authority | installed workflow only through pin; target workflow and intervening target entries after pin |
| `/tfw-init` | project-variable | tutorial carries `RND-1` examples and a dirty-clock root RES naming rule | current clock+ABBR examples and current `research/iter1/RES.md` topology |

The closure commands matter to the “working trajectory” requirement: Review does not reach DONE without Docs/Knowledge disposition. Treating them as secondary would hide 110,930 fixed words from the strict end-to-end baseline.

### E4: Concrete change catalogue

These are implementation recommendations, not changes made by the Researcher.

| # | File / section | Delete, merge, or redirect | Proposed operational wording | Reason |
|---|---|---|---|---|
| R1 | `AGENTS.md` Context Loading block | delete the four-file universal preload; keep conduct and command routing | “For a `/tfw-*` command, load its local skill. Task state is read before global libraries; the selected workflow names every additional input.” | Codex already loads AGENTS once; role selection belongs downstream |
| R2 | `.agents/skills/tfw-*/SKILL.md` and `.tfw/adapters/codex/skills/tfw-*/SKILL.md` | remove common-file and role-artifact lists duplicated by workflows | “Read the canonical workflow completely. It owns context order, gates, and stops. Do not preload framework libraries unless that workflow names a section at the current step.” | one owner for the graph; installed and source copies remain byte-checkable |
| R3 | `.tfw/conventions.md` §10 | replace “AGENTS, full conventions, full glossary, full KNOWLEDGE” with a resolver | “1. AGENTS is already active. 2. Read selected `status.md` and journal. 3. Read the role workflow. 4. Read the governing task artifacts it names. 5. Read only addressed shared-rule and PV sections triggered by the current checkpoint.” | makes progressive disclosure normative and measurable |
| R4 | `.tfw/conventions.md` §§3–5, §14–§15 | keep operative clauses in current sections; move incident narratives and measured origin stories to a non-runtime rationale appendix or their task sources | Each operative rule becomes “condition → required act/refusal → authority”; append “Rationale: {source task/decision}” as a link, not a narrative | preserves meaning while removing history from mandatory addressed sections |
| R5 | `.tfw/glossary.md` | stop mandatory loading; collapse mechanic-heavy articles to one-sentence definitions plus owner links | “`Revision` — repair ordered in the governing TS sibling; algorithm: conventions §5; file grammar: conventions §4.” | terms remain discoverable; mechanics cannot drift into a second authority |
| R6 | `.tfw/glossary.md` retired Debt Registry / Task Board articles | move under “Historical terms — lookup only” or redirect to `KNOWLEDGE.md` §3 and snapshots | “Historical term. Not used by current workflows. See {snapshot/decision}.” | preserves old trace readability without runtime residency |
| R7 | `KNOWLEDGE.md` loading contract | delete universal full read; keep Coordinator/Reviewer PV scan, Researcher/Executor citation-driven access | “Coordinator and Reviewer scan current D-record captions and sources in §1 independently. Researcher and Executor read exact HL §7.2 citations plus newly relevant items.” | preserves independent review and cross-task knowledge without irrelevant §2–§3 history |
| R8 | `KNOWLEDGE.md` §1 D-record rows | retain decision/status/source in the scan surface; redirect long failure narratives to source RF/REVIEW/RES | “Decision: {current claim}. Status: current/superseded. Source: {artifact}. Rationale and evidence: source.” | makes “scan all decisions” possible without deleting evidence |
| R9 | `.tfw/workflows/plan.md` Step 1 and footer | replace broad load and repeated §14/§5 reads with exact addressed checks | “Load status/journal, current task authority, PV scan, and the numbered rule sections cited by the step. At submit, run the compact Coordinator self-check; do not reread all anti-pattern history.” | preserves gates; removes third §14 exposure |
| R10 | `plan.md` Step 2 + `knowledge.md` Orient/Update + `knowledge_state.yaml` semantics | remove `current_seq` and `last_consolidation_seq` arithmetic | Candidate wording for iteration 2 validation: “Count distinct tasks with candidate-bearing RES/RF/REVIEW sections not marked processed; compare that count with `tfw.knowledge.interval`. Store the last consolidation timestamp in the existing date field at timestamp precision.” | current identifiers have no sequence; exact cursor semantics still need compatibility testing |
| R11 | `.tfw/workflows/handoff.md` Context Loading + Phase 1 | own the one Executor read list here; remove the later generic “Read all context” repeat | “Read once, in order: status/journal; master/phase HL; governing TS; prior REVIEW only on revision; exact cited/referenced files. Reopen only the section named by a later gate.” | eliminates two task-artifact rereads and one full foundation duplicate |
| R12 | `handoff.md` ONB/RF structure prose | delete copied section skeletons and mandatory-section essays; keep gates | “Copy `templates/ONB.md` and fill every section before WAIT.” / “Read RF headings at the Pre-RF Gate, then fill `templates/RF.md`; the template owns section grammar.” | algorithms in workflow, form in template |
| R13 | `.tfw/workflows/review.md` Context Loading / Steps 1–4 | own one baseline/task list and name partial reopenings; no second foundation | “Read status/journal; contract baseline; current Phase HL; governing TS; RF/EV/ONB; changed files. Map, Verify, and Judge reopen only their named sections.” | independent verification remains; duplicate loading leaves |
| R14 | `review.md`, `templates/review/judge.md`, `templates/REVIEW.md` Purpose/Disposition material | choose `judge.md` as check authority and conventions §5/§15 as routing authority; delete repeated incident rates and explanatory copies from REVIEW | Workflow wording: “Apply judge.md row 2 and conventions §5 routing; REVIEW records the result and citation.” | keeps structural check while preventing three normative statements |
| R15 | `.tfw/templates/RF.md`, `RES.md`, `REVIEW.md` repeated Fact Candidates / Strategic Insights blocks | move shared classification test to one addressed template fragment or compact one-line pointer; retain field-local empty-value instruction | “Record only human-sourced project knowledge; full test and categories: conventions §10.1.” | same cognitive rule currently occupies every writing template |
| R16 | `.tfw/workflows/resume.md` Phase 2 Step 5 | delete `HL__Phase*`/`TS__Phase*`/… glob | “Enumerate task child directories containing `status.md`; for each, read that state and the highest governing TS/REVIEW revision under conventions §4.” | current folder/state grammar, no legacy false negatives |
| R17 | `.tfw/workflows/init.md` Tutorial examples and Phase 3 | delete `RND-1` sequence examples, pseudo-board rows, dirty-clock root RES path | “Example task: `RND_20260902-123456_SAD` for *Sales Analysis Dashboard*.” / “Research writes `research/iter1/RES.md`.” | active onboarding must not teach retired grammars |
| R18 | `.tfw/workflows/config.md` Config Sync Registry | remove rows whose claimed inline subjects do not exist, or restore compact Pattern-A values at those exact sites | `plan.md`: “Defaults 50 files / 50 new / 5,000 LOC / 50 modified; config: `tfw.scope_budgets`.” `knowledge.md`: compact inline defaults for interval/gate/limits | D24 requires real inline enforcement; a registry pointing at absent rows is stale |
| R19 | `.tfw/workflows/docs.md` and `knowledge.md` plus their skills | make workflow the sole prerequisite owner; remove skill duplication | Docs reads KNOWLEDGE §§1–3 once. Knowledge reads state, KNOWLEDGE §4, topics, and candidate sources once. | saves 37,735 repeated words across closure before task variables |
| R20 | `.agents/skills/tfw-release`, `tfw-update`; corresponding workflows | stop full CHANGELOG preload | “Read only `[Unreleased]` and entries after the last project tag / between installed and target versions.” | the 24,360-word history has no decision use for a bounded version range |
| R21 | validation surface in Phase A | add a generated read-graph report only as test/evidence output; do not make roles read it | Report columns: command, checkpoint, source range, reason, words, repeat-of edge, authority. Fail on unknown full-library edge or >baseline regression. | generation detects drift without becoming source of truth |

### E5: Authority map after C8

| Information class | One authority | Other carriers |
|---|---|---|
| bootstrap conduct and command recognition | `AGENTS.md` | skills point to command workflow |
| role algorithm, role lock, gates, stops | selected workflow | skill points; template does not restate algorithm |
| artifact form and field-local constraints | artifact/stage template | workflow names template and gate only |
| cross-role grammar and compatibility rule | addressed `conventions.md` section | workflow points at exact rule |
| term meaning | compact query-only glossary | definition points to normative owner |
| project decision | compact `KNOWLEDGE.md` §1 row + source artifact | HL cites exact decision; rationale remains at source |
| live task state | task/phase `status.md` | derived index only |
| how state changed | immutable journal event | artifact text is referenced, not copied |
| historical rationale | task trace / CHANGELOG / migration / human essay | active rule links to it; role does not preload it |
| read graph measurement | generated evidence report | never a role input or authority |

### E6: Hypothesis extraction

| Hypothesis | Extract status | Evidence |
|---|---|---|
| H1 | confirmed | one foundation 30,828 words; role workflows 1,090–1,847; closure repeats add 110,930 fixed words |
| H2 | strongly supported, comprehension test pending | at least 2,920 glossary words repeat mechanics/history; operational terms already resolve to workflows/conventions/templates |
| H3 | strongly supported, edge-case replay pending | operative clauses and historical causes are separable; source artifacts and decisions already exist for rationale links |
| H4 | numerically confirmed, semantic proof pending | conservative fixed target clears every role and complete min-2 trajectory without reducing PV scan or changing task artifacts |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C8 addressed hybrid with audit-only manifest; conservative per-role and full-trajectory feasibility; single authority map; 21 exact file/section recommendations. | Pairwise inconsistency elimination, deliberate-inline exceptions, clean-receiver/compatibility counterexamples, and iteration-2 focus needed for semantic proof. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?

Stage complete: YES
→ User decision: advance pre-authorized by Coordinator direction for iteration 1.
