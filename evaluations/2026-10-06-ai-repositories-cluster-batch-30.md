# Avaliação — 30 repositórios de IA por clusters

Data: 2026-10-06

## Escopo

Lote avaliado por clusters de capability, usando `arsenal-autopilot` e o `ARSENAL INDEX.md` como router.

Nenhum installer, pacote, Docker image, MCP server, extensão, provider API ou script externo foi executado.

## Resultado resumido

Mudanças adotadas:
- nova skill `ai-workflow-automation-engineering`;
- nova skill `coding-agent-engineering`;
- `local-llm-inference-engineering` refinada com seleção explícita de runtime;
- `software-engineering-cycle` atualizado para rotear automação AI-first e coding agents;
- `ARSENAL INDEX.md` atualizado.

A maioria dos repositórios reforçou owners já existentes em vez de justificar skills novas.

## Capability ledger

| # | Repositório | Classe | Capability principal | Owner/decisão |
|---|---|---|---|---|
| 1 | n8n-io/n8n | A/D | AI workflow automation, connectors, approvals | CREATE/REFINE → `ai-workflow-automation-engineering` |
| 2 | ollama/ollama | A/D | local model runtime/convenience layer | UPDATE → `local-llm-inference-engineering` |
| 3 | huggingface/transformers | A/D | model framework, multimodal inference/training | UPDATE → `local-llm-inference-engineering` |
| 4 | langgenius/dify | A/D | visual AI workflows, RAG, agents, LLMOps | ABSORB → `ai-workflow-automation-engineering`; workspace capabilities already covered |
| 5 | open-webui/open-webui | B/D | self-hosted multi-model AI interface | KEEP_EXTERNAL_REFERENCE → `ai-workspace-operating-cycle` |
| 6 | langchain-ai/langchain | A/D | agent engineering/orchestration | KEEP → graph, multi-agent, retrieval and tool owners already exist |
| 7 | ggml-org/llama.cpp | A/D | portable/embedded local inference | UPDATE → `local-llm-inference-engineering` |
| 8 | vllm-project/vllm | A/D | high-throughput LLM serving | UPDATE/KEEP → local inference + `model-routing-gateway` |
| 9 | infiniflow/ragflow | A/D | RAG + agent context layer | KEEP → `retrieval-quality-engineering` |
| 10 | Mintplex-Labs/anything-llm | B/D | local-first AI workspace | KEEP_EXTERNAL_REFERENCE → `ai-workspace-operating-cycle` |
| 11 | microsoft/autogen | A/D | agentic/multi-agent framework | KEEP → `multi-agent-orchestration`, `graph-engineering` |
| 12 | BerriAI/litellm | A/D | model gateway/routing | KEEP → already primary provenance of `model-routing-gateway` |
| 13 | crewAIInc/crewAI | A/D | collaborative multi-agent orchestration | KEEP → `multi-agent-orchestration` |
| 14 | run-llama/llama_index | A/D | document/RAG context platform | KEEP → retrieval/document owners |
| 15 | Aider-AI/aider | A/D | interactive repo-level coding agent | CREATE → `coding-agent-engineering` |
| 16 | agno-agi/agno | A/D | agent platform/runtime | KEEP → existing agent owners |
| 17 | continuedev/continue | B/D | coding agent/IDE/CLI patterns | ABSORB → `coding-agent-engineering`; repo README states project is read-only |
| 18 | microsoft/semantic-kernel | A/D | LLM app/agent integration | KEEP → existing structured output, tools and agent owners |
| 19 | google/adk-python | A/D | agent development/evaluation/deployment | KEEP → multi-agent, eval and production owners |
| 20 | openai/openai-agents-python | A/D | lightweight multi-agent workflows | KEEP → `multi-agent-orchestration` |
| 21 | activepieces/activepieces | A/D | type-safe integrations, approvals, AI automation | CREATE/REFINE → `ai-workflow-automation-engineering` |
| 22 | triggerdotdev/trigger.dev | A/D | long-running AI tasks/workflows | ABSORB → AI workflow automation + existing durable workflow owner |
| 23 | Skyvern-AI/skyvern | A/D | browser workflow automation | KEEP → `computer-use-agent-engineering` |
| 24 | langflow-ai/langflow | A/D | visual agents/workflows, API/MCP export | CREATE/REFINE → `ai-workflow-automation-engineering` |
| 25 | opencode-ai/opencode | D | terminal coding agent | REJECT as current owner candidate: repository archived; historical reference only |
| 26 | charmbracelet/crush | A/D | terminal coding agent, LSP, sessions, MCP | CREATE/REFINE → `coding-agent-engineering` |
| 27 | microsoft/agent-framework | A/D | production agents/workflows, checkpointing, HITL | KEEP → multi-agent, graph, durable workflow, observability owners |
| 28 | Portkey-AI/gateway | A/D | AI gateway, guardrails, routing, MCP gateway | KEEP → `model-routing-gateway` + governance owners |
| 29 | onyx-dot-app/onyx | A/D | organizational context layer, ACL-aware RAG | KEEP → `ai-workspace-operating-cycle`, `agent-memory-engineering`, retrieval |
| 30 | TEN-framework/ten-framework | A/D | conversational voice agent framework | KEEP → `realtime-voice-agent-engineering` |

## Cluster 1 — AI workflow automation

### Fontes
- n8n
- Activepieces
- Dify
- Langflow
- Trigger.dev

### Gap detectado

O Arsenal possuía:
- `graph-engineering` para topologia;
- `durable-workflow-engineering` para durability;
- `agent-action-governance` para effects;
- `structured-output-contract` para contratos.

