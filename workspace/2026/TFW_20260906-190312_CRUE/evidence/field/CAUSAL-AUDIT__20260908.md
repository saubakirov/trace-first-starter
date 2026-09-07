# Causal source-to-result audit — 2026-09-08

This audit records the three Coordinator-requested source-to-result chains. It is evidence for the
single post-field correction package; it is not a native provider verdict and does not reopen a field
slot.

## A. Untagged Candidate, version, and release provenance

The field Candidate is `d6d26003972f7b18fe10d492960d0cbac9f0a3e8`, with `.tfw/VERSION=3.0.0` and no
`v3.0.0` tag. The pinned target workflow says:

> A local untagged Candidate is an experiment input, not a release identity. Version equality is not
> source identity and never proves that a previous update completed.

The receipt template separately requires the immutable source locator/full SHA and installed
provenance. The source did not explicitly state whether applying an authorized untagged Candidate may
advance `tfw.version` while preserving `tfw.installed_from`; the two successful Claude receivers made
different choices:

- helpdesk: `.tfw/VERSION=3.0.0`, `tfw.version=3.0.0`, and
  `tfw.installed_from=trace-first-starter@d6d26003972f7b18fe10d492960d0cbac9f0a3e8`. Its receipt records
  the untagged Candidate SHA and its final receiver HEAD is
  `37e73c515ed658d422eb618294f1e91cd6f77fdb`.
- Atamat: `.tfw/VERSION=3.0.0`, `tfw.version=3.0.0`, while
  `tfw.installed_from=https://github.com/saubakirov/trace-first-starter@v2.0.0`. Its receipt explicitly
  states that the Candidate was an experiment input, so installed provenance was not rewritten; under
  the settled source rule this is a reported provenance deviation, not a release identity claim. Its
  final receiver HEAD is `624b16ef93722a44fe49badf8e6d753bd8ef0d9f`.

The causal ambiguity is real. The minimal source correction in the existing update workflow now makes
the rule explicit: an authorized untagged Candidate advances `tfw.version` to the payload's
`.tfw/VERSION` and records the configured upstream plus the verified full Candidate SHA in
`tfw.installed_from` as actual source provenance. The receipt and outcome must label it an untagged
Candidate, never a release tag or invented `v{VERSION}`. This does not rewrite either field receiver.

## B. Plural self-install targets and legacy singular preservation

The pinned `manifest.yaml` declares Antigravity persistent target `.agents/rules/tfw.md` and command
target `.agents/workflows/tfw-{command}.md`. The pinned 3.0.0 migration states:

> Antigravity's persistent and command roots are plural `.agents/`; `.agent/` is the separate accepted
> workflow-copy surface.

The pinned update workflow further says that new self-install targets are plural `.agents`, while the
singular `.agent/rules` location remains backward-compatible and foreign/unowned singular files must
not be deleted. Therefore the source authority is unambiguous: plural `.agents` is the new declared
target; existing managed legacy `.agent` copies may be preserved/synchronised according to the
receiver's installed adapter surface, and project-owned adjacent files remain outside the payload.

The field results are a receiver-choice divergence, not a new source rule:

- helpdesk reported and independently reconciled 11 `.agents` command/skill copies plus 11 legacy
  `.agent` workflow copies; its safe final says the plural surface was adopted and the singular surface
  was kept in sync.
- Atamat reported 11 `.agent` command copies and explicitly declined plural `.agents` adoption as an
  owner decision. That owner decision was not independently supplied, so it remains an agent report and
  an AC-5/semantic-review limitation, not a promoted owner fact.

No adapter-source correction is required. Exact semantic parity and the legitimacy of the Atamat
decision remain Reviewer work.

## C. Technical report versus owner-facing briefing

Baseline `.tfw/templates/briefing.md` required owner-language framing: each changelog fact was to be
stated as “what it lets them do, not what the procedure calls it”, with the human-facing example
“you can run two tasks at once without meeting in one file” rather than a procedural label. Candidate
d6 replaced that with a generic benefit placeholder and an outcome template, but did not preserve the
plain-language/agent-technique distinction.

