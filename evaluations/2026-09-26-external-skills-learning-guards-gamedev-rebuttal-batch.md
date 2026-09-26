# External skills evaluation — learning, guards, gamedev, diagrams and rebuttal batch

Date: 2026-09-26

## Scope

Repositories reviewed:

- https://github.com/Kulaxyz/self-learning-skills
- https://github.com/alvinunreal/lazyskills
- https://github.com/amElnagdy/guard-skills
- https://github.com/openclaw/agent-skills
- https://github.com/kingbootoshi/directional-prompting
- https://github.com/gamedev-skills/awesome-gamedev-agent-skills
- https://github.com/DannyMac180/skills
- https://github.com/cclank/lanshu-animated-architecture-diagram
- https://github.com/alex-hyperagent/hyperagent-public-skills
- https://github.com/xiongqi123123/awesome-rebuttal

Evaluation followed `stacks/evaluate-and-import-skill/STACK.md` and the current `ARSENAL INDEX.md`.

## Summary

| Source | Class | Decision |
| --- | --- | --- |
| Kulaxyz/self-learning-skills | A | Adopt the verified golden-path capture pattern, but integrate it with existing learning/codification skills rather than copying tool-specific persistence logic. |
| alvinunreal/lazyskills | D | Useful external management/doctor tool for skill installations. Not a portable reasoning skill; do not import as an Arsenal skill. |
| amElnagdy/guard-skills | A/B | Strong guard-pass methodology. Most generic behavior overlaps with code-review, tdd, writing-quality and verify-before-claim. Keep as reference; do not duplicate all guards in this pass. |
| openclaw/agent-skills | A/B | Strong public skill discipline. Adopt black-box behavior-contract validation; other areas overlap with handoff/code review/session tooling or depend on external runtimes. |
| kingbootoshi/directional-prompting | B/A | Useful prompt-authoring discipline. Adopt a model-neutral version emphasizing explicit outcomes, success criteria, stopping conditions and positive actions. |
| gamedev-skills/awesome-gamedev-agent-skills | A/D | Rich game-development catalog and router. Too broad for wholesale import; retain as external vertical reference for future targeted gamedev skills. |
| DannyMac180/skills | B/D | Dynamic workflow and relay skills depend heavily on specific Codex/subagent primitives; explain-this overlaps strongly with teach/eli5/explanation-architecture. No new skill imported from this repo. |
| cclank/lanshu-animated-architecture-diagram | D/A | High-quality technical visual workflow, but dependent on bundled renderer, Python, Excalidraw and GIF tooling. Existing architecture-visualization/motion skills cover the portable methodology. |
| alex-hyperagent/hyperagent-public-skills | B/C | Collection of specialized JSON workflows. Useful as an idea catalog, but not imported wholesale because formats and tools are platform-specific and many entries overlap existing Arsenal domains. |
| xiongqi123123/awesome-rebuttal | A | Distinct academic rebuttal lifecycle with evidence, concern atomization, experiment triage and safety gates. Adapted into a portable Arsenal skill. |

## Adopted

### golden-path-capture
Source: `Kulaxyz/self-learning-skills`

Distinct value:
- promotion gate before converting a lesson into authoritative knowledge;
- verified path + named failure + ruled-out dead-end;
- explicit triage between procedure, fact and one-off;
- secrets hygiene;
- deduplication before creating a new skill.

Adaptation:
- removed automatic persistence assumptions and tool-specific skill directories;
- integrated conceptually with `retrospective-codify`, `session-learn`, `skill-builder` and `verify-before-claim`;
- no automatic write without an authorized repository/task context.

### directional-prompting
Source: `kingbootoshi/directional-prompting`

Distinct value:
- outcome block;
- checkable success criteria;
- explicit stopping condition;
- positive, action-oriented instruction language.

Adaptation:
- removed claims tied to specific model versions;
- kept negation when it is the clearest safety/scope mechanism;
- framed as an authoring/audit method rather than a universal law.

### behavior-contract-validation
Source: `openclaw/agent-skills`

Distinct value:
- black-box validation independent of source review;
- prewritten or derived behavior contract;
- clause-by-clause pass/fail/blocked/out-of-scope state;
- anti-false-positive probes.

Adaptation:
- removed fixed shell isolation requirements;
- mapped runtime interaction to whatever real tools are available;
- separated it from `code-review` and linked it to `runtime-ui-verification`.

### academic-rebuttal
Source: `xiongqi123123/awesome-rebuttal`

Distinct value:
- reviewer concern normalization and atomic concern ledger;
- evidence mapping;
- experiment triage;
- coverage gates;
- venue/anonymity/provenance checks;
- reviewer/AC stress test.

Adaptation:
- removed mandatory .awesome-rebuttal workspace, schemas, scripts, LaTeX environment and Overleaf-specific workflow;
- retained current venue rule verification as a requirement;
- integrated with `academic-paper-orchestration` and general research/writing skills.

## Not separately imported

### guard-skills
`docs-guard` has a valuable claim-verification framing and `test-guard` has useful test-quality rules. However:
- documentation truth checking overlaps `verify-before-claim`, `writing-quality`, `code-review`, and source-aware engineering;
- test quality overlaps `tdd`, `code-review`, and `codebase-design`.

These are retained as candidates for targeted updates to existing skills rather than copied as parallel guards.

### lazyskills
The repo is an application/TUI that scans skill installations, validates frontmatter, lock files and visibility across agents. Its value is operational tooling, not a portable skill. No installer or executable was run.

### gamedev catalog
The game-development catalog contains many useful vertical disciplines and engine-specific skills. It is too broad to import as a batch. Future game-development tasks should evaluate only the relevant engine/discipline files.

### DannyMac180/skills
- `codex-dynamic-workflows`: overlaps `graph-engineering`, `project-planning`, `loop-engineering` and current tool orchestration; several primitives are environment-specific.
- `codex-relay`: depends on task/thread primitives not generally available and is not portable.
- `explain-this`: overlaps `teach`, `eli5`, `explanation-architecture` and memory capabilities; its persistent learner-state implementation is tool-specific.
- `claude-mod-builder`: product/platform-specific.

### lanshu-animated-architecture-diagram
The style system and validation discipline are useful, but deterministic rendering depends on its Python renderer, Excalidraw contract and media tools. Portable ideas are already covered by `architecture-visualization`, `editable-visual-design`, `motion-asset-engineering` and `visual-explanation-sketch`.

### hyperagent-public-skills
The repository exposes platform-specific JSON skill packages spanning brand, media, simulation, design and operations. It is useful as a pattern catalog, but bulk adoption would create many overlapping skills and carry runtime assumptions that are not portable.

## Security review

- No external installer, shell script, renderer or executable was run.
- Repositories with bundled scripts/tooling were evaluated from source only.
- Tool-specific instructions were not copied as if their runtimes existed in ChatGPT.
- Secret values must never be captured in golden paths or validation evidence.
- Academic rebuttal workflows must not invent results, venue permissions, citations or reviewer positions.
- External prompt/instruction methodologies were adapted rather than treated as authoritative system-level instructions.

## Result

New skills:
- `golden-path-capture`
- `directional-prompting`
- `behavior-contract-validation`
- `academic-rebuttal`

The current Arsenal index was updated to route to them.
