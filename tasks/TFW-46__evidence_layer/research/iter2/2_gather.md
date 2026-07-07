# Gather — "What do we know and what's missing?"
> **Mindset:** Explorer. Cast wide. Collect before you filter. No judgment yet — just data.
> **Test:** "Have I found something that CHALLENGES iter1 decisions, not just confirms them?"
> Parent: [HL-TFW-46](../../HL-TFW-46__evidence_layer.md)

## Dimensions

> Decompose the problem into independent decision factors before collecting findings.

### Dim-1: Evidence Collection Placement (in handoff.md)
**Question:** Where does evidence collection sit in the executor's workflow?
**Alternatives:**
- **A1: New Step 10.5** — between Build gate (Step 10) and Pre-RF Gate (Step 11). Minimal flow disruption.
- **A2: Extension of Step 10** — evidence as additional build gate items. Conflates synthetic and real.
- **A3: New Phase 2.5** — separate "Evidence Phase" between Execution and RF. Maximum visibility.
- **A4: Part of Step 12** — evidence collection integrated into RF writing. Late, but couples evidence with documentation.

### Dim-2: Tooling Integration Level (in TFW guidance)
**Question:** How much tooling guidance should TFW provide vs leave project-specific?
**Alternatives:**
- **B1: Framework-level** — TFW specifies tool categories and provides setup guidance in handoff.md
- **B2: Project-level** — project_config.yaml lists available evidence tools, executor follows
- **B3: Task-level** — coordinator specifies tools in TS Evidence Plan per-AC
- **B4: Executor autonomy** — executor discovers and uses whatever tools are available

### Dim-3: Anti-Deception Enforcement Mechanism
**Question:** How do we structurally prevent agents from writing VERIFIED without real artifacts?
**Alternatives:**
- **C1: Convention rules only** — §14 anti-patterns, agent reads and follows
- **C2: Reviewer gate** — reviewer checks Evidence section for artifact references
- **C3: Structural enforcement** — file existence check (evidence/ folder must contain files)
- **C4: Dual enforcement** — convention rules + reviewer gate (no file existence check)

### Dim-4: Evidence Folder Convention
**Question:** Where do evidence artifacts live?
**Alternatives:**
- **D1: Task root** — `tasks/{ID}/evidence/`
- **D2: Phase subfolder** — `tasks/{ID}/phase-x/evidence/`
- **D3: No convention** — inline only, no folder
- **D4: Flexible** — convention defined but folder created only when needed (binary artifacts exist)

## Findings

### G1: Handoff Flow Analysis

Current handoff.md has 3 phases with clear cognitive transitions:

```
Phase 1: Onboarding (Steps 1-6)
  → Cognitive mode: Understanding, questioning
  → Output: ONB file

Phase 2: Execution (Steps 7-10)
  → Cognitive mode: Building, implementing
  Step 7: Update task board → 🟢 RF
  Step 8: Implement (follow TS, Execution Loops)
  Step 9: Run tests
  Step 10: Build gate — if fails, fix before RF
  → Natural boundary: code works (synthetic proof)

  [GAP ← Evidence collection goes here]

Phase 3: Write RF (Steps 11-12)
  Step 11: Pre-RF Gate — open RF template, read headings
  Step 12: Write RF with §1-§8
  → Cognitive mode: Documentation, reflection
```

**Key observation:** The gap between Step 10 (build gate) and Step 11 (Pre-RF Gate) is the natural insertion point. After synthetic verification passes, before documentation begins — this is the moment when the executor has a working system and should verify it in real conditions.

**Insertion analysis:**
- Step 10 ends with: "if build fails → fix BEFORE writing RF"
- Step 11 starts with: "open `.tfw/templates/RF.md`. Read all section headings"
- A new Step 10.5 (or renumber to Step 11, shifting Pre-RF to 12, Write RF to 13) fits naturally

**Cognitive flow:** Build → "it compiles/tests" → Evidence → "it actually works" → Document → "here's what I did". This matches the Evidence → Attestation → Proof hierarchy from iter1 D1.

### G2: Tooling Landscape (Playwright MCP + DB MCP + CLI)

**Playwright MCP Server:**
- Production-ready, integrates with Claude Code, Cursor, Windsurf, VS Code
- Key tools: `browser_navigate`, `browser_snapshot`, `browser_take_screenshot`
- Uses accessibility tree (structured, semantic) + screenshots (visual evidence)
- Supports: navigation, form interaction, tab handling, custom JS execution
- HiDPI/Retina screenshot support for high-quality visual evidence
- **Evidence capability:** Can navigate to deployed app, take screenshots, capture console output — ideal for web UI evidence

