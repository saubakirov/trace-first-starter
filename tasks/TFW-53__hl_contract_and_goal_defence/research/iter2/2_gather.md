# Gather — "What do we NOT know?"

> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW-53](../../HL-TFW-53__hl_contract_and_goal_defence.md)
> Goal: An approved HL is a contract, and the reviewer is its defender — review asks "is this what we set out to do?" against a north star above the task.

---

## Dimensions

Seven independent decision factors. No alternative is marked preferred — all stay open until Challenge.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| **D1: North-star locus** — where the anchor physically lives | Designated section of the **root `README.md`** | A **nominated existing HL** (AFD's pattern: HL-AFD-2) | A **new dedicated artifact** (`NORTH_STAR.md`) | A block in **`KNOWLEDGE.md` §0** (project principles) |
| **D2: North-star payload** — what the reviewer actually reads | **Purpose only** — what we are building and why, ~1 paragraph | **Purpose + project principles** | **Purpose + principles + explicit non-goals** | **Full vision document** (AFD's current 509-line form) |
| **D3: Anchor obligation** — what happens when a project has none | **Mandatory artifact**, no fallback — review cannot proceed | **Mandatory header field** with explicit `N/A` permitted (F21) | **Optional**, silent fallback to master HL §1 | **Mandatory field with a declared fallback chain**: north star → master HL §1 at the frozen baseline |
| **D4: Forcing-function form** — how alignment is evidenced | **Quote the clause verbatim + resolvable path** (D43 pattern) | **Name the clause id** only (`NS-3`) | **Free-text alignment rationale**, no citation required | **Quote + name the concrete harm** the work avoids or incurs |
| **D5: Verdict class** — how a goal failure is recorded | **Reuse `❌ REJECT`**; goal grounds live in the rationale prose | **A new distinct verdict token** on the Task Board | **Severity-tiered inside existing tokens** — goal-`REVISE` vs goal-`REJECT` | **Reuse `❌ REJECT` + a named finding class + mandatory owner routing** |
| **D6: Materiality mechanism** — what stops wording-only blocks | **Prose clause**: "material impact on the value, never phrasing" | **Required field**: "what breaks if this ships" | **Proportionality test**: "would another revision cycle be proportionate?" | **Two-part test**: name the violated claim **and** the concrete consequence |
| **D7: Reference set** — what the check measures against | **Master HL frozen baseline + north star** | **+ the Phase HL** | **+ the TS** | **North star only** |

---

## Findings

### G1: The review surface has no vocabulary for purpose at all

Not "weak" — absent. Measured across the entire reviewer-facing surface: `.tfw/workflows/review.md`, the three stage
templates (`map.md`, `verify.md`, `judge.md`), and the three mode files (`code.md`, `docs.md`, `spec.md` — 39 lines total).

| Term | Occurrences across the whole review surface |
|---|---|
| `purpose` | **0** |
| `goal` | **0** |
| `value` (as project value, not "value of X") | **0** |
| `intent` | **0** |
| `north star` | **0** |
| `rubber stamp` | **0** |
| `vision` | **1** — `review.md:28`, a context-loading bullet: *"**Master HL** for the task — understand vision, design philosophy, architecture decisions"* |

The single hit is an instruction to *read*, attached to no check, no field and no verdict consequence. Every evaluative
surface the reviewer fills — `judge.md`'s 7-row Universal Checklist, the mode checklists, `REVIEW.md` §3 and §4 — is
purely conformance-shaped. HL §3's claim that "every mindset asks *is this true and good?*, none asks *is this what we
set out to do?*" is not an interpretation of the text. There is no text.

Consequence for D4: the forcing function is not strengthening a weak clause; it is the first evaluative appearance of the
concept. Whatever form it takes will be the entire mechanism.

### G2: H12 corollary confirmed mechanically — PV priority 1 cites the wrong file in every TFW project

`glossary.md` PV Index priority 1 reads `README Values` → *"Core beliefs (e.g., Traces Over Code, Structural Enforcement)"*.
Those two named examples are headings inside **`.tfw/README.md` § Values and Principles** — the methodology document.

| Repository | Root `README.md` headings | Has a Values section? | `.tfw/README.md § Values and Principles` |
|---|---|---|---|
| `steps-framework` (TFW) | Who TFW Is For · Quick Start · How It Works · What's Inside · Tool Adapters · Key Concepts · Updating TFW · Links · Task Board | **No** | Present — 8 subsections |
| `ai-first-devices` (AFD) | Проблема · Цель · Устройства · Repository structure · Task Board · Quick Start · For AI Agents · Методология | **No** | Present — **byte-identical** to TFW's (verified by `diff` on the section range: no output) |

Both halves of H12's corollary hold, and the second half is stronger than the HL states:

1. Priority 1 resolves to `.tfw/README.md`, not to the project README. In the TFW repo this is invisible because the
   methodology *is* the product; in AFD it means the highest-priority Project Value source is *Traces Over Code* and
   *Structural Enforcement* while the project is a transit-device fleet platform.
2. The section is **byte-identical across projects**. A "Project Value" source that is the same bytes in every project
   carries zero project information by construction. This is not a resolution bug — priority 1 is structurally incapable
   of holding project purpose.
3. AFD's root README *does* answer the north-star question — `## Проблема` (zoo of vendor MDMs, fragmented management)
   and `## Цель` (own UEM, modular device code, AI-first architecture) — and nothing in the framework points at it.

H12's main clause is therefore **supported in substance and imprecise in form**: the root README *contains* the north
star, but under headings that no framework rule names, and AFD's own agents reach for a different artifact
(`HL-AFD-2`) when they need one. See G3.

### G3: H13 measured — and the anchor itself drifted

`HL-AFD-2__stack_and_architecture.md`, AFD's de-facto north star, referenced from `CLAUDE.md` and `tasks/README.md`.

| Section | Lines | Reviewer-relevant? |
|---|---|---|
| §1 Vision (incl. Business/Technical Impact + owner quote) | 9–36 → **28** | ✅ yes |
| §7 Principles (14 numbered items) | 369–385 → **17** | ✅ yes |
| Everything else (§2 as-is, §3 to-be + 3 visualizations, §4 four phases + scope addenda, §5/§6, §7.1/§7.2, §8–§11) | **464** | ❌ no |
| **Total** | **509** | **45 relevant = 8.8%** |

H13 is confirmed on the size question. Two findings the hypothesis did not anticipate:

**(a) The anchor drifted, and nothing logged it.** Six of §7's fourteen principles carry explicit post-approval markers:
`(Added post-research: D8-2)`, `(Corrected post-research: H3 rejected)`, `(Added post-research: D8-3)`,
`(Added 2026-04-30, post-Q1 ONB-A3: D14)`, and two `(Added 2026-04-30, post-Q3-4 closing)`. §4 additionally carries two
inline blocks titled *"Phase A scope additions (2026-04-30, post Q5/Q6 closing)"* and *"Phase A scope clarifications"*.
The artifact a project designates as its north star is, by TFW-53's own definition, a §7-and-§1-bearing HL — which means
it is **itself a frozen contract that grew by 40% of its principle list after approval, with no amendment log**. If the
anchor is an HL, the freeze must cover the anchor, or the reviewer's reference point drifts exactly like the task HL did.

**(b) Principle grade is uneven.** §7 mixes north-star-grade claims (P1 *AI-first*, P2 *Pure modules*) with
implementation detail (P11 *legacy applicationId*, P14 *GPS: dirty + filtered, Kalman filter*). A reviewer told to
"cite the clause the work serves" against this list can satisfy the requirement with P14 and never touch purpose. The
payload question (D2) is therefore not only about size; it is about **admission criteria** for what may sit in the list.

### G4: The negative-control corpus, recovered and counted precisely

`git ls-tree -r 721ca15` over `tasks/TFW-48*` and `tasks/TFW-49*` — 75 files. The review corpus is:

| Task | Phase | REVIEW file | Final verdict at `721ca15` |
|---|---|---|---|
| TFW-48 | A | `REVIEW__phase-a__method_kernel.md` | ✅ APPROVE |
| TFW-48 | B | `REVIEW__phase-b__planning_research_learning.md` | ✅ APPROVE |
| TFW-48 | C | `REVIEW__phase-c__specification_execution_evidence.md` | ✅ APPROVE |
| TFW-49 | A | `REVIEW__phase-a__canonical_contract_and_validator.md` | ✅ APPROVE |
| TFW-49 | B | `REVIEW__phase-b__workflow_and_adapter_consumption.md` | ✅ APPROVE |
| TFW-49 | C | `REVIEW__phase-c__repository_local_enforcement_migration.md` | ✅ APPROVE |

**Correction to HL §2 (free section, refinement).** The HL states *"All seven phase REVIEWs returned ✅ APPROVE."*
There are **six REVIEW files**. The seventh verdict is the superseded revision of TFW-49/phase-c at `1ebb680`
(*"[codex/TFW-49/phase-c/reviewer] request runtime lifecycle corrections"*, 🔄 REVISE, 7 of 10 Judge checks FAIL), which
the same file later replaced with ✅ APPROVE. TFW-48 phase-d exists at `721ca15` as HL + TS only — it never reached ONB,
RF or REVIEW. The accurate statement is **seven verdicts across six files; six of seven final verdicts were APPROVE, and
the single REVISE was overwritten three commits later.** The substance of the HL's claim is unchanged; the count is not.

**What the six Map sections measure.** Every one of them states scope conformance in units of *files touched*:

> "exactly six framework consumers" · "exactly twelve approved consumers" · "exactly eight framework consumers" ·
> "The declared framework scope is exactly 28 paths" · "remains exactly 29 framework paths" · "No new framework owner or
> out-of-scope implementation change was introduced"

Six reviews, six declarations that the *boundary* held. Zero sentences in any Map, Judge or Verdict section asking what
the work was for. The reviewers were not lazy — they answered the question the framework asked them, thoroughly.

### G5: AFD's Judge scored ✅ on the exact AC that carried the violation

`AFD-38/phase-b/review/judge.md`, HL §7 Principles Check table:

| Principle | Mapped AC | Met? | Evidence (verbatim) |
|---|---|---|---|
| P8 Owner sees what agent sees | **AC-B4** | **✅** | *"send-rate provisioned from DMP `GPS_PUBLISH_EVERY_N`, apply-class LIVE (no rebuild) — V4/V6"* |

Concluding line: *"No principle was mapped to a failed AC. No violation."*

The retraction in `REVIEW__phase-b__device_plane_hygiene.md` §0, one day later:

> *"F1 — Flags/configs bypass the AFD-37 single registry (P8 + single-registry north-star): hotfix, not investment.
> … `gpsPublishEveryN` was a bare `SettingsSnapshot` field with a hand-rolled `GPS_PUBLISH_EVERY_N` wire key. Neither was
> registered … A fleet-wide capability flag/config that bypasses the one typed registry is invisible to the owner-facing
> config plane (violates P8) and forks the single-registry vision. The TS's own words 'AFD-37 позже подхватит его в
> единый реестр' were the hotfix tell I should have blocked. I even noted it … and rationalized it away."*

This is sharper than HL §3 records it. The mapping-integrity check did not merely miss a violation elsewhere — it scored
**✅ on AC-B4, the very AC that contained the violation**, using the same wire key (`GPS_PUBLISH_EVERY_N`) as its evidence
of compliance. The check is not weak; it is structurally inverted. A principle mapped to a passing AC is *guaranteed* to
score ✅ regardless of whether the AC's content honours the principle, because the check reads the checkmark, not the work.

Also recovered: the reviewer's own tell-detector — *"the TS's own words … were the hotfix tell"*. The signal that the
work was a local workaround was **in the TS**, written down, and the reviewer read it and rationalised it. Any drafted
check must make that sentence a trigger rather than a footnote.

### G6: Three concurrent `P{n}` namespaces, and the owner's own directive is ambiguous inside them

DoD-24 asserts a namespace guard. The evidence is stronger than "AFD carries three namespaces":

| Namespace | `P8` resolves to |
|---|---|
| `KNOWLEDGE.md §0` (project-level, 17 items) | *Module = AI context — 200-800 LOC, fits an LLM context window* |
| `HL-AFD-2 §7` (north-star anchor, 14 items) | *Data-driven ads — рекламная инфраструктура = first-class citizen* |
| `HL-AFD-38 §7` (task HL, 10 items) | *Владельцу видно то же, что агенту* |

The AFD reviewer-defence memory rule cites **"P8 (владельцу видно то же, что агенту)"** — the *task-scoped* namespace —
while in the same sentence appealing to "the single-registry **north-star**", which has no P-number in any of the three
lists. The operative rule of the project's most load-bearing review practice cites a principle number that is correct in
one namespace, wrong in two, and pairs it with a north star that is not numbered anywhere. Namespace collision is not a
hygiene concern here; it is already producing ambiguous citations in the exact artifact that the forcing function (D4)
would ask reviewers to produce.

### G7: The framework's failure is retention, not invention — two independent instances

Iteration 1 found one (TFW-48's master DoD-11 + P7, both lost). A second, older instance is in this repository's live
knowledge base:

> `KNOWLEDGE.md` D46 — *"**Reviewer Identity**: overall identity statement (**"Quality guardian, not rubber stamp"**) +
> per-stage mindsets…"*

The shipped text in `review.md:35-36` is:

> *"**Reviewer Identity:** Quality guardian. Your job is to protect the project from unverified claims and incomplete
> work. Trust evidence, not declarations."*

The clause **"not rubber stamp"** — recorded in KNOWLEDGE.md as *part of the decision* — appears **nowhere in `.tfw/`**
(G1). The decision record and the implementation disagree, and the half that went missing is precisely the half this
task is now re-inventing under the name "goal defence".

Two independent losses of the same idea, four months apart, in two projects, through two different mechanisms
(phase-HL re-derivation; decision-to-implementation drift). The design target is not "state the rule well". It is
**"state the rule where it cannot be dropped"** — which is F4 (structural over exhortation) with an empirical base rate.

### G8: AFD verdict base rate, measured rather than cited

`find tasks -name "REVIEW*.md"` → 149 files. Verdict tokens on the header line:

| Token | Count |
|---|---|
| ✅ APPROVE | 134 |
| 🔄 REVISE | 26 |
| ❌ REJECT | 1 |

(161 tokens over 149 files; the excess is verdict-arc headers such as AFD-38/B's *"✅ APPROVE (rev3) … Arc: wrong ✅
APPROVE (rev1) → 🔄 REVISE (§0) → rev2/rev3 fixes → ✅ APPROVE"*.) The HL's figures (1 REJECT, 25 REVISE) are accurate to
within one. Non-approve rate ≈ 18%; goal-grounded non-approves ≈ 4, i.e. **~2.7% of reviews**. A dedicated stage would
therefore report "aligned" in roughly 145 of 149 runs — the H8 argument, re-confirmed on a direct count.

### G9: Verdict vocabulary — the corpus of what real reviewers actually wrote

Harvested verbatim from AFD reviews, because per D28 the naming is the deliverable and per iteration-1 D28 reasoning
terms from real usage outperform invented ones.

| Phrase (verbatim) | Source | What it names |
|---|---|---|
| *«объявленная функция фазы не достигнута»* — "the phase's declared function was not achieved" | AFD-52/B2 REVIEW header, rev1 REVISE reason | Purpose failure against the phase's own declared outcome |
| *"hotfix, not investment"* | AFD-38/B §0 F1; memory rule | The work is a local workaround, not a contribution to the target state |
| *"the TS's own words … were the **hotfix tell**"* | AFD-38/B §0 F1 | A confession of deferral inside the spec, treated as a trigger |
| *"I passed work that violates two of our own principles, which is a **failed quality gate**"* | AFD-38/B §0 | The reviewer's failure, named as a distinct event |
| *"**Verdict retraction** — FAILED GATE"* | AFD-38/B §0 heading | A verdict withdrawn on goal grounds after the fact |
| *"not clean against our architecture and **process values**"* / *"silently expands product scope"* | AFD-24/B REVIEW §Verdict (the single REJECT) | Grounds for the only hard reject in 149 reviews |
| *"The verdict remains REVISE, but **not for the initial wording complaint**. If wording were the only issue, another implementation revision would not be **proportionate**."* | AFD-48/B-S1 REVIEW | The materiality bar, stated by a reviewer under owner challenge |
| *"the reason it still blocks S1 is the approved **value proposition** itself"* | AFD-48/B-S1 REVIEW | The reference point that made the second block legitimate |
| *"This is **provenance, not decoration**."* | **TFW-49's own approved HL §1**, `9e19a4f` | The same idiom, already present in TFW, written by the owner-approved contract that was then breached |

The last row matters: *decoration vs delivery* is not an AFD import. TFW's own approved TFW-49 Vision drew that exact
line, and Phase C then shipped 5,910 lines of Python runtime under it.

### G10: External — the axis already has a standards-grade name

IEEE Std 1012 (System, Software and Hardware Verification and Validation) defines the two questions as a formal pair:

- **Verification** — *"Was the system built right?"* Conformance of a product to the requirements of its activity.
- **Validation** — *"Was the right system built?"* Whether the product satisfies its **intended use** and user needs.

This is exactly TFW-53's split, in a domain-agnostic standard that predates it by decades. It also maps onto the
existing review flow with unusual precision: `verify.md` already performs verification in the strict IEEE sense
(re-running tests, confirming files match RF claims), and the framework has simply never had the validation half.
Naming candidates and their collision risk are stress-tested in Challenge — `validation` is heavily overloaded in
software (schema validation, form validation; TFW-49's own artifacts call a commit-message linter "the validator").

### G11: External — audit standards have already solved the boilerplate problem, and their solution is citation-shaped

From ISA 240 (Revised) and PCAOB documentation standards:

- Documentation must let *"an experienced auditor, having no previous connection with the audit, understand the
  significant professional judgments made"* — the readability-by-a-stranger test, which is what a later agent session is.
- To discourage boilerplate, the standard requires **relating the matter directly to the specific circumstances of the
  entity that influenced the judgement**. Generic assertions are the named failure mode; entity-specific reference is
  the named remedy.
- *"Signing off on an audit program is rarely sufficient"* — a checkmark without documented nature, timing and extent is
  a documented deficiency, not a matter of style.
- Defensible documentation = *expectation → variance found → inquiry made → response → assessment of that response.*

This is independent, standards-grade support for **D4 Alt A/D over Alt B/C**: a citation that resolves to a specific
clause of a specific project's contract is the recognised anti-boilerplate device, and a bare ✅ is a recognised defect.
It is also the same device TFW already adopted once, for the same reason: D43 Knowledge Citations shipped because
*"an agent says 'per D28' without a link — could be hallucinated."*

### G12: External — how change gates degrade, and what the literature says stops it

Change-control-board practice describes the failure mode this task's amendment log and goal check both risk:

- *"Change requests arrive without impact assessments, so the board has no basis for rejection. The board approves
  everything because declining requires a rationale nobody wrote down. After a few cycles the board loses credibility."*
- Named as **"change theater: the appearance of governance with none of its function."**
- The prescribed remedy is **risk-based tiering** — lightweight paths for low-risk changes, deep review reserved for
  high-impact ones — because *"if every change needs the full board, your board will either slow the business down or
  start rubber-stamping. Neither outcome is acceptable."*

Two consequences. First, it corroborates iteration 1's D2 granularity decision from outside the project. Second, it
applies to the goal check itself: a check that must be answered in full on every review is the "every change needs the
full board" configuration. The materiality bar (D6) is the tiering mechanism on the review side — and the literature
says the burden must fall on the *proposer of the block*, i.e. the party asking for the extra cycle.

### G13: External — north-star document practice, and where it does not transfer

Product-management practice on North Star documents converges on: *the problem being solved, the proposed solution, the
factors that matter for success, and the outcomes the product will produce* — sized to be visualisable by the whole team,
and explicitly *"not a feature, not a metric, not a business goal, but a holistic vision that drives product decisions."*

Two transfer failures worth recording now rather than after shipping:

1. Most of the literature couples "North Star" to a **North Star Metric** — a single measurable number. TFW is
   domain-agnostic (F13) and its projects include writing, analytics and business process work where a single metric is
   either absent or actively misleading. TFW must take the *document* sense and explicitly disclaim the *metric* sense,
   or agents will import the metric framing and reviewers will start checking numbers.
2. The literature's payload is written for alignment (a team reading it to decide what to build). The reviewer's need is
   narrower: a **citable claim set** to test a finished result against. "Problem / solution / outcomes" satisfies the
   first and only partially the second — a reviewer also needs the **non-goals**, because the most common purpose
   failure in the corpus is not "did the wrong thing" but "did an adjacent thing that nobody excluded" (TFW-49 Phase C:
   *"safely bypass the current local hook"* → *"install a TFW-owned hook runtime"*).

### G14: The successor task already stated the rule the drifted one violated

TFW-50 re-did TFW-49's problem after the revert. Its approved Vision, `HL-TFW-50 §1`:

> *"Every AI-authored commit is understandable directly in `git log`… **One precise Markdown rule achieves this without
> enforcement software.**"*

Against TFW-49's approved Vision at `9e19a4f`:

> *"…The identity remains **readable without special tooling**, while structural validation prevents quiet drift…
> **This is provenance, not decoration.**"*

And TFW-49's approved Phase C deliverable 1: *"Replace or **safely bypass** the current local branch-prefix hook without
deleting history or unrelated user hooks."* Post-drift (`642c647`): *"install a TFW-owned hook runtime."* Delivered:
5,910 lines of Python runtime and tests, reverted in full.

The approved TFW-49 contract contained the words that condemn its own Phase C — *readable without special tooling*,
*provenance not decoration* — and DoF-6 (*"Normal human commits are blocked even though the approved policy covers only
agent-authored commits"*) was deleted in the same drift commit. **The reference set needed to block TFW-49 Phase C
existed, was owner-approved, and was recoverable from git the whole time.** The reviewers did not lack an anchor; they
lacked an instruction to read one. This is the single most important fact for sizing the intervention: the fix is a
reference-set rule plus a citation requirement, not a new document.

---

## Checkpoint

| Found | Remaining |
|-------|-----------|
| G1 — purpose vocabulary in the review surface: 0 occurrences of `purpose`/`goal`/`intent`/`north star`/`rubber stamp`, 1 of `vision` (a reading instruction) | Whether the anchor must be a new artifact at all, given G14 |
| G2 — PV priority 1 resolves to `.tfw/README.md`, byte-identical across projects; H12 corollary confirmed, main clause supported in substance, imprecise in form | Whether correcting PV priority 1 is in TFW-53 scope or a separate defect (→ Open Question) |
| G3 — H13 confirmed: 45 of 509 lines (8.8%) reviewer-relevant; **and the anchor itself drifted** — 6 of 14 principles added post-approval, unlogged | Whether a designated-HL north star must itself be frozen (→ Extract/Challenge) |
| G4 — corpus is 6 REVIEW files / 7 verdicts, not 7 files; all six Maps measure scope conformance in files-touched | Replay execution (→ Challenge) |
| G5 — the mapping check scored ✅ on AC-B4, the AC that *contained* the violation; the "hotfix tell" was written in the TS and rationalised away | How to make a spec-side deferral confession a trigger |
| G6 — three `P8`s; the owner's own operative rule cites the task-scoped one while appealing to an unnumbered north star | Namespace scheme (→ Extract) |
| G7 — D46's "not rubber stamp" is in KNOWLEDGE.md and absent from `.tfw/`; second independent retention failure | — |
| G8 — 134/26/1 over 149; goal-grounded blocks ≈2.7% | — |
| G9 — verbatim verdict corpus incl. TFW's own *"provenance, not decoration"* | Which terms survive de-domaining (→ Challenge) |
| G10 — IEEE 1012 supplies the standards-grade pair; `verify.md` is already verification in the strict sense | `validation` collision risk (→ Challenge) |
| G11 — audit standards: entity-specific citation is the named anti-boilerplate device; bare sign-off is a named defect | — |
| G12 — CCB: "change theater"; risk-based tiering; burden on whoever asks for the extra cycle | — |
| G13 — north-star literature transfers as *document*, not as *metric*; non-goals are the missing payload element | — |
| G14 — TFW-49's approved contract already contained the clauses that condemn its Phase C, and they were recoverable from git throughout | — |

**Sufficiency:**
- [x] External source used? — G10 (IEEE 1012), G11 (ISA 240 / PCAOB), G12 (CCB practice), G13 (north-star practice). 4 queries, within the 5/stage budget.
- [x] Briefing gap closed? — H12 and H13 answered with measurements; H11's evidentiary basis assembled (G1, G5, G11) for testing in Challenge.
- [x] Dimensions identified? — 7 dimensions × 4 alternatives, none marked preferred.

**Mode-specific (deep):**
- [x] Hypothesis tested? — H12 (mechanical resolution), H13 (line-count measurement).
- [x] Counter-evidence sought? — G14 is counter-evidence against the anchor deliverable itself (the reference set already
      existed); G13 is counter-evidence against importing north-star practice wholesale; G3(a) is counter-evidence
      against the designated-HL locus; G8 is counter-evidence against any high-frequency check design.

**Metacognitive check.** Three findings are genuinely new rather than confirmations. (1) **G3(a)** — the north-star
anchor is itself an unfrozen contract that drifted; nobody in this task had considered that designating an HL as the
anchor imports the exact problem the task exists to fix. (2) **G7** — D46 already contained "not rubber stamp" and it
never shipped, which moves the design target from *authoring* to *retention* and is a second instance of the pattern
iteration 1 found once. (3) **G14** — the reference set that would have blocked TFW-49 Phase C was approved and
retrievable the whole time, which argues the north-star *artifact* is not the load-bearing piece the HL says it is; the
*reference-set rule* is. G5's inversion (✅ scored on the violating AC) was expected in kind but not in this severity.
Sources not checked and deliberately deferred: the other 143 AFD reviews (sampled, not enumerated — the four
goal-relevant ones were already identified by prior recon); ISO 9000's V&V wording as a second standards source, since
IEEE 1012 is sufficient and the budget is better spent on the replay.

Stage complete: YES
→ User decision: autonomous run — self-checkpoint passed, proceeding to Extract.
