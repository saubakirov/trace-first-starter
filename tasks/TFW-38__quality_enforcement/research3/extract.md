# Extract — Iteration 3
> Parent: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> Goal: (A) TS over-spec problem vs feature analysis, (B) Final naming decisions.

## Thread A: Is TS Over-Specification a Problem or a Feature?

### E1: Arguments FOR Over-Specification (it's a feature)

1. **Deterministic output.** If TS contains exact code, the executor produces exactly what the coordinator intended. No ambiguity, no creative divergence. This is the "Completeness Over Speed" value.
2. **Reduced executor errors.** The SLA Engine in HD PhaseD is algorithmically complex (calendar-aware timer). Writing it in TS avoids the executor inventing a wrong algorithm.
3. **Onboarding clarity.** A new executor in a new session reads TS and immediately understands the full implementation plan. No guessing.
4. **Matches TFW philosophy.** "Traces Over Code" — the TS with full code IS the trace. The code in the file is context, not just output.

### E2: Arguments AGAINST Over-Specification (it's a problem)

1. **Token waste.** Coordinator spends ~10K tokens writing code that the executor will copy-paste. Then executor spends tokens reading it. Double spend.
2. **False sense of quality.** The coordinator writes code without running it. No tests, no runtime verification. The executor copies untested code and may not question it. HD PhaseD Step 5 L715-724 has a `__import__("datetime")` hack that suggests the coordinator was writing fast without testing.
3. **Executor degradation.** When TS is full implementation, the executor becomes a typist, not an engineer. The executor's value (runtime debugging, edge case handling, adaptive decisions) is suppressed.
4. **Template says "if relevant."** The TS template says "code examples IF relevant" — not "write the complete file." The coordinator is exceeding the template's intent.
5. **ONB becomes redundant.** If TS has full code, the executor ONB step ("do I understand the task?") becomes trivial — there's nothing to analyze, just copy.

### E3: The Spectrum

TS content exists on a spectrum:

```
REQUIREMENT ←──────────────────────────────── IMPLEMENTATION
"compute SLA     "SLA = calendar-aware     "class SLAEngine:
 deadline"        timer, input: created_at   def __init__(self, db):
                  + priority + tenant,         self.db = db
                  output: target_at          async def calculate..."
                  constraints: working
                  hours only, skip holidays"
```

| Level | Description | Example | Tokens | Executor Value |
|-------|-------------|---------|--------|----------------|
| L1: Goal | WHAT to achieve | "SLA deadline calculator" | Low | High (designs solution) |
| L2: Requirement | WHAT + constraints + AC | "calendar-aware, skip holidays, working hours only" | Medium | Medium (implements from requirements) |
| L3: Design | Requirements + architecture + signatures | "SLAEngine class with calculate_target_at(created_at, priority, tenant_id) → datetime" | Medium-High | Medium (fills in logic) |
| L4: Implementation | Design + full code | Complete Python with all edge cases | High | Low (copies and adjusts) |

**Current state:** Most TS files are at L4. The template implies L2-L3. The user suspects L4 is wasteful.

### E4: Verdict on Over-Specification

**Problem is NOT that full code exists — it's that ALL steps are at L4.**

Some steps genuinely need L4 (SLA algorithm = must be exact, wrong implementation = broken product). Others don't (CRUD repository = standard pattern, executor knows how to write it).

**Recommendation:** TS should use mixed levels:
- **L4 (full code)** for: algorithms, security-critical logic, API contracts, prompt engineering
- **L3 (design + signatures)** for: standard patterns (CRUD, service layer, routing)
- **L2 (requirements + constraints)** for: tests, CSS, boilerplate

This is NOT a TFW-38 scope change. It's a finding to record as a fact candidate and potentially a separate task (TS template conventions). Adding a note to HL recommendations.

## Thread B: Final Naming

### E5: Review Stage Names — Final Decision

Applying the "Naming Creates Behavior" filter: can someone understand the stage WITHOUT reading a description?

**Proposed: Map → Verify → Judge → Decide**

| Stage | Name | Syllables | Instant Meaning | Parallel |
|-------|------|-----------|-----------------|----------|
| 1 | **Map** | 1 | "Build mental map of what was done" | Navigator mapping territory |
| 2 | **Verify** | 3 | "Check if the claims are true" | Engineering audit |
| 3 | **Judge** | 1 | "Evaluate quality, apply standards" | Legal — ruling on evidence |
| 4 | **Decide** | 2 | "Make the call — approve, revise, reject" | Management — the decision |

