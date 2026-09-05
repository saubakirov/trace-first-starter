# Extract — «Чего мы не видим?»
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260905-124029_RTPSN](../../HL-TFW_20260905-124029_RTPSN.md)
> Goal: Make task-bound TFW sessions enter the intended canonical role workflow reliably before receiving a concise, evidence-selected identity.

## Configuration Space

The full Cartesian product would exceed 30 rows. The table keeps non-contradictory
configurations that vary at least one Gather dimension and makes two previously implicit
variants explicit: direct root dispatch and direct symlinked skill package.

| Config | D1. Failure boundary | D2. Entry architecture | D3. Runtime evidence | D4. Distribution state | D5. Adherence evidence | D6. Cost surface |
|--------|----------------------|------------------------|----------------------|------------------------|------------------------|------------------|
| C1 | skill/workflow non-load | byte-identical full copy | receiver file exists | declared and installed | static inspection | one workflow read; many synchronized receivers |
| C2 | workflow non-load | byte-identical full copy | completed read trace | clean receiver reproduced | historical reconstruction | one workflow read; copy-parity maintenance |
| C3 | post-load noncompliance | byte-identical full copy | later action conforms or violates | live host | repeated behavioural trial | one workflow read; full instruction context |
| C4 | command non-invocation | current thin proxy | skill-selection trace | Codex declared/installed/live | historical reconstruction | proxy + workflow double read |
| C5 | workflow non-load | current thin proxy | completed canonical read | Codex declared/installed/live | historical reconstruction | proxy + workflow double read |
| C6 | uncovered path | current thin proxy | branch/action trace | any reproducible receiver | deterministic structural test | unchanged entry cost; canonical algorithm fix elsewhere |
| C7 | post-load noncompliance | current thin proxy | later action conforms or violates | Codex live | repeated behavioural trial | baseline double-read cost |
| C8 | command or workflow non-load | strengthened minimal proxy | explicit pre-action/read marker | Codex declared/installed/live | historical reconstruction | baseline +10 words in `/tfw-plan` specimen |
| C9 | post-load noncompliance | strengthened minimal proxy | later action conforms or violates | clean receiver and live host | repeated behavioural trial | extra cue cost plus double read |
| C10 | command non-invocation | direct root dispatch | root-route trace + canonical read | root instructions live | historical reconstruction | canonical workflow only after root context |
| C11 | workflow non-load | direct symlinked skill package | selected skill + canonical read | symlink-capable Codex install | deterministic resolution test | one logical authority/read path |
| C12 | post-load noncompliance | direct single-authority entry | later action conforms or violates | representative live roles/adapters | repeated behavioural trial | lowest duplicate text; unchanged need for behavioural eval |

## Findings

### E1. Reliability is a ladder of evidence, not a property of file layout

The evidence levels form a strict chain:

1. **R0 — source presence:** an instruction exists somewhere.
2. **R1 — receiver parity:** the runtime-facing copy or link matches its source.
3. **R2 — invocation:** the runtime selected the command/skill.
4. **R3 — load:** the canonical workflow was read completely.
5. **R4 — conformance:** the later action followed the applicable instruction and branch.
6. **R5 — comparative estimate:** repeated, controlled trials estimate a difference between architectures.

Repository tests reach R1 and clean-install reproducibility. The two incidents reach R3
and then supply negative R4 observations. Neither reaches R5. Therefore a layout may be
byte-identical and still fail after loading; conversely, one observed successful run would
not prove a lower failure rate.

### E2. The four architectures affect different failure boundaries

| Architecture | Invocation/discovery | Canonical-load assurance | Path coverage | Later compliance |
|--------------|----------------------|--------------------------|---------------|------------------|
| Byte-identical full copy | still depends on vendor discovery/command routing | removes the second file boundary if the receiver itself is valid | unchanged | unchanged in the two known failure mechanisms |
| Current thin proxy | explicit Codex skill metadata and trigger text | requires a second completed read | unchanged | current proxy repeats Role Lock and stop cues, but does not enforce later behavior |
| Strengthened minimal proxy | same discovery as current proxy | makes the pre-action load boundary more explicit | unchanged | can restate priority/stop boundaries; effect remains empirical |
| Direct single authority | root mapping or symlink must provide discovery | no textual proxy-to-workflow handoff | unchanged | a single authority reduces ambiguity but cannot mechanically guarantee compliance |

No entry architecture repairs CRATM's missing resume-path action. None mechanically
prevents the RTPSN post-load decision. This separates “entry reliability” from “workflow
correctness” and “instruction-following reliability”; treating them as one metric would
make H3 unfalsifiable.

### E3. Runtime cost is small relative to canonical workflows, but not zero

