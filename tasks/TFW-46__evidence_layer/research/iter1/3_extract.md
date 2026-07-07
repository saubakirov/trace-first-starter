# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-46](../../HL-TFW-46__evidence_layer.md)
> Goal: Close the gap between "RF says done" and "actually works for the user" by adding an Evidence layer to TFW.

## Configuration Space

Dimensions from Gather:
- **D1: Terminology** — Evidence / Proof / Attestation / Acceptance
- **D2: Scope** — Universal / Proportional / Mode-based
- **D3: Status Vocabulary** — 4-status (VERIFIED/DEFERRED/BLOCKED/N/A) / 6-status (AFD PASS/FAIL/XFAIL/XPASS/BLOCKED/SKIP) / Organic (per-project)
- **D4: Artifact Storage** — evidence/ subfolder / Inline in RF / External reference / Mixed

Full cross-product = 4×3×3×4 = 144 combinations. Filtering to configurations where ≥1 dimension differs from the HL's default proposal (C1).

| Config | D1: Term | D2: Scope | D3: Statuses | D4: Storage | Notes |
|--------|----------|-----------|-------------|-------------|-------|
| **C1** | Evidence | Proportional | 4-status (VERIFIED/DEFERRED/BLOCKED/N/A) | Mixed (folder + inline) | HL's proposal |
| **C2** | Evidence | Universal | 4-status | evidence/ subfolder | AFD-inspired: all tasks get evidence folder |
| **C3** | Evidence | Proportional | 6-status (PASS/FAIL/XFAIL/XPASS/BLOCKED/SKIP) | evidence/ subfolder | AFD vocabulary transplanted to TFW |
| **C4** | Evidence | Mode-based | 4-status | Mixed | Evidence modes like review modes (code/docs/spec) |
| **C5** | Proof | Proportional | 4-status (PROVEN/DEFERRED/BLOCKED/N/A) | Mixed | HL's design with "Proof" terminology |
| **C6** | Attestation | Proportional | 4-status (ATTESTED/DEFERRED/BLOCKED/N/A) | Inline in RF | Formal attestation model |
| **C7** | Acceptance | Universal | 4-status (ACCEPTED/DEFERRED/BLOCKED/N/A) | External reference | Acceptance testing frame |
| **C8** | Evidence | Proportional | 4-status | Inline in RF only | Minimal: no folder, just RF table |
| **C9** | Evidence | Universal | 6-status | evidence/ subfolder | Full AFD model transplanted wholesale |
| **C10** | Evidence | Proportional | 4-status + PARTIAL | Mixed | Extended vocabulary: PARTIAL for partly-verified items |

## Findings

### E1: Template Integration Analysis — Where Evidence Sections Fit

Current template structure (section numbers):

