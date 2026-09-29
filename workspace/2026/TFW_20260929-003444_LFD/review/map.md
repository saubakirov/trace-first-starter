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

---

## Round 2 — bounded follow-up for TS revision 2 (2026-09-29)

> **Scope.** After the round-1 APPROVE the owner changed one accepted VALUE claim: the version line's limit, about 5 s to about 13 s (HL §12 A5). This appendix maps only that claim and what it depends on. The round-1 claims C1–C19 keep their REVIEW verdict unless this change touches them; the round-1 text above is history and is not edited.
> RF: [RF__TFW_20260929-003444_LFD.md](../RF__TFW_20260929-003444_LFD.md) round 2 (§§1.2–9.2) at `1e84191fbb7c4dc81746ae290660b4d1b6a3085f`, with EV round 2 (E25–E30) and trials "Round 2" at the same commit; return state (lifecycle `RF`) at `8ce93d1385c71e9f74fc24564082cc7d9c89b36e`
> TS: [TS__TFW_20260929-003444_LFD__rev2.md](../TS__TFW_20260929-003444_LFD__rev2.md), approved by the owner in gate answer 7417 and frozen with HL §12 A5 at `243a9c0b5a39b9fd61d8ad659f51f612bc717e0a`; predecessor revision 1 at `975fed5f`
> HL: [HL-TFW_20260929-003444_LFD.md](../HL-TFW_20260929-003444_LFD.md) frozen at `243a9c0b…` (first freeze `c4044d2e`); the A5 freeze itself changes only the header status line, DoD 6 and two free rows (§9 blackhole risk, §10 H3), and appends the §12 A5 row; the one other change since `975fed5f`, `ce30a943`, adds the Coordinator's economics-binding lines to the free "Material handover"; §4.1 is byte-identical at `c4044d2e`, `975fed5f` and `243a9c0b`
> Accepted subject: Candidate `cd4fe89a624897e2d0da2a58e31edb63cce052c7` on branch `lfd/exec` (tree `c3f5fbb8e5e347883de42a3585ca236473e520f8`), one commit after the round-1 Candidate `0b755dcada76fe0f22bf285a77b40f812c365c45`; Baseline `49703481e1b02ac725428dfd8da19c4d7c954c86` unchanged
> Reviewer unit: `claude-code:agent:local_e821cd09-6696-482b-bd88-ca93dba929a2/lfd-reviewer-r2`, activated by [dispatch ffae](../journal/20260929-124929__dispatch__ffae.md) (committed at `fd43cc21a57c6fb319ee4e586f3060a14551df09`); first message exactly `/tfw-review TFW_20260929-003444_LFD`; parent and return route `claude-code:session:local_e821cd09-6696-482b-bd88-ca93dba929a2`; originating proposer `none`

### Bootstrap record (round 2)

- **Spine.** `status.md` carries all seven routing fields plus the selection pair, unchanged in meaning: `coordinator_route` as above, `upstream_route: owner:saubakirov` matching `owner`, `dialogue: tfw-gates-only`, `activation` and `coordination_authority` both `HL-TFW_20260929-003444_LFD.md @ 243a9c0b…`, `reporting: native-gates`, `selection_ref: baseline`. Lifecycle `RF`, the Reviewer gate, entered by the transition event `c1fd` (`ONB → RF`).
- **Mandate.** HL §4.1 lets the Task Coordinator launch and continue the independent Reviewer as a named in-session agent. The round-1 Reviewer `lfd-reviewer` cannot be resumed in the restarted session; the dispatch names this fresh unit, its first message, the bounded scope and the return route, and states that one Reviewer is active at a time. `conventions.md` → `The 🔄 REVISE route`: "A fresh role holder resolves lineage from state/artifact references." The same reading applied to the round-2 Executor (dispatch 9c6f). The dispatch reads HL §4.1's "one independent Reviewer" as one active Reviewer at a time; no owner reservation is crossed by replacing an unreachable unit of the same role, so this is recorded as an observation for the Coordinator, not a blocker.
- **Independence.** This unit was created fresh; it has no Executor, Researcher or round-1 Reviewer context. It reads the round-1 stage files and REVIEW only as committed task artifacts, never another unit's transcript, chat or unreturned work; the scratch folder of this session holds files of other units, which were not opened. The Candidate is read from the shared object store; the Executor's worktree is not inspected.
- **Lineage.** Round-2 Executor commits `cf5085bb` (ONB), `ae156ec8` (state and handoff event), `cd4fe89a` (Candidate, `lfd/exec`), `1e84191f` (RF, EV, trials, economics) and `8ce93d13` (return state) each name only their own paths; Coordinator commits `243a9c0b` (freeze), `93a283d9`, `239a13bf`, `bd575c43` and `fd43cc21` name only HL, TS rev 2, status and journal paths.
- **Session identity.** `REVIEW · LFD` would be the title; an in-session agent has no title surface of its own, so title write and readback are unavailable and the parent session's title is not touched.
- **Economics binding** (`.tfw/economics/README.md`, Claude Code JSONL recipe): provider `claude.code-jsonl`; source is this unit's own transcript `subagents/agent-aa8148e62dc050632.jsonl` in session folder `31abf4fc-cdf2-4d07-9252-bc458855a801` (machine path omitted); its metadata reads back the name `lfd-reviewer-r2`; source ID `31abf4fc-cdf2-4d07-9252-bc458855a801/aa8148e62dc050632` (the `<sessionId>/<agentId>` form); source version `2.1.284`; range start line 0 (first message 2026-09-29T07:49:14.501Z); timezone `+05:00`; project `steps-framework`; owner `saubakirov`; role `reviewer`; unit as in the header. Selected from this session's own `subagents/` folder by the metadata name and the first line, not by recency.

