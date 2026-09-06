# Verify rev2 — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 18 implementation files (16 VALUE + 2 ASSURANCE)
> Files to verify: ⌈18 × 0.42⌉ = 8; verified: 18/18 Candidate blobs unchanged, plus 100% of the bounded admission sources, evidence, and assurance consumers.

## Verification Log

| # | Source | Claim under recheck | Actual | Match |
|---|--------|---------------------|--------|-------|
| V1 | Approved TS `6a7ede0549dca272c149b0294a972c013d5cb291`, lines 78–82 | Preserve the neutral eight-step contract; the supplied Codex profile carries the disclosed G1–G7 limit and no reliability claim; any additional profile needs all eight in one native run | Both distinct admission cases are explicit in the approved Git object and current TS | ✅ |
| V2 | Approved TS AC-1, lines 277–278 | The shipped initial profile's evidence limitation is explicit | This is a positive supplied-profile exception to the otherwise complete neutral gate | ✅ source requirement |
| V3 | Approved TS HC-D3, line 253 | Every non-supplied long-lived provider profile passes all eight gates in one unit before specification or dispatch | The hard constraint is expressly scoped to non-supplied profiles | ✅ source requirement |
| V4 | Approved TS AC-4, lines 348–360 | Codex profile is supplied and bounded; G8 reliability is not claimed | The adapter and native-profile evidence instantiate exactly that limited supplied profile | ✅ source requirement |
| V5 | `.tfw/conventions.md:822–835` | Implement the TS's admission distinction | Line 824 says universally that “A profile joins only” after all eight in one trial; line 835 says partial demonstrations never compose; no supplied-initial exception exists | ❌ |
| V6 | `.tfw/adapters/codex/AGENTS.md.template:20–22` and `AGENTS.md:46–48` | Supply the initial adapter profile honestly | Both say G1–G7 support mechanics and do not claim G8 reliability; managed-block parity holds | ✅ locally; incompatible with V5's admission precondition |
| V7 | `docs/scripts/test_runtime_context.py:3747–3793` | Source-derived AC-1 assurance | Parser separately checks eight headings, one-trial text, and no-partial text; it has no profile kind, supplied-profile exception, or admission-decision output | ❌ incomplete |
| V8 | `docs/scripts/test_runtime_context.py:3891–3919` | Source-derived AC-4 assurance | Adapter parser separately checks the G1–G7/no-G8 sentence, but never combines it with the canonical admission result | ❌ incomplete |
| V9 | `docs/scripts/test_runtime_context.py:4066–4068` and `phase-d-mutants.json` | Native admission mutants are sufficient | All eight `native-gate` mutants only rename one gate heading and expect `native-gates`; none makes the gate universal or accepts partial receipts | ❌ incomplete |
| V10 | `phase-d-native-profile.json` | Operational evidence supports the supplied profile without overclaim | The record says G1–G7 field-supported, G8 uncontrolled, no reliability rate, and mechanics rather than authority | ✅ evidence fact; under V5 it cannot satisfy canonical admission |
| V11 | Candidate→closure product lineage | Determine whether closure caused the defect | All eighteen Candidate VALUE/ASSURANCE blobs are byte-identical at closure tip `881f6e240db52e01bac1403cd4a807ddfde3172d` | ✅ defect is in Candidate; closure corrections preserved |
| V12 | `KNOWLEDGE.md` D82 | Check closure documentation for a competing admission rule | D82 says profiles describe mechanics, never authority; it does not state or resolve the supplied-versus-additional admission distinction | ✅ no competing source; does not cure V5 |

## Required Admission Cases

The expected decisions below are derived independently from the approved TS, not from the canonical
parser or adapter parser.

| Case | Source-derived fixture | Expected by approved TS | Current canonical result | Match |
|------|------------------------|-------------------------|--------------------------|-------|
| Positive — existing supplied profile | Supplied initial Codex profile; G1–G7 field-supported; G8 uncontrolled; limitation disclosed; no reliability claim | `ADMIT_SUPPLIED_LIMITED` | `REJECT_NO_G8` because line 824 quantifies over every profile | ❌ |
| Negative — additional profile without one native all-eight run | Non-supplied profile; partial receipts; no controlled G8/native complete unit | `REJECT_NO_NATIVE_G8` | `REJECT_NO_NATIVE_G8` | ✅ |

## Output-Changing Mutants

| Mutant | Baseline output | Mutant output | Changed? | Independent ruling |
|--------|-----------------|---------------|----------|--------------------|
| Make the intended admission gate universal | Positive supplied case: `ADMIT_SUPPLIED_LIMITED` | `REJECT_NO_G8` | ✅ | Rejected by TS lines 81–82 and AC-1 lines 277–278 |
| Let partial receipts compose for an additional profile | Negative additional case: `REJECT_NO_NATIVE_G8` | `ADMIT_FROM_PARTIAL` | ✅ | Rejected by TS line 82, HC-D3 line 253, and canon line 835 |

