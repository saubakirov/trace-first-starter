# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-56](../../HL-TFW-56__review_mode_removal.md)
> Goal: Review stops asking which kind of review this is — the `code / docs / spec` axis is deleted and the two checks inside it that ever carried signal are promoted into the universal checklist.

> **Headline:** the eight mode rows are not eight checks. Read by what they *found* rather than by
> what they are *called*, four of them are **one check wearing three genre costumes** — and it is the
> highest-firing check in the entire mechanism. The HL's promotion list names a narrow version of it
> ("claims traceable to sources") that misses its largest instance.

---

## E1 — The coverage matrix (H1, H2)

8 mode rows × 7 universal rows. Cell values: **D** duplicate · **P** partial · **·** absent.
Universal rows as they stand in `templates/review/judge.md`:
U1 DoD met · U2 Philosophy aligned · U3 Tech debt documented · U4 Style & standards ·
U5 Observations collected · U6 RF completeness §7-9 · U7 Evidence completeness.

| Mode row | non-✅ | U1 | U2 | U3 | U4 | U5 | U6 | U7 | Residue — what no universal row holds |
|---|---:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|
| Test coverage | **23.4%** | P | · | · | · | · | · | P | **Does the evidence bear on the claim?** U1 asks if the AC is met, U7 asks if evidence *exists*. Neither asks whether green tests test the thing |
| Analytical quality | 25.0% | · | P | · | P | · | · | P | **Is the method sound / are self-declared gates honest?** |
| Source attribution | 22.2% | · | · | · | · | · | · | P | **Do the cited sources support the claim?** |
| Source verification | 12.5% | · | · | · | · | · | · | P | same as above |
| Breaking changes | 8.5% | · | · | · | · | · | · | · | **Compatibility with existing consumers** — absent from all seven |
| Content quality | 5.9% | P | · | · | **D** | · | · | · | ~none — U4 covers clarity/tone |
| Code quality | 4.5% | · | P | · | **D** | · | · | · | **Design soundness** — U4 is naming/conventions; the 6 ❌ are contract violations |
| Security | 4.0% | · | · | · | · | · | · | · | **Safety** — absent from all seven |

**H1 verdict: refuted as stated, and the correction is not "more rows".**
The HL says three checks are absent (compatibility, source traceability, safety) and five are
covered. The matrix says **five** have residue, not three — but two of the five newly-surfaced ones
(Test coverage, Analytical quality) turn out to be the *same* residue as the two the HL already
identified. Collapsing by residue rather than by name gives **four**, not three, and not eight.

**H2 verdict: confirmed.** Line-by-line against the three mode files:

| Mode verify action | Already mandated unconditionally? | Where |
|---|---|---|
| `code` 1 · `docs` 1 · `spec` 1 — open `min_verify_ratio` of files, escalate on discrepancy | ✅ yes | `review.md` Verify step + `verify.md`; identical text in all three mode files |
| `code` 2 — re-run ≥1 build/test command | ✅ yes | `verify.md` Checkpoint |
| `code` 3 — cross-reference RF §3 checkmarks against TS DoD | ✅ yes | `verify.md` TS↔RF section; judge U1 |
| `code` 4 — if "Tests pass" claimed → check test file exists | ✅ yes | `review.md` Trust Protocol row |
| `docs` 2 — check document structure matches spec | ⚠️ **partial** | Nothing mandates structural conformance; U1 covers it only if the TS wrote an AC for it |
| `docs` 3 — spot-check 2-3 key claims/sources | ❌ **no** | This is the *action* behind the Source-verification residue. Not in `verify.md` |
| `spec` 2 — check citations traceable to real artifacts | ❌ **no** | same residue |
| `spec` 3 — verify data claims against primary sources | ❌ **no** | same residue |

The HL asserts H2 on the strength of `code`'s two actions and never enumerates `docs`/`spec`.
**Three docs/spec verify actions have no unconditional home.** They are not checklist rows — they
are Verify-stage actions, so promoting a judge row does not rescue them. DoF-1 is live here.

## E2 — The unexpected combination: four rows are one check in three genres

Read the Evidence cells of the non-✅ rows rather than the row titles. The findings converge:

| Row | Genre | An actual finding |
|---|---|---|
| Test coverage | code | *"All large suites pass, but the acceptance contract is green with a compiled forbidden production collector"* |
| Test coverage | code | *"1577 JVM/server + 72 Android are green, but the defining constructor bypass is untested and invisible to the current pin"* |
| Analytical quality | spec | *"Собственные completeness gates отмечены зелёными при невыполнении"* |
| Source attribution | spec | *"Один primary-source claim неверен, восемь source bindings отсутствуют"* |
| Source verification | docs | *"Security/source samples pass, migration and changeset source checks fail"* |

