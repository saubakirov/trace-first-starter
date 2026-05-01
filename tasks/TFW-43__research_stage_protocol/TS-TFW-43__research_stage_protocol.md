# TS — TFW-43: Research Stage Protocol

> **Date**: 2026-05-01
> **Author**: Coordinator (Antigravity)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-43](HL-TFW-43__research_stage_protocol.md)
> **Research**: [RES iter1](research/iter1/RES.md) — all hypotheses resolved

---

## 1. Summary

Add Mindset blocks (Strategist/Explorer/Analyst/Critic) to 4 research templates, add Briefing h1 guiding question, restructure `base.md` to copy-on-enter with 🛑 STOP after each stage checkpoint.

## 2. Scope

### Affected Files

| # | File | Action | Changes |
|---|------|--------|---------|
| 1 | `.tfw/templates/research/1_briefing.md` | modify | Add h1 guiding question + Mindset + Test blockquote |
| 2 | `.tfw/templates/research/2_gather.md` | modify | Add Mindset + Test blockquote |
| 3 | `.tfw/templates/research/3_extract.md` | modify | Add Mindset + Test blockquote |
| 4 | `.tfw/templates/research/4_challenge.md` | modify | Add Mindset + Test blockquote |
| 5 | `.tfw/workflows/research/base.md` | modify | Step 3: remove template copy. Step 4: add copy. Step 5: per-stage protocol with STOP |
| 6 | `.agent/workflows/tfw-research.md` | modify | Sync copy of base.md |
| 7 | `.claude/commands/tfw-research.md` | modify | Sync copy of base.md |
| 8 | `.tfw/VERSION` | modify | `0.8.6` → `0.8.7` |
| 9 | `.tfw/project_config.yaml` | modify | version bump |
| 10 | `.tfw/CHANGELOG.md` | modify | Add `[0.8.7]` entry |

**Budget:** 10 files / 0 new / ~50 LOC. Override justified: 4 templates = identical 2-line additions, 2 adapters = byte-copies, 2 version files = 1-line changes.

## 3. Principles Check

| HL §7 Principle | How TS enforces |
|-----------------|-----------------|
| P1: Copy-on-enter | AC-2 (no copy in Step 3), AC-3 (copy in Step 4), AC-4 (copy per stage in Step 5) |
| P2: Mindset-first | AC-1 (exact wording from RES D1-D7) |
| P3: STOP between stages | AC-5 |
| P4: Template = instruction + container | AC-1 three-layer verification: h1 (task) / Mindset+Test (identity) / Checkpoint (output) |

## 4. Acceptance Criteria

### AC-1: Mindset blocks in research templates [source: RES D1, D2, D3, D4, D5]

Each research template MUST have:
1. h1 with guiding question (existing for 3 stages, **new** for Briefing)
2. Mindset blockquote with role-noun + instruction + Test — between h1 and `> Parent:` line

**Exact content per template:**

#### `1_briefing.md`
```markdown
# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-{PREFIX}-{N}](../../HL-{PREFIX}-{N}__{title}.md)
```

#### `2_gather.md`
```markdown
# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-{PREFIX}-{N}](../../HL-{PREFIX}-{N}__{title}.md)
```

#### `3_extract.md`
```markdown
# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-{PREFIX}-{N}](../../HL-{PREFIX}-{N}__{title}.md)
```

#### `4_challenge.md`
```markdown
# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-{PREFIX}-{N}](../../HL-{PREFIX}-{N}__{title}.md)
```

**Design rationale (from RES):**
- Role-nouns are functional, not metaphorical — activates professional associations in LLM training data (RES D1)
- Test questions are existential external with stage-output reference — NOT "Did I..." format (RES D2, D6)
- h1 guiding question stays — dual signal with Mindset: h1 = task orientation, Mindset = cognitive orientation (RES D3)
- Instruction sentence follows `{context}. {action}. {constraint}` formula extracted from review templates (RES Extract E5)
- Test escalation: purpose → coverage → insight → robustness (RES D7)