**DB MCP Servers (Postgres, ClickHouse, etc.):**
- Schema discovery → NL-to-SQL → execution → results
- Read-only enforcement by default (safe for evidence queries)
- Query logging creates audit trail
- **Evidence capability:** Can run verification queries against live DB to prove data integrity, correct transformations, expected state

**CLI Tools for Evidence:**
- `curl` / `wget` — API response capture (JSON output as evidence)
- OS screenshot utilities (platform-dependent, less reliable for agents)
- `docker logs` — container output capture
- File rendering tools: `wkhtmltoimage`, `puppeteer` CLI for PDF/HTML screenshots
- **Agent-accessible:** all via `run_command` — no special setup needed

**Industry patterns (from external research):**
- Four-Layer Verification Stack: Input → Tool&Evidence → Output → Human Escalation
- "Define Done" early (= TS Evidence Plan)
- Independent verification (= reviewer Evidence Audit)
- Trace-based observability > static screenshots
- Cryptographic receipts emerging but overkill for TFW scope

**Tooling coverage estimate:**
| Domain | Automatable | Tool | Manual |
|--------|------------|------|--------|
| Web UI | 90% | Playwright MCP (screenshots, interaction) | Complex multi-step flows |
| API/Backend | 95% | curl, DB MCP, CLI | External service dependencies |
| Database | 90% | DB MCP queries | Schema migrations requiring visual check |
| Documents (HTML/PDF) | 70% | Playwright (rendered page), CLI tools | Print layout, encoding, fonts |
| Blog/CMS | 80% | Playwright (published URL) | SEO, social previews |
| Mobile/Desktop | 10% | — | Requires physical device or emulator |
| HR/Tenders | 20% | CLI (file checks), DB queries | Published listing, portal rendering |
| Analytics | 85% | DB MCP, CLI (query output) | Dashboard visual check |

