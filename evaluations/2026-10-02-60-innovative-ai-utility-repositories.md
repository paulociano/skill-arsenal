# Evaluation — 60 innovative AI and utility repositories

Date: 2026-10-02

Method: `arsenal-autopilot`.

## Scope

This batch evaluates the 60 repositories selected in the preceding discovery pass. The unit of comparison is capability, not repository name. No installer, package manager, model weight, Docker image, VM, browser extension, cloud service, training script or external executable was run.

Decisions:
- `CREATE_NEW`: capability was materially missing from the Arsenal.
- `UPDATE_EXISTING`: useful methodology improves an existing canonical owner.
- `KEEP_EXTERNAL_REFERENCE`: strong product/runtime/reference, but no new portable owner is justified.
- `REJECT_CURRENT`: no longer a good current reference because the project is archived, read-only, maintenance-only or explicitly superseded.

## Adopted capability clusters

### 1. Generative UI — CREATE_NEW

Sources:
- CopilotKit/OpenGenerativeUI
- thesysdev/openui
- CopilotKit/CopilotKit

Created owner: `generative-ui-engineering`.

Incremental capability:
- distinguish component-grammar generation from unrestricted document generation;
- derive model output contracts from an allowlisted component set;
- stream UI incrementally through a parser/renderer;
- isolate free-form HTML/SVG/Canvas/Three.js in sandboxed documents;
- keep actions behind a host bridge with schema validation and authorization;
- separate "rendering a control" from possessing the capability represented by that control.

Why existing owners were insufficient:
- `web-design-engineer` builds web interfaces but does not own model-generated runtime UI contracts;
- `structured-output-contract` validates schemas but does not own rendering/sandbox semantics;
- `interactive-system-diagram` is a specific artifact type rather than an agent UI protocol.

### 2. Long-term agent memory — CREATE_NEW

Sources:
- TIMAN-group/PlugMem
- tigerless-labs/agent-memory
- mem0ai/mem0
- letta-ai/letta

Created owner: `agent-memory-engineering`.

Incremental capability:
- Write / Read / Manage as separate memory subsystems;
- semantic/procedural/episodic distinctions when useful;
- capture before distillation so missed extraction is recoverable;
- progressive retrieval from index/abstract to full source and raw trace;
- inspectable source of truth with rebuildable indexes when architecture permits;
- temporal validity, correction/supersession and as-of reasoning;
- unattended deletion stricter than unattended add/update;
- evaluation that verifies whether the agent actually exercised the intended memory path.

### 3. Agent runtime action governance — CREATE_NEW

Primary source:
- CopilotKit/OpenBot

Created owner: `agent-action-governance`.

Incremental capability:
- a single pre-execution policy gateway;
- resolve target and classify effect before execution;
- deny-before-allow and fail-closed behavior;
- audit decision before effect;
- credentials used by runtime without entering transcript where possible;
- explicit human takeover/release states;
- different policy for interactive versus scheduled actions;
- audit states that distinguish permitted, refused, failed and succeeded.

This is distinct from `agent-choice-audit`, which audits implementation choices after the fact.

### 4. Computer-use agent engineering — CREATE_NEW

Sources:
- trycua/cua
- simular-ai/Agent-S
- bytedance/UI-TARS-desktop
- microsoft/OmniParser
- browser-use/browser-use
- browserbase/stagehand

Created owner: `computer-use-agent-engineering`.

Incremental capability:
- observe → ground → plan → act → verify loop;
- DOM/accessibility, vision and hybrid perception modes;
- GUI parsers treated as grounding evidence rather than permission;
- observed action spaces and stale-target guards;
- isolated VMs/profiles/workspaces for high-risk execution/evaluation;
- reproducible trajectories;
- human takeover states;
- evaluation beyond success rate: invalid actions, stale targets, retries, safety violations and interventions.

`runtime-ui-verification` remains owner of verifying an application's behavior; the new skill owns design/evaluation of the agent that operates the UI.

### 5. Scientific principle-space evolution — UPDATE_EXISTING

