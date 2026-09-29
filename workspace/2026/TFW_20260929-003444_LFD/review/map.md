# Map — "What must be true?"
> **Mindset:** Experienced newcomer. Understand the accepted result before judging it.
> **Test:** "Can I name the material claims, harms, boundaries, evidence identities and limits?"
> RF: [RF__TFW_20260929-003444_LFD.md](../RF__TFW_20260929-003444_LFD.md) at `b9a7ae57141fa0ebb99ba48d2d510119f1dbbb07` (lifecycle `RF` at `98b1a35efcd97d7859d54ddd9828dca6647d7dca`)
> TS: [TS__TFW_20260929-003444_LFD.md](../TS__TFW_20260929-003444_LFD.md), approved by the owner in gate answer 02ae (freeze `49703481e1b02ac725428dfd8da19c4d7c954c86`), amended in place at `4d1f5efda6a7dea8ba4dc170ccccd8d75e5f18b6` and `975fed5fac6f2ed2ae47af646907636a67b3dc82`; unchanged since
> HL: [HL-TFW_20260929-003444_LFD.md](../HL-TFW_20260929-003444_LFD.md), frozen at `975fed5fac6f2ed2ae47af646907636a67b3dc82`; the only later change (`ce30a943`) is the free "Material handover" section
> Accepted subject: Candidate `0b755dcada76fe0f22bf285a77b40f812c365c45` on branch `lfd/exec` (parent `a5c90d2b`), Baseline `49703481e1b02ac725428dfd8da19c4d7c954c86`
> Reviewer unit: `claude-code:agent:local_e821cd09-6696-482b-bd88-ca93dba929a2/lfd-reviewer`, activated by [dispatch ade4](../journal/20260929-111855__dispatch__ade4.md) (`7a00660a`); first message exactly `/tfw-review TFW_20260929-003444_LFD`; parent and return route `claude-code:session:local_e821cd09-6696-482b-bd88-ca93dba929a2`; originating proposer `none`

## Bootstrap record

- **Spine.** `status.md` carries all seven routing fields plus the selection pair: `coordinator_route`
  as above, `upstream_route: owner:saubakirov` matching `owner`, `dialogue: tfw-gates-only`,
  `activation` and `coordination_authority` both `HL-TFW_20260929-003444_LFD.md @ 975fed5f…`,
  `reporting: native-gates`, `selection_ref: baseline`. Lifecycle `RF`, the Reviewer gate.
- **Mandate.** HL §4.1 lets the Task Coordinator launch one independent Reviewer as a named in-session
  agent for this task only; dispatch ade4 is that act and names this unit, its first message, the
  fixed Candidate and the return route. No peer, Executor or owner route.
- **Independence.** This unit was created fresh for the review; it has no Researcher or Executor
  context and reads no other unit's transcript or unreturned worktree. The Candidate is read from the
  shared object store (`lfd/exec` is reachable there); the Executor's worktree is not inspected.
- **Lineage.** Executor commits `1590b5ce`, `6e28acc0`, `0b755dca`, `b9a7ae57` and `98b1a35e` each
  contain only their own exact paths; `lfd/exec` holds one commit after `a5c90d2b`, the Candidate.
- **Session identity.** `REVIEW · LFD` would be the title; an in-session agent has no title surface
  of its own, so title write/readback is unavailable and the parent session's title is not touched.
- **Economics binding** (`.tfw/economics/README.md`, Claude Code JSONL recipe): provider
  `claude.code-jsonl`; source is this unit's own transcript `subagents/agent-ad0017db913c3faeb.jsonl`
  in session folder `549ebd43-8839-4e1c-bfd7-1fd0be584ee7` (machine path omitted); its metadata reads
  back the name `lfd-reviewer`; source ID `549ebd43-8839-4e1c-bfd7-1fd0be584ee7`, source version
  `2.1.284`; range start line 0 (first message 2026-09-29T06:18:50.955Z); timezone `+05:00`; project
  `steps-framework`; owner `saubakirov`; role `reviewer`; unit as in the header.

