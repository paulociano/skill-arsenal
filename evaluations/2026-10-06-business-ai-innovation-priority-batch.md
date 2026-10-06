# Avaliação — 10 repositórios prioritários de negócios e IA

Data: 2026-10-06

## Escopo

Fontes avaliadas:

1. https://github.com/deanpeters/Product-Manager-Skills
2. https://github.com/EdoStra/Marketing-for-Founders
3. https://github.com/firecrawl/firecrawl
4. https://github.com/browser-use/browser-use
5. https://github.com/mem0ai/mem0
6. https://github.com/promptfoo/promptfoo
7. https://github.com/langfuse/langfuse
8. https://github.com/pipecat-ai/pipecat
9. https://github.com/pydantic/pydantic-ai
10. https://github.com/Comfy-Org/ComfyUI

Fluxo: `arsenal-autopilot` + `research-and-synthesize` + revisão manual de segurança/portabilidade.

Nenhum installer, pacote, Docker image, MCP server, browser automation runtime, custom node, provider API ou script externo foi executado durante a avaliação.

## Resultado resumido

Mudanças adotadas:

- `deanpeters/Product-Manager-Skills` → novas skills `stakeholder-strategy` e `product-lifecycle-transition`;
- `firecrawl/firecrawl` → atualização de `web-extraction-pipeline`;
- `pipecat-ai/pipecat` + `pydantic/pydantic-ai` → nova skill `realtime-voice-agent-engineering`;
- `product-management-cycle` atualizado para rotear stakeholder strategy e lifecycle transition;
- `ARSENAL INDEX.md` atualizado.

Fontes mantidas como owners já absorvidos ou referências externas:

- `Marketing-for-Founders` → já incorporado em `go-to-market-strategy`;
- `browser-use` → já incorporado em `computer-use-agent-engineering`;
- `mem0` → já incorporado em `agent-memory-engineering`;
- `promptfoo` → já incorporado em `llm-observability-evaluation` e `llm-red-team-evaluation`;
- `langfuse` → já incorporado em `llm-observability-evaluation`;
- `ComfyUI` → já considerado em `high-fidelity-image-generation`;
- `Pydantic AI` também reforça owners existentes como `structured-output-contract`, `multi-agent-orchestration` e `durable-workflow-engineering`, sem justificar cópias específicas do framework.

---

## 1. deanpeters/Product-Manager-Skills

### Classificação

A/B/D.

### O que faz

Biblioteca ampla de frameworks e workflows de Product Management, com discovery, estratégia, stakeholders, priorização, lifecycle/EOL, market intelligence, entregáveis e AI product work.

### Valor incremental

Grande parte do catálogo tem overlap com o Arsenal atual. Duas lacunas ficaram claras:

1. **Stakeholder strategy** — comparação entre Power × Interest e Impact × Power, incluindo atenção explícita a grupos altamente afetados com baixo poder.
2. **Product lifecycle/EOL** — diagnóstico antes da escolha entre extend, replace, harvest e retire, com EOL tratado como processo operacional completo.

### Segurança

APPROVE metodologicamente; CAUTION para plugins, installers e pacotes de runtime. Nenhuma instalação foi executada.

### Decisão

- `CREATE_NEW stakeholder-strategy`
- `CREATE_NEW product-lifecycle-transition`
- rejeitar importação em massa das 77 skills;
- manter owners existentes para discovery, specs, priorização, métricas, GTM e experimentação.

---

## 2. EdoStra/Marketing-for-Founders

### Classificação

A/B.

### O que faz

Organiza aquisição dos primeiros usuários de SaaS/apps/startups, com táticas por estágio e canal.

### Valor incremental

A metodologia principal já está explicitamente absorvida por `go-to-market-strategy`, incluindo diagnosis-before-tactics, primeiros usuários, canais, launch, buyer/adopter e conexão com activation/economics.

### Segurança

APPROVE como conteúdo/metodologia. Não há motivo para executar automações externas apenas para aproveitar o conhecimento.

### Decisão

`KEEP_EXTERNAL_REFERENCE` porque o valor metodológico relevante já possui owner canônico.

---

