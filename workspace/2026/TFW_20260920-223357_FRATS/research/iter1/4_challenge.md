# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. Attack every configuration; preserve a survivor only when its evidence and boundary remain explicit.
> **Test:** "Would the surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260920-223357_FRATS](../../HL-TFW_20260920-223357_FRATS.md)
> Goal: Refactor TFW from field evidence so its artifacts remain behaviorally complete while routine coordination moves from repeated dialogue to concise durable traces.
> Boundary: focused iteration-1 challenge only; H12–H17 and final interaction architecture remain iteration 2.

## Consistency Check

Pair checks below apply when both alternatives are asserted about the same artifact, update or
measurement epoch. Separating epochs can make an otherwise incompatible pair valid.

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|---|---|---|---|---|
| D1: receiver state | concurrent uncommitted framework update | D2: receipt relation | receipt condition resolved later | They cannot describe the same snapshot: RYC demonstrates that a sealed receipt and an uncommitted working result can coexist before later resolution. |
| D1: receiver state | clean but installed release is behind | D2: receipt relation | newer/current state lacks a settled committed receipt | “Behind” names the installed state; an uncommitted newer application is a second epoch and must not be folded into it. |
| D3: measurement continuity | exact historical replay | D6: filename state | current ten-command surface treated as the same historical issuance/runtime set | RCFR's exact selector includes eleven commands and Resume; the current surface has ten. Exact replay is historical, while current comparison needs a bridge. |
| D3: measurement continuity | exact historical replay | D4: runtime charge | all tracked `.tfw` text treated as charged runtime context | The accepted selector charges only discovered runtime sources/ranges; all-tracked text includes dormant migrations, receipts, adapter sources and history. |
| D5: rule/delivery relationship | foreign/customized content preserved | D2: receipt relation | “does not equal canonical” treated as current framework drift | Preservation outside framework ownership is an intended disposition, not parity failure. |
| D5: rule/delivery relationship | sole canonical owner | D6: filename state | historical non-current grammar used as new issuance authority | A readable historical artifact cannot become a second current producer rule merely because it exists or is cited. |
| D7: rule-compliance cause | native capability/readback limit | D8: principal context | missing principal treated as title authority | Title transport and principal/mandate resolution are separate; neither can prove the other. |

**Surviving configurations:**

All twelve Extract rows survive after their stated epoch and authority bounds are retained; none
contains the incompatible pair as a same-fact assertion. Their useful grouping is:

| Configs | D1 receiver family | D3 measurement family | D5/D6 rule and filename family | D8 identity family | Notes |
|---|---|---|---|---|---|
| C1, C6 | clean/committed | historical-only replay or explicit bridge | canonical owner with current/revision grammar | owner or selected-LEAD root | Exact replay remains historical; bridge remains labeled non-equal. |
| C2, C12 | clean/committed | bridge or successor measure | installed/canonical delivery with phase/revision grammar | no named operational principal | No-principal operation does not remove task, role, owner, gate or `via`. |
| C3, C8 | clean but behind | successor or historical measure | managed/foreign content with revision/history | owner or shared/multiple-human | A clean tree can still be stale, and shared-human attribution still requires a question. |
| C4, C7, C11 | project/task dirt | bridge/successor measure | preserved, managed or exact delivery | owner, LEAD or no-principal operational role | Project dirt does not itself establish update failure or adapter drift. |
| C5, C10 | concurrent uncommitted framework update | unavailable-at-epoch or successor measure | exact/foreign delivery with current grammar | shared or owner | Preserve the epoch; do not chase the moving receiver or infer an actor. |
| C9 | clean/committed | explicit bridge | managed delivery plus historical readability | selected-LEAD root | Historical names and native limits can coexist with a current LEAD without becoming authority. |

**Unexpected survivors:**

- **C5/C10:** a sealed receipt and an uncommitted update tree can coexist. The receipt can honestly
  describe the attempt without proving committed current state.
- **C8:** a clean-but-stale receiver with placeholder checks can remain internally consistent; it is
  limited evidence, not automatically a failed update.
- **C12:** an owner-launched operational role can retain task/role/owner/gate/transport traceability
  without a named agent principal, provided the multiple-human/shared-device and delegated-LEAD cases
  take a different branch.

## Findings

### C1: Fresh bridge replay survives; an all-tracked selector changes the question

The bridge was rerun in a fresh Python process at:

```text
source HEAD: 912be45b4106c64c1203aa0cf387eabc8ad9e465
relevant dirt under .tfw, AGENTS.md, CLAUDE.md, .agents, .claude: 0 paths
run time: 2026-09-20T23:32:56.4150563+05:00
accepted candidate: 25d0e89afe48144c79c11324ff09d300b76dd6e9
```

