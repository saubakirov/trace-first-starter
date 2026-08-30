# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | Eight of nine AC checkmarks hold against files and re-run commands (verify.md V1–V25, commands 1–8). **AC-2 bullet 1 is not met as written**: `migrate_board.py`:750 prints `**Unaccounted: 0.**` as a constant while the computed form stands eleven lines lower — the TS says "computed … or deleted. Not both left standing" (verify.md D1). **AC-6** holds on every bullet, but the rewrite that met it introduced a false statement — "Both temporary directories are gitignored" — twice (D2). Both are one-line fixes; neither touches the architecture. AC-8 release is DEFERRED to `/tfw-release` by TS revision 2 and §15 — correct, not a gap |
| 2 | (a) Purpose Check · (b) Design soundness | ✅ | **(a)** see field below. **(b)** Sound against §7 at the baseline: P1 — the fixture reproduces the real pain (`HD-30b`), and the fix is the cause (an unanchored search), not a fourth pattern; P4 — three grammars coexist, no directory moves (`four_corpora_compatibility.txt`, DoD 10); P5 — the manifest computes and discloses what it did not check; P9 — `_plain()` keeps identifier bytes; P10 — canon, templates, both workflows, six adapter copies, compiler and migration guide ship together. One dispatcher for three consumers (F11) rather than three regexes. The gate runs before the manifest is opened, stricter than revision 1 asked. No trace of a catch-all |
| 3 | Tech debt documented | ✅ | RF §6 present with four typed rows; each names file, lines and why it was filed rather than fixed (budget/ownership) |
| 4 | Style & standards | ✅ | Commit subject `[codex/TFW-60/phase-ab/executor] implement honest migration` follows §4 grammar; RF follows the template with §7–§9 present; event carries `on_behalf_of` + `via`; TFW-55 dirty files excluded from the commit; English content per `content_language: en`. **Minor:** the phase journal has no event for execution → RF (`status.md` `updated: 173155` has no entry behind it). Not a block; the REVISE round's re-entry event should say so |
| 5 | Observations collected | ✅ | O1–O4 are real: two stale `KNOWLEDGE.md` statements about the current grammar and the event suffix; a template that contradicts itself about who `team/` holds; an adapter source demanding a `{version}` substitution that put "TFW 0.8.5" in a consumer for two releases; an event template still defining `via` as an enumeration the canon just declared free-form. No filler. All four promoted below |
| 6 | RF completeness (§7-9) | ✅ | §7 "No fact candidates" with a reason — accepted: the human rulings of this phase (grammar lands now, no fourth external run, `HD-30b` closed, ABBR `ABT`) are already in HL §12 A5, TS §2 and ONB answers. §8 "No strategic insights" — accepted for the same reason. §9 diagram present and accurate to the code path (dispatcher → duplicate gate → partitions → guarantees → manifest → `--apply`) |
| 7 | Evidence completeness — does the evidence **exist**? | ✅ | EV file present with environment header, nine rows covering every TS AC gate, verdict line; five attachments exist and are indexed. Statuses drawn from the vocabulary; the one DEFERRED names its blocker (verify.md Evidence Verification) |
| 8 | Evidence sufficiency — does the evidence **establish the claim**? | ✅ | Green signals and what they establish: 283 tests re-run here establish the regressions; the inline reproduction of HELPDESK_SHAPE establishes parse-whole and prose fidelity independently of the executor's transcript; the deliberate `TFW-9` refusal establishes that the gate names guarantee and identifier; `exit 128` establishes the missing-tag stop; sha1 triplets establish adapter parity; the 53-task count establishes this corpus's compatibility claim. **Two limits, stated rather than hidden:** the three external corpora were verified on the stated method, not re-opened; E3's collision clause is a transcription of the rule — no second creation was attempted, and none could be, since the creation path is agent-executed prose. The EV should say "verified as text" there. Neither limit weakens an AC gate |
| 9 | Backward compatibility | ✅ | Consumers: three external projects on `2.0.0-dirty` grammar — every identifier still parses to the same kind and value (E1); no rename; `gen_docs.py` still resolves `PREFIX-N` and now `YYYYMMDD-HHMMSS__slug` too, which it previously did not. Retired config keys are named by `--check project` rather than silently ignored. `sort_key` for clock tasks changed shape (`(1, stamp, slug, "")`) — order preserved, tests pass. **One gap to file:** `conventions.md` §4 *Artifact file naming* has no example for the current grammar and its no-title rule is stated only for clock tasks; the AC-3 fixture appended `__approved_fixture` to an HL filename the status template says has no suffix. A new-grammar task's artifact names are undefined by the text |
| 10 | Safety | ✅ | No secrets, no credentials. Refusals happen **before** any output path is opened (`require_guarantees` in `plan()` and at the head of `render_manifest()`; duplicate-row test asserts the manifest file does not exist). External consumer worktrees were read at pinned commits and never written; the disposable `ABT` fixture was created in a temporary repository and discarded. Nothing here can destroy or rewrite a trace |