### Understanding (round 2)

Round 2 changes one clause of one shipped file: the startup card's version line now waits about 13 s, not about 5 s, for its one `git ls-remote --tags --refs`, because ordinary checks measured 3.2–4.8 s in round 1 and a slow link would show `unknown` too often (HL §12 A5, the owner's choice over a 10 s alternative). The Executor re-observed the unreachable case under the new limit, showed that ordinary and slow answers complete, and returned Candidate `cd4fe89a`, whose whole difference from the accepted Candidate is that number. The purpose is unchanged: visible version lag at new-task start that never blocks and never updates; the new cost is a start that can wait up to about 13 s on a network that drops packets, which the owner accepted.

### Accepted Claims and Boundaries (round 2)

| ID | Layer | Accepted claim / authority boundary | Risk or concrete harm | Affected behavior / dependencies | Relevant environment | Oracle / authority | Evidence identity (`subject@revision`, source) | Required? |
|---|---|---|---|---|---|---|---|---|
| R2-C1 | VALUE | The rule requires the one `ls-remote` "under a limit of about 13 s set on the agent's own command tool"; every other clause of the version line is unchanged (exact `vX.Y.Z`; suffixed tags never count; a tool that cannot bound time skips the call; how many newer and the `/tfw-update` offer; `unknown` with the reason; `installed_from: "self"` makes no call and no offer; never starts an update) | the wrong number ships to every receiver, or a clause is lost with it | `conventions.md` `New-task startup card`; `plan.md` Step 1 renders the card from the rule; any other text that restates the limit | text | TS rev 2 AC-6 bullet 1; HL §12 A5, DoD 6, §3 claim 4, principle 4 | `.tfw/conventions.md`@`cd4fe89a` (blob `66b1d877`) lines 1094–1101; EV E25 | yes |
| R2-C2 | VALUE / ASSURANCE (safety) | Under the 13 s limit an unreachable upstream returns control to the agent at the limit and the row reads `unknown`, nothing blocked | a new task held for 21–131 s by a Git that has no connect limit (DoF 3) | the shell tool's `timeout`; Git's behavior on a blackholed address; leftover process after the limit | Claude Code shell tool 2.1.284, Windows, Git 2.42 | TS rev 2 AC-6 bullet 2; HL DoD 6, DoF 3 | EV E26; trials R2-4 | yes |
| R2-C3 | ASSURANCE | An ordinary check completes under the new limit; an answer slower than the old limit and faster than the new one completes, and the old limit would have cut it | A5's purpose fails: `unknown` shown although the upstream answered | the same tool limit; ordinary `ls-remote` cost; the tag filter and newer count | same; public upstream | TS rev 2 AC-6 bullet 2 ("an ordinary check ... now completes") | EV E27, E28; trials R2-1 to R2-3, R2-5 to R2-7 | yes |
| R2-C4 | VALUE / TRACE | Only that clause changed: `cd4fe89a` differs from `0b755dca` by one line of `.tfw/conventions.md`; the other seven VALUE paths and the derived copy are byte-identical; `update.md` is 1,492 words (ceiling 1,500) and its adapter copy byte-equal; the release archive still holds the allow-list (AC-5 dependency); no new script, hook, dependency or tool | an unreviewed change rides along, or a carrier of the old limit survives elsewhere | AC-5 archive; AC-8; every text that names the limit | Git | TS rev 2 §4 and AC-8; HL DoD 5, 8 | `git diff 0b755dca cd4fe89a`; EV E29 | yes |
| R2-C5 | TRACE (identity floor) | The accepted result is exactly `cd4fe89a`: the first tested implementation commit of round 2, reachable on `lfd/exec`, before the EV/RF/state commits, with Executor mutation stopped | the wrong or a moving result is accepted | `lfd/exec` history; commit order; RF/EV commits | shared object store | TS §4 Candidate rule; dispatch ffae | `git log 0b755dca..lfd/exec`; `git branch --contains` | yes (mandatory) |
| R2-C6 | TRACE | Accounting for the round-2 Candidate: 8 logical VALUE files and 151 touched text lines against the immutable 8 / 160; identical to round 1 because the changed line lies inside an added paragraph | a late or mutable accounting fact widens authority silently | TS §4 NUL-safe method; both Baselines | PowerShell 5.1, Git 2.42 | TS rev 2 §4 prospective contract | EV E-accounting (round 2) | yes |
| R2-C7 | TRACE (authority floor) | The 13 s value, TS revision 2 and the denominator carry the owner's ruling before work; the freeze contains only what A5 authorizes; nothing reserved to the owner (final acceptance, tag, release, push) is exercised; final acceptance takes effect only when this re-check approves | an agent substitutes its own limit or scope for the owner's | gate answer 7417; freeze `243a9c0b`; HL §12 A5; TS rev 2 header | task records | HL §4.1, §12 A5; gate answer 7417 | journal, freeze diff, status | yes (mandatory) |
| R2-C8 | TRACE (safety floor) | No private receiver name or machine path in any file committed in round 2; no receiver, remote or GitHub change; no push or tag | permanent public leak (DoF 6) | every file this round commits; remote-tracking refs and tags | local guard, `.git/info/private-names` | TS §4 M1; HL DoF 6 | round-2 commits; refs | yes (mandatory) |
| R2-C9 | ASSURANCE | Limits stay named: the Codex sandbox and other tools that may not bound a command (HL §8), GitHub's own archive (E17), a fresh Coordinator's rendering of the card (round-1 O3) | principle 7 breached; a limit hidden behind VERIFIED | EV E9, E17; RF §3.2 | — | HL principle 7; TS rev 2 AC-6 | EV round 2 verdict | yes |
| R2-C10 | ASSURANCE (labelled control) | The configured build gate passes on the Candidate tree (14 collected, 14 passed) | an unrelated regression ships | `build.lint`, `build.test` | Python 3.13 | project config | EV E30 | selected; positive control only |
| R2-C11 | TRACE | The round-2 Executor's economics file is valid, hash-named and bound to `<sessionId>/<agentId>`; the round-1 Executor's file stays for the Coordinator's reconciliation (round-1 O9) | a unit's cost is mis-keyed or excluded | `.tfw/economics/` helper | Python 3.13 | `.tfw/economics/README.md` | `economics/roles/a7509c86….jsonl` at `1e84191f` | selected |
| R2-C12 | VALUE | Purpose: the change serves HL §1 (a lagging receiver is visible when work starts) and NS1–NS3 as amended, without adding process weight; the up-to-13 s worst-case wait is a disclosed, owner-accepted cost, not an unreviewed one | the limit trades new-task latency for fewer false `unknown` rows without being weighed | whole change | — | HL §1 and §12 A5 at the contract baseline; NS1–NS3 | Candidate diff; HL §12 A5 | yes |

