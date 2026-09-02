# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260902-175227_RCFR](../../HL-TFW_20260902-175227_RCFR.md)
> Goal: Reduce mandatory role context by at least 30% without changing TFW meaning, algorithms, authority boundaries, gates, or guarantees.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: common bootstrap | full `AGENTS + conventions + glossary + KNOWLEDGE` | compact common kernel plus addressed libraries | `AGENTS.md` router only; role workflow selects every other input | generated per-role bootstrap |
| D2: normative ownership | monolithic `conventions.md` owns most mechanics | role algorithm in workflow; shared invariants in addressed convention sections | four role-owned normative files | generated role views compiled from fragments |
| D3: terminology access | mandatory full glossary | compact glossary as term router, loaded only on lookup | definitions inline at first operational use | glossary removed; terms resolve only to normative owners |
| D4: project knowledge access | full `KNOWLEDGE.md` for every role | PV priority sections by address | coordinator citations drive Researcher/Executor reads; Reviewer retains independent scan | generated relevance index or query result |
| D5: rationale and history | inline beside every active rule | appendices in the same file, outside addressed runtime sections | task traces, CHANGELOG, migrations, and human essay only | generated rationale links from source annotations |
| D6: stale and compatibility mechanics | retain in active instructions | move to a compatibility appendix with an explicit reader | delete when no current or compatibility reader exists | keep only executable compatibility tests; remove prose class |
| D7: validation | word totals only | static read-graph extraction plus word totals | clean-context role scenarios plus semantic checklist | generated role bundles replayed against fixtures |

## Findings

### G1: Reproducible word method and two baselines

The measurement is a count of non-empty whitespace-delimited sequences. The PowerShell form used on this Windows checkout is:

```powershell
$text = Get-Content -Raw -Encoding UTF8 -LiteralPath $path
[regex]::Matches($text, '\S+').Count
```

This matches GNU Coreutils' definition of a word as a non-empty sequence of non-whitespace characters delimited by whitespace or an input boundary ([GNU `wc` manual](https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html)). A section read is the same calculation over the heading-to-next-peer-heading range. A repeated instructed read is a new edge and is counted again.

The frozen HL recorded the then-current carrier baseline. Current HEAD is slightly larger because another completed task changed active carriers after the freeze: `conventions.md` is now 11,269 rather than 11,194 words and `glossary.md` is 5,174 rather than 5,126. The current common foundation is therefore exact at 30,828 words:

| File | Words | Runtime classification |
|---|---:|---|
| `AGENTS.md` | 396 | current bootstrap and conduct authority, plus command routing |
| `.tfw/conventions.md` | 11,269 | current normative authority mixed with rationale and incident history |
| `.tfw/glossary.md` | 5,174 | term index mixed with repeated mechanics and retired concepts |
| `KNOWLEDGE.md` | 13,989 | decision/history index; not a general operating instruction |
| **One full foundation read** | **30,828** | mandatory once in every role skill today |

Two baselines are required because the HL table counted carriers once, while the actual protocols contain duplicate and checkpoint-specific reads:

| Role | Current carrier baseline: foundation + workflow + required templates | 30% ceiling | Known fixed instructed exposure, repeated reads included | 30% ceiling |
|---|---:|---:|---:|---:|
| Coordinator | 35,202 | 24,641 | 54,610 | 38,227 |
| Researcher | 33,831 | 23,681 | 34,057 | 23,839 |
| Executor | 33,669 | 23,568 | 64,738 | 45,316 |
| Reviewer | 35,879 | 25,115 | 83,875 | 58,712 |
| **Four-role fixed trajectory** | **138,581** | **97,006** | **237,280** | **166,096** |

The carrier baseline is the stable comparison with HL §2. The stricter column adds only fixed, directly instructed edges that the carrier table omitted: skill text; repeated foundation reads in `handoff.md` and `review.md`; addressed convention reads; the Coordinator/Reviewer PV scan; the Researcher mode configuration; the Executor's pre-RF headings read; and the Reviewer's later North Star read. It remains a lower bound because task artifacts, conversation history, relevant code, and completed stage files vary by task.

### G2: Exact transitive role and checkpoint graph

`F` below means one full 30,828-word foundation read. Variables are task-local word counts: `S` status, `J` journal, `H` master HL at the required version, `P` Phase HL, `T` governing TS, `O` ONB, `R` RF, `V` prior REVIEW, `E` evidence, `X` referenced/implementation files, `I` iteration control, and `Qn` completed stage files. The fixed numbers above deliberately exclude these variables; the graph does not.

