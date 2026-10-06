---
name: software-factory-operations
description: "Operar uma software factory com agentes usando fila durável, charter de autonomia, triage, spec gates, implementação limitada, verificação independente, back-pressure de revisão e merge humano."
---

# Software Factory Operations

## Objetivo

Transformar entrega de software assistida por agentes em um loop operacional repetível, reiniciável e auditável, sem automatizar julgamento humano de alto impacto.

## Quando usar

- triage automatizado de issues;
- implementação agentic em fila;
- software factory;
- sessões independentes que precisam continuar o mesmo trabalho;
- review queue com back-pressure;
- implementação + verifier separado;
- automação recorrente de manutenção de código.

## Princípio central

**Autonomia deve acompanhar consequência, não dificuldade.**

Uma mudança longa e mecânica pode ser segura para automação; uma mudança pequena em auth, billing ou dados pode exigir gates humanos.

## Modelo

Separar:
- **Charter**: escopo permitido, risco, protected paths, stop conditions;
- **Queue**: trabalho durável e visível;
- **Handoff**: contrato entre runs;
- **Worker**: executor efêmero;
- **Gates**: checks determinísticos;
- **Verifier**: revisão independente;
- **Human review**: decisão final;
- **Monitor**: feedback do sistema em produção.

## Workflow

1. **Charter**
   - tipos de trabalho permitidos;
   - paths/sistemas protegidos;
   - tier de autonomia;
   - checks obrigatórios;
   - limite máximo de itens aguardando revisão;
   - condições de parada.

2. **Triage**
   - classificar issue em:
     - ready-to-implement;
     - ready-to-spec;
     - needs-info;
     - blocked;
   - registrar por que;
   - não converter ambiguidade de produto em código especulativo;
   - tarefas de triage podem usar um modelo mais barato ou regra determinística quando o objetivo é apenas filtrar/rotear, preservando o modelo mais capaz para decisões que exigem julgamento real.

3. **Claim e freshness**
   - uma unidade de trabalho por run;
   - claim determinístico e atômico;
   - primeiro claim válido vence;
   - colisão deve falhar fechada, não criar dois writers;
   - antes de publicar resposta ou ação derivada de contexto compartilhado, verificar se surgiram mensagens, commits ou decisões mais novas;
   - resposta baseada em cursor/estado stale deve ser retida e reavaliada contra o contexto novo, não publicada por inércia.

4. **Spec gate**
   Quando intenção ou design não forem triviais:
   - produto;
   - comportamento observável;
   - desenho técnico;
   - slice de implementação;
   - aprovação humana antes de avançar quando o risco justificar.

5. **Implement**
   - branch/worktree isolado;
   - escopo mínimo;
   - teste que reproduz a falha/contrato quando aplicável;
   - mudança;
   - checks definidos no charter.

6. **Deterministic gates**
   - typecheck;
   - lint;
   - tests;
   - build;
   - security/audit;
   - architecture checks quando definidos.

   Gate ausente que deveria existir é MISCONFIGURED, não PASS.

7. **Independent verifier**
   - lê diff e spec friamente;
   - ignora a narrativa do writer;
   - tenta refutar o claim;
   - quando possível, remover/reverter a fix e confirmar que o teste falha;
   - uncertainty suficiente deve bloquear promoção.

8. **Draft PR**
   - somente após gates e verifier;
   - inclui evidência;
   - não faz merge automático.

9. **Back-pressure**
   - review queue possui limite numérico;
   - quando cheio, parar de produzir novos itens;
   - o gargalo real é julgamento humano pendente, não número de agentes disponíveis.

10. **Human decision**
    - review;
    - request changes;
    - close;
    - merge.

11. **Monitor**
    - observar branch principal, regressões e factory health;
    - novos findings voltam para a fila como issues;
    - não reabrir automaticamente trabalho resolvido sem nova evidência.

## Durable state

A factory não depende de memória da sessão.

Preferir estado durável em:
- issues/labels;
- PRs;
- committed policy;
- handoff records;
- test artifacts;
- run receipts.

Sessões devem poder começar frescas e continuar a partir desse estado.

## Guardrails

- writer não aprova o próprio trabalho;
- agents não alteram silenciosamente o charter;
- merge permanece humano;
- hooks são guardrail, não boundary final;
- branch protection/ruleset é enforcement mais forte quando disponível;
- scheduled automation deve respeitar as mesmas policies de ações interativas;
- green infrastructure run não equivale a task success;
- queue cheia deve interromper produção, não esconder review debt.

## Integração

`software-engineering-cycle`, `agent-action-governance`, `multi-agent-orchestration`, `software-testing-engineering`, `code-review`, `behavior-contract-validation`, `production-go-live`.

## Provenance

Adaptada de addyosmani/factory e enriquecida por padrões de coordenação observados em yetone/cumora. Preserva charter humano, queue durável, autonomy-by-consequence, fail-closed gates, verifier independente, review back-pressure e merge humano. De Cumora foram absorvidos freshness gate antes de responder/agir, claims atômicos sobre unidades reais de trabalho e triage econômico; o runtime, chat, Kubernetes e infraestrutura específicos não são requisitos. Remove dependência de Claude routines, hooks e instaladores específicos; GitHub é uma implementação possível, não requisito conceitual.
