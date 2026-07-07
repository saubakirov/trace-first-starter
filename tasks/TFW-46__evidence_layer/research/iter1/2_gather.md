# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW-46](../../HL-TFW-46__evidence_layer.md)
> Goal: Close the gap between "RF says done" and "actually works for the user" by adding an Evidence layer to TFW.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: Terminology | Evidence | Proof | Attestation | Acceptance |
| D2: Evidence Scope | Universal (all tasks) | Proportional (calibrated per task) | Mode-based (like review modes) | —  |
| D3: Status Vocabulary | VERIFIED / DEFERRED / BLOCKED / N/A (HL proposal) | PASS / FAIL / XFAIL / XPASS / BLOCKED / SKIP (AFD system) | ✅ / ❌ / ⚠️ / 🟡 (organic per-project) | — |
| D4: Artifact Storage | `evidence/` subfolder per task | Inline in RF (pasted output) | External reference (URL, path) | Mixed (folder + inline) |

## Findings

### G1: Cross-Discipline Terminology Analysis

Researched 6 disciplines for how "proof that something actually works" is framed:

| Discipline | Primary Term | Cognitive Framing | Agent Behavior It Would Trigger |
|-----------|-------------|-------------------|-------------------------------|
| **DevOps CI/CD** | "Deployment Verification" | Health checks, smoke tests, artifact integrity | "Run a post-deploy check" — automated, narrow |
| **QA/Testing** | "Acceptance Testing" | Pass/fail against requirements | "Run tests against criteria" — still test-centric, misses visual/real gap |
| **Audit/Compliance** | "Audit Evidence" + "Artifacts" | Raw proof → chain of custody → audit trail. ALCOA+ principles | "Collect artifacts that prove the claim" — artifact-focused, honest |
| **Scientific Research** | "Reproducibility Artifacts" | Data/code/environments enabling replication | "Produce materials others can use to verify" — replication-focused |
| **Security/Supply Chain** | Evidence → Attestation → Proof | Evidence = raw data, Attestation = signed claim, Proof = verdict | Three-tier hierarchy mapping to TFW roles |
| **AI Agent Evaluation** | "Evidence-Based Verification" | "Show me artifacts" vs "pass/fail" (traditional acceptance) | "Aggregate behavioral traces" — trajectory over outcome |

**Key finding — the Evidence → Attestation → Proof hierarchy:**

| Level | Security/Compliance Term | TFW Mapping | Who |
|-------|------------------------|-------------|-----|
| Raw artifacts | **Evidence** | Screenshots, logs, command output, rendered pages | Executor collects |
| Verified claim | **Attestation** / Audit | Evidence Table in RF with status per item | Executor writes |
| Verdict | **Proof** | Reviewer checks evidence, issues verdict | Reviewer audits |

This hierarchy is remarkably clean for TFW. "Evidence" sits at the raw-artifact level — which is exactly what the executor needs to produce.

### G2: Term Connotation Analysis (per D28 Naming-as-Prompting)

| Term | Connotation | What agent would do | Problem for TFW |
|------|------------|--------------------|-----------------| 
| **Evidence** | "Show me what happened" — raw, observable, incomplete is OK | Collect screenshots, logs, output. Honest about gaps | None — aligns with TFW's honesty principle |
| **Proof** | "Certainty, mathematical rigor" — binary, absolute | Try to prove correctness definitively. Silent about uncertainty | Too absolute — agents would avoid DEFERRED status |
| **Attestation** | "Formal signed statement" — legal/crypto | Generate a formal claim document. Process-heavy | Too formal — implies cryptographic signing, bureaucratic |
| **Acceptance** | "Did it pass the gate?" — binary, requirements-focused | Run acceptance tests. Check off criteria | Too test-centric — misses visual/rendered/real-world gap |
| **Verification** | "Did we build it right?" — already used in TFW §4 | Run build tools, check syntax, lint | Already taken — §4 IS "Verification" in TFW. Adding another "verification" creates confusion |

