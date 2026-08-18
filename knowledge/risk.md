# Knowledge: Risk

> Topic file for `risk` facts. Updated by `/tfw-knowledge`.
> See KNOWLEDGE.md §4 for the index.

> **Source format**: Use reference patterns (e.g., `RF TFW-18 §6`, `REVIEW TFW-22`).
> Build-time resolver converts these to hyperlinks. See compilable_contract.md §2.

| # | Fact | Verified | Source(s) | Added |
|---|------|----------|-----------|-------|
| F1 | **Two task sessions in one working tree share one git index, and the discipline that protects it lives nowhere durable.** The owner instructed both sessions about concurrent execution — «параллельно будет запущен tfw-56 исполнение, так что надо учитывать при коммитах» — and the executor that recorded the instruction as a fact candidate and reasoned about it in writing still swept three of the sibling task's deletions into its own commit. **A verbal staging directive has a demonstrated survival rate of 0 out of 1 against a broad `git add`**, which is the structural-enforcement-over-exhortation argument reproduced on the git index. Three consecutive phases of one task then produced three *different* ad-hoc answers — sweep-and-repair, generate-the-full-diff-and-apply-one-hunk, and leave-it-uncommitted-on-a-verbal-instruction — none written down. Under D55 the commit subject becomes the **only** record of which task a change belongs to, so a misattributed staging silently misattributes the trace. **This is TFW-54's problem arriving before TFW-54:** a coordinator running a team of delegate sessions faces the same index with more writers, so its grant must bound *what may be staged*, not only what may be decided. The concrete missing artifact is small — a staging rule in `handoff.md` and `review.md`: stage by explicit path, and what to do when a shared file carries someone else's hunk | ✅ verified | HL TFW-53 §11 (user run directive 2026-08-13); RF TFW-53/B §8 S1, REVIEW TFW-53/B §7 FC2 (`git show --stat fbdf443`, TD-144); RF TFW-53/C §8 S3, REVIEW TFW-53/C §7 FC2; REVIEW TFW-53/E TD-178 | 2026-08-18 |