## Understanding

The Candidate replaces `update.md`'s unspecified "materialize with `git archive`" fetch with one
written Git-only method (blobless, depth-1, cone-mode sparse clone of the pinned tag, an untagged
`init`/`fetch`/`checkout` route, a size check, one fallback, copy, raw-byte check, deletion), drops
three repeats under HL §12 A3 and makes the staging cleanup exact. Install (quickstart and both
prompts in three READMEs) fetches only `.tfw` and `editions` of a release, `.gitattributes` makes
archives framework-only, and the new-task startup card gains a version line. The purpose is that
installs and updates move about a megabyte instead of 114–179 MiB, no agent improvises the fetch, and
version lag becomes visible — without weakening pinning, provenance or receiver preservation.

## Accepted Claims and Boundaries

| ID | Layer | Accepted claim / authority boundary | Risk or concrete harm | Affected behavior / dependencies | Relevant environment | Oracle / authority | Evidence identity (`subject@revision`, source) | Required? |
|---|---|---|---|---|---|---|---|---|
| C1 | VALUE / ASSURANCE | The tag route in Step 0, run verbatim, stages only the pinned `.tfw` payload plus the named remainder, under 2 MiB at `v3.7.1`, every file raw-byte-equal | every receiver ships a broken or heavy fetch; improvisation returns | `update.md` Step 0; Git partial clone, cone sparse checkout, `count-objects`, `hash-object --no-filters` | Git Bash and PowerShell 5.1, Git 2.42; GitHub | TS AC-1, HL DoD 1, §3 claim 1 (A1), principle 1 | `update.md`@`0b755dca` lines 41–64; EV E1–E4; trials T1b–T3b | yes |
| C2 | VALUE / ASSURANCE | The untagged route works without `remote add` or promisor configuration (a deviation from TS §6 guidance, RF decision 2) | an authorized untagged update fails or silently downloads everything | promisor registration by a filtered fetch by URL; lazy checkout | Git 2.42/2.43; GitHub | TS AC-1 item 4; RF §2 item 2 | lines 48–54; EV E5; trials T5, T6 | yes |
| C3 | VALUE / ASSURANCE | A full download is never silent: the size check exposes a host without filters; the one fallback writes only `.tfw` and is disclosed by the same size rule | DoF 2: a silent 114 MiB download; long paths written into staging | `count-objects -vH`; the fallback wording | host without filter support (local plain server) | TS AC-1 items 2–3, AC-2 item 3; HL DoF 2 | lines 56–58; EV E6, E7; trials T4, T12 | yes |
| C4 | VALUE / ASSURANCE | `-c core.autocrlf=false -c core.attributesFile=` keeps bytes raw under the Git for Windows installer default and a hostile user attributes file | byte identity claimed but files rewritten to CRLF | clone config persistence; the untagged checkout's `-c` | Windows shells | HL §9 line-ending risk; RES iteration 1 D1, D3 | EV E8; trials T7 | yes |
| C5 | VALUE / TRACE | Pin and provenance guarantees keep their meaning: operator-named target, `VERSION` equals the tag, full SHA recorded, recheck before adapter sync, no live source `HEAD`, untagged labelling | an update installs an unintended or moved object | Step 0 prose; tag `ls-remote` line | text; trials | TS AC-3, HL DoD 3, KNOWLEDGE D70 | RF §3 AC-3 table; EV E11 | yes |
| C6 | VALUE (safety floor) | A receiver gets nothing outside the framework payload and keeps its state: staging starts empty, the copy exclusions stay, the pre-seal `git ls-files -- .tfw/.upstream` check replaces "only when safe" | DoF 1: upstream state or staging reaches a receiver's history or files | Step 0 leftover removal, Step 3 copy check, Step 4 cleanup | receiver Git working tree | HL DoF 1, F23; TS AC-7 item 4 | lines 42, 121–122, 168–170; EV E12, E21 | yes |
| C7 | VALUE | Three repeats are removed only as HL §12 A3 allows, and every protecting check stays | DoF 5: protection removed for speed | Step 4 adapter validation, payload checks, receipt template | text | TS AC-7, HL DoD 7, §12 A3 | `update.md`/`update_receipt.md` diff; RF §3 AC-7 table; EV E20, E22 | yes |
| C8 | VALUE / ASSURANCE | Install in `quickstart.md` and both prompts of three READMEs fetches only `.tfw` and `editions`, under 2 MiB, 88 installed `.tfw/` files, `editions/` byte-equal, Cyrillic names intact; the three languages say the same; each "Updating TFW" gains the one-time light-fetch request | new users still clone 123 MiB, or upstream state reaches a new receiver; a translation diverges | `quickstart.md` Step 1 and copy exclusions; README prompts and hints | Git Bash, PowerShell 5.1; GitHub | TS AC-4, HL DoD 4, §3 claim 2 | `quickstart.md` lines 22–34; README lines per EV E15; EV E13–E15; trials T8, T9 | yes |
| C9 | VALUE / ASSURANCE | `.gitattributes` makes a local archive of the Candidate contain only the allow-list, under 1 MiB, without `.gitattributes`; GitHub stated as unobserved | ZIP users keep getting 178.9 MiB, or an archive misses what old-receiver guides take from a release | `export-ignore` allow-list; `git archive` | local Git | TS AC-5, HL DoD 5, §3 claim 3 | `.gitattributes`@`0b755dca`; EV E16, E17 | yes |
| C10 | VALUE / ASSURANCE | The version line informs once at new-task start, never blocks or updates; behind, current, unreachable, offline and upstream cases observed | DoF 3: new-task start delayed or failed offline; an update without the owner | `conventions.md` `New-task startup card`; `plan.md` Step 1 renders the card | Claude Code shell tool | TS AC-6, HL DoD 6, §3 claim 4, principle 4 | `conventions.md` lines 1094–1101; EV E18, E19 | yes |
| C11 | VALUE / TRACE | Budget and form: `update.md` ≤ 1,500 words; byte-equal adapter copy; no script, hook, dependency or tool beyond Git; no VALUE path outside TS §4 | DoF 4; ceiling breach; adapter drift | word count, `cmp`, changed paths | Git | TS AC-8, HL DoD 8, §12 A4, principle 3 | EV E23 | yes |
| C12 | TRACE | Accounting: Baseline → Candidate touches 8 logical VALUE files and 151 text lines against the immutable 8 / 160 denominator; the Baseline move before launch is disclosed | a late or mutable accounting fact silently widens authority | TS §4 NUL-safe method; both Baselines | PowerShell 5.1, Git 2.42 | TS §4 prospective contract | RF §1 accounting; EV E-accounting; ONB §6 item 1 | yes |
| C13 | TRACE (identity floor) | The accepted result is exactly `0b755dca`: first tested implementation commit, reachable, before EV/RF/state; Executor mutation stopped | the wrong or a moving result is accepted | `lfd/exec`, commit parentage, RF/EV commits | shared object store | TS §4 Candidate rule; dispatch ade4 | `git branch --contains`, `git log a5c90d2b..lfd/exec` | yes (mandatory) |
| C14 | TRACE (safety floor) | No private receiver name or machine path in any committed file; no receiver, remote or GitHub change; no push or tag | DoF 6: permanent public leak | every file this task commits | local guard, `.git/info/private-names` | TS §4 M1 hard constraint, HL DoF 6 | Candidate and task commits | yes (mandatory) |
| C15 | TRACE (authority floor) | Every owner reservation held: HL and A1–A4 rulings, TS and denominator approval, no self-extended scope, final acceptance and every release/tag/push still reserved | an agent substitutes its own authority for the owner's | journal gate answers, freezes, TS amendments | task records | HL §4.1; gate answers 02ae, 235b | journal and freeze commits | yes (mandatory) |
| C16 | ASSURANCE | Unobserved environments and effects are named: Codex sandbox, GitHub archive, macOS, Git below 2.42, real filter-less hosts, long paths | principle 7 breached; a limit hidden behind VERIFIED | EV rows E9, E10, E17 | — | TS AC-2, HL principle 7 | EV E9, E10, E17 | yes |
| C17 | ASSURANCE | The configured build gate passes on the Candidate tree | an unrelated regression ships | `build.lint`, `build.test` | Python 3.13 | project config | RF §4; EV E24 | selected |
| C18 | TRACE | The Executor's economics contribution is valid and named with its limits | unaccounted or double-counted role cost | `.tfw/economics/` helper | Python 3.13 | `.tfw/economics/README.md` | RF §5; `economics/roles/8927ba18….jsonl` | selected |
| C19 | VALUE | Purpose: the change serves HL §1 and the Project North Star without adding process weight, and stays host-neutral | the task adds process or couples TFW to one host | whole Candidate | — | HL §1 at the contract baseline; NS1–NS3 | Candidate diff | yes |

