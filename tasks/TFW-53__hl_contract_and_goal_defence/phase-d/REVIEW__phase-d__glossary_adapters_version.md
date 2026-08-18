# REVIEW — TFW-53 / Phase D: Glossary, Adapters & Version

> **Date**: 2026-08-17 · **second pass 2026-08-18**
> **Author**: Reviewer (Codex)
> **Verdict**: ✅ **APPROVE** — second pass. _(First pass: 🔄 REVISE, four items; all material items discharged.)_
> **RF**: [RF Phase D](RF__phase-d__glossary_adapters_version.md)
> **TS**: [TS Phase D](TS__phase-d__glossary_adapters_version.md)
> **Reference set** (Purpose Check): HL-TFW-53 at Contract Baseline `11cd340`, recovered per `conventions.md` §3 rule 15 · Project North Star in root `README.md` and `.tfw/README.md`
> **Stage files**: [`review/map.md`](review/map.md), [`review/verify.md`](review/verify.md), [`review/judge.md`](review/judge.md)
> This file is a synthesis of stage findings. Stage files carry the raw evidence.

---

## 1. Map

Phase D completes the portability and release pass for the HL-contract mechanism: ten glossary articles,
canonical Contract Baseline / Project North Star terminology, fourteen repaired full-copy adapters, truthful
thin Codex routers, four bounded Claude entry-point edits, five named debt closures, and the 1.2.0 release.
The implementation leaves Phases A–C intact and keeps resolver implementation and broader template cleanup
outside the phase.

All seven TS acceptance criteria map to an implemented result. The substantive execution safeguards were
the pre-copy direction check, which established that canonical sources were ahead of their adapter copies,
and the decision to exclude `uncommitted baseline` from a mechanical synonym sweep because it names an
absence rather than the defined concept.

## 2. Verify

> Minimum verification: ⌈33 × 0.42⌉ = 14 files. Escalated to **33 of 33 (100%)** after D1.
> Raw log: [`review/verify.md`](review/verify.md).

| # | What was checked | Result | Evidence |
|---|-----------------|--------|----------|
| 1 | Seven AC outcomes and frozen DoD-30–33 | ✅ | Ten glossary articles at 41–50 body words with pointers; retired forms cleared; bounded entry-point edits; release and debt outcomes reproduced (V1–V10) |
| 2 | Full-copy and Codex adapter parity | ✅ | 14 parent-tree mismatches become 0; all 22 workflow/copy pairs and all 11 Codex source/installed pairs match (V4–V5) |
| 3 | Executable tests and repository hygiene | ✅ | `python -m pytest docs/scripts/` → **68 passed in 41.47s**; `git diff --check` and credential-pattern scan clean |
| 4 | Release history | ✅ | VERSION and `tfw.version` are 1.2.0; all 8 releases from 0.8.5 through 1.2.0 are lockstep (V7) |
| 5 | Scope budget | ❌ | **33 total files** against the independent 30-file limit; 28 modified and 5 new pass only their sub-limits. No explicit owner override exists (D1) |
| 6 | AC-7 diff ledger | ❌ | `git diff -U0` produces **16** hunk headers, not 12; the semantic ledger has **11** canonical substitutions, not 8. The actual changes remain within permitted categories (D2) |
| 7 | EV claims | ❌ 17/19 | E1–E16 and E18 establish their claims; E17 and E19 are overclaimed. The EV's `19/19 VERIFIED` verdict is unsupported |
| 8 | Knowledge citations and RF §7–9 | ⚠️ | All 30 cited knowledge items resolve and are relevant; diagrams are accurate. Four of five Fact Candidates and all four Strategic Insights fail their Human-Only Test (D3) |

