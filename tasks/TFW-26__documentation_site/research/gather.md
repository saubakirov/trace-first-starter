# Gather — "What do we NOT know?"
> Parent: [HL-TFW-26](../HL-TFW-26__documentation_site.md)
> Goal: Compile TFW project artifacts into a publishable documentation site — deterministic, scriptable, no agent involvement.

## Findings

### G1: SSG Landscape — Tool Capabilities Matrix

| Tool | Language | Multi-source dirs | Frontmatter inject | Custom build scripts | GitHub Pages | GitLab Pages | Community |
|------|----------|-------------------|--------------------|-----------------------|-------------|-------------|-----------|
| **MkDocs + Material** | Python | ❌ Single `docs_dir` only | ✅ Native YAML frontmatter | ✅ `mkdocs-gen-files` plugin (Python scripts at build time) | ✅ `mkdocs gh-deploy` | ✅ Standard CI/CD | Massive, industry standard |
| **Jekyll + Just-the-Docs** | Ruby | ⚠️ Collections within build dir | ✅ Native YAML frontmatter | ⚠️ Limited (plugins restricted on GH Pages) | ✅ Native (GH default) | ✅ Standard CI/CD | Large, native GH integration |
| **Hugo** | Go | ⚠️ Single `content/` dir | ✅ Native YAML/TOML frontmatter | ⚠️ No build-time script plugin | ✅ Via Actions | ✅ Standard CI/CD | Large, fastest builds |
| **Docusaurus** | React/Node | ⚠️ Plugin-based multi-instance | ✅ Native frontmatter | ✅ Plugin system | ✅ Via Actions | ✅ Standard CI/CD | Meta-backed, heavy |
| **Astro Starlight** | Node | ✅ Multiple content dirs via config | ✅ MDX/Markdown frontmatter | ✅ Full Astro plugin system | ✅ Via Actions | ✅ Standard CI/CD | Fast-growing, modern |
| **Zensical** | Rust+Python | ✅ Reads `mkdocs.yml` natively | ✅ Same as MkDocs | ✅ Same ecosystem | ✅ Via Actions | ✅ Standard CI/CD | New (2025), MkDocs successor |

**Key finding**: ALL major SSGs require files to be within their designated source directory. None can natively read from scattered locations (root `/`, `.tfw/`, `knowledge/`). This means TFW always needs an **aggregation step** — either symlinks, copy script, or `mkdocs-gen-files`.

### G2: MkDocs + `mkdocs-gen-files` — Deep Dive

The `mkdocs-gen-files` plugin is the strongest candidate for TFW's use case:
- Runs Python scripts during `mkdocs build`
- Scripts can read ANY file from the project, process it, and write to the virtual docs directory
- Files are generated in-memory — not checked into the repo
- Compatible with Material for MkDocs theme
- Compatible with Zensical (successor)

**How it solves TFW's problem:**
```python
# scripts/gen_docs.py (runs at build time)
import mkdocs_gen_files

# Read KNOWLEDGE.md from project root, write to docs/architecture/decisions.md
with open("KNOWLEDGE.md") as f:
    content = f.read()

# Extract §1 Architecture Decisions, add frontmatter
with mkdocs_gen_files.open("architecture/decisions.md", "w") as out:
    out.write("---\ntitle: Architecture Decisions\n---\n")
    out.write(extracted_section)
```

This is exactly the "compilation utility" the HL envisions — but it's a MkDocs plugin script, not a standalone utility. The script IS the compiler.

### G3: ADR Tooling — Limited Relevance

| Tool | What it does | Fits TFW? |
|------|-------------|-----------|
| `adr-tools` | CLI for creating ADR markdown files | ❌ No compilation, no site generation |
| `log4brains` | ADR creation + static site (built-in) | ⚠️ ADR-only, can't handle arbitrary artifact types |
| Backstage TechDocs | MkDocs-based docs-as-code for microservices | ⚠️ Opinionated Backstage platform integration |

**Conclusion**: ADR tools solve a narrower problem. TFW's artifacts are broader (decisions + facts + conventions + glossary + changelog). No existing ADR tool fits. MkDocs with custom gen-files scripts is the right abstraction level.

### G4: GitHub Pages Deployment Options

Current state: tfw.saubakirov.kz serves from **repo root, main branch** (CNAME file confirms `tfw.saubakirov.kz`).

Three deployment models:

| Model | How it works | Impact on repo |
|-------|-------------|----------------|
| **A: `/docs` folder** | GH Pages Settings → "Deploy from branch" → main, `/docs` | Compiled output checked into git. Pollutes history. |
| **B: `gh-pages` branch** | CI/CD builds → pushes to `gh-pages` branch | Clean main branch, but legacy pattern. |
| **C: GitHub Actions** | CI/CD builds → `actions/deploy-pages` artifact upload | **Recommended**. No build artifacts in git. Clean. Modern. |

**Model C is clearly best.** `mkdocs gh-deploy` already supports this. GitLab Pages uses standard `.gitlab-ci.yml` (`mkdocs build` → `mv site public`).

**Critical implication**: If we use GitHub Actions, `docs/` folder in the repo is NOT the compiled output — it's the **source** for MkDocs (or we skip `docs/` entirely and use `mkdocs-gen-files` to aggregate from scattered locations).

### G5: GitLab Pages Compatibility

Standard `.gitlab-ci.yml` for MkDocs:
```yaml
pages:
  image: python:3.11-slim
  script:
    - pip install mkdocs mkdocs-material mkdocs-gen-files
    - mkdocs build
    - mv site public
  artifacts:
    paths: [public]
```

**Fully compatible.** Same `mkdocs.yml` config works for both platforms. Only the CI/CD wrapper differs.

### G6: Critical Constraint — MkDocs `docs_dir` Limitation

