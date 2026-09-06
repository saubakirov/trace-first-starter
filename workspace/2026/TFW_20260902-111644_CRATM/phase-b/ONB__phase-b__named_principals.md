# ONB — TFW_20260902-111644_CRATM / Phase B: Named principals

> **Date**: 2026-09-06
> **Author**: Executor (Codex)
> **Status**: 🟠 ONB — Ready to execute; no blocking questions
> **Parent HL**: [HL-TFW_20260902-111644_CRATM](../HL-TFW_20260902-111644_CRATM.md)
> **Phase HL**: [HL Phase B](HL__phase-b__named_principals.md)
> **TS**: [TS Phase B](TS__phase-b__named_principals.md)
> **Approval/start state**: `1e2631bff51b3b62673808d5de57f812883d814b`

---

## 1. Understanding

Phase B adds the smallest complete Markdown contract for stable human and agent principals. The
profile schema gains optional descriptive roles, accountable-human linkage, a Boolean amendment
grant, and optional mentality; current journal events may name a declared principal as `writer`; and
the per-machine binding may select either a human or valid agent principal. Accountability remains
human, roles and mentality grant nothing, the filename token remains uniqueness only, all 28 legacy
`actor` events and the existing four-key human profile remain untouched, and the report-only reader
and its tests remain excluded. Phase C–E concepts are not introduced.

## 2. Entry Points

- Governing artifacts: the master HL, Phase B HL, and approved
  `TS__phase-b__named_principals.md`; immutable Baseline
  `a048b2db5f44f5d748f22f3a0133f4ecf0acd9c4` and approval commit
  `1e2631bff51b3b62673808d5de57f812883d814b`.
- VALUE owners: `.tfw/conventions.md`, `.tfw/templates/team/profile.md`,
  `.tfw/templates/journal/event.md`, and `.tfw/templates/bindings.yaml`.
- Compatibility inputs: unchanged `team/saubakirov.md`; the 28 tracked journal events containing
  legacy `actor`; `.tfw/scripts/gen_index.py` and `.tfw/scripts/test_gen_index.py` as read-only,
  report-only evidence subjects.
- Configured gates: `python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only`,
  `python -m pytest .tfw/scripts/ docs/scripts/ -q`, and
  `python .tfw/scripts/gen_index.py --check project`. The task diagnostic is run and disclosed
  separately, never promoted into acceptance authority.

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions. The approved TS fixes the field names, compatibility behavior, exact VALUE
selector, immutable denominator, Baseline, and stop conditions. The coordinator's dispatch explicitly
authorizes autonomous execution within that bound.

## 4. Recommendations (suggestions, not blocking)

1. Put one canonical profile/principal contract beside the existing task-control identity rules in
   `conventions.md`; keep each template focused on its own form and point back to that owner.
2. Keep `writer`, `on_behalf_of`, `via`, and the filename token visibly orthogonal in both the
   canonical rule and event template. Treat `actor` only as unchanged historical input.
3. Use disposable YAML fixtures and a documentation-contract checker for AC-1/2/4. This demonstrates
   the stated Markdown contract without changing or borrowing authority from `gen_index.py`.
4. Preserve the Phase A worktree, exact-path staging, and landing clauses byte-for-byte where Phase B
   has no reason to edit them; prove preservation against the Baseline.

## 5. Risks Found (edge cases, potential issues not in TS)

1. The report-only reader's closed `EVENT_KEYS` rejects a synthetic `writer`; evidence must disclose
   that expected diagnostic without treating it as a Phase B failure or changing the reader.
2. Agent validity is relational: `accountable_to` must resolve to an existing human rather than just
   match a handle shape. Fixtures must cover missing handles and agent-to-agent accountability.
3. A Boolean-looking YAML scalar can be quoted text. Evidence must reject `"true"`, `yes`, and other
   non-Boolean grant values even when a permissive YAML parser accepts them as scalars.
4. The three templates must remain below the ~1200-word attention threshold. `conventions.md` already
   exceeds it, so any growth needs a minimum-necessary judgment and exact Baseline/Candidate counts.
