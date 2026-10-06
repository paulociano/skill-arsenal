# Evaluation Batch — 2026-10-06

## Scope

Batch evaluated through `arsenal-autopilot` after reading the canonical `ARSENAL INDEX.md`.

Sources:
- https://github.com/nautechsystems/nautilus_trader
- https://github.com/immich-app/immich
- https://github.com/block/buzz
- https://github.com/earendil-works/pi
- https://github.com/HKUDS/DeepTutor
- https://github.com/lyogavin/airllm
- https://github.com/zenbu-labs/terminal-browser
- https://github.com/AprilNEA/OpenLogi
- https://github.com/Alain00/blobatar
- https://github.com/yetone/cumora
- https://github.com/CristianOlivera1/Aura
- https://github.com/HQBase/hqbase
- https://github.com/cinderline/northcinder
- https://github.com/seyedehsanhadi/sloptrim
- https://github.com/littledivy/durable-git
- https://github.com/KickNext/morphnext
- https://github.com/halcyon-video/halcyon-video

## Decisions

| Source | Class | Decision | Rationale / owner |
|---|---|---|---|
| nautechsystems/nautilus_trader | B/D | KEEP_EXTERNAL_REFERENCE | Strong event-driven trading architecture, deterministic simulation/live parity, adapters and reconciliation concerns. Useful technical reference, but too runtime/domain-specific to justify a new skill from README-level evidence alone. Revisit if a recurring algorithmic-trading engineering workflow appears. |
| immich-app/immich | D | REJECT_AS_SKILL | Excellent self-hosted photo/video product, but primarily application/runtime architecture. No incremental conversational methodology beyond existing software/system skills. |
| block/buzz | B/D | KEEP_EXTERNAL_REFERENCE | Signed event log, agent/human identity symmetry and workspace auditability are strong architecture ideas. Current Arsenal already owns agent governance, workspace operations and software factory concepts; no owner change justified in this pass. |
| earendil-works/pi | A/D | UPDATE_EXISTING | Minimal extensible agent harness, packages/skills/templates and JSON/RPC/SDK surfaces materially improve `coding-agent-engineering`. Explicitly did not absorb Pi's lack of a permission system. |
| HKUDS/DeepTutor | B/D | KEEP_EXTERNAL_REFERENCE | Rich lifelong tutoring system with memory, KBs, mastery paths and learner workspaces. `teach`, retrieval and memory owners already cover the core methodology; product/runtime details are not portable enough for a new skill. |
| lyogavin/airllm | D | KEEP_EXTERNAL_REFERENCE | Technically interesting low-VRAM layer streaming for very large models, but it is an inference implementation/runtime. No generic Arsenal behavior change adopted. |
| zenbu-labs/terminal-browser | D | KEEP_EXTERNAL_REFERENCE | Useful terminal/browser runtime and agent interaction surface. Existing `computer-use-agent-engineering` already owns the methodology; the terminal rendering mechanism is implementation-specific. |
| AprilNEA/OpenLogi | D | REJECT_AS_SKILL | Hardware-control application with valuable engineering work, but no reusable Arsenal method identified. |
| Alain00/blobatar | D | REJECT_AS_SKILL | Deterministic avatar component/library. Narrow implementation technique, not a reusable operational skill. |
| yetone/cumora | A/D | UPDATE_EXISTING | Freshness gate for stale replies/actions, atomic claims on work and cheap triage before expensive reasoning improve `software-factory-operations`. Chat/Kubernetes/runtime details were not absorbed. |
| CristianOlivera1/Aura | B/D | KEEP_EXTERNAL_REFERENCE | Good reference library for layered atmospheric gradients and export workflows. Existing creative-web/design skills can already generate such effects; no separate owner needed. |
| HQBase/hqbase | B/D | KEEP_EXTERNAL_REFERENCE | Strong self-hosted shared inbox, audit and remote MCP patterns. Existing `support-operations-engineering`, email tooling and agent governance cover the general capability. |
| cinderline/northcinder | A/D | CREATE_NEW | Clear incremental methodology around independent shopping research, seller trust, neutral ranking, explicit unknowns and one-use transaction approval. Created `shopping-agent-governance`. |
| seyedehsanhadi/sloptrim | B/D | ABSORB_METHOD_ONLY / NO CHANGE | Pattern-based local prose linting and benchmarking are useful, but authorship/AI detection is not a reliable capability to canonize. Existing `prose-lint` already treats checks as signals rather than truth, so no file change was required. |
| littledivy/durable-git | D | KEEP_EXTERNAL_REFERENCE | Interesting Git-on-Durable-Objects implementation. Valuable systems reference, not a new conversational method. |
| KickNext/morphnext | D | KEEP_EXTERNAL_REFERENCE | High-quality vector morph implementation for Flutter. Existing `ui-motion-design` owns the design decision; library mechanics are platform-specific. |
| halcyon-video/halcyon-video | B/D | KEEP_EXTERNAL_REFERENCE | Strong experiential 3D media browsing and remote-first interaction reference. Existing creative web/3D skills cover the reusable design methods; no new owner justified. |

## Security and portability review

No external installer, binary, package, hook or setup script was executed.

Key risks observed:
- several sources install through shell scripts, package managers or privileged runtimes;
- agent harnesses may inherit broad filesystem/network/process privileges;
- shopping/checkout systems cross a financial action boundary;
- shared-agent workspaces require stale-state, concurrency and credential controls;
- product-specific MCP, Kubernetes, Cloudflare, browser, hardware and GPU runtimes are not assumed to exist in ChatGPT.

Adaptations therefore:
- preserve methodology, not runtime claims;
- fail closed on stale coordination and transaction changes;
- keep explicit approval gates;
- avoid raw payment credentials;
- keep tool/runtime availability grounded in the actual environment.

## Materialized changes

1. Updated `skills/coding-agent-engineering/SKILL.md` with Pi-derived minimal-harness extensibility and automated control surfaces.
2. Updated `skills/software-factory-operations/SKILL.md` with Cumora-derived freshness checks, atomic claim emphasis and economical triage.
3. Created `skills/shopping-agent-governance/SKILL.md` from NorthCinder-derived methodology.
4. Updated `ARSENAL INDEX.md` with the new skill.

## Validation limits

This batch used repository metadata and README/root documentation for broad triage, consistent with the Autopilot batch policy. Deep code audits were not performed for sources that did not show plausible incremental capability. The adopted methods are intentionally narrower than the original products and do not imply compatibility with their runtimes.