Unchanged round-1 claims C1–C9 and C11 do not read the changed clause; the round-1 evidence for C10 (E18, E19, 5 s) is superseded for AC-6 by E25–E28, while the offline and upstream-itself cases in E19 do not depend on the limit and stay as observed.

### TS ↔ RF Alignment (round 2)

| TS rev 2 requirement | RF round 2 claim | Claim IDs | Aligned? |
|---|---|---|---|
| AC-6 bullet 1: rule text with "about 13 s", other clauses unchanged | RF §3.2 AC-6; EV E25 | R2-C1 | ✅ claimed; verify |
| AC-6 bullet 2: unreachable case under 13 s; an ordinary check (3–5 s in round 1) completes; other cases as observed unless affected | RF §3.2 AC-6; EV E26–E28 | R2-C2, R2-C3 | ⚠️ the 3–5 s window did not recur (1.07–1.31 s), so the Executor added an emulated 7.26 s answer; judge whether that establishes the claim |
| AC-1 to AC-5, AC-7 unchanged, evidence reused | RF §3.2 last bullet; EV E1–E17, E20–E22; archive re-derived E29 | R2-C4, R2-C9 | ✅ claimed; verify reuse conditions |
| AC-8 budget and form | RF §3.2 AC-8; EV E29 | R2-C4 | ✅ claimed; verify |
| TS §4 accounting, denominator 8 / 160 unchanged | RF round-2 accounting table; EV E-accounting (round 2) | R2-C6 | ✅ claimed; verify with the TS method |
| TS §7 DoF and HL DoF 1–6 | none claimed triggered | R2-C2, R2-C4, R2-C8 | ✅ claimed; verify |
| HL DoD 9 (APPROVE, owner acceptance, changelog) | not an RF claim; the changelog is written at closing | R2-C7 | n/a for this stage |