Source:
- eurekaw/pievo

Updated owner: `scientific-hypothesis-discovery`.

Incremental methodology:
- multiple hypotheses can fail because their shared principle/model class is wrong;
- explicitly track which principles generate which hypotheses;
- accumulate anomalies before revising principles;
- distinguish local hypothesis repair from a stronger principle-space update;
- preserve evidence and history of principle changes.

No separate PiEvo skill was created.

## 60-source ledger

| # | Repository | Class | Decision | Canonical owner / reason |
|---:|---|---|---|---|
| 1 | CopilotKit/OpenBot | A/D | CREATE_NEW | `agent-action-governance`; strong runtime policy/audit model |
| 2 | CopilotKit/OpenGenerativeUI | A/D | CREATE_NEW | `generative-ui-engineering`; sandboxed free-form generative UI |
| 3 | thesysdev/openui | A/D | CREATE_NEW | `generative-ui-engineering`; compact streaming component grammar |
| 4 | trycua/cua | A/D | CREATE_NEW | `computer-use-agent-engineering`; drivers, sandboxes, trajectories, benchmarks |
| 5 | simular-ai/Agent-S | A/D | CREATE_NEW | `computer-use-agent-engineering`; GUI agent planning/memory/evaluation |
| 6 | InternScience/InternAgent | A/D | KEEP_EXTERNAL_REFERENCE | scientific multi-agent runtime overlaps hypothesis/research/memory owners |
| 7 | eurekaw/pievo | A/D | UPDATE_EXISTING | adds principle-space evolution to `scientific-hypothesis-discovery` |
| 8 | TIMAN-group/PlugMem | A/D | CREATE_NEW | `agent-memory-engineering`; reusable semantic/procedural/episodic memory graph |
| 9 | tigerless-labs/agent-memory | A/D | CREATE_NEW | `agent-memory-engineering`; files-as-truth, progressive read, manage layer |
| 10 | bytedance/UI-TARS-desktop | A/D | CREATE_NEW | `computer-use-agent-engineering`; visual desktop/browser agent reference |
| 11 | browser-use/browser-use | A/D | ABSORB_METHOD_ONLY | computer-use action/observation patterns; runtime remains external |
| 12 | nanobrowser/nanobrowser | B/D | KEEP_EXTERNAL_REFERENCE | local browser multi-agent product; no distinct owner needed |
| 13 | browserbase/stagehand | A/D | KEEP_EXTERNAL_REFERENCE | observe/act/extract already absorbed by `runtime-ui-verification`; also informs computer-use |
| 14 | microsoft/OmniParser | A/D | CREATE_NEW | visual screen parsing / grounding input for computer-use |
| 15 | openai/openai-agents-python | A/D | KEEP_EXTERNAL_REFERENCE | agent/handoff/guardrail runtime overlaps multi-agent + graph + structured output |
| 16 | google/adk-python | A/D | KEEP_EXTERNAL_REFERENCE | agent framework/runtime; no portable capability gap |
| 17 | pydantic/pydantic-ai | A/D | KEEP_EXTERNAL_REFERENCE | typed agent contracts reinforce `structured-output-contract` |
| 18 | mastra-ai/mastra | A/D | KEEP_EXTERNAL_REFERENCE | TypeScript agent/workflow platform overlaps graph/routing/observability |
| 19 | CopilotKit/CopilotKit | A/D | CREATE_NEW | shared state / HITL / generative UI patterns feed `generative-ui-engineering` |
| 20 | langchain-ai/langgraph | A/D | KEEP_EXTERNAL_REFERENCE | stateful graphs already owned by `graph-engineering` |
| 21 | agno-agi/agno | A/D | KEEP_EXTERNAL_REFERENCE | agent platform/runtime with learning loop; overlap existing owners |
| 22 | microsoft/autogen | D | REJECT_CURRENT | README states maintenance mode; Microsoft Agent Framework is successor |
| 23 | microsoft/semantic-kernel | D | REJECT_CURRENT | README redirects new work to Microsoft Agent Framework |
| 24 | crewAIInc/crewAI | B/D | KEEP_EXTERNAL_REFERENCE | role/crew orchestration overlaps `multi-agent-orchestration` |
| 25 | All-Hands-AI/OpenHands → OpenHands/OpenHands | A/D | KEEP_EXTERNAL_REFERENCE | software-engineering agent/workspace; redirect resolved to current repo |
| 26 | block/goose → aaif-goose/goose | A/D | KEEP_EXTERNAL_REFERENCE | extensible coding agent; redirect resolved to current repo |
| 27 | QwenLM/qwen-code | A/D | KEEP_EXTERNAL_REFERENCE | coding-agent runtime with memory/subagents/MCP; overlaps coding/agent owners |
| 28 | plandex-ai/plandex | A/D | KEEP_EXTERNAL_REFERENCE | long-task coding/planning product; useful reference for persistent coding work |
| 29 | Aider-AI/aider | A/D | KEEP_EXTERNAL_REFERENCE | Git-native coding + repo map; reinforces code-understanding/code-review |
| 30 | continuedev/continue | D | REJECT_CURRENT | README says repository is no longer actively maintained/read-only |
| 31 | cline/cline | A/D | KEEP_EXTERNAL_REFERENCE | IDE/CLI agent with human approvals; overlaps governance/coding runtime |
| 32 | langchain-ai/open-swe | A/D | KEEP_EXTERNAL_REFERENCE | software factory/PR loop; overlaps coding delivery, CI and review skills |
| 33 | mem0ai/mem0 | A/D | CREATE_NEW | memory algorithm/reference for `agent-memory-engineering` |
| 34 | letta-ai/letta | A/D | CREATE_NEW | stateful agent memory reference; README points active source to letta-code |
| 35 | microsoft/graphrag | A/D | KEEP_EXTERNAL_REFERENCE | graph RAG methodology already owned by retrieval/graph skills; maintenance mode |
| 36 | HKUDS/LightRAG | A/D | KEEP_EXTERNAL_REFERENCE | graph-oriented RAG runtime; no new owner |
| 37 | infiniflow/ragflow | A/D | KEEP_EXTERNAL_REFERENCE | document parsing/RAG product overlaps document + retrieval stacks |
| 38 | run-llama/llama_index | A/D | KEEP_EXTERNAL_REFERENCE | context/document framework; current focus shifting toward parsing/extraction |
| 39 | open-webui/open-webui | D | KEEP_EXTERNAL_REFERENCE | self-hosted model/product surface; routing/runtime owners already exist |
| 40 | Mintplex-Labs/anything-llm | D | KEEP_EXTERNAL_REFERENCE | private AI workspace/RAG product; no new portable methodology |
| 41 | ollama/ollama | D | KEEP_EXTERNAL_REFERENCE | already represented in `model-routing-gateway` local-runtime guidance |
| 42 | mudler/LocalAI | D | KEEP_EXTERNAL_REFERENCE | OpenAI-compatible local inference gateway |
| 43 | janhq/jan | D | KEEP_EXTERNAL_REFERENCE | local desktop AI product |
| 44 | ggml-org/llama.cpp | D | KEEP_EXTERNAL_REFERENCE | inference runtime/quantization infrastructure |
| 45 | vllm-project/vllm | D | KEEP_EXTERNAL_REFERENCE | already represented in serving guidance |
| 46 | sgl-project/sglang | D | KEEP_EXTERNAL_REFERENCE | high-performance agentic/multimodal serving runtime |
| 47 | Comfy-Org/ComfyUI | A/D | KEEP_EXTERNAL_REFERENCE | visual generative graph runtime; reinforces graph/pipeline patterns |
| 48 | Lightricks/LTX-Video | D | REJECT_CURRENT | README says LTX-2 is now primary home for development |
| 49 | Wan-Video/Wan2.2 | D | KEEP_EXTERNAL_REFERENCE | video-generation model/runtime; useful external backend only |
| 50 | microsoft/TRELLIS.2 | D | KEEP_EXTERNAL_REFERENCE | already referenced by `image-to-3d` |
| 51 | Tencent-Hunyuan/Hunyuan3D-2.1 | D | KEEP_EXTERNAL_REFERENCE | external 3D generation backend |
| 52 | VAST-AI-Research/TripoSR | D | KEEP_EXTERNAL_REFERENCE | already referenced by `image-to-3d` |
| 53 | TencentARC/InstantMesh | D | KEEP_EXTERNAL_REFERENCE | already referenced by `image-to-3d` |
| 54 | FunAudioLLM/CosyVoice | D | KEEP_EXTERNAL_REFERENCE | speech synthesis/model runtime; no operational capability gap found |
| 55 | fishaudio/fish-speech | D | KEEP_EXTERNAL_REFERENCE | speech/voice model runtime |
| 56 | n8n-io/n8n | A/D | KEEP_EXTERNAL_REFERENCE | production workflow platform; graph/work-delivery/automation owners cover methodology |
| 57 | activepieces/activepieces | A/D | KEEP_EXTERNAL_REFERENCE | type-safe pieces + MCP exposure are implementation/runtime patterns |
| 58 | langflow-ai/langflow | A/D | KEEP_EXTERNAL_REFERENCE | visual agent graph + API/MCP runtime overlaps graph engineering |
| 59 | langgenius/dify | A/D | KEEP_EXTERNAL_REFERENCE | end-to-end AI app platform; capabilities already decomposed across owners |
| 60 | FlowiseAI/Flowise | D | REJECT_CURRENT | repository is archived |

