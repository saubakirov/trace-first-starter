# HL — TFW-56: Remove the Review Mode Axis

> **Date**: 2026-08-13
> **Author**: Coordinator (Claude Code)
> **Status**: 🔬 RES — contract frozen, research iteration 1 pending
> **Contract**: 🔒 FROZEN — approved by the owner 2026-08-13
> **Frozen**: §1 · §3 · §4 · §5 · §6 · §7 — locked on owner approval
> **Free**: §2 · §7.2 · §8 · §9 · §10 · §11 — research updates these directly
> **Append-only**: §12 Amendment Log — the only channel for changing a frozen section
> **Baseline**: `git log --grep="TFW-56/freeze"`

> **Sibling scope split (owner, 2026-08-13):** the same session raised three review questions.
> This task carries **only** the mode axis. The consolidator / subagent re-architecture went to
> [TFW-45 addendum](../TFW-45__multi_agent_workflows/PROPOSAL__TFW-45__review_swarm_consolidator.md).

---

## 1. Vision 🔒 FROZEN

Review stops asking which kind of review this is. The `code / docs / spec` axis — a config key, a
🛑 WAIT gate, three files, four template fields and eight checklist rows — is gone, and the two
checks inside it that ever carried signal are promoted into the universal checklist where every
review sees them. What to verify is declared **once**, by the TS: acceptance criteria (D49) and
`Evidence:` fields (D52). Nothing declares it a second time, more weakly, behind a gate.

**Impact:** One fewer blocking gate per review and one fewer stale config key per project. A reviewer
opening `review.md` sees Session Naming as Step 0 like every other TFW workflow — the anomaly
TD-106 warned about disappears instead of being annotated. And the review surface that
[TFW-53](../TFW-53__hl_contract_and_goal_defence/HL-TFW-53__hl_contract_and_goal_defence.md) Phase C
is about to load with goal defence gets smaller first, not larger.

> "I stopped answering a question that never changed what I checked."

## 2. Current State (As-Is) 🟢 FREE

### The axis has never produced a finding

Measured across every `judge.md` in this repository (17 files with a Mode-Specific section):

| Metric | Value |
|---|---|
| REVIEW files total | 61 |
| Carrying a `Review Mode` field (introduced TFW-38, 2026-04-14) | 18 |
| Distribution | `docs` 10 · `spec` 5 · `code` 3 |
| Mode-specific checklist rows filled, all reviews | **38** |
| → ✅ | 33 |
| → N/A | 4 (`code` mode on markdown: "Test coverage", "Security") |
| → ⚠️ | **1** — TFW-46/A row 10 Breaking changes, on RF section renumbering |
| → ❌ | **0** |
| `judge.md` files with no Mode-Specific section at all | TFW-41/A — the mandate is not even enforced |

One row in 38 carried signal, and it was the same row every time it could have: backward
compatibility. Everything else passed by construction.

### The base-rate argument is TFW's own

TFW-53 killed a proposed fifth review stage on exactly this ground:

> *"base rate ~4 goal-based blocks in 149 reviews → a dedicated stage would report 'aligned' ~145
> times and become the rubber stamp it was meant to replace"* — HL TFW-53 §4 Phase C

By that standard the mode axis is worse: 1 non-✅ in 38 rows, 0 blocks in 18 reviews.

### The three mode files barely differ

| | `code.md` | `docs.md` | `spec.md` |
|---|---|---|---|
| Verify action 1 | `min_verify_ratio` on files | **identical** | **identical** |
| Distinctive verify action | re-run build/test · check test file exists | — | — |
| Checklist row A | Code quality (conventions, naming) | Content quality (clarity, accuracy) | Analytical quality (logic, methodology) |
| Checklist row B | Test coverage | Source verification | Source attribution |
| Checklist row C/D | Security · Breaking changes | — | — |

`docs` and `spec` are synonyms of each other. And `code`'s two distinctive verify actions are
**already universal**, in the shared template and workflow, not in the mode file:

| Mode-file action | Where it already lives, unconditionally |
|---|---|
| "re-run at least 1 build/test command if possible" | `templates/review/verify.md` Checkpoint — *"Ran at least 1 build/test command (or documented why not)?"* |
| "if Tests pass claimed → check test file exists" | `review.md` Trust Protocol row — *"Tests pass" → Verify → re-run or check test file exists* |

So the axis duplicates what is already mandated and adds what cannot fail.

### Field signals that the axis does not classify the work

| Signal | Where |
|---|---|
| A REVIEW header reads **`docs + code`** — multi-select invented in the field, unsanctioned by any file | one of the 18 |
| An owner override recorded in the header: *"spec — owner override of the configured `code` default"* | [REVIEW TFW-53/A](../TFW-53__hl_contract_and_goal_defence/phase-a/REVIEW__phase-a__contract_in_artifacts.md) |
| `default_mode: code` is wrong for this repository and was never corrected — it was overridden per review instead | `.tfw/project_config.yaml:60` |