## TS ↔ RF Alignment

| TS requirement | RF claim | Claim IDs | Aligned? |
|---|---|---|---|
| AC-1 (exact commands, size check, fallback, untagged route, no `/` pattern or `$0`–`$9`, measured size and raw bytes, whole-workflow trial) | RF §3 AC-1, all checked | C1–C4, C6 | ✅ claimed; verify |
| AC-2 (environments and limits) | Git Bash, PowerShell, WSL, filter-less host observed; Codex DEFERRED; unobserved named | C3, C16 | ⚠️ partial by design: the TS allows "reported unavailable with the reason"; RF labels it DEFERRED with the reason |
| AC-3 (pin and provenance) | RF §3 AC-3 table | C5 | ✅ claimed; verify |
| AC-4 (install, three languages, update hint) | RF §3 AC-4 | C8 | ✅ claimed; verify, including the Reviewer's three-language reading |
| AC-5 (archive) | local archive checked; GitHub DEFERRED | C9 | ✅ with the TS-permitted deferral |
| AC-6 (version line) | rule text and five cases | C10 | ✅ claimed; verify |
| AC-7 (removals and kept checks) | RF §3 AC-7 table | C6, C7 | ✅ claimed; verify |
| AC-8 (budget and form) | 1,492 words, byte copy, no tool, scan | C11, C14 | ✅ claimed; verify |
| TS §4 accounting | RF §1 accounting | C12, C13, C15 | ✅ claimed; verify with the TS method |
| TS §7 DoF / HL DoF 1–6 | no DoF claimed triggered | C3, C6, C7, C10, C11, C14 | ✅ claimed; verify |
| HL DoD 9 (APPROVE, owner acceptance, changelog) | not an RF claim; changelog at closing (TS §2) | C15 | n/a for this stage |

