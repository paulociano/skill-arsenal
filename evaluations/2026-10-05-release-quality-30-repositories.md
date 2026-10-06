# Avaliação — 30 repositórios de release, QA e engenharia de qualidade

Data: 2026-10-05

## Objetivo

Avaliar 30 repositórios relevantes para lançamento de produtos digitais, sites, web apps, APIs, testes, qualidade, performance, acessibilidade, resiliência e release engineering, comparando-os com o Arsenal canônico.

## Resultado executivo

Criados:
- `release-engineering`;
- `progressive-delivery-verification`;
- `resilience-engineering`.

Atualizados:
- `software-testing-engineering`;
- `web-quality-audit`;
- `runtime-ui-verification`;
- `production-go-live`;
- `software-engineering-cycle`;
- `web-app-engineering-audit`;
- `ARSENAL INDEX.md`.

## Triage dos 30

| Fonte | Classe | Decisão |
|---|---|---|
| storybookjs/storybook | A/B/D | UPDATE_EXISTING |
| jestjs/jest | B/D | KEEP_EXISTING_OWNER |
| SeleniumHQ/selenium | A/D | KEEP_EXISTING_OWNER |
| grafana/k6 | A/D | ABSORB_METHOD_ONLY |
| locustio/locust | A/D | KEEP_EXTERNAL_REFERENCE |
| semantic-release/semantic-release | A/B/D | CREATE_NEW |
| zaproxy/zaproxy | A/D | KEEP_EXISTING_OWNER |
| changesets/changesets | A/B/D | CREATE_NEW |
| Shopify/toxiproxy | A/D | CREATE_NEW / ABSORB_METHOD_ONLY |
| webdriverio/webdriverio | A/D | KEEP_EXISTING_OWNER |
| spinnaker/spinnaker | A/D | KEEP_EXTERNAL_REFERENCE |
| apache/jmeter | A/D | KEEP_EXTERNAL_REFERENCE |
| artilleryio/artillery | A/D | ABSORB_METHOD_ONLY |
| tektoncd/pipeline | D | KEEP_EXISTING_OWNER |
| karatelabs/karate | A/D | UPDATE_EXISTING |
| GoogleChrome/web-vitals | A/B/D | UPDATE_EXISTING |
| chaos-mesh/chaos-mesh | A/D | CREATE_NEW |
| dequelabs/axe-core | A/B/D | UPDATE_EXISTING |
| googleapis/release-please | A/B/D | CREATE_NEW |
| wiremock/wiremock | A/D | UPDATE_EXISTING |
| garris/BackstopJS | B/D | UPDATE_EXISTING |
| fluxcd/flagger | A/D | CREATE_NEW |
| sitespeedio/sitespeed.io | A/D | UPDATE_EXISTING |
| mock-server/mockserver-monorepo | A/D | UPDATE_EXISTING |
| pa11y/pa11y | B/D | KEEP_EXISTING_OWNER |
| schemathesis/schemathesis | A/D | UPDATE_EXISTING |
| argoproj/argo-rollouts | A/D | CREATE_NEW |
| catchpoint/WebPageTest | A/D | KEEP_EXTERNAL_REFERENCE |
| pact-foundation/pact-js | A/D | UPDATE_EXISTING |
| open-feature/spec | A/B | CREATE_NEW / ABSORB_METHOD_ONLY |

## 1. Release engineering

Fontes principais:
- semantic-release/semantic-release;
- changesets/changesets;
- googleapis/release-please.

Valor incremental:
- classificar mudança por impacto no consumidor;
- separar release de deploy;
- declarar release impact perto da contribuição;
- manter release PR/candidate;
- versionar/changelogar unidades de release;
- rastrear artifact identity e publicação;
- tratar breaking/deprecation/migration como contrato do consumidor.

Decisão: criar `release-engineering`.

Near miss:
- publicar infraestrutura/aplicação em ambiente → `production-go-live`.

## 2. Progressive delivery verification

Fontes principais:
- argoproj/argo-rollouts;
- fluxcd/flagger;
- open-feature/spec.

Valor incremental:
- canary/blue-green/rings/cohorts;
- blast radius;
- analysis contract;
- baseline vs canary;
- technical and business KPIs;
- acceptance/load checks durante rollout;
- promotion, pause, abort e recovery;
- feature flags como mecanismo de exposure, não prova de sucesso.

Decisão: criar `progressive-delivery-verification`.

Near miss:
- A/B test causal de produto → `experiment-design`.

