# Evaluation — blendi-remade/dioramas

Date: 2026-10-02

## Source

- https://github.com/blendi-remade/dioramas
- README, docs/ENGINE.md, package.json, LICENSE and selected scripts reviewed statically.
- No installer, build, model generation, Playwright browser run or external service was executed.

## What it does

Dioramas is an MIT-licensed framework and reference implementation for cinematic interactive 3D websites where the 3D scene carries the full page rather than acting only as a hero background. Its concrete stack uses Three.js, postprocessing/N8AO, GSAP, Lenis, Playwright, generated 3D assets and an optimization/review pipeline.

Its method combines:
- brief → world/scene direction;
- AI-generated image → 3D hero asset;
- geometry/texture optimization;
- camera-driven scroll choreography;
- one signature interaction per world;
- HTML overlays over a fixed 3D canvas;
- screenshot/contact-sheet review across scroll stops;
- explicit desktop/mobile/FPS/error gates.

## Classification

**A/D — useful methodology with technical/runtime dependencies.**

## Incremental value

The Arsenal already owns the component capabilities:
- `creative-web-engineering`;
- `web-design-engineer`;
- `creative-web-effects`;
- `scroll-storytelling`;
- `cinematic-visual-direction`;
- `concept-to-3d-asset`;
- `runtime-ui-verification`;
- `web-quality-audit`.

The incremental value is not another Three.js skill. It is a reusable architecture for cases where **the scene is the page**:
- camera state doubles as layout state;
- 3D and typography are composed as one frame;
- one signature interaction is part of the concept;
- assets get an explicit download/poly/material contract;
- QA reviews representative visual states, mobile degradation, errors and performance together.

## Decision

**UPDATE_EXISTING**: add an `Immersive 3D page mode` to `stacks/creative-web-engineering/STACK.md`.

Do not create a standalone Dioramas skill. That would duplicate existing owners and couple the Arsenal to one runtime.

## Security and portability review

Verdict: **CAUTION for runtime, APPROVE for methodology**.

Observed sensitive/dependent surfaces:
- `FAL_KEY` credential for external fal.ai calls;
- paid external image/3D generation endpoints;
- network upload/download of assets;
- npm supply chain;
- Playwright-controlled Chrome;
- local file writes for manifests, generated models, optimized assets and screenshots;
- GPU/WebGL assumptions.

Selected scripts inspected:
- `scripts/gen.mjs`: submits image/mesh generation to fal endpoints, uploads local images, downloads returned assets, persists request IDs and disables Meshy's safety checker in its mesh-generation input;
- `scripts/optimize.mjs`: local GLB transform/compression pipeline;
- `scripts/review.mjs`: launches headless Chrome against a local dev server and captures screenshots/FPS/errors.

No hidden persistence, privilege escalation or destructive system operation was identified in the inspected files, but this was not a full-code audit.

## License

Code: MIT.

The repository states generated models/images are CC BY 4.0, with separate asset and third-party notices. Asset provenance/license must remain distinct from code license in downstream use.

## What was absorbed

- scene-as-page architecture;
- camera-as-layout;
- one signature interaction;
- asset/performance contract;
- frame-based QA across scroll states;
- explicit mobile degradation/fallback.

## What was not imported

- Three.js engine implementation;
- fal.ai / Nano Banana / Meshy bindings;
- prompts and generated models;
- runtime-specific postprocessing recipes;
- scripts or dependency assumptions;
- numeric budgets presented as universal defaults.

## Final owner

`creative-web-engineering` remains the canonical owner. Supporting skills are routed only when the actual project needs them.
