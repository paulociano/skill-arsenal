---
name: progressive-delivery-verification
description: "Planejar e verificar exposição progressiva de releases com canary, blue/green, cohorts, feature flags, métricas, acceptance tests, promotion/abort gates e blast radius controlado sem confundir deploy com sucesso."
---

# Progressive Delivery Verification

## Objetivo

Reduzir risco de release expondo uma mudança de forma gradual e verificável, usando sinais técnicos e de negócio para decidir promover, pausar ou abortar.

## Quando usar

- canary release;
- blue/green com verificação;
- rollout gradual;
- feature flag rollout;
- lançamento de mudança crítica para subconjunto de usuários;
- release com blast radius controlado;
- promoção automática ou assistida baseada em métricas;
- validação pós-deploy antes de 100% de exposição.

Para provisionar/publicar infraestrutura use `production-go-live`. Para desenhar experimento de produto use `experiment-design`.

## Princípio central

**Deploy é mudança de estado técnico; release bem-sucedida exige exposição observada e critérios explícitos de promoção.**

## Workflow

1. **Define release unit**
   - artifact/version;
   - config;
   - migrations;
   - feature flags;
   - dependencies;
   - rollback/recovery boundary.

2. **Define population**
   - baseline/stable;
   - canary cohort;
   - geography/tenant/device/user segment;
   - exclusion criteria;
   - exposure mechanism.

3. **Choose strategy**
   Conforme contexto:
   - canary traffic shifting;
   - blue/green;
   - ring deployment;
   - feature-flag cohort;
   - shadow/mirroring;
   - manual staged rollout.

4. **Blast radius**
   - starting exposure;
   - step size;
   - pause/observation window;
   - max canary exposure before promotion;
   - irreversible side effects;
   - data compatibility.

   Não usar percentual padrão sem considerar volume e risco.

5. **Pre-promotion checks**
   - artifact identity;
   - health/readiness;
   - schema compatibility;
   - smoke/conformance tests;
   - critical journeys;
   - observability availability.

6. **Analysis contract**
   Definir antes da leitura:
   - metric;
   - population;
   - window;
   - baseline/comparator;
   - success condition;
   - failure condition;
   - inconclusive condition;
   - missing-data behavior.

   Métricas possíveis:
   - request success;
   - latency;
   - saturation;
   - error classes;
   - domain conversion/success;
   - business guardrails;
   - support/incident signal.

7. **Progressive exposure**
   Para cada step:
   - apply exposure;
   - wait for minimum evidence window;
   - run acceptance/smoke/load checks when justified;
   - evaluate metrics;
   - classify `promote`, `pause`, `abort` ou `inconclusive`.

8. **Baseline comparison**
   Quando comparação direta ajudar:
   - stable e canary devem ter populações comparáveis;
   - evitar concluir causalidade de cohorts enviesados;
   - quando rollout também for experimento, usar `experiment-design`.

9. **Promotion**
   Promover somente quando:
   - blockers passaram;
   - failures estão dentro de policy;
   - evidence window é suficiente;
   - dados ausentes não foram tratados como sucesso.

10. **Abort / rollback**
    - stop new exposure;
    - route back to stable quando suportado;
    - disable flag quando esse for o mecanismo;
    - considerar migrations e side effects;
    - verificar recovery no runtime.

    Rollback não é universalmente seguro.

11. **Post-promotion watch**
    - ampliar observação após 100%;
    - detectar delayed failures;
    - confirmar que telemetry e support signals estabilizaram;
    - registrar release outcome.

12. **Learn**
    Registrar:
    - qual gate detectou ou perdeu o problema;
    - false positives/negatives;
    - thresholds úteis;
    - mudança necessária no próximo rollout.

## Guardrails

- não promover porque "não houve alerta";
- missing telemetry = `inconclusive`, não pass;
- readiness probe não substitui acceptance/business verification;
- thresholds precisam ser adequados ao tráfego e à janela;
- automação pode abortar/prometer apenas dentro de limites autorizados;
- mudanças de dados incompatíveis podem tornar rollback inviável;
- feature flag não apaga efeitos já persistidos;
- business KPI lento não serve como único gate para incidentes rápidos;
- não transformar canary em A/B test causal sem desenho experimental apropriado.

## Entregável

- release unit;
- rollout strategy;
- exposure steps;
- metric/acceptance contract;
- promotion/abort rules;
- rollback limits;
- observed evidence;
- final disposition;
- follow-up.

## Integração

Combina com:
- `production-go-live`;
- `release-engineering`;
- `software-observability-engineering`;
- `behavior-contract-validation`;
- `software-testing-engineering`;
- `experiment-design`;
- `verify-before-claim`.

## Provenance

Adaptada principalmente de:
- https://github.com/argoproj/argo-rollouts
- https://github.com/fluxcd/flagger
- https://github.com/open-feature/spec

Preserva progressive traffic exposure, analysis runs, acceptance/load checks, promotion/abort e feature-flag boundaries, sem exigir Kubernetes, service mesh ou fornecedor específico.