### The axis is already drifting

`config.md` and both of its adapter copies still route the key to **"Step 0: Select Review Mode"**.
It has been Step 1 since TFW-41/B. Three files carry a stale pointer to a step that never fires a
finding — the maintenance cost is real and it is being paid for nothing.

### What declares "what to check" today

| # | Declaration | Strength |
|---|---|---|
| 1 | TS §5 Acceptance Criteria (D49, requirements-first) | Binding — Judge row 1 checks against it |
| 2 | TS `Evidence:` fields → EV file (D52/D53) | Binding — Judge row 7, `verify.md` Evidence Verification |
| 3 | **Review mode** | 2–4 rows that have never failed, selected behind a 🛑 gate |

Three parallel declarations of the same thing. The weakest one is the only one with a gate.

### Adjacent work — boundaries

| Task | Status | Relationship |
|------|--------|--------------|
| [TFW-53](../TFW-53__hl_contract_and_goal_defence/HL-TFW-53__hl_contract_and_goal_defence.md) Phase C | 🔴 planned, DoD frozen | **Shared files:** `review.md`, `templates/review/judge.md`, `templates/REVIEW.md`, `glossary.md`, `conventions.md` §14. C adds the Purpose Check; this task removes the mode section from the same files. No frozen DoD of TFW-53 mentions mode files, so **no amendment is required** — but sequencing is mandatory (§8) |
| [TFW-45](../TFW-45__multi_agent_workflows/PROPOSAL__TFW-45__review_swarm_consolidator.md) | ❄️ FROZEN | Consolidator / subagent re-architecture. Downstream of this task and of TFW-53/C. This task frees the term "review mode" for it |
| TD-106 / `knowledge/process.md` F19 | open | Both describe `review.md`'s non-standard Step 0/Step 1. Deleting the step closes the debt instead of documenting it |

## 3. Target State (To-Be) 🔒 FROZEN

### What changes

1. **The axis is deleted, not renamed.** `.tfw/workflows/review/` and its three mode files are gone.
   No `code/docs/spec`, no `prompt`, no `design`, no `architecture`, no multi-select.
2. **The mode gate is gone.** `review.md` loses its mode step and its 🛑 WAIT, and its steps
   renumber contiguously with Step 0 = Session Naming, like every other TFW workflow.
3. **Substantive survivors are promoted, not dropped.** The universal `judge.md` checklist absorbs
   the checks that the mode rows carried and the universal set lacked. Every removed row is
   accounted for as *promoted*, *already covered elsewhere*, or *declined with a stated reason* —
   silence is not an option.
4. **`Mode:` disappears from the stage templates and the REVIEW header.** What kind of work it was
   is already legible from the TS and the RF.
5. **`tfw.review.default_mode` is removed from config; `min_verify_ratio` is untouched.**
6. **Adapters and entry points re-sync**, and the stale `config.md` step pointer dies with the key.
7. **History is not rewritten.** Existing REVIEW files keep their `Review Mode` headers; CHANGELOG
   entries stay as written. The trace of a removed mechanism is part of the record.

### The coverage decision — where the eight mode rows go

| Mode row | Disposition | Reason |
|---|---|---|
| `code` Breaking changes | **→ promoted** to the universal checklist | The only row that ever produced a non-✅ (TFW-46/A ⚠️). Generalizes past code: a renumbered template section, a moved doc anchor and a changed API all break consumers |
| `docs` Source verification · `spec` Source attribution | **→ promoted** as one universal row | Present in two of three modes, absent from the universal set. "Claims traceable to their source" is not a genre-specific check |
| `code` Security | **→ promoted** with explicit N/A | Scored N/A twice here and would score N/A in most framework work — but the cost of missing it once is asymmetric, and F21 makes the N/A a conscious trace rather than a silent skip |
| `code` Code quality | already covered | Universal row 4 *Style & standards* — conventions, naming |
| `code` Test coverage | already covered | Universal row 7 *Evidence completeness* + TS acceptance criteria |
| `docs` Content quality · `spec` Analytical quality | already covered | Universal rows 1 and 4; both mode rows were filled with generic clarity/logic prose in every instance |

Net: universal checklist 7 rows → 10. Total rows a reviewer fills goes from 9–11 to 10, and the
gate, the config key, three files and four template fields go away.

### 3.1 Result Visualization

> Written from the finished state. Every change carries its file; the value sits in the same picture.

**Every file that changes.** 3 deleted, 19 modified, **0 created** — a project adopting this pays
one `/tfw-update` and gains a shorter review.