Every one is the same shape: **the artifact carries a green signal, and the green signal does not
establish the claim.** In code it is a passing test that tests the wrong thing; in spec it is a
self-declared gate marked green while unmet; in docs it is a citation that does not support the
sentence. The genre changes the *instrument*; the check is identical.

Combined firing rate of the four: **28 non-✅ in 174 rows = 16.1%** — well above both the mode
average (10.2%) and the universal baseline (9.4%). **This is the most productive check TFW's review
has, and it currently exists only as three genre-specific fragments behind a gate.**

The HL's promoted row — *"Claims traceable to sources"* — captures the docs/spec fragments and
misses the code fragment, which is the largest one (141 of the 174 rows). Promoting the HL's wording
would carry ~35% of the signal and drop the rest, which is DoF-1 in the precise sense the HL defines
it: *coverage loss disguised as simplification*.

**Corrected survivor set — four rows, by residue:**

| # | Promoted row | Absorbs | Evidence rate |
|---|---|---|---|
| **S1** | **Evidence bears on the claim** — does the proof offered actually establish what it is offered for? (green tests that test the thing · cited sources that support the sentence · self-declared gates that were truly met) | Test coverage · Analytical quality · Source verification · Source attribution | **16.1%** (28/174) |
| **S2** | **Backward compatibility** — do existing consumers survive? (APIs, wire shapes, migrations, doc anchors, renumbered template sections) | Breaking changes | 8.5% (12/141) |
| **S3** | **Design soundness** — does the implementation honour the contract it claims, beyond naming and style? | Code quality residue | 4.5% (7/155) — but 6 of 7 are hard ❌ |
| **S4** | **Safety** — explicit N/A permitted (F21) | Security | 4.0% (6/150) |

Dropped as genuine duplicates: **Content quality** (U4 Style & standards — the sole ❌ in 17 rows
is a content-accuracy finding that S1 also covers).

S3 is the one I would flag as contestable: its residue overlaps U2 *Philosophy aligned* (HL §7
principles), and four of its six ❌ are arguably principle violations. A coordinator could defend
folding S3 into U2 by sharpening U2's wording rather than adding a row. **That decision belongs to
the TS, not to research** — but it must be made consciously, because leaving it implicit is how six
❌ findings lose their home.

## E3 — Configuration Space

Seven options × the six Gather dimensions. Not evaluated here — elimination is Challenge's job.
D1 substance · D2 firing · D3 priming · D4 consumers · D5 extension · D6 generality.

