# Avaliação — 16 repositórios de engenharia de software

Data: 2026-10-03

## Objetivo

Avaliar 15 repositórios selecionados de engenharia de software mais o repositório adicional `Charlytoc/ai-todo-app`, comparando-os com o Arsenal canônico e adotando apenas capacidades incrementais.

## Resultado executivo

Criados:
- `software-testing-engineering`
- `software-observability-engineering`
- `durable-workflow-engineering`
- `developer-platform-engineering`
- `software-supply-chain-engineering`
- `build-system-engineering`
- stack `software-engineering-cycle`

Atualizados:
- `production-go-live` com reproducible delivery e GitOps;
- `deep-grill` com modo draft-first inspirado em `ai-todo-app`;
- `ARSENAL INDEX.md`.

## Triage

| # | Repositório | Classe | Decisão |
|---|---|---|---|
| 1 | donnemartin/system-design-primer | A/B | KEEP_EXISTING_OWNER |
| 2 | testcontainers/testcontainers-java | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| 3 | HypothesisWorks/hypothesis | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| 4 | semgrep/semgrep | A/D | ABSORB_METHOD_ONLY |
| 5 | renovatebot/renovate | A/D | ABSORB_METHOD_ONLY |
| 6 | getsentry/sentry | A/D | ABSORB_METHOD_ONLY |
| 7 | open-telemetry/opentelemetry-collector | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| 8 | temporalio/temporal | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| 9 | backstage/backstage | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| 10 | bazelbuild/bazel | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| 11 | pantsbuild/pants | A/D | ABSORB_METHOD_ONLY |
| 12 | argoproj/argo-cd | A/D | UPDATE_EXISTING |
| 13 | dagger/dagger | A/D | UPDATE_EXISTING + ABSORB_METHOD_ONLY |
| 14 | aquasecurity/trivy | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| 15 | adr/madr | B | KEEP_EXISTING_OWNER |
| 16 | Charlytoc/ai-todo-app | B/C/D | ABSORB_METHOD_ONLY |

## 1. Software Testing Engineering

### Fontes
- Hypothesis
- Testcontainers

### Valor incremental

`tdd` já cobre red-green, mas não tinha owner geral para:
- property-based testing;
- invariant generation;
- shrinking;
- integration com dependências reais descartáveis;
- contract/E2E layering;
- flakiness control.

### Capabilities adotadas
- definir invariantes antes de generators;
- encontrar edge cases por geração;
- reduzir contraexemplo ao menor caso;
- testar banco/broker/cache real quando semântica importa;
- escolher a camada mais barata que prova o risco;
- retry de teste não transforma falha em pass.

### Decisão

Criar `software-testing-engineering`.

## 2. Software Observability Engineering

### Fontes
- OpenTelemetry Collector
- Sentry

### Capabilities adotadas
- traces, metrics e logs como sinais distintos;
- `receive → process → export`;
- correlation;
- cardinality budgets;
- sampling;
- SLO signals;
- telemetry pipeline health;
- production debugging;
- privacy/redaction.

### Decisão

Criar `software-observability-engineering`.

## 3. Durable Workflow Engineering

### Fonte principal
- Temporal

### Valor incremental

`graph-engineering` cobre topologia/dependências, mas não a sobrevivência do estado de execução a crashes, retries e long-running processes.

### Capabilities adotadas
- durable state/history;
- replay;
- activities separadas de orchestration;
- retries com idempotency;
- timers;
- external signals;
- compensation;
- human approval;
- workflow versioning;
- crash-between-effect-and-ack como failure mode de primeira classe.

### Decisão

Criar `durable-workflow-engineering`.

## 4. Developer Platform Engineering

### Fonte principal
- Backstage

### Capabilities adotadas
- software catalog;
- explicit ownership;
- golden paths;
- templates;
- self-service;
- docs-as-code;
- platform metrics;
- paved road com escape hatch.

### Decisão

Criar `developer-platform-engineering`.

`golden-path-capture` continua owner da promoção de workflows comprovados; a nova skill cuida da plataforma que disponibiliza caminhos e capacidades aos times.

## 5. Software Supply Chain Engineering

### Fontes
- Trivy
- Renovate
- Semgrep

### Capabilities adotadas
- dependency inventory;
- lock/pinning;
- automated dependency updates;
- vulnerability scanning;
- SBOM;
- secret scanning;
- IaC/misconfiguration;
- licenses;
- artifact provenance/signatures;
- finding triage por reachability/impact;
- exceptions com owner/expiry.

### Decisão