**Overall estimate: ~60-65% automatable** (weighted by task frequency in user's projects). H4's 70% threshold is optimistic. The gap is primarily in non-web domains (documents, HR, mobile) and complex multi-step verification scenarios.

### G2b: AFD Android Evidence Patterns (from project scan)

**Key finding: Android evidence ≠ screenshots. It's data-plane verification via adb + logcat.**

**Tools used (no scrcpy):**
- `adb install` / `pm install` — APK deployment verification
- `adb shell dumpsys package` — verify UID, shared user, version
- `adb shell dumpsys account` — verify account removal
- `adb shell dpm set-device-owner` — Device Owner provisioning
- `adb logcat` with tag filters — event emission proof
- `adb shell dumpsys activity` — verify LockTask mode
- `apksigner verify --print-certs` — certificate chain verification
- `/proc/uptime` reads — verify physical reboot happened

**Evidence artifacts are TEXT, not images:**
- `install_beta.txt` — adb install output verbatim
- `self_do.txt` — "Success: Device owner set to ComponentInfo{...}"
- `webview_privileged_crash.txt` — logcat crash capture
- `lifecycle_emitted.txt` — MQTT emission proof

**Two distinct evidence mediums in the same project:**
| Medium | Tool | What it proves | Example |
|--------|------|---------------|---------|
| Browser (visual) | Playwright MCP | What the user sees | 12 PNGs (dispatch-map, grafana-device, brand-dispatch) + 209 page states |
| Android (data-plane) | adb + logcat | What the system did | install logs, dumpsys output, logcat traces, certificate chains |

**Per-scenario anti-slop notes (unique to AFD):**
Every device scenario has a specific anti-false-green warning. Examples:
- US-DEV-01: "Asserting only 'dispatch returned Accepted' false-greens a login that never persisted a token"
- US-DEV-05: "The lazy trap is asserting on PaymentFsm (compiles, unit-tests pass, looks authoritative) — but it is dead on the live path"
- US-DEV-08: "Do NOT false-green by observing 'an ad was returned' — the stub returns all items unconditionally"

**Revised Mobile/Android tooling coverage:**
| Subcategory | Old estimate | Revised | Rationale |
|-------------|-------------|---------|-----------|
| Mobile app (visual) | 10% | 15% | No scrcpy/screencap used — visual is human-only |
| Mobile app (data-plane) | — | 70% | adb + logcat fully automatable by CLI agents |
| **Combined Mobile** | **10%** | **40-50%** | Most evidence is data-plane, not visual |

**Revised overall automation estimate: ~60-70%** (with Android data-plane evidence included, H4's 70% target is borderline achievable).

### G3: Evidence Plan Drafting (H2 — Coordinator Prediction Test)

**Test: Can I write a plausible Evidence Plan for 3 real tasks at TS time?**

#### AHA-6: Telegram Bot + Admin Panel (complex)
```
### AC-1: Bot responds to /start command
Gate: Run test_bot_start()
Evidence: Send /start to bot via Telegram API, capture response screenshot
Tool: Playwright MCP (Telegram Web) or curl (Telegram Bot API getUpdates)
Expected: Bot responds with welcome message + keyboard

### AC-2: Admin panel renders user list  
Gate: Run test_admin_panel()
Evidence: Navigate to admin panel URL, take screenshot of user list page
Tool: Playwright MCP (localhost:3000/admin/users)
Expected: Table with user data, correct column headers

### AC-3: Payment webhook processes correctly
Gate: Run test_webhook_handler()
Evidence: Send test webhook via curl, verify DB record via DB MCP query
Tool: curl + DB MCP
Expected: HTTP 200 + new payment record in payments table
```
**Observation:** For AHA-6, the coordinator CAN predict evidence requirements. The pattern is: for each AC, ask "what would convince a skeptical human that this actually works?" The answer maps to a tool + expected outcome.

#### HD-28: Helpdesk Backend Fixes (medium)
```
### AC-1: CORS headers correct for frontend
Gate: Run test_cors()
Evidence: curl -v to API endpoint, show response headers include Access-Control-Expose-Headers
Tool: curl (captures full header output)
Expected: expose_headers includes 'X-Custom-Header'

### AC-2: ORM lazy loading resolved
Gate: Run test_orm_queries()
Evidence: Run API request with SQL logging enabled, verify no MissingGreenlet error
Tool: curl + grep server logs
Expected: No MissingGreenlet exception in logs

### AC-3: Query performance improved
Gate: Run test_query_perf()
Evidence: DB MCP query with EXPLAIN ANALYZE, compare execution time
Tool: DB MCP
Expected: Query time < 100ms (was 2.5s before)
```
**Observation:** HD-28 evidence is almost entirely automatable (curl + DB MCP). Coordinator prediction works well for backend tasks.

#### TFW-36: Blog Post Writing (non-code)
```
### AC-1: Blog post renders correctly on site
Gate: Content review passes
Evidence: Navigate to published URL, take full-page screenshot
Tool: Playwright MCP
Expected: Page renders without broken layout, images load, code blocks formatted

### AC-2: All citations are real and verifiable
Gate: Citation list reviewed
Evidence: For each citation URL, curl HEAD request to verify URL exists (HTTP 200)
Tool: curl (batch verification)
Expected: All citation URLs return HTTP 200

### AC-3: SEO metadata correct
Gate: Meta tags present
Evidence: Playwright snapshot of page, extract meta description and title
Tool: Playwright MCP (accessibility tree extraction)
Expected: Title, description, og:image present and correct
```
**Observation:** Blog evidence mixes automatable (URL verification, rendering check) with harder-to-automate (content accuracy, fabricated citations). The fabricated citation issue in TFW-36 (FC3 from iter1) was caught by a human — no tool would have detected a plausible-but-false citation. Evidence Plan SHOULD flag this: "AC-2 Evidence: automated URL check + **DEFERRED to human for content accuracy verification**."

**H2 verdict: Coordinator CAN reliably predict evidence at TS time.** The pattern is mechanical:
1. For each AC, ask: "What would the executor show a skeptical reviewer?"
2. Identify the tool: Playwright (visual), curl (API), DB MCP (data), CLI (command output)
3. Specify expected outcome
4. Flag where evidence must be DEFERRED (human domain judgment needed)

The coordinator doesn't need domain expertise — they need the skill of converting "this should work" into "show me it works." This is a learnable pattern, not a prediction challenge.

### G4: Anti-Self-Deception Patterns

**From compliance/audit (external research):**

1. **Segregation of Duties (SoD):** The person who does the work ≠ the person who verifies. TFW already has this: Executor ≠ Reviewer. Evidence extends it: Executor collects evidence, Reviewer audits evidence.

2. **Evidence ≠ Assertion:** ISO 27001 distinguishes between a *statement* ("We have access controls") and *evidence* ("Here is the IAM configuration export"). TFW analog: RF §3 "AC met ✅" = assertion, RF §5 Evidence = evidence (actual artifacts).

3. **Operational Testing vs Policy Review:** Auditors test *actual effectiveness* of controls, not just review policy documents. TFW analog: §4 Verification = policy review (tools configured correctly), Evidence = operational testing (it actually works in real conditions).

4. **Continuous Monitoring > Annual Audit:** Don't wait for the review to check. TFW implication: Evidence should be collected AT EXECUTION TIME, not reconstructed during review.

5. **Audit Trail Immutability:** Once evidence is recorded, it shouldn't be modifiable. TFW implication: Evidence artifacts should be committed with the RF, not added later.

**Adapted anti-self-deception rules for TFW §14:**

| # | Rule | Rationale | Source |
|---|------|-----------|--------|
| R1 | Executor writes VERIFIED without evidence artifact reference = violation | Assertion without evidence = false attestation | ISO 27001 evidence requirement |
| R2 | Executor marks N/A without justification in TS Evidence Plan = violation | N/A must be planned (coordinator) or justified (executor with reason) | AFD RUNBOOK: SKIP requires reason |
| R3 | Executor writes Evidence section before actually collecting evidence = violation | Evidence collected during execution, documented after — not fabricated from memory | Analogous to existing: "writes RF before build/lint passes" |
| R4 | Reviewer approves Evidence without checking that referenced artifacts exist = violation | Reviewer must verify artifact references resolve to real files/outputs | ISO 27001: auditor checks evidence artifacts |
| R5 | DEFERRED without specific blocker reason = violation | "DEFERRED" alone is meaningless — must state why (no device, no deploy access, needs user) | AFD RUNBOOK: BLOCKED requires explanation |

### G5: RF Template Renumbering Impact Analysis

**Current RF template sections:**
```
§1. What Was Done
§2. Key Decisions
§3. Acceptance Criteria
§4. Verification  ← synthetic (lint, test, build)
§5. Observations   ← would become §6
§6. Fact Candidates ← would become §7
§7. Strategic Insights ← would become §8
§8. Diagrams ← would become §9
```

**Adding §5 Evidence (per iter1 D5) → renumbering §5-§8 to §6-§9:**

**Files requiring update (grep results):**

| File | Current reference | Update needed |
|------|------------------|---------------|
| `conventions.md` L94 | §6 Fact Candidates | §7 |
| `conventions.md` L95 | §7/§11 Strategic Insights | §8/§11 |
| `conventions.md` L86 | RF §8 Diagrams | §9 |
| `conventions.md` L406 | RF §6-8 mandatory | §7-9 |
| `glossary.md` L48 | RF §7 Strategic Insights | §8 |
| `templates/RF.md` L56 | §5 Observations, §7 Strategic Insights | §6, §8 |
| `templates/REVIEW.md` L34 | §6-8 present | §7-9 |
| `templates/review/judge.md` L13 | RF §5 Observations | §6 |
| `templates/review/judge.md` L16 | §6-8 | §7-9 |
| `templates/review/judge.md` L34 | §6-8 | §7-9 |
| `templates/review/map.md` L25 | RF §1-§5 | §1-§6 |
| `workflows/handoff.md` L94 | §5 Observations | §6 |
| `workflows/handoff.md` L95-98 | §6 FC, §7 SI, §8 Diagrams, §6-8 | §7, §8, §9, §7-9 |
| `workflows/review.md` L48 | RF §5 Observations | §6 |
| `workflows/review.md` L129 | REVIEW §6 traces | §7 (REVIEW) |
| `workflows/review.md` L135 | REVIEW §7 FC | §8 (REVIEW) |
| `workflows/knowledge.md` L42 | RF §7 Insights | §8 |
| `compilable_contract.md` L68-69 | RF §6, REVIEW §5 | RF §7, REVIEW §6 |
| `CHANGELOG.md` | Multiple historical references | Leave as-is (historical) |

**Total: ~22 active reference updates** across 10+ files (excluding CHANGELOG.md which is historical).

**REVIEW template also needs renumbering** if Evidence Audit adds to Judge:
```
Current REVIEW:
§1 Map → §2 Verify → §3 Judge → §4 Verdict → §5 Tech Debt → §6 Traces → §7 Fact Candidates

With Evidence Audit in Judge (iter1 D7): no section renumbering needed.
Evidence Audit = new check #7 in Judge table, not a new section.
```

**TS template — adding Evidence field to AC items:**
```
Current AC format:
### AC-1: {title}
{What the result should achieve}
- [ ] {Verifiable criterion}
Gate: {How to verify}

Proposed AC format (with Evidence):
### AC-1: {title}
{What the result should achieve}
- [ ] {Verifiable criterion}
Gate: {How to verify — synthetic}
Evidence: {What to verify in real environment — or N/A with reason}
```

No section renumbering needed in TS — Evidence is a field within AC items, not a new section (per iter1 D6).

### G3b: Project Scan Results (from subagent)

**Cross-task evidence pattern comparison (4 projects):**

| Dimension | AFD | AHA-6 | HD-28 | TFW-36 Blog |
|-----------|-----|-------|-------|-------------|
| Evidence maturity | ✅ Mature (evidence/, RUNBOOK) | ❌ None | 🟡 Ad-hoc (qa_evidence/ in HD-30) | 🟡 Post-hoc (Source Audit added after incidents) |
| Structural enforcement | ✅ RUNBOOK §3 (4 rules) | ❌ Trust-based | ❌ Trust-based | 🟡 After incidents only |
| Live vs synthetic distinction | ✅ Explicit (Local vs Live Beta) | ❌ Conflated (harness = "tested") | 🟡 Accidental (bugs found live) | ❌ Absent |
| Key failure mode | — (system works) | Harness pass ≠ live pass | curl pass ≠ browser pass | Citation pass ≠ fact pass |

**Domain-specific evidence gap patterns:**
- **Code/API:** curl/test passes ≠ browser/device works (HD-28: CORS + MissingGreenlet)
- **Agent/bot:** harness passes ≠ live API works (AHA-6: 10 ACs harness-only)
- **Content:** AI-generated text passes checks ≠ citations are real (TFW-36: fabricated Anthropic citation traversed 8 documents, 4 roles)
- **Device/platform:** local passes ≠ deployed works (AFD: explicit two-context)

**AFD RUNBOOK §3 anti-self-deception rules (4 rules):**
1. Assert observable outcome — evidence must show real observable result
2. Empty body ≠ PASS — no evidence = not passed
3. Known-broken ≠ PASS — if known broken, use XFAIL, not PASS
4. Can't verify = BLOCKED — never assume PASS

### G4b: Compliance Evidence Hierarchy (from subagent)

**Audit evidence hierarchy (weakest → strongest):**
```
Inquiry → Observation → Examination → Re-performance → CAATs
(asking)   (watching)    (reviewing)    (auditor does it)  (automated)
```

**Key distinction:** "Design Effectiveness" (control designed correctly on paper) vs "Operating Effectiveness" (control actually worked in practice). TFW's §4 Verification = Design Effectiveness, proposed §5 Evidence = Operating Effectiveness.

**Three evidence criteria:** Sufficiency × Appropriateness × Objectivity.

**Industry convergence finding:** Nobody has formalized evidence-based verification into a methodology framework yet. TFW is positioned to fill this gap. Key industry gaps:
- No standard format for "evidence receipts" (TFW's RF could be this)
- No standard for "sufficient proof" (TFW could define evidence levels)
- Visual verification always optional, never required
- Separation of performer and verifier matches TFW's Executor/Reviewer split

---

## OODA Loop Summary

**Loop 1:** Handoff flow + renumbering analysis → confirms natural insertion point (Step 10.5), quantifies renumbering scope (~22 references).

**Loop 2:** External research (Playwright MCP, compliance, industry patterns) → rich tooling landscape mapped, anti-self-deception rules drafted, four-layer verification stack discovered.

**Loop 3:** Evidence Plan drafting for 3 real tasks → H2 confirmed (coordinator CAN predict), 60-65% tooling coverage estimated (H4 70% is optimistic).

## Checkpoint

### Sufficiency Verdict
- [x] External source used? — Yes: Playwright MCP docs, ISO 27001/SOX compliance patterns, AI agent verification practices, DB MCP patterns
- [x] Briefing gap closed? — All 5 investigation lines covered (G1-G5)
- [x] Hypothesis tested? — H2 (coordinator prediction ✅ confirmed), H4 (tooling coverage 🟡 partially — 60-65%, not 70%)
- [x] Counter-evidence sought? — H4 counter-evidence found (non-web domains pull coverage below 70%), TFW-36 citation issue shows limits of automated evidence

### Metacognitive Check
I discovered genuinely new things:
- The four-layer verification stack maps cleanly to TFW roles (coordinator=input, executor=tool&evidence, reviewer=output, user=human escalation)
- The ~22 file update scope for renumbering is concrete and bounded — not a blocker
- Evidence Plan drafting for 3 tasks proved the pattern is mechanical, not predictive
- 60-65% automation estimate is lower than H4's 70% — the gap is in non-web domains
- Anti-self-deception rules from compliance map directly to TFW's existing structure

---
Stage complete: YES