| Role/checkpoint | Explicit path in current sources | Repeat accounting and decision purpose |
|---|---|---|
| Coordinator — bootstrap | command → `AGENTS.md` → `tfw-plan` skill → `F` → `S + J + relevant artifacts` → `plan.md` | the skill owns a full context list; the workflow then reads `conventions.md` §10 again to check completeness |
| Coordinator — Knowledge Gate | `knowledge_state.yaml` + `project_config.yaml#tfw.knowledge` | decides stop/remind/skip; `current_seq` is undefined for current identifiers, so the edge exists but the computation does not |
| Coordinator — understand/PV | README North Star sections + `.tfw/README.md` NS1–NS3 and methodology values/Success Criteria + `knowledge/philosophy.md` + `KNOWLEDGE.md` §1 + `conventions.md` §3/§11/§14 + relevant topics | exact priority 0–4 fixed scan is 16,033 words; 11,742 of those words repeat portions of `F` already loaded |
| Coordinator — HL/freeze | `templates/HL.md` → written HL → `conventions.md` §3 rule 15 | template owns form; contract section owns freeze semantics and baseline recovery |
| Coordinator — research return | every `research/iterN/RES.md` + `iterations.yaml` | reads iteration status and classifies recommendations; each iteration output is read once per return |
| Coordinator — TS / later phase | `templates/TS.md`; predecessor RF for Phase N>1 | template owns form; predecessor RF is the actual-result gate |
| Coordinator — self-check | `conventions.md` §14, then §5 | 3,161 more repeated words, after §14 was already read in `F` and again in the PV scan |
| Researcher — bootstrap/mode | command → `AGENTS.md` → skill → `F + S + J + H + I` → `base.md` → `conventions.md` §10 → `project_config.yaml#tfw.research` → `focused.md` | base says “verify loaded”, so the foundation is not instructed a second time; `I` is checked by skill context and again by iteration detection |
| Researcher — stages | each numbered stage template → corresponding stage file; external source + project sources per OODA loop | templates own stage form and mindset; no stage can be skipped |
| Researcher — synthesis | `Q1 + Q2 + Q3 + Q4` → `templates/RES.md` | all completed stage files are read again; this repeated exposure is variable and intentional because synthesis consumes them |
| Executor — bootstrap | command → `AGENTS.md` → skill → `F + S + J + H + P + T + V? + X` → `handoff.md` → **`F + H + P + T + V? + X` again** | the skill and workflow independently issue the same full foundation and task context list; first full duplicate has no distinct decision use |
| Executor — onboarding | `H + T + referenced X` again → `templates/ONB.md` → approval | Phase 1 says “Read all context” after both bootstrap lists; HL/TS/reference inputs can therefore be read a third time |
| Executor — revision return | highest TS revision → prior REVIEW → `conventions.md` §4 | TS is the order; REVIEW is reasoning; §4 owns sibling/append grammar. The returning subsection repeats T and V after both context lists |
| Executor — evidence/RF | `templates/evidence/EV.md`; RF headings (51 words) → full `templates/RF.md` | the headings pre-gate and full form have distinct uses and are deliberately both counted |
| Reviewer — bootstrap | command → `AGENTS.md` → skill → `F + S + J + H + P + T + R + E + X` → `review.md` → **`F + H + P + T + R + X` again** | the skill and workflow independently issue the same foundation and task list; baseline recovery changes the required H version but does not justify re-reading the other common files |
| Reviewer — Map | `templates/review/map.md` + RF §1–§5 + TS DoD + HL §7 + ONB | partial task artifacts are instructed again to establish comprehension |
| Reviewer — Verify/PV | `templates/review/verify.md` + files/commands/evidence + full PV priority 0–4 scan | independent verification is a real algorithmic use; the 16,033-word scan still repeats 11,742 words already present in each full foundation read |
| Reviewer — Judge | `templates/review/judge.md` + verify findings + contract baseline + North Star | the North Star is read again for the Purpose Check; the baseline is a task-variable repeat |
| Reviewer — Decide/close | all three review stage files → `templates/REVIEW.md` → `conventions.md` §5/§15 → `/tfw-docs` and maybe `/tfw-knowledge` | stage reread is intentional synthesis; closure adds secondary Coordinator-owned command paths |

For a first Executor pass, the dynamic part is at least `S + J + 3(H + P + T + X)`; a revision adds repeated `T` and `V` edges. For Review, it is at least `S + J + 2(H + P + T + R + X) + E + O + partial task-section rereads + review-stage rereads`. The current task illustrates why excluding task variables is necessary but not harmless: its HL alone is 3,682 words, status plus current journal is 138, and iteration control is 49.

### G3: Current sources of truth versus repeated, historical, and readerless text

