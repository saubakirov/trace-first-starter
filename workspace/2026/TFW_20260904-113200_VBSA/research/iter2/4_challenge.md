# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260904-113200_VBSA](../../HL-TFW_20260904-113200_VBSA.md)
> Goal: Replace repository-volume failure limits with reproducible VALUE-surface accounting, prospective scope decisions, and task-local hard constraints whose authority and evidence are explicit.

## Consistency Check

The comparison below tests the Extract configurations against the fixed-candidate rule, the four semantic classes, prospective authority, phase ownership, binary applicability, and approval-epoch compatibility.

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|---|---|---|---|---|
| D1 — applicability | LOC for every VALUE artifact | D3 — classification | Binary/non-text VALUE | Git reports binary numstat as `-/-`; inventing LOC would make the result neither replayable nor meaningful. |
| D2 — file-count meaning | Universal magnitude/risk proxy | D7 — hard-bound basis | Named material harm | Equal file weight cannot by itself establish effort, risk, value, or the protected harm. |
| D3/D10 — mixed role | Freehand line or hunk subtraction | D9 — existing carriers only | No maintained sub-file selector | A reviewer cannot replay an interpretive subtraction that the TS never declared. |
| D4/D5 — authority | Retroactive Coordinator acceptance | D5 — timing | Decision before added work | A post-act entry can disclose a deviation, but cannot be prospective authority. |
| D4 — authority | Coordinator decides a new deliverable or frozen target | HL role lock | Owner controls frozen intent | Necessary-constituent authority cannot create a separately accepted output, AC, phase, or frozen architecture/interface claim. |
| D6 — cross-phase | Count one shared-path delta in every phase | D1 — measurement | Exact per-phase result | Double attribution is not an exact decomposition of one repository delta. |
| D6 — cross-phase | Reconstruct semantic hunks after a combined commit | D9 — replay | Immutable refs plus path selector | The path-level contract cannot prove historical hunk ownership without a prior selector or separate candidate. |
| D7 — hard basis | Configured number alone | D5 — enforcement | Pre-write material stop | A default size number does not name harm, applicability, action, or waiver authority. |
| D8 — compatibility | Reinterpret every approved TS under new meaning | Trace immutability | No history rewrite | It changes the force of an already approved contract without its authority or amendment record. |
| D8 — compatibility | Infer old/new semantics from mutable current config | Reproducibility | Approval-epoch rule | Current config cannot prove which framework semantics governed an earlier approval. |
| D9 — carrier | RF supplies missing permission | D5 — timing | Prospective decision | RF is written after implementation and therefore can report but not authorize the work. |
| D10 — mixed role | Advance Candidate for excluded-only edits | D1 — fixed measurement interval | Last VALUE change | This recreates post-delivery self-invalidation by measuring TRACE or ASSURANCE churn after value was complete. |

**Surviving configurations:**

| Config | Applicability and signal | Classification and attribution | Authority and timing | Hard bounds | Compatibility and carrier | Verdict |
|---|---|---|---|---|---|---|
| X3 — planned-membership hybrid | Logical VALUE-file identity/cardinality always reported; text LOC only where applicable; absolute configured values stay soft | Whole path for an inseparable fixed diff; separate phase candidates, one path owner, or per-phase `INVALID` | Coordinator rules a necessary constituent before work; Owner rules new output/frozen change | M1–M6 admission test | Approval epoch; TS→RF→EV→REVIEW | **Survives**, with X12 overlay. |
| X4 — disclosure only | Cardinality only; no absolute trigger | Whole path; phase candidate | No threshold authority | Explicit task-local constraints only | Approval epoch; existing carriers | **Survives as fallback**, but loses a low-cost decomposition prompt already configured. |
| X5 — delivery-specific only | Domain measures only | Accepted-output component | Prospective Coordinator | Named harm | Forward change; existing carriers | **Eliminated** because it loses a universal, replayable path-membership check that exposed the missing TFW-27/A logo. |
| X6 — no numeric control | No numeric signal | Outcome mapping | Coherence judgment | Nonnumeric DoF only | Existing carriers | **Eliminated** because it cannot replay membership drift or applicable text magnitude. |
| X12 — zero-tolerance overlay | X3 soft signals | Whole measured path; separate phase candidates | Coordinator except frozen/external boundary | Exact zero-write/path/interface constraints may coexist with soft size triggers | Approval epoch; existing carriers | **Survives as part of X3**, not as a separate operating mode. |