## Security and portability findings

### Generative UI
Risks:
- model-generated HTML/JS can become arbitrary code execution;
- CDN/import maps can expand supply-chain surface;
- host bridges can accidentally expose secrets or privileged actions;
- streaming partial code can execute before validation.

Adaptation:
- component grammar first;
- sandbox free-form UI;
- validate bridge calls server/host-side;
- no direct credential/DOM/storage capability by default.

### Agent memory
Risks:
- long-term storage amplifies sensitive-data retention;
- embeddings may send content to external providers;
- automatic consolidation can rewrite or delete useful history;
- stale/incorrect memory can silently bias later decisions.

Adaptation:
- explicit scope and retention;
- no secrets;
- provenance;
- temporal validity;
- delete proposals stricter than add/update;
- evaluate actual retrieval exposure.

### Agent action governance / computer use
Risks:
- shell, browser sessions, authenticated accounts, files and remote writes are high-impact;
- screenshots/traces may capture secrets;
- stale coordinates can mutate the wrong target;
- VM/container isolation does not authorize the action;
- unknown tools may be incorrectly classified as read-only.

Adaptation:
- fail closed;
- audit before act;
- revalidate target;
- minimum permissions;
- human takeover;
- no runtime execution assumed merely because a source supports it.

### External models/runtimes
Ollama, LocalAI, llama.cpp, vLLM, SGLang, TRELLIS.2, Hunyuan3D, TripoSR, InstantMesh, Wan, CosyVoice and Fish Speech remain external dependencies. Hardware, model weights, licenses, checkpoint terms and runtime security must be revalidated at use time.

## What was deliberately not imported

- framework-specific CLIs;
- Docker/VM orchestration;
- model/provider credentials;
- AG-UI, MCP, A2A or OpenUI as mandatory protocols;
- specific benchmarks as universal quality claims;
- published model scores as routing truth;
- vendor cloud services;
- component libraries or model weights;
- automatic shell/browser permissions.

## Canonical changes from this batch

Created:
- `skills/generative-ui-engineering/SKILL.md`
- `skills/agent-memory-engineering/SKILL.md`
- `skills/agent-action-governance/SKILL.md`
- `skills/computer-use-agent-engineering/SKILL.md`

Updated:
- `skills/scientific-hypothesis-discovery/SKILL.md`
- `ARSENAL INDEX.md`

The rest remain external references or rejected-as-current sources.
