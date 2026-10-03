# Avaliação — lote de 22 repositórios multidomínio

Data: 2026-10-03

## Objetivo

Avaliar um lote heterogêneo de 22 repositórios enviados em sequência, cobrindo fitness assets, AI workspaces, OCR, voice UX, software factories, agent orchestration, local inference, embodied AI, persistent worlds, architecture visualization e support operations.

A unidade de adoção foi capability, não repositório.

## Resultado executivo

### Novos owners

- `software-factory-operations`
- `local-llm-inference-engineering`
- `embodied-agent-evaluation`
- `interactive-world-simulation`
- `support-operations-engineering`

### Owners/stacks atualizados

- `document-extraction-pipeline`
- `architecture-visualization`
- `empirical-prompt-tuning`
- `agent-memory-engineering`
- `agent-action-governance`
- `multi-agent-orchestration`
- `codex-cost-efficiency`
- `llm-observability-evaluation`
- `web-design-engineer`
- `ai-workspace-operating-cycle`
- `software-engineering-cycle`
- `game-development-cycle`
- `ARSENAL INDEX.md`

## Triage dos 22 repositórios

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 1 | bryllim/workout-guide | B/D | KEEP_EXTERNAL_REFERENCE |
| 2 | rome-os/rome | A/D | UPDATE_EXISTING |
| 3 | kgoedecke/doop | A/D | UPDATE_EXISTING |
| 4 | thiagotigaz/ocr-it | A/D | UPDATE_EXISTING |
| 5 | TarunTomar122/better-voice | A/D | UPDATE_EXISTING |
| 6 | proliferate-ai/proliferate | A/D | UPDATE_EXISTING |
| 7 | inkboard/system-atlas | A/D | UPDATE_EXISTING |
| 8 | kunchenguid/backpass | A/D | UPDATE_EXISTING |
| 9 | addyosmani/factory | A/D | CREATE_NEW |
| 10 | halofyai/halofy | A/D | UPDATE_EXISTING |
| 11 | NVlabs/SoL-Pi | A/D | UPDATE_EXISTING |
| 12 | donvito/codex-astra-luna-orchestrator | B/D | ABSORB_METHOD_ONLY |
| 13 | rizqinrr/viserys-agent | A/B/D | ABSORB_METHOD_ONLY |
| 14 | Edge0-AI/Edge0 | A/D | CREATE_NEW |
| 15 | air-embodied-brain/Zetta-Embodiment | A/D | CREATE_NEW |
| 16 | unstablebuild/rune | A/D | UPDATE_EXISTING |
| 17 | DefiLeoo/YOINK | A/D | UPDATE_EXISTING |
| 18 | anonymous-report-421/GPT-as-Policy | A/D | UPDATE_EXISTING |
| 19 | Qiuner/birdview | A/D | UPDATE_EXISTING |
| 20 | BuzzPlay/infinite-world | A/D | CREATE_NEW |
| 21 | letstri/motion-panels | B/D | UPDATE_EXISTING |
| 22 | mirza-rizvi/ResolveHQ | A/D | CREATE_NEW |

## 1. bryllim/workout-guide

### O que faz

Biblioteca de 302 exercícios, com três frames consistentes por exercício, SVG/PNG normalizados, metadata tipada, busca e gallery estática.

### Decisão

KEEP_EXTERNAL_REFERENCE.

É excelente asset library para guias de treino, mas não adiciona metodologia suficiente para criar um owner de treino no Arsenal. O valor é operacional:
- catálogo consistente;
- metadata estruturada;
- assets transparentes;
- integração web/mobile;
- licença CC BY-SA para assets.

Quando um projeto de fitness precisar de ilustrações, o repo pode ser consultado como referência/assets, com atribuição adequada.

## 2. rome-os/rome

### Capabilities

- actions;
- skills;
- apps persistentes;
- private app data;
- hooks/workflows;
- compounding de capabilities;
- código versionável/exportável.

### Decisão

UPDATE_EXISTING em `ai-workspace-operating-cycle`.

Padrão adotado:
`workflow recorrente → capability/app persistente`.

