# Challenge — "What could go wrong with our conclusions?"
> **Mindset:** Critic. Your job is to break what Extract built. Find the failure modes.
> **Test:** "Did I find a reason our surviving configuration might FAIL in practice?"
> Parent: [HL-TFW-46](../../HL-TFW-46__evidence_layer.md)

## Consistency Checks

### C1: Step 10.5 + Convention + Reviewer (A1+C4) — Stress Test

**Challenge:** Does adding Step 11 (Evidence Collection) break the handoff flow's cognitive rhythm?

**Current flow:**
```
Implement → Test → Build gate → [Evidence] → Pre-RF Gate → Write RF
```

**Test scenarios:**

| Scenario | What happens at new Step 11 | Breaks flow? |
|----------|----------------------------|-------------|
| Web app task, Playwright available | Navigate to deployed URL, take screenshot. 2-5 min | ❌ Natural pause between "code works" and "write about it" |
| API backend task, curl available | Run curl commands, capture output. 1-3 min | ❌ Trivial, almost part of existing verification |
| Trivial task (fix typo in docs) | TS has no Evidence fields → skip step entirely | ❌ Proportional scope (D3) handles this |
| Complex multi-device task (Android + web + API) | Need to deploy, set up scrcpy/adb, take screenshots across devices. 15-30 min | ⚠️ Significant time, but this is EXACTLY where evidence matters most |
| No tools available (no Playwright, no deploy env) | Executor marks DEFERRED for all evidence items | ❌ Honest — DEFERRED is by design (D2) |
| Content task (blog post) | Navigate to published URL, screenshot. Verify citations via curl. 5-10 min | ❌ Manageable, catches real issues (TFW-36 citation fabrication) |

**Verdict:** Step 11 doesn't break cognitive flow. It EXTENDS it naturally: "code works → actually works → document it." The proportional scope mechanism (coordinator can leave Evidence fields empty for trivial tasks) prevents bureaucratic overhead. The only pressure case is complex multi-device tasks — but those are precisely the tasks where evidence is most valuable.

