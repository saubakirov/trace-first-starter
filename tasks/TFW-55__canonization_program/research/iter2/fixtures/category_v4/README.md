# TFW55-I2-CATEGORY-FILEREAD-v4

Status: **PENDING EXECUTION-INSTRUMENTATION EXTRACT GATE — ZERO RUNS**

The coordinator authorized category v3 conditionally: actual dispatched scorer-prompt bytes had to be verifiable from orchestration trace. The collaboration runtime does not expose a post-dispatch copy/hash of the message sent to a subagent. No v3 run was started, because hashing the intended file or a reconstructed string would not satisfy that condition.

v4 implements the coordinator-directed file-read alternative. It changes delivery only. The experimental category and scorer content remains exactly the hash-guarded v2/v3 content.

For every fresh isolated critic or scorer:

1. Root verifies frozen v2, every v3 checksum, and the selected input hash.
2. The agent may invoke only `file_read_prompt.ps1` for the named input.
3. The reader independently repeats all upstream checks, validates the selected file and writes a run-specific pre-read attestation.
4. It emits the exact strict-UTF-8 file content without adding a newline; that stdout is the sole experimental prompt.
5. The agent writes its output once to the assigned raw-output file. Root hashes it before mechanical scorer assembly and never normalizes it.

Old invalidated v2 outputs are forbidden inputs. v3 has zero runs. A newly authorized v4 run restarts the complete category family at Q7 and retains all v2 mapping-seal, opaque-scoring and full-family replication rules.

No run is authorized until this package has a coordinator gate.
