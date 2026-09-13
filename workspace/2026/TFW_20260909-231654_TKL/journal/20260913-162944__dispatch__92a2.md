---
time: '2026-09-13T16:29:44+05:00'
kind: dispatch
writer: robert
on_behalf_of: saubakirov
via: codex
refs:
- status.md
- HL-TFW_20260909-231654_TKL.md
- TS__TFW_20260909-231654_TKL.md
- ONB__TFW_20260909-231654_TKL.md
- journal/20260913-145904__dispatch__3328.md
- journal/20260913-154924__dispatch__580a.md
summary: Start the two existing Q1 holders on the verified prepared receiver and independent
  first seals.
---

Source and sole operational parent: Coordinator `01a09974-6716-7cc0-9916-fd6d04c91481`. Destination: existing Executor `01a09a0c-c9e2-7d01-af4e-64931af967ed`, host local, direct native channel. Nonce: `TKL-Q1-e00ca51d`. Q1 proposal origin remains the Executor; this is synchronization inside the existing LEAD 3328 and 0173 bounds, not new scope or acceptance.

The actual tested Candidate is `27cdb701b91c5b45b9f54b3e98c9ad67635b3e30`. The prepared standalone receiver base is `e00ca51d05f4e451441cb9fc267579a7f9e4d4ce` at `C:/Users/c0rpa/AppData/Local/Temp/TFW_TKL_NATIVE_01a09a0c/concurrent-repo`; common Git directory ends `/concurrent-repo/.git`. Separate worktrees are `/coordinator` on `codex/tkl-native-coordinator` and `/executor` on `codex/tkl-native-executor`. Both clean heads were verified at that exact base with `git -c core.longpaths=true`. The initial status assertion without that required Windows long-path option failed; using the preparation command's explicit option observed both clean trees, without file repair or reset.

Executor's actual packet is `evidence/native/plan-and-authority.md` in its f3f3 TKL tree, SHA256 `fcf97e30a8d366e10afd7b5883139b03cc2a58cf1b82efc5b4c3dfa7504bfa55`; its prepared manifest SHA256 is `ae25e7219db94200c3e2c110a98769da155a6460d4803947992b576f8096b47d`. The Coordinator verified all 17 exported sources against actual original Git objects and all 22 prepared input hashes. The four future holder output paths were absent. Packet creation and Coordinator intake are preparation, not an observed holder publication or a PASS.

On direct start, each holder promptly reads only common plus its own prepared input and necessary bounded source context, authors its exact two granted source/record paths, and commits their first originals before sibling visibility. Record actual work/commit intervals and original raw/blob identities in only the holder's capture directory. Neither record is accepted. No invented wait or overlap, sibling instruction or shared inventory write is permitted. After both original seals, this Coordinator integrates the two real branches, retains both original blobs, and performs the granted handover, semantic, SLC alias retry and accepted-outcome repair/refusal decisions. Thirty active minutes exclude actual scheduler/authority wait; preserve partial output on exhaustion. The exact receiver actions and refusal conditions remain those in the packet and LEAD ruling.

Return sealed metadata only until both holders' originals exist, then exact observations/capture through the same direct channel. AC-7/AC-10 remain unstarted; the later honest initial BLOCKED EV/RF and one-Reviewer sequence is unchanged. This synchronization changes no live status, accepted knowledge, implementation Candidate or prior event.
