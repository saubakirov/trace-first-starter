# Knowledge: Constraint

> Topic file for `constraint` facts. Updated by `/tfw-knowledge`.
> See KNOWLEDGE.md §4 for the index.

| # | Fact | Verified | Source(s) | Added |
|---|------|----------|-----------|-------|
| F1 | User preferences MUST NOT be stored in shared files — they would propagate to the entire team. `.user_preferences.md` = gitignored, personal, per-user | ⚠️ 1 source | Chat TFW-18 (user) | 2026-04-03 |
| F2 | Workflow instructions degrade at >~1200 words per document — agents lose mid-document attention, skip stages and rules. Working range: 700-900 words. New projects (no KI context) suffer worst | ⚠️ 1 source | TFW-21 analysis + external research + user observation | 2026-04-03 |
| F3 | Agents generate filler facts and tech debt just because template sections exist. Quality filters (Human-Only Test, Quality bar) are mandatory to prevent noise accumulation | ⚠️ 1 source | Chat TFW-18B: "не рожали факты ради фактов, тех долги просто потому что надо" | 2026-04-03 |
| F4 | P{N} has irreconcilable double semantics: KNOWLEDGE.md §0 (global principles) vs HL §7 (task-local principles). Same number = different entity across contexts. Auto-resolution via regex impossible without context awareness | ✅ verified | RES TFW-27 FC2 (code scan of 5+ HLs with conflicting P1) | 2026-04-08 |
| F5 | Blog series (TFW-36) is English-only, targeting global developer audience. No Russian content. «English only for large auditory» | ⚠️ 1 source | HL TFW-36 S4 (user) | 2026-04-13 |
| F6 | TFW starter repo has dual identity: it is simultaneously the upstream template (source for tfw-init/tfw-update) AND a live project with real state (seq=38, 66 facts). This constrains how state files can be managed — live state must coexist with clean templates in the same repo. Design decisions for init/update/reset must account for both roles | ✅ verified | RF TFW-40/A §6 F2 + REVIEW TFW-40/A §7 FC1 (2 independent sources) | 2026-04-15 |
