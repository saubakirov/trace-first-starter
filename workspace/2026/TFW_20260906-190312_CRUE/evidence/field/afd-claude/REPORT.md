# Field report — afd-claude

- Provider: claude
- Actual field start epoch: 1788814726.2930703
- Real field native identity: `4f310c1f-0e81-40d4-b215-ad1fd4a972be` (allocation identity was not reused)
- Child exit: `1`; timed out: `false`; duration: `1.15s`
- Outcome: STOPPED before update; field auth harness mismatch / provider reported Not logged in
- Prompt SHA-256: `93f1403f274cf0247ddc176e9b0feaca998d06d39338a16430b03a1177552351`; raw output is retained only in the private subject runtime.
- Safe report SHA-256: `0508ff9e8d7d37818aba0d39a491577e86c3c945a8c30de3314c8e3af3a02bc3`; stdout bytes/hash: `747` / `b417baa965681c965471394d8696c7d558b43c48df3e03205c3c6917f8ccf2d4`; stderr bytes/hash: `0` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

## Independent receiver reconciliation

version 2.1.0; receiver clean; source d6; no receipt

## Interpretation

The field auth volume exposed /run/tfw/auth/.credentials.json while CLAUDE_CONFIG_DIR pointed at /run/tfw/auth/claude; this is a harness authentication/setup failure, not evidence about tfw-update behavior.

## Secret-safe native final text, actions and metadata

The following private-runtime safe report preserves the actual final assistant text and action/check metadata for AC-9 comparison; credentials, account identifiers, raw HTTP/TLS/debug bodies and secret response content are excluded.

````json
{
  "actions_and_assistant_text": [
    {
      "assistant_text": "Not logged in · Please run /login",
      "event": "result",
      "session_id": "4f310c1f-0e81-40d4-b215-ad1fd4a972be",
      "stop_reason": "stop_sequence",
      "subtype": "success",
      "terminal_reason": "completed",
      "uuid": "bad5636a-bc64-4f2d-b47c-19923cb3dcb7"
    }
  ],
  "native_identity": {
    "is_error": true,
    "item_types": [],
    "json_records": 1,
    "model": null,
    "num_turns": 1,
    "record_types": [
      "result"
    ],
    "result_subtype": "success",
    "result_text_bytes": 34,
    "result_text_sha256": "ddcf5c1f4a3b398837003d800ea793d0a3ebb7ec0a1304b3186393460a7d5bd6",
    "session_id": "4f310c1f-0e81-40d4-b215-ad1fd4a972be",
    "session_id_present": true,
    "stop_reason": "stop_sequence",
    "terminal_reason": "completed",
    "uuid": "bad5636a-bc64-4f2d-b47c-19923cb3dcb7",
    "uuid_present": true
  },
  "provider": "claude",
  "raw_output_bytes": 747,
  "raw_output_retained_privately": true,
  "raw_output_sha256": "b417baa965681c965471394d8696c7d558b43c48df3e03205c3c6917f8ccf2d4",
  "slot": "afd-claude"
}
````