## Verification Selection

| Claim IDs | Planned check or reusable evidence | Why this depth | Known gap or limit |
|---|---|---|---|
| C1, C4, C5, C6 | Re-run the tag route verbatim from the Candidate's `update.md` against GitHub `v3.7.1` in fresh scratch receivers, in Git Bash and in Windows PowerShell 5.1, with the installer-default `core.autocrlf=true` and a hostile user attributes file supplied through a scratch global config; record size, raw-byte result, copy, deletion, recheck, pre-seal result; then a staged negative control of the pre-seal check | TS-required Reviewer re-run; the method ships to every receiver; line endings are the highest-impact Windows risk | one machine and connection; Git 2.42 only |
| C4 | Counterfactual: the same hostile configuration without the two `-c` settings | shows the guard detects a relevant fault rather than passing trivially | — |
| C2 | Re-run the untagged route verbatim by the full `v3.7.1` SHA against GitHub; inspect the promisor configuration Git wrote | the Candidate departs from TS §6 guidance; a wrong sequence breaks authorized untagged updates | Git 2.42 only |
| C3 | Local `file://` bare mirror of `v3.7.1` built from this repository's objects (no network); clone with `uploadpack.allowFilter` false; run the fallback forms as worded | DoF 2 guard; failure case cannot be produced on GitHub | emulated plain host, not a real one |
| C8 | Run `quickstart.md` Step 1 verbatim in both Windows shells; copy with its exclusions; compare installed `.tfw/` and `editions/` raw bytes; Cyrillic names in PowerShell; read the three READMEs against English | TS-required reading; install is the first contact | README prompts are text-checked; their commands equal quickstart's |
| C9 | `git archive --format=zip` of the Candidate: size, member list against the allow-list, member bytes against blobs, `.gitattributes` absent; effect on the old `git archive` update method | first release carrying the file affects every ZIP user and old receivers | GitHub's archive stays unobserved |
| C10 | Read the rule against AC-6; time one `git ls-remote --tags --refs`; compute exact tags and the newer count for 3.1.0 and 3.7.1; unreachable address under the agent tool's 5 s limit; offline host | DoF 3 and the owner's control of updates | Claude Code only; the card's rendering by a fresh Coordinator is not re-observed |
| C7 | Whole-diff reading of Steps 0–4 and the receipt template against the AC-7 list; confirm the kept checks' text is unchanged; audit E12/E22 in trials | DoF 5 | removal costs come from one synthetic trial |
| C11 | `wc -w`, byte comparison, changed-path lists, search for new executables | TS gate | — |
| C12, C15 | Re-run the TS's PowerShell NUL-safe `--name-status`/`--numstat` commands against both Baselines; check the Baseline move against the approval and gate answers | accounting is an authority boundary | — |
| C13 | Candidate reachability, parentage, commit contents and first-tested status; RF/EV commits after it | identity floor | — |
| C14 | The local guard in manual mode over the Candidate and all task commits; the same scan over this review's own files before each commit | safety floor, public repository | pattern-based scan |
| C16 | Audit E9, E10, E17 wording | principle 7 | — |
| C17 | Build gate on an extracted Candidate tree outside the repository | cheap; confirms no regression | — |
| C18 | Validate the Executor's JSONL with the helper; confirm hash | RF claims it validates | reconciliation is the Coordinator's |
| C19 | PV scan (P0–P4 fully, P5–P7 by relevance) and HL §7.2 / ONB §7 citation checks at Verify; purpose judgment at Judge against HL §1 and NS1–NS3 | required stage reads | — |

