# Observations — afd-claude

- Slot consumed exactly once; no retry, continuation, resume or cross-slot feedback.
- The field auth volume exposed /run/tfw/auth/.credentials.json while CLAUDE_CONFIG_DIR pointed at /run/tfw/auth/claude; this is a harness authentication/setup failure, not evidence about tfw-update behavior.
- Independent reconciliation: version 2.1.0; receiver clean; source d6; no receipt.
- Project-check interpretation: only commands in `harness/PROJECT-CHECK-SET__20260908.md` count; unavailable, placeholder and policy-forbidden checks remain non-verifying.
