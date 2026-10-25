---
name: durable-workflow-engineering
description: "Projetar workflows duráveis distribuídos com state persistente, replay, retries, idempotency, timers, compensation e recovery após crash, distinguindo orquestração lógica de execução efêmera."
---

# Durable Workflow Engineering

## Objetivo

Projetar processos de longa duração que sobrevivam a crash, restart, timeouts e falhas parciais sem perder o estado lógico nem repetir efeitos indevidamente.

## Quando usar

- durable execution;
- long-running workflows;
- orchestration;
- retries;
- sagas/compensation;
- delayed/timed workflows;
- human approvals;
- multi-step external operations.

## Princípio central

**Process state must survive process lifetime.**

## Modelo

Separar:
- workflow/orchestration logic;
- activities/effects;
- durable history/state;
- workers/executors;
- timers/signals;
- external systems.

## Workflow de design

1. **State machine**
   - estados;
   - transitions;
   - terminal states;
   - external signals.

2. **Durability**
   - state/history persistido;
   - restart/replay;
   - deterministic orchestration quando runtime exigir.

3. **Activities**
   - efeitos externos fora da lógica replayable;
   - timeout;
   - retry policy;
   - idempotency key;
   - side-effect verification.

4. **Retries**
   - transient vs permanent;
   - exponential backoff;
   - max attempts/time budget;
   - consultar estado antes de repetir write ambíguo.

5. **Compensation**
   - undo lógico quando rollback real não existe;
   - compensation order;
   - compensation itself can fail and needs policy.

6. **Timers**
   - durable timers;
   - deadlines;
   - escalation;
   - clock semantics explicit.

7. **Human-in-loop**
   - pending approval state;
   - signal/resume;
   - expiry;
   - approver identity/audit.

8. **Versioning**
   - running workflows may outlive deploys;
   - compatibility/migration strategy;
   - do not silently reinterpret historical state.

9. **Observability**
   - workflow ID;
   - current state;
   - attempts;
   - pending activities;
   - timer/deadline;
   - failure reason.

10. **Testing**
    - replay/restart;
    - activity timeout;
    - duplicate signal;
    - crash between effect and acknowledgement;
    - compensation failure;
    - version transition.
## Conservação de trabalho e fencing de efeitos

- trabalho aceito precisa existir em estado durável antes de depender da vida de um processo;
- acknowledgement de recebimento não equivale a conclusão;
- registrar attempt/intenção antes de efeito externo quando recovery depender disso;
- se um worker morrer durante operação mutável, tratar o estado como ambíguo/interrompido, não como retry automaticamente seguro;
- consultar estado externo ou usar idempotency/fencing antes de repetir writes;
- usar generation/lease/fencing token para impedir worker antigo de sobrescrever estado mais novo;
- separar accepted → attempt → external effect → acknowledgement → terminal outcome;
- model checking complementa, mas não substitui boundary tests reais.


## Regras

- retry is not automatically safe;
- workflow history is not ordinary application log;
- orchestration and side effects need different determinism rules;
- crash after external success before local ack is a first-class scenario;
- compensation is not guaranteed rollback.

## Integração

`graph-engineering`, `agent-action-governance`, `system-design-engineering`, `software-observability-engineering`, `software-testing-engineering`.

## Provenance

Consolidada de Temporal durable execution architecture e padrões de workflow orchestration. Não exige Temporal server, SDK ou CLI.


## Atores duráveis como padrão de coordenação

Quando o problema envolve **estado por entidade/identidade** (sala, conversa, documento colaborativo, agente), considerar um ator durável como alternativa à orquestração por workflow. Identificar chave/owner por ator, limites de serialização de chamadas e `await`, acesso concorrente, interleaving intencional, campos persistidos, recuperação após interrupção, isolamento de tenants, schema migration, streaming/WebSocket, backpressure e observabilidade. Serialização por ator não implica transação entre atores nem exactly-once de efeitos externos; preservar idempotência, fencing e segurança de retry nas integrações. Comparar escalabilidade por hot key, armazenamento, latência de cold-start, distribuição e portability. Não presumir runtime/SDK Terse instalado ou garantias que não foram testadas. Referência: https://github.com/TerseAI/durable-actors.


## Agentes gerenciados com event log e workers intercambiáveis (Omnara, 2026-10-24)

Para plataformas que executam agentes em máquinas locais/remotas, separar contrato do agente (modelo, tools, política, fontes de máquina e memória), API/control plane, event log durável, workers stateless, executores/máquinas e superfície de acompanhamento humano. Cada turno, chamada de ferramenta, resultado, aprovação e erro deve ter identidade e transição auditável; o log só sustenta recuperação se a persistência for confirmada antes do ack.

Planejar reconexão de máquina, transferência entre executores, deduplicação de turnos, leases e fencing de writes, limites de concorrência, fila, budgets e recuperação em versões novas. Separar aprovação humana pendente da execução automática e herdar as políticas de `agent-action-governance`; acesso a shell, credenciais e rede deve ser minimizado, isolado e vinculado ao ator autorizado.

Conectores MCP, provedores de modelo, dashboard, agendamentos e daemon são integrações a implementar/testar explicitamente, não capacidades implícitas do ChatGPT. Sem infraestrutura real não prometer persistência, execução background, workers ou sandboxes autônomos.

**Should trigger:** 'Desenhe uma plataforma de agentes com aprovação, replay e execução em várias máquinas'. **Near miss:** 'Faça uma consulta pontual em um repositório'.

**Origem:** https://github.com/omnara-ai/omnara. Arquitetura conceitual absorvida; nenhum deploy, chave, máquina ou processo externo instalado.
