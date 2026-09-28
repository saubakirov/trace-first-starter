# Briefing — Light fetch, light install and the version check

> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW_20260929-003444_LFD](../../HL-TFW_20260929-003444_LFD.md)
> Goal: Installing or updating TFW moves only the framework, about one megabyte, by one written method, and a newer release shows in one line when new work starts; the owner decides whether and when to update.
> Producer unit: `claude-code:agent:local_e821cd09-6696-482b-bd88-ca93dba929a2/lfd-researcher`, as recorded by the dispatch; this in-session agent cannot read its own name back
> Parent Coordinator: `claude-code:session:local_e821cd09-6696-482b-bd88-ca93dba929a2`
> Activation / dispatch source: delegated; [dispatch](../../journal/20260929-005309__dispatch__c29b.md) committed in `8ebea35e23e559eff58d195b7d338b35429e9c70`; first message exactly `/tfw-research TFW_20260929-003444_LFD`
> Coordination authority: `HL-TFW_20260929-003444_LFD.md @ c4044d2efc78e2e422849b27bccc4e0d9da2688e`
> Originating proposer: none
> Mode: deep, ruled by the Coordinator (User Direction). Iteration 1 of `research/iterations.yaml`: H1, H3, H4.
> Selection: `baseline` · `native-gates` · `tfw-gates-only`. Returns go only to the Coordinator above. Navigation title `RESEARCH · LFD` is unavailable: an in-session agent has no title of its own.

## Why this investigation, and what would change the approach

The HL fixes *what* must hold: under 2 MiB, every framework file byte-equal to the pinned tree,
one written method with a disclosed fallback, no silent full download, a version check that never
blocks. It leaves open *which* Git method achieves that everywhere. R1 shows the danger: a method
that looked light moved ≈114 MiB, and the cause surfaced only on a second attempt. The approach
changes if any of these turns out true:

- a candidate needs a tool other than Git that resolves differently per shell, or a pipe that
  Windows PowerShell 5.1 corrupts;
- the Git for Windows installer default (`core.autocrlf=true`) rewrites line endings on output,
  or the usual check (`git hash-object`) hides that rewrite;
- a host or an older Git ignores the filter and the method falls back to a full download without
  a visible error;
- the version check can hang for tens of seconds on a blackholed network;
- install reads root files beyond `.tfw/` and `editions/`, or an archive-only `.gitattributes`
  removes something that `update.md` or a maintainer procedure archives.

## Planning inventory (not evidence; Gather observes again)

Git 2.42.0 for Windows; the system config sets `core.autocrlf=true`, which this user's global
config overrides with `input`, so a default install elsewhere behaves differently from this
machine. Windows PowerShell 5.1. `tar` resolves differently per shell: Git Bash has GNU tar 1.34,
while PowerShell finds an old third-party `tar` earlier on PATH than Windows' built-in one. The
Codex CLI is installed and offers `codex sandbox`, which runs a command under the Windows
restricted-token sandbox without a model. A WSL Ubuntu is present.

## Research Plan

Expected decision dimensions: transferred bytes · fidelity (file set, raw bytes, line endings) ·
portability (shell, extra tools, Git feature floor, sandbox) · failure visibility (no silent full
download, no hang) · pin/provenance fit · simplicity (commands, words, tools) · time.

### Gather — methods, a measuring rig that can see failure, sources

- **Rig first, proven against a known failure.** Transferred bytes = growth of loose and packed
  objects (`git count-objects -v`, because small fetches are unpacked), cross-checked with Git's
  own trace of every on-demand fetch. Fidelity = file set plus `git hash-object --no-filters`
  and SHA-256 of raw bytes against `git ls-tree -r v3.7.1 -- .tfw` from this repository.
  Positive control: reproduce R1's no-flag prefetch against a local `file://` copy of this
  repository (no network), to verify R1's explanation and not only its outcome.
- **Update candidates against GitHub, tag `v3.7.1`, in Windows Git Bash and Windows PowerShell
  5.1:** (A) blobless depth-1 clone plus `git archive --worktree-attributes` of `.tfw`;
  (B) blobless depth-1 clone narrowed by sparse checkout to `.tfw/`; (C) blobless clone without
  checkout plus a checkout of `.tfw` into a separate work tree. Record bytes, time (at least two
  runs), exact commands and every tool used beyond Git.
- **Line endings and file kinds:** run each candidate under this machine's effective setting and
  under the installer default emulated with `-c core.autocrlf=true`; list any `.tfw/` files
  stored with CRLF, binary, symbolic links or executable bits.
- **H3:** time `git ls-remote --tags --refs` (at least three runs, output bytes); time the failure
  for an unknown host, a refused connection and a blackholed address; list tag names for
  pre-release forms and check that version sorting orders them correctly; find how the upstream
  can recognise itself from `tfw.upstream`.
- **H4 and §3 claim 3:** every path that `quickstart.md`, `init.md`, the root README Quick Start
  and the adapter manifest read from the source; every `git archive` use in maintainer
  procedures, workflows, tools and CI. External sources: Git documentation for partial clone,
  sparse checkout, `git archive`, attributes and unpack limits; GitHub documentation on partial
  clone and archive attributes; Microsoft documentation on PowerShell 5.1 native pipes.