X1, X7, X9, X10 and X11 fail direct incompatibilities above. X2 is superseded by X3 because its six-condition boundary lacks architecture/interface and prospective-timing tests. X8 is not selected as a default: a predeclared deterministic sub-file selector is allowed, but a new maintained hunk-accounting carrier is unnecessary and would add more trace than the problem warrants.

**Unexpected survivors:**

- **X3 + X12:** a task can use the same configured file/LOC values as soft disclosure/decomposition triggers while enforcing a hard zero-write, exact-path, external-interface, or migration boundary. “Soft” describes the defaults, not every task-local constraint.
- **X4 as fallback:** if an owner later removes absolute configured triggers, the mandatory planned-versus-actual membership result still preserves the most cross-domain part of file counting.

## Findings

### C1 — The non-code replay closes applicability without pretending that binaries have LOC

The completed TFW-27 Phase A delivery is the required immutable non-code/binary counterexample corpus:

| Replay element | Result |
|---|---|
| Baseline → Candidate | `e3f67e124c7c05a77003f1ca31260590b6f2569a` → `5108c25135f171be1a8f54ade4884a3219fd6e34` |
| Accepted phase | TFW-27 Phase A brand identity; historical REVIEW verdict `APPROVE` |
| Planned product paths | 6 |
| Actual Phase A VALUE paths | 7: five new and two modified |
| Applicable text magnitude | 288 additions + 42 deletions = 330 touched LOC |
| Binary VALUE | `logo.png`, `logo_header.png`, `favicon.png`; LOC = `N/A` |
| ASSURANCE / TRACE / DERIVED in combined candidate | 2 / 16 / 0 tracked paths |

The seventh VALUE path, `docs/brand/logo_header.png`, was omitted from the Phase A TS/RF affected-file lists but is necessary because `docs/mkdocs.yml` configures it as the theme logo. The planned-versus-actual VALUE membership comparison therefore found a real delivery omission even though 7 files did not approach the configured 14-file value. This supports file identity/cardinality as a universal soft signal for file-backed deliveries, while refuting any claim that count measures internal magnitude or that binary VALUE needs invented LOC.

Git's official diff documentation independently supports the representation boundary: `--numstat` uses `-` rather than line counts for binary files, while its file-based distribution mode counts each changed file equally. That makes file count reproducible but deliberately coarse: <https://git-scm.com/docs/diff-options>.

The combined Phase A+B candidate also validates all four classes without creating a fifth class: 11 VALUE paths (665 touched text LOC plus three binary `N/A` results), 2 ASSURANCE paths (155), 16 TRACE paths (1,943), and no tracked DERIVED paths; the text totals reconcile to 2,763. Ignored `site/` output remains DERIVED even though it is required for delivery verification.

**Challenge result:** Thread 1 is closed. Non-code/binary deliveries use the same VALUE/ASSURANCE/TRACE/DERIVED classification, with file identity/count retained and LOC explicitly `N/A` where not applicable.

### C2 — File count survives only as identity/cardinality and a soft prompt

Three possible meanings were attacked:

1. **Magnitude, effort, risk, or quality:** eliminated. A one-byte configuration file and a complex binary asset both count as one; neither consequence follows from cardinality.
2. **Configured absolute decomposition prompt:** survives weakly. It is cheap, already configured, and may prompt a useful split, but the TFW-27/A replay supplies no evidence that 14 is materially significant.
3. **Planned-versus-actual VALUE membership:** survives strongly. It is independent of text/binary format, exposes missing or unexpected accepted artifacts, and is replayable from fixed refs plus a selector.

Therefore the universal result is not “N files means too large.” It is:

```text
planned VALUE membership ↔ actual VALUE membership
actual logical VALUE files = new + modified paths in the fixed candidate
configured absolute value = soft decomposition/disclosure trigger only
```

The configured file trigger is not removed because no counterevidence shows it is harmful when it cannot fail the task. It must, however, never substitute for the membership comparison or a task-local materiality argument.