5. Stale TFW-54 prose occurs beyond Phase B's four owners. Only owned passages needed to explain the
   shipped principal may change; the complete sweep remains Phase E.

## 6. Inconsistencies with Code (spec vs reality)

1. Expected current-state gap: `profile.md` still declares a four-key, people-only schema;
   `event.md` has no current `writer`; `bindings.yaml` forbids agent bindings; and the matching
   `conventions.md` passages say no writer/principal exists. These are exactly the four approved
   VALUE changes, not blockers.
2. Expected report-only mismatch: `.tfw/scripts/gen_index.py` includes legacy `actor` but not
   `writer` in `EVENT_KEYS`. The TS and rejected master amendments A1/A2 explicitly preserve this
   behavior and forbid treating it as current schema authority.
3. The master HL §7.2 citation numbers have drifted from the current North Star: its item 2 calls
   “Human authority, bounded delegation” NS2 principle 4, now principle 5; item 4 calls “Assurance
   proportional to risk” principle 6, now principle 7. The quotations still resolve, and Phase B HL
   B1 uses the current number. This is non-blocking and outside the Executor's artifact authority.
4. No unexpected implementation contradiction was found. Baseline and approval HEAD contain
   identical blobs for all four VALUE paths; the Baseline contains exactly 28 tracked `actor` event
   files and the current worktree begins clean.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | Master #1 · NS1 Purpose | ✅ | Applied | Stable, inspectable principals support authorized continuation without reconstructing chat. |