## Purpose Check — row 2 clause (a)

**Reference set:** master HL at `810b1b8` — §4 Phase AB declared outcome and deliverables 1–8, §5 DoD 10 and DoD 20, §6 DoF 8 — plus `.tfw/README.md` NS1.

**Field:** The result serves DoD 20 at the baseline — *"a migration tool refuses input it cannot parse whole rather than matching a prefix and discarding the remainder; it computes every invariant it asserts and names which guarantees were checked; and it preserves identifier characters in migrated prose while stripping only markup"* — and NS1 — *"another authorized person or agent can … inspect its material grounds and current result"*; the concrete harm it removes is the one A5 records: a completed, shipped task written back to `TODO` in a real project while the manifest asserted "Unaccounted: 0", three confident false statements with no warning.

**Three tests:**
1. **Excess and adjacency** — no. Every deliverable maps to baseline §4 AB 1–8: parse-whole (1), computed guarantees (2), the grammar with owner-approved abbreviation (3), prose fidelity (4), test separation (5), source quiescence (6), provenance drift (7), reachable checks (8). The `via` decision and the `update.md` word ceiling are debt items closed inside files the phase opens for 6–8; they add no capability the baseline does not name. `KNOWLEDGE.md` was left alone (D37). No consumer was retrofitted (phase boundary). `HD-30b` was not repaired (owner ruling; class not instance).
2. **Deferral confession** — the spec names `/tfw-release` as the home of VERSION, CHANGELOG and tag, and the result did **not** ship them here. That is the confession honoured, not violated.
3. **Materiality** — yes. The harm is silent reassignment of task state (a DoD 10 violation), not wording.

**Outcome: Aligned — ✅.** The two REVISE items in row 1 are the phase's own standard applied one layer in: a printed constant and a false sentence, each fixable in a line. Neither is a purpose failure and neither is a contract defect — DoD 18 (offline participants cannot collide) and the new grammar read together without tension: same second **and** same owner-approved abbreviation is one owner approving one name twice, and validation names both paths if it ever happens.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D68 — "A current task identifier is the whole `YYYYMMDD-HHMMSS__slug` directory name, and a current event name includes its actor" | Current grammar is `PREFIX_YYYYMMDD-HHMMSS_ABBR`; the event suffix is an opaque token since `2.0.0-dirty.3` | **Yes — known.** RF O1; D37 reserves the fix for `/tfw-docs` after approval. Not the executor's |
| 2 | §3 Legacy row 2 — same two statements | same | **Yes — known.** Same route |
| 3 | D54 — Codex skills are thin routers, no workflow body | `.agents/skills/` verified byte-identical to adapter source, not rewritten | No — the executor followed D54 and the coordinator withdrew the TS line that would have broken it |
| 4 | D59 — declared attribution ≠ authentication | `via` free-form, validated only as non-empty | No — this is D59 applied |
| 5 | D65 — reverting a result never reverts its trace | no directory renamed; malformed inputs reported, not repaired | No |

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Every `⚪ N/A` carries a stated reason — no row skipped as a bare ✅? — no N/A used
- [x] Row 2(a): answered against the contract baseline `810b1b8` and NS1 — never the TS or the Phase HL — with a quoted clause **and** a named harm in one field?
- [x] Rows 7 and 8 answered separately, with different reasoning? — 7: everything exists; 8: what each green signal establishes and two stated limits
- [x] Referenced verify.md findings in DoD assessment? — D1, D2, V1–V25, commands 1–8
- [x] Checked RF §7-9 for presence AND quality? — both empty sections carry reasons that hold; the diagram matches the code
- [x] KNOWLEDGE.md cross-referenced — contradictions documented? — two known, routed to `/tfw-docs`
- [x] Fact Candidates from RF reviewed — any that need challenge? — "No fact candidates" challenged and accepted: nothing human-only was said this phase that HL §12 A5, TS §2 and the ONB do not already carry

Stage complete: YES
