# HL — TFW-26 / Phase A: Compilable Contract + Infrastructure

> **Date**: 2026-04-05
> **Author**: Coordinator
> **Status**: 📝 HL_DRAFT — Awaiting review
> **Parent HL**: [HL-TFW-26](../HL-TFW-26__documentation_site.md)

---

## 1. Vision

Phase A delivers the **compilable contract** — a formal specification that ensures every TFW artifact is part of a navigable knowledge graph. This is the primary deliverable of TFW-26 (D3: "contract > tool choice").

The contract covers three concerns:
1. **Source manifest** — what files are compiled (ALL .md: root, .tfw/, knowledge/, tasks/)
2. **Reference format** — how agents cite sources (structured text patterns that a build-time resolver converts to hyperlinks)
3. **Template amendments** — where current templates need tighter conventions so the contract works end-to-end

After Phase A, two things are true:
1. Any agent writing TFW artifacts naturally produces text references that a build-time script can resolve into a navigable graph of decisions, facts, and tasks.
2. The `docs/` infrastructure exists and is ready for Phase B to implement the gen-files logic.

**Impact:** The graph of decisions becomes navigable. From a fact in knowledge/ → to the RF where it was recorded → to the HL that framed the investigation → to the user session where the insight emerged. For humans via web docs. For AI agents via file reading or MCP. The artifacts ARE the knowledge base; the docs site is a side effect.

> "We traced D24 back through the RF, the REVIEW, the research session, and the user's exact words. All clickable. The knowledge graph built itself — we just documented the contract."

## 2. Current State (As-Is)

| Aspect | Status |
|--------|--------|
| Artifact structure | Consistent, sufficient for compilation (D6) |
| Cross-references | Text-based, ad hoc format (`RF TFW-18 §6`, `` `tasks/TFW-2.../RF` ``, `D24`) |
| Compilable contract | Does not exist — no spec for what structure compiler expects |
| Template Source columns | Mix of backtick paths, plain text, and implicit formats |
| tasks/ in documentation | Not accessible outside repo (GitHub UI only) |
| `docs/` folder | Does not exist |
| Reference resolver | Does not exist |

## 3. Target State (To-Be)

### 3.1 Result Visualization

**The knowledge graph after Phase A:**

```
knowledge/convention.md F4
  Source: "RES TFW-22 FC#4, REVIEW TFW-22 FC#4"
    ↓ resolver
  [RES TFW-22](tasks/TFW-22.../RES__TFW-22...md)  ← hyperlink
    → RES §Decisions D4: "Naming > Explanation"
      Source: "HL-TFW-22"
        ↓ resolver
      [HL-TFW-22](tasks/TFW-22.../HL-TFW-22...md)  ← hyperlink
        → HL §7 Principles: "D28 applied"
          → KNOWLEDGE.md D28                          ← hyperlink to anchor

Full chain: Fact → RES → HL → Decision. Any consumer traverses it.
```

**What changes:**

| Aspect | As-Is | To-Be |
|--------|-------|-------|
| Source columns | Mixed formats | Standardized reference patterns (§16.2) |
| tasks/ in docs | Not published | All artifacts accessible, links work |
| Cross-references | Text → dead ends | Text → build-time resolved hyperlinks |
| Templates | No reference format spec | Source format note in all templates |
| Contract | Implicit | Explicit §16 in conventions.md |
| Infrastructure | None | docs/ folder, CI/CD, gen_docs.py skeleton |

## 4. Deliverables

1. **Compilable contract** (§16 in conventions.md): source manifest, reference format, resolution rules, frontmatter convention, output structure
2. **Template amendments**: KNOWLEDGE.md, TOPIC_FILE.md, RF.md, REVIEW.md, RES.md — standardize Source column format
3. **Glossary terms**: Compilable Contract, Reference Format, Source Manifest
4. **docs/ infrastructure**: mkdocs.yml, gen_docs.py skeleton, requirements.txt
5. **CI/CD**: .github/workflows/docs.yml

## 5. Principles (from Master HL §7)

1. **Contract is the interface** — serves ALL consumers (web, MCP, AI agents)
2. **Agents reference, scripts resolve** — agents write minimal text refs, build-time script converts to hyperlinks (Layer 1 = structured text, Layer 2 = deterministic resolution)
3. **Structure preservation** — tasks/ keep their folder structure in output, relative links work without rewriting
4. **Deterministic with warnings** — missing sources and unresolvable refs = WARNING, not build failure
5. **`.tfw/` = what, `docs/` = how** — contract in conventions.md, scripts in docs/

## 6. Fact Candidates (from planning session)

> Strategic insights from this Phase A planning discussion.
> These are NOT verified facts — they become facts after `/tfw-knowledge` consolidation.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | philosophy | The primary output of TFW is a **navigable knowledge graph**, not a docs site. The graph traces: fact → source RF → decision → HL → user session. Web docs and MCP are consumers of this graph, not the goal itself. "мы же строим что-то вроде цепочки или графа, чтобы другой ИИ или mcp или что бы там ни было, могло легко найти как то или иное решение было принято" | User, TFW-26/A planning session | ✅ high |
| FC2 | convention | Agents should **reference**, not generate hyperlinks. Text patterns like `RF TFW-18` are sufficient — a build-time script resolves them. Full markdown links waste tokens and are error-prone. Layer 1 (agents) produces structured text, Layer 2 (scripts) produces hyperlinks. "ссылка это ведь токены лишние. любой скрипт сможет по тексты найти артефакт и сам добить ссылку" | User, TFW-26/A planning session | ✅ high |
| FC3 | philosophy | Excluding tasks/ from docs output **destroys the knowledge graph**. Tasks contain the decision chains — HL (why), RES (what we investigated), RF (what we did), REVIEW (what we verified). Without them, knowledge/ facts and KNOWLEDGE.md decisions are dead ends with no traceability. "Вариант А неприемлим. однозначно надо все собирать" | User, TFW-26/A planning session | ✅ high |
| FC4 | process | Cross-reference "reason" column is redundant — the source artifact IS the reason. An inline reference like `Supersedes D17` in the Rationale text is sufficient. Extra columns = noise in already dense tables | User + Coordinator synthesis, TFW-26/A planning | ⚠️ medium |
| FC5 | process | Phase A scope must include template/workflow changes, not just documentation of the contract. The contract and the artifacts that conform to it are one deliverable. "Мы должны рассматривать широко, шаблоны, воркфлоу, все артефакты TFW. Что где нужно поменять и почему" | User, TFW-26/A planning session | ✅ high |
| FC6 | process | Coordinator fact capture remains an unresolved gap (S9 from Master HL). User wants a future task: "чтобы координатор тоже писал анализировал собирал и не терял мысли". Current workaround: HL §11-style sections, but no template/workflow enforcement | User, TFW-26/A planning session | ✅ high |
| FC7 | convention | User sessions (chat conversations) are valid linkable sources because they happen under tasks. Artifacts can reference them. The HL §11 pattern (capturing quotes from planning sessions) demonstrates this | User, TFW-26/A planning session | ⚠️ medium |

---

*HL — TFW-26 / Phase A: Compilable Contract + Infrastructure | 2026-04-05*