Não foi criado owner próprio de Rome/apps porque o comportamento pertence ao workspace persistente.

## 3. kgoedecke/doop

### Capabilities

- multiplayer AI canvas;
- human + agent presence;
- cursor/state compartilhados;
- design memory;
- AI-aware collaborative workspace.

### Decisão

UPDATE_EXISTING em `ai-workspace-operating-cycle`.

Valor absorvido:
- presença atribuível;
- edits/status visíveis;
- design memory como artifact, não memória invisível;
- canvas como view do record canônico.

## 4. thiagotigaz/ocr-it

### Capabilities

- OCR por região fixa;
- processamento página a página;
- auto-advance;
- duplicate-page detection;
- thumbnails de QA;
- OCR local;
- layout segmentation.

### Decisão

UPDATE_EXISTING em `document-extraction-pipeline`.

Entrou como **region-locked sequential OCR** para documentos em viewers paginados onde text layer não está acessível.

## 5. TarunTomar122/better-voice

### Capability principal

Voice interaction com apontamento/referência visual contextual.

### Decisão

UPDATE_EXISTING em `ai-workspace-operating-cycle`.

Padrão adotado:
`spoken intent + pointer/selection reference → contextual instruction`.

Guardrail:
referência deíctica não equivale a autorização de ação.

## 6. proliferate-ai/proliferate

### Capabilities

- coding agents paralelos;
- worktree-per-task;
- native harnesses;
- shared integrations;
- subagent delegation;
- isolated task state.

### Decisão

UPDATE_EXISTING em `multi-agent-orchestration`.

Entraram:
- isolamento por tarefa;
- subset mínimo de ferramentas por worker;
- child result precisa retornar ao coordinator;
- completion de subagent não significa integration complete.

## 7. inkboard/system-atlas

### Capabilities

- arquitetura como spec única;
- interactive atlas;
- generated text twin;
- chapters/progressive disclosure;
- question tracking;
- rebuild sincronizado de views.

### Decisão

UPDATE_EXISTING em `architecture-visualization`.

Padrão adotado:
`single source spec → interactive atlas + text twin`.

## 8. kunchenguid/backpass

### Capabilities

- aprender a partir de sessões reais;
- detectar falhas recorrentes;
- propor diffs de memória/instruções;
- exigir evidência de múltiplas sessões;
- human apply gate;
- pequenos gradient steps.

### Decisão

UPDATE_EXISTING em:
- `empirical-prompt-tuning`;
- `agent-memory-engineering`.

O Arsenal preserva evidence-gated memory edits e rejeita auto-modificação baseada em uma única sessão.

## 9. addyosmani/factory

### Lacuna encontrada

O Arsenal tinha multi-agent orchestration, code review e software engineering cycle, mas não um owner de **operação contínua de software factory**.

### Decisão

CREATE_NEW: `software-factory-operations`.

Capabilities:
- human-owned charter;
- durable queue;
- deterministic claim;
- triage;
- spec gate;
- isolated implementation;
- fail-closed deterministic checks;
- independent verifier;
- draft PR;
- numeric review back-pressure;
- human merge.

Princípio adotado:
**autonomy by consequence, not difficulty**.

## 10. halofyai/halofy

### Capabilities

- organizational context governance;
- server-owned identity;
- namespaces;
- ACL-scoped retrieval;
- supersedence;
- signed/auditable erasure;
- replaceable retrieval backend.

### Decisão

UPDATE_EXISTING em:
- `agent-memory-engineering`;
- `agent-action-governance`.

Padrão central:
policy boundary não deve ficar dentro do vector/search backend.

## 11. NVlabs/SoL-Pi

### Capabilities

- Action Fusion;
- ObservationPack;
- Evidence-Preserving Reducer;
- Online Context Compact;
- auto-research de eficiência de harness.

### Decisão

UPDATE_EXISTING em `codex-cost-efficiency`.

Entraram:
- edit/write + validation fusion quando seguro;
- large observation handles com recall exato;
- reduction apenas com evidence preservation;
- compaction em pontos de conclusão, não arbitrariamente.