```
.tfw/
├─ workflows/
│  ├─ review/                    ✂ DELETED — the whole folder
│  │   ├─ code.md                ✂  16 lines
│  │   ├─ docs.md                ✂  13 lines
│  │   └─ spec.md                ✂  13 lines
│  ├─ review.md                  − Step 1 "Select Review Mode" + 🛑 WAIT
│  │                             − mode-file load in Verify
│  │                             ↻ Steps 2-8 → 1-7, Step 0 = Session Naming (standard at last)
│  └─ config.md                  − review.default_mode row · ↻ fix stale step pointer
├─ templates/
│  ├─ review/
│  │  ├─ map.md                  − "Mode:" field
│  │  ├─ verify.md               − "Mode:" field  (build/test action already here — nothing to move)
│  │  └─ judge.md                − "Mode:" field · − Mode-Specific Checklist section
│  │                             + 3 promoted universal rows: compatibility · traceability · safety
│  ├─ REVIEW.md                  − "Review Mode" header · − mode placeholder comment
│  │                             ↻ §3 Judge table matches judge.md row-for-row
│  └─ project_config.yaml        − review.default_mode          (min_verify_ratio stays)
├─ project_config.yaml           − review.default_mode          (min_verify_ratio stays)
├─ conventions.md                ↻ Review subfolder entry · + §14 anti-pattern: a checklist row
│                                  that cannot produce a finding is ceremony
├─ glossary.md                   ↻ "coordinator in review mode" disambiguated — one meaning per name
└─ VERSION · CHANGELOG.md        ↻ bump + entry recording D42 revoked

.claude/commands/               ↻ tfw-review.md · tfw-config.md
.agent/workflows/               ↻ tfw-review.md · tfw-config.md
.tfw/adapters/codex/skills/     ↻ tfw-review/SKILL.md   ("review-mode WAIT gate" line)
.agents/skills/                 ↻ tfw-review/SKILL.md
TECH_DEBT.md                    ↻ TD-106 closed — the anomaly is deleted, not annotated
```

**The reviewer's first minute — before and after.**

```
BEFORE                                          AFTER
────────────────────────────────────────        ────────────────────────────────────────
Step 0  name the session                        Step 0  name the session
Step 1  read project_config default_mode        Step 1  Map        ← work starts here
        guess the mode from task context
        "Review mode: [docs]. Switch?"
        🛑 WAIT for the owner
        load workflows/review/docs.md
Step 2  Map                                     Step 2  Verify
Step 3  Verify  (+ mode verify actions,         Step 3  Judge
        action 1 identical in all 3 modes)      Step 4  Decide
Step 4  Judge   (+ 2-4 rows that have           …
        never failed in 38 fills)
…
```

**The Judge checklist — before and after.**

```
BEFORE                                          AFTER
1  DoD met?                                     1  DoD met?
2  Philosophy aligned                           2  Philosophy aligned
3  Tech debt documented                         3  Tech debt documented
4  Style & standards                            4  Style & standards
5  Observations collected                       5  Observations collected
6  RF completeness §7-9                         6  RF completeness §7-9
7  Evidence completeness                        7  Evidence completeness
                                                8  Backward compatibility        ← was code-only
── Mode-Specific ──────────────────             9  Claims traceable to sources   ← was docs+spec
7  Code quality        ✅ 33/38                 10 Safety (explicit N/A allowed)  ← was code-only
8  Test coverage       N/A 4/38
9  Security            ⚠️  1/38
10 Breaking changes    ❌  0/38
   ↑ the section every review copied
     from a file it had to be told to load
```

**What the grep gate proves on the last day.**

```
$ grep -rn "code / docs / spec\|default_mode: code\|Review Mode\|review/{code" \
       .tfw/ .claude/ .agent/ .agents/ --exclude=CHANGELOG.md
(no matches)

$ ls .tfw/workflows/review/
ls: cannot access '.tfw/workflows/review/': No such file or directory

$ ls tasks/TFW-53__*/phase-a/REVIEW__*.md   # history intact
> **Review Mode**: spec _(owner override …)_      ← still there, as written
```

**The value, stated as what stops happening.** A reviewer stops answering a question whose answer
never changed what they checked. A project stops carrying a config key whose default is wrong for it.
A maintainer stops fixing three stale pointers to a step that finds nothing. And the one check that
did find something — compatibility — stops being invisible to two thirds of reviews.

### 3.2 Value Flow

