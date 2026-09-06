# RF — TFW_20260902-111644_CRATM / Phase B: Named principals

> **Date**: 2026-09-06
> **Author**: Codex (Executor, acting as `saubakirov`)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW_20260902-111644_CRATM](../HL-TFW_20260902-111644_CRATM.md)
> **TS**: [TS Phase B](TS__phase-b__named_principals.md)

---

## 1. What Was Done

Implemented one compatible named-principal contract across profiles, current journal events, and
per-machine bindings. Humans keep their existing four-key profile form. Agents now have a stable
project-local handle, direct accountable human, immutable two-level amendment grant, and optional
descriptive mentality. Current events may name their writer without changing accountable-human,
tool, token, or legacy-actor meanings. Bindings select attribution only.

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `1e2631bff51b3b62673808d5de57f812883d814b`; approved planning content `b1cb7b0374703d87f76d9c8de67bbef264cddcc5` |
| Baseline / Candidate | `a048b2db5f44f5d748f22f3a0133f4ecf0acd9c4` / `0ee39046b760d6d3e8d837c2377e49c1c95668bd` |
| VALUE membership | `.tfw/conventions.md`, `M`, VALUE, shared principal/profile/event/binding semantics; `.tfw/templates/team/profile.md`, `M`, VALUE, compatible human/agent schema; `.tfw/templates/journal/event.md`, `M`, VALUE, optional writer and legacy composition; `.tfw/templates/bindings.yaml`, `M`, VALUE, principal selection without authority |
| Arithmetic | 143 additions + 72 deletions = 215 touched text LOC; 4 logical files; binary/non-text N/A |
| Membership deviations | None. The immutable four-path selector is exact. Actual LOC is a 25-line underspend against the approved 240-LOC comparison denominator, not a denominator change. |
| Trigger disposition | Cause: 4 files and 215 LOC remain below 50/5,000 prompts. Cost: one 215-LOC cross-owner contract. Assurance: 17/17 contract fixtures, 629-pass suite, unchanged legacy/reporter blobs, and structural/docs checks. Split alternative rejected because separating canon, profile, event, or binding would leave an unusable or ambiguous identity path. Authority remained Coordinator-level below 8 files/480 LOC and HC-B1 was unchanged. Terminal verdict: keep one Phase B. |
| Authority and timing | Owner-approved immutable denominator 4 files/240 LOC was recorded before execution in the approval ref. Candidate was committed 2026-09-06T10:17:51+05:00 after passing implementation gates and before EV, RF, REVIEW, or RF state. No additional ruling was required. |
| Reproduction | The approved literal four-path PowerShell array and unchanged NUL-safe `git diff --name-status --find-renames=50% -z` / `git diff --numstat --find-renames=50% -z` method reproduce four `M` records and per-path `41/13`, `70/32`, `14/11`, `18/16`; see EV E-accounting. |

This reports the approved contract; it cannot create a selector, move Candidate, ratchet the denominator,
or supply late authority.

### Round 2 — Evidence Provenance Return

Round 2 changes no implementation, assurance path, approved order, selector, accounting result, or
Candidate. It appends a complete executable validator to the cumulative EV, replays the exact 17
documented fixture payloads from that preserved program, and records the current result. Candidate
remains `0ee39046b760d6d3e8d837c2377e49c1c95668bd`; it is an ancestor of the Round 2 lineage, all four
VALUE paths have zero Candidate→working-tree diff, and `git log <Candidate>..HEAD -- <VALUE paths>`
returns no later VALUE commit.

### New Files

| File | Description |
|---|---|
| `ONB__phase-b__named_principals.md` | Executor onboarding, source coverage, constraints, risks, and pre-implementation recommendations |
| `evidence/EV__phase-b__named_principals.md` | Per-AC fixtures, compatibility/corpus checks, configured checks, and immutable accounting replay |

### Modified Files

| File | Changes |
|---|---|
| `.tfw/conventions.md` | Defines declared human/agent principals, stable grants, optional writer, legacy actor treatment, and principal binding resolution in §4. |
| `.tfw/templates/team/profile.md` | Documents compatible role fields, direct human accountability, Boolean amendment grant, mentality, and human/ruler/worker examples. |
| `.tfw/templates/journal/event.md` | Adds optional `writer` and separates principal, accountable human, tool, token, and historical `actor` semantics. |
| `.tfw/templates/bindings.yaml` | Allows a single external project mapping to select a human or valid agent principal while granting nothing. |