**D28 prediction:** "Evidence" produces the right behavior because:
1. It implies **artifacts** (not claims)
2. It allows **incomplete** evidence (DEFERRED is natural — you wouldn't say "deferred proof")
3. It's **domain-agnostic** (evidence of a rendered page, evidence of a working API, evidence of a fact-checked citation)
4. It creates a **natural pairing** with existing TFW "Verification" — Verification = synthetic tools, Evidence = real observation

### G3: Internal Project Evidence Pattern Scan

Subagent scanned 4 user projects. Cross-project comparison:

| Dimension | AFD testing/ | AHA-6 | Helpdesk HD-28 | Blog TFW-36 |
|-----------|-------------|-------|----------------|-------------|
| **Evidence folder** | ✅ Mature (`evidence/`, `raw/`) | ❌ None | 🟡 Ad-hoc (`qa_evidence/`) | ❌ None |
| **Status vocabulary** | PASS/FAIL/XFAIL/XPASS/BLOCKED/SKIP | `[x]`/`[ ]` + PASS + 🟡 | ✅/⚠️/❌ | ✅ VERIFIED / ❌ FABRICATED / ⚠️ SUBJECTIVE |
| **Anti-self-deception** | ✅ Structural (4 rules in RUNBOOK) | 🟡 Honest deferral (AC-11) | 🟡 Live-dev catches bugs | 🟡 Post-hoc (Source Audit Register) |
| **Mocked→real gap** | ✅ Explicit two-context (Local vs Live Beta) | 🔴 10 ACs harness-only, 1 deferred | 🔴 MissingGreenlet + CORS only found live | 🔴 Fabricated citation passed all gates |
| **What proves "done"** | STATUS.md ledger + per-scenario evidence | RF §4 synthetic + harness output | RF §4 gates + live curl | RF §4 content checks + source audit |

**AFD testing/ — the mature model:**
- 6-status vocabulary: PASS/FAIL/XFAIL/XPASS/BLOCKED/SKIP
- STATUS.md ledger per run — resumable, checkpoint per scenario
- `evidence/` and `raw/` folders with named PNGs and text files
- 4 anti-self-deception rules (RUNBOOK §3): assert observable outcome, empty body ≠ PASS, known-broken ≠ PASS, can't verify = BLOCKED
- PREFLIGHT.md (pre-run environment verification), LIVE_BETA.md (post-deploy playbook)
- Scenario catalog in `scenarios/` — 80 stable scenarios across 6 files

**AHA-6 — the honest deferral model:**
- RF §4 has 9 synthetic gates (compile, migration, spike, selftest, harness, graph integrity, secret-grep, build)
- AC-1–10 verified via harness (real LLM, real Postgres, real graph, intercepted Telegram)
- AC-11 explicitly 🟡 CL-gate (needs real deploy + Telegram test)
- The executor was honest — but the reviewer has no structural way to distinguish "harness pass" from "live pass" for ACs 1-10

**Helpdesk HD-28 — the accidental evidence model:**
- RF §4 has 19 verification gates including several live tests (cold export, warm cache, cross-origin, cancellation, multi-stretch)
- Two critical bugs caught ONLY by live testing: `MissingGreenlet` (lazy ORM vs cross-process) and CORS `expose_headers` (browser-only, invisible to curl)
- HD-30 had ad-hoc `qa_evidence/` folder with 1 browser screenshot
- Executor insight S4: "Live-dev validation catches a class of bugs that unit tests + curl smoke can't reach"

**Blog TFW-36 — the content evidence model:**
- §4 verification = content-specific checks (word count, keyword placement, banned phrases)
- §8 Source Audit Register = fact-checking with VERIFIED / FABRICATED / SUBJECTIVE statuses
- **Critical failure:** AI-fabricated citation traversed entire pipeline (Research → TS → Draft → RF) — caught only by user
- Reviewer self-assessment: "I did not open knowledge_state.yaml to verify numbers independently"
- Root cause identified: "TFW pipeline has no verification gate for external claims in content tasks. Code tasks have compilers; content tasks have nothing"

### G4: What "Real Evidence" Means Per Domain

| Domain | What tests/tools catch | What they miss (= Evidence gap) | What "real evidence" looks like |
|--------|----------------------|-------------------------------|-------------------------------|
| **Code (API/backend)** | Unit tests, integration, lint, build | Cross-process ORM issues, CORS browser behavior, real deploy behavior | Curl with real data, browser screenshot, deployed health check |
| **Code (UI/frontend)** | Component tests, build | Visual rendering, responsive layout, real data | Browser screenshot at target resolution, real user flow |
| **Code (mobile/device)** | Unit tests, emulator | Real device behavior, connectivity edge cases | Device logcat, on-device screenshot, real sensor data |
| **Document (Word/PDF)** | Spell check, template compliance | Layout breaks, encoding issues, visual appearance | Rendered screenshot, print preview |
| **Spreadsheet (Excel)** | Data validation, formula check | Cell sizing, color scheme, readability, encoding | Screenshot of rendered spreadsheet at working zoom |
| **Blog/content** | Word count, keyword check, structure | Factual accuracy, source validity, rendered appearance | Source verification table, published URL screenshot |
| **Analytics/SQL** | Query syntax, explain plan | Result correctness, performance on real data | Query result with real data, execution stats |
| **HR/tender/design** | Spell check, template structure | Visual presentation, format compliance, readability | Rendered document screenshot, stakeholder review |

**Pattern:** Evidence = "what you see when you open/deploy/render the actual output." Every domain has this gap between tool output and real observation.

### G5: ALCOA+ Principles (from Regulatory Compliance)

The pharmaceutical industry's ALCOA+ framework for evidence quality:

| Principle | Meaning | TFW Application |
|-----------|---------|-----------------|
| **A**ttributable | Who collected it, when | Evidence table includes executor identity + timestamp |
| **L**egible | Readable, interpretable | Evidence artifacts must be viewable (screenshots, not raw binary) |
| **C**ontemporaneous | Recorded at time of observation | Evidence collected during execution, not reconstructed after |
| **O**riginal | First-hand record | Screenshots/logs from actual environment, not recreated |
| **A**ccurate | True representation | Anti-self-deception rules (AFD RUNBOOK §3 pattern) |
| **+C**omplete | Full picture, not cherry-picked | Evidence for all AC items, not just the ones that work |
| **+C**onsistent | Same format across records | Fixed status vocabulary |
| **+E**nduring | Preserved for review | Stored in task folder (evidence/ subfolder or inline) |
| **+A**vailable | Accessible when needed | Reviewer can access evidence artifacts |

**This validates the Evidence section design:** a structured table with fixed statuses + artifact references + honest gaps (DEFERRED) satisfies most ALCOA+ requirements structurally.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| 4 clear dimensions for the Evidence design | None critical — dimensions well-defined |
| Term "Evidence" strongly validated across 6 disciplines | Counter-evidence for edge cases (iter2) |
| AFD testing/ = mature evidence system with transferable patterns | Which elements are AFD-specific vs generalizable |
| Domain catalog: 8 domains × evidence types | Proportionality heuristic (how much evidence per task type) |
| Blog TFW-36 proves evidence gap exists for non-code tasks | Content evidence patterns need deeper analysis (iter2) |
| ALCOA+ framework validates structural evidence design | How to simplify for TFW without regulatory overhead |

**Sufficiency:**
- [x] External source used? Yes — 5 web searches across DevOps, AI, audit, scientific, naming
- [x] Briefing gap closed? Yes — terminology compared, domain patterns extracted, internal projects scanned
- [x] Dimensions identified? Yes — 4 dimensions (Terminology, Scope, Status Vocabulary, Artifact Storage)
- [x] Hypothesis tested? H6 partially (Evidence validated across disciplines), H7 confirmed by naming research
- [x] Counter-evidence sought? Yes — searched for terms that might be better than "Evidence"

**Metacognitive check:** I discovered something new — the Evidence → Attestation → Proof hierarchy from security/compliance. I also found the ALCOA+ framework which I hadn't considered. The blog TFW-36 fabrication chain is a powerful counter-example showing evidence gaps beyond code. I didn't just confirm "Evidence is good" — I mapped the full alternative space.

Stage complete: YES
→ User decision: ___
