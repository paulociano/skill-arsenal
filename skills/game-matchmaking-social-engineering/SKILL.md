---
name: game-matchmaking-social-engineering
description: "Projetar matchmaking e sistemas sociais de jogos com tickets, pools, match functions, latency/skill/party constraints, backfill, server allocation, parties/lobbies e métricas de qualidade versus tempo de espera."
---

# Game Matchmaking & Social Engineering

## Objetivo

Formar partidas e grupos equilibrando qualidade, tempo de espera, latência, party integrity e capacidade de servidor, sem confundir matchmaking com simples fila FIFO.

## Quando usar

- matchmaking;
- ranked/unranked queues;
- parties;
- lobbies;
- server allocation;
- backfill;
- region selection;
- social grouping;
- match quality metrics.

## Princípio central

**Matchmaking otimiza um trade-off explícito entre qualidade e espera.**

## Workflow

1. **Ticket**
   - player/party id;
   - queue/mode;
   - region/latency;
   - skill/rating when applicable;
   - party size;
   - platform/input pool;
   - eligibility constraints.

2. **Pool**
   - separar candidatos compatíveis;
   - hard constraints primeiro;
   - soft preferences depois;
   - evitar fragmentação excessiva de filas.

3. **Match function**
   - team size;
   - skill spread;
   - latency;
   - party cohesion;
   - role requirements;
   - platform/crossplay policy;
   - widening rules por wait time.

4. **Evaluation**
   - proposta não vira assignment sem validation;
   - verificar capacity e duplicate assignment;
   - race conditions e retries idempotentes.

5. **Server allocation**
   - escolher region/build/version;
   - reservar capacidade;
   - retornar connection details apenas após allocation válida;
   - failure precisa requeue/recover sem perder ticket indevidamente.

6. **Backfill**
   - identificar vacancy;
   - preservar constraints relevantes;
   - evitar inserir player em partida próxima do fim quando policy proibir.

7. **Party/lobby**
   - leader/ownership;
   - join/leave;
   - privacy/invite;
   - ready state;
   - party skill/rating policy explícita;
   - disconnect/reconnect.

8. **Metrics**
   - queue time p50/p95;
   - match quality distribution;
   - latency distribution;
   - cancellation/abandon;
   - failed allocation;
   - backfill rate;
   - rematch/requeue.

9. **Testing**
   - empty/low-pop queue;
   - parties grandes;
   - region scarcity;
   - version mismatch;
   - server allocation failure;
   - duplicate/retry;
   - queue surge.

## Ranked guardrails

- rating update é sistema separado do matchmaker;
- smurf/abuse detection não deve ser inferida apenas de rating;
- widening deve ser observável e versionado;
- mudanças de algoritmo precisam de experiment/guardrails antes de rollout amplo.

## Regras

- menor queue time não é automaticamente melhor;
- maior skill similarity não é automaticamente melhor se latency explodir;
- party não deve ser quebrada silenciosamente;
- matchmaker não deve conhecer detalhes internos do game server além do contract necessário.

## Integração

`game-networking-engineering`, `live-game-operations-engineering`, `system-design-engineering`, `experiment-design`, `product-metrics-diagnostics` e `game-testing-quality-engineering`.

## Provenance

Consolidada de Google Open Match para tickets/pools/match functions/evaluation e Agones como referência de game-server allocation/orchestration. Não exige Kubernetes, Open Match ou Agones.