## 3. firecrawl/firecrawl

### Classificação

B/D.

### O que faz

Plataforma de aquisição de dados web com search, map, scrape, batch scrape, crawl, structured extraction, browser interaction e agentic retrieval.

### Valor incremental

Refina o owner `web-extraction-pipeline` com:
- distinção explícita search/map/scrape/batch/crawl/interact;
- fluxo map/search → filter → scrape antes de crawler completo;
- structured extraction schema-first;
- jobs assíncronos, status, checkpoint e retomada.

### Segurança

CAUTION alto para runtime real:
- API keys;
- rede;
- proxies;
- browser interaction;
- instalação CLI/MCP;
- possíveis ações em páginas autenticadas.

A metodologia não exige nenhum desses mecanismos.

### Decisão

`UPDATE_EXISTING web-extraction-pipeline`.

Claims promocionais de cobertura, velocidade e benchmark não foram adotados como garantias.

---

## 4. browser-use/browser-use

### Classificação

A/D.

### O que faz

Agente/browser runtime para automação web com biblioteca, CLI, cloud browser, profiles e integrações.

### Valor incremental

O Arsenal já incorporou os padrões centrais em `computer-use-agent-engineering`: grounding, action space, profiles isolados, allowlists, trajectories, evaluation e human takeover.

O README atual também enfatiza cloud browsers, CAPTCHA solving, residential proxies e hosted agents. Isso é infraestrutura, não uma nova metodologia portátil necessária ao Arsenal.

### Segurança

CAUTION alto:
- navegação autenticada;
- credenciais;
- cloud browsers;
- proxies;
- shell em algumas integrações;
- ações externas.

### Decisão

`KEEP_EXTERNAL_REFERENCE`; sem nova skill.

---

## 5. mem0ai/mem0

### Classificação

A/D.

### O que faz

Infraestrutura de memória para agentes com user/session/agent state, retrieval, SDKs, self-hosting e cloud.

### Valor incremental

O owner `agent-memory-engineering` já cita Mem0 e cobre write/read/manage, provenance, source of truth, correção/supersedence, retrieval e avaliação.

A configuração moderna do Mem0 reforça que memory runtime e memory methodology são coisas distintas.

### Segurança

CAUTION:
- persistência de dados pessoais;
- API keys;
- embeddings/LLMs externos;
- cloud storage;
- exposição acidental de memória entre usuários.

### Decisão

`KEEP_EXTERNAL_REFERENCE`; sem duplicação.

---

## 6. promptfoo/promptfoo

### Classificação

A/B/D.

### O que faz

Framework de evals, comparação de modelos/prompts/agentes/RAG e red teaming, integrável a CI.

### Valor incremental

Já está explicitamente absorvido por:
- `llm-observability-evaluation`;
- `llm-red-team-evaluation`.

Os owners existentes já cobrem datasets, regressão, trajectory/tool quality, judges, red teaming e CI.

### Segurança

CAUTION operacional:
- pode chamar providers e endpoints reais;
- red-team pode gerar payloads adversariais;
- plugins/configuração podem ampliar superfície.

### Decisão

`KEEP_EXTERNAL_REFERENCE`; sem alteração necessária.

---

## 7. langfuse/langfuse

### Classificação

A/B/D.

### O que faz

Observabilidade e avaliação de aplicações LLM/agentes com traces, evals, prompts, datasets e feedback.

### Valor incremental

Já é fonte explícita de `llm-observability-evaluation`.

O Arsenal mantém metodologia provider-agnostic e não exige Langfuse como backend.

### Segurança

CAUTION:
- traces podem conter PII, prompts, tool inputs e dados sensíveis;
- SaaS externo muda boundary de dados;
- self-hosting não elimina governança.

### Decisão

`KEEP_EXTERNAL_REFERENCE`.

---

## 8. pipecat-ai/pipecat

### Classificação

A/D.

### O que faz

Framework realtime para voice/multimodal agents, transports, STT/TTS, pipelines, turn-taking, structured conversations e multi-agent handoffs.

### Valor incremental

Havia lacuna real: o Arsenal possuía geração de voz e vídeo sintético, mas não um owner para engenharia de **conversação de voz em tempo real**.

