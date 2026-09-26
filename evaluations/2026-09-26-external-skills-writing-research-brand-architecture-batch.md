# External skills evaluation — writing, research, delegation, brand and skill architecture batch

Date: 2026-09-26

## Scope

Repositories reviewed:

- https://github.com/docwriter-org/plain-writing-skill
- https://github.com/amElnagdy/delegate-skills
- https://github.com/mikubaka88/CCFA-Skills
- https://github.com/vladignatyev/brain-map-skill
- https://github.com/gauss314/skills
- https://github.com/nekocode/filetree-skill
- https://github.com/Rimagination/good-question
- https://github.com/fivetaku/fablize
- https://github.com/arnabbagxd/Brand-building-skills
- https://github.com/AGI-comming/functional-skill-creator

Evaluation followed the current `ARSENAL INDEX.md` and `stacks/evaluate-and-import-skill/STACK.md`.

## Summary

| Source | Class | Decision |
| --- | --- | --- |
| docwriter-org/plain-writing-skill | A/B | Adopt a flexible plain-writing layer focused on clarity, simple wording and literal explanation. Avoid hard-coding all style preferences as universal rules. |
| amElnagdy/delegate-skills | D/A | Strong delegation system, but highly dependent on local implementer CLIs, Node relays, trust/sandbox details and platform-specific runtime. Keep as technical reference. |
| mikubaka88/CCFA-Skills | A/B | Rich academic research/paper workflow with major overlap in academic-paper-orchestration, academic-rebuttal, experiment-design and publication-figure-engineering. Do not bulk import; retain as targeted reference. |
| vladignatyev/brain-map-skill | D/B | Useful knowledge-map artifact generator, but depends on Python/Cytoscape and a specific markdown/frontmatter graph model. Existing visualization skills cover the portable method. |
| gauss314/skills | D | Large finance/data connector catalog tied to specific APIs, scrapers and credentials. Evaluate individual sources only when a task requires them. Do not bulk import. |
| nekocode/filetree-skill | D/B | Useful repository manifest optimization and incremental summarization pattern, but tightly coupled to scripts, hooks, subagents and FILETREE.md workflow. Retain as reference. |
| Rimagination/good-question | A | Distinct research-question methodology with evidence sufficiency gate, falsifiability, rival hypotheses and pilot design. Adapted as research-question-design. |
| fivetaku/fablize | B/D | Strong completion/verification harness, but the Arsenal already covers verification, loops, debugging, planning and runtime checks. Runtime hooks and effort escalation are host-specific. No duplicate skill added. |
| arnabbagxd/Brand-building-skills | A/B | Broad brand strategy library. Adopt a compact evidence-aware brand-strategy core rather than dozens of overlapping brand/marketing skills. |
| AGI-comming/functional-skill-creator | A | Distinct methodology for maintaining complex skills as modular function pipelines with contracts, tests and traces. Adapted as functional-skill-architecture. |

## Adopted

### plain-writing
Source: `docwriter-org/plain-writing-skill`

Distinct value:
- literal, easy-to-read prose;
- jargon reduction;
- topic-sentence + support structure;
- consistent terminology;
- anti-puffery review pass.

Adaptation:
- did not impose all original stylistic bans universally;
- allows technical language when precise;
- defers to requested voice and domain conventions;
- integrated with `writing-quality` and `prose-lint`.

### research-question-design
Source: `Rimagination/good-question`

Distinct value:
- separates topic/problem/hypothesis/project;
- evidence sufficiency gate before domain-specific recommendations;
- rival hypotheses and falsifiers;
- short pilot and rejection-risk framing;
- explicit source-backed/inference/unknown ledger.

Adaptation:
- removed source-specific reference-card dependencies;
- uses the Arsenal's current web/research capabilities when freshness matters;
- avoids turning a scoring rubric into a mechanical final decision.

### functional-skill-architecture
Source: `AGI-comming/functional-skill-creator`

Distinct value:
- explicit function contracts for complex skills;
- orchestration kept separate from deterministic work;
- migration that preserves existing behavior;
- regression cases and traces tied to actual failures.

Adaptation:
- no mandatory Node runtime;
- no mandatory viewers, logging framework or generated scaffolding;
- scripts/traces only when the environment and complexity justify them;
- complements rather than replaces `skill-builder` and `project-skill-architecture`.

### brand-strategy
Source: `arnabbagxd/Brand-building-skills`

Distinct value:
- category framing;
- audience + competitor + positioning coherence;
- proof-aware differentiation;
- connection from strategy into voice, messaging and identity implications.

Adaptation:
- consolidated strategy/positioning/voice into one core skill;
- removed invented personas and unsupported competitor claims;
- current market claims require research or explicit hypothesis labeling;
- specialized logo and voice work remains routed to existing Arsenal skills.

## Retained as references, not imported

### delegate-skills
The methodology around lane-based delegation, explicit approval, implementer capability discovery and review-after-delegation is strong. However, the package depends on many external CLIs, relays, sandbox modes and local configuration. The Arsenal should reuse the conceptual discipline only when real delegation tools are available.

### CCFA-Skills
The family has useful academic lifecycle specialization, including idea review, literature, experiments, integrity checks, writing, rebuttal and visuals. Most of that is already represented in the Arsenal. Future academic gaps should evaluate individual CCFA skills instead of copying the family.

### brain-map-skill
The output is an interactive HTML graph with timeline and filters built by bundled scripts. Portable concepts are already addressed by visualization/web artifact capabilities. No Python/Cytoscape dependency was introduced.

### gauss314/skills
This is primarily a financial data/API/scraper catalog, including trading-related sources. Each source has its own operational and credential/security surface. No scraper, API integration or trading skill was imported from this batch.

### filetree-skill
The incremental-summary idea is useful:
- preserve summaries when file purpose did not change;
- prefer diff over full-file reread;
- centralize canonical language;
- prove coverage before declaring sync.

Its full implementation is script/hook/subagent dependent and too specific for a general Arsenal skill.

### fablize
Useful principles such as evidence-backed completion, sequential verified goals, causal debugging and renderer-based artifact checks already map to `verify-before-claim`, `loop-engineering`, `diagnosing-bugs`, `behavior-contract-validation` and `runtime-ui-verification`. The host-specific setup/hooks were not imported.

## Security and dependency review

- No installer, plugin setup, scraper, trading command, external CLI or bundled script was executed.
- Delegate systems were not treated as available unless the current ChatGPT environment actually exposes an equivalent tool.
- Financial/trading repositories were not imported as executable capabilities.
- Knowledge-map and filetree scripts were read as methodology only.
- Functional traces must redact sensitive data.
- Brand and research claims must distinguish evidence from hypotheses.
- External skills were adapted rather than allowed to override the Arsenal's canonical instructions.

## Result

New skills:
- `plain-writing`
- `research-question-design`
- `functional-skill-architecture`
- `brand-strategy`

The Arsenal index was updated to route to all four.