Later Coordinator commits through `34f54d4` changed only task-local FRATS planning inputs; a path
diff from the recorded source HEAD found no change to the measured framework/adapter surfaces.

Fresh result:

```text
ACCEPTED_10_TRAJECTORY=108942
CURRENT_10_TRAJECTORY=113465
ACCEPTED_10_ACTIVE_CORPUS=31529
CURRENT_10_ACTIVE_CORPUS=37045
```

Exact reproduction recipe (run from a checkout whose relevant surfaces equal recorded source HEAD):

```powershell
$py = @'
import re
import subprocess
import sys
import types
from pathlib import Path

root = Path(r'D:\projects\research\steps-framework')
accepted = '25d0e89afe48144c79c11324ff09d300b76dd6e9'
current_ref = subprocess.check_output(['git','rev-parse','HEAD'], cwd=root, text=True).strip()
source = subprocess.check_output(
    ['git','show',accepted + ':docs/scripts/test_runtime_context.py'],
    cwd=root, text=True, encoding='utf-8')
source = source.replace(
    'PROJECT_ROOT = Path(__file__).resolve().parents[2]',
    'PROJECT_ROOT = Path(' + repr(str(root)) + ')')
name = 'fresh_rcfr_bridge'
module = types.ModuleType(name)
module.__file__ = '<memory>'
sys.modules[name] = module
exec(compile(source, '<fresh_rcfr_bridge>', 'exec'), module.__dict__)
ns = module.__dict__
ns['SECONDARY_COMMANDS'] = tuple(
    c for c in ns['SECONDARY_COMMANDS'] if c != '/tfw-resume')
ns['RUNTIME_VARIANTS'] = (
    *ns['PRIMARY_VARIANTS'], *ns['SECONDARY_COMMANDS'],
    '/tfw-handoff:revise', *ns['LIFECYCLE_VARIANTS'])
historic = ns['SourceTree'].from_git(root, accepted)
current = ns['SourceTree'].from_path(root)
commands = (*ns['PRIMARY_VARIANTS'], *ns['SECONDARY_COMMANDS'])

def trajectory(tree):
    return sum(ns['measure_graph'](
        tree, ns['discover_read_graph'](tree, command)) for command in commands)

def all_tracked_tfw(ref):
    paths = subprocess.check_output(
        ['git','ls-tree','-r','--name-only',ref,'--','.tfw'],
        cwd=root, text=True, encoding='utf-8').splitlines()
    words = text_files = binary_files = 0
    for path in paths:
        data = subprocess.check_output(['git','show',ref + ':' + path], cwd=root)
        try:
            text = data.decode('utf-8')
        except UnicodeDecodeError:
            binary_files += 1
            continue
        words += len(re.findall(r'\S+', text))
        text_files += 1
    return words, text_files, binary_files

print('ACCEPTED_REF=' + accepted)
print('CURRENT_REF=' + current_ref)
print('ACCEPTED_10_TRAJECTORY=' + str(trajectory(historic)))
print('CURRENT_10_TRAJECTORY=' + str(trajectory(current)))
print('ACCEPTED_10_ACTIVE_CORPUS=' + str(ns['active_runtime_corpus_words'](historic)))
print('CURRENT_10_ACTIVE_CORPUS=' + str(ns['active_runtime_corpus_words'](current)))
for label, ref in [('ACCEPTED_ALL_TRACKED_TFW', accepted),
                   ('CURRENT_ALL_TRACKED_TFW', current_ref)]:
    words, text_files, binary_files = all_tracked_tfw(ref)
    print(label + '_WORDS=' + str(words))
    print(label + '_TEXT_FILES=' + str(text_files))
    print(label + '_BINARY_FILES=' + str(binary_files))
'@
& python -X utf8 -c $py
```

Plausible alternate selector: every Git-tracked UTF-8 file under `.tfw`, counted once by `\S+`.
It produced:

| Selector | Accepted | Current | Delta |
|---|---:|---:|---:|
| all tracked `.tfw` words | 98,297 across 71 text files | 116,162 across 80 text files | +17,865 (+18.2%); zero binary files on both sides |
| active ten-command unique corpus | 31,529 | 37,045 | +5,516 (+17.5%) |

The alternate corroborates the direction of growth but not runtime exposure. It counts migrations,
receipts, dormant adapter sources, history and forms even when no role reads them. The active selector
counts discovered charged sources/ranges and deduplicates contained ranges. The similar percentages
are coincidental support for “the tree grew,” not proof that every tracked word consumes agent context.
The published eleven-command result also cannot be used as the current denominator because Resume no
longer exists. The ten-command bridge survives this attack precisely because it states its changed
command set and applies it symmetrically to both epochs.