| Surface | Current authority | Repetition/history/readership finding |
|---|---|---|
| `AGENTS.md` | project conduct and command recognition | repeats the context-loading list and the command map carried by skills; a small bootstrap duplication is justified, but the full list has no role-specific decision use |
| role skill | command discovery, selected workflow, role boundary | context lists repeat workflows; role lock text repeats workflows; the workflow is already declared canonical |
| role workflow | role algorithm, gates, stop, inline enforcement-critical values | strongest natural owner; `handoff.md` and `review.md` duplicate their skills' full load lists and restate template structures |
| `conventions.md` | cross-role invariants, shared grammars, compatibility guarantees | 11,269 words are forced into every role. Large parts of §§3–5, §14 and §15 mix operative clauses with incident narratives. History can justify a rule without being a runtime input |
| `glossary.md` | term meanings and routing | at least 2,920 words sit in sections that restate mechanics or retired classes: Contract/Purpose, Evidence, Task Naming, Status Flow, Roles, Execution Gates, Dimensional Analysis, retired Debt Registry, and retired Task Board |
| `KNOWLEDGE.md` | current decision index and project history | §1 is 7,986 words, §2 3,036, §3 2,749, §4 187. Only role-specific relevance and PV scans need it; full load by Researcher and Executor has no decision purpose |
| artifact templates | form, field-local constraints, cognitive cue at the point of writing | `handoff.md` repeats ONB/RF structure; `review.md`, `judge.md`, and `REVIEW.md` repeat Purpose/Disposition mechanics and incident rates. Long comments are paid even when the output needs one row |
| task `status.md` and journal | only live state and how it got there | bounded, high-value, task-local inputs; these should stay before global history |
| task HL/TS/RF/RES/REVIEW/EV | contract, order, result, research, verdict, evidence | current and role-specific; duplication occurs because both skills and workflows independently command reads |
| README/essay/book/history | human explanation and historical rationale | legitimate readers exist, but ordinary roles do not need the human narrative unless a named checkpoint cites a clause |

### G4: Stale and compatibility findings

1. `.tfw/workflows/plan.md` Step 2 requires `current_seq - last_consolidation_seq`; current task identifiers are clock-derived and expose no `current_seq`. The Knowledge Gate is an active but uncomputable mechanism.
2. `.tfw/workflows/knowledge.md` still scans “tasks since `last_consolidation_seq`”, so the stale assumption is not local to planning. A current, task-local cursor or timestamp is needed; inventing a sequence would violate the identifier design.
3. `.tfw/workflows/resume.md` scans `HL__Phase*`, `TS__Phase*`, `ONB__Phase*`, `RF__Phase*`, and `REVIEW__Phase*`, while current phase folders and kebab-case names are declared elsewhere. This is an active stale discovery algorithm, not historical compatibility.
4. Glossary articles for the retired Debt Registry and Task Board have historical readers, but no ordinary operational decision. They become harmless when the glossary is query-only; keeping them in a mandatory full read is unjustified.
5. The frozen TFW-57 proposal names a debt registry and TS change log that were superseded before this task. It is evidence for the origin of RCFR, not current scope authority.
6. No current source declares an exact read manifest. Consequently a duplicate context edge can be added in a skill or workflow without any receiving-project check reporting the exposure increase.

### G5: External cross-checks

The OpenAI prompt-caching documentation says a repeated prefix can reduce computation, latency, and cached-input price, but also says the cached object is the rendered context's KV state and that the rendered context includes instructions, tools, and conversation history ([OpenAI Prompt Caching](https://developers.openai.com/api/docs/guides/prompt-caching)). Therefore caching can reduce some cost of repetition but does not remove the repeated material from the model's usable context or resolve competing authorities. It is not an alternative to read-graph reduction.

The same source requires an identical rendered prefix for reuse. Role-specific task artifacts and changing conversation history make a large all-role foundation a poor reason to preserve irrelevant content merely for caching; stable common invariants can still remain prefix-friendly after the runtime path is reduced.

### G6: What is and is not closed after Gather

Closed:

- H1's premise is empirically supported: the common foundation is 30,828 words versus 1,090–1,847 words for a role workflow, before duplicate reads and PV scans.
- The current lower-bound carrier numbers undercount Executor and Reviewer by nearly one additional full foundation each.
- Current authority can be separated from history without guessing: task state/artifacts and role workflows have named operational readers; broad glossary/knowledge/history loads do not.
- The 30% target is numerically plausible because removing one foundation read alone saves 30,828 words from Executor and Reviewer, and removing the three non-router full files from Researcher saves 30,432 words.

Remaining for Extract/Challenge:

- choose a configuration that preserves the independent PV scan, D24-style inline enforcement, compatibility readers, and all stop gates;
- quantify conservative after-paths under the same edge-counting method;
- identify exact deletion/redirect/reword sites and reject configurations that create a second authority.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Exact current carrier counts, known repeated fixed exposure, algebraic task-variable graph, authority classification, and three active stale mechanisms. | Configuration choice, after-count model, pairwise incompatibilities, semantic-equivalence attack, and file-level wording recommendations. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?

Stage complete: YES
→ User decision: advance pre-authorized by Coordinator direction for iteration 1.