Padrões portáveis:
- streaming pipeline;
- transports;
- VAD/turn-taking;
- barge-in;
- structured conversation state;
- provider-agnostic STT/LLM/TTS;
- observabilidade de latência e sessão.

### Segurança

CAUTION alto:
- áudio/vídeo ao vivo;
- providers externos;
- gravação;
- PII;
- ferramentas com efeitos externos;
- telefonia/WebRTC.

### Decisão

`CREATE_NEW realtime-voice-agent-engineering`.

---

## 9. pydantic/pydantic-ai

### Classificação

A/D.

### O que faz

SDK Python para agentes tipados, structured outputs, tools, realtime voice, image generation, durable execution, evals, subagents, memory e observability.

### Valor incremental

Várias capabilities já têm owners canônicos:
- typed outputs → `structured-output-contract`;
- durable execution → `durable-workflow-engineering`;
- subagents → `multi-agent-orchestration`;
- observability/evals → `llm-observability-evaluation`;
- governance → owners de ação/safety.

O ganho novo material foi o reforço de voice agents como frontend/transport de um agent core, complementando Pipecat.

### Segurança

CAUTION alto para Harness/runtime completo:
- filesystem;
- shell;
- web;
- tools;
- providers;
- background execution;
- credentials.

### Decisão

`ABSORB_METHOD_ONLY` em `realtime-voice-agent-engineering`; não criar skill específica de Pydantic AI.

---

## 10. Comfy-Org/ComfyUI

### Classificação

B/D.

### O que faz

Engine visual por node graphs para image, video, audio, 3D e pipelines generativos, com workflows reutilizáveis e custom nodes.

### Valor incremental

O padrão de pipeline visual por nós já aparece em `high-fidelity-image-generation`. O restante é majoritariamente runtime e ecossistema técnico.

Pode ser uma excelente ferramenta em projetos específicos quando instalada/autorizada, mas isso não justifica uma skill ComfyUI no core do Arsenal.

### Segurança

CAUTION alto:
- custom nodes;
- modelos e weights;
- downloads;
- extensões;
- partner/API nodes;
- supply chain de terceiros.

### Decisão

`KEEP_EXTERNAL_REFERENCE`.

---

## Capability ledger resumido

| Capability | Fonte | Owner | Decisão |
| --- | --- | --- | --- |
| stakeholder mapping/engagement | Product-Manager-Skills | stakeholder-strategy | CREATE_NEW |
| mature/declining product + EOL | Product-Manager-Skills | product-lifecycle-transition | CREATE_NEW |
| early-user marketing | Marketing-for-Founders | go-to-market-strategy | KEEP |
| AI-ready web acquisition | Firecrawl | web-extraction-pipeline | UPDATE_EXISTING |
| browser agents | browser-use | computer-use-agent-engineering | KEEP |
| durable agent memory | Mem0 | agent-memory-engineering | KEEP |
| evals/red team | Promptfoo | llm-observability / llm-red-team | KEEP |
| LLM tracing/evals | Langfuse | llm-observability-evaluation | KEEP |
| realtime voice agents | Pipecat + Pydantic AI | realtime-voice-agent-engineering | CREATE_NEW |
| typed agent framework | Pydantic AI | multiple existing owners | ABSORB_METHOD_ONLY |
| visual generative node graphs | ComfyUI | high-fidelity-image-generation | KEEP |

## Mudanças publicadas

- `skills/stakeholder-strategy/SKILL.md`
- `skills/product-lifecycle-transition/SKILL.md`
- `skills/realtime-voice-agent-engineering/SKILL.md`
- `skills/web-extraction-pipeline/SKILL.md`
- `stacks/product-management-cycle/STACK.md`
- `ARSENAL INDEX.md`
- este registro de avaliação

## Limites

- revisão de segurança foi estática/manual;
- nenhum benchmark promocional foi reproduzido;
- nenhum runtime externo foi instalado;
- disponibilidade, preços, providers e APIs devem ser verificados novamente no momento de uso;
- classificação avalia valor para o Arsenal, não qualidade absoluta do projeto.
