# RES — TFW-46 Evidence Layer / Iteration 2

> **Date**: 2026-07-07
> **Mode**: deep (user-specified)
> **Focus**: Internal synthesis — apply iter1 findings to concrete TFW integration design
> **Parent**: [HL-TFW-46](../../HL-TFW-46__evidence_layer.md)
> **Predecessor**: [iter1/RES.md](../iter1/RES.md)

---

## Iteration Summary

Iteration 2 investigated 5 areas: handoff workflow integration (G1), tooling landscape with Playwright MCP + DB MCP + adb/logcat (G2/G2b), coordinator Evidence Plan prediction for 3 tasks (G3), anti-self-deception rules from compliance + AFD RUNBOOK (G4), and RF renumbering impact (~22 references across 10+ files, G5). External sources: ISO 27001/SOX compliance patterns, industry AI agent verification practices, Playwright MCP API, DB MCP capabilities, AFD project testing infrastructure.

## Decisions

### D9: Evidence Collection Step = new Step 11 in handoff.md

**Placement:** Between current Step 10 (build gate) and Step 11 (Pre-RF Gate). Current Steps 11-12 renumber to 12-13.

**Rationale:** Natural cognitive transition — "code compiles/tests pass" → "it actually works in real conditions" → "document what happened." A1+C4 survived all 6 stress-test scenarios (C1). The proportional scope mechanism (empty Evidence fields → skip step) prevents bureaucratic overhead for trivial tasks.

**Eliminated alternatives:**
- A2 (extend Step 10): conflates synthetic and real — violates D5
- A3 (Phase 2.5): too formal for proportional scope
- A4 (part of RF writing): evidence at documentation time = reconstructed, not contemporaneous — violates compliance principle

**Source:** Gather G1 (handoff flow analysis), Challenge C1 (6-scenario stress test)

### D10: Evidence field in TS AC items — guidance, not mandate

**Format:**
```markdown
### AC-1: {title}
- [ ] {Verifiable criterion}
Gate: {synthetic verification}
Evidence: {real-environment verification — or N/A with reason}
```

**Key design decision:** Evidence field uses the same "MAY deviate" principle as Technical Guidance §6. Coordinator specifies what to verify and suggests tools; executor MAY adapt with justification in RF. This prevents over-constraining.

**Evidence field grammar:**
- Full spec: `Evidence: Navigate to {URL}, verify {what}. Tool: {tool}. Expected: {outcome}`
- Minimal spec: `Evidence: {action}. Expected: {outcome}` (tool left to executor)
- Not applicable: `Evidence: N/A — {reason}`
- Runtime-dependent: `Evidence: DEFERRED — {reason}`
- Empty: executor decides (proportional scope)

**Source:** Gather G3 (3-task Evidence Plan test), Challenge C2 (coordinator prediction failures)

### D11: RF §5 Evidence table with 4-status vocabulary

**Format:**
```markdown
## 5. Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | {description} | {where} | VERIFIED | evidence/screenshot.png |
| E2 | AC-2 | {description} | {where} | VERIFIED | (inline curl output above) |
| E3 | AC-3 | {description} | {where} | DEFERRED (reason) | — |

Evidence verdict: {N}/{M} VERIFIED, {X} DEFERRED, {Y} BLOCKED, {Z} N/A
```

**Renumbering:** §5-§8 → §6-§9. ~22 active reference updates across 10+ `.tfw/` files. CHANGELOG.md excluded (historical). One-time mechanical operation — done before in TFW-25 (§5→§4) and TFW-41 (§4→§5).

**Source:** Iter1 D5 (separate section), Gather G5 (renumbering impact analysis)

### D12: Evidence Audit = Judge check #7 + verify.md evidence section

**In REVIEW judge.md — new check #7:**
```
| 7 | Evidence completeness | ✅/❌ | {All TS Evidence fields covered in RF §5?} |
```

**In verify.md — new Evidence Verification section:**
```markdown
### Evidence Verification
| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | evidence/login.png | ✅ | ✅ — shows login form |
```

No new REVIEW sections needed. Evidence Audit extends existing stages (D7 from iter1).

**Source:** Iter1 D7, Extract E4

### D13: Three-level tooling cascade (framework → coordinator → executor)