```
TS is written
   │
   ├─► §5 Acceptance Criteria  ─────────────┐
   └─► Evidence: fields (D52)  ─────────────┤   what to check — declared ONCE
                                            │
RF is delivered                             │
   │                                        ▼
   ▼                              ┌────────────────────┐
/tfw-review                       │  Judge checklist   │
   │                              │  10 universal rows │
   │  ✂ no mode read              │  explicit N/A      │
   │  ✂ no 🛑 WAIT                │  (F21)             │
   │  ✂ no mode file load         └────────────────────┘
   ▼                                        │
Map → Verify → Judge → Decide ──────────────┘
   │
   ▼
VERDICT

Value created:
  ONE DECLARATION   → the TS says what matters; nothing contradicts it more weakly
  GATE REMOVED      → one fewer blocking stop per review, zero coverage lost
  PROMOTION         → compatibility + traceability now checked in EVERY review, not one in three
  NO ANOMALY        → review.md Step 0 = Session Naming; TD-106 closed by deletion
  SMALLER SURFACE   → TFW-53/C loads goal defence onto a shorter file
```

## 4. Phases 🔒 FROZEN

**Single phase.** 22 files touched against a 30-file budget (`max_files_per_phase: 30`,
`max_modified_files: 30`), almost all of it deletion. Splitting core from adapters — the TFW-42/C,
TFW-46/C precedent — would open a desync window and buy a second TS/RF/REVIEW cycle for a task whose
verification is a single grep.

### Phase A: Remove the axis 🔴

> **Requires:** Independent — but see §8: land after TFW-53 Phase C, or coordinate at TS time
>
> **⚠️ Shared files with TFW-53 Phase C:** `review.md`, `templates/review/judge.md`,
> `templates/REVIEW.md`, `glossary.md`, `conventions.md` §14
>
> **Context for coordinator:**
> 1. `.tfw/workflows/review.md` — Step 1 (mode selection + WAIT), Step 3 Verify (mode-file load), Trust Protocol
> 2. `.tfw/workflows/review/{code,docs,spec}.md` — the full content being deleted, so the coverage table in §3 can be verified line by line
> 3. `.tfw/templates/review/{map,verify,judge}.md` — `Mode:` fields, Universal Checklist, Mode-Specific section, Checkpoints
> 4. `.tfw/templates/REVIEW.md` — header field, §3 Judge table, mode placeholder comment
> 5. `.tfw/workflows/config.md:92-93` — propagation rows, one of them stale
> 6. D41 (4-stage review + mode selection), **D42 (mode files — revoked by this task)**, D46 (WAIT gate at mode selection), D49 (requirements-first TS), D52/D53 (Evidence Layer), D54 (adapter parity = behavioural), D25 (Progressive Disclosure — the original argument for mode files)
> 7. `knowledge/philosophy.md` F13 (domain-agnostic), F20 (two workflow classes), F21 (explicit N/A), F22 (template minimalism), F24 (heuristics over instructions)
> 8. `knowledge/process.md` F19 + TD-106 — the Step 0/Step 1 anomaly this deletion closes
>
> **Key decisions:** D42 revoked (precedent: D53 revoked TFW-46 D16). D41's stage flow is **kept**
> — only its mode-selection clause dies. D46's WAIT gate loses its subject; the Reviewer Identity
> and Trust Protocol halves of D46 stay.
>
> **⚠️ Cascade dependency:** removing `review.md` Step 1 renumbers Steps 2-8 → 1-7. External
> references to those numbers exist only in `config.md` and its two adapter copies, and are already
> stale. TD-106 exists precisely because someone renumbered this file before.
>
> **Deliverables:**
> 1. `.tfw/workflows/review/` deleted with all three mode files
> 2. `review.md` — mode step and WAIT gate removed, mode-file load removed from Verify, steps renumbered contiguously, internal cross-references updated
> 3. `templates/review/judge.md` — `Mode:` field and Mode-Specific section removed; three promoted universal rows added per the §3 coverage table, each with explicit-N/A grammar
> 4. `templates/review/map.md`, `verify.md` — `Mode:` field removed; no verify action lost (both distinctive `code` actions already live in verify.md Checkpoint and the Trust Protocol)
> 5. `templates/REVIEW.md` — `Review Mode` header field and mode placeholder removed; §3 Judge table realigned row-for-row with judge.md
> 6. `project_config.yaml` + `templates/project_config.yaml` — `tfw.review.default_mode` removed, `min_verify_ratio` untouched
> 7. `config.md` — `review.default_mode` row removed, `min_verify_ratio` row's step pointer corrected
> 8. `conventions.md` — Review subfolder entry cleared of mode vocabulary; §14 anti-pattern added: a review checklist row that cannot produce a finding
> 9. `glossary.md` — no term defines review modes; the `Reviewer (AI — coordinator in review mode)` heading disambiguated so "review mode" carries one meaning (D28)
> 10. Adapter + entry-point sync: `.claude/commands/tfw-{review,config}.md`, `.agent/workflows/tfw-{review,config}.md`, `.tfw/adapters/codex/skills/tfw-review/SKILL.md`, `.agents/skills/tfw-review/SKILL.md`
> 11. `VERSION` bump + `CHANGELOG.md` entry recording the removal and D42's revocation
> 12. `TECH_DEBT.md` — TD-106 closed with the reason: the anomaly was deleted, not annotated