Mas faltava um owner para o problema prático de **conectar triggers, SaaS/APIs, regras, agentes, approvals, connectors, versioning e observability em automações AI-first**, especialmente em builders visuais/low-code.

### Decisão

`CREATE_NEW ai-workflow-automation-engineering`.

Padrões preservados:
- triggers e connectors;
- deterministic vs AI steps;
- human-in-loop;
- retries/idempotency;
- versioning;
- visual workflows como software;
- credentials/runtime boundary;
- observability por run.

Não foram importados:
- node catalogs;
- marketplace packages;
- Docker/setup;
- MCP servers;
- cloud-specific deployment.

## Cluster 2 — Coding agents

### Fontes
- Aider
- Continue
- Crush
- opencode (histórico/arquivado)

### Gap detectado

`software-factory-operations` cobre execução recorrente em fila e revisão humana, mas não o design de um **coding agent interativo** em IDE/terminal.

### Decisão

`CREATE_NEW coding-agent-engineering`.

Padrões preservados:
- repo map/context seletivo;
- LSP/symbol context;
- Git/diff/revert;
- patch locality;
- edit → lint/test → repair;
- sessões e handoff;
- multi-model como deployment choice;
- autonomy tiers.

Não foram importados:
- installers;
- auto-commit obrigatório;
- providers;
- shell irrestrito;
- telemetria/config específica.

## Cluster 3 — Local inference and serving

### Fontes
- Ollama
- llama.cpp
- vLLM
- Hugging Face Transformers

### Gap detectado

O owner `local-llm-inference-engineering` já cobria quantização, offload, adapters e benchmarking, mas não distinguia claramente as classes de runtime.

### Decisão

`UPDATE_EXISTING local-llm-inference-engineering` com quatro papéis:
- convenience/local model manager;
- embedded/portable inference;
- high-throughput serving;
- model framework/experimentation.

Referências exemplares:
- Ollama;
- llama.cpp;
- vLLM;
- Transformers.

Nenhum runtime é obrigatório.

## Cluster 4 — Agent frameworks

### Fontes
- LangChain
- AutoGen
- CrewAI
- Agno
- Semantic Kernel
- Google ADK
- OpenAI Agents SDK
- Microsoft Agent Framework

### Decisão

`KEEP/ABSORB_METHOD_ONLY`.

O Arsenal já possui owners mais estáveis por capability:
- `multi-agent-orchestration`;
- `graph-engineering`;
- `durable-workflow-engineering`;
- `agent-action-governance`;
- `structured-output-contract`;
- `llm-observability-evaluation`.

Criar uma skill por framework reduziria portabilidade.

Microsoft Agent Framework reforça especialmente:
- sequential/concurrent/handoff/group patterns;
- checkpointing;
- streaming;
- human-in-loop;
- OpenTelemetry;
- declarative agents.

Esses padrões já possuem owners canônicos.

## Cluster 5 — RAG, context and workspaces

### Fontes
- RAGFlow
- LlamaIndex
- Open WebUI
- AnythingLLM
- Onyx

### Decisão

`KEEP_EXTERNAL_REFERENCE` ou owners existentes.

Mapeamento:
- retrieval quality → `retrieval-quality-engineering`;
- organizational memory/context → `agent-memory-engineering`;
- persistent workspaces → `ai-workspace-operating-cycle`;
- document ingestion → document extraction owners;
- action governance → `agent-action-governance`.

Onyx reforça um princípio já incorporado: ACL/identity precisa permanecer no boundary de retrieval, não ser inferida pelo modelo.

## Cluster 6 — Gateways

### Fontes
- LiteLLM
- Portkey

### Decisão

`KEEP`.

`model-routing-gateway` já cobre:
- provider/model routing;
- retries vs fallback;
- budget;
- capability checks;
- observability;
- credentials;
- privacy;
- local runtimes;
- failure handling.

Portkey acrescenta implementações de guardrails e MCP gateway, mas não cria capability nova independente dos owners atuais.

## Cluster 7 — Browser and voice

### Fontes
- Skyvern
- TEN Framework

### Decisão

`KEEP`.

Owners:
- browser automation → `computer-use-agent-engineering`;
- realtime conversational voice → `realtime-voice-agent-engineering`.

## Segurança e portabilidade

Revisão estática/semântica. Riscos recorrentes do lote:
- installers curl/PowerShell;
- Docker/self-hosting;
- provider/API keys;
- connectors OAuth;
- MCP/plugins;
- shell/code execution;
- browser actions;
- community integrations;
- model downloads;
- traces contendo dados sensíveis;
- actions externas;
- licenses source-available/fair-code distintas de OSS permissivo.

Nenhuma dessas dependências foi presumida disponível ou executada.

## Mudanças publicadas

- `skills/ai-workflow-automation-engineering/SKILL.md`
- `skills/coding-agent-engineering/SKILL.md`
- `skills/local-llm-inference-engineering/SKILL.md`
- `stacks/software-engineering-cycle/STACK.md`
- `ARSENAL INDEX.md`
- este registro de avaliação

## Conclusão

Os 30 repositórios produziram somente dois novos owners. Isso é intencional.

O Arsenal agora consegue representar:
- automações AI-first independentes de n8n/Dify/Langflow/Activepieces;
- coding agents independentes de Aider/Crush/Continue;
- seleção de runtime local/serving sem amarrar arquitetura a Ollama, llama.cpp, vLLM ou Transformers.

Os demais projetos permanecem referências valiosas para implementação, mas não justificam duplicação de capability.