MkDocs requires **all source files in a single directory tree**. Cannot set `docs_dir: .` (project root) — causes recursive build issues. Cannot natively read from multiple directories.

**Three workarounds evaluated:**

| Approach | Pros | Cons | Windows-safe? |
|----------|------|------|---------------|
| **Symlinks** | No copy overhead | Fragile on Windows, CI/CD issues | ❌ |
| **Pre-build copy script** | Simple, portable | Duplicates files temporarily | ✅ |
| **`mkdocs-gen-files` plugin** | In-memory, no file duplication, runs at build time | Requires writing file-reading Python code | ✅ |

**`mkdocs-gen-files` wins.** It's the MkDocs-native way to aggregate from scattered directories. No symlinks, no copy scripts, no Windows issues.

### G7: AI-Queryability Landscape — DeepWiki, MCP, Chat-over-docs

User's insight: the end goal isn't just "web docs" — it's **AI-queryable knowledge endpoints**. Web docs is one output, MCP-powered AI assistants is another. Both consume the same structured artifacts.

**DeepWiki** (by Cognition/Devin):
- Analyzes repos → generates wiki-style docs + chat interface
- Uses RAG for Q&A over codebase
- **Problem for TFW**: DeepWiki analyzes *code*, not *structured knowledge*. TFW's value is in decisions, facts, processes — which DeepWiki can't distinguish from generic markdown

**Existing MCP servers for documentation:**

| Tool | Architecture | Fits TFW? |
|------|-------------|-----------|
| `markdown-rules-mcp` | Serves project md files as AI context. Smart dependency resolution, line-range embeds | ⚠️ Generic — serves files, no structure awareness |
| `Markdown Vault MCP` (LobeHub) | Full read/write to md folders. Frontmatter queries, regex search | ⚠️ Obsidian-optimized, but concept is right |
| `MCP-Markdown-RAG` | Local-first RAG with Milvus vector DB, semantic search | ⚠️ Heavy (requires vector DB), overkill for structured artifacts |
| `library-mcp` | Markdown KB server — retrieval by tags, date, full-text | ✅ Closest to TFW's needs — serves structured md with metadata |
| `mjm.local.docs` | .NET, Blazor web UI + MCP endpoint, semantic search | ⚠️ Interesting dual-interface (web + MCP) but heavy stack |

**Yandex Docs MCP architecture:**
- MCP server connects to Yandex Cloud documentation
- Agent queries → server retrieves relevant sections → injects into context
- **Key insight**: Yandex doesn't serve raw docs — it serves **indexed, structured content with search**. This is what makes it useful.

### G8: Architecture Implications — Three Output Layers

The user's vision reveals that Layer 2 from the HL is actually **multiple output targets**, not just a web site:

```
Layer 1 (Agent) → Maintains structured artifacts
                         ↓
Layer 2 (Utility) → Produces MULTIPLE outputs:
  ├── 2a: Static docs site (MkDocs → GitHub Pages)
  ├── 2b: MCP-servable knowledge (markdown files + index for MCP server)
  └── 2c: Zip/archive for distribution (portable knowledge bundle)
```

**Critical insight**: If TFW artifacts have consistent, compilable structure (the "compilable contract"), ALL these outputs can be produced from the same source:
- MkDocs reads artifacts → web site
- MCP server reads artifacts → AI context
- Zip tool archives artifacts → portable bundle

The compilable contract IS the common interface. The outputs are independent consumers.

**How this fits existing tools:**
- A simple MCP server (like `library-mcp` or custom) pointed at TFW's `knowledge/`, `KNOWLEDGE.md`, `.tfw/conventions.md` already works — agents can read these files directly
- The user already experiences this: Yandex Docs MCP + agents at Innoforce
- What's missing: a TFW-specific MCP server that understands the artifact structure (decisions, facts, conventions) and can answer structured queries like "what decisions exist?" or "what are the verified facts about X?"

**For TFW-26 scope**: Web docs (2a) is in scope. MCP server (2b) and distribution (2c) are future tasks. BUT: the compilable contract design must not preclude 2b/2c. This is a constraint on the design, not a deliverable.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| MkDocs + Material + `mkdocs-gen-files` is the strongest candidate for web output | Need to verify: can gen-files handle actual TFW artifact formatting? What transformations? |
| GitHub Actions deployment — no compiled output in git | Confirmed by user |
| GitLab Pages trivially compatible with MkDocs | Confirmed |
| ADR tools don't fit — TFW artifacts are broader | Confirmed |
| Zensical exists as MkDocs successor, reads same config | Risk: new, may not be stable. MkDocs is safer |
| AI-queryability is a parallel output target, not a replacement for web docs | Scope: compilable contract must support both, but MCP server is future task |
| Existing MCP servers for markdown exist and work — `library-mcp`, `markdown-rules-mcp` | TFW-specific MCP = future task. Generic MCP on TFW artifacts already works without any changes |
| The "compilable contract" design is the key deliverable — it serves ALL output targets | This is the Extract stage focus |

**Sufficiency:**
- [x] External source used? (10 web searches, 12+ tools evaluated)
- [x] Briefing gap closed? (SSG landscape + AI-queryability landscape fully mapped)

**Deep mode:**
- [x] Hypothesis tested? (H2: MkDocs + gen-files = yes. AI-queryability: existing MCP servers already work on raw files)
- [x] Counter-evidence sought? (All SSGs need aggregation. DeepWiki doesn't understand structured knowledge.)

**Metacognitive check (loop 2):** New insight — the compilable contract is more important than the tool choice. If artifacts have strict structure, they can serve web docs, MCP endpoints, AND portable distribution. The tool is just one consumer. This shifts the research focus from "which SSG?" to "what contract?"

Stage complete: YES
→ User decision: ___