## 5. Definition of Done (DoD) 🔒 FROZEN

- ✅ 1. `.tfw/workflows/review/` no longer exists; no mode file remains anywhere in `.tfw/`.
- ✅ 2. `review.md` contains no mode step, no mode WAIT gate and no mode-file load; its steps are contiguous with Step 0 = Session Naming, and every internal reference to a renumbered step is correct.
- ✅ 3. `templates/review/judge.md` has no `Mode:` field and no Mode-Specific Checklist; its universal checklist carries the promoted rows for **backward compatibility**, **claims traceable to sources** and **safety**, each with explicit-N/A grammar.
- ✅ 4. Every one of the eight mode-specific rows is accounted for in the RF as **promoted**, **already covered** (with the universal row named) or **declined** (with the reason) — none silently disappears.
- ✅ 5. `templates/review/map.md` and `verify.md` carry no `Mode:` field, and both distinctive `code`-mode verify actions remain mandated: the build/test command by `verify.md` Checkpoint, the test-file check by the `review.md` Trust Protocol.
- ✅ 6. `templates/REVIEW.md` has no `Review Mode` header field and no mode-specific placeholder; its §3 Judge table matches `judge.md`'s universal checklist row-for-row.
- ✅ 7. `tfw.review.default_mode` is absent from `.tfw/project_config.yaml` and `.tfw/templates/project_config.yaml`; `min_verify_ratio` and its 0.42 default behave exactly as before.
- ✅ 8. `config.md` no longer routes `review.default_mode`, and its `review.min_verify_ratio` row names the correct step number in the renumbered workflow.
- ✅ 9. `conventions.md` Review subfolder entry carries no mode vocabulary, and §14 carries the anti-pattern: adding a review checklist row that cannot produce a finding.
- ✅ 10. `glossary.md` defines no review-mode term, and "review mode" has exactly one meaning across `.tfw/` (D28).
- ✅ 11. All six adapter and entry-point copies carry no mode reference and match `.tfw/` behaviourally (D54).
- ✅ 12. `VERSION` bumped and `CHANGELOG.md` records the removal, the three promoted rows and D42's revocation.
- ✅ 13. TD-106 is closed in `TECH_DEBT.md` with the reason recorded.
- ✅ 14. Grep gate: `grep -rn "code / docs / spec\|default_mode: code\|Review Mode\|review/{code" .tfw/ .claude/ .agent/ .agents/ --exclude=CHANGELOG.md` returns zero matches, and the command with its output is recorded as evidence.
- ✅ 15. History intact: no existing task REVIEW file and no past CHANGELOG entry is edited to erase the mode field (TFW-40 D4 precedent — historical texts are not rewritten).

## 6. Definition of Failure (DoF) 🔒 FROZEN

- ❌ 1. A check or verify action available today disappears without a recorded home in the RF — coverage loss disguised as simplification.
- ❌ 2. The universal checklist grows a row that cannot produce a finding — one rubber stamp swapped for another.
- ❌ 3. A stale step reference survives the renumbering anywhere in `.tfw/` or the adapters — the TD-106 trap, sprung a second time.
- ❌ 4. `min_verify_ratio` behaviour changes as collateral of removing the sibling key.
- ❌ 5. Existing REVIEW files or past CHANGELOG entries are rewritten to remove the mode field.
- ❌ 6. Adapters left desynced from `.tfw/`, or the Codex skill still names a "review-mode WAIT gate" that no longer exists.
- ❌ 7. The axis is renamed rather than removed — a mode field kept "for information", a `default_mode: none`, or an empty `review/` folder left in place.
- ❌ 8. The change collides with TFW-53 Phase C in a shared file and forces an amendment against TFW-53's frozen DoD.

**On failure:** DoF-1/2/4 → revert the affected file to the pre-task baseline and re-derive the
coverage table before retrying. DoF-3/6 → fix forward, the grep gate is the acceptance test.
DoF-5 → restore from git; the trace is the product. DoF-8 → stop, file an amendment in TFW-53 §12
rather than editing a frozen section.

## 7. Principles 🔒 FROZEN

1. **Delete, don't relabel** — a mode field kept "for information" is the same maintenance cost with none of the behaviour.
2. **No coverage loss without a recorded home** — every removed row is promoted, proven duplicate, or explicitly declined with a reason. Silence fails the review.
3. **A check that cannot fail is not a check** — the base-rate rule TFW-53 already applied to stages, applied to rows.
4. **What to check is declared once** — by the TS: acceptance criteria (D49) and Evidence fields (D52). A second, weaker declaration behind a gate is worse than none.
5. **Explicit N/A over silent skip** — F21. A promoted row that is often N/A is a conscious trace; a mode-gated row is an invisible one.
6. **History is evidence, not debt** — existing REVIEW files and CHANGELOG entries stay exactly as written.
7. **Single Source of Truth, behavioural adapter parity** — one copy in `.tfw/`, adapters promise the same behaviour, not the same bytes (D54).
8. **Structural enforcement over promise** — the acceptance test is a grep whose output is recorded, not a claim that the sweep was done.