**Challenge result:** Thread 2 is closed. Logical VALUE-file count is a useful universal soft signal only for artifact identity/cardinality and membership drift; its absolute value is neither a universal hard limit nor sufficient evidence of scope risk.

### C3 — Five adversarial cases replace the original A2 boundary

| Attack | Proposed work | Who may decide before work? | Disposition | Why the original six conditions are insufficient |
|---|---|---|---|---|
| New deliverable | An implementation discovery could produce a separately useful/independently accepted manual, export, tool, or report | Owner through frozen amendment/new task or phase | Stop; do not treat it as an internal constituent | “Same goal” can still conceal a new accepted output and AC. |
| Mixed-role path | One fixed candidate diff contains necessary VALUE plus inseparable TRACE/ASSURANCE edits | Coordinator may classify the **whole path/diff as VALUE**; a narrower exclusion needs a deterministic TS selector | Count conservatively; no freehand line subtraction | Purpose is not reproducible below path level without a declared selector. |
| Late architecture | A newly discovered constituent changes a public interface, persisted-data model, security/trust/authority boundary, or frozen target architecture | Owner if a frozen claim changes; otherwise Coordinator revises TS prospectively and names affected stakeholders | Stop until ruling; architecture impact is explicit | An unchanged user-visible output can still hide a durable architectural or authority change. |
| Cross-phase reuse | A shared path is edited for two phases in one candidate | Coordinator must establish separate immutable phase candidates, assign the whole delta to one phase with dependency, or mark exact per-phase metric `INVALID` | No double counting or reconstructed hunk totals | “Same phase boundary” does not solve ownership when the evidence interval combines phases. |
| Retroactive discovery | Work was already added before a trigger/hard-bound disposition | No one converts it into prior approval; Coordinator records deviation, Reviewer adjudicates, Owner rules any frozen change | No retroactive waiver | A correct decision by the right role at the wrong time is still not authority for the performed act. |

NIST SP 800-53 CM-3 is useful counterevidence to a loose “record it later” model: it separates proposed-change review and approval, implementation of approved changes, retained decisions, and later monitoring. TFW does not import its control apparatus; it uses the same ordering distinction to keep authorization and evidence separate: <https://csrc.nist.gov/CSRC/media/Projects/risk-management/800-53%20Downloads/800-53r5/SP_800-53_v5_1-derived-OSCAL.pdf>.

The surviving authority rule is narrower than A2: Coordinator authority applies only to a necessary constituent of an existing accepted result that leaves goal, accepted outputs, AC, DoF, phase ownership, frozen target/architecture, public interfaces, persisted data, and security/trust/authority boundaries unchanged, and only when the live TS records the ruling before implementation. Ambiguous or already executed work does not satisfy the rule.

**Challenge result:** Thread 3 is closed. A2 should be superseded, not merely extended; the replacement adds architecture/interface/cross-phase tests and proof of prospective timing.

### C4 — Each link and each disposition field in the existing-carrier chain is irreducible

The smallest carrier chain remains TS §4/§5 → RF §1 → EV accounting row → REVIEW §2/§4. Removal tests produce these failures:

| Removed element | Failure introduced |
|---|---|
| TS Baseline/Candidate rule/Selector/Class reason | The measured surface can be selected after seeing the result. |
| TS configured triggers plus planned result | No reproducible crossing or membership-drift question exists. |
| TS hard tuple `{harm, subject/selector, metric+threshold, pre-write action, change authority}` | “Hard” becomes an unexplained number or an unenforceable warning. |
| TS disposition **cause** | The decision cannot be related to the discovery. |
| TS disposition **cost** | Acceptance hides the impact being traded. |
| TS disposition **assurance implication** | A split can silently reduce tests, review, or evidence. |
| TS disposition **split alternative** | The trigger becomes ceremonial because “accept” has no compared option. |
| TS disposition **authority + decision-before-work reference** | The record cannot prove the right role decided at the right time. |
| RF immutable Candidate and actual membership/result | EV cannot bind the calculation to what the Executor delivered. |
| RF deviation for missing/late ruling | Post-act prose can appear to repair unauthorized work. |
| EV exact replay and timing check | The executor's arithmetic and authority claim remain untested. |
| EV fail-closed status (`BLOCKED`; metric-only `N/A`) | Missing refs, binary LOC, or late decisions can be mistaken for a passing AC. |
| Reviewer rerun | The producer self-certifies the accounting. |
| REVIEW §2 discrepancy and §4 verdict | Evidence has no independent disposition; frozen changes cannot be rejected to the Owner. |