Criar `software-supply-chain-engineering`.

`secure-code-privacy-review` continua owner de vulnerabilidade/privacidade no código. A nova skill cobre a cadeia de dependências e artifacts.

## 6. Build System Engineering

### Fontes
- Bazel
- Pants
- Dagger

### Capabilities adotadas
- explicit dependency graph;
- hermetic inputs/toolchains;
- incremental execution;
- content-addressed caching;
- remote execution;
- monorepo ownership;
- affected targets;
- build metrics/critical path.

### Decisão

Criar `build-system-engineering`.

## 7. Production Go-Live

### Fontes
- Dagger
- Argo CD

### Decisão
UPDATE_EXISTING.

Adicionado a `production-go-live`:
- reproducible pipeline;
- local/CI logical parity where possible;
- immutable artifacts;
- desired state in version control;
- reconciliation/drift;
- CI/CD boundary;
- rollback limits across data/migrations.

Não foi criada `gitops-engineering` isolada porque o comportamento pertence ao ciclo de produção já existente.

## 8. System Design Primer

O Arsenal já possui `system-design-engineering`, originalmente adaptado desse mesmo repo.

Decisão: KEEP_EXISTING_OWNER.

Nenhuma nova skill ou duplicação.

## 9. MADR

O Arsenal já possui ADR guidance dentro de `domain-modeling`.

Decisão: KEEP_EXISTING_OWNER.

Não criar `adr-engineering`.

## 10. ai-todo-app

### O que o repo faz

App React/Vite + Express + Socket.IO no qual:
- usuário cria um todo;
- AI gera um primeiro draft;
- AI pode emitir uma ação textual `ask`;
- frontend transforma a action em campos;
- respostas são adicionadas ao contexto;
- draft é regenerado iterativamente;
- pending actions permanecem no estado do todo.

### Valor metodológico real

O padrão útil é:

`task → useful draft → limited clarifying questions → structured answers → revised draft → repeat`

Isso reduz bloqueio por perguntas antecipadas e dá ao usuário algo concreto para reagir.

### Problemas rejeitados

- parser de action delimitado por strings no texto do modelo;
- ausência de schema/tool-call robusto;
- `dangerouslySetInnerHTML` exige sanitização adequada em produção;
- CORS aberto;
- IDs por `length + 1`;
- file storage síncrono;
- modelo `gpt-4-vision-preview` está obsoleto;
- ausência de auth/multi-user boundary;
- action handling sem policy generalizada.

Nenhum desses padrões técnicos foi absorvido.

### Decisão

B/C/D — ABSORB_METHOD_ONLY.

`deep-grill` recebeu modo **draft-first**:
- produzir uma versão provisória antes de pedir contexto;
- perguntar poucas coisas de alto valor informacional por rodada;
- manter respostas como contexto estruturado;
- explicitar pendências;
- não usar draft-first quando um gate irreversível/regulatório precisa vir antes.

## Segurança e portabilidade

Verdict geral: CAUTION.

Nenhum installer, container, scanner, Temporal server, Backstage instance, build tool ou aplicação externa foi executado.

Superfícies:
- Docker/container runtimes;
- CI credentials;
- cluster credentials;
- package registries;
- supply-chain scanners;
- developer portals;
- telemetry potentially containing secrets/PII;
- durable workflow external actions;
- AI API keys;
- Socket.IO/browser surfaces.

Adaptação:
- methodology only;
- no tool assumed installed;
- approval gates remain in external writes;
- telemetry redaction;
- supply-chain findings require validation;
- AI action protocols use structured/tool contracts when runtime supports them, not text delimiters.

## Materialização

Criados:
- `skills/software-testing-engineering/SKILL.md`
- `skills/software-observability-engineering/SKILL.md`
- `skills/durable-workflow-engineering/SKILL.md`
- `skills/developer-platform-engineering/SKILL.md`
- `skills/software-supply-chain-engineering/SKILL.md`
- `skills/build-system-engineering/SKILL.md`
- `stacks/software-engineering-cycle/STACK.md`

Atualizados:
- `skills/production-go-live/SKILL.md`
- `skills/deep-grill/SKILL.md`
- `ARSENAL INDEX.md`

## Limites

- avaliação aprofundou READMEs/documentos centrais e código representativo; não auditou cada repo arquivo a arquivo;
- large runtime projects foram usados como fontes arquiteturais, não como dependências;
- google/eng-practices foi descartado do lote final por estar arquivado e por overlap com code-review;
- ferramentas de scanners/build/CI mudam e exigem version grounding quando usadas concretamente.
