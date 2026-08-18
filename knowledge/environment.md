# Knowledge: Environment

> Topic file for `environment` facts. Updated by `/tfw-knowledge`.
> See KNOWLEDGE.md §4 for the index.

| # | Fact | Verified | Source(s) | Added |
|---|------|----------|-----------|-------|
| F1 | TFW docs site deployed at custom domain `tfw.saubakirov.kz`. GitHub Pages enabled with Source: GitHub Actions. Default branch is `master` (not `main`) | ✅ verified | RF TFW-27/C, REVIEW TFW-27/C FC1 (user + deploy output) | 2026-04-08 |
| F2 | GitHub repo relocated from an old GitHub handle to `saubakirov/trace-first-starter`. Old URL redirects still work | ⚠️ 1 source | REVIEW TFW-27/C FC2 (git push output) | 2026-04-08 |
| F3 | **Two shells run against this repository and they disagree: Git Bash (MSYS2) rewrites a leading `/` in a command argument into a filesystem path before the program sees it.** Measured here: `git log --grep="/TFW-53/freeze/"` returns **0** rows under Git Bash and **5** under PowerShell 5.1; the slash-free form returns 5 under both. Any shell command written into TFW framework text must be verified in both shells, or it ships broken for half the sessions on this machine | ✅ verified | RF TFW-53/A §7 FC1 (executor measurement 2026-08-13, accepted as ONB Recommendation 1); `conventions.md` §3 rule 15 | 2026-08-18 |
| F4 | **`git log --grep` matches the whole commit message and cannot be made subject-only.** Git matches line by line, so `^` under `-E` and `\A` under `-P` both anchor to a *line* start, not to the subject: `git log -E --grep="^TD-137"` returns a commit where the token occurs only as the first word of a body line. Unanchored `--grep="TFW-53/freeze"` returned **6** commits where 5 were real, the sixth matching only because its body quoted the pattern it was fixing — which a mechanism's own corrective commits guarantee. **Any convention identifying commits by a subject prefix must filter `%s`, not the message** | ✅ verified | RF TFW-53/A §7 FC4, FC5 (executor measurement 2026-08-13 with a constructed negative fixture); `conventions.md` §3 rule 15 | 2026-08-18 |
