# Batch evaluation — 2026-10-02

## Scope

Sources supplied for Arsenal triage:
- incoai/splash
- Louis-CFM/coucou
- qiz029/dscode
- feitangyuan/onetake
- edenfunf/reelmimic
- LockedinLabs-AI/ag
- kevinzhow/Rungic
- ciromattia/kcc
- PostHog/jeeves
- alpcanaydin/tusk
- OpSafari/hypoarena
- slop-place/zulu
- openJiuwen-ai/iCode

Method: `arsenal-autopilot`. Unit of comparison: capability, not repository name.

## Decisions

### incoai/splash — D — KEEP_EXTERNAL_REFERENCE

What it is: local LLM inference engine for Apple Silicon with OpenAI/Anthropic-compatible APIs, speculative decoding, model-specific Metal kernels, caching and memory planning.

Incremental value: useful runtime reference for local inference and model-serving architecture, but it does not add a portable ChatGPT skill by itself.

Overlap/owner: `model-routing-gateway`, `ml-production-engineering`, `system-design-engineering`.

Portability/security: requires macOS/Apple Silicon, native binaries, model downloads and local server runtime. Do not import tooling assumptions into Arsenal.

Decision: no canonical skill change.

### Louis-CFM/coucou — B/D — ABSORB_METHOD_ONLY / KEEP_EXTERNAL_REFERENCE

What it is: desktop companion UI for agent sessions, approvals, context handoff and service status.

Useful ideas: ambient agent-state visibility, user approval surfaced at the moment of need, non-blocking status indicators, secrets stored in OS credential stores.

Overlap/owner: `multi-agent-orchestration`, `agenda-operations` for status surfaces, and product/UI skills when designing agent UX.

Decision: no new skill. The ideas are architectural/product patterns rather than a reusable standalone skill.

### qiz029/dscode — A/D — UPDATE_EXISTING by reference only

What it is: persistent coding-agent harness with cross-session communication, independent review, isolated worktrees, durable triggers, session cards, permissions and metrics.

Useful capabilities:
- persistent session/runtime and cross-session handoff;
- delegated work on isolated worktrees;
- independent reviewer after implementation;
- durable triggers with permission boundaries;
- session cards that summarize enough context to select a collaborator without dumping full transcripts.

Overlap/owners: `multi-agent-orchestration`, `graph-engineering`, `handoff`, `llm-observability-evaluation`, `code-review`, `automations` platform capability.

Decision: no new skill. Existing owners already cover the behavior. Keep as a strong external reference for future refinement.

### feitangyuan/onetake — A/D — KEEP_EXTERNAL_REFERENCE

What it is: agent skill + rendering toolkit for short product films built as deterministic HTML motion compositions with continuity/carry checks, measured motion, camera behavior, sound and automated QA.

Incremental value: strong methodology around visual continuity between beats, measured reference decomposition and objective QA.

Overlap/owners: `procedural-film`, `cinematic-visual-direction`, `video-editing-pipeline`, `runtime-ui-verification`.

License gate: PolyForm Noncommercial 1.0.0. Because the Arsenal is intended as a reusable general library, do not transplant source text, code, templates or distinctive implementation details into canonical commercial-capable skills.

Decision: external reference only. Conceptual inspiration may inform future independently-authored improvements, but no direct import from this source.

### edenfunf/reelmimic — A/D — ABSORB_METHOD_ONLY

What it is: reference-video-to-original-video production system with reference decomposition, style routing, user approval gate, multi-agent production, independent per-shot review, evidence-backed fixes and provenance for sourced assets.

Useful portable methodology:
- decompose reference technique separately from protected content;
- treat medium/style classification as a routing constraint;
- freeze an approved production plan before expensive generation;
- independent review of produced shots;
- require before/after evidence for claimed fixes;
- record asset source/author/license.

Overlap/owners: `watch-video`, `reels-scripting`, `video-editing-pipeline`, `procedural-film`, `multi-agent-orchestration`, `verify-before-claim`.

Decision: no new skill. Methodology is valuable but already has canonical owners. Use as provenance/reference for future targeted refinement.

### LockedinLabs-AI/ag — unresolved

The supplied URL resolves to `LockedinLabs-AI/ag`, which returned 404 from GitHub. Per Arsenal policy, do not guess the intended repository.

Decision: not evaluated.

### kevinzhow/Rungic — A/D — KEEP_EXTERNAL_REFERENCE

What it is: Android/Linux agent workspace system with separate visual workspaces, multi-agent teams, proactive system care, approval gates and evidence-bound repair flows.