### Extract — configuration map

- Method × shell × line-ending setting: bytes, time, fidelity, tools, command count and the trap
  each combination hits.
- Git feature floor per method (`--filter`, `--sparse`, `sparse-checkout set`, the archive
  attribute behaviour) against Git versions receivers plausibly run.
- Fit with the unchanged pin: full SHA from the operator-named tag, `VERSION` read at that
  commit, immutability recheck, no read of live `HEAD`.
- Version-line mechanics: one command, its limit, how "unknown" appears, pre-release exclusion,
  upstream self-recognition.
- Install payload: the exact path list and the project-state exclusions; a candidate
  archive-only `.gitattributes` with the measured size and content of a local archive.

### Challenge — what would make the survivor wrong

- Silent full download: a server that ignores `--filter` (the local copy served without filter
  support), a Git too old for one feature, a proxy.
- Broken byte identity: the installer default line-ending setting, a user-level attributes file,
  `git hash-object` normalization masking CRLF.
- A hanging version check: a blackholed network with no limit; which limit Git itself can impose
  and which only the agent's tool timeout can.
- `.gitattributes` side effects: export exclusion reaching the `.tfw/` payload, `update.md`'s own
  archive or a maintainer archive; GitHub's archive behaviour from documentation, while the real
  GitHub archive stays unobserved until the owner's push.
- Metacognitive check: what is new rather than merely confirmed, and which source was not checked.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | One Git method (partial clone limited to framework paths, or blobless clone plus `git archive --worktree-attributes`) transfers under 2 MiB and yields byte-identical framework files in Windows Git Bash, Windows PowerShell and the Codex sandbox. False case: an environment lacks support or converts line endings → the archive link becomes the documented fallback or primary. | open |
| H3 | A latest-release check via `git ls-remote --tags` costs about a second and fails fast offline and in sandboxes. False case: it can hang for tens of seconds or is blocked → the rule states an explicit limit or skips the check where network is known to be absent. | open — partly observed (1.1–1.3 s; bad host 0.3 s) |
| H4 | Install needs only `.tfw/` and `editions/` (plus the README files and LICENSE for archives). False case: init or quickstart reads other root files → list them explicitly. | open |

H2 (where update time goes) belongs to iteration 2, as prepared. Iteration 1 records fetch times
only as an input to it.

## Scope Intent

- **In scope:** H1, H3 and H4 as above; the install-path variant of each surviving method
  (`.tfw/` and `editions/`); local-archive behaviour of an archive-only `.gitattributes` in a
  scratch copy; every `git archive` use in maintainer procedures; the Codex sandbox and WSL
  Ubuntu if the Coordinator permits (question 1); external documentation at every stage.
- **Out of scope:** H2 and any removal from the update procedure (iteration 2); a trial update of
  a scratch receiver copy; any edit to repository files other than these research stage files;
  any receiver, remote or GitHub-side change; push; the real GitHub archive (needs the owner's
  push). A real no-network state would mean changing a system setting, so offline is simulated
  with an unknown host, a refused connection and a blackholed address, and reported as simulated.
- **Hygiene:** scratch directories outside the repository only; no private receiver names or
  machine paths in these files; the configured limits of 15 project files and 5 web queries per
  stage.

## Guiding Questions

1. **Extra environments.** May I run the same fetch and `ls-remote` trials (a) under the local
   Codex CLI's `codex sandbox` (Windows restricted-token sandbox; runs one command without a model
   or login; I stop if it asks for setup or elevation) and (b) in the local WSL Ubuntu as the
   Linux observation? If not, both are reported unobserved with that reason.
2. **One heavy download.** R1's explanation is tested first against a local `file://` copy, with
   no network. If that does not reproduce the prefetch, may I run the no-flag method once against
   GitHub (≈114 MiB)? The same run would give the old method's download time that H2 needs in
   iteration 2.

## User Direction

- **Mode (Coordinator ruling, 2026-09-29):** deep. Reason given: H1 selects the method every
  receiver runs, and the known failure stayed hidden until a with/without comparison, so
  counter-evidence fits the §9 risks. Extra loops run only when a stage checkpoint is unmet; the
  `tfw.research` file and web limits stay in force.
- **Session title (Coordinator):** an in-session agent cannot set its own title; recorded as
  unavailable.
- **Guiding questions:** awaiting the Coordinator's answers.

**Knowledge handover.** Producer and recipient as in the header. Inspected: `status.md`, the
journal, the frozen HL, `iterations.yaml`, `tfw.research`, the `conventions.md` sections the
workflow names, the HL §7.2 sources and `knowledge/records/`. Material so far: the plan, the
planning inventory and the two open questions. Record `TKL-20260913-01` replaces D82 only for how
the Knowledge Gate runs; D82's rule of no shipped executable or dependency still applies. No record
points at D70, D2 or F23. Uncertainty: every hypothesis is open. Continuation: the Coordinator's
answers, then Gather.

---
Stage complete: YES
Gate: WAIT — Briefing returned to the Coordinator; Gather needs its continuation.
