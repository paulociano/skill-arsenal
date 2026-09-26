# External skills evaluation — repo docs, visual, game, customer and document conversion batch

Date: 2026-09-26

## Scope

Repositories reviewed:

- https://github.com/dmmulroy/skills
- https://github.com/Cuimao777/eterna-image2image-skill
- https://github.com/YurunChen/repo-docs-skills
- https://github.com/dzhng/skills
- https://github.com/majidmanzarpour/threejs-game-skills
- https://github.com/jakubkrehel/skills
- https://github.com/Kappaemme-git/codex-first-customer-finder-skill
- https://github.com/wy51ai/edulab
- https://github.com/hajimi-kun/latex-to-word-workflow

Evaluation followed the current `ARSENAL INDEX.md` and `stacks/evaluate-and-import-skill/STACK.md`.

## Summary

| Source | Class | Decision |
| --- | --- | --- |
| dmmulroy/skills | A/B | Strong TypeScript and engineering discipline, with substantial overlap in domain modeling, codebase design, TDD and specs. Retain as targeted reference. |
| Cuimao777/eterna-image2image-skill | B/D | Useful image-to-image aesthetic direction and preservation constraints, but largely style-specific and tied to image editing/generation capabilities. Do not create a narrow ETERNA-branded Arsenal skill. |
| YurunChen/repo-docs-skills | A | Distinct behavior-first, evidence-first repository documentation model with surgical sync rules. Adapted as `repository-evidence-docs`. |
| dzhng/skills | A/B | Strong engineering factory methodology. Most loop/spec/review behavior overlaps existing Arsenal capabilities; `audit-choices` adds a distinct decision-review surface and was adapted. |
| majidmanzarpour/threejs-game-skills | A/D | Deep Three.js game stack with gameplay, visuals, QA and asset generators. Too broad and tool-dependent for bulk import; retain as vertical reference. |
| jakubkrehel/skills | A/B | High-quality interface craft and stress-test methods. Broad overlap with design direction, interaction polish, runtime UI verification, accessibility and visual review. Retain as targeted reference. |
| Kappaemme-git/codex-first-customer-finder-skill | A | Distinct evidence-backed early-customer discovery workflow with strong privacy and outreach boundaries. Adapted as `first-customer-research`. |
| wy51ai/edulab | D/A | Rich education artifact system with interactive lessons and videos, but heavily dependent on subject-specific Python kernels, Three.js, ffmpeg, Playwright and TTS. Retain as technical inspiration. |
| hajimi-kun/latex-to-word-workflow | A | Distinct document-conversion methodology that preserves scientific and Word semantics rather than treating conversion as text export. Adapted as `latex-to-word`. |

## Adopted

### repository-evidence-docs
Source: `YurunChen/repo-docs-skills`

Distinct value:
- behavior before file inventory;
- source evidence attached to durable explanations;
- representative walkthrough as the entry into code structure;
- explicit decision gate before updating docs;
- surgical sync instead of constant generated-document churn.

Adaptation:
- removed mandatory `repo-docs/` package layout;
- removed required root AGENTS/CLAUDE modifications;
- removed dependency on bundled validators;
- retained evidence, ownership and freshness rules.

### agent-choice-audit
Source: `dzhng/skills`, especially `audit-choices`

Distinct value:
- audits decisions introduced by the implementer where the spec was silent;
- distinguishes architecture ownership from ordinary diff correctness;
- records reach, reversibility and confidence;
- requires corrected decision, not just patch advice, for unsound choices.

Adaptation:
- no mandatory `choices.md`;
- no dependency on subagents or session transcripts;
- classifications simplified while preserving user-owned product decisions.

### first-customer-research
Source: `Kappaemme-git/codex-first-customer-finder-skill`

Distinct value:
- searches for actual public demand signals rather than speculative persona lists;
- source-original verification and separate publication/check dates;
- qualification across pain, fit, timing, reachability and evidence;
- privacy-safe research and strict separation between lead discovery and outreach.

Adaptation:
- no mandatory local product state or scripts;
- no fixed report generator;
- scores remain research prioritization aids, not conversion estimates;
- no outreach action is implied by research.

### latex-to-word
Source: `hajimi-kun/latex-to-word-workflow`

Distinct value:
- explicit LaTeX → converter → Word semantic bridge;
- distinguishes visual text from live Word/Zotero fields;
- prioritizes scientific semantics, numbering and citations over cosmetic fidelity;
- uses representative conversion probes before full conversion;
- makes Word desktop validation a separate capability gate.

Adaptation:
- no mandatory Pandoc, Zotero, Word or local scripts unless actually available;
- user-run desktop steps become explicit handoff gates;
- validation remains proportional to object risk.

## Retained as external references

### dmmulroy/skills
The collection reinforces correct-by-construction TypeScript, typed failures, parsing at boundaries, composition roots and technical specifications. Much of this overlaps:
- `domain-modeling`
- `codebase-design`
- `tdd`
- `project-planning`
- `code-review`

Future TypeScript-specific gaps can be evaluated file by file.

### eterna-image2image-skill
The useful portable ideas are:
- preserve subject identity and scene geometry unless creative rewrite is requested;
- use restrained color, highlight and shadow behavior as explicit direction;
- treat composition, lighting and texture as separate controls;
- use negative constraints against common synthetic artifacts.

Those principles belong in image-editing/design direction rather than an Arsenal skill tied to one film-simulation name. No proprietary LUT claim or color-science equivalence was imported.

### threejs-game-skills
This is a large production system covering gameplay, graphics, UI, QA, performance, generated assets and audio. It is valuable as a vertical reference, but most workflows depend on:
- Three.js/Vite runtime;
- browser and Playwright checks;
- external asset generation APIs;
- game-specific evidence scripts.

Portable parts already map to `creative-web-effects`, `shader-graphics-engineering`, `runtime-ui-verification`, `procedural-3d-reconstruction`, `interaction-polish` and general engineering skills.

### jakubkrehel/skills
Useful patterns include:
- one-axis UI variant exploration;
- stress-testing real components across content/state/width scenarios;
- measuring observed breakage rather than predicting it;
- contextual typography/layout/accessibility craft.

These largely reinforce existing web/design skills. No parallel "better-*" family was imported.

### wy51ai/edulab
The collection demonstrates a strong pattern for interactive education:
- deterministic subject kernel;
- explanatory visualization;
- interactive controls;
- self-contained HTML;
- narration-aligned animation and video.

However the current package is a collection of technical products, not a single portable methodology. Subject kernels and media tooling should be evaluated only when a concrete education-artifact need arises.

## Security and dependency review

- No installer, shell script, npm package, Python helper, TTS call, browser automation or external asset generator from the evaluated repositories was executed.
- Image/style references were treated as methodology, not as claims of official Fujifilm ETERNA reproduction.
- First-customer research excludes private-contact discovery, sensitive profiling and automatic outreach.
- Three.js and Edulab external generators/API keys were not adopted as available capabilities.
- LaTeX-to-Word validation does not claim Word/Zotero live-field semantics unless observed through an appropriate environment.
- External agent instructions were adapted rather than allowed to override the Arsenal's canonical rules.

## Result

New skills:
- `repository-evidence-docs`
- `agent-choice-audit`
- `first-customer-research`
- `latex-to-word`

The Arsenal index was updated to route to all four.
