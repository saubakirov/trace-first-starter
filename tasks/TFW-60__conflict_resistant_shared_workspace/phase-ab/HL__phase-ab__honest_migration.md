# HL — TFW-60 / Phase AB: Honest Migration

> **Date**: 2026-08-29
> **Author**: Claude Code (Coordinator)
> **Status**: 📝 HL_DRAFT — awaiting owner review
> **Parent HL**: [HL-TFW-60](../HL-TFW-60__conflict_resistant_shared_workspace.md)
> **Master freeze**: `810b1b8` — baseline after amendment A5
> **Authority**: derivation-only. Vision, Target State, Phases, DoD, DoF and Principles exist once, in the master HL.
> **Origin**: [third field report](../FIELD-REPORT__TFW-60__third_external_update.md), `helpdesk`, `0.8.7 → 2.0.0-dirty.3`
> **Predecessor**: Phase AA, closed by owner 2026-08-29 with review revision 3's blocking item 1 outstanding (TD-199)

---

## Phase Purpose

Phase AA made the framework deliverable and three external projects proved it. This phase makes the
tools that do the delivering **tell the truth**.

The third external update crossed four releases in one session and never had to reconstruct the order of
operations. Along the way one tool read a task identifier it could not parse whole, guessed, wrote a live
`TODO` onto a task that production had already shipped, and printed a guarantee it had never computed.

## The Release in One View

```text
WHAT HAPPENED — three levels, three confident false statements, no warning

board row   | [HD-30b](tasks/HD-30__tickets…/hd30b/) | ⬜ TODO — gates removed |
                    │
                    │  identifier not parsed whole; the remainder discarded
                    ▼
manifest    | 30 | HD-30 | … | 31 | HD-30 |        ← one identifier, listed twice
            "Every row and directory is accounted for exactly once. Unaccounted: 0"
                    │
                    ▼
status.md   lifecycle: TODO        ← on a task the board closed ✅ DONE
                    │
                    ▼
index       Closed | HD-30 | Outcome: ⬜ TODO — gates removed


AFTER PHASE AB

identifier ──> parsed WHOLE against three named forms ──> or it is `malformed`
                                                          and nothing guesses

manifest   ──> computes matched + directory_only == directories
               under "Guarantees checked", naming each one
               two rows resolving to one identifier is a HARD STOP

prose      ──> markup stripped, identifier characters preserved
               normalize_text() survives as normalize_text()
```

## Direct Answers to the Scope Questions

| Question | Phase AB answer |
|---|---|
| Does the identifier grammar change? | **Yes** — new tasks use `{PREFIX}_{YYYYMMDD-HHMMSS}_{ABBR}`. The owner ruled on 2026-08-29 that it lands here rather than after `2.0.0`, so an external user meets one new grammar instead of two in consecutive releases |
| Why in this phase and not its own? | A parser that must refuse what it cannot read whole and a grammar change are **the same work**. Split apart, the corpus migrates twice |
| Are existing tasks renamed? | **No.** DoF 8 and DoD 10 stand. Legacy `PREFIX-N__slug` and `2.0.0-dirty` `YYYYMMDD-HHMMSS__slug` remain readable forever |
| What makes the abbreviation legitimate? | It is **declared and approved at planning**, never derived silently. An opaque token nobody agreed to is not shorter, it is unreadable |
| Where does the full name live? | In `status.md` `title`, which already carries it, and in the HL header. No new carrier |
| Does the manifest keep printing guarantees? | Only the ones it computes. A claim without its arithmetic is removed or implemented — never both left standing |
| What happens to `HD-30b` specifically? | Nothing. The owner ruled it a closed sub-item of a closed task. This phase fixes the class, not the instance |
| Does Phase AB touch task state, journals or the index schema? | **No.** It changes how identifiers are *parsed* and how migration *reports*, not what a task carries |
| Does it re-open Phase A or AA? | **No.** Both declared outcomes are met. This is a distinct capability, added by amendment A5 |

## What Phase AB Delivers

