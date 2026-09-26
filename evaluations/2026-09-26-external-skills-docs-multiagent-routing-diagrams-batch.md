# External skills evaluation — document conversion, multi-agent, routing and interactive systems batch

Date: 2026-09-26

## Scope

Repositories reviewed:

- https://github.com/firecrawl/anydoc
- https://github.com/herdrdev/herdr
- https://github.com/stablyai/orca
- https://github.com/chaseai-yt/claudex-loop
- https://github.com/calesthio/OpenMontage
- https://github.com/diegosouzapw/OmniRoute
- https://github.com/tt-a1i/archify
- https://github.com/Kevin-Liu-01/Claude-of-Tanks

Evaluation followed the current `ARSENAL INDEX.md` and `stacks/evaluate-and-import-skill/STACK.md`.

## Summary

| Source | Class | Decision |
| --- | --- | --- |
| firecrawl/anydoc | A/D | Strong normalization layer for many document formats. Adopt the local-first conversion and OCR fallback method, not the specific CLI/service dependency. |
| herdrdev/herdr | A/D | Strong multi-agent terminal coordination semantics with explicit observable states and safety around retries, IDs and remote mutations. Adapt portable orchestration principles only. |
| stablyai/orca | B/D | Rich desktop orchestrator with parallel worktrees, embedded browser and agent tracking. Product/runtime specific; retain as reference for orchestration UX and worktree isolation. |
| chaseai-yt/claudex-loop | A/B | Independent plan review/build/final inspection loop is useful, but provider/model routing is host-specific and overlaps review/handoff skills. Absorb the independent-review pattern into multi-agent orchestration rather than create a Claude/Codex-specific skill. |
| calesthio/OpenMontage | D/B | Media/video production system. Useful as a technical reference, but overlaps content/video pipelines and depends on its own tooling. No new generic skill added. |
| diegosouzapw/OmniRoute | D | Large routing/proxy application with significant implementation/runtime surface. Existing `model-routing-gateway` already covers the portable methodology. Retain as technical reference. |
| tt-a1i/archify | A | Strong interactive diagram authoring discipline with typed topology, artifact validation and explicit separation between structural, browser and perceptual evidence. Adapted as `interactive-system-diagram`. |
| Kevin-Liu-01/Claude-of-Tanks | D/A | Large production Three.js game with mature subsystem skill ownership and evidence gates. Valuable as architecture/process reference; not portable as one skill. |

## Adopted

### document-to-markdown
Source: `firecrawl/anydoc`

Distinct value:
- one normalized intermediate representation for heterogeneous office/document formats;
- content-based format detection rather than trusting extensions;
- local conversion first;
- explicit OCR fallback only when needed;
- large-document strategy that avoids flooding context.

Adaptation:
- no assumption that anydoc, Node, Rust, Python bindings or Firecrawl Parse exist;
- hosted OCR requires explicit disclosure that content leaves the local environment;
- does not replace layout-sensitive or Office-semantic validation.

### multi-agent-orchestration
Sources: `herdrdev/herdr`, `stablyai/orca`, `chaseai-yt/claudex-loop`

Distinct value:
- explicit coordinator ownership;
- isolated workspaces/worktrees for parallel writing;
- observable agent states;
- prompt submission is not treated as completion;
- timeout/connection failures are ambiguous state, not permission to blindly retry;
- independent review by a different worker/provider can be used as a bounded verification step.

Adaptation:
- no assumption that Herdr, Orca, Claude Code, Codex CLI or worktrees are available;
- uses real delegation capabilities only when the current environment exposes them;
- no model ranking or provider preference is encoded;
- approvals from a blocked worker remain user decisions.

### interactive-system-diagram
Source: `tt-a1i/archify`

Distinct value:
- explicit router between architecture, workflow, sequence, dataflow and lifecycle;
- artifact-first authoring;
- semantic labels preserved through geometry repair;
- repository-backed topology when reflecting real code;
- separates structural validation, browser verification and perceptual visual review.

Adaptation:
- no dependency on Archify JSON schemas, CLI, presets or renderer;
- no branded update checker;
- output format remains capability-dependent while HTML is preferred when interaction matters.

## Retained as references

### Orca
Useful product patterns:
- parallel worktrees;
- compare-and-merge agent runs;
- agent tracking;
- browser/design context capture;
- remote execution.

These are product features rather than a portable skill contract. Their methodological subset is represented in `multi-agent-orchestration`.

### Claudex Loop
Useful pattern:
- coordinator forms requirements and plan;
- an independent agent challenges the plan;
- implementation occurs;
- a fresh independent reviewer inspects the result.

The provider-specific Claude/Codex pairing and model-selection advice were not imported. The general independent-review pattern is covered by orchestration plus `code-review` and `agent-choice-audit`.

### OpenMontage
The repository is a concrete media production system. The Arsenal already has `content-production`, `procedural-film`, `video-editing-pipeline`-style capabilities and media skills; future gaps should be evaluated at workflow/component level.

### OmniRoute
This is primarily a model/API routing implementation. Existing `model-routing-gateway` already covers provider selection, retries, fallbacks, budget and observability at the methodology level. No duplicate skill was created.

### Claude of Tanks
The repository demonstrates:
- hierarchical subsystem ownership through local SKILL.md files;
- deterministic evidence gates;
- source-backed procedural asset generation;
- browser/runtime/performance verification;
- integration discipline for a very large Three.js application.

These ideas reinforce `project-skill-architecture`, `functional-skill-architecture`, `runtime-ui-verification`, `procedural-3d-reconstruction` and engineering verification skills. The game-specific implementation is not imported.

## Security and dependency review

- No external installer, terminal multiplexer, desktop app, model router, media pipeline, game runtime, OCR service or diagram renderer was executed.
- Hosted OCR is never assumed safe for private files; content transfer must be explicit.
- Multi-agent tools may mutate separate worktrees or remote machines; ambiguous failures must be inspected before retry.
- Agent approvals and permission dialogs are not auto-accepted.
- Provider/model-specific recommendations were not treated as universal rankings.
- Archify's remote update workflow and product-specific runtime were not imported.
- Large product repositories were used as methodology references only.

## Result

New skills:
- `document-to-markdown`
- `multi-agent-orchestration`
- `interactive-system-diagram`

The Arsenal index was updated to route to all three.