No extra accounting artifact survives the subtraction test. ONB may preserve the discovery question, but the live TS is the only prospective authority carrier. RF observes, EV demonstrates, and REVIEW adjudicates. `DEFERRED` is not terminal for a crossed hard constraint or triggered decision; `N/A` applies to a particular inapplicable metric such as binary LOC, not to the accounting AC.

**Challenge result:** Thread 4 is closed. The exact chain and minimum fields fit existing carriers; adding a registry, ledger, fifth artifact, or hunk-accounting record would duplicate authority or create maintenance drift.

### C5 — Hard constraints pass only when metric, harm, timing, and authority align

The M1–M6 test from Extract survived attack:

```text
M1 named material consequence
M2 approved object/risk protected
M3 directly applicable metric + selector
M4 exact pre-act evaluation
M5 reason soft trigger/split/evidence/review is insufficient
M6 named change/waiver authority
```

| Candidate | Attack | Surviving hard form |
|---|---|---|
| Zero writes to AFD, Helpdesk, history | File count/LOC would be indirect | Exact path selector + zero write operations before any mutation; Owner controls expansion. |
| AFD incident corrective containment | A generic LOC cap does not prove blast radius | Exact allowed product/test path set tied to the incident boundary; LOC remains soft unless separately justified. |
| External submission attachment cap | Repository file count may include non-submitted files | Count logical attachments under the exact package selector; external rule/Owner controls change. |
| Irreversible migration boundary | LOC/files do not observe data harm | Domain AC over named schema/partition plus rollback gate before mutation; not a universal scope metric. |

The counterexamples remain rejected: generic 50-file/5,000-LOC limits; reviewer preference; caps on tests, evidence, research, RF, REVIEW, or journal; binary LOC; a post-act threshold; and a bound copied from another task without its harm and authority. Any failed M1–M6 question makes the candidate soft or inapplicable. “Material” is therefore not a label the author may assert; it is the conjunction of six inspectable facts.

**Challenge result:** the first half of Thread 5 is closed with material examples and counterexamples that distinguish hard constraints from size preferences.

### C6 — Approval epoch is the only same-key compatibility rule that survives all histories

The exact forward wording from Extract was tested against four states:

| State | Required interpretation | Result |
|---|---|---|
| TS approved before the release | The semantics recorded by that TS and the framework at its approval commit remain authoritative | No retroactive relaxation or failure. |
| New TS approved after update in an existing project | Existing configured numbers become default soft VALUE triggers | New behavior applies without rewriting config. |
| Customized numeric values | Numbers remain exactly as configured; only default enforcement semantics change for new approvals | Local tuning is preserved. |
| New task requiring a material hard bound | TS states the full hard tuple; the same config key does not silently become hard | Authority and harm remain task-local. |

Inferring semantics from install history was rejected because installations move and current files are mutable. The recoverable epoch is the TS approval commit and the `.tfw/VERSION`/canonical rules at that commit. Adding a `mode` key was rejected because the assignment requires no replacement key and because it would create two competing project-wide interpretations. Rewriting old TS/RES/REVIEW artifacts was rejected as a trace-integrity violation.

**Canonical forward wording:**

> **Forward applicability.** Beginning with the TFW version that introduces value-bearing scope accounting, the values under `tfw.scope_budgets` are default soft decomposition and disclosure triggers for each TS approved under that version. They are calculated only over the applicable declared VALUE surface. The change does not amend, relax, or reinterpret an already approved TS, an explicit task- or phase-local hard constraint, or any historical measurement. Existing projects retain their configured numeric values. A governing TS makes a constraint hard only by naming its protected harm, subject and selector, applicable metric and threshold, pre-write enforcement action, and authority permitted to change it.

**Exact `CHANGELOG` `Changed` bullet:**

