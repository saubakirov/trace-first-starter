# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

> Every row is asked in every review. There is no genre that exempts a row.
> **Status vocabulary:** `✅` holds · `❌` fails, with a specific finding · `⚪ N/A` does not apply here.
> `⚪ N/A` requires a stated reason in Evidence. A row skipped as a bare `✅` is a silent skip and the stage is not complete.
> Percentages are measured non-✅ rates from a 637-row corpus — they are why the row exists, not decoration.

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅/❌/⚪ | {reference verify.md §TS↔RF and specific items} |
| 2 | Philosophy aligned — two clauses, both answered. **(a) Mapping integrity:** does every TS §3 Principles Check row resolve to an AC that was actually met? **(b) Design soundness** _(4.5%)_: is the design itself sound against those principles — not "is it named well", which is row 4 | ✅/❌/⚪ | {reference HL §7 Principles; answer (a) and (b) separately} |
| 3 | Tech debt documented | ✅/❌/⚪ | {RF §6 Observations present/absent} |
| 4 | Style & standards | ✅/❌/⚪ | {conventions followed? naming?} |
| 5 | Observations collected | ✅/❌/⚪ | {quality filter: are they real issues?} |
| 6 | RF completeness (§7-9) | ✅/❌/⚪ | {§7 Fact Candidates, §8 Strategic Insights, §9 Diagrams — present?} |
| 7 | Evidence completeness — does the evidence **exist**? | ✅/❌/⚪ | {All TS Evidence fields covered in EV file? Statuses valid?} |
| 8 | Evidence sufficiency — does the evidence **establish the claim**? _(16.1% — the highest-firing check in TFW review)_ | ✅/❌/⚪ | {name the green signal and say what it does or does not establish} |
| 9 | Backward compatibility _(8.5%)_ — does the change break an existing consumer: an interface, a template section number, a document anchor, a downstream process, a report someone already relies on? | ✅/❌/⚪ | {who consumes this, and what happens to them} |
| 10 | Safety _(4.0%)_ — secrets, credentials, destructive or irreversible operations. Kept on consequence, not on rate | ✅/❌/⚪ | {what was checked, or why nothing here can cause harm} |

> **Rows 7 and 8 are not the same question, and answering them the same way means one of them was not asked.**
> Row 7 asks whether the evidence is *there*. Row 8 asks whether it *proves what it is offered to prove*:
> a passing test that tests the wrong thing, a self-declared gate marked green while unmet, a citation
> that does not support the sentence it is attached to, a screenshot of a page that was never the page
> under test. `✅` on 7 with `❌` on 8 is the normal shape of a real finding.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|

> If no KNOWLEDGE.md exists or nothing applies: "No applicable knowledge items."

## Checkpoint

**Self-check:**
- [ ] Every checklist item has evidence (not just ✅/❌)?
- [ ] Every `⚪ N/A` carries a stated reason — no row skipped as a bare ✅?
- [ ] Rows 7 and 8 answered separately, with different reasoning?
- [ ] Referenced verify.md findings in DoD assessment?
- [ ] Checked RF §7-9 for presence AND quality (not just existence)?
- [ ] KNOWLEDGE.md cross-referenced — contradictions documented or "None"?
- [ ] Fact Candidates from RF reviewed — any that need challenge?

Stage complete: YES / NO