| Level | Who | What | Where |
|-------|-----|------|-------|
| Framework | TFW | General guidance: "evidence often needs browser, CLI, DB tools" + proactive tooling principle | handoff.md Step 11 |
| Task | Coordinator | Per-AC evidence specification in TS Evidence field | TS §5 AC items |
| Execution | Executor | Discovers, installs, configures tools if coordinator didn't specify | handoff.md Step 11, proactive tooling note |

**Not a single-level choice.** The cascade means TFW doesn't need to be prescriptive about specific tools — each level fills the gap left by the one above.

**Source:** Extract E5 (emerged from Dim-2 × Dim-1 cross)

### D14: Two evidence mediums — visual and data-plane

**From AFD project scan:** Evidence is not always screenshots. Two distinct mediums exist:

| Medium | Tool | What it proves | Artifact type |
|--------|------|---------------|--------------|
| Visual | Playwright MCP, browser | What the user sees (UI state) | PNG screenshots, page state files |
| Data-plane | adb, logcat, curl, DB MCP, CLI | What the system did (internal state) | Text files (command output, query results, logs) |

**TFW design implication:** The Evidence table Artifact column accepts both file paths (PNG) and inline text (curl output, query results). The `evidence/` folder is for binary artifacts; text evidence goes inline in RF §5.

**Source:** Gather G2b (AFD project scan — 209 Playwright states + adb text evidence in same project)

### D15: Five anti-self-deception rules for conventions.md §14

| # | Rule | Rationale |
|---|------|-----------|
| R1 | VERIFIED without artifact reference = violation | Assertion without evidence = false attestation (ISO 27001) |
| R2 | N/A without justification = violation | Must be planned by coordinator or justified by executor |
| R3 | Evidence section written before evidence collected = violation | Contemporaneous documentation principle (compliance) |
| R4 | Reviewer approves without checking artifact references = violation | Extends existing "approves without opening files" |
| R5 | DEFERRED without specific blocker = violation | Must state what's missing and why |

**Adapted from:** AFD RUNBOOK §3 ("assert observable outcome", "empty body ≠ PASS", "can't verify = BLOCKED"), ISO 27001 evidence requirements, SOX segregation of duties.

**Per-scenario anti-slop notes from AFD (US-DEV-01 through US-DEV-08) are NOT adopted by TFW** — they are project-specific, not framework-level. TFW provides the structural rules; projects add domain-specific traps.

**Source:** Gather G4 + G4b (compliance + AFD RUNBOOK), Extract E6

### D16: Evidence folder convention — flexible, create when needed

**Convention:** `evidence/` subfolder created in task directory (or phase directory for multi-phase) ONLY when binary evidence artifacts exist (screenshots, recordings, exported files). Text evidence (curl output, query results, adb command output) goes inline in RF §5 Evidence table.

**Path:** `tasks/{ID}/evidence/` (single-phase) or `tasks/{ID}/phase-x/evidence/` (multi-phase).

**Source:** Iter1 D4 (mixed storage), Extract Dim-4 × Dim-3 analysis (D4+C4 survived)

## Hypothesis Status

| # | Hypothesis | Iter1 Status | Iter2 Status | Verdict |
|---|-----------|-------------|-------------|---------|
| H1 | Evidence can be domain-agnostic | 🟡 partially | ✅ confirmed | Domain-agnostic structure (table + 4-status), domain-specific medium (visual vs data-plane). Tested across 8 domains in C5 |
| H2 | Coordinator can predict evidence at TS time | 🟡 partially | ✅ confirmed (qualified) | Mechanical pattern: "what would convince a skeptical reviewer?" Evidence field = guidance, executor MAY adapt (D10) |
| H4 | MCP + browser + CLI can cover 70%+ | ⏳ deferred | 🟡 borderline (60-70%) | 70% achievable with domain decomposition (visual + data-plane). Depends on project tooling, not framework |
| H5 | Merging §4 + Evidence is better | ❌ refuted | ❌ confirmed refuted | Separate cognitive modes: synthetic (§4) vs real (§5). D5 from iter1 holds |

## Open Threads