### 7.2 Knowledge Citations 🟢 FREE

| # | Source | Item | How it applies |
|---|--------|------|----------------|
| 1 | KNOWLEDGE.md §1 | D42 — Review mode files, mode-specific checklists, Progressive Disclosure | **The decision this task revokes.** Its stated premise ("44% of the old checklist was code-only") is not disputed; its outcome — 0 findings in 38 rows — is |
| 2 | KNOWLEDGE.md §1 | D41 — 4-stage review flow + mode selection with 🛑 WAIT | The stage flow is kept intact; only D41's mode-selection clause dies |
| 3 | KNOWLEDGE.md §1 | D46 — Reviewer Identity, Trust Protocol, WAIT gate at mode selection | The WAIT gate loses its subject; identity and Trust Protocol are untouched, and the Trust Protocol is where one deleted mode action already lives |
| 4 | KNOWLEDGE.md §1 | D49 — Requirements-first TS, acceptance criteria as the binding declaration | Principle 4: the TS already says what to check |
| 5 | KNOWLEDGE.md §1 | D52 / D53 — Evidence Layer, mandatory `evidence/`, 4-status vocabulary | The executable-vs-textual distinction the mode axis was really groping for already exists here |
| 6 | KNOWLEDGE.md §1 | D54 — Adapter parity is a behavioural promise, not a file-layout promise | DoD-11: six adapter copies must behave the same, not match byte-for-byte |
| 7 | KNOWLEDGE.md §1 | D28 — Naming creates behaviour; one name = one behaviour | DoD-10: "review mode" must not mean two things once the axis is gone; also the counter-risk in H6 |
| 8 | KNOWLEDGE.md §1 | D25 — Progressive Disclosure (mode files loaded only when selected) | The original justification for mode files. It holds only if the loaded content earns its load; 38 rows say it does not |
| 9 | KNOWLEDGE.md §1 | D53 revoking TFW-46 D16 | Precedent that a recorded decision can be revoked by a later task rather than quietly ignored |
| 10 | `.tfw/README.md` § Values | **Structural Enforcement** — gates should be structural, not procedural | DoD-14: a recorded grep is the acceptance test, not a checkbox |
| 11 | `.tfw/README.md` § Values | **Naming Creates Behaviour** — if you must explain what a step does, it is named wrong | The mode step needed a config key, a table and a WAIT to explain itself |
| 12 | `.tfw/README.md` § Values | **Single Source of Truth** — one copy per rule, adapters reference | Six adapter copies of the mode step are the cost being removed |
| 13 | knowledge/philosophy.md | F13 — TFW is domain-agnostic; no code-specific terminology | Kills the extension option: `prompt`/`design`/`architecture` are software-domain enumeration inside a domain-agnostic framework |
| 14 | knowledge/philosophy.md | F21 — Explicit N/A turns a silent skip into a conscious trace | Principle 5 and the grammar of the three promoted rows |
| 15 | knowledge/philosophy.md | F22 — Template minimalism, «не захламляй шаблон» | Four `Mode:` fields and a placeholder comment across four templates |
| 16 | knowledge/philosophy.md | F20 — Two workflow classes: investigative (staged) vs procedural | The stages survive; this task removes a *parameter*, not a stage |
| 17 | knowledge/philosophy.md | F24 — Instructions produce compliance, heuristics produce competence | 33 ✅ out of 38 is compliance. The rows were filled, not used |
| 18 | knowledge/process.md | F19 — `review.md` is the only workflow with a non-standard Step 0/Step 1 | The anomaly is deleted rather than annotated; F19 becomes historical |
| 19 | TECH_DEBT.md | TD-106 — the Step 0 renumbering trap in `review.md` | DoD-13 closes it; the cascade warning in §4 is taken from it |
| 20 | conventions.md §6 | Scope budgets, and the project override to 30 files | Single-phase decision in §4 |
| 21 | conventions.md §14 | Anti-patterns registry | DoD-9 adds the row-that-cannot-fail anti-pattern so the axis cannot regrow under a new name |
| 22 | HL TFW-53 §4 Phase C | The base-rate argument that killed the fifth review stage | §2: the same standard, applied to rows, is stricter than the one applied to stages |

## 8. Dependencies 🟢 FREE