| Release surface | Concrete result |
|---|---|
| Identifier parsing | Three named forms, each matched whole; anything else is `malformed` and is reported, never guessed |
| Identifier grammar | `{PREFIX}_{YYYYMMDD-HHMMSS}_{ABBR}` for new tasks, with the abbreviation approved at planning and recorded in the HL |
| Migration honesty | Every asserted invariant computed under a stated heading; duplicate resolution is a hard stop before any write |
| Prose fidelity | Markup stripped, identifier characters preserved; a `snake_case` name survives migration unchanged |
| Test separation | Framework self-tests and receiving-corpus tests distinguishable, so `build.test` is not red merely because a migration is mid-flight |
| Source discipline | A quiescence rule for the update source, matching the one the receiver already has |
| Update accuracy | Provenance drift distinguished from customization; checks state conditions that can actually hold |
| Carried from Phase AA | `update.md` returned under its word ceiling (F4) and `via` either validated or declared free-form (TD-197) — both land in files this phase opens anyway |

## Explicitly Not in Phase AB

- renaming, moving or rewriting any existing task directory, in this repository or any consumer;
- any change to `status.md` keys, the journal event schema, the lifecycle vocabulary or the index format;
- the `actor` field, which returns with TFW-54 and not before;
- retrofitting the three consumer projects — they update when the release lands;
- Phase B debt locality and Phase C knowledge staging;
- transport mode, which is TFW-61;
- a fourth external run as a release gate: the owner ruled on 2026-08-29 that `2.0.0` follows this phase
  without one, since requiring a fresh external run to certify each correction the previous run produced
  defers the release forever.

## Evidence Required Before Phase AB Can Be Called Released

Inherited from master HL §5 — DoD 10, DoD 20 — and §7.1. This file creates no second Definition of Done.

| Evidence class | Required observation |
|---|---|
| Parse-whole | A fixture carrying `HD-30`, `HD-30b`, `TFW-01_single_underscore` and a new-grammar identifier: each is matched to its named form or reported malformed, and none is guessed |
| Duplicate resolution | Two board rows resolving to one identifier stop the run **before any write**, with both rows named |
| Computed guarantees | The manifest's own arithmetic fails on a deliberately unbalanced fixture and states which guarantee failed |
| Prose fidelity | A board cell containing `normalize_text()` inside backticks migrates with the identifier intact |
| Grammar coexistence | All three forms parse in one corpus; no existing path changes; the index and manifest agree on every identifier |
| Test separation | The suite is green on a project mid-migration, and the accounting invariant is exercised by something a receiving project is actually told to run |
| Regression | The exact helpdesk board shape reproduced as a fixture, failing before the change and passing after |

## Source Authority for Phase AB

| Source | What Phase AB inherits |
|---|---|
| [Master HL](../HL-TFW-60__conflict_resistant_shared_workspace.md) at `810b1b8` | Frozen purpose, Phase AB declared outcome, DoD 10 and DoD 20, DoF, principles |
| [Third field report](../FIELD-REPORT__TFW-60__third_external_update.md) | Seven defect groups, measured on a real corpus by an operator who did not write the code |
| [First field report](FIELD-REPORT__TFW-60__first_external_update.md) F4 | The same class in its earlier form: a grammar that did not match, and a generated artifact that described real work as something it was not |
| Phase AA REVIEW revision 3 | TD-197 and TD-199; the ruling that AC-13 half two is met |
| `conventions.md` §4 | The identifier grammar this phase extends |

## Phase-Local Risks

| Risk | Control carried into TS/evidence |
|---|---|
| A third grammar makes the parser harder to trust, not easier | Three **named** forms with one dispatcher; anything unmatched is malformed. The parser gets stricter, not more permissive |
| The abbreviation becomes unreadable noise | Declared and approved at planning; the full title stays in `status.md`, which the index renders |
| Fixing the instance instead of the class | `HD-30b` is explicitly out of scope; the evidence is a fixture, not a repair |
| Stricter parsing rejects something that used to work | Every existing corpus is re-run before and after; a form that parsed must still parse |
| Consumers already carry the `2.0.0-dirty` grammar | It stays a named, supported form forever; nothing they hold is renamed |
| The phase drifts into a fourth delivery pass | The declared outcome is honesty of the tools. A delivery finding is filed, not fixed here |

---

*HL — TFW-60 / Phase AB: Honest Migration | 2026-08-29*