**Gate:** Each template has exactly `> **Mindset:**` and `> **Test:**` lines between h1 and `> Parent:`. Wording matches exactly.

### AC-2: Step 3 — folder only, no template copy

`base.md` Step 3 MUST:
- Create `research/iterN/` subfolder (unchanged)
- NOT copy any template files

Iteration 2+ predecessor reference instructions stay in Step 3.

**Gate:** No mention of `copy` or template filenames in Step 3.

### AC-3: Step 4 — copy-on-enter for briefing

`base.md` Step 4 MUST include an explicit instruction to copy `1_briefing.md` from `templates/research/` into `research/iterN/` before writing.

**Gate:** Step 4 contains copy instruction for briefing template.

### AC-4: Step 5 — per-stage copy-on-enter protocol [depends: AC-1]

`base.md` Step 5 MUST be restructured as an explicit per-stage loop:

```
FOR EACH stage (Gather → Extract → Challenge):
1. Copy stage template from templates/research/ into research/iterN/
2. Read the Mindset block — adopt this cognitive mode
3. Execute OODA Stage Loop
4. Complete Checkpoint in stage file
```

The dimensional analysis thread paragraph stays before the loop. OODA Stage Loop section stays as subsection referenced from inside.

**Gate:** Step 5 contains explicit copy + mindset instruction per stage. No batch copy anywhere.

### AC-5: STOP gates between stages [depends: AC-4]

The existing Stage Checkpoint section already has `🛑 WAIT`. Verify it applies per-stage within the loop — each stage gets its own STOP.

**Gate:** `🛑` marker present in the per-stage loop.

### AC-6: Resume Protocol compatibility

Step 0 MUST work with copy-on-enter:
- File exists → stage started/complete
- File doesn't exist → stage not started → copy template and start

Current Step 0 text: "which stage files exist? Resume from first missing stage." — this is compatible. Verify no assumption about all files pre-existing.

**Gate:** Step 0 does NOT assume all 4 files exist.

### AC-7: Adapter sync

Both adapters byte-identical to `base.md` after changes.

**Gate:** file comparison → 0 differences.

### AC-8: Version and changelog

- `.tfw/VERSION` = `0.8.7`
- `.tfw/project_config.yaml` version = `0.8.7`
- CHANGELOG `[0.8.7]` entry with: Mindset blocks in research templates, copy-on-enter protocol, per-stage STOP gates, Briefing h1 guiding question

**Gate:** All 3 files updated.

## 5. Technical Guidance

**Mindset block format** — exact pattern from review templates:
```markdown
> **Mindset:** {Role}. {Context}. {Action}. {Constraint}.
> **Test:** "{Existential question with stage-output reference}"
```

**Step 5 restructure** — keep dimensional analysis paragraph as intro. Convert body to FOR EACH with numbered sub-steps. Keep OODA Stage Loop as subsection.

**Briefing h1** — change from `# Briefing` to `# Briefing — "What should we investigate?"`. Does NOT follow the "What do we NOT {x}?" pattern — that's specific to the 3 investigative stages. Review templates also don't force a single question pattern (RES D4).

## 6. Definition of Failure

- ❌ Mindset text is generic/decorative — each stage must have a distinct role-noun and stage-specific Test
- ❌ Test questions duplicate Checkpoint checklists — Test = identity check, Checkpoint = task check (RES D6)
- ❌ Any `copy.*template` instruction remains in Step 3
- ❌ Step 5 still says "Cover all three" without explicit per-stage protocol
- ❌ Role-noun wording deviates from RES D1 without documented justification

## 7. Phase Risks

| # | Risk | Mitigation |
|---|------|------------|
| R1 | Mindset text becomes tautological | Each role-noun occupies distinct position on convergent↔divergent, build↔break axes (RES Challenge C1) |
| R2 | Step 5 restructure breaks OODA loop reference | Keep OODA as subsection, reference from inside loop |

---

*TS — TFW-43: Research Stage Protocol | 2026-05-01*