| Dependency | Status |
|------------|--------|
| [TFW-53](../TFW-53__hl_contract_and_goal_defence/HL-TFW-53__hl_contract_and_goal_defence.md) Phase C — shares `review.md`, `judge.md`, `REVIEW.md`, `glossary.md`, `conventions.md` §14 | 🔴 planned, DoD frozen. **Recommendation: this task lands first** — C then edits a file with no Mode-Specific section, and C's own DoD-28 word budget on `review.md` gets easier. If the owner prefers C first, the two must be coordinated at TS time, file by file |
| No frozen TFW-53 DoD names a mode file | ✅ verified — DoD 18-29 name `judge.md`, `review.md:28`, `REVIEW.md`, `glossary.md`, `conventions.md` §14. No amendment to TFW-53 required |
| [TFW-45 addendum](../TFW-45__multi_agent_workflows/PROPOSAL__TFW-45__review_swarm_consolidator.md) | ❄️ FROZEN — downstream of both. Benefits: smaller surface, and the term "review mode" freed |
| `/tfw-update` config-merge semantics for a **removed** framework key | ⬜ unverified — see H4. Existing projects on an older version must not break on upgrade |

## 9. Risks 🟢 FREE

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| A mode row carried value the 38-fill sample cannot show — a real project's `code` review needs the security row to fire | Medium | Medium | Promote it (DoD-3) with explicit N/A rather than dropping it. H1 tests the survivor set |
| The axis's real function was **priming** the reviewer ("this is a docs review"), not the rows — D28 says naming changes behaviour | Medium | Medium | H6 tests this directly. If confirmed, the fallback is a non-gated one-line descriptor with no file and no config key, which keeps 80% of the saving |
| Step renumbering leaves a stale reference | Low | Medium | DoF-3 + the grep gate; the three known references are already stale and are in scope |
| An external project depends on the mode files as its extension point for custom checks | Low | Medium | H5. Fallback: a project-level checklist appended to the universal set, expressed in `project_config.yaml` — one place, no gate |
| Collision with TFW-53 Phase C in a shared file | Medium | High | §8 sequencing; DoF-8 forbids resolving it by editing a frozen section |
| Single phase means one larger review | Low | Low | The acceptance test is a recorded grep plus a 22-file diff that is almost entirely deletion |
| `/tfw-update` mishandles a removed config key on existing projects | Low | Medium | H4 — audit `update.md` CONFIG-merge semantics before shipping |

## 10. RESEARCH Case 🟢 FREE

### Blind Spots

- **External base rate.** AFD has ~149 REVIEW files on byte-identical review templates. If its mode-specific rows also never fire, the finding replicates outside this repo and the decision is settled. If they *do* fire, the axis works elsewhere and the honest fix is project-configurable, not deleted.
- **Priming vs rows.** Nobody has separated "the mode told the agent what kind of work this is" from "the mode gave the agent two extra rows". D28 says the first could be the whole value, and it is the one thing deletion destroys.
- **Consumer audit.** Unknown whether anything reads `tfw.review.default_mode` or the `Review Mode` header beyond the six files found by grep — the docs build (`gen_docs`), `update.md`'s CONFIG merge, or the `editions/` starters.
- **Non-code projects.** This repository is markdown-only and AFD is software. No data from an analytics, curriculum or business-process project, which is where a genre label would most plausibly earn its place (F13).

### Hypotheses

| # | Hypothesis | Status |
|---|----------|--------|
| H1 | The eight mode rows contain exactly three checks absent from the universal set — backward compatibility, source traceability, safety — and the other five are synonyms of universal rows or already mandated elsewhere | open |
| H2 | No verify action is lost by deleting the mode files: `code`'s two distinctive actions are already unconditional in `verify.md` Checkpoint and the `review.md` Trust Protocol | open |
| H3 | The finding replicates in AFD: mode-specific rows there also produce ~0 findings across ~149 reviews | open |
| H4 | No consumer breaks: nothing outside the six identified files reads `default_mode` or the `Review Mode` header, and `update.md`'s CONFIG merge handles a removed framework key without corrupting an existing project's config | open |
| H5 | No project uses the mode files as an extension point for custom checks; a project needing extra checks can express them in `project_config.yaml` without a mode axis | open |
| H6 | The axis's value was in its **rows**, not in **priming** the reviewer — so removing the label does not degrade review behaviour. (D28 predicts the opposite; this is the hypothesis most likely to be refuted) | open |

> **Filter — if false, would the approach change?**
> H1 false → more rows must be promoted; the coverage table in §3 is wrong.
> H2 false → verify actions must be migrated into `verify.md`, not just deleted.
> H3 false → the axis works in other projects; make it project-optional instead of removing it.
> H4 false → migration steps for existing projects, and `update.md` may need a change.
> H5 false → an extension slot is required and the design gains a component.
> H6 false → **do not delete the label.** Fall back to a non-gated descriptor: no file, no config key, no WAIT, one line of free text.