## 2. Key Decisions

1. A principal is a stable project-local profile handle, never a provider, model, executable,
   process, session, or workflow role. This preserves attribution across tools and sessions.
2. Agent accountability is one direct edge to an existing human. The Boolean grant records exactly
   two later-consumable levels, but Phase B creates no routing or permission behavior.
3. A grant is part of the principal's durable identity. Changing it requires a new handle/profile,
   so historical acts never acquire retroactive authority.
4. `writer`, `on_behalf_of`, `via`, and the filename token remain orthogonal. Legacy `actor` stays
   readable byte-for-byte and is never issued under the current contract.
5. The binding remains one external attribution selector. It gains no authority, runtime, liveness,
   fallback, device, or provider surface.

## 3. Acceptance Criteria

- [x] AC-1 — compatible optional organization/project role context and unchanged four-key humans.
- [x] AC-2 — accountable agent principals, exact two-level stable grants, and descriptive mentality.
- [x] AC-3 — current human/agent writer composition with unchanged legacy actor corpus and no blocking reporter path.
- [x] AC-4 — one-job external binding selects a declared principal and grants nothing.
- [x] AC-5 — four-path/Phase B boundary, Phase A and D79 compatibility, attention limits, and all configured checks hold.
- [x] AC-6 — approval, Baseline, Candidate, selector, arithmetic, trigger, authority, and timing replay exactly.

## 4. Verification

- Lint (`python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only`): PASS — 630 tests collected.
- Tests (`python -m pytest .tfw/scripts/ docs/scripts/ -q`): PASS — 629 passed, 1 skipped in 319.54 s.
- Contract fixtures (`$validator | python -`): PASS — 17/17 expected accept/reject outcomes.
- Project structure (`python .tfw/scripts/gen_index.py --check project`): PASS.
- Documentation (`python -m mkdocs build --config-file docs/mkdocs.yml`): PASS in 112.70 s; existing historical-reference and third-party advisory warnings only.
- Diff hygiene (`git diff --check <Baseline> <Candidate> -- <four VALUE paths>`): PASS.
- Report-only task diagnostic: unchanged Baseline→Candidate; the sole foreign RDP 123/120 summary warning remains disclosed and non-gating.

### Round 2 Verification

- Preserved-program replay: PASS — the fenced EV program was extracted and piped to Python; 17/17
  documented outcomes passed with exit 0.
- Recorded-output parity: PASS — 21 actual lines equal the 21-line EV output block; delta 0.
- External-state boundary: PASS — both documented real binding paths remained absent.
- Candidate immutability: PASS — Candidate exists and is an ancestor; Candidate→HEAD and
  Candidate→working-tree diffs over the four VALUE paths are empty; later VALUE commit count is 0.
- Historical provenance: intentionally not reconstructed. The precise first-round validator bytes
  and complete pre-commit shell transcript remain unavailable and are not attributed retrospectively.

## 5. Evidence

See [EV file](evidence/EV__phase-b__named_principals.md) for evidence details.

Evidence verdict: 6/6 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

### Round 2 Evidence Summary

Current cumulative evidence verdict: **7/7 rows VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A**. See
[EV Round 2](evidence/EV__phase-b__named_principals.md#round-2--preserved-executable-validator-evidence)
for the complete executable program, all 17 full YAML payloads, the exact extraction command, fresh
17/17 output, and output-parity check. This resolves the current reproducibility obligation for
AC-1, AC-2, and AC-4. It does not revise the first-round submission or claim that the now-preserved
program was the unrecorded historical pre-Candidate program.

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|---|---|---|---|
| 1 | `workspace/2026/TFW_20260902-111644_CRATM/HL-TFW_20260902-111644_CRATM.md` | 738, 740 | naming | The quoted principles are correct, but the source ordinals have drifted: “Human authority, bounded delegation” is now NS2 principle 5 rather than 4, and “Assurance proportional to risk” is now principle 7 rather than 6 (`.tfw/README.md` lines 86 and 88). Phase B B1 uses the current Human Authority ordinal. Correcting the frozen master citation is outside Executor authority. |

## 7. Fact Candidates

No fact candidates.

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

No diagrams.

---

*RF — TFW_20260902-111644_CRATM / Phase B: Named principals | 2026-09-06*