## 3. Resilience engineering

Fontes principais:
- Shopify/toxiproxy;
- chaos-mesh/chaos-mesh;
- litmuschaos/litmus;
- mock-server/mockserver-monorepo.

Valor incremental:
- steady state explícito;
- failure hypothesis;
- smallest credible fault;
- bounded blast radius;
- observability readiness;
- controlled fault injection;
- graceful degradation;
- recovery verification;
- descoberta vira regressão.

Decisão: criar `resilience-engineering`.

Near miss:
- listar failure modes sem executar/provar comportamento → `system-design-engineering`.

## 4. Software testing engineering

Fontes:
- schemathesis/schemathesis;
- pact-foundation/pact-js;
- wiremock/wiremock;
- mock-server/mockserver-monorepo;
- karatelabs/karate.

Capabilities absorvidas:
- schema-derived API cases;
- valid/invalid generation;
- stateful API workflows;
- reproducible/minimized generated failures;
- consumer/provider contracts;
- service virtualization;
- controlled latency/timeout/disconnect/rate-limit/malformed responses.

Decisão: UPDATE_EXISTING em `software-testing-engineering`, sem criar owner genérico de API testing.

## 5. Web quality

Fontes:
- dequelabs/axe-core;
- GoogleChrome/web-vitals;
- sitespeedio/sitespeed.io;
- catchpoint/WebPageTest;
- pa11y/pa11y.

Capabilities absorvidas:
- automated accessibility é cobertura parcial;
- resultados inconclusivos exigem manual review;
- performance budgets definidos antes da mudança;
- múltiplas execuções quando ruído é material;
- separar lab, field e synthetic;
- CI regression e production trend são sinais diferentes.

Decisão: UPDATE_EXISTING em `web-quality-audit`.

## 6. Runtime UI / visual regression

Fontes:
- storybookjs/storybook;
- garris/BackstopJS;
- reg-viz/reg-suit como referência secundária.

Capabilities absorvidas:
- coverage de estados de componente;
- loading/empty/error/disabled/overflow/viewport/permission;
- visual baseline reproduzível;
- reference → candidate → diff → review → approval;
- baseline só muda quando a mudança é intencional e aprovada.

Decisão: UPDATE_EXISTING em `runtime-ui-verification`.

## 7. Performance/load tools

Fontes:
- grafana/k6;
- artilleryio/artillery;
- locustio/locust;
- apache/jmeter.

Conclusão:
- metodologia de workload, latency, throughput e saturation é valiosa;
- parte do conteúdo entra em quality/resilience/testing;
- nesta rodada não foi demonstrada necessidade de um owner `performance-engineering` separado sem sobrepor web quality, observability e system design.

Decisão: ABSORB_METHOD_ONLY / KEEP_EXTERNAL_REFERENCE.

## 8. Security

Fonte principal:
- zaproxy/zaproxy.

O Arsenal já possui `web-application-security-audit` baseado em ASVS/WSTG.

Decisão: KEEP_EXISTING_OWNER. ZAP permanece ferramenta opcional, não autoridade.

## 9. CI/CD e pipelines

Fontes:
- tektoncd/pipeline;
- spinnaker/spinnaker.

O Arsenal já possui `production-go-live`, `build-system-engineering`, GitOps provenance e agora progressive delivery.

Decisão: KEEP_EXISTING_OWNER / external reference.

## Segurança e portabilidade

Não foram executados:
- installers;
- scanners;
- load generators;
- fault injectors;
- cluster controllers;
- package publishers;
- release bots;
- proxies.

As skills preservam metodologia e guardrails, removendo dependência de Kubernetes, Node.js, browsers específicos ou SaaS vendors.

## Prova de valor incremental

### release-engineering
Should trigger:
- “estruture versionamento, changelog e publicação de releases para este monorepo”.

### progressive-delivery-verification
Should trigger:
- “faça um plano de canary com 5%, 20%, 50% e promotion gates”.

### resilience-engineering
Should trigger:
- “prove que o checkout degrada corretamente se Redis ficar lento ou indisponível”.

## Limites

- estrelas/popularidade foram sinais de descoberta, não critério de adoção;
- ferramentas de performance e chaos podem produzir efeitos materiais e exigem ambiente/escopo autorizado;
- automated accessibility não prova conformidade total;
- visual diff não decide sozinho se uma mudança é correta;
- canary metrics precisam de volume e janela suficientes;
- rollback pode ser limitado por migrations e efeitos externos.
