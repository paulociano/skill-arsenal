---
name: resilience-engineering
description: "Projetar e validar resiliência por steady state, failure hypotheses, fault injection controlada, blast radius, observação, recovery e aprendizagem, sem transformar chaos engineering em falha aleatória ou teste destrutivo."
---

# Resilience Engineering

## Objetivo

Provar como um produto ou serviço se comporta quando dependências, rede, infraestrutura ou recursos degradam, usando falhas controladas e invariantes observáveis.

## Quando usar

- testar timeout, latency, connection reset ou dependency outage;
- validar retry/circuit breaker/fallback;
- chaos engineering;
- fault injection;
- graceful degradation;
- recovery testing;
- validar RTO/RPO operacional quando aplicável;
- testar comportamento sob DNS, clock, I/O, network ou resource faults.

Para apenas listar failure modes use `system-design-engineering`. Esta skill é usada quando o comportamento sob falha precisa ser testado ou operacionalizado.

## Princípio central

**Falha controlada só é útil quando existe um steady state/invariant explícito e um limite de blast radius.**

## Workflow

1. **Select critical behavior**
   - jornada;
   - service dependency;
   - invariant;
   - user-visible expectation;
   - data safety requirement.

2. **Define steady state**
   Exemplo:
   - request success above agreed floor;
   - queue drains within bound;
   - read path continues in degraded mode;
   - no duplicate charge;
   - no data loss;
   - recovery completes within target.

3. **Failure hypothesis**
   Formato:
   - Given steady state X,
   - when fault Y occurs,
   - system should preserve/degrade to Z,
   - and recover by condition R.

4. **Choose smallest credible fault**
   Exemplos:
   - latency;
   - timeout;
   - connection drop;
   - bandwidth reduction;
   - dependency unavailable;
   - malformed/partial response;
   - DNS failure;
   - process/pod loss;
   - clock skew;
   - I/O fault;
   - CPU/memory pressure.

   Começar na camada mais estreita que prova a hipótese.

5. **Safety / blast radius**
   - environment;
   - population;
   - duration;
   - resource scope;
   - data protection;
   - abort signal;
   - human owner;
   - cleanup/recovery path.

   Produção exige autorização e controles substancialmente mais fortes.

6. **Observability readiness**
   Antes de injetar:
   - telemetry necessária existe;
   - baseline foi observado;
   - signal delay conhecido;
   - recovery pode ser confirmado.

7. **Inject**
   - aplicar uma falha por vez quando possível;
   - registrar início, configuração e target;
   - não ampliar falha porque o resultado parece "interessante".

8. **Observe**
   Separar:
   - user impact;
   - system response;
   - retries/backpressure;
   - saturation;
   - error propagation;
   - failover/fallback;
   - data integrity;
   - telemetry behavior.

9. **Abort when needed**
   Parar quando:
   - safety threshold rompe;
   - escopo observado diverge;
   - telemetry some;
   - recovery path não está disponível;
   - impacto ultrapassa autorização.

10. **Recover**
    - remover fault;
    - confirmar dependência;
    - verificar steady state;
    - reconciliar filas/state;
    - confirmar ausência de efeito persistente inesperado.

11. **Classify**
    - resilient as expected;
    - graceful degradation;
    - unsafe failure;
    - recovery failure;
    - observation insufficient.

12. **Turn discovery into regression**
    Quando uma falha revelar bug:
    - criar teste reproduzível menor quando possível;
    - corrigir design/implementation;
    - retestar;
    - atualizar runbook/limits.

## Network/service virtualization

Para dependências externas:
- usar proxy/mock/fault layer quando disponível;
- preferir falhas determinísticas e bounded;
- testar status, latency, disconnect, malformed responses e rate limits;
- service virtualization deve modelar contratos relevantes, não uma fantasia conveniente da dependência.

## Retry safety

Sempre verificar:
- idempotency;
- retry storms;
- exponential backoff/jitter quando necessário;
- timeout budget;
- duplicate side effects;
- downstream saturation.

## Guardrails

- chaos não significa aleatoriedade sem hipótese;
- não começar em produção se ambiente menor consegue responder;
- não injetar falha destrutiva sem autorização;
- não testar credenciais/dados reais desnecessariamente;
- não misturar múltiplos faults antes de entender o básico;
- ausência de incidente não prova resiliência se o steady state não foi observado;
- recovery é parte do teste, não cleanup administrativo.

## Entregável

- steady state;
- failure hypothesis;
- fault scope;
- blast radius;
- observations;
- invariant result;
- recovery result;
- finding;
- remediation/retest.

## Integração

Combina com:
- `system-design-engineering`;
- `software-testing-engineering`;
- `software-observability-engineering`;
- `durable-workflow-engineering`;
- `production-go-live`;
- `diagnosing-bugs`.

## Provenance

Adaptada de:
- https://github.com/Shopify/toxiproxy
- https://github.com/chaos-mesh/chaos-mesh
- https://github.com/litmuschaos/litmus
- https://github.com/mock-server/mockserver-monorepo

Preserva fault injection, network degradation, steady-state checks, experiment orchestration e recovery. CLIs, clusters e runtimes dessas ferramentas são opcionais, não requisitos.
