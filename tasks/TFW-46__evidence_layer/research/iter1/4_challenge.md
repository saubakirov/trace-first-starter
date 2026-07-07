# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW-46](../../HL-TFW-46__evidence_layer.md)
> Goal: Close the gap between "RF says done" and "actually works for the user" by adding an Evidence layer to TFW.

## Consistency Check

Take each pair of dimensions from Gather and ask: "Can Alternative X coexist with Alternative Y?"

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1: Term | Proof | D3: Statuses | Any with DEFERRED | "Deferred proof" is linguistically contradictory — proof implies certainty; you can't defer certainty, only evidence |
| D1: Term | Attestation | D2: Scope | Proportional | Attestation = formal signed claim — proportionality undermines formality. You either attest or you don't; you can't "partly attest" |
| D1: Term | Acceptance | D2: Scope | Universal | "Acceptance evidence for a typo fix" = bureaucratic absurdity. Acceptance implies requirements-gate, which trivial tasks don't have |
| D2: Scope | Universal | D3: Statuses | 6-status (AFD) | 6-status requires analytical judgment (XFAIL vs FAIL vs XPASS) for every task — excessive for a universal methodology framework |
| D2: Scope | Mode-based | D4: Storage | Inline only | Mode-based implies structured evidence practices — inline-only contradicts this by being the least structured option |
| D3: Statuses | 6-status (AFD) | D4: Storage | Inline only | PASS/FAIL/XFAIL/XPASS implies per-scenario testing with evidence artifacts — inline-only can't hold screenshots/logs per scenario |
| D1: Term | Proof | D4: Storage | Inline only | "Proof" connotes definitive demonstration — inline text-only undermines the weight of the word |
| D3: Statuses | Organic | D2: Scope | Universal | Universal scope demands consistency — organic per-project vocabulary is the opposite of universal |