| 2 | Master #2 · NS2 Human authority, bounded delegation | ✅ | Applied | `accountable_to`, the fixed Boolean grant, and HC-B1 preserve human authority; current NS2 number is 5, not the cited 4. |
| 3 | Master #3 · NS3 Non-goals | ✅ | Applied | No runtime, provider identity, registry, hook, or executable addition. |
| 4 | Master #4 · NS2 Assurance proportional to risk | ✅ | Applied | Reuse existing checks plus temporary fixtures; add no permanent test surface. Current NS2 number is 7, not the cited 6. |
| 5 | Master #5 · Structural Enforcement | ✅ | Applied | Required profile relationships and grant bounds are explicit, testable form rules. |
| 6 | Master #6 · Naming Creates Behavior | ✅ | Applied | Lower-snake-case fields and stable handles separate identity, accountability, tool, and grant. |
| 7 | Master #7 · Portability | ✅ | Applied | Principal identity excludes provider, model, executable, process, and session. |
| 8 | Master #8 · `philosophy.md` F37 | ✅ | Applied | Neither mentality, role context, nor delegation widens authority. |
| 9 | Master #9 · `philosophy.md` F38 | ✅ | N/A to implementation mechanics | Supports the phase split; this Executor does not change sequencing. |
| 10 | Master #10 · D59 | ✅ | Applied | Declared attribution is not authentication; a session is not an independent person. |
| 11 | Master #11 · D68 | ✅ | Applied | Keep task-local state, opaque uniqueness tokens, and all legacy `actor` events unchanged. |
| 12 | Master #12 · D63 | ✅ | Applied | The frozen master is authority; no HL or scope change is made. |
| 13 | Master #13 · D64 | ✅ | Applied | Evidence and RF remain reviewable against purpose, not only the TS. |
| 14 | Master #14 · D55 | ✅ | Applied | Every Executor commit will use exact task/phase/role attribution. |
| 15 | Master #15 · D54 | ✅ | N/A to Phase B files | Adapter parity and the remaining vocabulary sweep belong to Phase E. |
| 16 | Master #16 · D31 | ✅ | N/A to Phase B files | No new state carrier is introduced; existing file-existence semantics remain. |
| 17 | Master #17 · conventions rules 17–19 | ✅ | Applied | The approved selector and multiplier are ceilings, not self-widening authority. |
| 18 | Master #18 · conventions rules 20–21 | ✅ | Applied | Phase HL is read as derivation-only and remains unmodified. |
| 19 | Master #19 · conventions §14 | ✅ | Applied | No out-of-TS bonus work, broad staging, role crossing, or fabricated evidence. |
| 20 | Master #20 · `convention.md` F19 | ✅ | Applied | All new keys use consistent lower-snake-case naming. |
| 21 | Master #21 · `process.md` F6 | ✅ | Applied | Four exact VALUE owners and HC-B1 prevent coordinator/executor scope expansion. |
| 22 | Master #22 · `process.md` F30 | ✅ | Applied | Rules land in the canonical contract and the forms that issue the fields. |
| 23 | Master #23 · `process.md` F7 | ✅ | Applied | Durable files, not session memory, carry the new meanings. |
| 24 | Master #24 · `constraint.md` F11 | ✅ | N/A as dated capability claim | The master records it as measured false; provider routing is Phase D/E, not Phase B. |
| 25 | Master #25 · `constraint.md` F12 | ✅ | Applied | Principal and grant obligations are written into repository-owned canonical files. |
| 26 | Master #26 · `constraint.md` F2 | ✅ | Applied | Exact word counts and minimum necessary growth will be evidence. |
| 27 | Master #27 · `risk.md` F1 | ✅ | Applied | Separate worktree plus exact-path commits; no broad staging. |
| 28 | Master #28 · `stakeholder.md` F6 | ✅ | Applied | Work proceeds autonomously only inside the immutable approved contract. |
| 29 | Master #29 · `stakeholder.md` F7 | ✅ | N/A to implementation form | The approved HL already rendered the result; this phase implements that bound. |
| 30 | Master #30 · `stakeholder.md` F8 | ✅ | Applied | Reporter output is disclosed as report-only rather than normalized or hidden. |
| 31 | Master #31 · `environment.md` F3/F4 | ✅ | N/A to Phase B commands | No new shell-portable subject-recovery command is authored; existing Phase A text stays intact. |
| 32 | Master #32 · Assisted team README | ✅ | Applied as field evidence only | Confirms two descriptive role dimensions and absence semantics; no schema convergence. |
| 33 | Master #33 · D68 opaque token | ✅ | Applied | `writer` never supplies filename uniqueness and legacy `actor` stays historical. |
| 34 | Master #34 · D73 | ✅ | Applied | The canonical contract is placed in the already selected §4 authority, without adapter edits. |
| 35 | Master #35 · D74/D75 | ✅ | Applied | Preserve selective reads, template-owned forms, and strict-current/tolerant-legacy separation. |
| 36 | Master #36 · `process.md` F39 | ✅ | Applied | Search defines relevant gates and legacy corpus; memory does not define the delivery set. |
| 37 | Phase B B1 · NS2 principle 5 | ✅ | Applied | Agent profiles require an accountable human and explicit two-level grant before use. |
| 38 | Phase B B2 · Methodology values | ✅ | Applied | Stable provider-neutral handles carry grant identity; naming remains precise and portable. |
| 39 | Phase B B3 · `philosophy.md` F37 | ✅ | Applied | Mentality and descriptive roles cannot create permission. |
| 40 | Phase B B4 · D59, D68, D76, D77, D79 | ✅ | Applied | Preserve orthogonal fields, immutable accounting, separate-worktree execution, and navigation-only session titles. |
| 41 | Phase B B5 · Task control files / Which handle a machine acts as | ✅ | Applied | Extend these exact canonical owners once while keeping one-profile and binding resolution behavior. |
| 42 | Phase B B6 · `convention.md` F19 | ✅ | Applied | New schema vocabulary is lower-snake-case and single-purpose. |
| 43 | Phase B B7 · `process.md` F30/F38/F39/F46 | ✅ | Applied | Put bounds at issuing sites, avoid late gates, derive searches, and respect sequenced shared files. |
| 44 | Phase B B8 · `constraint.md` F12 | ✅ | Applied | No principal obligation is left only in tool/session memory. |
| 45 | Phase B B9 · FA15ES HL §11 S6 | ✅ | Applied as evidence, not authority | Roles are project-local context, never permission; Full and Assisted remain independent. |

No new PV item was found that changes Phase B's implementation. The master citation-number drift is
recorded in §6 for Coordinator disposition rather than promoted into a new knowledge claim.

---

*ONB — TFW_20260902-111644_CRATM / Phase B: Named principals | 2026-09-06*
