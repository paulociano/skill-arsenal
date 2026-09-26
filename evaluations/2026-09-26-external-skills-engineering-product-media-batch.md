# External skill/repository evaluation — engineering, product, healthcare and media batch

Date: 2026-09-26

## Scope

Repositories reviewed:

- https://github.com/maziyarpanahi/openmed
- https://github.com/addyosmani/agent-skills
- https://github.com/phuryn/pm-skills
- https://github.com/refactoringhq/tolaria
- https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools
- https://github.com/obra/superpowers
- https://github.com/harry0703/MoneyPrinterTurbo
- https://github.com/mattpocock/skills

The review followed the Arsenal stack `evaluate-and-import-skill`: compare against the current Arsenal first, preserve useful methodology, avoid incompatible agent-specific commands, review dependency/security implications, and prefer extending existing capabilities over cloning repositories wholesale.

## Summary decision

| Source | Class | Decision |
| --- | --- | --- |
| maziyarpanahi/openmed | D | Do not import as a generic skill. Treat as a technical healthcare-AI reference requiring its own runtime/models and deployment validation. |
| addyosmani/agent-skills | A/B | Strong methodology, but broad overlap with existing engineering skills. Absorb only missing patterns in future targeted evaluations rather than bulk import. |
| phuryn/pm-skills | A/B | Useful PM methodology with significant overlap in discovery, prioritization, planning and metrics. Keep as a source for targeted gap-filling. |
| refactoringhq/tolaria | D | Primarily a technical system/repository rather than a portable single skill. Evaluate architecture/workflows separately before any import. |
| x1xhlol/system-prompts-and-models-of-ai-tools | B/C | Useful comparative corpus for agent design and prompt research, not a trustworthy drop-in skill source. Do not mirror system prompts into the Arsenal. |
| obra/superpowers | A/B | Strong engineering lifecycle methodology, largely covered by existing Arsenal skills. Its main value is orchestration patterns rather than duplicated skills. |
| harry0703/MoneyPrinterTurbo | D/B | Useful as a technical/media pipeline reference. Existing Arsenal content/video skills already cover much of the conceptual workflow; avoid importing provider/runtime specifics. |
| mattpocock/skills | A | High-value, composable engineering methodology. Most headline skills overlap, but domain modeling, deep-module/codebase design and merge-conflict resolution add distinct reusable behavior and were adapted. |

## Adopted from mattpocock/skills

### domain-modeling

Adopted as `skills/domain-modeling/SKILL.md`.

Distinct value:
- shared canonical domain language;
- explicit separation of domain glossary from implementation details;
- edge-case scenario stress tests;
- cross-checking code against stated domain semantics;
- sparing ADR criteria.

Portability changes:
- removed assumptions about fixed repository paths;
- removed agent-specific invocation mechanics;
- retained optional glossary/context and ADR outputs without requiring a specific tool.

### codebase-design

Adopted as `skills/codebase-design/SKILL.md`.

Distinct value:
- deep-module framing based on interface leverage;
- explicit seam/adapter/locality vocabulary;
- deletion test for shallow abstractions;
- interface-as-test-surface principle;
- YAGNI rule for hypothetical seams.

Portability changes:
- removed subagent requirements;
- removed HTML/Tailwind/Mermaid reporting as mandatory behavior;
- retained hot-spot-aware architecture review as a heuristic rather than a fixed command.

### merge-conflict-resolution

Adopted as `skills/merge-conflict-resolution/SKILL.md`.

Distinct value:
- resolves conflicts by primary-source intent, not line preference;
- preserves both intents when compatible;
- forbids opportunistic unrelated refactoring;
- validates the merged state with project checks.

Portability changes:
- removed assumptions that a local shell is always available;
- reframed command-specific steps as capability-dependent operations.

## mattpocock/skills overlap intentionally not duplicated

The following were not re-imported because the Arsenal already has equivalent or materially overlapping capabilities:

- `tdd`
- `diagnosing-bugs`
- `code-review`
- `to-spec`
- `to-tickets`
- `handoff`
- `teach`
- `wayfinder`
- grilling / grill-me / grill-with-docs concepts
- research workflow
- architecture review concepts now consolidated into `codebase-design`

`writing-for-agents` is valuable methodology, especially context pointers, progressive disclosure, completion criteria and pruning. It is not imported as a separate skill in this pass because much of that behavior belongs in `skill-builder`, `project-skill-architecture`, `source-to-skill` and Arsenal authoring conventions. It is a candidate for a focused future update to those skills.

## Security and dependency review

### General
No installer, script or executable from the reviewed repositories was run as part of this evaluation. Source material was read and adapted manually.

### openmed
High dependency footprint: Python/runtime packages, model artifacts, possible network model downloads, optional remote providers, and clinical/PII handling. Any future integration must validate model licenses, privacy behavior and clinical fitness. It is not treated as evidence of regulatory compliance.

### agent-skills / superpowers / mattpocock skills
Several instructions assume specific agents, local shell commands, plugins, subagents, worktrees or repository mutation. Those mechanics were not copied blindly. Only portable process rules were retained.

### system-prompts-and-models-of-ai-tools
Contains third-party system prompts/configurations and possibly reverse-engineered or leaked operational material. Treated only as comparative research material. No confidential-looking prompt corpus is copied into the Arsenal.

### MoneyPrinterTurbo
Large technical dependency surface including Python, Docker, media tooling and multiple third-party model/API providers. The Arsenal should reuse only provider-neutral workflow concepts unless a task explicitly needs the runtime.

### Tolaria
Large repository and toolchain surface. No code was executed. Any future adoption requires a narrower technical/security review.

## Result

New reusable Arsenal skills created:
- `domain-modeling`
- `codebase-design`
- `merge-conflict-resolution`

The remaining repositories are retained as evaluated external references rather than bulk-imported collections.

## Sources

Primary repository URLs listed in Scope. The current canonical Arsenal index and `stacks/evaluate-and-import-skill/STACK.md` were used as routing and adoption rules.