Nenhum percentual de economia da fonte foi adotado como garantia.

## 12. donvito/codex-astra-luna-orchestrator

### Capabilities

- root/orchestrator;
- explorer;
- researcher;
- worker;
- tester;
- reviewer;
- perfil de modelos por papel.

### Decisão

ABSORB_METHOD_ONLY em `multi-agent-orchestration`.

O Arsenal absorveu **role contracts + independent reviewer** e rejeitou model pinning específico como regra universal.

## 13. rizqinrr/viserys-agent

### Capabilities

`DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP`

com skills/personas/commands/checklists/validators multi-harness.

### Decisão

ABSORB_METHOD_ONLY.

O Arsenal já possui owners para spec, build, testing, review e shipping. O valor incremental foi reforçar:
- contracts explícitos por etapa;
- validators estruturais;
- separação entre implementação e review.

Não foi criada uma skill “Viserys”.

## 14. Edge0-AI/Edge0

### Lacuna encontrada

Não havia owner de inferência local/on-device de LLMs.

### Decisão

CREATE_NEW: `local-llm-inference-engineering`.

Capabilities:
- SSD expert offload;
- active-set memory budget;
- routing prediction/prefetch;
- quantization + quality recovery;
- immutable base + adapters;
- backend isolation;
- cold/warm benchmark;
- matched-quality comparisons.

Guardrail:
tokens/s sozinho não mede experiência real.

## 15. air-embodied-brain/Zetta-Embodiment

### Lacuna encontrada

Não havia owner para evolução/eval rigorosa de agents embodied/robóticos.

### Decisão

CREATE_NEW: `embodied-agent-evaluation`.

Pipeline:
`rollouts → failure cluster → diagnose → candidate → shadow replay → paired same-seed gate → held-out gate → promotion`.

Role boundary:
critic proposes; decision authority accepts/rejects; recovery actor executes bounded action; environment actor owns simulator write.

## 16. unstablebuild/rune

### Capabilities

- IDE/terminal multiplexer;
- persistent workspaces;
- headless node;
- encrypted peer network;
- multi-device continuity;
- plugins/skills.

### Decisão

UPDATE_EXISTING em:
- `ai-workspace-operating-cycle`;
- `multi-agent-orchestration`.

Valor:
workspace persistente/headless e continuidade entre dispositivos, preservando rede/filesystem/auth como boundaries.

## 17. DefiLeoo/YOINK

### Capabilities

- markdown source of truth;
- claims precommitted;
- settlement por fonte/teste explícito;
- calibration gap;
- Brier score;
- dead-note metrics;
- append-only hash-chained ledger.

### Decisão

UPDATE_EXISTING em `llm-observability-evaluation`.

Entraram:
- claims precisam ser settleable;
- fonte/teste definidos antes do outcome;
- settlement separado;
- calibration/Brier;
- ledger auditável/tamper-evident.

O Arsenal não absorveu qualquer capability de blockchain write; o próprio repo é read-only nessa superfície.

## 18. anonymous-report-421/GPT-as-Policy

### Capabilities

- GPT como direct embodied policy;
- hybrid reviewer/corrector sobre política base;
- aligned task/scene/seed cases;
- intervention-rate measurement;
- public report separado de control plane.

### Decisão

UPDATE_EXISTING em `embodied-agent-evaluation`.

Entrou comparação:
**direct policy vs hybrid review/correct policy**, com cases/seeds alinhados e intervention rate explícita.

Public reference não foi tratado como same-seed rerun.

## 19. Qiuner/birdview

### Capabilities

- architecture map;
- reviewed constraints;
- source coverage;
- declared change scope;
- confirmation before edit;
- actual verification records;
- standalone interactive HTML.

### Decisão

UPDATE_EXISTING em `architecture-visualization`.

Entrou o padrão:
`architecture + reviewed constraints + proposed change scope + coverage + verification`.

Importante:
agent-declared activity não é automaticamente observed runtime activity.

## 20. BuzzPlay/infinite-world

### Lacuna encontrada