| # | Thread | Status | Action |
|---|--------|--------|--------|
| 1 | H2 coordinator prediction | ✅ Closed | Confirmed. Pattern is mechanical, not predictive. Evidence field = guidance with "MAY deviate" |
| 2 | H4 tooling coverage | 🟡 Narrowed | 60-70% with domain decomposition. Remaining gap is structural: DEFERRED/BLOCKED handles it |
| 3 | Anti-self-deception rules | ✅ Closed | 5 rules drafted (D15), adapted from compliance + AFD RUNBOOK |
| 4 | Evidence folder convention | ✅ Closed | Flexible: create when binary artifacts exist (D16) |
| 5 | Handoff integration point | ✅ Closed | New Step 11 between build gate and Pre-RF Gate (D9) |
| 6 | Evidence medium distinction | ✅ NEW → Closed | Visual (Playwright) vs data-plane (adb/curl/DB) — both handled by same table (D14) |
| 7 | TS Evidence field semantics | ✅ NEW → Closed | Guidance, not mandate. "MAY deviate" principle (D10) |

## Findings Map

```
HL Vision: "RF says done" → "actually works"
  │
  ├── Iter1: WHAT the Evidence Layer is
  │   ├── D1: "Evidence" terminology ✅
  │   ├── D2: 4-status vocabulary (VERIFIED/DEFERRED/BLOCKED/N/A) ✅
  │   ├── D3: Proportional scope ✅
  │   ├── D4: Mixed storage (folder + inline) ✅
  │   ├── D5: Separate §5 (not merged with §4) ✅
  │   ├── D6: Evidence field in TS AC items ✅
  │   ├── D7: Evidence Audit in REVIEW ✅
  │   └── D8: Per-template naming ✅
  │
  └── Iter2: HOW the Evidence Layer integrates
      ├── D9:  Step 11 in handoff (placement) ✅
      ├── D10: Evidence field = guidance, MAY deviate ✅
      ├── D11: RF §5 table format + renumbering ✅
      ├── D12: Judge check #7 + verify.md section ✅
      ├── D13: Three-level tooling cascade ✅
      ├── D14: Two evidence mediums (visual + data-plane) ✅
      ├── D15: 5 anti-self-deception rules for §14 ✅
      └── D16: Flexible evidence folder convention ✅
```

## Iteration Status

**Recommendation: SUFFICIENT — ready for TS.**

All 5 open threads from iter1 are closed. Two new threads (D14, D10) emerged and were resolved within iter2. The design is concrete enough for TS:

- **Templates** are specified: TS AC Evidence field, RF §5 Evidence table, verify.md Evidence section, judge.md check #7
- **Workflow integration** is mapped: handoff.md Step 11, renumbering scope quantified (~22 references)
- **Anti-self-deception rules** are drafted: 5 rules for conventions.md §14
- **Tooling** is characterized: three-level cascade, two evidence mediums
- **Renumbering** is bounded: one-time mechanical operation, precedent in TFW-25 and TFW-41

No remaining hypothesis requires external research. H4 (tooling coverage) is narrowed to "project-dependent, 60-70% with domain decomposition" — this is a characterization, not a gap.

## Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | process | AFD uses TWO evidence mediums: Playwright screenshots (visual, 209 files) and adb text output (data-plane) — same anti-self-deception contract applies to both | AFD project scan, G2b | High |
| FC2 | process | AFD per-scenario anti-slop notes name SPECIFIC false-green traps (e.g., "asserting on PaymentFsm is dead on the live path") — this is project-level, not framework-level | AFD device.md scenarios | High |
| FC3 | philosophy | Compliance distinction between "Design Effectiveness" (control designed correctly) and "Operating Effectiveness" (control actually worked) maps to TFW's §4 Verification vs §5 Evidence | ISO 27001/SOX compliance research | Medium |
| FC4 | process | Industry has converged on evidence-based verification for AI agents but no framework has formalized it — TFW is positioned to fill this gap | External research, G4b | Medium |
| FC5 | constraint | Android evidence is TEXT-based (adb command output, logcat traces), not visual — scrcpy/screencap NOT used in AFD | AFD project scan, D14 | High |

> fact-candidates: processed 2026-07-07

## Strategic Insights (Research)

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | The "Evidence field = guidance, MAY deviate" principle (D10) mirrors Technical Guidance §6 — this creates a consistent pattern: TS specifies intent, executor adapts with justification. This is a deep architectural symmetry worth preserving. | philosophy | Cross-reference of TS §5 AC format with §6 Technical Guidance |
| S2 | AFD's per-scenario anti-slop notes are the strongest anti-self-deception mechanism found, but they're inherently project-specific. TFW should provide the structural rules (D15); projects add domain-specific traps. This is the right separation of concerns. | process | AFD project scan, user direction |

---

*RES — TFW-46 / Iteration 2 | 2026-07-07*