> **Scope-budget defaults become forward-only VALUE triggers.** The existing `tfw.scope_budgets` keys and each project's configured numbers remain unchanged. A TS approved under this release treats them as soft decomposition/disclosure triggers over applicable VALUE measures, not automatic failure limits. Any TS approved earlier and every historical result keep the semantics they recorded. A new TS may make a bound hard only by stating the protected harm, selector, metric, pre-write action and change authority. No task history is rewritten and no replacement key is added.

**Exact update-briefing text under “What you now do differently”:**

> For a TS you approve after this update, treat your existing scope-budget numbers as prompts to disclose and decide VALUE-surface growth. Keep every already approved TS and historical result under the meaning it recorded; state any new hard bound explicitly with the harm it protects and who may change it.

Semantic Versioning supplies a relevant publication constraint: released contents are immutable and public-contract changes are communicated through versioning. The appropriate release-number classification remains `/tfw-release` work, not a Researcher decision: <https://semver.org/>.

**Challenge result:** the compatibility half of Thread 5 is closed. Defaults change prospectively at the TS approval epoch; configured values and keys persist; approved contracts and history are not rewritten.

### C7 — Proposal and hypothesis disposition after attack

| Item | Challenge disposition |
|---|---|
| A1 (unapproved) | **Supersede.** Retain all configured values as soft prompts over applicable VALUE measures, but explicitly distinguish planned-membership drift from absolute file cardinality and admit hard constraints only through M1–M6. |
| A2 (unapproved) | **Supersede.** The six conditions are necessary but not sufficient; add frozen architecture/interface/persisted-data/security/trust/authority and cross-phase ownership boundaries plus prospective timing. |
| A3 (applied) | **Preserve.** Binary handling, `N/A`, logical rename/copy counting, and fixed refs survived the non-code replay. No new amendment is needed. |
| A4 (unapproved) | **Supersede narrowly.** Whole-path VALUE conservatism applies only to inseparable roles inside the fixed measured diff; no freehand sub-file subtraction and no Candidate advancement for later excluded-only edits. Phase attribution is separate. |
| H1 | **Confirmed with boundary.** Stable across all required corpora; fixed-path conservative ambiguity can overcount but is replayable. |
| H2 | **Confirmed.** ASSURANCE/TRACE/DERIVED remain mandatory where required and outside value-size arithmetic. |
| H3 | **Confirmed with condition.** Existing carriers suffice when candidate and phase ownership are explicit. |
| H4 | **Refuted as written.** A universal hard interpretation is not operational; the planned-membership + applicable-magnitude hybrid is. |
| H5 | **Confirmed.** All required replays preserve genuine VALUE growth while removing excluded-role self-reference; TFW-27 adds the binary/non-code case. |

## Checkpoint

| Found | Remaining |
|---|---|
| TFW-27/A closes the non-code/binary replay with 7 VALUE paths, 330 touched text LOC, and three binary `N/A` results. | None for applicability; delivery-specific quality measures remain TS/AC work, not a universal registry. |
| Universal file counting is useful for identity/cardinality and membership drift, not magnitude or hard failure. | None. |
| All five authority attacks require a prospective decision tree; original A2 does not survive unchanged. | None. |
| TS→RF→EV→REVIEW is irreducible and sufficient using current carriers. | None. |
| M1–M6 distinguishes hard constraints from preferences; approval-epoch wording handles old/new/customized histories with no rewrite or key. | Release-number classification remains deliberately assigned to `/tfw-release`, not another research iteration. |

**Sufficiency:**
- [x] External source used? Official Git and NIST documentation plus SemVer publication rules were used as countermodels, not imported wholesale.
- [x] Briefing gap closed? All five Iteration 2 threads are answered.
- [x] Pairwise incompatibility checked? Incompatible pairs and surviving configurations are listed.

**Subtraction result:** X3 with the X12 hard-bound overlay is the smallest surviving configuration. It uses no new class, key, registry, artifact, or historical rewrite. X4 remains a coherent lower-control fallback, but the evidence favors retaining the already configured absolute values as non-failing prompts.

Stage complete: YES
→ User decision: The owner's Iteration 2 assignment authorizes synthesis into RES; no further research iteration is recommended.
