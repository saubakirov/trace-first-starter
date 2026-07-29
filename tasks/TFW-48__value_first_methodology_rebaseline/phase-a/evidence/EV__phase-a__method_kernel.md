# EV — TFW-48 / Phase A: Method Kernel and Canonical Language

> **Date**: 2026-07-29
> **Author**: Executor (Codex)
> **Task**: TFW-48
> **TS**: [TS Phase A](../TS__phase-a__method_kernel.md)

---

## Environment

| Field | Value |
|-------|-------|
| OS | Windows, local workstation |
| Language / Runtime | Python 3.13.5; pytest 9.0.2; MkDocs 1.6.1 |
| Deploy target | Generated MkDocs site in `site/`, served on local loopback for rendered inspection |
| CI / Pipeline | Local verification |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | Canonical ownership is source-verifiable; behavioral consumer use is reserved for later phases as specified by the TS. | Canonical source set | N/A | `README.md`; `.tfw/README.md`; `.tfw/conventions.md`; `.tfw/glossary.md` |
| E2 | AC-2 | Opened the rendered landing and philosophy pages. The promise hierarchy, values section, six success criteria, and cross-page links were readable and navigable. A malformed rendered label on the philosophy entry link was found, corrected, rebuilt, and rechecked without browser errors. | MkDocs output served on local loopback; in-app browser | VERIFIED | `site/index.html`; `site/concepts/philosophy/index.html` |
| E3 | AC-3 | Phase A establishes the canonical Method Kernel contract; behavioral evidence belongs to later consuming phases. The source gate and research-code scan are recorded in RF §4. | Canonical source inspection | N/A | `.tfw/conventions.md` §1.1 |
| E4 | AC-4 | Terminology is source-verifiable. All 15 required glossary headings occur exactly once and their eight unique operational targets exist in the generated conventions page. | Source and generated-link scan | N/A | `.tfw/glossary.md`; `site/reference/conventions/index.html` |
| E5 | AC-5 | Phase A defines the Rule Deployment contract; scenario behavior is reserved for later workflow/template consumers. The required scenario mapping is recorded in RF §2. | Canonical source inspection | N/A | `.tfw/conventions.md` §1.1, “Rule Record and Rule Deployment” |
| E6 | AC-6 | Phase A defines claim-typed proof obligations without prescribing file count; real proof use belongs to later phases. The required claim examples are recorded in RF §2. | Canonical source inspection | N/A | `.tfw/conventions.md` §1.1, “Proof Records and Claim Boundaries” |
| E7 | AC-7 | Phase A defines independent learning and extension lifecycles; their consumers are reserved for later phases. The independence matrix is recorded in RF §2. | Canonical source inspection | N/A | `.tfw/conventions.md` §1.1, “Learning Transactions and Learning Receipts” and “Project Extensions and Registered Extensions” |
| E8 | AC-8 | Phase A defines the lifecycle and transitional eight-object ledger without changing runtime values or config; runtime numeric evidence is therefore not applicable. | Canonical source and config diff inspection | N/A | `.tfw/conventions.md` §1.1, “Numeric Controls”; empty diff for `.tfw/project_config.yaml` |
| E9 | AC-9 | Opened the rendered landing, philosophy, conventions, and glossary pages; verified readable layout and navigation. All 15 glossary term links resolved to existing conventions anchors. Documentation unit/integration tests passed: `68 passed`. | MkDocs output served on local loopback; in-app browser; local pytest | VERIFIED | `site/index.html`; `site/concepts/philosophy/index.html`; `site/reference/conventions/index.html`; `site/reference/glossary/index.html`; inline output from `python -m pytest docs/scripts/test_gen_docs.py docs/scripts/test_integration.py` |

## Verdict

Evidence verdict: 2/9 VERIFIED, 0 DEFERRED, 0 BLOCKED, 7 N/A

---

*EV — TFW-48 / Phase A: Method Kernel and Canonical Language | 2026-07-29*