**Cross-check against research stage names:**

| Research | Review |
|----------|--------|
| Briefing (plan) | Map (understand) |
| Gather (collect data) | Verify (check evidence) |
| Extract (find patterns) | Judge (apply standards) |
| Challenge (test) | — (no challenge in review) |
| RES (synthesize) | Decide (verdict + capture) |

**Structural parallel works.** Both flows use active verbs. Research is investigative (gather → extract → challenge). Review is evaluative (map → verify → judge → decide).

### E6: Review Mode Names — Final Decision

User rejected "prose." Need modes that describe output type in TFW's naming style.

**Filter:** Must be (1) 1-2 syllables, (2) instantly clear, (3) TFW-compatible, (4) domain-agnostic.

| Mode | For | Why This Name | Alternative Rejected | Why Rejected |
|------|-----|---------------|---------------------|--------------|
| **code** | Implementation tasks | Universal, obvious | "build", "dev" | "build" collides with CI, "dev" too informal |
| **docs** | Writing/documentation/design tasks | Short, clear, known | "prose", "write", "text", "content" | "prose" unclear to user, "write" is a verb (modes should be nouns), "text" too generic, "content" vague |
| **spec** | Analytical specs, research output, positioning | Short, precise, expected | "analysis", "research", "study" | "analysis" long, "research" collides with RES, "study" academic |

**code / docs / spec** — all nouns, all 1 syllable, all instantly clear what's being reviewed.

### E7: REVIEW Template Section Names

Mapping new stage names to REVIEW artifact sections:

| Section | Old (iter 2) | New |
|---------|-------------|-----|
| §1 | Comprehend | **Map** — "Summary of what was reviewed" |
| §2 | Verify | **Verify** — "Evidence table" |
| §3 | Assess (Checklist) | **Judge** — "Checklist" (mode-aware) |
| §4 | Verdict | **Decide** — "Verdict + Rationale" |
| §5 | Tech Debt | Tech Debt (unchanged) |
| §6 | Traces | Traces (unchanged) |
| §7 | Fact Candidates | Fact Candidates (unchanged) |

### E8: Full Naming Inventory

**Everything that gets a name in the review restructure:**

| Entity | Current (iter 2 proposal) | Final Proposal |
|--------|--------------------------|----------------|
| **Stage 1** | Comprehend | **Map** |
| **Stage 2** | Verify | **Verify** |
| **Stage 3** | Assess | **Judge** |
| **Stage 4** | Synthesize | **Decide** |
| **Mode A** | code | **code** |
| **Mode B** | prose | **docs** |
| **Mode C** | spec | **spec** |
| **Workflow path** | `.tfw/workflows/review.md` | unchanged |
| **Mode files path** | `.tfw/workflows/review/code.md` | `.tfw/workflows/review/code.md` |
| | `.tfw/workflows/review/prose.md` | `.tfw/workflows/review/docs.md` |
| | `.tfw/workflows/review/spec.md` | `.tfw/workflows/review/spec.md` |
| **Template** | `.tfw/templates/REVIEW.md` | unchanged path, restructured sections |
| **REVIEW §1** | Comprehend | **Map** |
| **REVIEW §2** | Verify | **Verify** |
| **REVIEW §3** | Assess | **Judge** |
| **REVIEW §4** | Verdict | **Decide** |
| **REVIEW §5-7** | Tech Debt, Traces, Fact Candidates | unchanged |
| **Config key** | `tfw.review.default_mode` | `tfw.review.default_mode` |
| **Checklist item #10** | RF completeness | **RF completeness (§6-8)** |
| **Verify action label** | "spot-check" | "spot-check 2-3 files" |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| TS is 49-71% code — problem is ALL steps at L4, not code presence itself (E3-E4) | Captured as finding, out of TFW-38 scope |
| Final stages: Map → Verify → Judge → Decide (E5) | Needs challenge validation |
| Final modes: code / docs / spec (E6) | Needs challenge validation |
| Full naming inventory documented (E8) | None |

**Sufficiency:**
- [x] External source used? (TFW values applied as naming filter)
- [x] Briefing gap closed? (Both threads analyzed)

Stage complete: YES
→ User decision: ___