### Risks of Not Researching

- We delete the label on the strength of the rows and lose the priming effect D28 predicts — the failure mode is invisible, because a worse review still produces a REVIEW file (H6).
- We generalize from 18 reviews in one markdown-only repository when a 149-review software corpus with identical templates is available and unmeasured (H3).
- We break an existing project's config on `/tfw-update` (H4) — the one failure mode that hits users rather than this repository.
- We migrate the wrong survivor set and the promoted rows become three more rows that cannot fail, which is DoF-2 (H1).

### Proposed RESEARCH Focus

1. **Gather** — measure AFD: how many REVIEW files carry a mode, the status distribution of every mode-specific row, and any instance where such a row drove a REVISE or REJECT (H3). Audit consumers: `grep` for `default_mode` and `Review Mode` across the docs build, `update.md`, `editions/`, and read `update.md`'s CONFIG-merge rules for key removal (H4, H5).
2. **Extract** — build the coverage matrix: 8 mode rows × 7 universal rows, each cell *duplicate / partial / absent*, to confirm or correct the three-survivor set and the N/A grammar (H1, H2).
3. **Challenge** — attack H6 head-on. Is there any evidence in the 18 reviews that the mode label changed reviewer behaviour beyond the rows it loaded — depth, tone, what got opened? Counter-argument to answer: D28 and the `.tfw/README.md` "Naming Creates Behaviour" value both predict that removing a name removes a behaviour, and this task is proposing to remove a name.

**Iterations.** `min_iterations` is 2 by config. I would propose an override to **1** with justification:
the question set is narrow, four of six hypotheses are settled by measurement rather than judgement,
and the AFD corpus plus a consumer grep is one Gather. If Challenge cannot close H6 in that pass, a
second iteration is warranted rather than assumed.

### Why Not Just...?

- **Why not add `prompt` / `design` / `architecture`?** Those are domains, not verification methods. The list cannot be closed (data, curriculum, contract, business process…), each addition costs two synonym rows, and enumerating software specialties inside a domain-agnostic framework violates F13. The axis that actually varies is executable-vs-textual, and the Evidence Layer already owns it.
- **Why not allow selecting 2-3 modes at once?** If every selected mode's rows apply, the result is a union of all rows — which is one universal checklist with explicit N/A, reached by way of a gate. The `docs + code` header already found in the field is evidence that one label does not classify the work; multi-select converges on deletion while keeping the ceremony.
- **Why not keep the mode as a non-gated descriptive field?** That is the H6 fallback, held in reserve. It is not the default because a field with no behaviour still needs a template slot, an instruction and a place in six adapter copies — and it is exactly the kind of decoration that regrows into a gate.
- **Why not wait and fold this into TFW-53 Phase C?** C is already 🔴 with 12 frozen DoD items. Adding a deletion sweep to a task built to prevent scope inflation would be a poor first use of its own contract.
- **Why not leave it alone — it costs nothing?** It costs a blocking gate per review, a wrong default in every new project, three stale pointers already in the tree, and eight rows of ✅ that dilute a checklist about to be given a real job by TFW-53 Phase C.

## 11. Strategic Insights (Planning) 🟢 FREE

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | Owner's framing is the design argument, not the data: *«что проверять задается рамкой задачи»* — the task frame already declares what to check, so the mode is a second, weaker declaration of something already binding. The measurement confirms an argument that stands without it | philosophy | User, 2026-08-13 |
| S2 | Owner arrived with three options (extend with prompt/design/architecture · multi-select 2-3 · remove) and chose removal after seeing the 38-row base rate. The evidence changed the decision — which makes the extension option the one that must be explicitly barred, or it returns as an obvious improvement later. This is what the §14 anti-pattern is for | process | User, 2026-08-13 |
| S3 | Owner deliberately split the session's three questions: mode deletion ships now, the consolidator/subagent re-architecture waits in TFW-45. Small reversible cleanup is not held hostage to a large unproven redesign — the same sequencing logic that split TFW-54 out of TFW-53 | process | User, 2026-08-13 |
| S4 | Owner connects the cleanup to the goal-defence work: *«к тому же мы добавляем защиту целей и ценностей в ревью»* — the checklist is about to be given a check that can actually reject work, which raises the bar for the decorative rows sitting next to it. Cleaning first is not cosmetic; it is preparing the surface | philosophy | User, 2026-08-13 |

## 12. Amendment Log 🟢 APPEND-ONLY

**No amendments.**

| # | Date | § | Type | Proposer | Proposed change | Evidence | Cost | Alternatives considered | Verdict |
|---|------|---|------|----------|-----------------|----------|------|------------------------|---------|

---

*HL — TFW-56: Remove the Review Mode Axis | 2026-08-13*