`procedural-game-content` gera worlds/levels, e `narrative-dialogue-engineering` gerencia branching narrative, mas nenhum owner mantinha um **world state multimodal persistente**.

### Decisão

CREATE_NEW: `interactive-world-simulation`.

Modelo:
- World;
- Scene;
- Interaction;
- Branch;
- History;
- Output;
- Preview;
- Replay.

Regra central:
**a cena é projeção do estado do mundo, não a fonte canônica do mundo.**

## 21. letstri/motion-panels

### Capabilities

- framework-agnostic resizing core;
- folding/collapse/snap animados;
- nested panels;
- reordering;
- keyboard;
- RTL;
- pixel/percentage size.

### Decisão

UPDATE_EXISTING em `web-design-engineer`.

Padrão adotado para workspaces:
- resize engine separado da camada visual;
- motion sobre layout real;
- min/max;
- keyboard/RTL;
- nesting/reordering rules.

Não justifica owner próprio.

## 22. mirza-rizvi/ResolveHQ

### Lacuna encontrada

Não havia owner para helpdesk/support operations.

### Decisão

CREATE_NEW: `support-operations-engineering`.

Capabilities:
- shared inbox;
- reliable email threading;
- assignment/status/priority/tags;
- SLA-aware schedules;
- snooze/wake;
- durable outbound/inbound queues;
- DLQ/recovery;
- KB/help center;
- scoped API keys;
- read-only MCP;
- AI opt-in;
- exports/erasure;
- retention;
- CSAT/reporting.

Guardrail:
AI-drafted response não é autorização para enviar.

## Segurança e portabilidade

Verdict geral: **CAUTION**, com áreas HIGH em embodied/robotics e credential-bearing agent runtimes.

Nenhum installer, shell script, model weight, Docker image, simulator, GPU runtime, browser extension ou external service foi executado.

### Superfícies encontradas

- curl/pipe-shell installers;
- agent hooks;
- remote/headless IDE networking;
- OAuth/API keys;
- MCP write surfaces;
- browser Accessibility/screen capture;
- email sending;
- scoped API keys;
- model weights;
- GPU/CUDA/MLX;
- simulators/robot actions;
- voice/visual capture;
- external AI providers;
- support customer data.

### Adaptações

- methodology separated from runtime;
- model names/profiles are not permanent Arsenal rules;
- external write remains approval-gated;
- embodied simulation does not imply real-robot safety;
- read-only integration preferred when write approval UX does not exist;
- local-first is not equivalent to zero privacy risk;
- benchmarks are source claims unless independently reproduced.

## Materialização

### Criados

- `skills/software-factory-operations/SKILL.md`
- `skills/local-llm-inference-engineering/SKILL.md`
- `skills/embodied-agent-evaluation/SKILL.md`
- `skills/interactive-world-simulation/SKILL.md`
- `skills/support-operations-engineering/SKILL.md`

### Atualizados

- `skills/document-extraction-pipeline/SKILL.md`
- `skills/architecture-visualization/SKILL.md`
- `skills/empirical-prompt-tuning/SKILL.md`
- `skills/agent-memory-engineering/SKILL.md`
- `skills/agent-action-governance/SKILL.md`
- `skills/multi-agent-orchestration/SKILL.md`
- `skills/codex-cost-efficiency/SKILL.md`
- `skills/llm-observability-evaluation/SKILL.md`
- `skills/web-design-engineer/SKILL.md`
- `stacks/ai-workspace-operating-cycle/STACK.md`
- `stacks/software-engineering-cycle/STACK.md`
- `stacks/game-development-cycle/STACK.md`
- `ARSENAL INDEX.md`

## Limites

- avaliação aprofundou README/documentos centrais e arquitetura representativa;
- não houve auditoria linha-a-linha de todos os 22 repositórios;
- claims de benchmark/performance não foram reproduzidos;
- roadmap não foi tratado como feature atual;
- licenças de modelos/assets/dependencies precisam ser verificadas no uso concreto;
- workout-guide permanece referência externa de assets, não owner metodológico.