Nothing was unverifiable. The two numeric discrepancies do not conceal an implementation-category violation:
the glossary, adapter and release results independently hold.

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ✅ | Seven of seven functional AC outcomes and frozen DoD-30–33 reproduced (verify.md V1–V10) |
| 2 | Purpose Check — is this what we set out to do? + design soundness | ✅ | Baseline Vision requires that *"the contract gains a defender"*; the north star requires the same `.tfw/` core across tools. One vocabulary and synchronized adapters prevent tool-dependent contract behavior. The design respects HL P3, P7–P9 and P12 |
| 3 | Tech debt documented | ✅ | Seven observations present; two new material items promoted, two already tracked/routed, one subsumed, two rejected by the quality filter |
| 4 | Style & standards | ❌ | D1: unapproved 33-file scope exceeds `max_files_per_phase: 30` by 3 |
| 5 | Observations collected | ✅ | Five observations describe real conditions; observations 6–7 have no material failure consequence |
| 6 | RF completeness (§7–9 present and usable) | ❌ | Sections exist, but D3 makes most of §7 and all of §8 inadmissible to the knowledge pipeline |
| 7 | Evidence completeness — does it exist? | ✅ | All 19 EV rows and four attachments exist and cover the TS Evidence fields |
| 8 | Evidence sufficiency — does it establish the claim? | ❌ | E17 and E19 do not; actual supported count is 17/19 (D1–D2) |
| 9 | Backward compatibility | ✅ | Full-copy and router parity hold; section structure and anchors stay stable; the glossary is additive and version markers remain lockstep |
| 10 | Safety | ✅ | No credentials or destructive behavior; text/config changes pass whitespace and secret-pattern checks; concurrent README work was preserved |

## 4. Verdict

**🔄 REVISE**

The delivered mechanism is functionally complete, purpose-aligned and safe: all seven acceptance-criterion
outcomes hold, 68 tests pass, adapter parity is clean, and release markers are consistent. This is not a
purpose failure and does not require HL or TS redesign.

The phase cannot be approved with its current trace. It exceeded the independent total-file scope budget
without an owner override, and the RF/EV masks that overrun by comparing only the modified/new sub-limits.
The same evidence record reports a `git diff -U0` count that does not reproduce. Finally, RF §7–8 would feed
agent-discoverable and agent-generated statements into a pipeline reserved for human-provided knowledge.
Those are correctable authorization and evidence-integrity defects, so REVISE is proportionate; REJECT is
not.

### If REVISE — items to fix:

1. **Resolve the 33 > 30 total-file budget breach.** Consolidate or remove at least three supporting
   evidence files while preserving auditable proof, or obtain and record an explicit owner override as a
   distinct act. Recount all independent scope limits in RF and EV; passing modified/new sub-limits is not
   a substitute for the total-file limit.
2. **Correct the AC-7 ledger.** Replace the claimed 12 `-U0` hunks / 8 substitutions with a reproducible
   command and unambiguous classification. The current repository gives 16 `-U0` hunk headers and 11
   semantic canonical substitutions; update RF §3, RF §9 and EV E17 consistently.
3. **Repair RF §7–8 under the Human-Only Test.** Retain FC3; move or remove FC1, FC2, FC4 and FC5 because
   they are artifact- or agent-derived. Move the four Strategic Insights to observations/analysis or state
   `No strategic insights.` unless genuinely human-sourced knowledge is available.
4. **Re-run the evidence verdict after items 1–3.** Until then the supported result is **17/19**, not
   `19/19 VERIFIED`; propagate the corrected count to EV and RF.

### If REJECT — fundamental issues:

None. No frozen-contract or design rework is required.

## 5. Tech Debt Collected

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| TD-171 | RF TFW-53/D §6 obs. 1 | Low | `.tfw/workflows/plan.md` Step 2 | TD-163 closed the wrong Knowledge Gate step pointer but left the separate ~50-word mode duplication only inside a closed row. Without an open registry item, the residual cannot be selected or closed independently | → TFW-57 / next authorized plan-workflow cleanup |
| TD-172 | RF TFW-53/D §6 obs. 5 | Medium | `CLAUDE.md`:51,53 | Two links use `.tfw/PROJECT_CONFIG.yaml`; the tracked filename is lowercase. Windows masks the defect, but case-sensitive clones receive broken entry-point links | → next entry-point/docs cleanup |

**Already tracked or routed:** observation 2 is TD-170; observation 3 is the recorded TD-131 reroute;
observation 4's residual is subsumed by TD-170 and the stale TD-133 disposition should be cleaned by
`/tfw-docs`.

