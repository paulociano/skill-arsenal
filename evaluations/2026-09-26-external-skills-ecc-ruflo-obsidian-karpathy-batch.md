# External skills evaluation — ECC, Ruflo, Obsidian CLI and Karpathy guidelines batch

Date: 2026-09-26

## Scope

Repositories reviewed:

- https://github.com/affaan-m/ECC
- https://github.com/ruvnet/ruflo
- https://github.com/pablo-mano/Obsidian-CLI-skill
- https://github.com/multica-ai/andrej-karpathy-skills

Evaluation followed the current `ARSENAL INDEX.md` and `stacks/evaluate-and-import-skill/STACK.md`.

## Summary

| Source | Class | Decision |
| --- | --- | --- |
| affaan-m/ECC | A/D | Large agent-harness operating system with planning, verification, memory, security scanning and hundreds of skills. Most portable methods already exist in the Arsenal. Retain as a broad external reference and absorb only distinct principles. |
| ruvnet/ruflo | A/D | Large meta-harness with swarms, memory, routing, hooks, observability and security. Strong system, but highly runtime-specific and heavily overlapping with existing orchestration, memory, routing and evaluation skills. Retain as technical reference. |
| pablo-mano/Obsidian-CLI-skill | D/A | Excellent app-specific operational skill for Obsidian CLI. Useful only when the actual Obsidian CLI/runtime is available. Do not create a generic Arsenal skill that pretends the integration exists. |
| multica-ai/andrej-karpathy-skills | A/B | Compact and highly portable coding discipline around explicit assumptions, simplicity, surgical diffs and verifiable goals. Adapted as `surgical-engineering`. |

## Adopted

### surgical-engineering
Primary source: `multica-ai/andrej-karpathy-skills`

Distinct value:
- explicit assumptions before coding;
- simplicity over speculative abstraction;
- surgical edits tied directly to the request;
- cleanup limited to orphans created by the change;
- success criteria defined before implementation;
- verification of the actual goal rather than generic "it works".

Additional reinforcement:
- ECC's plan/test/implement/review/verify discipline;
- Ruflo's emphasis on verification and bounded orchestration.

Adaptation:
- removed any requirement to stop and ask on every ambiguity; task-critical ambiguity is surfaced, while routine engineering choices remain autonomous;
- integrated with existing `tdd`, `diagnosing-bugs`, `code-review`, `verify-before-claim` and `agent-choice-audit`;
- no harness-specific hooks, commands or persistent runtime were imported.

## Retained as references

### ECC
ECC is an agent-harness operating system rather than one portable skill. It includes:
- planning and implementation agents;
- verification loops;
- continuous learning/memory;
- security scanning;
- parallelization;
- rules, hooks and many platform adapters.

The Arsenal already contains strong coverage across:
- `project-planning`
- `tdd`
- `code-review`
- `verify-before-claim`
- `golden-path-capture`
- `multi-agent-orchestration`
- `skill-security-review`
- `llm-observability-evaluation`
- `project-skill-architecture`

Bulk import would create large duplicate surfaces and runtime assumptions.

### Ruflo
Ruflo combines:
- swarms;
- persistent memory;
- multi-model routing;
- hooks;
- observability;
- ADR/DDD/SPARC workflows;
- cost tracking;
- security;
- plugins and remote/federated agents.

Portable methodology overlaps heavily with:
- `multi-agent-orchestration`
- `model-routing-gateway`
- `graph-engineering`
- `llm-observability-evaluation`
- `domain-modeling`
- `decision-analysis`
- `loop-engineering`
- `functional-skill-architecture`

The runtime-specific CLI/MCP/plugin system was not imported.

### Obsidian CLI skill
This is a well-structured integration skill covering note CRUD, daily notes, search, tasks, links, properties, sync, history, plugins and developer commands.

Decision:
- do not create an Arsenal skill that claims direct Obsidian access when the current environment may not expose the official CLI;
- retain it as an external integration reference;
- if an Obsidian connector or executable becomes available in a future environment, evaluate a capability-specific skill then.

Useful portable patterns:
- capability check before action;
- explicit vault targeting;
- structured command reference kept out of the main skill;
- distinction between explanation requests and action requests;
- app-specific troubleshooting kept near the integration rather than generalized.

## Security and dependency review

- No ECC installer, Ruflo installer, MCP server, hook package or plugin was executed.
- No Obsidian command was executed and no local vault access was assumed.
- ECC/Ruflo memory, hooks, agents and security surfaces were treated as implementation-specific capabilities.
- Large external skill catalogs were not mirrored wholesale.
- The Karpathy-inspired guidance was adapted as methodology rather than copied as global system instructions.

## Result

New skill:
- `surgical-engineering`

The Arsenal index was updated to route to it.
