---
name: tfw-feedback
description: Use when a contributor asks to investigate a TFW problem or turn feedback into an upstream issue in the affected conversation. Also handles a product question or an existing TFW issue or PR.
---

# Feedback for TFW

Work in the contributor's current conversation. Deliver a short answer or a copyable issue in their language. Use the authority and evidence already available there.

## Choose the decision

- **Incident.** Identify the user's intended result, the observed result and who had to do extra work. Investigate the first point where TFW behaved differently from what the user needed.
- **Product or roadmap question.** Answer from an available maintained source when it settles the question. Otherwise draft the decision the maintainer needs to make, with one concrete use case. Claim a roadmap commitment only with a source.
- **Existing issue or PR.** Use the known thread and add only the finding that changes the decision. With a PR, inspect the relevant change and its check if accessible. Say what the evidence supports accepting, correcting or asking the author. A new issue is useful for a distinct problem.

## Investigate an incident as a TFW developer

1. Reconstruct one affected operation from existing evidence. Identify the client, version, action, role and visible result where each matters. Mark what the contributor reported and what you observed yourself.
2. Open the relevant installed file under `.tfw/`. Locate the specific guard, instruction or assumption that governed this operation. Check its provenance if local customization matters. Use TFW's own purpose or North Star to explain what the user lost. A receiving project's purpose has a different owner.
3. Follow that assumption to the smallest authorized native observation that could change the fix. Inspect a saved receipt, a scoped metadata record or a parent/child binding the upstream maintainer cannot see. Compare expected and observed values. Check a plausible competing explanation using existing material. Stop when the evidence distinguishes the fixes or the next discriminating check needs new access or work.
4. Give the supported cause and its limits. If a version guard refused before opening storage, that proves the refusal. To recommend supporting a new model or orchestration mode, check where a saved call records model and usage, how parent and child are related, and whether usage already includes the child. Treat changes in storage or attribution as hypotheses until inspected. Quota percentages and elapsed time cannot establish a token count.
5. Propose the smallest change to the responsible TFW file or rule in words. Give a check with a concrete input and an observable pass condition. When the cause is open, name what you checked and one observation that would choose between the remaining explanations.

Use targeted, read-only checks on existing authorized data. Ask the contributor before starting a new paid run, explaining what it would distinguish. If they decline, finish with the evidence at hand. Keep ordinary feedback in the conversation. A Full task, new agent, patch and incident folder are unnecessary.

## Return the draft

Put the decision on the first screen. Use a short title and these lines when they carry information. Include a small before → after or a sketch when it clarifies the user's experience. Put any essential extra evidence below the decision.

    Title — [affected operation] loses [user-visible result]

    Need and impact — Who tried what? What could they decide with a fix?
    Evidence and cause — Which installed assumption met which local fact? What remains open?
    Proposed change — Which file or rule should change, and why there?
    Check — Given which saved input, what result would count as fixed?

Remove identifying details, customer and project names, private paths, raw logs, screenshots, secrets and conversation excerpts from the shareable text. Retain public product/version names and minimal technical observations only when safe. Show the complete sanitized text to the contributor for review and edits.

For an upstream report, resolve the repository from `tfw.upstream` in the receiving project's `.tfw/project_config.yaml`. Use the known matching issue when available. If the destination or access is uncertain, return the draft for manual routing. Publish only with the contributor's explicit authorization for that text and destination. After publishing, return its link.
