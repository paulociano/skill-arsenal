# Batch evaluation — jobs, UI components, documentation linting and model runtime

Date: 2026-10-02

## Sources

- https://github.com/suvamneog/jobradar
- https://github.com/kuratlielia/arc-library
- https://github.com/scarletkc/seiso
- https://github.com/NaiveAI-Labs/Naive-N0.5-Flash

Method: `arsenal-autopilot`.

No installer, package manager, model download, browser runtime, scheduler, email send, database migration or linter binary was executed.

## suvamneog/jobradar — A/D — CREATE_NEW

What it is: local job-monitoring system that watches multiple ATS sources, maintains state over time, compares openings against a resume, enforces hard eligibility gates in code, and emits alerts/digests.

Incremental capability:
- treats job search as a temporal diff rather than isolated search;
- stable identity and lifecycle: new, open, closed, reopened;
- closure only after a successful source fetch;
- per-source baseline prevents alert floods on first sighting;
- deterministic eligibility gates coexist with LLM fit scoring;
- fit score is explicitly a sort order, not a hiring prediction;
- budget is enforced per batch and notification channels have independent consumption state.

Why a new owner is justified:
- the Arsenal had job discovery/search capabilities at the product/tool layer, but no reusable methodology for persistent opportunity monitoring and stateful alerts;
- `decision-analysis` does not own temporal source diffing;
- `automations` can schedule checks but does not define the job-domain state model.

Decision: create `job-opportunity-monitoring`.

Security/portability:
- original installer creates a Python venv, installs requirements and writes/loads launchd agents;
- original flow uses resume PDF, API keys and Gmail app password;
- external ATS/aggregator requests and email delivery are runtime-specific;
- none of those mechanisms are imported as requirements;
- the skill uses only capabilities actually available in the current environment when executed.

## kuratlielia/arc-library — B/D — KEEP_EXTERNAL_REFERENCE

What it is: MIT React 19 component/block library with calm motion, CSS modules, semantic design tokens, Motion, keyboard support and reduced-motion paths.

Useful value:
- motion tokens as a shared small system;
- source-owned components instead of opaque runtime widgets;
- reduced-motion path as a first-class requirement;
- individual components can be copied without adopting a whole package.

Overlap:
- `web-design-engineer`;
- `shadcn-ui-engineering`;
- `interaction-polish`;
- `ui-motion-design`;
- existing external UI component catalogs.

Decision: no new skill. Add Arc to `web-design-engineer/references/ui-component-references.md`.

License: root MIT LICENSE confirmed. The repository distinguishes free/open-source items from Arc Pro; do not assume Pro examples are included in the MIT repository.

## scarletkc/seiso — A/D — UPDATE_EXISTING

What it is: Markdown convention and linter for repository docs, with document kinds, fact ownership, pointers, exceptions and empirically promoted lint rules.

Incremental methodology:
- separate document kinds by responsibility;
- each durable fact has one canonical owner;
- long-lived docs should point to volatile/runtime values instead of copying them;
- diagnostics distinguish mechanical consistency, convention breach and heuristics;
- ambiguous ownership remains an explicit judgment instead of being guessed;
- heuristic rules begin in preview and are promoted only after real-data evaluation;
- tuning and holdout are separated; behavior changed after holdout requires fresh evaluation;
- incomplete checks remain incomplete rather than silently passing.

Overlap/owner: `repository-evidence-docs`.

Decision: update `repository-evidence-docs`; no standalone Seiso skill.

Security/portability:
- seiso is an external Rust binary/tool distributed through cargo, PyPI and npm;
- the Arsenal does not require installation;
- methodology can be followed without the binary;
- root MIT license confirmed;
- `unsafe_code = "forbid"` is a positive implementation signal but not a complete security audit.

## NaiveAI-Labs/Naive-N0.5-Flash — D — KEEP_EXTERNAL_REFERENCE

What it is: MIT open-weight 309B MoE model with 15.5B active parameters, native 1M-token context, hybrid sliding-window/sparse attention and a specialized inference runtime.

Incremental value for Arsenal:
- useful external reference for sparse long-context architecture and throughput-oriented serving;
- published model/runtime claims need workload-specific validation before routing decisions.

Overlap/owner:
- `model-routing-gateway`;
- `ml-production-engineering`;
- `llm-observability-evaluation`.

Decision: no canonical skill change. It is a model/deployment option, not a portable operational methodology.

Security/portability:
- deployment requires FP8-capable NVIDIA hardware and approximately 315 GB just for model weights, plus inference memory;
- README quickstart uses `trust_remote_code=True`, which is a code-execution boundary and must be audited before use;
- weights/runtime are external and not available by default in ChatGPT;
- root MIT LICENSE confirmed.

## Adopted changes

1. Created `skills/job-opportunity-monitoring/SKILL.md`.
2. Added it to `ARSENAL INDEX.md`.
3. Updated `repository-evidence-docs` with document ownership and empirical lint-rule promotion gates.
4. Added Arc Library to the external UI component reference catalog.
5. No change for Naive-N0.5-Flash.

## Security conclusion

The evaluated repositories contain useful runtimes, but the Arsenal only absorbed portable methodology. No external installer or executable was run, and no credential/scheduler/provider assumption was promoted to a ChatGPT capability.