**Rejected by the quality filter:** observation 6 — the thin routers truthfully point to the canonical
workflows, so duplicating mechanism summaries would weaken their router role; observation 7 — a Markdown
line wrap can confuse a naive grep but does not create a second term or alter rendered meaning.

## 6. Traces Updated

- [x] README Task Board — status set to **📚 KNW (A, B, C) · 🔄 REVISE (D)** and the Phase D REVIEW linked; concurrent TFW-55 working-tree changes preserved
- [ ] HL status — not modified; reviewer role lock forbids HL edits and Phase D has not passed review
- [x] project_config.yaml — no `initial_seq` change needed
- [x] Other project files — TECH_DEBT.md appended with TD-171 and TD-172; stale TD-133 disposition noted for `/tfw-docs`
- [x] **tfw-docs: Applied 2026-08-18** — one pass across Phases A–E. `KNOWLEDGE.md` §1 Adapters row (drift check), **D63** contract · **D64** purpose defence · **D65** rejected trace; §2 three artifact rows; §3 six new legacy entries plus the TFW-48/49 row re-pointed at the post-mortems. `TECH_DEBT.md`: TD-176/177/178 added, TD-156 closed, TD-169(a) closed.
- [x] **tfw-knowledge: Applied 2026-08-18** — one pass across Phases A–E. **25 facts** written (105 → 130): philosophy +8, process +5, stakeholder +4, constraint +3, environment +2, convention +2, and a new `knowledge/risk.md` +1. RF §7 FC1 survived the Human-Only Test at the second pass and is written as `stakeholder` F8; this REVIEW's §7 FC1 is `convention` F22

## 7. Fact Candidates
> fact-candidates: processed 2026-08-18 (`/tfw-knowledge`, TFW-53 A–E)


| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | convention | The Task Board update in root `README.md` is a TFW process artifact, not an executor-derived product file, and does not spend the executor phase's product-file budget. Under this ruling Phase D counts 27 product files, not 28 | Owner clarification during second review, 2026-08-18 | High |

The first pass introduced no human-sourced fact. This candidate comes solely from the owner's corrective
clarification during the second review and should be consolidated together with TD-173's eventual rule text.

## 8. Second-Pass Review — 2026-08-18

### 8.1 Map

The coordinator added AC-8–AC-12 in commit `3d89b59`; the executor completed them in `2e60934`. The
corrective pass did not reopen the glossary, adapters, workflows, templates or release. It corrected the
ledger and knowledge sections, recomputed EV, fixed two case-wrong `CLAUDE.md` links, and recorded the two
general rule gaps as TD-173/TD-174.

| First-pass item | Second-pass outcome |
|---|---|
| 33 > 30 under an undefined denominator | ✅ Owner defined the subject and later clarified that README is a TFW process artifact. Governing count: **27/30 product files**, 0 new product, 6 trace files |
| 12 hunks / 8 substitutions did not reproduce | ✅ Exact command now reproduces **16 hunk headers / 11 substituted lines** with full per-file reconciliation |
| RF §7–§8 failed Human-Only admission | ✅ One owner-sourced Fact Candidate remains; §8 states `No strategic insights.`; agent material is re-homed or dropped |
| EV verdict unsupported at 19/19 | ✅ E17/E19 replaced, seven corrective rows added, EV recomputed to **26 rows**; implementation claims independently verified |

### 8.2 Verify

> Corrective scope: 5 files; opened **5/5 (100%)**. Raw evidence:
> [`review/verify.md`](review/verify.md), second-pass section.

| Check | Result |
|---|---|
| Corrective diff boundary | ✅ TS only in coordinator commit; `CLAUDE.md`, TECH_DEBT, RF and EV only in executor commit |
| Documentation tests | ✅ **68 passed in 34.47s** |
| Adapter parity | ✅ **22/22** full-copy pairs and **11/11** Codex source/installed pairs match |
| AC-9 ledger | ✅ 16 `-U0` headers; 11 substituted lines; 4 debt fixes; 2 addition sites; 47 insertions / 15 deletions |
| Entry-point links | ✅ 0 `PROJECT_CONFIG` hits in `CLAUDE.md`/`AGENTS.md`; lowercase target exists |
| Evidence structure | ✅ 26 unique EV rows and four attachments exist; material AC claims reproduce |
| Scope | ✅ Owner-governing count **27/30**; even RF's earlier conservative 28 count remained below the limit |