| Template | Current Sections | Evidence Insertion Options |
|----------|-----------------|--------------------------|
| **TS** | §1 Objective, §2 Scope, §3 Principles Check, §4 Affected Files, §5 AC, §6 Technical Guidance, §7 DoF, §8 Risks, §9 Cross-Phase | **Option A:** New §10 Evidence Plan (after §9). **Option B:** Embed in §5 AC per item (Gate → Evidence requirement) |
| **RF** | §1 What Was Done, §2 Key Decisions, §3 AC, §4 Verification, §5 Observations, §6 Fact Candidates, §7 Strategic Insights, §8 Diagrams | **Option A:** New §5 Evidence (between current §4 and §5, renumbering §5-8 to §6-9). **Option B:** Extend §4 into §4.1 Synthetic + §4.2 Evidence. **Option C:** New final §9 Evidence |
| **REVIEW** | §1 Map, §2 Verify, §3 Judge, §4 Verdict, §5 Tech Debt, §6 Traces, §7 Fact Candidates | **Option A:** New row in §3 Judge (check #7: "Evidence verified?"). **Option B:** New §2.1 Evidence Audit under Verify. **Option C:** New §3.5 Evidence Audit between Judge and Verdict |

**Cross-template consistency analysis:**

The HL proposes three matching sections: Evidence Plan (TS) → Evidence (RF) → Evidence Audit (REVIEW). Per D28, the *name* should be consistent across the pipeline. Let me check what cognitive mode each triggers:

| Role | Section | Cognitive Mode | Naming Pattern |
|------|---------|---------------|----------------|
| Coordinator | Evidence Plan | Design/anticipation — "what proof will we need?" | Plan = future-oriented, design |
| Executor | Evidence | Collection/honesty — "what did I actually observe?" | Evidence = present-tense, factual |
| Reviewer | Evidence Audit | Verification/skepticism — "does the evidence hold?" | Audit = verification, checking |

I notice these are three *different* cognitive modes — per conventions.md §3 Visual Sections, different cognitive modes → per-template naming. The proposed naming (Evidence Plan / Evidence / Evidence Audit) correctly applies this pattern.

### E2: Vocabulary Comparison — 4-status vs 6-status

| Status | HL 4-status | AFD 6-status | Meaning | When used |
|--------|-----------|-------------|---------|-----------|
| Positive confirmed | VERIFIED | PASS | Observable outcome matches expectation | After successful live check |
| Negative confirmed | — | FAIL | Observable outcome doesn't match | After failed live check |
| Known-gap (expected) | — | XFAIL | Known broken, failed as expected | When checking known issues |
| Known-gap (surprise) | — | XPASS | Known broken, but unexpectedly worked | When known issue is fixed |
| Can't run | BLOCKED | BLOCKED | Precondition not met | Missing environment/tools |
| Intentionally skipped | N/A | SKIP | Not applicable or explicitly skipped | Trivial tasks, irrelevant ACs |
| Deferred to human | DEFERRED | — | Needs human action (deploy, review) | CL-gates, user-only verification |

**Key differences:**

| Factor | 4-status (HL proposal) | 6-status (AFD) |
|--------|----------------------|---------------|
| FAIL handling | No explicit FAIL — absence of VERIFIED implies something isn't proven | Explicit FAIL — forces honest recording of actual failures |
| Expected failures | No XFAIL/XPASS — no vocabulary for "this was known broken" | XFAIL/XPASS — distinguishes known-gap from regression |
| Proportionality | Lower cognitive overhead — 4 states to learn | Higher precision — 6 states, more nuance |
| Fit for TFW | Good for methodology framework (simpler) | Good for testing system (more precise) |
| Agent behavior | Agent marks VERIFIED or DEFERRED — binary honest/not-ready | Agent must distinguish PASS from XFAIL from FAIL — more analytical |

**I notice:** AFD's 6-status vocabulary is designed for a *testing system* — it distinguishes regressions (FAIL) from known gaps (XFAIL) from surprises (XPASS). TFW Evidence is not a testing system — it's a *verification layer* in a methodology framework. The key question TFW Evidence answers is: "Was this AC actually observed in a real environment?" — not "Did this test pass or fail?"

For TFW, the executor is not running a test suite — they're demonstrating that their work produces the intended outcome in reality. The vocabulary should reflect:
1. "I demonstrated it" (VERIFIED)
2. "I couldn't demonstrate it and here's why" (DEFERRED — honest gap)
3. "I'm blocked from demonstrating it" (BLOCKED — external dependency)
4. "This AC doesn't require live demonstration" (N/A — coordinator-set or executor-justified)

FAIL and XFAIL/XPASS are testing concepts that don't map to TFW's evidence model. If the executor tries to demonstrate AC-3 and it doesn't work — that's not "FAIL evidence," that's "the AC isn't met." The executor goes back and fixes it or escalates. Evidence status tracks *verification completeness*, not *test outcomes*.

### E3: Scope Analysis — Universal vs Proportional vs Mode-based

| Approach | How it works | Pros | Cons |
|----------|-------------|------|------|
| **Universal** | Every task gets an Evidence section, every AC gets an evidence row | Consistent, no judgment needed | Bureaucratic for trivial tasks (fix a typo → evidence of what?) |
| **Proportional** | Coordinator calibrates evidence depth in Evidence Plan at TS time | Flexible, matches risk to effort | Coordinator might under-specify; inconsistent across tasks |
| **Mode-based** | Evidence modes (like review modes: code/docs/spec) with per-mode checklists | Structured proportionality | Adds complexity (mode files, selection step); review already has modes |

**Cross-reference with user's Q2 answer and project scan:**

User described document/spreadsheet failures (layout breaks, encoding, colors). These are *visual* evidence tasks — the evidence is a screenshot proving it looks right. For code tasks, evidence might be a curl response or browser screenshot. For content tasks, evidence is source verification.

I notice the **proportional** approach handles this naturally: the coordinator writes an Evidence Plan that says "take a screenshot of the rendered Excel" or "verify the deployed API returns correct data." Mode-based adds overhead (another mode selection step, mode files) without clear benefit — the proportionality is already expressed in the Evidence Plan.

But there's a risk: coordinator forgets to write an adequate Evidence Plan. Mitigation: the Evidence Plan section in TS should include a *minimum* — at least one evidence item per AC, even if it's "N/A (typo fix — visual inspection not required)."

### E4: Section Placement in RF — Merge vs Separate

Two structural options for RF:

**Option A: Separate sections** (§4 Verification + §5 Evidence)
```
§4. Verification — lint: OK, tests: OK, build: OK (synthetic tools)
§5. Evidence — what was actually observed in real environment (with artifacts)
```

**Option B: Merged section** (§4 Verification with subsections)
```
§4. Verification
  §4.1 Synthetic — lint: OK, tests: OK, build: OK
  §4.2 Evidence — what was actually observed (with artifacts)
```

| Factor | Option A: Separate | Option B: Merged |
|--------|-------------------|------------------|
| Cognitive mode | Two distinct modes: "tools ran OK" vs "I observed this in reality" | One mode: "verification" (blurs the synthetic/real distinction) |
| Per D28 (naming) | "Evidence" as a separate heading triggers "produce real artifacts" | "Verification §4.2" triggers "this is another verification step" — weaker |
| Section numbering | Requires renumbering §5-8 → §6-9 (breaking change) | No renumbering needed |
| Proportionality | Executor can write "No evidence required (typo fix)" in §5 | Executor can write §4.2 as "N/A" but the subsection still exists |
| HL's DoF-2 | HL says evidence shouldn't be redundant with §4 — separate sections make distinction clear | Merged risks conflation: reviewer might skip §4.2 because they already "checked §4" |

**I notice:** The HL explicitly says (DoF-4): "if evidence doesn't add anything beyond what §4 Verification already captures, it's redundant." Merging them makes this harder to enforce because the boundary becomes fuzzy. Separate sections with different names (Verification vs Evidence) create a structural boundary that agents can't accidentally cross.

### E5: Evidence Plan Integration in TS

Three integration points in the TS template:

**Option A: Standalone §10 Evidence Plan** — new section at the end
- Coordinator writes a table: per AC, what evidence is required, what tools/environment needed
- Standalone = executor can find it in one place
- But separated from the AC items it references

**Option B: Embedded in §5 AC** — each AC gets an Evidence field alongside Gate
```
### AC-1: Login page renders
- [ ] Page loads at /login
Gate: Browser test passes
Evidence: Screenshot of login page at localhost:3000 in Chrome (live, not test harness)
```
- Tight coupling: evidence requirement is right next to the AC
- But makes AC items longer; might feel heavy for trivial ACs

**Option C: Hybrid** — §5 AC has Evidence field per item (compact), §10 has evidence environment/tooling notes
- Best of both: AC items know what evidence they need, but environment setup is centralized
- But two places to maintain

**Cross-reference with existing TS pattern:** §5 AC already has a `Gate:` field. Adding `Evidence:` as a parallel field keeps the pattern consistent. The Gate says "how to verify synthetically" and Evidence says "how to verify in reality." This is clean — same cognitive mode (what to verify), different verification context (synthetic vs real).

### E6: Non-obvious Configuration — C8 (Inline Only, No Folder)

C8 proposes: Evidence stays entirely inline in the RF, no evidence/ subfolder.

**Arguments for:**
- Simplest implementation — no new folder convention
- Works for content tasks (source audit table is inline)
- No file management overhead

**Arguments against:**
- Screenshots and logs are binary/large — inline RF would be huge
- Evidence artifacts are reusable (reviewer needs to inspect them independently)
- AFD's mature pattern uses folders because evidence scales
- Inline evidence can't be inspected without opening the RF

**Verdict:** Inline works for text evidence (command output, URLs visited, query results). Folder works for binary evidence (screenshots, recordings, exports). Mixed = the natural answer. But the folder should be optional, not mandatory — many tasks produce only text evidence.

### E7: Review Integration — Evidence Audit Placement

Current review flow: Map → Verify → Judge → Decide.

Evidence Audit maps naturally to **Verify** stage (§2). The reviewer is already checking RF claims against reality. Adding evidence checks:

| Current Verify checks | Proposed Evidence checks |
|----------------------|------------------------|
| File changes match RF §1 | Evidence artifacts exist (files referenced in Evidence table) |
| Build/test results reproducible | Evidence status matches observable reality (spot-check 1-2 items) |
| Code quality acceptable | DEFERRED items have honest reasons |
| | No VERIFIED items without corresponding artifacts |

This extends §2 Verify rather than adding a new section. The judge (§3) gets one new check: "Evidence completeness — are all AC items covered?"

## Checkpoint

| Found | Remaining |
|-------|-----------|
| 10 configurations spanning the design space | Pairwise incompatibility analysis (Challenge) |
| Template integration analysis: Evidence Plan (TS) → Evidence (RF) → Evidence Audit (REVIEW) | Final placement decision |
| 4-status vocabulary justified over 6-status (different purpose: evidence ≠ testing) | Edge case stress-testing |
| Separate §5 Evidence preferred over merged §4.2 | Renumbering cost analysis |
| AC-level Evidence field in TS (parallel to Gate) | Feasibility of hybrid approach |
| Inline + optional folder = Mixed storage optimal | Folder convention details |
| Evidence Audit extends Review §2 Verify (not new section) | Judge §3 checklist item |

**Sufficiency:**
- [x] External source used? Yes — referenced Gather's external findings; template analysis is internal
- [x] Briefing gap closed? Yes — template integration points identified, vocabulary justified, scope decision analyzed
- [x] Configuration Space built from Gather dimensions? Yes — 10 configurations, meaningful cross-references

**Metacognitive check:** I discovered several things I didn't see before:
1. The Gate/Evidence parallel in TS §5 — Gate = synthetic, Evidence = real. Same cognitive mode, different context. Nobody proposed this in the Briefing.
2. 4-status is justified because TFW Evidence ≠ testing system. FAIL/XFAIL/XPASS are test concepts, not evidence concepts. If evidence "fails," the AC isn't met — go fix it.
3. Evidence Audit maps to existing Verify stage, not a new section — this is simpler than the HL anticipated.

Stage complete: YES
→ User decision: ___