### Verification Selection (round 2)

| Claim IDs | Planned check or reusable evidence | Why this depth | Known gap or limit |
|---|---|---|---|
| R2-C1 | Read lines 1094–1101 at `cd4fe89a`; diff against `0b755dca` and the Baseline; search the whole Candidate tree and this task's records for any other statement of the limit | the only VALUE change; a stale carrier would contradict it | search is textual |
| R2-C2 | Apply the rule with a harness written for this review (reads `.tfw/VERSION` and `tfw.upstream`, one `ls-remote`, exact-tag filter, prints the row; enforces no limit itself) in a scratch receiver whose upstream is a blackholed documentation address; run it through this unit's own shell tool with `timeout` 13,000 ms; note the tool's behavior at the limit, the process's own end and any leftover process | DoF 3 and the owner's control of the start; the mechanism is the tool's, so it must be observed on this tool | this tool's behavior only; other tools stay unobserved; a network that refuses fast would not exercise the bound, so the address's behavior is recorded |
| R2-C3 | Ordinary checks through the same harness and limit against the public upstream for behind (3.1.0) and current (3.7.1), several timings; a local slow-answer stand-in (a scratch localhost HTTP server that delays the real Git advertisement of a scratch repository by about 7 s) run under 13,000 ms and under 5,000 ms | proves the case A5 was made for, without depending on this connection's speed today | an emulation, not a real slow network; independent of the Executor's proxy design |
| R2-C4 | `git diff --name-status` and `--stat` between the two Candidates and against the Baseline; `wc -w`, `cmp`, blob ids; a search for `$0`–`$9` and `$ARGUMENTS` in the changed paragraph; local `git archive --format=zip` of `cd4fe89a`: size, member list against the allow-list, member bytes against blobs, `.gitattributes` absent | TS AC-8 gate; AC-5 depends on the changed file | GitHub's archive stays unobserved (E17) |
| R2-C5 | `git log 0b755dca..lfd/exec`, `git branch --contains`, per-commit file sets, commit times against the RF/EV/state commits | identity floor | — |
| R2-C6 | The TS's PowerShell NUL-safe `--name-status` and `--numstat` commands with `$valuePaths`, Baseline to both Candidates | authority boundary | — |
| R2-C7 | Freeze diff `975fed5f → 243a9c0b`; §4.1 unchanged since the first freeze; TS rev 1 to rev 2 diff; gate answer 7417 against the A5 row and TS header; no tag, no push (`git tag`, remote-tracking containment) | human authority floor | the owner's own words are read through the journal record only |
| R2-C8 | The repository's local guard in manual mode over every round-2 task commit and, before each of my commits, over its staged content; a positive control in a scratch repository | safety floor, public repository | pattern-based scan |
| R2-C9 | Read EV E9, E17 and the round-2 verdict wording; compare with HL §8 | principle 7 | — |
| R2-C10 | Build gate on the Candidate tree extracted outside the repository | cheap; labelled a positive control | does not exercise instruction text |
| R2-C11 | Helper `validate` and SHA-256 of the round-2 Executor file | RF claims it validates | reconciliation is the Coordinator's |
| R2-C12 | PV scan at Verify (P0–P4 fully, P5–P7 by relevance; HL §7.2 and ONB §7 citations); purpose judgment at Judge against the master HL at the contract baseline and NS1–NS3 | required stage reads | — |

### Deviations from TS (round 2)

1. The TS asks that round 2 confirm that "an ordinary check (3–5 s on 2026-09-29) now completes". The Executor's checks ran 1.07–1.31 s, so it added an emulated 7.26 s answer to reach the window it could not reproduce (RF §2.2 item 3, EV E27–E28). Recorded as a disclosed substitution; judged at Verify and Judge, not yet a finding.
2. No other item of TS revision 2 is left unaddressed; the changelog entry is written at closing (TS §2) and GitHub's archive stays DEFERRED to the owner's push.

### Checkpoint (round 2)

**Self-check:**
- [x] Read RF §§1–5 (both rounds), governing TS rev 2 AC/DoF, HL purpose/principles at the re-freeze, ONB (round 1 and §8) and referenced predecessors (round-1 REVIEW and stage files, dispatch ffae, gate answer 7417)?
- [x] Mapped every material accepted claim and the mandatory safety/security, authority and result-identity boundaries?
- [x] Bound each claim to affected behavior/dependencies, environment, oracle/authority and exact evidence identity?
- [x] Recorded a replayable verification selection and every known gap or limit?
- [x] Avoided classifying by filename, discrepancy count or artifact volume?

Stage complete: YES