The actual helpdesk owner-facing briefing exists at
`.tfw/update_receipts/BRIEFING__20260907-210839__ee08.md`, 6782 bytes, SHA-256
`7fe9964fb215d2e1ac9cba287be74c27dd5babe11e485b061da7855190027d99`; it is preserved in the exact
safe final report and independently read from the receiver. Atamat's receiver contains only
`UPDATE__20260907-211719__9495.md` (SHA-256
`ae25d24412d0f54b5f01941f6051c722be9215675db175ae3509b1e066451f4e`) plus the legacy-readme
attachment; the native final points to the UPDATE receipt. The absence of a separate BRIEFING filename
is not by itself a contract failure: an owner-facing message may be delivered in the native final and
recorded in the UPDATE receipt. A technical field report cannot substitute for an owner-facing message
or prove comprehension.

The minimal approved VALUE correction restores owner-language and agent-technique guidance in the
existing `.tfw/templates/briefing.md` and the existing Step 8 outcome wording in `.tfw/workflows/update.md`.
It does not restore the baseline's rigid four-block/no-free-text/only-CHANGELOG constraints and does not
edit either native briefing.

## Independent preservation observation

Using read-only, network-none containers as UID/GID 65532 with `GIT_OPTIONAL_LOCKS=0`, the following
two commands were run against each changed Claude receiver, scoped to root README, knowledge/state,
team/tasks, `workspace/2026`, code/deploy/rag, STEPS/TECH_DEBT, and the project-owned `.agent` rules and
adjacent workflows. Both commands exited 0 and produced 0 bytes for both helpdesk and Atamat:

```text
git diff --name-status HEAD -- README.md KNOWLEDGE.md knowledge .tfw/knowledge_state.yaml team tasks workspace/2026 code deploy rag STEPS.md TECH_DEBT.md .agent/rules/agents.md .agent/rules/conventions.md .agent/rules/glossary.md .agent/rules/harness-safety.md .agent/workflows/build-domain.md .agent/workflows/ci-status.md .agent/workflows/deploy-api.md .agent/workflows/deploy-landing.md .agent/workflows/deploy-web.md .agent/workflows/deploy-widget.md .agent/workflows/deploy-prod.md .agent/workflows/load-prod-snapshot.md .agent/workflows/local-dev.md .agent/workflows/migrate-db.md .agent/workflows/pre-push.md
git ls-files --others --exclude-standard -- README.md KNOWLEDGE.md knowledge .tfw/knowledge_state.yaml team tasks workspace/2026 code deploy rag STEPS.md TECH_DEBT.md .agent/rules/agents.md .agent/rules/conventions.md .agent/rules/glossary.md .agent/rules/harness-safety.md .agent/workflows/build-domain.md .agent/workflows/ci-status.md .agent/workflows/deploy-api.md .agent/workflows/deploy-landing.md .agent/workflows/deploy-web.md .agent/workflows/deploy-widget.md .agent/workflows/deploy-prod.md .agent/workflows/load-prod-snapshot.md .agent/workflows/local-dev.md .agent/workflows/migrate-db.md .agent/workflows/pre-push.md
```

This supports preservation of those selected paths only. It does not cover framework-managed adapters,
`.tfw/README.md`, config, all ownership, or adapter purpose. Helpdesk's expected RTBO deletion of
`workspace/00-INDEX.md` is outside the `workspace/2026` preservation selector and is reported separately.

Atamat's `.tfw/README.md` SHA-256 is
`05f440703a174082ab246212116ee3c73501fd804ed037fd0aaf1515a6cc7798`; its preserved legacy README
attachment SHA-256 is
`107c011228ffc9f6396f626ba9ade63bf476cd3992e2deca1aa7a9b0aa792f2a`, matching the approved exact-byte
preservation observation for that attachment. This proves attachment bytes, not purpose or authority.