**Surviving configurations** (from Extract's Configuration Space, after removing rows containing incompatible pairs):

| Config | D1: Term | D2: Scope | D3: Statuses | D4: Storage | Notes |
|--------|----------|-----------|-------------|-------------|-------|
| **C1** | Evidence | Proportional | 4-status (VERIFIED/DEFERRED/BLOCKED/N/A) | Mixed | HL's proposal — no incompatibilities |
| **C3** | Evidence | Proportional | 6-status (PASS/FAIL/XFAIL/XPASS/BLOCKED/SKIP) | evidence/ subfolder | Survives but heavy — AFD testing vocabulary may not fit methodology |
| **C4** | Evidence | Mode-based | 4-status | Mixed | Survives but adds complexity (mode files) |
| **C8** | Evidence | Proportional | 4-status | Inline only | Survives but limited for binary evidence |
| **C10** | Evidence | Proportional | 4-status + PARTIAL | Mixed | Survives — PARTIAL adds nuance but also complexity |

**Eliminated:**
- C2 (Universal + 4-status): survives technically but Universal scope is challenged below as bureaucratic
- C5 (Proof): eliminated — "Deferred Proof" is contradictory
- C6 (Attestation): eliminated — proportional attestation is contradictory
- C7 (Acceptance): eliminated — universal acceptance is bureaucratic
- C9 (Universal + 6-status): eliminated — 6-status + universal = excessive

**Unexpected survivors:**
- **C8 (Inline only):** survived despite seeming weak — because many tasks (docs, analytics, content) produce *text* evidence (query results, URLs, source tables), not screenshots. For these tasks, inline is sufficient and simpler. This suggests the folder should be optional, not mandatory.
- **C10 (4-status + PARTIAL):** survived — PARTIAL status addresses a real gap: "I verified part of this AC but not all." However, it adds a 5th status, increasing vocabulary complexity.

## Findings

### C1: Stress-test C1 (HL proposal) against edge cases

| Edge case | How C1 handles it | Verdict |
|-----------|-------------------|---------|
| **Typo fix** (trivial task) | Coordinator writes Evidence Plan: "N/A — visual diff in PR sufficient" or evidence row with N/A status. One line per AC | ✅ Acceptable — proportional design handles this cleanly |
| **Blog post** (content task) | Evidence Plan: "Verify rendered page at published URL, fact-check 3 external citations." Evidence: screenshot + source audit table | ✅ Works — the Blog TFW-36 pattern already does this ad-hoc |
| **Excel spreadsheet** (document task) | Evidence Plan: "Screenshot of rendered Excel at default zoom, verify cell sizing, check encoding." Evidence: screenshot + inline notes | ✅ Matches user's Q2 exactly — visual evidence captures layout/color/encoding issues |
| **API deployment** (code task) | Evidence Plan: "Curl live endpoint, verify response body, check logs." Evidence: command output + status codes | ✅ Standard — AFD/helpdesk already do this |
| **Mobile device** (hardware task) | Evidence Plan: "On-device screenshot, logcat output, sensor reading." Evidence: screenshots + raw logs in evidence/ folder | ✅ Matches AFD device gate pattern |
| **Analytics query** (data task) | Evidence Plan: "Run query on real data, verify result count and sample rows." Evidence: query output inline | ✅ Inline sufficient — no folder needed |
| **Task with no deployable output** (pure docs/config) | Evidence Plan: "N/A — this task modifies framework files only. Lint + build sufficient." | ✅ Honest N/A — proportional design allows this |
| **Task where evidence is impossible** (needs user's device/printer) | Evidence Plan: "DEFERRED — requires user's device. Describe what user should verify." | ✅ DEFERRED with reason — honest incompleteness principle |

**C1 survives all edge cases.** The proportional design + 4-status vocabulary handles the full spectrum from trivial to complex, code to non-code.

### C2: Stress-test C3 (6-status AFD vocabulary) — why it doesn't fit

| AFD Status | TFW Evidence context | Problem |
|-----------|---------------------|---------|
| PASS | AC evidence verified | Synonymous with VERIFIED. "PASS" triggers "test passed" frame — but evidence isn't a test, it's an observation |
| FAIL | AC evidence showed failure | If evidence shows the AC fails, the executor must **fix the AC**, not record evidence. FAIL is a test outcome, not an evidence status. Evidence records what was observed *after* the work is done |
| XFAIL | Known broken, expected to fail | Doesn't apply — TFW Evidence verifies *completed work*, not known-broken features. If something is known-broken, it shouldn't be in the AC |
| XPASS | Known broken but unexpectedly worked | Same — irrelevant for completed-work verification |
| BLOCKED | Can't verify | Maps to BLOCKED. Identical meaning |
| SKIP | Not applicable | Maps to N/A. Similar meaning |

**Conclusion:** AFD's 6-status vocabulary is for a *testing system* that runs against potentially-broken features. TFW Evidence is for a *verification layer* that confirms completed work in real conditions. FAIL/XFAIL/XPASS are structurally irrelevant because:
1. If evidence collection reveals a failure → the executor goes back and fixes the work, then collects evidence again
2. Evidence is collected *after* development, not *during* testing
3. Known-broken features shouldn't appear in AC items

C3 eliminated from serious consideration.

### C3: Stress-test C4 (Mode-based) — why it adds unnecessary complexity

| Factor | Mode-based Evidence | Proportional Evidence (C1) |
|--------|--------------------|-----------------------------|
| Implementation | Mode files in `.tfw/workflows/evidence/` (code.md, docs.md, spec.md) | Evidence Plan in TS — coordinator specifies per task |
| Selection | Agent selects mode at Evidence Plan time — needs WAIT gate | Coordinator writes Evidence Plan directly — no selection step |
| Flexibility | Per-mode checklists — fixed patterns per domain | Free-form — coordinator writes what matters for this specific task |
| Overhead | 3+ mode files to maintain, synced across adapters | One TS section — zero extra files |
| Parallel with review | Review already has modes (code/docs/spec) — evidence modes would need to align | No parallel needed — evidence is per-AC, not per-mode |

**The key argument against modes:** Review modes work because different task types need different *checklists* (code review checks ≠ docs review checks). Evidence doesn't need checklists — it needs *per-AC demonstration*. What constitutes evidence for AC-1 is entirely determined by what AC-1 does, not by whether the task is "code" or "docs."

A blog post task might have AC-1 (content structure — verify word count) and AC-2 (published rendering — verify screenshot). These are different evidence types *within the same task* — modes wouldn't help.

C4 eliminated — proportional (C1) provides the same flexibility with zero overhead.

### C4: Stress-test C10 (PARTIAL status) — worth adding?

**Scenario:** Executor verified AC-3 on Chrome but not Firefox. Should the status be VERIFIED or something else?

| With 4-status | With 5-status (+ PARTIAL) |
|---------------|--------------------------|
| VERIFIED with note: "Chrome only. Firefox not tested — no access to Firefox." | PARTIAL with note: same |
| Reviewer sees VERIFIED + note, decides if sufficient | Reviewer sees PARTIAL, knows to check details |

**Argument for PARTIAL:** It signals "I did some work but it's incomplete" — which is different from both VERIFIED ("all done") and DEFERRED ("nothing done").

**Argument against PARTIAL:** It's the slippery slope status. "PARTIAL" becomes the default for agents who don't want to commit to VERIFIED or DEFERRED. It muddies the signal: what does "partial" mean? 50% done? 90%? The note explains everything PARTIAL would convey, without adding a 5th vocabulary item.

**Counter-evidence sought:** In AFD testing (80 scenarios, 12 runs), is there a pattern of "partly passed" scenarios? AFD doesn't have PARTIAL — it has PASS/FAIL/XFAIL per scenario. Each scenario is either verified or not. The granularity is at the *scenario* level, not at a vague "partial" level.

**Verdict:** PARTIAL rejected. If evidence is partial, the correct approach is:
1. Split the AC-level evidence into sub-items (AC-3a: Chrome, AC-3b: Firefox)
2. Mark AC-3a VERIFIED, AC-3b DEFERRED (reason)

This keeps the vocabulary crisp and forces the executor to be specific about what was and wasn't verified.

C10 eliminated.

### C5: Section Renumbering Cost Analysis

Adding §5 Evidence to RF requires renumbering:
- Current §5 Observations → §6
- Current §6 Fact Candidates → §7
- Current §7 Strategic Insights → §8
- Current §8 Diagrams → §9

**Impact:**
- All existing RF files reference §6/§7/§8 by number in conventions.md, templates, and anti-patterns
- REVIEW §3 check #6 references "RF completeness (§6-8 present)" — would become "§7-9 present"
- conventions.md §14 references "Executor omits RF §6-8" — would need update
- Compilable contract may reference section numbers

**Mitigation:** This is a one-time cost, done in Phase A. All references are in `.tfw/` files that the executor controls. No external dependencies.

**Alternative (no renumber):** Place Evidence at the end as §9. But this is semantically wrong — Evidence should come *before* Observations and Facts because it's part of the "what I did" narrative (§1-§5), not the "what I learned" narrative (§6-§8). Evidence at the end feels like an afterthought.

**Verdict:** Accept renumbering cost. §5 Evidence is the right placement — it follows §4 Verification as the next logical step: "tools say OK (§4), and here's what it looks like in reality (§5)."

### C6: Counter-evidence — When Evidence Is Pure Bureaucracy

Deliberately seeking domains where the Evidence layer adds no value:

| Scenario | Does Evidence add value? | Analysis |
|----------|------------------------|----------|
| **TFW framework task** (modify conventions.md) | Questionable | "Evidence of conventions.md change" = reading the file? Tests don't apply. But: lint + build is synthetic, and rendering the mkdocs site IS evidence (TFW-27 deployed docs). Verdict: low value but not zero |
| **Infrastructure task** (modify docker-compose) | Yes | Synthetic: yaml lint passes. Evidence: services actually start, health checks respond. Real gap exists |
| **Research task** (write RES) | No | RES is a document produced by the researcher. Evidence = the document exists and is well-formed. This is tautological. Verdict: N/A is appropriate |
| **Pure planning task** (write HL/TS) | No | HL/TS are planning documents. Evidence = they exist. Tautological. Verdict: N/A is appropriate |

**Finding:** Evidence is most valuable when there's a gap between "file exists" and "it works in reality." Document/plan tasks have no such gap — the file IS the output. The proportional approach (C1) handles this correctly: coordinator marks "N/A" in Evidence Plan for tasks where the output is the document itself.

**But I notice a risk:** If too many tasks get "N/A" Evidence Plans, agents will habituate to N/A and skip evidence even when it's needed. Mitigation: the reviewer explicitly checks "was N/A justified?" in the Evidence Audit. The anti-self-deception rule from AFD: "If you cannot verify an outcome → BLOCKED, never assumed PASS." Adapted for TFW: "If evidence is marked N/A, the reviewer asks: could evidence have been collected?"

### C7: Counter-evidence — Does the Term "Evidence" Produce Wrong Behavior?

Per D28, let me actively seek cases where "Evidence" might trigger wrong agent behavior:

| Potential misfire | Likelihood | Analysis |
|------------------|-----------|----------|
| Agent treats Evidence as "legal evidence" — overly formal, document-heavy | Low | Context (TS section + RF section) constrains interpretation. No agent would write legal briefs in a methodology RF |
| Agent confuses Evidence with existing §4 Verification | Medium | Mitigated by separate sections with different names. §4 = "Verification (synthetic)," §5 = "Evidence (real)." Labels distinguish them |
| Agent produces excessive evidence (screenshot of every line) | Low | Proportional design + Evidence Plan constrains scope. Coordinator specifies what's needed |
| Agent marks everything VERIFIED without real artifacts | Medium | Anti-pattern in conventions.md §14 + reviewer gate in Evidence Audit. Structural enforcement: VERIFIED without artifact = violation |

**Strongest counter-evidence found:** The word "Evidence" might be *too passive* — it implies "showing what happened" rather than "actively demonstrating." Compare with "Demonstration" which implies active showing. But "Demonstration" has its own problems: "demonstration section" sounds like a demo/tutorial. "Evidence" is better because it's a *noun for artifacts*, not an action verb — and TFW needs artifacts, not performances.

**Verdict:** No serious misfire scenarios found. "Evidence" produces the right behavior.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C1 (HL proposal) survives all 8 edge cases + pairwise checks | None — C1 is robust |
| C3 (6-status) eliminated — testing vocabulary ≠ evidence vocabulary | — |
| C4 (mode-based) eliminated — proportional provides same flexibility, zero overhead | — |
| C5 (Proof) eliminated — "Deferred Proof" is contradictory | — |
| C6 (Attestation) eliminated — proportional attestation is contradictory | — |
| C7 (Acceptance) eliminated — "universal acceptance" = bureaucratic | — |
| C8 (inline only) eliminated as sole approach — but inline IS valid for text evidence | — |
| C10 (PARTIAL) eliminated — split into sub-items instead | — |
| Renumbering cost acceptable — §5 Evidence is right placement | — |
| N/A habituation risk identified — reviewer must check "was N/A justified?" | Anti-pattern for §14 |

**Sufficiency:**
- [x] External source used? Yes — referenced Gather's external findings throughout
- [x] Briefing gap closed? Yes — all configurations evaluated, survivors identified
- [x] Pairwise incompatibility checked? Yes — 8 incompatible pairs identified, 5 configurations eliminated
- [x] Hypothesis tested? H6 confirmed (Evidence is the right term), H7 confirmed (naming affects behavior — "Proof" would block DEFERRED, "Acceptance" would be bureaucratic)
- [x] Counter-evidence sought? Yes — actively sought domains where Evidence adds no value (planning tasks), sought term misfires, sought scenarios where 6-status might be better

**Metacognitive check:** The biggest discovery was the **testing-vs-evidence distinction** (C2/C3 analysis). I started assuming AFD's 6-status vocabulary might be better (more precise). After analysis, I found it's designed for a fundamentally different purpose — testing known/unknown features vs verifying completed work. This is NEW — it wasn't in the Briefing, and it changes the design rationale for vocabulary choice.

Stage complete: YES
→ User decision: ___