For `/tfw-plan`, current double-read overhead is 141 words (~188 estimated tokens), 6.15%
of the 2,291-word entry path. The 151-word strengthened specimen would produce 2,301 words
(~3,068 estimated tokens on the combined count), +10 words over baseline. A full-copy or
direct path would read 2,150 words (~2,867), saving the whole proxy overhead.

Representative Role Locks show the same pattern:

| Role / command | Current effective words | Full-copy/direct words | Proxy overhead |
|----------------|------------------------:|-----------------------:|---------------:|
| Coordinator — `/tfw-plan` | 2,291 | 2,150 | 141 (6.15%) |
| Researcher — `/tfw-research` | 1,454 | 1,304 | 150 (10.32%) |
| Executor — `/tfw-handoff` | 2,173 | 2,013 | 160 (7.36%) |
| Reviewer — `/tfw-review` | 2,257 | 2,102 | 155 (6.87%) |

All 11 canonical workflows contain explicit Role Locks: eight Coordinator routes and one
route each for Researcher, Executor, and Reviewer. The all-command proxy corpus is 1,576
words versus 12,598 canonical words, but that corpus total is not paid on one invocation.

### E4. Maintenance burden depends on authority count, not only runtime words

| Architecture | Algorithm-bearing receiver surface | Drift detection | Routine maintenance | Portability shape |
|--------------|------------------------------------|-----------------|---------------------|-------------------|
| Full copies for all four adapters | up to 44 receiver files for 11 canonical workflows, plus 11 authorities; root/rule dispatch remains | exact hash tests can detect divergence at test time | every canonical change requires regeneration/sync | high for vendors that require native command files; Codex needs valid skill metadata |
| Current mixed model | 11 canonical workflows; 11 Codex proxy sources + 11 installed proxies; full-copy vendor receivers | current tests cover exact copies and clean installation | proxy contract and canonical algorithm evolve separately | matches current Codex/Claude conventions; declared Cursor/Antigravity receivers still need installation |
| Strengthened proxy | same file count as current mixed model | same parity checks plus possible entry-contract assertions | +10 words in the specimen; duplicated boundary language must stay non-algorithmic | same as current Codex route |
| Direct single authority | 11 canonical workflows plus minimal root/discovery mapping; symlinks may expose the same content | link resolution and schema tests replace copy hashes | lowest textual synchronization work | root dispatch is TFW-specific; symlinks and skill schemas are not uniform across all four vendors |

The checkout demonstrates why “declared”, “present”, and “live” cannot be collapsed: the
test suite can successfully reproduce the plural Antigravity target while the current tree
contains only the undeclared singular compatibility surface.

### E5. Codex full-copy and direct variants have schema constraints

The current canonical `plan.md` is not a valid byte-identical Codex `SKILL.md`: it lacks
the required `name` field. Adding a wrapper would preserve the workflow body but cease to
be byte-identical; changing canonical frontmatter would be a broader format migration.
OpenAI's documented symlink support makes a linked skill directory a plausible direct
variant, but only after the target becomes a valid skill package. Root direct dispatch is
already a fallback in `AGENTS.md`; it avoids the proxy read when the repository skill is
unavailable, yet sacrifices the normal skill discovery boundary and depends on TFW's
literal `/tfw-*` convention.

### E6. Behavioural superiority requires an eval, not prompt intuition

OpenAI's model guidance describes instruction following as sensitive to context and to
unclear or conflicting skill instructions. It also recommends changing one prompt factor
at a time and re-running evals after incremental changes because model behaviour is
nondeterministic. Applied here, “materially better cross-role adherence” requires at least
a pinned model/effort, identical task fixtures, per-boundary graders, repeated trials, and
confidence intervals. Static word counts and two historical incidents can rank cost and
diagnose mechanisms, but cannot supply that comparative adherence estimate.

Sources: [OpenAI — Model guidance](https://developers.openai.com/api/docs/guides/latest-model),
[OpenAI — model migration/eval guidance](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.2).

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Six-level evidence ladder distinguishes load from conformance and comparative effect. | R5 behavioural evidence is absent by the iteration's explicit no-new-session constraint. |
| All four architectures were normalized against the same failure boundaries and cost units. | Cross-vendor live execution is unavailable on this Codex host. |
| Direct root dispatch and direct symlink package expose two distinct single-authority variants. | Their implementation details require a later TS if selected; this iteration must not create one. |
| Role representatives quantify double-read overhead across Coordinator, Researcher, Executor, Reviewer. | No evidence yet establishes a material adherence delta for any architecture. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?

Stage complete: YES
→ User decision: advance under the explicit mandate to complete Iteration 1 without starting Iteration 2.