## Deviations from TS

1. Untagged route: four commands without `remote add`, promisor or filter configuration and with the
   clone settings on `checkout` only (TS §6 is non-binding guidance; RF decision 2 justifies it by trial).
2. Fallback: clone `--no-checkout`, then `checkout <SHA> -- .tfw`, so only `.tfw` is written
   (RF decision 3); consistent with AC-1's "without filter and sparse options".
3. Added beyond the TS text: "Remove a leftover `.tfw/.upstream/` first, disclosing it" (RF decision 5)
   and an exact tag recheck through the recorded `ls-remote` line (RF decision 4).
4. README prompts no longer say "copy .tfw/"; they defer the copy to `quickstart.md` (RF decision 7),
   which AC-4's "keep the existing project-state exclusions" needs.
5. To verify: EV E23 cites `git diff --name-only 49703481 0b755dca` as returning 9 paths, while the
   Baseline precedes the Candidate's parent by five Coordinator commits.
6. Disclosed authority fact: the Coordinator moved the approved accounting Baseline from `a0ccb1a3` to
   `49703481` in place before launch (ONB §6 item 1); verify against the approval and gate answers.

No TS item is left unaddressed; the changelog entry and GitHub archive are TS-deferred.

## Checkpoint

**Self-check:**
- [x] Read RF §§1–5, governing TS AC/DoF, HL purpose/principles, ONB and referenced predecessors?
- [x] Mapped every material accepted claim and the mandatory safety/security, authority and result-identity boundaries?
- [x] Bound each claim to affected behavior/dependencies, environment, oracle/authority and exact evidence identity?
- [x] Recorded a replayable verification selection and every known gap or limit?
- [x] Avoided classifying by filename, discrepancy count or artifact volume?

Stage complete: YES