The first mutant reproduces the delivered canonical wording. The second confirms that correcting the
supplied-profile exception must not weaken the all-eight rule for any additional profile.

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | Exact `rg -n -C` source trace across TS, canon, adapter, RF, EV, and assurance | Resolved every cited clause and parser/mutant site |
| 2 | Read-only PowerShell source-derived admission probe | All five source facts resolved; positive expected/actual mismatch; negative match; both mutants changed output and were independently rejected |
| 3 | `git diff --exit-code <Candidate> HEAD -- <18 approved implementation paths>` | Exit 0; every Candidate VALUE/ASSURANCE blob remains unchanged at closure tip |
| 4 | `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q -k phase_d` | `8 passed, 1 failed, 285 deselected`; the eight admission-adjacent tests still pass despite V5–V9. The one failure is the post-review `KNOWLEDGE.md` closure write falling outside the test's Baseline→working-tree allowlist, not an admission result |

No full suite was run in this recheck. The source contradiction is dispositive, no correction has
been authorized or implemented, and the Coordinator/Main hold remains in force.

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | “The supplied Codex profile carries its disclosed G1–G7 evidence limit” | Approved TS lines 78–82; RF AC-4; EV E4 | Adapter line 22 and `phase-d-native-profile.json` | ✅ as a supplied-profile fact |
| C2 | “The provider-neutral eight-step admission gate is complete” | RF AC-1; EV E1 | Canon lines 822–835 and approved TS AC-1 | ❌ — all eight gate definitions exist, but the universal subject contradicts the TS's supplied-profile case |
| C3 | “45 output-changing mutants” establish admission behavior | EV E1; `phase-d-mutants.json` | Mutant source lines 4066–4068 and the JSON's eight `native-gate` rows | ❌ for this claim — those mutants establish heading completeness only, not supplied/additional admission decisions |

All cited files and immutable Git objects resolve. The data claims in this revision were recomputed
from the product sources, test source, JSON evidence, and Git objects rather than copied from RF text.

## Discrepancies Found

1. **Material Candidate/TS contradiction:** `.tfw/conventions.md:824` makes a complete native
   eight-gate trial a prerequisite for every profile, while the approved TS explicitly permits the
   supplied initial Codex profile at its disclosed G1–G7 evidence limit without a G8 reliability
   claim. The delivered adapter instantiates the limited case, so the shipped canon rejects its own
   only first-release profile.
2. **Assurance gap:** the tests validate the universal canon and the adapter limitation separately.
   They lack the required positive supplied-profile decision, negative additional-profile decision,
   and a mutant spanning the distinction; consequently eight bounded tests pass around the defect.
3. **Post-closure test-context observation:** one bounded integration test treats the required
   post-review `KNOWLEDGE.md` write as an unauthorized Baseline→working-tree path. This does not alter
   the Candidate contradiction and is not added to the proposed correction bound; the prior closure
   correction remains preserved.

Any discrepancy triggers 100% verification. The first review already opened all 18 Candidate files;
this revision verified their complete Candidate→closure byte stability and re-opened every source,
evidence item, and assurance consumer involved in admission.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | `evidence/EV__phase-d__team_mode_and_role_assignment.md` | ✅ | ❌ partial — E1 proves eight headings and existing mutants, but not the TS-required supplied/additional distinction |
| E2 | `phase-d-scenarios.json` | ✅ | ❌ for admission — scenarios cover AT declaration/activation and expose no profile-admission case |
| E3 | `phase-d-mutants.json` | ✅ | ❌ for admission — 45 rows exist and change output, but the native family checks heading omission only |
| E4 | `phase-d-native-profile.json` | ✅ | ✅ — accurately records G1–G7 mechanics, uncontrolled G8, and no authority/reliability claim; this is the positive fixture the canon mishandles |
| E5 | `phase-d-test-output.txt` | ✅ | ⚠️ — accurately records Candidate-time green runs, which did not exercise the missing combined rule |

The remaining accounting, parity, census, context, and protected-path attachments are not disputed
and remain as verified in the original review.

## Knowledge Citations Verified

The original same-Reviewer audit independently verified all 98 master/phase-HL/ONB citations across
PV priorities 0–4 and relevant P5–P7. All eighteen Candidate blobs remain unchanged. This revision
also re-opened current `KNOWLEDGE.md` D82 after `/tfw-docs`: the item exists and remains relevant, but
contains no admission exception capable of resolving the TS/canon contradiction. New source citations
in this revision resolve directly to the approved TS, research iteration 3, canon, adapter, evidence,
and assurance files.

Citation records retained: 98; resolved: 98; semantically verified: 98; irrelevant: 0;
hallucinated: 0. New bounded source citations: 6 source groups; resolved and semantically checked: 6.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈18 × 0.42⌉ files and recorded findings? — 18/18 Candidate blobs plus all bounded admission sources.
- [x] Ran at least 1 build/test command? — bounded source probe and Phase D pytest selection; no full suite before correction.
- [x] Claim & Source Checks filled — three load-bearing claims checked against primary sources.
- [x] Each bounded RF §3 checkmark verified against actual files? — AC-1/AC-4/AC-5 rechecked; one material contradiction found.
- [x] `KNOWLEDGE.md` checked — D82 does not resolve or worsen the admission contradiction.
- [x] Knowledge citations verified? — inherited 98/98 plus 6/6 bounded source groups.
- [x] Evidence artifacts verified? — all admission-relevant items opened; E1/E2/E3 are insufficient for the combined rule.

Stage complete: YES