Three stale summary labels remain: TS carries a duplicated `14 of the 28` tail; RF's file list calls EV
“19 rows”; RF's AC-12 row says `19/19` and five additions while RF §5/EV correctly say `26/26` and seven.
The owner explicitly ruled these arithmetic labels non-material and directed this pass to judge execution
quality. They do not change any behavior, test result, adapter, release marker or acceptance conclusion.

### 8.3 Judge

| # | Check | Status | Evidence |
|---|---|---:|---|
| 1 | DoD met? | ✅ | AC-1–AC-12 and frozen DoD-30–33 hold under the owner's final scope classification |
| 2 | Purpose + design | ✅ | Purpose remains aligned; only two broken configuration links changed, improving cross-tool portability |
| 3 | Tech debt documented | ✅ | TD-172 closed; TD-173/174 carry the two general rule gaps; TD-170/171 remain routed |
| 4 | Style & standards | ✅ | Governing product count 27/30; commits and diffs clean; non-material summary labels disclosed |
| 5 | Observations collected | ✅ | Every observation closed, routed, subsumed or rejected with reason |
| 6 | RF §7–§9 quality | ✅ | Human-only Fact Candidate retained; no agent Strategic Insights; diagrams and ledger accurate |
| 7 | Evidence completeness | ✅ | 26 rows and four attachments cover AC-1–AC-12 |
| 8 | Evidence sufficiency | ✅ | Former E17/E19 failures now reproduce; 68 tests and both parity sets independently pass |
| 9 | Backward compatibility | ✅ | Broken case-sensitive links repaired; no structural consumer changed |
| 10 | Safety | ✅ | Markdown-only corrective diff; no secrets/destructive operations; TFW-55 work preserved |

### 8.4 Final Verdict

**✅ APPROVE**

The implementation is complete and purpose-aligned. The first-pass material failures are discharged:
adapter behavior is identical across surfaces, all executable tests pass, the ledger reproduces, knowledge
admission is corrected, case-sensitive entry-point consumers are repaired, and the scope is 27/30 under the
owner's governing classification. The remaining labels are historical/editorial trace noise explicitly
accepted by the owner, not defects in execution quality.

This is APPROVE rather than APPROVE-with-hidden-exceptions: the residuals are named above, their lack of
material consequence is stated, and the two framework-wide ambiguities are preserved as TD-173 and TD-174
instead of being silently normalized inside Phase D.

### 8.5 Tech Debt and Traces

- TD-172 — ✅ closed by AC-11.
- TD-173 — remains open so the product-vs-TFW-artifact budget subject and the owner's README ruling become
  canonical rather than task-local.
- TD-174 — remains open for the contradictory Fact Candidate template instructions and knowledge back-check.
- No new debt promoted from observations 8–11: 8 is closed history, 9 is resolved by a ruled exclusion,
  10 is a declared Bash environment that succeeded, and 11 found no live occurrence.

- [x] README Task Board — Phase D set to **📚 KNW**, D REVIEW link marked ✅; TFW-55 changes preserved
- [ ] HL status — unchanged; reviewer role lock and post-APPROVE knowledge gate apply
- [x] project_config.yaml — no `initial_seq` change needed
- [x] TECH_DEBT.md — TD-173 updated with the owner's final README classification; TD-172/174 retained accurately
- [ ] tfw-docs — **pending**, next workflow after APPROVE
- [x] tfw-knowledge — **applied 2026-08-18**; RF FC1 → `stakeholder` F8, REVIEW FC1 → `convention` F22

---

*REVIEW — TFW-53 / Phase D: Glossary, Adapters & Version | second-pass verdict 2026-08-18*
