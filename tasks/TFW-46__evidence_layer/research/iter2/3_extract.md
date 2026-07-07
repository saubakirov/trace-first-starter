# Extract — "What patterns emerge when we cross-reference?"
> **Mindset:** Analyst. Connect dots between Gather findings. Build the Configuration Space — make combinations visible.
> **Test:** "Did the cross-reference reveal a combination I wouldn't have seen by looking at each dimension alone?"
> Parent: [HL-TFW-46](../../HL-TFW-46__evidence_layer.md)

## Configuration Space

Cross-reference of 4 Gather dimensions (Dim-1 through Dim-4):

### Dim-1 × Dim-3: Placement × Enforcement

| | C1: Convention only | C2: Reviewer gate | C3: Structural (files) | C4: Convention + reviewer |
|---|---|---|---|---|
| **A1: Step 10.5** | Weak: agent might skip step | Step done but reviewer catches omissions later | Evidence collected, files checked at review | ✅ Step + reviewer = dual enforcement |
| **A2: Step 10 extension** | Very weak: conflated with synthetic | Reviewer can't distinguish synthetic from real | File check meaningless (synthetic files exist) | ❌ Conflation defeats enforcement |
| **A3: Phase 2.5** | Overhead: new phase for every task | Phase exists but reviewer still needed | Too formal for proportional scope | ⚠️ Works for large tasks, overkill for small |
| **A4: Part of Step 12** | Evidence fabricated during documentation | Late: reviewer catches but work is done | Files created during RF writing, not during execution | ❌ Evidence at documentation time = reconstructed, not collected |

**Surviving combinations:**
- ✅ **A1+C4** (Step 10.5 with convention + reviewer gate) — minimal friction, dual enforcement
- ⚠️ **A3+C4** (Phase 2.5 with convention + reviewer gate) — viable for large tasks but proportionality problem

**Eliminated:**
- A2: conflates synthetic/real (violates D5 from iter1)
- A4: evidence at documentation time = reconstructed, not contemporaneous (violates compliance principle)
- C1 alone: insufficient for AI agents (they optimize for speed)
- C3: structural file existence is too rigid for text-only evidence (inline curl output, query results)

### Dim-2 × Dim-1: Tooling Level × Placement

| | A1: Step 10.5 | A3: Phase 2.5 |
|---|---|---|
| **B1: Framework-level** | TFW lists tool categories in handoff.md. Agent reads at Step 10.5 | TFW lists in separate Evidence Phase doc. Overkill |
| **B2: Project-level** | project_config.yaml lists tools. Agent reads at context loading | project_config.yaml list. Works but separate phase for config? |
| **B3: Task-level** | Coordinator writes per-AC tools in TS. Executor follows at Step 10.5 | Same but in separate phase. Over-structured |
| **B4: Executor autonomy** | Executor discovers tools at Step 10.5. Proactive but unpredictable | Executor discovers. Phase gives time but no guidance |

**Analysis:** B3 (task-level) is already solved by D6 (Evidence field in AC items). B1 (framework-level) adds general guidance. B4 (executor autonomy) is the proactive tooling principle from HL §7.6. These are NOT mutually exclusive:

