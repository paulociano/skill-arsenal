---
name: live-game-operations-engineering
description: "Projetar e operar features de live games como economia, remote config, eventos sazonais, rewards, battle pass, loja, leaderboards e backend state com autoridade, rollout, observabilidade e rollback."
---

# Live Game Operations Engineering

## Objetivo

Separar conteúdo/configuração mutável de regras autoritativas e operar mudanças live com rollout controlado, métricas, rollback e proteção contra abuso.

## Quando usar

- remote config;
- daily rewards;
- battle pass;
- seasonal events;
- virtual shop/economy;
- inventory/currencies;
- leaderboards/tournaments;
- mailbox/gifts;
- server authoritative progression;
- backend state de jogos;
- A/B tests em parâmetros de gameplay.

## Princípio central

**Config remota muda parâmetros; autoridade do servidor protege state e valor.**

## Workflow

1. **Classify feature**
   - cosmetic/config;
   - progression;
   - economy/value-bearing;
   - competitive ranking;
   - scheduled event;
   - experimentation.

2. **Define authority**
   - cliente pode solicitar;
   - servidor valida grants, purchases, cooldowns e progression quando valor/competição importam;
   - nunca confiar em preço, reward, balance ou eligibility enviado pelo cliente.

3. **Model economy**
   - sources;
   - sinks;
   - currencies/items;
   - inventory limits;
   - purchase/grant ledger;
   - idempotency;
   - refund/reversal quando aplicável.

4. **Remote config**
   - schema/version;
   - defaults locais seguros;
   - rollout segmentado;
   - start/end times em timezone definido;
   - fallback se serviço estiver indisponível;
   - config inválida falha para valor seguro.

5. **Scheduled content**
   - clock do servidor;
   - event definition versionada;
   - eligibility;
   - claim state;
   - restart/resume;
   - evitar depender do relógio do device para reward crítico.

6. **Experimentation**
   - hypothesis e primary metric;
   - assignment estável por usuário;
   - não mudar múltiplas variáveis sem rastreabilidade;
   - guardrails;
   - distinguir experiment de rollout operacional.

7. **State mutation**
   - operações idempotentes;
   - correlation/transaction id;
   - atomicidade quando múltiplos saldos/itens mudam;
   - retries não podem duplicar grant/purchase.

8. **Observability**
   - config version;
   - event version;
   - transaction/grant failures;
   - economy sources/sinks;
   - abnormal inflation;
   - claim/purchase conversion;
   - backend latency/errors.

9. **Rollout**
   - dev/test environment;
   - small cohort/canary;
   - monitor;
   - expand;
   - rollback path pré-definido.

10. **Security**
    - secrets/server keys nunca no client;
    - validate purchase receipts server-side;
    - rate limits;
    - abuse detection;
    - least privilege no dashboard/admin tooling.

## LiveOps versus gameplay code

Mover para config remota:
- números/tunables;
- content schedule;
- eligibility rules simples;
- store/catalog presentation quando suportado.

Manter em código/server logic:
- invariants;
- security boundaries;
- complex state transitions;
- anti-cheat;
- transaction semantics.

## Regras

- dashboard configurável não elimina versionamento;
- client-side reward grant não é authority;
- daily reward sem server clock é manipulável;
- retry sem idempotency pode duplicar valor;
- analytics sem event/config version impede explicar mudanças;
- uma promoção de retenção não deve ser tratada como prova causal sem experimento adequado.

## Integração

`game-development-engineering`, `game-networking-engineering`, `product-metrics-diagnostics`, `experiment-design`, `system-design-engineering`, `secure-code-privacy-review` e `production-go-live`.

## Provenance

Consolidada de Unity Gaming Services Use Cases, Heroic Labs Nakama e PlayFab Unity SDK como contraste de backend/live services. Absorve authority, economy, scheduling, storage, remote configuration, rollout e observabilidade sem exigir fornecedor específico.