| Config | What it is | D1 | D2 | D3 | D4 | D5 | D6 |
|---|---|---|---|---|---|---|---|
| **C1** | **Delete, promote HL's 3 rows** (the HL as frozen) | assumes 3 absent | assumes ~0 firing | assumes Alt A | Alt A | Alt A | Alt B |
| **C2** | **Delete, promote corrected 4 rows** (S1-S4, S1 reworded to cover code) | 4 absent by residue | 16.1/8.5/4.5/4.0% | assumes Alt A | Alt A | Alt A | Alt A |
| **C3** | **Delete axis, promote 4 rows, migrate the 3 orphan verify actions into `verify.md`** | as C2 + Verify layer | as C2 | Alt A | Alt A | Alt A | Alt A |
| **C4** | **Project-optional axis** — keep mechanism, `default_mode: none` disables it | unchanged | unchanged | Alt B | Alt B | Alt B | Alt B |
| **C5** | **Non-gated descriptor** — no file, no key, no WAIT; one free-text line in the header (the HL's H6 fallback) | rows still lost unless paired with C2/C3 | n/a | Alt B | Alt A | Alt A | Alt A |
| **C6** | **Extend the enum** (`prompt`/`design`/`architecture`) | +2 synonym rows each | untested | Alt B | Alt A | Alt C | Alt C — violates F13 |
| **C7** | **Replace genre with rigour** — delete `code/docs/spec`, and let the header declare *verification depth* (the variable the field actually writes there), bound to the surviving `min_verify_ratio` | as C2 needed separately | n/a | Alt B via a different label | Alt B — touches the key the HL keeps | Alt A | Alt A |

**C7 is the combination nobody proposed**, and it comes straight out of G6 rather than from
invention: 8 of the 13 free-text qualifiers reviewers wrote into the mode field encode *how hard they
looked* (`full mode — §6 guardrail`, `abbreviated — full codebase verified by AFD-6`, `Round 3`,
`89,6% LOC-budget`), not *what genre it was*. The field is already being repurposed. C7 says: the
axis was measuring the wrong variable, and the right one already has a config key.

C7 is **not** a recommendation — it enlarges scope, touches `min_verify_ratio` (DoF-4 territory),
and is a design proposal that belongs in an HL amendment or a sibling task, not smuggled into a
deletion. It is recorded because the Configuration Space exists to make it visible.

**Excluded as obviously contradictory:** multi-select (HL §10 already shows it converges on a union
= one universal checklist reached via a gate; G6's six field instances confirm reviewers do this
anyway) and "leave it alone" (the stale `config.md` pointers and the wrong `default_mode: code`
default are real costs nobody defends).

## E4 — What the numbers do and do not license

The HL's argument has two claims stacked on one measurement. They must be separated, because
**one survives and one does not.**

| Claim | Status | Evidence |
|---|---|---|
| *"The mode rows produce no findings"* | ❌ **false** | 65 non-✅ in 637 rows across 203 reviews; 10.2% vs 9.4% universal baseline; all 8 rows fire; no decay over 5 months; 28 of 63 tasks; ≥9 reviewer identities |
| *"The mode rows never changed a verdict"* | ✅ **true** | 0 of 203 reviews had a mode row as the sole non-✅. Every REVISE with a mode failure had ≥1 universal failure (median 4) |
| *"Therefore the axis can be deleted with 3 promoted rows"* | ⚠️ **does not follow** | The rows fire; the findings mostly have no other home (62/65 lexically distinct — an upper bound, but not zero); the promotion list is mis-specified (E2) and the docs/spec verify actions are orphaned (E1) |

The base-rate argument the HL borrows from TFW-53 Phase C is about **stages**, and the transfer is
not clean. A stage costs a 🛑 WAIT and a file load whether or not it finds anything; a checklist row
costs one line in a table the reviewer is already filling. **The base rate that justifies killing a
stage does not, at the same value, justify killing a row** — the denominators are different. And
here the base rate is not even low.

What genuinely survives from the HL, and it is substantial:
- The **gate** is unjustified — 0 verdict flips means the 🛑 WAIT buys nothing.
- The **three mode files** duplicate `verify.md` in their first action and are byte-identical across
  three installs — pure maintenance cost (G5, H5).
- The **config key** is wrong-by-default in this repo and routed by three stale pointers.
- **`docs` and `spec` are synonyms** — confirmed: their four rows collapse into one residue (S1).
- The **`Mode:` template fields** carry no behaviour once the gate is gone.

That is a real and defensible task. It is just **not the same task as "the rows never fired"**.

## E5 — H4's residue: the removed-key gap

`update.md` categorises files, never keys. A framework key deleted upstream is invisible to its
🟢/🟡/🔴 triage, so an existing project keeps `tfw.review.default_mode: code` indefinitely, pointing
at a workflow step that no longer exists. No corruption — but silent orphaning, and the same class of
stale-pointer debt as TD-106, which this task exists partly to close.

Two options for the TS, both cheap:
- **(a)** CHANGELOG `### Removed` entry naming the *key*, plus one line in `update.md` Step 3
  extending 🔴 to removed config keys. Generalises past this task.
- **(b)** Task-local migration note only. Cheaper, leaves the framework gap for the next removal.

Also recorded and **out of scope**: `min_verify_ratio` sits in the `tfw.review` block that update.md
marks *framework → update*, so a project that tuned it loses the tuning on any upgrade. Pre-existing,
not caused by this task → tech-debt candidate.

---

## Checkpoint

| Found | Remaining |
|-------|-----------|
| **Four rows are one check in three genres** — evidence-bears-on-claim, 16.1% firing, the most productive check in TFW review. The HL's promoted wording captures ~35% of it | Exact wording and N/A grammar for S1 — TS/HL work, not research |
| **Corrected survivor set is 4 (S1-S4), not 3** — and S3 (design soundness) is contestable against U2, which is a decision the TS must make explicitly | Whether S3 becomes a row or a sharpening of U2 |
| **H2 has a hole the HL never checked:** three `docs`/`spec` **verify actions** have no unconditional home. Promoting judge rows does not rescue Verify-stage actions | Whether they migrate into `verify.md` (C3) or are explicitly declined |
| **The two HL claims separate cleanly:** "rows never fire" is false; "rows never flipped a verdict" is true. The gate, files, key and `Mode:` fields are still defensible removals | Whether the owner accepts a re-scoped task — coordinator's call |
| **C7 surfaced:** the field is already being repurposed to declare verification *depth*, the variable `min_verify_ratio` owns. Recorded, not recommended | Out of scope for this HL; sibling-task candidate |
| **H4 residue:** `update.md` has no removed-key rule; silent orphaning, no corruption | (a) framework fix vs (b) task-local note — TS decision |

**Sufficiency:**
- [x] External source used? — LLM-judge rubric research (composite dilution, redundant-criteria degradation) applied to the promotion design; the 203-review external corpus underpins every rate
- [x] Briefing gap closed? — coverage matrix built and it corrected the HL rather than confirming it
- [x] Configuration Space built from Gather dimensions? — 7 configs × 6 dimensions, C7 unproposed before

Stage complete: YES
→ User decision: autonomous run authorised at briefing; proceeding to Challenge without a gate