**Counter-argument considered:** "Step 11 will be skipped because agents optimize for speed."
**Response:** Same argument applies to Step 9 (tests) and Step 10 (build gate). Convention + reviewer gate enforcement is the same mechanism that enforces testing. If the reviewer checks for evidence completeness (Judge check #7), agents can't skip it without reviewer catching it.

### C2: Coordinator Prediction (H2) — What if the coordinator gets the Evidence Plan wrong?

**Failure modes:**

1. **Coordinator specifies wrong tool** — e.g., writes "Playwright" but app needs native mobile testing
   - **Fallback:** Executor can deviate from TS Evidence Plan with justification in RF (same as Technical Guidance §6: "Executor MAY deviate with justification")
   - **Structural fix:** Evidence field says what to verify, not mandating how. "Evidence: Verify login page renders correctly" is better than "Evidence: Playwright screenshot of login page"

2. **Coordinator misses an AC that needs evidence** — e.g., forgets to add Evidence for the most critical AC
   - **Fallback:** Executor proactively collects evidence even when Evidence field is empty (proactive tooling principle, HL §7.6)
   - **Structural fix:** This is why the empty Evidence field means "executor decides" — not "no evidence needed"

3. **Coordinator over-specifies evidence for trivial task** — unnecessary bureaucracy
   - **Fallback:** Executor can mark N/A with reason in RF
   - **Risk:** Low — the proportional scope principle (D3) guides coordinators

4. **Coordinator can't predict environment at TS time** — e.g., deploy target unknown until execution
   - **Fallback:** Evidence field: "DEFERRED — deploy target unknown at TS time. Executor determines environment."
   - **This is expected and handled by design**

**Verdict:** H2 confirmed with qualification — coordinator prediction works as a STARTING POINT, not a contract. The executor has freedom to adapt. The Evidence field is guidance, not mandate (parallels Technical Guidance §6 "MAY deviate").

**Important design implication:** The Evidence field instruction in TS template should say: "What to verify in real environment. Executor MAY adapt tool and environment with justification." NOT: "Executor MUST follow exactly."

### C3: Tooling Coverage (H4) — Is 60-65% realistic?

**Challenge to the 60-65% automation estimate from Gather G2:**

| Domain | G2 Estimate | Counter-evidence | Revised |
|--------|-------------|------------------|---------|
| Web UI | 90% | Complex multi-step flows, 2FA, OAuth redirects — Playwright handles most but not all | 85% |
| API/Backend | 95% | External service dependencies, rate limits, auth tokens | 90% |
| Database | 90% | Schema migrations, data integrity across services | 85% |
| Documents | 70% | Print layout, fonts, encoding — Playwright renders but can't verify typographic quality | 60% |
| Blog/CMS | 80% | Social previews, SEO crawlers, citation accuracy (TFW-36!) | 65% |
| Mobile/Android | 10% | **AFD scan: no scrcpy. adb+logcat text evidence for data-plane. Visual = human-only** | 40-50% (data-plane 70%, visual 15%) |
| HR/Tenders | 20% | Portal rendering, published listing — mostly manual | 20% |
| Analytics | 85% | Dashboard visual check — Playwright can screenshot dashboards | 80% |

**Revised overall estimate:** ~60-70% (weighted). H4's 70% threshold is borderline achievable when Android evidence is properly split into data-plane (automatable) vs visual (human).

**Key insight from AFD:** Evidence medium is domain-dependent — browser evidence is VISUAL (Playwright screenshots), Android evidence is DATA-PLANE (adb text output). Same anti-self-deception contract, different artifact type. TFW's Evidence table handles both: Artifact column accepts file paths (PNG) or inline text (adb output).

**H4 verdict:** 🟡 Borderline — 60-70% with proper domain decomposition. The original 70% is achievable if we count data-plane evidence for non-visual domains. The right framing: evidence coverage depends on available tooling PER PROJECT, not per framework.

### C4: Renumbering Risk — Could it break existing projects?

**Challenge:** 22 file updates sounds manageable, but what about existing projects that forked TFW and have RF files with §5 Observations, §6 FC, etc.?

**Analysis:**
- `.tfw/` files: all updated in the Evidence Layer task — no drift
- Existing RF files in `tasks/`: these are HISTORICAL artifacts. They reference old section numbers. This is expected — CHANGELOG.md already has historical §5 references from pre-TFW-25 renumbering
- Knowledge topic files: reference RF §6, RF §7 — would need updating if they cite specific section numbers
- `compilable_contract.md`: reference format resolver needs to handle both old and new numbering for historical compatibility

**Verdict:** Renumbering is a ONE-TIME mechanical operation. Historical artifacts keep their numbering (they're traces). Only `.tfw/` framework files and active templates need updating. This has been done before (KNOWLEDGE.md §5→§4 in TFW-25, TS §4→§5 in TFW-41). Not a blocker.

### C5: Domain-Agnosticity (H1) — Final Validation

**Test:** Does the Evidence table work for ALL domain types from HL §7.4?

| Domain | AC example | Evidence field | Status | Artifact type |
|--------|-----------|----------------|--------|--------------|
| Code (web) | Login page renders | Navigate to localhost:3000, screenshot | VERIFIED | evidence/login.png |
| Code (API) | Endpoint returns 200 | curl -v /api/health, paste output | VERIFIED | inline |
| Analytics | Report shows correct totals | DB MCP query, paste result | VERIFIED | inline |
| Blog | Post renders without broken styles | Playwright screenshot of published URL | VERIFIED | evidence/blog_render.png |
| HR | Job listing published on portal | Manual check on portal — DEFERRED (needs user login) | DEFERRED | — |
| Design | Mockup matches specification | Visual comparison — DEFERRED (needs human judgment) | DEFERRED | — |
| Document | PDF opens without encoding issues | Open PDF, screenshot first page | VERIFIED | evidence/doc_page1.png |
| Mobile app | App launches, main screen loads | scrcpy screenshot via adb (if available) — or DEFERRED | VERIFIED/DEFERRED | evidence/app_screen.png or — |

**Verdict:** H1 ✅ confirmed — the Evidence table + 4-status vocabulary works across all domains. The key is that DEFERRED is not a failure — it's honest reporting. Domain-specific differences are in evidence TYPE (screenshot vs query vs curl output), not in evidence STRUCTURE (the table is universal).

### C6: "Evidence becomes another checkbox" (HL DoF-1) — Stress Test

**The most critical failure mode from HL §6.**

**How it could happen:**
1. Agent reads Evidence table, writes "VERIFIED" for all items without actually doing anything
2. Agent takes a screenshot of localhost but the app isn't actually running (empty page)
3. Agent writes plausible evidence descriptions from memory without executing

**How the design prevents it:**

| Prevention | Mechanism | Where |
|------------|-----------|-------|
| Artifact requirement | VERIFIED must reference a file path or inline output | Anti-pattern R1 in §14 |
| Temporal ordering | Evidence collected BEFORE RF writing (Step 11 before Step 12-13) | Handoff.md flow |
| Reviewer verification | Reviewer checks that artifacts exist and match claims | Review verify.md, Judge check #7 |
| DEFERRED honesty | DEFERRED is structurally easier than fabricating evidence | 4-status vocabulary (D2) |
| Proportional scope | Trivial tasks can skip evidence entirely (empty Evidence fields) | TS design, D3 |

**Verdict:** The design makes fabrication HARDER than honest reporting. Fabricating a plausible screenshot requires deploying the app (which IS the evidence). Writing DEFERRED takes 5 seconds. The incentive structure favors honesty.

**Remaining risk:** Agent takes real screenshot but of wrong thing (e.g., screenshots the code instead of the running app). This is a quality-of-evidence issue, not a structural issue. The reviewer catches it during Evidence Audit.

---

## OODA Loop Summary

**Loop 1:** Stress-tested A1+C4 (Step 10.5 + convention + reviewer) against 6 scenarios. Holds. Key: proportional scope prevents bureaucracy, reviewer gate prevents skipping.

**Loop 2:** Challenged coordinator prediction (H2). Confirmed with qualification: Evidence field is guidance, not contract. Executor MAY adapt. Important template instruction implication.

**Loop 3:** Challenged tooling coverage (H4). Refuted 70% target, reframed: any automation > 0% is a win. DEFERRED/BLOCKED handles the rest. Pending: Android scrcpy/adb data from AFD project scan.

## Checkpoint

### Sufficiency Verdict
- [x] External source used? — Compliance contemporaneous documentation principle, industry "shift-left verification" pattern
- [x] Briefing gap closed? — All surviving configurations stress-tested
- [x] Hypothesis tested? — H1 (✅ confirmed), H2 (✅ confirmed with qualification), H4 (❌ refuted as stated, ✅ reframed)
- [x] Counter-evidence sought? — Yes: coordinator prediction failures, DoF-1 checkbox risk, renumbering compatibility, tooling automation limits

### Metacognitive Check
The most valuable NEW insight from Challenge is the **reframing of H4**. The original question "Can 70% of evidence be automated?" is the WRONG question. The right question is "Does the design handle the gap between automated and manual evidence honestly?" And it does — via DEFERRED/BLOCKED. This reframing eliminates a whole class of objections ("but you can't automate evidence for HR documents!") — true, and that's fine, because the design accounts for it structurally.

The second new insight is that the Evidence field in TS should be phrased as GUIDANCE, not mandate — paralleling Technical Guidance §6's "MAY deviate" clause. This prevents the coordinator from over-constraining the executor.

**Pending:** AFD Android evidence scan results (scrcpy/adb patterns). Will integrate into RES when available.

---
Stage complete: YES
