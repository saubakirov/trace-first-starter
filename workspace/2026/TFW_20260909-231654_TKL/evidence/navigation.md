# Actual source and compiled navigation evidence

Candidate `27cdb701b91c5b45b9f54b3e98c9ad67635b3e30` changes only nested record inclusion at the compiler
boundary. SLC's complete-link resolver remains unchanged. The final run 13 production build exited 0;
its actual stdout/stderr/receipt are in `checks/13-full/build/`. Seven final HTML files and their hashes
are preserved in [13-output/manifest.json](navigation/13-output/manifest.json). The corresponding
run 11 generation remains separately preserved; neither is called run 08 bytes.

The actual run 08 in-app browser observation opened local served output at `127.0.0.1:60801` during
15:47:42–15:50:26 +05. [Original observation account](navigation/08-browser/observation.json) is an
Executor-written account of actual browser tool results, not a provider transcript/export. The local
server was stopped and the temporary tab closed; no site was published.

| Family | Actual intended destination |
|---|---|
| Independent record | `knowledge/records/TKL-20260913-01/` |
| Relation to legacy D37 | `knowledge-index/#d37` |
| Legacy topic | `knowledge/process/` |
| Legacy RES source | `tasks/TFW-22__coordinator_research_enrichment/RES__TFW-22__coordinator_research_enrichment/` |
| Relation to legacy D82 | `knowledge-index/#d82` |
| Current owner decision | `tasks/2026/TFW_20260909-231654_TKL/journal/20260913-141400__handoff__8c2a/` |
| Current HL artifact | `tasks/2026/TFW_20260909-231654_TKL/HL-TFW_20260909-231654_TKL/` |

The record, D37, topic, legacy RES, D82 and owner-decision navigation worked through actual opened
links. The HL click left the URL unchanged and waitForURL timed out; the observed exact href was then
opened directly and reached the real HL. That failed click is not relabelled success. Browser content
export was unsupported. The attempt to preserve run 08 HTML after a later build started found those
files already cleaned; no later bytes were mislabeled as 08. Run 11 and final 13 outputs were copied
from their own actual builds.

The final 13 integration suite verifies all seven exact destinations. Five preserved HTML pages
(record, topic, legacy RES, current owner decision and current HL) are byte-identical between 11 and
13; the two knowledge-index captures differ because of the actual current Architecture Map sentence
correction. Both legacy anchors remain. The browser observation is bounded to run 08; stable links,
source applicability and final output assertions support the later generation without claiming a new
browser run. Legacy topic/D/source meaning stays preserved. None of this establishes AC10's unseen
first answer or AC7's actual receiver adoption. Later EV/RF/control prose was absent from the Candidate
build and needs its own applicable final-output judgment if selected for acceptance.