### C2: The largest growth owners contain required behavior and repeated expression

| Growth owner / range | Actual readers | Consequence if the job disappears | Challenge result |
|---|---|---|---|
| `conventions.md` → Task Statuses / phase state | Plan routes work; Handoff and Review transition only the selected carrier; Coordinator closure reconstructs terminal state | wrong role/phase runs, history is overwritten, or a task closes from an invalid carrier | Required semantic owner. Compression must preserve the state machine; form details duplicated with templates remain candidates only after a reader-by-reader check. |
| Scope/value accounting ranges | Plan fixes the prospective selector/authority; Handoff fixes Candidate and actual membership; Review independently recomputes | late denominator changes, hidden scope growth or self-authorized overruns | Required new control, not removable merely because it adds words. |
| Knowledge use/handover/qualification ranges | every producing role at return; Docs/Knowledge at qualification | material insight disappears, stale claims are applied, or a receiver publishes unqualified knowledge | Required behavior. The separation of producer handover from qualification has distinct readers/consequences. |
| Session identity plus acting-principal rules | six workflows read title rendering; Research/Handoff/Review repeat the binding/question table inline | sessions become hard to navigate or acts are misattributed on shared/multiple-human machines | Mixed. Rendering has one shared owner. `Which handle a machine acts as` is not selected by the ten-command read graph while three workflows repeat its algorithm; this is concrete repeated expression/readerless-owner evidence, but the safety branch itself must stay. |
| `workflows/update.md` | `/tfw-update` through exact Claude/Antigravity copies and a Codex dispatcher | wrong source, overwritten customization, split semantic group, unsafe cleanup, false verification or receipt-as-state errors | Mostly required algorithm with observed firing: Helpdesk caught basename masking and concurrent HEAD movement; RYC demonstrated changing epochs. The receipt template owns output fields rather than duplicating the execution order. |
| `.tfw/README.md` | Init/Update classify receiver purpose; Reviewer/Plan use North Star/value ranges | customized purpose can be overwritten or a result can pass its TS while failing purpose | Purpose is required. Charging the whole philosophical document where a named North-Star range would suffice remains a section-addressing candidate; deletion is not supported. |

This falsifies the broad form of H4 (“most growth is only repeated prose”). Much of the increase
implements new accounting, knowledge, migration and state behavior. A narrower H4 survives: repeated
principal-selection prose and potentially over-broad North-Star reads coexist with required growth in
the same high-exposure owners. H8 remains feasible only as source/range consolidation with preserved
consequences, never as a percentage-driven cut.

### C3: Explicit producer emission closes H10 without renaming history

Attack: perhaps the CRUE hyphenated TS/RF files prove a second grammar is needed because 32 Markdown
files reference the TS name and 23 reference the RF name.

Counter-evidence: those references resolve because both historical files remain present. Current
conventions authorize only double-underscore issuance, current tasks demonstrate that form, and no
current workflow/skill authorizes `TS-{ID}` or `RF-{ID}`. Handoff and Review consume selected task
state plus governing artifact lineage; they do not require historical files to be renamed.

Surviving repair class for later planning: each producer emits the topology-aware filename selected
from the existing naming table at its write gate:

- Plan: single/phase TS and TS revision;
- Handoff: single/phase ONB and RF, with append-not-sibling return behavior;
- Review: single/phase REVIEW and REVIEW revision;
- Research: keep the already explicit `research/iterN/RES.md` path.

A single hard-coded filename in a generic template would fail phase and revision cases; explicit
producer emission must be topology-aware. Historical CRUE remains readable and cited. H10 is supported:
the defect is incomplete producer emission plus attractive precedent, not a necessary competing
current grammar.

### C4: Conditional principal resolution survives four falsification cases

| Attack | What would falsify the conditional rule | Observed constraint | Survivor |
|---|---|---|---|
| several humans | skipping identity could attribute an act to the wrong human | task owner does not prove which human is operating | retain one short question when accountable human is ambiguous |
| shared/copied device binding | a project-root mapping may be stale or copied | current rule already treats shared/copied binding as unresolved | retain the question; never trust binding as authentication or authority |
| same-root owner versus selected LEAD | one static project binding cannot express session mode | LEAD requires mandate, stable agent principal and exact root unit; owner-launched non-AT role has none | resolve principal when stable delegation/provenance is actually required; task/mandate state, not title, selects the branch |
| AT child using the same principal | a shared profile could be mistaken for inherited authority | actual unit address, parent, scope, channel, dispatch and origin remain mandatory | principal may describe provenance but never replaces unit/dispatch facts |