Useful ideas:
- agent workspace isolation from the user's active workspace;
- evidence revision invalidates stale repair approval;
- issue state and agent-task state should be tracked separately;
- an agent finishing a task does not prove the underlying issue is fixed.

Overlap/owners: `mobile-device-automation`, `multi-agent-orchestration`, `agent-choice-audit`, `verify-before-claim`, `project-health-review`.

Decision: no new skill. Strong systems reference.

### ciromattia/kcc — D — KEEP_EXTERNAL_REFERENCE

What it is: production utility for converting comics/manga to device-specific ebook formats with image processing optimized for e-ink readers.

Incremental value: useful specialized tool for ebook/device publishing, but not a general reasoning methodology.

Overlap/owner: `illustrated-ebook-production` could reference KCC when a user specifically targets Kindle/Kobo comic output and the runtime/tool is actually available.

Decision: no canonical skill change.

### PostHog/jeeves — D — KEEP_EXTERNAL_REFERENCE

What it is: trained 9B reasoning classifier with calibrated-style outputs for yes/no, choice and score questions.

Incremental value: model/runtime option, not a portable workflow. The Arsenal already owns structured decision workflows separately from model architecture.

Overlap/owners: `decision-analysis`, `structured-output-contract`, `llm-observability-evaluation`, `model-routing-gateway`.

Decision: no skill import.

### alpcanaydin/tusk — B/D — ABSORB_METHOD_ONLY

What it is: native database client with AI-assisted query generation that cannot execute SQL directly.

Useful pattern: separate query generation from execution, force human review at the effect boundary, and surface assumptions.

Overlap/owners: `secure-code-privacy-review`, data-analysis workflows, `verify-before-claim`.

Decision: no standalone skill. Keep the human-in-the-loop effect-boundary pattern as reference.

### OpSafari/hypoarena — A/D — CREATE_NEW

What it is: offline hypothesis-discovery workbench that decomposes generate → verify → deduplicate → debate → rank → evolve → accumulate → report into testable stages.

Incremental capability:
- operating over a hypothesis/evidence graph rather than only designing one research question;
- generating competing hypotheses, verifying grounding, deduplicating paraphrase-equivalent ideas, structured critique/revision and evidence accumulation;
- keeping synthetic-demo claims separate from real scientific-discovery claims;
- reproducible artifacts/checkpoints.

Why existing skills do not fully own it:
- `research-question-design` creates strong research questions but does not run an iterative hypothesis population;
- `evidence-claim-verification` verifies claims but does not generate/evolve candidate hypotheses;
- `experiment-design` plans tests after hypotheses exist.

Decision: create `scientific-hypothesis-discovery` as a portable methodology. Do not import the runtime, ranking implementation or synthetic-demo claims as if they were available capabilities.

### slop-place/zulu — C/D — REJECT

What it is: Zulip client emphasizing topic-first UX.

Incremental value for Arsenal: none as a reusable operational skill. It is a product implementation.

Decision: reject from skill catalog.

### openJiuwen-ai/iCode — A/D — KEEP_EXTERNAL_REFERENCE

What it is: terminal agent/workflow orchestrator with agent configuration as data, model profiles, workflow graph view, diff/rollback, per-turn trajectory and shell integration.

Useful ideas:
- agent configuration should be inspectable and editable as data;
- model/tool/hook time should be separable in trajectory views;
- rollback should show exactly which file changes will be reverted;
- workflow execution should expose node state and token/tool cost.

Overlap/owners: `graph-engineering`, `llm-observability-evaluation`, `agent-choice-audit`, `code-review`.

Decision: no new skill. Strong external reference for agent-workspace product design.

## Adopted changes

1. Create `scientific-hypothesis-discovery`.
2. Add it to `ARSENAL INDEX.md`.
3. Keep OneTake, DSCODE, Rungic, iCode, Splash, Jeeves, KCC and Tusk as external references rather than pretending their runtimes are available.
4. No changes for Zulu.
5. `LockedinLabs-AI/ag` remains unresolved until a valid repository URL is provided.

## Security and portability notes

- No installers, binaries or scripts from evaluated repositories were executed.
- Runtime-specific features were not treated as ChatGPT capabilities.
- External credentials, hooks, shell permissions, sandboxes and local daemons were not imported.
- OneTake's noncommercial license blocked direct adaptation into canonical reusable skill text/code.
- HypoArena's methodology was adapted at the process level; the new skill does not claim its offline package, ranking code or model adapters are present.
