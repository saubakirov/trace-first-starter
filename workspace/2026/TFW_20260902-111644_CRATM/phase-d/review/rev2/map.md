# Map rev2 — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase D](../../RF__phase-d__team_mode_and_role_assignment.md)
> TS: [TS Phase D](../../TS__phase-d__team_mode_and_role_assignment.md)

## Understanding

This bounded recheck leaves Candidate `9edbebcf68872a72a9274765ad053e8d25fa66ac` and the completed
Phase D closure unchanged. It reopens only the relationship among the approved TS's profile-admission
rules, the implemented provider-neutral canon, the supplied Codex adapter profile, and the assurance
that claimed AC-1 and AC-4.

The approved TS defines two admission cases. Its supplied initial Codex profile carries a disclosed
G1–G7 evidence limit without a G8 reliability claim, while any additional provider profile must pass
all eight gates in one native run (TS lines 78–82, AC-1 lines 277–278, HC-D3 line 253, AC-4 lines
348–360). The implementation supplies that limited Codex profile in the adapter, but canon says
without qualification that “A profile joins only when one provider-native unit passes all eight gates
in one trial” (`.tfw/conventions.md:824`).

## TS ↔ RF Alignment

| TS requirement | RF claim | Source mapping |
|----------------|----------|----------------|
| AC-1 — complete neutral gate plus explicit evidence limitation for the shipped initial profile | RF §§1, 3 and EV E1 claim the neutral gate and source-derived tests | Canon contains all eight gate headings and the one-trial/no-partial rule; adapter contains the limited-profile disclosure; assurance parses those facts independently and has no combined admission decision |
| AC-4 — supplied Codex profile is bounded and makes no G8 reliability claim | RF §§1, 3 and EV E4 claim the adapter and operational trace establish mechanics only | Adapter and `phase-d-native-profile.json` disclose G1–G7 support and uncontrolled G8; current canon's universal admission sentence has no supplied-profile exception |
| HC-D3 — every non-supplied profile needs one complete native eight-gate run | RF §§3–4 and EV E1/E4 claim complete gates plus no second-provider profile | Current canon enforces the all-eight condition for additional profiles, and the protected/census evidence shows no additional profile |
| AC-5 — source-derived positive, negative, and output-changing mutant assurance | RF §§3–4 and EV E1/E5 claim scenarios and 45 mutants | Existing scenarios exercise AT declaration/activation rather than profile admission; native mutants remove gate headings one at a time; no case distinguishes the supplied initial exception from an additional profile |

## Deviations from TS

- The canon's admission subject is universal (“A profile”), whereas the approved TS distinguishes the
  supplied initial profile from every additional profile.
- The adapter and native evidence instantiate the supplied profile with G1–G7 evidence and no
  controlled G8. Read under the universal canonical sentence, that supplied profile cannot join even
  though the TS says it may proceed at the disclosed limit.
- Assurance verifies the canonical all-eight text and adapter evidence-limit text as separate booleans.
  It contains neither a positive supplied-profile admission case nor a negative additional-profile
  admission decision, so their incompatibility does not change an existing test output.
- No later product edit caused the mismatch: Candidate→closure tip is byte-identical for the two
  product sources and two assurance modules involved in this recheck.

The prior REVIEW's two diagnostic dispositions and Coordinator closure corrections are separate from
this source relationship and remain unchanged.

## Checkpoint

**Self-check:**
- [x] Read RF §1–§5 completely?
- [x] Read TS DoD and matched the bounded AC-1/AC-4/AC-5 items to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES
