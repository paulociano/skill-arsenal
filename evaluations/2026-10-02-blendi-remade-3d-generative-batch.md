# Batch evaluation — blendi-remade 3D/generative projects

Date: 2026-10-02

## Sources

- https://github.com/blendi-remade/isometric-city-fal
- https://github.com/blendi-remade/fal-3d-anything
- https://github.com/blendi-remade/fal-3d-unreal
- https://github.com/blendi-remade/banana-peel
- https://github.com/blendi-remade/desi-universe

Method: `arsenal-autopilot`.

No installer, build, browser extension, Unreal project, database migration, model generation, dataset download or external API call was executed.

## blendi-remade/isometric-city-fal — B/D — KEEP_EXTERNAL_REFERENCE

What it is: Next.js/Canvas isometric city-building simulation with traffic, economy, pathfinding and optional AI-generated building sprites.

Useful pattern: generation is constrained by the destination system. The pipeline chooses aspect ratio for the intended building silhouette, removes background, then derives game metadata separately from the generated image.

Overlap: `high-fidelity-image-generation`, `creative-web-effects`, application/game-specific engineering.

Decision: no new skill. The useful idea is already covered by destination-aware asset preparation and structured downstream validation. The simulation/game engine itself is product-specific.

Security/portability: external fal.ai calls and `FAL_KEY`; npm/Next.js runtime; server-side API route. Repository includes an MIT LICENSE.

## blendi-remade/fal-3d-anything — D — KEEP_EXTERNAL_REFERENCE

What it is: Chrome extension that turns webpage images into 3D models using Meshy via fal.ai and embeds an interactive Three.js viewer.

Overlap: `image-to-3d`, `creative-web-effects`, `shader-graphics-engineering`.

Decision: no canonical change. The Arsenal already owns image → 3D routing and 3D viewer integration.

Security/portability: extension stores the fal key in `chrome.storage.local`; it performs network generation and page injection. `package.json` also has a `postinstall` build step. README says MIT, but no root LICENSE file was found during this review, so downstream license verification remains necessary.

## blendi-remade/fal-3d-unreal — A/D — UPDATE_EXISTING

What it is: Unreal Engine runtime pipeline for text/image → pose-controlled concept → 3D mesh → auto-rig → multiple animation clips → playable character swap.

Incremental value:
- makes riggability a first-class target contract before reconstruction;
- uses pose-controlled concept/reference images to reduce limb overlap before rigging;
- validates the generated asset in the destination runtime instead of treating a valid GLB as completion;
- exposes failure modes such as scale mismatch, limb blending, props/cloth skinning badly and hard-cut animation switching.

Decision: update `concept-to-3d-asset` with an explicit riggable/animatable character path. Do not import Unreal/fal/Meshy/glTFRuntime specifics.

Security/portability: requires UE 5.5, C++ project build, git submodule, external fal.ai calls, local `.env` credential and downloaded generated assets. README says MIT, but no root LICENSE file was found during this review.

## blendi-remade/banana-peel — B/D — KEEP_EXTERNAL_REFERENCE

What it is: collaborative image-evolution platform where generated image variants form branching social threads.

Potential methodology: provenance/lineage of creative variants as an explicit tree rather than overwriting prior generations.

Overlap: `high-fidelity-image-generation`, project/workspace versioning patterns, social/product implementation.

Decision: no new skill. The Arsenal already recommends preserving references, variants and targeted iterations. A collaborative social tree is product architecture rather than a distinct operational skill.

Security/portability: Supabase auth/database/storage, service-role secret, fal key, external generation, migrations and deployment dependencies. README states MIT, but no root LICENSE file was found during review.

## blendi-remade/desi-universe — A/D — UPDATE_EXISTING

What it is: browser visualization of 1.4M+ DESI DR1 spectroscopic objects with scientific preprocessing, compact binary GPU buffers, shader-based slicing/coloring, picking and an optional AI "artist impression" feature.

Incremental value:
- preprocess heavy scientific source formats into compact browser-ready buffers;
- keep coordinate transformation and quality cuts explicit;
- use GPU-first point-cloud structures instead of JS objects per observation;
- introduce a clear LOD/streaming boundary for still-larger datasets;
- explicitly label generated imagery as artistic interpretation rather than scientific observation.

Decision: update `shader-graphics-engineering` with a large scientific point-cloud mode. Do not import DESI-specific cosmology, Three.js implementation or fal endpoint.

Security/portability: external dataset downloads, Python scientific stack, browser GPU requirements and optional server-side fal key. README states MIT but no root LICENSE file was found in this review; DESI data also has its own citation/data policy.

## Adopted changes

1. `concept-to-3d-asset`: added a riggable/animatable character route.
2. `shader-graphics-engineering`: added a large scientific point-cloud mode.
3. No new skill created for the other three repositories.

## General security/portability conclusion

- No external scripts were executed.
- fal.ai, Meshy, Unreal, Chrome-extension APIs, Supabase and DESI data are treated as external runtimes/services.
- Credentials are not assumed available.
- README license claims are not treated as a substitute for a missing LICENSE file when downstream reuse requires certainty.
