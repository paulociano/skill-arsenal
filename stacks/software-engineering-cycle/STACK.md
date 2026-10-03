---
name: software-engineering-cycle
description: "Conduzir trabalho de engenharia de software da arquitetura ao build, testes, observabilidade, supply chain, workflows duráveis, plataforma e produção, carregando apenas os owners necessários."
---

# Software Engineering Cycle

## Objetivo

Orquestrar decisões recorrentes de engenharia de software sem transformar cada projeto em uma coleção de ferramentas.

## Router

System design:
- `system-design-engineering`

Codebase/module design:
- `codebase-design`

Testing:
- `tdd`
- `software-testing-engineering`

Debugging:
- `diagnosing-bugs`

Observability:
- `software-observability-engineering`

Durable workflows:
- `durable-workflow-engineering`

Build systems/monorepos:
- `build-system-engineering`

Supply chain/security:
- `software-supply-chain-engineering`
- `secure-code-privacy-review`

Developer platform:
- `developer-platform-engineering`

Architecture decisions/domain:
- `domain-modeling`

Production delivery:
- `production-go-live`

Behavior verification:
- `behavior-contract-validation`

## Fluxo

1. **Scope**
   - behavior;
   - users;
   - constraints;
   - SLOs;
   - risk;
   - deployment/runtime.

2. **Design**
   - architecture only as complex as current requirements justify;
   - identify seams, state, dependencies and failure modes.

3. **Build graph**
   - explicit dependencies;
   - reproducible inputs;
   - package/runtime versions grounded.

4. **Implement in slices**
   - public behavior first;
   - TDD where useful;
   - keep modules deep and interfaces small.

5. **Test by risk**
   - examples;
   - properties;
   - integration;
   - contracts;
   - E2E only for critical journeys.

6. **Instrument**
   - metrics/traces/logs;
   - correlation;
   - SLO signals;
   - telemetry privacy.

7. **Secure supply chain**
   - dependency inventory;
   - scanning;
   - update policy;
   - artifact provenance.

8. **Durability when needed**
   - retries;
   - idempotency;
   - replay;
   - timers;
   - compensation;
   - human approval.

9. **Platform/golden path**
   - only when repeated team toil justifies a reusable internal platform.

10. **Release**
   - immutable artifacts;
   - reproducible pipeline;
   - approval;
   - deploy/reconcile;
   - runtime verification;
   - rollback limits.

11. **Operate and learn**
   - production signals;
   - incidents;
   - drift;
   - codify verified golden paths.

## Selection rule

Não carregar todas as skills.

Exemplos:
- biblioteca simples: `codebase-design` + `tdd`;
- serviço web: adicionar `system-design-engineering`, `software-testing-engineering`, `software-observability-engineering`;
- workflow longo: adicionar `durable-workflow-engineering`;
- monorepo pesado: adicionar `build-system-engineering`;
- organização com muitos times: `developer-platform-engineering`;
- release real: `production-go-live`.

## Regras

- framework/tool não define arquitetura;
- scanner não substitui review;
- observabilidade não deve começar por “coletar tudo”;
- retry sem idempotência pode amplificar incidente;
- cache/build optimization precisa de measurement;
- golden path só vira padrão depois de provar valor;
- production claim exige runtime verification.

## Provenance

Stack construída do lote 2026-10-03 de 16 repositórios de software engineering, com maior peso em Hypothesis, Testcontainers, OpenTelemetry Collector, Temporal, Backstage, Trivy, Renovate, Semgrep, Bazel/Pants, Dagger e Argo CD. Charlytoc/ai-todo-app contribuiu para o padrão draft-first, absorvido em `deep-grill`.