**Combined model:** B1 (framework guidance in handoff.md about tool categories) + B3 (coordinator specifies per-AC in TS) + B4 (executor proactively seeks if coordinator didn't specify). This is a **cascade**, not a choice:
1. Framework says "evidence often needs browser, CLI, DB tools"
2. Coordinator writes specific tool per AC in Evidence Plan
3. Executor follows coordinator's specification, OR discovers/configures tools if coordinator left Evidence field open

### Dim-4 × Dim-3: Folder Convention × Enforcement

| | C2: Reviewer gate | C4: Convention + reviewer |
|---|---|---|
| **D1: Task root evidence/** | Reviewer checks `evidence/` for files. Simple but misleading when no binary evidence needed | Convention says "create if binary artifacts." Reviewer checks Evidence table references |
| **D2: Phase subfolder evidence/** | Same as D1 but phase-scoped. Better for multi-phase | Same, phase-scoped |
| **D3: No convention** | Reviewer has nowhere to look for artifacts | No structural place for artifacts = relies entirely on inline RF text |
| **D4: Flexible (create when needed)** | Reviewer knows convention: if Evidence table references files → check evidence/ | Convention: "Evidence folder created when binary artifacts exist. Not required for text-only evidence" |

**Surviving combination:** D4+C4 (flexible folder + convention + reviewer gate). Matches D4 from iter1 (mixed storage: optional folder + inline).

## Key Extractions

### E1: Evidence Collection Step Design

Based on A1+C4 surviving configuration:

**New Step 11** (current Steps 11-12 become 12-13):

```markdown
## Step 11: Evidence Collection

> After synthetic verification passes (Step 10), verify your work in real conditions.
> Evidence = observable outcomes in live environments. NOT re-running tests.

For each AC with an `Evidence:` field in TS:
1. **Set up environment** — deploy, open browser, connect to real service
2. **Collect evidence** — run the verification specified in TS Evidence field
3. **Record result** — VERIFIED (with artifact reference) / DEFERRED (with reason) / BLOCKED (with blocker) / N/A (justified in TS)
4. **Save artifacts** — screenshots → `evidence/`, text output → inline in RF §5 Evidence table

If TS Evidence field is empty for an AC: executor decides whether evidence adds value.
If no ACs have Evidence fields: skip this step (proportional scope from D3).

> **Proactive tooling:** If tools are needed but not available, seek, configure, or create them.
> Check: MCP servers (browser, DB), CLI utilities, API endpoints.
> Don't skip evidence because tools aren't pre-configured.
```

**Cognitive flow preserved:**
```
Phase 2 (Execution):
  Step 7-8: Implement
  Step 9: Tests
  Step 10: Build gate
  → "Code works (synthetic proof)"
  
  Step 11: Evidence Collection  ← NEW
  → "It actually works (real proof)"

Phase 3 (Write RF):
  Step 12: Pre-RF Gate (was Step 11)
  Step 13: Write RF (was Step 12)
  → "Here's what I did"
```

### E2: Evidence Field in TS AC Items

Based on D6 from iter1, made concrete:

```markdown
### AC-1: {title}
{What the result should achieve — 1-2 sentences.}
- [ ] {Verifiable criterion}
- [ ] {Verifiable criterion}
Gate: {How to verify — synthetic (test command, lint, build)}
Evidence: {What to verify in real environment — or N/A with reason}
```

**Evidence field grammar:**
- `Evidence: Navigate to {URL}, verify {what}. Tool: {tool}. Expected: {outcome}` — full spec
- `Evidence: {action}. Expected: {outcome}` — minimal spec (tool left to executor)
- `Evidence: N/A — {reason}` — not applicable with justification
- `Evidence: DEFERRED — {reason}` — cannot be collected at TS time (needs runtime context)
- Empty field: executor decides (proportional scope)

### E3: RF §5 Evidence Table

Based on D5 (separate section) and the example from HL §3.1:

```markdown
## 5. Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | {description} | {where} | VERIFIED / DEFERRED / BLOCKED / N/A | {path or inline} |
| E2 | AC-2 | {description} | {where} | VERIFIED | evidence/screenshot.png |
| E3 | AC-3 | {description} | {where} | DEFERRED (reason) | — |

Evidence verdict: {N}/{M} VERIFIED, {X} DEFERRED, {Y} BLOCKED, {Z} N/A
```

**Section placement rationale:**
```
§4 Verification  ← synthetic (tools: lint, test, build)
§5 Evidence       ← real (environments: browser, deployed, live service)
§6 Observations   ← was §5
§7 Fact Candidates ← was §6
§8 Strategic Insights ← was §7
§9 Diagrams ← was §8
```

### E4: REVIEW Evidence Audit Integration

Based on D7 from iter1 (extends Verify and Judge, not new section):

**In verify.md** — add evidence artifact checks:
```markdown
### Evidence Verification
| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | evidence/login.png | ✅ | ✅ — shows login form |
| E2 | (inline curl output) | ✅ (in RF text) | ✅ — headers correct |
```

**In judge.md** — add check #7:
```markdown
| 7 | Evidence completeness | ✅/❌ | {All AC items with Evidence field in TS covered in RF §5?} |
```

**In REVIEW template** — §2 Verify table gets evidence verification rows, §3 Judge gets check #7.

### E5: Tooling Cascade Model

Three-level guidance, not a single point:

| Level | Who | What | Where |
|-------|-----|------|-------|
| Framework | TFW | "Evidence often needs browser automation, DB queries, CLI tools. Seek and configure proactively" | handoff.md Step 11, general guidance |
| Task | Coordinator | "AC-1 Evidence: Playwright MCP screenshot of deployed page" | TS §5 AC Evidence field |
| Execution | Executor | Discovers, installs, configures tools not pre-specified | handoff.md Step 11, proactive tooling note |

### E6: Anti-Self-Deception Rules (conventions.md §14)

Adapted from G4 + a project runbook + compliance patterns:

1. **Executor writes VERIFIED in Evidence table without artifact reference** — must reference file path or inline output. "I verified it" is not evidence (analogous to "assert observable outcome" from a mobile testing project)
2. **Executor marks Evidence N/A without justification** — N/A must be either (a) planned by coordinator in TS Evidence field or (b) justified by executor with specific reason
3. **Executor writes Evidence section before collecting evidence** — evidence is recorded from execution, not fabricated from memory (analogous to "writes RF before build/lint passes" existing anti-pattern)
4. **Reviewer approves without checking evidence artifact references** — reviewer must verify that referenced artifacts exist and match claims (extends existing: "approves without opening any files")
5. **DEFERRED without specific blocker** — must state what's missing (no device, no deploy access, needs user approval). "DEFERRED" alone is meaningless

### E7: Renumbering Migration Path

**Scope:** ~22 active references across 10+ `.tfw/` files (CHANGELOG.md excluded — historical).

**Not a blocker.** This is a mechanical one-time operation:
1. RF template: add §5 Evidence, renumber §5-§8 → §6-§9
2. All files referencing RF §5-§8: update numbers
3. REVIEW template: add check #7 in Judge, adjust §5-§7 references
4. Handoff.md: renumber §5-§8 references in Phase 3
5. All `§6-8` shorthand references → `§7-9`

Can be done in a single TS phase with a grep-and-update checklist.

---

## Checkpoint

### Sufficiency Verdict
- [x] External source used? — Cross-referenced with compliance evidence hierarchy, industry verification patterns
- [x] Briefing gap closed? — All 4 dimensions crossed, 5 surviving configurations identified
- [x] Hypothesis tested? — H1 (domain-agnostic ✅ — 4 domain evidence plans work with fixed vocabulary), H2 (coordinator prediction ✅ — mechanical pattern confirmed)
- [x] Counter-evidence sought? — Challenged A3 (Phase 2.5 — too formal), C3 (structural file check — too rigid for text evidence)

### Metacognitive Check
Genuinely new insight: The tooling integration is NOT a single-level choice but a **three-level cascade** (framework → coordinator → executor). This wasn't visible from looking at Dim-2 alone — it emerged from crossing Dim-2 with Dim-1 (placement). The cascade model means tooling guidance doesn't need to be prescriptive at any one level.

Also new: The A4 (evidence during RF writing) elimination is important. Evidence MUST be collected during execution, not reconstructed during documentation. This is the compliance principle of "contemporaneous documentation" — and it's a strong argument against merging evidence into the RF writing step.

---
Stage complete: YES