Additional attacks do not overturn the distinction:

- Commit attribution uses the AI product name (`codex`) plus task/scope/role; it does not require a
  stable `team/{handle}` principal.
- Optional `writer`, required accountable human/owner, actual non-empty `via`, workflow role, task
  address and gate recipient are separate fields; naming one agent cannot manufacture authority.
- A stable named principal may still have a durable delegation/provenance job for a human-facing LEAD,
  but that is H12/H13/H16 territory assigned to iteration 2.

H11 survives in refined form: unconditional per-session principal selection is not necessary for a
bounded owner-launched non-AT operational role when no stable agent attribution is required, but the
question remains mandatory for ambiguous humans/shared devices and explicit stable delegation.

### C5: Receiver counterexamples limit H5 to a risk typology

- **Helpdesk counterexample:** the receipt documents real update hazards, but the current tree is
  clean. An observed hazard did not imply persistent receiver failure.
- **KazNPU counterexample:** the tree is clean under `.tfw` but stale at 3.1.0; its 27 current dirty
  paths are unrelated content. Dirt count is not update quality.
- **AFD counterexample:** the receipt closed its historical-container decision while leaving project
  task work and tests outside update authority. Preservation can be correct even when the project is red.
- **RYC counterexample:** the update receipt can be complete while the update remains uncommitted in
  Git. Receipt completeness and repository landing are separate facts.

H5 is therefore supported only as a source-bound typology: ownership/customization, concurrency and
verification quality repeatedly shape update risk. Four selected receivers do not establish cluster
frequency, universal causation or that payload copying is unimportant.

### C6: Iteration-1 hypothesis dispositions after attack

| Hypothesis | Disposition | Grounds |
|---|---|---|
| H1 | unresolved | One exact Codex title mutation/readback succeeded; no source-bound failure sample or Claude-native test isolates placement versus capability. The identity question was a different gate. |
| H4 | partially refuted and narrowed | +17.5% active-corpus growth is real, but large additions include necessary accounting, knowledge, update and state behavior. Repeated identity prose and broad purpose reads remain concrete candidates. |
| H5 | partially supported | Recurrent risk dimensions exist; the corpus cannot support frequency/universal-cause claims. |
| H8 | open but measurable | Exact historical guarantees replay and a current bridge exists. Specific consolidation candidates exist, but semantic preservation has not been implemented or proven. |
| H9 | unresolved | No controlled correlation across placement, conflicts, loaded scope and raw length exists. Current success shows long instructions do not deterministically cause failure. |
| H10 | supported | One current grammar exists; topology-aware producer emission is incomplete; historical names can remain readable without new issuance. |
| H11 | supported in refined conditional form | Human/shared-device ambiguity and explicit LEAD delegation require identity resolution; bounded owner-launched non-AT operation need not invent a named agent principal. |

Owner inputs H12–H17 and S15–S19 are retained as iteration-2 hypotheses/insights only. This stage did
not test persistent LEAD architecture, single mutating lanes, sibling collisions, capability sets,
least-privilege enforcement or commit-provenance architecture.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Fresh bridge replay is stable at a clean recorded source epoch; the all-tracked selector exposes denominator sensitivity without overturning the growth signal. | Iteration 2 must challenge architecture and native provider behavior; later implementation evidence must prove any reduction preserves the named consequences. |
| Required new behavior and concrete repeated expression are separated by actual readers and failure consequences. | Coordinator must decide which refinements enter planning; Researcher does not edit HL or framework. |
| H10 survives with a topology-aware producer-emission repair class and no historical rename. | Planning must specify every producer/consumer and revision form before implementation. |
| H11 survives only as a conditional rule preserving human/shared/LEAD/child safety cases. | Iteration 2 must test whether named principals add unique durable delegation/provenance value. |
| H1 and H9 remain honestly unresolved; H4/H5 are narrowed rather than overclaimed. | Native Codex/Claude and interaction-topology challenge belongs to iteration 2. |

**Sufficiency:**
- [x] External source used? — fresh immutable/current Git replay, live workflow/template/manifest readers, receiver receipts and exact historical references.
- [x] Briefing gap closed? — measurement, growth causes, filename issuance, identity counterexamples and receiver causal limits were attacked.
- [x] Pairwise incompatibility checked? Surviving configurations listed? — seven incompatible same-fact pairs and all twelve bounded survivors are recorded.

Stage complete: YES
→ User decision: pending Coordinator gate
